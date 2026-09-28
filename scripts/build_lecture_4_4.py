import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '4_4'
LECTURE_ID = 'c81dc416-7aa4-4e26-a2af-341d6c03fa52'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '4.4 Managing the Impacts of Tectonic Hazards'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.4: Quản lý tác động của Hiểm họa Địa chất",
        "selector": "#sec-header",
        "en": "Lesson 4.4: Managing the Impacts of Tectonic Hazards. In this lesson, we master the 4 Ps management framework, the Park Model disaster response curve, seismic engineering, and volcano mitigation case studies.",
        "vi": "Bài bốn chấm bốn: Quản lý tác động của các Hiểm họa Địa chất. Trong bài học này, chúng ta sẽ làm chủ khung quản lý bốn chữ P, mô hình đường cong phản ứng thảm họa Park Model, kỹ thuật xây dựng kháng chấn và các điển cứu giảm nhẹ núi lửa."
    },
    {
        "id": "sec_4ps_framework",
        "title": "1. Khung quản lý 4 chữ P (Prediction, Protection, Preparation, Planning)",
        "selector": "#sec-4ps-framework",
        "en": "Section 1: The 4 Ps Management Framework. Minimizing human disaster relies on prediction using science, protection through engineering, community preparation via drills, and spatial planning restricting hazard-zone construction.",
        "vi": "Phần một: Khung quản lý bốn chữ P. Giảm thiểu thảm họa dựa trên dự báo khoa học, bảo vệ bằng các công trình công nghệ, chuẩn bị cộng đồng qua diễn tập và quy hoạch không gian hạn chế xây dựng ở vùng nguy hiểm."
    },
    {
        "id": "p_prediction",
        "title": "1. Dự báo khoa học (Prediction: Núi lửa vs Động đất)",
        "selector": "#card-p-prediction",
        "en": "Prediction. Highly reliable for volcanic monitoring through ground swelling and gas emissions, but impossible for earthquakes beyond broad statistical probability over centuries.",
        "vi": "Dự báo khoa học. Rất chính xác đối với núi lửa thông qua đo biến dạng mặt đất và khí thải, nhưng hiện tại bất khả thi đối với động đất ngoài việc xác định xác suất thống kê dài hạn."
    },
    {
        "id": "p_protection",
        "title": "2. Bảo vệ & Công trình chống chịu (Protection: Engineering)",
        "selector": "#card-p-protection",
        "en": "Protection. Designing physical defenses that withstand shockwaves or divert volcanic material, including base isolators, tuned mass dampers, and lava diversion channels.",
        "vi": "Bảo vệ và Công trình chống chịu. Thiết kế các công trình phòng thủ vật lý có thể chịu được sóng xung kích hoặc chuyển hướng dòng núi lửa, bao gồm gối cách chấn đáy, con lắc triệt tiêu dao động và kênh chuyển hướng dung nham."
    },
    {
        "id": "p_preparation",
        "title": "3. Chuẩn bị cộng đồng (Preparation: Drills & Kits)",
        "selector": "#card-p-preparation",
        "en": "Preparation. Training emergency services and the public through routine nationwide evacuation drills, automated phone alerts, emergency grab-and-go kits, and medical stockpiling.",
        "vi": "Chuẩn bị cộng đồng. Huấn luyện các lực lượng cứu hộ và người dân thông qua diễn tập sơ tán định kỳ toàn quốc, cảnh báo tự động qua điện thoại, balo khẩn cấp và tích trữ vật tư y tế."
    },
    {
        "id": "p_planning",
        "title": "4. Quy hoạch sử dụng đất (Planning: Land-Use Zoning)",
        "selector": "#card-p-planning",
        "en": "Spatial Planning. Enforcing strict land-use zoning that bans high-density residential development, schools, and hospitals on active fault lines, liquefaction zones, or lahar pathways.",
        "vi": "Quy hoạch không gian sử dụng đất. Thực thi phân vùng sử dụng đất nghiêm ngặt, cấm xây dựng các khu dân cư đông đúc, trường học và bệnh viện trên các đường đứt gãy, vùng đất hóa lỏng hoặc lòng máng lũ bùn núi lửa."
    },
    {
        "id": "sec_park_model",
        "title": "2. Mô hình Park Model: Đường cong phản ứng thảm họa (Disaster Response Curve)",
        "selector": "#sec-park-model",
        "en": "Section 2: The Park Model. Depicts the trajectory of quality of life following a disaster, tracking the steep descent during impact through relief and rehabilitation to long-term reconstruction.",
        "vi": "Phần hai: Mô hình Park Model và Đường cong phản ứng thảm họa. Minh họa quỹ đạo chất lượng cuộc sống sau thảm họa, từ cú sụt giảm nghiêm trọng trong giai đoạn tác động đến cứu trợ khẩn cấp, phục hồi và tái thiết lâu dài."
    },
    {
        "id": "park_phase_relief",
        "title": "Giai đoạn Cứu trợ khẩn cấp (Relief Phase: Giờ đến Ngày)",
        "selector": "#park-phase-relief",
        "en": "The Relief Phase. Hours to days after impact. Search-and-rescue teams deploy sniffer dogs and thermal cameras; emergency triage clinics, bottled water, and temporary tents prevent hypothermia and dehydration.",
        "vi": "Giai đoạn Cứu trợ khẩn cấp. Vài giờ đến vài ngày sau thảm họa. Các đội tìm kiếm cứu nạn sử dụng chó nghiệp vụ và camera nhiệt; các bệnh viện dã chiến, nước uống đóng chai và lều bạt khẩn cấp giúp ngăn mất nước và hạ thân nhiệt."
    },
    {
        "id": "park_phase_rehab",
        "title": "Giai đoạn Phục hồi sinh hoạt (Rehabilitation: Tuần đến Tháng)",
        "selector": "#park-phase-rehab",
        "en": "The Rehabilitation Phase. Weeks to months later. Essential lifelines are restored: reconnecting electricity grids, repairing water mains, clearing transport arteries, and opening temporary schools.",
        "vi": "Giai đoạn Phục hồi sinh hoạt. Vài tuần đến vài tháng sau đó. Các huyết mạch thiết yếu được tái kết nối: khôi phục mạng lưới điện, hàn gắn ống nước, thông đường giao thông và mở các trường học dã chiến."
    },
    {
        "id": "park_phase_reconstruction",
        "title": "Giai đoạn Tái thiết lâu dài: Xây dựng lại tốt hơn (Reconstruction)",
        "selector": "#park-phase-reconstruction",
        "en": "The Reconstruction Phase. Months to years of rebuilding. High-income countries build back better with upgraded seismic standards; poor low-income countries often remain trapped in permanent quality of life deficits.",
        "vi": "Giai đoạn Tái thiết lâu dài. Nhiều tháng đến nhiều năm tái thiết. Các nước giàu tái thiết tốt hơn với các tiêu chuẩn kháng chấn nâng cấp; ngược lại, các nước nghèo thường bị mắc kẹt trong tình trạng suy giảm chất lượng sống vĩnh viễn."
    },
    {
        "id": "sec_earthquake_mitigation",
        "title": "3. Kỹ thuật công trình chống động đất (Earthquake Engineering)",
        "selector": "#sec-earthquake-mitigation",
        "en": "Section 3: Earthquake Mitigation and Structural Engineering. Modern buildings are designed to absorb and dissipate seismic shear forces through flexible structural design rather than rigid brittle strength.",
        "vi": "Phần ba: Kỹ thuật công trình chống động đất. Các tòa nhà hiện đại được thiết kế để hấp thụ và tiêu tán lực cắt địa chấn thông qua cấu trúc linh hoạt uốn dẻo thay vì độ cứng giòn cố định."
    },
    {
        "id": "eng_base_isolation",
        "title": "Gối cách chấn đáy (Base Isolation: Cao su & Chì)",
        "selector": "#eng-base-isolation",
        "en": "Base Isolation Bearings. Heavy laminated lead-rubber bearings installed between foundations and bedrock decouple the building from ground motion, absorbing up to eighty percent of horizontal seismic shock.",
        "vi": "Gối cách chấn đáy. Các tấm đệm cao su nhiều lớp có lõi chì đặt giữa móng và nền đá giúp tách rời tòa nhà khỏi rung chấn mặt đất, hấp thụ tới tám mươi phần trăm xung lực ngang."
    },
    {
        "id": "eng_tuned_mass_damper",
        "title": "Con lắc triệt tiêu dao động (Tuned Mass Damper: Taipei 101)",
        "selector": "#eng-tuned-mass-damper",
        "en": "Tuned Mass Dampers. Enormous suspended pendulum counterweights, such as the 660-tonne steel sphere in Taipei 101, sway in the opposite direction of ground vibrations to dampen skyscraper oscillation.",
        "vi": "Con lắc triệt tiêu dao động. Những quả cầu kim loại đối trọng khổng lồ như khối thép nặng sáu trăm sáu mươi tấn trên đỉnh tháp Đài Bắc một trăm lẻ một, đu đưa ngược hướng chấn động để dập tắt sự rung lắc của tòa nhà chọc trời."
    },
    {
        "id": "eng_cross_bracing",
        "title": "Hệ giằng thép chữ X (Steel Cross-Bracing)",
        "selector": "#eng-cross-bracing",
        "en": "Steel Cross-Bracing. Diagonal lattice frameworks built into building frames distribute twisting shear forces evenly throughout the structure, preventing catastrophic pancaking.",
        "vi": "Hệ giằng thép chữ X. Khung giằng chéo hình mắt cáo gia cố ngoại thất giúp phân tán đều các lực xoắn cắt địa chấn khắp khung nhà, ngăn ngừa hiện tượng sụp đổ tầng."
    },
    {
        "id": "sec_volcano_management",
        "title": "4. Quản lý núi lửa & Nghiên cứu điển hình (Núi Etna vs Haiti 2021)",
        "selector": "#sec-volcano-management",
        "en": "Section 4: Volcano Management and Case Studies. Active surveillance through seismographs, tiltmeters, and gas sensors enables successful warning, as demonstrated on Mount Etna, contrasted with compound disasters in Haiti.",
        "vi": "Phần bốn: Quản lý núi lửa và Các nghiên cứu điển hình. Giám sát địa chấn, đo độ nghiêng và cảm biến khí giúp dự báo chính xác, minh chứng tại núi lửa Etna ở Ý, đối lập với thảm họa kép tại Haiti năm hai nghìn không trăm hai mươi mốt."
    },
    {
        "id": "case_etna_italy",
        "title": "🌋 Điển cứu Núi Etna, Ý: Giám sát hiện đại & Kênh đổi dòng dung nham",
        "selector": "#case-etna-italy",
        "en": "Case Study: Mount Etna, Sicily. Monitored continuously by the INGV. Explosives and concrete blocks diverted advancing lava flows away from Zafferana, ensuring zero casualties despite regular explosive activity.",
        "vi": "Nghiên cứu điển hình: Núi Etna ở Si-xin nước Ý. Được viện địa chất quốc gia giám sát liên tục hai mươi tư trên bảy. Thuốc nổ và các khối bê tông đã chuyển hướng thành công dòng dung nham ra khỏi thị trấn Zafferana, không để xảy ra thương vong dù núi lửa thường xuyên hoạt động."
    },
    {
        "id": "case_haiti_2021",
        "title": "🇭🇹 Điển cứu Bán đảo Tiburon, Haiti (2021): Thảm họa kép",
        "selector": "#case-haiti-2021",
        "en": "Case Study: Haiti 2021 Earthquake. An Mw 7.2 earthquake was struck 48 hours later by Tropical Storm Grace. Extreme poverty and political collapse crippled search-and-rescue, leaving 2,200 dead and 137,000 homes wrecked.",
        "vi": "Nghiên cứu điển hình: Động đất Bán đảo Tiburon Haiti năm hai nghìn không trăm hai mươi mốt. Trận động đất bảy phẩy hai độ Mw bị bão nhiệt đới Grace bồi thêm chỉ sau bốn mươi tám giờ. Đói nghèo và khủng hoảng chính trị làm tê liệt công tác cứu hộ, khiến hơn hai nghìn hai trăm người chết và hàng trăm nghìn ngôi nhà đổ nát."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 5},
    "sec_4ps_framework": {"start": 1, "end": 5},
    "sec_park_model": {"start": 6, "end": 9},
    "sec_earthquake_mitigation": {"start": 10, "end": 13},
    "sec_volcano_management": {"start": 14, "end": 16}
}

