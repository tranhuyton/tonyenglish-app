import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 1.3 ID
LID = 'a8ebc541-78ef-4202-96ad-161ed647a1b1'
CODE = '1_3'
TITLE = '1.3 Enterprise, business growth and size'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 18 AUDIO SEGMENTS FOR LESSON 1.3
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.3: Khởi sự, Tăng trưởng và Quy mô Doanh nghiệp",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.3: Enterprise, Business Growth and Size. In this lesson, we examine the qualities of successful entrepreneurs, the components and benefits of a business plan, government startup initiatives, methods and limitations of measuring business size, internal versus external growth strategies, and why businesses remain small or fail.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.3: Khởi sự, Tăng trưởng và Quy mô Doanh nghiệp. Trong bài học này, chúng ta sẽ tìm hiểu các phẩm chất của doanh nhân thành công, cấu trúc và lợi ích của kế hoạch kinh doanh, chính sách hỗ trợ khởi nghiệp của chính phủ, các thước đo quy mô doanh nghiệp, chiến lược tăng trưởng nội bộ và sáp nhập, cùng lý do doanh nghiệp giữ quy mô nhỏ hoặc phá sản."
    },
    {
        "id": "sec_entrepreneurship",
        "title": "1. Tinh thần Doanh nhân (Entrepreneurship)",
        "selector": "#sec-entrepreneurship",
        "en": "Section 1 defines an entrepreneur as an individual who organizes, operates, and assumes the financial risks of a new business venture. Entrepreneurs bring together Land, Labour, and Capital to produce goods and services, driving innovation, employment, and economic growth.",
        "vi": "Mục 1 định nghĩa doanh nhân (entrepreneur) là người đứng ra tổ chức, vận hành và dám gánh vác rủi ro tài chính cho một dự án kinh doanh mới. Doanh nhân kết nối Đất đai, Lao động và Vốn để sản xuất hàng hóa và dịch vụ, tạo động lực đổi mới, việc làm và tăng trưởng kinh tế."
    },
    {
        "id": "card_entrepreneur_traits",
        "title": "🎯 8 Phẩm chất Cốt lõi của Doanh nhân Thành công",
        "selector": "#card-entrepreneur-traits",
        "en": "Cambridge identifies eight essential characteristics of successful entrepreneurs: calculated risk-taking, creativity, optimism, self-confidence, innovativeness, independence, persuasive communication, and relentless hard work. Possessing these traits enables founders to navigate commercial uncertainty and persevere through early business setbacks.",
        "vi": "Giáo trình Cambridge chỉ ra 8 phẩm chất cốt lõi của một doanh nhân thành công: dám chấp nhận rủi ro có tính toán, óc sáng tạo, tinh thần lạc quan, sự tự tin, năng lực đổi mới, tính tự chủ độc lập, kỹ năng giao tiếp thuyết phục và sự chăm chỉ kiên trì. Những phẩm chất này giúp nhà sáng lập vượt qua các bất định thương mại và đứng dậy sau những thử thách ban đầu."
    },
    {
        "id": "sec_business_plan",
        "title": "2. Kế hoạch Kinh doanh (Business Plan)",
        "selector": "#sec-business-plan",
        "en": "Section 2 focuses on the business plan—a formal written document setting out the business objectives, marketing strategy, operations structure, and financial forecasts, including cash flow projections and break-even calculations. A robust business plan forces founders to anticipate obstacles and provides clear operational direction.",
        "vi": "Mục 2 tập trung vào bản kế hoạch kinh doanh (business plan) – một văn bản chính thức vạch rõ các mục tiêu của doanh nghiệp, chiến lược tiếp thị, kế hoạch vận hành và các dự báo tài chính như dòng tiền và điểm hòa vốn. Bản kế hoạch kinh doanh chặt chẽ giúp nhà sáng lập lường trước khó khăn và định hướng vận hành xuyên suốt."
    },
    {
        "id": "card_plan_contents",
        "title": "📑 9 Nội dung Trọng tâm trong Bản Kế hoạch Kinh doanh",
        "selector": "#card-plan-contents",
        "en": "A comprehensive business plan covers nine vital areas: an executive summary, owner background, business description, target market analysis, advertising strategies, premises and equipment requirements, organizational structure, cost and pricing models, and cash flow forecasts.",
        "vi": "Một bản kế hoạch kinh doanh hoàn chỉnh bao gồm 9 nội dung trọng tâm: tóm tắt dự án, lý lịch và kinh nghiệm của chủ sở hữu, mô tả sản phẩm dịch vụ, phân tích thị trường mục tiêu và đối thủ, kế hoạch quảng bá tiếp thị, địa điểm và trang thiết bị nhà xưởng, cơ cấu tổ chức pháp lý, chi phí và cấu trúc định giá, cùng dự báo dòng tiền và kế hoạch mở rộng tương lai."
    },
    {
        "id": "card_plan_benefits",
        "title": "🌟 Lợi ích của Kế hoạch Kinh doanh",
        "selector": "#card-plan-benefits",
        "en": "Developing a business plan yields three crucial benefits: it keeps management focused on the core mission and long-term vision, it aligns and motivates employees around transparent targets, and it is strictly required by banks and investors when evaluating loan and equity finance applications.",
        "vi": "Xây dựng kế hoạch kinh doanh mang lại 3 lợi ích then chốt: giúp ban lãnh đạo không bị chệch hướng khỏi sứ mệnh và tầm nhìn dài hạn, tạo động lực gắn kết nhân viên theo các mục tiêu minh bạch, và là điều kiện bắt buộc để các ngân hàng và nhà đầu tư thẩm định cấp vốn vay hoặc góp vốn cổ phần."
    },
    {
        "id": "sec_gov_support",
        "title": "3. Hỗ trợ của Chính phủ cho Doanh nghiệp Khởi nghiệp (Startups)",
        "selector": "#sec-gov-support",
        "en": "Section 3 examines government support for startups. A startup is an entrepreneurial venture in its early stages designed to capitalize on perceived market demand. Governments actively foster startup ecosystems to generate broad economic and social benefits.",
        "vi": "Mục 3 tìm hiểu chính sách hỗ trợ của chính phủ dành cho doanh nghiệp khởi nghiệp (startups). Startup là doanh nghiệp ở giai đoạn đầu thành lập nhằm khai thác nhu cầu thị trường tiềm năng. Chính phủ tích cực nuôi dưỡng hệ sinh thái khởi nghiệp vì những lợi ích to lớn đối với nền kinh tế và xã hội."
    },
    {
        "id": "card_why_gov_help",
        "title": "❓ Vì sao Chính phủ Khuyến khích Khởi nghiệp?",
        "selector": "#card-why-gov-help",
        "en": "Governments assist startups for four strategic reasons: they create new employment opportunities, expand national economic output and GDP, generate export revenues if internationally competitive, and introduce disruptive technologies and ideas that raise overall industrial productivity.",
        "vi": "Chính phủ hỗ trợ khởi nghiệp vì 4 lý do chiến lược: giải quyết việc làm cho người lao động, thúc đẩy tăng trưởng sản lượng quốc gia và GDP, đóng góp vào kim ngạch xuất khẩu khi vươn ra thị trường quốc tế, và đưa các ý tưởng công nghệ đột phá vào đời sống giúp nâng cao năng suất toàn ngành."
    },
    {
        "id": "card_how_gov_support",
        "title": "🛠️ Các Biện pháp Hỗ trợ Khởi nghiệp Thực tế",
        "selector": "#card-how-gov-support",
        "en": "Governments deploy multiple supportive measures: offering free bureaucratic and legal advice, providing subsidized enterprise zones with affordable rent, issuing low-interest commercial loans, awarding non-repayable capital grants, financing management training workshops, and granting tax holidays.",
        "vi": "Chính phủ triển khai nhiều hình thức hỗ trợ cụ thể: tư vấn pháp lý và thủ tục hành chính miễn phí, cấp mặt bằng giá ưu đãi tại các khu ươm tạo doanh nghiệp, cung cấp các gói vay lãi suất thấp, tài trợ các khoản viện trợ không hoàn lại để mua sắm máy móc, tổ chức các khóa đào tạo kỹ năng quản trị, và áp dụng chính sách miễn giảm thuế (tax holidays) trong những năm đầu."
    },
    {
        "id": "sec_measuring_size",
        "title": "4. Đo lường Quy mô Doanh nghiệp (Measuring Business Size)",
        "selector": "#sec-measuring-size",
        "en": "Section 4 outlines the four accepted Cambridge criteria for measuring business size: total number of employees, total physical volume or value of output, total value of sales revenue, and total capital employed in long-term assets.",
        "vi": "Mục 4 trình bày 4 tiêu chí chuẩn mực theo Cambridge để đo lường quy mô doanh nghiệp: tổng số lượng lao động tuyển dụng, giá trị hoặc sản lượng sản phẩm đầu ra, doanh thu bán hàng, và tổng số vốn hoạt động dài hạn (capital employed)."
    },
    {
        "id": "card_profit_not_size",
        "title": "🚫 Lưu ý Đề thi: Lợi nhuận KHÔNG phải là Thước đo Quy mô",
        "selector": "#card-profit-not-size",
        "en": "Examiners stress that profit is never an acceptable measure of business size. A huge multinational with thousands of staff can incur temporary losses during economic downturns, while a tiny boutique firm can earn enormous profit margins. Furthermore, profits fluctuate unpredictably with tax and accounting adjustments.",
        "vi": "Giám khảo Cambridge đặc biệt lưu ý: Lợi nhuận tuyệt đối không được dùng làm thước đo quy mô doanh nghiệp. Một tập đoàn đa quốc gia khổng lồ với hàng chục ngàn nhân viên vẫn có thể tạm thời thua lỗ trong thời kỳ suy thoái kinh tế, trong khi một văn phòng luật ngách chỉ có hai người lại có thể đạt tỷ suất lợi nhuận cực cao. Hơn nữa, lợi nhuận biến động liên tục theo chính sách thuế và kế toán."
    },
    {
        "id": "card_size_limitations",
        "title": "⚠️ Hạn chế của các Thước đo Quy mô",
        "selector": "#card-size-limitations",
        "en": "Each measurement method has significant limitations. Comparing employee numbers fails between automated capital-intensive factories and labour-intensive workshops. Comparing sales revenue or output value is misleading when contrasting high-value luxury goods with cheap mass-market items.",
        "vi": "Mỗi phương pháp đo lường đều có hạn chế nhất định. Việc so sánh số lượng nhân viên sẽ sai lệch khi so một nhà máy tự động hóa hiện đại với một xưởng thủ công sử dụng nhiều lao động. Việc so sánh doanh thu hay giá trị sản lượng cũng không chính xác khi đặt cạnh nhau sản phẩm xa xỉ giá cao với hàng tiêu dùng đại trà giá rẻ."
    },
    {
        "id": "sec_business_growth",
        "title": "5. Chiến lược Tăng trưởng Doanh nghiệp (Business Growth)",
        "selector": "#sec-business-growth",
        "en": "Section 5 contrasts internal and external growth. Internal organic growth expands existing operations using retained profits. External growth involves mergers and takeovers, enabling rapid market penetration.",
        "vi": "Mục 5 phân tích hai con đường tăng trưởng doanh nghiệp. Tăng trưởng nội bộ (internal growth) là việc tự mở rộng hoạt động hiện có từ nguồn lợi nhuận giữ lại. Tăng trưởng bên ngoài (external growth) diễn ra thông qua sáp nhập và mua lại (M&A), giúp thâm nhập thị trường thần tốc."
    },
    {
        "id": "card_external_growth_types",
        "title": "🔗 4 Hình thức Sáp nhập & Mua lại (Integration Types)",
        "selector": "#card-external-growth-types",
        "en": "External integration takes four forms: horizontal integration with a direct competitor at the same production stage; backward vertical integration with a raw material supplier; forward vertical integration with a retail outlet; and conglomerate diversification into an entirely different industry to spread risk.",
        "vi": "Tăng trưởng bên ngoài gồm 4 hình thức sáp nhập: sáp nhập ngang (horizontal) với đối thủ cạnh tranh cùng ngành ở cùng công đoạn; sáp nhập dọc lùi (backward vertical) với nhà cung ứng nguyên liệu; sáp nhập dọc tiến (forward vertical) với các kênh bán lẻ tiêu thụ; và sáp nhập tập đoàn đa ngành (conglomerate) vào lĩnh vực hoàn toàn mới để phân tán rủi ro."
    },
    {
        "id": "card_growth_problems_overcome",
        "title": "🛡️ Thách thức khi Mở rộng và Giải pháp Quản trị",
        "selector": "#card-growth-problems-overcome",
        "en": "Rapid growth introduces managerial diseconomies of scale, cash flow overtrading, and cultural conflict. Managers overcome these by decentralising decision-making, adopting controlled expansion financed by equity, upgrading IT communication networks, and conducting proactive change management.",
        "vi": "Tăng trưởng nóng thường kéo theo phi tính kinh tế của quy mô, tình trạng cạn kiệt vốn lưu động (overtrading) và xung đột văn hóa sau sáp nhập. Các nhà quản trị khắc phục bằng cách phân quyền quản lý cho cấp dưới, kiểm soát tốc độ mở rộng bằng vốn tự có thay vì nợ ngắn hạn, nâng cấp hạ tầng CNTT kết nối nội bộ và chủ động thực hiện quản trị thay đổi văn hóa doanh nghiệp."
    },
    {
        "id": "sec_why_stay_small",
        "title": "6. Tại sao Nhiều Doanh nghiệp Chọn Duy trì Quy mô Nhỏ",
        "selector": "#sec-why-stay-small",
        "en": "Section 6 highlights why businesses deliberately stay small: operating in specialized service industries requiring personal touch, serving niche geographic markets with limited total demand, or fulfilling owner lifestyle objectives for independence, personal customer relationships, and low managerial stress.",
        "vi": "Mục 6 lý giải nguyên nhân nhiều doanh nghiệp chủ động giữ quy mô nhỏ: hoạt động trong các ngành dịch vụ cá nhân đòi hỏi sự chăm sóc trực tiếp như cắt tóc, phục vụ các thị trường ngách có nhu cầu khiêm tốn tại địa phương, hoặc đáp ứng mục tiêu sống của chủ doanh nghiệp muốn tự do, giảm áp lực và duy trì mối quan hệ gần gũi với khách hàng."
    },
    {
        "id": "card_why_fail_main",
        "title": "❌ Nguyên nhân Cốt lõi Dẫn đến Doanh nghiệp Thất bại",
        "selector": "#card-why-fail-main",
        "en": "Businesses fail primarily due to poor managerial competency, failure to adapt to changing market environments and technologies, acute liquidity shortages where cash runs out despite paper profits, and aggressive overtrading without sufficient long-term working capital.",
        "vi": "Doanh nghiệp thất bại chủ yếu do năng lực quản trị non kém, chậm thích ứng trước biến động của thị trường và công nghệ mới, khủng hoảng thanh khoản (dù trên sổ sách có lãi nhưng thực tế cạn kiệt tiền mặt trả nợ), và tăng trưởng nóng không kiểm soát khiến vốn lưu động bị thâm hụt nghiêm trọng."
    },
    {
        "id": "card_why_startups_fail",
        "title": "⚠️ Vì sao Doanh nghiệp Mới Khởi nghiệp có Nguy cơ Thất bại Cao hơn",
        "selector": "#card-why-startups-fail",
        "en": "Startups face heightened failure risks during their vulnerable early years due to lack of operational experience, unfamiliarity with consumer market dynamics, low initial sales volumes before establishing a brand reputation, and inadequate reserves of startup capital.",
        "vi": "Các doanh nghiệp mới khởi nghiệp đối mặt với rủi ro phá sản đặc biệt cao trong những năm đầu do thiếu kinh nghiệm thực chiến, chưa am hiểu tường tận biến động thị hiếu khách hàng, doanh số ban đầu còn thấp khi chưa tạo dựng được uy tín thương hiệu, và thiếu hụt nguồn vốn dự phòng vượt qua giai đoạn đầu."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_entrepreneurship": {"start": 1, "end": 2},
    "sec_business_plan": {"start": 3, "end": 5},
    "sec_gov_support": {"start": 6, "end": 8},
    "sec_measuring_size": {"start": 9, "end": 11},
    "sec_business_growth": {"start": 12, "end": 14},
    "sec_why_stay_small": {"start": 15, "end": 15},
    "sec_why_fail": {"start": 16, "end": 17}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.3 Enterprise, Business Growth and Size (Khởi sự, Tăng trưởng và Quy mô)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. ENTREPRENEURSHIP -->
    <div style="margin-bottom: 45px;">
        <div id="sec-entrepreneurship" class="lecture-interactive-card" data-lecture-section="sec_entrepreneurship" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💡 1. ENTREPRENEURSHIP</h2>
            <div style="background: #f5f3ff; border-left: 5px solid #7c3aed; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #4c1d95; line-height: 1.6;">
                An <b>entrepreneur</b> is a person who organizes, operates and takes risks for a new business venture. The entrepreneur brings together the various factors of production to produce goods or services.
            </div>
        </div>

        <div id="card-entrepreneur-traits" class="lecture-interactive-card" data-lecture-section="card_entrepreneur_traits" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h4 style="color: #6d28d9; font-size: 18px; margin: 0 0 12px 0;">🎯 8 Characteristics of Successful Entrepreneurs</h4>
            <p style="font-size: 14.5px; color: #475569; margin: 0 0 15px 0;">Check below to see whether you have what it takes to be a successful entrepreneur:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">🎯 Risk taker</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">🎨 Creative</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">✨ Optimistic</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">💪 Self-confident</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">🚀 Innovative</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">🦅 Independent</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">🗣️ Effective communicator</span>
                <span style="background: #ede9fe; color: #5b21b6; padding: 8px 15px; border-radius: 20px; font-size: 14px; font-weight: bold;">⚙️ Hard working</span>
            </div>
        </div>
    </div>

    <!-- 2. BUSINESS PLAN -->
    <div style="margin-bottom: 45px;">
        <div id="sec-business-plan" class="lecture-interactive-card" data-lecture-section="sec_business_plan" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📝 2. BUSINESS PLAN</h2>
            <div style="background: #eff6ff; border: 2px solid #bfdbfe; padding: 18px 20px; border-radius: 10px;">
                <p style="margin: 0 0 8px 0; font-size: 16px; color: #1e40af; font-weight: bold;">
                    A business plan is a document containing the business objectives and important details about the operations, finance and owners of the new business.
                </p>
                <p style="margin: 0; font-size: 14.5px; color: #2563eb; line-height: 1.6;">
                    It provides a complete description of the venture, target customers, market research, financial forecasts, and capital requirements to demonstrate commercial viability.
                </p>
            </div>
        </div>

        <div id="card-plan-contents" class="lecture-interactive-card" data-lecture-section="card_plan_contents" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 19px; margin-top: 0; margin-bottom: 14px;">📑 9 Key Contents of a Business Plan</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">Executive summary:</b> Key features of business and plan.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">The owner:</b> Background, qualifications and experience.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">The business:</b> Product details and production methods.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">The market:</b> Target customers and competitor analysis.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">Promotion:</b> Marketing methods and estimated costs.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">Premises &amp; Equipment:</b> Location and capital needs.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">Organisation:</b> Form of business legal structure.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">Costs &amp; Finance:</b> Pricing model and source of funds.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;"><b style="color: #2563eb;">Cash flow:</b> Forecast cash inflow and break-even.</div>
            </div>
        </div>

        <div id="card-plan-benefits" class="lecture-interactive-card" data-lecture-section="card_plan_benefits" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; padding: 20px 22px; border-radius: 12px; cursor: pointer; transition: all 0.2s;">
            <h4 style="margin: 0 0 10px 0; color: #15803d; font-size: 17px;">🌟 3 Key Benefits of a Business Plan</h4>
            <ul style="margin: 0; padding-left: 20px; line-height: 1.6; color: #166534; font-size: 14.5px;">
                <li><b>Strategic focus:</b> Reduces risk of losing sight of core mission and long-term vision.</li>
                <li><b>Team motivation:</b> Motivates managers and staff by setting clear operational targets.</li>
                <li><b>Securing finance:</b> Essential prerequisite to obtain bank loans or equity investments.</li>
            </ul>
        </div>
    </div>

    <!-- 3. GOVERNMENT SUPPORT FOR STARTUPS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-gov-support" class="lecture-interactive-card" data-lecture-section="sec_gov_support" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🤝 3. GOVERNMENT SUPPORT FOR STARTUPS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                A <b>startup</b> is an entrepreneurial venture in its early stages of development. Governments actively support startups to boost the national economy:
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-why-gov-help" class="lecture-interactive-card" data-lecture-section="card_why_gov_help" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #d97706; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #d97706; font-size: 18px; margin: 0 0 12px 0;">❓ Why do governments support startups?</h4>
                <ul style="margin: 0; padding-left: 20px; color: #92400e; font-size: 14.5px; line-height: 1.6;">
                    <li><b>Job creation:</b> Startups reduce national unemployment.</li>
                    <li><b>Economic growth:</b> Increase GDP output and competition.</li>
                    <li><b>Export revenue:</b> Successful firms export goods abroad.</li>
                    <li><b>Innovation:</b> Introduce fresh ideas and disruptive technologies.</li>
                </ul>
            </div>

            <div id="card-how-gov-support" class="lecture-interactive-card" data-lecture-section="card_how_gov_support" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #15803d; font-size: 18px; margin: 0 0 12px 0;">🛠️ How do governments support startups?</h4>
                <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 14.5px; line-height: 1.6;">
                    <li><b>Expert advice:</b> Free legal, accounting, and mentorship info.</li>
                    <li><b>Low cost premises:</b> Enterprise zones with subsidized rent.</li>
                    <li><b>Low interest loans:</b> Government-backed affordable credit.</li>
                    <li><b>Capital grants:</b> Non-repayable funds for equipment.</li>
                    <li><b>Training schemes:</b> Subsidized managerial workshops.</li>
                    <li><b>Tax holidays:</b> Temporary exemption from business taxes.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 4. MEASURING BUSINESS SIZE -->
    <div style="margin-bottom: 45px;">
        <div id="sec-measuring-size" class="lecture-interactive-card" data-lecture-section="sec_measuring_size" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📏 4. MEASURING BUSINESS SIZE</h2>
            <p style="font-size: 15px; color: #475569; margin: 0 0 18px 0; line-height: 1.6;">Cambridge accepts 4 standard criteria to compare business size:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 22px; margin-bottom: 4px;">👥</div>
                    <b style="color: #0f766e; font-size: 14.5px;">Number of Employees</b>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 22px; margin-bottom: 4px;">📦</div>
                    <b style="color: #0f766e; font-size: 14.5px;">Value of Output</b>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 22px; margin-bottom: 4px;">💰</div>
                    <b style="color: #0f766e; font-size: 14.5px;">Capital Employed</b>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 22px; margin-bottom: 4px;">💳</div>
                    <b style="color: #0f766e; font-size: 14.5px;">Sales Revenue</b>
                </div>
            </div>
        </div>

        <div id="card-profit-not-size" class="lecture-interactive-card" data-lecture-section="card_profit_not_size" style="background: #fff1f2; border: 1.5px solid #fecdd3; border-left: 5px solid #e11d48; padding: 20px 22px; border-radius: 12px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                <span style="font-size: 22px;">🚫</span>
                <b style="color: #be123c; font-size: 17px;">CRITICAL SYLLABUS NOTE: Profit is NOT a method of measuring business size!</b>
            </div>
            <ul style="margin: 0; padding-left: 20px; font-size: 14px; color: #9f1239; line-height: 1.6;">
                <li><b>Profit depends on margins, not scale:</b> A huge business with 30,000 employees can make a temporary loss, but it is still large.</li>
                <li><b>Small firms can make high profits:</b> A specialized medical clinic with 2 doctors can earn huge profits, but remains small.</li>
                <li><b>Profits fluctuate:</b> Influenced by tax and accounting rules, making it an unreliable size indicator.</li>
            </ul>
        </div>

        <div id="card-size-limitations" class="lecture-interactive-card" data-lecture-section="card_size_limitations" style="background: #fef2f2; border: 1.5px solid #fecaca; border-left: 5px solid #ef4444; padding: 18px 22px; border-radius: 12px; cursor: pointer; transition: all 0.2s;">
            <b style="color: #b91c1c; font-size: 16px;">⚠️ Limitations of Measuring Methods:</b>
            <p style="margin: 6px 0 0 0; font-size: 14px; color: #7f1d1d; line-height: 1.6;">
                A capital-intensive factory produces huge output with very few workers, making the 'employee' metric inaccurate. Similarly, comparing sales revenue fails between high-value jewellery and cheap bread.
            </p>
        </div>
    </div>

    <!-- 5. BUSINESS GROWTH -->
    <div style="margin-bottom: 45px;">
        <div id="sec-business-growth" class="lecture-interactive-card" data-lecture-section="sec_business_growth" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📈 5. BUSINESS GROWTH</h2>
            <p style="font-size: 15px; color: #475569; margin: 0 0 16px 0; line-height: 1.6;">Businesses expand to gain economies of scale, increase market share, and reduce average unit costs:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 18px;">
                    <h4 style="color: #0f172a; font-size: 17px; margin: 0 0 8px 0;">🌱 Internal (Organic) Growth</h4>
                    <p style="margin: 0; font-size: 14px; color: #475569; line-height: 1.5;">Expands existing operations (opening new branches, buying more machines) financed by retained profits.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 18px;">
                    <h4 style="color: #0f172a; font-size: 17px; margin: 0 0 8px 0;">🤝 External Growth (Integration)</h4>
                    <p style="margin: 0; font-size: 14px; color: #475569; line-height: 1.5;">Mergers (mutual agreement) or takeovers (buying out majority shares) with other operating businesses.</p>
                </div>
            </div>
        </div>

        <div id="card-external-growth-types" class="lecture-interactive-card" data-lecture-section="card_external_growth_types" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; overflow: hidden; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <div style="padding: 16px 20px; background: #f8fafc; border-bottom: 1px solid #e2e8f0; font-weight: bold; font-size: 17px; color: #0f172a;">🔗 4 Types of External Integration</div>
            <div style="padding: 18px 20px; border-bottom: 1px solid #e2e8f0;">
                <b style="color: #2563eb; font-size: 15.5px;">1. Horizontal Integration:</b> Same industry at the <b>same stage of production</b> (e.g. bank + bank). <span style="color: #16a34a; font-size: 13.5px;">➔ Benefits: Eliminates competitors, economies of scale.</span>
            </div>
            <div style="padding: 18px 20px; border-bottom: 1px solid #e2e8f0; background: #fafafa;">
                <b style="color: #059669; font-size: 15.5px;">2. Backward Vertical Integration:</b> Same industry but at a stage <b>BEHIND</b> (e.g. bakery + wheat flour farm). <span style="color: #16a34a; font-size: 13.5px;">➔ Benefits: Secures supply, absorbs supplier margin.</span>
            </div>
            <div style="padding: 18px 20px; border-bottom: 1px solid #e2e8f0;">
                <b style="color: #059669; font-size: 15.5px;">3. Forward Vertical Integration:</b> Same industry but at a stage <b>AHEAD</b> (e.g. car maker + car dealership). <span style="color: #16a34a; font-size: 13.5px;">➔ Benefits: Assured retail outlet, controls selling prices.</span>
            </div>
            <div style="padding: 18px 20px; background: #fafafa;">
                <b style="color: #9333ea; font-size: 15.5px;">4. Conglomerate Integration:</b> Firms in a <b>completely different industry</b> (e.g. hotel + clothing brand). <span style="color: #16a34a; font-size: 13.5px;">➔ Benefits: Diversifies and spreads risk across markets.</span>
            </div>
        </div>

        <div id="card-growth-problems-overcome" class="lecture-interactive-card" data-lecture-section="card_growth_problems_overcome" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; padding: 22px; border-radius: 12px; cursor: pointer; transition: all 0.2s;">
            <h4 style="margin: 0 0 12px 0; color: #15803d; font-size: 18px;">🛡️ Growth Drawbacks &amp; Management Solutions</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px;">
                <div style="background: #ffffff; padding: 12px 16px; border-radius: 8px; border: 1px solid #dcfce7; font-size: 13.5px;">
                    <b style="color: #166534;">Decentralisation:</b> Solves coordination issues by delegating power to regional branch managers.
                </div>
                <div style="background: #ffffff; padding: 12px 16px; border-radius: 8px; border: 1px solid #dcfce7; font-size: 13.5px;">
                    <b style="color: #166534;">Controlled Expansion:</b> Solves cash shortages by financing growth with retained earnings.
                </div>
                <div style="background: #ffffff; padding: 12px 16px; border-radius: 8px; border: 1px solid #dcfce7; font-size: 13.5px;">
                    <b style="color: #166534;">Modern IT Systems:</b> Solves communication bottlenecks through unified digital networks.
                </div>
                <div style="background: #ffffff; padding: 12px 16px; border-radius: 8px; border: 1px solid #dcfce7; font-size: 13.5px;">
                    <b style="color: #166534;">Change Management:</b> Solves post-merger cultural clash through open communication.
                </div>
            </div>
        </div>
    </div>

    <!-- 6. WHY BUSINESSES STAY SMALL -->
    <div id="sec-why-stay-small" class="lecture-interactive-card" data-lecture-section="sec_why_stay_small" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #64748b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏠 6. WHY BUSINESSES STAY SMALL</h2>
        <p style="font-size: 15px; color: #475569; margin: 0 0 16px 0; line-height: 1.6;">Not all businesses grow. Many deliberately choose to operate on a small scale:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 14px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px;">
                <h4 style="color: #334155; margin: 0 0 6px 0; font-size: 16px;">💇‍♀️ Industry Type</h4>
                <p style="margin: 0; font-size: 14px; color: #475569;">Personalized services (hairdressers, tailors) cannot easily scale up.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px;">
                <h4 style="color: #334155; margin: 0 0 6px 0; font-size: 16px;">🗺️ Market Size</h4>
                <p style="margin: 0; font-size: 14px; color: #475569;">Niche or rural markets have small total demand, restricting expansion.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px;">
                <h4 style="color: #334155; margin: 0 0 6px 0; font-size: 16px;">🎯 Owners' Objectives</h4>
                <p style="margin: 0; font-size: 14px; color: #475569;">Owners value work-life balance, direct control, and low stress.</p>
            </div>
        </div>
    </div>

    <!-- 7. WHY BUSINESSES FAIL -->
    <div style="margin-bottom: 45px;">
        <div style="margin-bottom: 18px;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💥 7. WHY BUSINESSES FAIL</h2>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-why-fail-main" class="lecture-interactive-card" data-lecture-section="card_why_fail_main" style="background: #ffffff; border: 1.5px solid #fecaca; border-left: 5px solid #dc2626; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #dc2626; font-size: 18px; margin: 0 0 12px 0;">❌ 4 Main Causes of Business Failure</h4>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 14px; line-height: 1.6;">
                    <li><b>Poor management skills:</b> Incompetence in cash management, pricing, and marketing.</li>
                    <li><b>Failure to adapt:</b> Inability to keep up with new technology or customer trends.</li>
                    <li><b>Liquidity crisis:</b> Running out of cash to pay daily bills despite book profits.</li>
                    <li><b>Over-expansion (Overtrading):</b> Growing too quickly without adequate working capital.</li>
                </ul>
            </div>

            <div id="card-why-startups-fail" class="lecture-interactive-card" data-lecture-section="card_why_startups_fail" style="background: #fff5f5; border: 1.5px solid #fecaca; border-left: 5px solid #b91c1c; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #b91c1c; font-size: 18px; margin: 0 0 12px 0;">⚠️ Why Startups Face Greater Risk</h4>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 14px; line-height: 1.6;">
                    <li><b>Lack of experience:</b> Inexperienced founders struggle against veteran rivals.</li>
                    <li><b>New brand:</b> Low initial sales before customer loyalty is formed.</li>
                    <li><b>Low reserves:</b> Any initial disruption drains scarce reserve capital.</li>
                </ul>
            </div>
        </div>
    </div>

</div>"""
    return html

# ==============================================================================
# 3. GENERATE NEW HTML FOR PAGE 2 (BILINGUAL)
# ==============================================================================
def build_page_2_html(original_p2):
    pattern = r'<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">[\s\S]*?</div>'
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.3 Enterprise, Business Growth and Size (Khởi sự, Tăng trưởng và Quy mô)</h1>
        </div>
    </div>"""
    new_p2 = re.sub(pattern, header_banner, original_p2, count=1)
    
    # Fix the unclosed div in page 2 if present
    o = len(re.findall(r'<div\b', new_p2))
    c = len(re.findall(r'</div>', new_p2))
    if o > c:
        new_p2 = new_p2.strip() + ("\n</div>" * (o - c))
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 1.3 Audio and HTML ===")
    
    # 0. Clean stale audio files so that all 18 segments match perfectly
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)
    valid_ids = {s['id'] for s in segments}
    for fname in os.listdir(audio_dir):
        if fname.endswith('.mp3'):
            base_id = fname[:-4]
            if base_id not in valid_ids or base_id in {'sec_entrepreneurship', 'sec_business_plan', 'sec_gov_support', 'sec_measuring_size', 'sec_business_growth', 'sec_why_fail'}:
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
    with open('scripts/bs_1_3_page_2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 1.3 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
