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
# LECTURE 1: The Basic Economic Problem
# =====================================================================
LEC1_ID = "1fba7e8c-742f-4697-b93e-a0205fc7d825"
LEC1_TITLE = "1. The Basic Economic Problem"

lec1_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1: Vấn đề Kinh tế Cơ bản",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 1: The Basic Economic Problem. In this lesson, we explore how finite resources clash with unlimited human wants, causing universal scarcity and compelling consumers, workers, firms, and governments to make critical choices. We will also examine the three core economic questions and distinguish between economic goods and free goods.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 1: Vấn đề Kinh tế Cơ bản. Trong bài học này, chúng ta sẽ tìm hiểu cách các nguồn lực hữu hạn đối mặt với nhu cầu vô hạn của con người, dẫn đến sự khan hiếm phổ quát và buộc người tiêu dùng, người lao động, doanh nghiệp và chính phủ phải đưa ra các lựa chọn kinh tế. Chúng ta cũng sẽ tìm hiểu ba câu hỏi kinh tế cốt lõi và phân biệt giữa hàng hóa kinh tế và hàng hóa tự do."
    },
    {
        "id": "sec_nature",
        "title": "1. Bản chất của Vấn đề Kinh tế Cơ bản",
        "selector": "#sec-nature",
        "en": "Section 1 defines the nature of the basic economic problem: finite economic resources are insufficient to satisfy infinite human wants and needs. Scarcity exists everywhere and can never be completely eliminated. Because resources cannot satisfy every desire, society is forced to make fundamental economic choices.",
        "vi": "Mục 1 phân tích bản chất của vấn đề kinh tế cơ bản: nguồn lực kinh tế hữu hạn không thể đáp ứng đầy đủ nhu cầu vô hạn của con người. Sự khan hiếm tồn tại ở mọi nơi và không bao giờ có thể bị loại bỏ hoàn toàn. Do nguồn lực không đủ đáp ứng mọi mong muốn, xã hội bắt buộc phải đưa ra các quyết định lựa chọn kinh tế."
    },
    {
        "id": "card_concept_map",
        "title": "Sơ đồ Khái niệm: Nhu cầu vô hạn, Nguồn lực hữu hạn & Sự khan hiếm",
        "selector": "#card-concept-map",
        "en": "The interactive concept map illustrates the core economic chain: unlimited wants collide with finite resources, generating persistent scarcity. This forces society to make choices by resolving three fundamental questions: what to produce, how to produce, and who to produce for.",
        "vi": "Sơ đồ khái niệm tương tác minh họa chuỗi mắt xích cốt lõi: mong muốn vô hạn va chạm với các nguồn lực hữu hạn, sinh ra sự khan hiếm dai dẳng. Điều này buộc xã hội phải lựa chọn thông qua việc giải quyết ba câu hỏi nền tảng: sản xuất cái gì, sản xuất như thế nào và sản xuất cho ai."
    },
    {
        "id": "sec_contexts",
        "title": "2. Vấn đề Kinh tế Cơ bản trong 4 Hoàn cảnh",
        "selector": "#sec-contexts",
        "en": "Section 2 explores how scarcity impacts four major economic decision-makers. Every agent operates under tight constraints and must prioritize competing desires.",
        "vi": "Mục 2 tìm hiểu cách sự khan hiếm tác động đến bốn chủ thể quyết định kinh tế chính. Mỗi chủ thể đều chịu các ràng buộc nguồn lực và phải sắp xếp thứ tự ưu tiên cho những mục tiêu của mình."
    },
    {
        "id": "card_consumers",
        "title": "🛒 Người tiêu dùng (Consumers)",
        "selector": "#card-consumers",
        "en": "Consumers face limited incomes and savings against unlimited wants for food, technology, and travel. They must prioritize essential necessities and forgo discretionary luxury items.",
        "vi": "Người tiêu dùng đối mặt với thu nhập và tiền tiết kiệm có hạn trước mong muốn vô tận về thực phẩm, đồ công nghệ và du lịch. Họ phải ưu tiên các nhu cầu thiết yếu và hy sinh những mặt hàng xa xỉ."
    },
    {
        "id": "card_workers",
        "title": "👷 Người lao động (Workers)",
        "selector": "#card-workers",
        "en": "Workers face a strict constraint of 24 hours per day and finite physical stamina. They must balance working overtime to maximize wage income against enjoying valuable leisure and family time.",
        "vi": "Người lao động bị giới hạn bởi 24 giờ mỗi ngày và thể lực có hạn. Họ phải cân bằng giữa việc làm thêm giờ để kiếm thêm tiền lương với thời gian quý giá dành cho gia đình và giải trí."
    },
    {
        "id": "card_producers",
        "title": "🏭 Doanh nghiệp / Nhà sản xuất (Producers)",
        "selector": "#card-producers",
        "en": "Producers have limited investment capital, factory space, and machinery. They must decide whether to allocate capital towards manufacturing electric vehicles or traditional petrol vehicles to maximize profit.",
        "vi": "Nhà sản xuất có vốn đầu tư, diện tích nhà xưởng và máy móc hạn chế. Họ phải quyết định phân bổ vốn để sản xuất xe điện hay xe xăng truyền thống nhằm tối đa hóa lợi nhuận."
    },
    {
        "id": "card_governments",
        "title": "🏛️ Chính phủ (Governments)",
        "selector": "#card-governments",
        "en": "Governments collect finite tax revenue and possess borrowing limits. They face critical trade-offs between funding modern healthcare, public education, national defence, and new transportation infrastructure.",
        "vi": "Chính phủ thu ngân sách có hạn từ thuế và bị giới hạn trần nợ công. Họ phải đối mặt với các đánh đổi mang tính chiến lược giữa tài trợ y tế hiện đại, giáo dục công lập, quốc phòng và hạ tầng giao thông mới."
    },
    {
        "id": "sec_questions",
        "title": "3. Ba Câu hỏi Phân bổ Nguồn lực Cơ bản",
        "selector": "#sec-questions",
        "en": "Section 3 addresses the three fundamental questions every economy must resolve: What to produce, deciding the mix of consumer versus capital goods; How to produce, choosing between labor-intensive and capital-intensive methods; and Who to produce for, determining whether goods are distributed by purchasing power or government allocation.",
        "vi": "Mục 3 phân tích ba câu hỏi kinh tế căn bản mà mọi quốc gia phải giải quyết: Sản xuất cái gì, lựa chọn tỷ lệ giữa hàng tiêu dùng và tư liệu sản xuất; Sản xuất như thế nào, lựa chọn giữa phương thức thâm dụng lao động hay thâm dụng vốn; và Sản xuất cho ai, quyết định hàng hóa được phân phối theo sức mua thị trường hay do nhà nước phân bổ."
    },
    {
        "id": "card_three_questions",
        "title": "⚖️ Chi tiết 3 Câu hỏi Kinh tế",
        "selector": "#card-three-questions",
        "en": "The three allocation questions dictate resource deployment: What to produce balances immediate consumption against future investment; How to produce determines production efficiency and technology; and Who to produce for governs wealth and output distribution across society.",
        "vi": "Ba câu hỏi phân bổ định hình cách thức sử dụng nguồn lực: Sản xuất cái gì giúp cân đối giữa tiêu dùng hiện tại và đầu tư tương lai; Sản xuất như thế nào xác định công nghệ và hiệu quả sản xuất; và Sản xuất cho ai chi phối sự phân phối của cải và thành quả kinh tế trong xã hội."
    },
    {
        "id": "sec_distinctions",
        "title": "4. Phân biệt Nhu cầu Thiết yếu vs Mong muốn & Khu vực Kinh tế",
        "selector": "#sec-distinctions",
        "en": "Section 4 highlights key distinctions. Needs are goods and services essential for survival, like water and shelter, whereas wants are discretionary desires that continually expand. In the private sector, individuals own enterprises and seek profit maximisation, whereas the public sector is state-owned and strives to advance social welfare.",
        "vi": "Mục 4 nhấn mạnh các phân biệt quan trọng. Nhu cầu thiết yếu là các hàng hóa, dịch vụ sống còn như nước và chỗ ở, trong khi mong muốn là những nhu cầu tiện ích không ngừng mở rộng. Ở khu vực tư nhân, cá nhân làm chủ doanh nghiệp với mục tiêu tối đa hóa lợi nhuận, còn khu vực công thuộc sở hữu nhà nước hướng đến nâng cao phúc lợi xã hội."
    },
    {
        "id": "card_needs_wants",
        "title": "💧 Nhu cầu thiết yếu vs 📱 Mong muốn",
        "selector": "#card-needs-wants",
        "en": "A need is indispensable for human survival, including clean water, basic food, shelter, and medical care. Wants represent infinite desires for luxury and comfort, such as smartphones, designer clothing, and holidays, which continually evolve as incomes grow.",
        "vi": "Nhu cầu thiết yếu là điều kiện không thể thiếu để sinh tồn, gồm nước sạch, lương thực cơ bản, nhà ở và y tế. Mong muốn là khao khát vô tận về sự tiện nghi và xa xỉ như điện thoại thông minh, quần áo hàng hiệu và du lịch, liên tục phát triển khi thu nhập tăng lên."
    },
    {
        "id": "card_sectors",
        "title": "🏢 Khu vực Tư nhân vs 🏛️ Khu vực Công",
        "selector": "#card-sectors",
        "en": "The private sector is owned by private individuals whose main incentive is profit maximisation, such as commercial retailers and private tech companies. The public sector is governed by the state to provide public services like state schools, police, and hospitals.",
        "vi": "Khu vực tư nhân thuộc sở hữu của tư nhân với mục tiêu tối đa hóa lợi nhuận như các cửa hàng bán lẻ và công ty công nghệ. Khu vực công do nhà nước quản lý nhằm cung ứng các dịch vụ công như trường học công lập, cảnh sát và bệnh viện công."
    },
    {
        "id": "sec_goods",
        "title": "5. Hàng hóa Kinh tế vs Hàng hóa Tự do",
        "selector": "#sec-goods",
        "en": "Section 5 distinguishes between economic goods and free goods. Economic goods are scarce, consume valuable factors of production, carry an opportunity cost, and command a market price. Free goods are abundant gifts of nature, like fresh air and sunlight, involving zero opportunity cost. Crucially, free government services are economic goods, not free goods, because tax resources are used.",
        "vi": "Mục 5 phân biệt hàng hóa kinh tế và hàng hóa tự do. Hàng hóa kinh tế có tính khan hiếm, tiêu tốn các yếu tố sản xuất, có chi phí cơ hội và có giá thị trường. Hàng hóa tự do là quà tặng dồi dào từ thiên nhiên như không khí và ánh nắng, không có chi phí cơ hội. Cần ghi nhớ, các dịch vụ công miễn phí của chính phủ vẫn là hàng hóa kinh tế, không phải hàng hóa tự do, vì tiền thuế và các nguồn lực xã hội đã được sử dụng."
    },
    {
        "id": "card_goods_comparison",
        "title": "📦 Economic Goods vs 🌬️ Free Goods & Lưu ý thi cử",
        "selector": "#card-goods-comparison",
        "en": "Economic goods require scarce resources and incur an opportunity cost when produced. Free goods exist naturally in unlimited supply with zero opportunity cost. In exams, remember that state-provided healthcare is an economic good because scarce tax revenues fund doctors and medical equipment.",
        "vi": "Hàng hóa kinh tế đòi hỏi nguồn lực khan hiếm và phát sinh chi phí cơ hội khi sản xuất. Hàng hóa tự do tồn tại sẵn trong tự nhiên với số lượng không giới hạn và không có chi phí cơ hội. Khi đi thi, hãy nhớ rằng y tế công miễn phí vẫn là hàng hóa kinh tế vì ngân sách thuế có hạn đã được dùng để trả lương bác sĩ và mua trang thiết bị."
    }
]

