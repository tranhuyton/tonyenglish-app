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
# LECTURE 5: Microeconomics and Macroeconomics
# =====================================================================
LEC5_ID = "d6e6ad94-1106-43ae-b37c-1b36832f03e6"
LEC5_TITLE = "5. Microeconomics and Macroeconomics"

lec5_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 5: Kinh tế Vi mô và Kinh tế Vĩ mô",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 5: Microeconomics and Macroeconomics. In this foundational lesson for Topic 2, we distinguish between the study of individual decision-makers and markets in microeconomics, and the aggregate economy in macroeconomics. We also examine the primary aims of households, firms, and the government.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 5: Kinh tế Vi mô và Kinh tế Vĩ mô. Trong bài học nền tảng của Chủ đề 2 này, chúng ta sẽ phân biệt giữa việc nghiên cứu các chủ thể và thị trường riêng lẻ trong kinh tế vi mô, với việc phân tích toàn bộ nền kinh tế tổng thể trong kinh tế vĩ mô. Chúng ta cũng sẽ tìm hiểu mục tiêu cốt lõi của hộ gia đình, doanh nghiệp và chính phủ."
    },
    {
        "id": "sec_micro_macro",
        "title": "1. Khái niệm & Phân biệt Kinh tế Vi mô và Vĩ mô",
        "selector": "#sec-micro-macro",
        "en": "Section 1 divides economic analysis into microeconomics and macroeconomics. Microeconomics examines individual consumers, workers, firms, and specific markets like housing or agriculture. Macroeconomics studies the economy as a whole, focusing on national output, inflation, unemployment, and the balance of payments.",
        "vi": "Mục 1 chia phân tích kinh tế thành kinh tế vi mô và kinh tế vĩ mô. Kinh tế vi mô nghiên cứu các cá nhân tiêu dùng, người lao động, doanh nghiệp và các thị trường cụ thể như nhà ở hoặc nông sản. Kinh tế vĩ mô nghiên cứu toàn bộ nền kinh tế, tập trung vào tổng sản lượng quốc gia, lạm phát, tỷ lệ thất nghiệp và cán cân thanh toán."
    },
    {
        "id": "card_micro",
        "title": "🔬 Kinh tế Vi mô (Microeconomics)",
        "selector": "#card-micro",
        "en": "Microeconomics focuses on small-scale economic units. It investigates how individual consumers allocate their income, how firms set prices and output to maximize profits, and how supply and demand interact in single commodity markets.",
        "vi": "Kinh tế vi mô tập trung vào các đơn vị kinh tế quy mô nhỏ. Lĩnh vực này khảo sát cách người tiêu dùng phân bổ thu nhập, cách doanh nghiệp định giá và sản lượng để tối đa hóa lợi nhuận, cũng như cách cung cầu tương tác trên từng thị trường hàng hóa riêng lẻ."
    },
    {
        "id": "card_macro",
        "title": "🌍 Kinh tế Vĩ mô (Macroeconomics)",
        "selector": "#card-macro",
        "en": "Macroeconomics evaluates aggregate national performance. Key topics include economic growth measured by Gross Domestic Product, government policies like fiscal and monetary interventions, exchange rates, and international trade.",
        "vi": "Kinh tế vĩ mô đánh giá hiệu quả hoạt động tổng thể của cả quốc gia. Các chủ đề trọng tâm bao gồm tăng trưởng kinh tế đo bằng Tổng sản phẩm quốc nội GDP, các chính sách tài khóa và tiền tệ của chính phủ, tỷ giá hối đoái và thương mại quốc tế."
    },
    {
        "id": "card_criteria_table",
        "title": "📊 Bảng So sánh Tiêu chí Vi mô vs Vĩ mô",
        "selector": "#card-criteria-table",
        "en": "Our comparison table clarifies the differences: microeconomics investigates individual prices and single industry wages, while macroeconomics addresses the general price level, national unemployment, and economic stability.",
        "vi": "Bảng so sánh làm rõ các tiêu chuẩn: kinh tế vi mô khảo sát giá cả của từng mặt hàng và tiền lương trong từng ngành; trong khi kinh tế vĩ mô giải quyết mức giá chung của nền kinh tế, tỷ lệ thất nghiệp toàn quốc và sự ổn định kinh tế."
    },
    {
        "id": "sec_decision_makers",
        "title": "2. Ba Chủ thể Kinh tế Quyết định và Mục tiêu Cốt lõi",
        "selector": "#sec-decision-makers",
        "en": "Section 2 identifies the three main economic decision-makers and their economic aims: Households seek to maximize utility and living standards; Firms aim to maximize profits; and the Government strives to maximize overall social welfare.",
        "vi": "Mục 2 xác định ba chủ thể quyết định kinh tế chính và mục tiêu cốt lõi của họ: Hộ gia đình tìm cách tối đa hóa mức độ hài lòng và mức sống; Doanh nghiệp hướng tới tối đa hóa lợi nhuận; và Chính phủ phấn đấu tối đa hóa phúc lợi xã hội nói chung."
    },
    {
        "id": "card_households",
        "title": "🛒 Hộ gia đình / Người tiêu dùng",
        "selector": "#card-households",
        "en": "Households allocate disposable income to purchase goods and services that generate maximum satisfaction and utility, while providing labor to earn wages.",
        "vi": "Hộ gia đình phân bổ thu nhập khả dụng để mua hàng hóa, dịch vụ mang lại mức độ thỏa mãn tối đa, đồng thời cung ứng sức lao động để kiếm tiền lương."
    },
    {
        "id": "card_firms",
        "title": "🏭 Doanh nghiệp / Nhà sản xuất",
        "selector": "#card-firms",
        "en": "Firms combine land, labour, and capital to produce goods. Their overarching commercial objective is profit maximisation, achieved when total revenue exceeds total costs by the widest margin.",
        "vi": "Doanh nghiệp kết hợp đất đai, lao động và tư bản để sản xuất hàng hóa. Mục tiêu thương mại bao trùm của họ là tối đa hóa lợi nhuận, đạt được khi tổng doanh thu vượt trên tổng chi phí ở mức cao nhất."
    },
    {
        "id": "card_government",
        "title": "🏛️ Chính phủ (Government)",
        "selector": "#card-government",
        "en": "Governments aim to maximize social welfare. They intervene to correct market failure, provide public goods like policing and healthcare, and ensure equitable resource distribution.",
        "vi": "Chính phủ hướng tới mục tiêu tối đa hóa phúc lợi xã hội. Họ can thiệp để khắc phục thất bại thị trường, cung ứng hàng hóa công như an ninh trật tự và y tế, đồng thời đảm bảo sự phân phối nguồn lực công bằng."
    }
]

lec5_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_micro_macro": {"start": 1, "end": 4},
    "sec_decision_makers": {"start": 5, "end": 8}
}

# =====================================================================
# LECTURE 6: The Role of Market in Allocating Resources
# =====================================================================
LEC6_ID = "71e51517-0174-49fc-9796-802abee0c5a5"
LEC6_TITLE = "6. The Role of Market in Allocating Resources"

