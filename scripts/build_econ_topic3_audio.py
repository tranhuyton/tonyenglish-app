import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

COURSE_TITLE = "Cambridge IGCSE Economics (0455)"

# =====================================================================
# LECTURE 16: Money and Banking
# =====================================================================
LEC16_ID = "3adca75c-b852-48be-9cbf-5074ae12e430"
LEC16_TITLE = "16. Money and Banking"

lec16_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 16: Tiền tệ và Hệ thống Ngân hàng",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 3: Microeconomic Decision Makers. In Lesson 16, we explore Money and Banking. We will trace the historical transition from barter systems to modern digital money, examine the four core functions and six characteristics of good money, compare the roles of central banks and commercial banks, and evaluate why businesses face lending constraints.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Chủ đề 3: Các Chủ thể Quyết định Kinh tế Vi mô. Trong Bài 16, chúng ta tìm hiểu về Tiền tệ và Hệ thống Ngân hàng. Chúng ta sẽ theo dõi hành trình chuyển đổi từ hình thức đổi hàng lấy hàng sang tiền tệ kỹ thuật số hiện đại, phân tích bốn chức năng cốt lõi và sáu đặc tính của tiền tệ, so sánh vai trò của ngân hàng trung ương với ngân hàng thương mại, và tìm hiểu lý do tại sao doanh nghiệp gặp rào cản khi vay vốn."
    },
    {
        "id": "sec_evolution",
        "title": "1. Sự Tiến hóa & Các Hình thức của Tiền tệ",
        "selector": "#sec-evolution",
        "en": "Section 1 charts the history of exchange. Barter economies suffered from the double coincidence of wants, where trade only occurred if both parties desired each other's goods. Money emerged as a universal medium of exchange, evolving from commodity money like cattle and shells, to precious metals, minted coins, paper fiat money, and contemporary digital payment cards and mobile transfers.",
        "vi": "Mục 1 phác họa lịch sử giao thương. Nền kinh tế đổi hàng từng gặp trở ngại lớn bởi yêu cầu trùng khớp kép về nhu cầu, nghĩa là trao đổi chỉ diễn ra khi hai bên cùng cần hàng hóa của nhau. Tiền tệ ra đời như một phương tiện trao đổi phổ quát, tiến hóa từ tiền hàng hóa như gia súc và vỏ sò, sang kim loại quý, tiền kim loại đúc, tiền giấy pháp định và ngày nay là thẻ thanh toán điện tử cùng chuyển khoản di động."
    },
    {
        "id": "card_forms",
        "title": "A. Các Hình thức Tiến hóa của Tiền tệ",
        "selector": "#card-forms",
        "en": "The evolution of money shows continuous improvements in convenience: starting with Commodity Money having intrinsic value; transitioning to Metal Coins with standardised weights; developing Paper Banknotes representing legal tender backed by central banks; and culminating in Digital and Electronic Money enabling instant global settlement.",
        "vi": "Tiến trình phát triển của tiền tệ liên tục nâng cao sự tiện lợi: khởi đầu từ Tiền hàng hóa có giá trị nội tại; chuyển sang Tiền kim loại với trọng lượng tiêu chuẩn; phát triển thành Tiền giấy pháp định được ngân hàng trung ương bảo chứng; và đỉnh cao là Tiền kỹ thuật số điện tử cho phép thanh toán toàn cầu tức thì."
    },
    {
        "id": "sec_functions",
        "title": "2. Chức năng & Đặc điểm của Tiền tệ",
        "selector": "#sec-functions",
        "en": "Section 2 establishes the economic foundations of money. Money must fulfill four distinct functions: medium of exchange, unit of account, store of value, and standard for deferred payments. To perform these roles reliably, an asset must possess six physical and economic traits: acceptability, durability, portability, divisibility, scarcity, and uniformity.",
        "vi": "Mục 2 xác lập nền tảng kinh tế của tiền tệ. Tiền tệ phải đảm bảo bốn chức năng: phương tiện trao đổi, thước đo giá trị, phương tiện cất trữ giá trị và phương tiện thanh toán trả chậm. Để hoàn thành những vai trò này, một tài sản cần có đủ sáu đặc tính: được chấp nhận rộng rãi, bền bỉ, dễ mang theo, có thể chia nhỏ, khan hiếm và đồng nhất."
    },
    {
        "id": "card_four_functions",
        "title": "A. Bốn Chức năng Cốt lõi của Tiền tệ",
        "selector": "#card-four-functions",
        "en": "Money operates across four roles: First, as a Medium of Exchange eliminating the barter problem. Second, as a Unit of Account providing common pricing benchmarks. Third, as a Store of Value preserving purchasing power into the future. Fourth, as a Standard of Deferred Payment enabling credit contracts and borrowing.",
        "vi": "Tiền tệ vận hành qua bốn vai trò: Thứ nhất, là Phương tiện Trao đổi xóa bỏ trở ngại của đổi hàng. Thứ hai, là Thước đo Giá trị làm chuẩn mực định giá thống nhất. Thứ ba, là Phương tiện Cất trữ Giá trị bảo toàn sức mua cho tương lai. Thứ tư, là Tiêu chuẩn Thanh toán Trả chậm tạo tiền đề cho các hợp đồng tín dụng và vay nợ."
    },
    {
        "id": "card_characteristics",
        "title": "B. Sáu Đặc tính Thiết yếu của Tiền tệ Tốt",
        "selector": "#card-characteristics",
        "en": "The six characteristics guarantee confidence in money: Acceptability ensures people trust it; Durability withstands wear and tear; Portability makes everyday transport effortless; Divisibility allows exact change; Scarcity maintains real purchasing power; and Uniformity standardises value across identical denominations.",
        "vi": "Sáu đặc tính bảo đảm niềm tin vào tiền tệ: Tính được chấp nhận tạo dựng lòng tin; Tính bền bỉ giúp tiền không bị mục nát; Tính dễ di chuyển giúp mang theo nhẹ nhàng; Tính dễ chia nhỏ cho phép giao dịch chính xác; Tính khan hiếm giữ vững sức mua thực tế; và Tính đồng nhất chuẩn hóa giá trị của mọi tờ tiền cùng mệnh giá."
    },
    {
        "id": "sec_banking",
        "title": "3. Hệ thống Ngân hàng: Ngân hàng Trung ương vs NHTM",
        "selector": "#sec-banking",
        "en": "Section 3 contrasts the two tiers of the banking system. The Central Bank is the state-owned monetary authority responsible for macroeconomic stability, interest rates, issuing banknotes, and acting as the lender of last resort. Commercial Banks are profit-seeking private enterprises that accept consumer deposits, provide business loans, and facilitate everyday payments.",
        "vi": "Mục 3 phân biệt hai cấp trong hệ thống ngân hàng. Ngân hàng Trung ương là cơ quan tiền tệ thuộc sở hữu nhà nước, chịu trách nhiệm ổn định kinh tế vĩ mô, ấn định lãi suất cơ bản, phát hành tiền giấy và giữ vai trò người cho vay cứu cánh cuối cùng. Ngân hàng Thương mại là doanh nghiệp tư nhân hoạt động vì lợi nhuận, thực hiện nhận tiền gửi, cấp tín dụng và cung cấp các dịch vụ thanh toán hàng ngày."
    },
    {
        "id": "card_central_bank",
        "title": "🏛️ Ngân hàng Trung ương (Central Bank)",
        "selector": "#card-central-bank",
        "en": "Key functions of a central bank include: monopoly issuer of currency; managing national foreign exchange reserves; setting monetary policy and official interest rates; supervising the commercial banking sector; and advising the government on public debt management.",
        "vi": "Các chức năng cốt lõi của ngân hàng trung ương gồm có: độc quyền phát hành tiền tệ quốc gia; quản lý dự trữ ngoại hối; điều hành chính sách tiền tệ và lãi suất; thanh tra giám sát ngân hàng thương mại; và làm đại lý tư vấn quản lý nợ công cho chính phủ."
    },
    {
        "id": "card_commercial_bank",
        "title": "🏢 Ngân hàng Thương mại (Commercial Bank)",
        "selector": "#card-commercial-bank",
        "en": "Commercial banks intermediate between savers and borrowers: accepting demand and savings deposits; providing overdrafts, mortgages, and commercial loans; making money through net interest margins; and offering modern digital payment facilities.",
        "vi": "Ngân hàng thương mại đóng vai trò trung gian tài chính giữa người gửi tiền và người đi vay: tiếp nhận tiền gửi thanh toán và tiết kiệm; cấp hạn mức thấu chi, cho vay mua nhà và tín dụng doanh nghiệp; tạo lợi nhuận từ biên lãi thuần; và cung cấp tiện ích thanh toán điện tử hiện đại."
    },
    {
        "id": "sec_borrowing",
        "title": "4. Trọng tâm Thi: Tại sao Doanh nghiệp khó Vay vốn?",
        "selector": "#sec-borrowing",
        "en": "Section 4 highlights a vital examination topic: lending constraints. Small and startup firms often struggle to borrow from commercial banks due to a lack of collateral, unproven credit history, high default risk, and information asymmetry, compelling them to rely on retained profits, trade credit, or venture capital.",
        "vi": "Mục 4 tập trung vào một câu hỏi then chốt trong các kỳ thi: rào cản tiếp cận vốn vay. Các doanh nghiệp nhỏ và mới thành lập thường gặp khó khăn khi vay ngân hàng thương mại do thiếu tài sản bảo đảm, chưa có lịch sử tín dụng uy tín, rủi ro vỡ nợ cao và bất cân xứng thông tin, buộc họ phải dựa vào lợi nhuận giữ lại, tín dụng thương mại hoặc vốn khởi nghiệp."
    }
]