lec1_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_nature": {"start": 1, "end": 2},
    "sec_contexts": {"start": 3, "end": 7},
    "sec_questions": {"start": 8, "end": 9},
    "sec_distinctions": {"start": 10, "end": 12},
    "sec_goods": {"start": 13, "end": 14}
}

# =====================================================================
# LECTURE 2: The Factors of Production
# =====================================================================
LEC2_ID = "34bbcc7c-6b51-40fd-9585-9eb3c37da582"
LEC2_TITLE = "2. The Factors of Production"

lec2_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 2: Các Yếu tố Sản xuất",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 2: The Factors of Production. In this lesson, we study the four essential productive inputs: land, labour, capital, and enterprise, along with their respective economic rewards. We also analyze the geographical and occupational mobility of these factors and examine how an economy can expand its output through increases in their quantity and quality.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 2: Các Yếu tố Sản xuất. Trong bài học này, chúng ta sẽ tìm hiểu bốn nguồn lực sản xuất thiết yếu: đất đai, lao động, tư bản và doanh nhân, cùng với các phần thưởng kinh tế tương ứng. Chúng ta cũng sẽ phân tích tính linh hoạt về địa lý và nghề nghiệp của các yếu tố này, đồng thời khảo sát cách nền kinh tế mở rộng sản lượng thông qua việc nâng cao số lượng và chất lượng của chúng."
    },
    {
        "id": "sec_factors",
        "title": "1. Bốn Yếu tố Sản xuất và Phần thưởng Kinh tế",
        "selector": "#sec-factors",
        "en": "Section 1 examines the four factors of production. Land encompasses all gifts of nature, earning rent. Labour represents all human physical and mental effort, rewarded by wages. Capital denotes man-made physical resources used to make other goods, earning interest. Enterprise is the risk-taking initiative of the entrepreneur, rewarded with profit.",
        "vi": "Mục 1 phân tích bốn yếu tố sản xuất. Đất đai bao gồm tất cả các tặng phẩm của tự nhiên, nhận tiền thuê. Lao động đại diện cho thể lực và trí lực của con người, được trả công bằng tiền lương. Tư bản là các tài sản vật chất do con người tạo ra để sản xuất hàng hóa khác, nhận tiền lãi. Doanh nhân là sáng kiến và tinh thần dám chịu rủi ro, được thưởng bằng lợi nhuận."
    },
    {
        "id": "card_factors_grid",
        "title": "Sơ đồ 4 Yếu tố: Đất đai, Lao động, Tư bản & Doanh nhân",
        "selector": "#card-factors-grid",
        "en": "The interactive factor map highlights each input: Land provides raw materials and earns rent; Labour applies human skills for wages; Capital provides tools and factories earning interest; and Enterprise coordinates the other three factors to create a viable business earning profit.",
        "vi": "Sơ đồ tương tác làm nổi bật từng yếu tố: Đất đai cung cấp tài nguyên tự nhiên và nhận tiền thuê; Lao động cống hiến kỹ năng và nhận tiền lương; Tư bản cung cấp máy móc, nhà xưởng và nhận tiền lãi; và Doanh nhân điều phối cả ba yếu tố trên để vận hành doanh nghiệp sinh lời."
    },
    {
        "id": "card_capital_distinction",
        "title": "🔍 Phân biệt: Tư bản Thực tế vs Tiền vốn (Capital vs Money)",
        "selector": "#card-capital-distinction",
        "en": "In economics, capital refers strictly to physical capital goods—man-made physical assets like machinery and factories. Money itself is financial capital and not an economic factor of production, because currency cannot physically produce goods; it merely purchases real capital.",
        "vi": "Trong kinh tế học, tư bản chỉ bao gồm tư bản vật chất thực tế—những tài sản vật chất do con người tạo ra như máy móc và nhà xưởng. Tiền bản thân nó là vốn tài chính chứ không phải yếu tố sản xuất, vì tiền không thể tự tạo ra sản phẩm mà chỉ dùng để mua các tư liệu sản xuất thực tế."
    },
    {
        "id": "sec_mobility",
        "title": "2. Tính Linh hoạt của các Yếu tố Sản xuất (Mobility)",
        "selector": "#sec-mobility",
        "en": "Section 2 investigates factor mobility—how easily resources relocate between locations or transfer between different occupations. High mobility allows an economy to adapt swiftly to structural changes and consumer demand shifts.",
        "vi": "Mục 2 tìm hiểu tính linh hoạt của các yếu tố sản xuất—mức độ dễ dàng khi nguồn lực di chuyển giữa các địa phương hoặc chuyển đổi giữa các ngành nghề. Tính linh hoạt cao giúp nền kinh tế thích ứng nhanh chóng với các thay đổi cơ cấu và sự dịch chuyển của nhu cầu người tiêu dùng."
    },
    {
        "id": "card_mobility_types",
        "title": "🏃‍♂️ Độ linh hoạt Địa lý và Nghề nghiệp của 4 Yếu tố",
        "selector": "#card-mobility-types",
        "en": "Land is geographically immobile but occupationally mobile. Labour faces geographical hurdles like housing costs, and occupational hurdles like training deficits. Capital varies: computers are highly mobile, while blast furnaces are immovable. Enterprise is highly mobile across both dimensions.",
        "vi": "Đất đai bất động về mặt địa lý nhưng có thể chuyển đổi mục đích sử dụng. Lao động gặp rào cản địa lý như chi phí nhà ở và rào cản nghề nghiệp do thiếu kỹ năng. Tư bản rất đa dạng: máy tính rất linh hoạt nhưng lò luyện kim thì bất động. Doanh nhân có tính linh hoạt rất cao ở cả hai khía cạnh."
    },
    {
        "id": "sec_quant_qual",
        "title": "3. Số lượng và Chất lượng của các Yếu tố Sản xuất",
        "selector": "#sec-quant-qual",
        "en": "Section 3 analyzes how economies expand output by increasing factor quantity or enhancing factor quality. Quantity increases via resource discoveries, investment, and immigration. Quality rises through education, technical training, and technological innovation.",
        "vi": "Mục 3 phân tích cách nền kinh tế mở rộng sản lượng bằng cách tăng số lượng hoặc nâng cao chất lượng của các yếu tố sản xuất. Số lượng tăng lên nhờ phát hiện tài nguyên, đầu tư và nhập cư. Chất lượng cải thiện thông qua giáo dục, đào tạo tay nghề và đổi mới công nghệ."
    },
    {
        "id": "card_quant_qual_table",
        "title": "📈 Bảng Tổng hợp Biến động Số lượng & Chất lượng",
        "selector": "#card-quant-qual-table",
        "en": "Our comprehensive table shows that land quality improves with irrigation, labour quality rises with higher healthcare and schooling, capital quality advances through automation and AI, and enterprise improves through executive training and mentorship.",
        "vi": "Bảng tổng hợp chi tiết cho thấy chất lượng đất đai được nâng cao nhờ hệ thống tưới tiêu, chất lượng lao động tăng lên nhờ y tế và giáo dục, chất lượng tư bản tiến bộ nhờ tự động hóa và AI, còn năng lực doanh nhân được hoàn thiện qua đào tạo và kinh nghiệm quản trị."
    }
]