lec6_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 6: Vai trò của Thị trường trong Phân bổ Nguồn lực",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 6: The Role of the Market in Allocating Resources. In this lesson, we explore how markets coordinate buyers and sellers, how the price mechanism signals shortages and surpluses, and how different economic systems—planned, mixed, and free market—resolve the three core allocation questions.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 6: Vai trò của Thị trường trong Phân bổ Nguồn lực. Trong bài học này, chúng ta sẽ khám phá cách thị trường kết nối người mua và người bán, cách cơ chế giá phát tín hiệu về tình trạng dư thừa và khan hiếm, và cách các hệ thống kinh tế khác nhau—kế hoạch hóa, hỗn hợp và thị trường tự do—giải quyết ba câu hỏi phân bổ nguồn lực."
    },
    {
        "id": "sec_market_work",
        "title": "1. Khái niệm Thị trường & Cách thức Vận hành",
        "selector": "#sec-market-work",
        "en": "Section 1 defines a market as any arrangement bringing buyers and sellers together to agree on an exchange of goods or services. Markets operate across physical retail stores, 24/7 digital e-commerce platforms, and factor markets for labour and capital.",
        "vi": "Mục 1 định nghĩa thị trường là bất kỳ cơ chế nào kết nối người mua và người bán để thống nhất việc trao đổi hàng hóa hoặc dịch vụ. Thị trường hoạt động đa dạng qua các cửa hàng bán lẻ truyền thống, các sàn thương mại điện tử 24/7 và thị trường yếu tố sản xuất cho lao động và vốn."
    },
    {
        "id": "card_market_types",
        "title": "🏪 Phân loại: Thị trường Vật lý, Trực tuyến & Thị trường Yếu tố",
        "selector": "#card-market-types",
        "en": "Physical markets involve face-to-face transactions in retail shops; online markets connect global users electronically; and factor markets trade productive inputs like raw materials, commercial loans, and skilled labour.",
        "vi": "Thị trường vật lý bao gồm các giao dịch trực tiếp tại cửa hàng; thị trường trực tuyến kết nối người dùng toàn cầu qua mạng internet; còn thị trường yếu tố sản xuất là nơi giao dịch các nguồn lực đầu vào như nguyên vật liệu, vốn vay thương mại và lao động tay nghề cao."
    },
    {
        "id": "card_participants",
        "title": "⚖️ Vai trò của Người mua (Demand) và Người bán (Supply)",
        "selector": "#card-participants",
        "en": "Buyers represent market demand seeking to maximize utility within their income constraints. Sellers represent market supply aiming to maximize profits where total revenues exceed total costs.",
        "vi": "Người mua đại diện cho cầu thị trường với mục tiêu tối đa hóa mức độ thỏa mãn trong giới hạn thu nhập. Người bán đại diện cho cung thị trường với mục tiêu tối đa hóa lợi nhuận khi tổng doanh thu vượt trên tổng chi phí."
    },
    {
        "id": "sec_allocation_decisions",
        "title": "2. Ba Quyết định Phân bổ Nguồn lực Cốt lõi",
        "selector": "#sec-allocation-decisions",
        "en": "Section 2 revisits the three fundamental questions. In resolving how to produce, economies choose between capital-intensive production relying on machinery and automation, and labour-intensive production relying on manual human effort.",
        "vi": "Mục 2 xem xét lại ba câu hỏi phân bổ căn bản. Khi giải quyết câu hỏi sản xuất như thế nào, nền kinh tế lựa chọn giữa sản xuất thâm dụng vốn dựa vào máy móc, tự động hóa; và sản xuất thâm dụng lao động dựa vào bàn tay con người."
    },
    {
        "id": "card_how_to_produce",
        "title": "🚜 Thâm dụng Vốn vs 👷‍♂️ Thâm dụng Lao động",
        "selector": "#card-how-to-produce",
        "en": "Capital-intensive production uses a high proportion of advanced machinery and robotics, offering high consistency and lower long-run unit costs. Labour-intensive production uses predominantly manual workers, providing flexibility and customization.",
        "vi": "Sản xuất thâm dụng vốn sử dụng tỷ trọng lớn máy móc hiện đại và robot, mang lại tính đồng bộ cao và chi phí đơn vị thấp trong dài hạn. Sản xuất thâm dụng lao động sử dụng chủ yếu công nhân thủ công, đem lại sự linh hoạt và khả năng cá nhân hóa sản phẩm."
    },
    {
        "id": "sec_price_mechanism",
        "title": "3. Cơ chế Giá và Phân bổ Nguồn lực",
        "selector": "#sec-price-mechanism",
        "en": "Section 3 examines the price mechanism—the Adam Smith 'invisible hand'. Prices guide resource allocation through three core functions: the signalling function, the incentive function, and the rationing function.",
        "vi": "Mục 3 phân tích cơ chế giá—được ví như 'bàn tay vô hình' của Adam Smith. Giá cả định hướng việc phân bổ nguồn lực qua ba chức năng cốt lõi: chức năng phát tín hiệu, chức năng khuyến khích và chức năng phân phối hạn ngạch."
    },
    {
        "id": "card_price_functions",
        "title": "🚦 3 Chức năng của Giá: Phát tín hiệu, Khuyến khích & Phân phối",
        "selector": "#card-price-functions",
        "en": "Prices perform three essential jobs: Prices signal changing consumer tastes; price increases incentivize producers to supply more output to earn higher profits; and high prices ration scarce goods to consumers willing and able to pay.",
        "vi": "Giá cả đảm nhận ba nhiệm vụ thiết yếu: Giá phát tín hiệu về thị hiếu tiêu dùng thay đổi; giá tăng khuyến khích nhà sản xuất cung ứng nhiều hàng hơn để tìm kiếm lợi nhuận; và giá cao sẽ phân phối hạn ngạch lượng hàng khan hiếm cho những người có khả năng và sẵn sàng chi trả."
    },
    {
        "id": "card_price_in_action",
        "title": "🔍 Cơ chế Giá trong Thực tế: Phân tích Dịch chuyển Cung Cầu",
        "selector": "#card-price-in-action",
        "en": "When consumer demand surges, higher prices signal profitability, inducing firms to reallocate land, labour, and capital into that expanding industry until market balance is restored.",
        "vi": "Khi nhu cầu tiêu dùng tăng đột biến, mức giá cao hơn sẽ phát tín hiệu về cơ hội sinh lời, thu hút các doanh nghiệp tái phân bổ đất đai, lao động và vốn vào ngành đang mở rộng đó cho đến khi thiết lập trạng thái cân bằng mới."
    },
    {
        "id": "sec_economic_systems",
        "title": "4. Quang phổ các Hệ thống Kinh tế",
        "selector": "#sec-economic-systems",
        "en": "Section 4 surveys the economic systems spectrum. In a planned economy, the state makes all allocation decisions. In a free market, private enterprise and price mechanism govern entirely. In a mixed economy, market forces and government intervention work together.",
        "vi": "Mục 4 khảo sát quang phổ các hệ thống kinh tế. Trong nền kinh tế chỉ huy, nhà nước quyết định mọi việc phân bổ. Trong nền kinh tế thị trường tự do, doanh nghiệp tư nhân và cơ chế giá quyết định hoàn toàn. Trong nền kinh tế hỗn hợp, lực lượng thị trường và sự can thiệp của chính phủ cùng song hành."
    },
    {
        "id": "card_economic_spectrum",
        "title": "⚖️ So sánh Kinh tế Chỉ huy, Hỗn hợp & Thị trường Tự do",
        "selector": "#card-economic-spectrum",
        "en": "Planned economies eliminate wasteful competition but suffer shortages and inefficiency. Free markets maximize dynamism and choice but cause inequality and ignore externalities. Mixed economies combine private efficiency with public protection.",
        "vi": "Kinh tế chỉ huy loại bỏ cạnh tranh lãng phí nhưng dễ rơi vào tình trạng thiếu hụt hàng hóa và trì trệ. Kinh tế thị trường tự do tối đa hóa sự năng động và đa dạng nhưng gây bất bình đẳng và bỏ qua ngoại ứng. Kinh tế hỗn hợp kết hợp sự hiệu quả của tư nhân với sự bảo trợ của nhà nước."
    }
]

lec6_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_market_work": {"start": 1, "end": 3},
    "sec_allocation_decisions": {"start": 4, "end": 5},
    "sec_price_mechanism": {"start": 6, "end": 8},
    "sec_economic_systems": {"start": 9, "end": 10}
}

# =====================================================================
# LECTURE 7: Demand
# =====================================================================
LEC7_ID = "06450a33-0477-4bd2-9d1b-4e424f8e973d"
LEC7_TITLE = "7. Demand"

