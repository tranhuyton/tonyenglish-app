import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "8_3"
LECTURE_ID = "7da208d1-559d-4e60-a6a3-ebfb8c2d232f"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "8.3 Achieving Sustainable Development"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 8.3: Đạt được sự phát triển bền vững",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 8.3: Achieving Sustainable Development. In this lecture, we examine solutions to balance human progress with planetary boundaries: exploring the UN Sustainable Development Goals, mastering Circular Economy loops and the Environmental Kuznets Curve, evaluating international aid versus Fair Trade, and analyzing how Indonesia balances nickel mining industrialization against rainforest conservation.",
        "vi": "Chào mừng các em đến với bài tám chấm ba: Đạt được sự phát triển bền vững. Trong bài giảng này, chúng ta sẽ khảo sát các giải pháp cân bằng giữa tiến bộ nhân loại và giới hạn sinh thái của hành tinh: tìm hiểu các Mục tiêu Phát triển Bền vững của Liên Hợp Quốc, nắm vững chu trình Kinh tế tuần hoàn và Đường cong Kuznets môi trường, đánh giá viện trợ quốc tế so với Thương mại công bằng Fair Trade, đồng thời phân tích cách Indonesia dung hòa giữa công nghiệp chế biến quặng niken với bảo tồn rừng nhiệt đới."
    },
    {
        "id": "sec_three_pillars",
        "title": "1. Ba trụ cột bền vững và 17 Mục tiêu SDG",
        "selector": "#sec-three-pillars",
        "en": "Section 1 establishes the tripartite foundation of sustainable development: Economic viability, Social equity, and Environmental stewardship. In 2015, the United Nations codified these into 17 Sustainable Development Goals targeting absolute poverty eradication and climate action by 2030.",
        "vi": "Mục một thiết lập nền tảng tam giác của phát triển bền vững: Hiệu quả kinh tế, Công bằng xã hội, và Bảo vệ môi trường sinh thái. Năm 2015, Liên Hợp Quốc đã cụ thể hóa các trụ cột này thành mười bảy Mục tiêu Phát triển Bền vững SDG hướng tới xóa nghèo cùng cực và hành động vì khí hậu vào năm 2030."
    },
    {
        "id": "sec_environmental_sustainability",
        "title": "2. Bền vững môi trường: Kinh tế tuần hoàn và Đường cong Kuznets",
        "selector": "#sec-environmental-sustainability",
        "en": "Section 2 investigates systemic economic models for environmental protection, contrasting obsolete linear 'take-make-dispose' industrial systems against regenerative circular loops, and evaluating the Environmental Kuznets Curve hypothesis.",
        "vi": "Mục hai nghiên cứu các mô hình kinh tế mang tính hệ thống để bảo vệ môi trường, đối chiếu chu trình công nghiệp tuyến tính lỗi thời 'khai thác - sản xuất - vứt bỏ' với mô hình kinh tế tuần hoàn tái sinh, và đánh giá giả thuyết Đường cong Kuznets môi trường."
    },
    {
        "id": "circular_kuznets_svg",
        "title": "Sơ đồ: Vòng lặp kinh tế tuần hoàn và Đường cong Kuznets môi trường",
        "selector": "#card-circular-kuznets-svg",
        "en": "This diagram illustrates how circular loops eliminate waste through industrial symbiosis and remanufacturing, alongside the Environmental Kuznets Curve which shows environmental degradation peaking before declining as higher incomes fund clean technology.",
        "vi": "Sơ đồ này minh họa cách vòng lặp tuần hoàn triệt tiêu rác thải thông qua cộng sinh công nghiệp và tái chế, đồng thời biểu thị Đường cong Kuznets môi trường cho thấy mức độ ô nhiễm đạt đỉnh rồi suy giảm khi thu nhập cao hơn cho phép đầu tư công nghệ sạch."
    },
    {
        "id": "sec_aid_microfinance",
        "title": "3. Viện trợ quốc tế, Tài chính vi mô và Thương mại công bằng",
        "selector": "#sec-aid-microfinance",
        "en": "Section 3 evaluates development finance mechanisms: bilateral and multilateral emergency humanitarian aid versus long-term development assistance, grassroots Grameen microfinance empowering female entrepreneurs, and the Fairtrade certification model.",
        "vi": "Mục ba đánh giá các cơ chế tài chính phát triển: viện trợ nhân đạo khẩn cấp song phương và đa phương so với viện trợ phát triển dài hạn, mô hình tài chính vi mô Grameen trao quyền cho phụ nữ khởi nghiệp, cùng chuỗi giá trị Thương mại công bằng Fairtrade."
    },
    {
        "id": "aid_fairtrade_svg",
        "title": "Sơ đồ: Các kênh viện trợ quốc tế và Chuỗi giá trị Fairtrade",
        "selector": "#card-aid-fairtrade-svg",
        "en": "This visual architecture maps official development assistance flows while detailing how Fairtrade guarantees a minimum price floor and social premiums directly to farming cooperatives, shielding smallholders from commodity market collapse.",
        "vi": "Sơ đồ cấu trúc này phác họa các dòng viện trợ phát triển chính thức, đồng thời chi tiết hóa cách Fairtrade bảo đảm mức giá sàn tối thiểu và trao quỹ thưởng xã hội trực tiếp cho các hợp tác xã nông dân, bảo vệ các hộ sản xuất nhỏ trước sự sụt giá nông sản toàn cầu."
    },
    {
        "id": "sec_indonesia_casestudy",
        "title": "4. Nghiên cứu tình huống chi tiết: Indonesia",
        "selector": "#sec-indonesia-casestudy",
        "en": "Section 4 examines Indonesia, Southeast Asia's largest economy. With a population of 275 million spread across thousands of islands, Indonesia showcases the delicate balance between rapid industrialization and ecological stewardship.",
        "vi": "Mục bốn nghiên cứu Indonesia, nền kinh tế lớn nhất Đông Nam Á. Với quy mô dân số hai trăm bảy mươi lăm triệu người trải dài trên hàng ngàn hòn đảo, Indonesia là minh chứng điển hình cho sự cân bằng mong manh giữa công nghiệp hóa vũ bão và bảo tồn sinh thái."
    },
    {
        "id": "indonesia_drivers",
        "title": "Các động lực chính trong chiến lược phát triển bền vững của Indonesia",
        "selector": "#card-indonesia-drivers",
        "en": "Key Indonesian strategies include the downstreaming mineral mandate banning raw nickel exports to build domestic electric vehicle battery industries, the historic moratorium on primary palm oil deforestation, and the monumental relocation of the sinking capital Jakarta to the planned green smart city Nusantara.",
        "vi": "Các chiến lược trọng yếu của Indonesia gồm chính sách hạ nguồn cấm xuất khẩu quặng niken thô để xây dựng chuỗi công nghiệp pin xe điện trong nước, lệnh tạm đình chỉ cấp phép phá rừng nguyên sinh để trồng cọ dầu, và quyết định lịch sử di dời thủ đô Jakarta đang lún sụt sang thành phố thông minh sinh thái Nusantara."
    },
    {
        "id": "exam_summary",
        "title": "Tổng kết trọng tâm ôn thi Cambridge IGCSE: Chủ đề 8.3",
        "selector": "#card-exam-summary",
        "en": "For exam 7-mark case study questions, always critique aid dependency versus self-reliance, describe how Fairtrade premiums build local schools and wells, and use Indonesia's nickel downstreaming policy to demonstrate how emerging nations capture value locally while managing environmental trade-offs.",
        "vi": "Trong các câu hỏi tình huống bảy điểm, các em hãy luôn phân tích mặt trái của sự phụ thuộc viện trợ so với tự chủ kinh tế, mô tả cách quỹ phúc lợi Fairtrade xây dựng trường học và giếng nước sạch, đồng thời dùng chính sách hạ nguồn quặng niken của Indonesia để minh họa cách các nước mới nổi gia tăng giá trị kinh tế đi đôi với quản lý đánh đổi môi trường."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_three_pillars", "title": "1. Ba trụ cột bền vững & 17 SDG", "startSegmentId": "sec_three_pillars"},
    {"id": "sec_environmental_sustainability", "title": "2. Kinh tế tuần hoàn & Đường cong Kuznets", "startSegmentId": "sec_environmental_sustainability"},
    {"id": "sec_aid_microfinance", "title": "3. Viện trợ quốc tế & Fairtrade", "startSegmentId": "sec_aid_microfinance"},
    {"id": "sec_indonesia_casestudy", "title": "4. Nghiên cứu tình huống: Indonesia", "startSegmentId": "sec_indonesia_casestudy"},
    {"id": "card_exam_summary", "title": "Trọng tâm ôn thi Cambridge", "startSegmentId": "exam_summary"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px;">1. The Three Pillars of Sustainability & The 17 SDGs</h2>',
        '<h2 id="sec-three-pillars" class="lecture-interactive-card" data-lecture-section="sec_three_pillars" style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">1. The Three Pillars of Sustainability & The 17 SDGs</h2>'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px;">2. Environmental Sustainability: Circular Economy & The Kuznets Curve</h2>',
        '<h2 id="sec-environmental-sustainability" class="lecture-interactive-card" data-lecture-section="sec_environmental_sustainability" style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">2. Environmental Sustainability: Circular Economy & The Kuznets Curve</h2>'
    )

    # Circular Economy & Kuznets SVG Card
    target_circular = '<div style="margin: 28px 0; background: #ffffff; border: 1px solid #a7f3d0; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">'
    repl_circular = '<div id="card-circular-kuznets-svg" class="lecture-interactive-card" data-lecture-section="circular_kuznets_svg" style="margin: 28px 0; background: #ffffff; border: 1px solid #a7f3d0; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">'
    html = html.replace(target_circular, repl_circular)

    # Section 3 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px;">3. International Aid, Microfinance & Fair Trade</h2>',
        '<h2 id="sec-aid-microfinance" class="lecture-interactive-card" data-lecture-section="sec_aid_microfinance" style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">3. International Aid, Microfinance & Fair Trade</h2>'
    )

    # Aid Channels vs Fairtrade SVG Card
    target_aid = '<div style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">'
    repl_aid = '<div id="card-aid-fairtrade-svg" class="lecture-interactive-card" data-lecture-section="aid_fairtrade_svg" style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">'
    html = html.replace(target_aid, repl_aid)

    # Section 4 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px;">4. Detailed Specific Example: Indonesia - An Emerging Economy Navigating Growth</h2>',
        '<h2 id="sec-indonesia-casestudy" class="lecture-interactive-card" data-lecture-section="sec_indonesia_casestudy" style="font-size: 24px; font-weight: 800; color: #065f46; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">4. Detailed Specific Example: Indonesia - An Emerging Economy Navigating Growth</h2>'
    )

    # Indonesia Drivers Heading
    html = html.replace(
        '<h3 style="font-size: 18px; font-weight: 700; color: #064e3b; margin-top: 24px;">Key Drivers of Indonesia\'s Sustainable Development Strategy:</h3>',
        '<h3 id="card-indonesia-drivers" class="lecture-interactive-card" data-lecture-section="indonesia_drivers" style="font-size: 18px; font-weight: 700; color: #064e3b; margin-top: 24px; cursor:pointer;">Key Drivers of Indonesia\'s Sustainable Development Strategy:</h3>'
    )

    # Exam Summary Card
    html = html.replace(
        '<div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-top: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">',
        '<div id="card-exam-summary" class="lecture-interactive-card" data-lecture-section="exam_summary" style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-top: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">'
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
