import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 1.1 ID
LID = '6049f916-3af9-428a-bcd0-ce0574f1d7f7'
CODE = '1_1'
TITLE = '1.1 Business activity'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 18 AUDIO SEGMENTS
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.1: Hoạt động Kinh doanh",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.1: Business Activity. In this foundational lesson, we explore the core purpose of business activity: how enterprises organise scarce resources to satisfy unlimited consumer wants and needs, the concepts of scarcity and opportunity cost, the four factors of production, the role of specialisation, and how businesses create added value.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.1: Hoạt động Kinh doanh. Trong bài học nền tảng này, chúng ta sẽ tìm hiểu mục đích cốt lõi của doanh nghiệp: cách thức tổ chức các nguồn lực khan hiếm để thỏa mãn nhu cầu vô hạn của con người, bản chất của sự khan hiếm và chi phí cơ hội, bốn yếu tố sản xuất, vai trò của chuyên môn hóa và cách thức doanh nghiệp tạo ra giá trị gia tăng."
    },
    {
        "id": "sec_intro_business",
        "title": "1. Giới thiệu về Doanh nghiệp",
        "selector": "#sec-intro-business",
        "en": "Section 1 introduces business studies. Businesses surround us every day, supplying the goods and services that sustain modern civilization. Academically, business studies examines the economics and management of how enterprises organise resources to satisfy consumer demands in competitive markets.",
        "vi": "Mục 1 giới thiệu về hoạt động kinh doanh. Các doanh nghiệp hiện diện quanh chúng ta mỗi ngày, cung ứng hàng hóa và dịch vụ thiết yếu cho cuộc sống hiện đại. Dưới góc độ học thuật, môn Nghiên cứu Kinh doanh khảo sát cách thức các doanh nghiệp quản trị và tổ chức các nguồn lực nhằm thỏa mãn tối ưu nhu cầu của người tiêu dùng trên thị trường cạnh tranh."
    },
    {
        "id": "sec_economic_problem",
        "title": "2. Vấn đề Kinh tế Cơ bản (The Economic Problem)",
        "selector": "#sec-economic-problem",
        "en": "Section 2 investigates the basic economic problem. All societies face the universal challenge of resource allocation. To understand economics and business, we must first distinguish between human needs, human wants, and the inevitable reality of economic scarcity.",
        "vi": "Mục 2 tìm hiểu về vấn đề kinh tế cơ bản. Mọi xã hội đều phải đối mặt với thách thức phân bổ nguồn lực. Để hiểu bản chất của kinh doanh, trước hết chúng ta cần phân biệt rõ ràng giữa nhu cầu sinh tồn, mong muốn tiện ích và thực tế tất yếu của sự khan hiếm kinh tế."
    },
    {
        "id": "sec_economic_need",
        "title": "🍞 Need (Nhu cầu Thiết yếu)",
        "selector": "#card-need",
        "en": "A need is a good or service essential for living and survival. Without basic needs, human life cannot be sustained. Primary examples include clean drinking water, nutritious food, protective clothing, and safe shelter. Businesses that produce basic necessities often enjoy stable, inelastic consumer demand.",
        "vi": "Nhu cầu thiết yếu (Need) là những hàng hóa hoặc dịch vụ cần thiết sống còn để duy trì sự sống. Nếu thiếu những nhu cầu này, con người không thể tồn tại. Các ví dụ điển hình bao gồm nước sạch, lương thực thực phẩm, quần áo và nhà ở an toàn. Các doanh nghiệp sản xuất nhu yếu phẩm cơ bản thường có lượng cầu tiêu dùng rất ổn định."
    },
    {
        "id": "sec_economic_want",
        "title": "🚗 Want (Mong muốn Tiện ích)",
        "selector": "#card-want",
        "en": "A want is a good or service that people desire to have, but is not required for basic survival. Human wants are virtually unlimited—as soon as one desire is satisfied, new desires arise. Examples include luxury sports cars, modern smartphones, gourmet dining, and international vacations. Businesses constantly innovate to stimulate and satisfy these endless consumer wants.",
        "vi": "Mong muốn (Want) là những hàng hóa hoặc dịch vụ mà con người khao khát sở hữu nhưng không bắt buộc phải có để sinh tồn. Mong muốn của con người là vô hạn—khi một mong muốn được thỏa mãn, những mong muốn mới lại nảy sinh. Ví dụ như xe hơi hạng sang, điện thoại thông minh, ẩm thực cao cấp và du lịch quốc tế. Doanh nghiệp luôn đổi mới sáng tạo để kích thích và đáp ứng những mong muốn vô tận này."
    },
    {
        "id": "sec_economic_scarcity",
        "title": "⚠️ Scarcity (Sự Khan hiếm Nguồn lực)",
        "selector": "#card-scarcity",
        "en": "Scarcity is the fundamental economic problem underlying all human activity. It arises because human wants are unlimited, whereas the resources available to produce goods and services are strictly limited. Because there are never enough resources to satisfy everyone's desires, societies and businesses must make critical choices about what to produce, how to produce, and for whom to produce.",
        "vi": "Sự khan hiếm (Scarcity) là vấn đề kinh tế cốt lõi chi phối mọi hoạt động xã hội. Hiện tượng này phát sinh do mong muốn của con người là vô hạn, trong khi các nguồn lực sẵn có để sản xuất hàng hóa và dịch vụ lại hữu hạn. Do không bao giờ có đủ nguồn lực để thỏa mãn tất cả mọi người, các xã hội và doanh nghiệp buộc phải đưa ra lựa chọn quan trọng: sản xuất cái gì, sản xuất như thế nào và sản xuất cho ai."
    },
    {
        "id": "sec_opportunity_cost",
        "title": "3. Chi phí Cơ hội (Opportunity Cost)",
        "selector": "#sec-opportunity-cost",
        "en": "Section 3 explains opportunity cost. Because resources are scarce, every choice comes with a trade-off. Opportunity cost is defined as the next best alternative forgone by choosing another item. For example, if a firm has limited capital and chooses to buy a new delivery van rather than launch an advertising campaign, the opportunity cost is the potential increase in sales and brand awareness that the marketing campaign would have generated.",
        "vi": "Mục 3 giải thích về chi phí cơ hội. Do nguồn lực khan hiếm, mọi quyết định đều phải đánh đổi. Chi phí cơ hội được định nghĩa là phương án tốt nhất tiếp theo bị bỏ qua khi đưa ra một quyết định lựa chọn. Ví dụ, nếu một doanh nghiệp có vốn hữu hạn và chọn mua xe tải giao hàng thay vì chạy chiến dịch quảng cáo, thì chi phí cơ hội chính là doanh số và mức độ nhận diện thương hiệu mà chiến dịch quảng cáo đó có thể mang lại."
    },
    {
        "id": "sec_factors_of_production",
        "title": "4. Bốn Yếu tố Sản xuất (Factors of Production)",
        "selector": "#sec-factors-of-production",
        "en": "Section 4 introduces the four Factors of Production. These are the scarce economic inputs combined by enterprises to produce goods and services. They are categorized into Land, Labour, Capital, and Enterprise. Each factor contributes a unique capability and earns a specific economic reward.",
        "vi": "Mục 4 giới thiệu bốn yếu tố sản xuất (Factors of Production). Đây là các nguồn lực kinh tế đầu vào khan hiếm được doanh nghiệp phối hợp để tạo ra sản phẩm và dịch vụ. Chúng được phân loại thành: Đất đai, Lao động, Vốn và Tinh thần khởi nghiệp. Mỗi yếu tố đóng góp một năng lực riêng biệt và nhận về phần thưởng kinh tế tương ứng."
    },
    {
        "id": "fop_land",
        "title": "🌲 Land (Đất đai & Địa tô)",
        "selector": "#card-fop-land, #svg-fop-land",
        "en": "Land refers to all natural resources provided by nature, both renewable and non-renewable. This includes agricultural soil, mineral deposits, crude oil, natural gas, forests, and clean water. The economic reward for the owners of land is Rent.",
        "vi": "Đất đai (Land) bao gồm toàn bộ các tài nguyên tự nhiên do thiên nhiên ban tặng, cả tài nguyên tái tạo và không tái tạo. Yếu tố này gồm đất canh tác, mỏ khoáng sản, dầu mỏ, khí đốt, rừng và nguồn nước. Phần thưởng kinh tế dành cho chủ sở hữu tài nguyên đất đai là Địa tô (Rent) hay tiền thuê mặt bằng."
    },
    {
        "id": "fop_labour",
        "title": "👷‍♂️ Labour (Lao động & Tiền lương)",
        "selector": "#card-fop-labour, #svg-fop-labour",
        "en": "Labour encompasses the physical and mental efforts exerted by human workers in the production of goods and services. This includes factory operators, engineers, teachers, doctors, and accountants. The economic reward paid to labour is Wages or Salaries.",
        "vi": "Lao động (Labour) bao gồm toàn bộ nỗ lực thể chất và trí tuệ của con người đóng góp vào quy trình sản xuất hàng hóa và dịch vụ. Yếu tố này bao gồm công nhân nhà máy, kỹ sư, giáo viên, bác sĩ và kế toán viên. Phần thưởng kinh tế chi trả cho người lao động là Tiền công hoặc Tiền lương (Wages / Salaries)."
    },
    {
        "id": "fop_capital",
        "title": "🚜 Capital (Vốn & Lãi suất)",
        "selector": "#card-fop-capital, #svg-fop-capital",
        "en": "Capital consists of all man-made physical assets used in the production process, such as machinery, factory buildings, tools, and computer technology, as well as the financial capital used to purchase them. Capital increases worker productivity. The economic reward for providing capital is Interest.",
        "vi": "Vốn (Capital) là toàn bộ tư liệu sản xuất vật chất do con người tạo ra để phục vụ sản xuất, như máy móc, nhà xưởng, công cụ và công nghệ máy tính, cũng như nguồn vốn tài chính để mua sắm chúng. Vốn giúp tăng mạnh năng suất lao động. Phần thưởng kinh tế khi đầu tư cung cấp vốn là Lãi suất (Interest)."
    },
    {
        "id": "fop_enterprise",
        "title": "💡 Enterprise (Khởi nghiệp & Lợi nhuận)",
        "selector": "#card-fop-enterprise, #svg-fop-enterprise",
        "en": "Enterprise is the skill, vision, and risk-taking ability of the entrepreneur. The entrepreneur takes the financial risk to bring Land, Labour, and Capital together into a viable operating business. Without enterprise, the other three factors remain idle. The economic reward earned by enterprise is Profit.",
        "vi": "Tinh thần khởi nghiệp (Enterprise) là năng lực, tầm nhìn và sự sẵn sàng chấp nhận rủi ro của doanh nhân. Doanh nhân dám mạo hiểm tài chính để kết nối Đất đai, Lao động và Vốn thành một doanh nghiệp vận hành hiệu quả. Nếu thiếu tinh thần khởi nghiệp, ba yếu tố còn lại sẽ ở trạng thái tĩnh. Phần thưởng kinh tế nhận được từ tinh thần doanh nhân là Lợi nhuận (Profit)."
    },
    {
        "id": "sec_specialisation",
        "title": "5. Tầm quan trọng của Chuyên môn hóa & Phân công lao động",
        "selector": "#sec-specialisation",
        "en": "Section 5 examines Specialisation and the Division of Labour. Specialisation occurs when individuals, businesses, or countries concentrate on the tasks and products they perform best. Division of labour splits production into separate, sequential steps where each worker specializes in one specific task, dramatically raising output per worker.",
        "vi": "Mục 5 phân tích về Chuyên môn hóa và Phân công lao động. Chuyên môn hóa diễn ra khi các cá nhân, doanh nghiệp hoặc quốc gia tập trung vào những lĩnh vực và sản phẩm mà họ làm tốt nhất. Phân công lao động chia nhỏ quy trình sản xuất thành các công đoạn tuần tự riêng biệt, nơi mỗi công nhân chuyên tâm làm một việc duy nhất, giúp gia tăng vượt bậc sản lượng trên mỗi lao động."
    },
    {
        "id": "sec_specialisation_advantages",
        "title": "✅ Ưu điểm của Chuyên môn hóa (Advantages)",
        "selector": "#card-specialisation-advantages",
        "en": "Specialisation offers substantial business advantages. Workers become faster and more skilled through continuous repetition. Production moves faster because workers do not waste time switching tools and stations. Furthermore, training labourers for specialized single tasks is much quicker and less costly, significantly driving down unit production costs.",
        "vi": "Chuyên môn hóa mang lại nhiều lợi thế vượt trội cho doanh nghiệp. Công nhân làm việc nhanh hơn và thành thạo hơn nhờ thao tác lặp đi lặp lại. Tiến độ sản xuất được đẩy nhanh do không lãng phí thời gian chuyển đổi dụng cụ hay vị trí làm việc. Hơn nữa, việc đào tạo công nhân cho một thao tác chuyên biệt diễn ra rất nhanh và ít tốn kém, giúp giảm đáng kể chi phí trên từng đơn vị sản phẩm."
    },
    {
        "id": "sec_specialisation_disadvantages",
        "title": "❌ Nhược điểm của Chuyên môn hóa (Disadvantages)",
        "selector": "#card-specialisation-disadvantages",
        "en": "However, specialisation carries significant risks. Performing the same repetitive task all day causes monotony and severe boredom, leading to demotivation, careless errors, and high employee turnover. Crucially, it creates over-dependency: if a key specialized worker is absent, the entire assembly line can grind to a halt.",
        "vi": "Tuy nhiên, chuyên môn hóa cũng tiềm ẩn nhiều rủi ro lớn. Việc lặp đi lặp lại một thao tác suốt cả ngày gây ra sự đơn điệu và nhàm chán, dẫn đến suy giảm động lực, sai sót và tỷ lệ nghỉ việc cao. Đặc biệt, nó tạo ra sự phụ thuộc quá mức: nếu một công nhân chuyên trách vắng mặt, toàn bộ dây chuyền sản xuất có nguy cơ bị đình trệ hoàn toàn."
    },
    {
        "id": "sec_purpose_business",
        "title": "6. Mục đích của Hoạt động Doanh nghiệp",
        "selector": "#sec-purpose-business",
        "en": "Section 6 highlights the primary purpose of business activity. A business is an organization that combines all four factors of production to produce goods and services that satisfy human wants and needs. In doing so, businesses create employment, pay wages, foster innovation, and generate wealth for the broader economy.",
        "vi": "Mục 6 nhấn mạnh mục đích cốt lõi của hoạt động kinh doanh. Doanh nghiệp là một tổ chức kết hợp cả bốn yếu tố sản xuất nhằm tạo ra hàng hóa và dịch vụ thỏa mãn nhu cầu và mong muốn của con người. Thông qua đó, doanh nghiệp tạo công ăn việc làm, trả lương nuôi sống gia đình người lao động, thúc đẩy đổi mới sáng tạo và tạo ra của cải cho toàn bộ nền kinh tế."
    },
    {
        "id": "sec_added_value",
        "title": "7. Giá trị gia tăng (Added Value)",
        "selector": "#sec-added-value",
        "en": "Section 7 introduces one of the most critical concepts in IGCSE Business: Added Value. Added value is the difference between the selling price of a product and the cost of bought-in raw materials used to make it. For example, if a carpenter buys raw timber for 20 dollars and crafts a dining chair sold for 120 dollars, 100 dollars of added value has been created through skill and craftsmanship. Crucially, added value is not profit, because other expenses like rent and wages must still be deducted.",
        "vi": "Mục 7 trình bày khái niệm trọng tâm bậc nhất trong đề thi IGCSE: Giá trị gia tăng (Added Value). Giá trị gia tăng là phần chênh lệch giữa giá bán của thành phẩm và chi phí mua nguyên vật liệu thô đầu vào. Ví dụ, nếu người thợ mộc mua gỗ thô với giá 20 đô la và đóng thành chiếc ghế ăn bán với giá 120 đô la, họ đã tạo ra 100 đô la giá trị gia tăng nhờ tay nghề và thiết kế. Cần nhớ rằng giá trị gia tăng chưa phải là lợi nhuận, vì doanh nghiệp còn phải trang trải các chi phí khác như tiền thuê xưởng và tiền lương."
    },
    {
        "id": "card_increase_added_value",
        "title": "Các phương pháp gia tăng giá trị & Ví dụ Thực tiễn",
        "selector": "#card-increase-added-value",
        "en": "Businesses can increase added value in two fundamental ways: by lowering the cost of bought-in materials while maintaining selling price, or by raising the selling price while maintaining material costs. Practical methods include building a prestigious brand reputation, adding unique innovative features, delivering convenience and speed, or providing exceptional personalized customer service, as seen when luxury jewellery stores invest in velvet packaging and ambient showrooms to command premium prices.",
        "vi": "Doanh nghiệp có thể gia tăng giá trị gia tăng theo hai hướng cơ bản: giảm chi phí nguyên vật liệu mua vào trong khi giữ nguyên giá bán, hoặc tăng giá bán trong khi giữ nguyên chi phí nguyên liệu. Các biện pháp thực tiễn bao gồm xây dựng thương hiệu uy tín, bổ sung tính năng độc đáo, cung cấp dịch vụ nhanh chóng tiện lợi, hoặc mang đến dịch vụ chăm sóc khách hàng đẳng cấp, như cách các cửa hàng trang sức cao cấp đầu tư hộp nhung sang trọng và không gian trưng bày lộng lẫy để bán sản phẩm với mức giá vượt trội."
    }
]