lec16_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_evolution": {"start": 1, "end": 2},
    "sec_functions": {"start": 3, "end": 5},
    "sec_banking": {"start": 6, "end": 8},
    "sec_borrowing": {"start": 9, "end": 9}
}

# =====================================================================
# LECTURE 17: Households: Income, Saving, Borrowing & Spending
# =====================================================================
LEC17_ID = "123d8a13-d619-45cd-b363-702e9039627a"
LEC17_TITLE = "17. Households: Income, Saving, Borrowing & Spending"

lec17_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 17: Hộ Gia đình: Thu nhập, Tiết kiệm, Vay nợ & Tiêu dùng",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 17: Households: Income, Saving, Borrowing and Spending. In this lesson, we analyse how households allocate their disposable income between present consumption and future savings, how borrowing finances larger purchases, and how interest rates, income levels, and wealth reshape household economic decisions.",
        "vi": "Chào mừng các bạn đến với Bài 17: Hộ Gia đình: Thu nhập, Tiết kiệm, Vay nợ và Tiêu dùng. Trong bài này, chúng ta sẽ phân tích cách các hộ gia đình phân bổ thu nhập khả dụng giữa tiêu dùng hiện tại và tiết kiệm cho tương lai, cách vay nợ tài trợ cho các khoản mua sắm lớn, và cách lãi suất, mức thu nhập cùng của cải định hình các quyết định kinh tế của hộ gia đình."
    },
    {
        "id": "sec_spending",
        "title": "1. Tiêu dùng của Hộ gia đình (Spending / Consumption)",
        "selector": "#sec-spending",
        "en": "Section 1 examines household spending. Disposable income—gross income minus income taxes plus welfare transfers—is the single primary determinant of consumption. As disposable income rises, total consumer spending increases, but the proportion of income spent on basic necessities like food falls, while expenditure on luxury goods and services rises.",
        "vi": "Mục 1 khảo sát chi tiêu tiêu dùng của hộ gia đình. Thu nhập khả dụng—tổng thu nhập trừ thuế thu nhập cá nhân cộng các khoản trợ cấp xã hội—là nhân tố then chốt chi phối tiêu dùng. Khi thu nhập khả dụng tăng lên, tổng chi tiêu tiêu dùng cũng tăng, nhưng tỷ trọng thu nhập dành cho các nhu yếu phẩm thiết yếu như thực phẩm sẽ giảm dần, nhường chỗ cho các dịch vụ và hàng hóa tiện nghi cao cấp."
    },
    {
        "id": "card_spending_factors",
        "title": "A. Các Yếu tố Ảnh hưởng đến Chi tiêu Tiêu dùng",
        "selector": "#card-spending-factors",
        "en": "Apart from income, key influences on spending include: real interest rates, where higher rates increase borrowing costs and reward saving; consumer confidence regarding future job security; family size and age distribution; and the wealth effect generated by rising housing or equity prices.",
        "vi": "Ngoài thu nhập, các yếu tố tác động mạnh đến chi tiêu gồm có: lãi suất thực, khi lãi suất tăng sẽ làm tăng chi phí vay nợ và khuyến khích gửi tiết kiệm; niềm tin của người tiêu dùng về công việc và kinh tế; quy mô cùng cơ cấu độ tuổi gia đình; và hiệu ứng của cải sinh ra khi giá nhà đất hoặc chứng khoán tăng giá."
    },
    {
        "id": "sec_saving",
        "title": "2. Tiết kiệm của Hộ gia đình (Household Saving)",
        "selector": "#sec-saving",
        "en": "Section 2 investigates saving, defined as disposable income not spent on current goods and services. Saving provides funds for future emergencies, major retirement planning, and children's education. Higher-income households typically have a higher average propensity to save than lower-income households.",
        "vi": "Mục 2 tìm hiểu về tiết kiệm, được định nghĩa là phần thu nhập khả dụng không đem tiêu dùng cho các hàng hóa, dịch vụ hiện tại. Tiết kiệm tạo nguồn lực dự phòng bất trắc, tài trợ cho kế hoạch hưu trí và đầu tư cho tương lai con cái. Các hộ gia đình thu nhập cao luôn có xu hướng tiết kiệm bình quân lớn hơn nhiều so với các hộ gia đình thu nhập thấp."
    },
    {
        "id": "card_saving_motives",
        "title": "A. Động cơ & Các Yếu tố Quyết định Tiết kiệm",
        "selector": "#card-saving-motives",
        "en": "Core saving motives include: precautionary saving for unforeseen contingencies; target saving for major future purchases like houses; and retirement planning. High interest rates incentivize saving by yielding greater returns on bank deposits.",
        "vi": "Các động cơ tiết kiệm cốt lõi gồm: tiết kiệm phòng ngừa cho rủi ro bất ngờ; tiết kiệm mục tiêu cho các khoản mua sắm lớn như mua nhà; và chuẩn bị tài chính tuổi già. Lãi suất tiền gửi cao sẽ kích thích người dân gửi tiền vào ngân hàng để thu về lợi tức hấp dẫn."
    },
    {
        "id": "sec_borrowing",
        "title": "3. Vay mượn của Hộ gia đình (Household Borrowing)",
        "selector": "#sec-borrowing",
        "en": "Section 3 addresses household borrowing. Borrowing allows households to consume beyond their current income by using mortgages for homes, personal bank loans, or credit cards. The availability of credit, consumer confidence, and the level of interest rates directly regulate the volume of consumer debt.",
        "vi": "Mục 3 phân tích hoạt động vay nợ của hộ gia đình. Vay nợ cho phép người tiêu dùng chi tiêu vượt quá thu nhập hiện tại thông qua vay thế chấp mua nhà, vay tiêu dùng tín chấp hoặc quẹt thẻ tín dụng. Mức độ sẵn có của hạn mức tín dụng, niềm tin người tiêu dùng và mặt bằng lãi suất trực tiếp điều tiết quy mô nợ vay cá nhân."
    },
    {
        "id": "sec_wealth",
        "title": "4. Trọng tâm Thi: Mối quan hệ giữa Tiêu dùng, Tiết kiệm & Của cải",
        "selector": "#sec-wealth",
        "en": "Section 4 focuses on exam integration: Income is a flow of money earned per time period, whereas wealth is a stock of accumulated financial and physical assets. Rising wealth stimulates spending through collateralised borrowing and confidence, even if current cash income remains unchanged.",
        "vi": "Mục 4 nhấn mạnh điểm thi trọng tâm: Thu nhập là một dòng tiền kiếm được trong một khoảng thời gian, còn của cải là một lượng tích lũy tài sản tài chính và vật chất. Của cải gia tăng kích thích chi tiêu nhờ khả năng thế chấp vay vốn dễ dàng hơn và tinh thần lạc quan, ngay cả khi thu nhập tiền mặt hiện tại không đổi."
    }
]

