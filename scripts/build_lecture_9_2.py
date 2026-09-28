import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "9_2"
LECTURE_ID = "5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "9.2 The Impact of Globalisation and Transnational Corporations"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 9.2: Tác động của Toàn cầu hóa và các Tập đoàn Đa quốc gia",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 9.2: The Impact of Globalisation and the Role of Transnational Corporations. In this lecture, we examine the interconnected modern world: defining globalisation drivers from containerisation to fiber-optic cables, analyzing the organizational structure of Transnational Corporations, tracing Nike's global footwear value chain, and critically evaluating host and origin country trade-offs.",
        "vi": "Chào mừng các em đến với bài chín chấm hai: Tác động của Toàn cầu hóa và Vai trò của các Tập đoàn Đa quốc gia TNC. Trong bài giảng này, chúng ta sẽ khảo sát thế giới hiện đại siêu kết nối: xác định các động lực toàn cầu hóa từ vận tải container đến cáp quang internet, phân tích cơ cấu tổ chức của các tập đoàn đa quốc gia, lần theo chuỗi cung ứng giày dép toàn cầu của Nike, và đánh giá sắc bén tác động hai chiều giữa quốc gia bản địa và quốc gia sở tại."
    },
    {
        "id": "sec_globalisation",
        "title": "1. Toàn cầu hóa và các đặc trưng cốt lõi",
        "selector": "#sec-globalisation",
        "en": "Section 1 defines globalisation as the growing interdependence and integration of the world's economies, cultures, and populations, driven by cross-border trade in goods, international flows of capital, and rapid transmission of information.",
        "vi": "Mục một định nghĩa toàn cầu hóa là sự gia tăng tính phụ thuộc lẫn nhau và hội nhập giữa các nền kinh tế, văn hóa và cộng đồng trên khắp thế giới, được thúc đẩy bởi thương mại hàng hóa xuyên biên giới, các dòng vốn quốc tế và sự lan truyền thông tin tức thời."
    },
    {
        "id": "globalisation_factors",
        "title": "Các nhân tố thúc đẩy toàn cầu hóa kinh tế",
        "selector": "#card-globalisation-factors",
        "en": "Figure 9.22 illustrates the accelerating engines of globalisation: standard 20-foot shipping containers slashing freight costs, deregulation and free trade agreements, jet travel, and instant satellite telecommunications.",
        "vi": "Hình chín chấm hai mươi hai minh họa các động cơ tăng tốc của toàn cầu hóa: container tiêu chuẩn hai mươi feet cắt giảm mạnh chi phí vận tải biển, xóa bỏ hàng rào thuế quan qua các hiệp định thương mại tự do, hàng không phản lực giá rẻ và mạng lưới viễn thông vệ tinh thời gian thực."
    },
    {
        "id": "sec_what_is_tnc",
        "title": "2. Tập đoàn Đa quốc gia (TNC) là gì?",
        "selector": "#sec-what-is-tnc",
        "en": "Section 2 explores Transnational Corporations: giant enterprises that manage production facilities or deliver services across multiple countries, leveraging spatial margins of profitability to maximize shareholder returns.",
        "vi": "Mục hai nghiên cứu các Tập đoàn Đa quốc gia TNC: những doanh nghiệp khổng lồ điều hành các cơ sở sản xuất hoặc cung ứng dịch vụ tại nhiều quốc gia khác nhau, tận dụng lợi thế so sánh không gian để tối đa hóa lợi nhuận cho cổ đông."
    },
    {
        "id": "tnc_structure_svg",
        "title": "Sơ đồ cấu trúc phân công không gian của TNC",
        "selector": "#card-tnc-structure-svg",
        "en": "This diagram reveals the classic spatial division of labor: Corporate headquarters, strategic research and development, and executive branding remain rooted in high-income home countries, while labor-intensive assembly is outsourced to low-wage developing nations.",
        "vi": "Sơ đồ này bộc lộ sự phân công lao động không gian kinh điển: Trụ sở đầu não, nghiên cứu phát triển R&D chiến lược và thương hiệu giữ ở các nước phát triển giàu có, trong khi các công đoạn lắp ráp thâm dụng lao động được gia công sang các nước đang phát triển có chi phí nhân công thấp."
    },
    {
        "id": "sec_nike_supply_chain",
        "title": "3. Bản đồ tương tác: Chuỗi cung ứng toàn cầu của Nike",
        "selector": "#sec-nike-supply-chain",
        "en": "Section 3 investigates Nike as the quintessential case study: headquartered in Beaverton, Oregon, but manufacturing virtually 100 percent of its athletic footwear across contracted mega-factories in Vietnam, Indonesia, and China.",
        "vi": "Mục ba khảo sát hãng Nike như một trường hợp điển hình: đặt đại bản doanh tại Beaverton bang Oregon Hoa Kỳ, nhưng gia công gần như một trăm phần trăm sản lượng giày thể thao tại các đại công xưởng liên kết ở Việt Nam, Indonesia và Trung Quốc."
    },
    {
        "id": "nike_map_svg",
        "title": "Bản đồ chuỗi cung ứng và logistics toàn cầu của Nike",
        "selector": "#card-nike-map-svg",
        "en": "This interactive map tracks Nike's global web: design patents originating in Oregon, synthetic rubber and leather sourced across Southeast Asia, assembly in Ho Chi Minh City, and containerized distribution to retail markets worldwide.",
        "vi": "Bản đồ tương tác này theo dõi mạng lưới toàn cầu của Nike: bản quyền thiết kế khởi nguồn tại Oregon, cao su tổng hợp và da thu mua khắp Đông Nam Á, lắp ráp hoàn thiện tại Thành phố Hồ Chí Minh, và đóng container xuất khẩu đến các thị trường bán lẻ toàn cầu."
    },
    {
        "id": "sec_tnc_impacts",
        "title": "4. Tác động đa chiều của các tập đoàn TNC",
        "selector": "#sec-tnc-impacts",
        "en": "Section 4 critically balances TNC impacts: host countries gain formal manufacturing jobs, foreign currency, and infrastructure upgrades, but risk economic leakage of profits back to Western headquarters, sweatshop working conditions, and environmental pollution.",
        "vi": "Mục bốn đánh giá khách quan các tác động đa chiều của TNC: các nước tiếp nhận có thêm hàng triệu việc làm công nghiệp, nguồn thu ngoại tệ và cơ sở hạ tầng, nhưng đối mặt nguy cơ chảy máu lợi nhuận về các công ty mẹ ở phương Tây, điều kiện lao động áp lực và ô nhiễm môi trường."
    },
    {
        "id": "tnc_impacts_list",
        "title": "Bảng tổng hợp: Tác động tích cực và tiêu cực của TNC",
        "selector": "#card-tnc-impacts-list",
        "en": "This comparative summary provides essential balance for Cambridge exams: contrasting employment generation and technology transfer against footloose mobility, tax avoidance, and environmental exploitation.",
        "vi": "Bảng tổng hợp đối chiếu này cung cấp góc nhìn cân bằng cốt lõi cho kỳ thi Cambridge: so sánh giữa tạo việc làm và chuyển giao công nghệ với tính chất doanh nghiệp dễ dịch chuyển footloose, né tránh thuế và khai thác kiệt quệ tài nguyên môi trường."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_globalisation", "title": "1. Toàn cầu hóa & Động lực thúc đẩy", "startSegmentId": "sec_globalisation"},
    {"id": "sec_what_is_tnc", "title": "2. Cấu trúc tập đoàn đa quốc gia", "startSegmentId": "sec_what_is_tnc"},
    {"id": "sec_nike_supply_chain", "title": "3. Chuỗi cung ứng toàn cầu của Nike", "startSegmentId": "sec_nike_supply_chain"},
    {"id": "sec_tnc_impacts", "title": "4. Tác động đa chiều của TNC", "startSegmentId": "sec_tnc_impacts"}
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
        '<h2>1. Globalisation and its key features</h2>',
        '<h2 id="sec-globalisation" class="lecture-interactive-card" data-lecture-section="sec_globalisation" style="cursor:pointer;">1. Globalisation and its key features</h2>'
    )
    target_f22 = '<div class="img-box" style="margin:24px 0; text-align:center;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_22.png'
    repl_f22 = '<div id="card-globalisation-factors" class="lecture-interactive-card img-box" data-lecture-section="globalisation_factors" style="margin:24px 0; text-align:center; cursor:pointer;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t9_fig_9_22.png'
    html = html.replace(target_f22, repl_f22)

    # Sec 2
    html = html.replace(
        '<h2>2. What is a Transnational Corporation (TNC)?</h2>',
        '<h2 id="sec-what-is-tnc" class="lecture-interactive-card" data-lecture-section="sec_what_is_tnc" style="cursor:pointer;">2. What is a Transnational Corporation (TNC)?</h2>'
    )
    html = html.replace(
        '<div class="interactive-svg-container" style="text-align: center;">',
        '<div id="card-tnc-structure-svg" class="lecture-interactive-card interactive-svg-container" data-lecture-section="tnc_structure_svg" style="text-align: center; cursor:pointer;">'
    )

    # Sec 3
    html = html.replace(
        "<h2>3. Interactive Map: Nike's Global Supply Chain</h2>",
        '<h2 id="sec-nike-supply-chain" class="lecture-interactive-card" data-lecture-section="sec_nike_supply_chain" style="cursor:pointer;">3. Interactive Map: Nike\'s Global Supply Chain</h2>'
    )
    html = html.replace(
        '<div class="interactive-svg-container">',
        '<div id="card-nike-map-svg" class="lecture-interactive-card interactive-svg-container" data-lecture-section="nike_map_svg" style="cursor:pointer;">'
    )

    # Sec 4
    html = html.replace(
        '<h2>4. Impacts of TNCs</h2>',
        '<h2 id="sec-tnc-impacts" class="lecture-interactive-card" data-lecture-section="sec_tnc_impacts" style="cursor:pointer;">4. Impacts of TNCs</h2>'
    )
    html = html.replace(
        '<div class="card-list">',
        '<div id="card-tnc-impacts-list" class="lecture-interactive-card card-list" data-lecture-section="tnc_impacts_list" style="cursor:pointer;">'
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
