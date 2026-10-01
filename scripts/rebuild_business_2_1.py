import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 2.1 ID
LID = 'cd1763a9-f030-4be1-b65b-c6dc6dde91c9'
CODE = '2_1'
TITLE = '2.1. Motivating employees'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 15 AUDIO SEGMENTS FOR LESSON 2.1
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 2.1: Động lực làm việc của nhân viên",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 2.1: Motivating Employees. In this opening chapter of Topic 2, People in Business, we examine why employee motivation is critical to enterprise performance, unpack classical theories by Taylor, Maslow, and Herzberg, and analyze financial and non-financial motivation methods.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 2.1: Động lực làm việc của nhân viên. Trong bài mở đầu của Chủ đề hai về Con người trong Doanh nghiệp, chúng ta sẽ phân tích tầm quan trọng của động lực lao động, các học thuyết kinh điển của Taylor, Maslow, Herzberg, cùng các phương pháp tạo động lực bằng tài chính và phi tài chính."
    },
    {
        "id": "sec_motivation_work",
        "title": "1. Vai trò của Động lực lao động",
        "selector": "#sec-motivation-work",
        "en": "Section 1 defines motivation as the internal and external factors that stimulate desire and energy in workers to remain committed to a job. A highly motivated workforce drives higher labour productivity, lowers absenteeism, cuts employee turnover and recruitment expenses, improves customer service quality, and fosters workplace innovation.",
        "vi": "Mục một định nghĩa động lực là các yếu tố kích thích sự nhiệt huyết và năng lượng của người lao động để cống hiến cho công việc. Lực lượng lao động có động lực cao sẽ nâng cao năng suất lao động, giảm tỷ lệ vắng mặt, cắt giảm chi phí tuyển dụng do nhân viên thôi việc, nâng cao chất lượng dịch vụ khách hàng và thúc đẩy tinh thần đổi mới sáng tạo."
    },
    {
        "id": "card_why_work",
        "title": "🤔 Vì sao con người cần làm việc?",
        "selector": "#card-why-work",
        "en": "People work for multiple reasons: earning income to achieve a better standard of living for needs and wants; financial security against illness or retirement; social interaction and belonging; gaining professional status and respect; and experiencing intrinsic job satisfaction from completing meaningful tasks.",
        "vi": "Con người làm việc vì nhiều lý do: kiếm thu nhập để nâng cao mức sống và thỏa mãn nhu cầu; đảm bảo an toàn tài chính trước các rủi ro ốm đau hay hưu trí; giao lưu xã hội và tìm kiếm cảm giác hòa nhập tập thể; xây dựng địa vị và sự tôn trọng trong xã hội; và tận hưởng niềm vui thỏa mãn nội tại khi hoàn thành tốt công việc ý nghĩa."
    },
    {
        "id": "card_why_motivate",
        "title": "🎯 Lợi ích then chốt khi Doanh nghiệp Tạo động lực cho Nhân viên",
        "selector": "#card-why-motivate",
        "en": "Firms must motivate workers because motivated staff demonstrate high productivity, reducing unit costs. They take fewer sick days, which minimizes absenteeism and avoids production bottlenecks. Furthermore, low labour turnover retains experienced talent, saving substantial recruitment and training expenditures, directly driving higher corporate profitability.",
        "vi": "Doanh nghiệp phải tạo động lực cho nhân viên vì nhân viên có tinh thần tốt sẽ tạo ra năng suất vượt trội, giúp hạ giá thành đơn vị. Họ ít nghỉ ốm, giảm tỷ lệ vắng mặt và tránh ách tắc sản xuất. Hơn nữa, tỷ lệ nghỉ việc thấp giúp giữ chân nhân tài lâu năm, tiết kiệm chi phí tuyển dụng và đào tạo tốn kém, trực tiếp gia tăng lợi nhuận công ty."
    },
    {
        "id": "sec_theories",
        "title": "2. Tổng quan các Học thuyết Động lực",
        "selector": "#sec-theories",
        "en": "Section 2 introduces three foundational motivation frameworks examined in the Cambridge syllabus: F.W. Taylor's Scientific Management, Abraham Maslow's Hierarchy of Needs, and Frederick Herzberg's Two-Factor Theory. Understanding how psychological needs evolve is essential for designing effective workforce rewards.",
        "vi": "Mục hai giới thiệu ba học thuyết động lực nền tảng trong chương trình Cambridge: Quản trị khoa học của F.W. Taylor, Tháp nhu cầu của Abraham Maslow và Thuyết hai yếu tố của Frederick Herzberg. Hiểu rõ sự phát triển nhu cầu tâm lý là cơ sở để thiết kế chính sách đãi ngộ nhân sự hiệu quả."
    },
    {
        "id": "card_taylor",
        "title": "👨‍💼 F. W. Taylor: Quản trị theo Khoa học (Scientific Management)",
        "selector": "#card-taylor",
        "en": "F.W. Taylor viewed workers as purely rational economic agents driven by financial gain. His scientific management model breaks down tasks into standard repetitive movements and links compensation directly to output through differential piece-rates. While effective for simple factory production lines, Taylorism ignores social belonging, causes workplace boredom, and neglects intrinsic job satisfaction.",
        "vi": "F.W. Taylor coi người lao động là những cá nhân kinh tế thuần túy hành động vì tiền bạc. Mô hình quản trị khoa học chia nhỏ quy trình thành các thao tác chuẩn mực lặp đi lặp lại và trả lương theo sản phẩm (piece-rate). Dù rất hiệu quả trong các dây chuyền sản xuất đơn giản, học thuyết Taylor bỏ qua nhu cầu xã hội, gây ra sự nhàm chán và xem nhẹ niềm vui công việc nội tại."
    },
    {
        "id": "card_maslow",
        "title": "🔺 Tháp Nhu cầu của Abraham Maslow",
        "selector": "#card-maslow",
        "en": "Abraham Maslow proposed that human beings are motivated by five ascending tiers of needs: physiological survival, safety and job security, social belonging and team camaraderie, esteem and recognition, and finally self-actualisation. Once a lower-level need is satisfied, it ceases to motivate, and the individual strives to fulfil the next level.",
        "vi": "Abraham Maslow đưa ra hệ thống phân cấp gồm năm tầng nhu cầu: sinh lý căn bản, an toàn và việc làm ổn định, xã hội và gắn kết đồng đội, được tôn trọng và công nhận, và cuối cùng là hoàn thiện bản thân (self-actualisation). Khi một nhu cầu bậc thấp đã được thỏa mãn, nó không còn là động lực thúc đẩy nữa và con người sẽ hướng lên bậc cao hơn."
    },
    {
        "id": "card_herzberg",
        "title": "⚖️ Thuyết Hai Yếu tố của Frederick Herzberg",
        "selector": "#card-herzberg",
        "en": "Herzberg separated workplace drivers into Hygiene factors and Motivators. Hygiene factors, such as basic pay, clean working conditions, company policy, and job security, prevent dissatisfaction but cannot stimulate superior performance. True motivation comes exclusively from Motivators: achievement, meaningful responsibility, personal recognition, and career advancement.",
        "vi": "Herzberg chia các yếu tố nơi làm việc thành Yếu tố duy trì (Hygiene factors) và Yếu tố tạo động lực (Motivators). Yếu tố duy trì như mức lương cơ bản, điều kiện làm việc, chính sách công ty và sự an toàn chỉ giúp ngăn ngừa bất mãn chứ không tạo ra động lực bứt phá. Động lực thực sự chỉ đến từ các yếu tố thúc đẩy: thành tựu, trách nhiệm công việc, sự công nhận và cơ hội thăng tiến."
    },
    {
        "id": "sec_financial",
        "title": "3. Phương pháp tạo Động lực bằng Tài chính",
        "selector": "#sec-financial",
        "en": "Section 3 evaluates financial reward systems: hourly wages, fixed salaries, piece rates, sales commissions, performance-related bonuses, profit sharing, and share ownership schemes. While financial rewards are direct and quantifiable, over-reliance on individual incentives can sacrifice product quality, undermine teamwork, and escalate total operational costs.",
        "vi": "Mục ba đánh giá các phương thức đãi ngộ tài chính: tiền công theo giờ, tiền lương cố định, trả theo sản phẩm, hoa hồng bán hàng, tiền thưởng hiệu suất, chia sẻ lợi nhuận và cổ phiếu thưởng. Mặc dù khuyến khích tài chính mang lại tác dụng tức thì, việc quá phụ thuộc vào tiền thưởng cá nhân có thể làm giảm chất lượng sản phẩm, chia rẽ tinh thần đồng đội và đẩy chi phí vận hành tăng vọt."
    },
    {
        "id": "card_wages_salaries",
        "title": "💵 Tiền công theo thời gian, theo sản phẩm & Tiền lương cố định",
        "selector": "#card-wages-salaries",
        "en": "Wages and salaries represent standard base remuneration: Time-rate pays hourly, providing income certainty but not rewarding higher effort; Piece-rate pays per unit manufactured, strongly boosting output volume but risking poor quality; and Salaries provide fixed monthly payments for management and white-collar professionals.",
        "vi": "Tiền công và tiền lương đại diện cho các hình thức thù lao cơ bản: Trả theo thời gian (Time-rate) tính theo giờ làm việc, mang lại sự an tâm nhưng không thưởng thêm cho nỗ lực vượt bậc; Trả theo sản phẩm (Piece-rate) trả theo số lượng hoàn thành, kích thích sản lượng tối đa nhưng dễ làm sút giảm chất lượng; và Tiền lương (Salary) là khoản chi trả cố định hàng tháng cho cấp quản lý và nhân viên văn phòng."
    },
    {
        "id": "card_incentive_pay",
        "title": "🎁 Hoa hồng, Tiền thưởng, Đánh giá hiệu suất & Cổ phiếu thưởng",
        "selector": "#card-incentive-pay",
        "en": "Incentive pay structures link reward to commercial success: Sales commissions offer a percentage of revenue sold; Lump-sum bonuses reward exceptional achievement; Performance-related pay reflects appraisal ratings; and Profit sharing with employee share ownership aligns staff interests directly with long-term shareholder value.",
        "vi": "Các cấu trúc thù lao khuyến khích gắn liền quyền lợi nhân viên với kết quả kinh doanh: Hoa hồng (Commission) trích tỷ lệ phần trăm theo doanh số bán; Tiền thưởng (Bonus) trao cho các thành tích vượt chỉ tiêu; Lương theo hiệu suất (PRP) dựa vào kết quả đánh giá năng lực; và Chia sẻ lợi nhuận cùng Cổ phiếu thưởng (Share ownership) giúp gắn kết lợi ích lâu dài của nhân viên với giá trị công ty."
    },
    {
        "id": "sec_non_financial",
        "title": "4. Phương pháp tạo Động lực Phi tài chính",
        "selector": "#sec-non-financial",
        "en": "Section 4 investigates non-financial motivators and job redesign. Techniques include job rotation to relieve monotony, job enlargement to broaden variety, and job enrichment to delegate higher-level decision making. Combined with teamworking, flexible working hours, and subsidized fringe benefits, non-financial strategies foster long-term loyalty and deep intrinsic job engagement.",
        "vi": "Mục bốn phân tích các giải pháp phi tài chính và thiết kế lại công việc. Các kỹ thuật bao gồm luân chuyển công việc (job rotation) giảm sự nhàm chán, mở rộng công việc (job enlargement) tăng thêm đầu việc tương đương, và làm giàu công việc (job enrichment) trao thêm quyền tự quyết cao hơn. Kết hợp cùng làm việc nhóm, giờ giấc linh hoạt và phúc lợi phụ cấp, phương pháp phi tài chính giúp xây dựng lòng trung thành bền vững."
    },
    {
        "id": "card_fringe_benefits",
        "title": "🚗 Phúc lợi Bổ sung (Fringe Benefits / Perks)",
        "selector": "#card-fringe-benefits",
        "en": "Fringe benefits are non-cash perks provided alongside regular wages. Examples include company cars, private health insurance, subsidized housing, staff discounts, free holidays, and children's education allowances. These benefits elevate social status, ease living expenses, and foster strong organizational commitment.",
        "vi": "Phúc lợi bổ sung (Fringe benefits) là các đãi ngộ phi tiền mặt đi kèm tiền lương chính. Ví dụ như xe ô tô công vụ, bảo hiểm y tế tư nhân, nhà ở trợ cấp, phiếu giảm giá mua hàng, kỳ nghỉ dưỡng miễn phí và học bổng cho con em nhân viên. Những đãi ngộ này giúp nâng cao vị thế xã hội, giảm áp lực sinh hoạt và thắt chặt cam kết gắn bó của nhân viên với công ty."
    },
    {
        "id": "card_job_satisfaction",
        "title": "🔄 Thiết kế Công việc & Tạo sự Thỏa mãn Nghề nghiệp",
        "selector": "#card-job-satisfaction",
        "en": "Job satisfaction is enhanced through strategic work redesign: Job rotation swaps tasks to prevent monotony; Job enlargement adds diverse tasks of equal skill level; Job enrichment delegates greater autonomy, complex challenge, and responsibility; while Autonomous teamworking empowers groups to coordinate projects collaboratively.",
        "vi": "Sự thỏa mãn nghề nghiệp được nâng cao thông qua việc thiết kế lại công việc: Luân chuyển công việc (Job rotation) hoán đổi vị trí định kỳ để chống đơn điệu; Mở rộng công việc (Job enlargement) bổ sung thêm các đầu việc có kỹ năng tương đương; Làm giàu công việc (Job enrichment) trao thêm quyền tự quyết và thử thách phức tạp hơn; trong khi Làm việc nhóm (Team-working) trao quyền cho tập thể cùng phối hợp hoàn thành mục tiêu chung."
    },
    {
        "id": "sec_recommend_motivation",
        "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất phương pháp tạo động lực",
        "selector": "#sec-recommend-motivation",
        "en": "Section 5 details the Cambridge evaluation strategy for motivation questions. Candidates must tailor recommendations to employee types and business context: factory operatives often respond to piece rates and bonuses, whereas creative and professional staff prioritize autonomy and enrichment. Conclude by balancing financial cost against potential productivity gains.",
        "vi": "Mục năm cung cấp chiến lược làm bài thi Cambridge cho các câu hỏi đánh giá tạo động lực. Thí sinh phải gắn giải pháp với từng đối tượng lao động và bối cảnh cụ thể: công nhân sản xuất thường phản ứng tốt với lương sản phẩm và thưởng năng suất, trong khi chuyên gia sáng tạo lại coi trọng sự tự chủ và trao quyền. Luôn kết luận bằng cách cân đối giữa chi phí tài chính và mức tăng năng suất dự kiến."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_motivation_work": {"start": 1, "end": 3},
    "sec_theories": {"start": 4, "end": 7},
    "sec_financial": {"start": 8, "end": 10},
    "sec_non_financial": {"start": 11, "end": 13},
    "sec_recommend_motivation": {"start": 14, "end": 14}
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
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 2</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.1 Motivating Employees (Động lực làm việc của nhân viên)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. MOTIVATION AT WORK -->
    <div style="margin-bottom: 45px;">
        <div id="sec-motivation-work" class="lecture-interactive-card" data-lecture-section="sec_motivation_work" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🚀 1. MOTIVATION AT WORK</h2>
            <div style="background: #eff6ff; border-left: 5px solid #3b82f6; padding: 15px 20px; border-radius: 8px; font-size: 15.5px; color: #1e40af; margin-bottom: 10px; line-height: 1.6;">
                <b>Motivation</b> is the reason why employees want to work hard and work effectively for the business.
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 18px;">
            <div id="card-why-work" class="lecture-interactive-card" data-lecture-section="card_why_work" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; box-shadow: 0 3px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #2563eb; font-size: 18px; margin: 0 0 12px 0;">🤔 Why do people work?</h4>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 14px; line-height: 1.6;">
                    <li><b>Better standard of living:</b> Earning incomes to satisfy needs and wants.</li>
                    <li><b>Security:</b> Maintaining financial safety against illness or retirement.</li>
                    <li><b>Experience &amp; Status:</b> Building competence and earning reputable social status.</li>
                    <li><b>Job satisfaction:</b> The intrinsic pleasure of doing a meaningful job well.</li>
                </ul>
            </div>

            <div id="card-why-motivate" class="lecture-interactive-card" data-lecture-section="card_why_motivate" style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 12px; padding: 20px; box-shadow: 0 3px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <h4 style="color: #15803d; font-size: 18px; margin: 0 0 10px 0;">🎯 Why must firms motivate workers?</h4>
                <p style="margin: 0 0 8px 0; font-size: 14px; color: #166534;">Well-motivated workers become:</p>
                <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 14px; line-height: 1.6;">
                    <li><b>Highly productive:</b> Producing greater output and lowering unit costs.</li>
                    <li><b>Absent less often:</b> Minimizing costly disruptions from sickness.</li>
                    <li><b>Low labor turnover:</b> Retaining key talent and saving recruitment fees.</li>
                </ul>
                <p style="margin: 10px 0 0 0; font-size: 14px; color: #14532d; font-weight: bold;">➔ Increases efficiency and output, leading directly to higher profits.</p>
            </div>
        </div>
    </div>

    <!-- 2. MOTIVATION THEORIES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-theories" class="lecture-interactive-card" data-lecture-section="sec_theories" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🧠 2. MOTIVATION THEORIES</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Management researchers have developed key theoretical models explaining human behavior in organizations: <b>F.W. Taylor</b> (Scientific Management), <b>Abraham Maslow</b> (Hierarchy of Needs), and <b>Frederick Herzberg</b> (Two-Factor Theory).
            </p>
        </div>

        <!-- TAYLOR -->
        <div id="card-taylor" class="lecture-interactive-card" data-lecture-section="card_taylor" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="margin: 0 0 12px 0; color: #6d28d9; font-size: 19px;">👨‍💼 F. W. Taylor (Scientific Management)</h3>
            <p style="margin: 0 0 12px 0; font-size: 14.5px; color: #475569;">
                Taylor assumed that <b><span style="color: #be185d;">workers are motivated purely by personal financial gain (money)</span></b> and that increasing pay directly increases productivity.
            </p>
            <ul style="margin: 0 0 14px 0; padding-left: 20px; color: #475569; font-size: 14px; line-height: 1.6;">
                <li>Proposed the <b>Piece-rate system</b>: Workers get paid per unit of output produced.</li>
                <li>Suggested <b>scientific management</b>: Breaking down labour (division of labour) to maximize speed and efficiency.</li>
            </ul>
            <div style="background: #fef2f2; padding: 12px 14px; border-radius: 6px; border-left: 4px solid #ef4444; font-size: 13.5px; color: #991b1b;">
                <b>⚠️ Limitations:</b> Modern workers seek non-financial rewards. Piece-rate is impractical in services and can cause rushed work with defective quality.
            </div>
        </div>

        <!-- MASLOW -->
        <div id="card-maslow" class="lecture-interactive-card" data-lecture-section="card_maslow" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="margin: 0 0 12px 0; color: #6d28d9; font-size: 19px;">🔺 Abraham Maslow’s Hierarchy of Needs</h3>
            <p style="margin: 0 0 16px 0; font-size: 14.5px; color: #475569;">
                Employees are motivated by <b><span style="color: #be185d;">ascending tiers of needs</span></b>. Once a lower level is met, it ceases to motivate and the individual seeks to fulfil the next:
            </p>
            <div style="text-align: center; margin-bottom: 16px;">
                <svg viewBox="0 0 500 350" width="100%" style="max-width: 500px; background:#ffffff; border-radius:8px; border:1px solid #cbd5e1; font-family: Arial, sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: block; margin: 0 auto;">
                    <polygon points="90,260 50,320 450,320 410,260" fill="#ef4444" stroke="#ffffff" stroke-width="4"></polygon>
                    <text x="250" y="290" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Physiological Needs</text>
                    <text x="250" y="310" text-anchor="middle" font-size="13" fill="#fee2e2">Food, Water, Shelter, Rest</text>

                    <polygon points="130,200 90,260 410,260 370,200" fill="#f59e0b" stroke="#ffffff" stroke-width="4"></polygon>
                    <text x="250" y="230" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Safety Needs</text>
                    <text x="250" y="250" text-anchor="middle" font-size="13" fill="#fef3c7">Security, Safety, Employment</text>

                    <polygon points="170,140 130,200 370,200 330,140" fill="#10b981" stroke="#ffffff" stroke-width="4"></polygon>
                    <text x="250" y="170" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Social Needs</text>
                    <text x="250" y="190" text-anchor="middle" font-size="13" fill="#d1fae5">Friends, Family, Belonging</text>

                    <polygon points="210,80 170,140 330,140 290,80" fill="#3b82f6" stroke="#ffffff" stroke-width="4"></polygon>
                    <text x="250" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#ffffff">Esteem Needs</text>
                    <text x="250" y="130" text-anchor="middle" font-size="13" fill="#dbeafe">Prestige, Accomplishment</text>

                    <polygon points="250,20 210,80 290,80" fill="#8b5cf6" stroke="#ffffff" stroke-width="4"></polygon>
                    <text x="250" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">Self-</text>
                    <text x="250" y="72" text-anchor="middle" font-size="14" font-weight="bold" fill="#ffffff">actualization</text>
                </svg>
            </div>
            <div style="background: #fef2f2; padding: 12px 14px; border-radius: 6px; border-left: 4px solid #ef4444; font-size: 13.5px; color: #991b1b;">
                <b>⚠️ Limitations:</b> Does not apply uniformly. Some employees skip stages or prioritise recognition over social interaction.
            </div>
        </div>

        <!-- HERZBERG -->
        <div id="card-herzberg" class="lecture-interactive-card" data-lecture-section="card_herzberg" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="margin: 0 0 12px 0; color: #6d28d9; font-size: 19px;">⚖️ Frederick Herzberg’s Two-Factor Theory</h3>
            <p style="margin: 0 0 16px 0; font-size: 14.5px; color: #475569;">Herzberg distinguishes between factors that prevent dissatisfaction and those that create true motivation:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 16px;">
                <div style="flex: 1; min-width: 250px; background: #fffbeb; border: 1px solid #fde68a; padding: 18px; border-radius: 8px;">
                    <h4 style="margin: 0 0 8px 0; color: #d97706; font-size: 16px;">🧹 Hygiene Factors (Prevent Dissatisfaction)</h4>
                    <p style="margin: 0 0 8px 0; font-size: 13px; color: #92400e; font-style: italic;">Must be satisfied to avoid grievance, but do not generate positive motivation on their own:</p>
                    <ul style="margin: 0; padding-left: 20px; color: #92400e; font-size: 13.5px; line-height: 1.6;">
                        <li>Status &amp; Job Security</li>
                        <li>Safe working conditions</li>
                        <li>Company policies &amp; administration</li>
                        <li>Relationship with superiors &amp; peers</li>
                        <li>Basic salary</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 18px; border-radius: 8px;">
                    <h4 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px;">🔥 Motivators (Psychological Growth)</h4>
                    <p style="margin: 0 0 8px 0; font-size: 13px; color: #166534; font-style: italic;">Provide deep intrinsic satisfaction and inspire workers to achieve superior performance:</p>
                    <ul style="margin: 0; padding-left: 20px; color: #166534; font-size: 13.5px; line-height: 1.6;">
                        <li>Achievement</li>
                        <li>Recognition from management</li>
                        <li>Personal growth &amp; development</li>
                        <li>Promotion opportunities</li>
                        <li>Challenging and meaningful work itself</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. FINANCIAL MOTIVATORS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-financial" class="lecture-interactive-card" data-lecture-section="sec_financial" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💰 3. FINANCIAL MOTIVATORS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Financial motivators utilize direct monetary compensation to reward employee effort, output, and organizational contribution.
            </p>
        </div>

        <div id="card-wages-salaries" class="lecture-interactive-card" data-lecture-section="card_wages_salaries" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; margin-bottom: 18px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 12px;">💵 Basic Remuneration: Wages and Salaries</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669; font-size: 15px;">⏱️ Time-Rate (Wages)</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">Pay based on <b>number of hours worked</b>. Offers financial certainty, but does not reward individual extra productivity.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669; font-size: 15px;">📦 Piece-Rate (Wages)</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">Pay based on <b>number of units produced</b>. Drives volume, but risks high defect rates as workers rush.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669; font-size: 15px;">📅 Salary</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;">A fixed monthly or annual amount, typical for administrative, professional, and management roles.</p>
                </div>
            </div>
        </div>

        <div id="card-incentive-pay" class="lecture-interactive-card" data-lecture-section="card_incentive_pay" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 12px;">🎁 Additional Financial Incentives</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669;">🤝 Commission:</b> Paid as a percentage of sales revenue generated; motivates sales reps but causes income instability.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669;">🎁 Bonus:</b> Additional lump-sum reward for hitting special seasonal or project targets.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669;">📊 Performance-Related Pay:</b> Linked directly to formal annual staff appraisal ratings.
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #059669;">📈 Profit Sharing &amp; Shares:</b> Distributing company profits or equity to align staff with shareholders.
                </div>
            </div>
        </div>
    </div>

    <!-- 4. NON-FINANCIAL MOTIVATORS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-non-financial" class="lecture-interactive-card" data-lecture-section="sec_non_financial" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">✨ 4. NON-FINANCIAL MOTIVATORS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Non-financial methods provide intrinsic satisfaction and psychological fulfillment beyond monetary compensation.
            </p>
        </div>

        <div id="card-fringe-benefits" class="lecture-interactive-card" data-lecture-section="card_fringe_benefits" style="background: #fdf2f8; border: 1.5px solid #fbcfe8; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #be185d; font-size: 18px; margin-top: 0; margin-bottom: 10px;">🎁 Fringe Benefits ("Perks")</h3>
            <p style="margin: 0 0 12px 0; font-size: 14px; color: #831843;">Non-cash benefits given to employees to elevate status and ease living costs:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <span style="background: #ffffff; color: #9d174d; padding: 6px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #fbcfe8; font-weight: 600;">🚗 Company vehicle</span>
                <span style="background: #ffffff; color: #9d174d; padding: 6px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #fbcfe8; font-weight: 600;">🏥 Health insurance</span>
                <span style="background: #ffffff; color: #9d174d; padding: 6px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #fbcfe8; font-weight: 600;">🎓 Education subsidies</span>
                <span style="background: #ffffff; color: #9d174d; padding: 6px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #fbcfe8; font-weight: 600;">🏠 Free housing</span>
                <span style="background: #ffffff; color: #9d174d; padding: 6px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #fbcfe8; font-weight: 600;">✈️ Holiday vouchers</span>
                <span style="background: #ffffff; color: #9d174d; padding: 6px 14px; border-radius: 20px; font-size: 13px; border: 1px solid #fbcfe8; font-weight: 600;">🏷️ Staff merchandise discounts</span>
            </div>
        </div>

        <div id="card-job-satisfaction" class="lecture-interactive-card" data-lecture-section="card_job_satisfaction" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 12px;">🌟 Job Redesign Methods for Employee Satisfaction</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border-left: 4px solid #3b82f6; padding: 14px; border-radius: 6px; border: 1px solid #e2e8f0;">
                    <b style="color: #1d4ed8; font-size: 15px;">🔄 Job Rotation</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Swapping tasks periodically to alleviate monotony and cross-train staff.</p>
                </div>
                <div style="background: #f8fafc; border-left: 4px solid #8b5cf6; padding: 14px; border-radius: 6px; border: 1px solid #e2e8f0;">
                    <b style="color: #6d28d9; font-size: 15px;">➕ Job Enlargement</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Adding extra tasks of a similar level to introduce variety without extra pressure.</p>
                </div>
                <div style="background: #f8fafc; border-left: 4px solid #ec4899; padding: 14px; border-radius: 6px; border: 1px solid #e2e8f0;">
                    <b style="color: #be185d; font-size: 15px;">⭐ Job Enrichment</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Delegating higher responsibility and decision-making power, demonstrating trust.</p>
                </div>
                <div style="background: #f8fafc; border-left: 4px solid #10b981; padding: 14px; border-radius: 6px; border: 1px solid #e2e8f0;">
                    <b style="color: #047857; font-size: 15px;">🤝 Team-Working</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Empowering self-managed teams to organize their own workflow, fulfilling social needs.</p>
                </div>
                <div style="background: #f8fafc; border-left: 4px solid #f59e0b; padding: 14px; border-radius: 6px; border: 1px solid #e2e8f0;">
                    <b style="color: #b45309; font-size: 15px;">📈 Training &amp; Promotion</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Providing career development paths, enabling employees to fulfill self-actualization.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. RECOMMEND AND JUSTIFY (CAMBRIDGE EXAM STRATEGY) -->
    <div id="sec-recommend-motivation" class="lecture-interactive-card" data-lecture-section="sec_recommend_motivation" style="margin-bottom: 45px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
        <h2 style="color: #1e3a8a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; font-size: 22px; margin-top: 0; display: inline-block;">
            🎯 5. HOW TO RECOMMEND &amp; JUSTIFY MOTIVATION METHODS (Cambridge Exam Strategy)
        </h2>
        <p style="font-size: 15px; color: #1e40af; margin-bottom: 18px; line-height: 1.6;">
            Cambridge Paper 1 &amp; Paper 2 scenarios ask candidates to recommend and justify motivational schemes based on job context:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 16px;">
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #1e40af; font-size: 15px;">🏭 Factory / Assembly Workers:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Recommend <b>Piece-rate</b> combined with a <b>quality bonus</b> and <b>job rotation</b> to prevent monotonous repetitive strain.
                </p>
            </div>
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #047857; font-size: 15px;">💼 Sales Personnel:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Recommend <b>Base Salary + Commission</b> to balance financial stability with strong incentives to maximize sales volume.
                </p>
            </div>
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #f59e0b; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #b45309; font-size: 15px;">💻 Skilled Professionals:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Recommend <b>Job enrichment</b>, autonomous decision-making, and <b>profit sharing</b> to engage creative talent.
                </p>
            </div>
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #ec4899; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #be185d; font-size: 15px;">🛒 Retail / Hourly Staff:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Recommend <b>Fair hourly wage above minimum wage</b>, guaranteed hours, and merchandise discounts (satisfying basic Maslow needs).
                </p>
            </div>
        </div>
        <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
            <b style="color: #1e40af; font-size: 14.5px;">💡 Cambridge Evaluation Formula:</b>
            <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #334155; line-height: 1.5;">
                State the recommendation ➔ Explain 2 distinct benefits to the business ➔ Address 1 limitation (cost or quality) with a countermeasure ➔ Conclude why it outmatches alternatives.
            </p>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.1 Motivating Employees (Động lực làm việc của nhân viên)</h1>
        </div>
    </div>"""
    # Insert banner right after the opening container div
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 2.1 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/2_1_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 2.1 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
