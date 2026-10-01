import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 6.2 ID
LID = 'a1d571ff-fa12-46c2-a49d-1df88df13214'
CODE = '6_2'
TITLE = '6.2. Environmental and ethical issues'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 10 AUDIO SEGMENTS FOR LESSON 6.2
# ==============================================================================
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
        "id": "card_environmental_impacts",
        "title": "🌍 Tác Động Môi Trường Cốt Lõi & Biện Pháp Kiểm Soát của Chính Phủ",
        "selector": "#card-environmental-impacts",
        "en": "Industrial production inflicts environmental strains: deforestation and fossil energy depletion, microplastic ocean contamination, and unsafe e-waste landfill dumping. Regulatory authorities step in by outlawing toxic chemicals, levying steep cleanup fines, and issuing tradable pollution permits.",
        "vi": "Sản xuất công nghiệp gây sức ép nặng nề lên môi trường: phá rừng và cạn kiệt năng lượng hóa thạch, rác thải hạt vi nhựa làm ô nhiễm đại dương và bãi chôn lấp rác thải điện tử độc hại. Cơ quan quản lý nhà nước can thiệp bằng cách cấm hóa chất độc hại, phạt tiền nặng phục hồi môi trường và cấp hạn ngạch giấy phép xả thải."
    },
    {
        "id": "sec_externalities",
        "title": "2. Ngoại tác: Chi phí Xã hội và Lợi ích Xã hội",
        "selector": "#sec-externalities",
        "en": "Section 2 provides the core economic equation: Social Costs equal Private Costs plus External Costs. Social Benefits equal Private Benefits plus External Benefits. Negative externalities—such as toxic factory smog or heavy traffic congestion—are borne by the local community rather than the polluting firm.",
        "vi": "Mục hai đưa ra công thức kinh tế học cốt lõi: Chi phí xã hội bằng Chi phí tư nhân cộng Chi phí ngoại tác. Lợi ích xã hội bằng Lợi ích tư nhân cộng Lợi ích ngoại tác. Ngoại tác tiêu cực như khói bụi độc hại hay tắc đường do xe tải nhà máy gây ra là những tổn thất mà cộng đồng địa phương phải gánh chịu thay cho doanh nghiệp."
    },
    {
        "id": "card_externalities_formula",
        "title": "🔗 Công Thức Ngoại Tác & Quyết Định Phê Duyệt Dự Án",
        "selector": "#card-externalities-formula",
        "en": "Master the externalities equation: Social Cost equals Private Cost plus External Cost, and Social Benefit equals Private Benefit plus External Benefit. Governments approve commercial factory developments only when Social Benefits definitively outweigh Social Costs.",
        "vi": "Nắm vững công thức ngoại tác: Chi phí xã hội bằng Chi phí tư nhân cộng Chi phí ngoại tác, và Lợi ích xã hội bằng Lợi ích tư nhân cộng Lợi ích ngoại tác. Chính phủ và chính quyền địa phương chỉ cấp phép cho các dự án xây dựng nhà xưởng khi Lợi ích xã hội tạo ra vượt trội hơn hẳn Chi phí xã hội phát sinh."
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
        "title": "📢 Vai trò của Nhóm Áp lực (Pressure Groups)",
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
        "id": "card_ethical_practices",
        "title": "⚖️ Bộ Quy Tắc Đạo Đức: Tiền Lương Sống, Chống Phân Biệt Giới & Nguồn Cung Minh Bạch",
        "selector": "#card-ethical-practices",
        "en": "Ethical codes of practice enforce zero child exploitation in supply chains, close the gender wage gap, guarantee fair trade purchasing prices, and eliminate misleading promotional claims. Committing to ethical standards earns strong consumer trust and boosts employee retention.",
        "vi": "Bộ quy tắc đạo đức doanh nghiệp bảo đảm tuyệt đối không bóc lột lao động trẻ em trong chuỗi cung ứng, thu hẹp khoảng cách lương theo giới tính, cam kết mức giá mua hàng công bằng cho nông dân và loại bỏ quảng cáo gây hiểu lầm. Cam kết đạo đức giúp xây dựng niềm tin tiêu dùng vững chắc và gắn kết người lao động."
    },
    {
        "id": "sec_ethics_profitability",
        "title": "5. Đạo đức đối chiếu với Lợi nhuận (Cambridge Exam Strategy)",
        "selector": "#sec-ethics-profitability",
        "en": "Section 5 details the Cambridge evaluation dilemma: Acting ethically raises operating production costs in the short run, but builds prestigious brand reputation, attracts ethical investors, and avoids crippling consumer boycotts in the long term.",
        "vi": "Mục năm cung cấp chiến lược giải quyết bài toán tình huống Cambridge: Hành xử có đạo đức có thể làm tăng chi phí sản xuất trong ngắn hạn, nhưng về lâu dài lại kiến tạo uy tín thương hiệu vững chắc, thu hút các quỹ đầu tư bền vững và tránh được những làn sóng tẩy chay phá hủy doanh nghiệp."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_environmental_concerns": {"start": 1, "end": 2},
    "sec_externalities": {"start": 3, "end": 4},
    "sec_sustainable_development": {"start": 5, "end": 6},
    "sec_business_ethics": {"start": 7, "end": 8},
    "sec_ethics_profitability": {"start": 9, "end": 9}
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
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 6</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">6.2 Environmental and Ethical Issues (Vấn đề Môi trường &amp; Đạo đức)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. ENVIRONMENTAL CONCERNS & IMPACTS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-environmental-concerns" class="lecture-interactive-card" data-lecture-section="sec_environmental_concerns" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🌍 1. ENVIRONMENTAL CONCERNS &amp; IMPACTS</h2>
            <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #15803d; margin-bottom: 10px;">
                Industrial manufacturing activity extracts natural resources, discharges waste pollutants, and imposes lasting ecological footprints on local environments.
            </div>
        </div>

        <!-- SUB-CARD: ENVIRONMENTAL IMPACTS -->
        <div id="card-environmental-impacts" class="lecture-interactive-card" data-lecture-section="card_environmental_impacts" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #059669; font-weight: 700;">🌍 Core Environmental Issues &amp; Government Controls</h3>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🪓 Resource Depletion:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        Logging timber and commercial farming lead to deforestation, habitat loss, and global warming.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🏭 Industrial Pollution:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        Smokestack emissions cause acid rain; toxic chemical effluents pollute rivers and destroy marine ecosystems.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🗑️ Solid &amp; Electronic Waste:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        Single-use plastics take hundreds of years to degrade; hazardous electronic scrap is dumped in developing nations.
                    </p>
                </div>
            </div>

            <div style="background: #f0fdf4; border: 1px dashed #10b981; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #15803d;">
                <b>⚖️ Government Controls:</b> Authorities enact legal bans on dumping hazardous materials, levy punitive pollution fines, and issue tradable <b>Pollution Permits</b> to incentivize clean tech.
            </div>
        </div>
    </div>

    <!-- 2. EXTERNALITIES -->
    <div style="margin-bottom: 50px;">
        <div id="sec-externalities" class="lecture-interactive-card" data-lecture-section="sec_externalities" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🔗 2. EXTERNALITIES (SPILLOVER EFFECTS)</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                Externalities occur when business activities impose unintended third-party costs or benefits on people outside the commercial transaction.
            </div>
        </div>

        <!-- SUB-CARD: EXTERNALITIES FORMULA -->
        <div id="card-externalities-formula" class="lecture-interactive-card" data-lecture-section="card_externalities_formula" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">🔗 Social Costs vs Social Benefits Equation</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #fef2f2; border: 1.5px dashed #fca5a5; padding: 16px; border-radius: 10px; text-align: center;">
                    <b style="color: #b91c1c; font-size: 16px;">Social Cost = Private Cost + External Cost</b>
                    <p style="margin: 8px 0 0 0; font-size: 12.5px; color: #991b1b; text-align: left; line-height: 1.5;">
                        <b>Private:</b> Building construction &amp; wages paid by firm.<br/>
                        <b>External:</b> Toxic factory smoke, heavy traffic noise, loss of park land suffered by neighbors.
                    </p>
                </div>

                <div style="background: #f0fdf4; border: 1.5px dashed #86efac; padding: 16px; border-radius: 10px; text-align: center;">
                    <b style="color: #15803d; font-size: 16px;">Social Benefit = Private Benefit + External Benefit</b>
                    <p style="margin: 8px 0 0 0; font-size: 12.5px; color: #166534; text-align: left; line-height: 1.5;">
                        <b>Private:</b> Sales revenue and financial profits earned.<br/>
                        <b>External:</b> Job creation for local residents, infrastructure roads built, and higher local spending.
                    </p>
                </div>
            </div>

            <div style="background: #eff6ff; border: 1px solid #bfdbfe; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #1e40af;">
                <b>💡 Government Approval Rule:</b> Public planners only approve major industrial ventures if <b>Social Benefits exceed Social Costs</b>!
            </div>
        </div>
    </div>

    <!-- 3. SUSTAINABLE DEVELOPMENT & PRESSURE GROUPS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-sustainable-development" class="lecture-interactive-card" data-lecture-section="sec_sustainable_development" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🌱 3. SUSTAINABLE DEVELOPMENT</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                <b>Sustainable development</b> meets present population needs without compromising the ability of future generations to achieve a comparable quality of life.
            </p>
        </div>

        <!-- SUB-CARD: PRESSURE GROUPS -->
        <div id="card-pressure-groups" class="lecture-interactive-card" data-lecture-section="card_pressure_groups" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">📢 Pressure Groups (Nhóm Áp Lực)</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <p style="font-size: 14px; color: #475569; margin: 0 0 16px 0;">
                Organizations that seek to influence business and government policies to champion specific environmental or social causes.
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 14px; border-radius: 10px;">
                    <b style="color: #d97706; font-size: 14px;">🚫 Consumer Boycotts:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #92400e; line-height: 1.5;">
                        Urging the public to stop purchasing goods from offending firms, causing catastrophic revenue collapses.
                    </p>
                </div>
                <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 14px; border-radius: 10px;">
                    <b style="color: #d97706; font-size: 14px;">📱 Viral Public Relations Campaigns:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #92400e; line-height: 1.5;">
                        Using social media exposés and peaceful protests to tarnish corporate brand reputation and deter ethical investors.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. BUSINESS ETHICS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-business-ethics" class="lecture-interactive-card" data-lecture-section="sec_business_ethics" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 4. BUSINESS ETHICS (ĐẠO ĐỨC KINH DOANH)</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Ethics governs moral rules and behavioral standards guiding decision making beyond what is strictly mandated by statutory law.
            </p>
        </div>

        <!-- SUB-CARD: ETHICAL PRACTICES -->
        <div id="card-ethical-practices" class="lecture-interactive-card" data-lecture-section="card_ethical_practices" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #be185d; font-weight: 700;">⚖️ Ethical Codes of Practice &amp; Corporate Responsibility</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff1f2; color: #be185d; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 16px;">
                <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 14px; border-radius: 10px;">
                    <b style="color: #9d174d; font-size: 14px;">Fair Working Standards:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #475569; line-height: 1.5;">
                        Paying living wages rather than minimum legal wages; closing gender wage gaps; providing safe working gear.
                    </p>
                </div>
                <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 14px; border-radius: 10px;">
                    <b style="color: #9d174d; font-size: 14px;">Supply Chain Transparency:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #475569; line-height: 1.5;">
                        Refusing sweatshop factories and child labour; paying Fairtrade price premiums to small agricultural farmers.
                    </p>
                </div>
            </div>

            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #475569;">
                <b>🌟 Commercial Benefit:</b> Ethical enterprises command premium retail prices, attract high-calibre employees, and secure favorable financing from ESG investment funds.
            </div>
        </div>
    </div>

    <!-- 5. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-ethics-profitability" class="lecture-interactive-card" data-lecture-section="sec_ethics_profitability" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 5. ETHICS VS PROFITABILITY (Cambridge Exam Evaluation Guide)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Cambridge questions regularly present dilemmas: <i>"Recommend whether this enterprise should source only Fairtrade ingredients even if it reduces short-term profit."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #047857; font-size: 15px;">Benefits of Ethical Strategy:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Builds enduring brand prestige; creates unique competitive differentiation; avoids devastating consumer boycotts and regulatory legal penalties.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #ef4444; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #b91c1c; font-size: 15px;">Drawbacks / Commercial Risks:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Higher unit operating costs; risk of losing price-sensitive consumers to cheaper unprincipled rivals; lower immediate annual dividend payouts to shareholders.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">6.2 Environmental and Ethical Issues (Vấn đề Môi trường &amp; Đạo đức)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 6.2 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/6_2_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 6.2 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