# Major section ranges for section playback mode
major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_intro_business": {"start": 1, "end": 1},
    "sec_economic_problem": {"start": 2, "end": 5},
    "sec_opportunity_cost": {"start": 6, "end": 6},
    "sec_factors_of_production": {"start": 7, "end": 11},
    "sec_specialisation": {"start": 12, "end": 14},
    "sec_purpose_business": {"start": 15, "end": 15},
    "sec_added_value": {"start": 16, "end": 17}
}

# ==============================================================================
# 2. GENERATE NEW HTML FOR PAGE 1
# ==============================================================================
def build_page_1_html():
    html = """<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (NO STUDY RESOURCES) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 1</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.1 Business Activity (Hoạt động Kinh doanh)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. INTRODUCTION TO BUSINESS -->
    <div id="sec-intro-business" class="lecture-interactive-card" data-lecture-section="sec_intro_business" style="margin-bottom: 40px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 18px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">👋 1. INTRODUCTION TO BUSINESS</h2>
        <p style="font-size: 16px; color: #475569; margin-bottom: 15px;">The word ‘business’ is very familiar to us. We are surrounded by businesses and we could not imagine our life without the products we buy from them. So what is a business, or what is business studies?</p>
        <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px 20px; border-radius: 8px; margin-bottom: 15px; font-size: 16px; color: #1e3a8a;">
            Here’s the academic definition for it: <b>“The study of economics and management in how enterprises organise resources to satisfy consumer demands.”</b>
        </div>
        <p style="font-size: 15px; color: #64748b; font-style: italic; margin-bottom: 0;">By the end of this chapter, you will understand the fundamental purpose of business activity and how businesses add value to scarce resources.</p>
    </div>

    <!-- 2. THE ECONOMIC PROBLEM -->
    <div style="margin-bottom: 45px;">
        <div id="sec-economic-problem" class="lecture-interactive-card" data-lecture-section="sec_economic_problem" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 2. THE ECONOMIC PROBLEM</h2>
            <p style="font-size: 15.5px; color: #475569; margin: 0; line-height: 1.6;">The fundamental economic problem is <b>scarcity</b>: human beings have unlimited needs and wants, but the economic resources available to satisfy them are finite. Explore the 3 key concepts below:</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 20px;">
            <div id="card-need" class="lecture-interactive-card" data-lecture-section="sec_economic_need" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #16a34a; font-size: 19px; margin: 0 0 12px 0; border-bottom: 2px dashed #86efac; padding-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🍞 Need</span>
                    <span style="font-size: 12px; background: #dcfce7; color: #16a34a; padding: 2px 8px; border-radius: 12px; font-weight: 600;">Essential</span>
                </h4>
                <p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.6;">A good or service <b>essential for living</b> and survival. <br><i style="color: #64748b;">Examples: clean water, basic food, clothing, and shelter.</i></p>
            </div>

            <div id="card-want" class="lecture-interactive-card" data-lecture-section="sec_economic_want" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #d97706; font-size: 19px; margin: 0 0 12px 0; border-bottom: 2px dashed #fcd34d; padding-bottom: 6px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🚗 Want</span>
                    <span style="font-size: 12px; background: #fef3c7; color: #d97706; padding: 2px 8px; border-radius: 12px; font-weight: 600;">Unlimited</span>
                </h4>
                <p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.6;">A good or service that people would like to have, but is <b>not required</b> for living (unlimited desires). <br><i style="color: #64748b;">Examples: luxury cars, smartphones, dining out, watching movies.</i></p>
            </div>
        </div>

        <div id="card-scarcity" class="lecture-interactive-card" data-lecture-section="sec_economic_scarcity" style="background: #fff5f5; border: 1.5px solid #fecaca; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s;">
            <h4 style="color: #dc2626; font-size: 19px; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
                <span>⚠️ Scarcity (Sự khan hiếm)</span>
            </h4>
            <p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.6;">
                Scarcity is the basic economic problem. It is a situation that exists when <b><span style="color: #dc2626;">there are unlimited wants and limited resources</span></b> to produce the goods and services to satisfy those wants. <br><br>
                <i style="color: #64748b;">For example, consumers have limited income but endless desires to purchase goods. Similarly, economies have limited factors of production to produce everything citizens want.</i>
            </p>
        </div>
    </div>

    <!-- 3. OPPORTUNITY COST -->
    <div id="sec-opportunity-cost" class="lecture-interactive-card" data-lecture-section="sec_opportunity_cost" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 12px; margin-bottom: 18px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🔄 3. OPPORTUNITY COST</h2>
        <p style="font-size: 16px; color: #475569; margin-bottom: 20px;"><b>Opportunity cost</b> is the <b>next best alternative forgone by choosing another item</b>. Due to scarcity, consumers, businesses, and governments are forced to make choices. Every choice involves an opportunity cost.</p>

        <div style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: center; align-items: center; background: #fff7ed; padding: 18px 20px; border-radius: 10px; border: 2px dashed #fed7aa; color: #ea580c; font-weight: bold; font-size: 17px; margin-bottom: 20px; text-align: center;">
            <span>SCARCITY (Nguồn lực có hạn)</span> <span>➔</span> <span>CHOICE (Lựa chọn)</span> <span>➔</span> <span>OPPORTUNITY COST (Chi phí cơ hội)</span>
        </div>

        <div style="background: #f8fafc; border-left: 4px solid #94a3b8; padding: 16px 20px; border-radius: 8px; font-size: 15px; color: #475569; line-height: 1.6;">
            <b>Example:</b> A business has limited capital and must choose between purchasing a new delivery van or investing in an advertising campaign. If the business chooses the van, the opportunity cost is the potential increase in sales and customer awareness that could have been gained from the advertising campaign.
        </div>
    </div>

    <!-- 4. FACTORS OF PRODUCTION -->
    <div style="margin-bottom: 45px;">
        <div id="sec-factors-of-production" class="lecture-interactive-card" data-lecture-section="sec_factors_of_production" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #a855f7; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏭 4. FACTORS OF PRODUCTION</h2>
            <p style="font-size: 15.5px; color: #475569; margin: 0; line-height: 1.6;">Factors of Production are the scarce resources required to produce goods or services. They are classified into four categories: <b>Land, Labour, Capital, and Enterprise</b>. Bấm vào từng yếu tố bên dưới hoặc sơ đồ để nghe giảng chi tiết:</p>
        </div>

        <div id="card-fop-map" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 28px; box-shadow: 0 4px 10px rgba(0,0,0,0.03); margin-bottom: 25px;">
            <h3 style="text-align: center; color: #0f172a; margin-top: 0; font-size: 20px; margin-bottom: 8px;">Interactive F.O.P Map</h3>
            <p style="text-align: center; color: #64748b; font-style: italic; margin-bottom: 25px; font-size: 14px;">Bấm hoặc lướt chuột vào 4 yếu tố sản xuất dưới đây để xem định nghĩa và nghe bài giảng:</p>

            <div style="display: flex; flex-wrap: wrap; gap: 30px; align-items: center; justify-content: center;">
                <div style="flex: 1; min-width: 250px; max-width: 320px; position: relative;">
                    <svg viewBox="0 0 300 300" width="100%" height="auto" style="display: block; margin: 0 auto;">
                        <circle cx="150" cy="150" r="40" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="3"></circle>
                        <text x="150" y="145" font-family="Arial" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">Factors of</text>
                        <text x="150" y="165" font-family="Arial" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">Production</text>
                        <line x1="150" y1="110" x2="150" y2="70" stroke="#cbd5e1" stroke-width="3"></line>
                        <line x1="150" y1="190" x2="150" y2="230" stroke="#cbd5e1" stroke-width="3"></line>
                        <line x1="110" y1="150" x2="70" y2="150" stroke="#cbd5e1" stroke-width="3"></line>
                        <line x1="190" y1="150" x2="230" y2="150" stroke="#cbd5e1" stroke-width="3"></line>

                        <!-- LAND -->
                        <g id="svg-fop-land" class="lecture-interactive-card" data-lecture-section="fop_land" style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-land-bus').innerHTML; this.children[0].setAttribute('stroke', '#15803d'); this.children[0].setAttribute('stroke-width', '4');" onmouseout="this.children[0].setAttribute('stroke', '#4ade80'); this.children[0].setAttribute('stroke-width', '2');" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-land-bus').innerHTML;">
                            <circle cx="150" cy="45" r="35" fill="#dcfce7" stroke="#4ade80" stroke-width="2"></circle>
                            <text x="150" y="50" font-family="Arial" font-size="13" font-weight="bold" fill="#166534" text-anchor="middle">LAND</text>
                        </g>

                        <!-- LABOUR -->
                        <g id="svg-fop-labour" class="lecture-interactive-card" data-lecture-section="fop_labour" style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-labour-bus').innerHTML; this.children[0].setAttribute('stroke', '#1d4ed8'); this.children[0].setAttribute('stroke-width', '4');" onmouseout="this.children[0].setAttribute('stroke', '#60a5fa'); this.children[0].setAttribute('stroke-width', '2');" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-labour-bus').innerHTML;">
                            <circle cx="150" cy="255" r="35" fill="#dbeafe" stroke="#60a5fa" stroke-width="2"></circle>
                            <text x="150" y="260" font-family="Arial" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">LABOUR</text>
                        </g>

                        <!-- CAPITAL -->
                        <g id="svg-fop-capital" class="lecture-interactive-card" data-lecture-section="fop_capital" style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-capital-bus').innerHTML; this.children[0].setAttribute('stroke', '#b45309'); this.children[0].setAttribute('stroke-width', '4');" onmouseout="this.children[0].setAttribute('stroke', '#facc15'); this.children[0].setAttribute('stroke-width', '2');" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-capital-bus').innerHTML;">
                            <circle cx="45" cy="150" r="35" fill="#fef3c7" stroke="#facc15" stroke-width="2"></circle>
                            <text x="45" y="155" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">CAPITAL</text>
                        </g>

                        <!-- ENTERPRISE -->
                        <g id="svg-fop-enterprise" class="lecture-interactive-card" data-lecture-section="fop_enterprise" style="cursor: pointer; transition: 0.2s;" onmouseover="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-enterprise-bus').innerHTML; this.children[0].setAttribute('stroke', '#7e22ce'); this.children[0].setAttribute('stroke-width', '4');" onmouseout="this.children[0].setAttribute('stroke', '#c084fc'); this.children[0].setAttribute('stroke-width', '2');" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-enterprise-bus').innerHTML;">
                            <circle cx="255" cy="150" r="35" fill="#f3e8ff" stroke="#c084fc" stroke-width="2"></circle>
                            <text x="255" y="155" font-family="Arial" font-size="10" font-weight="bold" fill="#6b21a8" text-anchor="middle">ENTERPRISE</text>
                        </g>
                    </svg>
                </div>

                <div id="fop-panel-bus" style="flex: 1.5; min-width: 250px; background: #fdf4ff; border-left: 6px solid #d946ef; border-radius: 10px; padding: 22px; min-height: 180px; display: flex; flex-direction: column; justify-content: center; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
                    <h4 style="margin: 0 0 10px 0; color: #9333ea; font-size: 20px;">💡 ENTERPRISE</h4>
                    <p style="margin: 0 0 15px 0; font-size: 15px; color: #4c1d95; line-height: 1.6;">The risk taking ability of the person who brings the other factors of production together to produce a good or service.</p>
                    <div style="background: #f3e8ff; padding: 8px 14px; border-radius: 6px; font-size: 15px; color: #9333ea; font-weight: bold; border: 1px dashed #d8b4fe; display: inline-block;">🏆 Reward: PROFIT</div>
                </div>
            </div>
        </div>

        <!-- 4 DISTINCT FACTOR CARDS -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
            <div id="card-fop-land" class="lecture-interactive-card" data-lecture-section="fop_land" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s;" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-land-bus').innerHTML;">
                <h4 style="margin: 0 0 8px 0; color: #16a34a; font-size: 17px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🌲 LAND (Đất đai)</span>
                    <span style="font-size: 11px; background: #dcfce7; padding: 2px 6px; border-radius: 10px; font-weight: 700;">Rent</span>
                </h4>
                <p style="margin: 0 0 10px 0; font-size: 14px; color: #14532d; line-height: 1.5;">Natural resources obtained from nature: soil, minerals, forests, oil, gas and water.</p>
                <div style="font-size: 13px; color: #15803d; font-weight: bold;">🏆 Reward: RENT</div>
            </div>

            <div id="card-fop-labour" class="lecture-interactive-card" data-lecture-section="fop_labour" style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-left: 5px solid #2563eb; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s;" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-labour-bus').innerHTML;">
                <h4 style="margin: 0 0 8px 0; color: #2563eb; font-size: 17px; display: flex; align-items: center; justify-content: space-between;">
                    <span>👷‍♂️ LABOUR (Lao động)</span>
                    <span style="font-size: 11px; background: #dbeafe; padding: 2px 6px; border-radius: 10px; font-weight: 700;">Wages</span>
                </h4>
                <p style="margin: 0 0 10px 0; font-size: 14px; color: #1e3a8a; line-height: 1.5;">Physical and mental human efforts contributed by workers in the production process.</p>
                <div style="font-size: 13px; color: #1d4ed8; font-weight: bold;">🏆 Reward: WAGE / SALARY</div>
            </div>

            <div id="card-fop-capital" class="lecture-interactive-card" data-lecture-section="fop_capital" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #d97706; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s;" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-capital-bus').innerHTML;">
                <h4 style="margin: 0 0 8px 0; color: #d97706; font-size: 17px; display: flex; align-items: center; justify-content: space-between;">
                    <span>🚜 CAPITAL (Vốn)</span>
                    <span style="font-size: 11px; background: #fef3c7; padding: 2px 6px; border-radius: 10px; font-weight: 700;">Interest</span>
                </h4>
                <p style="margin: 0 0 10px 0; font-size: 14px; color: #713f12; line-height: 1.5;">Man-made equipment, finance, machinery, buildings and tools used to produce goods.</p>
                <div style="font-size: 13px; color: #b45309; font-weight: bold;">🏆 Reward: INTEREST</div>
            </div>

            <div id="card-fop-enterprise" class="lecture-interactive-card" data-lecture-section="fop_enterprise" style="background: #faf5ff; border: 1.5px solid #e9d5ff; border-left: 5px solid #9333ea; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s;" onclick="document.getElementById('fop-panel-bus').innerHTML = document.getElementById('fop-enterprise-bus').innerHTML;">
                <h4 style="margin: 0 0 8px 0; color: #9333ea; font-size: 17px; display: flex; align-items: center; justify-content: space-between;">
                    <span>💡 ENTERPRISE (Khởi nghiệp)</span>
                    <span style="font-size: 11px; background: #f3e8ff; padding: 2px 6px; border-radius: 10px; font-weight: 700;">Profit</span>
                </h4>
                <p style="margin: 0 0 10px 0; font-size: 14px; color: #4c1d95; line-height: 1.5;">The risk-taking skill to coordinate Land, Labour and Capital into a viable enterprise.</p>
                <div style="font-size: 13px; color: #7e22ce; font-weight: bold;">🏆 Reward: PROFIT</div>
            </div>
        </div>

        <!-- HIDDEN TEMPLATES FOR PANEL -->
        <div style="display: none;">
            <div id="fop-land-bus">
                <h4 style="margin: 0 0 10px 0; color: #16a34a; font-size: 20px;">🌳 LAND</h4>
                <p style="margin: 0 0 10px 0; font-size: 15px; color: #14532d; line-height: 1.6;">The natural resources that can be obtained from nature. This includes minerals, forests, oil, gas and water.</p>
                <div style="background: #dcfce7; padding: 8px 12px; border-radius: 6px; font-size: 15px; color: #16a34a; font-weight: bold; border: 1px dashed #86efac; display: inline-block;">🏆 Reward: RENT</div>
            </div>
            <div id="fop-labour-bus">
                <h4 style="margin: 0 0 10px 0; color: #2563eb; font-size: 20px;">👷‍♂️ LABOUR</h4>
                <p style="margin: 0 0 10px 0; font-size: 15px; color: #1e3a8a; line-height: 1.6;">The physical and mental efforts put in by the workers in the production process.</p>
                <div style="background: #dbeafe; padding: 8px 12px; border-radius: 6px; font-size: 15px; color: #2563eb; font-weight: bold; border: 1px dashed #93c5fd; display: inline-block;">🏆 Reward: WAGE / SALARY</div>
            </div>
            <div id="fop-capital-bus">
                <h4 style="margin: 0 0 10px 0; color: #d97706; font-size: 20px;">🚜 CAPITAL</h4>
                <p style="margin: 0 0 10px 0; font-size: 15px; color: #713f12; line-height: 1.6;">The finance, machinery and man-made equipment needed for the production of goods and services.</p>
                <div style="background: #fef3c7; padding: 8px 12px; border-radius: 6px; font-size: 15px; color: #d97706; font-weight: bold; border: 1px dashed #fcd34d; display: inline-block;">🏆 Reward: INTEREST</div>
            </div>
            <div id="fop-enterprise-bus">
                <h4 style="margin: 0 0 10px 0; color: #9333ea; font-size: 20px;">💡 ENTERPRISE</h4>
                <p style="margin: 0 0 15px 0; font-size: 15px; color: #4c1d95; line-height: 1.6;">The risk taking ability of the person who brings the other factors of production together to produce a good or service.</p>
                <div style="background: #f3e8ff; padding: 8px 12px; border-radius: 6px; font-size: 15px; color: #9333ea; font-weight: bold; border: 1px dashed #d8b4fe; display: inline-block;">🏆 Reward: PROFIT</div>
            </div>
        </div>
    </div>

    <!-- 5. SPECIALIZATION & DIVISION OF LABOUR -->
    <div style="margin-bottom: 45px;">
        <div id="sec-specialisation" class="lecture-interactive-card" data-lecture-section="sec_specialisation" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🎯 5. IMPORTANCE OF SPECIALISATION</h2>
            <p style="font-size: 15.5px; color: #475569; margin-bottom: 15px;">Specialization occurs when a person, organisation or country <b>concentrates on a task at which they are best at</b>, rather than trying to produce everything themselves.</p>

            <div style="background: #f0fdfa; border-left: 4px solid #0d9488; padding: 15px 20px; border-radius: 6px; margin-bottom: 15px;">
                <b style="color: #0f766e; font-size: 15.5px;">🔑 Division of Labour:</b> When the production process is split into separate tasks, and each worker specialises in performing one specific task.
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; font-size: 14.5px;">
                    <b style="color: #0f766e;">👤 By Individuals:</b> Specialise in a trade/profession (e.g. engineer, doctor, accountant).
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; font-size: 14.5px;">
                    <b style="color: #0f766e;">🏢 By Businesses:</b> Focus on specific product lines to gain market edge.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; font-size: 14.5px;">
                    <b style="color: #0f766e;">🌍 By Countries:</b> Produce goods endowed by nature (e.g. coffee in Vietnam).
                </div>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-specialisation-advantages" class="lecture-interactive-card" data-lecture-section="sec_specialisation_advantages" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #15803d; font-size: 18px; margin: 0 0 14px 0; display: flex; align-items: center; justify-content: space-between;">
                    <span>✅ Advantages of Specialisation</span>
                </h4>
                <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 14.5px; line-height: 1.6;">
                    <li>Workers specialise in specific tasks, <b>increasing efficiency and output</b>.</li>
                    <li><b>Saves time and energy</b>: production is faster without tool-switching delays.</li>
                    <li><b>Quicker to train labourers</b>: workers concentrate on one task.</li>
                    <li><b>Skill development</b>: workers master their craft through repetition.</li>
                </ul>
            </div>

            <div id="card-specialisation-disadvantages" class="lecture-interactive-card" data-lecture-section="sec_specialisation_disadvantages" style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #b91c1c; font-size: 18px; margin: 0 0 14px 0; display: flex; align-items: center; justify-content: space-between;">
                    <span>❌ Disadvantages of Specialisation</span>
                </h4>
                <ul style="margin: 0; padding-left: 20px; color: #991b1b; font-size: 14.5px; line-height: 1.6;">
                    <li>Work becomes <b>monotonous and boring</b>, reducing motivation.</li>
                    <li><b>Higher labour turnover</b> or absenteeism as bored workers leave.</li>
                    <li><b>Over-dependency</b>: if a specialist is absent, the entire process can halt.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 6. PURPOSE OF BUSINESS ACTIVITY -->
    <div id="sec-purpose-business" class="lecture-interactive-card" data-lecture-section="sec_purpose_business" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #6366f1; padding-bottom: 12px; margin-bottom: 18px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🚀 6. PURPOSE OF BUSINESS ACTIVITY</h2>
        <p style="font-size: 16px; color: #475569; margin-bottom: 16px;">Businesses exist to solve the economic problem by transforming scarce inputs into valuable outputs:</p>
        <div style="background: #eef2ff; border: 2px solid #c7d2fe; padding: 20px; border-radius: 10px; margin-bottom: 16px; text-align: center;">
            <p style="margin: 0; font-size: 17.5px; color: #4338ca; font-weight: bold; line-height: 1.5;">
                A business is an organization that combines all four factors of production (resources) to create goods and services to satisfy human wants and needs.
            </p>
        </div>
        <p style="font-size: 15px; color: #64748b; margin: 0; line-height: 1.6;">Businesses allocate scarce resources efficiently to produce and distribute goods and services that satisfy consumer needs and wants, creating jobs and wealth.</p>
    </div>

    <!-- 7. ADDED VALUE -->
    <div style="margin-bottom: 45px;">
        <div id="sec-added-value" class="lecture-interactive-card" data-lecture-section="sec_added_value" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">✨ 7. ADDED VALUE</h2>
            <p style="font-size: 16px; color: #475569; margin-bottom: 16px; line-height: 1.6;">
                Added value is the <b><span style="color: #be185d;">difference between the cost of materials bought in and the selling price of the product</span></b>. <br><br>
                It is the amount of value the business has added to the raw materials by processing them into finished products. Adding value enables businesses to charge a price well above their raw material costs and make a profit.
            </p>
            <div style="background: #fdf2f8; border-left: 4px solid #f472b6; padding: 16px 20px; border-radius: 8px; font-size: 15px; color: #831843;">
                <b>Example:</b> Raw timber bought by a furniture maker costs $20. The carpenter crafts it into a dining chair and sells it for $120. The carpenter has <b>added $100 of value</b> to the timber through craftsmanship, design, and manufacturing.
            </div>
        </div>

        <div id="card-increase-added-value" class="lecture-interactive-card" data-lecture-section="card_increase_added_value" style="padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h3 style="color: #0f172a; font-size: 20px; margin-top: 0; margin-bottom: 14px;">📈 How can a business increase added value?</h3>
            <ul style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 15px; line-height: 1.6;">
                <li><b>Reducing the cost of materials/production:</b> Lower purchase cost of raw materials while maintaining the same selling price increases added value.</li>
                <li><b>Raising the selling price:</b> Increase prices while keeping material costs unchanged increases added value.</li>
            </ul>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px;">
                <div style="background: #fafafa; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px;">
                    <h4 style="color: #ec4899; font-size: 17px; margin: 0 0 12px 0;">🛠️ Practical Methods to Add Value</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 14px; line-height: 1.6;">
                        <li><b>Branding:</b> Strong brand image that creates trust and loyalty.</li>
                        <li><b>Special features:</b> Unique design or enhanced functionality.</li>
                        <li><b>Convenience &amp; speed:</b> Rapid, hassle-free service.</li>
                        <li><b>Premium service:</b> Expert advice and luxury packaging.</li>
                    </ul>
                </div>

                <div style="background: #fafafa; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px;">
                    <h4 style="color: #ec4899; font-size: 17px; margin: 0 0 12px 0;">💍 Practical Example: Jewellery Store</h4>
                    <ul style="margin: 0 0 10px 0; padding-left: 18px; color: #475569; font-size: 14px; line-height: 1.6;">
                        <li>Design an attractive luxury gift box with velvet lining.</li>
                        <li>Create an ambient, well-lit shop-window display.</li>
                        <li>Hire well-dressed sales staff for personal advice.</li>
                    </ul>
                    <p style="margin: 0; font-size: 13.5px; color: #be185d; font-weight: bold;">➔ These measures command premium selling prices far exceeding costs.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- SCRIPT FOR AUTO-SYNCING INTERACTIVE PANEL -->
    <script>
    window.addEventListener('message', function(e) {
        if (e.data && e.data.type === 'HIGHLIGHT_LECTURE_SECTION') {
            var sel = e.data.selector || '';
            var fopMap = {
                'land': 'fop-land-bus',
                'labour': 'fop-labour-bus',
                'capital': 'fop-capital-bus',
                'enterprise': 'fop-enterprise-bus'
            };
            for (var k in fopMap) {
                if (sel.indexOf(k) !== -1) {
                    var p = document.getElementById('fop-panel-bus');
                    var src = document.getElementById(fopMap[k]);
                    if (p && src) {
                        p.innerHTML = src.innerHTML;
                    }
                    break;
                }
            }
        }
    });
    </script>
</div>"""
    return html

