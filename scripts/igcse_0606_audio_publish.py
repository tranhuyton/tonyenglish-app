# -*- coding: utf-8 -*-
"""
Generates Bilingual Audio Lectures (en-US-AndrewNeural + vi-VN-HoaiMyNeural)
for ALL 18 lectures of Cambridge IGCSE Additional Mathematics (0606) 2025-2027!
Outputs to: public/audio/lectures/igcse_0606/{code}/s1.mp3, s2.mp3, s3.mp3, manifest.json
Idempotent: skips MP3s that already exist (>1KB) so re-runs are instant.
"""

import asyncio
import json
import os
import shutil
import subprocess
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import edge_tts

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IDS_PATH = os.path.join(os.path.dirname(__file__), 'igcse_maths_ids.json')

EN_VOICE = 'en-US-BrianNeural'
EN_FALLBACK = 'en-US-GuyNeural'
VI_VOICE = 'vi-VN-HoaiMyNeural'
VI_FALLBACK = 'vi-VN-NamMinhNeural'

COURSE_TITLE = 'Cambridge IGCSE Additional Mathematics (0606)'

# 18 Lectures x 3 rich bilingual segments (Core Concepts, Formulas & Method, Exam Traps & Paper 1/2 Strategy)
AUDIO_SCRIPTS_0606 = {
    'c1': (
        'Chapter 1: Functions',
        [
            (
                's1',
                '1. Core Concepts: Domain, Range & One-to-One Functions',
                'Welcome to Chapter 1 of Cambridge Additional Mathematics 0606: Functions. A function maps every input in the domain to exactly one output in the range. For a function to have an inverse, it must be strictly one-to-one, passing the horizontal line test.',
                'Chào mừng các em đến với Chương 1 Toán Nâng Cao 0606: Hàm số. Một hàm số ánh xạ mỗi giá trị đầu vào thuộc tập xác định Domain tới duy nhất một đầu ra thuộc tập giá trị Range. Để hàm số tồn tại hàm ngược, nó bắt buộc phải là đơn ánh một-một, tức mọi đường nằm ngang chỉ cắt đồ thị tối đa một điểm.',
            ),
            (
                's2',
                '2. Golden Rules: Composite fg(x) & Inverse Mirror y = x',
                'Remember the golden swap rule for inverse functions: the domain of f inverse equals the range of f, and the range of f inverse equals the domain of f. To solve f of x equals f inverse of x without messy algebra, simply solve f of x equals x along the mirror line y equals x.',
                'Hãy thuộc lòng quy tắc hoán đổi vàng cho hàm ngược: Tập xác định của f mũ trừ 1 chính là tập giá trị của f, và ngược lại. Khi đề bắt giải phương trình f x bằng f ngược x, đừng tìm hàm ngược cồng kềnh mà hãy giải thẳng f x bằng x ngay trên đường đối xứng y bằng x!',
            ),
            (
                's3',
                '3. Paper 1 Exam Traps: Domain Restriction & Modulus Graphs',
                'Watch out on Paper 1 Non-Calculator for quadratic domain restrictions: always cut the parabola at its vertex x equals h! And when sketching modulus graphs like y equals modulus of a x plus b, reflect the negative branch sharply above the x-axis to form a crisp V-shape.',
                'Bẫy kinh điển trên Paper 1 Không Máy Tính là tìm miền thu hẹp để hàm bậc hai có hàm ngược: luôn cắt ngay tại hoành độ đỉnh x bằng h! Còn khi vẽ đồ thị trị tuyệt đối, hãy lật đối xứng toàn bộ nhánh âm lên phía trên trục Ox tạo thành góc chữ V sắc nét.',
            ),
        ],
    ),
    'c2': (
        'Chapter 2: Quadratic Functions',
        [
            (
                's1',
                '1. Completing the Square & Turning Points',
                'Chapter 2 focuses on Quadratic Functions. Completing the square transforms a x squared plus b x plus c into a times x plus p all squared plus q. This immediately reveals the turning point at minus p, q and gives you the exact range of the quadratic without calculus.',
                'Chương 2 tập trung vào Hàm bậc hai. Kỹ thuật hoàn chỉnh bình phương biến đổi biểu thức bậc hai về dạng a nhân x cộng p tất cả bình cộng q. Từ đó ta đọc ngay tọa độ đỉnh trừ p phẩy q và tìm ra tập giá trị chính xác mà không cần dùng đạo hàm.',
            ),
            (
                's2',
                '2. Discriminant Conditions for Intersections & Tangency',
                'The discriminant delta equals b squared minus 4 a c controls every intersection problem in Additional Maths. Greater than zero means two distinct roots or intersections; equal to zero means tangency or equal roots; strictly less than zero means no real roots and the line misses the curve completely.',
                'Biệt thức delta bằng b bình trừ 4 a c là chìa khóa cho mọi bài toán tương giao trong 0606. Delta lớn hơn 0 là hai nghiệm hay hai giao điểm phân biệt; bằng 0 là nghiệm kép hay tiếp xúc tiếp tuyến; nhỏ hơn 0 là vô nghiệm, đường thẳng và đường cong không cắt nhau.',
            ),
            (
                's3',
                '3. Quadratic Inequalities & Hidden Quadratics',
                'Never divide a quadratic inequality by an unknown x! Always factorise to find critical values, sketch a quick U-shape parabola, and shade above or below the x-axis. Also train your eyes to spot hidden quadratics like e to the 2 x or x to the two-thirds using substitution u.',
                'Tuyệt đối không chia hai vế bất phương trình bậc hai cho ẩn x! Hãy phân tích nhân tử tìm nghiệm biên, phác nhanh chữ U của parabol rồi đọc khoảng dương hoặc âm. Đồng thời luyện nhận diện phương trình bậc hai ẩn phụ như e mũ 2x hay x mũ hai phần ba bằng cách đặt ẩn u.',
            ),
        ],
    ),
    'c3': (
        'Chapter 3: Indices and Surds (Paper 1 Foundation Bridge)',
        [
            (
                's1',
                '1. Paper 1 Non-Calculator Foundation Bridge (2025–2027)',
                'In the 2025 to 2027 syllabus, Chapter 3 Indices and Surds is your essential Foundation Bridge for Paper 1 Non-Calculator. Every law of indices—negative powers as reciprocals and fractional powers as roots—must be executed cleanly by hand with zero calculator assistance.',
                'Trong chương trình 2025 đến 2027, Chương 3 Lũy thừa và Căn thức là cầu nối nền tảng sống còn cho Paper 1 Không Máy Tính. Mọi quy tắc số mũ âm là nghịch đảo và số mũ phân số là căn bậc phải được biến đổi thành thạo hoàn toàn bằng tay.',
            ),
            (
                's2',
                '2. Rationalising Denominators with Conjugates',
                'Cambridge never awards full final marks for an unrationalised denominator! Multiply top and bottom by the conjugate pair: a plus root b pairs with a minus root b, collapsing the denominator cleanly into a squared minus b using the difference of two squares.',
                'Cambridge không bao giờ cho trọn điểm kết quả nếu mẫu số còn chứa căn thức! Hãy nhân cả tử và mẫu với biểu thức liên hợp a cộng căn b và a trừ căn b để khử sạch căn ở mẫu bằng hằng đẳng thức hiệu hai bình phương.',
            ),
            (
                's3',
                '3. Surds in Geometry & Exponential Index Equations',
                'Expect Paper 1 questions combining surds with triangle areas, trapezium heights, or quadratic roots, as well as index equations like 9 to the x minus 4 times 3 to the x plus 3 equals zero. Always reduce every base to its smallest prime power first!',
                'Hãy chuẩn bị cho các câu Paper 1 ghép căn thức vào tính diện tích tam giác, chiều cao hình thang, hoặc phương trình mũ như 9 mũ x trừ 4 nhân 3 mũ x cộng 3 bằng 0. Luôn đưa tất cả về cùng cơ số nguyên tố nhỏ nhất trước khi giải!',
            ),
        ],
    ),
    'c4': (
        'Chapter 4: Factors of Polynomials',
        [
            (
                's1',
                '1. Remainder Theorem & Factor Theorem',
                'Chapter 4 unlocks cubic and higher-degree polynomials. By the Remainder Theorem, dividing polynomial f of x by a x minus b leaves remainder f of b over a. When that remainder equals zero, a x minus b is an exact linear factor—this is the Factor Theorem.',
                'Chương 4 mở khóa các đa thức bậc ba và bậc cao. Theo Định lý Số dư, khi chia đa thức f x cho a x trừ b, số dư chính là f của b phần a. Khi số dư bằng 0 thì a x trừ b là một nhân tử đúng, đó chính là Định lý Nhân tử.',
            ),
            (
                's2',
                '2. Fast Cubic Factorisation by Comparing Coefficients',
                'Once you spot one linear factor x minus r by testing small divisors of the constant term like plus or minus 1, 2, or 3, factorise the cubic into x minus r times a x squared plus b x plus c. Comparing coefficients is much faster and less error-prone than long division on Paper 1.',
                'Sau khi thử nhanh các ước nhỏ của hệ số tự do như cộng trừ 1, 2, 3 để tìm một nhân tử x trừ r, hãy tách đa thức bậc ba thành x trừ r nhân một tam thức bậc hai. Đồng nhất hệ số nhanh hơn và ít sai dấu hơn hẳn so với chia đa thức truyền thống trên Paper 1.',
            ),
            (
                's3',
                '3. Solving Cubic Equations & Double-Unknown Remainder Traps',
                'Always check whether the remaining quadratic factor can be factorised further or has a negative discriminant meaning only one real root exists. For two-unknown problems giving two remainders, set up simultaneous equations carefully and verify your constants by substitution.',
                'Luôn kiểm tra xem tam thức bậc hai còn lại có phân tích tiếp được không hay có delta âm dẫn tới phương trình chỉ có một nghiệm thực duy nhất. Với bài tìm hai ẩn a, b từ hai số dư, hãy lập hệ hai phương trình và thay ngược lại để kiểm chứng.',
            ),
        ],
    ),
    'c5': (
        'Chapter 5: Equations, Inequalities and Graphs',
        [
            (
                's1',
                '1. Solving Modulus Equations & Inequalities',
                'Chapter 5 tackles modulus equations, cubic graphs, and non-linear simultaneous equations. To solve modulus of a x plus b equals modulus of c x plus d, either square both sides or split cleanly into two linear cases: equal or negative.',
                'Chương 5 chinh phục phương trình trị tuyệt đối, đồ thị bậc ba và hệ phương trình phi tuyến. Để giải trị tuyệt đối a x cộng b bằng trị tuyệt đối c x cộng d, các em có thể bình phương hai vế hoặc tách gọn thành hai trường hợp bằng nhau và đối nhau.',
            ),
            (
                's2',
                '2. Non-Linear Simultaneous Equations & Substitution',
                'When solving one linear and one quadratic equation simultaneously, isolate the simpler variable from the linear equation first, substitute into the curve, and solve for both coordinate pairs x comma y. Always pair each x with its exact corresponding y!',
                'Khi giải hệ gồm một phương trình bậc nhất và một phương trình bậc hai, hãy rút ẩn đơn giản từ phương trình bậc nhất thế vào đường cong, giải tìm đủ các cặp nghiệm x phẩy y. Đừng bao giờ quên ghép đúng từng giá trị x với giá trị y tương ứng!',
            ),
            (
                's3',
                '3. Sketching Cubic & Modulus Curves for Inequalities',
                'When solving cubic inequalities like x minus 1 times x plus 2 times x minus 4 is greater than zero, plot the three x-intercepts on a number line, follow the leading-coefficient end behaviour, and read off the intervals cleanly without losing boundary signs.',
                'Khi giải bất phương trình bậc ba dạng tích ba nhân tử, hãy đánh dấu cả ba nghiệm trên trục số, xét dấu hệ số bậc cao nhất để vẽ dáng điệu đồ thị, sau đó đọc chính xác các khoảng nghiệm theo dấu lớn hơn hay nhỏ hơn của đề bài.',
            ),
        ],
    ),
    'c6': (
        'Chapter 6: Logarithmic and Exponential Functions',
        [
            (
                's1',
                '1. Core Laws of Logarithms & Change of Base',
                'Chapter 6 is a guaranteed exam favourite on both papers. Master the three laws: log of a product is the sum of logs, log of a quotient is the difference, and powers drop straight in front. Whenever bases differ—such as log base 4 and log base 2—apply the change-of-base formula immediately.',
                'Chương 6 là phần chắc chắn xuất hiện ở cả hai đề thi. Hãy thuộc nằm lòng ba quy tắc: log tích bằng tổng log, log thương bằng hiệu log, và số mũ được đưa ra phía trước. Hễ gặp khác cơ số như cơ số 4 và cơ số 2, áp dụng ngay công thức đổi cơ số.',
            ),
            (
                's2',
                '2. Exponential Equations, Natural Log ln & Asymptotes',
                'Remember that y equals e to the x and y equals ln x are exact inverse reflections across y equals x. The curve y equals a e to the b x plus c has horizontal asymptote y equals c, while y equals ln of a x plus b has vertical asymptote where a x plus b equals zero.',
                'Hãy nhớ hàm y bằng e mũ x và y bằng ln x là hai hàm ngược đối xứng qua đường y bằng x. Đồ thị y bằng a e mũ b x cộng c có tiệm cận ngang y bằng c, còn đồ thị y bằng ln của a x cộng b có tiệm cận đứng tại nơi biểu thức bên trong bằng 0.',
            ),
            (
                's3',
                '3. Critical Trap: Rejecting Extraneous Negative Roots',
                'The number one mark-losing trap in Chapter 6 is forgetting domain checks! You can only take the logarithm of a strictly positive number. After solving a quadratic from a log equation, always check every root against the original equation and explicitly cross out invalid solutions.',
                'Cái bẫy mất điểm số một của Chương 6 là quên điều kiện xác định của logarit! Biểu thức trong log bắt buộc phải dương ngặt. Sau khi giải phương trình bậc hai sinh ra từ phương trình log, luôn thay thử vào đề gốc và gạch bỏ rõ ràng nghiệm ngoại lai.',
            ),
        ],
    ),
    'c7': (
        'Chapter 7: Straight Line Graphs & Linear Law',
        [
            (
                's1',
                '1. Perpendicular Bisectors & Shoelace Polygon Area',
                'Chapter 7 combines precision coordinate geometry with Linear Law transformations. A perpendicular bisector always uses the midpoint of AB and the negative reciprocal gradient minus 1 over m. For areas of triangles and quadrilaterals on axes, the anticlockwise shoelace formula gives rapid accuracy.',
                'Chương 7 kết hợp hình học tọa độ đường thẳng và phép tuyến tính hóa Linear Law. Đường trung trực luôn đi qua trung điểm AB và có hệ số góc nghịch đảo đối trừ 1 phần m. Để tính nhanh diện tích tam giác hay tứ giác tọa độ, công thức dây giày ngược chiều kim đồng hồ cho độ chính xác tuyệt đối.',
            ),
            (
                's2',
                '2. Transforming Non-Linear Curves into Y = mX + c',
                'Linear Law is almost guaranteed on Paper 2! To linearise y equals A x to the n, take logarithms of both sides to get ln y equals n ln x plus ln A, so gradient m equals n and vertical intercept c equals ln A. For y equals A b to the x, plot ln y against x so gradient equals ln b.',
                'Linear Law gần như chắc chắn có mặt trong Paper 2! Để tuyến tính hóa y bằng A x mũ n, lấy ln hai vế ta được ln y bằng n ln x cộng ln A, suy ra hệ số góc là n và tung độ gốc là ln A. Còn với y bằng A b mũ x, vẽ ln y theo x để hệ số góc bằng ln b.',
            ),
            (
                's3',
                '3. Exam Warning: Intercept is ln A, Not A!',
                'Watch the classic Linear Law trap: when reading the y-intercept c from a log graph, c equals ln A, so you must compute A equals e to the c—or 10 to the c for base-10 logs—and always check whether the horizontal axis starts at zero before reading the intercept!',
                'Cẩn thận bẫy kinh điển của Linear Law: tung độ gốc c đọc từ đồ thị log là ln A chứ không phải A, nên bắt buộc phải tính A bằng e mũ c hoặc 10 mũ c. Đặc biệt kiểm tra xem trục hoành có bắt đầu từ số 0 hay không trước khi đọc tung độ gốc!',
            ),
        ],
    ),
    'c7b': (
        'Chapter 7B: Coordinate Geometry of the Circle (NEW 2025–2027)',
        [
            (
                's1',
                '1. NEW 2025–2027 Compulsory Topic: Standard & Expanded Circle Equations',
                'Welcome to Chapter 7B: Coordinate Geometry of the Circle—the brand-new compulsory addition to the Cambridge 0606 2025 to 2027 syllabus! Memorise both forms: standard form x minus a squared plus y minus b squared equals r squared, and expanded form x squared plus y squared plus 2 g x plus 2 f y plus c equals zero with centre minus g, minus f and radius square root of g squared plus f squared minus c.',
                'Chào mừng các em đến với Chương 7B: Hình học tọa độ Đường tròn — chuyên đề MỚI BẮT BUỘC trong đề thi Cambridge 0606 từ năm 2025 đến 2027! Hãy thuộc cả hai dạng: dạng chính tắc x trừ a bình cộng y trừ b bình bằng r bình, và dạng khai triển tìm tâm trừ g phẩy trừ f cùng bán kính căn bậc hai g bình cộng f bình trừ c.',
            ),
            (
                's2',
                '2. Tangents, Normals & Chord Bisector Geometry',
                'Three circle theorems power every coordinate proof: first, the normal passes through the centre and is perpendicular to the tangent, so gradient of tangent equals minus 1 over gradient of radius; second, the perpendicular bisector of any chord passes right through the centre; third, chord length equals 2 times square root of r squared minus d squared.',
                'Ba tính chất hình học cốt lõi giải quyết mọi bài chứng minh: thứ nhất, pháp tuyến đi qua tâm và vuông góc với tiếp tuyến nên tích hai hệ số góc bằng trừ 1; thứ hai, trung trực của mọi dây cung đều đi qua tâm; thứ ba, độ dài dây cung bằng hai lần căn bậc hai r bình trừ d bình.',
            ),
            (
                's3',
                '3. Line–Circle Discriminant & Two-Circle Touching Conditions',
                'To test if a line is a tangent to a circle, substitute y equals m x plus c into the circle and set discriminant delta equal to zero. For two circles with centre distance d, they touch externally when d equals r 1 plus r 2, and touch internally when d equals absolute value of r 1 minus r 2. Always divide by k first if the equation starts with k x squared plus k y squared!',
                'Để chứng minh đường thẳng tiếp xúc đường tròn, thế phương trình đường thẳng vào đường tròn và giải biệt thức delta bằng 0. Với hai đường tròn cách tâm đoạn d, chúng tiếp xúc ngoài khi d bằng r1 cộng r2 và tiếp xúc trong khi d bằng trị tuyệt đối r1 trừ r2. Luôn nhớ chia hai vế cho k nếu đầu phương trình là k x bình cộng k y bình!',
            ),
        ],
    ),
    'c8': (
        'Chapter 8: Circular Measure',
        [
            (
                's1',
                '1. Radians, Arc Length s = rθ & Sector Area ½r²θ',
                'Chapter 8 introduces Radian Measure, where pi radians equals exactly 180 degrees. In radians, arc length simplifies beautifully to s equals r theta, and sector area becomes one-half r squared theta. These compact formulas are mandatory for both Circular Measure and Trigonometry calculus!',
                'Chương 8 giới thiệu đơn vị đo góc Radian, với pi radian bằng đúng 180 độ. Khi dùng radian, độ dài cung tròn rút gọn cực đẹp thành s bằng r nhân theta, và diện tích hình quạt là một phần hai r bình nhân theta. Đây là nền tảng bắt buộc cho cả Hình học lẫn Giải tích lượng giác!',
            ),
            (
                's2',
                '2. Shaded Segments & Composite Perimeters',
                'To find the area of a minor segment, subtract the triangle area one-half r squared sine theta from the sector area, giving one-half r squared times theta minus sine theta. For shaded perimeters, carefully trace every boundary piece—curved arcs plus straight chords or tangents!',
                'Để tính diện tích hình viên phân, lấy diện tích hình quạt trừ đi diện tích tam giác một phần hai r bình sin theta, ra công thức một phần hai r bình nhân hiệu theta trừ sin theta. Khi tính chu vi miền tô đậm, hãy rà soát kỹ từng đoạn biên cong và thẳng để không bỏ sót cạnh nào!',
            ),
            (
                's3',
                '3. Paper 1 Exact Angles vs Paper 2 Radian Mode Check',
                'On Paper 1 Non-Calculator, angles will be exact fractions of pi like pi over 3 or pi over 6, so leave your answers in exact terms of pi and root 3. On Paper 2 Calculator, switch your Casio to RAD mode immediately and keep full calculator precision until rounding to 3 significant figures at the very end.',
                'Trên Paper 1 Không Máy Tính, góc sẽ là các phân số đẹp của pi như pi phần 3 hay pi phần 6, hãy giữ đáp án chính xác theo pi và căn 3. Trên Paper 2 Có Máy Tính, chuyển ngay máy Casio sang chế độ RAD và giữ nguyên độ chính xác máy tính đến bước làm tròn 3 chữ số có nghĩa cuối cùng.',
            ),
        ],
    ),
    'c9': (
        'Chapter 9: Trigonometry',
        [
            (
                's1',
                '1. Graphs a sin(bx) + c & Exact Radian Values',
                'Chapter 9 elevates trigonometry to A-level readiness. For y equals a sine of b x plus c, amplitude is modulus of a, period is 360 degrees or 2 pi divided by b, and the midline shifts vertically by c. Memorise exact values for pi over 6, pi over 4, and pi over 3 cold for Paper 1!',
                'Chương 9 nâng tầm lượng giác lên chuẩn tiền A-Level. Với hàm y bằng a sin b x cộng c, biên độ là trị tuyệt đối a, chu kỳ bằng 360 độ hoặc 2 pi chia b, và trục giữa dịch lên xuống theo c. Hãy thuộc như cháo giá trị chính xác tại pi phần 6, pi phần 4 và pi phần 3 cho Paper 1!',
            ),
            (
                's2',
                '2. Reciprocal Functions & Pythagorean Identities',
                'Know the third-letter trick for reciprocal functions: secant is 1 over cosine, cosecant is 1 over sine, and cotangent is 1 over tangent. Use the printed Pythagorean identities sec squared equals 1 plus tan squared and cosec squared equals 1 plus cot squared to convert quadratic trig equations into a single trig ratio.',
                'Dùng mẹo chữ cái thứ ba cho hàm nghịch đảo: sec là 1 phần cos, cosec là 1 phần sin, và cot là 1 phần tan. Tận dụng hai hằng đẳng thức in sẵn trên đề là sec bình bằng 1 cộng tan bình và cosec bình bằng 1 cộng cot bình để đưa phương trình lượng giác bậc hai về cùng một ẩn.',
            ),
            (
                's3',
                '3. Adjusting the Domain for Multiple-Angle Equations',
                'Never lose roots on equations like sine of 2 x minus 30 degrees equals 0.5! Always adjust the domain to match the inside angle 2 x minus 30 FIRST, find every CAST quadrant angle inside that expanded domain, and only then add 30 and divide by 2 at the very last line.',
                'Đừng bao giờ để sót nghiệm trong phương trình dạng sin của 2 x trừ 30 độ bằng 0.5! Bắt buộc biến đổi miền nghiệm theo góc bên trong 2 x trừ 30 độ trước tiên, tìm đủ tất cả các góc theo vòng tròn CAST trong miền mới đó, rồi mới cộng 30 và chia 2 ở dòng cuối cùng.',
            ),
        ],
    ),
    'c10': (
        'Chapter 10: Permutations and Combinations',
        [
            (
                's1',
                '1. Permutations (Order Matters) vs Combinations (Order Does Not)',
                'Chapter 10 tests logical counting—almost always on Paper 2 Calculator. Ask one crucial question first: does order matter? Arranging people in a row, letters in a code, or digits in a number uses Permutations n P r; choosing a committee or team uses Combinations n C r.',
                'Chương 10 kiểm tra tư duy tổ hợp chỉnh hợp — gần như luôn nằm trên Paper 2 Có Máy Tính. Luôn tự hỏi câu đầu tiên: thứ tự có quan trọng không? Xếp hàng, lập mật mã hay ghép chữ số thì dùng Hoán vị Chỉnh hợp nPr; còn chọn đội hay ban đại diện không phân biệt vị trí thì dùng Tổ hợp nCr.',
            ),
            (
                's2',
                '2. Golden Strategies: Glue Method & Gap Method',
                'When items must stay together, glue them into one super-block, arrange the blocks, and multiply by the internal arrangements inside the block. When items must NOT be adjacent, arrange all other items first and slot the separated items into the gaps between them!',
                'Khi các phần tử phải đứng cạnh nhau, hãy dán chúng thành một khối duy nhất, xếp các khối rồi nhân với số cách hoán vị nội bộ bên trong khối. Khi các phần tử KHÔNG được đứng cạnh nhau, hãy xếp toàn bộ nhóm còn lại trước rồi chèn nhóm tách rời vào các khoảng trống xen giữa!',
            ),
            (
                's3',
                '3. At-Least Problems & Complementary Counting',
                'For "at least one" or "at least two" selection problems, either list mutually exclusive cases carefully or use the fast complement rule: Total unrestricted selections minus the forbidden cases. Always double-check that you never accidentally double-count identical items.',
                'Với bài toán chọn có điều kiện "ít nhất một" hoặc "ít nhất hai", các em có thể chia trường hợp rời nhau hoặc dùng quy tắc phần bù siêu nhanh: Tổng số cách chọn tự do trừ đi các trường hợp vi phạm. Luôn kiểm tra kỹ để tránh đếm trùng các trường hợp giống hệt nhau.',
            ),
        ],
    ),
    'c11': (
        'Chapter 11: Series (Binomial, AP & GP)',
        [
            (
                's1',
                '1. Binomial Expansion & Specific Terms',
                'Chapter 11 covers Binomial Expansions, Arithmetic Progressions, and Geometric Progressions. In the expansion of a plus b x to the n, the general term is n C r times a to the n minus r times b x to the r. Always keep brackets around negative terms like minus 2 x so signs alternate accurately!',
                'Chương 11 gồm Khai triển Nhị thức Newton, Cấp số cộng AP và Cấp số nhân GP. Trong khai triển a cộng b x mũ n, số hạng tổng quát là nCr nhân a mũ n trừ r nhân b x mũ r. Luôn bọc ngoặc quanh số hạng âm như trừ 2 x để không bao giờ bị sai dấu cộng trừ!',
            ),
            (
                's2',
                '2. Arithmetic & Geometric Progressions (AP & GP)',
                'Both AP and GP formulas are printed on your 0606 formula sheet—your job is setting up clean equations for first term a, common difference d, or common ratio r. A Geometric Progression converges to a finite sum to infinity a over 1 minus r if and only if modulus of r is strictly less than 1.',
                'Toàn bộ công thức AP và GP đều được in sẵn trên tờ công thức 0606 — nhiệm vụ của các em là lập hệ phương trình chuẩn xác để tìm số hạng đầu a, công sai d hoặc công bội r. Cấp số nhân chỉ hội tụ về tổng vô hạn a chia 1 trừ r khi và chỉ khi trị tuyệt đối của r nhỏ hơn hẳn 1.',
            ),
            (
                's3',
                '3. Classic Traps: Product Expansions & Inequalities for n',
                'For product expansions like 1 plus k x times 2 minus x to the 5, expand up to the exact power needed and cross-multiply matching pairs only. When solving GP sum inequalities for n, remember that dividing by ln r flips the inequality sign whenever r is between 0 and 1!',
                'Với khai triển tích như 1 cộng k x nhân 2 trừ x mũ 5, chỉ khai triển tới đúng số mũ cần tìm rồi nhân chéo các cặp khớp bậc. Khi giải bất phương trình tìm n bằng logarit, cực kỳ lưu ý: nếu 0 nhỏ hơn r nhỏ hơn 1 thì ln r mang dấu âm, chia hai vế cho ln r BẮT BUỘC phải đảo chiều bất đẳng thức!',
            ),
        ],
    ),
    'c12': (
        'Chapter 12: Differentiation 1',
        [
            (
                's1',
                '1. Chain, Product & Quotient Rules',
                'Welcome to Calculus in Chapter 12! Beyond basic power differentiation, Additional Maths demands instant fluency in three core rules: Chain Rule for composite powers, Product Rule u v prime plus v u prime, and Quotient Rule v u prime minus u v prime all over v squared.',
                'Chào mừng các em bước vào Giải tích ở Chương 12! Ngoài đạo hàm lũy thừa cơ bản, 0606 đòi hỏi phản xạ tức thì với ba quy tắc vàng: Đạo hàm hàm hợp Chain Rule, Quy tắc Tích u v phẩy cộng v u phẩy, và Quy tắc Thương v u phẩy trừ u v phẩy tất cả chia v bình.',
            ),
            (
                's2',
                '2. Tangents, Normals & Stationary Points',
                'Evaluating d y by d x at x equals x 1 gives the gradient of the tangent; taking its negative reciprocal gives the gradient of the normal. Stationary points occur strictly where d y by d x equals zero—never confuse stationary points with x-intercepts where y equals zero!',
                'Thay hoành độ x1 vào đạo hàm dy chia dx ta thu được hệ số góc tiếp tuyến, còn nghịch đảo đối của nó là hệ số góc pháp tuyến. Điểm dừng stationary point luôn xảy ra tại nơi dy chia dx bằng 0 — tuyệt đối đừng nhầm với giao điểm trục hoành nơi y bằng 0!',
            ),
            (
                's3',
                '3. Classifying Maxima & Minima with Second Derivative',
                'Use the second derivative test to classify stationary points fast: if d squared y by d x squared is negative, the curve bends downward giving a local Maximum; if positive, it bends upward giving a local Minimum. Always write your conclusion clearly to secure the final A1 mark!',
                'Dùng đạo hàm cấp hai để phân loại cực đại cực tiểu cực nhanh: nếu đạo hàm cấp hai âm, đồ thị úp xuống cho điểm Cực đại Maximum; nếu dương, đồ thị ngửa lên cho điểm Cực tiểu Minimum. Luôn viết câu kết luận rõ ràng để ăn trọn điểm A1 cuối cùng!',
            ),
        ],
    ),
    'c13': (
        'Chapter 13: Vectors (2025–2027 Scope)',
        [
            (
                's1',
                '1. 2025–2027 Syllabus Update: Core Vectors Only (No Relative Velocity)',
                'Important 2025 to 2027 syllabus update for Chapter 13: Relative Velocity has been officially removed from 0606 exams! Focus 100 percent of your effort on position vectors, vector magnitude, unit vectors, geometric ratio division, and proving collinearity.',
                'Cập nhật chương trình 2025 đến 2027 cực kỳ quan trọng cho Chương 13: Phần Vận tốc tương đối Relative Velocity đã chính thức được BỎ khỏi đề thi 0606! Hãy dồn 100 phần trăm sức lực vào vectơ vị trí, độ dài, vectơ đơn vị, tỉ số chia đoạn thẳng và chứng minh thẳng hàng.',
            ),
            (
                's2',
                '2. Unit Vectors & Position Vector Bridge AB = b − a',
                'Every vector from A to B equals position vector O B minus position vector O A. To find a vector of magnitude k parallel to vector v, first divide v by its magnitude square root of x squared plus y squared to get the unit vector, then scale by k.',
                'Mọi vectơ AB đều bằng hiệu vectơ vị trí OB trừ OA. Để tìm một vectơ có độ dài k cùng phương với vectơ v, bước một chia v cho độ dài căn bậc hai x bình cộng y bình để tạo vectơ đơn vị, sau đó nhân với hệ số k.',
            ),
            (
                's3',
                '3. Proving Collinearity & Equating Non-Parallel Coefficients',
                'To prove three points A, B, and C are collinear, show that vector A C equals a scalar multiple of A B AND explicitly state they share the common point A! When an equation equates two combinations of non-parallel vectors a and b, equate the coefficients of a and b separately to solve for lambda and mu.',
                'Để chứng minh ba điểm A, B, C thẳng hàng, hãy chỉ ra vectơ AC bằng k lần vectơ AB VÀ bắt buộc viết thêm câu hai vectơ có chung điểm A! Khi so sánh hai tổ hợp của hai vectơ không cùng phương a và b, hãy đồng nhất riêng hệ số của a và hệ số của b để giải ra lambda và mu.',
            ),
        ],
    ),
    'c14': (
        'Chapter 14: Differentiation 2 (Trig, Exp, Ln & Rates)',
        [
            (
                's1',
                '1. Derivatives of Trig, Exponential & Logarithmic Functions',
                'Chapter 14 expands your differentiation toolkit to transcendental functions—all using radians for trig! Memorise: sine a x differentiates to a cosine a x; cosine a x to minus a sine a x; tangent a x to a sec squared a x; e to the a x to a e to the a x; and ln of a x plus b to a over a x plus b.',
                'Chương 14 mở rộng kho vũ khí đạo hàm sang hàm lượng giác, mũ và logarit — lưu ý lượng giác luôn tính bằng radian! Thuộc lòng: đạo hàm sin ax là a cos ax, cos ax là trừ a sin ax, tan ax là a sec bình ax, e mũ ax là a e mũ ax, và ln của ax cộng b là a chia ax cộng b.',
            ),
            (
                's2',
                '2. Connected Rates of Change & Small Changes',
                'Connected rates use the Chain Rule like cancelling fractions: d V by d t equals d V by d r multiplied by d r by d t. For small changes, use the linear approximation delta y is approximately equal to d y by d x times delta x—always note whether the variable increases positive or decreases negative!',
                'Bài toán tốc độ biến thiên liên kết dùng Quy tắc dây chuyền cực mượt: dV chia dt bằng dV chia dr nhân dr chia dt. Với bài toán số gia nhỏ Small Changes, dùng xấp xỉ delta y gần bằng dy chia dx nhân delta x — luôn kiểm tra kỹ dấu cộng khi tăng và dấu trừ khi giảm!',
            ),
            (
                's3',
                '3. Applied Optimisation Problems (Show-That + Second Derivative)',
                'Optimisation questions always follow a two-part blueprint: first use a constraint like fixed surface area or perimeter to prove a given volume formula; second differentiate, set to zero, solve for the optimal dimension, and check the second derivative to confirm maximum or minimum.',
                'Bài toán tối ưu luôn đi theo cấu trúc hai phần kinh điển: phần một dùng điều kiện ràng buộc về diện tích hay chu vi để chứng minh công thức đề bài cho; phần hai lấy đạo hàm cho bằng 0, giải kích thước tối ưu rồi kiểm tra đạo hàm cấp hai để khẳng định cực đại hay cực tiểu.',
            ),
        ],
    ),
    'c15': (
        'Chapter 15: Integration',
        [
            (
                's1',
                '1. Reverse Differentiation & Core Integration Rules',
                'Chapter 15 reverses differentiation. Whenever you integrate a linear bracket a x plus b to the n, exponential e to the a x plus b, or trig functions sine, cosine, and sec squared, ALWAYS divide by the inner coefficient a—and never forget plus c for indefinite integrals!',
                'Chương 15 là phép toán ngược của đạo hàm. Mỗi khi lấy tích phân của biểu thức bậc nhất ax cộng b mũ n, hàm mũ e mũ ax cộng b, hay các hàm lượng giác sin, cos, sec bình, LUÔN PHẢI chia cho hệ số a bên trong — và không bao giờ quên hằng số cộng c ở tích phân bất định!',
            ),
            (
                's2',
                '2. The Signature 0606 Trick: "Hence Integrate..."',
                'The most iconic Cambridge 0606 calculus question has part a: differentiate a product like x e to the 2 x, followed by part b: hence find the integral of x e to the 2 x! Simply integrate both sides of your part a identity, rearrange algebraically, and isolate the target integral cleanly.',
                'Dạng câu hỏi đặc trưng nhất của 0606 gồm câu a lấy đạo hàm một tích như x nhân e mũ 2x, rồi câu b yêu cầu từ đó tính tích phân của x e mũ 2x! Chỉ cần lấy tích phân hai vế của đẳng thức câu a, chuyển vế rút gọn là ra ngay đáp án mà không cần phương pháp tích phân từng phần.',
            ),
            (
                's3',
                '3. Definite Integrals & Area Under / Between Curves',
                'For area between two curves, integrate top curve minus bottom curve between their intersection x-limits. Remember that any region lying below the x-axis produces a negative definite integral, so always take its positive magnitude when summing total geometric area!',
                'Để tính diện tích giữa hai đường cong, lấy tích phân của đường nằm trên trừ đường nằm dưới giữa hai cận giao điểm. Nhớ rằng phần hình nằm dưới trục hoành sẽ cho giá trị tích phân âm, nên luôn lấy trị tuyệt đối dương khi cộng tổng diện tích hình học!',
            ),
        ],
    ),
    'c16': (
        'Chapter 16: Kinematics',
        [
            (
                's1',
                '1. The Calculus Triangle: Displacement s ↔ Velocity v ↔ Acceleration a',
                'Chapter 16 brings Calculus to life in motion along a straight line. Moving down the chain uses differentiation: velocity v equals d s by d t, and acceleration a equals d v by d t. Moving back up uses integration—and you MUST use the given initial conditions at t equals 0 to find every constant c!',
                'Chương 16 ứng dụng Giải tích vào chuyển động thẳng. Đi xuôi xuống dưới dùng đạo hàm: vận tốc v bằng ds chia dt, gia tốc a bằng dv chia dt. Đi ngược lên trên dùng tích phân — và BẮT BUỘC thay điều kiện ban đầu tại t bằng 0 để tìm chính xác từng hằng số cộng c!',
            ),
            (
                's2',
                '2. Decoding Key Exam Phrases Instantly',
                'Translate Cambridge kinematics vocabulary automatically: "instantaneously at rest" means v equals 0; "returns to fixed point O" means displacement s equals 0; "maximum or minimum velocity" means acceleration a equals 0; and "constant velocity" means a equals 0.',
                'Hãy dịch tự động các từ khóa động học Cambridge: đứng yên tức thời nghĩa là v bằng 0; quay về gốc O nghĩa là độ dời s bằng 0; vận tốc cực đại hay cực tiểu nghĩa là gia tốc a bằng 0; và chuyển động đều nghĩa là a bằng 0.',
            ),
            (
                's3',
                '3. Displacement vs Total Distance Travelled Trap',
                'Never confuse displacement with total distance travelled! Before computing total distance between t 1 and t 2, ALWAYS check whether the particle reverses direction by solving v equals 0 inside that interval. If it turns around at t star, split the journey into two parts and add their absolute displacements.',
                'Tuyệt đối không nhầm giữa độ dời và tổng quãng đường đi được! Trước khi tính tổng quãng đường từ t1 đến t2, LUÔN giải v bằng 0 xem hạt có đổi chiều bên trong khoảng thời gian đó hay không. Nếu có điểm quay đầu, hãy tách thành hai chặng rồi cộng trị tuyệt đối độ dời của từng chặng.',
            ),
        ],
    ),
    'rev': (
        'Year End Revision: Paper 1 (Non-Calculator) Playbook & Master Formula Sheet',
        [
            (
                's1',
                '1. 2025–2027 Exam Blueprint: Paper 1 Non-Calc vs Paper 2 Calc',
                'Congratulations on reaching the 0606 Year End Revision! In the 2025 to 2027 exam structure, Paper 1 is strictly Non-Calculator and Paper 2 is Calculator—both 2 hours, 80 marks each, counting 50 percent each. Budget 1.5 minutes per mark so you always finish with 10 minutes to check!',
                'Chúc mừng các em đã tới bài Tổng ôn cuối khóa 0606! Trong cấu trúc thi 2025 đến 2027, Paper 1 hoàn toàn Không Máy Tính và Paper 2 Có Máy Tính — mỗi đề dài 2 tiếng, 80 điểm, chiếm đúng 50 phần trăm. Hãy phân bổ 1 phẩy 5 phút cho mỗi điểm để luôn dư 10 phút soát lại bài!',
            ),
            (
                's2',
                '2. Master Formula Strategy: Printed vs Must-Memorise',
                'Know what Cambridge prints on page 2: Quadratic Formula, Binomial, AP, GP, and Pythagorean Trig identities. That means you MUST memorise Circle equations, Circular Measure radian formulas, Logarithmic laws, Exact Trig table, and every Differentiation and Integration rule by heart.',
                'Hãy nắm rõ những gì Cambridge in sẵn trang 2: Công thức nghiệm bậc hai, Nhị thức Newton, AP, GP và hằng đẳng thức lượng giác. Điều đó có nghĩa các em BẮT BUỘC thuộc lòng phương trình Đường tròn, công thức Radian, quy tắc Logarit, bảng Lượng giác chính xác và toàn bộ bảng Đạo hàm — Tích phân.',
            ),
            (
                's3',
                '3. Final A* Checklist Before Entering the Exam Hall',
                'Before handing in your script, run the A-star checklist: rationalise all surds on Paper 1, reject negative roots in logarithms, include plus c on indefinite integrals, check RAD versus DEG mode on Paper 2, and round non-exact Paper 2 answers to 3 significant figures. You are ready to ace 0606!',
                'Trước khi nộp bài, hãy rà soát danh sách săn điểm A sao: trục căn mọi mẫu số trên Paper 1, loại nghiệm ngoại lai của logarit, kiểm tra cộng c ở tích phân bất định, soát đúng chế độ RAD hay DEG trên Paper 2, và làm tròn chuẩn 3 chữ số có nghĩa. Chúc các em chinh phục trọn vẹn điểm A sao 0606!',
            ),
        ],
    ),
}