lec7_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 7: Cầu (Demand)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 7: Demand. In this lesson, we define effective demand and the law of demand, distinguish movements along the demand curve from shifts of the curve, and analyze the key non-price determinants that increase or decrease consumer demand.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 7: Cầu (Demand). Trong bài học này, chúng ta sẽ định nghĩa cầu có khả năng thanh toán và quy luật cầu, phân biệt sự di chuyển dọc theo đường cầu với sự dịch chuyển của toàn bộ đường cầu, đồng thời phân tích các yếu tố phi giá làm tăng hoặc giảm lượng cầu tiêu dùng."
    },
    {
        "id": "sec_demand_intro",
        "title": "1. Khái niệm Cầu & Quy luật Cầu (The Law of Demand)",
        "selector": "#sec-demand-intro",
        "en": "Section 1 defines demand in economics as effective demand—the willingness and financial ability of consumers to buy a good at various prices over a given period. The Law of Demand states that as price rises, quantity demanded falls, ceteris paribus, creating a downward-sloping curve.",
        "vi": "Mục 1 định nghĩa cầu trong kinh tế học là cầu có khả năng thanh toán—sự sẵn sàng và khả năng chi trả của người tiêu dùng để mua một hàng hóa ở các mức giá khác nhau trong một khoảng thời gian nhất định. Quy luật Cầu chỉ ra rằng khi giá tăng thì lượng cầu giảm (trong điều kiện các yếu tố khác không đổi), tạo nên đường cầu dốc xuống."
    },
    {
        "id": "card_law_of_demand",
        "title": "⚖️ Quy luật Cầu & Cầu Cá nhân vs Cầu Thị trường",
        "selector": "#card-law-of-demand",
        "en": "Individual demand reflects one buyer's purchases, while market demand is the horizontal sum of all individual demands at each price level. The downward slope reflects the substitution effect and the income effect.",
        "vi": "Cầu cá nhân phản ánh lượng mua của một người tiêu dùng, còn cầu thị trường là tổng theo chiều ngang của tất cả các mức cầu cá nhân tại từng mức giá. Độ dốc đi xuống phản ánh hiệu ứng thay thế và hiệu ứng thu nhập."
    },
    {
        "id": "sec_movements",
        "title": "2. Di chuyển Dọc theo Đường Cầu (Movements along a Demand Curve)",
        "selector": "#sec-movements",
        "en": "Section 2 investigates movements along the curve, caused strictly by changes in the good's own price. A price rise causes a contraction in demand; a price fall causes an extension in demand.",
        "vi": "Mục 2 khảo sát sự di chuyển dọc theo đường cầu, chỉ xảy ra khi giá của chính hàng hóa đó thay đổi. Khi giá tăng sẽ gây ra sự co hẹp của cầu; khi giá giảm sẽ gây ra sự mở rộng của cầu."
    },
    {
        "id": "card_movements",
        "title": "📉 Co hẹp Cầu (Contraction) vs 🟢 Mở rộng Cầu (Extension)",
        "selector": "#card-movements",
        "en": "Remember for exams: when the price of the good itself changes, you move ALONG the existing curve. It is called a change in quantity demanded, not a change in demand.",
        "vi": "Cần nhớ kỹ khi làm bài thi: khi giá của chính sản phẩm thay đổi, chúng ta DI CHUYỂN DỌC trên đường cầu hiện có. Đây được gọi là sự thay đổi lượng cầu, chứ không phải sự thay đổi của cầu."
    },
    {
        "id": "sec_shifts",
        "title": "3. Dịch chuyển Toàn bộ Đường Cầu (Shifts in the Demand Curve)",
        "selector": "#sec-shifts",
        "en": "Section 3 explains shifts of the entire curve, caused by non-price factors. A rightward shift represents an increase in demand at all prices; a leftward shift represents a decrease in demand.",
        "vi": "Mục 3 giải thích sự dịch chuyển của toàn bộ đường cầu, do các yếu tố phi giá gây ra. Dịch chuyển sang phải thể hiện cầu tăng ở mọi mức giá; dịch chuyển sang trái thể hiện cầu giảm."
    },
    {
        "id": "sec_determinants",
        "title": "4. Các Yếu tố Phi giá Xác định Cầu (Non-Price Determinants)",
        "selector": "#sec-determinants",
        "en": "Section 4 details non-price determinants: consumer disposable income, prices of substitutes and complements, consumer tastes and advertising, demographic changes, interest rates, and weather conditions.",
        "vi": "Mục 4 trình bày chi tiết các yếu tố phi giá: thu nhập khả dụng của người tiêu dùng, giá của hàng hóa thay thế và bổ sung, thị hiếu và quảng cáo, sự thay đổi dân số, lãi suất vay và điều kiện thời tiết."
    },
    {
        "id": "card_determinants",
        "title": "🧠 6 Yếu tố Dịch chuyển Cầu: Thu nhập, Hàng thay thế, Thị hiếu...",
        "selector": "#card-determinants",
        "en": "For normal goods, higher income shifts demand rightward. For inferior goods, higher income shifts demand leftward. A price rise in tea increases demand for coffee, while a price rise in petrol reduces demand for large cars.",
        "vi": "Với hàng hóa thông thường, thu nhập cao hơn làm đường cầu dịch sang phải. Với hàng hóa thứ cấp, thu nhập cao lại làm cầu dịch sang trái. Giá trà tăng làm tăng cầu cà phê (hàng thay thế), trong khi giá xăng tăng làm giảm cầu xe hơi phân khối lớn (hàng bổ sung)."
    }
]

lec7_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_demand_intro": {"start": 1, "end": 2},
    "sec_movements": {"start": 3, "end": 4},
    "sec_shifts": {"start": 5, "end": 5},
    "sec_determinants": {"start": 6, "end": 7}
}

# =====================================================================
# LECTURE 8: Supply
# =====================================================================
LEC8_ID = "d15b56e7-9b09-4120-829c-1955efd21602"
LEC8_TITLE = "8. Supply"

