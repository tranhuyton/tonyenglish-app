import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# LECTURE 3.1: Marketing, competition and the customer
# ==============================================================================
async def build_3_1():
    lid = '6cbe4a84-26ed-4a1d-933b-5843e9b9a501'
    code = '3_1'
    title = '3.1. Marketing, competition and the customer'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-what-is-marketing" class="lecture-interactive-card" data-lecture-section="sec_what_is_marketing" style="cursor: pointer; ')
    
    t_h3_role = str(h3s[0])
    r_h3_role = t_h3_role.replace('<h3', '<h3 id="card-marketing-role" class="lecture-interactive-card" data-lecture-section="card_marketing_role" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-market-changes" class="lecture-interactive-card" data-lecture-section="sec_market_changes" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-niche-mass" class="lecture-interactive-card" data-lecture-section="sec_niche_mass" style="cursor: pointer; ')
    
    t_h3_niche = str(h3s[4])
    r_h3_niche = t_h3_niche.replace('<h3', '<h3 id="card-niche-vs-mass" class="lecture-interactive-card" data-lecture-section="card_niche_vs_mass" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_role, r_h3_role, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h3_niche, r_h3_niche, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3.1: Tiếp thị, Cạnh tranh và Khách hàng",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 3.1: Marketing, Competition and the Customer. In this opening chapter of Topic 3, we define the strategic role of marketing, explore why consumer spending patterns change, evaluate intensifying market competition, and contrast niche versus mass marketing.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 3.1: Tiếp thị, Cạnh tranh và Khách hàng. Trong bài mở đầu của Chủ đề ba về Tiếp thị, chúng ta sẽ định nghĩa vai trò chiến lược của marketing, tìm hiểu lý do thay đổi xu hướng tiêu dùng, đánh giá áp lực cạnh tranh gia tăng và so sánh thị trường ngách với thị trường đại trà."
        },
        {
            "id": "sec_what_is_marketing",
            "title": "1. Bản chất và Vai trò của Tiếp thị (Marketing)",
            "selector": "#sec-what-is-marketing",
            "en": "Section 1 defines marketing as identifying, anticipating, and satisfying customer requirements profitably. Modern marketing centers on building long-term customer relationships and brand loyalty rather than merely making one-off sales.",
            "vi": "Mục một định nghĩa marketing là quá trình nhận diện, dự đoán và thỏa mãn nhu cầu của khách hàng một cách có sinh lời. Marketing hiện đại tập trung vào việc kiến tạo mối quan hệ lâu dài và lòng trung thành với thương hiệu thay vì chỉ bán hàng một lần."
        },
        {
            "id": "card_marketing_role",
            "title": "Các Mục tiêu Marketing then chốt",
            "selector": "#card-marketing-role",
            "en": "Core marketing objectives include: boosting sales revenue and market share, building brand image and perceived customer equity, entering foreign overseas markets, and innovating new products to replace declining product lines.",
            "vi": "Các mục tiêu marketing then chốt gồm: gia tăng doanh thu và mở rộng thị phần, củng cố hình ảnh thương hiệu và giá trị cảm nhận của khách hàng, thâm nhập thị trường quốc tế mới và liên tục cải tiến sản phẩm để thay thế các dòng sản phẩm đang bước vào giai đoạn suy thoái."
        },
        {
            "id": "sec_market_changes",
            "title": "2. Biến động Thị trường và Áp lực Cạnh tranh",
            "selector": "#sec-market-changes",
            "en": "Section 2 investigates market dynamics. Customer spending shifts due to changing consumer tastes and fashions, rising disposable incomes, demographic changes such as an aging population, and rapid technological breakthroughs. To survive intensifying globalization and e-commerce rivalry, businesses must maintain competitive prices, uphold superior quality, and sustain promotional presence.",
            "vi": "Mục hai nghiên cứu sự biến động của thị trường. Hành vi chi tiêu của người tiêu dùng thay đổi do thị hiếu và xu hướng mới, thu nhập khả dụng tăng, biến đổi nhân khẩu học như già hóa dân số và sự phát triển công nghệ vượt bậc. Để tồn tại trước sức ép toàn cầu hóa và thương mại điện tử, doanh nghiệp phải duy trì mức giá cạnh tranh, chất lượng vượt trội và đẩy mạnh truyền thông quảng bá."
        },
        {
            "id": "sec_niche_mass",
            "title": "3. Thị trường Ngách (Niche) và Thị trường Đại trà (Mass)",
            "selector": "#sec-niche-mass",
            "en": "Section 3 compares Niche Marketing—targeting a small, highly specialized segment of a larger market—against Mass Marketing, which sells standardized products to the entire market. Niche marketing avoids giant competitors and commands premium pricing, while mass marketing exploits massive economies of scale and widespread market reach.",
            "vi": "Mục ba so sánh Thị trường ngách (Niche Marketing) – nhắm vào một phân khúc khách hàng nhỏ có nhu cầu chuyên biệt – với Thị trường đại trà (Mass Marketing) cung cấp sản phẩm chuẩn hóa cho số đông. Thị trường ngách giúp né tránh các đối thủ khổng lồ và định giá cao, trong khi thị trường đại trà tận dụng triệt để lợi thế kinh tế theo quy mô và độ phủ rộng lớn."
        },
        {
            "id": "card_niche_vs_mass",
            "title": "So sánh Ưu nhược điểm: Niche vs Mass Marketing",
            "selector": "#card-niche-vs-mass",
            "en": "Niche marketing benefits from high profit margins and dedicated customer loyalty, but suffers from limited total sales volume and vulnerability if niche demand collapses. Conversely, mass marketing yields high total revenues, but faces cutthroat price competition, heavy advertising expenditures, and standardized product inflexibility.",
            "vi": "Thị trường ngách mang lại biên lợi nhuận cao và sự gắn bó của khách hàng nhưng quy mô doanh thu bị giới hạn và rủi ro cao nếu nhu cầu phân khúc đó biến mất. Ngược lại, thị trường đại trà đem lại tổng doanh số khổng lồ nhưng phải đối mặt với cuộc chiến giá khốc liệt, ngân sách quảng cáo tốn kém và sự thiếu linh hoạt của sản phẩm đại trà."
        }
    ]
    
    major_sections = [
        {"id": "sec_what_is_marketing", "title": "1. Bản chất và Mục tiêu Tiếp thị"},
        {"id": "sec_market_changes", "title": "2. Biến động Thị trường và Cạnh tranh"},
        {"id": "sec_niche_mass", "title": "3. Thị trường Ngách và Thị trường Đại trà"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 3.1 successfully built!")


# ==============================================================================
# LECTURE 3.2: Market research
# ==============================================================================
async def build_3_2():
    lid = '356dede8-277a-441a-ad73-ef9384973eb7'
    code = '3_2'
    title = '3.2. Market research'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-business-orientation" class="lecture-interactive-card" data-lecture-section="sec_business_orientation" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-market-research-intro" class="lecture-interactive-card" data-lecture-section="sec_market_research_intro" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-primary-research" class="lecture-interactive-card" data-lecture-section="sec_primary_research" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-secondary-research" class="lecture-interactive-card" data-lecture-section="sec_secondary_research" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-accuracy-presentation" class="lecture-interactive-card" data-lecture-section="sec_accuracy_presentation" style="cursor: pointer; ')
    
    t_h2_6 = str(h2s[5])
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-sampling-methods" class="lecture-interactive-card" data-lecture-section="sec_sampling_methods" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)\
                   .replace(t_h2_6, r_h2_6, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3.2: Nghiên cứu thị trường",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 3.2: Market Research. In this lesson, we explore product-oriented versus market-oriented business approaches, examine primary and secondary data collection techniques, evaluate sampling methods, and assess the accuracy of market intelligence.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 3.2: Nghiên cứu thị trường. Trong bài học này, chúng ta sẽ tìm hiểu định hướng sản phẩm và định hướng thị trường, các phương pháp thu thập dữ liệu sơ cấp và thứ cấp, kỹ thuật chọn mẫu cùng phương pháp đánh giá độ tin cậy của số liệu."
        },
        {
            "id": "sec_business_orientation",
            "title": "1. Định hướng Doanh nghiệp: Sản phẩm hay Thị trường",
            "selector": "#sec-business-orientation",
            "en": "Section 1 contrasts Product-Oriented businesses—which focus primarily on manufacturing excellence and technical innovation before trying to sell—against Market-Oriented businesses, which conduct comprehensive consumer research first to ensure new goods align precisely with customer preferences.",
            "vi": "Mục một đối chiếu Doanh nghiệp định hướng sản phẩm (Product-Oriented) – tập trung vào kỹ thuật và chất lượng sản phẩm trước khi bán – với Doanh nghiệp định hướng thị trường (Market-Oriented), luôn nghiên cứu nhu cầu khách hàng trước để bảo đảm sản phẩm mới đáp ứng đúng kỳ vọng của người tiêu dùng."
        },
        {
            "id": "sec_market_research_intro",
            "title": "2. Vai trò của Nghiên cứu Thị trường",
            "selector": "#sec-market-research-intro",
            "en": "Section 2 introduces Market Research: the systematic gathering, recording, and analysis of data about the market for goods and services. Research minimizes commercial launch risks, identifies market gaps, reveals customer willingness to pay, and gauges competitive strengths.",
            "vi": "Mục hai giới thiệu về Nghiên cứu thị trường: quá trình thu thập, ghi chép và phân tích có hệ thống thông tin về thị trường hàng hóa và dịch vụ. Nghiên cứu giúp hạn chế rủi ro ra mắt sản phẩm mới, phát hiện khoảng trống thị trường, xác định mức giá sẵn sàng chi trả và đánh giá đối thủ cạnh tranh."
        },
        {
            "id": "sec_primary_research",
            "title": "3. Nghiên cứu Sơ cấp (Field Research)",
            "selector": "#sec-primary-research",
            "en": "Section 3 examines Primary Research: gathering original first-hand data directly from respondents via questionnaires, focus groups, interviews, and direct observation. Primary data is up-to-date, directly relevant, and exclusive to the firm, but is expensive and time-consuming to execute.",
            "vi": "Mục ba phân tích Nghiên cứu sơ cấp (Primary Research): thu thập dữ liệu gốc lần đầu từ đối tượng khảo sát thông qua bảng câu hỏi, nhóm thảo luận tập trung, phỏng vấn sâu và quan sát thực tế. Dữ liệu sơ cấp có tính cập nhật cao, liên quan trực tiếp và mang tính độc quyền nhưng tốn kém chi phí và thời gian."
        },
        {
            "id": "sec_secondary_research",
            "title": "4. Nghiên cứu Thứ cấp (Desk Research)",
            "selector": "#sec-secondary-research",
            "en": "Section 4 covers Secondary Research: gathering second-hand data already published by internal records, government census bureaus, trade journals, or commercial research agencies. Secondary research is cheap and instantly accessible, but may be outdated, biased, or too general.",
            "vi": "Mục bốn trình bày Nghiên cứu thứ cấp (Secondary Research): khai thác dữ liệu đã được công bố từ hồ sơ nội bộ, số liệu thống kê chính phủ, tạp chí chuyên ngành hoặc báo cáo thị trường. Nghiên cứu thứ cấp chi phí thấp và tra cứu tức thì nhưng số liệu có thể bị lỗi thời hoặc không khớp với mục tiêu nghiên cứu cụ thể."
        },
        {
            "id": "sec_accuracy_presentation",
            "title": "5. Độ chính xác và Trình bày Dữ liệu",
            "selector": "#sec-accuracy-presentation",
            "en": "Section 5 analyzes data presentation via bar charts, pie charts, and line graphs, and identifies sources of inaccuracies such as sample bias, poorly worded leading questions, dishonest respondent replies, and outdated secondary data.",
            "vi": "Mục năm phân tích cách trình bày dữ liệu bằng biểu đồ cột, biểu đồ tròn và đồ thị đường thẳng, đồng thời chỉ ra các nguyên nhân gây sai lệch số liệu như mẫu khảo sát thiếu đại diện, câu hỏi định kiến dẫn dắt, câu trả lời thiếu trung thực và số liệu thứ cấp đã lỗi thời."
        },
        {
            "id": "sec_sampling_methods",
            "title": "6. Kỹ thuật Chọn mẫu và Chiến lược thi Cambridge",
            "selector": "#sec-sampling-methods",
            "en": "Section 6 explores sampling methods including random sampling and quota sampling. In Cambridge exam evaluations, candidates must balance the budget constraints and speed of secondary desk research against the specialized accuracy of primary field studies.",
            "vi": "Mục sáu nghiên cứu các phương pháp chọn mẫu như chọn mẫu ngẫu nhiên (random sampling) và chọn mẫu theo hạn ngạch (quota sampling). Trong đề thi Cambridge, thí sinh cần cân đối ngân sách và tốc độ của nghiên cứu thứ cấp với độ chính xác chuyên sâu của nghiên cứu sơ cấp."
        }
    ]
    
    major_sections = [
        {"id": "sec_business_orientation", "title": "1. Định hướng Doanh nghiệp"},
        {"id": "sec_primary_research", "title": "2. Nghiên cứu Sơ cấp (Primary)"},
        {"id": "sec_secondary_research", "title": "3. Nghiên cứu Thứ cấp (Secondary)"},
        {"id": "sec_sampling_methods", "title": "4. Kỹ thuật Chọn mẫu và Độ chính xác"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 3.2 successfully built!")


# ==============================================================================
# LECTURE 3.3: The marketing mix
# ==============================================================================
async def build_3_3():
    lid = '25fe41d9-780d-41a6-876d-fff3e0d854c5'
    code = '3_3'
    title = '3.3. The marketing mix'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-product" class="lecture-interactive-card" data-lecture-section="sec_product" style="cursor: pointer; ')
    
    t_h3_plc = str(h3s[2])
    r_h3_plc = t_h3_plc.replace('<h3', '<h3 id="card-plc" class="lecture-interactive-card" data-lecture-section="card_plc" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-price" class="lecture-interactive-card" data-lecture-section="sec_price" style="cursor: pointer; ')
    
    t_h3_pricing = str(h3s[3])
    r_h3_pricing = t_h3_pricing.replace('<h3', '<h3 id="card-pricing-methods" class="lecture-interactive-card" data-lecture-section="card_pricing_methods" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-place" class="lecture-interactive-card" data-lecture-section="sec_place" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-promotion" class="lecture-interactive-card" data-lecture-section="sec_promotion" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-marketing-tech" class="lecture-interactive-card" data-lecture-section="sec_marketing_tech" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_plc, r_h3_plc, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_pricing, r_h3_pricing, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3.3: Tiếp thị hỗn hợp (The 4Ps)",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 3.3: The Marketing Mix. In this flagship chapter, we unpack the four Ps of marketing: Product, Price, Place, and Promotion, evaluate the product life cycle, examine pricing mechanisms, map distribution channels, and analyze e-commerce and social media.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 3.3: Tiếp thị hỗn hợp (Marketing Mix 4P). Trong bài học trọng tâm này, chúng ta sẽ khảo sát bốn chữ P của tiếp thị: Sản phẩm (Product), Giá (Price), Phân phối (Place) và Chiêu thị (Promotion), cùng vòng đời sản phẩm, các chiến lược định giá, kênh phân phối và thương mại điện tử."
        },
        {
            "id": "sec_product",
            "title": "1. Chữ P thứ nhất: Sản phẩm (Product)",
            "selector": "#sec-product",
            "en": "Section 1 analyzes Product strategy. New Product Development (NPD) generates ideas, creates prototypes, and conducts test marketing. Strong branding and distinctive packaging differentiate the product, establish consumer trust, and allow premium pricing.",
            "vi": "Mục một phân tích chiến lược Sản phẩm. Quá trình phát triển sản phẩm mới (NPD) bao gồm sáng tạo ý tưởng, thử nghiệm mẫu và bán thử nghiệm trên thị trường. Thương hiệu mạnh và bao bì bắt mắt giúp định vị sản phẩm khác biệt, xây dựng niềm tin và cho phép định giá cao hơn đối thủ."
        },
        {
            "id": "card_plc",
            "title": "Vòng đời Sản phẩm (Product Life Cycle - PLC)",
            "selector": "#card-plc",
            "en": "The Product Life Cycle traces sales volume across six stages: Development, Introduction, Growth, Maturity, Saturation, and Decline. Extension strategies—such as rebranding, reformulating ingredients, or entering overseas markets—rejuvenate sales before a product reaches full obsolescence.",
            "vi": "Vòng đời sản phẩm (PLC) theo dõi doanh số qua sáu giai đoạn: Phát triển, Giới thiệu, Tăng trưởng, Chín muồi, Bão hòa và Suy thoái. Các chiến lược kéo dài vòng đời như đổi mới bao bì, cải tiến công thức hoặc mở rộng thị trường xuất khẩu giúp khôi phục đà tăng trưởng trước khi sản phẩm bị đào thải."
        },
        {
            "id": "sec_price",
            "title": "2. Chữ P thứ hai: Giá cả (Price)",
            "selector": "#sec-price",
            "en": "Section 2 investigates pricing strategies: Cost-plus pricing adds a markup margin over unit costs; Penetration pricing sets low entry prices to rapidly capture market share; Price skimming charges high initial prices for novel technologies; and Competitive pricing matches prevailing market levels.",
            "vi": "Mục hai nghiên cứu các chiến lược định giá: Định giá cộng chi phí (Cost-plus) cộng biên lợi nhuận vào chi phí đơn vị; Định giá thâm nhập (Penetration) đặt giá thấp ban đầu để nhanh chóng chiếm thị phần; Định giá hớt váng (Skimming) đặt giá cao ngất ngưởng cho công nghệ mới độc quyền; và Định giá theo đối thủ cạnh tranh."
        },
        {
            "id": "card_pricing_methods",
            "title": "Độ co giãn của Cầu theo Giá (Price Elasticity of Demand - PED)",
            "selector": "#card-pricing-methods",
            "en": "Price Elasticity of Demand measures the responsiveness of quantity demanded to a change in price. For price-elastic goods with many substitutes, price cuts boost total revenue; for price-inelastic necessities, raising prices expands revenue without significantly denting sales volume.",
            "vi": "Độ co giãn của cầu theo giá (PED) đo lường mức độ phản ứng của lượng cầu khi giá thay đổi. Với hàng hóa co giãn có nhiều sản phẩm thay thế, giảm giá sẽ làm tăng tổng doanh thu; ngược lại với hàng thiết yếu kém co giãn, tăng giá giúp tăng mạnh doanh thu mà không làm sụt giảm sản lượng."
        },
        {
            "id": "sec_place",
            "title": "3. Chữ P thứ ba: Phân phối (Place)",
            "selector": "#sec-place",
            "en": "Section 3 evaluates distribution channels: Channel 1 sells directly from producer to consumer; Channel 2 utilizes independent retailers; Channel 3 introduces wholesalers; and Channel 4 deploys overseas sales agents. Direct selling maximizes profit margins, while wholesaler networks maximize physical retail coverage.",
            "vi": "Mục ba đánh giá các kênh phân phối: Kênh 1 bán trực tiếp từ nhà sản xuất đến người tiêu dùng; Kênh 2 thông qua nhà bán lẻ; Kênh 3 qua nhà bán buôn và bán lẻ; Kênh 4 qua đại lý xuất khẩu. Bán trực tiếp tối đa hóa biên lợi nhuận, trong khi mạng lưới đại lý và bán buôn tối đa hóa độ phủ sóng trên thị trường."
        },
        {
            "id": "sec_promotion",
            "title": "4. Chữ P thứ tư: Chiêu thị (Promotion)",
            "selector": "#sec-promotion",
            "en": "Section 4 covers the promotional mix: Above-the-line advertising via television, radio, billboards, and internet banners; and Below-the-line promotions via point-of-sale discounts, buy-one-get-one-free offers, sponsorship, and public relations.",
            "vi": "Mục bốn bao quát phối thức chiêu thị: Quảng cáo trên các phương tiện đại chúng (Above-the-line) như truyền hình, phát thanh, biển bảng và banner trực tuyến; cùng các chương trình xúc tiến bán trực tiếp (Below-the-line) như giảm giá tại quầy, mua một tặng một, tài trợ sự kiện và quan hệ công chúng (PR)."
        },
        {
            "id": "sec_marketing_tech",
            "title": "5. Công nghệ trong Tiếp thị: Thương mại điện tử và Mạng xã hội",
            "selector": "#sec-marketing-tech",
            "en": "Section 5 evaluates how digital technology transforms marketing. E-commerce enables round-the-clock global trading, dynamic algorithmic pricing, and reduced physical shop rent. Social media advertising facilitates precision demographic targeting and viral word-of-mouth campaigns.",
            "vi": "Mục năm phân tích sự chuyển đổi tiếp thị trong thời đại số. Thương mại điện tử cho phép bán hàng toàn cầu 24/7, định giá linh hoạt theo thuật toán và cắt giảm chi phí thuê mặt bằng vật lý. Quảng cáo mạng xã hội giúp nhắm mục tiêu chính xác theo nhân khẩu học và tạo chiến dịch lan tỏa tự nhiên."
        }
    ]
    
    major_sections = [
        {"id": "sec_product", "title": "1. Chiến lược Sản phẩm & PLC"},
        {"id": "sec_price", "title": "2. Chiến lược Giá cả & PED"},
        {"id": "sec_place", "title": "3. Kênh Phân phối (Place)"},
        {"id": "sec_promotion", "title": "4. Phối thức Chiêu thị (Promotion)"},
        {"id": "sec_marketing_tech", "title": "5. E-commerce & Digital Marketing"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 3.3 successfully built!")


# ==============================================================================
# LECTURE 3.4: The marketing strategy
# ==============================================================================
async def build_3_4():
    lid = 'c0d60bf9-ad33-456c-807e-9e29318113b8'
    code = '3_4'
    title = '3.4. The marketing strategy'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-marketing-strategy" class="lecture-interactive-card" data-lecture-section="sec_marketing_strategy" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-legal-controls" class="lecture-interactive-card" data-lecture-section="sec_legal_controls" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-entering-markets" class="lecture-interactive-card" data-lecture-section="sec_entering_markets" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-recommend-strategy" class="lecture-interactive-card" data-lecture-section="sec_recommend_strategy" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3.4: Chiến lược tiếp thị",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 3.4: The Marketing Strategy. In this concluding chapter of Topic 3, we define how businesses combine the 4Ps into an integrated marketing strategy, examine legal consumer protections, analyze the hurdles of global market entry, and master Cambridge evaluation questions.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 3.4: Chiến lược tiếp thị. Trong bài học tổng kết Chủ đề ba, chúng ta sẽ tìm hiểu cách kết hợp 4 chữ P thành một chiến lược tiếp thị nhất quán, các quy định pháp luật bảo vệ người tiêu dùng, cách vượt qua rào cản khi mở rộng ra thị trường quốc tế và phương pháp làm bài thi Cambridge."
        },
        {
            "id": "sec_marketing_strategy",
            "title": "1. Chiến lược Marketing Tích hợp",
            "selector": "#sec-marketing-strategy",
            "en": "Section 1 defines a Marketing Strategy as a coherent plan combining the 4Ps of the marketing mix to achieve specific corporate marketing objectives. The elements of the marketing mix must be mutually supportive: a premium luxury perfume requires prestigious glass packaging, selective boutique distribution, and sophisticated lifestyle advertising.",
            "vi": "Mục một định nghĩa Chiến lược tiếp thị là một kế hoạch phối hợp chặt chẽ bốn chữ P nhằm đạt được các mục tiêu kinh doanh cụ thể. Các yếu tố marketing mix phải bổ trợ tương hỗ cho nhau: một dòng nước hoa cao cấp đòi hỏi thiết kế chai thủy tinh sang trọng, phân phối tại các cửa hàng chọn lọc và quảng cáo tôn vinh đẳng cấp sống."
        },
        {
            "id": "sec_legal_controls",
            "title": "2. Khung Pháp lý Bảo vệ Người tiêu dùng",
            "selector": "#sec-legal-controls",
            "en": "Section 2 investigates statutory consumer protection laws: bans on misleading advertising, weight and measurement standards, product safety regulations, and laws against anti-competitive price collusion. Businesses failing to comply risk hefty fines, loss of reputation, and product recalls.",
            "vi": "Mục hai khảo sát các quy định pháp luật bảo vệ người tiêu dùng: nghiêm cấm quảng cáo sai sự thật, chuẩn hóa đơn vị đo lường và trọng lượng, quy chuẩn an toàn sản phẩm và luật chống độc quyền thao túng giá. Doanh nghiệp vi phạm sẽ bị xử phạt hành chính nặng nề, mất uy tín thương hiệu và bị buộc thu hồi sản phẩm."
        },
        {
            "id": "sec_entering_markets",
            "title": "3. Thâm nhập Thị trường Quốc tế",
            "selector": "#sec-entering-markets",
            "en": "Section 3 analyzes the challenges of entering foreign overseas markets: linguistic barriers, cultural differences in consumer tastes, import tariffs and trade quotas, and exchange rate volatility. Strategies to overcome these hurdles include international joint ventures, franchising to domestic partners, and establishing local production subsidiaries.",
            "vi": "Mục ba phân tích những thách thức khi vươn ra thị trường quốc tế: rào cản ngôn ngữ, khác biệt văn hóa tiêu dùng, thuế quan nhập khẩu và hạn ngạch thương mại, cùng biến động tỷ giá hối đoái. Giải pháp vượt qua khó khăn bao gồm liên doanh quốc tế, nhượng quyền cho đối tác bản địa và thành lập chi nhánh sản xuất tại nước sở tại."
        },
        {
            "id": "sec_recommend_strategy",
            "title": "4. Chiến lược làm bài thi Cambridge: Đề xuất Chiến lược Tiếp thị",
            "selector": "#sec-recommend-strategy",
            "en": "Section 4 presents the Cambridge examination formula for evaluating marketing strategies. Candidates must synthesize available financial resources, target customer demographic profiles, and competitor strengths to construct a cohesive, fully justified marketing plan.",
            "vi": "Mục bốn hướng dẫn công thức chấm điểm của giám khảo Cambridge cho câu hỏi chiến lược tiếp thị. Thí sinh cần tổng hợp ngân sách tài chính sẵn có, đặc điểm nhân khẩu học của khách hàng mục tiêu và điểm mạnh của đối thủ để xây dựng một kế hoạch tiếp thị nhất quán và có sức thuyết phục cao."
        }
    ]
    
    major_sections = [
        {"id": "sec_marketing_strategy", "title": "1. Chiến lược Marketing Tích hợp"},
        {"id": "sec_legal_controls", "title": "2. Pháp lý Bảo vệ Người tiêu dùng"},
        {"id": "sec_entering_markets", "title": "3. Thâm nhập Thị trường Quốc tế"},
        {"id": "sec_recommend_strategy", "title": "4. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 3.4 successfully built!")


# ==============================================================================
# MAIN BATCH RUNNER FOR TOPIC 3
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING TOPIC 3 BUILD: ALL 4 LECTURES (3.1 -> 3.4)")
    print("*******************************************************\n")
    
    await build_3_1()
    await asyncio.sleep(2)
    
    await build_3_2()
    await asyncio.sleep(2)
    
    await build_3_3()
    await asyncio.sleep(2)
    
    await build_3_4()
    
    print("\n*******************************************************")
    print("TOPIC 3 COMPLETE: ALL 4 LECTURES PROCESSED SUCCESSFULLY!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
