import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 1.5 ID
LID = 'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3'
CODE = '1_5'
TITLE = '1.5 Business objectives and stakeholder objectives'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 9 AUDIO SEGMENTS FOR LESSON 1.5
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.5: Mục tiêu doanh nghiệp và các bên liên quan",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 1.5: Business Objectives and Stakeholder Objectives. In this concluding lesson of Unit 1, we analyse why enterprises formulate strategic aims, contrast private profit targets with public service mandates, identify internal and external stakeholders, and resolve the inevitable conflicts between differing stakeholder priorities.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 1.5: Mục tiêu doanh nghiệp và Mục tiêu của các bên liên quan. Trong bài học kết thúc Chủ đề một này, chúng ta sẽ phân tích lý do doanh nghiệp thiết lập mục tiêu chiến lược, so sánh mục tiêu lợi nhuận của khu vực tư nhân với mục tiêu dịch vụ công, nhận diện các bên liên quan nội bộ và bên ngoài, cùng các giải pháp xử lý xung đột quyền lợi."
    },
    {
        "id": "sec_business_objectives",
        "title": "1. Mục tiêu Kinh doanh & 4 Lợi ích Cốt lõi",
        "selector": "#sec-business-objectives",
        "en": "Section 1 defines business objectives as measurable targets that direct corporate activities. Setting clear objectives provides strategic focus, unites managers and employees toward common goals, motivates the workforce through clear milestones, guides critical decision-making, and establishes quantifiable benchmarks to evaluate overall business performance.",
        "vi": "Mục 1 định nghĩa mục tiêu kinh doanh là các đích đến đo lường được để định hướng toàn bộ hoạt động của doanh nghiệp. Việc xác lập mục tiêu rõ ràng giúp vạch ra định hướng chiến lược, gắn kết ban quản trị và nhân viên, tạo động lực phấn đấu, hỗ trợ ra quyết định kinh doanh chính xác và cung cấp tiêu chuẩn định lượng để đánh giá hiệu quả hoạt động."
    },
    {
        "id": "card_private_objectives",
        "title": "🏢 4 Mục tiêu Trọng tâm của Khu vực Tư nhân",
        "selector": "#card-private-objectives",
        "en": "Private sector firms pursue four primary commercial objectives: short-term survival during economic recessions or initial launch; profit maximization to provide returns for owners and fund capital reinvestment; continuous growth to exploit economies of scale and dominate industries; and expanding market share to cement brand loyalty.",
        "vi": "Các doanh nghiệp khu vực tư nhân theo đuổi 4 mục tiêu thương mại trọng tâm: mục tiêu sinh tồn (survival) trong giai đoạn khởi nghiệp hoặc suy thoái kinh tế; tối đa hóa lợi nhuận (profit) để trả cổ tức cho cổ đông và tái đầu tư mở rộng; tăng trưởng quy mô (growth) nhằm tận dụng tính kinh tế của quy mô; và gia tăng thị phần (market share) để khẳng định vị thế thương hiệu dẫn đầu."
    },
    {
        "id": "card_social_enterprise",
        "title": "🤝 Doanh nghiệp Xã hội & Mô hình Triple Bottom Line (3Ps)",
        "selector": "#card-social-enterprise",
        "en": "A social enterprise operates with primarily social objectives, reinvesting operational surpluses to benefit society rather than maximizing payouts to private shareholders. It balances the Triple Bottom Line: People, protecting employees and community welfare; Planet, minimizing environmental footprint through green sustainable practices; and Profit, generating self-sustaining financial surplus.",
        "vi": "Doanh nghiệp xã hội (Social enterprise) vận hành chủ yếu vì các mục tiêu xã hội, tái đầu tư toàn bộ thặng dư tài chính vào các hoạt động cộng đồng thay vì chi trả cổ tức tối đa cho cổ đông tư nhân. Mô hình này cân bằng ba yếu tố (Triple Bottom Line - 3 chữ P): Con người (People - bảo vệ quyền lợi lao động và hỗ trợ người yếu thế); Hành tinh (Planet - bảo vệ môi trường, giảm phát thải và tái chế); và Lợi nhuận (Profit - tạo ra thặng dư tài chính để tự chủ vận hành lâu dài)."
    },
    {
        "id": "sec_public_objectives",
        "title": "2. Mục tiêu của Doanh nghiệp Khu vực Nhà nước",
        "selector": "#sec-public-objectives",
        "en": "Section 2 contrasts public sector targets with private commerce. State corporations pursue three mandates: Financial targets to meet government budget benchmarks; Service targets guaranteeing universal, reliable, and high-quality access for all citizens; and Social targets creating stable employment, keeping prices subsidized, and fostering balanced regional development.",
        "vi": "Mục 2 đối chiếu mục tiêu của khu vực nhà nước với thương mại tư nhân. Các tổng công ty nhà nước hướng tới 3 nhóm mục tiêu: Mục tiêu tài chính nhằm đạt chỉ tiêu ngân sách chính phủ giao; Mục tiêu dịch vụ bảo đảm cung ứng dịch vụ công thiết yếu đáng tin cậy với chất lượng cao cho toàn dân; và Mục tiêu xã hội giúp tạo việc làm ổn định, trợ giá hàng hóa thiết yếu và thúc đẩy phát triển kinh tế vùng sâu vùng xa."
    },
    {
        "id": "sec_stakeholders",
        "title": "3. Khái niệm Các Bên Liên quan (Stakeholders)",
        "selector": "#sec-stakeholders",
        "en": "Section 3 defines a stakeholder as any individual or organized group that has a direct interest in, or is affected by, the operations, decisions, and performance of a business. Stakeholders are divided into internal participants and external community members.",
        "vi": "Mục 3 định nghĩa các bên liên quan (stakeholders) là bất kỳ cá nhân hoặc tổ chức nào có lợi ích trực tiếp, hoặc chịu tác động từ các hoạt động, quyết định và kết quả kinh doanh của doanh nghiệp. Các bên liên quan được phân chia thành nhóm nội bộ bên trong và nhóm cộng đồng bên ngoài."
    },
    {
        "id": "card_internal_stakeholders",
        "title": "🏢 Các Bên Liên quan Nội bộ (Internal Stakeholders)",
        "selector": "#card-internal-stakeholders",
        "en": "Internal stakeholders operate directly inside the firm: Shareholders and owners demand strong returns on capital and rising share values; Workers demand job security, safe conditions, fair treatment, and living wages; and Managers seek career advancement, higher salaries, executive bonuses, and the prestige of running growing organisations.",
        "vi": "Các bên liên quan nội bộ hoạt động trực tiếp bên trong doanh nghiệp: Cổ đông và chủ sở hữu đòi hỏi tỷ suất sinh lời cao trên vốn đầu tư và giá trị cổ phiếu gia tăng; Người lao động đòi hỏi hợp đồng minh bạch, công việc an toàn, môi trường công bằng và tiền lương xứng đáng; và Ban quản lý tìm kiếm sự thăng tiến nghề nghiệp, mức lương thưởng cao cùng uy tín quản trị."
    },
    {
        "id": "card_external_stakeholders",
        "title": "🌍 Các Bên Liên quan Bên ngoài (External Stakeholders)",
        "selector": "#card-external-stakeholders",
        "en": "External stakeholders exist outside daily company boundaries: Customers expect safe, reliable products priced fairly; Governments demand compliance with labour and tax laws, rising employment, and fiscal contributions; Banks demand steady interest payments and guaranteed capital repayment; and the Local Community demands job opportunities and environmental preservation without toxic pollution.",
        "vi": "Các bên liên quan bên ngoài hiện diện bên ngoài ranh giới doanh nghiệp: Khách hàng kỳ vọng sản phẩm an toàn, chất lượng tương xứng với giá tiền; Chính phủ đòi hỏi tuân thủ nghiêm pháp luật lao động, nộp thuế đầy đủ và mở rộng việc làm; Ngân hàng đòi hỏi khả năng thanh toán lãi vay đúng hạn và bảo toàn vốn gốc; và Cộng đồng địa phương mong muốn có thêm việc làm, sản xuất không gây ô nhiễm môi trường."
    },
    {
        "id": "sec_stakeholder_conflicts",
        "title": "⚔️ 4. Xung đột Mục tiêu giữa các Bên Liên quan",
        "selector": "#sec-stakeholder-conflicts",
        "en": "Section 4 analyses unavoidable stakeholder conflicts. Satisfying one group frequently harms another: paying higher wages satisfies workers but slashes shareholder profits; building new factories creates jobs but causes noise and air pollution that outrages the community; and raising prices increases profit margins but angers customers. Successful managers must negotiate pragmatic compromises, adopting corporate social responsibility to achieve sustainable long-term equilibrium.",
        "vi": "Mục 4 phân tích các mâu thuẫn quyền lợi không thể tránh khỏi giữa các bên liên quan. Thỏa mãn mục tiêu của nhóm này thường xâm phạm lợi ích của nhóm khác: tăng lương làm hài lòng người lao động nhưng lại bào mòn lợi nhuận của cổ đông; xây thêm nhà máy tạo việc làm nhưng lại gây khói bụi và tiếng ồn khiến cư dân phản đối; và tăng giá bán giúp tăng lợi nhuận nhưng lại khiến khách hàng rời bỏ. Nhà quản trị giỏi phải biết dung hòa, thực hiện trách nhiệm xã hội doanh nghiệp để đạt được sự phát triển hài hòa bền vững."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_business_objectives": {"start": 1, "end": 3},
    "sec_public_objectives": {"start": 4, "end": 4},
    "sec_stakeholders": {"start": 5, "end": 7},
    "sec_stakeholder_conflicts": {"start": 8, "end": 8}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.5 Business Objectives and Stakeholder Objectives (Mục tiêu Doanh nghiệp &amp; Các bên liên quan)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. BUSINESS OBJECTIVES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-business-objectives" class="lecture-interactive-card" data-lecture-section="sec_business_objectives" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🎯 1. BUSINESS OBJECTIVES</h2>
            <div style="background: #eff6ff; border-left: 5px solid #3b82f6; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.6;">
                Business objectives are the <b>aims and quantifiable targets</b> that an enterprise works towards to direct operations and achieve long-term success.
            </div>
            <h4 style="color: #1e3a8a; font-size: 16px; margin: 0 0 12px 0;">🌟 4 Key Benefits of Setting Objectives:</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;">
                    <b style="color: #2563eb;">🔥 Motivates workforce:</b> Gives staff clear milestones to work towards.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;">
                    <b style="color: #2563eb;">⚡ Guides decisions:</b> Fast decisions based on clear strategic targets.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;">
                    <b style="color: #2563eb;">🤝 Unites business:</b> Reduces conflicts by aligning all departments.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 14px; border-radius: 8px; font-size: 13.5px;">
                    <b style="color: #2563eb;">📊 Performance benchmark:</b> Enables managers to assess success accurately.
                </div>
            </div>
        </div>

        <div id="card-private-objectives" class="lecture-interactive-card" data-lecture-section="card_private_objectives" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 19px; margin-top: 0; margin-bottom: 14px;">🏢 4 Core Objectives of Private Sector Businesses</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-bottom: 14px;">
                <div style="background: #fff5f5; border: 1px solid #fecaca; border-left: 4px solid #dc2626; border-radius: 8px; padding: 14px;">
                    <b style="color: #dc2626; font-size: 15px;">🛡️ Survival</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">Key priority for startups or during recessions; firms lower prices to keep trading.</p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 4px solid #16a34a; border-radius: 8px; padding: 14px;">
                    <b style="color: #16a34a; font-size: 15px;">💰 Profit Maximization</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">Provides returns for shareholders and capital for future reinvestment.</p>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-left: 4px solid #2563eb; border-radius: 8px; padding: 14px;">
                    <b style="color: #2563eb; font-size: 15px;">📈 Growth</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">Achieves economies of scale, lowers unit costs, and enhances market influence.</p>
                </div>
                <div style="background: #faf5ff; border: 1px solid #e9d5ff; border-left: 4px solid #9333ea; border-radius: 8px; padding: 14px;">
                    <b style="color: #9333ea; font-size: 15px;">🥧 Market Share</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">Proportion of total market sales gained; cements brand dominance and customer loyalty.</p>
                </div>
            </div>
            <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 10px 14px; border-radius: 6px; font-size: 13.5px; color: #92400e;">
                <b>⚠️ Note:</b> Objectives evolve over time. A firm focusing on survival in a slump will shift to profit once established.
            </div>
        </div>

        <div id="card-social-enterprise" class="lecture-interactive-card" data-lecture-section="card_social_enterprise" style="background: #f0fdfa; border: 1.5px solid #99f6e4; border-left: 5px solid #0d9488; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s;">
            <h4 style="color: #0d9488; font-size: 18px; margin: 0 0 10px 0; display: flex; align-items: center; gap: 8px;">
                <span>🤝</span> Objectives of Social Enterprises (Triple Bottom Line - 3Ps)
            </h4>
            <p style="margin: 0 0 12px 0; font-size: 14.5px; color: #334155; line-height: 1.6;">
                A <b>social enterprise</b> balances social and environmental missions with commercial independence, reinvesting profits into society:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
                <div style="background: #ffffff; padding: 12px 14px; border-radius: 8px; border: 1px solid #ccfbf1; font-size: 13.5px;">
                    <b style="color: #0f766e;">1. People (Social):</b> Support disadvantaged communities, provide jobs and healthcare.
                </div>
                <div style="background: #ffffff; padding: 12px 14px; border-radius: 8px; border: 1px solid #ccfbf1; font-size: 13.5px;">
                    <b style="color: #15803d;">2. Planet (Environmental):</b> Use sustainable raw materials and minimize carbon footprint.
                </div>
                <div style="background: #ffffff; padding: 12px 14px; border-radius: 8px; border: 1px solid #ccfbf1; font-size: 13.5px;">
                    <b style="color: #b45309;">3. Profit (Financial):</b> Generate enough surplus to remain solvent and fund social goals.
                </div>
            </div>
        </div>
    </div>

    <!-- 2. PUBLIC-SECTOR OBJECTIVES -->
    <div id="sec-public-objectives" class="lecture-interactive-card" data-lecture-section="sec_public_objectives" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏛️ 2. PUBLIC-SECTOR BUSINESS OBJECTIVES</h2>
        <p style="font-size: 15px; color: #475569; margin: 0 0 16px 0; line-height: 1.6;">
            Government-owned enterprises do not aim for profit maximization. Instead, they pursue public welfare mandates:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; margin-bottom: 20px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #059669; font-size: 15px;">💵 Financial Target:</b> Meet budgets set by the treasury to fund operations responsibly.
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #059669; font-size: 15px;">🛎️ Service Target:</b> Provide essential services (water, rail, health) to high quality standards.
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #059669; font-size: 15px;">🌍 Social Target:</b> Protect jobs, maintain universal affordability, and support regional growth.
            </div>
        </div>

        <div style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 10px; overflow: hidden;">
            <div style="background: #0f766e; color: #ffffff; padding: 10px 16px; font-weight: bold; font-size: 15px;">
                ⚖️ Differences Between Private and Public Sector Objectives
            </div>
            <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13.5px;">
                    <thead>
                        <tr style="background: #f1f5f9; color: #0f172a; border-bottom: 2px solid #cbd5e1;">
                            <th style="padding: 10px 14px;">Feature</th>
                            <th style="padding: 10px 14px;">Private Sector</th>
                            <th style="padding: 10px 14px;">Public Sector</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold;">Main Objective</td>
                            <td style="padding: 10px 14px; color: #16a34a;">Profit maximization &amp; shareholder value.</td>
                            <td style="padding: 10px 14px; color: #0284c7;">Public service &amp; citizen welfare.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                            <td style="padding: 10px 14px; font-weight: bold;">Funding Source</td>
                            <td style="padding: 10px 14px;">Private share capital &amp; commercial loans.</td>
                            <td style="padding: 10px 14px;">Taxpayer funds &amp; government budget.</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 14px; font-weight: bold;">Accountability</td>
                            <td style="padding: 10px 14px;">Accountable to private shareholders.</td>
                            <td style="padding: 10px 14px;">Accountable to parliament &amp; taxpayers.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- 3. STAKEHOLDERS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-stakeholders" class="lecture-interactive-card" data-lecture-section="sec_stakeholders" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">👥 3. STAKEHOLDERS</h2>
            <div style="background: #fff7ed; border-left: 5px solid #ea580c; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #9a3412; line-height: 1.6;">
                A <b>stakeholder</b> is any person or group that is interested in or directly affected by the performance, decisions, and activities of a business.
            </div>
        </div>

        <div id="card-internal-stakeholders" class="lecture-interactive-card" data-lecture-section="card_internal_stakeholders" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🏢 Internal Stakeholders (Work for or own the business)</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">💼 Shareholders / Owners</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13.5px; color: #475569;">Invest capital and bear commercial risk.</p>
                    <div style="font-size: 13px; color: #16a34a;"><b>🎯 Objectives:</b> High return on capital (dividends) and share price growth.</div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">👷 Workers</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13.5px; color: #475569;">Employed staff directly involved in operations.</p>
                    <div style="font-size: 13px; color: #1d4ed8;"><b>🎯 Objectives:</b> Job security, fair wages, safe working conditions.</div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">👔 Managers</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13.5px; color: #475569;">Control business operations and make decisions.</p>
                    <div style="font-size: 13px; color: #7e22ce;"><b>🎯 Objectives:</b> High salary bonuses, career status, and business expansion.</div>
                </div>
            </div>
        </div>

        <div id="card-external-stakeholders" class="lecture-interactive-card" data-lecture-section="card_external_stakeholders" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🌍 External Stakeholders (Outside the business)</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #0f172a;">🛒 Customers:</b> Demand reliable, safe products at reasonable prices.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #0f172a;">🏛️ Government:</b> Expects legal compliance, tax revenue, and job creation.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #0f172a;">🏦 Banks:</b> Demand regular loan interest payments and sound liquidity.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #0f172a;">🏘️ Community:</b> Demands local employment without environmental pollution.
                </div>
            </div>
        </div>
    </div>

    <!-- 4. CONFLICTS OF STAKEHOLDERS' OBJECTIVES -->
    <div id="sec-stakeholder-conflicts" class="lecture-interactive-card" data-lecture-section="sec_stakeholder_conflicts" style="margin-bottom: 45px; padding: 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚔️ 4. CONFLICTS OF STAKEHOLDERS' OBJECTIVES</h2>
        <p style="font-size: 15px; color: #475569; margin: 0 0 16px 0; line-height: 1.6;">
            Because different stakeholders pursue conflicting interests, businesses cannot satisfy everyone at once. Managers must negotiate compromises:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
            <div style="display: flex; flex-wrap: wrap; align-items: stretch; border: 1.5px solid #e2e8f0; border-radius: 10px; overflow: hidden;">
                <div style="flex: 1; min-width: 200px; background: #eff6ff; padding: 14px 18px; text-align: center;">
                    <b style="color: #1d4ed8; font-size: 15px;">👷‍♂️ Workers:</b> Want higher wages and benefits.
                </div>
                <div style="display: flex; align-items: center; justify-content: center; background: #f1f5f9; padding: 10px 16px; font-weight: bold; color: #64748b;">
                    VS
                </div>
                <div style="flex: 1; min-width: 200px; background: #fdf2f8; padding: 14px 18px; text-align: center;">
                    <b style="color: #be185d; font-size: 15px;">💼 Shareholders:</b> Higher wage costs reduce profit dividends.
                </div>
            </div>

            <div style="display: flex; flex-wrap: wrap; align-items: stretch; border: 1.5px solid #e2e8f0; border-radius: 10px; overflow: hidden;">
                <div style="flex: 1; min-width: 200px; background: #f0fdf4; padding: 14px 18px; text-align: center;">
                    <b style="color: #15803d; font-size: 15px;">🏢 The Business:</b> Wants to expand factories for scale.
                </div>
                <div style="display: flex; align-items: center; justify-content: center; background: #f1f5f9; padding: 10px 16px; font-weight: bold; color: #64748b;">
                    VS
                </div>
                <div style="flex: 1; min-width: 200px; background: #fef2f2; padding: 14px 18px; text-align: center;">
                    <b style="color: #b91c1c; font-size: 15px;">🏘️ Community:</b> Protests noise, traffic, and pollution.
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
    pattern = r'<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">[\s\S]*?</div>'
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">1.5 Business Objectives and Stakeholder Objectives (Mục tiêu Doanh nghiệp &amp; Các bên liên quan)</h1>
        </div>
    </div>"""
    new_p2 = re.sub(pattern, header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 1.5 Audio and HTML ===")
    
    # 0. Clean stale audio files so that all 9 segments match perfectly
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)
    valid_ids = {s['id'] for s in segments}
    for fname in os.listdir(audio_dir):
        if fname.endswith('.mp3'):
            base_id = fname[:-4]
            if base_id not in valid_ids or base_id in {'sec_business_objectives', 'sec_public_objectives', 'sec_stakeholders', 'sec_stakeholder_conflicts'}:
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
    with open('scripts/bs_1_5_page_2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 1.5 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
