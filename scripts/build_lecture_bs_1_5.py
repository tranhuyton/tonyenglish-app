import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ========================================================
# LECTURE 1.5: Business objectives and stakeholder objectives
# ========================================================
async def build_1_5():
    lid = 'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3'
    code = '1_5'
    title = '1.5. Business objectives and stakeholder objectives'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    t_h2_1 = '<h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🎯 1. BUSINESS OBJECTIVES</h2>'
    r_h2_1 = '<h2 id="sec-business-objectives" class="lecture-interactive-card" data-lecture-section="sec_business_objectives" style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🎯 1. BUSINESS OBJECTIVES</h2>'
    
    t_h3_2 = '<h3 style="color: #0f172a; font-size: 20px; margin-bottom: 15px;">🏢 Private Sector Objectives</h3>'
    r_h3_2 = '<h3 id="card-private-objectives" class="lecture-interactive-card" data-lecture-section="card_private_objectives" style="color: #0f172a; font-size: 20px; margin-bottom: 15px; cursor: pointer;">🏢 Private Sector Objectives</h3>'
    
    t_h2_2 = '<h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏛️ 2. PUBLIC-SECTOR BUSINESS OBJECTIVES</h2>'
    r_h2_2 = '<h2 id="sec-public-objectives" class="lecture-interactive-card" data-lecture-section="sec_public_objectives" style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🏛️ 2. PUBLIC-SECTOR BUSINESS OBJECTIVES</h2>'
    
    t_h2_3 = '<h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">👥 3. STAKEHOLDERS</h2>'
    r_h2_3 = '<h2 id="sec-stakeholders" class="lecture-interactive-card" data-lecture-section="sec_stakeholders" style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">👥 3. STAKEHOLDERS</h2>'
    
    t_h3_3 = '<h3 style="color: #0f172a; font-size: 20px; margin-bottom: 15px; padding-bottom: 5px; border-bottom: 2px dashed #cbd5e1;">🏢 Internal Stakeholders (Work for or own the business)</h3>'
    r_h3_3 = '<h3 id="card-stakeholder-groups" class="lecture-interactive-card" data-lecture-section="card_stakeholder_groups" style="color: #0f172a; font-size: 20px; margin-bottom: 15px; padding-bottom: 5px; border-bottom: 2px dashed #cbd5e1; cursor: pointer;">🏢 Internal Stakeholders (Work for or own the business)</h3>'
    
    t_h2_4 = '<h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">⚔️ 4. CONFLICTS OF STAKEHOLDERS\' OBJECTIVES</h2>'
    r_h2_4 = '<h2 id="sec-stakeholder-conflicts" class="lecture-interactive-card" data-lecture-section="sec_stakeholder_conflicts" style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">⚔️ 4. CONFLICTS OF STAKEHOLDERS\' OBJECTIVES</h2>'

    new_html = html.replace(t_header, r_header, 1).replace(t_h2_1, r_h2_1, 1).replace(t_h3_2, r_h3_2, 1).replace(t_h2_2, r_h2_2, 1).replace(t_h2_3, r_h2_3, 1).replace(t_h3_3, r_h3_3, 1).replace(t_h2_4, r_h2_4, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1.5: Mục tiêu doanh nghiệp và các bên liên quan",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.5: Business Objectives and Stakeholder Objectives. In this concluding lesson of Unit 1, we analyse why enterprises formulate strategic aims, contrast private profit targets with public service mandates, identify internal and external stakeholders, and resolve the inevitable conflicts between differing stakeholder priorities.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.5: Mục tiêu doanh nghiệp và Mục tiêu của các bên liên quan. Trong bài học kết thúc Chủ đề một này, chúng ta sẽ phân tích lý do doanh nghiệp thiết lập mục tiêu chiến lược, so sánh mục tiêu lợi nhuận của khu vực tư nhân với mục tiêu dịch vụ công, nhận diện các bên liên quan nội bộ và bên ngoài, cùng các giải pháp xử lý xung đột quyền lợi."
        },
        {
            "id": "sec_business_objectives",
            "title": "1. Mục tiêu kinh doanh và Lợi ích",
            "selector": "#sec-business-objectives",
            "en": "Section 1 defines business objectives as measurable targets that direct corporate activities. Setting clear objectives provides strategic focus, unites managers and employees toward common goals, motivates the workforce through clear milestones, guides critical decision-making, and establishes quantifiable benchmarks to evaluate overall business performance.",
            "vi": "Mục một định nghĩa mục tiêu kinh doanh là các đích đến đo lường được để định hướng toàn bộ hoạt động của doanh nghiệp. Việc xác lập mục tiêu rõ ràng giúp vạch ra định hướng chiến lược, gắn kết ban quản trị và nhân viên, tạo động lực phấn đấu, hỗ trợ ra quyết định kinh doanh chính xác và cung cấp tiêu chuẩn định lượng để đánh giá hiệu quả hoạt động."
        },
        {
            "id": "card_private_objectives",
            "title": "Các mục tiêu trọng tâm của Khu vực Tư nhân",
            "selector": "#card-private-objectives",
            "en": "In the private sector, commercial objectives vary by enterprise lifecycle. Business survival is paramount for newly launched ventures and during economic recessions. Profitability satisfies owner returns and finances reinvestment. Growth and market share expansion achieve economies of scale and market dominance. Returns to shareholders maintain investor confidence, and corporate social responsibility builds sustainable brand equity.",
            "vi": "Trong khu vực tư nhân, các mục tiêu kinh doanh thay đổi theo từng giai đoạn phát triển. Mục tiêu sinh tồn (survival) là tối quan trọng đối với doanh nghiệp mới khởi nghiệp hoặc trong khủng hoảng kinh tế. Lợi nhuận (profit) bảo đảm quyền lợi cho chủ sở hữu và tái đầu tư. Tăng trưởng và thị phần (growth & market share) mang lại lợi thế kinh tế theo quy mô. Lợi tức cho cổ đông duy trì niềm tin của nhà đầu tư, trong khi trách nhiệm xã hội củng cố uy tín thương hiệu lâu dài."
        },
        {
            "id": "sec_public_objectives",
            "title": "2. Mục tiêu của Doanh nghiệp Nhà nước",
            "selector": "#sec-public-objectives",
            "en": "Section 2 contrasts private motives with public-sector objectives. State-owned enterprises do not prioritize profit maximization; instead, they deliver affordable essential public services like utilities, healthcare, and education, safeguard local employment, and stimulate balanced regional economic development to ensure universal public access and reduce social inequalities.",
            "vi": "Mục hai đối chiếu động cơ tư nhân với các mục tiêu của khu vực nhà nước. Các tổ chức công không đặt tối đa hóa lợi nhuận lên hàng đầu; thay vào đó, họ tập trung cung cấp các dịch vụ công thiết yếu với giá cả phải chăng như điện nước, y tế, giáo dục, bảo vệ việc làm cho người dân địa phương và thúc đẩy phát triển kinh tế vùng nhằm bảo đảm công bằng xã hội."
        },
        {
            "id": "sec_stakeholders",
            "title": "3. Các bên liên quan (Stakeholders)",
            "selector": "#sec-stakeholders",
            "en": "Section 3 investigates stakeholders: any individual or group with a direct interest in the operations and performance of a business. Stakeholders are divided into internal stakeholders, such as owners, managers, and workers, and external stakeholders, including customers, suppliers, commercial lenders, local communities, and national governments.",
            "vi": "Mục ba nghiên cứu về các bên liên quan (stakeholders): bất kỳ cá nhân hay nhóm người nào có quyền lợi hoặc chịu tác động trực tiếp từ hoạt động của doanh nghiệp. Các bên liên quan được chia thành nhóm nội bộ (chủ sở hữu, nhà quản lý, người lao động) và nhóm bên ngoài (khách hàng, nhà cung ứng, ngân hàng, cộng đồng địa phương và chính phủ)."
        },
        {
            "id": "card_stakeholder_groups",
            "title": "Quyền lợi và Động cơ của từng nhóm Stakeholders",
            "selector": "#card-stakeholder-groups",
            "en": "Each stakeholder group has distinct motivations. Owners seek high dividends and capital appreciation; managers desire career progression, prestige, and executive bonuses; workers seek job security, safe working environments, and fair wages. Externally, customers demand quality at competitive prices, suppliers demand timely settlement, and governments enforce tax compliance and employment regulations.",
            "vi": "Mỗi nhóm bên liên quan đều mang những kỳ vọng riêng biệt. Chủ sở hữu và cổ đông kỳ vọng cổ tức cao và tăng giá trị vốn; nhà quản lý mong muốn thăng tiến sự nghiệp và thưởng hiệu quả; người lao động cần sự an toàn việc làm, môi trường làm việc tốt và mức lương thỏa đáng. Bên ngoài, khách hàng đòi hỏi sản phẩm chất lượng với giá hợp lý, nhà cung cấp yêu cầu thanh toán đúng hạn, còn chính phủ kiểm soát tuân thủ thuế và luật lao động."
        },
        {
            "id": "sec_stakeholder_conflicts",
            "title": "4. Xung đột mục tiêu giữa các bên liên quan",
            "selector": "#sec-stakeholder-conflicts",
            "en": "Section 4 addresses stakeholder conflicts. Because different stakeholders pursue competing aims, business decisions invariably require compromises. For example, paying higher wages pleases workers but diminishes shareholder profits; automating factory lines cuts costs and boosts efficiency for owners but threatens shopfloor job security. Senior leadership must carefully balance conflicting expectations to achieve long-term commercial harmony.",
            "vi": "Mục bốn giải quyết bài toán xung đột mục tiêu. Do các nhóm theo đuổi những lợi ích trái ngược, mọi quyết định quản trị đều phải dung hòa. Ví dụ: tăng lương sẽ làm hài lòng người lao động nhưng làm giảm lợi nhuận của cổ đông; đầu tư dây chuyền tự động hóa giúp giảm chi phí và nâng cao hiệu suất nhưng lại đe dọa việc làm của công nhân. Ban điều hành phải cân bằng khéo léo các kỳ vọng để bảo đảm sự phát triển bền vững."
        }
    ]
    
    major_sections = [
        {"id": "sec_business_objectives", "title": "1. Mục tiêu kinh doanh"},
        {"id": "sec_public_objectives", "title": "2. Mục tiêu khu vực nhà nước"},
        {"id": "sec_stakeholders", "title": "3. Các bên liên quan (Stakeholders)"},
        {"id": "sec_stakeholder_conflicts", "title": "4. Xung đột mục tiêu"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 1.5 successfully built!")

if __name__ == "__main__":
    asyncio.run(build_1_5())