lec17_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_spending": {"start": 1, "end": 2},
    "sec_saving": {"start": 3, "end": 4},
    "sec_borrowing": {"start": 5, "end": 5},
    "sec_wealth": {"start": 6, "end": 6}
}

# =====================================================================
# LECTURE 18: Workers: Wage Determination & Labour Mobility
# =====================================================================
LEC18_ID = "95fb66bf-66f0-4bbd-a7e4-418f191f487a"
LEC18_TITLE = "18. Workers: Wage Determination & Labour Mobility"

lec18_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 18: Người Lao động: Lựa chọn Nghề nghiệp & Tiền lương",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 18: Workers: Wage Determination, Specialisation, and Labour Mobility. In this lesson, we analyse the factors individuals weigh when choosing a career, how wages are determined through labour demand and supply, the consequences of national minimum wages, reasons behind wage differentials, and the advantages of division of labour.",
        "vi": "Chào mừng các bạn đến với Bài 18: Người Lao động: Xác định Tiền lương, Chuyên môn hóa và Tính Cơ động của Lao động. Trong bài này, chúng ta sẽ phân tích các nhân tố khi lựa chọn nghề nghiệp, cách tiền lương được quyết định qua cung cầu lao động, tác động của mức lương tối thiểu quốc gia, nguyên nhân gây chênh lệch thu nhập và lợi thế của phân công lao động."
    },
    {
        "id": "sec_occupation",
        "title": "1. Lựa chọn Nghề nghiệp: Yếu tố Lương vs Phi Lương",
        "selector": "#sec-occupation",
        "en": "Section 1 divides occupational influences into wage and non-wage factors. While basic pay, overtime rates, and bonuses provide financial incentives, individuals often value non-wage factors like job satisfaction, working hours, commuting distances, job security, promotional prospects, and holiday allowances just as highly.",
        "vi": "Mục 1 chia các yếu tố định hình lựa chọn nghề nghiệp thành yếu tố tiền lương và yếu tố phi tiền lương. Mặc dù lương cơ bản, tiền làm thêm giờ và tiền thưởng là động lực tài chính mạnh mẽ, người lao động cũng coi trọng không kém các yếu tố phi tiền lương như sự hài lòng công việc, giờ giấc làm việc, khoảng cách đi lại, độ ổn định của công việc, cơ hội thăng tiến và chế độ nghỉ phép."
    },
    {
        "id": "card_wage_factors",
        "title": "💰 Yếu tố Tiền lương & Thu nhập",
        "selector": "#card-wage-factors",
        "en": "Wage payment methods include: time rates paid per hour; piece rates paid per unit produced; commission paid as a percentage of sales; and performance-related pay linking compensation to achieving operational targets.",
        "vi": "Các phương thức trả lương gồm có: trả lương theo thời gian làm việc mỗi giờ; trả lương theo sản phẩm hoàn thành; trả hoa hồng tính theo phần trăm doanh thu bán hàng; và trả lương theo hiệu quả hoàn thành mục tiêu công việc."
    },
    {
        "id": "card_non_wage_factors",
        "title": "🌟 Yếu tố Phi Tiền lương",
        "selector": "#card-non-wage-factors",
        "en": "Non-wage considerations frequently determine job choice: intrinsic job satisfaction, positive workplace environment, training and career development opportunities, fringe benefits such as healthcare or company transport, and flexible working arrangements.",
        "vi": "Các yếu tố phi tiền lương thường quyết định sự gắn bó nghề nghiệp: sự đam mê và yêu thích công việc, môi trường làm việc thân thiện, cơ hội đào tạo và nâng cao tay nghề, các phúc lợi phụ như bảo hiểm sức khỏe hoặc xe đưa đón, cùng thời gian làm việc linh hoạt."
    },
    {
        "id": "sec_wage_determination",
        "title": "2. Xác định Tiền lương trên Thị trường Lao động",
        "selector": "#sec-wage-determination",
        "en": "Section 2 illustrates wage determination through market equilibrium: Labour Demand is a derived demand originating from the consumer demand for the final goods workers produce. Labour Supply reflects the willingness of qualified workers to offer their labour at various wage rates. The intersection yields the equilibrium wage and employment level.",
        "vi": "Mục 2 minh họa cách xác định tiền lương thông qua cân bằng thị trường: Cầu lao động là cầu phái sinh bắt nguồn từ nhu cầu tiêu dùng hàng hóa cuối cùng do người lao động tạo ra. Cung lao động thể hiện số lượng nhân lực sẵn sàng làm việc tại các mức lương khác nhau. Điểm giao nhau quyết định mức tiền lương và số lượng lao động cân bằng."
    },
    {
        "id": "sec_nmw",
        "title": "3. Mức lương Tối thiểu Quốc gia (National Minimum Wage)",
        "selector": "#sec-nmw",
        "en": "Section 3 evaluates a statutory National Minimum Wage. Imposed as a price floor above the free market wage, it aims to prevent worker exploitation and reduce poverty. However, if set too high, it increases employers' production costs, which may cause businesses to cut hours or create surplus unemployment.",
        "vi": "Mục 3 đánh giá chính sách Mức lương Tối thiểu Quốc gia do nhà nước quy định. Đóng vai trò là giá sàn đặt trên mức lương cân bằng thị trường tự do, chính sách này nhằm ngăn chặn bóc lột và giảm nghèo đói. Tuy nhiên, nếu quy định quá cao, nó làm tăng chi phí sản xuất của doanh nghiệp, có thể dẫn đến việc cắt giảm giờ làm hoặc gây ra thất nghiệp dư thừa."
    },
    {
        "id": "sec_wage_differentials",
        "title": "4. Chênh lệch Tiền lương (Wage Differentials)",
        "selector": "#sec-wage-differentials",
        "en": "Section 4 explains why wages differ across occupations. Skilled workers command higher wages because their supply is inelastic due to lengthy education and training, while their productivity is high. Differentials also arise between public and private sectors, manual and non-manual work, and traditional gender pay gaps.",
        "vi": "Mục 4 lý giải nguyên nhân dẫn đến chênh lệch tiền lương giữa các ngành nghề. Lao động có tay nghề cao nhận được mức lương vượt trội vì cung lao động kém co giãn do đòi hỏi thời gian đào tạo dài lâu, đồng thời năng suất đóng góp của họ rất lớn. Chênh lệch tiền lương cũng xuất hiện giữa khu vực công và tư nhân, lao động chân tay và trí óc, cũng như khoảng cách giới tính."
    },
    {
        "id": "sec_mobility_division",
        "title": "5. Tính Cơ động của Lao động & Phân công Lao động",
        "selector": "#sec-mobility-division",
        "en": "Section 5 examines labour mobility and specialisation: Occupational mobility requires transferable skills, while geographical mobility requires affordable housing and moving grants. Division of labour breaks production into repetitive sub-tasks, boosting output and worker efficiency, but risks worker boredom and structural unemployment.",
        "vi": "Mục 5 tìm hiểu tính cơ động của lao động và chuyên môn hóa: Cơ động nghề nghiệp đòi hỏi kỹ năng có thể chuyển đổi, còn cơ động địa lý cần nhà ở giá hợp lý và trợ cấp di chuyển. Phân công lao động chia nhỏ quy trình sản xuất thành các khâu lặp lại, nâng cao sản lượng và sự thành thạo, nhưng có thể gây nhàm chán và nguy cơ thất nghiệp cơ cấu."
    }
]