lec8_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 8: Cung (Supply)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 8: Supply. In this lesson, we explore how firms respond to market prices according to the law of supply, distinguish movements along the supply curve from whole-curve shifts, and examine the critical non-price determinants influencing production.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 8: Cung (Supply). Trong bài học này, chúng ta sẽ tìm hiểu cách các doanh nghiệp phản ứng trước giá thị trường theo quy luật cung, phân biệt sự di chuyển dọc theo đường cung với sự dịch chuyển của toàn bộ đường cung, và khảo sát các yếu tố phi giá quan trọng chi phối sản xuất."
    },
    {
        "id": "sec_supply_intro",
        "title": "1. Khái niệm Cung & Quy luật Cung (The Law of Supply)",
        "selector": "#sec-supply-intro",
        "en": "Section 1 defines supply as the quantity of a good or service that producers are willing and able to offer for sale at various prices over a given period. The Law of Supply states that as price rises, quantity supplied increases, creating an upward-sloping supply curve.",
        "vi": "Mục 1 định nghĩa cung là lượng hàng hóa hoặc dịch vụ mà người sản xuất sẵn sàng và có khả năng bán ở các mức giá khác nhau trong một thời kỳ nhất định. Quy luật Cung chỉ ra rằng khi giá tăng thì lượng cung tăng, tạo nên đường cung dốc lên."
    },
    {
        "id": "card_law_of_supply",
        "title": "⚖️ Quy luật Cung & Cung Cá nhân vs Cung Thị trường",
        "selector": "#card-law-of-supply",
        "en": "The positive relationship exists because higher prices offer greater profit margins, incentivizing existing producers to expand output and attracting new firms into the industry.",
        "vi": "Mối quan hệ tỷ lệ thuận tồn tại vì mức giá cao hơn mang lại biên lợi nhuận lớn hơn, khuyến khích các nhà sản xuất hiện tại mở rộng quy mô và thu hút các doanh nghiệp mới gia nhập ngành."
    },
    {
        "id": "sec_movements",
        "title": "2. Di chuyển Dọc theo Đường Cung (Movements along a Supply Curve)",
        "selector": "#sec-movements",
        "en": "Section 2 investigates movements along the curve, caused exclusively by changes in the market price of the good. A price rise leads to an extension in supply; a price drop causes a contraction in supply.",
        "vi": "Mục 2 khảo sát sự di chuyển dọc theo đường cung, chỉ do sự thay đổi mức giá thị trường của chính sản phẩm đó. Giá tăng dẫn đến sự mở rộng cung; giá giảm dẫn đến sự co hẹp cung."
    },
    {
        "id": "card_movements",
        "title": "⬆️ Mở rộng Cung (Extension) vs ⬇️ Co hẹp Cung (Contraction)",
        "selector": "#card-movements",
        "en": "Always distinguish a change in quantity supplied (movement along the curve due to price) from a change in supply (a shift of the curve due to costs or technology).",
        "vi": "Hãy luôn phân biệt sự thay đổi lượng cung (di chuyển dọc theo đường cung do giá) với sự thay đổi của cung (dịch chuyển cả đường cung do chi phí hoặc công nghệ)."
    },
    {
        "id": "sec_shifts",
        "title": "3. Dịch chuyển Toàn bộ Đường Cung (Shifts in the Supply Curve)",
        "selector": "#sec-shifts",
        "en": "Section 3 explains shifts in supply. An outward shift to the right means producers offer more output at every price level. An inward shift to the left means producers supply less at every price.",
        "vi": "Mục 3 giải thích sự dịch chuyển của đường cung. Dịch chuyển sang phải nghĩa là nhà sản xuất cung ứng nhiều hàng hơn ở mọi mức giá. Dịch chuyển sang trái nghĩa là nhà sản xuất cung ứng ít hơn ở mọi mức giá."
    },
    {
        "id": "sec_determinants",
        "title": "4. Các Yếu tố Phi giá Xác định Cung (Non-Price Determinants)",
        "selector": "#sec-determinants",
        "en": "Section 4 covers non-price determinants: costs of production (wages, raw materials), indirect taxes and government subsidies, technological advances, weather and climate shocks, and prices of substitute products in production.",
        "vi": "Mục 4 bao gồm các yếu tố phi giá: chi phí sản xuất (tiền lương, giá nguyên liệu), thuế gián thu và trợ cấp của chính phủ, tiến bộ công nghệ, điều kiện thời tiết khí hậu và giá của các hàng hóa thay thế trong sản xuất."
    },
    {
        "id": "card_determinants",
        "title": "🧠 5 Yếu tố Dịch chuyển Cung: Chi phí, Thuế, Trợ cấp, Công nghệ...",
        "selector": "#card-determinants",
        "en": "Lower production costs, new automation technology, and state subsidies shift the supply curve to the right. Higher business taxes, expensive raw materials, and poor harvest weather shift supply to the left.",
        "vi": "Chi phí sản xuất giảm, công nghệ tự động hóa mới và trợ cấp nhà nước làm đường cung dịch sang phải. Thuế doanh nghiệp tăng, nguyên liệu đắt đỏ và thời tiết mất mùa làm đường cung dịch sang trái."
    }
]

lec8_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_supply_intro": {"start": 1, "end": 2},
    "sec_movements": {"start": 3, "end": 4},
    "sec_shifts": {"start": 5, "end": 5},
    "sec_determinants": {"start": 6, "end": 7}
}

# =====================================================================
# LECTURE 9: Price Determination
# =====================================================================
LEC9_ID = "763cd322-6b7d-43b0-a18d-15da34137d9d"
LEC9_TITLE = "9. Price Determination"

lec9_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 9: Sự Hình thành Giá cả (Price Determination)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 9: Price Determination. In this lesson, we bring demand and supply together to determine market equilibrium. We analyze the market clearing price, examine disequilibrium situations involving surpluses and shortages, and discover how price movements automatically restore market balance.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 9: Sự Hình thành Giá cả (Price Determination). Trong bài học này, chúng ta sẽ kết hợp cung và cầu để xác định trạng thái cân bằng thị trường. Chúng ta sẽ phân tích mức giá cân bằng, xem xét các tình huống mất cân bằng gồm dư thừa và thiếu hụt hàng hóa, đồng thời khám phá cách biến động giá tự động tái lập cân bằng thị trường."
    },
    {
        "id": "sec_price_mechanism",
        "title": "1. Cơ chế Giá cả (The Price Mechanism)",
        "selector": "#sec-price-mechanism",
        "en": "Section 1 reviews how free market interaction determines prices without government intervention. Prices fluctuate until the quantity consumers want to buy equals the quantity producers want to sell.",
        "vi": "Mục 1 ôn lại cách thức tương tác của thị trường tự do xác định giá cả mà không cần sự can thiệp của chính phủ. Giá cả sẽ tự điều chỉnh cho đến khi lượng người mua muốn mua bằng đúng lượng người bán muốn bán."
    },
    {
        "id": "sec_equilibrium",
        "title": "2. Cân bằng Thị trường (Market Equilibrium)",
        "selector": "#sec-equilibrium",
        "en": "Section 2 defines market equilibrium, where the demand curve intersects the supply curve. At this equilibrium price, there is neither an unsold surplus nor an unsatisfied shortage; the market completely clears.",
        "vi": "Mục 2 định nghĩa cân bằng thị trường, nơi đường cầu cắt đường cung. Tại mức giá cân bằng này, không có tình trạng ế thừa hàng cũng như không có sự thiếu hụt hàng hóa; thị trường hoàn toàn được giải tỏa."
    },
    {
        "id": "card_equilibrium",
        "title": "✅ Giá Cân bằng, Lượng Cân bằng & Biểu Lịch Thị trường",
        "selector": "#card-equilibrium",
        "en": "At equilibrium price Pe, quantity demanded exactly equals quantity supplied Qe. All consumers willing and able to pay Pe acquire the good, and all producers willing to sell at Pe sell their goods.",
        "vi": "Tại mức giá cân bằng Pe, lượng cầu bằng chính xác lượng cung Qe. Tất cả người tiêu dùng sẵn sàng và có khả năng trả Pe đều mua được hàng, và tất cả nhà sản xuất sẵn sàng bán ở giá Pe đều tiêu thụ được sản phẩm."
    },
    {
        "id": "sec_disequilibrium",
        "title": "3. Mất Cân bằng Thị trường (Market Disequilibrium)",
        "selector": "#sec-disequilibrium",
        "en": "Section 3 investigates market disequilibrium when current price deviates from equilibrium, creating either excess supply or excess demand.",
        "vi": "Mục 3 khảo sát trạng thái mất cân bằng thị trường khi mức giá hiện tại chênh lệch khỏi mức giá cân bằng, tạo ra tình trạng dư cung hoặc dư cầu."
    },
    {
        "id": "card_excess_supply",
        "title": "📈 Dư thừa Hàng hóa (Excess Supply / Market Surplus)",
        "selector": "#card-excess-supply",
        "en": "If price is set above equilibrium, quantity supplied exceeds quantity demanded, creating unsold stock. To eliminate surplus inventories, competing sellers cut prices back toward equilibrium.",
        "vi": "Nếu giá bị đặt cao hơn mức cân bằng, lượng cung vượt quá lượng cầu tạo ra hàng tồn kho ế thừa. Để giải phóng hàng tồn, các nhà bán cạnh tranh buộc phải hạ giá dần về mức cân bằng."
    },
    {
        "id": "card_excess_demand",
        "title": "📉 Thiếu hụt Hàng hóa (Excess Demand / Market Shortage)",
        "selector": "#card-excess-demand",
        "en": "If price is below equilibrium, quantity demanded exceeds quantity supplied, causing empty shelves and long queues. Recognizing unmet demand, sellers raise prices back up to equilibrium.",
        "vi": "Nếu giá thấp hơn mức cân bằng, lượng cầu vượt xa lượng cung gây ra tình trạng khan hiếm và xếp hàng dài. Nhận thấy nhu cầu chưa được đáp ứng, người bán sẽ nâng giá dần lên mức cân bằng."
    }
]

