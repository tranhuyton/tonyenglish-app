import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 3.3 ID
LID = '25fe41d9-780d-41a6-876d-fff3e0d854c5'
CODE = '3_3'
TITLE = '3.3. Marketing mix'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 14 AUDIO SEGMENTS FOR LESSON 3.3
# ==============================================================================
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
        "id": "card_npd_brand",
        "title": "🚀 Phát triển Sản phẩm Mới (NPD) & Thương hiệu, Bao bì",
        "selector": "#card-npd-brand",
        "en": "New Product Development involves six systematic stages: idea generation, screening, sales assessment, prototyping, test launch, and full launch. Concurrently, distinctive branding and protective packaging build customer recognition, command premium prices, and safeguard products during distribution.",
        "vi": "Quy trình phát triển sản phẩm mới (NPD) gồm sáu bước: tìm ý tưởng, sàng lọc, đánh giá tiềm năng doanh số, tạo mẫu thử, bán thử nghiệm và ra mắt chính thức. Đồng thời, thương hiệu độc đáo và bao bì bảo vệ giúp tăng cường nhận diện của khách hàng, cho phép định giá cao và bảo quản sản phẩm an toàn."
    },
    {
        "id": "card_plc",
        "title": "📈 Vòng đời Sản phẩm (Product Life Cycle - PLC)",
        "selector": "#card-plc",
        "en": "The Product Life Cycle traces sales volume across six stages: Development, Introduction, Growth, Maturity, Saturation, and Decline. Extension strategies—such as rebranding, reformulating ingredients, or entering overseas markets—rejuvenate sales before a product reaches full obsolescence.",
        "vi": "Vòng đời sản phẩm (PLC) theo dõi doanh số qua các giai đoạn: Phát triển, Giới thiệu, Tăng trưởng, Chín muồi, Bão hòa và Suy thoái. Các chiến lược kéo dài vòng đời như đổi mới bao bì, cải tiến công thức hoặc mở rộng thị trường xuất khẩu giúp khôi phục đà tăng trưởng trước khi sản phẩm bị đào thải."
    },
    {
        "id": "sec_price",
        "title": "2. Chữ P thứ hai: Giá cả (Price)",
        "selector": "#sec-price",
        "en": "Section 2 focuses on Price: the monetary consideration exchanged between buyers and sellers. Pricing decisions must reflect manufacturing costs, product uniqueness, competitive intensity, and the target market's purchasing power.",
        "vi": "Mục hai tập trung vào Giá cả (Price): số tiền trao đổi giữa người mua và người bán. Quyết định định giá phải phản ánh chi phí sản xuất, tính độc đáo của sản phẩm, mức độ cạnh tranh trên thị trường và khả năng chi trả của khách hàng mục tiêu."
    },
    {
        "id": "card_pricing_methods",
        "title": "💵 5 Phương pháp Định giá Cốt lõi (Methods of Pricing)",
        "selector": "#card-pricing-methods",
        "en": "Businesses utilize distinct pricing tactics: Market Skimming sets high prices for innovative novelties; Penetration Pricing starts low to capture market share; Competitive Pricing aligns with rivals; Cost-plus Pricing guarantees markup over expenses; while Loss Leaders sacrifice immediate margins to drive foot traffic.",
        "vi": "Doanh nghiệp áp dụng các chiến lược giá khác nhau: Hớt váng (Skimming) đặt giá cao cho sản phẩm đột phá; Thâm nhập (Penetration) đặt giá thấp để giành thị phần; Cạnh tranh (Competitive) bám sát đối thủ; Cộng chi phí (Cost-plus) bảo đảm lợi nhuận trên chi phí; và Giá bán lỗ thu hút (Loss Leader) hy sinh lợi nhuận ngắn hạn để kéo khách hàng đến điểm bán."
    },
    {
        "id": "card_ped",
        "title": "📊 Độ co giãn của Cầu theo Giá (Price Elasticity of Demand - PED)",
        "selector": "#card-ped",
        "en": "Price Elasticity of Demand measures how responsive demand is to price changes. For price-elastic products with close substitutes, cutting prices boosts sales volume and revenue. For inelastic necessities with high brand loyalty, raising prices expands overall revenue because demand barely drops.",
        "vi": "Độ co giãn của cầu theo giá (PED) đo lường mức độ phản ứng của lượng cầu khi giá bán thay đổi. Với sản phẩm có cầu co giãn (nhiều hàng thay thế), giảm giá sẽ đẩy mạnh doanh số và tổng doanh thu. Với hàng thiết yếu có cầu không co giãn hoặc thương hiệu mạnh, tăng giá sẽ giúp tăng tổng doanh thu vì lượng cầu sụt giảm rất ít."
    },
    {
        "id": "sec_place",
        "title": "3. Chữ P thứ ba: Kênh phân phối (Place)",
        "selector": "#sec-place",
        "en": "Section 3 examines Place: distribution channels connecting manufacturers to end consumers. Whether selling directly, via retailers, through wholesalers, or using specialist overseas agents, channel decisions dictate logistics costs and retail coverage.",
        "vi": "Mục ba xem xét Kênh phân phối (Place): các mắt xích kết nối nhà sản xuất với người tiêu dùng cuối. Dù bán trực tiếp, qua nhà bán lẻ, thông qua nhà bán buôn hay đại lý nước ngoài, quyết định kênh phân phối quyết định chi phí vận tải và độ phủ thị trường."
    },
    {
        "id": "card_distribution_channels",
        "title": "🚚 4 Kênh Phân phối & Quyết định Lựa chọn Kênh",
        "selector": "#card-distribution-channels",
        "en": "Businesses choose between four distribution channels: direct to consumer for maximum profit margins; via retailers for convenience; through wholesalers for bulk breaking; or via overseas agents for export markets. Decisions depend on product perishability, unit value, technical complexity, and target market geography.",
        "vi": "Doanh nghiệp lựa chọn giữa bốn kênh phân phối: trực tiếp cho người tiêu dùng để giữ trọn lợi nhuận; qua nhà bán lẻ để tạo thuận tiện mua sắm; qua nhà bán buôn để chia nhỏ lô hàng; hoặc qua đại lý xuất khẩu ra nước ngoài. Quyết định phụ thuộc vào hạn sử dụng của sản phẩm, giá trị đơn vị, độ phức tạp kỹ thuật và vị trí địa lý của thị trường mục tiêu."
    },
    {
        "id": "sec_promotion",
        "title": "4. Chữ P thứ tư: Chiêu thị & Quảng bá (Promotion)",
        "selector": "#sec-promotion",
        "en": "Section 4 covers Promotion: paid advertising, below-the-line sales promotions, personal selling, direct mail, and sponsorships designed to inform and persuade consumers while building enduring brand goodwill.",
        "vi": "Mục bốn bao quát Chiêu thị (Promotion): quảng cáo truyền thông, khuyến mãi bán hàng, chào hàng trực tiếp, gửi thư quảng bá và tài trợ sự kiện nhằm cung cấp thông tin, thuyết phục người tiêu dùng và xây dựng hình ảnh thương hiệu bền vững."
    },
    {
        "id": "card_promotion_types",
        "title": "✨ Các Hình thức Chiêu thị: Quảng cáo, Khuyến mại & Bán hàng trực tiếp",
        "selector": "#card-promotion-types",
        "en": "The promotional mix combines above-the-line informative and persuasive advertising with below-the-line tactics: buy-one-get-one-free sales promotions, coupons, personal selling for high-value items, direct mail, and event sponsorship. Decisions reflect promotional budgets, the product life cycle stage, and target audience media habits.",
        "vi": "Phối thức chiêu thị kết hợp quảng cáo đại chúng (thông tin và thuyết phục) với các hoạt động kích cầu: khuyến mại mua một tặng một, phiếu giảm giá, bán hàng trực tiếp đối với mặt hàng giá trị cao, gửi thư trực tiếp và tài trợ sự kiện. Việc lựa chọn phản ánh ngân sách chiêu thị, giai đoạn vòng đời sản phẩm và thói quen tiếp nhận truyền thông của khách hàng mục tiêu."
    },
    {
        "id": "sec_marketing_tech",
        "title": "5. Công nghệ & Tiếp thị Hỗn hợp (E-Commerce & Social Media)",
        "selector": "#sec-marketing-tech",
        "en": "Section 5 examines Technology in the Marketing Mix, highlighting how e-commerce unlocks global consumer bases 24/7, reduces overhead store costs, and harnesses viral social media promotion—while exposing firms to fierce international competition and cybersecurity risks.",
        "vi": "Mục năm nghiên cứu Công nghệ trong Tiếp thị hỗn hợp, nhấn mạnh thương mại điện tử giúp tiếp cận khách hàng toàn cầu 24/7, giảm chi phí mặt bằng và tận dụng lan tỏa mạng xã hội – đồng thời đặt doanh nghiệp trước cạnh tranh toàn cầu và rủi ro an ninh mạng."
    },
    {
        "id": "card_ecommerce_impact",
        "title": "📱 Tác động của E-commerce & Tiếp thị Mạng xã hội",
        "selector": "#card-ecommerce-impact",
        "en": "E-commerce empowers businesses with 24/7 global reach, lower fixed retail rents, and dynamic targeted marketing via social media algorithms and viral influencers. However, firms face aggressive global price competition, website maintenance overheads, return logistics, and cybersecurity threats.",
        "vi": "Thương mại điện tử mang lại cho doanh nghiệp khả năng tiếp cận toàn cầu 24/7, giảm chi phí thuê mặt bằng cố định và cho phép quảng cáo nhắm mục tiêu linh hoạt qua thuật toán mạng xã hội và người ảnh hưởng. Tuy nhiên, doanh nghiệp phải đương đầu với cạnh tranh giá khốc liệt trên toàn cầu, chi phí bảo trì trang web, xử lý hàng hoàn trả và các mối đe dọa an ninh mạng."
    },
    {
        "id": "sec_recommend_4ps",
        "title": "6. Chiến lược làm bài thi Cambridge: Đề xuất Phối thức Marketing Mix",
        "selector": "#sec-recommend-4ps",
        "en": "Section 6 highlights Cambridge exam strategy for recommending marketing mix decisions. Candidates must ensure full alignment across all four Ps, justify pricing and distribution choices using case study context, respect budgetary limitations, and evaluate potential competitor retaliation.",
        "vi": "Mục sáu nhấn mạnh chiến lược làm bài thi Cambridge khi đề xuất phối thức tiếp thị hỗn hợp. Thí sinh phải bảo đảm sự nhất quán hoàn hảo giữa cả 4 chữ P, giải thích thuyết phục cho lựa chọn giá và kênh phân phối dựa vào bối cảnh đề bài, tôn trọng giới hạn ngân sách và đánh giá phản ứng đáp trả của đối thủ."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_product": {"start": 1, "end": 3},
    "sec_price": {"start": 4, "end": 6},
    "sec_place": {"start": 7, "end": 8},
    "sec_promotion": {"start": 9, "end": 10},
    "sec_marketing_tech": {"start": 11, "end": 12},
    "sec_recommend_4ps": {"start": 13, "end": 13}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">3.3 The Marketing Mix (Tiếp thị Hỗn hợp: 4Ps)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- MARKETING MIX INTRO BOX -->
    <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px 20px; border-radius: 8px; font-size: 16px; color: #1e40af; margin-bottom: 40px;">
        <b>Marketing Mix</b> refers to the different elements involved in the marketing of a good or service – the 4 P’s: <b>Product, Price, Place, and Promotion</b>.
    </div>

    <!-- 1. PRODUCT -->
    <div style="margin-bottom: 50px;">
        <div id="sec-product" class="lecture-interactive-card" data-lecture-section="sec_product" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📦 1. PRODUCT</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Product is the <b>good or service being produced and sold</b> in the market. This includes all its features and final packaging. Types include: <i>consumer goods, consumer services, producer goods, producer services.</i>
            </p>
        </div>

        <!-- Video 1 -->
        <div style="margin: 20px 0 25px 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; background: #0f172a;">
            <div style="padding: 10px 16px; background: #1e293b; color: #f8fafc; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="background: #ef4444; color: #ffffff; padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px;">VIDEO BÀI GIẢNG</span>
                    <span>3.3 Marketing Mix: 1. Product (Sản phẩm)</span>
                </div>
                <a href="https://www.youtube.com/watch?v=ALwDbKo1LZw" target="_blank" style="color: #94a3b8; font-size: 11px; text-decoration: none; display: flex; align-items: center; gap: 4px;">Xem YouTube ↗</a>
            </div>
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #000;">
                <iframe src="https://www.youtube.com/embed/ALwDbKo1LZw?rel=0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>

        <!-- SUB-CARD: NPD & BRAND IMAGE -->
        <div id="card-npd-brand" class="lecture-interactive-card" data-lecture-section="card_npd_brand" style="margin-bottom: 25px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">🚀 New Product Development (NPD) &amp; Brand Image</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 18px; margin-bottom: 20px;">
                <h4 style="margin: 0 0 10px 0; color: #0f172a; font-size: 15px;">🌟 What makes a successful product?</h4>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 13.5px; line-height: 1.6;">
                    <li>Satisfies existing needs and wants of customers.</li>
                    <li>Able to stimulate new wants from consumers.</li>
                    <li>Design (performance, reliability, quality) is consistent with brand image.</li>
                    <li>Distinctive from competitors and stands out.</li>
                    <li>Not too expensive to produce (price covers the costs).</li>
                </ul>
            </div>

            <p style="font-size: 14px; color: #0f172a; font-weight: 700; margin-bottom: 10px;">The 6-step process of developing a new product:</p>
            <ol style="margin: 0 0 20px 0; padding-left: 20px; color: #475569; font-size: 13.5px; line-height: 1.6;">
                <li><b>Generate ideas:</b> Brainstorm using customer/employee suggestions and R&amp;D.</li>
                <li><b>Select the best ideas:</b> Abandon costly or unpopular ideas; research the rest.</li>
                <li><b>Assess sales potential:</b> Forecast sales, market share, and cost-benefit analysis.</li>
                <li><b>Develop a prototype:</b> See how it can be manufactured and fix problems (often 3D computer simulations).</li>
                <li><b>Test launch:</b> Sold to one section of the market (e.g., beta versions for apps).</li>
                <li><b>Full launch:</b> The product is launched to the entire market.</li>
            </ol>

            <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">
                <div style="flex: 1; min-width: 250px; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 15px; border-radius: 8px;">
                    <h4 style="color: #15803d; margin: 0 0 8px 0; font-size: 14px;">✅ Advantages of NPD</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12.5px; line-height: 1.5;">
                        <li>Creates a <b>Unique Selling Point (USP)</b> to charge high prices.</li>
                        <li>Increases potential sales, revenue, and profit.</li>
                        <li>Spreads risks across multiple products.</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; background: #fef2f2; border: 1px solid #fecaca; padding: 15px; border-radius: 8px;">
                    <h4 style="color: #b91c1c; margin: 0 0 8px 0; font-size: 14px;">❌ Disadvantages of NPD</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12.5px; line-height: 1.5;">
                        <li>Market research is expensive and time-consuming.</li>
                        <li>High investment and development costs with risk of failure.</li>
                    </ul>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px;">
                    <h4 style="color: #2563eb; margin: 0 0 6px 0; font-size: 14px;">🏷️ Why Brand Image matters</h4>
                    <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #475569;">Differentiates product from competitors and builds <b>brand loyalty</b>.</p>
                    <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 12px; line-height: 1.5;">
                        <li>Consumers recognize brand instantly.</li>
                        <li>Allows charging higher premium prices.</li>
                        <li>Easier to launch new extensions (e.g., Apple).</li>
                    </ul>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px;">
                    <h4 style="color: #2563eb; margin: 0 0 6px 0; font-size: 14px;">📦 Why Packaging matters</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 12px; line-height: 1.5;">
                        <li>Protects product contents and maintains freshness.</li>
                        <li>Provides vital information (ingredients, warnings, expiry).</li>
                        <li>Aids instant consumer brand recognition on store shelves.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: PLC -->
        <div id="card-plc" class="lecture-interactive-card" data-lecture-section="card_plc" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">📈 Product Life Cycle (PLC) &amp; Extension Strategies</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14px; color: #475569; margin-bottom: 15px;">The stages a product goes through from introduction to retirement in terms of sales. Different stages require different marketing decisions.</p>

            <div style="margin-bottom: 20px; overflow-x: auto;">
                <svg viewBox="0 0 700 320" width="100%" style="min-width: 600px; background:#ffffff; border-radius:12px; border:1px solid #cbd5e1; font-family: Arial, sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: block;">
                    <line x1="60" y1="260" x2="660" y2="260" stroke="#334155" stroke-width="2"></line>
                    <line x1="60" y1="40" x2="60" y2="260" stroke="#334155" stroke-width="2"></line>
                    <text x="350" y="300" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Time</text>
                    <text x="30" y="150" transform="rotate(-90 30,150)" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Sales / Profits</text>

                    <line x1="180" y1="40" x2="180" y2="260" stroke="#94a3b8" stroke-dasharray="5,5"></line>
                    <text x="120" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#64748b">Introduction</text>

                    <line x1="330" y1="40" x2="330" y2="260" stroke="#94a3b8" stroke-dasharray="5,5"></line>
                    <text x="255" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#64748b">Growth</text>

                    <line x1="510" y1="40" x2="510" y2="260" stroke="#94a3b8" stroke-dasharray="5,5"></line>
                    <text x="420" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#64748b">Maturity</text>

                    <text x="585" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#64748b">Decline</text>

                    <line x1="60" y1="220" x2="660" y2="220" stroke="#cbd5e1" stroke-width="1"></line>
                    <text x="50" y="224" text-anchor="end" font-size="12" fill="#94a3b8">0</text>

                    <path d="M 60 255 Q 150 250, 200 150 T 330 60 Q 420 40, 510 80 T 660 240" fill="none" stroke="#2563eb" stroke-width="4"></path>
                    <text x="400" y="45" fill="#2563eb" font-size="14" font-weight="bold">Sales</text>

                    <path d="M 60 250 Q 120 280, 180 220 T 330 110 Q 420 80, 510 140 T 660 220" fill="none" stroke="#10b981" stroke-width="3" stroke-dasharray="6,4"></path>
                    <text x="350" y="135" fill="#059669" font-size="14" font-weight="bold">Profit</text>
                </svg>
            </div>

            <div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 20px;">
                <table style="width: 100%; border-collapse: collapse; min-width: 650px; text-align: left; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                            <th style="padding: 10px; color: #0f172a;">Marketing Mix</th>
                            <th style="padding: 10px; color: #475569; border-left: 1px solid #e2e8f0;">Introduction</th>
                            <th style="padding: 10px; color: #475569; border-left: 1px solid #e2e8f0;">Growth</th>
                            <th style="padding: 10px; color: #475569; border-left: 1px solid #e2e8f0;">Maturity</th>
                            <th style="padding: 10px; color: #475569; border-left: 1px solid #e2e8f0;">Decline</th>
                        </tr>
                    </thead>
                    <tbody style="color: #475569;">
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; font-weight: bold; color: #2563eb;">Product</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Basic model</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Add features / variations</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Extension strategies</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Phase out slow items</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                            <td style="padding: 10px; font-weight: bold; color: #059669;">Price</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Skimming or Penetration</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Maintain or reduce slightly</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Competitive / Promotional</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Discount to clear stock</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; font-weight: bold; color: #d97706;">Place</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Selective distribution</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Intensive distribution</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Widest network possible</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Focus on loyal outlets</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; color: #db2777;">Promotion</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">High informative ads</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Brand building / Persuasive</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Sales promo &amp; Loyalty</td>
                            <td style="padding: 10px; border-left: 1px solid #e2e8f0;">Cut advertising spending</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #6366f1; padding: 18px; border-radius: 4px;">
                <h4 style="margin: 0 0 8px 0; color: #4338ca; font-size: 15px;">🔄 Extension Strategies</h4>
                <p style="margin: 0 0 12px 0; font-size: 13.5px; color: #475569;">Marketing techniques used to extend the maturity stage of a product:</p>
                <ul style="margin: 0 0 16px 0; padding-left: 20px; color: #475569; font-size: 13px;">
                    <li>Finding new markets or new uses for the product.</li>
                    <li>Redesigning the product or packaging to improve appeal.</li>
                    <li>Increasing advertising and promotional activities.</li>
                </ul>

                <div style="overflow-x: auto;">
                    <svg viewBox="0 0 500 220" width="100%" style="min-width: 450px; background:#ffffff; border-radius:8px; border:1px solid #cbd5e1; font-family: Arial, sans-serif; display: block;">
                        <line x1="40" y1="180" x2="460" y2="180" stroke="#334155" stroke-width="2"></line>
                        <line x1="40" y1="20" x2="40" y2="180" stroke="#334155" stroke-width="2"></line>
                        <text x="250" y="210" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">Time</text>
                        <text x="20" y="100" transform="rotate(-90 20,100)" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">Sales</text>

                        <path d="M 40 170 Q 120 170, 180 80 T 300 40" fill="none" stroke="#2563eb" stroke-width="4"></path>
                        <path d="M 300 40 Q 360 50, 420 120" fill="none" stroke="#94a3b8" stroke-width="3" stroke-dasharray="5,5"></path>
                        <text x="430" y="130" font-size="11" fill="#64748b">Original Decline</text>

                        <path d="M 270 45 Q 340 10, 430 20" fill="none" stroke="#10b981" stroke-width="3"></path>
                        <text x="440" y="25" font-size="11" font-weight="bold" fill="#059669">Extension 1</text>

                        <path d="M 290 42 Q 350 25, 430 50" fill="none" stroke="#f59e0b" stroke-width="3"></path>
                        <text x="440" y="55" font-size="11" font-weight="bold" fill="#d97706">Extension 2</text>
                    </svg>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. PRICE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-price" class="lecture-interactive-card" data-lecture-section="sec_price" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💰 2. PRICE</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Price is the amount of money producers are willing to sell or consumers are willing to buy the product for.
            </p>
        </div>

        <!-- Video 2 -->
        <div style="margin: 20px 0 25px 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; background: #0f172a;">
            <div style="padding: 10px 16px; background: #1e293b; color: #f8fafc; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="background: #ef4444; color: #ffffff; padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px;">VIDEO BÀI GIẢNG</span>
                    <span>3.3 Marketing Mix: 2. Price (Chiến lược giá)</span>
                </div>
                <a href="https://www.youtube.com/watch?v=OPpGREn5pIg" target="_blank" style="color: #94a3b8; font-size: 11px; text-decoration: none; display: flex; align-items: center; gap: 4px;">Xem YouTube ↗</a>
            </div>
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #000;">
                <iframe src="https://www.youtube.com/embed/OPpGREn5pIg?rel=0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>

        <!-- SUB-CARD: PRICING METHODS -->
        <div id="card-pricing-methods" class="lecture-interactive-card" data-lecture-section="card_pricing_methods" style="margin-bottom: 25px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #047857; font-weight: 700;">💵 Methods of Pricing</h3>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                    <h4 style="margin: 0 0 4px 0; color: #059669; font-size: 15px;">1. Market Skimming</h4>
                    <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #475569;">Setting high price for a new, unique product.</p>
                    <div style="font-size: 11.5px; color: #475569;">
                        <b style="color: #16a34a;">✅ Pros:</b> High profit; recovers R&amp;D costs.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Fails if rivals sell cheaper copies.
                    </div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                    <h4 style="margin: 0 0 4px 0; color: #059669; font-size: 15px;">2. Penetration Pricing</h4>
                    <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #475569;">Setting very low price to attract customers.</p>
                    <div style="font-size: 11.5px; color: #475569;">
                        <b style="color: #16a34a;">✅ Pros:</b> Wins market share quickly.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Low revenue; slow to cover costs.
                    </div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                    <h4 style="margin: 0 0 4px 0; color: #059669; font-size: 15px;">3. Competitive Pricing</h4>
                    <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #475569;">Setting price similar to market competitors.</p>
                    <div style="font-size: 11.5px; color: #475569;">
                        <b style="color: #16a34a;">✅ Pros:</b> Compete on service/quality.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Still requires extra promos to win sales.
                    </div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                    <h4 style="margin: 0 0 4px 0; color: #059669; font-size: 15px;">4. Cost-plus Pricing</h4>
                    <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #475569;">Adding a markup amount to manufacturing cost.</p>
                    <div style="font-size: 11.5px; color: #475569;">
                        <b style="color: #16a34a;">✅ Pros:</b> Easy to calculate; covers costs.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> May exceed consumer willingness to pay.
                    </div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                    <h4 style="margin: 0 0 4px 0; color: #059669; font-size: 15px;">5. Promotional / Loss Leader</h4>
                    <p style="margin: 0 0 8px 0; font-size: 12.5px; color: #475569;">Setting price below cost to draw customers in.</p>
                    <div style="font-size: 11.5px; color: #475569;">
                        <b style="color: #16a34a;">✅ Pros:</b> Sells excess stock; boosts footfall.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Thins margins if customers buy nothing else.
                    </div>
                </div>
            </div>

            <div style="background: #fff7ed; border: 1px solid #fed7aa; padding: 16px; border-radius: 8px;">
                <h4 style="color: #c2410c; margin: 0 0 8px 0; font-size: 14px;">🤔 What affects pricing methods?</h4>
                <ul style="margin: 0; padding-left: 18px; color: #9a3412; font-size: 12.5px; line-height: 1.5;">
                    <li><b>New or existing?</b> New = Skimming/Penetration. Existing = Competitive/Promotional.</li>
                    <li><b>Is it unique?</b> Yes = Skimming.</li>
                    <li><b>Level of competition?</b> High = Competitive.</li>
                    <li><b>Brand image?</b> Strong brand = Skimming.</li>
                    <li><b>Costs?</b> High costs = Cost-plus. Low costs = Penetration/Promotional.</li>
                    <li><b>Objectives?</b> Quick market share = Penetration. Maintain sales = Competitive.</li>
                </ul>
            </div>
        </div>

        <!-- SUB-CARD: PED -->
        <div id="card-ped" class="lecture-interactive-card" data-lecture-section="card_ped" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #047857; font-weight: 700;">📊 Price Elasticity of Demand (PED)</h3>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>
            <p style="margin: 0 0 10px 0; font-size: 14px; color: #475569;">Responsiveness of quantity demanded to changes in price.</p>
            <div style="background: #ccfbf1; color: #0f766e; padding: 12px; font-weight: bold; text-align: center; border-radius: 8px; margin-bottom: 16px; font-size: 15px;">
                PED = % change in quantity demanded / % change in price
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 14px;">
                    <b style="color: #15803d; font-size: 14px;">Elastic Demand (PED &gt; 1):</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">
                        High % change in demand. Customers sensitive to price.<br/>
                        <b>Strategy:</b> <b>Lower prices</b> to heavily expand demand and revenue.
                    </p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 14px;">
                    <b style="color: #15803d; font-size: 14px;">Inelastic Demand (PED &lt; 1):</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">
                        Low % change in demand. Essential good with few substitutes.<br/>
                        <b>Strategy:</b> <b>Raise prices</b> to increase total revenue without losing customers.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. PLACE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-place" class="lecture-interactive-card" data-lecture-section="sec_place" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📍 3. PLACE</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Place refers to how the product is distributed from the producer to the final consumer (Distribution Channels).
            </p>
        </div>

        <!-- Video 3 -->
        <div style="margin: 20px 0 25px 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; background: #0f172a;">
            <div style="padding: 10px 16px; background: #1e293b; color: #f8fafc; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="background: #ef4444; color: #ffffff; padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px;">VIDEO BÀI GIẢNG</span>
                    <span>3.3 Marketing Mix: 3. Place (Kênh phân phối)</span>
                </div>
                <a href="https://www.youtube.com/watch?v=aeZ4oBioUMY" target="_blank" style="color: #94a3b8; font-size: 11px; text-decoration: none; display: flex; align-items: center; gap: 4px;">Xem YouTube ↗</a>
            </div>
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #000;">
                <iframe src="https://www.youtube.com/embed/aeZ4oBioUMY?rel=0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>

        <!-- SUB-CARD: DISTRIBUTION CHANNELS -->
        <div id="card-distribution-channels" class="lecture-interactive-card" data-lecture-section="card_distribution_channels" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fde68a; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #b45309; font-weight: 700;">🚚 4 Channels of Distribution</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fffbeb; color: #d97706; padding: 4px 10px; border-radius: 6px; border: 1px solid #fde68a;">Nghe thẻ này</span>
            </div>

            <div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 20px;">
                <table style="width: 100%; border-collapse: collapse; min-width: 700px; text-align: left; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #fef3c7; border-bottom: 2px solid #fde68a;">
                            <th style="padding: 12px; color: #92400e; width: 22%;">Channel</th>
                            <th style="padding: 12px; color: #92400e; width: 28%;">Explanation</th>
                            <th style="padding: 12px; color: #166534; width: 25%;">✅ Advantages</th>
                            <th style="padding: 12px; color: #991b1b; width: 25%;">❌ Disadvantages</th>
                        </tr>
                    </thead>
                    <tbody style="color: #475569;">
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 12px; font-weight: bold;">1. Producer ➔ Consumer</td>
                            <td style="padding: 12px;">Sold straight from factory or online.</td>
                            <td style="padding: 12px;">All profit kept; complete marketing control.</td>
                            <td style="padding: 12px;">High delivery &amp; storage costs.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 12px; font-weight: bold;">2. Producer ➔ Retailer ➔ Consumer</td>
                            <td style="padding: 12px;">Sold to retailer who stocks store shelves.</td>
                            <td style="padding: 12px;">Retailer pays storage &amp; promos; convenient for buyers.</td>
                            <td style="padding: 12px;">Retailer takes profit markup; sells rival brands.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 12px; font-weight: bold;">3. Producer ➔ Wholesaler ➔ Retailer ➔ Consumer</td>
                            <td style="padding: 12px;">Wholesaler buys bulk and breaks bulk for retailers.</td>
                            <td style="padding: 12px;">Wholesaler pays transport &amp; storage.</td>
                            <td style="padding: 12px;">Multiple middlemen take profit cuts; loss of control.</td>
                        </tr>
                        <tr>
                            <td style="padding: 12px; font-weight: bold;">4. Producer ➔ Agent ➔ Wholesaler...</td>
                            <td style="padding: 12px;">Agent with market contacts handles foreign exports.</td>
                            <td style="padding: 12px;">Deep specialist knowledge of foreign markets.</td>
                            <td style="padding: 12px;">Highest profit deduction by intermediary agents.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="background: #f8fafc; border-left: 4px solid #f59e0b; padding: 15px 18px; border-radius: 4px;">
                <h4 style="margin: 0 0 8px 0; color: #b45309; font-size: 14px;">🔍 What affects place decisions?</h4>
                <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 12.5px; line-height: 1.5;">
                    <li><b>Type of product:</b> Producer goods = direct/wholesaler. Consumer goods = retail.</li>
                    <li><b>Technicality:</b> Highly technical = direct selling to explain features.</li>
                    <li><b>Purchase frequency:</b> Daily goods need widespread retail stores.</li>
                    <li><b>Price:</b> Luxury goods need specialist, high-end outlets.</li>
                    <li><b>Durability:</b> Perishables need wide retail networks to sell quickly.</li>
                    <li><b>Customer location:</b> Global customers require e-commerce.</li>
                    <li><b>Competitors:</b> Sell where competitors sell to directly compete.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 4. PROMOTION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-promotion" class="lecture-interactive-card" data-lecture-section="sec_promotion" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📣 4. PROMOTION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Marketing activities used to communicate with customers to inform and persuade them to buy. Aims include informing, persuading, creating brand image, and increasing sales/market share.
            </p>
        </div>

        <!-- Video 4 -->
        <div style="margin: 20px 0 25px 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; background: #0f172a;">
            <div style="padding: 10px 16px; background: #1e293b; color: #f8fafc; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="background: #ef4444; color: #ffffff; padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px;">VIDEO BÀI GIẢNG</span>
                    <span>3.3 Marketing Mix: 4. Promotion (Chiến dịch xúc tiến/quảng bá)</span>
                </div>
                <a href="https://www.youtube.com/watch?v=Zbn6fqHmNT0" target="_blank" style="color: #94a3b8; font-size: 11px; text-decoration: none; display: flex; align-items: center; gap: 4px;">Xem YouTube ↗</a>
            </div>
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #000;">
                <iframe src="https://www.youtube.com/embed/Zbn6fqHmNT0?rel=0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>

        <!-- SUB-CARD: PROMOTION TYPES -->
        <div id="card-promotion-types" class="lecture-interactive-card" data-lecture-section="card_promotion_types" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #db2777; font-weight: 700;">✨ Types of Promotion</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fdf2f8; color: #db2777; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <h4 style="margin: 0 0 4px 0; color: #db2777; font-size: 15px;">📺 Advertising (Above-the-line)</h4>
                    <p style="margin: 0 0 10px 0; font-size: 12.5px; color: #475569;">Paid mass communication via TV, radio, print, and billboards.</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 4px; font-size: 11px;">
                        <span style="background: #ffffff; border: 1px solid #fbcfe8; padding: 3px 6px; border-radius: 4px; color: #be185d;">1. Objectives</span> ➔
                        <span style="background: #ffffff; border: 1px solid #fbcfe8; padding: 3px 6px; border-radius: 4px; color: #be185d;">2. Budget</span> ➔
                        <span style="background: #ffffff; border: 1px solid #fbcfe8; padding: 3px 6px; border-radius: 4px; color: #be185d;">3. Campaign</span> ➔
                        <span style="background: #ffffff; border: 1px solid #fbcfe8; padding: 3px 6px; border-radius: 4px; color: #be185d;">4. Media</span>
                    </div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <h4 style="margin: 0 0 4px 0; color: #db2777; font-size: 15px;">🎁 Sales Promotion (Below-the-line)</h4>
                    <p style="margin: 0; font-size: 12.5px; color: #475569;">BOGO discounts, point-of-sale displays, coupons, free samples to spark instant buying.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <h4 style="margin: 0 0 4px 0; color: #db2777; font-size: 15px;">🤝 Personal Selling</h4>
                    <p style="margin: 0; font-size: 12.5px; color: #475569;">Sales staff negotiate directly with buyers, forming long-term B2B relationships.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <h4 style="margin: 0 0 4px 0; color: #db2777; font-size: 15px;">✉️ Direct Mail</h4>
                    <p style="margin: 0; font-size: 12.5px; color: #475569;">Brochures, catalog mailings, and email newsletters sent directly to addresses.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <h4 style="margin: 0 0 4px 0; color: #db2777; font-size: 15px;">⚽ Sponsorship</h4>
                    <p style="margin: 0; font-size: 12.5px; color: #475569;">Financial support linking a brand to athletes, teams, or cultural events for prestige.</p>
                </div>
            </div>

            <div style="background: #fdf2f8; border-left: 4px solid #db2777; padding: 15px 18px; border-radius: 4px;">
                <h4 style="margin: 0 0 8px 0; color: #9d174d; font-size: 14px;">🤔 What affects promotional decisions?</h4>
                <ul style="margin: 0; padding-left: 18px; color: #831843; font-size: 12.5px; line-height: 1.5;">
                    <li><b>Stage of the PLC:</b> Heavy informative launch vs defensive loyalty reminder.</li>
                    <li><b>Nature of product:</b> Consumer goods use persuasive mass ads; producer goods use bulk price deals.</li>
                    <li><b>Target market:</b> Mass market vs niche specialist magazines.</li>
                    <li><b>Cost-effectiveness:</b> Expected sales must exceed campaign budget costs.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 5. TECHNOLOGY & MARKETING MIX -->
    <div style="margin-bottom: 50px;">
        <div id="sec-marketing-tech" class="lecture-interactive-card" data-lecture-section="sec_marketing_tech" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #0284c7; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🌐 5. TECHNOLOGY AND THE MARKETING MIX</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                <b>E-commerce</b> is the buying and selling of goods and services using the internet and digital electronic systems.
            </p>
        </div>

        <!-- Video 5 -->
        <div style="margin: 20px 0 25px 0; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; background: #0f172a;">
            <div style="padding: 10px 16px; background: #1e293b; color: #f8fafc; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: space-between;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="background: #ef4444; color: #ffffff; padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px;">VIDEO BÀI GIẢNG</span>
                    <span>3.3 Marketing Mix: 5. Technology & Marketing Mix (Thương mại điện tử & MXH)</span>
                </div>
                <a href="https://www.youtube.com/watch?v=PXbnxsks8OY" target="_blank" style="color: #94a3b8; font-size: 11px; text-decoration: none; display: flex; align-items: center; gap: 4px;">Xem YouTube ↗</a>
            </div>
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #000;">
                <iframe src="https://www.youtube.com/embed/PXbnxsks8OY?rel=0" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>

        <!-- SUB-CARD: ECOMMERCE IMPACT -->
        <div id="card-ecommerce-impact" class="lecture-interactive-card" data-lecture-section="card_ecommerce_impact" style="margin-bottom: 25px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #bae6fd; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #0284c7; font-weight: 700;">📱 Impact of E-commerce &amp; Social Media</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 4px 10px; border-radius: 6px; border: 1px solid #bae6fd;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #0284c7; font-size: 15px; margin: 0 0 8px 0;">🏢 Impact on Businesses</h4>
                    <div style="font-size: 12.5px; line-height: 1.5; color: #334155;">
                        <b style="color: #16a34a;">✅ Opportunities:</b>
                        <ul style="margin: 4px 0 8px 0; padding-left: 18px;">
                            <li>Global customer reach without physical stores.</li>
                            <li>Lower fixed overhead rents and retail wages.</li>
                            <li>Customer analytics to personalize promotions.</li>
                        </ul>
                        <b style="color: #dc2626;">❌ Threats:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 18px;">
                            <li>Global price competition from mega-retailers.</li>
                            <li>High software maintenance, security, return costs.</li>
                        </ul>
                    </div>
                </div>

                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #0284c7; font-size: 15px; margin: 0 0 8px 0;">🛍️ Impact on Consumers</h4>
                    <div style="font-size: 12.5px; line-height: 1.5; color: #334155;">
                        <b style="color: #16a34a;">✅ Opportunities:</b>
                        <ul style="margin: 4px 0 8px 0; padding-left: 18px;">
                            <li>Convenient 24/7 shopping and home delivery.</li>
                            <li>Easy price comparison across multiple vendors.</li>
                            <li>Vast international variety available.</li>
                        </ul>
                        <b style="color: #dc2626;">❌ Threats:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 18px;">
                            <li>Fraud risk; shipping delays; return hassles.</li>
                            <li>Cannot touch or test product before purchase.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 8px; padding: 15px;">
                <h4 style="color: #be185d; font-size: 15px; margin: 0 0 6px 0;">📱 Social Media Promotion &amp; Viral Marketing</h4>
                <p style="margin: 0; font-size: 13px; color: #475569; line-height: 1.5;">
                    Businesses leverage Instagram, TikTok, and YouTube to reach targeted demographics cost-effectively. Influencer partnerships and shareable viral videos propagate brand messages organically at low incremental cost.
                </p>
            </div>
        </div>

        <!-- 6. CAMBRIDGE EXAM EVALUATION (SUB-CARD / SECTION) -->
        <div id="sec-recommend-4ps" class="lecture-interactive-card" data-lecture-section="sec_recommend_4ps" style="padding: 22px 24px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="color: #1e3a8a; margin: 0; font-size: 18px; font-weight: 700;">
                    🎯 Cambridge Exam Strategy: Recommending 4Ps Marketing Mix
                </h3>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 13.5px; color: #1e40af; margin-bottom: 16px; line-height: 1.5;">
                In 12-mark evaluation questions, candidates must recommend a cohesive marketing strategy where all 4 elements mutually reinforce each other:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #10b981;">
                    <b style="color: #047857; font-size: 14px;">Recommending Pricing:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        • <b>Skimming:</b> For innovative, highly differentiated tech with few rivals.<br/>
                        • <b>Penetration:</b> For highly competitive mass markets with price-sensitive buyers.<br/>
                        • <b>Competitive:</b> For mature markets where goods are standardized.
                    </p>
                </div>
                <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                    <b style="color: #b45309; font-size: 14px;">Recommending Distribution:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        • <b>Direct to Consumer:</b> For perishables, customized items, or software.<br/>
                        • <b>Via Retailer:</b> For bulky consumer goods like furniture or clothing.<br/>
                        • <b>Via Wholesaler:</b> For low-cost daily impulse items like candy.
                    </p>
                </div>
            </div>
        </div>
    </div>

</div>"""
    return html

# ==============================================================================
# 3. GENERATE NEW HTML FOR PAGE 2 (BILINGUAL)
# ==============================================================================
def build_page_2_html(original_p2):
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">3.3 The Marketing Mix (Tiếp thị Hỗn hợp: 4Ps)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 3.3 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/3_3_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 3.3 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