def transform_html(raw_html):
    html = raw_html
    
    # 1. Header
    html = re.sub(
        r'(<div style="background:linear-gradient\(135deg, #b91c1c, #dc2626, #ea580c\);[^"]*">[\s\S]*?</div>)',
        r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; border-radius:12px; margin-bottom:24px; transition:all 0.2s ease;">\1</div>',
        html, count=1
    )
    
    # 2. Section 1: 4 Ps
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*1\. The 3 Ps / 4 Ps Management Framework\s*</h2>)',
        r'<div id="sec-4ps-framework" class="lecture-interactive-card" data-lecture-section="sec_4ps_framework" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*2\. The Park Model)',
        r'</div>\1\2',
        html, count=1
    )
    
    # 4 Ps cards
    html = html.replace(
        '<div style="background:#fef2f2; border:1px solid #fca5a5; border-radius:8px; padding:15px;">\n        <h4 style="margin:0 0 6px 0; color:#b91c1c; font-size:15px; font-weight:bold;">1. Prediction</h4>',
        '<div id="card-p-prediction" class="lecture-interactive-card" data-lecture-section="p_prediction" style="background:#fef2f2; border:1px solid #fca5a5; border-radius:8px; padding:15px; cursor:pointer;">\n        <h4 style="margin:0 0 6px 0; color:#b91c1c; font-size:15px; font-weight:bold;">1. Prediction</h4>'
    )
    html = html.replace(
        '<div style="background:#fff7ed; border:1px solid #fed7aa; border-radius:8px; padding:15px;">\n        <h4 style="margin:0 0 6px 0; color:#c2410c; font-size:15px; font-weight:bold;">2. Protection</h4>',
        '<div id="card-p-protection" class="lecture-interactive-card" data-lecture-section="p_protection" style="background:#fff7ed; border:1px solid #fed7aa; border-radius:8px; padding:15px; cursor:pointer;">\n        <h4 style="margin:0 0 6px 0; color:#c2410c; font-size:15px; font-weight:bold;">2. Protection</h4>'
    )
    html = html.replace(
        '<div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:15px;">\n        <h4 style="margin:0 0 6px 0; color:#1d4ed8; font-size:15px; font-weight:bold;">3. Preparation</h4>',
        '<div id="card-p-preparation" class="lecture-interactive-card" data-lecture-section="p_preparation" style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:15px; cursor:pointer;">\n        <h4 style="margin:0 0 6px 0; color:#1d4ed8; font-size:15px; font-weight:bold;">3. Preparation</h4>'
    )
    html = html.replace(
        '<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:15px;">\n        <h4 style="margin:0 0 6px 0; color:#15803d; font-size:15px; font-weight:bold;">4. Planning</h4>',
        '<div id="card-p-planning" class="lecture-interactive-card" data-lecture-section="p_planning" style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:15px; cursor:pointer;">\n        <h4 style="margin:0 0 6px 0; color:#15803d; font-size:15px; font-weight:bold;">4. Planning</h4>'
    )
    
    # 3. Section 2: Park Model
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*2\. The Park Model \(Disaster Response Curve\)\s*</h2>)',
        r'<div id="sec-park-model" class="lecture-interactive-card" data-lecture-section="sec_park_model" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*3\. Earthquake Mitigation)',
        r'</div>\1\2',
        html, count=1
    )
    
    # SVG 1 Park Model bands
    html = html.replace('<rect x="160" y="40" width="160" height="300" fill="#ef4444" opacity="0.08"/>', '<g id="park-phase-relief" data-lecture-section="park_phase_relief" style="cursor:pointer;"><rect x="160" y="40" width="160" height="300" fill="#ef4444" opacity="0.08"/>')
    html = html.replace('<text x="240" y="75" fill="#94a3b8" font-size="9.5" text-anchor="middle">Search &amp; rescue, triage, tents</text>', '<text x="240" y="75" fill="#94a3b8" font-size="9.5" text-anchor="middle">Search &amp; rescue, triage, tents</text></g>')
    
    html = html.replace('<rect x="320" y="40" width="180" height="300" fill="#38bdf8" opacity="0.08"/>', '<g id="park-phase-rehab" data-lecture-section="park_phase_rehab" style="cursor:pointer;"><rect x="320" y="40" width="180" height="300" fill="#38bdf8" opacity="0.08"/>')
    html = html.replace('<text x="410" y="75" fill="#94a3b8" font-size="9.5" text-anchor="middle">Restore power, water, clinics</text>', '<text x="410" y="75" fill="#94a3b8" font-size="9.5" text-anchor="middle">Restore power, water, clinics</text></g>')
    
    html = html.replace('<rect x="500" y="40" width="280" height="300" fill="#10b981" opacity="0.08"/>', '<g id="park-phase-reconstruction" data-lecture-section="park_phase_reconstruction" style="cursor:pointer;"><rect x="500" y="40" width="280" height="300" fill="#10b981" opacity="0.08"/>')
    html = html.replace('<text x="640" y="75" fill="#94a3b8" font-size="9.5" text-anchor="middle">Rebuild infrastructure, seismic codes</text>', '<text x="640" y="75" fill="#94a3b8" font-size="9.5" text-anchor="middle">Rebuild infrastructure, seismic codes</text></g>')
    
    # 4. Section 3: Engineering
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*3\. Earthquake Mitigation &amp; Structural Engineering\s*</h2>)',
        r'<div id="sec-earthquake-mitigation" class="lecture-interactive-card" data-lecture-section="sec_earthquake_mitigation" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#b91c1c;[^"]*">\s*4\. Volcano Management)',
        r'</div>\1\2',
        html, count=1
    )
    
    # SVG 2 engineering elements
    html = html.replace('<rect x="70" y="345" width="220" height="42" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>', '<g id="eng-base-isolation" data-lecture-section="eng_base_isolation" style="cursor:pointer;"><rect x="70" y="345" width="220" height="42" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>')
    html = html.replace('<text x="180" y="377" fill="#64748b" font-size="9.5" text-anchor="middle">Absorbs 80% of horizontal ground shock</text>', '<text x="180" y="377" fill="#64748b" font-size="9.5" text-anchor="middle">Absorbs 80% of horizontal ground shock</text></g>')
    
    html = html.replace('<rect x="605" y="55" width="225" height="46" rx="4" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>', '<g id="eng-tuned-mass-damper" data-lecture-section="eng_tuned_mass_damper" style="cursor:pointer;"><rect x="605" y="55" width="225" height="46" rx="4" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>')
    html = html.replace('<text x="717" y="88" fill="#64748b" font-size="9.5" text-anchor="middle">660-tonne pendulum counters sway (Taipei 101)</text>', '<text x="717" y="88" fill="#64748b" font-size="9.5" text-anchor="middle">660-tonne pendulum counters sway (Taipei 101)</text></g>')
    
    html = html.replace('<rect x="60" y="190" width="200" height="42" rx="4" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>', '<g id="eng-cross-bracing" data-lecture-section="eng_cross_bracing" style="cursor:pointer;"><rect x="60" y="190" width="200" height="42" rx="4" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>')
    html = html.replace('<text x="160" y="222" fill="#64748b" font-size="9.5" text-anchor="middle">Distributes lateral shear forces</text>', '<text x="160" y="222" fill="#64748b" font-size="9.5" text-anchor="middle">Distributes lateral shear forces</text></g>')
    
    # 5. Section 4: Volcano Management
    html = re.sub(
        r'(<h2 style="color:#b91c1c;[^"]*">\s*4\. Volcano Management &amp; Case Studies\s*</h2>)',
        r'<div id="sec-volcano-management" class="lecture-interactive-card" data-lecture-section="sec_volcano_management" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    # Case study cards
    html = html.replace(
        '<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:8px; padding:20px;">\n        <h4 style="margin:0 0 10px 0; color:#15803d; font-size:17px; font-weight:bold;">🌋 Case Study: Mount Etna, Sicily (HIC Volcano Management)</h4>',
        '<div id="case-etna-italy" class="lecture-interactive-card" data-lecture-section="case_etna_italy" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:8px; padding:20px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#15803d; font-size:17px; font-weight:bold;">🌋 Case Study: Mount Etna, Sicily (HIC Volcano Management)</h4>'
    )
    html = html.replace(
        '<div style="background:#fef2f2; border:1px solid #fca5a5; border-left:5px solid #dc2626; border-radius:8px; padding:20px;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:17px; font-weight:bold;">🇭🇹 Case Study: Tiburon Peninsula Earthquake, Haiti (2021)</h4>',
        '<div id="case-haiti-2021" class="lecture-interactive-card" data-lecture-section="case_haiti_2021" style="background:#fef2f2; border:1px solid #fca5a5; border-left:5px solid #dc2626; border-radius:8px; padding:20px; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:17px; font-weight:bold;">🇭🇹 Case Study: Tiburon Peninsula Earthquake, Haiti (2021)</h4>'
    )
    
    html += '</div>'
    return html

async def main():
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )
    
    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
    
    new_html = transform_html(raw_html)
    
    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")
    
    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == '__main__':
    asyncio.run(main())
