import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_6"
LECTURE_ID = "fb30c141-db3a-49e8-aa55-028c913640d4"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.6 The Impacts of Energy Production"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10.6: Tác động của Sản xuất Năng lượng",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 10.6: The Impacts of Energy Production. In this lecture, we critically evaluate the global energy trilemma: analyzing the environmental and respiratory costs of fossil fuels, evaluating the low-carbon baseload advantages and radiological hazards of nuclear power, assessing ecological trade-offs of renewables like wind and hydroelectricity, and examining Sweden's world-leading transition towards 100 percent fossil-free energy.",
        "vi": "Chào mừng các em đến với bài mười chấm sáu: Tác động của Sản xuất Năng lượng. Trong bài giảng này, chúng ta sẽ đánh giá toàn diện tam giác nan giải năng lượng: phân tích cái giá môi trường và sức khỏe hô hấp của nhiên liệu hóa thạch, cân nhắc giữa lợi thế điện nền phát thải thấp và hiểm họa phóng xạ của điện hạt nhân, đánh giá các tác động đánh đổi sinh thái của năng lượng tái tạo như thủy điện và điện gió, đồng thời phân tích hình mẫu chuyển dịch năng lượng không hóa thạch của Thụy Điển."
    },
    {
        "id": "sec_fossil_impacts",
        "title": "1. Tác động môi trường và Sức khỏe của Nhiên liệu hóa thạch",
        "selector": "#sec-fossil-impacts",
        "en": "Section 1 examines the destructive lifecycle impacts of coal, oil, and gas: mountaintop removal mining obliterating watersheds, acid rain triggered by sulfur dioxide emissions dissolving forest canopies and leaching toxic heavy metals, particulate matter causing millions of premature cardiopulmonary deaths, and massive carbon dioxide emissions driving catastrophic anthropogenic climate change.",
        "vi": "Mục một phân tích các tác động phá hủy môi trường trong toàn bộ vòng đời của than đá, dầu mỏ và khí đốt: khai thác bạt đỉnh núi san phẳng lưu vực sông, mưa axit từ khí lưu huỳnh đioxit làm trơ trụi rừng cây và hòa tan kim loại nặng độc hại, bụi mịn gây ra hàng triệu ca tử vong sớm do bệnh tim phổi, cùng lượng khí nhà kính khổng lồ thúc đẩy biến đổi khí hậu do con người gây ra."
    },
    {
        "id": "sec_nuclear_power",
        "title": "2. Điện hạt nhân: Nguồn điện nền phát thải thấp vs Hiểm họa phóng xạ",
        "selector": "#sec-nuclear-power",
        "en": "Section 2 investigates nuclear energy: generating colossal gigawatts of continuous baseload electricity with virtually zero operational greenhouse gas emissions and high energy density. However, it carries extreme capital construction costs, the unsolved multi-millennial dilemma of deep geological high-level radioactive waste disposal, and catastrophic meltdown risks as witnessed at Chernobyl and Fukushima.",
        "vi": "Mục hai nghiên cứu năng lượng hạt nhân: cung cấp nguồn điện nền liên tục khổng lồ với phát thải khí nhà kính gần như bằng không trong quá trình vận hành và mật độ năng lượng cực cao. Tuy nhiên, nó đòi hỏi chi phí đầu tư ban đầu đắt đỏ, bài toán nan giải hàng ngàn năm về chôn lấp rác thải phóng xạ hoạt tính cao dưới lòng đất, cùng nguy cơ thảm họa nóng chảy lõi lò phản ứng như bài học Chernobyl và Fukushima."
    },
    {
        "id": "sec_renewable_tradeoffs",
        "title": "3. Năng lượng tái tạo: Nhãn xanh vs Các đánh đổi sinh thái",
        "selector": "#sec-renewable-tradeoffs",
        "en": "Section 3 evaluates renewable energy trade-offs: Large hydroelectric mega-dams like Three Gorges displace hundreds of thousands of people and trigger downstream silt starvation, wind turbines generate visual and acoustic blight while fragmenting avian flyways, and solar photovoltaic utility fields consume vast land tracts and demand rare mineral extraction.",
        "vi": "Mục ba đánh giá các đánh đổi sinh thái của năng lượng tái tạo: Đại thủy điện như đập Tam Hiệp làm xáo trộn cuộc sống của hàng trăm ngàn dân tái định cư và chặn giữ phù sa hạ lưu, tua-bin gió gây ô nhiễm thị giác tiếng ồn và đe dọa đường bay của các loài chim, trong khi cánh đồng điện mặt trời chiếm diện tích đất khổng lồ và đòi hỏi khai thác khoáng sản đất hiếm phức tạp."
    },
    {
        "id": "sec_global_trends",
        "title": "4. Xu hướng tiêu thụ năng lượng toàn cầu (1970–2023)",
        "selector": "#sec-global-trends",
        "en": "Section 4 analyzes five decades of global consumption patterns: while renewable capacity has expanded rapidly in percentage terms, absolute fossil fuel combustion continues to increase in emerging economies to support urbanization, underscoring the formidable inertia of the global hydrocarbon economy.",
        "vi": "Mục bốn phân tích xu hướng tiêu thụ năng lượng toàn cầu trong năm thập kỷ qua: dù công suất năng lượng tái tạo tăng trưởng nhanh về mặt tỉ lệ, tổng khối lượng đốt nhiên liệu hóa thạch tuyệt đối vẫn tiếp tục gia tăng tại các nền kinh tế mới nổi để đáp ứng đô thị hóa, cho thấy sức ì to lớn của nền kinh tế carbon toàn cầu."
    },
    {
        "id": "sec_sweden_casestudy",
        "title": "5. Nghiên cứu tình huống IGCSE: Chiến lược phi carbon hóa của Thụy Điển",
        "selector": "#sec-sweden-casestudy",
        "en": "Section 5 showcases Sweden as an exemplary decarbonization model: leveraging a stable twin foundation of hydro and nuclear baseload power, combined with pioneering district heating networks powered by municipal waste-to-energy incineration and aggressive carbon taxation enacted in 1991.",
        "vi": "Mục năm giới thiệu Thụy Điển như một hình mẫu chuyển dịch phi carbon hóa tiêu biểu: tận dụng nền tảng điện kép vững chắc giữa thủy điện và điện hạt nhân, kết hợp mạng lưới sưởi ấm khu vực tuần hoàn đốt rác thu hồi năng lượng, cùng chính sách thuế carbon mang tính đột phá được ban hành từ năm 1991."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 10.6",
        "selector": "#card-exam-strategy",
        "en": "In exam 7-mark case study questions on energy impacts, never depict any energy source as flawless: critically balance economic feasibility against environmental degradation, discuss NIMBYism and aesthetic opposition, and cite quantitative national data like Sweden's 98 percent fossil-free electricity generation.",
        "vi": "Trong các câu hỏi tình huống bảy điểm về tác động năng lượng, các em không bao giờ được mô tả bất kỳ nguồn năng lượng nào là hoàn hảo tuyệt đối: hãy cân nhắc giữa tính khả thi kinh tế với suy thoái môi trường, đề cập đến tâm lý phản đối xây dựng tại địa phương NIMBY, và trích dẫn số liệu định lượng quốc gia như việc Thụy Điển đã đạt chín mươi tám phần trăm sản lượng điện không phát thải hóa thạch."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_fossil_impacts", "title": "1. Tác động của nhiên liệu hóa thạch", "startSegmentId": "sec_fossil_impacts"},
    {"id": "sec_nuclear_power", "title": "2. Điện hạt nhân: Ưu điểm & Rủi ro", "startSegmentId": "sec_nuclear_power"},
    {"id": "sec_renewable_tradeoffs", "title": "3. Đánh đổi sinh thái của năng lượng tái tạo", "startSegmentId": "sec_renewable_tradeoffs"},
    {"id": "sec_global_trends", "title": "4. Xu hướng tiêu thụ năng lượng toàn cầu", "startSegmentId": "sec_global_trends"},
    {"id": "sec_sweden_casestudy", "title": "5. Nghiên cứu tình huống: Thụy Điển", "startSegmentId": "sec_sweden_casestudy"},
    {"id": "card_exam_strategy", "title": "Chiến lược làm bài thi", "startSegmentId": "exam_strategy"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Header
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 60%, #3b82f6 100%);',
        '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 60%, #3b82f6 100%); cursor:pointer;'
    )

    # Sec 1
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Environmental & Health Impacts of Fossil Fuels\n        </h2>',
        '<h2 id="sec-fossil-impacts" class="lecture-interactive-card" data-lecture-section="sec_fossil_impacts" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Environmental & Health Impacts of Fossil Fuels\n        </h2>'
    )

    # Sec 2
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Nuclear Power: Low-Carbon Baseload vs Radiological Risks\n        </h2>',
        '<h2 id="sec-nuclear-power" class="lecture-interactive-card" data-lecture-section="sec_nuclear_power" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Nuclear Power: Low-Carbon Baseload vs Radiological Risks\n        </h2>'
    )

    # Sec 3
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Renewable Energy: Green Credentials vs Environmental Trade-offs\n        </h2>',
        '<h2 id="sec-renewable-tradeoffs" class="lecture-interactive-card" data-lecture-section="sec_renewable_tradeoffs" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Renewable Energy: Green Credentials vs Environmental Trade-offs\n        </h2>'
    )

    # Sec 4
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Global Energy Consumption Trends (1970–2023)\n        </h2>',
        '<h2 id="sec-global-trends" class="lecture-interactive-card" data-lecture-section="sec_global_trends" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Global Energy Consumption Trends (1970–2023)\n        </h2>'
    )

    # Sec 5 (Case Study Sweden)
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          IGCSE Case Study: Sweden\'s Sustainable Decarbonisation\n        </h2>',
        '<h2 id="sec-sweden-casestudy" class="lecture-interactive-card" data-lecture-section="sec_sweden_casestudy" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          IGCSE Case Study: Sweden\'s Sustainable Decarbonisation\n        </h2>'
    )

    # Exam Hint Box
    target_hint = '<div style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border: 1px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 20px; margin-top: 32px;">'
    repl_hint = '<div id="card-exam-strategy" class="lecture-interactive-card" data-lecture-section="exam_strategy" style="background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border: 1px solid #bfdbfe; border-left: 6px solid #2563eb; border-radius: 10px; padding: 20px; margin-top: 32px; cursor:pointer;">'
    html = html.replace(target_hint, repl_hint)

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