# ==============================================================================
# 3. GENERATE NEW HTML FOR PAGE 2 (BILINGUAL)
# ==============================================================================
def build_page_2_html(original_p2):
    # Remove the Study Resources block from page 2 and replace with Top Header Banner
    pattern = r'<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">[\s\S]*?</div>'
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.1 Business Activity (Hoạt động Kinh doanh)</h1>
        </div>
    </div>"""
    new_p2 = re.sub(pattern, header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 1.1 Audio and HTML ===")
    
    # 0. Clean stale audio files so that all 18 segments match perfectly
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)
    valid_ids = {s['id'] for s in segments}
    for fname in os.listdir(audio_dir):
        if fname.endswith('.mp3'):
            base_id = fname[:-4]
            # Remove audio if not in valid_ids or if segment text was redesigned
            if base_id not in valid_ids or base_id in {'sec_economic_problem', 'sec_factors_of_production', 'sec_specialisation', 'sec_added_value', 'fop_interactive_map'}:
                try:
                    os.remove(os.path.join(audio_dir, fname))
                    print(f"  [CLEAN] Removed outdated audio: {fname}")
                except Exception as e:
                    print(f"  [WARN] Could not remove {fname}: {e}")

    # 1. Generate audio files and write manifest.json
    print(f"\nGenerating {len(segments)} audio segments...")
    manifest = await process_lecture_audio(CODE, LID, COURSE_TITLE, TITLE, segments, major_sections, subject='business')
    
    # 2. Build Page 1 HTML
    p1_html = build_page_1_html()
    diff1 = len(p1_html.split('<div')) - len(p1_html.split('</div>'))
    print(f"\nPage 1 HTML div diff: {diff1}")
    if diff1 != 0:
        raise ValueError(f"Page 1 has div balance error: {diff1}")
        
    # 3. Build Page 2 HTML
    with open('scripts/bs_1_1_page_2.html', 'r', encoding='utf-8') as f:
        orig_p2 = f.read()
    p2_html = build_page_2_html(orig_p2)
    diff2 = len(p2_html.split('<div')) - len(p2_html.split('</div>'))
    print(f"Page 2 HTML div diff: {diff2}")
    if diff2 != 0:
        raise ValueError(f"Page 2 has div balance error: {diff2}")
        
    # 4. Update Supabase
    print("\nUpdating Supabase page 1...")
    res1 = sb.table('lecture_pages').update({'content_html': p1_html}).eq('lecture_id', LID).eq('page_number', 1).execute()
    print(f"Page 1 updated: {len(res1.data)} rows.")
    
    print("Updating Supabase page 2...")
    res2 = sb.table('lecture_pages').update({'content_html': p2_html}).eq('lecture_id', LID).eq('page_number', 2).execute()
    print(f"Page 2 updated: {len(res2.data)} rows.")
    
    print("\n✅ REBUILD 1.1 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
