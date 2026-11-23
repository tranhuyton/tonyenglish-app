# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — 2 Formula & Desmos Speed Games (100 Flashcards Total)
Matches the exact TonyEnglish Game Engine schema (`MCQ (Standard)` in sat_vocab_500.py):
  - Set 1 (sat_math_game_01, theme='vocab-racing', order_index=1):
      50 Formula & Desmos Speed Cards — Algebra & Advanced Math
  - Set 2 (sat_math_game_02, theme='ninja-survival', order_index=2):
      50 Formula & Concept Speed Cards — Geometry, Trigonometry & Data Analysis

All strings use crisp plain text & Unicode math symbols (NO LaTeX, NO HTML)
so VocabRacing.tsx and NinjaSurvival.tsx render them cleanly at high speed.
"""

import random


# Each card tuple: (prompt, correct_option, [trap1, trap2, trap3], explanation)
GAME_1_CARDS = [
    # --- 1. Linear Equations & Systems (12 cards) ---
    (
        'Công thức hệ số góc (Slope m) của đường thẳng đi qua (x₁, y₁) và (x₂, y₂)?',
        'm = (y₂ - y₁) / (x₂ - x₁)',
        [
            'm = (x₂ - x₁) / (y₂ - y₁)',
            'm = (y₂ + y₁) / (x₂ + x₁)',
            'm = (y₂ - x₂) / (y₁ - x₁)',
        ],
        'Slope = Rise / Run = Δy / Δx = (y₂ - y₁) / (x₂ - x₁).',
    ),
    (
        'Phương trình đường thẳng dạng Slope-Intercept chuẩn là gì?',
        'y = mx + b (m: hệ số góc, b: tung độ gốc)',
        [
            'y = bx + m (b: hệ số góc, m: hoành độ gốc)',
            'x = my + b (m: tung độ gốc, b: hệ số góc)',
            'y = m(x + b) (b luôn là giao điểm trục Ox)',
        ],
        'Trong y = mx + b: m là độ dốc (rate of change), b là giá trị y tại x = 0 (y-intercept).',
    ),
    (
        'Phương trình đường thẳng dạng Point-Slope đi qua (x₁, y₁) có độ dốc m?',
        'y - y₁ = m(x - x₁)',
        [
            'y + y₁ = m(x + x₁)',
            'x - x₁ = m(y - y₁)',
            'y - x₁ = m(x - y₁)',
        ],
        'Point-Slope Form: y - y₁ = m(x - x₁), cực nhanh khi đề cho 1 điểm và hệ số góc m.',
    ),
    (
        'Hệ số góc (slope) của đường thẳng dạng tổng quát Ax + By = C (B ≠ 0)?',
        'm = -A / B',
        [
            'm = A / B',
            'm = -B / A',
            'm = C / B',
        ],
        'Đưa Ax + By = C về y = (-A/B)x + C/B ⇒ hệ số góc m = -A/B.',
    ),
    (
        'Tung độ gốc (y-intercept) của đường thẳng Ax + By = C (B ≠ 0)?',
        'y = C / B',
        [
            'y = C / A',
            'y = -C / B',
            'y = -A / C',
        ],
        'Thay x = 0 vào Ax + By = C ⇒ By = C ⇒ y = C/B.',
    ),
    (
        'Hoành độ gốc (x-intercept) của đường thẳng Ax + By = C (A ≠ 0)?',
        'x = C / A',
        [
            'x = C / B',
            'x = -C / A',
            'x = A / C',
        ],
        'Thay y = 0 vào Ax + By = C ⇒ Ax = C ⇒ x = C/A.',
    ),
    (
        'Điều kiện để hai đường thẳng y = m₁x + b₁ và y = m₂x + b₂ SONG SONG?',
        'm₁ = m₂ và b₁ ≠ b₂',
        [
            'm₁ × m₂ = -1 và b₁ ≠ b₂',
            'm₁ = m₂ và b₁ = b₂',
            'm₁ = -m₂ và b₁ = b₂',
        ],
        'Song song (Parallel): cùng hệ số góc m₁ = m₂ nhưng khác tung độ gốc b₁ ≠ b₂ (0 giao điểm).',
    ),
    (
        'Quan hệ hệ số góc của hai đường thẳng VUÔNG GÓC (Perpendicular)?',
        'm₁ × m₂ = -1 (hay m₂ = -1/m₁)',
        [
            'm₁ × m₂ = 1 (hay m₂ = 1/m₁)',
            'm₁ + m₂ = 0 (hay m₂ = -m₁)',
            'm₁ = m₂',
        ],
        'Hai đường vuông góc có hệ số góc là số đối nghịch đảo của nhau: m₂ = -1/m₁.',
    ),
    (
        'Điều kiện hệ a₁x + b₁y = c₁ và a₂x + b₂y = c₂ VÔ NGHIỆM (No solution)?',
        'a₁/a₂ = b₁/b₂ ≠ c₁/c₂',
        [
            'a₁/a₂ = b₁/b₂ = c₁/c₂',
            'a₁/a₂ ≠ b₁/b₂',
            'a₁ × a₂ + b₁ × b₂ = 0',
        ],
        'Vô nghiệm ⇔ hai đường thẳng song song phân biệt: tỷ số hệ số x và y bằng nhau, nhưng khác tỷ số hằng số c.',
    ),
    (
        'Điều kiện hệ a₁x + b₁y = c₁ và a₂x + b₂y = c₂ có VÔ SỐ NGHIỆM?',
        'a₁/a₂ = b₁/b₂ = c₁/c₂',
        [
            'a₁/a₂ = b₁/b₂ ≠ c₁/c₂',
            'a₁/a₂ ≠ b₁/b₂ = c₁/c₂',
            'a₁ + a₂ = b₁ + b₂ = c₁ + c₂',
        ],
        'Vô số nghiệm (Infinite solutions) ⇔ hai phương trình trùng khít nhau: a₁/a₂ = b₁/b₂ = c₁/c₂.',
    ),
    (
        'Điều kiện hệ hai phương trình bậc nhất có DUY NHẤT 1 nghiệm (One solution)?',
        'a₁/a₂ ≠ b₁/b₂ (khác hệ số góc)',
        [
            'a₁/a₂ = b₁/b₂ ≠ c₁/c₂',
            'c₁/c₂ ≠ 1',
            'a₁/a₂ = b₁/b₂ = c₁/c₂',
        ],
        'Chỉ cần hai đường thẳng có hệ số góc khác nhau (a₁/a₂ ≠ b₁/b₂), chúng chắc chắn cắt nhau tại đúng 1 điểm.',
    ),
    (
        'Khi giải bất phương trình bậc nhất, dấu bất đẳng thức bị ĐỔI CHIỀU khi nào?',
        'Khi nhân hoặc chia cả 2 vế cho một số ÂM',
        [
            'Khi cộng hoặc trừ cả 2 vế cho một số âm',
            'Khi chuyển một hạng tử dương sang vế kia',
            'Khi chia cả 2 vế cho một phân số dương nhỏ hơn 1',
        ],
        'Cộng/trừ số âm giữ nguyên chiều; chỉ NHÂN hoặc CHIA hai vế cho số âm mới đảo chiều bất đẳng thức.',
    ),

    # --- 2. Quadratics, Vertex, Discriminant & Vieta (14 cards) ---
    (
        'Hoành độ đỉnh (Vertex x-coordinate) của parabol y = ax² + bx + c?',
        'x = -b / (2a)',
        [
            'x = b / (2a)',
            'x = -b / a',
            'x = -2b / a',
        ],
        'Trục đối xứng và hoành độ đỉnh của parabol chuẩn luôn là x = -b / (2a).',
    ),
    (
        'Phương trình parabol dạng đỉnh (Vertex Form) có đỉnh tại (h, k)?',
        'y = a(x - h)² + k',
        [
            'y = a(x + h)² + k',
            'y = a(x - k)² + h',
            'y = (x - h)² - k',
        ],
        'Chú ý dấu TRỪ trước h trong ngoặc: y = a(x - h)² + k có đỉnh (h, k).',
    ),
    (
        'Phương trình parabol dạng tích (Factored Form) có 2 nghiệm thực r₁, r₂?',
        'y = a(x - r₁)(x - r₂)',
        [
            'y = a(x + r₁)(x + r₂)',
            'y = (x - r₁)(x - r₂) + a',
            'y = a(x - r₁)² - r₂',
        ],
        'Biết 2 x-intercepts r₁, r₂ ⇒ viết ngay y = a(x - r₁)(x - r₂) rồi thay 1 điểm để tìm a.',
    ),
    (
        'Hoành độ đỉnh h của parabol khi biết hai nghiệm (x-intercepts) là r₁ và r₂?',
        'h = (r₁ + r₂) / 2',
        [
            'h = r₁ + r₂',
            'h = (r₁ - r₂) / 2',
            'h = √(r₁ × r₂)',
        ],
        'Do tính đối xứng của parabol, đỉnh nằm đúng giữa hai nghiệm: h = (r₁ + r₂) / 2.',
    ),
    (
        'Công thức nghiệm tổng quát (Quadratic Formula) của ax² + bx + c = 0?',
        'x = (-b ± √(b² - 4ac)) / (2a)',
        [
            'x = (b ± √(b² - 4ac)) / (2a)',
            'x = (-b ± √(b² + 4ac)) / (2a)',
            'x = (-b ± √(b² - 4ac)) / a',
        ],
        'Nhớ đủ 3 chi tiết: dấu -b, dấu trừ -4ac trong căn, và mẫu số 2a.',
    ),
    (
        'Biểu thức biệt thức (Discriminant Δ) của phương trình ax² + bx + c = 0?',
        'Δ = b² - 4ac',
        [
            'Δ = b² + 4ac',
            'Δ = 4ac - b²',
            'Δ = √(b² - 4ac) / (2a)',
        ],
        'Discriminant Δ = b² - 4ac là phần biểu thức bên trong dấu căn của công thức nghiệm.',
    ),
    (
        'Điều kiện để ax² + bx + c = 0 có 2 NGHIỆM THỰC PHÂN BIỆT?',
        'b² - 4ac > 0',
        [
            'b² - 4ac = 0',
            'b² - 4ac < 0',
            'b² - 4ac ≥ 0',
        ],
        'Δ > 0 ⇒ ±√Δ tạo ra 2 giá trị thực phân biệt (parabol cắt trục Ox tại 2 điểm).',
    ),
    (
        'Điều kiện để ax² + bx + c = 0 có ĐÚNG 1 NGHIỆM THỰC (nghiệm kép)?',
        'b² - 4ac = 0',
        [
            'b² - 4ac > 0',
            'b² - 4ac < 0',
            'b = 0',
        ],
        'Δ = b² - 4ac = 0 ⇒ nghiệm kép x = -b/(2a), đỉnh parabol tiếp xúc trục Ox.',
    ),
    (
        'Điều kiện để ax² + bx + c = 0 KHÔNG CÓ NGHIỆM THỰC (No real solutions)?',
        'b² - 4ac < 0',
        [
            'b² - 4ac = 0',
            'b² - 4ac > 0',
            'a < 0 và c < 0',
        ],
        'Δ = b² - 4ac < 0 ⇒ biểu thức dưới căn bậc hai âm, không có nghiệm thực.',
    ),
    (
        'Định lý Viète: TỔNG hai nghiệm x₁ + x₂ của ax² + bx + c = 0?',
        'x₁ + x₂ = -b / a',
        [
            'x₁ + x₂ = b / a',
            'x₁ + x₂ = c / a',
            'x₁ + x₂ = -b / (2a)',
        ],
        'Tổng nghiệm = -b/a (gấp đôi hoành độ đỉnh -b/(2a)). Rất hay ra trên SAT Hard M2!',
    ),
    (
        'Định lý Viète: TÍCH hai nghiệm x₁ × x₂ của ax² + bx + c = 0?',
        'x₁ × x₂ = c / a',
        [
            'x₁ × x₂ = -c / a',
            'x₁ × x₂ = -b / a',
            'x₁ × x₂ = c / (2a)',
        ],
        'Tích hai nghiệm của ax² + bx + c = 0 luôn bằng c/a (nhớ chia cho hệ số a!).',
    ),
    (
        'Để hoàn thành bình phương (Completing the Square) cho x² + bx, cần cộng thêm số nào?',
        '(b / 2)²',
        [
            'b² / 2',
            '2b²',
            '(b / 4)²',
        ],
        'x² + bx + (b/2)² = (x + b/2)². Chia đôi hệ số b rồi bình phương!',
    ),
    (
        'Parabol y = ax² + bx + c đạt GIÁ TRỊ LỚN NHẤT (Maximum) tại đỉnh khi nào?',
        'a < 0 (bề lõm hướng xuống)',
        [
            'a > 0 (bề lõm hướng lên)',
            'c > 0',
            'b < 0',
        ],
        'a < 0 ⇒ parabol úp xuống, đỉnh là Maximum; a > 0 ⇒ parabol ngửa lên, đỉnh là Minimum.',
    ),
    (
        'Điều kiện để đường thẳng y = mx + k TIẾP XÚC với parabol y = ax² + bx + c (đúng 1 giao điểm)?',
        'Đưa về phương trình bậc hai = 0 rồi giải Δ = b² - 4ac = 0',
        [
            'Đặt hệ số góc m = a',
            'Giải phương trình Δ = b² - 4ac > 0',
            'Đặt tung độ gốc k = c',
        ],
        'Tiếp xúc (tangent) ⇔ phương trình ax² + (b - m)x + (c - k) = 0 có đúng 1 nghiệm ⇔ Δ = 0.',
    ),

    # --- 3. Exponents, Radicals & Exponentials (9 cards) ---
    (
        'Quy tắc nhân hai lũy thừa cùng cơ số: aᵐ × aⁿ = ?',
        'a^(m + n)',
        [
            'a^(m × n)',
            'a^(m - n)',
            '(2a)^(m + n)',
        ],
        'Nhân cùng cơ số → giữ nguyên cơ số và CỘNG số mũ: aᵐ × aⁿ = a^(m + n).',
    ),
    (
        'Quy tắc lũy thừa của lũy thừa: (aᵐ)ⁿ = ?',
        'a^(m × n)',
        [
            'a^(m + n)',
            'a^(mⁿ)',
            'a^(m / n)',
        ],
        'Lũy thừa chồng lũy thừa (aᵐ)ⁿ = a^(m × n) (NHÂN hai số mũ).',
    ),
    (
        'Giá trị của lũy thừa số mũ âm a⁻ⁿ (với a ≠ 0) bằng gì?',
        '1 / aⁿ',
        [
            '-aⁿ',
            '-1 / aⁿ',
            'a^(1/n)',
        ],
        'Số mũ âm nghĩa là lấy NGHỊCH ĐẢO cơ số, KHÔNG tạo dấu âm phía trước: a⁻ⁿ = 1/aⁿ.',
    ),
    (
        'Đổi lũy thừa số mũ phân số a^(m/n) sang dạng căn thức (với a > 0)?',
        'ⁿ√(aᵐ) = (ⁿ√a)ᵐ',
        [
            'ᵐ√(aⁿ)',
            'aᵐ / n',
            '(a / n)ᵐ',
        ],
        'Tử số m là số mũ (power), mẫu số n là bậc căn (root): a^(m/n) = ⁿ√(aᵐ).',
    ),
    (
        'Mô hình hàm mũ TĂNG trưởng p% sau mỗi chu kỳ t từ giá trị đầu a?',
        'f(t) = a(1 + p/100)^t',
        [
            'f(t) = a(p/100)^t',
            'f(t) = a + (p/100)t',
            'f(t) = a(1 + p)^t',
        ],
        'Tăng p% mỗi chu kỳ ⇒ nhân hệ số (1 + p/100) sau mỗi đơn vị thời gian t.',
    ),
    (
        'Mô hình hàm mũ SUY GIẢM p% sau mỗi chu kỳ t từ giá trị đầu a?',
        'f(t) = a(1 - p/100)^t',
        [
            'f(t) = a(p/100)^t',
            'f(t) = a(1 + p/100)^(-t)',
            'f(t) = a - (p/100)^t',
        ],
        'Giảm p% mỗi chu kỳ ⇒ còn lại (1 - p/100) sau mỗi bước: f(t) = a(1 - p/100)^t.',
    ),
    (
        'Mô hình dân số tăng GẤP ĐÔI sau mỗi chu kỳ d năm (Doubling Time)?',
        'P(t) = P₀ × 2^(t / d)',
        [
            'P(t) = P₀ × 2^(d × t)',
            'P(t) = P₀ × 2^(d / t)',
            'P(t) = P₀ × d^(t / 2)',
        ],
        'Sau t năm trải qua t/d chu kỳ gấp đôi ⇒ P(t) = P₀ × 2^(t/d).',
    ),
    (
        'Mô hình bán rã phóng xạ (Half-Life): giảm một nửa sau mỗi chu kỳ h năm?',
        'A(t) = A₀ × (1/2)^(t / h)',
        [
            'A(t) = A₀ × (1/2)^(h / t)',
            'A(t) = A₀ × (1/2)^(h × t)',
            'A(t) = A₀ × (1 - t/(2h))',
        ],
        'Mỗi h năm nhân 1/2 ⇒ sau t năm có t/h chu kỳ bán rã: A(t) = A₀ × (1/2)^(t/h).',
    ),
    (
        'Ý nghĩa của a và b trong hàm mũ y = a × bˣ (với a > 0, b > 0)?',
        'a là giá trị ban đầu y(0); b là hệ số nhân mỗi khi x tăng 1',
        [
            'a là tốc độ tăng hằng số; b là giá trị ban đầu y(0)',
            'a là hoành độ gốc; b là phần trăm tăng trưởng',
            'a là giá trị tại x = 1; b là giá trị tại x = 0',
        ],
        'Tại x = 0: y = a × b⁰ = a (initial value); khi x tăng 1, y nhân thêm b (growth/decay factor).',
    ),

    # --- 4. Polynomials, Factoring & Functions (9 cards) ---
    (
        'Khai triển hằng đẳng thức hiệu hai bình phương (Difference of Squares): a² - b² = ?',
        '(a - b)(a + b)',
        [
            '(a - b)²',
            'a² - 2ab + b²',
            '(a + b)² - 2ab',
        ],
        'a² - b² = (a - b)(a + b) — hằng đẳng thức xuất hiện nhiều nhất trong SAT Math!',
    ),
    (
        'Khai triển đúng của bình phương một hiệu (a - b)² = ?',
        'a² - 2ab + b²',
        [
            'a² - b²',
            'a² + 2ab - b²',
            'a² - ab + b²',
        ],
        'Cẩn thận bẫy bỏ quên -2ab: (a - b)² = a² - 2ab + b².',
    ),
    (
        'Định lý số dư (Remainder Theorem): Số dư khi chia đa thức P(x) cho (x - c) bằng gì?',
        'P(c)',
        [
            'P(-c)',
            'P(0) - c',
            'c × P(1)',
        ],
        'Remainder Theorem: Chia P(x) cho (x - c) luôn cho số dư bằng P(c) (chia cho x + c cho số dư P(-c)).',
    ),
    (
        'Định lý nhân tử (Factor Theorem): (x - c) là một nhân tử của đa thức P(x) khi nào?',
        'Khi và chỉ khi P(c) = 0',
        [
            'Khi và chỉ khi P(-c) = 0',
            'Khi và chỉ khi P(0) = c',
            'Khi và chỉ khi P(c) = 1',
        ],
        'P(c) = 0 ⇔ x = c là nghiệm (x-intercept) ⇔ (x - c) chia hết P(x).',
    ),
    (
        'Đồ thị y = f(x - h) + k (với h > 0, k > 0) dịch chuyển thế nào so với y = f(x)?',
        'Sang PHẢI h đơn vị và LÊN TRÊN k đơn vị',
        [
            'Sang TRÁI h đơn vị và LÊN TRÊN k đơn vị',
            'Sang PHẢI h đơn vị và XUỐNG DƯỚI k đơn vị',
            'Sang TRÁI h đơn vị và XUỐNG DƯỚI k đơn vị',
        ],
        'Trong ngoặc ngược dấu (x - h dịch PHẢI h); ngoài ngoặc thuận dấu (+k dịch LÊN k).',
    ),
    (
        'Đồ thị y = -f(x) thu được từ đồ thị y = f(x) bằng phép biến hình nào?',
        'Đối xứng qua trục hoành Ox (lật trên-dưới)',
        [
            'Đối xứng qua trục tung Oy (lật trái-phải)',
            'Dịch chuyển xuống dưới 1 đơn vị',
            'Quay 90° ngược chiều kim đồng hồ',
        ],
        'Đổi dấu y thành -y giữ nguyên x ⇒ lật đối xứng qua trục Ox.',
    ),
    (
        'Đồ thị y = f(-x) thu được từ đồ thị y = f(x) bằng phép biến hình nào?',
        'Đối xứng qua trục tung Oy (lật trái-phải)',
        [
            'Đối xứng qua trục hoành Ox (lật trên-dưới)',
            'Dịch chuyển sang trái 1 đơn vị',
            'Không thay đổi hình dạng với mọi hàm',
        ],
        'Đổi dấu x thành -x giữ nguyên y ⇒ lật đối xứng qua trục tung Oy.',
    ),
    (
        'Phương trình giá trị tuyệt đối |ax + b| = c (với c > 0) tương đương với gì?',
        'ax + b = c hoặc ax + b = -c',
        [
            'ax + b = c (chỉ có 1 nghiệm)',
            'ax - b = c hoặc ax + b = c',
            'Vô nghiệm vì dấu giá trị tuyệt đối',
        ],
        'Với c > 0, |U| = c tách thành 2 trường hợp U = c và U = -c (còn nếu c < 0 thì vô nghiệm ngay!).',
    ),
    (
        'Bẫy bắt buộc phải kiểm tra khi giải phương trình chứa căn thức √A = B là gì?',
        'Thử lại nghiệm vào phương trình gốc để loại nghiệm ngoại lai (B phải ≥ 0)',
        [
            'Chỉ nhận nghiệm nguyên dương',
            'Luôn cộng thêm ± vào cả hai vế sau khi bình phương',
            'Bỏ qua điều kiện của vế phải B',
        ],
        'Bình phương hai vế có thể sinh nghiệm ngoại lai làm vế phải B < 0 (mà √A luôn ≥ 0).',
    ),

    # --- 5. Desmos 800 Speed Syntax (6 cards) ---
    (
        'Trên máy tính Desmos tích hợp Bluebook, ký hiệu nào dùng để chạy hồi quy (Regression) tìm hằng số?',
        'Dấu ngã ~ (tilde)',
        [
            'Dấu bằng kép ==',
            'Dấu mũi tên ->',
            'Dấu phần trăm %',
        ],
        'Desmos dùng dấu ~ (ví dụ y1 ~ m x1 + b) để giải tự động các tham số chưa biết chỉ trong 2 giây.',
    ),
    (
        'Cú pháp Desmos chuẩn để tìm đường thẳng đi qua các điểm trong bảng (x₁, y₁)?',
        'y1 ~ m x1 + b',
        [
            'y = m x + b',
            'y1 = m x1 + b',
            'x1 ~ m y1 + b',
        ],
        'Gõ bảng x1, y1 rồi nhập y1 ~ m x1 + b ⇒ Desmos tự xuất chính xác m, b và hệ số R².',
    ),
    (
        'Cú pháp Desmos chuẩn để tìm hàm bậc hai (parabol) khớp 3 điểm trong bảng (x₁, y₁)?',
        'y1 ~ a x1² + b x1 + c',
        [
            'y ~ a x² + b x + c',
            'y1 = a x1² + b x1 + c',
            'y1 ~ a (x1 + b)²',
        ],
        'Chỉ cần nhập 3 điểm vào bảng x1, y1 và gõ y1 ~ a x1² + b x1 + c để tìm a, b, c ngay lập tức.',
    ),
    (
        'Cú pháp Desmos chuẩn để tìm hàm mũ từ bảng số liệu (x₁, y₁)?',
        'y1 ~ a · b^(x1)',
        [
            'y1 ~ a · x1^b',
            'y1 = a · b^x',
            'y1 ~ a + b^(x1)',
        ],
        'Hàm mũ có biến ở số mũ: y1 ~ a · b^(x1) (nhớ tick Log Mode nếu cần khớp bài toán textbook).',
    ),
    (
        'Cách giải siêu tốc phương trình phức tạp f(x) = g(x) bằng Desmos trong phòng thi?',
        'Vẽ y = f(x) và y = g(x), bấm vào giao điểm để đọc giá trị x',
        [
            'Chỉ nhập f(x) + g(x) rồi đọc tung độ gốc',
            'Chuyển hết sang bảng x1 rồi dùng mean(x1)',
            'Chỉ nhìn giá trị y tại giao điểm và bỏ qua x',
        ],
        'Hoành độ x của giao điểm hai đồ thị y = f(x) và y = g(x) chính là nghiệm thực của f(x) = g(x).',
    ),
    (
        'Mẹo Desmos 800 tìm tham số k để hai biểu thức đa thức đồng nhất (equivalent) với mọi x?',
        'Đặt danh sách x1 = [1, 2, 3, 4] rồi gõ hồi quy VeTrai(x1) ~ VePhai(x1)',
        [
            'Thay duy nhất x = 0 vào một vế',
            'Đặt k = 0 rồi tìm x-intercept',
            'Vẽ hai đồ thị mà không thêm thanh trượt (slider)',
        ],
        'Khi x1 là danh sách nhiều giá trị, phép hồi quy ~ ép Desmos tìm đúng tham số k làm hai vế bằng nhau với mọi x!',
    ),
]


GAME_2_CARDS = [
    # --- 1. Angles, Triangles & Polygons (7 cards) ---
    (
        'Công thức tổng số đo các góc trong của một đa giác lồi n cạnh?',
        '(n - 2) × 180°',
        [
            'n × 180°',
            '(n - 1) × 180°',
            '(n - 2) × 360°',
        ],
        'Mọi đa giác n cạnh chia được thành (n - 2) tam giác ⇒ tổng góc trong = (n - 2) × 180°.',
    ),
    (
        'Số đo MỖI góc trong của một đa giác ĐỀU (Regular Polygon) n cạnh?',
        '(n - 2) × 180° / n',
        [
            '360° / n',
            '(n - 2) × 360° / n',
            '180° / (n - 2)',
        ],
        'Lấy tổng góc trong (n - 2) × 180° chia đều cho n đỉnh (còn 360°/n là góc NGOÀI của đa giác đều!).',
    ),
    (
        'Định lý góc ngoài tam giác (Exterior Angle Theorem) phát biểu gì?',
        'Góc ngoài bằng TỔNG 2 góc trong không kề với nó',
        [
            'Góc ngoài bằng 180° trừ tổng 2 góc trong không kề',
            'Góc ngoài bằng hiệu 2 góc trong không kề',
            'Góc ngoài luôn bằng góc trong kề với nó',
        ],
        'Góc ngoài tại một đỉnh = tổng hai góc trong ở hai đỉnh còn lại (rút ngắn 2 bước trừ 180°).',
    ),
    (
        'Bất đẳng thức tam giác cho độ dài cạnh thứ ba c khi biết hai cạnh a và b?',
        '|a - b| < c < a + b',
        [
            '|a - b| ≤ c ≤ a + b',
            '0 < c < a × b',
            'a + b < c < 2(a + b)',
        ],
        'Cạnh thứ ba luôn lớn hơn ngặt hiệu hai cạnh kia và nhỏ hơn ngặt tổng hai cạnh kia.',
    ),
    (
        'Hai tam giác ĐỒNG DẠNG (Similar Triangles) có tính chất cốt lõi nào?',
        'Các góc tương ứng BẰNG NHAU và các cạnh tương ứng TỶ LỆ với nhau',
        [
            'Diện tích luôn bằng nhau',
            'Các cạnh tương ứng bằng nhau tuyệt đối',
            'Chu vi luôn bằng nhau nhưng góc có thể khác nhau',
        ],
        'Đồng dạng (AA, SAS, SSS): góc bằng nhau, tỷ số cạnh bằng k, tỷ số diện tích bằng k².',
    ),
    (
        'Khi một đường cắt (transversal) cắt hai đường song song, các cặp góc nào BẰNG NHAU?',
        'Đồng vị (Corresponding) và So le trong (Alternate Interior)',
        [
            'Hai góc trong cùng phía (Consecutive Interior)',
            'Hai góc kề bù bất kỳ',
            'Chỉ có hai góc vuông mới bằng nhau',
        ],
        'Đồng vị & So le trong bằng nhau; còn hai góc trong cùng phía bù nhau (tổng = 180°).',
    ),
    (
        'Đoạn thẳng nối trung điểm hai cạnh của tam giác (Midsegment) có tính chất gì?',
        'Song song cạnh thứ 3 và dài bằng 1/2 cạnh thứ 3',
        [
            'Vuông góc cạnh thứ 3 và dài bằng 1/2 cạnh thứ 3',
            'Song song cạnh thứ 3 và chia diện tích thành hai phần bằng nhau',
            'Dài bằng 1/3 cạnh thứ 3',
        ],
        'Đường trung bình song song đáy, dài bằng 1/2 đáy (và cắt ra tam giác nhỏ có diện tích bằng 1/4 tam giác lớn).',
    ),

    # --- 2. Special Right Triangles & Coordinate Geometry (7 cards) ---
    (
        'Tỷ lệ độ dài 3 cạnh của tam giác vuông đặc biệt 30°-60°-90°?',
        'x : x√3 : 2x',
        [
            'x : x : x√2',
            'x : 2x : 3x',
            'x : x√2 : 2x',
        ],
        'Đối diện 30° là x; đối diện 60° là x√3; cạnh huyền đối diện 90° là 2x.',
    ),
    (
        'Tỷ lệ độ dài 3 cạnh của tam giác vuông cân 45°-45°-90°?',
        'x : x : x√2',
        [
            'x : x√3 : 2x',
            'x : x : 2x',
            'x : 2x : x√5',
        ],
        'Hai cạnh góc vuông bằng nhau (x, x), cạnh huyền dài x√2 (cũng là đường chéo hình vuông cạnh x).',
    ),
    (
        'Bốn bộ ba số Pitago (Pythagorean Triples) kinh điển phải thuộc lòng cho SAT 800?',
        '3-4-5, 5-12-13, 7-24-25, 8-15-17',
        [
            '2-3-4, 4-5-6, 6-7-8, 8-9-10',
            '3-4-5, 5-10-12, 7-14-15, 8-12-16',
            '3-5-7, 5-12-15, 7-24-26, 9-12-16',
        ],
        'Thuộc 4 bộ gốc (và các bội như 6-8-10, 9-12-15, 10-24-26) giúp giải tam giác vuông trong 3 giây!',
    ),
    (
        'Độ dài đường cao h của một tam giác ĐỀU (Equilateral Triangle) cạnh s?',
        'h = (s√3) / 2',
        [
            'h = (s√2) / 2',
            'h = s / 2',
            'h = (s²√3) / 4',
        ],
        'Đường cao chia tam giác đều thành 2 tam giác 30°-60°-90° ⇒ h = (s√3)/2.',
    ),
    (
        'Công thức diện tích của một tam giác ĐỀU cạnh s?',
        'Area = (s²√3) / 4',
        [
            'Area = (s²√3) / 2',
            'Area = (s√3) / 4',
            'Area = s² / 2',
        ],
        'A = (1/2) × đáy × cao = (1/2) × s × (s√3/2) = (s²√3)/4.',
    ),
    (
        'Công thức khoảng cách (Distance Formula) giữa hai điểm (x₁, y₁) và (x₂, y₂)?',
        'd = √((x₂ - x₁)² + (y₂ - y₁)²)',
        [
            'd = √((x₂ + x₁)² + (y₂ + y₁)²)',
            'd = √((x₂ - x₁)² - (y₂ - y₁)²)',
            'd = (x₂ - x₁)² + (y₂ - y₁)²',
        ],
        'Bản chất là định lý Pitago: d = √(Δx² + Δy²). Nhớ lấy căn bậc hai!',
    ),
    (
        'Công thức tọa độ trung điểm (Midpoint) của đoạn nối (x₁, y₁) và (x₂, y₂)?',
        'M = ((x₁ + x₂)/2, (y₁ + y₂)/2)',
        [
            'M = ((x₂ - x₁)/2, (y₂ - y₁)/2)',
            'M = (x₁ + x₂, y₁ + y₂)',
            'M = ((x₁ + y₁)/2, (x₂ + y₂)/2)',
        ],
        'Trung điểm là trung bình cộng hoành độ và trung bình cộng tung độ.',
    ),

    # --- 3. Circles, Arcs & Radians (9 cards) ---
    (
        'Phương trình chuẩn (Standard Form) của đường tròn tâm (h, k), bán kính r?',
        '(x - h)² + (y - k)² = r²',
        [
            '(x + h)² + (y + k)² = r²',
            '(x - h)² + (y - k)² = r',
            '(x - h)² - (y - k)² = r²',
        ],
        'Đổi dấu trong ngoặc để đọc tâm (h, k), và lấy CĂN vế phải để ra bán kính r!',
    ),
    (
        'Tọa độ tâm của đường tròn có phương trình khai triển x² + y² + Dx + Ey + F = 0?',
        '(-D/2, -E/2)',
        [
            '(D/2, E/2)',
            '(-D, -E)',
            '(D, E)',
        ],
        'Chia hệ số x và y cho -2 để đọc nhanh tọa độ tâm trong 2 giây!',
    ),
    (
        'Từ x² + Dx + y² + Ey = C, công thức tính nhanh r² (Completing the Square)?',
        'r² = C + (D/2)² + (E/2)²',
        [
            'r² = C - (D/2)² - (E/2)²',
            'r² = C + D² + E²',
            'r = C + (D/2)² + (E/2)²',
        ],
        'Khi thêm (D/2)² và (E/2)² vào vế trái để tạo bình phương, phải cộng đúng lượng đó vào vế phải C.',
    ),
    (
        'Hệ thức quy đổi cốt lõi giữa Radian và Độ (Radians ↔ Degrees)?',
        'π rad = 180° (nên 2π rad = 360°)',
        [
            'π rad = 360° (nên 2π rad = 720°)',
            'π rad = 90°',
            '1 rad = 180°',
        ],
        'Đổi Độ → Radian: nhân π/180°; đổi Radian → Độ: thay π bằng 180°.',
    ),
    (
        'Công thức độ dài cung tròn (Arc Length) ứng với góc ở tâm θ tính theo ĐỘ?',
        's = (θ / 360°) × 2πr',
        [
            's = (θ / 180°) × 2πr',
            's = (θ / 360°) × πr²',
            's = θ × r',
        ],
        'Độ dài cung là phần tỷ lệ (θ/360°) của toàn bộ chu vi đường tròn 2πr.',
    ),
    (
        'Công thức độ dài cung tròn (Arc Length) ứng với góc ở tâm θ tính theo RADIAN?',
        's = r × θ',
        [
            's = (1/2)r²θ',
            's = 2πrθ',
            's = r / θ',
        ],
        'Khi góc θ đã ở đơn vị Radian, độ dài cung rút gọn siêu đẹp thành s = rθ!',
    ),
    (
        'Công thức diện tích hình quạt tròn (Sector Area) với góc ở tâm θ tính theo ĐỘ?',
        'A = (θ / 360°) × πr²',
        [
            'A = (θ / 360°) × 2πr',
            'A = (θ / 180°) × πr²',
            'A = (1/2)r²θ',
        ],
        'Diện tích hình quạt bằng tỷ lệ góc (θ/360°) nhân diện tích cả hình tròn πr².',
    ),
    (
        'Công thức diện tích hình quạt tròn (Sector Area) với góc ở tâm θ tính theo RADIAN?',
        'A = (1/2)r²θ',
        [
            'A = r²θ',
            'A = r × θ',
            'A = (1/2)πr²θ',
        ],
        'Từ (θ / 2π) × πr² rút gọn π ta có ngay A = (1/2)r²θ.',
    ),
    (
        'Quan hệ giữa góc nội tiếp (Inscribed Angle) và góc ở tâm cùng chắn một cung (và tính chất tiếp tuyến)?',
        'Góc nội tiếp = (1/2) góc ở tâm; tiếp tuyến luôn vuông góc bán kính',
        [
            'Góc nội tiếp = 2 × góc ở tâm; tiếp tuyến song song bán kính',
            'Góc nội tiếp = góc ở tâm; tiếp tuyến tạo góc 45° với bán kính',
            'Góc nội tiếp + góc ở tâm = 180°',
        ],
        'Góc nội tiếp bằng nửa góc ở tâm cùng chắn cung (đặc biệt chắn nửa đường tròn = 90°); tiếp tuyến ⊥ bán kính tại tiếp điểm.',
    ),

    # --- 4. 3D Volumes, Surface Area & Scaling k / k² / k³ (8 cards) ---
    (
        'Công thức thể tích hình trụ tròn (Right Circular Cylinder) bán kính r, cao h?',
        'V = πr²h',
        [
            'V = (1/3)πr²h',
            'V = 2πrh',
            'V = 2πr²h',
        ],
        'Thể tích lăng trụ/hình trụ luôn bằng Diện tích đáy × Chiều cao = πr²h.',
    ),
    (
        'Công thức thể tích hình nón (Right Circular Cone) bán kính r, cao h?',
        'V = (1/3)πr²h',
        [
            'V = πr²h',
            'V = (1/2)πr²h',
            'V = (4/3)πr²h',
        ],
        'Hình nón có thể tích bằng đúng 1/3 thể tích hình trụ cùng đáy và cùng chiều cao.',
    ),
    (
        'Công thức thể tích hình cầu (Sphere) có bán kính r?',
        'V = (4/3)πr³',
        [
            'V = 4πr²',
            'V = (4/3)πr²',
            'V = (1/3)πr³',
        ],
        'Thể tích hình cầu là (4/3)πr³ (còn 4πr² là diện tích mặt cầu!).',
    ),
    (
        'Công thức thể tích hình chóp (Pyramid) có diện tích đáy B và chiều cao h?',
        'V = (1/3)Bh',
        [
            'V = (1/2)Bh',
            'V = Bh',
            'V = (2/3)Bh',
        ],
        'Mọi hình chóp (đáy tam giác, hình chữ nhật hay đa giác) đều có V = (1/3) × B × h.',
    ),
    (
        'Công thức diện tích toàn phần (Surface Area) của hình lập phương cạnh s?',
        'SA = 6s²',
        [
            'SA = s³',
            'SA = 4s²',
            'SA = 12s',
        ],
        'Hình lập phương có 6 mặt vuông bằng nhau, mỗi mặt diện tích s² ⇒ SA = 6s².',
    ),
    (
        'Khi hai hình đồng dạng có tỷ số cạnh (Linear Scale Factor) bằng k, tỷ số DIỆN TÍCH là?',
        'k²',
        [
            'k',
            '2k',
            'k³',
        ],
        'Chiều dài tăng k lần ⇒ Diện tích (2D) tăng k² lần!',
    ),
    (
        'Khi hai khối đồng dạng có tỷ số cạnh bằng k, tỷ số THỂ TÍCH là?',
        'k³',
        [
            'k²',
            '3k',
            'k',
        ],
        'Chiều dài tăng k lần ⇒ Diện tích tăng k² lần ⇒ Thể tích (3D) tăng k³ lần!',
    ),
    (
        'Độ dài đường chéo không gian (Space Diagonal) của hình hộp chữ nhật kích thước l × w × h?',
        'd = √(l² + w² + h²)',
        [
            'd = l + w + h',
            'd = √(l² + w²) + h',
            'd = ∛(l² + w² + h²)',
        ],
        'Áp dụng định lý Pitago hai lần liên tiếp cho ra d = √(l² + w² + h²).',
    ),

    # --- 5. Trigonometry (7 cards) ---
    (
        'Quy tắc lượng giác SOH-CAH-TOA trong tam giác vuông?',
        'sin = Đối/Huyền, cos = Kề/Huyền, tan = Đối/Kề',
        [
            'sin = Kề/Huyền, cos = Đối/Huyền, tan = Kề/Đối',
            'sin = Đối/Kề, cos = Kề/Huyền, tan = Đối/Huyền',
            'sin = Huyền/Đối, cos = Huyền/Kề, tan = Đối/Kề',
        ],
        'SOH (Sin = Opposite/Hypotenuse), CAH (Cos = Adjacent/Hypotenuse), TOA (Tan = Opposite/Adjacent).',
    ),
    (
        'Đẳng thức góc phụ nhau (Complementary Angle Identity) hay thi nhất trên Digital SAT?',
        'sin(x) = cos(90° - x) (hay sin(x) = cos(π/2 - x))',
        [
            'sin(x) = cos(180° - x)',
            'sin(x) = -cos(90° - x)',
            'tan(x) = cos(90° - x)',
        ],
        'Trong tam giác vuông, hai góc nhọn cộng lại bằng 90° nên sin góc này luôn bằng cos góc kia!',
    ),
    (
        'Hằng đẳng thức Pitago lượng giác cơ bản đúng với mọi góc x?',
        'sin²(x) + cos²(x) = 1',
        [
            'sin(x) + cos(x) = 1',
            'sin²(x) - cos²(x) = 1',
            'tan²(x) + cos²(x) = 1',
        ],
        'Từ a² + b² = c² chia cả hai vế cho c² ⇒ sin²(x) + cos²(x) = 1.',
    ),
    (
        'Biểu diễn tan(x) theo sin(x) và cos(x)?',
        'tan(x) = sin(x) / cos(x)',
        [
            'tan(x) = cos(x) / sin(x)',
            'tan(x) = sin(x) × cos(x)',
            'tan(x) = 1 / cos(x)',
        ],
        'tan(x) = (Đối/Huyền) / (Kề/Huyền) = sin(x) / cos(x).',
    ),
    (
        'Giá trị lượng giác chính xác của sin(30°) và cos(60°)?',
        '1/2 (= 0.5)',
        [
            '√3 / 2',
            '√2 / 2',
            '√3 / 3',
        ],
        'Trong tam giác 30°-60°-90° (1 : √3 : 2), sin(30°) = cos(60°) = 1/2.',
    ),
    (
        'Giá trị lượng giác chính xác của sin(60°) và cos(30°)?',
        '√3 / 2',
        [
            '1/2',
            '√2 / 2',
            '√3',
        ],
        'Trong tam giác 30°-60°-90° (1 : √3 : 2), sin(60°) = cos(30°) = √3 / 2.',
    ),
    (
        'Giá trị lượng giác chính xác của sin(45°) và cos(45°)?',
        '√2 / 2 (và tan(45°) = 1)',
        [
            '1/2 (và tan(45°) = √2)',
            '√3 / 2 (và tan(45°) = 1)',
            '1 (và tan(45°) = √2 / 2)',
        ],
        'Tam giác 45°-45°-90° (1 : 1 : √2) ⇒ sin(45°) = cos(45°) = 1/√2 = √2 / 2, tan(45°) = 1.',
    ),

    # --- 6. Ratios, Units, Statistics, Probability, Margin of Error & Study Design (12 cards) ---
    (
        'Bẫy đổi đơn vị diện tích và thể tích (VD: ft² → yd² hay in³ → ft³) phải xử lý thế nào?',
        'Bình phương hệ số cho diện tích (k²); lập phương hệ số cho thể tích (k³)',
        [
            'Dùng nguyên hệ số độ dài k cho cả diện tích và thể tích',
            'Nhân đôi hệ số (2k) cho diện tích và nhân ba (3k) cho thể tích',
            'Lấy căn bậc hai hệ số k cho diện tích',
        ],
        '1 yd = 3 ft ⇒ 1 yd² = 9 ft²; 1 ft = 12 in ⇒ 1 ft³ = 1,728 in³.',
    ),
    (
        'Công thức vận tốc trung bình chuẩn (và trường hợp đặc biệt 2 chặng bằng nhau)?',
        'Tổng quãng đường / Tổng thời gian (bằng 2v₁v₂/(v₁+v₂) khi d₁ = d₂)',
        [
            'Luôn lấy trung bình cộng (v₁ + v₂) / 2',
            'Tổng thời gian / Tổng quãng đường',
            '√(v₁ × v₂) với mọi quãng đường',
        ],
        'Vận tốc trung bình KHÔNG phải (v₁ + v₂)/2 khi đi cùng quãng đường; luôn dùng Total Distance / Total Time.',
    ),
    (
        'Công thức Percent Change và cách dịch chuẩn cụm "X is p% greater than Y"?',
        '% Change = (New - Old)/Old × 100%; X = (1 + p/100)Y',
        [
            '% Change = (New - Old)/New × 100%; X = (p/100)Y',
            '% Change = (Old - New)/New × 100%; X = Y + p',
            '% Change = (New / Old) × 100%; X = (1 - p/100)Y',
        ],
        'Mẫu số Percent Change luôn là giá trị GỐC (Old); "p% greater than Y" = (100 + p)% của Y!',
    ),
    (
        'Công thức khối lượng riêng (Density) liên hệ khối lượng m và thể tích V?',
        'Density = Mass / Volume (ρ = m / V)',
        [
            'Density = Volume / Mass (ρ = V / m)',
            'Density = Mass × Volume (ρ = m × V)',
            'Density = Mass / Area',
        ],
        'ρ = m / V ⇒ Mass = Density × Volume (luôn đồng nhất đơn vị thể tích trước khi nhân!).',
    ),
    (
        'Khi CỘNG cùng một hằng số +c vào MỌI giá trị trong tập dữ liệu, điều gì xảy ra?',
        'Mean & Median tăng +c; Range & Standard Deviation KHÔNG ĐỔI',
        [
            'Cả Mean, Median, Range và Standard Deviation đều tăng +c',
            'Mean tăng +c, còn Median, Range và SD không đổi',
            'Range và SD tăng +c, còn Mean và Median không đổi',
        ],
        'Cộng hằng số chỉ tịnh tiến cả tập dữ liệu: tâm (Mean/Median) dịch +c, độ phân tán (Range/IQR/SD) giữ nguyên!',
    ),
    (
        'Khi NHÂN mọi giá trị trong tập dữ liệu với hằng số k > 0, điều gì xảy ra?',
        'Mean, Median, Range và Standard Deviation đều NHÂN với k',
        [
            'Chỉ Mean và Median nhân k; Range và SD giữ nguyên',
            'SD nhân với k² còn Mean nhân với k',
            'Mean nhân k, còn SD chia cho k',
        ],
        'Phép nhân k > 0 phóng đại cả vị trí tâm lẫn khoảng cách giữa các điểm ⇒ Mean, Median, Range, SD đều nhân k.',
    ),
    (
        'Khi thêm hoặc xóa một giá trị ngoại lệ cực lớn (High Outlier), thước đo nào thay đổi MẠNH hơn?',
        'Mean thay đổi mạnh hơn nhiều so với Median (Median kháng ngoại lệ tốt hơn)',
        [
            'Median thay đổi mạnh hơn nhiều so với Mean',
            'Mean luôn giữ nguyên còn Median biến động mạnh',
            'Cả Mean và Median luôn thay đổi chính xác bằng nhau',
        ],
        'Mean cộng dồn mọi giá trị nên bị outlier kéo rất mạnh; Median chỉ phụ thuộc thứ tự ở giữa nên ổn định hơn.',
    ),
    (
        'So sánh nhanh Độ lệch chuẩn (Standard Deviation) của 2 tập dữ liệu có cùng Mean?',
        'Tập nào dữ liệu dồn ra 2 đầu mút xa Mean hơn thì có SD LỚN HƠN',
        [
            'Tập nào dữ liệu dồn sát vào Mean hơn thì có SD lớn hơn',
            'Cứ có cùng Range thì SD chắc chắn bằng nhau',
            'Tập nào có nhiều giá trị lặp lại ở giữa nhất thì có SD lớn nhất',
        ],
        'SD đo mức độ phân tán quanh Mean (dạng chữ U có SD lớn hơn dạng hình chuông dù cùng Range).',
    ),
    (
        'Công thức xác suất có điều kiện P(A | B) ("given B") trên bảng hai chiều?',
        'P(A | B) = Số phần tử (A và B) / Tổng số phần tử của riêng nhóm B',
        [
            'P(A | B) = Số phần tử (A và B) / Tổng toàn bảng',
            'P(A | B) = Số phần tử (A và B) / Tổng nhóm A',
            'P(A | B) = (Tổng A + Tổng B) / Tổng toàn bảng',
        ],
        'Từ khóa "given that B" / "selected from those who B" thu hẹp mẫu số về ĐÚNG tổng hàng/cột B!',
    ),
    (
        'Công thức Phần dư (Residual) của một điểm dữ liệu trên biểu đồ phân tán (Scatterplot)?',
        'Residual = y_actual - y_predicted (dương nếu điểm nằm trên đường)',
        [
            'Residual = y_predicted - y_actual',
            'Residual = x_actual - y_predicted',
            'Residual = y_actual / y_predicted',
        ],
        'Residual = Thực tế - Dự đoán (Actual minus Predicted). Điểm nằm trên đường best fit có phần dư dương.',
    ),
    (
        'Biên độ sai số (Margin of Error) & tác động của cỡ mẫu n trên SAT?',
        'Khoảng hợp lý: p ± ME; cỡ mẫu n tăng 4 lần ⇒ ME giảm √4 = 2 lần (ME ∝ 1/√n)',
        [
            'Đảm bảo 100% quần thể nằm trong p ± ME; n tăng 4 lần ⇒ ME giảm 4 lần',
            'n tăng 4 lần ⇒ ME tăng 2 lần',
            'Biên độ sai số không phụ thuộc vào cỡ mẫu n',
        ],
        'ME tạo khoảng "plausible values" [p - ME, p + ME] cho quần thể mẫu và tỷ lệ nghịch với √n.',
    ),
    (
        'Ma trận Thiết kế nghiên cứu SAT: Random Selection vs Random Assignment cho phép kết luận gì?',
        'Random Selection → Khái quát hóa quần thể; Random Assignment → Kết luận nhân quả',
        [
            'Random Selection → Kết luận nhân quả; Random Assignment → Khái quát hóa quần thể',
            'Cả hai đều chỉ chứng minh tương quan, không bao giờ có nhân quả',
            'Chỉ cần cỡ mẫu n > 100 là suy ra được cả nhân quả lẫn khái quát toàn cầu',
        ],
        'Chọn mẫu ngẫu nhiên (Selection) ⇒ Generalize to population; Phân nhóm ngẫu nhiên (Assignment) ⇒ Causation!',
    ),
]


GAME_SETS = [
    {
        'key': 'sat_math_game_01',
        'order_index': 1,
        'theme': 'vocab-racing',
        'title': 'SAT Math Speed Game 1: 50 Công thức Đại số & Hàm số 800 (Algebra & Advanced Math)',
        'cards': GAME_1_CARDS,
    },
    {
        'key': 'sat_math_game_02',
        'order_index': 2,
        'theme': 'ninja-survival',
        'title': 'SAT Math Speed Game 2: 50 Công thức Hình học, Lượng giác & Thống kê 800 (Geometry, Trig & Data)',
        'cards': GAME_2_CARDS,
    },
]


def build_math_game_json(gset, course_id):
    """Builds exact TonyEnglish Game Engine (`MCQ (Standard)`) content_json."""
    rng = random.Random(gset['key'])
    labels = ['A', 'B', 'C', 'D']
    # Deterministic balanced slot assignment (13, 13, 12, 12 across 50 cards)
    target_slots = [0] * 13 + [1] * 13 + [2] * 12 + [3] * 12
    rng.shuffle(target_slots)
    questions = []

    for idx, (prompt, correct_opt, traps, explanation) in enumerate(gset['cards']):
        assert len(traps) == 3, f"{gset['key']} card {idx+1} must have 3 traps"
        all_four = [correct_opt] + list(traps)
        assert len({o.strip().lower() for o in all_four}) == 4, (
            f"{gset['key']} card {idx+1} has duplicate options: {all_four}"
        )
        shuffled_traps = list(traps)
        rng.shuffle(shuffled_traps)
        correct_idx = target_slots[idx]
        opts = []
        t_ptr = 0
        for slot in range(4):
            if slot == correct_idx:
                opts.append(correct_opt)
            else:
                opts.append(shuffled_traps[t_ptr])
                t_ptr += 1

        questions.append({
            'id': str(idx + 1),
            'content': prompt,
            'options': opts,
            'correctAnswer': labels[correct_idx],
            'explanation': explanation,
        })

    return {
        'basicInfo': {
            'title': gset['title'],
            'category': 'game',
            'gameTheme': gset['theme'],
            'courseId': course_id,
        },
        'parts': [
            {
                'id': '1',
                'title': '',
                'sections': [
                    {
                        'id': '1',
                        'title': '',
                        'questionType': 'Trắc nghiệm',
                        'questions': questions,
                    }
                ],
            }
        ],
    }


def get_math_games(course_id):
    """Returns [(key, title, order_index, theme, content_json), ...] for both 50-card games."""
    out = []
    for gset in GAME_SETS:
        assert len(gset['cards']) == 50, f"{gset['key']} has {len(gset['cards'])} cards, expected 50"
        cjson = build_math_game_json(gset, course_id)
        out.append((gset['key'], gset['title'], gset['order_index'], gset['theme'], cjson))
    return out


def verify_all_games():
    """Verifies 2 sets × 50 cards = 100 unique plain-text game questions with 0 duplicates and balanced keys."""
    games = get_math_games('TEST_COURSE_ID')
    assert len(games) == 2, f"Expected 2 games, got {len(games)}"

    seen_prompts = set()
    total_cards = 0

    for key, title, order_idx, theme, cjson in games:
        bi = cjson['basicInfo']
        assert bi['category'] == 'game'
        assert bi['gameTheme'] == theme
        assert bi['title'] == title
        assert bi['courseId'] == 'TEST_COURSE_ID'

        sec = cjson['parts'][0]['sections'][0]
        assert sec['questionType'] == 'Trắc nghiệm'
        qs = sec['questions']
        assert len(qs) == 50, f"{key}: expected 50 questions, got {len(qs)}"

        key_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for i, q in enumerate(qs):
            assert q['id'] == str(i + 1), f"{key}: bad id {q['id']}"
            prompt = q['content'].strip()
            assert len(prompt) >= 12, f"{key} Q{i+1}: prompt too short"
            assert prompt.lower() not in seen_prompts, f"Duplicate prompt across sets: {prompt}"
            seen_prompts.add(prompt.lower())

            opts = q['options']
            assert len(opts) == 4, f"{key} Q{i+1}: must have 4 options"
            assert len({o.strip().lower() for o in opts}) == 4, f"{key} Q{i+1}: duplicate options"
            assert q['correctAnswer'] in ('A', 'B', 'C', 'D')
            key_counts[q['correctAnswer']] += 1
            assert len(q['explanation'].strip()) >= 12

            # Verify plain text / Unicode only (NO KaTeX delimiters, NO HTML tags)
            combined = prompt + ' ' + ' '.join(opts) + ' ' + q['explanation']
            assert r'\(' not in combined and r'\[' not in combined, f"LaTeX found in {key} Q{i+1}"
            assert '<p>' not in combined and '<b>' not in combined and '<br' not in combined, (
                f"HTML tag found in {key} Q{i+1}"
            )
            assert '$' not in combined, f"Dollar sign found in {key} Q{i+1}"

        # Ensure answer keys are well balanced across A/B/C/D
        assert max(key_counts.values()) <= 20 and min(key_counts.values()) >= 6, (
            f"{key}: imbalanced keys {key_counts}"
        )
        total_cards += len(qs)
        print(f"  [PASS] {key} ({theme}, order={order_idx}): 50 unique cards, keys={key_counts}")

    assert total_cards == 100 and len(seen_prompts) == 100
    print(f"[ALL PASS] 2 sets × 50 cards = {total_cards} unique verified SAT Math Speed Game flashcards (0 duplicates)!")


if __name__ == '__main__':
    verify_all_games()