lec18_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_occupation": {"start": 1, "end": 3},
    "sec_wage_determination": {"start": 4, "end": 4},
    "sec_nmw": {"start": 5, "end": 5},
    "sec_wage_differentials": {"start": 6, "end": 6},
    "sec_mobility_division": {"start": 7, "end": 7}
}

# =====================================================================
# LECTURE 19: Trade Unions
# =====================================================================
LEC19_ID = "1943e7bc-cdee-45b1-93d5-830b704a4017"
LEC19_TITLE = "19. Trade Unions"

lec19_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 19: Công đoàn Lao động (Trade Unions)",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 19: Trade Unions. In this lesson, we explore how worker organisations use collective bargaining to negotiate higher wages and improved conditions, inspect the forms of industrial action they take, analyse factors determining their bargaining power, and evaluate their overall economic benefits and costs.",
        "vi": "Chào mừng các bạn đến với Bài 19: Công đoàn Lao động. Trong bài này, chúng ta sẽ tìm hiểu cách các tổ chức người lao động sử dụng đàm phán tập thể để thương lượng nâng lương và cải thiện điều kiện làm việc, khảo sát các hình thức đấu tranh công nghiệp, phân tích các yếu tố quyết định sức mạnh thương lượng, và đánh giá toàn diện lợi ích cùng chi phí đối với nền kinh tế."
    },
    {
        "id": "sec_union_intro",
        "title": "1. Khái niệm & Vai trò Cốt lõi của Công đoàn",
        "selector": "#sec-union-intro",
        "en": "Section 1 defines a trade union as an organisation of employees formed to protect and promote their common interests. Through collective bargaining, a union represents all member workers in wage negotiations, securing safety standards, job security, and training opportunities more effectively than individual workers could alone.",
        "vi": "Mục 1 định nghĩa công đoàn là tổ chức của người lao động được thành lập nhằm bảo vệ và thúc đẩy các quyền lợi chung. Thông qua thương lượng tập thể, công đoàn đại diện cho toàn thể đoàn viên trong các cuộc đàm phán tiền lương, bảo đảm tiêu chuẩn an toàn lao động, việc làm ổn định và cơ hội bồi dưỡng tay nghề hiệu quả hơn nhiều so với từng cá nhân riêng lẻ."
    },
    {
        "id": "card_union_types",
        "title": "A. Bốn Loại hình Công đoàn Chính",
        "selector": "#card-union-types",
        "en": "Trade unions span four main categories: Craft unions organising workers with specific craft skills; Industrial unions grouping all workers in an entire industry; General unions enrolling workers across diverse skill levels and industries; and White-collar unions representing professional and administrative staff.",
        "vi": "Công đoàn được chia thành bốn nhóm chính: Công đoàn thợ thủ công tập hợp lao động có cùng kỹ năng nghề chuyên biệt; Công đoàn ngành kết nạp toàn bộ công nhân trong một ngành công nghiệp; Công đoàn đại chúng mở rộng cho mọi lao động thuộc nhiều ngành nghề; và Công đoàn lao động trí óc đại diện cho giới nhân viên văn phòng và chuyên viên."
    },
    {
        "id": "sec_industrial_action",
        "title": "2. Các Hình thức Đấu tranh Công nghiệp",
        "selector": "#sec-industrial-action",
        "en": "Section 2 reviews industrial action when negotiations stall: Strikes represent complete withdrawal of labour; Overtime bans refuse work beyond standard contracts; Work-to-rule obeys employment rules to the letter to slow operational pace; and Go-slow deliberately reduces worker output speeds.",
        "vi": "Mục 2 điểm qua các hình thức đấu tranh công nghiệp khi đàm phán bế tắc: Đình công là việc ngừng việc hoàn toàn; Cấm làm thêm giờ là từ chối làm việc ngoài giờ chuẩn; Làm việc theo đúng quy chế là tuân thủ máy móc các nội quy để làm chậm tiến độ vận hành; và Lãnh công có chủ đích làm giảm tốc độ sản xuất của công nhân."
    },
    {
        "id": "sec_bargaining_power",
        "title": "3. Sức mạnh Đàm phán của Công đoàn",
        "selector": "#sec-bargaining-power",
        "en": "Section 3 evaluates union bargaining leverage. Union strength increases when: a high percentage of the workforce are members (closed shop); the demand for the final product and labour is price inelastic; the firm earns high monopoly profits; and the legal framework provides robust strike protections.",
        "vi": "Mục 3 đánh giá quyền lực đàm phán của công đoàn. Sức mạnh của công đoàn gia tăng khi: tỷ lệ công nhân tham gia công đoàn rất cao; cầu đối với sản phẩm cuối cùng và lao động kém co giãn; doanh nghiệp đang thu được lợi nhuận độc quyền lớn; và hệ thống luật pháp bảo vệ quyền đình công vững chắc."
    },
    {
        "id": "sec_evaluation",
        "title": "4. Đánh giá: Lợi ích và Chi phí của Công đoàn",
        "selector": "#sec-evaluation",
        "en": "Section 4 weighs trade union impacts: Unions can improve wages, bolster worker motivation, and facilitate clear communication with employers. However, excessive wage demands can spark cost-push inflation, reduce international competitiveness, and cause employer cutbacks leading to structural unemployment.",
        "vi": "Mục 4 cân nhắc tác động hai mặt của công đoàn: Công đoàn có thể nâng cao tiền lương, tạo động lực làm việc và làm cầu nối đối thoại minh bạch với chủ sử dụng lao động. Tuy nhiên, đòi hỏi tăng lương quá mức có thể châm ngòi cho lạm phát chi phí đẩy, giảm sức cạnh tranh quốc tế và buộc doanh nghiệp phải sa thải bớt nhân sự, gây thất nghiệp cơ cấu."
    }
]