lec2_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_factors": {"start": 1, "end": 3},
    "sec_mobility": {"start": 4, "end": 5},
    "sec_quant_qual": {"start": 6, "end": 7}
}

# =====================================================================
# LECTURE 3: Opportunity Cost
# =====================================================================
LEC3_ID = "9b0e6a87-ed26-43bb-a20c-ffa636f9ef11"
LEC3_TITLE = "3. Opportunity Cost"

lec3_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 3: Chi phí Cơ hội",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 3: Opportunity Cost. In this lesson, we master the fundamental definition of opportunity cost as the next best alternative forgone when making a decision. We examine how this concept influences consumers, workers, firms, and governments, and clarify common exam pitfalls.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 3: Chi phí Cơ hội. Trong bài học này, chúng ta sẽ nắm vững định nghĩa cốt lõi của chi phí cơ hội là phương án thay thế tốt nhất bị bỏ qua khi đưa ra quyết định. Chúng ta sẽ xem xét cách khái niệm này chi phối người tiêu dùng, người lao động, doanh nghiệp và chính phủ, đồng thời giải quyết các bẫy thường gặp trong kỳ thi."
    },
    {
        "id": "sec_definition",
        "title": "1. Định nghĩa Chuẩn của Chi phí Cơ hội",
        "selector": "#sec-definition",
        "en": "Section 1 introduces the Cambridge standard definition: Opportunity cost is the cost of the next best alternative forgone when making a decision. Because economic resources are scarce, committing resources to one use automatically requires sacrificing the benefits of the alternative option.",
        "vi": "Mục 1 giới thiệu định nghĩa chuẩn Cambridge: Chi phí cơ hội là chi phí của phương án thay thế tốt nhất bị bỏ qua khi đưa ra một quyết định. Do nguồn lực kinh tế khan hiếm, việc dành nguồn lực cho một mục đích đồng nghĩa với việc bắt buộc phải hy sinh lợi ích của phương án thay thế tiếp theo."
    },
    {
        "id": "card_definition",
        "title": "⚖️ Định nghĩa & Các Ví dụ Thực tế Sinh động",
        "selector": "#card-definition",
        "en": "Everyday examples demonstrate the concept: for a graduate attending university, the opportunity cost is full-time wage income forgone; for a government building an airport, it is the public hospitals that cannot be funded; and for a farmer growing wheat, it is the yield of soybeans sacrificed.",
        "vi": "Các ví dụ thực tế chứng minh khái niệm này: đối với một sinh viên học đại học, chi phí cơ hội là khoản tiền lương đi làm toàn thời gian bị mất; đối với chính phủ xây sân bay, đó là các bệnh viện công không đủ tiền xây; và với người nông dân trồng lúa mì, đó là sản lượng đậu tương bị bỏ qua."
    },
    {
        "id": "sec_decision_making",
        "title": "2. Chi phí Cơ hội trong Quyết định Kinh tế",
        "selector": "#sec-decision-making",
        "en": "Section 2 illustrates how opportunity cost guides economic agents. Consumers trade off spending on immediate luxuries against future savings. Workers trade off extra overtime earnings against leisure. Producers trade off launching new product lines against upgrading current machinery. Governments trade off funding defence against spending on healthcare and schools.",
        "vi": "Mục 2 minh họa cách chi phí cơ hội định hướng các chủ thể kinh tế. Người tiêu dùng đánh đổi giữa mua đồ xa xỉ với tiền tiết kiệm tương lai. Người lao động đánh đổi giữa tiền làm thêm giờ với sự nghỉ ngơi. Doanh nghiệp đánh đổi giữa ra mắt sản phẩm mới với nâng cấp dây chuyền cũ. Chính phủ đánh đổi giữa chi cho quốc phòng với đầu tư cho y tế và trường học."
    },
    {
        "id": "card_agent_tradeoffs",
        "title": "👥 Sơ đồ Tương tác 4 Chủ thể: Đánh đổi & Quyết định",
        "selector": "#card-agent-tradeoffs",
        "en": "Our interactive decision map shows the specific dilemmas: consumers face income limits; workers face 24-hour time constraints; firms face investment capital limits; and governments face finite tax revenues. Every choice carries an inescapable opportunity cost.",
        "vi": "Sơ đồ quyết định tương tác thể hiện rõ các thế tiến thoái lưỡng nan: người tiêu dùng bị giới hạn thu nhập; người lao động bị giới hạn quỹ thời gian 24 giờ; doanh nghiệp bị giới hạn vốn đầu tư; và chính phủ bị giới hạn bởi ngân sách thuế. Mọi lựa chọn đều đi kèm một chi phí cơ hội không thể tránh khỏi."
    },
    {
        "id": "sec_pitfalls",
        "title": "3. Nguyên lý Trọng tâm & Bẫy Thi cử Cần tránh",
        "selector": "#sec-pitfalls",
        "en": "Section 3 highlights crucial principles for exam success. First, opportunity cost refers only to the single next best alternative, not all discarded options combined. Second, it includes non-monetary sacrifices such as lost time and leisure. Third, free goods like sunlight involve zero opportunity cost because their use deprives no one else.",
        "vi": "Mục 3 nhấn mạnh các nguyên tắc then chốt để đạt điểm cao trong kỳ thi. Thứ nhất, chi phí cơ hội chỉ là một phương án thay thế tốt nhất duy nhất, không phải tổng gộp của tất cả các phương án bị bỏ. Thứ hai, nó bao gồm cả các hy sinh phi tiền tệ như thời gian và sự thư giãn. Thứ ba, hàng hóa tự do như ánh nắng mặt trời có chi phí cơ hội bằng không vì việc sử dụng chúng không tước đoạt cơ hội của ai khác."
    }
]

