import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 6.3 ID
LID = '1bc6f5c1-e71b-4d0d-8153-d2f74180a845'
CODE = '6_3'
TITLE = '6.3. Business and globalisation'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL AUDIO SEGMENTS FOR LESSON 6.3
# ==============================================================================
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
        "title": "1. Bản chất & Động lực Toàn cầu hóa",
        "selector": "#sec-globalisation",
        "en": "Section 1 defines Globalisation as the increasing integration and interdependence of world economies through trade, capital flows, and technology. Drivers include reduced transport container shipping costs, free trade agreements, and global internet e-commerce platforms.",
        "vi": "Mục một định nghĩa Toàn cầu hóa là sự gia tăng hội nhập và phụ thuộc lẫn nhau giữa các nền kinh tế trên thế giới qua thương mại, luân chuyển vốn và công nghệ. Các động lực chính gồm chi phí vận tải container giảm, các hiệp định thương mại tự do và sự phát triển của thương mại điện tử toàn cầu."
    },
    {
        "id": "card_globalisation_drivers",
        "title": "🚀 Động Lực Toàn Cầu Hóa & Khái Niệm Xuất Nhập Khẩu",
        "selector": "#card-globalisation-drivers",
        "en": "Drivers and Dynamics of Globalisation: Technological innovation in communication, worldwide trade liberalisation removing tariffs, efficient container shipping networks, and open foreign investment policies have integrated national economies into a single global marketplace.",
        "vi": "Động lực của Toàn cầu hóa: Đột phá công nghệ truyền thông và internet, tự do hóa thương mại dỡ bỏ hàng rào thuế quan, mạng lưới vận tải container siêu rẻ và các cải cách mở cửa thu hút FDI đã hợp nhất các nền kinh tế quốc gia thành một thị trường toàn cầu gắn kết."
    },
    {
        "id": "card_globalisation_impacts",
        "title": "⚖️ Cơ Hội & Thách Thức của Toàn Cầu Hóa",
        "selector": "#card-globalisation-impacts",
        "en": "Opportunities versus Threats: Globalisation unlocks massive overseas customer bases and access to low-cost foreign resources, but simultaneously exposes domestic businesses to fierce competition from global giants with overwhelming economies of scale.",
        "vi": "Cơ hội đối đầu Thách thức: Toàn cầu hóa mở ra thị trường khách hàng quốc tế rộng lớn và nguồn nguyên liệu ngoại giá rẻ, nhưng đồng thời khiến doanh nghiệp trong nước phải đối mặt với sự cạnh tranh khốc liệt từ các tập đoàn toàn cầu có lợi thế kinh tế theo quy mô vượt trội."
    },
    {
        "id": "sec_tariffs_quotas",
        "title": "2. Bảo hộ Thương mại: Thuế quan và Hạn ngạch (Tariffs & Quotas)",
        "selector": "#sec-tariffs-quotas",
        "en": "Section 2 investigates trade protectionism: Import Tariffs—taxes levied on imported foreign goods to make them more expensive than domestic products; and Import Quotas—physical quantitative ceilings on the volume of foreign goods allowed into the country.",
        "vi": "Mục hai nghiên cứu các biện pháp bảo hộ mậu dịch: Thuế quan nhập khẩu (Import Tariffs) là thuế đánh vào hàng hóa nước ngoài để làm tăng giá bán so với hàng nội địa; và Hạn ngạch nhập khẩu (Import Quotas) là giới hạn định lượng về số lượng sản phẩm nhập khẩu tối đa được phép đưa vào thị trường trong nước."
    },
    {
        "id": "card_protectionism_tools",
        "title": "🚧 So Sánh Thuế Quan Nhập Khẩu & Hạn Ngạch Bảo Hộ",
        "selector": "#card-protectionism-tools",
        "en": "Tariffs versus Quotas: An import tariff is an ad valorem tax raising import prices to protect fledgling domestic industries, while an import quota establishes a physical quantitative ceiling on foreign goods, spurring local production but restricting consumer choice.",
        "vi": "Thuế quan so với Hạn ngạch: Thuế quan là khoản thuế đánh vào hàng nhập khẩu nhằm tăng giá bán để bảo vệ các ngành công nghiệp non trẻ nội địa, trong khi hạn ngạch áp đặt trần định lượng số lượng tối đa hàng ngoại, thúc đẩy sản xuất trong nước nhưng giới hạn sự lựa chọn của người tiêu dùng."
    },
    {
        "id": "sec_mncs",
        "title": "3. Tập đoàn Đa quốc gia (Multinational Corporations - MNCs)",
        "selector": "#sec-mncs",
        "en": "Section 3 examines Multinational Corporations: businesses that possess manufacturing operations or service branches in more than one country. Motives for foreign direct investment include slashing labor costs, avoiding import tariffs, and accessing local mineral resources.",
        "vi": "Mục ba xem xét các Tập đoàn đa quốc gia (MNCs): doanh nghiệp có cơ sở sản xuất hoặc chi nhánh dịch vụ tại nhiều hơn một quốc gia. Động lực đầu tư trực tiếp nước ngoài (FDI) gồm cắt giảm chi phí nhân công, vượt qua hàng rào thuế quan và tiếp cận trực tiếp nguồn tài nguyên thiên nhiên bản địa."
    },
    {
        "id": "card_mnc_strategy",
        "title": "✨ Lợi Ích & Động Cơ Trở Thành Tập Đoàn Đa Quốc Gia",
        "selector": "#card-mnc-strategy",
        "en": "Strategic Rationale of Multinationals: Firms expand globally to capture massive economies of scale, diversify market risks across borders, bypass trade protectionist tariffs through domestic production, and secure favourable corporate tax rates.",
        "vi": "Chiến lược trở thành Tập đoàn Đa quốc gia: Doanh nghiệp vươn ra toàn cầu nhằm khai thác tối đa lợi thế quy mô, phân tán rủi ro thị trường qua nhiều quốc gia, vượt qua hàng rào thuế quan bằng cách đặt nhà máy tại chỗ và hưởng các mức thuế thu nhập ưu đãi."
    },
    {
        "id": "card_mnc_stakeholders",
        "title": "🤝 Tác Động Của MNCs Lên Các Bên Liên Quan (Stakeholders)",
        "selector": "#card-mnc-stakeholders",
        "en": "Stakeholder Trade-offs: While employees gain structured training and suppliers experience heightened order volumes, multinationals often exert aggressive price pressure on suppliers and may crowd out domestic businesses, creating market dominance.",
        "vi": "Tác động đa chiều lên các bên liên quan: Người lao động được đào tạo chuyên môn bài bản và nhà cung ứng có thêm đơn hàng lớn, song các tập đoàn đa quốc gia cũng thường ép giá nhà cung cấp nội địa và có thể đẩy các doanh nghiệp nhỏ bản địa vào bước đường phá sản."
    },
    {
        "id": "sec_impact_host_countries",
        "title": "4. Tác động của MNCs lên Quốc gia Sở tại",
        "selector": "#sec-impact-host-countries",
        "en": "Section 4 weighs the benefits and drawbacks of MNCs on host nations. Benefits include generating employment, transferring modern industrial skills, and paying corporate taxes. Drawbacks include driving local indigenous competitors out of business, repatriating profits back to foreign headquarters, and exploiting lax environmental standards.",
        "vi": "Mục bốn cân nhắc mặt tích cực và tiêu cực của MNCs đối với nước sở tại. Mặt tích cực gồm tạo việc làm cho lao động địa phương, chuyển giao công nghệ kỹ thuật và đóng góp thuế cho ngân sách. Mặt tiêu cực gồm đè bẹp các doanh nghiệp bản địa, chuyển toàn bộ lợi nhuận về nước mẹ và khai thác lỗ hổng môi trường."
    },
    {
        "id": "card_host_eval",
        "title": "🛬 Đánh Giá Lợi Ích & Bất Lợi Đối Với Quốc Gia Sở Tại (Host Countries)",
        "selector": "#card-host-eval",
        "en": "Evaluating Impacts on Host Economies: Developing nations enjoy capital injections, infrastructure improvements, and technological transfers, yet face profit repatriation, potential depletion of non-renewable national resources, and aggressive transfer pricing schemes.",
        "vi": "Đánh giá Tác động lên Nước sở tại: Các quốc gia đang phát triển hưởng lợi từ dòng vốn FDI, nâng cấp cơ sở hạ tầng và chuyển giao công nghệ mới, nhưng cũng đối mặt với nguy cơ bị chuyển toàn bộ lợi nhuận về nước mẹ, cạn kiệt tài nguyên thiên nhiên và các thủ thuật chuyển giá trốn thuế."
    },
    {
        "id": "sec_exchange_rates",
        "title": "5. Biến động Tỷ giá Hối đoái và Quy tắc SPICED",
        "selector": "#sec-exchange-rates",
        "en": "Section 5 analyzes exchange rate currency fluctuations using the famous Cambridge mnemonic: SPICED—Stronger Pound Imports Cheaper, Exports Dearer. A currency appreciation makes imported raw materials cheaper but reduces overseas price competitiveness for domestic exporters.",
        "vi": "Mục năm phân tích biến động tỷ giá hối đoái thông qua quy tắc ghi nhớ Cambridge SPICED: Đồng nội tệ tăng giá làm cho hàng nhập khẩu rẻ hơn nhưng hàng xuất khẩu trở nên đắt đỏ hơn. Ngược lại, đồng nội tệ giảm giá kích thích xuất khẩu nhưng làm tăng chi phí nhập khẩu nguyên liệu từ nước ngoài."
    },
    {
        "id": "card_spiced_rules",
        "title": "💱 Phân Tích Quy Tắc SPICED & Tác Động Xuất Nhập Khẩu",
        "selector": "#card-spiced-rules",
        "en": "The SPICED and WPIDEC Rules: Under a strong domestic currency, imports become cheaper but exports dearer, hurting exporters while rewarding importers. Conversely, currency depreciation makes exports cheaper and competitive abroad, but spikes domestic import costs.",
        "vi": "Quy tắc SPICED và WPIDEC: Khi đồng nội tệ tăng giá (SPICED), hàng nhập khẩu rẻ hơn nhưng hàng xuất khẩu trở nên đắt đỏ, gây bất lợi cho xuất khẩu nhưng có lợi cho nhập khẩu. Ngược lại khi nội tệ giảm giá (WPIDEC), hàng xuất khẩu rẻ và đắt khách ở nước ngoài, nhưng chi phí nhập khẩu nguyên liệu tăng vọt."
    },
    {
        "id": "sec_recommend_globalisation",
        "title": "6. Chiến lược làm bài thi Cambridge: Đánh giá Tác động của MNCs",
        "selector": "#sec-recommend-globalisation",
        "en": "Section 6 presents the Cambridge evaluation formula for globalization case studies. Candidates must balance national economic growth against sovereignty, environmental degradation, and profit repatriation before delivering a balanced final judgement.",
        "vi": "Mục sáu cung cấp công thức đánh giá toàn diện đề thi Cambridge cho các bài tập tình huống toàn cầu hóa. Thí sinh phải cân nhắc giữa lợi ích tăng trưởng kinh tế, việc làm với các nguy cơ ô nhiễm môi trường và chuyển giá lợi nhuận trước khi đưa ra nhận định tổng kết xác đáng."
    },
    {
        "id": "card_cambridge_global_strategy",
        "title": "🎯 Kỹ Năng Đánh Giá & Ra Quyết Định Đề Thi Cambridge",
        "selector": "#card-cambridge-global-strategy",
        "en": "Exam Synthesis and Judgement: In 6-mark and 12-mark questions, evaluate how multinational expansion interacts with macroeconomic factors, supporting your final recommendation with contextual evidence regarding exchange rates, employment, and profit retention.",
        "vi": "Chiến lược làm bài thi Cambridge: Trong các câu hỏi tự luận 6 điểm và 12 điểm, hãy đánh giá tác động tương hỗ giữa mở rộng đa quốc gia với các yếu tố kinh tế vĩ mô, củng cố kết luận bằng dẫn chứng thực tế về tỷ giá, tạo việc làm và tỷ lệ lợi nhuận được giữ lại tại địa phương."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_globalisation": {"start": 1, "end": 3},
    "sec_tariffs_quotas": {"start": 4, "end": 5},
    "sec_mncs": {"start": 6, "end": 8},
    "sec_impact_host_countries": {"start": 9, "end": 10},
    "sec_exchange_rates": {"start": 11, "end": 12},
    "sec_recommend_globalisation": {"start": 13, "end": 14}
}