lec19_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_union_intro": {"start": 1, "end": 2},
    "sec_industrial_action": {"start": 3, "end": 3},
    "sec_bargaining_power": {"start": 4, "end": 4},
    "sec_evaluation": {"start": 5, "end": 5}
}

# =====================================================================
# LECTURE 20: Firms: Size, Growth & Integration
# =====================================================================
LEC20_ID = "07e42111-1e2c-4810-bce3-02d8df497c97"
LEC20_TITLE = "20. Firms: Size, Growth & Integration"

lec20_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 20: Doanh nghiệp: Quy mô, Tăng trưởng & Sáp nhập",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 20: Firms: Size, Growth, and Integration. In this lesson, we classify firms by economic sector, examine the competitive advantages that allow small businesses to coexist alongside large multinationals, explore internal and external growth routes through mergers, and uncover internal and external economies and diseconomies of scale.",
        "vi": "Chào mừng các bạn đến với Bài 20: Doanh nghiệp: Quy mô, Tăng trưởng và Sáp nhập. Trong bài này, chúng ta sẽ phân loại doanh nghiệp theo các khu vực kinh tế, khảo sát những lợi thế cạnh tranh giúp doanh nghiệp nhỏ cùng tồn tại song song với các tập đoàn đa quốc gia, tìm hiểu các con đường tăng trưởng nội sinh và sáp nhập, cùng các tính kinh tế và phi kinh tế theo quy mô."
    },
    {
        "id": "sec_classification",
        "title": "1. Phân loại Doanh nghiệp theo Ngành & Khu vực",
        "selector": "#sec-classification",
        "en": "Section 1 categorises firms: by economic stage into primary extraction, secondary manufacturing, and tertiary services; and by ownership structure into sole traders, partnerships, private and public limited companies, and state-owned public corporations.",
        "vi": "Mục 1 phân loại doanh nghiệp: theo các giai đoạn kinh tế gồm khu vực sơ cấp khai thác, khu vực thứ cấp chế biến chế tạo và khu vực tam cấp dịch vụ; cũng như theo hình thức sở hữu gồm hộ kinh doanh cá thể, công ty hợp danh, công ty trách nhiệm hữu hạn tư nhân, công ty cổ phần đại chúng và tập đoàn nhà nước."
    },
    {
        "id": "sec_firm_size",
        "title": "2. Quy mô Doanh nghiệp: Doanh nghiệp Nhỏ vs Lớn",
        "selector": "#sec-firm-size",
        "en": "Section 2 investigates why small firms survive despite large firm cost advantages: Small firms thrive in niche markets offering personalised customer care, flexible customized production, geographical convenience, and personal services where economies of scale are negligible.",
        "vi": "Mục 2 tìm hiểu lý do các doanh nghiệp nhỏ vẫn tồn tại vững chắc trước lợi thế chi phí của các tập đoàn lớn: Doanh nghiệp nhỏ phát triển mạnh ở các thị trường ngách nhờ dịch vụ chăm sóc khách hàng tận tâm, khả năng sản xuất linh hoạt theo yêu cầu, thuận tiện về địa lý và cung cấp các dịch vụ cá nhân hóa nơi tính kinh tế theo quy mô không đáng kể."
    },
    {
        "id": "card_small_vs_large",
        "title": "🏪 Doanh nghiệp Nhỏ vs 🏢 Doanh nghiệp Lớn",
        "selector": "#card-small-vs-large",
        "en": "Comparison reveals distinct traits: Small firms enjoy agile decision-making, direct staff motivation, and niche adaptability. Large firms command massive investment resources, global brand recognition, and lower unit production costs.",
        "vi": "So sánh làm nổi bật các đặc trưng riêng biệt: Doanh nghiệp nhỏ có tốc độ ra quyết định linh hoạt, động lực gắn kết nhân viên trực tiếp và dễ thích nghi thị trường ngách. Doanh nghiệp lớn nắm giữ nguồn lực tài chính khổng lồ, danh tiếng thương hiệu toàn cầu và chi phí sản xuất trên từng đơn vị sản phẩm thấp hơn."
    },
    {
        "id": "sec_integration",
        "title": "3. Sáp nhập & Hợp nhất Doanh nghiệp (Integration)",
        "selector": "#sec-integration",
        "en": "Section 3 outlines external growth via integration: Horizontal integration combines firms in the same industry at the same stage of production; Vertical integration joins firms at consecutive stages either backward toward raw materials or forward toward consumers; Conglomerate integration unites completely unrelated industries to diversify business risk.",
        "vi": "Mục 3 trình bày các hình thức tăng trưởng thông qua sáp nhập: Hợp nhất theo chiều ngang kết hợp các doanh nghiệp cùng ngành ở cùng một công đoạn sản xuất; Hợp nhất theo chiều dọc liên kết các khâu liên tiếp hoặc về phía sau để kiểm soát nguồn nguyên liệu hoặc về phía trước để tiếp cận người tiêu dùng; Hợp nhất tập đoàn kết hợp các ngành hoàn toàn độc lập nhằm đa dạng hóa rủi ro kinh doanh."
    },
    {
        "id": "sec_economies_scale",
        "title": "4. Tính kinh tế & Phi kinh tế theo Quy mô",
        "selector": "#sec-economies-scale",
        "en": "Section 4 analyzes scale dynamics: Internal economies of scale reduce long-run average costs through purchasing discounts, technical machinery, financial credit terms, and managerial specialization. Beyond optimal capacity, diseconomies of scale emerge due to communication bottlenecks, bureaucratic delays, and worker alienation.",
        "vi": "Mục 4 phân tích tính quy mô: Tính kinh tế theo quy mô nội bộ giúp hạ thấp chi phí bình quân dài hạn thông qua chiết khấu mua hàng số lượng lớn, máy móc kỹ thuật hiện đại, điều kiện vay vốn ưu đãi và chuyên môn hóa quản lý. Vượt quá quy mô tối ưu, tính phi kinh tế theo quy mô xuất hiện do tắc nghẽn thông tin liên lạc, bộ máy quan liêu chậm chạp và tinh thần làm việc sa sút của công nhân."
    }
]

