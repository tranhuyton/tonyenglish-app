import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 2.4 ID
LID = '47166a31-2a55-40ea-a86c-81569cfafa32'
CODE = '2_4'
TITLE = '2.4. Internal and external communication'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 12 AUDIO SEGMENTS FOR LESSON 2.4
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 2.4: Giao tiếp nội bộ và bên ngoài",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 2.4: Internal and External Communication. In this final lesson of Unit 2, we evaluate effective business communication, distinguish internal from external networks, trace one-way and two-way directional channels, compare verbal, written, and visual media, and dissect how to overcome communication barriers.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 2.4: Giao tiếp nội bộ và bên ngoài. Trong bài học kết thúc Chủ đề hai này, chúng ta sẽ phân tích quy trình giao tiếp hiệu quả, phân biệt mạng lưới nội bộ và bên ngoài, các luồng giao tiếp một chiều và hai chiều, so sánh các phương thức lời nói, văn bản, trực quan cùng cách khắc phục rào cản giao tiếp."
    },
    {
        "id": "sec_effective_comm",
        "title": "1. Bản chất của Giao tiếp Hiệu quả",
        "selector": "#sec-effective-comm",
        "en": "Section 1 defines communication as the process of transferring a message from a sender to a receiver who accurately understands it. Effective communication avoids costly industrial mistakes, aligns departments toward strategic goals, and boosts workforce morale.",
        "vi": "Mục một định nghĩa giao tiếp là quá trình truyền tải thông điệp từ người gửi tới người nhận sao cho người nhận hiểu đúng ý nghĩa thông điệp. Giao tiếp hiệu quả giúp tránh sai sót nghiệp vụ, gắn kết các phòng ban theo mục tiêu chung và nâng cao tinh thần làm việc của nhân viên."
    },
    {
        "id": "card_comm_elements",
        "title": "⚙️ Bốn Thành tố của Quy trình Giao tiếp (Sender ➔ Medium ➔ Receiver ➔ Feedback)",
        "selector": "#card-comm-elements",
        "en": "Every communication cycle contains four core elements: 1. The Sender who initiates the message; 2. The Medium or channel chosen to transmit it; 3. The Receiver who decodes the content; and 4. The Feedback or response confirming whether the message was accurately understood.",
        "vi": "Mọi chu trình giao tiếp đều bao gồm bốn thành tố cốt lõi: 1. Người gửi (Sender) khởi tạo thông điệp; 2. Phương tiện (Medium) hoặc kênh truyền tải được chọn; 3. Người nhận (Receiver) tiếp nhận và giải mã nội dung; và 4. Phản hồi (Feedback) xác nhận thông điệp đã được thấu hiểu chính xác."
    },
    {
        "id": "card_internal_vs_external",
        "title": "🏢 Giao tiếp Nội bộ đối chiếu Giao tiếp Bên ngoài",
        "selector": "#card-internal-vs-external",
        "en": "Internal communication occurs between colleagues inside the enterprise—such as notices to staff, inter-department memos, and team briefings. External communication connects the firm with outside stakeholders, including supplier orders, marketing commercials, and bank correspondence.",
        "vi": "Giao tiếp nội bộ diễn ra giữa các thành viên bên trong doanh nghiệp – ví dụ thông báo nội bộ, văn bản liên phòng ban và các cuộc họp giao ban. Giao tiếp bên ngoài kết nối doanh nghiệp với các đối tượng bên ngoài, bao gồm đơn đặt hàng nhà cung ứng, quảng cáo tiếp thị và giao dịch với ngân hàng."
    },
    {
        "id": "sec_directions",
        "title": "2. Các Hướng Giao tiếp trong Tổ chức",
        "selector": "#sec-directions",
        "en": "Section 2 investigates communication directions. We contrast one-way messages requiring no reply against two-way communication that invites active feedback. Channels move vertically—downward for directives, upward for reports—and horizontally across peers on equivalent tiers.",
        "vi": "Mục hai khảo sát các hướng giao tiếp trong tổ chức. Chúng ta phân biệt thông điệp một chiều không cần phản hồi với giao tiếp hai chiều đòi hỏi phản hồi tích cực. Luồng giao tiếp vận động theo chiều dọc – từ trên xuống cho các mệnh lệnh, từ dưới lên cho các báo cáo – và chiều ngang giữa các đồng nghiệp cùng cấp bậc."
    },
    {
        "id": "card_direction_flow",
        "title": "↕️ Giao tiếp Một chiều, Hai chiều, Dọc (Xuống/Lên) & Chiều ngang",
        "selector": "#card-direction-flow",
        "en": "Communication direction follows operational hierarchy: One-way communication issues instructions without feedback; Two-way communication encourages feedback and elevates motivation. Downward flows pass orders from managers to subordinates; Upward flows convey feedback and grievances; Horizontal flows coordinate peers on equal tiers.",
        "vi": "Hướng giao tiếp tuân theo cấp bậc tổ chức: Giao tiếp một chiều đưa ra mệnh lệnh không cần phản hồi; Giao tiếp hai chiều khuyến khích lắng nghe phản hồi giúp tạo động lực. Giao tiếp từ trên xuống truyền đạt chỉ thị của quản lý; Giao tiếp từ dưới lên phản ánh tâm tư nguyện vọng của nhân viên; và Giao tiếp ngang giúp phối hợp nhịp nhàng giữa các đồng nghiệp cùng cấp."
    },
    {
        "id": "sec_comm_methods",
        "title": "3. Các Phương thức Giao tiếp",
        "selector": "#sec-comm-methods",
        "en": "Section 3 evaluates three primary media: Verbal, Written, and Visual. Choosing the best method depends on speed required, cost, need for a permanent legal record, confidentiality, and whether two-way feedback is needed.",
        "vi": "Mục ba đánh giá ba phương thức truyền tải chủ đạo: Lời nói, Văn bản và Trực quan. Việc lựa chọn phương thức tối ưu phụ thuộc vào tốc độ, chi phí, yêu cầu lưu hồ sơ pháp lý, tính bảo mật và nhu cầu nhận phản hồi hai chiều."
    },
    {
        "id": "card_verbal_methods",
        "title": "🗣️ Phương thức Bằng lời nói (Verbal Communication)",
        "selector": "#card-verbal-methods",
        "en": "Verbal communication includes phone calls, face-to-face meetings, and video conferences. It offers immediate feedback, interactive persuasion, and personal warmth, but lacks permanent legal records and takes time when disputes arise.",
        "vi": "Phương thức bằng lời nói bao gồm gọi điện thoại, gặp mặt trực tiếp và họp trực tuyến. Ưu điểm là nhận phản hồi tức thì, tăng tính thuyết phục qua ngữ điệu và biểu cảm, nhưng không lưu lại bằng chứng văn bản lâu dài và mất thời gian nếu phát sinh tranh luận kéo dài."
    },
    {
        "id": "card_written_methods",
        "title": "📝 Phương thức Bằng văn bản (Written Communication)",
        "selector": "#card-written-methods",
        "en": "Written methods include emails, formal reports, letters, and notices. They provide durable legal documentation and accurately communicate intricate technical data, but eliminate spontaneous feedback and risk being overlooked in crowded inboxes.",
        "vi": "Phương thức văn bản gồm email, báo cáo tài chính, thư từ và bảng thông báo. Điểm mạnh là lưu giữ hồ sơ pháp lý lâu dài và truyền đạt dữ liệu kỹ thuật phức tạp, nhưng không có phản hồi tức thời và dễ bị nhân viên bỏ sót trong hòm thư điện tử."
    },
    {
        "id": "card_visual_methods",
        "title": "📊 Phương thức Trực quan & Giao tiếp Chính thức/Không chính thức",
        "selector": "#card-visual-methods",
        "en": "Visual methods utilize charts, diagrams, and video demonstrations to present complex trends clearly. Organizations also manage formal communication channels for verified business reporting alongside the informal 'grapevine' network used by leaders to gauge workplace sentiment.",
        "vi": "Phương thức trực quan sử dụng biểu đồ, sơ đồ và video minh họa để làm rõ các xu hướng phức tạp một cách sinh động. Doanh nghiệp cũng đồng thời vận hành các kênh giao tiếp chính thức phục vụ báo cáo pháp lý cùng mạng lưới phi chính thức (grapevine) giúp ban quản trị nắm bắt tâm tư ngầm của nhân viên."
    },
    {
        "id": "sec_comm_barriers",
        "title": "4. Rào cản Giao tiếp và Cách khắc phục",
        "selector": "#sec-comm-barriers",
        "en": "Section 4 classifies communication barriers into sender problems (technical jargon, unclear articulation), medium failures (lost mail, breakdown of IT servers), receiver obstacles (poor listening, lack of trust), and feedback breakdowns. Managers must overcome barriers by simplifying language, insisting on feedback, and shortening communication channels.",
        "vi": "Mục bốn phân loại rào cản giao tiếp thành các nhóm lỗi người gửi (dùng thuật ngữ khó hiểu, diễn đạt ấp úng), lỗi phương tiện truyền tải (thư thất lạc, hỏng máy chủ IT), rào cản người nhận (thiếu tập trung, thiếu sự tin tưởng) và lỗi do thiếu phản hồi. Nhà quản trị khắc phục rào cản bằng cách đơn giản hóa ngôn từ, yêu cầu xác nhận phản hồi và rút ngắn các kênh truyền tin."
    },
    {
        "id": "sec_recommend_comm",
        "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất phương thức giao tiếp",
        "selector": "#sec-recommend-comm",
        "en": "Section 5 demonstrates Cambridge examination technique for recommending communication media. Match business needs across scenarios: disciplinary warnings require confidential meetings followed by formal letters; safety emergencies need instant tannoy broadcasts; complex finance requires written reports; and design brainstorming thrives in face-to-face meetings.",
        "vi": "Mục năm hướng dẫn chiến lược thi Cambridge khi đề xuất phương thức giao tiếp phù hợp. Gắn nhu cầu với từng kịch bản: kỷ luật nhân viên cần đối thoại trực tiếp kèm thư chính thức; khẩn cấp an toàn cần loa phát thanh tức thì; báo cáo tài chính cần văn bản gửi kèm; và thảo luận sáng tạo cần họp trực tiếp."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_effective_comm": {"start": 1, "end": 3},
    "sec_directions": {"start": 4, "end": 5},
    "sec_comm_methods": {"start": 6, "end": 9},
    "sec_comm_barriers": {"start": 10, "end": 10},
    "sec_recommend_comm": {"start": 11, "end": 11}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.4 Internal and External Communication (Giao tiếp Nội bộ &amp; Bên ngoài)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. EFFECTIVE COMMUNICATION -->
    <div style="margin-bottom: 45px;">
        <div id="sec-effective-comm" class="lecture-interactive-card" data-lecture-section="sec_effective_comm" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🗣️ 1. EFFECTIVE COMMUNICATION</h2>
            <div style="background: #eff6ff; border-left: 5px solid #3b82f6; padding: 14px 18px; border-radius: 8px; font-size: 15.5px; color: #1e40af; line-height: 1.6;">
                <b>Communication</b> is the transferring of a message from the sender to the receiver, who accurately understands the message.
            </div>
        </div>

        <div id="card-comm-elements" class="lecture-interactive-card" data-lecture-section="card_comm_elements" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; margin-bottom: 20px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">⚙️ The 4 Elements of Effective Communication</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center; background: #f8fafc; padding: 18px; border-radius: 10px; border: 1px solid #e2e8f0; font-weight: bold; color: #334155;">
                <span style="background: #dbeafe; color: #1e40af; padding: 8px 16px; border-radius: 20px; font-size: 14px;">1. Sender (Originator)</span> ➔
                <span style="background: #fef3c7; color: #92400e; padding: 8px 16px; border-radius: 20px; font-size: 14px;">2. Medium (Channel)</span> ➔
                <span style="background: #dcfce7; color: #166534; padding: 8px 16px; border-radius: 20px; font-size: 14px;">3. Receiver (Recipient)</span> ➔
                <span style="background: #f3e8ff; color: #6b21a8; padding: 8px 16px; border-radius: 20px; font-size: 14px;">4. Feedback / Response</span>
            </div>
        </div>

        <div id="card-internal-vs-external" class="lecture-interactive-card" data-lecture-section="card_internal_vs_external" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🏢 Internal vs External Communication</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15px;">🏢 Internal Communication:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Between members of the <b>same organization</b>. <br/><i>(e.g., inter-departmental notices, staff meetings, factory safety signboards).</i></p>
                </div>
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 16px;">
                    <b style="color: #1d4ed8; font-size: 15px;">🌍 External Communication:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Between the organization and <b>outside parties</b>. <br/><i>(e.g., purchase orders to suppliers, advertising to customers, tax filings to governments).</i></p>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. DIRECTIONS OF COMMUNICATION -->
    <div style="margin-bottom: 45px;">
        <div id="sec-directions" class="lecture-interactive-card" data-lecture-section="sec_directions" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🧭 2. DIRECTIONS OF COMMUNICATION</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 16px;">
                    <b style="color: #d97706; font-size: 15px;">➡️ One-way communication:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #92400e;">Message does not require feedback (e.g. 'No Smoking' signs, emergency evacuation instructions).</p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15px;">🔄 Two-way communication:</b>
                    <p style="margin: 5px 0 0 0; font-size: 13.5px; color: #166534;">Receiver gives a response. Confirms understanding and motivates workers by making them feel involved.</p>
                </div>
            </div>
        </div>

        <div id="card-direction-flow" class="lecture-interactive-card" data-lecture-section="card_direction_flow" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">↕️ Vertical and Horizontal Channels</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 24px; margin-bottom: 4px;">⬇️</div>
                    <b style="color: #334155; font-size: 15px;">Downward Flow</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Directives and operational goals from managers down to shopfloor subordinates.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 24px; margin-bottom: 4px;">⬆️</div>
                    <b style="color: #334155; font-size: 15px;">Upward Flow</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Reports, questions, grievances, and feedback from employees up to managers.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <div style="font-size: 24px; margin-bottom: 4px;">↔️</div>
                    <b style="color: #334155; font-size: 15px;">Horizontal Flow</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Cross-functional coordination between managers/peers on the same hierarchical level.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. COMMUNICATION METHODS -->
    <div style="margin-bottom: 45px;">
        <div id="sec-comm-methods" class="lecture-interactive-card" data-lecture-section="sec_comm_methods" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📲 3. COMMUNICATION METHODS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Enterprises select media based on speed, cost, confidentiality, need for permanent record, and receiver characteristics:
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
            <div id="card-verbal-methods" class="lecture-interactive-card" data-lecture-section="card_verbal_methods" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-top: 4px solid #be185d; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <b style="color: #be185d; font-size: 16px;">🗣️ Verbal Methods</b>
                <p style="margin: 4px 0 10px 0; font-size: 12.5px; color: #64748b;">Phone calls, face-to-face, video meetings.</p>
                <div style="font-size: 13px; line-height: 1.5;">
                    <b style="color: #16a34a;">✅ Pros:</b> Immediate feedback; personal body language reinforcement.<br/>
                    <b style="color: #dc2626;">❌ Cons:</b> Time-consuming debates; no permanent legal record.
                </div>
            </div>

            <div id="card-written-methods" class="lecture-interactive-card" data-lecture-section="card_written_methods" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-top: 4px solid #2563eb; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <b style="color: #2563eb; font-size: 16px;">📝 Written Methods</b>
                <p style="margin: 4px 0 10px 0; font-size: 12.5px; color: #64748b;">Letters, memos, emails, contracts, reports.</p>
                <div style="font-size: 13px; line-height: 1.5;">
                    <b style="color: #16a34a;">✅ Pros:</b> Permanent legal evidence; accurately conveys complex technical data.<br/>
                    <b style="color: #dc2626;">❌ Cons:</b> No immediate feedback; risk of messages being overlooked.
                </div>
            </div>

            <div id="card-visual-methods" class="lecture-interactive-card" data-lecture-section="card_visual_methods" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-top: 4px solid #d97706; border-radius: 12px; padding: 18px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                <b style="color: #d97706; font-size: 16px;">📊 Visual &amp; Networks</b>
                <p style="margin: 4px 0 10px 0; font-size: 12.5px; color: #64748b;">Charts, diagrams, slides &amp; Formal / Informal channels.</p>
                <div style="font-size: 13px; line-height: 1.5;">
                    <b style="color: #16a34a;">✅ Pros:</b> Highly engaging visual appeal; grapevine tests informal staff mood.<br/>
                    <b style="color: #dc2626;">❌ Cons:</b> Can be misread; informal gossip can spread damaging falsehoods.
                </div>
            </div>
        </div>
    </div>

    <!-- 4. COMMUNICATION BARRIERS -->
    <div id="sec-comm-barriers" class="lecture-interactive-card" data-lecture-section="sec_comm_barriers" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #ef4444; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🚧 4. COMMUNICATION BARRIERS &amp; SOLUTIONS</h2>
        <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 13.5px; text-align: left;">
                <thead>
                    <tr style="background: #f1f5f9; color: #0f172a; border-bottom: 2px solid #cbd5e1;">
                        <th style="padding: 10px 12px; width: 22%;">Barrier Category</th>
                        <th style="padding: 10px 12px; width: 43%;">Common Cause</th>
                        <th style="padding: 10px 12px; width: 35%;">Management Solution</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: bold; color: #dc2626; background: #fef2f2;">Sender Problems</td>
                        <td style="padding: 10px 12px;">Technical jargon, speaking too rapidly, or messages too lengthy.</td>
                        <td style="padding: 10px 12px; color: #15803d;">Use concise, simple terminology and request verification.</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: bold; color: #d97706; background: #fffbeb;">Medium Problems</td>
                        <td style="padding: 10px 12px;">IT server failure, lost mail, or overlong chain of command distortion.</td>
                        <td style="padding: 10px 12px; color: #15803d;">Shorten communication channels and establish backup channels.</td>
                    </tr>
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 10px 12px; font-weight: bold; color: #2563eb; background: #eff6ff;">Receiver Problems</td>
                        <td style="padding: 10px 12px;">Inattention, distraction, or mistrust of the sender's motives.</td>
                        <td style="padding: 10px 12px; color: #15803d;">Emphasize message importance and cultivate mutual trust.</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 12px; font-weight: bold; color: #7c3aed; background: #faf5ff;">Feedback Problems</td>
                        <td style="padding: 10px 12px;">Feedback is absent, received too late, or distorted via intermediaries.</td>
                        <td style="padding: 10px 12px; color: #15803d;">Provide direct two-way channels allowing immediate questions.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 5. RECOMMEND AND JUSTIFY (CAMBRIDGE EXAM STRATEGY) -->
    <div id="sec-recommend-comm" class="lecture-interactive-card" data-lecture-section="sec_recommend_comm" style="margin-bottom: 45px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
        <h2 style="color: #1e3a8a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; font-size: 22px; margin-top: 0; display: inline-block;">
            🎯 5. HOW TO RECOMMEND &amp; JUSTIFY A COMMUNICATION METHOD (Cambridge Exam Strategy)
        </h2>
        <p style="font-size: 15px; color: #1e40af; margin-bottom: 16px; line-height: 1.6;">
            Paper 1 &amp; 2 exam questions require matching methods to precise operational situations:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 16px;">
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                <b style="color: #1e40af; font-size: 14.5px;">Disciplinary Warning:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">Confidential one-to-one interview (empathy, feedback) followed by a formal letter (legal permanent record).</p>
            </div>
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #ef4444;">
                <b style="color: #dc2626; font-size: 14.5px;">Safety Emergency:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">Tannoy loudspeaker or instant push alert where transmission speed overrides all other factors.</p>
            </div>
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <b style="color: #b45309; font-size: 14.5px;">Complex Financials:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">Detailed written report with charts; data is too complex to be remembered orally and requires study.</p>
            </div>
            <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #10b981;">
                <b style="color: #047857; font-size: 14.5px;">Creative Brainstorming:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">Interactive face-to-face meeting enabling spontaneous idea generation, sketching, and instant consensus.</p>
            </div>
        </div>
        <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
            <b style="color: #1e40af; font-size: 14px;">💡 Cambridge 5 Decision Factors:</b>
            <p style="margin: 4px 0 0 0; font-size: 13px; color: #334155;">1. Speed | 2. Cost | 3. Need for written record | 4. Confidentiality | 5. Requirement for two-way feedback.</p>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">2.4 Internal and External Communication (Giao tiếp Nội bộ &amp; Bên ngoài)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 2.4 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/2_4_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 2.4 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
