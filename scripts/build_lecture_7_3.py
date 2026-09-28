import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "7_3"
LECTURE_ID = "0b658b3f-bf70-4991-95d5-d65616b7ec1a"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "7.3 The Management of Urban Growth"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 7.3: Quản lý tăng trưởng đô thị",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 7.3: The Management of Urban Growth. In this lecture, we tackle sustainable urban development: resolving the brownfield versus greenfield debate, exploring the Egan Wheel framework, analyzing carrots and sticks in public transit, evaluating Shanghai's dual-core master plan, and examining policy interventions to combat Delhi's hazardous air quality crisis.",
        "vi": "Chào mừng các em đến với bài bảy chấm ba: Quản lý tăng trưởng đô thị. Trong bài học này, chúng ta sẽ tìm hiểu các giải pháp phát triển đô thị bền vững: giải quyết bài toán giữa khu đất nâu và khu đất xanh, khám phá khung mô hình Bánh xe Egan, phân tích chiến lược cây gậy và củ cà rốt trong giao thông công cộng, đánh giá quy hoạch tổng thể hai lõi của Thượng Hải, và khảo sát các chính sách can thiệp nhằm giảm thiểu ô nhiễm không khí nguy hại tại Delhi."
    },
    {
        "id": "sec_housing_brownfield",
        "title": "1. Nhà ở đô thị và Bài toán Đất nâu vs Đất xanh",
        "selector": "#sec-housing-brownfield",
        "en": "Section 1 addresses the critical planning dilemma between urban densification and outward expansion. Brownfield sites repurpose contaminated or derelict industrial lands inside the urban core, while greenfield sites develop untouched agricultural countryside at the urban fringe.",
        "vi": "Mục một giải quyết bài toán quy hoạch giữa tăng mật độ nội đô và mở rộng ra bên ngoài. Khu đất nâu tái sử dụng đất công nghiệp cũ bị bỏ hoang hoặc ô nhiễm trong lõi đô thị, trong khi khu đất xanh khai phá các vùng đồng ruộng nông thôn nguyên vẹn ở rìa thành phố."
    },
    {
        "id": "brownfield_greenfield_table",
        "title": "Bảng so sánh: Dự án Đất nâu vs Dự án Đất xanh",
        "selector": "#card-brownfield-greenfield-table",
        "en": "This table contrasts the two approaches: Brownfields preserve precious green belts and utilize existing roads and sewers, though they carry higher decontamination costs. Greenfields offer cheaper flat land with blank-slate architectural flexibility, but destroy farmland and lock in car dependence.",
        "vi": "Bảng này so sánh hai hướng tiếp cận: Đất nâu bảo vệ vành đai xanh và tận dụng đường xá cấp thoát nước sẵn có dù chi phí xử lý ô nhiễm cao hơn. Đất xanh có quỹ đất bằng phẳng giá rẻ với thiết kế linh hoạt, nhưng phá vỡ đất canh tác nông nghiệp và gây phụ thuộc vào xe ô tô cá nhân."
    },
    {
        "id": "sec_sustainable_cities",
        "title": "2. Các nguyên lý thành phố bền vững: Khung mô hình Bánh xe Egan",
        "selector": "#sec-sustainable-cities",
        "en": "Section 2 introduces the Egan Wheel framework for urban sustainability. A truly sustainable city balances environmental stewardship, economic viability, and social inclusion to meet current needs without compromising future generations.",
        "vi": "Mục hai giới thiệu khung mô hình Bánh xe Egan cho phát triển đô thị bền vững. Một thành phố thực sự bền vững phải cân bằng giữa bảo vệ môi trường sinh thái, tăng trưởng kinh tế bền vững và hòa nhập xã hội để phục vụ nhu cầu hôm nay mà không phương hại tới thế hệ mai sau."
    },
    {
        "id": "egan_wheel_svg",
        "title": "Sơ đồ tương tác: Ba trụ cột quản lý đô thị bền vững",
        "selector": "#card-egan-wheel-svg",
        "en": "This interactive diagram breaks down the three integrated pillars: Environmental protection through zero-waste circular loops, Social harmony via inclusive governance and affordable housing, and Economic vitality through green employment and efficient transit.",
        "vi": "Sơ đồ tương tác này phân tích ba trụ cột gắn kết: Bảo vệ môi trường qua mô hình tuần hoàn không rác thải, Hài hòa xã hội nhờ quản trị dung nạp và nhà ở vừa túi tiền, cùng Sức sống kinh tế từ việc làm xanh và giao thông hiệu quả."
    },
    {
        "id": "sec_transport_strategies",
        "title": "3. Chiến lược giao thông đô thị bền vững",
        "selector": "#sec-transport-strategies",
        "en": "Section 3 evaluates how modern metropolises conquer gridlock and emissions by harmonizing carrot policies that incentivize mass transit with stick policies that penalize private vehicle usage.",
        "vi": "Mục ba đánh giá cách các đại đô thị giải quyết ùn tắc và khí thải thông qua kết hợp hài hòa các chính sách củ cà rốt khuyến khích giao thông công cộng với các chính sách cây gậy hạn chế phương tiện cá nhân."
    },
    {
        "id": "transit_carrot_stick",
        "title": "Chiến lược Cây gậy và Củ cà rốt trong giao thông",
        "selector": "#card-transit-carrot-stick",
        "en": "Carrot incentives include Curitiba's Bus Rapid Transit tube stations and Copenhagen's Cycle Superhighways. Stick restrictions include London's Congestion Charge, Singapore's Electronic Road Pricing, and restricted parking quotas.",
        "vi": "Chính sách củ cà rốt bao gồm trạm xe buýt nhanh BRT dạng ống tại Curitiba và siêu xa lộ xe đạp ở Copenhagen. Chính sách cây gậy gồm phí ùn tắc ở Luân Đôn, thu phí đường bộ điện tử tại Singapore và hạn ngạch bãi đỗ xe nội đô nghiêm ngặt."
    },
    {
        "id": "sec_shanghai_casestudy",
        "title": "4. Nghiên cứu tình huống: Quy hoạch Thượng Hải và Tái tạo sinh thái",
        "selector": "#sec-shanghai-casestudy",
        "en": "Section 4 investigates Shanghai, China's economic juggernaut. We analyze its transformation from dense historic Puxi into a futuristic dual-core metropolis anchored by the Lujiazui financial center in Pudong.",
        "vi": "Mục bốn nghiên cứu Thượng Hải, đầu tàu kinh tế của Trung Quốc. Chúng ta phân tích quá trình chuyển mình từ khu Phố Tây lịch sử đông đúc thành đại đô thị hai lõi hiện đại với trung tâm tài chính Lục Gia Chủy bên bờ Phố Đông."
    },
    {
        "id": "shanghai_svg",
        "title": "Sơ đồ quy hoạch hai lõi và giao thông Thượng Hải",
        "selector": "#card-shanghai-svg",
        "en": "This spatial diagram details Shanghai's master plan: the 800-kilometer Shanghai Metro network connecting satellite eco-cities like Lingang, alongside environmental remediation projects like the Suzhou Creek Rehabilitation.",
        "vi": "Sơ đồ không gian này chi tiết hóa quy hoạch của Thượng Hải: mạng lưới tàu điện ngầm dài tám trăm cây số kết nối các đô thị sinh thái vệ tinh như Lâm Cảng, song hành cùng các dự án phục hồi môi trường tiêu biểu như cải tạo sông Tô Châu."
    },
    {
        "id": "sec_delhi_hazards",
        "title": "5. Hiểm họa môi trường ở đại đô thị: Chất lượng không khí tại Delhi",
        "selector": "#sec-delhi-hazards",
        "en": "Section 5 confronts the severe environmental fallout of uncurbed megacity growth, focusing on Delhi's seasonal air pollution crisis where winter thermal inversions trap deadly particulate matter.",
        "vi": "Mục năm đối diện với những hệ lụy môi trường nghiêm trọng của các siêu đô thị bùng nổ dân số, tập trung vào cuộc khủng hoảng ô nhiễm không khí theo mùa ở Delhi khi hiện tượng nghịch nhiệt mùa đông giam giữ các hạt bụi mịn độc hại."
    },
    {
        "id": "delhi_interventions",
        "title": "Các giải pháp đa tầng cải thiện không khí tại Delhi",
        "selector": "#card-delhi-interventions",
        "en": "To combat hazardous Air Quality Index spikes over 450, Delhi deployed multi-tiered interventions: converting all public buses and auto-rickshaws to Compressed Natural Gas, enforcing Odd-Even license plate traffic rationing, and installing anti-smog water cannons.",
        "vi": "Để ứng phó với chỉ số AQI vượt ngưỡng nguy hại trên bốn trăm năm mươi, Delhi đã áp dụng các giải pháp đa tầng: chuyển toàn bộ xe buýt và xe lam sang chạy khí thiên nhiên nén CNG, phân luồng xe biển số chẵn lẻ và lắp đặt các tháp phun sương dập bụi."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 7.3",
        "selector": "#card-exam-strategy",
        "en": "In exam 7-mark case study questions on urban sustainability, always name specific schemes, cite quantifiable data, and critically analyze both short-term economic trade-offs and long-term socio-environmental dividends.",
        "vi": "Trong các câu hỏi tình huống bảy điểm về đô thị bền vững, các em phải luôn nêu tên dự án cụ thể, trích dẫn số liệu định lượng và phân tích sắc bén cả sự đánh đổi chi phí kinh tế ngắn hạn lẫn lợi ích xã hội môi trường dài hạn."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_housing_brownfield", "title": "1. Nhà ở đô thị: Đất nâu vs Đất xanh", "startSegmentId": "sec_housing_brownfield"},
    {"id": "sec_sustainable_cities", "title": "2. Nguyên lý thành phố bền vững", "startSegmentId": "sec_sustainable_cities"},
    {"id": "sec_transport_strategies", "title": "3. Chiến lược giao thông bền vững", "startSegmentId": "sec_transport_strategies"},
    {"id": "sec_shanghai_casestudy", "title": "4. Quy hoạch siêu đô thị Thượng Hải", "startSegmentId": "sec_shanghai_casestudy"},
    {"id": "sec_delhi_hazards", "title": "5. Quản lý chất lượng không khí tại Delhi", "startSegmentId": "sec_delhi_hazards"},
    {"id": "card_exam_strategy", "title": "Chiến lược làm bài thi", "startSegmentId": "exam_strategy"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    1. Urban Housing & The Brownfield vs. Greenfield Dilemma\n  </h2>',
        '<h2 id="sec-housing-brownfield" class="lecture-interactive-card" data-lecture-section="sec_housing_brownfield" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    1. Urban Housing & The Brownfield vs. Greenfield Dilemma\n  </h2>'
    )

    # Brownfield vs Greenfield table wrapper card
    html = html.replace(
        '<div style="overflow-x:auto; margin:20px 0;">\n    <table style="width:100%; border-collapse:collapse;',
        '<div id="card-brownfield-greenfield-table" class="lecture-interactive-card" data-lecture-section="brownfield_greenfield_table" style="overflow-x:auto; margin:20px 0; cursor:pointer;">\n    <table style="width:100%; border-collapse:collapse;'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    2. Principles of Sustainable Cities: The Egan Wheel Framework\n  </h2>',
        '<h2 id="sec-sustainable-cities" class="lecture-interactive-card" data-lecture-section="sec_sustainable_cities" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    2. Principles of Sustainable Cities: The Egan Wheel Framework\n  </h2>'
    )

    # Egan Wheel SVG card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#0d9488; border-radius:50%;"></span>\n    Interactive Vector Diagram: The 3 Pillars of Sustainable Urban Management (Egan Wheel)',
        '<div id="card-egan-wheel-svg" class="lecture-interactive-card" data-lecture-section="egan_wheel_svg" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#0d9488; border-radius:50%;"></span>\n    Interactive Vector Diagram: The 3 Pillars of Sustainable Urban Management (Egan Wheel)'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    3. Sustainable Urban Transport Strategies\n  </h2>',
        '<h2 id="sec-transport-strategies" class="lecture-interactive-card" data-lecture-section="sec_transport_strategies" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    3. Sustainable Urban Transport Strategies\n  </h2>'
    )

    # Transit Carrot & Stick card
    html = html.replace(
        '<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:18px; margin:20px 0;">\n    <div style="background:#f0fdfa; border-left:4px solid #0d9488;',
        '<div id="card-transit-carrot-stick" class="lecture-interactive-card" data-lecture-section="transit_carrot_stick" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:18px; margin:20px 0; cursor:pointer;">\n    <div style="background:#f0fdfa; border-left:4px solid #0d9488;'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    4. Megacity Case Study: Shanghai\'s Master Plan & Ecological Regeneration\n  </h2>',
        '<h2 id="sec-shanghai-casestudy" class="lecture-interactive-card" data-lecture-section="sec_shanghai_casestudy" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    4. Megacity Case Study: Shanghai\'s Master Plan & Ecological Regeneration\n  </h2>'
    )

    # Shanghai SVG card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#2563eb; border-radius:50%;"></span>\n    Spatial Case Study: Shanghai Megacity Dual-Core Planning & Transit Infrastructure',
        '<div id="card-shanghai-svg" class="lecture-interactive-card" data-lecture-section="shanghai_svg" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#2563eb; border-radius:50%;"></span>\n    Spatial Case Study: Shanghai Megacity Dual-Core Planning & Transit Infrastructure'
    )

    # Section 5 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    5. Environmental Hazards in Megacities: Air Quality in Delhi\n  </h2>',
        '<h2 id="sec-delhi-hazards" class="lecture-interactive-card" data-lecture-section="sec_delhi_hazards" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    5. Environmental Hazards in Megacities: Air Quality in Delhi\n  </h2>'
    )

    # Delhi Interventions card
    html = html.replace(
        '<div style="background:#eff6ff; border-left:4px solid #3b82f6; padding:16px; border-radius:8px; margin:18px 0;">\n    <div style="font-weight:700; color:#1d4ed8; margin-bottom:6px;">Delhi\'s Multi-Tiered Management Interventions:</div>',
        '<div id="card-delhi-interventions" class="lecture-interactive-card" data-lecture-section="delhi_interventions" style="background:#eff6ff; border-left:4px solid #3b82f6; padding:16px; border-radius:8px; margin:18px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#1d4ed8; margin-bottom:6px;">Delhi\'s Multi-Tiered Management Interventions:</div>'
    )

    # Exam Strategy card
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); border:1px solid #99f6e4; border-left:6px solid #0d9488; border-radius:10px; padding:20px; margin:32px 0;">',
        '<div id="card-exam-strategy" class="lecture-interactive-card" data-lecture-section="exam_strategy" style="background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); border:1px solid #99f6e4; border-left:6px solid #0d9488; border-radius:10px; padding:20px; margin:32px 0; cursor:pointer;">'
    )

    return html

async def main():
    print(f"--- Starting Audio & Manifest for {LECTURE_CODE} ---")
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()

    new_html = transform_html(raw_html)

    # Verify div balance
    open_divs = len(re.findall(r'<div\b', new_html, re.I))
    close_divs = len(re.findall(r'</div\b', new_html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch in {LECTURE_CODE}: Diff={diff}"

    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Saved interactive HTML to {interactive_path}")

    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} uploaded successfully to Supabase!\n")

if __name__ == '__main__':
    asyncio.run(main())