lec20_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_classification": {"start": 1, "end": 1},
    "sec_firm_size": {"start": 2, "end": 3},
    "sec_integration": {"start": 4, "end": 4},
    "sec_economies_scale": {"start": 5, "end": 5}
}

# =====================================================================
# LECTURE 21: Firms and Production: Costs, Revenue & Objectives
# =====================================================================
LEC21_ID = "604d1490-caed-47aa-a562-a6a902790a30"
LEC21_TITLE = "21. Firms and Production: Factor Demand & Productivity"

lec21_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 21: Doanh nghiệp & Sản xuất: Cầu Yếu tố, Năng suất & Chi phí",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 21: Firms and Production: Factor Demand, Productivity, and Short-Run Costs. In this lesson, we study what drives demand for land, labour, and capital, contrast labour-intensive with capital-intensive production, distinguish between total output and efficiency, and define fixed and variable costs.",
        "vi": "Chào mừng các bạn đến với Bài 21: Doanh nghiệp và Sản xuất: Cầu Yếu tố Sản xuất, Năng suất và Chi phí Ngắn hạn. Trong bài này, chúng ta sẽ tìm hiểu các nhân tố quyết định cầu về đất đai, lao động và vốn, so sánh phương thức sản xuất thâm dụng lao động với thâm dụng vốn, phân biệt tổng sản lượng và năng suất hiệu quả, cùng các khái niệm chi phí cố định và chi phí biến đổi."
    },
    {
        "id": "sec_factor_demand",
        "title": "1. Cầu về các Yếu tố Sản xuất (Derived Demand)",
        "selector": "#sec-factor-demand",
        "en": "Section 1 explains that factor demand is derived: firms purchase machinery and hire workers solely to manufacture goods that consumers demand. A rise in market demand for consumer goods elevates factor demand, alongside the relative costs and productivity of labour compared to automated capital equipment.",
        "vi": "Mục 1 giải thích bản chất cầu phái sinh: doanh nghiệp chỉ mua máy móc và tuyển dụng nhân công nhằm chế tạo những hàng hóa mà người tiêu dùng có nhu cầu. Nhu cầu thị trường đối với sản phẩm tiêu dùng tăng lên sẽ kéo theo sự gia tăng cầu về các yếu tố sản xuất, song hành với tương quan chi phí và năng suất của lao động so với máy móc tự động hóa."
    },
    {
        "id": "sec_intensity",
        "title": "2. Thâm dụng Lao động vs Thâm dụng Vốn",
        "selector": "#sec-intensity",
        "en": "Section 2 compares production intensity: Labour-intensive production relies predominantly on human workforce, suited for personalized services, handmade goods, and low-wage economies. Capital-intensive production relies on heavy machinery, robotics, and advanced automation, enabling standardized mass production at lower unit costs.",
        "vi": "Mục 2 so sánh cường độ sản xuất: Sản xuất thâm dụng lao động dựa chủ yếu vào lực lượng nhân công, rất phù hợp với các dịch vụ cá nhân hóa, hàng thủ công tinh xảo và các quốc gia có tiền lương thấp. Sản xuất thâm dụng vốn dựa vào máy móc cơ giới, robot và dây chuyền tự động hóa tiên tiến, cho phép sản xuất hàng loạt với chi phí trên từng đơn vị sản phẩm cực thấp."
    },
    {
        "id": "sec_productivity",
        "title": "3. Phân biệt Sản lượng (Production) vs Năng suất (Productivity)",
        "selector": "#sec-productivity",
        "en": "Section 3 addresses a critical conceptual boundary: Production is the total physical volume of goods and services produced. Productivity is a measure of efficiency, calculated as output per unit of input, such as output per worker per hour. Boosting productivity through capital investment, staff training, and technological innovation lowers average production costs.",
        "vi": "Mục 3 phân định ranh giới khái niệm quan trọng: Sản lượng là tổng khối lượng vật chất của hàng hóa và dịch vụ được tạo ra. Năng suất là thước đo hiệu quả kinh tế, được tính bằng sản lượng trên mỗi đơn vị yếu tố đầu vào, chẳng hạn như sản lượng trên mỗi công nhân mỗi giờ. Nâng cao năng suất qua đầu tư máy móc, đào tạo tay nghề và đổi mới công nghệ giúp giảm chi phí sản xuất bình quân."
    },
    {
        "id": "sec_short_run_costs",
        "title": "4. Chi phí Sản xuất Ngắn hạn: Cố định vs Biến đổi",
        "selector": "#sec-short-run-costs",
        "en": "Section 4 defines cost behaviors in the short run: Fixed Costs do not alter with changes in output, such as factory rent and insurance. Variable Costs vary directly with output volume, such as raw material costs and direct hourly wages. Total Cost equals total fixed cost plus total variable cost.",
        "vi": "Mục 4 định nghĩa hành vi chi phí trong ngắn hạn: Chi phí cố định không thay đổi theo mức sản lượng tạo ra, ví dụ như tiền thuê nhà xưởng và phí bảo hiểm. Chi phí biến đổi thay đổi trực tiếp theo số lượng sản phẩm, như tiền mua nguyên vật liệu và tiền lương trả theo giờ. Tổng chi phí bằng tổng chi phí cố định cộng tổng chi phí biến đổi."
    }
]