# ==============================================================================
# 2. GENERATE NEW HTML FOR PAGE 1
# ==============================================================================
def build_page_1_html():
    html = """<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- HEADER CARD -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="margin-bottom: 35px; padding: 22px 25px; background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%); border-radius: 14px; border: 1.5px solid #7dd3fc; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <span style="display: inline-block; font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #0284c7; background: #e0f2fe; padding: 4px 10px; border-radius: 999px; margin-bottom: 6px;">Cambridge IGCSE Business Studies • Chapter 6.3</span>
                <h1 style="margin: 0; font-size: 24px; font-weight: 800; color: #0f172a;">Business &amp; The International Economy</h1>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; background: white; padding: 8px 14px; border-radius: 999px; border: 1px solid #bae6fd; font-size: 13px; font-weight: 700; color: #0369a1;">
                <span>🎙️ Bài giảng tương tác song ngữ</span>
            </div>
        </div>
        <p style="margin: 10px 0 0 0; font-size: 14px; color: #334155; line-height: 1.5;">
            Khảo sát toàn cầu hóa, thuế quan và hạn ngạch bảo hộ, sự bành trướng của các tập đoàn đa quốc gia (MNCs) và tác động của biến động tỷ giá (SPICED vs WPIDEC).
        </p>
    </div>

    <!-- 1. GLOBALISATION -->
    <div id="sec-globalisation" class="lecture-interactive-card" data-lecture-section="sec_globalisation" style="margin-bottom: 45px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 3px solid #3b82f6; padding-bottom: 12px;">
            <h2 style="color: #0f172a; margin: 0; font-size: 24px; font-weight: 800;">
                🌍 1. THE IMPORTANCE OF GLOBALISATION
            </h2>
            <span style="font-size: 12px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 12px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe cả phần</span>
        </div>

        <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px 20px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 22px;">
            <b>Globalisation</b> is the economic integration of different countries through increasing freedoms in the cross-border movement of people, goods/services, technology, and finance.
        </div>

        <!-- Sub-card: Drivers & Trade Flow -->
        <div id="card-globalisation-drivers" class="lecture-interactive-card" data-lecture-section="card_globalisation_drivers" style="margin-bottom: 22px; background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <b style="color: #0f172a; font-size: 16px;">🚀 Reasons for Globalisation &amp; Trade Flows</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #2563eb; padding: 3px 8px; border-radius: 4px; border: 1px solid #cbd5e1;">Nghe thẻ này</span>
            </div>

            <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 15px;">
                <div style="flex: 1; min-width: 240px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px 15px;">
                    <b style="color: #0f172a; font-size: 14px;">📥 Imports</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Goods bought from abroad. <i>(Money leaves domestic economy).</i></p>
                </div>
                <div style="flex: 1; min-width: 240px; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px 15px;">
                    <b style="color: #0f172a; font-size: 14px;">📤 Exports</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Goods sold to overseas buyers. <i>(Money flows into domestic economy).</i></p>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #2563eb; font-size: 13.5px;">💻 Advances in Tech</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #475569;">High-speed internet &amp; ecommerce cut communication barriers.</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #059669; font-size: 13.5px;">🤝 Trade Liberalisation</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #475569;">Removal of quotas and tariffs via trade blocs (EU, CPTPP).</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #d97706; font-size: 13.5px;">🚢 Transport Advances</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #475569;">Standardised containerisation drastically slashes shipping costs.</p>
                </div>
                <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #7c3aed; font-size: 13.5px;">🏛️ Market Reforms</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #475569;">Governments deregulate markets and welcome inward FDI.</p>
                </div>
            </div>
        </div>

        <!-- Sub-card: Opps & Threats -->
        <div id="card-globalisation-impacts" class="lecture-interactive-card" data-lecture-section="card_globalisation_impacts" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <b style="color: #0f172a; font-size: 16px;">⚖️ Opportunities &amp; Threats of Globalisation</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #2563eb; padding: 3px 8px; border-radius: 4px; border: 1px solid #cbd5e1;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px;">🌟 Opportunities</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 13.5px; line-height: 1.5;">
                        <li><b>Market expansion:</b> Exporting spreads business risk and multiplies total sales volume.</li>
                        <li><b>Lower costs:</b> Sourcing cheaper foreign materials and relocating plants to lower wage nations.</li>
                        <li><b>Resource access:</b> Securing rare raw materials and specialized technical talent overseas.</li>
                    </ul>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 16px;">
                    <h4 style="margin: 0 0 8px 0; color: #b91c1c; font-size: 16px;">⚠️ Threats</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 13.5px; line-height: 1.5;">
                        <li><b>Intense competition:</b> Domestic firms face multinational rivals with massive economies of scale.</li>
                        <li><b>MNC talent poaching:</b> Global firms poach skilled workers by offering higher pay packages.</li>
                        <li><b>Cultural &amp; regulatory risks:</b> High adaptation costs and complex compliance across borders.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. TARIFFS & QUOTAS -->
    <div id="sec-tariffs-quotas" class="lecture-interactive-card" data-lecture-section="sec_tariffs_quotas" style="margin-bottom: 45px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 3px solid #f97316; padding-bottom: 12px;">
            <h2 style="color: #0f172a; margin: 0; font-size: 24px; font-weight: 800;">
                🚧 2. TRADE PROTECTIONISM: TARIFFS &amp; QUOTAS
            </h2>
            <span style="font-size: 12px; font-weight: 700; background: #fff7ed; color: #c2410c; padding: 4px 12px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe cả phần</span>
        </div>

        <p style="font-size: 14.5px; color: #475569; margin-bottom: 20px;">
            Governments introduce <b>trade barriers</b> to protect infant domestic industries, curb unfair foreign dumping, and preserve domestic employment.
        </p>

        <!-- Sub-card: Protectionism Tools -->
        <div id="card-protectionism-tools" class="lecture-interactive-card" data-lecture-section="card_protectionism_tools" style="background: #fff7ed; border: 1.5px solid #fdba74; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <b style="color: #9a3412; font-size: 16px;">💰 Import Tariffs vs 📦 Import Quotas</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #c2410c; padding: 3px 8px; border-radius: 4px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <!-- Tariffs -->
            <div style="background: #ffffff; border: 1px solid #fed7aa; border-radius: 10px; padding: 16px; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #ffedd5; color: #c2410c; font-weight: 700; font-size: 13px; padding: 3px 8px; border-radius: 4px;">Tariff (Thuế quan)</span>
                    <span style="font-size: 13px; color: #64748b;">A tax placed on imported foreign goods to artificially increase their retail price.</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 10px 12px; font-size: 12.5px; color: #166534;">
                        <b>✅ Benefits:</b> Raises government tax revenue; protects domestic jobs from low-price dumping.
                    </div>
                    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 10px 12px; font-size: 12.5px; color: #991b1b;">
                        <b>❌ Drawbacks:</b> Domestic importers face high raw material costs; consumers pay higher prices.
                    </div>
                </div>
            </div>

            <!-- Examiner Tip -->
            <div style="background: #fdf2f8; border: 1.5px dashed #db2777; border-radius: 8px; padding: 14px 18px; margin-bottom: 16px;">
                <b style="color: #9d174d; font-size: 14px;">🎓 Cambridge Examiner Tip: Who actually pays the tariff?</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #831843;">
                    It is <b>NOT the foreign exporter</b> who pays the tariff! It is the <b>domestic importing enterprise</b> that pays the customs tax upon entry, immediately inflating its unit manufacturing cost.
                </p>
            </div>

            <!-- Quotas -->
            <div style="background: #ffffff; border: 1px solid #fed7aa; border-radius: 10px; padding: 16px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="background: #ffedd5; color: #c2410c; font-weight: 700; font-size: 13px; padding: 3px 8px; border-radius: 4px;">Quota (Hạn ngạch)</span>
                    <span style="font-size: 13px; color: #64748b;">A legal physical limit on the maximum quantity of a product allowed into the nation.</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 10px 12px; font-size: 12.5px; color: #166534;">
                        <b>✅ Benefits:</b> Guarantees market share for local suppliers; stimulates domestic factory hiring.
                    </div>
                    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 10px 12px; font-size: 12.5px; color: #991b1b;">
                        <b>❌ Drawbacks:</b> Restricts consumer supply causing price surges; can ignite retaliatory trade wars.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. MULTINATIONAL COMPANIES (MNCS) -->
    <div id="sec-mncs" class="lecture-interactive-card" data-lecture-section="sec_mncs" style="margin-bottom: 45px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 3px solid #10b981; padding-bottom: 12px;">
            <h2 style="color: #0f172a; margin: 0; font-size: 24px; font-weight: 800;">
                🏢 3. MULTINATIONAL COMPANIES (MNCs)
            </h2>
            <span style="font-size: 12px; font-weight: 700; background: #ecfdf5; color: #047857; padding: 4px 12px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe cả phần</span>
        </div>

        <p style="font-size: 14.5px; color: #475569; margin-bottom: 20px;">
            A <b>Multinational Company (MNC)</b> is an enterprise registered in one nation with manufacturing, processing, or service operations in multiple other countries <i>(e.g., Apple, Toyota, Unilever, McDonald's)</i>.
        </p>

        <!-- Sub-card: Why Become MNC -->
        <div id="card-mnc-strategy" class="lecture-interactive-card" data-lecture-section="card_mnc_strategy" style="margin-bottom: 22px; background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <b style="color: #065f46; font-size: 16px;">✨ Strategic Motives for Multinationals</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #059669; padding: 3px 8px; border-radius: 4px; border: 1px solid #86efac;">Nghe thẻ này</span>
            </div>

            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <span style="background: #ffffff; border: 1px solid #bbf7d0; color: #065f46; padding: 8px 14px; border-radius: 8px; font-size: 13px;"><b>Economies of scale:</b> Giant production runs drive down unit fixed costs.</span>
                <span style="background: #ffffff; border: 1px solid #bbf7d0; color: #065f46; padding: 8px 14px; border-radius: 8px; font-size: 13px;"><b>Risk diversification:</b> Sluggish sales in one continent offset by booming foreign markets.</span>
                <span style="background: #ffffff; border: 1px solid #bbf7d0; color: #065f46; padding: 8px 14px; border-radius: 8px; font-size: 13px;"><b>Bypassing tariffs:</b> Producing inside target nations completely circumvents import taxes!</span>
                <span style="background: #ffffff; border: 1px solid #bbf7d0; color: #065f46; padding: 8px 14px; border-radius: 8px; font-size: 13px;"><b>Tax incentives:</b> Incorporating entities in low corporate tax jurisdictions.</span>
                <span style="background: #ffffff; border: 1px solid #bbf7d0; color: #065f46; padding: 8px 14px; border-radius: 8px; font-size: 13px;"><b>Lower logistics costs:</b> Assembling finished goods adjacent to final overseas customers.</span>
            </div>
        </div>

        <!-- Sub-card: Stakeholders Impact Table -->
        <div id="card-mnc-stakeholders" class="lecture-interactive-card" data-lecture-section="card_mnc_stakeholders" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <b style="color: #0f172a; font-size: 16px;">🤝 Impact of MNCs on Key Stakeholders</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #0f172a; padding: 3px 8px; border-radius: 4px; border: 1px solid #cbd5e1;">Nghe thẻ này</span>
            </div>

            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13px; border: 1px solid #e2e8f0;">
                    <thead>
                        <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                            <th style="padding: 10px 12px; color: #0f172a; width: 22%;">Stakeholder</th>
                            <th style="padding: 10px 12px; color: #15803d; width: 39%; border-left: 1px solid #e2e8f0;">✅ Positive Impacts</th>
                            <th style="padding: 10px 12px; color: #b91c1c; width: 39%; border-left: 1px solid #e2e8f0;">❌ Negative Impacts</th>
                        </tr>
                    </thead>
                    <tbody style="color: #475569;">
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #0f172a;">Employees</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Structured technical training, career ladder, higher pay than local firms.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Top executive roles often reserved for expatriates; weak job security if plants relocate.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #0f172a;">Local Community</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Infrastructure upgrades (paved roads, water, utilities); CSR social initiatives.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Industrial pollution and congestion; erosion of traditional local business culture.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #0f172a;">Consumers</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Broader product diversity, consistent brand quality, lower competitive prices.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Drives local unique artisans out of business; risk of monopoly dominance.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #0f172a;">Suppliers</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Tremendous surge in raw material purchase order volume.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">MNCs demand aggressive cost discounts and extended 90-day credit terms.</td>
                        </tr>
                        <tr style="background: #ffffff;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #0f172a;">Shareholders</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">High corporate profits yielding substantial long-term dividend returns.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0;">Profits may be consumed by risky high-cost foreign acquisition investments.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- 4. IMPACT ON HOST COUNTRIES -->
    <div id="sec-impact-host-countries" class="lecture-interactive-card" data-lecture-section="sec_impact_host_countries" style="margin-bottom: 45px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 3px solid #ec4899; padding-bottom: 12px;">
            <h2 style="color: #0f172a; margin: 0; font-size: 24px; font-weight: 800;">
                🛬 4. IMPACT ON HOST COUNTRIES
            </h2>
            <span style="font-size: 12px; font-weight: 700; background: #fdf2f8; color: #db2777; padding: 4px 12px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe cả phần</span>
        </div>

        <p style="font-size: 14.5px; color: #475569; margin-bottom: 20px;">
            The presence of multinational corporations introduces profound macroeconomic benefits alongside serious sovereign and environmental dilemmas for host developing nations.
        </p>

        <!-- Sub-card: Host Evaluation -->
        <div id="card-host-eval" class="lecture-interactive-card" data-lecture-section="card_host_eval" style="background: #fdf2f8; border: 1.5px solid #f472b6; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <b style="color: #9d174d; font-size: 16px;">⚖️ Evaluating MNCs on Host Nations</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #db2777; padding: 3px 8px; border-radius: 4px; border: 1px solid #f472b6;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #ffffff; border: 1px solid #fbcfe8; border-top: 4px solid #10b981; border-radius: 8px; padding: 16px;">
                    <h4 style="margin: 0 0 10px 0; color: #059669; font-size: 16px;">✅ Benefits to Host Country</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #334155; font-size: 13px; line-height: 1.55;">
                        <li><b>Foreign Direct Investment (FDI):</b> Inflow of investment capital stimulates national GDP.</li>
                        <li><b>Balance of Payments:</b> Boosted when the MNC manufactures goods and exports them abroad.</li>
                        <li><b>Technology &amp; Skills:</b> Knowledge transfer trains local labour in advanced management techniques.</li>
                        <li><b>Corporate Tax Revenue:</b> Taxes paid on local profits bolster government fiscal budgets.</li>
                    </ul>
                </div>

                <div style="background: #ffffff; border: 1px solid #fbcfe8; border-top: 4px solid #ef4444; border-radius: 8px; padding: 16px;">
                    <h4 style="margin: 0 0 10px 0; color: #dc2626; font-size: 16px;">❌ Drawbacks to Host Country</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #334155; font-size: 13px; line-height: 1.55;">
                        <li><b>Repatriation of Profits:</b> MNCs send vast profits back to headquarters, depleting foreign exchange reserves.</li>
                        <li><b>Transfer Pricing:</b> Booking profits through low-tax havens to evade local corporate tax liabilities.</li>
                        <li><b>Resource Depletion:</b> Unsustainable extraction of local mineral and agricultural reserves.</li>
                        <li><b>Crowding Out:</b> Local infant businesses unable to compete go bankrupt, destroying local entrepreneurship.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. THE IMPACT OF EXCHANGE RATES -->
    <div id="sec-exchange-rates" class="lecture-interactive-card" data-lecture-section="sec_exchange_rates" style="margin-bottom: 45px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px;">
            <h2 style="color: #0f172a; margin: 0; font-size: 24px; font-weight: 800;">
                💱 5. THE IMPACT OF EXCHANGE RATES
            </h2>
            <span style="font-size: 12px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 12px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe cả phần</span>
        </div>

        <p style="font-size: 14.5px; color: #475569; margin-bottom: 20px;">
            An <b>exchange rate</b> is the price of one national currency expressed in terms of another <i>(e.g., £1 = $1.30 or €1.15)</i>. Movements in exchange rates alter international pricing and profit margins.
        </p>

        <!-- Sub-card: SPICED & Exchange Rate Rules -->
        <div id="card-spiced-rules" class="lecture-interactive-card" data-lecture-section="card_spiced_rules" style="background: #faf5ff; border: 1.5px solid #c084fc; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <b style="color: #6b21a8; font-size: 16px;">💡 Mastering the SPICED &amp; WPIDEC Principles</b>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #7e22ce; padding: 3px 8px; border-radius: 4px; border: 1px solid #c084fc;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 16px;">
                <div style="background: #ffffff; border: 1px solid #e9d5ff; border-radius: 8px; padding: 14px;">
                    <h4 style="color: #6d28d9; font-size: 15px; margin: 0 0 6px 0;">📈 Appreciation (Strong Currency)</h4>
                    <p style="margin: 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        Currency value rises <i>(e.g., £1 = $1.20 moves to £1 = $1.35)</i>.<br/>
                        <b>SPICED:</b> <b>S</b>trong <b>P</b>ound ➔ <b>I</b>mports <b>C</b>heaper, <b>E</b>xports <b>D</b>earer.
                    </p>
                </div>
                <div style="background: #ffffff; border: 1px solid #e9d5ff; border-radius: 8px; padding: 14px;">
                    <h4 style="color: #6d28d9; font-size: 15px; margin: 0 0 6px 0;">📉 Depreciation (Weak Currency)</h4>
                    <p style="margin: 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        Currency value falls <i>(e.g., £1 = $1.20 moves to £1 = $1.05)</i>.<br/>
                        <b>WPIDEC:</b> <b>W</b>eak <b>P</b>ound ➔ <b>I</b>mports <b>D</b>earer, <b>E</b>xports <b>C</b>heaper.
                    </p>
                </div>
            </div>

            <!-- Table of Impact -->
            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13.5px; border: 1px solid #e2e8f0;">
                    <thead>
                        <tr style="background-color: #f3e8ff; border-bottom: 2px solid #d8b4fe;">
                            <th style="padding: 10px 12px; color: #581c87; width: 30%;">Currency Status</th>
                            <th style="padding: 10px 12px; color: #581c87; width: 35%; border-left: 1px solid #e2e8f0;">Impact on Exporters</th>
                            <th style="padding: 10px 12px; color: #581c87; width: 35%; border-left: 1px solid #e2e8f0;">Impact on Importers</th>
                        </tr>
                    </thead>
                    <tbody style="color: #475569;">
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #2563eb;">Appreciation (Strong)</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0; color: #dc2626;"><b>BAD:</b> Goods expensive abroad; sales volume drops unless prices slashed.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0; color: #16a34a;"><b>GOOD:</b> Cost of imported foreign raw materials drops significantly.</td>
                        </tr>
                        <tr style="background: #ffffff;">
                            <td style="padding: 10px 12px; font-weight: bold; color: #dc2626;">Depreciation (Weak)</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0; color: #16a34a;"><b>GOOD:</b> Products cheap overseas, driving surging export demand.</td>
                            <td style="padding: 10px 12px; border-left: 1px solid #e2e8f0; color: #dc2626;"><b>BAD:</b> Imported components become expensive, squeezing margins.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- 6. CAMBRIDGE EXAM GUIDE -->
    <div id="sec-recommend-globalisation" class="lecture-interactive-card" data-lecture-section="sec_recommend_globalisation" style="margin-bottom: 50px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; padding: 25px; cursor: pointer; transition: all 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
            <h2 style="color: #1e3a8a; margin: 0; font-size: 22px; font-weight: 800;">
                🎯 6. CAMBRIDGE EXAM EVALUATION &amp; DECISION STRATEGY
            </h2>
            <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e40af; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe cả phần</span>
        </div>

        <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
            Paper 1 and Paper 2 frequently challenge candidates to evaluate whether governments should welcome a new multinational corporation or whether a business should expand internationally.
        </p>

        <!-- Sub-card: Cambridge Strategy -->
        <div id="card-cambridge-global-strategy" class="lecture-interactive-card" data-lecture-section="card_cambridge_global_strategy" style="background: #ffffff; border: 1.5px solid #93c5fd; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s ease;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <b style="color: #1e40af; font-size: 15.5px;">💡 Cambridge 12-Mark Evaluation Framework</b>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #2563eb; padding: 3px 8px; border-radius: 4px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 14px;">
                <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 12px 14px; border-radius: 6px;">
                    <b style="color: #1d4ed8; font-size: 13.5px;">1. Analytical Argumentation (Chain of Impact)</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        Connect each policy change to business consequences: e.g., <i>Imposing a 10% tariff ➔ increases import costs for local bakers ➔ raises bread prices ➔ reduces consumer demand.</i>
                    </p>
                </div>
                <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 12px 14px; border-radius: 6px;">
                    <b style="color: #047857; font-size: 13.5px;">2. Contextualized Judgement</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        State whether MNC entry is overall beneficial: <i>Yes if local unemployment is critical; No if dominant local manufacturers will be pushed into bankruptcy.</i>
                    </p>
                </div>
            </div>

            <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 12px 15px; font-size: 13px; color: #1e40af;">
                <b>🔑 Golden Rule for Exchange Rates:</b> Always verify whether the business in the case study is an <b>exporter</b> or an <b>importer</b> before applying SPICED or WPIDEC!
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">6.3 Business &amp; The International Economy (Doanh nghiệp &amp; Kinh tế Quốc tế)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 6.3 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/6_3_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 6.3 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
