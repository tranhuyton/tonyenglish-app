import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 2.2 ID
LID = 'fe4967aa-7d4c-480c-af71-e0d867459044'
CODE = '2_2'
TITLE = '2.2. Organisation and people management'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 13 AUDIO SEGMENTS FOR LESSON 2.2
# ==============================================================================
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
        "title": "🔑 Tầm kiểm soát, Chuỗi mệnh lệnh & Nhà quản lý trực tiếp/chuyên trách",
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
        "title": "🤝 Sự Ủy quyền trong Quản lý (Delegation)",
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
        "id": "card_autocratic",
        "title": "🗣️ Phong cách Lãnh đạo Độc đoán (Autocratic Style)",
        "selector": "#card-autocratic",
        "en": "Autocratic leaders make all decisions independently and demand strict obedience without consulting subordinates. Communication flows strictly downwards. It is ideal in emergency crises, military operations, or urgent factory safety situations, but severely undermines employee morale and initiative over the long term.",
        "vi": "Nhà lãnh đạo độc đoán tự mình đưa ra toàn bộ quyết định và yêu cầu cấp dưới chấp hành nghiêm ngặt mà không cần thảo luận. Luồng thông tin truyền đạt nghiêm ngặt từ trên xuống. Phong cách này phát huy hiệu quả tối đa trong tình huống khủng hoảng khẩn cấp, quốc phòng hoặc an toàn sản xuất, nhưng về lâu dài sẽ làm triệt tiêu tinh thần chủ động và sáng tạo của nhân viên."
    },
    {
        "id": "card_democratic",
        "title": "🤝 Phong cách Lãnh đạo Dân chủ (Democratic Style)",
        "selector": "#card-democratic",
        "en": "Democratic leaders encourage two-way communication and actively consult employees before making final decisions. This approach boosts worker morale, fosters belonging, and generates innovative ideas from experienced staff, though the consultation process can slow down urgent decision-making.",
        "vi": "Nhà lãnh đạo dân chủ khuyến khích giao tiếp hai chiều và tích cực tham vấn ý kiến nhân viên trước khi ra quyết định cuối cùng. Cách tiếp cận này nâng cao tinh thần làm việc, tạo cảm giác gắn kết và khai thác được nhiều sáng kiến hữu ích từ đội ngũ nhân viên, dù quá trình thảo luận có thể làm chậm tốc độ xử lý công việc."
    },
    {
        "id": "card_laissez_faire",
        "title": "🕊️ Phong cách Lãnh đạo Tự do (Laissez-faire Style)",
        "selector": "#card-laissez-faire",
        "en": "Laissez-faire leadership establishes broad strategic objectives while granting employees full autonomy to make decisions and organize their own tasks. It works best with highly skilled, self-motivated research scientists and software engineers, but risks severe lack of direction if workers lack experience or discipline.",
        "vi": "Lãnh đạo tự do vạch ra các mục tiêu chiến lược tổng thể nhưng trao quyền tự quyết hoàn toàn cho nhân viên trong việc tổ chức công việc. Mô hình này phù hợp nhất với các nhóm nghiên cứu khoa học và kỹ sư phần mềm có chuyên môn cao và tính tự giác lớn, nhưng tiềm ẩn nguy cơ mất phương hướng nếu nhân sự thiếu kinh nghiệm hoặc kỷ luật."
    },
    {
        "id": "sec_trade_unions",
        "title": "4. Công đoàn và Thương lượng tập thể",
        "selector": "#sec-trade-unions",
        "en": "Section 4 explores Trade Unions—independent worker associations that engage in collective bargaining with employers to secure fair wages, safe working environments, and legal representation. For employers, negotiating with a single union representative streamlines discussions, although unresolved labour disputes can trigger disruptive industrial action.",
        "vi": "Mục bốn phân tích vai trò của Công đoàn (Trade Unions) – tổ chức đại diện cho người lao động tiến hành thương lượng tập thể với người sử dụng lao động để bảo đảm mức lương công bằng, điều kiện an toàn và hỗ trợ pháp lý. Với chủ doanh nghiệp, việc đàm phán qua một đại diện công đoàn giúp tiết kiệm thời gian, dù tranh chấp bất đồng có thể dẫn tới đình công ảnh hưởng sản xuất."
    },
    {
        "id": "card_union_workers",
        "title": "👥 Lợi ích và Hạn chế của Công đoàn đối với Người lao động",
        "selector": "#card-union-workers",
        "en": "For employees, trade unions provide collective strength, legal defense against unfair dismissal, and negotiate higher wages, shorter hours, and safer working conditions. However, workers must pay recurring membership dues and may be compelled to participate in unpaid strike actions they personally oppose.",
        "vi": "Đối với người lao động, công đoàn mang lại sức mạnh tập thể, bảo vệ quyền lợi pháp lý trước các quyết định sa thải bất công và đàm phán nâng lương, giảm giờ làm, cải thiện an toàn lao động. Tuy nhiên, đoàn viên phải đóng đoàn phí định kỳ và có thể phải tham gia các cuộc đình công không lương dù bản thân không mong muốn."
    },
    {
        "id": "card_union_employers",
        "title": "🏢 Tác động của Công đoàn đối với Người sử dụng lao động",
        "selector": "#card-union-employers",
        "en": "For employers, trade unions simplify human resources through collective bargaining with a single representative rather than hundreds of individuals, fostering structured dispute resolution. Conversely, unions possess bargaining power that increases wage costs, and industrial disputes can halt factory production and damage commercial goodwill.",
        "vi": "Đối với chủ doanh nghiệp, công đoàn giúp đơn giản hóa quản trị nhân sự nhờ thương lượng tập thể với một đại diện duy nhất thay vì hàng trăm cá nhân riêng lẻ, giúp giải quyết tranh chấp có trật tự. Ngược lại, công đoàn có sức mạnh mặc cả đẩy chi phí tiền lương lên cao, và các cuộc tranh chấp lao động có thể làm tê liệt sản xuất và gây tổn hại uy tín thương mại."
    },
    {
        "id": "sec_recommend_leadership",
        "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất phong cách lãnh đạo",
        "selector": "#sec-recommend-leadership",
        "en": "Section 5 outlines exam technique for leadership recommendation questions. Candidates must evaluate contextual factors: crisis situations require autocratic direction; creative technical projects thrive under democratic or laissez-faire autonomy. Always balance employee morale against decision turnaround time.",
        "vi": "Mục năm cung cấp chiến thuật làm bài thi Cambridge cho câu hỏi đề xuất phong cách lãnh đạo. Thí sinh cần phân tích bối cảnh tình huống: trường hợp khủng hoảng đòi hỏi phong cách độc đoán; dự án sáng tạo kỹ thuật lại phát huy tối đa với phong cách dân chủ hoặc tự do. Luôn đối chiếu giữa tinh thần nhân viên và tốc độ ra quyết định."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_org_structure": {"start": 1, "end": 2},
    "sec_management": {"start": 3, "end": 4},
    "sec_leadership_styles": {"start": 5, "end": 8},
    "sec_trade_unions": {"start": 9, "end": 11},
    "sec_recommend_leadership": {"start": 12, "end": 12}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.2 Organisation and People Management (Cơ cấu Tổ chức &amp; Quản trị Con người)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. ORGANIZATIONAL STRUCTURE -->
    <div style="margin-bottom: 45px;">
        <div id="sec-org-structure" class="lecture-interactive-card" data-lecture-section="sec_org_structure" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏢 1. ORGANIZATIONAL STRUCTURE</h2>
            <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center;">
                <div style="flex: 1; min-width: 300px;">
                    <svg viewBox="0 0 500 250" width="100%" style="max-width: 500px; background:#ffffff; border-radius:8px; border:1px solid #cbd5e1; font-family: Arial, sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: block; margin: 0 auto;">
                        <rect x="175" y="20" width="150" height="30" fill="#1e40af" rx="4"></rect>
                        <text x="250" y="40" text-anchor="middle" font-size="12" font-weight="bold" fill="#ffffff">Managing Director</text>
                        <line x1="250" y1="50" x2="250" y2="70" stroke="#64748b" stroke-width="2"></line>
                        <line x1="60" y1="70" x2="440" y2="70" stroke="#64748b" stroke-width="2"></line>
                        <line x1="60" y1="70" x2="60" y2="90" stroke="#64748b" stroke-width="2"></line>
                        <rect x="10" y="90" width="100" height="30" fill="#3b82f6" rx="4"></rect>
                        <text x="60" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Operations</text>
                        <text x="60" y="117" text-anchor="middle" font-size="10" fill="#eff6ff">Director</text>
                        <line x1="186" y1="70" x2="186" y2="90" stroke="#64748b" stroke-width="2"></line>
                        <rect x="136" y="90" width="100" height="30" fill="#3b82f6" rx="4"></rect>
                        <text x="186" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Marketing</text>
                        <text x="186" y="117" text-anchor="middle" font-size="10" fill="#eff6ff">Director</text>
                        <line x1="313" y1="70" x2="313" y2="90" stroke="#64748b" stroke-width="2"></line>
                        <rect x="263" y="90" width="100" height="30" fill="#3b82f6" rx="4"></rect>
                        <text x="313" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">Finance</text>
                        <text x="313" y="117" text-anchor="middle" font-size="10" fill="#eff6ff">Director</text>
                        <line x1="440" y1="70" x2="440" y2="90" stroke="#64748b" stroke-width="2"></line>
                        <rect x="390" y="90" width="100" height="30" fill="#3b82f6" rx="4"></rect>
                        <text x="440" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff">HR Director</text>
                        <line x1="186" y1="120" x2="186" y2="140" stroke="#64748b" stroke-width="2"></line>
                        <line x1="140" y1="140" x2="232" y2="140" stroke="#64748b" stroke-width="2"></line>
                        <line x1="140" y1="140" x2="140" y2="160" stroke="#64748b" stroke-width="2"></line>
                        <rect x="100" y="160" width="80" height="30" fill="#60a5fa" rx="4"></rect>
                        <text x="140" y="175" text-anchor="middle" font-size="10" font-weight="bold" fill="#ffffff">Manager</text>
                        <line x1="232" y1="140" x2="232" y2="160" stroke="#64748b" stroke-width="2"></line>
                        <rect x="192" y="160" width="80" height="30" fill="#60a5fa" rx="4"></rect>
                        <text x="232" y="175" text-anchor="middle" font-size="10" font-weight="bold" fill="#ffffff">Manager</text>
                    </svg>
                </div>
                <div style="flex: 1.5; min-width: 300px;">
                    <p style="font-size: 15px; color: #475569; margin: 0 0 14px 0;">
                        <b>Organizational structure</b> refers to the levels of management and division of responsibilities within a business, officially depicted on organizational charts.
                    </p>
                    <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 12px 16px; border-radius: 6px;">
                        <b style="color: #047857; font-size: 14.5px;">✅ Key Advantages:</b>
                        <ul style="margin: 4px 0 0 0; padding-left: 18px; color: #065f46; font-size: 13.5px; line-height: 1.5;">
                            <li>Clarifies official lines of authority and reporting.</li>
                            <li>Shows departmental inter-relationships and fosters belonging.</li>
                            <li>Delayering removes management layers to quicken communication.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <div id="card-org-concepts" class="lecture-interactive-card" data-lecture-section="card_org_concepts" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🔑 Span of Control, Chain of Command &amp; Management Types</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 14px;">
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px;">
                    <b style="color: #1d4ed8; font-size: 15px;">📏 Span of Control:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #334155;">Number of subordinates directly reporting to a single superior.</p>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px;">
                    <b style="color: #1d4ed8; font-size: 15px;">🔗 Chain of Command:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #334155;">The vertical route passing directives down through management levels.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px;">
                    <b style="color: #334155; font-size: 15px;">👔 Line vs Staff Managers:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #475569;"><b>Line:</b> Direct operational authority. <b>Staff:</b> Specialist advisory experts (e.g. Legal, IT).</p>
                </div>
            </div>
            <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 10px 14px; border-radius: 6px; font-size: 13.5px; color: #92400e;">
                <b>⚡ The Golden Rule:</b> The WIDER the span of control ↔ The SHORTER the chain of command (quicker decisions, higher trust).
            </div>
        </div>
    </div>

    <!-- 2. MANAGEMENT -->
    <div style="margin-bottom: 45px;">
        <div id="sec-management" class="lecture-interactive-card" data-lecture-section="sec_management" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">👔 2. MANAGEMENT FUNCTIONS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0 0 16px 0; line-height: 1.6;">Henri Fayol identified 5 primary functions executed by managers:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px; text-align: center;">
                    <b style="color: #059669; font-size: 15px;">📅 Planning</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Setting aims &amp; forecasting resources.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px; text-align: center;">
                    <b style="color: #059669; font-size: 15px;">🗂️ Organizing</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Allocating resources &amp; delegating duties.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px; text-align: center;">
                    <b style="color: #059669; font-size: 15px;">🔄 Coordinating</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Harmonizing cross-department activities.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px; text-align: center;">
                    <b style="color: #059669; font-size: 15px;">🗣️ Commanding</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Supervising, guiding &amp; leading staff.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 14px; text-align: center;">
                    <b style="color: #059669; font-size: 15px;">📊 Controlling</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Evaluating output against targets.</p>
                </div>
            </div>
        </div>

        <div id="card-delegation" class="lecture-interactive-card" data-lecture-section="card_delegation" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 12px;">🤝 Delegation: Passing Authority to Subordinates</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f0fdfa; border: 1px solid #99f6e4; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f766e; font-size: 15px;">👑 Benefits to Managers:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #115e59; line-height: 1.5;">Frees executive time for strategic planning; provides a mechanism to test subordinate competence.</p>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px;">
                    <b style="color: #1d4ed8; font-size: 15px;">👷 Benefits to Subordinates:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #1e40af; line-height: 1.5;">Enriches work, demonstrates managerial trust, increases motivation, and trains workers for promotion.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. LEADERSHIP STYLES -->
    <div style="margin-bottom: 45px;">
        <div id="sec-leadership-styles" class="lecture-interactive-card" data-lecture-section="sec_leadership_styles" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">👑 3. THREE LEADERSHIP STYLES</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Leadership style describes the way a leader approaches decision-making, communication, and interpersonal authority.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
            <div id="card-autocratic" class="lecture-interactive-card" data-lecture-section="card_autocratic" style="background: #ffffff; border: 1.5px solid #fecaca; border-top: 4px solid #dc2626; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <div style="font-size: 26px; margin-bottom: 8px;">🗣️</div>
                <h4 style="color: #dc2626; font-size: 18px; margin: 0 0 10px 0;">Autocratic Style</h4>
                <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.6;">
                    Manager holds all decision-making authority. One-way downwards communication. Essential in crises and hazardous settings; causes staff resentment if overused.
                </p>
            </div>

            <div id="card-democratic" class="lecture-interactive-card" data-lecture-section="card_democratic" style="background: #ffffff; border: 1.5px solid #bbf7d0; border-top: 4px solid #16a34a; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <div style="font-size: 26px; margin-bottom: 8px;">🤝</div>
                <h4 style="color: #16a34a; font-size: 18px; margin: 0 0 10px 0;">Democratic Style</h4>
                <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.6;">
                    Manager actively consults employees and encourages two-way dialogue before deciding. Boosts morale and creative input; consultation can slow urgent action.
                </p>
            </div>

            <div id="card-laissez-faire" class="lecture-interactive-card" data-lecture-section="card_laissez_faire" style="background: #ffffff; border: 1.5px solid #e9d5ff; border-top: 4px solid #9333ea; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <div style="font-size: 26px; margin-bottom: 8px;">🕊️</div>
                <h4 style="color: #9333ea; font-size: 18px; margin: 0 0 10px 0;">Laissez-faire Style</h4>
                <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.6;">
                    Manager sets broad objectives and leaves staff with total autonomy to organize tasks. Ideal for research teams; risks drift if workers lack clear self-discipline.
                </p>
            </div>
        </div>
    </div>

    <!-- 4. TRADE UNIONS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-trade-unions" class="lecture-interactive-card" data-lecture-section="sec_trade_unions" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🤝 4. TRADE UNIONS</h2>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 14px 18px; border-radius: 8px; font-size: 15px; color: #831843; line-height: 1.6;">
                A <b>trade union</b> is an organized body of employees formed to defend rights, negotiate pay and conditions, and represent workers in industrial disputes.
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">
            <div id="card-union-workers" class="lecture-interactive-card" data-lecture-section="card_union_workers" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h3 style="color: #0f172a; font-size: 17px; margin-top: 0; margin-bottom: 12px;">👥 Trade Unions: Impact on Workers</h3>
                <div style="margin-bottom: 10px;">
                    <b style="color: #16a34a; font-size: 14px;">✅ Benefits:</b>
                    <ul style="margin: 4px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                        <li>Collective bargaining power for higher wages and safety.</li>
                        <li>Legal representation against unfair dismissal.</li>
                    </ul>
                </div>
                <div>
                    <b style="color: #dc2626; font-size: 14px;">❌ Drawbacks:</b>
                    <ul style="margin: 4px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                        <li>Mandatory union membership subscription dues.</li>
                        <li>Risk of loss of wages during unpaid strike actions.</li>
                    </ul>
                </div>
            </div>

            <div id="card-union-employers" class="lecture-interactive-card" data-lecture-section="card_union_employers" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <h3 style="color: #0f172a; font-size: 17px; margin-top: 0; margin-bottom: 12px;">🏢 Trade Unions: Impact on Employers</h3>
                <div style="margin-bottom: 10px;">
                    <b style="color: #16a34a; font-size: 14px;">✅ Benefits:</b>
                    <ul style="margin: 4px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                        <li>Negotiating with one union official saves executive time.</li>
                        <li>Disciplined framework to settle grievances peacefully.</li>
                    </ul>
                </div>
                <div>
                    <b style="color: #dc2626; font-size: 14px;">❌ Drawbacks:</b>
                    <ul style="margin: 4px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                        <li>Upward pressure on labour costs and wage bills.</li>
                        <li>Industrial action (strikes, go-slows) halts output.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. RECOMMEND AND JUSTIFY (CAMBRIDGE EXAM STRATEGY) -->
    <div id="sec-recommend-leadership" class="lecture-interactive-card" data-lecture-section="sec_recommend_leadership" style="margin-bottom: 45px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
        <h2 style="color: #1e3a8a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; font-size: 22px; margin-top: 0; display: inline-block;">
            🎯 5. HOW TO RECOMMEND &amp; JUSTIFY A LEADERSHIP STYLE (Cambridge Exam Strategy)
        </h2>
        <p style="font-size: 15px; color: #1e40af; margin-bottom: 18px; line-height: 1.6;">
            Paper 1 and Paper 2 frequently present scenarios requiring candidates to recommend and justify the most suitable leadership style:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 16px;">
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #ef4444; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #b91c1c; font-size: 15px;">Autocratic:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Best during emergencies, sudden safety risks, or with temporary unskilled workers requiring strict direction.
                </p>
            </div>
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #047857; font-size: 15px;">Democratic:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Best with experienced, skilled staff when rolling out organizational change to ensure morale and staff buy-in.
                </p>
            </div>
            <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #9333ea; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                <b style="color: #7e22ce; font-size: 15px;">Laissez-faire:</b>
                <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                    Best with self-motivated creative researchers or software engineers who possess specialist expertise.
                </p>
            </div>
        </div>
        <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
            <b style="color: #1e40af; font-size: 14.5px;">💡 Cambridge Evaluation Formula:</b>
            <p style="margin: 4px 0 0 0; font-size: 13.5px; color: #334155; line-height: 1.5;">
                State the recommendation ➔ Cite 2 specific context advantages ➔ Acknowledge 1 significant drawback and explain how to mitigate it ➔ Conclude why it outranks the alternative.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.2 Organisation and People Management (Cơ cấu Tổ chức &amp; Quản trị Con người)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 2.2 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/2_2_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 2.2 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