lec9_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_price_mechanism": {"start": 1, "end": 1},
    "sec_equilibrium": {"start": 2, "end": 3},
    "sec_disequilibrium": {"start": 4, "end": 6}
}

# =====================================================================
# LECTURE 10: Price Changes
# =====================================================================
LEC10_ID = "16314014-7787-41dc-9ff5-47fd1d2c7409"
LEC10_TITLE = "10 . Price Changes"

lec10_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10: Sự Thay đổi Giá cả (Price Changes)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 10: Price Changes. In this lesson, we examine how shifts in demand and supply curves disrupt original equilibria, analyzing the resulting adjustments in market clearing prices and quantities across four core shift scenarios.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 10: Sự Thay đổi Giá cả (Price Changes). Trong bài học này, chúng ta sẽ khảo sát cách các dịch chuyển của đường cung và cầu phá vỡ trạng thái cân bằng ban đầu, phân tích các điều chỉnh về giá và lượng cân bằng qua bốn kịch bản dịch chuyển kinh điển."
    },
    {
        "id": "sec_causes",
        "title": "1. Nguyên nhân Dịch chuyển Cung Cầu gây Thay đổi Giá",
        "selector": "#sec-causes",
        "en": "Section 1 reviews the non-price causes of shifts. Demand shifts from changes in incomes, advertising, tastes, and substitute prices. Supply shifts from changes in production costs, technology, indirect taxes, and subsidies.",
        "vi": "Mục 1 ôn lại các nguyên nhân phi giá làm dịch chuyển đường cung cầu. Cầu dịch chuyển do thu nhập, quảng cáo, thị hiếu và giá hàng thay thế. Cung dịch chuyển do chi phí sản xuất, công nghệ, thuế gián thu và trợ cấp."
    },
    {
        "id": "sec_consequences",
        "title": "2. Tác động Lên Cân bằng Thị trường (4 Kịch bản)",
        "selector": "#sec-consequences",
        "en": "Section 2 explores the four standard shift cases: An increase in demand raises both price and quantity. A decrease in demand lowers both price and quantity. An increase in supply lowers price but raises quantity. A decrease in supply raises price and lowers quantity.",
        "vi": "Mục 2 phân tích bốn trường hợp dịch chuyển tiêu chuẩn: Cầu tăng làm tăng cả giá và sản lượng cân bằng. Cầu giảm làm giảm cả giá và sản lượng. Cung tăng làm giảm giá nhưng tăng sản lượng. Cung giảm làm tăng giá và giảm sản lượng."
    },
    {
        "id": "card_four_scenarios",
        "title": "📊 Tổng kết 4 Kịch bản Dịch chuyển Cung Cầu",
        "selector": "#card-four-scenarios",
        "en": "Remember the dual-rule for exams: Demand shifts move price and quantity in the SAME direction (both up or both down); Supply shifts move price and quantity in OPPOSITE directions.",
        "vi": "Hãy ghi nhớ quy tắc kép khi đi thi: Dịch chuyển cầu kéo giá và sản lượng đi CÙNG CHIỀU (cùng tăng hoặc cùng giảm); Dịch chuyển cung đẩy giá và sản lượng đi NGƯỢC CHIỀU nhau."
    }
]

lec10_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_causes": {"start": 1, "end": 1},
    "sec_consequences": {"start": 2, "end": 3}
}

# =====================================================================
# LECTURE 11: Price Elasticity of Demand (PED)
# =====================================================================
LEC11_ID = "4a5f97fd-91d2-41f4-8cbb-b928f5aea5e9"
LEC11_TITLE = "11. Price Easticity of Demand"

lec11_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 11: Độ co giãn của Cầu theo Giá (PED)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 11: Price Elasticity of Demand, or PED. In this crucial lesson, we calculate PED using the percentage formula, contrast elastic and inelastic demand, explore three special cases, evaluate the SPLAT determinants, and examine how PED dictates business revenues and government tax policies.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 11: Độ co giãn của Cầu theo Giá (PED). Trong bài học then chốt này, chúng ta sẽ tính toán PED bằng công thức phần trăm, so sánh cầu co giãn và không co giãn, tìm hiểu ba trường hợp đặc biệt, đánh giá các yếu tố quyết định theo quy tắc SPLAT, và xem xét cách PED chi phối doanh thu doanh nghiệp cùng chính sách thuế của chính phủ."
    },
    {
        "id": "sec_ped_intro",
        "title": "1. Khái niệm & Công thức Tính PED (The PED Formula)",
        "selector": "#sec-ped-intro",
        "en": "Section 1 defines PED as the numerical responsiveness of quantity demanded to a change in price. The formula is: percentage change in quantity demanded divided by percentage change in price. Because price and quantity demanded move inversely, PED is negative, but economists evaluate its absolute value.",
        "vi": "Mục 1 định nghĩa PED là thước đo mức độ phản ứng của lượng cầu khi giá sản phẩm thay đổi. Công thức là: phần trăm thay đổi lượng cầu chia cho phần trăm thay đổi giá cả. Do giá và lượng cầu biến thiên ngược chiều, giá trị PED mang dấu âm, nhưng các nhà kinh tế học thường xét giá trị tuyệt đối của nó."
    },
    {
        "id": "sec_elastic_inelastic",
        "title": "2. Cầu Co giãn vs Cầu Không co giãn (Elastic vs Inelastic)",
        "selector": "#sec-elastic-inelastic",
        "en": "Section 2 contrasts elastic and inelastic demand. Demand is inelastic when absolute PED is less than 1, meaning quantity demanded changes by a smaller percentage than price. Demand is elastic when absolute PED is greater than 1, meaning quantity responds more than proportionately.",
        "vi": "Mục 2 so sánh cầu co giãn và không co giãn. Cầu không co giãn khi trị tuyệt đối của PED nhỏ hơn 1, nghĩa là phần trăm thay đổi lượng cầu nhỏ hơn phần trăm thay đổi giá. Cầu co giãn khi trị tuyệt đối của PED lớn hơn 1, nghĩa là lượng cầu phản ứng mạnh hơn tỷ lệ biến động của giá."
    },
    {
        "id": "sec_special_cases",
        "title": "3. Ba Trường hợp Đặc biệt của PED",
        "selector": "#sec-special-cases",
        "en": "Section 3 covers three extreme cases: Perfectly Inelastic demand (PED = 0), a vertical line where quantity never changes; Perfectly Elastic demand (PED = infinity), a horizontal line where price is fixed; and Unitary Elastic demand (PED = -1), where percentage changes in price and quantity are identical.",
        "vi": "Mục 3 trình bày ba trường hợp đặc biệt: Cầu hoàn toàn không co giãn (PED = 0) là đường thẳng đứng với lượng cầu cố định; Cầu co giãn hoàn toàn (PED = vô cùng) là đường nằm ngang với giá cố định; và Cầu co giãn đơn vị (PED = -1) khi tỷ lệ thay đổi của giá và lượng cầu hoàn toàn bằng nhau."
    },
    {
        "id": "sec_determinants",
        "title": "4. Các Yếu tố Xác định PED (Quy tắc SPLAT)",
        "selector": "#sec-determinants",
        "en": "Section 4 outlines the key determinants of PED, remembered by the acronym SPLAT: Substitutes availability, Proportion of income spent, Luxury vs necessity, Addictive nature, and Time period to adjust.",
        "vi": "Mục 4 chỉ ra các yếu tố quyết định độ co giãn qua chữ viết tắt SPLAT: Sự sẵn có của hàng thay thế (Substitutes), Tỷ trọng thu nhập chi trả (Proportion), Hàng xa xỉ hay thiết yếu (Luxury), Tính gây nghiện (Addictive), và Khoảng thời gian thích ứng (Time)."
    },
    {
        "id": "sec_revenue",
        "title": "5. Mối quan hệ giữa PED và Tổng Doanh thu (Total Revenue)",
        "selector": "#sec-revenue",
        "en": "Section 5 reveals the golden rule of pricing: If demand is inelastic, raising price increases total revenue. If demand is elastic, raising price reduces total revenue, whereas cutting price expands total revenue.",
        "vi": "Mục 5 tiết lộ nguyên tắc vàng về giá: Nếu cầu không co giãn, tăng giá sẽ làm tăng tổng doanh thu. Nếu cầu co giãn, tăng giá làm giảm doanh thu, trong khi giảm giá lại làm tăng tổng doanh thu."
    },
    {
        "id": "sec_significance",
        "title": "6. Ứng dụng Thực tiễn của PED đối với Doanh nghiệp & Chính phủ",
        "selector": "#sec-significance",
        "en": "Section 6 highlights the real-world significance. Producers use PED to set profitable pricing strategies and implement price discrimination. Governments target price-inelastic goods like petrol, cigarettes, and alcohol with indirect taxes because tax yield is high and demand does not collapse.",
        "vi": "Mục 6 nêu bật ý nghĩa thực tiễn. Doanh nghiệp dùng PED để định giá sinh lời và áp dụng chính sách phân biệt giá. Chính phủ áp thuế tiêu thụ đặc biệt vào các mặt hàng có cầu kém co giãn như xăng dầu, thuốc lá, rượu bia vì nguồn thu thuế ổn định và lượng cầu không bị sụt giảm quá nhiều."
    }
]

