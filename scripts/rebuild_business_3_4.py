import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 3.4 ID
LID = 'c0d60bf9-ad33-456c-807e-9e29318113b8'
CODE = '3_4'
TITLE = '3.4. Marketing strategy'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 10 AUDIO SEGMENTS FOR LESSON 3.4
# ==============================================================================
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
        "id": "card_strategy_factors",
        "title": "🧩 5 Yếu tố Quyết định Chiến lược Tiếp thị",
        "selector": "#card-strategy-factors",
        "en": "Marketing strategies are influenced by five critical variables: the financial marketing budget, target market demographics, overarching corporate marketing objectives, rival firms' competitive counter-actions, and the current product life cycle stage.",
        "vi": "Chiến lược tiếp thị chịu sự chi phối của năm yếu tố then chốt: quy mô ngân sách tiếp thị, đặc điểm khách hàng mục tiêu, các mục tiêu tiếp thị dài hạn của công ty, phản ứng cạnh tranh của đối thủ và giai đoạn hiện tại trong vòng đời sản phẩm."
    },
    {
        "id": "sec_legal_controls",
        "title": "2. Khung Pháp lý Bảo vệ Người tiêu dùng",
        "selector": "#sec-legal-controls",
        "en": "Section 2 investigates statutory consumer protection laws: bans on misleading advertising, weight and measurement standards, product safety regulations, and laws against anti-competitive price collusion. Businesses failing to comply risk hefty fines, loss of reputation, and product recalls.",
        "vi": "Mục hai khảo sát các quy định pháp luật bảo vệ người tiêu dùng: nghiêm cấm quảng cáo sai sự thật, chuẩn hóa đơn vị đo lường và trọng lượng, quy chuẩn an toàn sản phẩm và luật chống độc quyền thao túng giá. Doanh nghiệp vi phạm sẽ bị xử phạt hành chính nặng nề, mất uy tín thương hiệu và bị buộc thu hồi sản phẩm."
    },
    {
        "id": "card_consumer_protection_laws",
        "title": "⚖️ 3 Luật Bảo vệ Người tiêu dùng Cốt lõi",
        "selector": "#card-consumer-protection-laws",
        "en": "Three key legal pillars protect consumers: Product Quality and Safety legislation prevents sales of hazardous merchandise; Truth-in-Advertising bans deceitful promotional claims; and Anti-Monopoly regulations prevent dominant companies from price gouging in uncompetitive markets.",
        "vi": "Ba trụ cột pháp lý bảo vệ người tiêu dùng gồm: Luật an toàn và chất lượng sản phẩm ngăn chặn kinh doanh hàng nguy hiểm kém chất lượng; Luật chống quảng cáo sai sự thật xử phạt các tuyên bố phóng đại gian lận; và Luật chống độc quyền ngăn các công ty chiếm vị thế thống lĩnh thao túng chèn ép giá cả."
    },
    {
        "id": "sec_entering_markets",
        "title": "3. Thâm nhập Thị trường Quốc tế (Foreign Market Entry)",
        "selector": "#sec-entering-markets",
        "en": "Section 3 explores overseas expansion. Expanding internationally unlocks immense new sales volumes and spreads commercial risks when domestic markets hit saturation, but forces businesses to navigate cultural divides, currency volatility, and distant distribution logistics.",
        "vi": "Mục ba tìm hiểu việc mở rộng ra thị trường nước ngoài. Phát triển ra quốc tế đem lại sản lượng tiêu thụ khổng lồ và phân tán rủi ro khi thị trường trong nước đã bão hòa, nhưng đồng thời buộc doanh nghiệp phải xử lý bất đồng văn hóa, biến động tỷ giá và logistics xa xôi."
    },
    {
        "id": "card_foreign_market_problems",
        "title": "⚠️ 6 Rào cản khi Thâm nhập Thị trường Nước ngoài",
        "selector": "#card-foreign-market-problems",
        "en": "Foreign expansion introduces six hurdles: language and cultural miscommunications, lack of local customer familiarity, economic purchasing power disparity, elevated long-distance freight costs, conflicting societal habits, and unfamiliar overseas legal frameworks.",
        "vi": "Gia nhập thị trường quốc tế đối mặt sáu trở ngại: bất đồng ngôn ngữ và văn hóa, thiếu hiểu biết về thị hiếu bản địa, khác biệt về mức thu nhập kinh tế, chi phí vận chuyển quốc tế cao, phong tục tập quán xã hội khác biệt và các quy định pháp lý nước ngoài phức tạp."
    },
    {
        "id": "card_joint_venture",
        "title": "🤝 Phương thức 1: Liên doanh (Joint Venture)",
        "selector": "#card-joint-venture",
        "en": "In a Joint Venture, an overseas business partners with a domestic company to share equity and management, as illustrated by Maruti Suzuki. Joint ventures cut initial investment costs and harness local expertise, but can generate governance friction and shared reputational vulnerability.",
        "vi": "Trong mô hình Liên doanh (Joint Venture), doanh nghiệp nước ngoài hợp tác với một doanh nghiệp bản địa để chia sẻ vốn và quản lý, như trường hợp Maruti Suzuki. Liên doanh giúp giảm gánh nặng vốn ban đầu và tận dụng sự am hiểu địa phương, nhưng tiềm ẩn xung đột phong cách lãnh đạo và rủi ro ảnh hưởng uy tín chung."
    },
    {
        "id": "card_franchising",
        "title": "👑 Phương thức 2: Nhượng quyền Thương mại (Franchising & Licensing)",
        "selector": "#card-franchising",
        "en": "Franchising permits local franchisees to operate under a global brand name in exchange for upfront fees and recurring royalties. Franchisors achieve rapid, low-capital global scaling, while franchisees gain a proven business model, though franchisors risk brand damage if individual franchisees cut service quality.",
        "vi": "Nhượng quyền thương mại (Franchising) cho phép bên nhận quyền kinh doanh dưới thương hiệu toàn cầu để đổi lấy phí nhượng quyền ban đầu và tiền bản quyền định kỳ. Bên nhượng quyền mở rộng thần tốc mà ít tốn vốn, còn bên nhận quyền sở hữu mô hình kinh doanh đã thành công, dù vậy bên nhượng quyền đối mặt rủi ro hoen ố thương hiệu nếu bên nhận quyền làm giảm chất lượng."
    },
    {
        "id": "sec_recommend_strategy",
        "title": "4. Chiến lược làm bài thi Cambridge: Đề xuất & Biện minh Kế hoạch Tiếp thị",
        "selector": "#sec-recommend-strategy",
        "en": "Section 4 outlines Cambridge evaluation technique for 12-mark questions. Candidates must harmonise all four marketing mix elements so they tell a consistent story, verify that proposed campaigns fit within stated budget constraints, anticipate rival retaliation, and evaluate whether Joint Ventures or Franchising offer the optimal market entry vehicle.",
        "vi": "Mục bốn tổng kết phương pháp làm bài thi Cambridge cho câu hỏi đánh giá 12 điểm. Thí sinh phải bảo đảm tính đồng bộ của 4 chữ P để tạo nên một câu chuyện thương hiệu nhất quán, kiểm chứng chiến dịch đề xuất nằm gọn trong ngân sách cho phép, dự đoán phản ứng đáp trả của đối thủ và so sánh xem Liên doanh hay Nhượng quyền là lựa chọn tối ưu cho việc thâm nhập thị trường."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_marketing_strategy": {"start": 1, "end": 2},
    "sec_legal_controls": {"start": 3, "end": 4},
    "sec_entering_markets": {"start": 5, "end": 8},
    "sec_recommend_strategy": {"start": 9, "end": 9}
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
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 3</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">3.4 Marketing Strategy (Chiến lược Tiếp thị)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. MARKETING STRATEGY -->
    <div style="margin-bottom: 50px;">
        <div id="sec-marketing-strategy" class="lecture-interactive-card" data-lecture-section="sec_marketing_strategy" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🎯 1. MARKETING STRATEGY</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 12px;">
                A <b>marketing strategy</b> is a plan to combine the right combination of the four elements of the marketing mix (Product, Price, Place, Promotion) for a product to achieve its marketing objectives.
            </div>
            <p style="font-size: 14.5px; color: #475569; margin: 0; line-height: 1.5;">
                <i>Marketing objectives could include maintaining market shares, increasing sales in a niche market, or increasing sales of an existing product by using extension strategies.</i>
            </p>
        </div>

        <!-- SUB-CARD: STRATEGY FACTORS -->
        <div id="card-strategy-factors" class="lecture-interactive-card" data-lecture-section="card_strategy_factors" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">🧩 Factors that affect the marketing strategy:</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="margin-bottom: 15px; text-align: center; overflow-x: auto; padding: 10px 0;">
                <svg viewBox="0 0 600 350" width="100%" style="min-width: 500px; background:#ffffff; border-radius:12px; border:1px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: block; margin: 0 auto; font-family: Arial, sans-serif;">
                    <line x1="300" y1="175" x2="150" y2="90" stroke="#94a3b8" stroke-width="2"></line>
                    <line x1="300" y1="175" x2="450" y2="90" stroke="#94a3b8" stroke-width="2"></line>
                    <line x1="300" y1="175" x2="150" y2="260" stroke="#94a3b8" stroke-width="2"></line>
                    <line x1="300" y1="175" x2="450" y2="260" stroke="#94a3b8" stroke-width="2"></line>
                    <line x1="300" y1="175" x2="300" y2="50" stroke="#94a3b8" stroke-width="2"></line>

                    <rect x="220" y="150" width="160" height="50" fill="#2563eb" rx="8"></rect>
                    <text x="300" y="175" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff" dominant-baseline="middle">MARKETING STRATEGY</text>

                    <rect x="220" y="25" width="160" height="40" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" rx="6"></rect>
                    <text x="300" y="50" text-anchor="middle" font-size="13" font-weight="bold" fill="#334155" dominant-baseline="middle">Marketing Budget</text>

                    <rect x="70" y="70" width="160" height="40" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" rx="6"></rect>
                    <text x="150" y="95" text-anchor="middle" font-size="13" font-weight="bold" fill="#334155" dominant-baseline="middle">Target Market</text>

                    <rect x="370" y="70" width="160" height="40" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" rx="6"></rect>
                    <text x="450" y="95" text-anchor="middle" font-size="13" font-weight="bold" fill="#334155" dominant-baseline="middle">Marketing Objectives</text>

                    <rect x="70" y="240" width="160" height="40" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" rx="6"></rect>
                    <text x="150" y="265" text-anchor="middle" font-size="13" font-weight="bold" fill="#334155" dominant-baseline="middle">Competitors' Actions</text>

                    <rect x="370" y="240" width="160" height="40" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" rx="6"></rect>
                    <text x="450" y="265" text-anchor="middle" font-size="13" font-weight="bold" fill="#334155" dominant-baseline="middle">Stage of PLC</text>
                </svg>
            </div>
        </div>
    </div>

    <!-- 2. LEGAL CONTROLS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-legal-controls" class="lecture-interactive-card" data-lecture-section="sec_legal_controls" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 2. LEGAL CONTROLS ON MARKETING</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                There are various laws that can affect marketing decisions regarding quality, price, and the contents of advertisements.
            </p>
        </div>

        <!-- SUB-CARD: CONSUMER PROTECTION LAWS -->
        <div id="card-consumer-protection-laws" class="lecture-interactive-card" data-lecture-section="card_consumer_protection_laws" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fecaca; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #b91c1c; font-weight: 700;">⚖️ 3 Core Consumer Protection Laws</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fef2f2; color: #b91c1c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fecaca;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 16px; border-radius: 8px;">
                    <div style="font-size: 22px; margin-bottom: 8px;">🛡️</div>
                    <h4 style="margin: 0 0 5px 0; color: #b91c1c; font-size: 15px;">Product Quality &amp; Safety</h4>
                    <p style="margin: 0; font-size: 13px; color: #7f1d1d; line-height: 1.5;">Laws protecting consumers from being sold faulty, dangerous, or contaminated merchandise.</p>
                </div>

                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 16px; border-radius: 8px;">
                    <div style="font-size: 22px; margin-bottom: 8px;">🤥</div>
                    <h4 style="margin: 0 0 5px 0; color: #b91c1c; font-size: 15px;">Misleading Advertising</h4>
                    <p style="margin: 0; font-size: 13px; color: #7f1d1d; line-height: 1.5;">Laws preventing fraudulent or deceitful claims. <i>(e.g., Volkswagen diesel emissions scandal).</i></p>
                </div>

                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 16px; border-radius: 8px;">
                    <div style="font-size: 22px; margin-bottom: 8px;">🛑</div>
                    <h4 style="margin: 0 0 5px 0; color: #b91c1c; font-size: 15px;">Anti-Monopoly Laws</h4>
                    <p style="margin: 0; font-size: 13px; color: #7f1d1d; line-height: 1.5;">Regulations stopping monopolies from exploiting buyers with collusive price fixing.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. ENTERING MARKETS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-entering-markets" class="lecture-interactive-card" data-lecture-section="sec_entering_markets" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🌍 3. ENTERING NEW MARKETS</h2>
            <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 14px 18px; border-radius: 4px; font-size: 14.5px; color: #065f46; margin: 0;">
                Growing business in other countries can <b>increase sales, revenue, and profits</b> by reaching a wider group of potential customers. Firms often enter international markets when home markets are saturated (in the maturity stage).
            </div>
        </div>

        <!-- SUB-CARD: PROBLEMS OF FOREIGN MARKETS -->
        <div id="card-foreign-market-problems" class="lecture-interactive-card" data-lecture-section="card_foreign_market_problems" style="margin-bottom: 25px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #065f46; font-weight: 700;">⚠️ 6 Problems of entering foreign markets</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f0fdf4; color: #047857; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <b style="color: #0f172a; font-size: 14px;">🗣️ Language &amp; Culture</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Communication barriers exist. <i>(e.g., McDonald’s vegetarian menu in India).</i></p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <b style="color: #0f172a; font-size: 14px;">❓ Lack of market knowledge</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Unfamiliar customers and lack of brand awareness make setup expensive.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <b style="color: #0f172a; font-size: 14px;">💵 Economic differences</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Purchasing power differences complicate profitable price points.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <b style="color: #0f172a; font-size: 14px;">🚢 High transport costs</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Long-distance freight physically increases unit logistics costs.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <b style="color: #0f172a; font-size: 14px;">🤝 Social differences</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Foreign consumers exhibit distinct buying habits and social values.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <b style="color: #0f172a; font-size: 14px;">⚖️ Different legal controls</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Must modify products to comply with local consumer safety codes.</p>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: JOINT VENTURE -->
        <div id="card-joint-venture" class="lecture-interactive-card" data-lecture-section="card_joint_venture" style="margin-bottom: 25px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">🤝 Overcoming Problems: 1. Joint Venture</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 14px 18px; border-radius: 4px; font-size: 14.5px; color: #9a3412; margin-bottom: 16px;">
                <b>Joint Venture:</b> An agreement between two or more businesses to work together on a project. The foreign business works with a domestic business. <br><i>Ex: Japan’s Suzuki Motor Corp partnered with India’s Maruti Udyog to create Maruti Suzuki.</i>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #15803d; font-size: 15px; margin: 0 0 10px 0;">✅ Advantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 13px; line-height: 1.5;">
                        <li>Reduces risks and cuts initial capital costs.</li>
                        <li>Partners bring complementary domestic market expertise.</li>
                        <li>Expands market access rapidly for both businesses.</li>
                    </ul>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #b91c1c; font-size: 15px; margin: 0 0 10px 0;">❌ Disadvantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 13px; line-height: 1.5;">
                        <li>Mistakes reflect on all parties, harming reputations.</li>
                        <li>Decision friction due to conflicting corporate cultures.</li>
                        <li>Profits must be shared between the partners.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: FRANCHISING -->
        <div id="card-franchising" class="lecture-interactive-card" data-lecture-section="card_franchising" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #be185d; font-weight: 700;">👑 Overcoming Problems: 2. Franchise / Licensing</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fdf2f8; color: #db2777; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>

            <div style="background: #fdf2f8; border-left: 4px solid #db2777; padding: 14px 18px; border-radius: 4px; font-size: 14.5px; color: #831843; margin-bottom: 16px;">
                <b>Franchise / License:</b> The owner of a business (<b>franchisor</b>) grants a licence to another person or business (<b>franchisee</b>) to use their business idea. <br><i>Ex: McDonald’s and Subway operating worldwide.</i>
            </div>

            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; margin-bottom: 14px;">
                <div style="background: #f8fafc; padding: 10px 16px; border-bottom: 1px solid #e2e8f0; font-weight: bold; color: #0f172a; font-size: 14.5px;">👑 To Franchisor (The Brand Owner)</div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
                    <div style="padding: 14px; background: #f0fdf4; border-right: 1px solid #e2e8f0;">
                        <b style="color: #15803d; font-size: 13px;">✅ Advantages:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 16px; color: #166534; font-size: 12.5px; line-height: 1.4;">
                            <li>Rapid, low-capital global expansion.</li>
                            <li>Steady royalty fees and upfront payments.</li>
                            <li>Franchisee understands local tastes.</li>
                        </ul>
                    </div>
                    <div style="padding: 14px; background: #fef2f2;">
                        <b style="color: #b91c1c; font-size: 13px;">❌ Disadvantages:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 16px; color: #991b1b; font-size: 12.5px; line-height: 1.4;">
                            <li>Shared profit margins.</li>
                            <li>Loss of direct operational control.</li>
                            <li>A single bad operator damages brand prestige.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden;">
                <div style="background: #f8fafc; padding: 10px 16px; border-bottom: 1px solid #e2e8f0; font-weight: bold; color: #0f172a; font-size: 14.5px;">🏪 To Franchisee (The Local Operator)</div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));">
                    <div style="padding: 14px; background: #f0fdf4; border-right: 1px solid #e2e8f0;">
                        <b style="color: #15803d; font-size: 13px;">✅ Advantages:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 16px; color: #166534; font-size: 12.5px; line-height: 1.4;">
                            <li>Established brand recognition lowers business risk.</li>
                            <li>Training and equipment supplied by franchisor.</li>
                        </ul>
                    </div>
                    <div style="padding: 14px; background: #fef2f2;">
                        <b style="color: #b91c1c; font-size: 13px;">❌ Disadvantages:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 16px; color: #991b1b; font-size: 12.5px; line-height: 1.4;">
                            <li>High startup fees &amp; ongoing royalty charges.</li>
                            <li>Must strictly obey franchisor guidelines without autonomy.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. RECOMMENDING & JUSTIFYING A MARKETING STRATEGY -->
    <div style="margin-bottom: 50px;">
        <div id="sec-recommend-strategy" class="lecture-interactive-card" data-lecture-section="sec_recommend_strategy" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 4. HOW TO RECOMMEND &amp; JUSTIFY A MARKETING STRATEGY (Cambridge Framework)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Paper 2 frequently includes a 12-mark recommendation question: <i>"Recommend the most appropriate marketing strategy for this business to increase its sales."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 18px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                    <b style="color: #1e40af; font-size: 14.5px;">1. Harmonise the 4Ps</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        The 4 elements must not contradict. A luxury good cannot be discounted in wholesale flyers. Price, Product, Promotion, and Place must tell one cohesive story.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #10b981;">
                    <b style="color: #047857; font-size: 14.5px;">2. Align with Budget</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        A small sole trader cannot afford television commercials. Recommend targeted social media ads, local leaflet drops, or loyalty reward schemes instead.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                    <b style="color: #b45309; font-size: 14.5px;">3. Competitors' Responses</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        If the strategy relies on aggressive price cuts, larger rivals may retaliate with lower prices, triggering a ruinous price war.
                    </p>
                </div>
            </div>

            <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
                <b style="color: #1e40af; font-size: 14px;">💡 Cambridge Evaluation Formula for Foreign Market Entry:</b>
                <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                    When deciding between a <b>Joint Venture</b> and <b>Franchising</b>: A Joint Venture is optimal when the business needs deep local regulatory expertise and wants to share heavy capital setup costs; Franchising is superior when the firm possesses a globally famous brand name (like McDonald's) and seeks rapid zero-capital expansion.
                </p>
            </div>
        </div>
    </div>

</div>"""
    return html

# ==============================================================================
# 3. GENERATE NEW HTML FOR PAGE 2 (BILINGUAL) - REMOVE STUDY RESOURCES
# ==============================================================================
def build_page_2_html(original_p2):
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">3.4 Marketing Strategy (Chiến lược Tiếp thị)</h1>
        </div>
    </div>"""
    
    # 1. Strip the Study Resources box from page 2
    # In original_p2, it's:
    # <!-- STUDY RESOURCES -->
    # <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; ...>...</div>
    sr_pattern = r'<!-- STUDY RESOURCES -->\s*<div style="display: flex; flex-wrap: wrap;.*?</div>\s*</div>'
    # Wait, let's match the div cleanly:
    cleaned_p2 = re.sub(r'<!-- STUDY RESOURCES -->\s*<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">[\s\S]*?</div>', '', original_p2)
    
    # 2. Add header banner right after the container div
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, cleaned_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 3.4 Audio and HTML ===")
    
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)

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
    with open('scripts/raw_pages/3_4_p2.html', 'r', encoding='utf-8') as f:
        orig_p2 = f.read()
    p2_html = build_page_2_html(orig_p2)
    diff2 = len(p2_html.split('<div')) - len(p2_html.split('</div>'))
    print(f"Page 2 HTML div diff: {diff2}")
    if diff2 != 0:
        raise ValueError(f"Page 2 has div balance error: {diff2}")
        
    # 4. Check for any remaining Study Resources in Page 1 or Page 2
    for name, content in [('Page 1', p1_html), ('Page 2', p2_html)]:
        if 'Study Resources' in content or 'Tài liệu học tập' in content:
            print(f"⚠️ WARNING: {name} still contains Study Resources references!")
        else:
            print(f"✅ {name} confirmed clean of Study Resources.")
        
    # 5. Update Supabase
    print("\nUpdating Supabase page 1...")
    res1 = sb.table('lecture_pages').update({'content_html': p1_html}).eq('lecture_id', LID).eq('page_number', 1).execute()
    print(f"Page 1 updated: {len(res1.data)} rows.")
    
    print("Updating Supabase page 2...")
    res2 = sb.table('lecture_pages').update({'content_html': p2_html}).eq('lecture_id', LID).eq('page_number', 2).execute()
    print(f"Page 2 updated: {len(res2.data)} rows.")
    
    print("\n✅ REBUILD 3.4 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
