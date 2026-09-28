import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "9_3"
LECTURE_ID = "53517557-9eb4-450d-a8dd-18b73c71938a"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "9.3 Tourism is a Growing Industry"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 9.3: Ngành du lịch đang tăng trưởng mạnh mẽ",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 9.3: Tourism is a Growing Industry. In this lecture, we explore global tertiary leisure travel: identifying the catalysts driving exponential tourist growth, interpreting Butler's Tourism Area Life Cycle model, analyzing intercontinental holiday flows, categorizing tourism niches, evaluating economic, social, and environmental impacts via the EVE framework, and investigating ecotourism strategies through the case study of Jamaica.",
        "vi": "Chào mừng các em đến với bài chín chấm ba: Du lịch là một ngành kinh tế đang tăng trưởng. Trong bài học này, chúng ta sẽ khảo sát ngành du lịch dịch vụ toàn cầu: nhận diện các chất xúc tác thúc đẩy lượng khách quốc tế tăng vọt, phân tích mô hình Chu kỳ khu du lịch của Butler, theo dõi các luồng du khách liên lục địa, phân loại các phân khúc du lịch, đánh giá tác động kinh tế, xã hội và môi trường qua khung EVE, đồng thời tìm hiểu các chiến lược phát triển du lịch sinh thái qua nghiên cứu tình huống Jamaica."
    },
    {
        "id": "sec_growth_tourism",
        "title": "1. Sự tăng trưởng bùng nổ của ngành du lịch toàn cầu",
        "selector": "#sec-growth-tourism",
        "en": "Section 1 examines why global international tourism surpassed 1.4 billion arrivals annually: propelled by rising disposable incomes, paid annual leave, budget airlines like Ryanair and AirAsia, and the democratization of internet booking platforms.",
        "vi": "Mục một phân tích lý do du lịch quốc tế vượt mốc một phẩy bốn tỉ lượt khách mỗi năm: được thúc đẩy bởi thu nhập khả dụng ngày càng cao, chế độ nghỉ phép có lương, các hãng hàng không giá rẻ như Ryanair và AirAsia, cùng sự phổ cập của các nền tảng đặt phòng trực tuyến."
    },
    {
        "id": "butler_model",
        "title": "Mô hình chu kỳ phát triển điểm du lịch của Butler",
        "selector": "#card-butler-model",
        "en": "Figure 9.37 displays Butler's Tourism Area Life Cycle: tracking destinations from initial Exploration and Local Involvement, through rapid Development and Consolidation, to the critical crossroad of Stagnation, where locations either Rejuvenate through sustainable reinvention or enter terminal Decline.",
        "vi": "Hình chín chấm ba mươi bảy minh họa Chu kỳ khu du lịch của Butler: theo dõi các điểm đến từ giai đoạn Thám sát ban đầu và Sự tham gia của địa phương, qua Phát triển nhanh và Ổn định vững chắc, đến ngã ba đường Ngưng trệ then chốt, nơi điểm du lịch hoặc sẽ Trẻ hóa nhờ đổi mới bền vững hoặc rơi vào Suy tàn kiệt quệ."
    },
    {
        "id": "sec_tourism_flows",
        "title": "2. Bản đồ tương tác: Các luồng du lịch toàn cầu",
        "selector": "#sec-tourism-flows",
        "en": "Section 2 maps spatial movements: Mediterranean sun-and-sand migratory corridors from Northern Europe, winter sun migrations to the Caribbean and Florida, and explosive outbound tourism surges from China into Southeast Asia.",
        "vi": "Mục hai phác họa các dòng di chuyển không gian: hành lang nghỉ dưỡng biển Địa Trung Hải từ Bắc Âu đổ xuống, các chuyến tránh đông tới vùng biển Caribe và bang Florida, cùng làn sóng khách du lịch nước ngoài bùng nổ từ Trung Quốc sang khắp Đông Nam Á."
    },
    {
        "id": "tourism_flows_svg",
        "title": "Bản đồ tương tác dòng khách du lịch quốc tế",
        "selector": "#card-tourism-flows-svg",
        "en": "This interactive map reveals global tourism corridors: contrasting high-density seasonal beach migrations against emerging eco-safari trails and adventure trekking routes across the developing world.",
        "vi": "Bản đồ tương tác này thể hiện các hành lang du lịch quốc tế: đối chiếu các dòng du khách bãi biển theo mùa mật độ cao với các tour du lịch sinh thái hoang dã và tuyến leo núi mạo hiểm đang nở rộ tại các quốc gia đang phát triển."
    },
    {
        "id": "sec_types_tourism",
        "title": "3. Các loại hình du lịch",
        "selector": "#sec-types-tourism",
        "en": "Section 3 classifies diverse travel motivations: Coastal mass tourism, Cultural and heritage tourism exploring historical landmarks, Eco-tourism prioritizing wildlife conservation, and Adventure tourism seeking physical thrills.",
        "vi": "Mục ba phân loại các động cơ du lịch đa dạng: Du lịch đại chúng nghỉ dưỡng bờ biển, Du lịch văn hóa di sản khám phá các di tích lịch sử, Du lịch sinh thái ưu tiên bảo tồn thiên nhiên hoang dã, và Du lịch mạo hiểm trải nghiệm cảm giác mạnh."
    },
    {
        "id": "sec_impacts_tourism",
        "title": "4. Tác động của du lịch: Khung phân tích EVE",
        "selector": "#sec-impacts-tourism",
        "en": "Section 4 assesses multi-dimensional impacts using the EVE framework: evaluating Economic benefits against leakages, Social cultural exchanges against commercialization of traditions, and Environmental revenues against habitat destruction.",
        "vi": "Mục bốn đánh giá các tác động đa chiều qua khung phân tích EVE: so sánh lợi ích Kinh tế với thất thoát doanh thu ra nước ngoài, giao lưu Xã hội văn hóa với thương mại hóa truyền thống, cùng nguồn thu môi trường với hiểm họa phá hủy sinh cảnh."
    },
    {
        "id": "impacts_grid",
        "title": "Bảng tổng hợp: Tác động Kinh tế, Xã hội và Môi trường",
        "selector": "#card-impacts-grid",
        "en": "This matrix breaks down key trade-offs: massive foreign exchange and multiplier effects versus severe economic leakage where up to 80 percent of all-inclusive package revenues flow directly back to foreign tour operators and hotel chains.",
        "vi": "Bảng ma trận này bóc tách các mặt đối lập cốt lõi: nguồn thu ngoại tệ khổng lồ và hiệu ứng nhân tử đối mặt với tình trạng rò rỉ kinh tế nghiêm trọng khi có tới tám mươi phần trăm doanh thu tour trọn gói chảy ngược về túi các hãng lữ hành và chuỗi khách sạn nước ngoài."
    },
    {
        "id": "sec_sustainable_tourism",
        "title": "5. Du lịch bền vững và Nghiên cứu tình huống: Jamaica",
        "selector": "#sec-sustainable-tourism",
        "en": "Section 5 presents sustainable management frameworks, spotlighting Jamaica's transition towards eco-tourism: zoning marine parks, instituting reef protection ordinances, and channeling visitor entry levies into local rainforest preservation.",
        "vi": "Mục năm trình bày các khung quản lý du lịch bền vững, làm nổi bật bước chuyển của Jamaica sang du lịch sinh thái: phân vùng các công viên hải dương, ban hành quy chế bảo vệ rạn san hô, và trích phí tham quan để tài trợ trực tiếp cho các dự án bảo tồn rừng nhiệt đới của cộng đồng bản địa."
    },
    {
        "id": "jamaica_case_study",
        "title": "Nghiên cứu tình huống: Công viên Quốc gia và Hải dương tại Jamaica",
        "selector": "#card-jamaica-case-study",
        "en": "Figure 9.47 highlights Jamaica's protected conservation networks: Montego Bay Marine Park and the Blue and John Crow Mountains, demonstrating how community-managed ecotourism creates sustainable ranger jobs while protecting fragile biodiversity.",
        "vi": "Hình chín chấm bốn mươi bảy làm nổi bật mạng lưới bảo tồn của Jamaica: Công viên Hải dương Vịnh Montego và Vườn quốc gia dãy núi Blue và John Crow, minh chứng cho việc du lịch sinh thái do cộng đồng quản lý đã tạo ra việc làm kiểm lâm bền vững trong khi bảo vệ đa dạng sinh học mong manh."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_growth_tourism", "title": "1. Sự tăng trưởng của du lịch", "startSegmentId": "sec_growth_tourism"},
    {"id": "sec_tourism_flows", "title": "2. Các luồng du lịch toàn cầu", "startSegmentId": "sec_tourism_flows"},
    {"id": "sec_types_tourism", "title": "3. Các loại hình du lịch", "startSegmentId": "sec_types_tourism"},
    {"id": "sec_impacts_tourism", "title": "4. Tác động của du lịch (EVE)", "startSegmentId": "sec_impacts_tourism"},
    {"id": "sec_sustainable_tourism", "title": "5. Du lịch bền vững: Jamaica", "startSegmentId": "sec_sustainable_tourism"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Header
    html = html.replace(
        '<div style="text-align: center; margin-bottom: 30px;">',
        '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="text-align: center; margin-bottom: 30px; cursor:pointer;">'
    )

    # Sec 1
    html = html.replace(
        '<h2>1. The Global Growth of Tourism</h2>',
        '<h2 id="sec-growth-tourism" class="lecture-interactive-card" data-lecture-section="sec_growth_tourism" style="cursor:pointer;">1. The Global Growth of Tourism</h2>'
    )
    target_butler = '<div class="img-box" style="margin:24px 0; text-align:center;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_37.png'
    repl_butler = '<div id="card-butler-model" class="lecture-interactive-card img-box" data-lecture-section="butler_model" style="margin:24px 0; text-align:center; cursor:pointer;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_37.png'
    html = html.replace(target_butler, repl_butler)

    # Sec 2
    html = html.replace(
        '<h2>2. Interactive Map: Global Tourism Flows</h2>',
        '<h2 id="sec-tourism-flows" class="lecture-interactive-card" data-lecture-section="sec_tourism_flows" style="cursor:pointer;">2. Interactive Map: Global Tourism Flows</h2>'
    )
    html = html.replace(
        '<div class="interactive-svg-container">',
        '<div id="card-tourism-flows-svg" class="lecture-interactive-card interactive-svg-container" data-lecture-section="tourism_flows_svg" style="cursor:pointer;">'
    )

    # Sec 3
    html = html.replace(
        '<h2>3. Types of Tourism</h2>',
        '<h2 id="sec-types-tourism" class="lecture-interactive-card" data-lecture-section="sec_types_tourism" style="cursor:pointer;">3. Types of Tourism</h2>'
    )

    # Sec 4
    html = html.replace(
        '<h2>4. Impacts of Tourism (EVE framework)</h2>',
        '<h2 id="sec-impacts-tourism" class="lecture-interactive-card" data-lecture-section="sec_impacts_tourism" style="cursor:pointer;">4. Impacts of Tourism (EVE framework)</h2>'
    )
    html = html.replace(
        '<div class="card-grid">',
        '<div id="card-impacts-grid" class="lecture-interactive-card card-grid" data-lecture-section="impacts_grid" style="cursor:pointer;">'
    )

    # Sec 5
    html = html.replace(
        '<h2>5. Sustainable Tourism</h2>',
        '<h2 id="sec-sustainable-tourism" class="lecture-interactive-card" data-lecture-section="sec_sustainable_tourism" style="cursor:pointer;">5. Sustainable Tourism</h2>'
    )
    target_jam = '<div class="img-box" style="margin:24px 0; text-align:center;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_47.png'
    repl_jam = '<div id="card-jamaica-case-study" class="lecture-interactive-card img-box" data-lecture-section="jamaica_case_study" style="margin:24px 0; text-align:center; cursor:pointer;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_47.png'
    html = html.replace(target_jam, repl_jam)

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
