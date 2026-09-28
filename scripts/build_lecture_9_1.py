import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "9_1"
LECTURE_ID = "6c14f92b-774a-45d1-a68d-2e9fe5e0b85d"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "9.1 Changing Employment Structures"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 9.1: Chuyển dịch cơ cấu lao động",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 9.1: Changing Employment Structures. In this lecture, we examine how human economies evolve: classifying jobs into primary, secondary, tertiary, and quaternary sectors, analyzing global employment maps across development tiers, mastering the Clark-Fisher transition model, interpreting triangular graphs, and tracking the complete agribusiness food product chain.",
        "vi": "Chào mừng các em đến với bài chín chấm một: Chuyển dịch cơ cấu lao động. Trong bài giảng này, chúng ta sẽ khảo sát sự tiến hóa của nền kinh tế nhân loại: phân loại việc làm thành bốn khu vực sơ cấp, thứ cấp, dịch vụ và tri thức, phân tích bản đồ cơ cấu lao động toàn cầu qua các bậc phát triển, nắm vững mô hình chuyển dịch Clark-Fisher, đọc biểu đồ tam giác, và theo dõi trọn vẹn chuỗi giá trị sản phẩm nông sản chế biến."
    },
    {
        "id": "sec_four_sectors",
        "title": "1. Bốn khu vực kinh tế",
        "selector": "#sec-four-sectors",
        "en": "Section 1 defines the four sectors of economic activity: Primary extracting raw natural resources, Secondary manufacturing finished goods, Tertiary providing commercial and personal services, and Quaternary providing high-tech research and digital knowledge.",
        "vi": "Mục một định nghĩa bốn khu vực hoạt động kinh tế: Khu vực Sơ cấp khai thác tài nguyên thiên nhiên thô, Khu vực Thứ cấp chế biến sản xuất hàng hóa, Khu vực Dịch vụ cung cấp thương mại và phục vụ đời sống, và Khu vực Tri thức nghiên cứu công nghệ cao và tri thức số."
    },
    {
        "id": "four_sectors_grid",
        "title": "Minh họa bốn khu vực kinh tế trên thế giới",
        "selector": "#card-four-sectors-grid",
        "en": "From dairy farming in New Zealand and automated grain processing in the USA, to trans-continental logistics networks and advanced biochemical laboratories, these four sectors encompass all global employment.",
        "vi": "Từ chăn nuôi bò sữa tại New Zealand và nhà máy chế biến ngũ cốc tự động hóa tại Hoa Kỳ, đến mạng lưới logistics xuyên lục địa và phòng thí nghiệm hóa sinh chuyên sâu, bốn khu vực này bao trùm toàn bộ thị trường lao động toàn cầu."
    },
    {
        "id": "sec_employment_map",
        "title": "2. Bản đồ tương tác: Cơ cấu lao động toàn cầu",
        "selector": "#sec-employment-map",
        "en": "Section 2 investigates global employment distributions: Low-Income Countries like Mali have over 65 percent of workers in agriculture, Middle-Income economies like Vietnam balance rising manufacturing with services, while High-Income nations like the UK and USA employ over 80 percent in tertiary and quaternary services.",
        "vi": "Mục hai khảo sát sự phân bố lao động toàn cầu: Các quốc gia thu nhập thấp như Mali có hơn sáu mươi lăm phần trăm lao động trong nông nghiệp, các nền kinh tế thu nhập trung bình như Việt Nam cân bằng giữa công nghiệp chế biến đang lên và dịch vụ, trong khi các nước phát triển như Anh và Hoa Kỳ tập trung hơn tám mươi phần trăm nhân lực vào dịch vụ và tri thức."
    },
    {
        "id": "employment_map_svg",
        "title": "Bản đồ phân bố cơ cấu lao động theo quốc gia",
        "selector": "#card-employment-map-svg",
        "en": "This interactive map reveals the structural contrast between agrarian subsistence economies in Sub-Saharan Africa and high-value financial, educational, and research hubs in North America and Western Europe.",
        "vi": "Bản đồ tương tác này bộc lộ sự tương phản cơ cấu sâu sắc giữa các nền kinh tế nông nghiệp tự cung tự cấp ở châu Phi cận Sahara với các trung tâm tài chính, giáo dục và công nghệ giá trị cao tại Bắc Mỹ và Tây Âu."
    },
    {
        "id": "sec_clark_fisher",
        "title": "3. Mô hình Clark-Fisher",
        "selector": "#sec-clark-fisher",
        "en": "Section 3 analyzes the Clark-Fisher Model. It traces national economic transformation through three distinct phases: the Pre-industrial agrarian stage, the Industrial manufacturing boom, and the Post-industrial service revolution.",
        "vi": "Mục ba phân tích Mô hình Clark-Fisher. Mô hình theo dõi sự chuyển mình kinh tế của một quốc gia qua ba giai đoạn riêng biệt: giai đoạn Tiền công nghiệp lấy nông nghiệp làm trụ cột, giai đoạn Bùng nổ công nghiệp chế tạo, và giai đoạn Hậu công nghiệp bùng nổ dịch vụ."
    },
    {
        "id": "clark_fisher_svg",
        "title": "Sơ đồ tương tác: Chu kỳ chuyển dịch mô hình Clark-Fisher",
        "selector": "#card-clark-fisher-svg",
        "en": "This interactive graph illustrates the historical transition curves: as agricultural mechanization releases labor, secondary factory employment surges, before automation and consumer affluence elevate tertiary and quaternary services to complete dominance.",
        "vi": "Đồ thị tương tác này minh họa các đường cong chuyển dịch lịch sử: khi cơ giới hóa nông nghiệp giải phóng sức lao động, việc làm trong nhà máy công nghiệp tăng vọt, trước khi tự động hóa và đời sống tiêu dùng nâng tầm ngành dịch vụ và tri thức chiếm lĩnh vị trí áp đảo."
    },
    {
        "id": "triangular_graph",
        "title": "Biểu đồ tam giác thể hiện cơ cấu việc làm",
        "selector": "#card-triangular-graph",
        "en": "Figure 9.11 demonstrates how geographers plot three simultaneous percentage variables on a triangular graph, allowing direct spatial comparison of employment structures across dozens of nations simultaneously.",
        "vi": "Hình chín chấm mười một minh chứng cách các nhà địa lý biểu diễn đồng thời ba biến số phần trăm trên một biểu đồ tam giác, cho phép so sánh trực quan cấu trúc việc làm của hàng chục quốc gia cùng một lúc."
    },
    {
        "id": "sec_product_chain",
        "title": "4. Chuỗi giá trị sản phẩm trong ngành thực phẩm",
        "selector": "#sec-product-chain",
        "en": "Section 4 tracks the intersectoral commodity chain using the food industry as a classic case: illustrating how raw agricultural inputs are transported, industrially refined, packaged, and retailed to modern consumers.",
        "vi": "Mục bốn theo dõi chuỗi giá trị hàng hóa liên ngành lấy công nghiệp thực phẩm làm ví dụ kinh điển: minh họa cách các nông sản thô sơ cấp được vận tải, chế biến tinh trong nhà máy, đóng gói và phân phối bán lẻ đến tay người tiêu dùng hiện đại."
    },
    {
        "id": "product_chain_svg",
        "title": "Sơ đồ chuỗi giá trị: Từ nông trại đến bàn ăn",
        "selector": "#card-product-chain-svg",
        "en": "This diagram links primary wheat farms and dairy herds, secondary flour mills and bakeries, tertiary refrigerated logistics fleets and supermarkets, and quaternary food science research developing longer shelf-life packaging.",
        "vi": "Sơ đồ này kết nối các trang trại lúa mì và bò sữa sơ cấp, nhà máy xay xát và lò bánh mì thứ cấp, đội xe lạnh và hệ thống siêu thị bán lẻ dịch vụ, cùng các phòng nghiên cứu khoa học thực phẩm tri thức phát triển bao bì sinh học bảo quản dài lâu."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_four_sectors", "title": "1. Bốn khu vực kinh tế", "startSegmentId": "sec_four_sectors"},
    {"id": "sec_employment_map", "title": "2. Cơ cấu lao động toàn cầu", "startSegmentId": "sec_employment_map"},
    {"id": "sec_clark_fisher", "title": "3. Mô hình Clark-Fisher", "startSegmentId": "sec_clark_fisher"},
    {"id": "sec_product_chain", "title": "4. Chuỗi sản phẩm ngành thực phẩm", "startSegmentId": "sec_product_chain"}
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
        '<h2>1. The Four Economic Sectors</h2>',
        '<h2 id="sec-four-sectors" class="lecture-interactive-card" data-lecture-section="sec_four_sectors" style="cursor:pointer;">1. The Four Economic Sectors</h2>'
    )
    html = html.replace(
        '<div class="image-grid">',
        '<div id="card-four-sectors-grid" class="lecture-interactive-card image-grid" data-lecture-section="four_sectors_grid" style="cursor:pointer;">'
    )

    # Sec 2
    html = html.replace(
        '<h2>2. Interactive Map: Employment Structures Globally</h2>',
        '<h2 id="sec-employment-map" class="lecture-interactive-card" data-lecture-section="sec_employment_map" style="cursor:pointer;">2. Interactive Map: Employment Structures Globally</h2>'
    )
    html = html.replace(
        '<div class="interactive-svg-container">',
        '<div id="card-employment-map-svg" class="lecture-interactive-card interactive-svg-container" data-lecture-section="employment_map_svg" style="cursor:pointer;">'
    )

    # Sec 3
    html = html.replace(
        '<h2>3. The Clark-Fisher Model</h2>',
        '<h2 id="sec-clark-fisher" class="lecture-interactive-card" data-lecture-section="sec_clark_fisher" style="cursor:pointer;">3. The Clark-Fisher Model</h2>'
    )
    html = html.replace(
        '<div class="interactive-svg-container" style="text-align: center;">',
        '<div id="card-clark-fisher-svg" class="lecture-interactive-card interactive-svg-container" data-lecture-section="clark_fisher_svg" style="text-align: center; cursor:pointer;">'
    )

    # Triangular graph
    target_tri = '<div class="img-box" style="margin:24px 0; text-align:center;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_11.png'
    repl_tri = '<div id="card-triangular-graph" class="lecture-interactive-card img-box" data-lecture-section="triangular_graph" style="margin:24px 0; text-align:center; cursor:pointer;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_11.png'
    html = html.replace(target_tri, repl_tri)

    # Sec 4
    html = html.replace(
        "<h2>4. The Food Industry's Product Chain</h2>",
        '<h2 id="sec-product-chain" class="lecture-interactive-card" data-lecture-section="sec_product_chain" style="cursor:pointer;">4. The Food Industry\'s Product Chain</h2>'
    )
    html = html.replace(
        '<div class="interactive-svg-container" style="text-align: center; background: #fffbeb; border-color: #fde68a;">',
        '<div id="card-product-chain-svg" class="lecture-interactive-card interactive-svg-container" data-lecture-section="product_chain_svg" style="text-align: center; background: #fffbeb; border-color: #fde68a; cursor:pointer;">'
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