lec11_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_ped_intro": {"start": 1, "end": 1},
    "sec_elastic_inelastic": {"start": 2, "end": 2},
    "sec_special_cases": {"start": 3, "end": 3},
    "sec_determinants": {"start": 4, "end": 4},
    "sec_revenue": {"start": 5, "end": 5},
    "sec_significance": {"start": 6, "end": 6}
}

# =====================================================================
# LECTURE 12: Price Elasticity of Supply (PES)
# =====================================================================
LEC12_ID = "38954a57-c9bc-4714-b53e-e404e78379cd"
LEC12_TITLE = "12. Price Elasticity of Supply"

lec12_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 12: Độ co giãn của Cung theo Giá (PES)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 12: Price Elasticity of Supply, or PES. In this lesson, we define and calculate PES, distinguish elastic and inelastic supply curves, explore three special cases, evaluate factors that make supply responsive, and analyze its importance for producers and governments.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 12: Độ co giãn của Cung theo Giá (PES). Trong bài học này, chúng ta sẽ định nghĩa và tính toán PES, phân biệt cung co giãn và kém co giãn, khám phá ba trường hợp đặc biệt, đánh giá các yếu tố giúp tăng độ linh hoạt của cung, và phân tích tầm quan trọng của PES đối với doanh nghiệp và chính phủ."
    },
    {
        "id": "sec_pes_intro",
        "title": "1. Khái niệm & Công thức Tính PES (The PES Formula)",
        "selector": "#sec-pes-intro",
        "en": "Section 1 defines PES as the responsiveness of quantity supplied to a change in the price of the good. The formula is percentage change in quantity supplied divided by percentage change in price. Because price and supply are positively related, PES is always positive.",
        "vi": "Mục 1 định nghĩa PES là thước đo mức độ phản ứng của lượng cung khi giá sản phẩm thay đổi. Công thức là phần trăm thay đổi lượng cung chia cho phần trăm thay đổi giá cả. Do giá và lượng cung tỷ lệ thuận, giá trị PES luôn là số dương."
    },
    {
        "id": "sec_elastic_inelastic",
        "title": "2. Cung Co giãn vs Cung Không co giãn (Elastic vs Inelastic Supply)",
        "selector": "#sec-elastic-inelastic",
        "en": "Section 2 contrasts elastic and inelastic supply. Supply is price-elastic (PES > 1) when producers can quickly and substantially increase production following a price rise. Supply is price-inelastic (PES < 1) when output cannot easily expand due to technical or resource constraints.",
        "vi": "Mục 2 so sánh cung co giãn và kém co giãn. Cung co giãn (PES > 1) khi người sản xuất có thể nhanh chóng tăng mạnh sản lượng khi giá tăng. Cung kém co giãn (PES < 1) khi sản lượng khó có thể mở rộng do hạn chế về kỹ thuật hoặc khan hiếm nguồn lực đầu vào."
    },
    {
        "id": "sec_special_cases",
        "title": "3. Ba Trường hợp Đặc biệt của PES",
        "selector": "#sec-special-cases",
        "en": "Section 3 examines three special cases: Perfectly Inelastic supply (PES = 0), a vertical supply curve like original artwork or stadium seating; Perfectly Elastic supply (PES = infinity), a horizontal line; and Unitary Elastic supply (PES = 1), any straight-line supply curve starting from the origin.",
        "vi": "Mục 3 khảo sát ba trường hợp đặc biệt: Cung hoàn toàn không co giãn (PES = 0) là đường thẳng đứng như tác phẩm nghệ thuật độc bản hay số ghế sân vận động; Cung co giãn hoàn toàn (PES = vô cùng) là đường nằm ngang; và Cung co giãn đơn vị (PES = 1) là bất kỳ đường cung thẳng nào đi qua gốc tọa độ."
    },
    {
        "id": "sec_determinants",
        "title": "4. Các Yếu tố Xác định Độ co giãn của Cung (Determinants of PES)",
        "selector": "#sec-determinants",
        "en": "Section 4 covers determinants of PES: spare productive capacity in factories, availability of inventory and stocks, the length of the production period, factor mobility, and time horizon.",
        "vi": "Mục 4 bao gồm các yếu tố quyết định PES: công suất máy móc còn dư thừa, mức độ sẵn có của hàng tồn kho, chu kỳ thời gian sản xuất dài hay ngắn, độ linh hoạt của các yếu tố đầu vào và khoảng thời gian phản ứng."
    },
    {
        "id": "sec_significance",
        "title": "5. Tầm quan trọng của PES đối với Doanh nghiệp & Chính phủ",
        "selector": "#sec-significance",
        "en": "Section 5 highlights why PES matters. Highly elastic supply allows businesses to swiftly capture profit windfalls during price booms. For governments, understanding farm product inelasticity explains why agricultural prices and farmers' incomes fluctuate dramatically.",
        "vi": "Mục 5 chỉ ra tầm quan trọng của PES. Cung có độ co giãn cao giúp doanh nghiệp nhanh chóng chớp lấy cơ hội siêu lợi nhuận khi giá thị trường tăng vọt. Đối với chính phủ, việc hiểu tính kém co giãn của nông sản giúp giải thích tại sao giá nông sản và thu nhập người nông dân thường biến động rất mạnh."
    }
]

lec12_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_pes_intro": {"start": 1, "end": 1},
    "sec_elastic_inelastic": {"start": 2, "end": 2},
    "sec_special_cases": {"start": 3, "end": 3},
    "sec_determinants": {"start": 4, "end": 4},
    "sec_significance": {"start": 5, "end": 5}
}

# =====================================================================
# LECTURE 13: Market Economic System
# =====================================================================
LEC13_ID = "6f3173be-e12a-4a93-8f76-8cb09fb026fe"
LEC13_TITLE = "13. Market Economic System"

