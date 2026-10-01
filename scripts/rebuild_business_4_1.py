import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 4.1 ID
LID = '1e280547-ce64-44c2-8fcf-997f7d61cacf'
CODE = '4_1'
TITLE = '4.1. Production of goods and services'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 12 AUDIO SEGMENTS FOR LESSON 4.1
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.1: Sản xuất Hàng hóa và Dịch vụ",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.1: Production of Goods and Services. In this opening chapter of Topic 4, Operations Management, we explore productivity metrics, inventory control, lean production techniques, job, batch, and flow production methods, and modern manufacturing automation.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.1: Sản xuất Hàng hóa và Dịch vụ. Trong bài mở đầu của Chủ đề bốn về Quản trị Vận hành, chúng ta sẽ khảo sát các chỉ số đo lường năng suất, quản lý hàng tồn kho, phương pháp sản xuất tinh gọn (lean), các hình thức sản xuất đơn chiếc, theo lô, liên tục và tự động hóa nhà máy."
    },
    {
        "id": "sec_production_productivity",
        "title": "1. Sản xuất và Năng suất lao động",
        "selector": "#sec-production-productivity",
        "en": "Section 1 distinguishes production—the absolute volume of output produced—from productivity, which measures output per unit of input over time. Boosting labour productivity drives down average unit costs, enhancing price competitiveness and widening profit margins.",
        "vi": "Mục một phân biệt giữa sản lượng sản xuất (production) – tổng số lượng hàng hóa tạo ra – với năng suất (productivity), là sản lượng tính trên một đơn vị đầu vào theo thời gian. Nâng cao năng suất lao động giúp kéo giảm chi phí sản xuất trên mỗi đơn vị sản phẩm, gia tăng năng lực cạnh tranh về giá và mở rộng biên lợi nhuận."
    },
    {
        "id": "card_productivity",
        "title": "📈 Công thức tính Năng suất & Giải pháp nâng cao",
        "selector": "#card-productivity",
        "en": "Productivity equals Total Output divided by Total Inputs such as labour hours or capital machines. Ways to increase productivity include: upgrading employee training, modernizing machinery, automating repetitive tasks, and motivating staff through productivity-linked incentives.",
        "vi": "Năng suất được tính bằng Tổng sản lượng đầu ra chia cho Tổng đầu vào như giờ công lao động hoặc số máy móc. Các giải pháp nâng cao năng suất gồm: đào tạo chuyên môn cho công nhân, hiện đại hóa máy móc thiết bị, tự động hóa các khâu lặp đi lặp lại và khuyến khích tài chính gắn liền với năng suất."
    },
    {
        "id": "sec_inventory",
        "title": "2. Quản lý Hàng tồn kho (Inventory Management)",
        "selector": "#sec-inventory",
        "en": "Section 2 investigates inventory management: raw materials, work-in-progress, and finished goods. Holding buffer inventories ensures smooth operations against delivery delays but locks up working capital in storage, insurance, and obsolescence risks.",
        "vi": "Mục hai nghiên cứu quản trị hàng tồn kho: nguyên vật liệu thô, sản phẩm dở dang trên dây chuyền và thành phẩm hoàn chỉnh. Duy trì lượng hàng dự trữ giúp sản xuất liên tục không bị gián đoạn nhưng gây ứ đọng vốn lưu động, tốn chi phí thuê kho bãi, bảo hiểm và đối mặt rủi ro hàng hóa lỗi thời."
    },
    {
        "id": "card_inventory_control",
        "title": "📦 Biểu đồ Kiểm soát Tồn kho: Reorder Level, Lead Time & Buffer Stock",
        "selector": "#card-inventory-control",
        "en": "The inventory control chart tracks stock levels over time. The Maximum Inventory Level represents warehouse capacity; the Reorder Level triggers purchase requisitions before stock runs out; Lead Time measures delivery duration; and Buffer Inventory protects the firm from unexpected demand spikes or supplier stock-outs.",
        "vi": "Biểu đồ kiểm soát tồn kho theo dõi lượng hàng theo thời gian. Mức tồn kho tối đa thể hiện sức chứa của kho; Điểm đặt hàng lại (Reorder Level) kích hoạt đơn mua hàng mới trước khi hết hàng; Thời gian chờ hàng (Lead Time) là khoảng thời gian từ khi đặt đến khi hàng về; và Lượng tồn kho an toàn (Buffer Inventory) bảo vệ doanh nghiệp trước những biến động đột xuất của thị trường."
    },
    {
        "id": "sec_lean_production",
        "title": "3. Sản xuất Tinh gọn & 7 Loại Lãng phí (Lean Production)",
        "selector": "#sec-lean-production",
        "en": "Section 3 explores Lean Production: operational philosophies aimed at cutting waste and eliminating non-value-adding activities across seven dimensions: overproduction, waiting, transportation, unnecessary inventory, excessive motion, overprocessing, and defects.",
        "vi": "Mục ba tìm hiểu Sản xuất tinh gọn (Lean Production): triết lý vận hành nhằm cắt giảm lãng phí và loại bỏ các hoạt động không tạo ra giá trị gia tăng trên bảy khía cạnh: sản xuất thừa, thời gian chờ đợi, vận chuyển không cần thiết, tồn kho dư thừa, thao tác thừa, xử lý quá mức và hàng lỗi hỏng."
    },
    {
        "id": "card_lean_methods",
        "title": "✨ Các Kỹ thuật Lean cốt lõi: JIT, Kaizen & Cell Production",
        "selector": "#card-lean-methods",
        "en": "Key lean techniques include Just-In-Time (JIT)—where materials arrive exactly as required on the assembly line, eliminating warehouse storage entirely; Kaizen, continuous incremental improvement driven by frontline employee feedback; and Cell Production, organizing workers into autonomous quality units.",
        "vi": "Các kỹ thuật tinh gọn cốt lõi gồm Sản xuất đúng thời điểm (Just-In-Time - JIT) – nguyên vật liệu được giao đúng lúc cần ráp vào dây chuyền, xóa bỏ hoàn toàn chi phí lưu kho; Kaizen, triết lý cải tiến liên tục từng bước nhỏ dựa trên sáng kiến của công nhân; và Sản xuất theo ô (Cell Production), chia nhỏ dây chuyền thành các tổ độc lập nâng cao tinh thần trách nhiệm."
    },
    {
        "id": "sec_methods_production",
        "title": "4. Ba Phương pháp Sản xuất: Job, Batch và Flow",
        "selector": "#sec-methods-production",
        "en": "Section 4 compares three core manufacturing methods: Job production crafts single customized items like wedding dresses; Batch production creates identical groups of products before resetting equipment, as in bakeries; Flow continuous mass production runs non-stop assembly lines like car factories, yielding massive economies of scale.",
        "vi": "Mục bốn so sánh ba phương pháp sản xuất: Sản xuất đơn chiếc (Job) làm theo yêu cầu cá nhân hóa như may váy cưới; Sản xuất theo lô (Batch) tạo ra từng mẻ sản phẩm giống nhau trước khi chuyển đổi máy móc như tiệm bánh; Sản xuất liên tục (Flow) vận hành dây chuyền tự động hàng loạt 24/7 như lắp ráp ô tô, đạt hiệu quả quy mô tối đa."
    },
    {
        "id": "card_production_methods",
        "title": "⚙️ So sánh Job, Batch, Flow & Yếu tố Lựa chọn",
        "selector": "#card-production-methods",
        "en": "Job production crafts bespoke individual products with high worker motivation but at high unit labour costs. Batch production manufactures identical product groups with flexible equipment changeovers. Flow continuous production achieves unmatched mass volume and lowest average unit costs through automated lines, but requires substantial capital setup and reduces worker morale.",
        "vi": "Sản xuất đơn chiếc (Job) tạo ra sản phẩm cá nhân hóa theo yêu cầu với tinh thần làm việc của thợ cao nhưng chi phí nhân công trên mỗi sản phẩm lớn. Sản xuất theo lô (Batch) tạo ra từng đợt sản phẩm giống nhau với khả năng linh hoạt chuyển đổi mẫu mã. Sản xuất liên tục (Flow) đạt sản lượng đại trà khổng lồ và chi phí đơn vị thấp nhất nhờ tự động hóa, nhưng đòi hỏi vốn đầu tư lớn và dễ gây nhàm chán cho công nhân."
    },
    {
        "id": "sec_tech_production",
        "title": "5. Công nghệ trong Sản xuất: CAD, CAM và CIM",
        "selector": "#sec-tech-production",
        "en": "Section 5 evaluates technological innovation: Computer-Aided Design (CAD) for digital prototyping; Computer-Aided Manufacturing (CAM) utilizing industrial robots; and Computer-Integrated Manufacturing (CIM) unifying entire factories under integrated software controllers.",
        "vi": "Mục năm đánh giá sự đổi mới công nghệ: Thiết kế có sự trợ giúp của máy tính (CAD) giúp phác thảo mẫu kỹ thuật số 3D; Sản xuất có sự trợ giúp của máy tính (CAM) sử dụng robot công nghiệp; và Sản xuất tích hợp máy tính (CIM) đồng bộ hóa toàn bộ nhà máy dưới sự điều khiển của hệ thống phần mềm trung tâm."
    },
    {
        "id": "card_tech_methods",
        "title": "💻 Ứng dụng Công nghệ (CAD, CAM, CIM, EPOS) & Ưu nhược điểm",
        "selector": "#card-tech-methods",
        "en": "Modern manufacturing incorporates CAD software for digital styling, CAM robotics for automated assembly, CIM networks for factory-wide digital synchronization, and EPOS scanners for real-time inventory decrement. Technology improves precision and slashes operating waste, but carries steep capital costs and employee redundancy risks.",
        "vi": "Sản xuất hiện đại tích hợp phần mềm thiết kế CAD, robot sản xuất CAM, mạng lưới tích hợp CIM đồng bộ toàn xưởng và máy quét mã vạch EPOS để tự động trừ kho theo thời gian thực. Công nghệ nâng cao độ chuẩn xác và triệt tiêu lãng phí, nhưng đòi hỏi vốn đầu tư lớn và tiềm ẩn nguy cơ dư thừa lao động."
    },
    {
        "id": "sec_recommend_production",
        "title": "6. Chiến lược làm bài thi Cambridge: Đề xuất Phương pháp Sản xuất",
        "selector": "#sec-recommend-production",
        "en": "Section 6 details the Cambridge evaluation strategy for production methods. Candidates must analyze market demand volume, product customization requirements, and capital budget before justifying the optimal manufacturing method.",
        "vi": "Mục sáu hướng dẫn chiến lược trả lời câu hỏi Cambridge về phương pháp sản xuất. Thí sinh phải phân tích quy mô nhu cầu thị trường, mức độ tùy biến sản phẩm theo yêu cầu khách hàng và ngân sách đầu tư thiết bị trước khi đưa ra khuyến nghị lựa chọn phương án tối ưu."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_production_productivity": {"start": 1, "end": 2},
    "sec_inventory": {"start": 3, "end": 4},
    "sec_lean_production": {"start": 5, "end": 6},
    "sec_methods_production": {"start": 7, "end": 8},
    "sec_tech_production": {"start": 9, "end": 10},
    "sec_recommend_production": {"start": 11, "end": 11}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.1 Production of Goods and Services (Sản xuất Hàng hóa &amp; Dịch vụ)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. PRODUCTION & PRODUCTIVITY -->
    <div style="margin-bottom: 50px;">
        <div id="sec-production-productivity" class="lecture-interactive-card" data-lecture-section="sec_production_productivity" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🏭 1. PRODUCTION &amp; PRODUCTIVITY</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 16px;">
                <b>Production</b> is the effective management of resources in producing goods and services. The <b>Operations Department</b> overlooks this process.
            </div>
            <h4 style="color: #0f172a; font-size: 16px; margin: 0 0 8px 0;">🎯 Roles of the Operations Department:</h4>
            <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 13.5px; line-height: 1.6;">
                <li>Use resources in a cost-effective and efficient manner.</li>
                <li>Manage inventory effectively to satisfy orders without excessive stockholding.</li>
                <li>Produce the required output to meet consumer demands.</li>
                <li>Meet the quality standards expected by customers.</li>
            </ul>
        </div>

        <!-- SUB-CARD: PRODUCTIVITY -->
        <div id="card-productivity" class="lecture-interactive-card" data-lecture-section="card_productivity" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">📈 Productivity &amp; How to Increase It</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14px; color: #475569; margin-bottom: 16px;">Productivity is a <b>measure of the efficiency</b> of inputs used in the production process over a period of time.</p>

            <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 20px;">
                <div style="flex: 1; min-width: 240px; background: #f8fafc; border: 1.5px dashed #94a3b8; padding: 16px; border-radius: 8px; text-align: center;">
                    <b style="color: #334155; font-size: 15px;">General Productivity</b>
                    <div style="margin-top: 8px; font-size: 16px; color: #2563eb; font-weight: bold;">
                        <span style="border-bottom: 2px solid #2563eb; padding-bottom: 2px;">Total Output</span><br>
                        <span style="padding-top: 2px; display: inline-block;">Total Input</span>
                    </div>
                </div>
                <div style="flex: 1; min-width: 240px; background: #f8fafc; border: 1.5px dashed #94a3b8; padding: 16px; border-radius: 8px; text-align: center;">
                    <b style="color: #334155; font-size: 15px;">Labour Productivity</b>
                    <div style="margin-top: 8px; font-size: 16px; color: #059669; font-weight: bold;">
                        <span style="border-bottom: 2px solid #059669; padding-bottom: 2px;">Total Output</span><br>
                        <span style="padding-top: 2px; display: inline-block;">Number of Employees</span>
                    </div>
                </div>
            </div>

            <div style="background: #f0fdf4; border-left: 4px solid #10b981; padding: 15px 18px; border-radius: 4px;">
                <h4 style="margin: 0 0 8px 0; color: #047857; font-size: 15px;">💡 Ways to increase productivity:</h4>
                <ul style="margin: 0; padding-left: 18px; color: #065f46; font-size: 13px; line-height: 1.6;">
                    <li><b>Training:</b> Improving worker skills so they work faster and waste less materials.</li>
                    <li><b>Automation:</b> Using machinery and IT so production is faster, continuous, and error-free.</li>
                    <li><b>Motivation:</b> Incentive compensation structures increase employee willingness to work efficiently.</li>
                    <li><b>Quality Control:</b> Robust operational systems prevent costly scrap rework.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 2. INVENTORY MANAGEMENT -->
    <div style="margin-bottom: 50px;">
        <div id="sec-inventory" class="lecture-interactive-card" data-lecture-section="sec_inventory" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📦 2. INVENTORY MANAGEMENT</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Firms hold inventory (stock) of raw materials, work-in-progress, and finished goods to fulfill unexpected rises in demand and buffer against supplier delivery interruptions.
            </p>
        </div>

        <!-- SUB-CARD: INVENTORY CONTROL -->
        <div id="card-inventory-control" class="lecture-interactive-card" data-lecture-section="card_inventory_control" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">📦 Inventory Control Graph: Reorder Level, Lead Time &amp; Buffer Stock</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="margin-bottom: 20px; overflow-x: auto; padding-top: 6px;">
                <svg viewBox="0 0 600 320" width="100%" style="min-width: 500px; background:#ffffff; border-radius:12px; border:1px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: block; margin: 0 auto; font-family: Arial, sans-serif;">
                    <line x1="60" y1="280" x2="560" y2="280" stroke="#334155" stroke-width="2"></line>
                    <line x1="60" y1="20" x2="60" y2="280" stroke="#334155" stroke-width="2"></line>
                    <text x="310" y="315" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Time</text>
                    <text x="25" y="150" transform="rotate(-90 25,150)" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Inventory Level</text>

                    <line x1="60" y1="50" x2="560" y2="50" stroke="#10b981" stroke-dasharray="5,5" stroke-width="2"></line>
                    <text x="70" y="40" font-size="13" font-weight="bold" fill="#059669">Maximum Inventory Level</text>

                    <line x1="60" y1="150" x2="560" y2="150" stroke="#f59e0b" stroke-dasharray="5,5" stroke-width="2"></line>
                    <text x="70" y="140" font-size="13" font-weight="bold" fill="#d97706">Reorder Level</text>

                    <line x1="60" y1="230" x2="560" y2="230" stroke="#ef4444" stroke-dasharray="5,5" stroke-width="2"></line>
                    <text x="70" y="220" font-size="13" font-weight="bold" fill="#dc2626">Buffer Inventory (Minimum)</text>

                    <path d="M 60 50 L 160 230 L 160 50" fill="none" stroke="#2563eb" stroke-width="3"></path>
                    <path d="M 160 50 L 260 230 L 260 50" fill="none" stroke="#2563eb" stroke-width="3"></path>
                    <path d="M 260 50 L 360 230 L 360 50" fill="none" stroke="#2563eb" stroke-width="3"></path>
                    <path d="M 360 50 L 460 230 L 460 50" fill="none" stroke="#2563eb" stroke-width="3"></path>

                    <circle cx="204" cy="150" r="5" fill="#f59e0b"></circle>
                    <line x1="204" y1="150" x2="204" y2="280" stroke="#64748b" stroke-dasharray="3,3"></line>

                    <circle cx="260" cy="230" r="5" fill="#ef4444"></circle>
                    <line x1="260" y1="230" x2="260" y2="280" stroke="#64748b" stroke-dasharray="3,3"></line>

                    <path d="M 204 265 L 260 265" stroke="#334155" stroke-width="2" fill="none"></path>
                    <polygon points="260,265 255,260 255,270" fill="#334155"></polygon>
                    <polygon points="204,265 209,260 209,270" fill="#334155"></polygon>
                    <text x="232" y="255" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">Lead Time</text>
                </svg>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 14px;">
                <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 14px; border-radius: 8px;">
                    <h4 style="color: #d97706; margin: 0 0 4px 0; font-size: 15px;">🔔 Reorder Level</h4>
                    <p style="margin: 0; font-size: 13px; color: #92400e;">The stock count that triggers a reorder so goods arrive just before stocks dip below buffer.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 14px; border-radius: 8px;">
                    <h4 style="color: #334155; margin: 0 0 4px 0; font-size: 15px;">⏳ Lead Time</h4>
                    <p style="margin: 0; font-size: 13px; color: #475569;">The delivery duration between placing the purchase order and receiving physical stock at the factory.</p>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 14px; border-radius: 8px;">
                    <h4 style="color: #dc2626; margin: 0 0 4px 0; font-size: 15px;">🛡️ Buffer Inventory</h4>
                    <p style="margin: 0; font-size: 13px; color: #7f1d1d;">The safety margin held to satisfy unexpected demand bursts or compensate for supplier delays.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. LEAN PRODUCTION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-lean-production" class="lecture-interactive-card" data-lecture-section="sec_lean_production" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🚀 3. LEAN PRODUCTION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0 0 14px 0; line-height: 1.6;">
                Techniques a firm adopts to reduce wastage and increase efficiency across seven classic waste categories:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 8px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">1. Overproduction:</b> Producing unsought goods.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">2. Waiting:</b> Line delays between operations.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">3. Transportation:</b> Unneeded transit of materials.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">4. Inventory:</b> Excess holding ties up funds.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">5. Motion:</b> Wasted worker ergonomics.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">6. Over-processing:</b> Unnecessary complex specs.</div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 6px; font-size: 12.5px;"><b style="color: #dc2626;">7. Defects:</b> Faulty items requiring scrap.</div>
            </div>
        </div>

        <!-- SUB-CARD: LEAN METHODS -->
        <div id="card-lean-methods" class="lecture-interactive-card" data-lecture-section="card_lean_methods" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #6d28d9; font-weight: 700;">✨ Methods of Lean: Kaizen, JIT &amp; Cell Production</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>

            <!-- Kaizen block -->
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; margin-bottom: 16px;">
                <h4 style="margin: 0 0 6px 0; color: #7c3aed; font-size: 16px;">🔄 Kaizen (Continuous Improvement)</h4>
                <p style="margin: 0 0 12px 0; font-size: 13px; color: #475569;">Frontline staff meet regularly in small quality circles to streamline equipment layout into U-shaped cell production lines.</p>
                <div style="text-align: center;">
                    <svg viewBox="0 0 600 180" width="100%" style="max-width: 580px; background:#ffffff; border-radius:8px; border:1px dashed #cbd5e1; font-family: Arial, sans-serif;">
                        <text x="140" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">Before Kaizen (Chaotic)</text>
                        <rect x="40" y="45" width="35" height="35" fill="#cbd5e1" rx="4"></rect>
                        <rect x="180" y="45" width="35" height="35" fill="#cbd5e1" rx="4"></rect>
                        <rect x="110" y="110" width="35" height="35" fill="#cbd5e1" rx="4"></rect>
                        <path d="M 75 62 L 180 62 M 195 80 L 145 125 M 110 125 L 60 80" stroke="#ef4444" stroke-width="2" fill="none"></path>

                        <line x1="280" y1="15" x2="280" y2="165" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"></line>

                        <text x="440" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">After Kaizen (U-Shape Cell)</text>
                        <rect x="340" y="55" width="35" height="35" fill="#6ee7b7" rx="4"></rect>
                        <rect x="420" y="55" width="35" height="35" fill="#6ee7b7" rx="4"></rect>
                        <rect x="500" y="55" width="35" height="35" fill="#6ee7b7" rx="4"></rect>
                        <rect x="340" y="115" width="35" height="35" fill="#6ee7b7" rx="4"></rect>
                        <rect x="420" y="115" width="35" height="35" fill="#6ee7b7" rx="4"></rect>
                        <rect x="500" y="115" width="35" height="35" fill="#6ee7b7" rx="4"></rect>

                        <path d="M 375 72 L 420 72 M 455 72 L 500 72 M 518 90 L 518 115 M 500 132 L 455 132 M 420 132 L 375 132" stroke="#10b981" stroke-width="2" fill="none"></path>
                    </svg>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <h4 style="margin: 0 0 6px 0; color: #7c3aed; font-size: 15px;">🚚 Just-in-Time (JIT)</h4>
                    <p style="margin: 0 0 8px 0; font-size: 13px; color: #475569;">Supplies arrive only when ordered for assembly. Zero warehouse storage.</p>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12px; line-height: 1.5;">
                        <li>Cuts inventory holding rent and insurance.</li>
                        <li>Prevents capital lock-up and perishable decay.</li>
                    </ul>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <h4 style="margin: 0 0 6px 0; color: #7c3aed; font-size: 15px;">🧩 Cell Production</h4>
                    <p style="margin: 0 0 8px 0; font-size: 13px; color: #475569;">Dividing assembly lines into self-managing multi-skilled teams.</p>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12px; line-height: 1.5;">
                        <li>Boosts worker morale through group autonomy.</li>
                        <li>Pinpoints quality defects to specific cell pods.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. METHODS OF PRODUCTION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-methods-production" class="lecture-interactive-card" data-lecture-section="sec_methods_production" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚙️ 4. METHODS OF PRODUCTION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Firms select from three principal production methods depending on customization, order volumes, capital assets, and market size.
            </p>
        </div>

        <!-- SUB-CARD: PRODUCTION METHODS -->
        <div id="card-production-methods" class="lecture-interactive-card" data-lecture-section="card_production_methods" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #db2777; font-weight: 700;">⚙️ Comparing Job, Batch, and Flow Production</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fdf2f8; color: #db2777; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 18px;">
                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
                    <div style="background: #f8fafc; padding: 12px; border-bottom: 1px solid #e2e8f0;">
                        <h4 style="margin: 0; color: #db2777; font-size: 16px;">✂️ Job Production</h4>
                        <p style="margin: 4px 0 0 0; font-size: 12px; color: #475569;">Bespoke single orders. <i>(e.g., designer gowns, luxury yachts).</i></p>
                    </div>
                    <div style="padding: 12px; font-size: 12px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Exact bespoke fit; high pride of work.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Expensive craftsman labour; slow speed.
                    </div>
                </div>

                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
                    <div style="background: #f8fafc; padding: 12px; border-bottom: 1px solid #e2e8f0;">
                        <h4 style="margin: 0; color: #db2777; font-size: 16px;">📦 Batch Production</h4>
                        <p style="margin: 4px 0 0 0; font-size: 12px; color: #475569;">Identical product sets. <i>(e.g., bakeries, shoe sizes).</i></p>
                    </div>
                    <div style="padding: 12px; font-size: 12px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Flexible switching; lowers unit cost vs job.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Downtime while retooling equipment.
                    </div>
                </div>

                <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; overflow: hidden;">
                    <div style="background: #f8fafc; padding: 12px; border-bottom: 1px solid #e2e8f0;">
                        <h4 style="margin: 0; color: #db2777; font-size: 16px;">🏭 Flow Production</h4>
                        <p style="margin: 4px 0 0 0; font-size: 12px; color: #475569;">Mass continuous 24/7 output. <i>(e.g., automotive lines).</i></p>
                    </div>
                    <div style="padding: 12px; font-size: 12px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Lowest unit cost via massive economies of scale.<br>
                        <b style="color: #dc2626;">❌ Cons:</b> Huge machinery cost; boring repetitive tasks.
                    </div>
                </div>
            </div>

            <div style="background: #fdf2f8; border-left: 4px solid #db2777; padding: 14px 18px; border-radius: 4px;">
                <h4 style="margin: 0 0 6px 0; color: #9d174d; font-size: 14px;">🤔 Factors governing selection:</h4>
                <ul style="margin: 0; padding-left: 18px; color: #831843; font-size: 12.5px; line-height: 1.5;">
                    <li><b>Product Customization:</b> Custom orders require Job; standard consumer goods require Flow.</li>
                    <li><b>Market Demand Volume:</b> Small niche = Job/Batch. Mass global market = Flow.</li>
                    <li><b>Capital Capability:</b> Small firms lack multi-million automated lines, utilizing Batch instead.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 5. TECHNOLOGY IN PRODUCTION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-tech-production" class="lecture-interactive-card" data-lecture-section="sec_tech_production" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💻 5. TECHNOLOGY IN PRODUCTION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Computerized operations transform manufacturing output, inventory reconciliation, and product precision.
            </p>
        </div>

        <!-- SUB-CARD: TECH APPLICATIONS -->
        <div id="card-tech-methods" class="lecture-interactive-card" data-lecture-section="card_tech_methods" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #99f6e4; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <h3 style="margin: 0; font-size: 18px; color: #0f766e; font-weight: 700;">💻 Technological Tools: CAD, CAM, CIM &amp; EPOS</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f0fdfa; color: #0f766e; padding: 4px 10px; border-radius: 6px; border: 1px solid #99f6e4;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-bottom: 18px;">
                <div style="background: #f0fdfa; border: 1px solid #ccfbf1; padding: 12px; border-radius: 8px;">
                    <b style="color: #0f766e; font-size: 13px;">🤖 Automation:</b>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #475569;">Equipment controlled fully by robotic programs.</p>
                </div>
                <div style="background: #f0fdfa; border: 1px solid #ccfbf1; padding: 12px; border-radius: 8px;">
                    <b style="color: #0f766e; font-size: 13px;">📐 CAD:</b>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #475569;">Computer Aided Design (3D modeling simulations).</p>
                </div>
                <div style="background: #f0fdfa; border: 1px solid #ccfbf1; padding: 12px; border-radius: 8px;">
                    <b style="color: #0f766e; font-size: 13px;">🏭 CAM:</b>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #475569;">Computer Aided Manufacturing (automated production).</p>
                </div>
                <div style="background: #f0fdfa; border: 1px solid #ccfbf1; padding: 12px; border-radius: 8px;">
                    <b style="color: #0f766e; font-size: 13px;">🔗 CIM:</b>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #475569;">Integrated CAD + CAM factory networks.</p>
                </div>
                <div style="background: #f0fdfa; border: 1px solid #ccfbf1; padding: 12px; border-radius: 8px;">
                    <b style="color: #0f766e; font-size: 13px;">🛒 EPOS:</b>
                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #475569;">Electronic Point of Sale automatic stock deduction.</p>
                </div>
            </div>

            <div style="display: flex; flex-wrap: wrap; gap: 14px;">
                <div style="flex: 1; min-width: 250px; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 8px;">
                    <h4 style="color: #15803d; margin: 0 0 6px 0; font-size: 14px;">✅ Advantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12px; line-height: 1.5;">
                        <li>Rapid, flawless production velocity.</li>
                        <li>Standardized quality reduces customer returns.</li>
                        <li>Automated stock reconciliation lowers administrative overhead.</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; background: #fef2f2; border: 1px solid #fecaca; padding: 14px; border-radius: 8px;">
                    <h4 style="color: #b91c1c; margin: 0 0 6px 0; font-size: 14px;">❌ Disadvantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12px; line-height: 1.5;">
                        <li>Massive capital outlay for hardware setup.</li>
                        <li>Redundancies and worker resistance to tech change.</li>
                        <li>Rapid obsolescence demands expensive recurring software upgrades.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 6. CAMBRIDGE EXAM EVALUATION (SUB-CARD / SECTION) -->
    <div style="margin-bottom: 50px;">
        <div id="sec-recommend-production" class="lecture-interactive-card" data-lecture-section="sec_recommend_production" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 6. HOW TO RECOMMEND &amp; JUSTIFY PRODUCTION METHODS (Cambridge Exam Strategy)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Paper 1 and Paper 2 frequently ask candidates: <i>"Recommend whether this business should switch from Batch to Flow production."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 18px;">
                <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                    <b style="color: #1e40af; font-size: 14px;">Recommend Job Production When:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        The product is unique, customized, and buyers willingly pay premium prices (bespoke fashion, artisan furnishings).
                    </p>
                </div>

                <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #10b981;">
                    <b style="color: #047857; font-size: 14px;">Recommend Batch Production When:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        Demand exists for distinct varieties (bakeries baking different breads; clothing firms making S, M, L sizes).
                    </p>
                </div>

                <div style="background: #ffffff; padding: 14px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                    <b style="color: #b45309; font-size: 14px;">Recommend Flow Production When:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        Massive, stable demand exists for uniform commodities (bottled beverages). Large initial capital is recouped through economies of scale.
                    </p>
                </div>
            </div>

            <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
                <b style="color: #1e40af; font-size: 14px;">💡 Cambridge Paper 2 Evaluation Nuance:</b>
                <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                    Switching to Flow production is only viable if the firm possesses <b>substantial capital reserves</b> for automated machinery, and <b>reliable supplier logistics (JIT)</b> so assembly lines never grind to an unplanned halt.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.1 Production of Goods &amp; Services (Sản xuất Hàng hóa &amp; Dịch vụ)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 4.1 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/4_1_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 4.1 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
