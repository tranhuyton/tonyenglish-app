import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# LECTURE 1.2: Classification of Businesses
# ==========================================
async def build_1_2():
    lid = '7027f2e2-0ac5-4ee6-8913-7d93c7857733'
    code = '1_2'
    title = '1.2. Classification of businesses'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    t_h2_1 = '<h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏭 1. PRIMARY, SECONDARY AND TERTIARY SECTOR</h2>'
    r_h2_1 = '<h2 id="sec-sectors" class="lecture-interactive-card" data-lecture-section="sec_sectors" style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🏭 1. PRIMARY, SECONDARY AND TERTIARY SECTOR</h2>'
    
    t_basis = '<div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 18px 20px; border-radius: 6px; margin-bottom: 30px;">'
    r_basis = '<div id="card-sector-basis" class="lecture-interactive-card" data-lecture-section="card_sector_basis" style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 18px 20px; border-radius: 6px; margin-bottom: 30px; cursor: pointer;">'
    
    t_deind = '<div style="background: #f8fafc; border-left: 4px solid #64748b; padding: 20px; border-radius: 4px; font-size: 15px; color: #475569; line-height: 1.6;">'
    r_deind = '<div id="card-deindustrialisation" class="lecture-interactive-card" data-lecture-section="card_deindustrialisation" style="background: #f8fafc; border-left: 4px solid #64748b; padding: 20px; border-radius: 4px; font-size: 15px; color: #475569; line-height: 1.6; cursor: pointer;">'
    
    t_h2_2 = '<h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🤝 2. PRIVATE AND PUBLIC SECTOR IN A MIXED ECONOMY</h2>'
    r_h2_2 = '<h2 id="sec-mixed-economy" class="lecture-interactive-card" data-lecture-section="sec_mixed_economy" style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🤝 2. PRIVATE AND PUBLIC SECTOR IN A MIXED ECONOMY</h2>'
    
    t_pubpriv = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 25px;">'
    r_pubpriv = '<div id="card-private-public-sector" class="lecture-interactive-card" data-lecture-section="card_private_public_sector" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 25px; cursor: pointer;">'

    new_html = html.replace(t_header, r_header, 1).replace(t_h2_1, r_h2_1, 1).replace(t_basis, r_basis, 1).replace(t_deind, r_deind, 1).replace(t_h2_2, r_h2_2, 1).replace(t_pubpriv, r_pubpriv, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1.2: Phân loại Doanh nghiệp",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.2: Classification of Businesses. In this lesson, we examine how economies are structured into primary, secondary, and tertiary stages of production, explore the structural shift known as de-industrialisation, and compare private versus public sector ownership in mixed economies.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.2: Phân loại Doanh nghiệp. Trong bài học này, chúng ta sẽ tìm hiểu cơ cấu nền kinh tế qua ba khu vực sản xuất: sơ cấp, thứ cấp và tam cấp, hiện tượng phi công nghiệp hóa trong các nền kinh tế phát triển, và so sánh vai trò giữa khu vực tư nhân và khu vực nhà nước trong nền kinh tế hỗn hợp."
        },
        {
            "id": "sec_sectors",
            "title": "1. Ba khu vực kinh tế: Sơ cấp, Thứ cấp và Tam cấp",
            "selector": "#sec-sectors",
            "en": "Section 1 classifies economic activities into three progressive stages. The primary sector extracts and harvests natural resources, such as farming, fishing, forestry, and mining. The secondary sector processes, manufactures, and constructs tangible goods from raw materials. The tertiary sector provides commercial and personal services, including banking, transportation, retail, healthcare, and education.",
            "vi": "Mục một phân loại hoạt động kinh tế thành ba khu vực kế tiếp nhau. Khu vực sơ cấp (primary sector) khai thác tài nguyên thiên nhiên như nông nghiệp, đánh bắt thủy sản, lâm nghiệp và khai khoáng. Khu vực thứ cấp (secondary sector) chế biến và sản xuất hàng hóa vật chất từ nguyên liệu thô. Khu vực tam cấp (tertiary sector) cung cấp các dịch vụ thương mại và cá nhân, bao gồm ngân hàng, vận tải, bán lẻ, y tế và giáo dục."
        },
        {
            "id": "card_sector_basis",
            "title": "Cơ sở phân loại và Chuỗi giá trị kinh tế",
            "selector": "#card-sector-basis",
            "en": "Economists measure the relative importance of these three sectors through two key metrics: the percentage of total national employment in each sector, and the proportion of total output contributing to Gross Domestic Product. All three sectors are deeply interdependent, forming an integrated supply chain that takes raw materials from the earth through factories to retail shelves.",
            "vi": "Các nhà kinh tế đo lường tầm quan trọng của ba khu vực này dựa trên hai chỉ số chính: tỷ lệ việc làm trong từng khu vực và tỷ trọng đóng góp vào Tổng sản phẩm quốc nội (GDP). Cả ba khu vực đều có mối quan hệ phụ thuộc lẫn nhau chặt chẽ, tạo thành chuỗi cung ứng khép kín từ khâu khai thác tài nguyên, qua nhà máy chế tạo đến kệ hàng bán lẻ."
        },
        {
            "id": "card_deindustrialisation",
            "title": "Quá trình phi công nghiệp hóa (De-industrialisation)",
            "selector": "#card-deindustrialisation",
            "en": "Over time, economic development alters the balance between sectors. In developed high-income nations, de-industrialisation occurs as manufacturing employment declines while service sector jobs expand. This structural shift is driven by depletion of domestic raw materials, rising local wage rates causing factories to relocate to lower-cost emerging economies, and rising consumer disposable incomes spent increasingly on travel, leisure, and financial services.",
            "vi": "Theo thời gian, phát triển kinh tế làm thay đổi cán cân giữa các khu vực. Tại các quốc gia phát triển, quá trình phi công nghiệp hóa (de-industrialisation) diễn ra khi việc làm trong ngành sản xuất sụt giảm và dịch vụ tăng vọt. Sự dịch chuyển này bắt nguồn từ sự cạn kiệt tài nguyên thô, chi phí nhân công trong nước tăng khiến nhà máy chuyển dịch sang các nước đang phát triển, và thu nhập khả dụng tăng thúc đẩy người dân chi tiêu nhiều hơn cho du lịch, giải trí và dịch vụ tài chính."
        },
        {
            "id": "sec_mixed_economy",
            "title": "2. Nền kinh tế hỗn hợp (Mixed Economy)",
            "selector": "#sec-mixed-economy",
            "en": "Section 2 explores mixed economies, where resources are allocated by both market forces and government intervention. In a pure market economy, all resources are privately owned; in a command economy, the state controls all production. Modern nations operate as mixed economies to capture the efficiency of private enterprise while protecting public welfare through state-funded infrastructure and essential services.",
            "vi": "Mục hai khám phá nền kinh tế hỗn hợp, nơi nguồn lực được phân bổ bởi cả cơ chế thị trường và sự can thiệp của chính phủ. Trong nền kinh tế thị trường thuần túy, mọi nguồn lực do tư nhân sở hữu; ngược lại trong nền kinh tế chỉ huy, nhà nước kiểm soát toàn bộ. Các quốc gia hiện đại đều áp dụng mô hình kinh tế hỗn hợp nhằm tận dụng tính năng động của doanh nghiệp tư nhân, đồng thời bảo đảm an sinh xã hội qua các dịch vụ công thiết yếu."
        },
        {
            "id": "card_private_public_sector",
            "title": "So sánh Khu vực Tư nhân và Khu vực Nhà nước",
            "selector": "#card-private-public-sector",
            "en": "In the private sector, businesses are owned by private individuals, partners, or shareholders, with primary aims of profitability, growth, and market share. In contrast, the public sector is owned and managed by the government, financed through taxation, and focuses on social equity, universal accessibility, and public healthcare. When governments sell state-owned enterprises to private investors, this process is called privatisation.",
            "vi": "Trong khu vực tư nhân, doanh nghiệp thuộc sở hữu của các cá nhân hoặc cổ đông, với mục tiêu hàng đầu là lợi nhuận, tăng trưởng và thị phần. Ngược lại, khu vực nhà nước thuộc sở hữu của chính phủ, vận hành bằng tiền thuế và hướng tới mục tiêu phục vụ cộng đồng, duy trì giá cả hợp lý và bảo đảm an sinh xã hội. Quá trình chính phủ bán các doanh nghiệp nhà nước cho các nhà đầu tư tư nhân được gọi là tư nhân hóa (privatisation)."
        }
    ]
    
    major_sections = [
        {"id": "sec_sectors", "title": "1. Ba khu vực kinh tế"},
        {"id": "sec_mixed_economy", "title": "2. Khu vực Tư nhân và Nhà nước trong Nền kinh tế hỗn hợp"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 1.2 successfully built!")

if __name__ == "__main__":
    asyncio.run(build_1_2())