lec13_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 13: Hệ thống Kinh tế Thị trường",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 13: The Market Economic System. In this lesson, we study the core pillars of a free market economy: private property rights, profit incentives, consumer sovereignty, and the price mechanism. We also evaluate the significant merits of market efficiency alongside critical demerits like monopoly exploitation and social inequality.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 13: Hệ thống Kinh tế Thị trường. Trong bài học này, chúng ta sẽ tìm hiểu các trụ cột cốt lõi của nền kinh tế thị trường tự do: quyền sở hữu tư nhân, động lực lợi nhuận, chủ quyền của người tiêu dùng và cơ chế giá. Chúng ta cũng sẽ đánh giá những ưu điểm lớn về hiệu quả kinh tế cùng với những nhược điểm nghiêm trọng như độc quyền và bất bình đẳng xã hội."
    },
    {
        "id": "sec_market_system",
        "title": "1. Bản chất & Đặc trưng của Hệ thống Kinh tế Thị trường",
        "selector": "#sec-market-system",
        "en": "Section 1 defines the market economy, where resource allocation decisions are determined solely by market supply and demand with zero state intervention. Key features include private ownership of land and capital, the pursuit of profit, consumer sovereignty deciding what gets made, and decentralized price rationing.",
        "vi": "Mục 1 định nghĩa nền kinh tế thị trường, nơi các quyết định phân bổ nguồn lực hoàn toàn do cung và cầu quyết định mà không có sự can thiệp của nhà nước. Các đặc trưng chính gồm quyền sở hữu tư nhân về đất đai và tư bản, mục tiêu theo đuổi lợi nhuận, quyền tối cao của người tiêu dùng trong việc định đoạt sản phẩm, và cơ chế giá phân bổ phi tập trung."
    },
    {
        "id": "card_features",
        "title": "🏛️ 4 Trụ cột Cốt lõi: Sở hữu Tư nhân, Lợi nhuận, Quyền Người tiêu dùng & Cơ chế Giá",
        "selector": "#card-features",
        "en": "Private property motivates hard work and investment; profit motive drives innovation; consumer sovereignty ensures firms cater strictly to buyer preferences; and the price mechanism allocates scarce resources efficiently.",
        "vi": "Quyền sở hữu tư nhân thúc đẩy làm việc chăm chỉ và đầu tư; động lực lợi nhuận kích thích đổi mới sáng tạo; quyền tối cao của người tiêu dùng buộc doanh nghiệp phải phục vụ đúng nhu cầu; và cơ chế giá tự động phân bổ nguồn lực khan hiếm hiệu quả."
    },
    {
        "id": "sec_merits_demerits",
        "title": "2. Đánh giá Ưu điểm & Nhược điểm (Merits & Demerits)",
        "selector": "#sec-merits-demerits",
        "en": "Section 2 evaluates the market economy. Merits include productive efficiency, intense innovation, consumer choice, and freedom from bureaucratic red tape. Demerits include underprovision of merit goods like schooling, missing public goods like street lighting, negative pollution externalities, and severe income inequality.",
        "vi": "Mục 2 đánh giá nền kinh tế thị trường. Ưu điểm bao gồm hiệu quả sản xuất cao, sáng tạo liên tục, tự do lựa chọn và không bị thủ tục hành chính cồng kềnh cản trở. Nhược điểm gồm sự thiếu hụt hàng hóa công cộng như đèn đường, cung ứng thiếu hàng hóa khuyến dụng như giáo dục, ô nhiễm môi trường và khoảng cách giàu nghèo gia tăng."
    }
]

lec13_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_market_system": {"start": 1, "end": 2},
    "sec_merits_demerits": {"start": 3, "end": 3}
}

# =====================================================================
# LECTURE 14: Market Failure
# =====================================================================
LEC14_ID = "69df5ed2-ce91-4e2a-b818-0e2957483b12"
LEC14_TITLE = "14. Market Failure"

lec14_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 14: Thất bại Thị trường (Market Failure)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 14: Market Failure. In this critical topic, we analyze why free market forces fail to achieve an efficient and socially optimal allocation of resources. We examine the six major causes of market failure, master the formulas for social costs and benefits, and dissect negative and positive externalities.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 14: Thất bại Thị trường (Market Failure). Trong chủ đề trọng yếu này, chúng ta sẽ phân tích lý do tại sao các lực lượng thị trường tự do lại thất bại trong việc đạt được mức phân bổ nguồn lực tối ưu cho xã hội. Chúng ta sẽ khảo sát sáu nguyên nhân chính gây thất bại thị trường, nắm vững các công thức chi phí và lợi ích xã hội, đồng thời mổ xẻ các ngoại ứng tiêu cực và tích cực."
    },
    {
        "id": "sec_market_failure_intro",
        "title": "1. Khái niệm Thất bại Thị trường & Sai lệch Nguồn lực",
        "selector": "#sec-market-failure-intro",
        "en": "Section 1 defines market failure as a situation where the free market mechanism leads to a misallocation of resources, resulting in allocative or productive inefficiency, deadweight social loss, and reduced economic welfare.",
        "vi": "Mục 1 định nghĩa thất bại thị trường là tình trạng cơ chế thị trường tự do dẫn đến việc phân bổ sai lệch các nguồn lực, gây ra sự kém hiệu quả trong phân bổ hoặc sản xuất, tạo ra tổn thất xã hội và làm suy giảm phúc lợi kinh tế chung."
    },
    {
        "id": "sec_causes",
        "title": "2. Sáu Nguyên nhân Cốt lõi Gây ra Thất bại Thị trường",
        "selector": "#sec-causes",
        "en": "Section 2 explores the six primary causes: missing public goods due to non-excludability and the free rider problem; underconsumption of merit goods; overconsumption of demerit goods; unpriced externalities; monopoly abuse; and factor immobility causing structural unemployment.",
        "vi": "Mục 2 khảo sát sáu nguyên nhân chính: thiếu vắng hoàn toàn hàng hóa công cộng do tính không thể loại trừ và hiện tượng 'kẻ đi nhờ' miễn phí; tiêu dùng dưới mức tối ưu các hàng hóa khuyến dụng; tiêu dùng quá mức các hàng hóa phi khuyến dụng; các ngoại ứng không được định giá; lạm quyền độc quyền; và sự bất linh hoạt của các yếu tố sản xuất gây thất nghiệp cơ cấu."
    },
    {
        "id": "sec_externalities",
        "title": "3. Ngoại ứng (Externalities) & Công thức Chi phí Xã hội",
        "selector": "#sec-externalities",
        "en": "Section 3 masters the Cambridge social equations: Social Cost equals Private Cost plus External Cost. Social Benefit equals Private Benefit plus External Benefit. When negative externalities occur, social cost exceeds private cost, causing market overproduction and pollution.",
        "vi": "Mục 3 làm chủ các công thức xã hội chuẩn Cambridge: Chi phí Xã hội bằng Chi phí Tư nhân cộng Chi phí Ngoại ứng. Lợi ích Xã hội bằng Lợi ích Tư nhân cộng Lợi ích Ngoại ứng. Khi có ngoại ứng tiêu cực, chi phí xã hội lớn hơn chi phí tư nhân, dẫn đến sản xuất dư thừa và gây ô nhiễm môi trường."
    },
    {
        "id": "sec_consequences",
        "title": "4. Hậu quả Thực tế & Trọng tâm Thi cử về Thất bại Thị trường",
        "selector": "#sec-consequences",
        "en": "Section 4 highlights exam implications: Market failure justifies government intervention. Free markets overprovide tobacco and alcohol while underproviding healthcare and schools, requiring corrective taxes, subsidies, and regulations.",
        "vi": "Mục 4 nhấn mạnh trọng tâm thi cử: Thất bại thị trường là lý do căn bản biện minh cho sự can thiệp của chính phủ. Thị trường tự do cung ứng thừa thuốc lá, rượu bia nhưng lại cung ứng thiếu trạm xá, trường học, đòi hỏi nhà nước phải can thiệp bằng thuế, trợ cấp và luật định."
    }
]

lec14_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_market_failure_intro": {"start": 1, "end": 1},
    "sec_causes": {"start": 2, "end": 2},
    "sec_externalities": {"start": 3, "end": 3},
    "sec_consequences": {"start": 4, "end": 4}
}

# =====================================================================
# LECTURE 15: Mixed Economic System
# =====================================================================
LEC15_ID = "1af33337-f02c-45ff-a8d0-040864272c98"
LEC15_TITLE = "15. Mixed Economic System"

