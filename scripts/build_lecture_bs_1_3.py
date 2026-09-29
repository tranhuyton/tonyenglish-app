import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ========================================================
# LECTURE 1.3: Enterprise, business growth and size
# ========================================================
async def build_1_3():
    lid = 'a8ebc541-78ef-4202-96ad-161ed647a1b1'
    code = '1_3'
    title = '1.3. Enterprise, business growth and size'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    t_h2_1 = '<h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">💡 1. ENTREPRENEURSHIP</h2>'
    r_h2_1 = '<h2 id="sec-entrepreneurship" class="lecture-interactive-card" data-lecture-section="sec_entrepreneurship" style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">💡 1. ENTREPRENEURSHIP</h2>'
    
    t_h2_2 = '<h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">📝 2. BUSINESS PLAN</h2>'
    r_h2_2 = '<h2 id="sec-business-plan" class="lecture-interactive-card" data-lecture-section="sec_business_plan" style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">📝 2. BUSINESS PLAN</h2>'
    
    t_h2_3 = '<h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🤝 3. GOVERNMENT SUPPORT FOR STARTUPS</h2>'
    r_h2_3 = '<h2 id="sec-gov-support" class="lecture-interactive-card" data-lecture-section="sec_gov_support" style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🤝 3. GOVERNMENT SUPPORT FOR STARTUPS</h2>'
    
    t_h2_4 = '<h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">📏 4. MEASURING BUSINESS SIZE</h2>'
    r_h2_4 = '<h2 id="sec-measuring-size" class="lecture-interactive-card" data-lecture-section="sec_measuring_size" style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">📏 4. MEASURING BUSINESS SIZE</h2>'
    
    t_h2_5 = '<h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">📈 5. BUSINESS GROWTH</h2>'
    r_h2_5 = '<h2 id="sec-business-growth" class="lecture-interactive-card" data-lecture-section="sec_business_growth" style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">📈 5. BUSINESS GROWTH</h2>'
    
    t_h2_6 = '<h2 style="color: #0f172a; border-bottom: 3px solid #64748b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏠 6. WHY BUSINESSES STAY SMALL</h2>'
    r_h2_6 = '<h2 id="sec-why-stay-small" class="lecture-interactive-card" data-lecture-section="sec_why_stay_small" style="color: #0f172a; border-bottom: 3px solid #64748b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🏠 6. WHY BUSINESSES STAY SMALL</h2>'
    
    t_h2_7 = '<h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">💥 7. WHY BUSINESSES FAIL</h2>'
    r_h2_7 = '<h2 id="sec-why-fail" class="lecture-interactive-card" data-lecture-section="sec_why_fail" style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">💥 7. WHY BUSINESSES FAIL</h2>'

    new_html = html.replace(t_header, r_header, 1).replace(t_h2_1, r_h2_1, 1).replace(t_h2_2, r_h2_2, 1).replace(t_h2_3, r_h2_3, 1).replace(t_h2_4, r_h2_4, 1).replace(t_h2_5, r_h2_5, 1).replace(t_h2_6, r_h2_6, 1).replace(t_h2_7, r_h2_7, 1)
    
    # Fix the unclosed outer div in 1.3
    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff == 1:
        new_html = new_html.strip() + "\n</div>"
        print("Fixed unclosed outer div in 1.3! New diff = 0")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1.3: Khởi sự, Tăng trưởng và Quy mô Doanh nghiệp",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.3: Enterprise, Business Growth and Size. In this comprehensive lesson, we investigate the characteristics of successful entrepreneurs, the anatomy of a business plan, government startup initiatives, methods and limitations of measuring business size, internal versus external growth strategies, and the reasons why businesses remain small or fail.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.3: Khởi sự, Tăng trưởng và Quy mô Doanh nghiệp. Trong bài học này, chúng ta sẽ phân tích các phẩm chất của doanh nhân thành công, cấu trúc kế hoạch kinh doanh, chính sách hỗ trợ khởi nghiệp của chính phủ, các thước đo quy mô doanh nghiệp, chiến lược tăng trưởng nội bộ và sáp nhập, cùng nguyên nhân khiến doanh nghiệp giữ quy mô nhỏ hoặc phá sản."
        },
        {
            "id": "sec_entrepreneurship",
            "title": "1. Tinh thần Doanh nhân (Entrepreneurship)",
            "selector": "#sec-entrepreneurship",
            "en": "Section 1 examines the role and characteristics of entrepreneurs. An entrepreneur is an innovative individual who spots a commercial opportunity, commits capital, and assumes financial risk to start a business. Essential traits include creativity, self-motivation, resilience after failure, leadership, and a willingness to take calculated risks. In return, entrepreneurs achieve financial independence, personal fulfillment, and potentially unlimited profit rewards.",
            "vi": "Mục một tìm hiểu vai trò và tố chất của doanh nhân. Doanh nhân là người sáng tạo, phát hiện cơ hội thương mại, bỏ vốn và chấp nhận rủi ro tài chính để thành lập doanh nghiệp. Những phẩm chất quan trọng gồm tính tự chủ, kiên định, khả năng lãnh đạo và tinh thần dám mạo hiểm có tính toán. Đổi lại, họ đạt được sự độc lập tài chính, khẳng định bản thân và tiềm năng thu được lợi nhuận không giới hạn."
        },
        {
            "id": "sec_business_plan",
            "title": "2. Kế hoạch Kinh doanh (Business Plan)",
            "selector": "#sec-business-plan",
            "en": "Section 2 focuses on the business plan—a formal written document setting out the business objectives, marketing strategy, operations structure, and financial forecasts, including cash flow projections and break-even calculations. A robust business plan forces founders to anticipate obstacles, provides strategic operational direction, and is strictly required by banks and venture capitalists when evaluating loan applications.",
            "vi": "Mục hai tập trung vào kế hoạch kinh doanh (business plan) – văn bản chính thức xác định mục tiêu của doanh nghiệp, chiến lược tiếp thị, kế hoạch vận hành và dự báo tài chính như dòng tiền và điểm hòa vốn. Một bản kế hoạch kinh doanh chặt chẽ giúp nhà sáng lập dự lường rủi ro, định hướng vận hành và là điều kiện tiên quyết để các ngân hàng và nhà đầu tư xem xét cấp vốn vay."
        },
        {
            "id": "sec_gov_support",
            "title": "3. Chính sách hỗ trợ khởi nghiệp của Chính phủ",
            "selector": "#sec-gov-support",
            "en": "Section 3 outlines why and how governments support business startups. Governments assist new enterprises to reduce domestic unemployment, spur technological innovation, generate competition that lowers consumer prices, and promote economic diversification. Support mechanisms include non-repayable cash grants, enterprise zones with discounted rent and tax holidays, low-interest microloans, and free vocational training.",
            "vi": "Mục ba lý giải tại sao và bằng cách nào chính phủ hỗ trợ các doanh nghiệp khởi nghiệp. Chính phủ khuyến khích khởi nghiệp nhằm giảm tỷ lệ thất nghiệp, thúc đẩy đổi mới công nghệ, gia tăng cạnh tranh giúp giảm giá hàng hóa và đa dạng hóa nền kinh tế. Các biện pháp hỗ trợ gồm có viện trợ tài chính không hoàn lại, các khu kinh tế ưu đãi thuế và giá thuê đất, các khoản vay lãi suất thấp và đào tạo kỹ năng quản trị miễn phí."
        },
        {
            "id": "sec_measuring_size",
            "title": "4. Đo lường Quy mô Doanh nghiệp và Hạn chế",
            "selector": "#sec-measuring-size",
            "en": "Section 4 evaluates the four accepted Cambridge methods of measuring business size: number of employees, value of output, value of sales revenue, and value of capital employed. Critical exam warning: profit is never a measure of business size, as large multinational firms can incur temporary losses. Each measurement has limitations: automated car factories employ few workers but utilize massive capital, while labour-intensive garment workshops exhibit the opposite.",
            "vi": "Mục bốn đánh giá bốn thước đo quy mô doanh nghiệp theo chuẩn Cambridge: số lượng nhân viên, giá trị sản lượng đầu ra, doanh thu bán hàng và vốn hoạt động (capital employed). Lưu ý sống còn trong bài thi: Lợi nhuận tuyệt đối không phải thước đo quy mô vì một tập đoàn khổng lồ vẫn có thể tạm thời thua lỗ. Mỗi thước đo đều có giới hạn: một nhà máy tự động hóa có ít công nhân nhưng vốn cực lớn, ngược lại xưởng may thủ công thì rất đông lao động nhưng ít vốn."
        },
        {
            "id": "sec_business_growth",
            "title": "5. Chiến lược Tăng trưởng Doanh nghiệp",
            "selector": "#sec-business-growth",
            "en": "Section 5 explores internal and external business growth. Internal organic growth occurs by purchasing additional machinery, opening new branches, or launching new product lines financed through retained profits. External growth involves mergers and takeovers, categorized into horizontal integration with direct competitors, vertical backward integration with suppliers, vertical forward integration with retail outlets, and conglomerate diversification into unrelated industries.",
            "vi": "Mục năm tìm hiểu các hình thức tăng trưởng doanh nghiệp. Tăng trưởng nội bộ (internal growth) diễn ra thông qua việc mua thêm máy móc, mở chi nhánh mới hoặc phát triển sản phẩm mới từ lợi nhuận giữ lại. Tăng trưởng bên ngoài (external growth) thực hiện qua sáp nhập và mua lại (M&A), bao gồm: sáp nhập ngang với đối thủ cạnh tranh, sáp nhập dọc lùi với nhà cung cấp, sáp nhập dọc tiến với mạng lưới bán lẻ và sáp nhập tập đoàn đa ngành vào các lĩnh vực hoàn toàn mới."
        },
        {
            "id": "sec_why_stay_small",
            "title": "6. Tại sao nhiều Doanh nghiệp giữ Quy mô nhỏ",
            "selector": "#sec-why-stay_small",
            "en": "Section 6 analyzes why millions of enterprises deliberately remain small. Owners often value personal lifestyle freedom and avoid the high stress and loss of control of larger corporations. Furthermore, small firms excel in specialized niche markets with limited total demand, such as bespoke tailoring, antique restoration, or localized personal services where customers demand direct personal interaction with the proprietor.",
            "vi": "Mục sáu phân tích lý do hàng triệu doanh nghiệp chủ động duy trì quy mô nhỏ. Chủ doanh nghiệp thường coi trọng sự tự do, cân bằng cuộc sống và muốn duy trì quyền kiểm soát trực tiếp thay vì gánh vác áp lực của tập đoàn lớn. Ngoài ra, doanh nghiệp nhỏ chiếm ưu thế tuyệt đối trong các thị trường ngách có quy mô khiêm tốn như may đo cao cấp, sửa chữa đồ cổ hoặc các dịch vụ cá nhân đòi hỏi sự chăm sóc trực tiếp."
        },
        {
            "id": "sec_why_fail",
            "title": "7. Nguyên nhân khiến Doanh nghiệp thất bại",
            "selector": "#sec-why-fail",
            "en": "Section 7 examines the primary causes of business failure, especially among early-stage startups. Over 50% of new businesses fail within their first five years due to severe working capital shortages, poor liquidity management, inadequate market research leading to unwanted products, intense competitor reactions, macroeconomic recessions, and reckless over-expansion without sufficient long-term finance.",
            "vi": "Mục bảy tổng kết các nguyên nhân chính dẫn đến thất bại của doanh nghiệp, đặc biệt ở giai đoạn khởi nghiệp. Hơn 50% doanh nghiệp mới đóng cửa trong 5 năm đầu do thiếu hụt vốn lưu động, quản lý dòng tiền yếu kém, nghiên cứu thị trường hời hợt dẫn đến sản phẩm không ai mua, sự đáp trả khốc liệt từ đối thủ cạnh tranh, suy thoái kinh tế hoặc tăng trưởng nóng không kiểm soát được dòng vốn."
        }
    ]
    
    major_sections = [
        {"id": "sec_entrepreneurship", "title": "1. Tinh thần Doanh nhân"},
        {"id": "sec_business_plan", "title": "2. Kế hoạch Kinh doanh"},
        {"id": "sec_gov_support", "title": "3. Hỗ trợ của Chính phủ"},
        {"id": "sec_measuring_size", "title": "4. Đo lường Quy mô Doanh nghiệp"},
        {"id": "sec_business_growth", "title": "5. Tăng trưởng Doanh nghiệp"},
        {"id": "sec_why_stay_small", "title": "6. Tại sao Doanh nghiệp giữ Quy mô nhỏ"},
        {"id": "sec_why_fail", "title": "7. Nguyên nhân Doanh nghiệp thất bại"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 1.3 successfully built!")

if __name__ == "__main__":
    asyncio.run(build_1_3())