lec3_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_definition": {"start": 1, "end": 2},
    "sec_decision_making": {"start": 3, "end": 4},
    "sec_pitfalls": {"start": 5, "end": 5}
}

# =====================================================================
# LECTURE 4: Production Possibility Curve
# =====================================================================
LEC4_ID = "9d5f779b-5254-48ed-8284-3918eaacd579"
LEC4_TITLE = "4. Production Possibility Curve"

lec4_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4: Đường Giới hạn Khả năng Sản xuất (PPC)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 4: The Production Possibility Curve, or PPC. In this lesson, we explore how the PPC graphically models resource scarcity, opportunity cost, and productive efficiency. We analyze movements along the curve, contrast bowed-out versus straight-line curves, and examine the causes of outward and inward shifts representing economic growth and decline.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 4: Đường Giới hạn Khả năng Sản xuất (PPC). Trong bài học này, chúng ta sẽ tìm hiểu cách đồ thị PPC mô hình hóa sự khan hiếm nguồn lực, chi phí cơ hội và hiệu quả sản xuất. Chúng ta sẽ phân tích sự dịch chuyển dọc theo đường cong, so sánh đường cong lồi và đường thẳng, đồng thời khảo sát các nguyên nhân làm dịch chuyển đường PPC ra ngoài hoặc vào trong."
    },
    {
        "id": "sec_ppc_intro",
        "title": "1. Khái niệm Đường Giới hạn Khả năng Sản xuất (PPC)",
        "selector": "#sec-ppc-intro",
        "en": "Section 1 defines the PPC as the boundary illustrating the maximum combinations of two goods an economy can produce when all resources are fully and efficiently employed. It maps the frontier of national productive capacity at a given point in time.",
        "vi": "Mục 1 định nghĩa đường PPC là đường ranh giới thể hiện các tổ hợp sản lượng tối đa của hai loại hàng hóa mà một nền kinh tế có thể sản xuất được khi sử dụng toàn bộ nguồn lực một cách đầy đủ và hiệu quả nhất. Nó xác định giới hạn năng lực sản xuất của quốc gia tại một thời điểm nhất định."
    },
    {
        "id": "card_ppc_points",
        "title": "📈 Sơ đồ Tương tác PPC: Điểm Dưới, Trên và Ngoài Đường Cong",
        "selector": "#card-ppc-points",
        "en": "Our interactive diagram demonstrates three crucial positions: Point A inside represents inefficiency and unemployed resources, where output can grow with zero opportunity cost; Point B on the boundary shows productive efficiency and full employment; and Point C beyond the curve is unattainable in the short run without economic growth.",
        "vi": "Sơ đồ tương tác minh họa ba vị trí trọng yếu: Điểm A nằm bên trong thể hiện sự kém hiệu quả và nguồn lực nhàn rỗi, nơi sản lượng có thể tăng mà không tốn chi phí cơ hội; Điểm B nằm trên đường cong thể hiện hiệu quả sản xuất và toàn dụng nguồn lực; còn Điểm C nằm bên ngoài là bất khả thi trong ngắn hạn nếu không có tăng trưởng kinh tế."
    },
    {
        "id": "sec_movements",
        "title": "2. Di chuyển Dọc theo Đường PPC (Movements along a PPC)",
        "selector": "#sec-movements",
        "en": "Section 2 investigates movements along the PPC. Moving along the curve reflects reallocating scarce resources from one industry to another. Gaining more consumer goods requires sacrificing some capital goods, illustrating the principle of opportunity cost under full employment.",
        "vi": "Mục 2 khảo sát sự di chuyển dọc theo đường PPC. Việc di chuyển trên đường cong phản ánh việc tái phân bổ nguồn lực khan hiếm từ ngành này sang ngành khác. Để có thêm hàng tiêu dùng, bắt buộc phải hy sinh một lượng tư liệu sản xuất nhất định, minh chứng cho nguyên lý chi phí cơ hội trong điều kiện toàn dụng nguồn lực."
    },
    {
        "id": "card_movements",
        "title": "🔄 Tái phân bổ Nguồn lực & Hai Điều kiện Vận hành trên PPC",
        "selector": "#card-movements",
        "en": "An economy operates strictly on its PPC when two conditions are fulfilled: full employment of all available factors, leaving zero involuntary unemployment; and productive efficiency, ensuring zero waste in production techniques.",
        "vi": "Nền kinh tế chỉ vận hành chuẩn xác trên đường PPC khi thỏa mãn hai điều kiện: toàn dụng mọi nguồn lực sẵn có, không có lao động hay máy móc bị thất nghiệp ngoài ý muốn; và đạt hiệu quả sản xuất cao nhất, đảm bảo quy trình không bị lãng phí."
    },
    {
        "id": "sec_shape",
        "title": "3. Hình dạng Đường PPC: Chi phí Cơ hội Tăng dần vs Không đổi",
        "selector": "#sec-shape",
        "en": "Section 3 analyzes the shape of the PPC. A bowed-out curve, concave to the origin, reflects increasing opportunity cost because economic factors are imperfectly substitutable between industries. A straight-line PPC indicates constant opportunity cost, meaning resources are perfectly adaptable and equally suited to producing both goods.",
        "vi": "Mục 3 phân tích hình dạng đường PPC. Đường cong hình cánh cung lồi ra ngoài phản ánh chi phí cơ hội tăng dần do các yếu tố sản xuất không thể thay thế hoàn hảo cho nhau giữa các ngành. Đường PPC dạng đường thẳng thể hiện chi phí cơ hội không đổi, hàm ý các nguồn lực có thể thích nghi hoàn hảo và phù hợp như nhau để sản xuất cả hai loại hàng."
    },
    {
        "id": "sec_shifts",
        "title": "4. Dịch chuyển Đường PPC: Tăng trưởng Kinh tế & Suy giảm",
        "selector": "#sec-shifts",
        "en": "Section 4 explains shifts of the entire PPC. An outward shift signifies potential economic growth, driven by new resource discoveries, skilled immigration, better education, and automated technology. An inward shift indicates depleted productive capacity, caused by natural disasters, armed conflicts, or severe brain drain.",
        "vi": "Mục 4 giải thích sự dịch chuyển của toàn bộ đường PPC. Dịch chuyển ra ngoài biểu thị tăng trưởng kinh tế tiềm năng nhờ phát hiện tài nguyên mới, lao động nhập cư tay nghề cao, giáo dục cải thiện và công nghệ tự động hóa. Dịch chuyển vào trong thể hiện năng lực sản xuất bị suy giảm do thiên tai, chiến tranh tàn phá hoặc tình trạng chảy máu chất xám nghiêm trọng."
    },
    {
        "id": "card_shifts_comparison",
        "title": "🚀 Phân biệt Tăng trưởng Thực tế (Actual) vs Tăng trưởng Tiềm năng (Potential)",
        "selector": "#card-shifts-comparison",
        "en": "In exams, carefully distinguish actual growth from potential growth. Actual growth is moving from an internal point of unemployment towards the curve, putting idle factories to work. Potential growth is the outward expansion of the boundary itself, increasing the nation's maximum productive ceiling.",
        "vi": "Khi làm bài thi, cần phân biệt cẩn thận giữa tăng trưởng thực tế và tăng trưởng tiềm năng. Tăng trưởng thực tế là sự di chuyển từ một điểm thất nghiệp bên trong tiến dần ra đường biên, đưa các nhà xưởng nhàn rỗi vào vận hành. Tăng trưởng tiềm năng là sự mở rộng của chính đường biên ra phía ngoài, nâng cao mức trần năng lực sản xuất tối đa của cả quốc gia."
    }
]

lec4_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_ppc_intro": {"start": 1, "end": 2},
    "sec_movements": {"start": 3, "end": 4},
    "sec_shape": {"start": 5, "end": 5},
    "sec_shifts": {"start": 6, "end": 7}
}

ALL_TOPIC1_LECTURES = [
    ("1", LEC1_ID, COURSE_TITLE, LEC1_TITLE, lec1_segments, lec1_major_sections),
    ("2", LEC2_ID, COURSE_TITLE, LEC2_TITLE, lec2_segments, lec2_major_sections),
    ("3", LEC3_ID, COURSE_TITLE, LEC3_TITLE, lec3_segments, lec3_major_sections),
    ("4", LEC4_ID, COURSE_TITLE, LEC4_TITLE, lec4_segments, lec4_major_sections),
]

async def main():
    print("=================================================================")
    print("GENERATING AUDIO & MANIFEST FOR TOPIC 1 (LECTURES 1 - 4)")
    print("=================================================================")
    for code, lid, course, title, segments, major_sections in ALL_TOPIC1_LECTURES:
        await process_lecture_audio(code, lid, course, title, segments, major_sections, subject='economics')
    print("\n✅ ALL TOPIC 1 AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
