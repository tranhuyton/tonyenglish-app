import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 1.4 ID
LID = '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0'
CODE = '1_4'
TITLE = '1.4 Types of business organisation'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 19 AUDIO SEGMENTS FOR LESSON 1.4
# ==============================================================================
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
        "title": "1. Doanh nghiệp Tư nhân (Sole Trader)",
        "selector": "#sec-sole-trader",
        "en": "Section 1 examines the sole trader, also known as a sole proprietorship. This is a business owned, financed, and controlled by a single individual. Although a sole trader can hire employees, the owner assumes all legal and financial liabilities personally.",
        "vi": "Mục 1 tìm hiểu về doanh nghiệp tư nhân (Sole Trader). Đây là hình thức kinh doanh do một cá nhân duy nhất bỏ vốn thành lập, quản lý và sở hữu toàn bộ. Mặc dù chủ doanh nghiệp tư nhân có thể thuê nhân viên làm việc, nhưng họ phải tự gánh vác mọi trách nhiệm pháp lý và tài chính."
    },
    {
        "id": "card_sole_trader_adv",
        "title": "✅ Ưu điểm của Doanh nghiệp Tư nhân",
        "selector": "#card-sole-trader-adv",
        "en": "Sole traders enjoy four major advantages: minimal setup costs with few legal formalities, total autonomy in rapid decision-making, retention of 100% of earned profits, and close personalized contact with customers fostering intense brand loyalty.",
        "vi": "Doanh nghiệp tư nhân có 4 ưu điểm nổi bật: thủ tục thành lập nhanh gọn và chi phí thấp, toàn quyền tự quyết định linh hoạt không cần hội ý, được hưởng trọn vẹn 100% lợi nhuận làm ra, và duy trì mối quan hệ chăm sóc khách hàng gần gũi giúp xây dựng lòng trung thành thương hiệu."
    },
    {
        "id": "card_sole_trader_disadv",
        "title": "❌ Nhược điểm của Doanh nghiệp Tư nhân (Unlimited Liability)",
        "selector": "#card-sole-trader-disadv",
        "en": "The critical drawback of a sole trader is unlimited liability: because the business is unincorporated, personal assets such as houses and savings can be seized by court order to pay company debts. Additional limitations include full operational workload on one person, difficulty raising bank loans, and total lack of business continuity if the owner retires or passes away.",
        "vi": "Bất lợi nghiêm trọng nhất của doanh nghiệp tư nhân là trách nhiệm vô hạn (unlimited liability): do doanh nghiệp không có tư cách pháp nhân tách rời, tài sản cá nhân như nhà cửa và tiền tiết kiệm của chủ sở hữu có thể bị tịch thu để trả nợ. Ngoài ra còn có gánh nặng công việc dồn lên một người, khó vay vốn ngân hàng lớn và không có tính kế thừa liên tục nếu chủ sở hữu nghỉ hưu hoặc qua đời."
    },
    {
        "id": "sec_partnerships",
        "title": "2. Công ty Hợp danh (Partnerships)",
        "selector": "#sec-partnerships",
        "en": "Section 2 investigates partnerships. A partnership is a formal legal agreement between two or more people, typically up to twenty partners, who agree to jointly own, finance, and operate a business and share profits according to a deed of partnership.",
        "vi": "Mục 2 phân tích về công ty hợp danh (Partnership). Hợp danh là sự thỏa thuận pháp lý giữa từ hai người trở lên, thông thường tối đa 20 thành viên, cùng nhau góp vốn, quản trị doanh nghiệp và phân chia lợi nhuận theo hợp đồng hợp danh."
    },
    {
        "id": "card_partnerships_adv",
        "title": "✅ Ưu điểm của Công ty Hợp danh",
        "selector": "#card-partnerships-adv",
        "en": "Partnerships offer clear benefits over sole traders: more capital can be invested by pooling resources, diverse specialist skills and management ideas are brought together, and workloads and operational responsibilities are shared among partners.",
        "vi": "Công ty hợp danh có nhiều ưu thế so với doanh nghiệp tư nhân: huy động được nhiều vốn hơn từ sự đóng góp của các thành viên, kết hợp được nhiều kỹ năng chuyên môn và ý tưởng quản trị đa dạng, đồng thời khối lượng công việc và trách nhiệm điều hành được san sẻ."
    },
    {
        "id": "card_partnerships_disadv",
        "title": "❌ Nhược điểm của Công ty Hợp danh",
        "selector": "#card-partnerships-disadv",
        "en": "However, ordinary partnerships still carry unlimited liability for all partners. Serious disputes can paralyze decision-making, decisions made by one partner legally bind all others, capital remains limited compared to companies, and the partnership legally dissolves if any partner departs.",
        "vi": "Tuy nhiên, công ty hợp danh thông thường vẫn chịu trách nhiệm vô hạn cho tất cả thành viên. Những bất đồng quan điểm có thể làm đình trệ việc ra quyết định, quyết định của một thành viên có giá trị ràng buộc trách nhiệm lên toàn bộ các thành viên khác, vốn vẫn hạn chế so với công ty cổ phần, và công ty sẽ phải giải thể nếu một thành viên rút lui hoặc qua đời."
    },
    {
        "id": "card_unincorp_vs_incorp",
        "title": "⚖️ So sánh Doanh nghiệp Chưa có Pháp nhân & Có Tư cách Pháp nhân",
        "selector": "#card-unincorp-vs-incorp",
        "en": "A fundamental Cambridge distinction is between unincorporated entities (sole traders and partnerships) and incorporated companies (Ltd and Plc). Incorporated companies possess a separate legal identity, meaning the company can own property, sign contracts, and be sued in its own name. Crucially, shareholders enjoy limited liability, risking only their invested share capital while personal assets remain 100% protected, and enjoy perpetual continuity.",
        "vi": "Một phân định nền tảng trong giáo trình Cambridge là giữa doanh nghiệp chưa có tư cách pháp nhân (doanh nghiệp tư nhân, hợp danh) và doanh nghiệp có tư cách pháp nhân độc lập (công ty Ltd và Plc). Công ty có tư cách pháp nhân là một chủ thể pháp lý độc lập tách biệt với các chủ sở hữu, có quyền đứng tên tài sản, ký hợp đồng và chịu kiện tụng. Quan trọng nhất, các cổ đông được hưởng trách nhiệm hữu hạn, chỉ chịu rủi ro trong phạm vi số tiền mua cổ phần và tài sản cá nhân được bảo vệ tuyệt đối, cùng tính hoạt động liên tục không phụ thuộc vào đời sống của người sáng lập."
    },
    {
        "id": "sec_companies",
        "title": "3. Công ty Cổ phần (Joint-Stock Companies)",
        "selector": "#sec-companies",
        "en": "Section 3 examines joint-stock companies. Companies raise capital by issuing shares of ownership. Those who buy shares become shareholders, earning periodic dividend payments from company profits and electing a Board of Directors to supervise executive management.",
        "vi": "Mục 3 tìm hiểu về các công ty cổ phần. Doanh nghiệp huy động vốn bằng cách phát hành các cổ phần sở hữu. Những người mua cổ phần trở thành cổ đông, nhận cổ tức định kỳ từ lợi nhuận của công ty và bầu ra Hội đồng quản trị để giám sát ban điều hành."
    },
    {
        "id": "card_company_ltd",
        "title": "🔒 Công ty TNHH Tư nhân (Private Limited Company - Ltd)",
        "selector": "#card-company-ltd",
        "en": "A Private Limited Company (Ltd) is owned by shareholders who can sell shares only to people known to existing owners, such as family and close associates. Shares cannot be sold to the general public or traded on a stock exchange, keeping control tightly concentrated in family or private hands.",
        "vi": "Công ty TNHH Tư nhân (Private Limited Company - Ltd) thuộc sở hữu của các cổ đông chỉ được phép chuyển nhượng hoặc bán cổ phần cho những người quen biết như người thân trong gia đình hoặc đối tác thân thiết. Cổ phần không được chào bán ra công chúng và không được niêm yết trên sàn chứng khoán, giúp quyền kiểm soát luôn nằm chắc trong tay nhóm sáng lập."
    },
    {
        "id": "card_company_plc",
        "title": "🌐 Công ty Cổ phần Đại chúng (Public Limited Company - Plc)",
        "selector": "#card-company-plc",
        "en": "A Public Limited Company (Plc) is authorized to sell shares to the general public and financial institutions via recognized stock exchanges. This enables Plcs to raise colossal sums of equity capital to fund global expansion, but subjects them to intense regulatory scrutiny.",
        "vi": "Công ty Cổ phần Đại chúng (Public Limited Company - Plc) được phép chào bán cổ phần rộng rãi cho công chúng và các quỹ tài chính thông qua thị trường chứng khoán. Điều này giúp các công ty đại chúng huy động được những nguồn vốn khổng lồ để bành trướng quy mô toàn cầu, nhưng đổi lại phải chịu sự giám sát pháp lý vô cùng nghiêm ngặt."
    },
    {
        "id": "card_company_adv",
        "title": "✅ Ưu điểm của Công ty Cổ phần",
        "selector": "#card-company-adv",
        "en": "Companies offer immense strategic strengths: limited liability safeguards shareholder wealth, massive capital can be raised to finance large-scale operations, perpetual continuity ensures long-term survival, and professional directors and specialized executives can be hired.",
        "vi": "Các công ty cổ phần mang lại những thế mạnh chiến lược vượt bậc: trách nhiệm hữu hạn bảo vệ an toàn tài sản cho cổ đông, khả năng huy động vốn khổng lồ để tài trợ sản xuất quy mô lớn, tính trường tồn vĩnh cửu bảo đảm hoạt động lâu dài, và dễ dàng thuê các giám đốc điều hành chuyên nghiệp có trình độ cao."
    },
    {
        "id": "card_company_disadv",
        "title": "❌ Nhược điểm của Công ty Cổ phần",
        "selector": "#card-company-disadv",
        "en": "Drawbacks include complex and expensive legal incorporation procedures, mandatory disclosure of detailed annual financial accounts to the public, high costs of hosting Annual General Meetings, and in Plcs, the risk of divorce of ownership from control where professional managers pursue goals different from shareholder interests.",
        "vi": "Nhược điểm bao gồm thủ tục pháp lý thành lập phức tạp và tốn kém, bắt buộc phải công khai báo cáo tài chính kiểm toán chi tiết hàng năm ra công chúng, chi phí tổ chức Đại hội đồng cổ đông thường niên tốn kém, và ở các công ty đại chúng dễ phát sinh tình trạng phân ly giữa quyền sở hữu và quyền quản lý, khi ban điều hành theo đuổi các mục tiêu cá nhân khác với kỳ vọng của cổ đông."
    },
    {
        "id": "sec_franchises",
        "title": "4. Nhượng quyền Thương mại (Franchises)",
        "selector": "#sec-franchises",
        "en": "Section 4 covers franchising. A franchise agreement exists when an established brand owner, the franchisor, licenses an independent operator, the franchisee, to trade under its brand name, business format, and trademark in exchange for initial fees and ongoing royalties.",
        "vi": "Mục 4 phân tích mô hình nhượng quyền thương mại (Franchising). Nhượng quyền là hợp đồng pháp lý trong đó chủ sở hữu thương hiệu (Franchisor) cấp phép cho một cá nhân hoặc đơn vị kinh doanh độc lập (Franchisee) được quyền sử dụng thương hiệu, mô hình kinh doanh và bí quyết sản phẩm để buôn bán tại một khu vực nhất định để đổi lấy phí nhượng quyền và phí bản quyền định kỳ."
    },
    {
        "id": "card_franchisor",
        "title": "👑 Lợi ích & Thách thức đối với Bên Nhượng quyền (Franchisor)",
        "selector": "#card-franchisor",
        "en": "To the franchisor, advantages include rapid business expansion with minimal capital investment and steady royalty income. However, drawbacks include sharing profits with franchisees, potential loss of direct operational control, and the catastrophic risk that one substandard outlet damages the worldwide reputation of the brand.",
        "vi": "Đối với bên nhượng quyền (Franchisor), ưu điểm là bành trướng mạng lưới cực nhanh mà không phải tự bỏ vốn đầu tư mặt bằng, cùng dòng tiền bản quyền đều đặn. Tuy nhiên, nhược điểm là phải chia sẻ lợi nhuận, giảm bớt quyền kiểm soát trực tiếp và rủi ro nghiêm trọng khi một cửa hàng nhượng quyền làm ăn cẩu thả có thể phá hủy uy tín của toàn bộ hệ thống thương hiệu."
    },
    {
        "id": "card_franchisee",
        "title": "🏪 Lợi ích & Thách thức đối với Bên Nhận quyền (Franchisee)",
        "selector": "#card-franchisee",
        "en": "To the franchisee, advantages include launching with a globally recognized brand with low failure risk, receiving comprehensive staff training and equipment support, and secure raw material supplies. Disadvantages include steep initial setup fees, ongoing royalty payments, and lack of creative freedom due to strict franchisor operating manuals.",
        "vi": "Đối với bên nhận quyền (Franchisee), lợi thế là được kinh doanh một thương hiệu nổi tiếng đã được kiểm chứng nên tỷ lệ thất bại rất thấp, được hỗ trợ đào tạo bài bản và cung ứng nguyên vật liệu tận nơi. Ngược lại, điểm bất lợi là chi phí mua quyền kinh doanh ban đầu rất đắt đỏ, phải trích phần trăm doanh thu trả tiền bản quyền liên tục và không có quyền tự do sáng tạo do phải tuân thủ nghiêm ngặt quy trình chuẩn mực."
    },
    {
        "id": "sec_joint_ventures",
        "title": "5. Liên doanh Thương mại (Joint Ventures)",
        "selector": "#sec-joint-ventures",
        "en": "Section 5 discusses joint ventures. A joint venture occurs when two or more independent businesses collaborate on a specific commercial project while retaining their separate corporate identities. Joint ventures allow firms to share immense capital costs and operational risks, and combine technical strengths with local market cultural expertise, although disagreements over leadership styles can create conflict.",
        "vi": "Mục 5 trình bày về hình thức liên doanh (Joint Venture). Liên doanh diễn ra khi hai hoặc nhiều doanh nghiệp độc lập bắt tay hợp tác cùng thực hiện một dự án kinh doanh cụ thể nhưng vẫn giữ nguyên tư cách pháp nhân riêng rẽ. Liên doanh giúp chia sẻ chi phí đầu tư khổng lồ và rủi ro, kết hợp thế mạnh công nghệ với sự am hiểu thị trường bản địa, mặc dù sự khác biệt về văn hóa doanh nghiệp có thể nảy sinh xung đột quản lý."
    },
    {
        "id": "sec_public_corporations",
        "title": "6. Tổng công ty Khu vực Nhà nước (Public Sector Corporations)",
        "selector": "#sec-public-corporations",
        "en": "Section 6 highlights public sector corporations. These are enterprises owned and operated by the government to provide essential national infrastructure such as railways, clean water, and healthcare. Main aims are keeping consumer prices affordable, maintaining universal access, and safeguarding employment, although government subsidies and lack of competition can foster operational inefficiency.",
        "vi": "Mục 6 khái quát các tổng công ty thuộc khu vực nhà nước. Đây là các doanh nghiệp do chính phủ sở hữu và vận hành nhằm cung ứng các hạ tầng và tiện ích quốc gia trọng yếu như đường sắt, nước sạch và chăm sóc y tế. Mục tiêu chính là duy trì giá cả phải chăng cho mọi người dân, bảo đảm phục vụ toàn diện và duy trì việc làm ổn định, mặc dù sự bảo hộ ngân sách và thiếu vắng cạnh tranh có thể dẫn đến sự trì trệ trong vận hành."
    },
    {
        "id": "sec_exam_recommendation",
        "title": "🎯 7. Chiến lược Đề thi: Lựa chọn & Biện minh Loại hình Doanh nghiệp",
        "selector": "#sec-exam-recommendation",
        "en": "Section 7 synthesizes the Cambridge exam strategy for choosing the optimal business organisation. When advising entrepreneurs, evaluate four core determinants: capital requirements, degree of risk and liability, desire for managerial control, and the scale of the target market. Sole traders suit small localized services; partnerships suit complementary professional practices; private limited companies protect growing family firms; and public limited companies enable massive industrial expansion.",
        "vi": "Mục 7 đúc kết chiến lược làm bài thi Cambridge về việc đề xuất và biện minh cho loại hình doanh nghiệp tối ưu. Khi tư vấn cho doanh nhân, hãy đánh giá 4 yếu tố trọng tâm: nhu cầu về vốn, mức độ rủi ro và trách nhiệm pháp lý, mong muốn kiểm soát quyền lực, và quy mô thị trường mục tiêu. Doanh nghiệp tư nhân phù hợp với dịch vụ nhỏ tại chỗ; hợp danh lý tưởng cho văn phòng chuyên môn phối hợp; công ty TNHH tư nhân bảo vệ doanh nghiệp gia đình đang phát triển; và công ty đại chúng mở đường cho sự bành trướng quy mô lớn trên toàn cầu."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_sole_trader": {"start": 1, "end": 3},
    "sec_partnerships": {"start": 4, "end": 6},
    "card_unincorp_vs_incorp": {"start": 7, "end": 7},
    "sec_companies": {"start": 8, "end": 12},
    "sec_franchises": {"start": 13, "end": 15},
    "sec_joint_ventures": {"start": 16, "end": 16},
    "sec_public_corporations": {"start": 17, "end": 17},
    "sec_exam_recommendation": {"start": 18, "end": 18}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.4 Types of Business Organisation (Các loại hình tổ chức doanh nghiệp)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. SOLE TRADER -->
    <div style="margin-bottom: 45px;">
        <div id="sec-sole-trader" class="lecture-interactive-card" data-lecture-section="sec_sole_trader" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">👤 1. SOLE TRADER / SOLE PROPRIETORSHIP</h2>
            <div style="background: #eff6ff; border-left: 5px solid #3b82f6; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #1e40af; line-height: 1.6;">
                A business organization <b>owned, financed, and controlled by one person</b>. Sole traders can employ other workers, but only the owner invests capital, reaps the rewards, and takes the risks.
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-sole-trader-adv" class="lecture-interactive-card" data-lecture-section="card_sole_trader_adv" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #15803d; font-size: 18px; margin: 0 0 12px 0;">✅ Advantages of a Sole Trader</h4>
                <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 14px; line-height: 1.6;">
                    <li><b>Easy to set up:</b> Very few legal formalities; minimal initial capital needed.</li>
                    <li><b>Total control:</b> Quick decisions without consulting partners or shareholders.</li>
                    <li><b>Keeps all profit:</b> 100% of profit goes directly to the sole proprietor.</li>
                    <li><b>Personal customer service:</b> Builds close, long-lasting client relationships.</li>
                    <li><b>Privacy:</b> No legal obligation to publish annual financial accounts.</li>
                </ul>
            </div>

            <div id="card-sole-trader-disadv" class="lecture-interactive-card" data-lecture-section="card_sole_trader_disadv" style="background: #fef2f2; border: 1.5px solid #fecaca; border-left: 5px solid #dc2626; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #b91c1c; font-size: 18px; margin: 0 0 12px 0;">❌ Disadvantages (Unlimited Liability)</h4>
                <ul style="margin: 0; padding-left: 20px; color: #991b1b; font-size: 14px; line-height: 1.6;">
                    <li><b>Unlimited liability:</b> Personal assets (home, car) can be seized to pay debts.</li>
                    <li><b>Limited capital:</b> Low borrowing power from banks restricts expansion.</li>
                    <li><b>Heavy workload:</b> Sole owner handles accounts, purchasing, and marketing.</li>
                    <li><b>No continuity:</b> Business dissolves if the owner retires or dies.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 2. PARTNERSHIPS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-partnerships" class="lecture-interactive-card" data-lecture-section="sec_partnerships" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🤝 2. PARTNERSHIPS</h2>
            <div style="background: #f5f3ff; border-left: 5px solid #7c3aed; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #4c1d95; line-height: 1.6;">
                A partnership is a legal agreement between <b>two or more people (usually up to 20)</b> to jointly own, finance, and operate a business venture and share profits under a <i>Deed of Partnership</i>.
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-partnerships-adv" class="lecture-interactive-card" data-lecture-section="card_partnerships_adv" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #15803d; font-size: 18px; margin: 0 0 12px 0;">✅ Advantages of a Partnership</h4>
                <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 14px; line-height: 1.6;">
                    <li><b>More capital:</b> Multiple partners contribute significantly greater funds.</li>
                    <li><b>Shared workload:</b> Partners divide operational duties and specialized tasks.</li>
                    <li><b>Complementary skills:</b> Diverse professional expertise (e.g. legal, marketing).</li>
                    <li><b>Simple setup:</b> Relatively quick with a written Partnership Agreement.</li>
                </ul>
            </div>

            <div id="card-partnerships-disadv" class="lecture-interactive-card" data-lecture-section="card_partnerships_disadv" style="background: #fef2f2; border: 1.5px solid #fecaca; border-left: 5px solid #dc2626; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #b91c1c; font-size: 18px; margin: 0 0 12px 0;">❌ Disadvantages of a Partnership</h4>
                <ul style="margin: 0; padding-left: 20px; color: #991b1b; font-size: 14px; line-height: 1.6;">
                    <li><b>Unlimited liability:</b> All general partners risk personal assets for firm debts.</li>
                    <li><b>Disagreements:</b> Conflict between partners can delay strategic decisions.</li>
                    <li><b>Joint liability:</b> An error by one partner legally binds all other partners.</li>
                    <li><b>Lack of continuity:</b> If one partner leaves or dies, the firm must dissolve.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- COMPARISON TABLE: UNINCORPORATED VS INCORPORATED -->
    <div id="card-unincorp-vs-incorp" class="lecture-interactive-card" data-lecture-section="card_unincorp_vs_incorp" style="margin-bottom: 45px; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
        <h3 style="color: #0f172a; font-size: 20px; margin-top: 0; margin-bottom: 14px; display: flex; align-items: center; gap: 10px;">
            <span>⚖️</span> Unincorporated Businesses vs Incorporated Limited Companies
        </h3>
        <p style="font-size: 14.5px; color: #475569; margin-bottom: 16px; line-height: 1.6;">
            A cornerstone concept in Cambridge Business Studies is the fundamental legal difference between unincorporated entities and incorporated companies:
        </p>
        <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13.5px; background: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
                <thead>
                    <tr style="background: #0ea5e9; color: #ffffff;">
                        <th style="padding: 10px 14px;">Feature</th>
                        <th style="padding: 10px 14px;">Unincorporated (Sole Trader / Partnership)</th>
                        <th style="padding: 10px 14px;">Incorporated (Ltd / Plc Companies)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Legal Identity</td>
                        <td style="padding: 10px 14px; color: #b91c1c;">No separate legal identity (owner IS the business).</td>
                        <td style="padding: 10px 14px; color: #15803d;">Separate legal identity (company is a legal person).</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                        <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Liability</td>
                        <td style="padding: 10px 14px; color: #b91c1c;">Unlimited liability (personal property can be seized).</td>
                        <td style="padding: 10px 14px; color: #15803d;">Limited liability (shareholders risk only invested funds).</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Continuity</td>
                        <td style="padding: 10px 14px; color: #64748b;">No continuity (business ceases on death of owner).</td>
                        <td style="padding: 10px 14px; color: #15803d;">Perpetual continuity (survives changes of owners).</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                        <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Capital Potential</td>
                        <td style="padding: 10px 14px; color: #64748b;">Low to moderate (limited to personal savings and loans).</td>
                        <td style="padding: 10px 14px; color: #15803d;">High (can sell shares to raise massive capital).</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Accounts Privacy</td>
                        <td style="padding: 10px 14px; color: #15803d;">Private (no requirement to publish accounts).</td>
                        <td style="padding: 10px 14px; color: #b91c1c;">Must publish accounts (Plcs publish full public reports).</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 3. JOINT-STOCK COMPANIES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-companies" class="lecture-interactive-card" data-lecture-section="sec_companies" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏢 3. JOINT-STOCK COMPANIES</h2>
            <p style="font-size: 15px; color: #475569; margin: 0 0 14px 0; line-height: 1.6;">
                Companies sell shares of ownership to raise capital. Shareholders earn <b>dividends</b>, enjoy <b>limited liability</b>, and elect a <b>Board of Directors</b> to govern company operations.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div id="card-company-ltd" class="lecture-interactive-card" data-lecture-section="card_company_ltd" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 5px solid #059669; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #059669; font-size: 17px; margin: 0 0 8px 0;">🔒 Private Limited Company (Ltd)</h4>
                <p style="margin: 0 0 8px 0; font-size: 14px; color: #475569; line-height: 1.5;">Shares sold <b>only to known people</b> (family &amp; friends). Cannot sell to general public.</p>
                <div style="font-size: 13px; color: #166534; font-weight: bold;">Example: Ikea</div>
            </div>

            <div id="card-company-plc" class="lecture-interactive-card" data-lecture-section="card_company_plc" style="background: #fffbeb; border: 1.5px solid #fde68a; border-left: 5px solid #d97706; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #d97706; font-size: 17px; margin: 0 0 8px 0;">🌐 Public Limited Company (Plc)</h4>
                <p style="margin: 0 0 8px 0; font-size: 14px; color: #475569; line-height: 1.5;">Shares traded on <b>stock exchanges</b> to any member of the public, raising huge capital.</p>
                <div style="font-size: 13px; color: #b45309; font-weight: bold;">Example: Verizon, Microsoft</div>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-company-adv" class="lecture-interactive-card" data-lecture-section="card_company_adv" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #15803d; font-size: 17px; margin: 0 0 10px 0;">✅ Company Advantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 14px; line-height: 1.6;">
                    <li><b>Limited liability:</b> Financial risk capped at share purchase value.</li>
                    <li><b>Enormous capital:</b> Ability to raise large equity funds for scale.</li>
                    <li><b>Perpetual existence:</b> Independent continuity past founders' lives.</li>
                </ul>
            </div>

            <div id="card-company-disadv" class="lecture-interactive-card" data-lecture-section="card_company_disadv" style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #b91c1c; font-size: 17px; margin: 0 0 10px 0;">❌ Company Disadvantages</h4>
                <ul style="margin: 0; padding-left: 20px; color: #991b1b; font-size: 14px; line-height: 1.6;">
                    <li><b>Public disclosure:</b> Annual published accounts reveal secrets to rivals.</li>
                    <li><b>Expensive formalities:</b> High legal setup and AGM meeting costs.</li>
                    <li><b>Divorce of ownership:</b> Directors can outvote minority shareholders.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 4. FRANCHISES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-franchises" class="lecture-interactive-card" data-lecture-section="sec_franchises" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🍔 4. FRANCHISES</h2>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #831843; line-height: 1.6;">
                A franchisor licenses an independent franchisee to trade using its brand name, recipes, and operating systems in exchange for licence fees and royalties (e.g. McDonald's, Subway).
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div id="card-franchisor" class="lecture-interactive-card" data-lecture-section="card_franchisor" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #0f172a; font-size: 17px; margin: 0 0 10px 0;">👑 To Franchisor (Brand Owner)</h4>
                <div style="margin-bottom: 10px; font-size: 13.5px; color: #166534;"><b>✅ Pros:</b> Rapid low-cost global expansion; steady stream of royalty revenue.</div>
                <div style="font-size: 13.5px; color: #b91c1c;"><b>❌ Cons:</b> Profits shared; one bad franchisee damages whole brand reputation.</div>
            </div>

            <div id="card-franchisee" class="lecture-interactive-card" data-lecture-section="card_franchisee" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h4 style="color: #0f172a; font-size: 17px; margin: 0 0 10px 0;">🏪 To Franchisee (Local Operator)</h4>
                <div style="margin-bottom: 10px; font-size: 13.5px; color: #166534;"><b>✅ Pros:</b> Established brand reduces failure risk; receives training and supplies.</div>
                <div style="font-size: 13.5px; color: #b91c1c;"><b>❌ Cons:</b> Expensive setup fees; no operational freedom; must pay royalties.</div>
            </div>
        </div>
    </div>

    <!-- 5. JOINT VENTURES -->
    <div id="sec-joint-ventures" class="lecture-interactive-card" data-lecture-section="sec_joint_ventures" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🚀 5. JOINT VENTURES</h2>
        <div style="background: #fff7ed; border-left: 5px solid #ea580c; padding: 15px 20px; border-radius: 8px; font-size: 15px; color: #9a3412; margin-bottom: 18px; line-height: 1.6;">
            A joint venture is an agreement between two or more separate businesses to collaborate on a specific project, sharing capital, risks, and profits (e.g. Google Earth = Google + NASA).
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 14px; font-size: 13.5px; color: #166534;">
                <b>✅ Benefits:</b> Cuts costs and shares financial risk; combines complementary skills with local market expertise.
            </div>
            <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 14px; font-size: 13.5px; color: #991b1b;">
                <b>❌ Drawbacks:</b> Conflicts between different corporate cultures; mistakes by one party damage reputations of all.
            </div>
        </div>
    </div>

    <!-- 6. PUBLIC SECTOR CORPORATIONS -->
    <div id="sec-public-corporations" class="lecture-interactive-card" data-lecture-section="sec_public_corporations" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏛️ 6. PUBLIC SECTOR CORPORATIONS</h2>
        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 20px; margin-bottom: 18px; font-size: 14.5px; color: #475569; line-height: 1.6;">
            Wholly owned and run by the state to deliver critical national public services (water, rail, health). Funded by government subsidies with overriding aims of affordability and universal access.
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 14px; font-size: 13.5px; color: #166534;">
                <b>✅ Pros:</b> Safeguards vital industries; avoids wasteful duplication; keeps services accessible to low-income citizens.
            </div>
            <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 14px; font-size: 13.5px; color: #991b1b;">
                <b>❌ Cons:</b> Lower staff motivation without profit incentives; lack of competition breeds operational inefficiency.
            </div>
        </div>
    </div>

    <!-- 7. RECOMMEND & JUSTIFY -->
    <div id="sec-exam-recommendation" class="lecture-interactive-card" data-lecture-section="sec_exam_recommendation" style="margin-bottom: 45px; padding: 24px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #1e3a8a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 16px; font-size: 22px; margin-top: 0; display: inline-block;">
            🎯 7. HOW TO RECOMMEND &amp; JUSTIFY A FORM OF ORGANISATION (Cambridge Exam Strategy)
        </h2>
        <p style="font-size: 14.5px; color: #334155; margin-bottom: 14px; line-height: 1.6;">
            In Cambridge Paper 1 &amp; 2 exam questions, always justify your recommendation based on the business's specific context:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; font-size: 13.5px;">
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border: 1px solid #bfdbfe;">
                <b style="color: #2563eb;">1. Growth &amp; Capital:</b> If vast capital is required for mass factories, recommend <b>Plc</b> or <b>Ltd</b>.
            </div>
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border: 1px solid #bfdbfe;">
                <b style="color: #2563eb;">2. Risk &amp; Liability:</b> If high debt risk exists, recommend <b>Ltd</b> to safeguard personal assets.
            </div>
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border: 1px solid #bfdbfe;">
                <b style="color: #2563eb;">3. Independence &amp; Control:</b> If owner demands total control without interference, recommend <b>Sole Trader</b>.
            </div>
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border: 1px solid #bfdbfe;">
                <b style="color: #2563eb;">4. International Expansion:</b> To expand abroad rapidly with low capital, recommend <b>Franchising</b> or <b>Joint Venture</b>.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.4 Types of Business Organisation (Các loại hình tổ chức doanh nghiệp)</h1>
        </div>
    </div>"""
    new_p2 = re.sub(pattern, header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 1.4 Audio and HTML ===")
    
    # 0. Clean stale audio files so that all 19 segments match perfectly
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)
    valid_ids = {s['id'] for s in segments}
    for fname in os.listdir(audio_dir):
        if fname.endswith('.mp3'):
            base_id = fname[:-4]
            if base_id not in valid_ids or base_id in {'sec_sole_trader', 'sec_partnerships', 'sec_companies', 'sec_franchises', 'sec_joint_ventures', 'sec_public_corporations', 'sec_exam_recommendation'}:
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
    with open('scripts/bs_1_4_page_2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 1.4 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