lec15_segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 15: Hệ thống Kinh tế Hỗn hợp",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Economics, Topic 15: The Mixed Economic System. In this concluding lesson of Topic 2, we explore how modern economies combine private market enterprise with government intervention. We evaluate price controls including maximum and minimum prices, indirect taxation, subsidies, state regulations, privatization, and nationalization.",
        "vi": "Chào mừng các bạn đến với môn Kinh tế học Cambridge IGCSE, Bài 15: Hệ thống Kinh tế Hỗn hợp. Trong bài học kết thúc Chủ đề 2 này, chúng ta sẽ tìm hiểu cách các nền kinh tế hiện đại kết hợp giữa thị trường tư nhân với sự can thiệp của nhà nước. Chúng ta sẽ đánh giá các biện pháp kiểm soát giá gồm giá trần và giá sàn, thuế gián thu, trợ cấp, quy định pháp luật, tư nhân hóa và quốc hữu hóa."
    },
    {
        "id": "sec_mixed_system",
        "title": "1. Khái niệm & Bản chất của Hệ thống Kinh tế Hỗn hợp",
        "selector": "#sec-mixed-system",
        "en": "Section 1 defines a mixed economy as an economic system combining private enterprise guided by market price mechanism with public sector intervention by the government to correct market failures.",
        "vi": "Mục 1 định nghĩa nền kinh tế hỗn hợp là hệ thống kinh tế kết hợp giữa doanh nghiệp tư nhân vận hành theo cơ chế giá thị trường với sự can thiệp của khu vực công nhằm khắc phục các thất bại thị trường."
    },
    {
        "id": "sec_price_controls",
        "title": "2. Biện pháp Kiểm soát Giá: Giá Trần (Max Price) & Giá Sàn (Min Price)",
        "selector": "#sec-price-controls",
        "en": "Section 2 analyzes price controls. A maximum price or price ceiling is set below equilibrium to make staple foods or rents affordable, but risks shortages and black markets. A minimum price or price floor is set above equilibrium to guarantee farmer incomes or minimum wages, creating unsold surpluses.",
        "vi": "Mục 2 phân tích các biện pháp kiểm soát giá. Giá trần (maximum price) được ấn định dưới mức giá cân bằng để giữ giá lương thực thiết yếu hoặc tiền thuê nhà ở mức phải chăng, nhưng có nguy cơ gây khan hiếm và thị trường chợ đen. Giá sàn (minimum price) được đặt trên mức cân bằng để bảo vệ thu nhập nông dân hoặc tiền lương tối thiểu, dẫn đến dư thừa lượng cung."
    },
    {
        "id": "sec_intervention",
        "title": "3. Các Biện pháp Can thiệp Khác: Thuế, Trợ cấp & Quy định",
        "selector": "#sec-intervention",
        "en": "Section 3 explores additional intervention tools: indirect taxes on demerit goods to internalize external costs; subsidies on merit goods like public transit and vaccines to expand consumption; and strict legal regulations such as smoking bans and mandatory seatbelts.",
        "vi": "Mục 3 khảo sát các công cụ can thiệp khác: thuế gián thu đánh vào hàng hóa phi khuyến dụng để nội hóa chi phí ngoại ứng; trợ cấp cho hàng hóa khuyến dụng như xe buýt công cộng và vắc xin để mở rộng tiêu dùng; và các quy định pháp luật nghiêm ngặt như cấm hút thuốc nơi công cộng và bắt buộc thắt dây an toàn."
    },
    {
        "id": "sec_privatisation",
        "title": "4. Tư nhân hóa (Privatisation) & Quốc hữu hóa (Nationalisation)",
        "selector": "#sec-privatisation",
        "en": "Section 4 contrasts privatization—selling state-owned businesses to private investors to boost efficiency and competition—with nationalization, bringing critical private firms into public ownership to secure vital public services and prevent private monopoly abuse.",
        "vi": "Mục 4 so sánh tư nhân hóa—bán doanh nghiệp nhà nước cho tư nhân để tăng hiệu quả và cạnh tranh—với quốc hữu hóa, chuyển các doanh nghiệp tư nhân trọng yếu về sở hữu nhà nước để bảo vệ lợi ích công cộng và ngăn ngừa lạm quyền độc quyền."
    },
    {
        "id": "sec_direct_provision",
        "title": "5. Cung cấp Trực tiếp Dịch vụ Công & Hạn ngạch (Quotas)",
        "selector": "#sec-direct-provision",
        "en": "Section 5 examines direct provision of public and merit goods like state schooling and defence free at the point of delivery, funded by taxation. It also discusses environmental quotas limiting fishing catches and carbon emissions to conserve scarce natural resources.",
        "vi": "Mục 5 tìm hiểu việc cung cấp trực tiếp các hàng hóa công cộng và khuyến dụng như giáo dục công lập và quốc phòng miễn phí khi thụ hưởng, chi trả bằng tiền thuế. Phần này cũng phân tích hạn ngạch môi trường giới hạn sản lượng đánh bắt cá và phát thải carbon để bảo tồn tài nguyên thiên nhiên."
    },
    {
        "id": "sec_merits_demerits",
        "title": "6. Đánh giá Ưu và Nhược điểm của Kinh tế Hỗn hợp",
        "selector": "#sec-merits_demerits",
        "en": "Section 6 synthesizes the evaluation: Mixed economies aim to capture the dynamic efficiency and innovation of markets while providing a vital social safety net. However, governments risk government failure, regulatory capture, and bureaucratic inefficiencies.",
        "vi": "Mục 6 tổng hợp đánh giá: Kinh tế hỗn hợp nhằm tận dụng tính hiệu quả và sáng tạo của thị trường, đồng thời xây dựng lưới an sinh xã hội vững chắc. Tuy nhiên, chính phủ cũng có nguy cơ vấp phải thất bại chính phủ, sự chi phối của nhóm lợi ích và bộ máy hành chính quan liêu."
    }
]

lec15_major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_mixed_system": {"start": 1, "end": 1},
    "sec_price_controls": {"start": 2, "end": 2},
    "sec_intervention": {"start": 3, "end": 3},
    "sec_privatisation": {"start": 4, "end": 4},
    "sec_direct_provision": {"start": 5, "end": 5},
    "sec_merits_demerits": {"start": 6, "end": 6}
}

ALL_TOPIC2_LECTURES = [
    ("5", LEC5_ID, COURSE_TITLE, LEC5_TITLE, lec5_segments, lec5_major_sections),
    ("6", LEC6_ID, COURSE_TITLE, LEC6_TITLE, lec6_segments, lec6_major_sections),
    ("7", LEC7_ID, COURSE_TITLE, LEC7_TITLE, lec7_segments, lec7_major_sections),
    ("8", LEC8_ID, COURSE_TITLE, LEC8_TITLE, lec8_segments, lec8_major_sections),
    ("9", LEC9_ID, COURSE_TITLE, LEC9_TITLE, lec9_segments, lec9_major_sections),
    ("10", LEC10_ID, COURSE_TITLE, LEC10_TITLE, lec10_segments, lec10_major_sections),
    ("11", LEC11_ID, COURSE_TITLE, LEC11_TITLE, lec11_segments, lec11_major_sections),
    ("12", LEC12_ID, COURSE_TITLE, LEC12_TITLE, lec12_segments, lec12_major_sections),
    ("13", LEC13_ID, COURSE_TITLE, LEC13_TITLE, lec13_segments, lec13_major_sections),
    ("14", LEC14_ID, COURSE_TITLE, LEC14_TITLE, lec14_segments, lec14_major_sections),
    ("15", LEC15_ID, COURSE_TITLE, LEC15_TITLE, lec15_segments, lec15_major_sections),
]

async def main():
    print("=================================================================")
    print("GENERATING AUDIO & MANIFEST FOR TOPIC 2 (LECTURES 5 - 15)")
    print("=================================================================")
    for code, lid, course, title, segments, major_sections in ALL_TOPIC2_LECTURES:
        await process_lecture_audio(code, lid, course, title, segments, major_sections, subject='economics')
    print("\n✅ ALL TOPIC 2 AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
