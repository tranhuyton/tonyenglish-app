# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 1 Lectures (Algebra & Desmos Mastery):
- m1_1: Desmos 800 Speed Playbook & Linear Equations/Systems
- m1_2: Linear Functions, Slope-Intercept Models & Word Problems
- m1_3: Linear Inequalities, Systems of Inequalities & Feasible Regions
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

DESMOS_BOX_STYLE = 'background:#ecfdf5; border-left:4px solid #059669; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; color:#064e3b;'

def get_m1_lectures():
    lectures = []

    # =========================================================================
    # LECTURE M1.1: Desmos 800 Speed Playbook & Linear Equations/Systems
    # =========================================================================
    m1_1_cards = f'''
  <div id="sec-blueprint" class="sat-card lecture-interactive-card" data-lecture-section="blueprint">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Cấu trúc Digital SAT Math 800 &amp; Bản đồ 4 Content Domains</h2>
    <p>Phần <b>Digital SAT Math</b> gồm <b>2 Modules × 22 câu = 44 câu</b> trong <b>70 phút</b> (35 phút/module, trung bình <b>95 giây/câu</b>). Khoảng 75% là trắc nghiệm (MCQ) và 25% (~5–6 câu/module) là <b>Student-Produced Response (SPR — tự điền số)</b>.</p>
    <table class="sat-table">
      <thead><tr><th>Content Domain</th><th>Tỉ trọng</th><th>Số câu / Đề</th><th>Trọng tâm 780–800</th></tr></thead>
      <tbody>
        <tr><td><b>Algebra</b></td><td>~35%</td><td>13–15 câu</td><td>Hệ phương trình tham số vô nghiệm/vô số nghiệm, hàm bậc nhất, bất phương trình.</td></tr>
        <tr><td><b>Advanced Math</b></td><td>~35%</td><td>13–15 câu</td><td>Parabol (Δ, Vieta, đỉnh), đa thức, hàm mũ tăng trưởng kép, hệ phi tuyến.</td></tr>
        <tr><td><b>Problem-Solving &amp; Data</b></td><td>~15%</td><td>5–7 câu</td><td>Đổi đơn vị bình/lập phương, phần trăm kép, độ lệch chuẩn (SD), Margin of Error.</td></tr>
        <tr><td><b>Geometry &amp; Trigonometry</b></td><td>~15%</td><td>5–7 câu</td><td>Đường tròn (hoàn thành bình phương), tam giác đồng dạng &amp; 30-60-90, sin x = cos(90° − x), tỉ lệ 3D k/k²/k³.</td></tr>
      </tbody>
    </table>
    <div class="sat-rule-box">
      <b>🎯 Chiến lược phân bổ thời gian 800 Math:</b>
      <br>• <b>Module 1 (Routing ≥ 15/22, mục tiêu 22/22):</b> Xử lý sạch 22 câu trong 25 phút đầu, dành 10 phút cuối kiểm tra lại bằng Desmos để khóa tuyệt đối nhánh <b>Hard Module 2</b>.
      <br>• <b>Module 2 Hard:</b> 15 câu đầu xử lý gọn trong 15 phút (mỗi câu ~60s) để dành trọn <b>20 phút cho 7 câu "Boss" cuối (Q16–Q22)</b>.
    </div>
  </div>

  <div id="sec-desmos" class="sat-card lecture-interactive-card" data-lecture-section="desmos">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Desmos 800 Speed Playbook — 4 Vũ khí giải toán trong 10 giây</h2>
    <p>Trên Digital SAT thật (và ngay trong Bluebook Simulator của TonyEnglish), máy tính đồ thị <b>Desmos</b> được phép dùng cho <b>100% câu hỏi</b>. Học viên đạt 790–800 không giải tay mọi thứ — họ biết khi nào gõ Desmos để ăn chắc 100% không sai dấu!</p>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ 4 Chiêu Desmos tối thượng trên SAT:</b>
      <br>1. <b>Giao điểm tức thì (Intersections):</b> Gõ thẳng 2 vế phương trình hoặc 2 phương trình của hệ (ví dụ <code>3x + 2y = 14</code> và <code>5x − y = 6</code>) → click vào chấm xám giao điểm để đọc ngay <code>(x, y)</code>.
      <br>2. <b>Hồi quy tìm hàm siêu tốc (Regression <code>~</code>):</b> Khi đề cho bảng 2–3 điểm, bấm dấu <code>+</code> → <b>Table</b>, nhập tọa độ <code>(x₁, y₁)</code> rồi gõ dòng dưới: <code>y₁ ~ mx₁ + b</code> (hàm bậc nhất) hoặc <code>y₁ ~ ax₁² + bx₁ + c</code> (parabol). Desmos trả về chính xác <code>m, b, a, c</code> trong 3 giây!
      <br>3. <b>Thanh trượt tham số (Sliders):</b> Khi đề chứa hằng số <code>k</code> hoặc <code>a</code> và hỏi khi nào đồ thị tiếp xúc / song song / cắt tại 1 điểm, gõ nguyên phương trình kèm <code>k</code> → bấm <b>Add slider: k</b> → kéo thanh trượt để quan sát trực quan.
      <br>4. <b>Kiểm tra biểu thức tương đương:</b> Với câu hỏi "Which expression is equivalent to...", gõ biểu thức gốc thành <code>f(x) = ...</code> và gõ đáp án thành <code>g(x) = ...</code> → nếu 2 đồ thị <b>trùng khít 100%</b>, đó là đáp án đúng!
    </div>
    <div class="sat-trap-box">
      <b>🚨 Bẫy kinh điển:</b> Đừng gõ phương trình có biến khác <code>x, y</code> (ví dụ <code>p, t, n</code>) vào Desmos mà quên đổi tên — Desmos sẽ hiểu <code>t</code> là thanh trượt (slider) thay vì trục tọa độ! Luôn đổi biến độc lập thành <code>x</code> và hàm số thành <code>y</code>.
    </div>
  </div>

  <div id="sec-systems" class="sat-card lecture-interactive-card" data-lecture-section="systems">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Hệ phương trình bậc nhất tham số &amp; Phím tắt "Cộng/Trừ thẳng biểu thức"</h2>
    <p>Trong Module 2 Hard, College Board cực thích cho hệ hai phương trình dạng chuẩn <code>a₁x + b₁y = c₁</code> và <code>a₂x + b₂y = c₂</code> có chứa tham số <code>k</code> hoặc <code>r</code> và hỏi điều kiện số nghiệm.</p>
    <div class="sat-gold-box">
      <b>⭐ Công thức Vàng Tỉ lệ Hệ số (Zero-Algebra 5 giây):</b>
      <br>• <b>Đúng 1 nghiệm (Unique solution):</b> <code>a₁ / a₂ ≠ b₁ / b₂</code> (hai đường thẳng cắt nhau, khác hệ số góc).
      <br>• <b>Vô nghiệm (No solution):</b> <code>a₁ / a₂ = b₁ / b₂ ≠ c₁ / c₂</code> (hai đường thẳng <b>song song</b>, cùng slope nhưng khác y-intercept).
      <br>• <b>Vô số nghiệm (Infinitely many solutions):</b> <code>a₁ / a₂ = b₁ / b₂ = c₁ / c₂</code> (hai đường thẳng <b>trùng nhau hoàn toàn</b>).
    </div>
    <div class="sat-ex-box">
      <b>Ví dụ Hard M2:</b> Cho hệ <code>4x − 6y = 18</code> và <code>kx + 9y = −27</code> có <b>vô số nghiệm</b>. Tìm <code>k</code>.
      <br><b>Giải trong 5 giây:</b> Để vô số nghiệm: <code>k / 4 = 9 / (−6) = −27 / 18</code>.
      <br>Kiểm tra tỉ lệ: <code>9 / (−6) = −3/2</code> và <code>−27 / 18 = −3/2</code> (khớp!). Vậy <code>k = 4 × (−3/2) = −6</code>.
    </div>
    <div class="sat-rule-box">
      <b>⚡ Mẹo "Đề hỏi biểu thức gì, ghép ra thẳng biểu thức đó":</b> Nếu đề cho <code>3x + 5y = 19</code> và <code>x − y = 3</code> rồi hỏi giá trị của <code>2x + 2y</code>, khoan vội giải riêng <code>x</code> và <code>y</code>! Lấy phương trình 1 cộng/trừ bội của phương trình 2 (ví dụ PT1 + PT2 = <code>4x + 4y = 22</code> → chia 2 ra ngay <code>2x + 2y = 11</code>!).
    </div>
  </div>
'''
    m1_1_qc = make_quick_check_html(
        'qc_m1_1',
        'Hệ phương trình 5x − 3y = 12 và kx + 6y = 10 có VÔ NGHIỆM (no solution). Giá trị của hằng số k là bao nhiêu?',
        'Given the system:<br><b>5x − 3y = 12</b><br><b>kx + 6y = 10</b><br>If the system has <b>no solution</b>, what is the value of <i>k</i>?',
        ['−10', '−5/2', '5/2', '10'],
        0,
        'Để hệ vô nghiệm (song song), tỉ lệ hệ số x và y phải bằng nhau nhưng khác tỉ lệ hằng số tự do: k / 5 = 6 / (−3) = −2 → k = −10. Kiểm tra hằng số: 10 / 12 ≠ −2 (đúng vô nghiệm!). Bẫy phổ biến là chọn +10 do quên dấu trừ ở −3y.'
    )
    m1_1_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 1 • ALGEBRA & DESMOS',
        '1.1 Desmos 800 Speed Playbook & Linear Equations/Systems',
        'Làm chủ cấu trúc thi 44 câu Adaptive, 4 tuyệt chiêu Desmos 10 giây và công thức tỉ lệ hệ số xử lý gọn mọi hệ phương trình tham số Hard M2.',
        [
            'Nắm vững tỉ trọng 4 Content Domains và chiến lược phân bổ 35 phút/module để đạt 780–800 Math.',
            'Sử dụng thành thạo 4 chiêu Desmos: Intersections, Regression (~), Sliders và kiểm tra biểu thức tương đương.',
            'Giải quyết hệ phương trình vô nghiệm / vô số nghiệm chứa tham số trong 5 giây bằng tỉ lệ a₁/a₂ = b₁/b₂.',
        ],
        m1_1_cards,
        m1_1_qc
    )
    m1_1_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Digital SAT Math 1500+',
            'selector': '#sec-header',
            'en': 'Welcome to Digital SAT Math 1500 Plus! To reach 780 to 800 on the Math section, you need two superpowers: rock-solid algebraic intuition and ruthless speed with the built-in Desmos graphing calculator. Let us unlock both right now.',
            'vi': 'Chào mừng bạn đến với khóa Digital SAT Math 1500 Plus! Để chạm ngưỡng 780 đến 800 điểm Toán, bạn cần hai siêu năng lực: tư duy đại số sắc bén và tốc độ làm chủ máy tính đồ thị Desmos tích hợp sẵn. Chúng ta bắt đầu ngay bài học nền tảng quan trọng nhất này.'
        },
        {
            'id': 'blueprint',
            'title': 'Cấu trúc 44 câu & 4 Content Domains',
            'selector': '#sec-blueprint',
            'en': 'Digital SAT Math consists of two thirty-five-minute modules with twenty-two questions each. Seventy percent of the test comes from Algebra and Advanced Math, while the remaining thirty percent covers Problem Solving, Data Analysis, Geometry, and Trigonometry. Aim to finish the first fifteen questions of Hard Module Two in fifteen minutes so you save twenty full minutes for the toughest seven questions at the end.',
            'vi': 'Phần Toán gồm 2 module, mỗi module 22 câu trong 35 phút, tức trung bình 95 giây một câu. Có tới 70 phần trăm đề thi nằm ở hai mảng Algebra và Advanced Math, 30 phần trăm còn lại là Data Analysis và Geometry. Bí quyết đạt 800 là ở Module 2 Hard, hãy xử lý gọn 15 câu đầu trong 15 phút để dành trọn 20 phút cho 7 câu khó nhất ở cuối.'
        },
        {
            'id': 'desmos',
            'title': '4 Vũ khí Desmos 10 giây',
            'selector': '#sec-desmos',
            'en': 'Desmos is allowed on every single Math question. Master four moves: first, graph two equations and click the gray intersection dot. Second, enter a table of points and run a tilde regression to find exact linear or quadratic coefficients instantly. Third, add sliders for unknown constants like k. Fourth, graph equivalent expressions to verify they overlap completely. Always replace variables like t or n with x and y so Desmos plots them properly.',
            'vi': 'Desmos được dùng xuyên suốt cả bài thi Toán. Hãy thuộc nằm lòng 4 tuyệt chiêu: một là vẽ 2 phương trình rồi bấm thẳng chấm xám giao điểm; hai là nhập bảng dữ liệu rồi dùng dấu ngã hồi quy để tìm hệ số m, b, a, c trong 3 giây; ba là dùng thanh trượt slider cho tham số k; bốn là vẽ 2 hàm f x và g x xem có trùng khít không để kiểm tra biểu thức tương đương. Nhớ luôn đổi các ẩn t, n, p thành x và y khi gõ vào Desmos.'
        },
        {
            'id': 'systems',
            'title': 'Hệ phương trình tham số & Mẹo ghép biểu thức',
            'selector': '#sec-systems',
            'en': 'For a linear system in standard form, compare the coefficient ratios. If a one over a two equals b one over b two, the lines have the same slope. If that ratio does not equal c one over c two, the lines are parallel and there is no solution. If all three ratios are equal, the lines coincide and there are infinitely many solutions. Also, when a question asks for an expression like two x plus two y, try adding or subtracting the equations directly before solving for x and y individually.',
            'vi': 'Với hệ phương trình bậc nhất dạng chuẩn, đừng biến đổi rườm rà mà hãy so thẳng tỉ số hệ số. Khi a một trên a hai bằng b một trên b hai nhưng khác c một trên c hai, hai đường thẳng song song nên hệ vô nghiệm. Khi cả ba tỉ số bằng nhau, hai đường thẳng trùng nhau nên hệ có vô số nghiệm. Ngoài ra, khi đề hỏi trực tiếp một biểu thức như 2x cộng 2y, hãy thử cộng hoặc trừ hai phương trình trước khi mất công tìm lẻ từng ẩn.'
        }
    ]
    lectures.append({
        'code': 'm1_1',
        'module_key': 'math_m1',
        'order_index': 1,
        'title': '1.1 Desmos 800 Speed Playbook & Linear Equations/Systems',
        'drill_key': 'drill_m1_1',
        'html': m1_1_html,
        'segments': m1_1_segs,
        'major_sections': [
            {'title': 'Cấu trúc 44 câu & 4 Domains', 'startSegmentId': 'blueprint'},
            {'title': '4 Vũ khí Desmos 10 giây', 'startSegmentId': 'desmos'},
            {'title': 'Hệ phương trình tham số', 'startSegmentId': 'systems'},
        ],
    })

    # =========================================================================
    # LECTURE M1.2: Linear Functions, Slope-Intercept Models & Word Problems
    # =========================================================================
    m1_2_cards = f'''
  <div id="sec-slope" class="sat-card lecture-interactive-card" data-lecture-section="slope">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Giải mã Slope (m) và y-Intercept (b) trong bài toán thực tế</h2>
    <p>Mọi đường thẳng trên Digital SAT đều xoay quanh 3 dạng phương trình — nhận diện đúng dạng giúp đọc ngay kết quả mà không cần biến đổi:</p>
    <table class="sat-table">
      <thead><tr><th>Dạng phương trình</th><th>Công thức</th><th>Thông tin lộ diện ngay lập tức</th></tr></thead>
      <tbody>
        <tr><td><b>Slope-Intercept</b></td><td><code>y = mx + b</code></td><td>Hệ số góc <code>m</code> (tốc độ thay đổi mỗi 1 đơn vị x) &amp; tung độ gốc <code>(0, b)</code> (giá trị ban đầu).</td></tr>
        <tr><td><b>Standard Form</b></td><td><code>Ax + By = C</code></td><td><code>slope = −A / B</code> • <code>y-intercept = C / B</code> • <code>x-intercept = C / A</code>.</td></tr>
        <tr><td><b>Point-Slope Form</b></td><td><code>y − y₁ = m(x − x₁)</code></td><td>Đi qua điểm <code>(x₁, y₁)</code> với hệ số góc <code>m</code>.</td></tr>
      </tbody>
    </table>
    <div class="sat-trap-box">
      <b>🚨 Bẫy "Đơn vị bước nhảy" (Step-Size Trap):</b> Khi đề cho hàm <code>T(h) = 42 − 1.8h</code> và hỏi nhiệt độ thay đổi bao nhiêu khi <code>h</code> tăng thêm <b>5 đơn vị</b> (không phải 1 đơn vị!), đáp án là <code>−1.8 × 5 = −9</code> chứ không phải <code>−1.8</code>! Hoặc nếu đề cho <code>f(x + 3) − f(x) = 12</code> thì hệ số góc là <code>m = 12 / 3 = 4</code>.
    </div>
  </div>

  <div id="sec-perp" class="sat-card lecture-interactive-card" data-lecture-section="perp">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Đường thẳng Song song, Vuông góc &amp; Phép tịnh tiến đồ thị</h2>
    <div class="sat-gold-box">
      <b>⭐ Bộ công thức Quan hệ 2 đường thẳng:</b>
      <br>• <b>Song song (Parallel):</b> <code>m₁ = m₂</code> (cùng hệ số góc, khác y-intercept).
      <br>• <b>Vuông góc (Perpendicular):</b> <code>m₁ · m₂ = −1</code> tức <code>m₂ = −1 / m₁</code> (<b>nghịch đảo đổi dấu</b> — negative reciprocal!).
      <br>• <b>Mẹo Standard Form siêu nhanh:</b> Đường thẳng vuông góc với <code>Ax + By = C</code> luôn có dạng <code>Bx − Ay = D</code>! (Đổi chỗ A, B và đổi dấu ở giữa — mất đúng 2 giây!).
    </div>
    <div class="sat-rule-box">
      <b>📌 Phép tịnh tiến hàm bậc nhất (Translations):</b>
      <br>• Dịch <b>lên k đơn vị</b>: <code>g(x) = f(x) + k</code> (y-intercept cộng thêm k).
      <br>• Dịch <b>sang phải h đơn vị</b>: <code>g(x) = f(x − h)</code> → thay mọi <code>x</code> bằng <code>(x − h)</code>!
      <br>• <b>Cảnh giác bẫy:</b> Nếu <code>f(x) = 3x + 5</code> được dịch <b>sang phải 4 đơn vị</b>, hàm mới là <code>g(x) = 3(x − 4) + 5 = 3x − 7</code> (y-intercept giảm đi <code>3 × 4 = 12</code>, KHÔNG PHẢI giảm 4!).
    </div>
  </div>

  <div id="sec-table-models" class="sat-card lecture-interactive-card" data-lecture-section="table_models">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Đọc bảng dữ liệu có Input lệch &amp; Chiến thuật Desmos Regression</h2>
    <p>Trong Module 2 Hard, đề hay cho bảng giá trị của <code>x</code> và <code>f(x) + 7</code> (hoặc <code>2f(x)</code>) thay vì <code>f(x)</code> thuần túy, rồi hỏi tung độ gốc hoặc nghiệm của <code>f(x) = 0</code>.</p>
    <div class="sat-ex-box">
      <b>Ví dụ Hard M2:</b> Cho bảng giá trị của hàm bậc nhất <code>f</code> dưới dạng <code>g(x) = f(x) − 4</code>: tại <code>x = 2</code> thì <code>g(2) = 5</code>; tại <code>x = 6</code> thì <code>g(6) = 17</code>. Tìm <code>f(0)</code>.
      <br><b>Bước 1:</b> Khôi phục <code>f(x) = g(x) + 4</code> → ta có 2 điểm của <code>f</code> là <code>(2, 9)</code> và <code>(6, 21)</code>.
      <br><b>Bước 2:</b> Hệ số góc <code>m = (21 − 9) / (6 − 2) = 12 / 4 = 3</code>.
      <br><b>Bước 3:</b> <code>f(0) = 9 − 3(2) = 3</code>.
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Mẹo Desmos:</b> Tạo bảng <code>x₁ = [2, 6]</code>, <code>y₁ = [9, 21]</code> → gõ <code>y₁ ~ mx₁ + b</code> → Desmos báo ngay <code>m = 3, b = 3</code>! Không bao giờ tính nhầm dấu trừ.
    </div>
  </div>
'''
    m1_2_qc = make_quick_check_html(
        'qc_m1_2',
        'Đường thẳng d có phương trình 4x − 5y = 20. Đường thẳng k vuông góc với d và đi qua điểm (8, −3). Tung độ gốc (y-intercept) của đường thẳng k là bao nhiêu?',
        'Line <i>d</i> is defined by <b>4x − 5y = 20</b>. Line <i>k</i> is <b>perpendicular</b> to line <i>d</i> and passes through the point <b>(8, −3)</b>. What is the y-intercept of line <i>k</i>?',
        ['(0, 7)', '(0, −13)', '(0, 13)', '(0, −7)'],
        0,
        'Đường d có slope m₁ = 4/5 → đường k vuông góc có slope m₂ = −5/4. Thay (8, −3) vào y = (−5/4)x + b: −3 = (−5/4)(8) + b = −10 + b → b = 7. Vậy y-intercept là (0, 7). Dùng mẹo nhanh Standard Form: 5x + 4y = D → 5(8) + 4(−3) = 28 → y-intercept = 28/4 = 7!'
    )
    m1_2_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 1 • ALGEBRA',
        '1.2 Linear Functions, Slope-Intercept Models & Word Problems',
        'Làm chủ ý nghĩa thực tế của slope, x-intercept, y-intercept, quy tắc vuông góc nhanh 2 giây và bẫy bảng dữ liệu hàm dịch chuyển.',
        [
            'Đọc tức thì hệ số góc và giao điểm trục từ cả 3 dạng Slope-Intercept, Standard Form và Point-Slope.',
            'Áp dụng quy tắc đổi hệ số nhanh Bx − Ay = D cho đường thẳng vuông góc và tránh bẫy tịnh tiến ngang f(x − h).',
            'Phát hiện ngay bẫy đơn vị bước nhảy (Δx ≠ 1) và bảng giá trị bị cộng/nhân thêm hằng số trong Hard M2.',
        ],
        m1_2_cards,
        m1_2_qc
    )
    m1_2_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Hàm bậc nhất & Bài toán thực tế',
            'selector': '#sec-header',
            'en': 'Linear functions are the backbone of SAT Algebra. Even on Hard Module Two, the College Board loves disguising simple lines inside word problems, standard form equations, and shifted data tables. Let us strip away every disguise.',
            'vi': 'Hàm số bậc nhất là xương sống của phần Đại số SAT. Ngay cả trong Module 2 Hard, College Board rất thích ngụy trang những đường thẳng quen thuộc dưới dạng bài toán lời văn, phương trình dạng chuẩn hoặc bảng dữ liệu bị dịch chuyển. Hãy cùng bóc tách từng dạng một.'
        },
        {
            'id': 'slope',
            'title': 'Slope, Intercepts & Bẫy bước nhảy',
            'selector': '#sec-slope',
            'en': 'Remember the three linear forms. In standard form A x plus B y equals C, the slope is immediately negative A over B, and the y-intercept is C over B. Watch out for the step-size trap: the slope tells you the change in y when x increases by one unit, so if a question asks about an increase of five units in x, multiply the slope by five.',
            'vi': 'Hãy ghi nhớ nhanh công thức dạng chuẩn A x cộng B y bằng C: hệ số góc lập tức là trừ A trên B, và tung độ gốc là C trên B. Đặc biệt cảnh giác bẫy bước nhảy: hệ số góc chỉ cho biết mức thay đổi của y khi x tăng một đơn vị, nên nếu đề hỏi x tăng thêm năm đơn vị thì bắt buộc phải nhân hệ số góc với năm.'
        },
        {
            'id': 'perp',
            'title': 'Song song, Vuông góc & Tịnh tiến',
            'selector': '#sec-perp',
            'en': 'Perpendicular lines have negative reciprocal slopes, meaning their product is negative one. In standard form, a line perpendicular to A x plus B y equals C always has the form B x minus A y equals D—just swap A and B and flip the middle sign. For horizontal shifts, moving a graph h units to the right replaces x with x minus h inside the parentheses, which changes the y-intercept by negative m times h.',
            'vi': 'Hai đường thẳng vuông góc có tích hai hệ số góc bằng trừ một, tức nghịch đảo và đổi dấu. Ở dạng chuẩn, đường vuông góc với A x cộng B y bằng C luôn có dạng B x trừ A y bằng D: chỉ cần đổi chỗ A, B và đổi dấu ở giữa trong 2 giây. Khi tịnh tiến đồ thị sang phải h đơn vị, ta thay x bằng x trừ h trong ngoặc nên tung độ gốc sẽ thay đổi một lượng bằng trừ m nhân h chứ không phải trừ h.'
        },
        {
            'id': 'table_models',
            'title': 'Bảng dữ liệu bị dịch chuyển & Desmos',
            'selector': '#sec-table-models',
            'en': 'Hard questions frequently give you a table for f of x minus a constant, or a multiple of f of x, instead of f of x directly. Always reconstruct the true values of f of x first, then run a quick linear regression y one tilde m x one plus b in Desmos to guarantee zero sign errors.',
            'vi': 'Các câu khó hay cho bảng giá trị của f x trừ đi một hằng số thay vì f x trực tiếp. Luôn luôn khôi phục cột giá trị thực của f x trước, sau đó gõ hồi quy tuyến tính y một ngã m x một cộng b trong Desmos để chắc chắn không bao giờ nhầm dấu.'
        }
    ]
    lectures.append({
        'code': 'm1_2',
        'module_key': 'math_m1',
        'order_index': 2,
        'title': '1.2 Linear Functions, Slope-Intercept Models & Word Problems',
        'drill_key': 'drill_m1_2',
        'html': m1_2_html,
        'segments': m1_2_segs,
        'major_sections': [
            {'title': 'Slope, Intercepts & Bẫy bước nhảy', 'startSegmentId': 'slope'},
            {'title': 'Song song, Vuông góc & Tịnh tiến', 'startSegmentId': 'perp'},
            {'title': 'Bảng dữ liệu lệch & Desmos', 'startSegmentId': 'table_models'},
        ],
    })

    # =========================================================================
    # LECTURE M1.3: Linear Inequalities, Systems & Feasible Regions
    # =========================================================================
    m1_3_cards = f'''
  <div id="sec-flip" class="sat-card lecture-interactive-card" data-lecture-section="flip">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Quy tắc Đổi chiều bất đẳng thức &amp; Tối ưu hóa số nguyên (Integer Constraints)</h2>
    <p>Bất phương trình bậc nhất rất dễ ăn điểm tối đa, nhưng College Board luôn cài 2 cái bẫy chí mạng:</p>
    <div class="sat-rule-box">
      <b>1. Quy tắc Đổi chiều:</b> Nhân hoặc chia cả hai vế cho một <b>số âm</b> → BẮT BUỘC <b>đảo chiều dấu</b> (<code>&lt;</code> thành <code>&gt;</code>, <code>≤</code> thành <code>≥</code>).
      <br><b>2. Bẫy Ngôn ngữ (Word-Problem Inequalities):</b>
      <br>• <i>"at least" / "no less than" / "minimum of"</i> → <b><code>≥</code></b>
      <br>• <i>"at most" / "no more than" / "maximum of" / "cannot exceed"</i> → <b><code>≤</code></b>
      <br>• <i>"more than" / "exceeds"</i> → <b><code>&gt;</code></b> (nghiêm ngặt, KHÔNG có dấu bằng!)
      <br>• <i>"fewer than" / "less than"</i> → <b><code>&lt;</code></b>
    </div>
    <div class="sat-trap-box">
      <b>🚨 Bẫy làm tròn số nguyên (Rounding Trap):</b> Nếu số thùng hàng phải thỏa mãn <code>x ≤ 14.8</code> → giá trị nguyên lớn nhất là <b>14</b> (KHÔNG làm tròn lên 15!). Ngược lại, nếu số chuyến xe cần thỏa mãn <code>n ≥ 6.2</code> → giá trị nguyên nhỏ nhất là <b>7</b> (làm tròn lên!). Với bất đẳng thức nghiêm ngặt <code>x &lt; 12</code> → số nguyên lớn nhất là <b>11</b>.
    </div>
  </div>

  <div id="sec-quadrants" class="sat-card lecture-interactive-card" data-lecture-section="quadrants">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Hệ Bất phương trình 2 ẩn &amp; Bài toán "Góc phần tư (Quadrant)"</h2>
    <p>Trong mặt phẳng tọa độ Oxy, đường biên của bất phương trình 2 ẩn phân chia mặt phẳng thành hai nửa:</p>
    <table class="sat-table">
      <thead><tr><th>Dấu bất đẳng thức (sau khi cô lập y)</th><th>Đường biên</th><th>Miền nghiệm (Shading)</th></tr></thead>
      <tbody>
        <tr><td><code>y &gt; mx + b</code></td><td>Nét đứt (Dashed — không lấy biên)</td><td>Tô phần <b>phía trên</b> đường thẳng</td></tr>
        <tr><td><code>y ≥ mx + b</code></td><td>Nét liền (Solid — lấy cả biên)</td><td>Tô phần <b>phía trên</b> đường thẳng</td></tr>
        <tr><td><code>y &lt; mx + b</code></td><td>Nét đứt (Dashed)</td><td>Tô phần <b>phía dưới</b> đường thẳng</td></tr>
        <tr><td><code>y ≤ mx + b</code></td><td>Nét liền (Solid)</td><td>Tô phần <b>phía dưới</b> đường thẳng</td></tr>
      </tbody>
    </table>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Hack cho bài toán Quadrant &amp; Điểm thuộc miền nghiệm:</b>
      <br>Gõ <b>nguyên văn</b> 2 bất phương trình (ví dụ <code>y &gt; 2x + 3</code> và <code>y &lt; −x + 1</code>) vào Desmos! Desmos tự động tô màu miền giao nhau (vùng đậm nhất).
      <br>• Muốn biết góc phần tư nào <b>KHÔNG chứa nghiệm nào</b> (Quadrant I: <code>x&gt;0, y&gt;0</code>; II: <code>x&lt;0, y&gt;0</code>; III: <code>x&lt;0, y&lt;0</code>; IV: <code>x&gt;0, y&lt;0</code>) → nhìn thẳng bằng mắt trên Desmos trong 3 giây!
      <br>• Muốn kiểm tra điểm <code>(a, b)</code> có thuộc hệ không → gõ thẳng tọa độ <code>(a, b)</code> lên Desmos xem chấm đó có nằm trong vùng tô đậm hay không (chú ý nét đứt thì điểm trên biên KHÔNG tính!).
    </div>
  </div>

  <div id="sec-param-ineq" class="sat-card lecture-interactive-card" data-lecture-section="param_ineq">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bất phương trình Tham số &amp; Biểu thức Chặn (Hard M2 780–800)</h2>
    <p>Dạng bài ăn điểm 800 trong Module 2 Hard thường cho một điểm <code>(x₀, y₀)</code> thỏa mãn hệ bất phương trình có chứa tham số <code>a, b</code> hoặc yêu cầu tìm miền giá trị lớn nhất/nhỏ nhất của tổ hợp <code>ax + by</code>.</p>
    <div class="sat-ex-box">
      <b>Ví dụ Hard M2:</b> Cho <code>y ≤ −2x + 15</code> và <code>y ≤ 3x + 5</code>. Nếu điểm <code>(x, y)</code> thỏa mãn cả hai bất phương trình, giá trị <b>lớn nhất</b> có thể của <code>y</code> là bao nhiêu?
      <br><b>Phân tích đỉnh (Vertex Rule):</b> Vì cả hai đường đều chặn <b>phía trên</b> của <code>y</code> (một đường dốc xuống, một đường dốc lên), điểm cao nhất của miền nghiệm hình chữ V ngược chính là <b>giao điểm của hai đường biên</b>!
      <br>Giải <code>−2x + 15 = 3x + 5</code> → <code>5x = 10</code> → <code>x = 2</code> → <code>y_max = 3(2) + 5 = 11</code>.
    </div>
    <div class="sat-gold-box">
      <b>💡 Quy tắc Đỉnh Giao điểm (Corner-Point Rule):</b> Trong hệ bất phương trình tuyến tính, giá trị lớn nhất hoặc nhỏ nhất của <code>x</code>, <code>y</code> hoặc biểu thức tuyến tính <code>ax + by</code> luôn đạt tại <b>giao điểm (đỉnh)</b> của các đường biên. Gõ thẳng hệ lên Desmos rồi bấm vào đỉnh giao nhau để chốt đáp án trong 5 giây!
    </div>
  </div>
'''
    m1_3_qc = make_quick_check_html(
        'qc_m1_3',
        'Trong mặt phẳng tọa độ xy, một điểm (a, b) thỏa mãn cả hai bất phương trình y ≤ −3x + 19 và y ≤ 2x + 4. Giá trị lớn nhất có thể của b là bao nhiêu?',
        'In the xy-plane, a point (<i>a</i>, <i>b</i>) is a solution to the system of inequalities:<br><b>y ≤ −3x + 19</b><br><b>y ≤ 2x + 4</b><br>What is the <b>maximum</b> possible value of <i>b</i>?',
        ['3', '10', '11', '19'],
        1,
        'Vì cả hai đường đều có dạng y ≤ ... (một đường slope âm −3, một đường slope dương +2), miền nghiệm có đỉnh cao nhất nằm đúng tại giao điểm 2 đường thẳng: −3x + 19 = 2x + 4 → 5x = 15 → x = 3 → y = 2(3) + 4 = 10. Vậy giá trị lớn nhất của b là 10!'
    )
    m1_3_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 1 • ALGEBRA',
        '1.3 Linear Inequalities, Systems of Inequalities & Feasible Regions',
        'Chinh phục triệt để bài toán bất phương trình, làm tròn số nguyên, loại góc phần tư bằng Desmos và quy tắc Đỉnh giao điểm cho câu Hard M2.',
        [
            'Dịch chuẩn 100% từ khóa bất đẳng thức (at least, at most, exceeds) và tránh bẫy làm tròn số nguyên.',
            'Sử dụng Desmos tô miền nghiệm để chốt bài toán Quadrant và kiểm tra biên nét đứt/nét liền trong 5 giây.',
            'Áp dụng Quy tắc Đỉnh giao điểm (Corner-Point Rule) tìm Max/Min của hệ bất phương trình tuyến tính Hard M2.',
        ],
        m1_3_cards,
        m1_3_qc
    )
    m1_3_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Bất phương trình tuyến tính',
            'selector': '#sec-header',
            'en': 'Linear inequalities test precision. One flipped sign, one careless rounding step, or one missed dashed boundary line can cost you ten points. Let us lock down every inequality rule and Desmos visual trick.',
            'vi': 'Bất phương trình bậc nhất là bài kiểm tra sự cẩn thận tuyệt đối. Chỉ cần quên đổi chiều dấu, làm tròn nhầm hướng hoặc nhầm đường biên nét đứt với nét liền là mất ngay 10 điểm. Chúng ta sẽ khóa chặt mọi quy tắc và mẹo Desmos cho chuyên đề này.'
        },
        {
            'id': 'flip',
            'title': 'Đổi chiều dấu & Bẫy làm tròn số nguyên',
            'selector': '#sec-flip',
            'en': 'Whenever you multiply or divide both sides of an inequality by a negative number, immediately flip the inequality sign. In word problems, translate at least as greater than or equal to, and at most as less than or equal to. For integer constraints, never blindly round to the nearest integer: if x is at most fourteen point eight, the maximum integer is fourteen, not fifteen.',
            'vi': 'Mỗi khi nhân hoặc chia hai vế cho số âm, phải đảo chiều dấu ngay lập tức. Trong bài toán lời văn, at least là lớn hơn hoặc bằng, còn at most là nhỏ hơn hoặc bằng. Đặc biệt với điều kiện số nguyên, tuyệt đối không làm tròn theo kiểu gần nhất: nếu x nhỏ hơn hoặc bằng 14 phẩy 8 thì số nguyên lớn nhất là 14, còn nếu n lớn hơn hoặc bằng 6 phẩy 2 thì số nguyên nhỏ nhất phải là 7.'
        },
        {
            'id': 'quadrants',
            'title': 'Miền nghiệm 2 ẩn & Desmos Shading',
            'selector': '#sec-quadrants',
            'en': 'For two-variable systems of inequalities, type both inequalities directly into Desmos. The overlapping darkest shaded region is your feasible region. You can visually spot which quadrant contains no solutions in three seconds. Just remember that points sitting right on a dashed line are not solutions.',
            'vi': 'Với hệ bất phương trình hai ẩn, hãy gõ thẳng cả hai bất phương trình vào Desmos. Vùng tô màu đậm nhất chồng lên nhau chính là miền nghiệm chung. Bạn sẽ nhìn ra ngay góc phần tư nào không có nghiệm nào chỉ trong 3 giây. Chỉ cần nhớ điểm nằm trên đường nét đứt không thuộc miền nghiệm.'
        },
        {
            'id': 'param_ineq',
            'title': 'Quy tắc Đỉnh giao điểm cho câu Max/Min Hard M2',
            'selector': '#sec-param-ineq',
            'en': 'On Hard Module Two, you are often asked for the maximum or minimum possible value of y, x, or a linear combination inside a feasible region. By the Corner-Point Rule, extreme values of linear systems always occur at the intersection vertex of the boundary lines. Set the boundary equations equal, or click the vertex directly in Desmos.',
            'vi': 'Trong Module 2 Hard, đề hay hỏi giá trị lớn nhất hoặc nhỏ nhất của y hoặc x trong miền nghiệm của hai bất phương trình. Theo quy tắc Đỉnh giao điểm, giá trị cực trị luôn xảy ra ngay tại giao điểm của hai đường biên. Chỉ cần cho hai đường biên bằng nhau hoặc bấm vào đỉnh giao điểm trên Desmos là ra ngay đáp án.'
        }
    ]
    lectures.append({
        'code': 'm1_3',
        'module_key': 'math_m1',
        'order_index': 3,
        'title': '1.3 Linear Inequalities, Systems of Inequalities & Feasible Regions',
        'drill_key': 'drill_m1_3',
        'html': m1_3_html,
        'segments': m1_3_segs,
        'major_sections': [
            {'title': 'Đổi chiều dấu & Bẫy số nguyên', 'startSegmentId': 'flip'},
            {'title': 'Miền nghiệm 2 ẩn & Desmos', 'startSegmentId': 'quadrants'},
            {'title': 'Quy tắc Đỉnh giao điểm Hard M2', 'startSegmentId': 'param_ineq'},
        ],
    })

    return lectures
