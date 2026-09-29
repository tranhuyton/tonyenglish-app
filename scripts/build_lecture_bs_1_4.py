import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ========================================================
# LECTURE 1.4: Types of business organisation
# ========================================================
async def build_1_4():
    lid = '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0'
    code = '1_4'
    title = '1.4. Types of business organisation'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    t_h2_1 = '<h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">👤 1. SOLE TRADER / SOLE PROPRIETORSHIP</h2>'
    r_h2_1 = '<h2 id="sec-sole-trader" class="lecture-interactive-card" data-lecture-section="sec_sole_trader" style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">👤 1. SOLE TRADER / SOLE PROPRIETORSHIP</h2>'
    
    t_h2_2 = '<h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🤝 2. PARTNERSHIPS</h2>'
    r_h2_2 = '<h2 id="sec-partnerships" class="lecture-interactive-card" data-lecture-section="sec_partnerships" style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🤝 2. PARTNERSHIPS</h2>'
    
    t_h2_3 = '<h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏢 3. JOINT-STOCK COMPANIES</h2>'
    r_h2_3 = '<h2 id="sec-companies" class="lecture-interactive-card" data-lecture-section="sec_companies" style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🏢 3. JOINT-STOCK COMPANIES</h2>'
    
    t_h2_4 = '<h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🍔 4. FRANCHISES</h2>'
    r_h2_4 = '<h2 id="sec-franchises" class="lecture-interactive-card" data-lecture-section="sec_franchises" style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🍔 4. FRANCHISES</h2>'
    
    t_h2_5 = '<h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🚀 5. JOINT VENTURES</h2>'
    r_h2_5 = '<h2 id="sec-joint-ventures" class="lecture-interactive-card" data-lecture-section="sec_joint_ventures" style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🚀 5. JOINT VENTURES</h2>'
    
    t_h2_6 = '<h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0;">🏛️ 6. PUBLIC SECTOR CORPORATIONS</h2>'
    r_h2_6 = '<h2 id="sec-public-corporations" class="lecture-interactive-card" data-lecture-section="sec_public_corporations" style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 15px; margin-bottom: 25px; display: inline-block; font-size: 26px; line-height: 1.2; margin-top: 0; cursor: pointer;">🏛️ 6. PUBLIC SECTOR CORPORATIONS</h2>'
    
    soup = BeautifulSoup(html, 'html.parser')
    h2_7 = soup.find_all('h2')[6]
    t_h2_7 = str(h2_7)
    r_h2_7 = t_h2_7.replace('<h2', '<h2 id="sec-exam-recommendation" class="lecture-interactive-card" data-lecture-section="sec_exam_recommendation" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1).replace(t_h2_1, r_h2_1, 1).replace(t_h2_2, r_h2_2, 1).replace(t_h2_3, r_h2_3, 1).replace(t_h2_4, r_h2_4, 1).replace(t_h2_5, r_h2_5, 1).replace(t_h2_6, r_h2_6, 1).replace(t_h2_7, r_h2_7, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1.4: Các loại hình tổ chức doanh nghiệp",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.4: Types of Business Organisation. In this pivotal lesson, we examine the legal structures available to commercial enterprises: sole traders, partnerships, private limited companies (Ltd), public limited companies (Plc), franchises, joint ventures, and public sector corporations.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.4: Các loại hình tổ chức doanh nghiệp. Trong bài học then chốt này, chúng ta sẽ khảo sát các hình thức pháp lý của doanh nghiệp: doanh nghiệp tư nhân, công ty hợp danh, công ty trách nhiệm hữu hạn tư nhân (Ltd), công ty đại chúng (Plc), nhượng quyền thương mại, liên doanh và các tổng công ty nhà nước."
        },
        {
            "id": "sec_sole_trader",
            "title": "1. Doanh nghiệp tư nhân (Sole Trader)",
            "selector": "#sec-sole-trader",
            "en": "Section 1 analyzes the sole trader structure. Owned and managed by a single individual, sole proprietorships offer total autonomy, simple statutory establishment, and complete retention of profits. However, the crucial legal disadvantage is unlimited liability: the owner is personally responsible for all business debts, placing private assets like houses and vehicles at risk if the business becomes insolvent.",
            "vi": "Mục một phân tích loại hình doanh nghiệp tư nhân (sole trader). Do một cá nhân sở hữu và điều hành, loại hình này mang lại quyền tự quyết tuyệt đối, thủ tục thành lập đơn giản và hưởng trọn lợi nhuận. Tuy nhiên, bất lợi pháp lý lớn nhất là chế độ trách nhiệm vô hạn (unlimited liability): chủ sở hữu phải chịu trách nhiệm bằng toàn bộ tài sản cá nhân cho các khoản nợ của doanh nghiệp nếu phá sản."
        },
        {
            "id": "sec_partnerships",
            "title": "2. Công ty hợp danh (Partnerships)",
            "selector": "#sec-partnerships",
            "en": "Section 2 examines partnerships, formed between two and twenty individuals under a formal Deed of Partnership. Partnerships inject greater capital, share workloads, and combine complementary professional expertise. Yet, partners typically share joint and several unlimited liability, and business continuity is legally dissolved if any partner resigns or passes away.",
            "vi": "Mục hai tìm hiểu về công ty hợp danh (partnerships), được thành lập giữa 2 đến 20 thành viên dựa trên Hợp đồng hợp danh (Deed of Partnership). Công ty hợp danh giúp huy động nguồn vốn lớn hơn, chia sẻ khối lượng công việc và kết hợp chuyên môn đa dạng. Dù vậy, các thành viên vẫn phải chịu trách nhiệm vô hạn liên đới, và doanh nghiệp có nguy cơ giải thể nếu một thành viên rút vốn hoặc qua đời."
        },
        {
            "id": "sec_companies",
            "title": "3. Công ty cổ phần (Joint-Stock Companies)",
            "selector": "#sec-companies",
            "en": "Section 3 introduces joint-stock companies. Unlike unincorporated entities, companies possess separate legal personality from their owners and offer limited liability, meaning shareholders risk only their invested share capital. Private limited companies (Ltd) sell shares privately with existing shareholder consent, preventing hostile takeovers, whereas Public Limited Companies (Plc) trade shares publicly on the stock exchange, raising colossal capital but exposing the firm to hostile acquisition.",
            "vi": "Mục ba giới thiệu về công ty cổ phần. Khác với doanh nghiệp tư nhân, công ty cổ phần có tư cách pháp nhân độc lập và chế độ trách nhiệm hữu hạn (limited liability), bảo vệ an toàn tài sản cá nhân của cổ đông. Công ty TNHH tư nhân (Ltd) chỉ bán cổ phần nội bộ để tránh nguy cơ bị thâu tóm, trong khi Công ty cổ phần đại chúng (Plc) niêm yết tự do trên sàn chứng khoán, huy động vốn cực lớn nhưng đối mặt nguy cơ bị thâu tóm thù địch."
        },
        {
            "id": "sec_franchises",
            "title": "4. Nhượng quyền thương mại (Franchises)",
            "selector": "#sec-franchises",
            "en": "Section 4 investigates the franchise business model. A franchisor licenses a proven commercial brand, recipes, and operational systems to an independent franchisee in exchange for upfront license fees and ongoing management royalties. Franchisees gain immediate brand recognition and head-office support, but must surrender operational flexibility and accept strict brand conformity.",
            "vi": "Mục bốn phân tích mô hình nhượng quyền thương mại (franchise). Bên nhượng quyền (franchisor) cấp phép thương hiệu, công thức và quy trình vận hành cho bên nhận quyền (franchisee) để thu phí nhượng quyền ban đầu và phần trăm doanh thu định kỳ. Bên nhận quyền được thừa hưởng uy tín thương hiệu ngay từ ngày đầu, nhưng bị ràng buộc nghiêm ngặt và không có quyền tự ý thay đổi sản phẩm."
        },
        {
            "id": "sec_joint_ventures",
            "title": "5. Doanh nghiệp Liên doanh (Joint Ventures)",
            "selector": "#sec-joint-ventures",
            "en": "Section 5 explores joint ventures—formal collaborations where two or more independent corporations launch a joint project, sharing capital investment, operational risks, and profits. Joint ventures are widely deployed when Western multinationals enter foreign markets, partnering with indigenous domestic firms to navigate local legal regulations, distribution channels, and cultural nuances.",
            "vi": "Mục năm tìm hiểu về doanh nghiệp liên doanh (joint ventures) – sự hợp tác chính thức giữa hai hay nhiều tập đoàn độc lập nhằm thực hiện một dự án chung, cùng chia sẻ vốn đầu tư, rủi ro và lợi nhuận. Liên doanh thường được các tập đoàn đa quốc gia áp dụng khi thâm nhập thị trường nước ngoài bằng cách bắt tay với doanh nghiệp bản địa để nắm vững luật pháp và thị hiếu địa phương."
        },
        {
            "id": "sec_public_corporations",
            "title": "6. Tổng công ty Nhà nước (Public Sector Corporations)",
            "selector": "#sec-public-corporations",
            "en": "Section 6 examines public sector corporations, fully owned by the state and funded through the national treasury. These entities operate vital strategic infrastructure such as national railways, water utilities, and postal networks, where natural monopolies exist, prioritizing universal affordability and equitable service over short-term commercial profits.",
            "vi": "Mục sáu xem xét các tổng công ty nhà nước (public sector corporations), thuộc sở hữu nhà nước và cấp vốn từ ngân sách quốc gia. Các tổ chức này quản lý cơ sở hạ tầng chiến lược như đường sắt, mạng lưới cấp nước và bưu chính quốc gia – những lĩnh vực có tính chất độc quyền tự nhiên, ưu tiên phục vụ cộng đồng và giá cả ổn định hơn là chạy theo lợi nhuận trước mắt."
        },
        {
            "id": "sec_exam_recommendation",
            "title": "7. Chiến lược làm bài thi Cambridge: Đề xuất loại hình doanh nghiệp",
            "selector": "#sec-exam-recommendation",
            "en": "Section 7 details the Cambridge Exam Justification Formula for evaluation questions. When recommending a business structure, candidates must balance capital requirements, the owner's risk appetite regarding unlimited liability, the desired degree of operational secrecy, and the potential threat of losing control. Always evaluate the trade-offs in context before delivering a justified recommendation.",
            "vi": "Mục bảy hướng dẫn công thức biện minh chuẩn Cambridge cho các câu hỏi đánh giá. Khi đề xuất loại hình doanh nghiệp, học sinh cần cân nhắc nhu cầu vốn, mức độ chấp nhận rủi ro trách nhiệm vô hạn của chủ sở hữu, mức độ bảo mật báo cáo tài chính và nguy cơ mất quyền kiểm soát. Luôn phân tích ưu nhược điểm gắn liền với ngữ cảnh tình huống trước khi đưa ra kết luận thuyết phục."
        }
    ]
    
    major_sections = [
        {"id": "sec_sole_trader", "title": "1. Doanh nghiệp tư nhân (Sole Trader)"},
        {"id": "sec_partnerships", "title": "2. Công ty hợp danh (Partnerships)"},
        {"id": "sec_companies", "title": "3. Công ty cổ phần (Joint-Stock Companies)"},
        {"id": "sec_franchises", "title": "4. Nhượng quyền thương mại (Franchises)"},
        {"id": "sec_joint_ventures", "title": "5. Doanh nghiệp Liên doanh (Joint Ventures)"},
        {"id": "sec_public_corporations", "title": "6. Tổng công ty Nhà nước"},
        {"id": "sec_exam_recommendation", "title": "7. Chiến lược đề xuất loại hình doanh nghiệp"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 1.4 successfully built!")

if __name__ == "__main__":
    asyncio.run(build_1_4())
