import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 6.1 ID
LID = '0e8fbc94-5976-4c7f-8588-471ea93926f5'
CODE = '6_1'
TITLE = '6.1. Economic issues'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 9 AUDIO SEGMENTS FOR LESSON 6.1
# ==============================================================================
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
        "title": "🔄 Bốn Giai Đoạn Chu Kỳ Kinh Tế: Growth, Boom, Recession & Slump",
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
        "id": "card_macro_impacts",
        "title": "⚡ Tác Động Chi Tiết của Thất Nghiệp, Lạm Phát & Tăng Trưởng GDP",
        "selector": "#card-macro-impacts",
        "en": "Macroeconomic shifts dictate commercial realities: High unemployment creates recruitment pools at lower wages but suppresses luxury demand. High inflation increases material procurement costs and triggers central bank interest rate hikes. Growing GDP boosts business confidence, whereas contracting GDP forces inventory liquidation.",
        "vi": "Biến động kinh tế vĩ mô chi phối hoạt động kinh doanh: Thất nghiệp cao tạo nguồn tuyển dụng dồi dào với tiền lương mềm hơn nhưng lại bóp nghẹt nhu cầu hàng cao cấp. Lạm phát cao làm tăng chi phí thu mua nguyên liệu và khiến ngân hàng trung ương tăng lãi suất. GDP tăng trưởng củng cố niềm tin đầu tư, trong khi GDP suy thoái buộc doanh nghiệp phải xả lỗ hàng tồn kho."
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
        "id": "card_policy_tools",
        "title": "⚖️ Công Cụ Chính Sách: Thuế, Chi Tiêu Công & Lãi Suất Ngân Hàng",
        "selector": "#card-policy-tools",
        "en": "Governments steer economies through three primary policy levers: Taxation cuts consumer disposable income and corporation retained earnings. Public spending builds state infrastructure and injects commercial demand. Interest rate hikes increase variable debt repayments, depressing credit card and mortgage spending.",
        "vi": "Chính phủ điều tiết nền kinh tế qua ba đòn bẩy chính sách: Tăng thuế làm giảm thu nhập khả dụng của dân cư và giảm lợi nhuận giữ lại của doanh nghiệp. Chi tiêu công xây dựng cơ sở hạ tầng quốc gia và bơm dòng tiền mua sắm công. Tăng lãi suất làm đội chi phí trả nợ vay ngân hàng, kìm hãm chi tiêu mua sắm trả góp và vay mua nhà."
    },
    {
        "id": "sec_business_policy_response",
        "title": "5. Phản ứng của Doanh nghiệp trước Chính sách Kinh tế (Cambridge Exam Guide)",
        "selector": "#sec-business-policy-response",
        "en": "Section 5 details corporate adaptation. When central banks hike interest rates, borrowing costs soar and consumer mortgage payments climb, forcing businesses to cancel debt-funded investments and discount inventory to generate immediate cash reserves.",
        "vi": "Mục năm phân tích sự thích ứng của doanh nghiệp. Khi ngân hàng trung ương tăng lãi suất, chi phí vay nợ tăng cao và gánh nặng trả góp của người dân tăng lên, buộc doanh nghiệp phải hủy bỏ các dự án đầu tư sử dụng vốn vay và giảm giá hàng tồn kho để tạo dòng tiền mặt dự phòng."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_business_cycle": {"start": 1, "end": 2},
    "sec_economic_impacts": {"start": 3, "end": 4},
    "sec_gov_objectives": {"start": 5, "end": 5},
    "sec_economic_policies": {"start": 6, "end": 7},
    "sec_business_policy_response": {"start": 8, "end": 8}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">6.1 Economic Issues (Các Vấn đề Kinh tế vĩ mô)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. THE BUSINESS CYCLE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-business-cycle" class="lecture-interactive-card" data-lecture-section="sec_business_cycle" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📉 1. THE BUSINESS CYCLE</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                The business cycle charts recurring waves in national economic output (<b>Gross Domestic Product or GDP</b>) across four distinct operational phases.
            </div>
        </div>

        <!-- SUB-CARD: 4 STAGES -->
        <div id="card-cycle-stages" class="lecture-interactive-card" data-lecture-section="card_cycle_stages" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">🔄 The Four Stages of the Business Cycle</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #15803d; font-size: 16px; margin: 0 0 8px 0;">🌱 1. Growth</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12.5px; line-height: 1.5;">
                        <li>GDP expands steadily; jobs created.</li>
                        <li>Consumer disposable incomes increase.</li>
                        <li>Businesses invest in new capacity.</li>
                    </ul>
                </div>

                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #2563eb; font-size: 16px; margin: 0 0 8px 0;">🚀 2. Boom</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #1e40af; font-size: 12.5px; line-height: 1.5;">
                        <li>Production reaches maximum peak.</li>
                        <li>Severe shortages of skilled workers.</li>
                        <li>High demand creates overheated inflation.</li>
                    </ul>
                </div>

                <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #d97706; font-size: 16px; margin: 0 0 8px 0;">⚠️ 3. Recession</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #92400e; font-size: 12.5px; line-height: 1.5;">
                        <li>Two consecutive quarters of negative GDP.</li>
                        <li>Incomes and consumer demand contract.</li>
                        <li>Profits drop and unemployment rises.</li>
                    </ul>
                </div>

                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #b91c1c; font-size: 16px; margin: 0 0 8px 0;">💥 4. Slump</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12.5px; line-height: 1.5;">
                        <li>Prolonged deep economic contraction.</li>
                        <li>Mass unemployment and business bankruptcies.</li>
                        <li>Government emergency welfare intervention.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. ECONOMIC IMPACTS ON BUSINESS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-economic-impacts" class="lecture-interactive-card" data-lecture-section="sec_economic_impacts" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚡ 2. ECONOMIC IMPACTS ON BUSINESS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Macroeconomic variables—unemployment, inflation, and GDP—exert powerful, uneven impacts across different industrial sectors.
            </p>
        </div>

        <!-- SUB-CARD: MACRO IMPACTS -->
        <div id="card-macro-impacts" class="lecture-interactive-card" data-lecture-section="card_macro_impacts" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #6d28d9; font-weight: 700;">⚡ Unemployment, Inflation &amp; GDP Fluctuations</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #6d28d9; font-size: 15px;">👥 Employment &amp; Wage Dynamics:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        <b>High unemployment</b> eases staff hiring and tempers wage growth demands, but dampens consumer sales. <b>Low unemployment</b> empowers workers to negotiate bonuses, raising operating wage bills.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #6d28d9; font-size: 15px;">📈 Inflation Pressure:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #475569; line-height: 1.5;">
                        <b>High inflation</b> drives up raw material supply costs and forces central banks to hike interest rates. Domestic goods become uncompetitive against cheaper foreign imports.
                    </p>
                </div>
            </div>

            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 12px 16px; border-radius: 4px; font-size: 13px; color: #1e40af;">
                <b>💡 Asymmetric Sector Impact:</b> During recessions, premium luxury brands (Rolex, BMW) suffer steep revenue declines, while discount grocery chains (Lidl, Aldi) experience booming demand!
            </div>
        </div>
    </div>

    <!-- 3. GOVERNMENT ECONOMIC OBJECTIVES -->
    <div style="margin-bottom: 50px;">
        <div id="sec-gov-objectives" class="lecture-interactive-card" data-lecture-section="sec_gov_objectives" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <h2 style="color: #059669; margin: 0; font-size: 22px; font-weight: 700;">🎯 3. GOVERNMENT ECONOMIC OBJECTIVES</h2>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14px; color: #475569; margin: 0 0 16px 0;">
                National authorities formulate macroeconomic policy to simultaneously target four primary benchmarks:
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 10px;">
                    <b style="color: #15803d; font-size: 14px;">1. Sustainable GDP Growth</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Increases output per person, lifting national living standards and business tax revenue.
                    </p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 10px;">
                    <b style="color: #15803d; font-size: 14px;">2. Low Stable Inflation (~2%)</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Preserves purchasing power of wages and prevents speculative price chaos.
                    </p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 10px;">
                    <b style="color: #15803d; font-size: 14px;">3. Low Unemployment</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Maximizes productive human resources and reduces costly welfare benefit handouts.
                    </p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 10px;">
                    <b style="color: #15803d; font-size: 14px;">4. Balance of Payments Stability</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Ensures export revenue covers import expenditure, protecting the foreign currency exchange rate.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. TAXES, SPENDING & INTEREST RATES -->
    <div style="margin-bottom: 50px;">
        <div id="sec-economic-policies" class="lecture-interactive-card" data-lecture-section="sec_economic_policies" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 4. TAXES, SPENDING &amp; INTEREST RATES</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Governments manage demand and productive supply capacity through Fiscal, Monetary, and Supply-Side policies.
            </p>
        </div>

        <!-- SUB-CARD: POLICY TOOLS -->
        <div id="card-policy-tools" class="lecture-interactive-card" data-lecture-section="card_policy_tools" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">⚖️ Fiscal Policy vs Monetary Policy vs Supply-Side Policy</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px; padding: 16px;">
                    <b style="color: #c2410c; font-size: 15px;">🏛️ Fiscal Policy (Taxation &amp; Spending):</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #9a3412; line-height: 1.5;">
                        <b>Higher Income Tax</b> reduces disposable consumer spending. <b>Higher Corporation Tax</b> shrinks retained profits. <b>Infrastructure Spending</b> boosts logistics efficiency and creates construction jobs.
                    </p>
                </div>

                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 16px;">
                    <b style="color: #1d4ed8; font-size: 15px;">🏦 Monetary Policy (Interest Rates):</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #1e40af; line-height: 1.5;">
                        <b>Higher base rates</b> increase loan interest expenses, encourage saving over spending, and cause domestic currency appreciation, making exports uncompetitive overseas.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-business-policy-response" class="lecture-interactive-card" data-lecture-section="sec_business_policy_response" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 5. HOW BUSINESSES RESPOND TO ECONOMIC POLICY (Cambridge Exam Guide)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Cambridge questions regularly ask: <i>"Explain the impact of an interest rate increase on this business and recommend two suitable strategies."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #ef4444; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #b91c1c; font-size: 15px;">Impact of Rising Interest Rates:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Borrowing costs jump on overdrafts and mortgages; consumer credit dries up. <b>Response:</b> Postpone capital factory projects; switch to fixed-rate debt; slash luxury price tags.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #f59e0b; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #b45309; font-size: 15px;">Impact of Increased Income Tax:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Consumers suffer lower take-home pay. <b>Response:</b> Introduce promotional discounts (BOGO), focus on value-for-money essentials, and expand into low-tax export markets.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">6.1 Economic Issues (Các Vấn đề Kinh tế vĩ mô)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 6.1 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/6_1_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 6.1 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