lec21_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_factor_demand": {"start": 1, "end": 1},
    "sec_intensity": {"start": 2, "end": 2},
    "sec_productivity": {"start": 3, "end": 3},
    "sec_short_run_costs": {"start": 4, "end": 4}
}

# =====================================================================
# LECTURE 22: Market Structure: Competitive Markets
# =====================================================================
LEC22_ID = "d2019792-c956-44e2-98ed-c247617a9162"
LEC22_TITLE = "22. Firms' Objectives, Costs, Revenue & Break-even"

lec22_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 22: Mục tiêu Doanh nghiệp, Chi phí, Doanh thu & Điểm Hòa vốn",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 22: Firms' Objectives, Costs, Revenue, and Break-even Analysis. In this lesson, we study the multiple goals firms pursue, compute average and marginal revenues, apply cost formulas, and interpret break-even charts to determine the margin of safety.",
        "vi": "Chào mừng các bạn đến với Bài 22: Mục tiêu Doanh nghiệp, Chi phí, Doanh thu và Phân tích Hòa vốn. Trong bài này, chúng ta sẽ tìm hiểu các mục tiêu đa dạng của doanh nghiệp, tính toán doanh thu bình quân và cận biên, áp dụng các công thức chi phí, và phân tích biểu đồ hòa vốn để xác định giới hạn an toàn tài chính."
    },
    {
        "id": "sec_objectives",
        "title": "1. Các Mục tiêu của Doanh nghiệp (Objectives of Firms)",
        "selector": "#sec-objectives",
        "en": "Section 1 reviews business goals: While textbook economics assumes profit maximisation, firms frequently pursue other aims such as short-term survival during recessions, sales growth to capture dominant market share, social welfare enhancement, and environmental sustainability.",
        "vi": "Mục 1 phân tích các mục tiêu kinh doanh: Dù kinh tế học truyền thống giả định tối đa hóa lợi nhuận, trên thực tế doanh nghiệp thường theo đuổi các mục tiêu khác như duy trì sự tồn tại trong khủng hoảng, mở rộng doanh thu để chiếm lĩnh thị phần, nâng cao phúc lợi cộng đồng và phát triển bền vững bảo vệ môi trường."
    },
    {
        "id": "card_objectives_grid",
        "title": "🎯 Bốn Mục tiêu Doanh nghiệp Cốt lõi",
        "selector": "#card-objectives-grid",
        "en": "The four main business objectives include: 1. Profit Maximisation (widening the gap between revenue and costs); 2. Survival (maintaining liquidity in tough markets); 3. Growth and Market Share (expanding scale to secure pricing power); and 4. Corporate Social Responsibility (ethical sourcing and reduced emissions).",
        "vi": "Bốn mục tiêu kinh doanh chủ chốt gồm: 1. Tối đa hóa Lợi nhuận (nới rộng khoảng cách giữa doanh thu và chi phí); 2. Tồn tại và Duy trì Hoạt động (bảo toàn thanh khoản trong nghịch cảnh); 3. Tăng trưởng Thị phần (mở rộng quy mô để gia tăng vị thế định giá); và 4. Trách nhiệm Xã hội Doanh nghiệp (sản xuất có đạo đức và giảm thiểu khí thải)."
    },
    {
        "id": "sec_formulas",
        "title": "2. Các Công thức Chi phí & Bảng Tính Chi phí",
        "selector": "#sec-formulas",
        "en": "Section 2 focuses on essential mathematical relationships: Average Fixed Cost falls continuously as output expands, spreading fixed costs over more units. Average Variable Cost initially declines before rising due to diminishing returns. Average Total Cost equals Total Cost divided by total output.",
        "vi": "Mục 2 tập trung vào các công thức tính toán cốt lõi: Chi phí cố định bình quân liên tục giảm khi sản lượng tăng, do chi phí cố định được san sẻ cho nhiều đơn vị hàng hóa hơn. Chi phí biến đổi bình quân ban đầu giảm dần rồi sau đó tăng lên do hiệu suất giảm dần. Chi phí tổng bình quân bằng tổng chi phí chia cho tổng sản lượng."
    },
    {
        "id": "sec_revenue_breakeven",
        "title": "3. Doanh thu, Lợi nhuận & Phân tích Điểm Hòa vốn",
        "selector": "#sec-revenue-breakeven",
        "en": "Section 3 examines financial results: Total Revenue equals Price times Quantity sold. Profit equals Total Revenue minus Total Cost. The Break-Even point occurs where Total Revenue precisely equals Total Cost, leaving neither profit nor loss. Operating above break-even establishes a margin of safety against unexpected demand downturns.",
        "vi": "Mục 3 phân tích kết quả tài chính: Tổng doanh thu bằng giá bán nhân số lượng bán ra. Lợi nhuận bằng tổng doanh thu trừ đi tổng chi phí. Điểm hòa vốn là điểm mà tại đó tổng doanh thu vừa vặn bù đắp toàn bộ tổng chi phí, không có lãi cũng không chịu lỗ. Sản xuất và bán hàng trên mức hòa vốn tạo ra biên an toàn bảo vệ doanh nghiệp trước các sụt giảm bất ngờ của thị trường."
    }
]

lec22_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_objectives": {"start": 1, "end": 2},
    "sec_formulas": {"start": 3, "end": 3},
    "sec_revenue_breakeven": {"start": 4, "end": 4}
}

# =====================================================================
# LECTURE 23: Market Structure: Monopoly
# =====================================================================
LEC23_ID = "4a814791-86ae-4aab-b9e2-a94b2565c55c"
LEC23_TITLE = "23. Market Structure: Competition vs Monopoly"

