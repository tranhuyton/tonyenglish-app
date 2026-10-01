import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 2.3 ID
LID = 'c2d359f6-1921-459e-a295-def7e891c352'
CODE = '2_3'
TITLE = '2.3. Recruitment, selection and training of employees'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 14 AUDIO SEGMENTS FOR LESSON 2.3
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 2.3: Tuyển dụng, Chọn lọc và Đào tạo nhân viên",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 2.3: Recruitment, Selection and Training of Employees. In this lesson, we study the human resources department lifecycle: identifying vacancies, writing job descriptions and person specifications, internal versus external recruitment, selection methods, induction, on-the-job and off-the-job training, workforce downsizing, and employment legislation.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 2.3: Tuyển dụng, Chọn lọc và Đào tạo nhân viên. Trong bài học này, chúng ta sẽ tìm hiểu toàn diện quy trình nhân sự: xác định vị trí trống, xây dựng bản mô tả và tiêu chuẩn công việc, tuyển dụng nội bộ và bên ngoài, các phương pháp phỏng vấn, đào tạo hội nhập, tại chỗ và ngoài chỗ làm, tinh giản nhân sự cùng luật lao động."
    },
    {
        "id": "sec_hr_role",
        "title": "1. Vai trò của Bộ phận Quản trị Nhân sự",
        "selector": "#sec-hr-role",
        "en": "Section 1 defines the strategic role of Human Resources. The HR team forecasts workforce requirements, plans recruitment campaigns, designs remuneration packages, oversees health and safety compliance, administers disciplinary procedures, and mediates industrial relations.",
        "vi": "Mục một xác định vai trò chiến lược của Bộ phận Nhân sự. Đội ngũ nhân sự chịu trách nhiệm dự báo nhu cầu nhân lực, lên kế hoạch tuyển dụng, thiết kế chế độ lương thưởng, giám sát an toàn lao động, giải quyết kỷ luật và hòa giải quan hệ lao động trong doanh nghiệp."
    },
    {
        "id": "sec_recruitment",
        "title": "2. Quy trình Tuyển dụng và Các Tài liệu Cốt lõi",
        "selector": "#sec-recruitment",
        "en": "Section 2 defines recruitment as the complete process from identifying that a vacancy exists to receiving candidates' applications. Crucial preliminary steps include job analysis to evaluate duties, job descriptions detailing tasks and working conditions, and person specifications establishing required qualifications and experience.",
        "vi": "Mục hai định nghĩa tuyển dụng là toàn bộ quy trình từ khi phát hiện vị trí công việc bị khuyết cho đến khi tiếp nhận hồ sơ ứng tuyển. Các bước chuẩn bị cốt lõi gồm phân tích công việc nhằm xác định rõ nhiệm vụ, bản mô tả công việc liệt kê chi tiết trách nhiệm và điều kiện làm việc, và bản tiêu chuẩn ứng viên nêu rõ bằng cấp và kinh nghiệm cần có."
    },
    {
        "id": "card_job_analysis",
        "title": "🔍 Phân tích Công việc, Bản Mô tả & Bản Tiêu chuẩn Ứng viên",
        "selector": "#card-job-analysis",
        "en": "Job Analysis surveys the tasks involved in a vacant post. The Job Description outlines the role's responsibilities, reporting hierarchy, salary, and hours to prospective candidates. The Job Specification outlines the required personal qualifications, skills, and experience needed to shortlist candidates effectively.",
        "vi": "Phân tích công việc (Job Analysis) khảo sát cụ thể các nhiệm vụ của vị trí trống. Bản mô tả công việc (Job Description) nêu rõ trách nhiệm, hệ thống báo cáo, mức lương và thời gian làm việc cho ứng viên. Bản tiêu chuẩn ứng viên (Job Specification) quy định bằng cấp chuyên môn, kỹ năng và kinh nghiệm cần thiết để sàng lọc hồ sơ ứng viên."
    },
    {
        "id": "card_internal_external",
        "title": "🏢 Tuyển dụng Nội bộ đối chiếu Tuyển dụng Bên ngoài",
        "selector": "#card-internal-external",
        "en": "Internal recruitment promotes existing employees, saving advertising costs and motivating workers, but limits fresh perspective. External recruitment utilizes job centres, newspapers, and agencies to inject new talent and specialist skills, although it incurs significant recruitment expenditures and longer induction periods.",
        "vi": "Tuyển dụng nội bộ cất nhắc nhân viên hiện hữu, giúp tiết kiệm chi phí đăng tin và khích lệ tinh thần làm việc, nhưng giới hạn các ý tưởng đột phá mới. Tuyển dụng bên ngoài sử dụng trung tâm việc làm, báo chí và công ty săn đầu người để mang lại nhân tài mới cùng kỹ năng chuyên sâu, dù tốn kém chi phí tuyển dụng và mất thời gian hội nhập lâu hơn."
    },
    {
        "id": "sec_selection",
        "title": "3. Phương pháp Chọn lọc và Hợp đồng Lao động",
        "selector": "#sec-selection",
        "en": "Section 3 covers selection instruments and the employment agreement. Selection assesses applicant aptitude, emotional intelligence, and team dynamics through structured interviews, psychometric profiling, and practical skills testing to select the best match.",
        "vi": "Mục ba trình bày các công cụ chọn lọc và thỏa thuận lao động. Quá trình chọn lọc đánh giá năng lực, chỉ số cảm xúc và sự hòa nhập đội ngũ của ứng viên qua phỏng vấn có cấu trúc, trắc nghiệm tâm lý và kiểm tra tay nghề thực tế nhằm tìm ra người phù hợp nhất."
    },
    {
        "id": "card_selection_tests",
        "title": "🎯 Phỏng vấn & Bốn loại Bài kiểm tra Tuyển dụng",
        "selector": "#card-selection-tests",
        "en": "Selection employs four primary tests alongside interviews: Skills tests assessing technical competence; Aptitude tests evaluating capacity to learn new processes; Personality tests assessing temperament and cultural fit; and Group situation tests observing teamwork, communication, and leadership under pressure.",
        "vi": "Quy trình chọn lọc sử dụng bốn bài kiểm tra then chốt bên cạnh phỏng vấn: Kiểm tra kỹ năng (Skills tests) đánh giá tay nghề nghiệp vụ; Kiểm tra năng khiếu (Aptitude tests) đo lường khả năng tiếp thu công nghệ mới; Trắc nghiệm tính cách (Personality tests) xem xét mức độ phù hợp văn hóa doanh nghiệp; và Bài kiểm tra tình huống nhóm (Group tests) quan sát tinh thần đồng đội và tố chất lãnh đạo."
    },
    {
        "id": "card_employment_contract",
        "title": "📝 Hợp đồng Lao động (The Contract of Employment)",
        "selector": "#card-employment-contract",
        "en": "The Contract of Employment is a legally enforceable agreement establishing mutual commitments between employer and employee. It mandates job title, employment commencement date, exact wage rates, hours of work, holiday entitlement, disciplinary codes, and statutory notice periods for termination.",
        "vi": "Hợp đồng lao động (Contract of Employment) là thỏa thuận pháp lý mang tính ràng buộc thiết lập nghĩa vụ song phương giữa người sử dụng lao động và người lao động. Hợp đồng quy định rõ chức danh, ngày bắt đầu công việc, mức tiền lương, số giờ làm việc, chế độ nghỉ phép, quy tắc kỷ luật và thời hạn thông báo trước khi chấm dứt hợp đồng."
    },
    {
        "id": "sec_training",
        "title": "4. Các Hình thức Đào tạo Nhân sự",
        "selector": "#sec-training",
        "en": "Section 4 evaluates the three forms of employee training: Induction training introduces workplace rules and colleagues; On-the-job training involves hands-on mentoring at the workstation; and Off-the-job training provides structured education at external vocational colleges.",
        "vi": "Mục bốn đánh giá ba hình thức đào tạo nhân viên: Đào tạo hội nhập (Induction) phổ biến nội quy và giới thiệu đồng nghiệp; Đào tạo tại chỗ (On-the-job) kèm cặp thực hành trực tiếp tại bàn làm việc; và Đào tạo ngoài chỗ làm (Off-the-job) cung cấp chương trình đào tạo chuyên sâu tại các trường đào tạo nghề uy tín."
    },
    {
        "id": "card_training_types",
        "title": "🎓 So sánh: Đào tạo Hội nhập, Tại chỗ (On-the-job) & Ngoài chỗ làm (Off-the-job)",
        "selector": "#card-training-types",
        "en": "On-the-job training is cost effective and maintains continuous production, but risks passing on senior workers' bad habits. Off-the-job training delivers expert cutting-edge instruction without damaging workplace output, but incurs expensive course tuition and risks trained employees being poached by competitors.",
        "vi": "Đào tạo tại chỗ tiết kiệm chi phí và duy trì sản xuất liên tục, nhưng dễ lây nhiễm các thói quen xấu của người đi trước. Đào tạo ngoài chỗ làm mang lại kỹ năng chuyên gia tiên tiến mà không làm hỏng sản phẩm của khách hàng, nhưng phát sinh học phí đắt đỏ và tiềm ẩn rủi ro nhân viên sau khi học xong bị đối thủ săn đón mất."
    },
    {
        "id": "sec_part_full_time",
        "title": "⏰ 5. Nhân viên Bán thời gian vs Toàn thời gian",
        "selector": "#sec-part-full-time",
        "en": "Section 5 contrasts part-time flexibility against full-time workforce stability. Part-time staff enable businesses to adjust staffing around peak customer hours and trim wage bills, but may show lower organizational commitment and suffer higher communication fragmentation across shifting rosters.",
        "vi": "Mục năm đối chiếu sự linh hoạt của nhân viên bán thời gian với sự ổn định của lực lượng toàn thời gian. Nhân viên bán thời gian giúp doanh nghiệp dễ dàng điều chỉnh nhân sự theo các khung giờ cao điểm và giảm thiểu quỹ lương chết, nhưng có thể có mức độ gắn kết thấp hơn và gây khó khăn cho việc giao tiếp đồng bộ giữa các ca kíp."
    },
    {
        "id": "sec_downsizing",
        "title": "📉 6. Tinh giản Nhân sự: Sa thải (Dismissal) vs Cắt giảm Dôi dư (Redundancy)",
        "selector": "#sec-downsizing",
        "en": "Section 6 explains workforce downsizing. Dismissal terminates an employee due to poor performance, persistent absence, or gross misconduct, with the job vacancy remaining open. Redundancy eliminates the post entirely due to restructuring, falling demand, or automation, entitling workers to statutory severance packages.",
        "vi": "Mục sáu phân tích quá trình tinh giản nhân sự. Sa thải (Dismissal) chấm dứt hợp đồng do nhân viên yếu kém năng lực, thường xuyên vắng mặt hoặc vi phạm kỷ luật nghiêm trọng, trong khi vị trí công việc đó vẫn tiếp tục tuyển người mới thay thế. Cắt giảm dôi dư (Redundancy) xóa bỏ hoàn toàn vị trí công việc do tái cơ cấu, sụt giảm thị trường hoặc tự động hóa, và nhân viên được nhận bồi thường dôi dư theo luật."
    },
    {
        "id": "sec_legal_controls",
        "title": "⚖️ 7. Khung Pháp lý Điều chỉnh Quan hệ Lao động",
        "selector": "#sec-legal-controls",
        "en": "Section 7 reviews employment laws: written employment contracts, statutory minimum wages to avoid exploitation, anti-discrimination laws protecting gender, race, age, and disability, workplace health and safety mandates, and protection against unfair dismissal.",
        "vi": "Mục bảy tổng hợp các quy định pháp luật lao động: hợp đồng lao động bằng văn bản, mức lương tối thiểu vùng ngăn ngừa bóc lột, luật chống phân biệt đối xử bảo vệ bình đẳng giới, sắc tộc, tuổi tác và người khuyết tật, tiêu chuẩn an toàn vệ sinh lao động và quy định chống sa thải bất công."
    },
    {
        "id": "sec_recommend_recruitment",
        "title": "🎯 8. Chiến lược làm bài thi Cambridge: Đề xuất Phương án Tuyển chọn Nhân sự",
        "selector": "#sec-recommend-recruitment",
        "en": "Section 8 provides the Cambridge 4-step recruitment evaluation strategy. Candidates must diagnose the company's precise operating crisis, match 2 candidate strengths to strategic needs, address the chosen applicant's key drawback with a mitigating action, and reject rival candidates using clear contextual reasoning.",
        "vi": "Mục tám cung cấp chiến thuật 4 bước giải quyết bài thi chọn lọc nhân sự của Cambridge. Thí sinh phải nắm bắt chính xác nhu cầu cốt lõi của doanh nghiệp, ghép 2 thế mạnh nổi bật của ứng viên vào yêu cầu công việc, đưa ra giải pháp khắc phục điểm yếu của ứng viên đó và giải thích lý do từ chối các ứng viên còn lại dựa trên bối cảnh thực tế."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_hr_role": {"start": 1, "end": 1},
    "sec_recruitment": {"start": 2, "end": 4},
    "sec_selection": {"start": 5, "end": 7},
    "sec_training": {"start": 8, "end": 9},
    "sec_part_full_time": {"start": 10, "end": 10},
    "sec_downsizing": {"start": 11, "end": 11},
    "sec_legal_controls": {"start": 12, "end": 12},
    "sec_recommend_recruitment": {"start": 13, "end": 13}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.3 Recruitment, Selection and Training of Employees (Tuyển dụng, Chọn lọc &amp; Đào tạo)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. THE ROLE OF THE H.R. DEPARTMENT -->
    <div id="sec-hr-role" class="lecture-interactive-card" data-lecture-section="sec_hr_role" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏢 1. THE ROLE OF THE H.R. DEPARTMENT</h2>
        <p style="font-size: 15px; color: #475569; margin: 0 0 16px 0; line-height: 1.6;">The Human Resource department is responsible for managing people throughout their employment lifecycle:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                <b style="color: #2563eb; font-size: 15px;">🎯 Recruitment &amp; Selection</b>
                <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Attracting and evaluating candidates to fill organizational vacancies.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                <b style="color: #2563eb; font-size: 15px;">💰 Wages &amp; Salaries</b>
                <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Designing fair compensation packages to attract, retain, and motivate talent.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                <b style="color: #2563eb; font-size: 15px;">🤝 Industrial Relations</b>
                <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Handling employee grievances and mediating with trade union representatives.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                <b style="color: #2563eb; font-size: 15px;">📈 Training Programmes</b>
                <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Upgrading workforce technical skills to maximize productivity and safety.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                <b style="color: #2563eb; font-size: 15px;">🛡️ Health &amp; Safety</b>
                <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Ensuring strict workplace legal compliance to protect worker welfare.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                <b style="color: #2563eb; font-size: 15px;">👋 Redundancy &amp; Dismissal</b>
                <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Administering fair disciplinary dismissals and statutory redundancy schemes.</p>
            </div>
        </div>
    </div>

    <!-- 2. RECRUITMENT -->
    <div style="margin-bottom: 45px;">
        <div id="sec-recruitment" class="lecture-interactive-card" data-lecture-section="sec_recruitment" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📄 2. RECRUITMENT</h2>
            <div style="background: #f0fdf4; border-left: 5px solid #10b981; padding: 14px 18px; border-radius: 8px; font-size: 15px; color: #065f46; line-height: 1.6;">
                <b>Recruitment</b> is the process from identifying that the business needs to employ someone up to the point where applications have arrived at the business.
            </div>
        </div>

        <div id="card-job-analysis" class="lecture-interactive-card" data-lecture-section="card_job_analysis" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🔍 Job Analysis, Description &amp; Specification</h3>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="background: #fffbeb; border: 1px solid #fde68a; border-left: 5px solid #f59e0b; padding: 14px 18px; border-radius: 8px;">
                    <b style="color: #d97706; font-size: 15px;">1. Job Analysis:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Surveys and records all the actual tasks and responsibilities of the vacant role.</p>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-left: 5px solid #3b82f6; padding: 14px 18px; border-radius: 8px;">
                    <b style="color: #2563eb; font-size: 15px;">2. Job Description:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Outlines duties, reporting lines, pay scale, and working hours for applicants.</p>
                </div>
                <div style="background: #faf5ff; border: 1px solid #e9d5ff; border-left: 5px solid #8b5cf6; padding: 14px 18px; border-radius: 8px;">
                    <b style="color: #7c3aed; font-size: 15px;">3. Job Specification:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;">Specifies necessary qualifications, skills, experience, and personal attributes needed.</p>
                </div>
            </div>
        </div>

        <div id="card-internal-external" class="lecture-interactive-card" data-lecture-section="card_internal_external" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">📢 Internal vs External Recruitment</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🏢 Internal Recruitment (Promote from within)</b>
                    <div style="margin-top: 8px; font-size: 13px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Cheaper, faster; known work ethic; motivates existing staff.<br/>
                        <b style="color: #dc2626;">❌ Cons:</b> No new ideas/skills; creates another vacancy; potential workplace jealousy.
                    </div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🌐 External Recruitment (New candidates)</b>
                    <div style="margin-top: 8px; font-size: 13px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Injects fresh perspectives and cutting-edge specialized skills.<br/>
                        <b style="color: #dc2626;">❌ Cons:</b> Expensive adverts/agency fees; longer induction; candidate personality unknown.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. SELECTION & THE CONTRACT -->
    <div style="margin-bottom: 45px;">
        <div id="sec-selection" class="lecture-interactive-card" data-lecture-section="sec_selection" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">✅ 3. SELECTION &amp; THE CONTRACT</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Selection screens shortlisted applicants to choose the optimal candidate, followed by formalizing a legal contract.
            </p>
        </div>

        <div id="card-selection-tests" class="lecture-interactive-card" data-lecture-section="card_selection_tests" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #6d28d9; font-size: 18px; margin-top: 0; margin-bottom: 12px;">🎯 Selection Methods &amp; 4 Types of Tests</h3>
            <p style="font-size: 14px; color: #475569; margin-bottom: 14px;">Interviews and references assess character, supported by specialized testing:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
                <div style="background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 14px;">Skills tests:</b> Measures actual practical ability to perform specific tasks.
                </div>
                <div style="background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 14px;">Aptitude tests:</b> Evaluates potential capacity to acquire new competencies.
                </div>
                <div style="background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 14px;">Personality tests:</b> Assesses temperament, stress handling, and cultural fit.
                </div>
                <div style="background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 8px; padding: 12px;">
                    <b style="color: #6b21a8; font-size: 14px;">Group tests:</b> Observes interpersonal teamwork, communication, and leadership.
                </div>
            </div>
        </div>

        <div id="card-employment-contract" class="lecture-interactive-card" data-lecture-section="card_employment_contract" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 12px;">📝 The Contract of Employment</h3>
            <p style="margin: 0 0 10px 0; font-size: 14px; color: #475569;">A legal agreement outlining employee and employer rights. Key contents include:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 13px; border: 1px solid #cbd5e1;">📄 Job title &amp; Start date</span>
                <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 13px; border: 1px solid #cbd5e1;">⏱️ Working hours &amp; Overtime</span>
                <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 13px; border: 1px solid #cbd5e1;">💵 Pay rate &amp; Frequency</span>
                <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 13px; border: 1px solid #cbd5e1;">🏖️ Paid holiday entitlement</span>
                <span style="background: #f1f5f9; padding: 6px 12px; border-radius: 6px; font-size: 13px; border: 1px solid #cbd5e1;">📢 Termination notice period</span>
            </div>
        </div>
    </div>

    <!-- 4. TRAINING -->
    <div style="margin-bottom: 45px;">
        <div id="sec-training" class="lecture-interactive-card" data-lecture-section="sec_training" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🎓 4. EMPLOYEE TRAINING</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Training elevates worker competence, reduces operational mistakes, improves morale, and prepares employees for advancement.
            </p>
        </div>

        <div id="card-training-types" class="lecture-interactive-card" data-lecture-section="card_training_types" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #d97706; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🎓 Three Training Methods: Induction, On-the-job &amp; Off-the-job</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 14px;">
                    <b style="color: #b45309; font-size: 15px;">👋 Induction Training:</b>
                    <p style="margin: 4px 0 6px 0; font-size: 13px; color: #475569;">Introduces new employees to company facilities, customs, safety, and colleagues.</p>
                    <div style="font-size: 12.5px;"><b style="color: #16a34a;">Pros:</b> Settles quickly, prevents early blunders. <b style="color: #dc2626;">Cons:</b> Wages paid while non-productive.</div>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 14px;">
                    <b style="color: #15803d; font-size: 15px;">👀 On-the-job Training:</b>
                    <p style="margin: 4px 0 6px 0; font-size: 13px; color: #475569;">Mentoring by an experienced colleague at the workstation.</p>
                    <div style="font-size: 12.5px;"><b style="color: #16a34a;">Pros:</b> Inexpensive, maintains production output. <b style="color: #dc2626;">Cons:</b> Bad habits passed on; trainer slowed down.</div>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px;">
                    <b style="color: #1d4ed8; font-size: 15px;">🏫 Off-the-job Training:</b>
                    <p style="margin: 4px 0 6px 0; font-size: 13px; color: #475569;">Conducted away from work at vocational colleges or simulation centres.</p>
                    <div style="font-size: 12.5px;"><b style="color: #16a34a;">Pros:</b> Expert tuition, latest techniques. <b style="color: #dc2626;">Cons:</b> High course fees; trained staff may be poached.</div>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. PART-TIME VS FULL-TIME -->
    <div id="sec-part-full-time" class="lecture-interactive-card" data-lecture-section="sec_part_full_time" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⏰ 5. PART-TIME VS FULL-TIME EMPLOYEES</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #6d28d9; font-size: 15px;">🕐 Advantages of Part-time Employees:</b>
                <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13.5px; color: #334155; line-height: 1.5;">
                    <li>High scheduling flexibility during customer peak hours.</li>
                    <li>Lowers total wage expenses by avoiding idle paid hours.</li>
                    <li>Attracts diverse talent pools (parents, students, retirees).</li>
                </ul>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #b91c1c; font-size: 15px;">⚠️ Limitations of Part-time Employees:</b>
                <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13.5px; color: #334155; line-height: 1.5;">
                    <li>Lower organizational commitment and higher turnover.</li>
                    <li>Communication coordination difficulties across varied shifts.</li>
                    <li>Higher induction and training cost per productive hour worked.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 6. DOWNSIZING -->
    <div id="sec-downsizing" class="lecture-interactive-card" data-lecture-section="sec_downsizing" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📉 6. DOWNSIZING: DISMISSAL VS REDUNDANCY</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 16px;">
            <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 16px;">
                <b style="color: #b91c1c; font-size: 15.5px;">🚫 Dismissal (Sa Thải)</b>
                <p style="margin: 6px 0 8px 0; font-size: 13.5px; color: #7f1d1d;">Caused by worker fault (incompetence, gross misconduct). <b>The job post remains open</b> and a replacement is hired.</p>
            </div>
            <div style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 16px;">
                <b style="color: #c2410c; font-size: 15.5px;">📦 Redundancy (Dôi Dư Nhân Sự)</b>
                <p style="margin: 6px 0 8px 0; font-size: 13.5px; color: #9a3412;">Caused by business restructuring, falling demand, or automation. <b>The job post is eliminated</b>; worker gets compensation.</p>
            </div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px;">
            <b style="color: #0f172a; font-size: 14.5px;">Criteria for Redundancy Selection:</b>
            <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #475569;"><b>LIFO (Last In, First Out)</b> preserves long-term loyalty; Performance/Productivity retains top talent; Disciplinary records prioritize poor attendees.</p>
        </div>
    </div>

    <!-- 7. LEGAL CONTROLS -->
    <div id="sec-legal-controls" class="lecture-interactive-card" data-lecture-section="sec_legal_controls" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 7. LEGAL CONTROLS OVER EMPLOYMENT ISSUES</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                <b style="color: #0f766e; font-size: 14px;">1. Employment Contracts:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Legally binding terms on wages, hours, and notice periods.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                <b style="color: #0f766e; font-size: 14px;">2. Unfair Dismissal Laws:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Protects staff from dismissal without fair warnings or legitimate cause.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                <b style="color: #0f766e; font-size: 14px;">3. Anti-Discrimination:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Prohibits bias in hiring or pay based on gender, race, age, or disability.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                <b style="color: #0f766e; font-size: 14px;">4. Health &amp; Safety:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Mandates protective gear, fire exits, and safe machines with stiff fines.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                <b style="color: #0f766e; font-size: 14px;">5. Legal Minimum Wage:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Guarantees statutory hourly wage floor to prevent worker exploitation.</p>
            </div>
        </div>
    </div>

    <!-- 8. RECOMMEND AND JUSTIFY (CAMBRIDGE EXAM STRATEGY) -->
    <div id="sec-recommend-recruitment" class="lecture-interactive-card" data-lecture-section="sec_recommend_recruitment" style="margin-bottom: 45px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
        <h2 style="color: #1e3a8a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; font-size: 22px; margin-top: 0; display: inline-block;">
            🎯 8. HOW TO RECOMMEND &amp; JUSTIFY WHO TO EMPLOY (Cambridge Exam Strategy)
        </h2>
        <p style="font-size: 15px; color: #1e40af; margin-bottom: 16px; line-height: 1.6;">
            Paper 2 candidates are presented with candidate profiles and asked to recommend and justify the best applicant:
        </p>
        <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px 20px;">
            <b style="color: #1e40af; font-size: 15px;">💡 Cambridge 4-Step Selection Justification Formula:</b>
            <ol style="margin: 8px 0 0 0; padding-left: 20px; font-size: 13.5px; color: #334155; line-height: 1.6;">
                <li><b>Identify exact business requirements:</b> Cite whether the firm faces tight cash, needs immediate launch, or requires digital modernization.</li>
                <li><b>Match candidate strengths to business needs:</b> Explain how candidate's experience cuts induction time and raises immediate revenue.</li>
                <li><b>Mitigate chosen candidate's main limitation:</b> Address high wage expectation or lack of specific software skills with a clear countermeasure.</li>
                <li><b>Reject rival candidate with context justification:</b> Explain why the competitor's profile fails the firm's immediate operational deadline.</li>
            </ol>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.3 Recruitment, Selection and Training of Employees (Tuyển dụng, Chọn lọc &amp; Đào tạo)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 2.3 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/2_3_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 2.3 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