async def _gen_tts(text: str, voice: str, out_file: str, max_retries: int = 25):
    # Clean characters that occasionally trigger Edge TTS NoAudioReceived
    clean_text = (
        text.replace('—', ', ')
        .replace('–', ' - ')
        .replace('↔', ' and ')
        .replace('θ', 'theta')
        .replace('π', 'pi')
        .replace('²', ' squared ')
        .replace('³', ' cubed ')
        .replace('⁻¹', ' inverse ')
        .replace('∞', ' infinity ')
        .replace('−', ' minus ')
        .replace('×', ' times ')
        .replace('…', '...')
    )
    for attempt in range(1, max_retries + 1):
        try:
            if os.path.exists(out_file):
                try:
                    os.remove(out_file)
                except Exception:
                    pass
            cur_voice = voice
            if attempt >= 2:
                if voice == VI_VOICE:
                    cur_voice = VI_FALLBACK if (attempt % 2 == 0) else VI_VOICE
                elif voice == EN_VOICE:
                    cur_voice = EN_FALLBACK if (attempt % 2 == 0) else EN_VOICE
            communicate = edge_tts.Communicate(clean_text, cur_voice)
            await asyncio.wait_for(communicate.save(out_file), timeout=15.0)
            if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
                await asyncio.sleep(0.15)
                return
            raise RuntimeError(f'Empty audio output {out_file}')
        except Exception as e:
            if attempt == max_retries:
                raise
            wait = min(0.5 * attempt, 2.5)
            print(f'  [RETRY {attempt}] {cur_voice}: {e} -> wait {wait:.1f}s', flush=True)
            await asyncio.sleep(wait)


