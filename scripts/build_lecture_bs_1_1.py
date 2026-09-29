import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

LECTURE_CODE = "1_1"
LECTURE_ID = "6049f916-3af9-428a-bcd0-ce0574f1d7f7"
COURSE_TITLE = "Cambridge IGCSE Business Studies"
LECTURE_TITLE = "1.1 Business activity"

async def main():
    # 1. Fetch current HTML
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    # 2. Tag HTML elements
    # Header card
    target_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    repl_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    # H2 sections
    target_h2_1 = '<h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">👋 1. INTRODUCTION TO BUSINESS</h2>'
    repl_h2_1 = '<h2 id="sec-intro-business" class="lecture-interactive-card" data-lecture-section="sec_intro_business" style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">👋 1. INTRODUCTION TO BUSINESS</h2>'
    
    target_h2_2 = '<h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">⚖️ 2. THE ECONOMIC PROBLEM</h2>'
    repl_h2_2 = '<h2 id="sec-economic-problem" class="lecture-interactive-card" data-lecture-section="sec_economic_problem" style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">⚖️ 2. THE ECONOMIC PROBLEM</h2>'
    
    target_h2_3 = '<h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🔄 3. OPPORTUNITY COST</h2>'
    repl_h2_3 = '<h2 id="sec-opportunity-cost" class="lecture-interactive-card" data-lecture-section="sec_opportunity_cost" style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🔄 3. OPPORTUNITY COST</h2>'
    
    target_h2_4 = '<h2 style="color: #0f172a; border-bottom: 3px solid #a855f7; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏭 4. FACTORS OF PRODUCTION</h2>'
    repl_h2_4 = '<h2 id="sec-factors-of-production" class="lecture-interactive-card" data-lecture-section="sec_factors_of_production" style="color: #0f172a; border-bottom: 3px solid #a855f7; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🏭 4. FACTORS OF PRODUCTION</h2>'
    
    target_fop = '<div style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px;">'
    repl_fop = '<div id="card-fop-map" class="lecture-interactive-card" data-lecture-section="fop_interactive_map" style="background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); margin-bottom: 40px; cursor: pointer;">'
    
    target_h2_5 = '<h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🎯 5. IMPORTANCE OF SPECIALISATION</h2>'
    repl_h2_5 = '<h2 id="sec-specialisation" class="lecture-interactive-card" data-lecture-section="sec_specialisation" style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🎯 5. IMPORTANCE OF SPECIALISATION</h2>'
    
    target_h2_6 = '<h2 style="color: #0f172a; border-bottom: 3px solid #6366f1; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🚀 6. PURPOSE OF BUSINESS ACTIVITY</h2>'
    repl_h2_6 = '<h2 id="sec-purpose-business" class="lecture-interactive-card" data-lecture-section="sec_purpose_business" style="color: #0f172a; border-bottom: 3px solid #6366f1; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🚀 6. PURPOSE OF BUSINESS ACTIVITY</h2>'
    
    target_h2_7 = '<h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">✨ 7. ADDED VALUE</h2>'
    repl_h2_7 = '<h2 id="sec-added-value" class="lecture-interactive-card" data-lecture-section="sec_added_value" style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">✨ 7. ADDED VALUE</h2>'
    
    target_h3_av = '<h3 style="color: #0f172a; font-size: 20px; margin-bottom: 15px;">📈 How can a business increase added value?</h3>'
    repl_h3_av = '<h3 id="card-increase-added-value" class="lecture-interactive-card" data-lecture-section="card_increase_added_value" style="color: #0f172a; font-size: 20px; margin-bottom: 15px; cursor: pointer;">📈 How can a business increase added value?</h3>'

    for name, target in [
        ('header', target_header), ('h2_1', target_h2_1), ('h2_2', target_h2_2),
        ('h2_3', target_h2_3), ('h2_4', target_h2_4), ('fop', target_fop),
        ('h2_5', target_h2_5), ('h2_6', target_h2_6), ('h2_7', target_h2_7),
        ('h3_av', target_h3_av)
    ]:
        if target not in html:
            print(f"[ERROR] Target {name} not found in HTML!")
            return

    new_html = html.replace(target_header, repl_header, 1)
    new_html = new_html.replace(target_h2_1, repl_h2_1, 1)
    new_html = new_html.replace(target_h2_2, repl_h2_2, 1)
    new_html = new_html.replace(target_h2_3, repl_h2_3, 1)
    new_html = new_html.replace(target_h2_4, repl_h2_4, 1)
    new_html = new_html.replace(target_fop, repl_fop, 1)
    new_html = new_html.replace(target_h2_5, repl_h2_5, 1)
    new_html = new_html.replace(target_h2_6, repl_h2_6, 1)
    new_html = new_html.replace(target_h2_7, repl_h2_7, 1)
    new_html = new_html.replace(target_h3_av, repl_h3_av, 1)
    
    # Check div balance
    open_divs = len(new_html.split('<div')) - 1
    close_divs = len(new_html.split('</div>')) - 1
    diff = open_divs - close_divs
    print(f"HTML Div Balance: open={open_divs}, close={close_divs}, diff={diff}")
    if diff != 0:
        print("[ERROR] Div balance mismatch!")
        return

    # 3. Segments definition
    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1.1: Hoạt động Kinh doanh",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.1: Business Activity. In this opening lesson, we establish the foundations of business: how enterprises organise scarce resources to satisfy unlimited consumer demands, the nature of scarcity and opportunity cost, the four factors of production, the importance of specialisation, and how businesses generate added value.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.1: Hoạt động Kinh doanh. Trong bài học nền tảng này, chúng ta sẽ tìm hiểu mục đích cốt lõi của doanh nghiệp: cách thức tổ chức các nguồn lực khan hiếm để thỏa mãn nhu cầu vô hạn của con người, bản chất của sự khan hiếm và chi phí cơ hội, bốn yếu tố sản xuất, vai trò của chuyên môn hóa và cách thức doanh nghiệp tạo ra giá trị gia tăng."
        },
        {
            "id": "sec_intro_business",
            "title": "1. Giới thiệu về Doanh nghiệp",
            "selector": "#sec-intro-business",
            "en": "Section 1 defines business studies. We are surrounded by commercial enterprises that provide goods and services essential to modern life. Academically, business studies examines the economics and management of how enterprises organize physical, human, and financial resources to produce goods and services that satisfy consumer demands in competitive markets.",
            "vi": "Mục một định nghĩa về hoạt động kinh doanh. Chúng ta được bao quanh bởi vô số các tổ chức thương mại cung ứng hàng hóa và dịch vụ thiết yếu cho cuộc sống. Dưới góc độ học thuật, môn Nghiên cứu Kinh doanh khảo sát các nguyên lý kinh tế và quản trị trong việc điều phối các nguồn lực vật chất, nhân sự và tài chính nhằm thỏa mãn tối ưu nhu cầu của khách hàng trên thị trường."
        },
        {
            "id": "sec_economic_problem",
            "title": "2. Vấn đề kinh tế: Nhu cầu, Mong muốn & Sự khan hiếm",
            "selector": "#sec-economic-problem",
            "en": "Section 2 investigates the foundational economic problem. Human beings have basic needs required for survival, such as water, nutritious food, clothing, and shelter. Beyond survival, humans have unlimited wants—desires for luxury cars, holidays, and fashion. However, economic resources are strictly finite. This imbalance creates scarcity—the fundamental economic problem where unlimited wants collide with limited resources.",
            "vi": "Mục hai phân tích vấn đề kinh tế căn bản. Con người có những nhu cầu thiết yếu để sinh tồn như nước, lương thực, trang phục và nhà ở. Bên cạnh đó, con người có mong muốn vô hạn đối với các sản phẩm cao cấp, du lịch và giải trí. Tuy nhiên, các nguồn lực kinh tế luôn có hạn. Sự mất cân đối này dẫn đến sự khan hiếm – bài toán kinh tế cốt lõi khi mong muốn vô hạn va chạm với nguồn lực hữu hạn."
        },
        {
            "id": "sec_opportunity_cost",
            "title": "3. Chi phí cơ hội (Opportunity Cost)",
            "selector": "#sec-opportunity-cost",
            "en": "Section 3 explains opportunity cost. Because resources are scarce, economic agents must make choices. Every choice involves a sacrifice. Opportunity cost is defined as the benefit of the next best alternative given up by deciding to allocate resources elsewhere. For instance, if a business invests its limited capital into buying automated factory robots, the opportunity cost is the marketing campaign that cannot now be funded.",
            "vi": "Mục ba giải thích về chi phí cơ hội. Vì nguồn lực khan hiếm, các chủ thể kinh tế buộc phải đưa ra sự lựa chọn, và mỗi lựa chọn đều phải đánh đổi. Chi phí cơ hội được định nghĩa là giá trị hoặc lợi ích của phương án tốt nhất tiếp theo bị bỏ qua khi quyết định phân bổ nguồn lực. Ví dụ, nếu doanh nghiệp dành toàn bộ vốn để mua robot tự động hóa, chi phí cơ hội chính là chiến dịch tiếp thị mà họ phải từ bỏ."
        },
        {
            "id": "sec_factors_of_production",
            "title": "4. Bốn yếu tố sản xuất (Factors of Production)",
            "selector": "#sec-factors-of-production",
            "en": "Section 4 classifies the four factors of production required to produce any good or service. Land encompasses all natural renewable and non-renewable resources, earning rent. Labour represents the human physical and mental effort, earning wages or salaries. Capital comprises man-made assets like machinery, factories, and technology, earning interest. Enterprise is the skill and risk-taking ability of the entrepreneur who organizes the other three factors, earning profit.",
            "vi": "Mục bốn phân loại bốn yếu tố sản xuất thiết yếu để tạo ra mọi sản phẩm. Đất đai bao gồm toàn bộ tài nguyên thiên nhiên, mang lại phần thưởng là địa tô. Lao động là sức lực thể chất và trí tuệ của con người, nhận phần thưởng là tiền lương. Vốn là tư liệu sản xuất do con người tạo ra như máy móc, nhà xưởng và công nghệ, sinh ra lãi suất. Và Tinh thần doanh nhân là năng lực chấp nhận rủi ro và điều phối ba yếu tố trên, mang lại lợi nhuận."
        },
        {
            "id": "fop_interactive_map",
            "title": "Sơ đồ tương tác 4 Yếu tố sản xuất (F.O.P Map)",
            "selector": "#card-fop-map",
            "en": "This interactive diagram maps the economic interplay between the four factors of production. Notice that without an entrepreneur to take financial risks and orchestrate operations, land, labour, and capital remain inert. The entrepreneur brings innovation, establishes production systems, and shoulders the ultimate legal and commercial liabilities of the firm in exchange for residual profits.",
            "vi": "Sơ đồ tương tác này minh họa mối liên kết chặt chẽ giữa bốn yếu tố sản xuất. Hãy chú ý rằng nếu thiếu doanh nhân dám chấp nhận rủi ro tài chính và điều phối hoạt động, đất đai, lao động và vốn sẽ ở trạng thái tĩnh. Doanh nhân chính là nhân tố mang lại sự đổi mới sáng tạo, thiết lập quy trình sản xuất và gánh vác trách nhiệm pháp lý thương mại để đổi lấy phần lợi nhuận thặng dư."
        },
        {
            "id": "sec_specialisation",
            "title": "5. Tầm quan trọng của Chuyên môn hóa & Phân công lao động",
            "selector": "#sec-specialisation",
            "en": "Section 5 examines specialisation and the division of labour. Specialisation occurs when individuals, businesses, or entire nations concentrate on tasks where they have distinct advantages. Division of labour splits complex production into discrete repetitive steps. This dramatically accelerates worker speed, enhances quality, and reduces training costs, though extreme monotony can cause worker alienation, absenteeism, and production bottlenecks.",
            "vi": "Mục năm tìm hiểu về chuyên môn hóa và phân công lao động. Chuyên môn hóa diễn ra khi cá nhân, doanh nghiệp hoặc quốc gia tập trung vào lĩnh vực mà họ có lợi thế rõ rệt. Phân công lao động chia nhỏ quy trình sản xuất thành các công đoạn lặp lại đơn giản. Điều này giúp tăng vọt năng suất, cải thiện chất lượng và giảm chi phí đào tạo, dù sự đơn điệu quá mức có thể gây ra nhàm chán, nghỉ việc và tắc nghẽn dây chuyền."
        },
        {
            "id": "sec_purpose_business",
            "title": "6. Mục đích của Hoạt động Doanh nghiệp",
            "selector": "#sec-purpose-business",
            "en": "Section 6 highlights the primary purpose of business activity: combining scarce factors of production to produce marketable goods and services that satisfy consumer needs and wants. Businesses employ workers, distribute wages that support livelihoods, invent technological solutions, and generate wealth for both local communities and the broader national macroeconomy.",
            "vi": "Mục sáu nhấn mạnh mục đích cốt lõi của hoạt động kinh doanh: kết hợp các yếu tố sản xuất khan hiếm để tạo ra hàng hóa và dịch vụ thương mại nhằm đáp ứng tối đa nhu cầu của người tiêu dùng. Thông qua đó, doanh nghiệp tạo việc làm, chi trả tiền lương đảm bảo sinh kế cho người lao động, sáng tạo giải pháp công nghệ và đóng góp vào sự phồn vinh của nền kinh tế quốc gia."
        },
        {
            "id": "sec_added_value",
            "title": "7. Giá trị gia tăng (Added Value)",
            "selector": "#sec-added-value",
            "en": "Section 7 introduces one of the most critical concepts in IGCSE Business: Added Value. Added value is the difference between the selling price of a finished product and the cost of bought-in raw materials and components used to make it. It is calculated as Selling Price minus Cost of Materials. Importantly, added value is not the same as profit, because it does not yet deduct operational expenses like wages, rent, and utility bills.",
            "vi": "Mục bảy trình bày một trong những khái niệm trọng tâm nhất của đề thi IGCSE: Giá trị gia tăng. Giá trị gia tăng là phần chênh lệch giữa giá bán của thành phẩm và chi phí mua nguyên vật liệu cấu thành. Công thức tính là: Giá bán trừ đi Chi phí nguyên vật liệu đầu vào. Cần đặc biệt ghi nhớ: Giá trị gia tăng không đồng nhất với lợi nhuận, vì nó chưa trừ đi các chi phí vận hành khác như tiền lương, tiền thuê mặt bằng và chi phí điện nước."
        },
        {
            "id": "card_increase_added_value",
            "title": "Các phương pháp gia tăng giá trị cho doanh nghiệp",
            "selector": "#card-increase-added-value",
            "en": "Businesses can increase added value via four primary levers: establishing prestigious branding that commands premium prices, elevating product quality and finishing standards, incorporating unique innovative features and design aesthetics, or delivering exceptional personalised customer service. Higher added value shields firms from intense price competition and expands their operating gross profit margins.",
            "vi": "Doanh nghiệp có thể gia tăng giá trị thông qua bốn đòn bẩy chiến lược chính: xây dựng thương hiệu uy tín để định giá bán cao hơn, nâng cao tiêu chuẩn chất lượng và độ hoàn thiện của sản phẩm, tích hợp các tính năng thiết kế độc đáo và sáng tạo, hoặc cung cấp dịch vụ chăm sóc khách hàng xuất sắc. Giá trị gia tăng cao giúp doanh nghiệp thoát khỏi áp lực cạnh tranh gay gắt về giá và nới rộng biên lợi nhuận hoạt động."
        }
    ]
    
    major_sections = [
        {"id": "sec_intro_business", "title": "1. Giới thiệu về Doanh nghiệp"},
        {"id": "sec_economic_problem", "title": "2. Vấn đề kinh tế: Nhu cầu, Mong muốn & Sự khan hiếm"},
        {"id": "sec_opportunity_cost", "title": "3. Chi phí cơ hội (Opportunity Cost)"},
        {"id": "sec_factors_of_production", "title": "4. Bốn yếu tố sản xuất (Factors of Production)"},
        {"id": "sec_specialisation", "title": "5. Tầm quan trọng của Chuyên môn hóa"},
        {"id": "sec_purpose_business", "title": "6. Mục đích của Hoạt động Doanh nghiệp"},
        {"id": "sec_added_value", "title": "7. Giá trị gia tăng (Added Value)"}
    ]
    
    # 4. Process audio and write manifest
    await process_lecture_audio(
        lecture_code=LECTURE_CODE,
        lecture_id=LECTURE_ID,
        course_title=COURSE_TITLE,
        lecture_title=LECTURE_TITLE,
        segments=segments,
        major_sections=major_sections,
        subject='business'
    )
    
    # 5. Update Supabase DB
    update_supabase_page(LECTURE_ID, new_html)
    print("✅ Lecture 1.1 successfully built and updated!")

if __name__ == "__main__":
    asyncio.run(main())
