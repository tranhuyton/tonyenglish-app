import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# LECTURE 6.1: Economic issues
# ==============================================================================
async def build_6_1():
    lid = '0e8fbc94-5976-4c7f-8588-471ea93926f5'
    code = '6_1'
    title = '6.1. Economic issues'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-business-cycle" class="lecture-interactive-card" data-lecture-section="sec_business_cycle" style="cursor: pointer; ')
    
    t_h3_cycle = str(h3s[0])
    r_h3_cycle = t_h3_cycle.replace('<h3', '<h3 id="card-cycle-stages" class="lecture-interactive-card" data-lecture-section="card_cycle_stages" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-economic-impacts" class="lecture-interactive-card" data-lecture-section="sec_economic_impacts" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-gov-objectives" class="lecture-interactive-card" data-lecture-section="sec_gov_objectives" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-economic-policies" class="lecture-interactive-card" data-lecture-section="sec_economic_policies" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-business-policy-response" class="lecture-interactive-card" data-lecture-section="sec_business_policy_response" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_cycle, r_h3_cycle, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 6.1: Các Vấn đề Kinh tế vĩ mô",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 6.1: Economic Issues. In this opening chapter of Topic 6, External Influences on Business Activity, we explore the four stages of the business cycle, analyze how GDP, inflation, and unemployment impact enterprises, examine government economic objectives, and assess fiscal and monetary policy.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 6.1: Các Vấn đề Kinh tế vĩ mô. Trong bài mở đầu của Chủ đề sáu về Các Tác động Bên ngoài, chúng ta sẽ khảo sát bốn giai đoạn của chu kỳ kinh tế, tác động của GDP, lạm phát và thất nghiệp đến doanh nghiệp, các mục tiêu kinh tế vĩ mô của chính phủ cùng chính sách tài khóa và tiền tệ."
        },
        {
            "id": "sec_business_cycle",
            "title": "1. Chu kỳ Kinh tế (The Business Cycle)",
            "selector": "#sec-business-cycle",
            "en": "Section 1 charts fluctuations in national output over time across four recurring stages: Growth, where consumer spending and employment climb; Boom, where factories operate at full capacity and inflation overheats; Recession, where GDP contracts for two consecutive quarters; and Slump, marked by high unemployment and business bankruptcies.",
            "vi": "Mục một phác họa sự biến động của sản lượng quốc gia qua bốn giai đoạn chu kỳ kinh tế: Tăng trưởng (Growth) khi chi tiêu tiêu dùng và việc làm gia tăng; Đỉnh hưng thịnh (Boom) khi nhà máy vận hành hết công suất và lạm phát tăng cao; Suy thoái (Recession) khi GDP sụt giảm hai quý liên tiếp; và Đình đốn (Slump) với tỷ lệ thất nghiệp tăng vọt và hàng loạt doanh nghiệp phá sản."
        },
        {
            "id": "card_cycle_stages",
            "title": "Chiến lược Thích ứng với Chu kỳ Kinh tế",
            "selector": "#card-cycle-stages",
            "en": "During economic booms, luxury brands expand production lines and raise prices. During recessions, discount retailers thrive as consumers downscale spending to essential budget ranges, while heavy capital machinery producers face collapsing demand.",
            "vi": "Trong thời kỳ đỉnh cao kinh tế, các thương hiệu cao cấp mở rộng sản xuất và tăng giá bán. Trong giai đoạn suy thoái, các nhà bán lẻ giá rẻ lại phát đạt do người tiêu dùng thắt chặt chi tiêu vào các mặt hàng thiết yếu, trong khi các nhà sản xuất máy móc thiết bị nặng phải đối mặt với sự sụt giảm nhu cầu nghiêm trọng."
        },
        {
            "id": "sec_economic_impacts",
            "title": "2. Tác động của Thất nghiệp, Lạm phát và GDP",
            "selector": "#sec-economic-impacts",
            "en": "Section 2 investigates macroeconomic indicators: Rising unemployment reduces consumer purchasing power but lowers recruitment wage pressures. High inflation erodes real wages, escalates raw material costs, and diminishes export competitiveness. Expanding GDP widens sales opportunities across consumer markets.",
            "vi": "Mục hai nghiên cứu các chỉ số kinh tế vĩ mô: Thất nghiệp tăng làm giảm sức mua của người tiêu dùng nhưng giúp doanh nghiệp dễ tuyển dụng lao động với chi phí thấp hơn. Lạm phát cao bào mòn tiền lương thực tế, đẩy chi phí nguyên vật liệu tăng vọt và làm giảm sức cạnh tranh xuất khẩu. GDP tăng trưởng mở rộng cơ hội bán hàng trên toàn thị trường."
        },
        {
            "id": "sec_gov_objectives",
            "title": "3. Bốn Mục tiêu Kinh tế của Chính phủ",
            "selector": "#sec-gov-objectives",
            "en": "Section 3 outlines the four core macroeconomic aims of national governments: sustainable economic growth measured by rising real GDP, low stable inflation, low unemployment, and a healthy balance of payments where export revenues balance import expenditures.",
            "vi": "Mục ba tổng kết bốn mục tiêu kinh tế vĩ mô của chính phủ: tăng trưởng kinh tế bền vững đo lường bằng sự gia tăng GDP thực tế, lạm phát thấp và ổn định, duy trì tỷ lệ thất nghiệp thấp, và cân bằng cán cân thanh toán quốc tế giữa kim ngạch xuất khẩu và nhập khẩu."
        },
        {
            "id": "sec_economic_policies",
            "title": "4. Chính sách Tài khóa, Tiền tệ và Cung ứng",
            "selector": "#sec-economic-policies",
            "en": "Section 4 contrasts economic management tools: Fiscal Policy uses taxes and government spending; Monetary Policy adjusts interest rates and credit availability; and Supply-Side Policy invests in vocational training, deregulation, and infrastructure to boost national productive potential.",
            "vi": "Mục bốn phân biệt các công cụ điều hành kinh tế: Chính sách tài khóa (Fiscal Policy) sử dụng thuế và chi tiêu công; Chính sách tiền tệ (Monetary Policy) điều chỉnh lãi suất và hạn mức tín dụng; và Chính sách phía cung (Supply-Side Policy) đầu tư vào đào tạo nghề, giảm bớt thủ tục hành chính và nâng cấp cơ sở hạ tầng để mở rộng năng lực sản xuất quốc gia."
        },
        {
            "id": "sec_business_policy_response",
            "title": "5. Phản ứng của Doanh nghiệp trước Chính sách Kinh tế",
            "selector": "#sec-business-policy-response",
            "en": "Section 5 details corporate adaptation. When central banks hike interest rates, borrowing costs soar and consumer mortgage payments climb, forcing businesses to cancel debt-funded investments and discount inventory to generate immediate cash reserves.",
            "vi": "Mục năm phân tích sự thích ứng của doanh nghiệp. Khi ngân hàng trung ương tăng lãi suất, chi phí vay nợ tăng cao và gánh nặng trả góp của người dân tăng lên, buộc doanh nghiệp phải hủy bỏ các dự án đầu tư sử dụng vốn vay và giảm giá hàng tồn kho để tạo dòng tiền mặt dự phòng."
        }
    ]
    
    major_sections = [
        {"id": "sec_business_cycle", "title": "1. Chu kỳ Kinh tế (Business Cycle)"},
        {"id": "sec_economic_impacts", "title": "2. Tác động của Lạm phát, Thất nghiệp & GDP"},
        {"id": "sec_gov_objectives", "title": "3. Mục tiêu Kinh tế của Chính phủ"},
        {"id": "sec_economic_policies", "title": "4. Chính sách Tài khóa & Tiền tệ"},
        {"id": "sec_business_policy_response", "title": "5. Phản ứng Doanh nghiệp & Chiến lược thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 6.1 successfully built!")


# ==============================================================================
# LECTURE 6.2: Environmental and ethical issues
# ==============================================================================
async def build_6_2():
    lid = 'a1d571ff-fa12-46c2-a49d-1df88df13214'
    code = '6_2'
    title = '6.2. Environmental and ethical issues'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-environmental-concerns" class="lecture-interactive-card" data-lecture-section="sec_environmental_concerns" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-externalities" class="lecture-interactive-card" data-lecture-section="sec_externalities" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-sustainable-development" class="lecture-interactive-card" data-lecture-section="sec_sustainable_development" style="cursor: pointer; ')
    
    t_h3_pressure = str(h3s[3])
    r_h3_pressure = t_h3_pressure.replace('<h3', '<h3 id="card-pressure-groups" class="lecture-interactive-card" data-lecture-section="card_pressure_groups" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-business-ethics" class="lecture-interactive-card" data-lecture-section="sec_business_ethics" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-ethics-profitability" class="lecture-interactive-card" data-lecture-section="sec_ethics_profitability" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h3_pressure, r_h3_pressure, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 6.2: Các Vấn đề Môi trường và Đạo đức",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 6.2: Environmental and Ethical Issues. In this modern chapter, we evaluate social costs and benefits, unpack negative externalities, explore sustainable development and environmental pressure groups, and examine the trade-off between ethical principles and commercial profit.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 6.2: Các Vấn đề Môi trường và Đạo đức kinh doanh. Trong bài học mang tính thời sự này, chúng ta sẽ đánh giá chi phí xã hội và lợi ích xã hội, ngoại tác tiêu cực, phát triển bền vững và các nhóm áp lực môi trường, cùng sự đánh đổi giữa đạo đức và lợi nhuận."
        },
        {
            "id": "sec_environmental_concerns",
            "title": "1. Mối quan tâm Môi trường và Trách nhiệm Xã hội",
            "selector": "#sec-environmental-concerns",
            "en": "Section 1 examines environmental impacts: air and river pollution, global warming carbon emissions, and resource depletion. Governments enforce legal environmental controls, fines, and pollution permits to curb industrial degradation.",
            "vi": "Mục một xem xét các tác động môi trường: ô nhiễm không khí và nguồn nước, khí thải carbon gây biến đổi khí hậu và cạn kiệt tài nguyên thiên nhiên. Chính phủ áp dụng các chế tài pháp lý, xử phạt hành chính và giấy phép xả thải để kiểm soát ô nhiễm công nghiệp."
        },
        {
            "id": "sec_externalities",
            "title": "2. Ngoại tác: Chi phí Xã hội và Lợi ích Xã hội",
            "selector": "#sec-externalities",
            "en": "Section 2 provides the core economic equation: Social Costs equal Private Costs plus External Costs. Social Benefits equal Private Benefits plus External Benefits. Negative externalities—such as toxic factory smog or heavy traffic congestion—are borne by the local community rather than the polluting firm.",
            "vi": "Mục hai đưa ra công thức kinh tế học cốt lõi: Chi phí xã hội bằng Chi phí tư nhân cộng Chi phí ngoại tác. Lợi ích xã hội bằng Lợi ích tư nhân cộng Lợi ích ngoại tác. Ngoại tác tiêu cực như khói bụi độc hại hay tắc đường do xe tải nhà máy gây ra là những tổn thất mà cộng đồng địa phương phải gánh chịu thay cho doanh nghiệp."
        },
        {
            "id": "sec_sustainable_development",
            "title": "3. Phát triển Bền vững (Sustainable Development)",
            "selector": "#sec-sustainable-development",
            "en": "Section 3 defines Sustainable Development as economic activity that meets the needs of the present without compromising the ability of future generations to meet their own needs. Enterprises embrace renewable solar energy, biodegradable packaging, and circular recycling initiatives.",
            "vi": "Mục ba định nghĩa Phát triển bền vững là hoạt động kinh tế đáp ứng các nhu cầu của hiện tại mà không làm tổn hại đến khả năng đáp ứng nhu cầu của các thế hệ tương lai. Doanh nghiệp chủ động chuyển đổi sang năng lượng mặt trời, bao bì tự phân hủy sinh học và mô hình tái chế tuần hoàn."
        },
        {
            "id": "card_pressure_groups",
            "title": "Vai trò của Nhóm Áp lực (Pressure Groups)",
            "selector": "#card-pressure-groups",
            "en": "Pressure Groups are organized citizen associations that seek to influence government policies and corporate actions. Tactics include consumer boycotts, viral social media campaigns, and staging peaceful demonstrations to hold polluting enterprises publicly accountable.",
            "vi": "Nhóm áp lực (Pressure Groups) là tổ chức của người dân nhằm tác động lên chính sách của chính phủ và hành vi của doanh nghiệp. Các biện pháp bao gồm kêu gọi người tiêu dùng tẩy chay sản phẩm, tổ chức chiến dịch truyền thông và biểu tình hòa bình để buộc các doanh nghiệp gây ô nhiễm phải chịu trách nhiệm trước công chúng."
        },
        {
            "id": "sec_business_ethics",
            "title": "4. Đạo đức Kinh doanh (Business Ethics)",
            "selector": "#sec-business-ethics",
            "en": "Section 4 investigates Business Ethics: moral rules and behavioral standards guiding decision making beyond statutory legal compliance. Issues include child labour in overseas factories, fair trade wages for smallholder farmers, and deceptive marketing to vulnerable children.",
            "vi": "Mục bốn phân tích Đạo đức kinh doanh: các nguyên tắc đạo đức và chuẩn mực hành vi định hướng ra quyết định vượt lên trên các yêu cầu tối thiểu của luật pháp. Các vấn đề bao gồm bóc lột lao động trẻ em tại các xưởng gia công, trả giá thương mại công bằng (fair trade) cho nông dân và cấm quảng cáo lừa dối hướng vào trẻ em."
        },
        {
            "id": "sec_ethics_profitability",
            "title": "5. Đạo đức đối chiếu với Lợi nhuận (Cambridge Exam Strategy)",
            "selector": "#sec-ethics-profitability",
            "en": "Section 5 details the Cambridge evaluation dilemma: Acting ethically raises operating production costs in the short run, but builds prestigious brand reputation, attracts ethical investors, and avoids crippling consumer boycotts in the long term.",
            "vi": "Mục năm cung cấp chiến lược giải quyết bài toán tình huống Cambridge: Hành xử có đạo đức có thể làm tăng chi phí sản xuất trong ngắn hạn, nhưng về lâu dài lại kiến tạo uy tín thương hiệu vững chắc, thu hút các quỹ đầu tư bền vững và tránh được những làn sóng tẩy chay phá hủy doanh nghiệp."
        }
    ]
    
    major_sections = [
        {"id": "sec_environmental_concerns", "title": "1. Mối quan tâm Môi trường"},
        {"id": "sec_externalities", "title": "2. Ngoại tác (Social Costs & Benefits)"},
        {"id": "sec_sustainable_development", "title": "3. Phát triển Bền vững & Nhóm Áp lực"},
        {"id": "sec_business_ethics", "title": "4. Đạo đức Kinh doanh (Ethics)"},
        {"id": "sec_ethics_profitability", "title": "5. Đạo đức vs Lợi nhuận & Chiến lược thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 6.2 successfully built!")


# ==============================================================================
# LECTURE 6.3: Business and globalisation
# ==============================================================================
async def build_6_3():
    lid = '1bc6f5c1-e71b-4d0d-8153-d2f74180a845'
    code = '6_3'
    title = '6.3. Business and globalisation'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-globalisation" class="lecture-interactive-card" data-lecture-section="sec_globalisation" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-tariffs-quotas" class="lecture-interactive-card" data-lecture-section="sec_tariffs_quotas" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-mncs" class="lecture-interactive-card" data-lecture-section="sec_mncs" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-impact-host-countries" class="lecture-interactive-card" data-lecture-section="sec_impact_host_countries" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-exchange-rates" class="lecture-interactive-card" data-lecture-section="sec_exchange_rates" style="cursor: pointer; ')
    
    t_h2_6 = str(h2s[5])
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-recommend-globalisation" class="lecture-interactive-card" data-lecture-section="sec_recommend_globalisation" style="cursor: pointer; ')

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
            "title": "Giới thiệu Bài 6.3: Doanh nghiệp và Toàn cầu hóa",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 6.3: Business and Globalisation. In this final chapter of the course, we examine the forces driving globalisation, import tariffs and quotas, multinational corporations (MNCs), their impacts on host nations, and the mechanics of foreign exchange rate fluctuations.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 6.3: Doanh nghiệp và Toàn cầu hóa. Trong bài học kết thúc toàn bộ khóa học, chúng ta sẽ khảo sát động lực của toàn cầu hóa, thuế quan và hạn ngạch nhập khẩu, các tập đoàn đa quốc gia (MNC), tác động của họ lên các nước sở tại cùng tác động của biến động tỷ giá hối đoái."
        },
        {
            "id": "sec_globalisation",
            "title": "1. Động lực và Tác động của Toàn cầu hóa",
            "selector": "#sec-globalisation",
            "en": "Section 1 defines Globalisation as the increasing integration and interdependence of world economies through trade, capital flows, and technology. Drivers include reduced transport container shipping costs, free trade agreements, and global internet e-commerce platforms.",
            "vi": "Mục một định nghĩa Toàn cầu hóa là sự gia tăng hội nhập và phụ thuộc lẫn nhau giữa các nền kinh tế trên thế giới qua thương mại, luân chuyển vốn và công nghệ. Các động lực chính gồm chi phí vận tải container giảm, các hiệp định thương mại tự do và sự phát triển của thương mại điện tử toàn cầu."
        },
        {
            "id": "sec_tariffs_quotas",
            "title": "2. Bảo hộ Thương mại: Thuế quan và Hạn ngạch (Tariffs & Quotas)",
            "selector": "#sec-tariffs-quotas",
            "en": "Section 2 investigates trade protectionism: Import Tariffs—taxes levied on imported foreign goods to make them more expensive than domestic products; and Import Quotas—physical quantitative ceilings on the volume of foreign goods allowed into the country.",
            "vi": "Mục hai nghiên cứu các biện pháp bảo hộ mậu dịch: Thuế quan nhập khẩu (Import Tariffs) là thuế đánh vào hàng hóa nước ngoài để làm tăng giá bán so với hàng nội địa; và Hạn ngạch nhập khẩu (Import Quotas) là giới hạn định lượng về số lượng sản phẩm nhập khẩu tối đa được phép đưa vào thị trường trong nước."
        },
        {
            "id": "sec_mncs",
            "title": "3. Tập đoàn Đa quốc gia (Multinational Corporations - MNCs)",
            "selector": "#sec-mncs",
            "en": "Section 3 examines Multinational Corporations: businesses that possess manufacturing operations or service branches in more than one country. Motives for foreign direct investment include slashing labor costs, avoiding import tariffs, and accessing local mineral resources.",
            "vi": "Mục ba xem xét các Tập đoàn đa quốc gia (MNCs): doanh nghiệp có cơ sở sản xuất hoặc chi nhánh dịch vụ tại nhiều hơn một quốc gia. Động lực đầu tư trực tiếp nước ngoài (FDI) gồm cắt giảm chi phí nhân công, vượt qua hàng rào thuế quan và tiếp cận trực tiếp nguồn tài nguyên thiên nhiên bản địa."
        },
        {
            "id": "sec_impact_host_countries",
            "title": "4. Tác động của MNCs lên Quốc gia Sở tại",
            "selector": "#sec-impact-host-countries",
            "en": "Section 4 weighs the benefits and drawbacks of MNCs on host nations. Benefits include generating employment, transferring modern industrial skills, and paying corporate taxes. Drawbacks include driving local indigenous competitors out of business, repatriating profits back to foreign headquarters, and exploiting lax environmental standards.",
            "vi": "Mục bốn cân nhắc mặt tích cực và tiêu cực của MNCs đối với nước sở tại. Mặt tích cực gồm tạo việc làm cho lao động địa phương, chuyển giao công nghệ kỹ thuật và đóng góp thuế cho ngân sách. Mặt tiêu cực gồm đè bẹp các doanh nghiệp bản địa, chuyển toàn bộ lợi nhuận về nước mẹ và khai thác lỗ hổng môi trường."
        },
        {
            "id": "sec_exchange_rates",
            "title": "5. Biến động Tỷ giá Hối đoái và Quy tắc SPICED",
            "selector": "#sec-exchange-rates",
            "en": "Section 5 analyzes exchange rate currency fluctuations using the famous Cambridge mnemonic: SPICED—Stronger Pound Imports Cheaper, Exports Dearer. A currency appreciation makes imported raw materials cheaper but reduces overseas price competitiveness for domestic exporters.",
            "vi": "Mục năm phân tích biến động tỷ giá hối đoái thông qua quy tắc ghi nhớ Cambridge SPICED: Đồng nội tệ tăng giá làm cho hàng nhập khẩu rẻ hơn nhưng hàng xuất khẩu trở nên đắt đỏ hơn. Ngược lại, đồng nội tệ giảm giá kích thích xuất khẩu nhưng làm tăng chi phí nhập khẩu nguyên liệu từ nước ngoài."
        },
        {
            "id": "sec_recommend_globalisation",
            "title": "6. Chiến lược làm bài thi Cambridge: Đánh giá Tác động của MNCs",
            "selector": "#sec-recommend-globalisation",
            "en": "Section 6 presents the Cambridge evaluation formula for globalization case studies. Candidates must balance national economic growth against sovereignty, environmental degradation, and profit repatriation before delivering a balanced final judgement.",
            "vi": "Mục sáu cung cấp công thức đánh giá toàn diện đề thi Cambridge cho các bài tập tình huống toàn cầu hóa. Thí sinh phải cân nhắc giữa lợi ích tăng trưởng kinh tế, việc làm với các nguy cơ ô nhiễm môi trường và chuyển giá lợi nhuận trước khi đưa ra nhận định tổng kết xác đáng."
        }
    ]
    
    major_sections = [
        {"id": "sec_globalisation", "title": "1. Bản chất & Động lực Toàn cầu hóa"},
        {"id": "sec_tariffs_quotas", "title": "2. Thuế quan & Hạn ngạch (Protectionism)"},
        {"id": "sec_mncs", "title": "3. Tập đoàn Đa quốc gia (MNCs)"},
        {"id": "sec_impact_host_countries", "title": "4. Tác động của MNCs lên Nước sở tại"},
        {"id": "sec_exchange_rates", "title": "5. Biến động Tỷ giá & Quy tắc SPICED"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 6.3 successfully built!")


# ==============================================================================
# MAIN BATCH RUNNER FOR TOPIC 6
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING TOPIC 6 BUILD: ALL 3 LECTURES (6.1 -> 6.3)")
    print("*******************************************************\n")
    
    await build_6_1()
    await asyncio.sleep(2)
    
    await build_6_2()
    await asyncio.sleep(2)
    
    await build_6_3()
    
    print("\n*******************************************************")
    print("TOPIC 6 COMPLETE: ALL 3 LECTURES PROCESSED SUCCESSFULLY!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
