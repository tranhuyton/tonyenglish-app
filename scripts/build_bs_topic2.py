import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# LECTURE 2.1: Motivating employees
# ==============================================================================
async def build_2_1():
    lid = 'cd1763a9-f030-4be1-b65b-c6dc6dde91c9'
    code = '2_1'
    title = '2.1. Motivating employees'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-motivation-work" class="lecture-interactive-card" data-lecture-section="sec_motivation_work" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-theories" class="lecture-interactive-card" data-lecture-section="sec_theories" style="cursor: pointer; ')
    
    t_h3_taylor = str(h3s[0])
    r_h3_taylor = t_h3_taylor.replace('<h3', '<h3 id="card-taylor" class="lecture-interactive-card" data-lecture-section="card_taylor" style="cursor: pointer; ')
    
    t_h3_maslow = str(h3s[1])
    r_h3_maslow = t_h3_maslow.replace('<h3', '<h3 id="card-maslow" class="lecture-interactive-card" data-lecture-section="card_maslow" style="cursor: pointer; ')
    
    t_h3_herzberg = str(h3s[2])
    r_h3_herzberg = t_h3_herzberg.replace('<h3', '<h3 id="card-herzberg" class="lecture-interactive-card" data-lecture-section="card_herzberg" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-financial" class="lecture-interactive-card" data-lecture-section="sec_financial" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-non-financial" class="lecture-interactive-card" data-lecture-section="sec_non_financial" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-recommend-motivation" class="lecture-interactive-card" data-lecture-section="sec_recommend_motivation" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_taylor, r_h3_taylor, 1)\
                   .replace(t_h3_maslow, r_h3_maslow, 1)\
                   .replace(t_h3_herzberg, r_h3_herzberg, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

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
            "id": "sec_theories",
            "title": "2. Tổng quan các Học thuyết Động lực",
            "selector": "#sec-theories",
            "en": "Section 2 introduces three foundational motivation frameworks examined in the Cambridge syllabus: F.W. Taylor's Scientific Management, Abraham Maslow's Hierarchy of Needs, and Frederick Herzberg's Two-Factor Theory. Understanding how psychological needs evolve is essential for designing effective workforce rewards.",
            "vi": "Mục hai giới thiệu ba học thuyết động lực nền tảng trong chương trình Cambridge: Quản trị khoa học của F.W. Taylor, Tháp nhu cầu của Abraham Maslow và Thuyết hai yếu tố của Frederick Herzberg. Hiểu rõ sự phát triển nhu cầu tâm lý là cơ sở để thiết kế chính sách đãi ngộ nhân sự hiệu quả."
        },
        {
            "id": "card_taylor",
            "title": "Học thuyết F. W. Taylor: Quản trị theo khoa học",
            "selector": "#card-taylor",
            "en": "F.W. Taylor viewed workers as purely rational economic agents driven by financial gain. His scientific management model breaks down tasks into standard repetitive movements and links compensation directly to output through differential piece-rates. While effective for simple factory production lines, Taylorism ignores social belonging, causes workplace boredom, and neglects intrinsic job satisfaction.",
            "vi": "F.W. Taylor coi người lao động là những cá nhân kinh tế thuần túy hành động vì tiền bạc. Mô hình quản trị khoa học chia nhỏ quy trình thành các thao tác chuẩn mực lặp đi lặp lại và trả lương theo sản phẩm (piece-rate). Dù rất hiệu quả trong các dây chuyền sản xuất đơn giản, học thuyết Taylor bỏ qua nhu cầu xã hội, gây ra sự nhàm chán và xem nhẹ niềm vui công việc nội tại."
        },
        {
            "id": "card_maslow",
            "title": "Tháp Nhu cầu của Abraham Maslow",
            "selector": "#card-maslow",
            "en": "Abraham Maslow proposed that human beings are motivated by five ascending tiers of needs: physiological survival, safety and job security, social belonging and team camaraderie, esteem and recognition, and finally self-actualisation. Once a lower-level need is satisfied, it ceases to motivate, and the individual strives to fulfil the next level.",
            "vi": "Abraham Maslow đưa ra hệ thống phân cấp gồm năm tầng nhu cầu: sinh lý căn bản, an toàn và việc làm ổn định, xã hội và gắn kết đồng đội, được tôn trọng và công nhận, và cuối cùng là hoàn thiện bản thân (self-actualisation). Khi một nhu cầu bậc thấp đã được thỏa mãn, nó không còn là động lực thúc đẩy nữa và con người sẽ hướng lên bậc cao hơn."
        },
        {
            "id": "card_herzberg",
            "title": "Thuyết Hai yếu tố của Frederick Herzberg",
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
            "id": "sec_non_financial",
            "title": "4. Phương pháp tạo Động lực Phi tài chính",
            "selector": "#sec-non-financial",
            "en": "Section 4 investigates non-financial motivators and job redesign. Techniques include job rotation to relieve monotony, job enlargement to broaden variety, and job enrichment to delegate higher-level decision making. Combined with teamworking, flexible working hours, and subsidized fringe benefits, non-financial strategies foster long-term loyalty and deep intrinsic job engagement.",
            "vi": "Mục bốn phân tích các giải pháp phi tài chính và thiết kế lại công việc. Các kỹ thuật bao gồm luân chuyển công việc (job rotation) giảm sự nhàm chán, mở rộng công việc (job enlargement) tăng thêm đầu việc tương đương, và làm giàu công việc (job enrichment) trao thêm quyền tự quyết cao hơn. Kết hợp cùng làm việc nhóm, giờ giấc linh hoạt và phúc lợi phụ cấp, phương pháp phi tài chính giúp xây dựng lòng trung thành bền vững."
        },
        {
            "id": "sec_recommend_motivation",
            "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất phương pháp tạo động lực",
            "selector": "#sec-recommend-motivation",
            "en": "Section 5 details the Cambridge evaluation strategy for motivation questions. Candidates must tailor recommendations to employee types and business context: factory operatives often respond to piece rates and bonuses, whereas creative and professional staff prioritize autonomy and enrichment. Conclude by balancing financial cost against potential productivity gains.",
            "vi": "Mục năm cung cấp chiến lược làm bài thi Cambridge cho các câu hỏi đánh giá tạo động lực. Thí sinh phải gắn giải pháp với từng đối tượng lao động và bối cảnh cụ thể: công nhân sản xuất thường phản ứng tốt với lương sản phẩm và thưởng năng suất, trong khi chuyên gia sáng tạo lại coi trọng sự tự chủ và trao quyền. Luôn kết luận bằng cách cân đối giữa chi phí tài chính và mức tăng năng suất dự kiến."
        }
    ]
    
    major_sections = [
        {"id": "sec_motivation_work", "title": "1. Vai trò của Động lực lao động"},
        {"id": "sec_theories", "title": "2. Các Học thuyết Động lực (Taylor, Maslow, Herzberg)"},
        {"id": "sec_financial", "title": "3. Đãi ngộ Tài chính"},
        {"id": "sec_non_financial", "title": "4. Đãi ngộ Phi tài chính"},
        {"id": "sec_recommend_motivation", "title": "5. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 2.1 successfully built!")


# ==============================================================================
# LECTURE 2.2: Organisation and people management
# ==============================================================================
async def build_2_2():
    lid = 'fe4967aa-7d4c-480c-af71-e0d867459044'
    code = '2_2'
    title = '2.2. Organisation and people management'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-org-structure" class="lecture-interactive-card" data-lecture-section="sec_org_structure" style="cursor: pointer; ')
    
    t_h3_concepts = str(h3s[0])
    r_h3_concepts = t_h3_concepts.replace('<h3', '<h3 id="card-org-concepts" class="lecture-interactive-card" data-lecture-section="card_org_concepts" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-management" class="lecture-interactive-card" data-lecture-section="sec_management" style="cursor: pointer; ')
    
    t_h3_delegation = str(h3s[1])
    r_h3_delegation = t_h3_delegation.replace('<h3', '<h3 id="card-delegation" class="lecture-interactive-card" data-lecture-section="card_delegation" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-leadership-styles" class="lecture-interactive-card" data-lecture-section="sec_leadership_styles" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-trade-unions" class="lecture-interactive-card" data-lecture-section="sec_trade_unions" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-recommend-leadership" class="lecture-interactive-card" data-lecture-section="sec_recommend_leadership" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_concepts, r_h3_concepts, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_delegation, r_h3_delegation, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    # Balance unclosed outer div in 2.2
    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff == 1:
        new_html = new_html.strip() + "\n</div>"
        print("Fixed unclosed outer div in 2.2! New diff = 0")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2.2: Cơ cấu tổ chức và Quản trị con người",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 2.2: Organisation and People Management. In this lesson, we analyze how enterprises design organizational charts, explore spans of control and chain of command, evaluate management roles and delegation, compare autocratic, democratic, and laissez-faire leadership, and assess the role of trade unions.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 2.2: Cơ cấu tổ chức và Quản trị con người. Trong bài học này, chúng ta sẽ khảo sát sơ đồ tổ chức doanh nghiệp, tầm kiểm soát và chuỗi mệnh lệnh, vai trò của nhà quản trị và sự ủy quyền, so sánh ba phong cách lãnh đạo độc đoán, dân chủ, tự do, cùng vai trò của công đoàn."
        },
        {
            "id": "sec_org_structure",
            "title": "1. Cơ cấu Tổ chức Doanh nghiệp",
            "selector": "#sec-org-structure",
            "en": "Section 1 examines organizational structures. An organizational chart illustrates lines of authority and communication across functional departments. We contrast tall hierarchical structures—having narrow spans of control and long chains of command—against flat structures with wide spans of control. Delayering removes intermediate management tiers to accelerate decision making and lower overhead expenses.",
            "vi": "Mục một xem xét cơ cấu tổ chức doanh nghiệp. Sơ đồ tổ chức thể hiện quyền hạn và các kênh liên lạc giữa các phòng ban. Chúng ta phân biệt cơ cấu hình tháp nhiều tầng (tall structure) có tầm kiểm soát hẹp và chuỗi mệnh lệnh dài với cơ cấu phẳng (flat structure) có tầm kiểm soát rộng. Quá trình cắt giảm tầng nấc quản lý (delayering) giúp ra quyết định nhanh hơn và tiết kiệm chi phí lương."
        },
        {
            "id": "card_org_concepts",
            "title": "Các khái niệm then chốt trong Sơ đồ tổ chức",
            "selector": "#card-org-concepts",
            "en": "Key structural concepts include: Chain of Command—the vertical route through which instructions pass down from directors to shopfloor workers; Span of Control—the number of subordinates directly answering to a superior; and the distinction between Line Managers possessing executive authority and Staff Managers providing specialist advisory support.",
            "vi": "Các khái niệm then chốt gồm: Chuỗi mệnh lệnh (Chain of Command) – con đường truyền đạt chỉ thị từ giám đốc xuống nhân viên; Tầm kiểm soát (Span of Control) – số lượng cấp dưới do một cấp trên trực tiếp quản lý; cùng sự phân biệt giữa Nhà quản lý trực tiếp (Line Manager) có quyền ra lệnh và Nhà quản lý chuyên trách (Staff Manager) giữ vai trò cố vấn chuyên môn."
        },
        {
            "id": "sec_management",
            "title": "2. Vai trò và Chức năng Quản trị",
            "selector": "#sec-management",
            "en": "Section 2 details the classical five managerial functions defined by Henri Fayol: Planning strategic targets, Organising corporate resources, Commanding operational directives, Coordinating cross-departmental efforts, and Controlling performance against planned budgets.",
            "vi": "Mục hai trình bày năm chức năng quản trị kinh điển của Henri Fayol: Lập kế hoạch (Planning) mục tiêu tương lai, Tổ chức (Organising) phân bổ nguồn lực, Chỉ huy (Commanding) ban hành mệnh lệnh, Điều phối (Coordinating) phối hợp giữa các phòng ban, và Kiểm soát (Controlling) đo lường hiệu quả so với chỉ tiêu đã định."
        },
        {
            "id": "card_delegation",
            "title": "Sự Ủy quyền trong Quản lý (Delegation)",
            "selector": "#card-delegation",
            "en": "Delegation is the passing down of operational authority from a senior manager to a subordinate to execute specific tasks, while ultimate accountability remains with the manager. Effective delegation frees executive time for strategic planning, trains employees for promotion, and demonstrates trust, though poor supervision risks operational blunders.",
            "vi": "Ủy quyền (Delegation) là việc trao quyền quyết định từ cấp quản lý xuống cấp dưới để hoàn thành công việc cụ thể, nhưng trách nhiệm giải trình cuối cùng vẫn thuộc về nhà quản lý. Ủy quyền hiệu quả giúp cấp trên có thời gian cho chiến lược dài hạn, rèn luyện nhân viên thăng tiến và thể hiện sự tin tưởng, dù việc thiếu giám sát có thể gây sai sót nghiệp vụ."
        },
        {
            "id": "sec_leadership_styles",
            "title": "3. Ba Phong cách Lãnh đạo",
            "selector": "#sec-leadership-styles",
            "en": "Section 3 compares three primary leadership styles: Autocratic leaders retain all decision-making authority without consulting workers, vital in emergencies or on fast production lines. Democratic leaders involve employees through active consultation, enhancing motivation and idea generation. Laissez-faire leaders provide broad objectives and allow skilled professionals total execution autonomy.",
            "vi": "Mục ba so sánh ba phong cách lãnh đạo chủ đạo: Lãnh đạo độc đoán (Autocratic) nắm giữ mọi quyền quyết định không qua thảo luận, rất cần thiết trong tình huống khẩn cấp hoặc sản xuất dây chuyền. Lãnh đạo dân chủ (Democratic) lắng nghe và tham vấn ý kiến nhân viên, giúp nâng cao động lực và tính sáng tạo. Lãnh đạo tự do (Laissez-faire) giao mục tiêu tổng thể và trao quyền hành động tuyệt đối cho đội ngũ chuyên gia tự quyết."
        },
        {
            "id": "sec_trade_unions",
            "title": "4. Công đoàn và Thương lượng tập thể",
            "selector": "#sec-trade-unions",
            "en": "Section 4 explores Trade Unions—independent worker associations that engage in collective bargaining with employers to secure fair wages, safe working environments, and legal representation. For employers, negotiating with a single union representative streamlines discussions, although unresolved labour disputes can trigger disruptive industrial action.",
            "vi": "Mục bốn phân tích vai trò của Công đoàn (Trade Unions) – tổ chức đại diện cho người lao động tiến hành thương lượng tập thể với người sử dụng lao động để bảo đảm mức lương công bằng, điều kiện an toàn và hỗ trợ pháp lý. Với chủ doanh nghiệp, việc đàm phán qua một đại diện công đoàn giúp tiết kiệm thời gian, dù tranh chấp bất đồng có thể dẫn tới đình công ảnh hưởng sản xuất."
        },
        {
            "id": "sec_recommend_leadership",
            "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất phong cách lãnh đạo",
            "selector": "#sec-recommend-leadership",
            "en": "Section 5 presents Cambridge exam techniques for recommending leadership styles. High-scoring answers evaluate situational context: autocratic leadership suits crisis turnarounds or low-skilled repetitive assembly, whereas democratic styles maximize productivity among creative teams and R&D engineers. Justify by weighing speed of execution against workforce morale.",
            "vi": "Mục năm cung cấp kỹ năng làm bài Cambridge khi đề xuất phong cách lãnh đạo. Bài làm điểm cao cần bám sát tình huống: lãnh đạo độc đoán phù hợp khi khủng hoảng cần hành động gấp hoặc công việc lặp đi lặp lại ít đòi hỏi kỹ năng, trong khi phong cách dân chủ phát huy tối đa hiệu quả trong nhóm sáng tạo và nghiên cứu phát triển. Biện minh bằng cách cân đối giữa tốc độ xử lý và tinh thần nhân viên."
        }
    ]
    
    major_sections = [
        {"id": "sec_org_structure", "title": "1. Cơ cấu Tổ chức Doanh nghiệp"},
        {"id": "sec_management", "title": "2. Vai trò Quản trị và Sự ủy quyền"},
        {"id": "sec_leadership_styles", "title": "3. Ba Phong cách Lãnh đạo"},
        {"id": "sec_trade_unions", "title": "4. Công đoàn lao động"},
        {"id": "sec_recommend_leadership", "title": "5. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 2.2 successfully built!")


# ==============================================================================
# LECTURE 2.3: Recruitment, selection and training of employees
# ==============================================================================
async def build_2_3():
    lid = 'c2d359f6-1921-459e-a295-def7e891c352'
    code = '2_3'
    title = '2.3. Recruitment, selection and training of employees'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-hr-role" class="lecture-interactive-card" data-lecture-section="sec_hr_role" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-recruitment" class="lecture-interactive-card" data-lecture-section="sec_recruitment" style="cursor: pointer; ')
    
    t_h3_analysis = str(h3s[0])
    r_h3_analysis = t_h3_analysis.replace('<h3', '<h3 id="card-job-analysis" class="lecture-interactive-card" data-lecture-section="card_job_analysis" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-selection" class="lecture-interactive-card" data-lecture-section="sec_selection" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-training" class="lecture-interactive-card" data-lecture-section="sec_training" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-part-full-time" class="lecture-interactive-card" data-lecture-section="sec_part_full_time" style="cursor: pointer; ')
    
    t_h2_6 = str(h2s[5])
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-downsizing" class="lecture-interactive-card" data-lecture-section="sec_downsizing" style="cursor: pointer; ')
    
    t_h2_7 = str(h2s[6])
    r_h2_7 = t_h2_7.replace('<h2', '<h2 id="sec-legal-controls" class="lecture-interactive-card" data-lecture-section="sec_legal_controls" style="cursor: pointer; ')
    
    t_h2_8 = str(h2s[7])
    r_h2_8 = t_h2_8.replace('<h2', '<h2 id="sec-recommend-recruitment" class="lecture-interactive-card" data-lecture-section="sec_recommend_recruitment" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_analysis, r_h3_analysis, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)\
                   .replace(t_h2_6, r_h2_6, 1)\
                   .replace(t_h2_7, r_h2_7, 1)\
                   .replace(t_h2_8, r_h2_8, 1)

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
            "title": "2. Quy trình Tuyển dụng và Tài liệu cốt lõi",
            "selector": "#sec-recruitment",
            "en": "Section 2 distinguishes the three vital documents of recruitment: Job Analysis identifies tasks involved; Job Description outlines responsibilities, reporting lines, and working conditions of the role; and Person Specification details qualifications, experience, skills, and personal attributes demanded of the ideal candidate.",
            "vi": "Mục hai phân biệt ba tài liệu cốt lõi trong tuyển dụng: Phân tích công việc (Job Analysis) khảo sát chi tiết đầu việc; Bản mô tả công việc (Job Description) nêu rõ trách nhiệm, cấp quản lý trực tiếp và điều kiện làm việc; và Bản tiêu chuẩn ứng viên (Person Specification) quy định bằng cấp, kinh nghiệm và kỹ năng cần có của người ứng tuyển."
        },
        {
            "id": "card_job_analysis",
            "title": "Tuyển dụng Nội bộ đối chiếu với Tuyển dụng Bên ngoài",
            "selector": "#card-job-analysis",
            "en": "Internal recruitment fills vacancies by promoting existing staff, which is cheaper, faster, motivates loyal workers, and minimizes induction time. However, it limits the applicant pool and creates a subsequent vacancy. External recruitment advertises vacancies publicly, injecting fresh talent and innovative industry ideas, though advertising and agency fees are significantly higher.",
            "vi": "Tuyển dụng nội bộ cất nhắc nhân viên hiện có, giúp tiết kiệm chi phí, quy trình nhanh chóng, khích lệ nhân viên và rút ngắn thời gian hội nhập nhưng không đem lại ý tưởng mới và để lại vị trí trống phía dưới. Ngược lại, tuyển dụng bên ngoài mở rộng ra công chúng mang về nhân tố mới với góc nhìn đột phá, dù chi phí quảng cáo và tuyển mộ tốn kém hơn nhiều."
        },
        {
            "id": "sec_selection",
            "title": "3. Phương pháp Chọn lọc và Hợp đồng lao động",
            "selector": "#sec-selection",
            "en": "Section 3 covers selection instruments: CV screening, structured interviews, aptitude tests, psychometric profiling, and practical assessment tasks. Once an offer is accepted, a legally binding Contract of Employment defines wages, working hours, statutory holiday entitlement, job title, and notice periods.",
            "vi": "Mục ba bao gồm các công cụ chọn lọc: sàng lọc hồ sơ CV, phỏng vấn có cấu trúc, bài kiểm tra năng lực, trắc nghiệm tâm lý tính cách và bài kiểm tra kỹ năng thực tế. Khi trúng tuyển, Hợp đồng lao động (Contract of Employment) mang tính pháp lý ràng buộc sẽ quy định mức lương, thời gian làm việc, chế độ nghỉ phép, chức danh và thời hạn thông báo nghỉ việc."
        },
        {
            "id": "sec_training",
            "title": "4. Các hình thức Đào tạo nhân sự",
            "selector": "#sec-training",
            "en": "Section 4 investigates Induction training for new joiners, On-the-job training where employees learn from experienced colleagues while working on real machinery, and Off-the-job training at specialized educational colleges. On-the-job is cost-effective but passes on bad habits, whereas off-the-job imparts state-of-the-art skills without disrupting actual workshop output.",
            "vi": "Mục bốn phân tích Đào tạo hội nhập (Induction) cho nhân viên mới, Đào tạo tại chỗ (On-the-job) kèm cặp trực tiếp trên dây chuyền sản xuất, và Đào tạo ngoài chỗ làm (Off-the-job) tại các trung tâm đào tạo chuyên nghiệp. Đào tạo tại chỗ chi phí thấp nhưng dễ lây thói quen xấu, trong khi đào tạo ngoài chỗ làm tiếp thu kỹ thuật hiện đại mà không làm gián đoạn sản xuất tại phân xưởng."
        },
        {
            "id": "sec_part_full_time",
            "title": "5. Nhân viên Bán thời gian và Tinh giản nhân sự",
            "selector": "#sec-part-full-time",
            "en": "Section 5 contrasts part-time flexibility against full-time loyalty, and clarifies the legal difference between Dismissal and Redundancy. Dismissal occurs when an employee is terminated due to incompetence or gross misconduct. Redundancy happens when a post becomes completely unnecessary due to falling demand, factory closure, or technological automation.",
            "vi": "Mục năm đối chiếu sự linh hoạt của nhân viên bán thời gian với tính gắn kết của nhân viên toàn thời gian, đồng thời phân biệt rõ Sa thải (Dismissal) và Cắt giảm dôi dư (Redundancy). Sa thải diễn ra khi nhân viên yếu kém năng lực hoặc vi phạm kỷ luật nghiêm trọng. Trong khi đó, cắt giảm dôi dư là do vị trí công việc không còn cần thiết vì nhu cầu thị trường sụt giảm, đóng cửa nhà máy hoặc tự động hóa công nghệ."
        },
        {
            "id": "sec_recommend_recruitment",
            "title": "6. Chiến lược làm bài thi Cambridge: Đề xuất phương án nhân sự",
            "selector": "#sec-recommend-recruitment",
            "en": "Section 6 guides exam answers on staffing decisions. Candidates must balance financial budget, speed of deployment, required technical mastery, and long-term staff morale before recommending whether to train existing workers or recruit external specialists.",
            "vi": "Mục sáu hướng dẫn giải quyết bài tập tình huống nhân sự trong đề thi Cambridge. Thí sinh phải cân nhắc kỹ lưỡng ngân sách tài chính, tiến độ thực hiện, yêu cầu chuyên môn kỹ thuật và tâm lý nhân viên trước khi đưa ra quyết định nên đào tạo nhân sự nội bộ hay tuyển chuyên gia bên ngoài."
        }
    ]
    
    major_sections = [
        {"id": "sec_hr_role", "title": "1. Vai trò của Bộ phận Nhân sự"},
        {"id": "sec_recruitment", "title": "2. Quy trình Tuyển dụng"},
        {"id": "sec_selection", "title": "3. Phương pháp Chọn lọc và Hợp đồng"},
        {"id": "sec_training", "title": "4. Đào tạo nhân sự (On-the-job & Off-the-job)"},
        {"id": "sec_part_full_time", "title": "5. Bán thời gian & Tinh giản nhân sự"},
        {"id": "sec_recommend_recruitment", "title": "6. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 2.3 successfully built!")


# ==============================================================================
# LECTURE 2.4: Internal and external communication
# ==============================================================================
async def build_2_4():
    lid = '47166a31-2a55-40ea-a86c-81569cfafa32'
    code = '2_4'
    title = '2.4. Internal and external communication'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-effective-comm" class="lecture-interactive-card" data-lecture-section="sec_effective_comm" style="cursor: pointer; ')
    
    t_h3_elements = str(h3s[0])
    r_h3_elements = t_h3_elements.replace('<h3', '<h3 id="card-comm-elements" class="lecture-interactive-card" data-lecture-section="card_comm_elements" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-directions" class="lecture-interactive-card" data-lecture-section="sec_directions" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-comm-methods" class="lecture-interactive-card" data-lecture-section="sec_comm_methods" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-comm-barriers" class="lecture-interactive-card" data-lecture-section="sec_comm_barriers" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-recommend-comm" class="lecture-interactive-card" data-lecture-section="sec_recommend_comm" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_elements, r_h3_elements, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2.4: Giao tiếp nội bộ và bên ngoài",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 2.4: Internal and External Communication. In this final chapter of Topic 2, we explore the four essential components of effective communication, analyze vertical and horizontal communication directions, evaluate verbal, written, visual, and electronic media, and overcome communication barriers.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 2.4: Giao tiếp nội bộ và bên ngoài. Trong bài học khép lại Chủ đề hai, chúng ta sẽ khảo sát bốn thành phần cốt lõi của giao tiếp hiệu quả, các hướng giao tiếp dọc và ngang, đánh giá các phương thức truyền thông bằng lời, văn bản, hình ảnh, điện tử và các giải pháp vượt qua rào cản giao tiếp."
        },
        {
            "id": "sec_effective_comm",
            "title": "1. Bản chất của Giao tiếp hiệu quả",
            "selector": "#sec-effective-comm",
            "en": "Section 1 defines effective communication as the transfer of information from a sender to a receiver with the message being clearly understood. Effective communication ensures clear instructions, speeds up decision execution, reduces costly mistakes, and builds employee morale.",
            "vi": "Mục một định nghĩa giao tiếp hiệu quả là sự truyền đạt thông tin từ người gửi đến người nhận sao cho thông điệp được thấu hiểu chính xác. Giao tiếp mạch lạc giúp hướng dẫn rõ ràng, đẩy nhanh tốc độ thực thi, hạn chế sai sót gây lãng phí và củng cố tinh thần làm việc của nhân viên."
        },
        {
            "id": "card_comm_elements",
            "title": "Bốn thành tố của Quy trình Giao tiếp",
            "selector": "#card-comm-elements",
            "en": "The communication process consists of four indispensable elements: The Transmitter or sender who initiates the message; The Medium or channel carrying the message; The Receiver who decodes the information; and Crucially, Feedback, which confirms whether the message was received and understood correctly.",
            "vi": "Quy trình giao tiếp bao gồm bốn thành tố không thể thiếu: Người gửi (Transmitter) khởi tạo thông điệp; Phương tiện truyền tải (Medium) như email hay thư từ; Người nhận (Receiver) tiếp nhận và giải mã thông tin; và đặc biệt là Phản hồi (Feedback) giúp xác nhận thông điệp đã được hiểu đúng hay chưa."
        },
        {
            "id": "sec_directions",
            "title": "2. Các Hướng Giao tiếp trong Tổ chức",
            "selector": "#sec-directions",
            "en": "Section 2 maps organizational communication pathways: Downward communication sends instructions from executives to operational staff; Upward communication conveys worker feedback and grievance reporting back to management; and Horizontal communication coordinates projects between peers across departments.",
            "vi": "Mục hai phác thảo các tuyến đường truyền thông trong tổ chức: Giao tiếp từ trên xuống (Downward) truyền đạt chỉ đạo từ ban giám đốc xuống cấp dưới; Giao tiếp từ dưới lên (Upward) phản hồi tâm tư và đề xuất của nhân viên lên lãnh đạo; và Giao tiếp ngang (Horizontal) phối hợp công việc giữa các đồng nghiệp cùng cấp giữa các phòng ban."
        },
        {
            "id": "sec_comm_methods",
            "title": "3. Các Phương thức Giao tiếp",
            "selector": "#sec-comm-methods",
            "en": "Section 3 evaluates communication media: Verbal communication via meetings provides instant feedback and tone nuance but leaves no written record. Written communication via letters and reports creates permanent audit trails but lacks personal warmth. Visual diagrams and electronic communications like intranet and video conferencing offer rapid global reach.",
            "vi": "Mục ba đánh giá các phương thức truyền thông: Giao tiếp bằng lời nói (Verbal) qua các cuộc họp cho phép phản hồi tức thì và biểu cảm sinh động nhưng không để lại bằng chứng văn bản. Giao tiếp bằng văn bản (Written) lưu trữ hồ sơ pháp lý rõ ràng nhưng thiếu sự tương tác cảm xúc. Phương tiện trực quan và các kênh điện tử như mạng nội bộ, video conference mang lại tốc độ truyền tải xuyên biên giới vượt trội."
        },
        {
            "id": "sec_comm_barriers",
            "title": "4. Rào cản Giao tiếp và Cách khắc phục",
            "selector": "#sec-comm-barriers",
            "en": "Section 4 investigates communication barriers: technical jargon, excessive information overload, physical noise, inappropriate channels, long chains of command distorting messages, and cultural misunderstandings. Solutions require concise messaging, active two-way feedback, and selecting the right medium for the context.",
            "vi": "Mục bốn phân tích các rào cản giao tiếp: thuật ngữ chuyên môn khó hiểu, quá tải thông tin, tiếng ồn vật lý, chọn sai phương tiện truyền tải, chuỗi mệnh lệnh quá dài gây tam sao thất bản và khác biệt văn hóa. Giải pháp khắc phục đòi hỏi thông điệp súc tích, khuyến khích phản hồi hai chiều và lựa chọn phương tiện phù hợp với ngữ cảnh."
        }
    ]
    
    major_sections = [
        {"id": "sec_effective_comm", "title": "1. Bản chất Giao tiếp và 4 Thành tố"},
        {"id": "sec_directions", "title": "2. Hướng Giao tiếp trong Tổ chức"},
        {"id": "sec_comm_methods", "title": "3. Phương thức Giao tiếp"},
        {"id": "sec_comm_barriers", "title": "4. Rào cản Giao tiếp và Giải pháp"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 2.4 successfully built!")


# ==============================================================================
# MAIN BATCH RUNNER FOR TOPIC 2
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING TOPIC 2 BUILD: ALL 4 LECTURES (2.1 -> 2.4)")
    print("*******************************************************\n")
    
    await build_2_1()
    await asyncio.sleep(2)
    
    await build_2_2()
    await asyncio.sleep(2)
    
    await build_2_3()
    await asyncio.sleep(2)
    
    await build_2_4()
    
    print("\n*******************************************************")
    print("TOPIC 2 COMPLETE: ALL 4 LECTURES PROCESSED SUCCESSFULLY!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
