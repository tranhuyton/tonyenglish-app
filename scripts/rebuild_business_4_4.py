import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 4.4 ID
LID = '95eb54ae-44d4-42f6-9d1d-c5c729a69954'
CODE = '4_4'
TITLE = '4.4. Location decisions'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 11 AUDIO SEGMENTS FOR LESSON 4.4
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.4: Quyết định Địa điểm Kinh doanh",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.4: Location Decisions. In this lesson, we examine why location choices are made, analyze key determinants across manufacturing, service, and retail sectors, evaluate international relocation factors, and assess government zoning controls.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.4: Quyết định Địa điểm Kinh doanh. Trong bài học này, chúng ta sẽ tìm hiểu lý do đưa ra quyết định chọn địa điểm, phân tích các yếu tố chi phối trong ngành sản xuất, dịch vụ và bán lẻ, đánh giá động lực mở rộng địa điểm ra quốc tế cùng các biện pháp kiểm soát quy hoạch của chính phủ."
    },
    {
        "id": "sec_location_decisions",
        "title": "1. Tầm quan trọng của Quyết định Địa điểm",
        "selector": "#sec-location-decisions",
        "en": "Section 1 addresses location decisions. Businesses choose new operating locations at startup, during market expansion, or when current premises prove inefficient. Location directly influences fixed rental expenses, logistics transport costs, skilled worker recruitment, and market reach.",
        "vi": "Mục một xem xét các quyết định về địa điểm. Doanh nghiệp cần lựa chọn địa điểm khi mới thành lập, khi mở rộng quy mô, hoặc khi địa điểm hiện tại hoạt động kém hiệu quả. Địa điểm chi phối trực tiếp chi phí thuê mặt bằng cố định, chi phí logistics vận chuyển, khả năng tuyển dụng nhân sự lành nghề và độ phủ thị trường."
    },
    {
        "id": "sec_factors_location",
        "title": "2. Các Yếu tố Chi phối Lựa chọn Địa điểm",
        "selector": "#sec-factors-location",
        "en": "Section 2 investigates the diverse factors influencing site selection, which differ radically depending on whether the business operates in heavy manufacturing, professional services, or high-street consumer retail.",
        "vi": "Mục hai nghiên cứu các yếu tố chi phối việc chọn mặt bằng, vốn có sự khác biệt sâu sắc tùy thuộc vào việc doanh nghiệp hoạt động trong lĩnh vực sản xuất công nghiệp, dịch vụ chuyên nghiệp hay bán lẻ tiêu dùng."
    },
    {
        "id": "card_location_manufacturing",
        "title": "🏭 Yếu tố Địa điểm cho Doanh nghiệp Sản xuất (Manufacturing)",
        "selector": "#card-location-manufacturing",
        "en": "Manufacturing location decisions prioritize access to heavy raw materials to reduce freight costs, reliable electric power grids, availability of specialized skilled labour, comprehensive transport links including highways and shipping ports, and affordable industrial land rents.",
        "vi": "Quyết định địa điểm sản xuất ưu tiên tiếp cận các nguồn nguyên liệu thô cồng kềnh để giảm chi phí vận chuyển, hệ thống lưới điện đáng tin cậy, nguồn lao động lành nghề, mạng lưới giao thông đường bộ và cảng biển thuận tiện, cùng giá thuê đất công nghiệp hợp lý."
    },
    {
        "id": "card_location_services",
        "title": "🛎️ Yếu tố Địa điểm cho Doanh nghiệp Dịch vụ (Service-Sector)",
        "selector": "#card-location-services",
        "en": "Service businesses with direct customer interaction—such as restaurants and retail clinics—require accessible, prestigious locations. Conversely, back-office IT and bank call centers locate in low-rent, low-wage suburban districts with robust internet connectivity.",
        "vi": "Doanh nghiệp dịch vụ có tương tác trực tiếp với khách hàng – như nhà hàng và phòng khám – đòi hỏi địa điểm dễ tiếp cận, uy tín. Ngược lại, các trung tâm chăm sóc khách hàng và công nghệ thông tin có thể đặt tại các khu vực ngoại thành có chi phí thuê nhà và tiền lương rẻ hơn với hạ tầng mạng internet ổn định."
    },
    {
        "id": "card_location_retailing",
        "title": "🛍️ Yếu tố Địa điểm cho Cửa hàng Bán lẻ (Retailing)",
        "selector": "#card-location-retailing",
        "en": "Retailing locations demand massive pedestrian footfall in shopping malls or prime high streets, convenient customer parking amenities, proximity to complementary retailers, and secure delivery logistics access to avoid stock depletion.",
        "vi": "Địa điểm bán lẻ đòi hỏi lưu lượng người đi bộ qua lại đông đúc trong các trung tâm mua sắm hoặc tuyến phố lớn, tiện ích đỗ xe thuận tiện cho khách, nằm gần các cửa hàng bổ trợ và lối tiếp cận bốc dỡ hàng an toàn để không bị gián đoạn nguồn hàng."
    },
    {
        "id": "sec_international_location",
        "title": "3. Lý do Doanh nghiệp Mở rộng Địa điểm ra Nước ngoài",
        "selector": "#sec-international-location",
        "en": "Section 3 examines international relocation and offshoring. Businesses set up overseas branches to tap fast-growing customer markets, exploit cheaper foreign wage rates, and secure local raw materials.",
        "vi": "Mục ba xem xét việc dịch chuyển địa điểm ra nước ngoài. Doanh nghiệp thiết lập chi nhánh quốc tế để khai thác các thị trường tiêu dùng tăng trưởng nhanh, tận dụng mức tiền lương rẻ hơn và tiếp cận nguồn nguyên liệu phong phú tại chỗ."
    },
    {
        "id": "card_international_factors",
        "title": "🌍 Động lực Di dời Quốc tế: Thị trường Mới, Chi phí & Hàng rào Thuế quan",
        "selector": "#card-international-factors",
        "en": "Businesses expand overseas to access vast new customer demographics when domestic markets saturate, to capitalize on lower regional wage rates, and to bypass import tariffs and quotas by establishing physical operations inside protected trading blocs.",
        "vi": "Doanh nghiệp mở rộng ra nước ngoài nhằm tiếp cận tệp khách hàng mới tiềm năng khi thị trường trong nước bão hòa, tận dụng mức tiền lương khu vực thấp hơn, và vượt qua các rào cản thuế quan hay hạn ngạch nhập khẩu bằng cách đặt cơ sở sản xuất ngay bên trong các khối thương mại bảo hộ."
    },
    {
        "id": "sec_legal_location",
        "title": "4. Kiểm soát Pháp lý & Chính sách Hỗ trợ Địa điểm",
        "selector": "#sec-legal-location",
        "en": "Section 4 covers government intervention. Authorities encourage investment in regions of high unemployment through subsidies, while imposing zoning regulations and planning restrictions to safeguard protected green spaces from heavy industrial pollution.",
        "vi": "Mục bốn phân tích sự can thiệp của chính phủ. Nhà nước khuyến khích doanh nghiệp đầu tư vào các khu vực có tỷ lệ thất nghiệp cao thông qua các gói trợ cấp, đồng thời áp đặt các quy định phân vùng và giới hạn quy hoạch để bảo vệ các vành đai xanh khỏi ô nhiễm công nghiệp nặng."
    },
    {
        "id": "card_legal_incentives",
        "title": "⚖️ Trợ cấp Khu vực Khó khăn vs Quy hoạch Phân vùng (Zoning Laws)",
        "selector": "#card-legal-incentives",
        "en": "Governments actively guide business location: providing financial regional grants and tax holidays to incentivize job creation in economically depressed areas, while imposing stringent zoning and environmental planning restrictions to protect historic and natural zones.",
        "vi": "Chính phủ chủ động định hướng địa điểm kinh doanh: cung cấp các khoản trợ cấp phát triển khu vực và miễn giảm thuế để khuyến khích tạo việc làm tại các vùng khó khăn, đồng thời áp đặt các quy định phân vùng và hạn chế quy hoạch môi trường nghiêm ngặt để bảo vệ các khu vực tự nhiên và di sản."
    },
    {
        "id": "sec_recommend_location",
        "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất & Biện minh Lựa chọn Địa điểm",
        "selector": "#sec-recommend-location",
        "en": "Section 5 details Cambridge evaluation strategy when comparing Site A and Site B. Candidates must weigh trade-offs: prime high-traffic city centres demand exorbitant rents, whereas cheaper rural sites require heavy transport logistics and customer parking investments.",
        "vi": "Mục năm cung cấp chiến lược làm bài thi Cambridge khi so sánh Địa điểm A và Địa điểm B. Thí sinh phải cân nhắc sự đánh đổi: khu vực trung tâm đông đúc có chi phí thuê đắt đỏ, trong khi địa điểm ngoại ô giá rẻ lại đòi hỏi đầu tư mạnh cho chi phí vận tải và bãi đỗ xe cho khách."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_location_decisions": {"start": 1, "end": 1},
    "sec_factors_location": {"start": 2, "end": 5},
    "sec_international_location": {"start": 6, "end": 7},
    "sec_legal_location": {"start": 8, "end": 9},
    "sec_recommend_location": {"start": 10, "end": 10}
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
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 4</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.4 Location Decisions (Quyết định Địa điểm Kinh doanh)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. LOCATION DECISIONS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-location-decisions" class="lecture-interactive-card" data-lecture-section="sec_location_decisions" style="padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📍 1. LOCATION DECISIONS</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                Owners make location choices when starting up, expanding operations, or when current operating premises prove unsatisfactory.
            </div>
            <p style="margin: 0; font-size: 14px; color: #475569;">
                <b>Why is it important?</b> Location heavily affects fixed rent, labour wages, delivery transit costs, total operating profits, and the demographic market base the firm reaches.
            </p>
        </div>
    </div>

    <!-- 2. FACTORS AFFECTING LOCATION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-factors-location" class="lecture-interactive-card" data-lecture-section="sec_factors_location" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🧩 2. FACTORS AFFECTING LOCATION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Location determinants differ profoundly across manufacturing, service, and retailing businesses:
            </p>
        </div>

        <!-- SUB-CARD A: MANUFACTURING -->
        <div id="card-location-manufacturing" class="lecture-interactive-card" data-lecture-section="card_location_manufacturing" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; color: #0f172a; font-size: 18px; font-weight: 700;">🏭 A. Manufacturing Sector Determinants</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f1f5f9; color: #334155; padding: 4px 10px; border-radius: 6px; border: 1px solid #cbd5e1;">Nghe thẻ này</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #0f172a; font-size: 13.5px;">⚙️ Production Method</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Job production is flexible; Flow production requires massive industrial acreage.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #0f172a; font-size: 13.5px;">🛒 Proximity to Market</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Perishable goods must locate close to retail markets to prevent spoil.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #0f172a; font-size: 13.5px;">🧱 Raw Materials</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Locate near heavy/bulky raw materials to minimize high freight haulage costs.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #0f172a; font-size: 13.5px;">👷 Labour Availability</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Areas with relevant engineering skills or high unemployment for lower wages.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #0f172a; font-size: 13.5px;">🚆 Transport &amp; Utilities</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Motorway and deep-water port links alongside reliable power and water grids.</p>
                </div>
            </div>
        </div>

        <!-- SUB-CARD B: SERVICES -->
        <div id="card-location-services" class="lecture-interactive-card" data-lecture-section="card_location_services" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #e9d5ff; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; color: #6b21a8; font-size: 18px; font-weight: 700;">🛎️ B. Service-Sector Determinants</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fdf4ff; color: #6b21a8; padding: 4px 10px; border-radius: 6px; border: 1px solid #e9d5ff;">Nghe thẻ này</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 13.5px;">👥 Direct Customers</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Restaurants and salons require convenient, prominent street access.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 13.5px;">💻 Technology &amp; Call Centres</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Back-office IT can locate in low-rent, low-wage outer suburbs.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 13.5px;">🏢 Proximity to Clients</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">B2B accounting and law firms must stay close to client corporate headquarters.</p>
                </div>
            </div>
        </div>

        <!-- SUB-CARD C: RETAILING -->
        <div id="card-location-retailing" class="lecture-interactive-card" data-lecture-section="card_location_retailing" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; color: #c2410c; font-size: 18px; font-weight: 700;">🛍️ C. Retailing Sector Determinants</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #c2410c; font-size: 13.5px;">🚶 Footfall Density</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Busy shopping malls or prime high street shopping centers.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #c2410c; font-size: 13.5px;">🅿️ Customer Parking</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Accessible parking facilities attract families and bulk buyers.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px;">
                    <b style="color: #c2410c; font-size: 13.5px;">🏬 Space &amp; Security</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Adequate inventory storage, rear delivery docks, and commercial security guards.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. INTERNATIONAL LOCATION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-international-location" class="lecture-interactive-card" data-lecture-section="sec_international_location" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🌍 3. WHY BUSINESSES LOCATE IN DIFFERENT COUNTRIES</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Multinational offshoring is driven by access to expanding foreign consumer markets, lower regional labour costs, raw materials, and the need to circumvent protectionist trade walls.
            </p>
        </div>

        <!-- SUB-CARD: INTERNATIONAL FACTORS -->
        <div id="card-international-factors" class="lecture-interactive-card" data-lecture-section="card_international_factors" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; color: #047857; font-size: 18px; font-weight: 700;">🌍 Strategic Drivers of International Expansion</h3>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #047857; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px;">
                    <b style="color: #15803d; font-size: 13.5px;">🌎 Tap New Overseas Markets:</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Expanding customer base when domestic markets reach maturity saturation.</p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px;">
                    <b style="color: #15803d; font-size: 13.5px;">👷 Cheaper Wage Rates:</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Lower unit labour costs dramatically widen gross profit margins.</p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px;">
                    <b style="color: #15803d; font-size: 13.5px;">🧱 Cheaper Raw Materials:</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Direct on-site processing avoids international shipping markups.</p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 12px; border-radius: 8px;">
                    <b style="color: #15803d; font-size: 13.5px;">🚧 Bypass Trade Barriers:</b>
                    <p style="margin: 3px 0 0 0; font-size: 12px; color: #475569;">Locating plants inside trade blocs bypasses costly import tariffs and quotas.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. LEGAL CONTROLS ON LOCATION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-legal-location" class="lecture-interactive-card" data-lecture-section="sec_legal_location" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 4. LEGAL CONTROLS ON LOCATION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Governments intervene to channel commercial investment into high-unemployment zones while restricting development in ecologically sensitive areas.
            </p>
        </div>

        <!-- SUB-CARD: LEGAL INCENTIVES -->
        <div id="card-legal-incentives" class="lecture-interactive-card" data-lecture-section="card_legal_incentives" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; color: #be185d; font-size: 18px; font-weight: 700;">⚖️ Regional Grants vs Planning Zoning Controls</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fdf2f8; color: #db2777; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #fdf2f8; border: 1.5px dashed #fbcfe8; border-radius: 10px; padding: 18px;">
                    <h4 style="color: #db2777; font-size: 16px; margin: 0 0 8px 0;">🟢 Encouraging Businesses (Assisted Areas)</h4>
                    <p style="margin: 0; font-size: 13px; color: #831843; line-height: 1.5;">
                        Governments provide <b>capital grants, subsidies, and tax holidays</b> to encourage firms to set up in regions suffering from high unemployment and industrial decline.
                    </p>
                </div>
                <div style="background: #fef2f2; border: 1.5px dashed #fecaca; border-radius: 10px; padding: 18px;">
                    <h4 style="color: #dc2626; font-size: 16px; margin: 0 0 8px 0;">🛑 Restricting Businesses (Zoning Laws)</h4>
                    <p style="margin: 0; font-size: 13px; color: #7f1d1d; line-height: 1.5;">
                        Governments enforce strict <b>planning permission laws</b> to prohibit factories from building in overcrowded historic centres or areas of outstanding natural beauty.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-recommend-location" class="lecture-interactive-card" data-lecture-section="sec_recommend_location" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 5. HOW TO RECOMMEND &amp; JUSTIFY LOCATION DECISIONS (Cambridge Exam Strategy)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Paper 1 and Paper 2 frequently ask candidates to: <i>"Recommend which location (Site A or Site B) this business should choose."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 18px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                    <b style="color: #1e40af; font-size: 14.5px;">For Manufacturing Businesses:</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        Prioritise <b>transport links</b>, proximity to bulky raw materials (to minimise freight costs), availability of skilled or cheap factory labour, and cheap industrial land/rent.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #10b981;">
                    <b style="color: #047857; font-size: 14.5px;">For Retail &amp; Service Businesses:</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        Prioritise <b>high customer footfall</b> (busy shopping centres, city high streets), nearby customer parking, and competitor proximity to capture passing shoppers.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                    <b style="color: #b45309; font-size: 14.5px;">For International Relocation:</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        Weigh lower wage rates and government subsidies against risks like <b>import tariffs/trade barriers</b>, language barriers, exchange rate fluctuations, and transport delays.
                    </p>
                </div>
            </div>

            <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
                <b style="color: #1e40af; font-size: 14px;">💡 Cambridge Justification Formula:</b>
                <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                    Always evaluate the <b>trade-off</b>. A city centre location has higher footfall but significantly higher rent; an out-of-town location is much cheaper but requires heavy advertising and ample customer parking to attract visitors.
                </p>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.4 Location Decisions (Quyết định Địa điểm Kinh doanh)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 4.4 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/4_4_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 4.4 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