def get_audio_duration(file_path: str) -> float:
    res = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True,
    )
    return round(float(res.stdout.strip()), 2)


async def build_one_lecture(sem, code, lecture_id, title, seg_tuples):
    async with sem:
        out_dir = os.path.join(ROOT_DIR, 'public', 'audio', 'lectures', 'igcse_0606', code)
        tmp_dir = os.path.join(ROOT_DIR, 'scratch', f'audio_temp_igcse_0606_{code}')
        os.makedirs(out_dir, exist_ok=True)
        os.makedirs(tmp_dir, exist_ok=True)

        print(f'[AUDIO 0606/{code}] {title} ({len(seg_tuples)} segs)', flush=True)
        segments = []
        major_sections = {}
        curr = 0.0
        for idx, (sid, stitle, en_txt, vi_txt) in enumerate(seg_tuples):
            final_mp3 = os.path.join(out_dir, f'{sid}.mp3')
            if not (os.path.exists(final_mp3) and os.path.getsize(final_mp3) > 1000):
                en_tmp = os.path.join(tmp_dir, f'{sid}_en.mp3')
                vi_tmp = os.path.join(tmp_dir, f'{sid}_vi.mp3')
                await _gen_tts(en_txt, EN_VOICE, en_tmp)
                await _gen_tts(vi_txt, VI_VOICE, vi_tmp)
                subprocess.run(
                    [
                        'ffmpeg', '-y',
                        '-i', en_tmp,
                        '-f', 'lavfi', '-t', '0.35', '-i', 'anullsrc=r=24000:cl=mono',
                        '-i', vi_tmp,
                        '-filter_complex', '[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]',
                        '-map', '[out]', '-b:a', '96k', final_mp3,
                    ],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                )
                for t in (en_tmp, vi_tmp):
                    if os.path.exists(t):
                        os.remove(t)
            dur = get_audio_duration(final_mp3)
            seg_obj = {
                'id': sid,
                'title': stitle,
                'selector': f'[data-lecture-section="{sid}"]',
                'en': en_txt,
                'vi': vi_txt,
                'duration': dur,
                'startTime': round(curr, 2),
                'endTime': round(curr + dur, 2),
                'audioUrl': f'/audio/lectures/igcse_0606/{code}/{sid}.mp3',
            }
            segments.append(seg_obj)
            major_sections[sid] = {'start': idx, 'end': idx}
            curr += dur

        manifest = {
            'lectureId': lecture_id,
            'courseTitle': COURSE_TITLE,
            'lectureTitle': title,
            'totalDuration': round(curr, 2),
            'majorSections': major_sections,
            'segments': segments,
        }
        with open(os.path.join(out_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        shutil.rmtree(tmp_dir, ignore_errors=True)
        print(f'  [OK] igcse_0606/{code}/manifest.json ({round(curr, 1)}s)', flush=True)


async def main_async():
    with open(IDS_PATH, 'r', encoding='utf-8') as f:
        ids = json.load(f)
    lecs = ids['m0606']['lectures']
    sem = asyncio.Semaphore(3)
    tasks = []
    for code, (title, segs) in AUDIO_SCRIPTS_0606.items():
        lid = lecs.get(code)
        if not lid:
            raise RuntimeError(f'Missing 0606 lecture ID for code={code} — run igcse_0606_upgrade_lectures.py first!')
        tasks.append(build_one_lecture(sem, code, lid, title, segs))
    await asyncio.gather(*tasks)
    print(f'\n[ALL DONE] Generated bilingual audio manifests for all {len(tasks)} lectures of IGCSE Maths 0606!', flush=True)


if __name__ == '__main__':
    asyncio.run(main_async())