lec23_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 23: Cấu trúc Thị trường: Cạnh tranh vs Độc quyền",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 23: Market Structure: Competitive Markets versus Monopoly. In this concluding lesson of Topic 3, we contrast competitive market structures with pure monopoly, assess barriers to entry, observe how competition disciplines prices and quality, and evaluate whether monopolies are inevitably harmful to consumer welfare.",
        "vi": "Chào mừng các bạn đến với Bài 23: Cấu trúc Thị trường: Thị trường Cạnh tranh vs Độc quyền. Trong bài học kết bài của Chủ đề 3 này, chúng ta sẽ so sánh cấu trúc thị trường cạnh tranh với độc quyền thuần túy, phân tích rào cản gia nhập thị trường, quan sát cách cạnh tranh điều tiết giá cả và chất lượng, đồng thời đánh giá xem liệu độc quyền có luôn gây hại cho phúc lợi người tiêu dùng hay không."
    },
    {
        "id": "sec_competition_vs_monopoly",
        "title": "1. Thị trường Cạnh tranh vs Thị trường Độc quyền",
        "selector": "#sec-competition-vs-monopoly",
        "en": "Section 1 defines the structural spectrum: Highly competitive markets feature many buyers and sellers, homogeneous or differentiated products, low entry barriers, and firms acting as price takers. A pure monopoly features a single dominant supplier, unique products with no close substitutes, high entry barriers, and the power to act as a price maker.",
        "vi": "Mục 1 xác định phổ cấu trúc thị trường: Thị trường cạnh tranh cao có rất nhiều người mua và người bán, sản phẩm đồng nhất hoặc có sự khác biệt nhẹ, rào cản gia nhập thị trường thấp và các doanh nghiệp là người chấp nhận giá thị trường. Ngược lại, độc quyền thuần túy chỉ có duy nhất một nhà cung ứng độc tôn, sản phẩm độc nhất không có hàng thay thế gần gũi, rào cản gia nhập cực cao và doanh nghiệp nắm quyền lực định đoạt giá bán."
    },
    {
        "id": "card_comparison_table",
        "title": "📊 Bảng So sánh 4 Chiều kích Cốt lõi",
        "selector": "#card-comparison-table",
        "en": "The comparison table synthesises four vital dimensions: 1. Number of Sellers (many versus single); 2. Nature of Product (standardised versus unique); 3. Barriers to Entry (free entry versus formidable legal, financial, or technical barriers); and 4. Pricing Power (price taker versus price maker).",
        "vi": "Bảng so sánh tổng hợp bốn chiều kích nền tảng: 1. Số lượng Người bán (vô số đối thủ cạnh tranh so với một doanh nghiệp duy nhất); 2. Đặc tính Sản phẩm (tiêu chuẩn hóa so với sản phẩm độc nhất vô nhị); 3. Rào cản Gia nhập (tự do ra vào thị trường so với rào cản pháp lý, công nghệ và tài chính khổng lồ); và 4. Quyền lực Định giá (người chấp nhận giá so với người quyết định giá)."
    },
    {
        "id": "sec_impact_price_output",
        "title": "3. Tác động của Cạnh tranh lên Giá cả và Sản lượng",
        "selector": "#sec-impact-price-output",
        "en": "Section 3 demonstrates market mechanics: Competition forces firms to operate efficiently, lowering prices toward minimum average cost and expanding total market supply. Monopoly power restricts market output, allowing the monopolist to push prices above competitive levels and extract economic supernormal profits.",
        "vi": "Mục 3 minh chứng cơ chế vận hành thị trường: Áp lực cạnh tranh buộc các doanh nghiệp phải tối ưu hóa năng suất, kéo giá bán xuống sát mức chi phí bình quân tối thiểu và mở rộng sản lượng cung ứng cho xã hội. Quyền lực độc quyền hạn chế sản lượng trên thị trường, giúp nhà độc quyền đẩy giá lên cao vượt xa mức cạnh tranh để thâu tóm siêu lợi nhuận kinh tế."
    },
    {
        "id": "sec_evaluating_monopoly",
        "title": "4. Đánh giá Độc quyền: Ưu và Nhược điểm đối với Người tiêu dùng",
        "selector": "#sec-evaluating-monopoly",
        "en": "Section 4 provides an objective economic appraisal: Monopolies can disadvantage consumers through higher prices, restricted choices, and complacency. Conversely, natural monopolies avoid wasteful duplication of infrastructure like water pipes, and substantial supernormal profits fund heavy research and development into ground-breaking innovations.",
        "vi": "Mục 4 đưa ra đánh giá kinh tế khách quan: Độc quyền có thể gây thiệt thòi cho người tiêu dùng vì giá bán đắt đỏ, sự lựa chọn nghèo nàn và thói chây ỳ trì trệ. Tuy nhiên, độc quyền tự nhiên giúp tránh sự trùng lặp lãng phí hệ thống cơ sở hạ tầng như đường ống nước, và nguồn siêu lợi nhuận khổng lồ cung cấp ngân sách dồi dào cho hoạt động nghiên cứu phát triển các phát minh công nghệ đột phá."
    }
]

lec23_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_competition_vs_monopoly": {"start": 1, "end": 2},
    "sec_impact_price_output": {"start": 3, "end": 3},
    "sec_evaluating_monopoly": {"start": 4, "end": 4}
}

ALL_TOPIC3_LECTURES = [
    ("16", LEC16_ID, COURSE_TITLE, LEC16_TITLE, lec16_segments, lec16_major_sections),
    ("17", LEC17_ID, COURSE_TITLE, LEC17_TITLE, lec17_segments, lec17_major_sections),
    ("18", LEC18_ID, COURSE_TITLE, LEC18_TITLE, lec18_segments, lec18_major_sections),
    ("19", LEC19_ID, COURSE_TITLE, LEC19_TITLE, lec19_segments, lec19_major_sections),
    ("20", LEC20_ID, COURSE_TITLE, LEC20_TITLE, lec20_segments, lec20_major_sections),
    ("21", LEC21_ID, COURSE_TITLE, LEC21_TITLE, lec21_segments, lec21_major_sections),
    ("22", LEC22_ID, COURSE_TITLE, LEC22_TITLE, lec22_segments, lec22_major_sections),
    ("23", LEC23_ID, COURSE_TITLE, LEC23_TITLE, lec23_segments, lec23_major_sections),
]

async def main():
    print("=================================================================")
    print("GENERATING AUDIO & MANIFEST FOR TOPIC 3 (LECTURES 16 - 23)")
    print("=================================================================")
    for code, lid, course, title, segments, major_sections in ALL_TOPIC3_LECTURES:
        await process_lecture_audio(code, lid, course, title, segments, major_sections, subject='economics')
    print("\n✅ ALL TOPIC 3 AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
