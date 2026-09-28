import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_4"
LECTURE_ID = "199a26cd-1226-4ff7-b063-f7df7fa7b5ba"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.4 How Our Energy is Produced: Sources & Systems"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10.4: Các nguồn năng lượng và Hệ thống sản xuất",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 10.4: How Our Energy is Produced: Sources & Systems. In this lecture, we examine global energy foundations: distinguishing primary natural fuels from secondary electricity, analyzing non-renewable fossil stocks versus renewable flows, investigating the acute fuelwood crisis affecting billions in low-income nations, and tracking the progressive ascent up the Energy Ladder from dung to zero-carbon solar and nuclear baseloads.",
        "vi": "Chào mừng các em đến với bài mười chấm bốn: Các nguồn năng lượng và Hệ thống sản xuất. Trong bài giảng này, chúng ta sẽ khảo sát nền tảng năng lượng toàn cầu: phân biệt các nhiên liệu tự nhiên sơ cấp với dòng điện thứ cấp, phân tích trữ lượng hóa thạch không thể tái tạo so với các dòng năng lượng tái tạo vô tận, điều tra cuộc khủng hoảng củi đốt đè nặng lên hàng tỉ người tại các quốc gia thu nhập thấp, và theo dõi nấc thang tiến bộ năng lượng từ sinh khối chất đốt thô sơ lên điện hạt nhân và năng lượng mặt trời không phát thải."
    },
    {
        "id": "sec_energy_taxonomy",
        "title": "1. Phân loại năng lượng nền tảng: Sơ cấp vs Thứ cấp",
        "selector": "#sec-energy-taxonomy",
        "en": "Section 1 establishes foundational energy taxonomy: Primary energy captures unconverted raw natural resources like coal seams, crude oil deposits, moving river currents, and raw uranium ores. Secondary energy represents manufactured, refined carriers like electricity grids and refined petrol created through conversion processes.",
        "vi": "Mục một thiết lập hệ thống phân loại năng lượng nền tảng: Năng lượng sơ cấp là các nguồn tài nguyên thiên nhiên thô nguyên bản chưa qua biến đổi như vỉa than đá, mỏ dầu thô, dòng chảy thủy điện và quặng uranium. Năng lượng thứ cấp đại diện cho các dạng năng lượng đã qua chế biến tinh chế như lưới điện quốc gia và xăng dầu thương phẩm."
    },
    {
        "id": "sec_fuelwood_crisis",
        "title": "2. Khủng hoảng củi đốt: Nghèo đói năng lượng ở các quốc gia thu nhập thấp",
        "selector": "#sec-fuelwood-crisis",
        "en": "Section 2 investigates energy poverty: over 2.4 billion people worldwide rely on traditional biomass and fuelwood for cooking and basic heating. In Sub-Saharan Africa and rural South Asia, women and children walk up to 10 kilometers daily to gather scarce wood, causing severe deforestation, accelerated soil erosion, and deadly indoor smoke inhalation.",
        "vi": "Mục hai nghiên cứu tình trạng nghèo đói năng lượng: hơn hai phẩy bốn tỉ người trên thế giới vẫn phụ thuộc vào sinh khối truyền thống và củi khô để đun nấu và sưởi ấm. Tại châu Phi cận Sahara và vùng nông thôn Nam Á, phụ nữ và trẻ em phải đi bộ tới mười cây số mỗi ngày để kiếm củi, gây ra nạn phá rừng nghiêm trọng, thúc đẩy xói mòn đất và gây tử vong do ngạt khói độc trong nhà."
    },
    {
        "id": "sec_energy_ladder",
        "title": "3. Thang năng lượng tương tác và Quá trình chuyển dịch phi carbon hóa",
        "selector": "#sec-energy-ladder",
        "en": "Section 3 models the socioeconomic Energy Ladder: showing how households and nations transition as disposable income rises: moving upward from animal dung and charcoal, through kerosene and liquefied petroleum gas, to modern networked electricity and distributed rooftop photovoltaic solar arrays.",
        "vi": "Mục ba mô hình hóa Thang bậc Năng lượng kinh tế xã hội: minh họa cách các hộ gia đình và quốc gia chuyển dịch khi thu nhập tăng lên: từ chất thải động vật và than củi thô sơ bước lên dầu hỏa và khí hóa lỏng LPG, tiến tới mạng lưới điện thông minh và hệ thống pin mặt trời áp mái phi tập trung."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 10.4",
        "selector": "#card-exam-strategy",
        "en": "In exam questions on energy supply, always provide precise technical classifications: clearly separate non-renewable exhaustible fossil fuels like coal from infinite renewable flows like geothermal, and explain the physical-geographical conditions required to site hydroelectric dams or offshore wind arrays.",
        "vi": "Trong các câu hỏi thi về nguồn cung năng lượng, các em hãy luôn phân loại kỹ thuật chính xác: tách bạch nhiên liệu hóa thạch hữu hạn không thể tái sinh với các dòng năng lượng vô tận như địa nhiệt, đồng thời giải thích rõ các điều kiện địa lý tự nhiên cần thiết để lựa chọn địa điểm xây đập thủy điện hoặc trang trại điện gió ngoài khơi."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_energy_taxonomy", "title": "1. Phân loại năng lượng sơ cấp & thứ cấp", "startSegmentId": "sec_energy_taxonomy"},
    {"id": "sec_fuelwood_crisis", "title": "2. Khủng hoảng củi đốt & Nghèo năng lượng", "startSegmentId": "sec_fuelwood_crisis"},
    {"id": "sec_energy_ladder", "title": "3. Thang năng lượng & Chuyển dịch xanh", "startSegmentId": "sec_energy_ladder"},
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
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Foundational Energy Taxonomy: Primary vs Secondary Energy\n        </h2>',
        '<h2 id="sec-energy-taxonomy" class="lecture-interactive-card" data-lecture-section="sec_energy_taxonomy" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Foundational Energy Taxonomy: Primary vs Secondary Energy\n        </h2>'
    )

    # Sec 2
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          The Fuelwood Crisis: Energy Poverty in Low-Income Nations\n        </h2>',
        '<h2 id="sec-fuelwood-crisis" class="lecture-interactive-card" data-lecture-section="sec_fuelwood_crisis" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          The Fuelwood Crisis: Energy Poverty in Low-Income Nations\n        </h2>'
    )

    # Sec 3
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Interactive Energy Ladder & Decarbonisation Transition\n        </h2>',
        '<h2 id="sec-energy-ladder" class="lecture-interactive-card" data-lecture-section="sec_energy_ladder" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Interactive Energy Ladder & Decarbonisation Transition\n        </h2>'
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
