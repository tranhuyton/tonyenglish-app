# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 3 Lectures (Problem-Solving & Data Analysis):
- m3_1: Ratios, Rates, Squared/Cubed Unit Conversions & Multi-Step Percentages
- m3_2: Statistics (Mean/Median/SD Shifts), Probability, Margin of Error & Study Design
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

DESMOS_BOX_STYLE = 'background:#ecfdf5; border-left:4px solid #059669; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; color:#064e3b;'

def get_m3_lectures():
    lectures = []

    # =========================================================================
    # LECTURE M3.1: Ratios, Rates, Squared/Cubed Units & Percentages
    # =========================================================================
    m3_1_cards = f'''
  <div id="sec-units" class="sat-card lecture-interactive-card" data-lecture-section="units">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Bẫy Đổi đơn vị Diện tích (bình phương) &amp; Thể tích (lập phương)</h2>
    <p>Học sinh aim 1500+ rất ít khi sai đổi đơn vị chiều dài, nhưng hơn một nửa thí sinh bị sập bẫy khi đề yêu cầu đổi <b>đơn vị diện tích (square units)</b> hoặc <b>thể tích (cubic units)</b>!</p>
    <div class="sat-gold-box">
      <b>⭐ Quy tắc Lũy thừa Hệ số đổi đơn vị:</b>
      <br>• Chiều dài: <code>1 yard = 3 feet</code> (hệ số <code>3</code>)
      <br>• Diện tích: <code>1 yd² = 3² ft² = 9 ft²</code> (phải <b>BÌNH PHƯƠNG</b> hệ số!)
      <br>• Thể tích: <code>1 yd³ = 3³ ft³ = 27 ft³</code> (phải <b>LẬP PHƯƠNG</b> hệ số!)
      <br>• Tương tự: <code>1 m = 100 cm</code> → <code>1 m² = 10,000 cm²</code> và <code>1 m³ = 1,000,000 cm³</code>!
    </div>
    <div class="sat-ex-box">
      <b>Ví dụ Hard M2:</b> Một bề mặt có diện tích <code>540 square inches</code>. Đổi sang <code>square feet</code> (biết <code>1 foot = 12 inches</code>).
      <br><b>Sai lầm chí mạng:</b> Chia cho 12 ra 45 (SAI!).
      <br><b>Cách làm 800:</b> <code>1 ft² = 12² = 144 in²</code> → <code>540 / 144 = 3.75 ft²</code>!
    </div>
  </div>

  <div id="sec-percent" class="sat-card lecture-interactive-card" data-lecture-section="percent">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Ngôn ngữ Phần trăm &amp; Bẫy Phần trăm Kép (Successive Percent Changes)</h2>
    <table class="sat-table">
      <thead><tr><th>Cụm từ tiếng Anh trên đề SAT</th><th>Công thức toán học chính xác</th><th>Ví dụ với p = 40%</th></tr></thead>
      <tbody>
        <tr><td><code>A is p% of B</code></td><td><code>A = (p / 100) · B</code></td><td><code>A = 0.40 · B</code></td></tr>
        <tr><td><code>A is p% GREATER than B</code></td><td><code>A = (1 + p / 100) · B</code></td><td><code>A = 1.40 · B</code></td></tr>
        <tr><td><code>A is p% LESS than B</code></td><td><code>A = (1 − p / 100) · B</code></td><td><code>A = 0.60 · B</code></td></tr>
        <tr><td><code>Percent Change from Old to New</code></td><td><code>[(New − Old) / Old] × 100%</code></td><td>Luôn chia cho <b>Old (giá trị gốc)</b>!</td></tr>
      </tbody>
    </table>
    <div class="sat-trap-box">
      <b>🚨 Bẫy Cộng/Trừ phần trăm liên tiếp:</b> Một mặt hàng tăng giá <b>25%</b>, sau đó giảm giá <b>20%</b>. Giá cuối cùng KHÔNG tăng 5%! Ta phải <b>NHÂN</b> các hệ số: <code>1.25 × 0.80 = 1.00</code> → quay về đúng <b>100% giá ban đầu (thay đổi 0%)</b>!
      <br><b>Mẹo đặt 100 cho chuỗi phần trăm đại số:</b> Khi đề cho "<i>a is 220% of b, and b is 30% of c. What percent of c is a?</i>" → đặt ngay <code>c = 100</code> → <code>b = 30</code> → <code>a = 2.20 × 30 = 66</code> → đáp án <b>66%</b> trong 5 giây!
    </div>
  </div>

  <div id="sec-density" class="sat-card lecture-interactive-card" data-lecture-section="density">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Tỉ suất (Rates), Khối lượng riêng (Density) &amp; Vận tốc trung bình</h2>
    <div class="sat-rule-box">
      <b>• Khối lượng riêng (Density):</b> <code>Density = Mass / Volume</code> → nhớ tam giác <code>M = D · V</code>.
      <br><b>• Vận tốc trung bình (Average Speed):</b> <code>Average Speed = Total Distance / Total Time</code> — <b>KHÔNG BAO GIỜ</b> lấy trung bình cộng <code>(v₁ + v₂) / 2</code> khi hai chặng có thời gian khác nhau!
    </div>
    <div class="sat-ex-box">
      <b>Ví dụ Kinh điển:</b> Đi quãng đường 60 km với vận tốc 30 km/h, quay về 60 km với vận tốc 60 km/h.
      <br>• Thời gian đi = <code>60/30 = 2 giờ</code> • Thời gian về = <code>60/60 = 1 giờ</code>.
      <br>• Vận tốc trung bình = <code>(60 + 60) / (2 + 1) = 120 / 3 = 40 km/h</code> (KHÔNG phải <code>(30+60)/2 = 45</code>!).
    </div>
  </div>
'''
    m3_1_qc = make_quick_check_html(
        'qc_m3_1',
        'Số dương a lớn hơn b 150% (a is 150% greater than b), và b bằng 40% của c. Hỏi a bằng bao nhiêu phần trăm của c?',
        'Positive number <i>a</i> is <b>150% greater than</b> <i>b</i>, and <i>b</i> is <b>40% of</b> <i>c</i>. What percent of <i>c</i> is <i>a</i>?',
        ['60%', '100%', '110%', '190%'],
        1,
        'Đặt c = 100 → b = 40% của 100 = 40. Chú ý cụm "150% GREATER than b" nghĩa là a = (1 + 1.50) · b = 2.50 · b (CHỨ KHÔNG PHẢI 1.50 · b!). Vậy a = 2.50 × 40 = 100 → a bằng đúng 100% của c!'
    )
    m3_1_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 3 • PROBLEM-SOLVING & DATA',
        '3.1 Ratios, Rates, Squared/Cubed Units & Percent Traps',
        'Vượt qua mọi bẫy đổi đơn vị bình/lập phương, phân biệt "p% greater than" vs "p% of", chuỗi phần trăm đặt 100 và công thức vận tốc trung bình.',
        [
            'Bình phương và lập phương chính xác hệ số quy đổi khi chuyển đơn vị diện tích (ft² ↔ in²) và thể tích.',
            'Phân biệt tuyệt đối "p% of" (nhân p/100) với "p% greater than" (nhân 1 + p/100) và áp dụng mẹo đặt c = 100.',
            'Tính chuẩn khối lượng riêng (M = D · V) và vận tốc trung bình (Tổng quãng đường / Tổng thời gian).',
        ],
        m3_1_cards,
        m3_1_qc
    )
    m3_1_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Tỉ lệ, Đơn vị & Phần trăm 800',
            'selector': '#sec-header',
            'en': 'Problem-Solving and Data Analysis looks straightforward, yet it hides two of the deadliest wording traps on the SAT: squared or cubed unit conversions and the difference between p percent of versus p percent greater than.',
            'vi': 'Chuyên đề Tỉ lệ và Phần trăm tưởng chừng dễ ăn điểm, nhưng lại ẩn chứa hai cái bẫy ngôn từ nguy hiểm nhất đề SAT: đổi đơn vị diện tích, thể tích và sự khác biệt giữa p phần trăm của với lớn hơn p phần trăm.'
        },
        {
            'id': 'units',
            'title': 'Bẫy Đổi đơn vị Diện tích & Thể tích',
            'selector': '#sec-units',
            'en': 'Whenever you convert area units like square inches to square feet, you must square the linear conversion factor. One foot is twelve inches, so one square foot is one hundred forty-four square inches, not twelve. For volume conversions, cube the linear factor.',
            'vi': 'Mỗi khi đổi đơn vị diện tích như từ inch vuông sang feet vuông, bạn bắt buộc phải bình phương hệ số quy đổi chiều dài. Một foot bằng 12 inch, nên một foot vuông phải bằng 144 inch vuông chứ không phải 12. Tương tự với thể tích thì phải lập phương hệ số.'
        },
        {
            'id': 'percent',
            'title': 'Ngôn ngữ phần trăm & Mẹo đặt 100',
            'selector': '#sec-percent',
            'en': 'Read percent wording like a lawyer. A is one hundred fifty percent of B means multiply B by one point five. But A is one hundred fifty percent greater than B means add one hundred fifty percent on top of one hundred percent, multiplying B by two point five! For successive percent changes, multiply the factors rather than adding percentages, and plug in one hundred for algebraic percent chains.',
            'vi': 'Đọc từ ngữ phần trăm phải chính xác tuyệt đối. A bằng 150 phần trăm của B là nhân với 1 phẩy 5. Nhưng A lớn hơn B 150 phần trăm nghĩa là cộng thêm 150 phần trăm vào 100 phần trăm gốc, tức phải nhân với 2 phẩy 5! Với chuỗi phần trăm liên tiếp, hãy nhân các hệ số và đặt ẩn cuối bằng 100 để tính nhẩm trong 5 giây.'
        },
        {
            'id': 'density',
            'title': 'Khối lượng riêng & Vận tốc trung bình',
            'selector': '#sec-density',
            'en': 'Remember density equals mass divided by volume, and average speed always equals total distance divided by total time—never average the two speeds directly when the travel times differ.',
            'vi': 'Nhớ công thức khối lượng riêng bằng khối lượng chia thể tích, và vận tốc trung bình luôn bằng tổng quãng đường chia tổng thời gian, tuyệt đối không lấy trung bình cộng hai vận tốc.'
        }
    ]
    lectures.append({
        'code': 'm3_1',
        'module_key': 'math_m3',
        'order_index': 1,
        'title': '3.1 Ratios, Rates, Squared/Cubed Units & Percent Traps',
        'drill_key': 'drill_m3_1',
        'html': m3_1_html,
        'segments': m3_1_segs,
        'major_sections': [
            {'title': 'Đổi đơn vị Bình/Lập phương', 'startSegmentId': 'units'},
            {'title': 'Phần trăm & Mẹo đặt 100', 'startSegmentId': 'percent'},
            {'title': 'Density & Average Speed', 'startSegmentId': 'density'},
        ],
    })

    # =========================================================================
    # LECTURE M3.2: Statistics, Probability, Margin of Error & Study Design
    # =========================================================================
    m3_2_cards = f'''
  <div id="sec-stats" class="sat-card lecture-interactive-card" data-lecture-section="stats">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Mean, Median, Range &amp; Standard Deviation (Quy tắc Dịch chuyển &amp; Outlier)</h2>
    <p>Trên Digital SAT, bạn <b>không bao giờ phải tính tay công thức căn bậc hai của Standard Deviation (SD)</b> — thay vào đó, đề kiểm tra hiểu biết bản chất: <b>SD đo mức độ phân tán (spread) của dữ liệu quanh Mean</b>!</p>
    <table class="sat-table">
      <thead><tr><th>Phép biến đổi tập dữ liệu</th><th>Mean (Trung bình)</th><th>Median (Trung vị)</th><th>Range &amp; Standard Deviation (SD)</th></tr></thead>
      <tbody>
        <tr><td><b>Cộng cùng hằng số +c vào mọi số</b></td><td>Tăng thêm <code>+c</code></td><td>Tăng thêm <code>+c</code></td><td><b>KHÔNG ĐỔI!</b> (Khoảng cách giữa các điểm giữ nguyên)</td></tr>
        <tr><td><b>Nhân mọi số với k (k &gt; 0)</b></td><td>Nhân <code>k</code></td><td>Nhân <code>k</code></td><td>Nhân <code>k</code></td></tr>
        <tr><td><b>Xóa bỏ một Outlier cực lớn/cực nhỏ</b></td><td><b>Thay đổi mạnh</b> (bị kéo về phía còn lại)</td><td><b>Thay đổi rất ít hoặc không đổi</b></td><td><b>Giảm mạnh</b> (dữ liệu co cụm lại)</td></tr>
      </tbody>
    </table>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Stats Commands:</b> Gõ <code>L = [4, 7, 7, 10, 12]</code> rồi dùng ngay các lệnh tích hợp <code>mean(L)</code>, <code>median(L)</code>, <code>stdev(L)</code> (mẫu) hoặc <code>stdevp(L)</code> (tổng thể) để so sánh độ lệch chuẩn chính xác 100%!
    </div>
  </div>

  <div id="sec-prob" class="sat-card lecture-interactive-card" data-lecture-section="prob">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Xác suất có điều kiện (Two-Way Tables) &amp; Residuals trên Scatterplot</h2>
    <div class="sat-rule-box">
      <b>📌 Bẫy Mẫu số trong Xác suất có điều kiện (Conditional Probability):</b>
      <br>Đọc thật kỹ cụm từ <b>"If a [Group A] is selected at random..."</b> hoặc <b>"Given that the student chose [X]..."</b>!
      <br>• <b>Mẫu số (Denominator)</b> KHÔNG PHẢI là tổng toàn bảng (Grand Total), mà CHỈ là <b>tổng của đúng hàng/cột điều kiện</b> được nêu!
      <br>• <b>Residual (Phần dư trên Scatterplot):</b> <code>Residual = Observed (y thực tế) − Predicted (y trên đường hồi quy)</code>. Điểm nằm <b>trên</b> đường hồi quy → Residual <b>dương</b>; nằm <b>dưới</b> → Residual <b>âm</b>!
    </div>
  </div>

  <div id="sec-moe" class="sat-card lecture-interactive-card" data-lecture-section="moe">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Margin of Error &amp; Thiết kế Nghiên cứu (Random Selection vs Random Assignment)</h2>
    <div class="sat-gold-box">
      <b>⭐ 2 Quy tắc Vàng của Margin of Error (Sai số biên):</b>
      <br>1. <b>Khoảng giá trị hợp lý (Plausible Interval):</b> Nếu tỉ lệ mẫu là <code>62%</code> với margin of error <code>±4%</code>, ta kết luận: <i>"It is plausible that between 58% and 66% of the <b>sampled population</b>..."</i> (KHÔNG BAO GIỜ chọn câu khẳng định 100% chắc chắn "is definitely" hay "at least 62%"!).
      <br>2. <b>Tác động của Cỡ mẫu (Sample Size n):</b> Cỡ mẫu <code>n</code> càng <b>LỚN</b> → Margin of Error càng <b>NHỎ</b> (tỉ lệ nghịch với <code>√n</code>). Muốn giảm sai số biên đi một nửa, cần tăng cỡ mẫu lên <b>4 lần</b>!
    </div>
    <table class="sat-table">
      <thead><tr><th>Phương pháp lấy mẫu / thí nghiệm</th><th>Được phép suy rộng ra Tổng thể (Generalize)?</th><th>Được phép kết luận Nhân–Quả (Causation)?</th></tr></thead>
      <tbody>
        <tr><td><b>Random Selection (Chọn ngẫu nhiên từ quần thể X)</b></td><td>✅ <b>CÓ</b> — nhưng <b>CHỈ cho đúng quần thể X</b>! (VD: chọn trong trường A chỉ suy rộng cho trường A, không suy rộng cho toàn quốc)</td><td>❌ <b>KHÔNG</b> (Nếu chỉ khảo sát/quan sát)</td></tr>
        <tr><td><b>Random Assignment (Chia ngẫu nhiên vào nhóm điều trị &amp; đối chứng)</b></td><td>Phụ thuộc có Random Selection hay không</td><td>✅ <b>CÓ!</b> (Chỉ thí nghiệm có Random Assignment mới chứng minh được Cause-and-Effect!)</td></tr>
      </tbody>
    </table>
  </div>
'''
    m3_2_qc = make_quick_check_html(
        'qc_m3_2',
        'Tập dữ liệu A gồm 15 số có trung bình (mean) là 24 và độ lệch chuẩn (standard deviation) là 5.2. Tập dữ liệu B được tạo bằng cách cộng thêm 10 vào mỗi giá trị trong tập A. Khẳng định nào đúng về tập B?',
        'Data set A consists of 15 values with a mean of 24 and a standard deviation of 5.2. Data set B is formed by <b>adding 10 to each value</b> in data set A. Which statement is true about data set B?',
        ['Mean = 34 và SD = 15.2', 'Mean = 34 và SD = 5.2', 'Mean = 24 và SD = 5.2', 'Mean = 34 và SD = 10.4'],
        1,
        'Khi cộng cùng một hằng số (+10) vào TẤT CẢ các phần tử của tập dữ liệu, toàn bộ biểu đồ chỉ tịnh tiến sang phải 10 đơn vị: Mean và Median đều tăng thêm 10 (24 + 10 = 34), còn khoảng cách phân tán giữa các điểm giữ nguyên tuyệt đối nên Standard Deviation và Range KHÔNG ĐỔI (vẫn bằng 5.2)!'
    )
    m3_2_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 3 • PROBLEM-SOLVING & DATA',
        '3.2 Statistics, Probability, Margin of Error & Study Design',
        'Nắm trọn quy tắc biến đổi Mean/Median/SD, bẫy mẫu số xác suất có điều kiện, Margin of Error và phân biệt Random Selection với Random Assignment.',
        [
            'Dự đoán tức thì tác động của phép dịch (+c), co giãn (×k) và xóa Outlier lên Mean, Median, Range và Standard Deviation.',
            'Chốt chuẩn mẫu số xác suất có điều kiện từ bảng hai chiều và công thức Residual = Observed − Predicted.',
            'Nhận diện đúng phạm vi suy rộng tổng thể (Random Selection) và điều kiện kết luận nhân-quả (Random Assignment).',
        ],
        m3_2_cards,
        m3_2_qc
    )
    m3_2_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Thống kê, Xác suất & Thiết kế Nghiên cứu',
            'selector': '#sec-header',
            'en': 'Data analysis and statistics reward conceptual clarity over heavy calculation. On the Digital SAT, understanding how shifts affect standard deviation, how conditional probability restricts the denominator, and what random assignment proves will earn you fast, guaranteed points.',
            'vi': 'Phần Thống kê và Xác suất trên Digital SAT ưu tiên sự sắc bén về bản chất hơn là tính toán nặng. Chỉ cần hiểu rõ độ lệch chuẩn đổi ra sao khi cộng hằng số, mẫu số xác suất có điều kiện là gì và sự khác nhau giữa chọn mẫu ngẫu nhiên với phân nhóm ngẫu nhiên, bạn sẽ ăn trọn điểm mảng này rất nhanh.'
        },
        {
            'id': 'stats',
            'title': 'Mean, Median, SD & Quy tắc Dịch chuyển',
            'selector': '#sec-stats',
            'en': 'Standard deviation measures how spread out data points are from the mean. If you add a constant c to every data point, the mean and median both increase by c, while the range and standard deviation stay completely unchanged because the spacing between values did not change. Removing an extreme outlier pulls the mean sharply and lowers the standard deviation, while barely moving the median.',
            'vi': 'Độ lệch chuẩn đo mức độ phân tán của các số liệu quanh giá trị trung bình. Khi bạn cộng cùng một hằng số c vào mọi phần tử, cả mean và median đều tăng thêm c, nhưng range và độ lệch chuẩn hoàn toàn không đổi vì khoảng cách giữa các số giữ nguyên. Còn khi xóa bỏ một giá trị ngoại lai outlier, mean thay đổi mạnh và độ lệch chuẩn giảm mạnh, trong khi median hầu như ít đổi.'
        },
        {
            'id': 'prob',
            'title': 'Xác suất có điều kiện & Residuals',
            'selector': '#sec-prob',
            'en': 'In two-way probability tables, look for conditional phrasing like given that or if a member of group A is chosen at random. That condition shrinks your denominator from the grand total down to just that specific row or column total. On scatterplots, a residual equals the actual observed y value minus the line of best fit predicted y value.',
            'vi': 'Trong bảng xác suất hai chiều, hãy soi kỹ các cụm điều kiện như given that hoặc nếu chọn ngẫu nhiên một người trong nhóm A. Khi đó mẫu số không phải tổng toàn bảng mà thu gọn lại đúng tổng của hàng hoặc cột điều kiện đó. Trên biểu đồ phân tán, phần dư residual bằng giá trị thực tế trừ giá trị dự đoán trên đường xu hướng.'
        },
        {
            'id': 'moe',
            'title': 'Margin of Error & Random Selection vs Assignment',
            'selector': '#sec-moe',
            'en': 'A margin of error creates a range of plausible values for the sampled population, never a hundred-percent guarantee, and larger sample sizes produce smaller margins of error. Finally, remember the golden rule of study design: random selection allows you to generalize to that exact population, while only random assignment in an experiment allows you to claim cause and effect.',
            'vi': 'Sai số biên tạo ra một khoảng giá trị hợp lý plausible values cho đúng quần thể được lấy mẫu, tuyệt đối không phải khẳng định chắc chắn trăm phần trăm, và cỡ mẫu càng lớn thì sai số biên càng nhỏ. Cuối cùng, nhớ quy tắc vàng: chọn mẫu ngẫu nhiên cho phép suy rộng ra đúng quần thể đó, còn chỉ có phân nhóm ngẫu nhiên trong thí nghiệm mới được phép kết luận quan hệ nhân quả.'
        }
    ]
    lectures.append({
        'code': 'm3_2',
        'module_key': 'math_m3',
        'order_index': 2,
        'title': '3.2 Statistics, Probability, Margin of Error & Study Design',
        'drill_key': 'drill_m3_2',
        'html': m3_2_html,
        'segments': m3_2_segs,
        'major_sections': [
            {'title': 'Mean, Median & Standard Deviation', 'startSegmentId': 'stats'},
            {'title': 'Xác suất có điều kiện & Residuals', 'startSegmentId': 'prob'},
            {'title': 'Margin of Error & Study Design', 'startSegmentId': 'moe'},
        ],
    })

    return lectures
