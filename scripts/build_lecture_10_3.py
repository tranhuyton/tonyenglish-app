import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_3"
LECTURE_ID = "96d7f427-3b6d-43e3-84dc-f8f052f20033"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.3 The Challenges of Food Supply: Insecurity & Solutions"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10.3: Thách thức An ninh Lương thực và Giải pháp",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 10.3: The Challenges of Food Supply: Insecurity & Solutions. In this lecture, we tackle global hunger: defining the four pillars of food security, contrasting Malthusian catastrophe against Boserupian agricultural innovation, investigating the complex drivers of Nigeria's food crisis, and evaluating sustainable solutions including terracing, shelterbelts, and drip irrigation.",
        "vi": "Chào mừng các em đến với bài mười chấm ba: Thách thức An ninh Lương thực và Giải pháp. Trong bài giảng này, chúng ta sẽ đi sâu vào bài toán đói nghèo toàn cầu: định nghĩa bốn trụ cột của an ninh lương thực, đối chiếu thảm họa nhân khẩu học Malthus với sự đổi mới sáng tạo nông nghiệp theo Boserup, điều tra các nguyên nhân phức tạp dẫn tới cuộc khủng hoảng lương thực tại Nigeria, và đánh giá các giải pháp canh tác bền vững bao gồm ruộng bậc thang, đai rừng chắn gió và tưới nhỏ giọt."
    },
    {
        "id": "sec_food_security",
        "title": "1. Định nghĩa An ninh Lương thực và Đo lường nạn đói toàn cầu",
        "selector": "#sec-food-security",
        "en": "Section 1 establishes the FAO definition of food security: when all people, at all times, have physical, social, and economic access to sufficient, safe, and nutritious food to meet their dietary needs for an active, healthy life. It rests on four pillars: Availability, Access, Utilization, and Stability.",
        "vi": "Mục một thiết lập định nghĩa chuẩn của FAO về an ninh lương thực: khi mọi người ở mọi thời điểm đều có quyền tiếp cận thể chất, xã hội và kinh tế đối với nguồn thực phẩm đầy đủ, an toàn và bổ dưỡng nhằm đáp ứng nhu cầu bữa ăn cho một cuộc sống khỏe mạnh, năng động. An ninh lương thực dựa trên bốn trụ cột: Tính sẵn có, Khả năng tiếp cận, Mức độ sử dụng, và Tính ổn định."
    },
    {
        "id": "sec_insecurity_hotspots",
        "title": "2. Điểm nóng mất an ninh lương thực và Mô hình lý thuyết",
        "selector": "#sec-insecurity-hotspots",
        "en": "Section 2 investigates hunger hotspots across the Sahel, the Horn of Africa, and conflict zones, while analyzing the great demographic debate between Thomas Malthus and Ester Boserup.",
        "vi": "Mục hai khảo sát các điểm nóng nạn đói trên dải Sahel, vùng sừng châu Phi và các khu vực xung đột vũ trang, đồng thời phân tích cuộc tranh luận nhân khẩu học kinh điển giữa Thomas Malthus và Ester Boserup."
    },
    {
        "id": "malthus_boserup",
        "title": "Tranh luận lý thuyết: Thomas Malthus đối đầu Ester Boserup",
        "selector": "#card-malthus-boserup",
        "en": "This card contrasts Thomas Malthus's pessimistic thesis that arithmetic food growth cannot support exponential population growth leading to inevitable famine checks, against Ester Boserup's optimistic model where population pressure acts as an indispensable catalyst driving agricultural technological innovation.",
        "vi": "Mục này đối chiếu quan điểm bi quan của Thomas Malthus rằng sản lượng lương thực tăng theo cấp số cộng không thể bắt kịp dân số tăng theo cấp số nhân dẫn tới nạn đói thảm khốc không thể tránh khỏi, với mô hình lạc quan của Ester Boserup cho rằng áp lực dân số chính là chất xúc tác bắt buộc thúc đẩy đổi mới công nghệ nông nghiệp."
    },
    {
        "id": "sec_nigeria_crisis",
        "title": "3. Nghiên cứu tình huống chi tiết: Khủng hoảng lương thực tại Nigeria",
        "selector": "#sec-nigeria-crisis",
        "en": "Section 3 examines Nigeria, Africa's most populous nation with over 220 million people. Despite abundant arable land, Nigeria faces acute food insecurity driven by Boko Haram insurgencies displacing northern farmers, desertification encroaching south, and extreme food inflation.",
        "vi": "Mục ba nghiên cứu Nigeria, quốc gia đông dân nhất châu Phi với hơn hai trăm hai mươi triệu người. Dù sở hữu quỹ đất canh tác màu mỡ dồi dào, Nigeria đối mặt với nạn mất an ninh lương thực gay gắt do phiến quân Boko Haram làm gián đoạn mùa màng ở miền bắc, sa mạc hóa xâm lấn xuống phía nam, cùng lạm phát giá lương thực phi mã."
    },
    {
        "id": "sec_sustainable_food",
        "title": "4. Chiến lược bền vững: Bảo tồn đất và Công nghệ tưới tiêu tiên tiến",
        "selector": "#sec-sustainable-food",
        "en": "Section 4 highlights physical and technological remediation: contour plowing and hillside terracing to prevent topsoil gullying, shelterbelt windbreaks to halt desert encroachment, and precision drip irrigation that delivers micro-doses of water directly to plant roots with zero evaporative loss.",
        "vi": "Mục bốn nêu bật các giải pháp công nghệ và canh tác bền vững: cày rãnh theo đường đồng mức và làm ruộng bậc thang chống xói mòn rửa trôi tầng đất mặt, trồng đai rừng chắn gió chặn đứng sa mạc hóa, cùng hệ thống tưới nhỏ giọt chính xác đưa từng giọt nước dinh dưỡng tới tận rễ cây mà không bị bốc hơi lãng phí."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 10.3",
        "selector": "#card-exam-strategy",
        "en": "For 7-mark case study questions on food shortages, always balance physical causes like drought and locust swarms with human triggers like armed conflict and food hoarding, and evaluate both emergency food aid versus long-term soil conservation schemes.",
        "vi": "Trong các câu hỏi tình huống bảy điểm về khan hiếm lương thực, các em hãy luôn cân bằng giữa nguyên nhân tự nhiên như hạn hán dịch châu chấu với nguyên nhân nhân tạo như xung đột vũ trang và găm hàng đầu cơ, đồng thời đánh giá cả cứu trợ lương thực khẩn cấp lẫn các chương trình bảo tồn đất dài hạn."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_food_security", "title": "1. Khái niệm An ninh Lương thực", "startSegmentId": "sec_food_security"},
    {"id": "sec_insecurity_hotspots", "title": "2. Điểm nóng & Tranh luận Malthus - Boserup", "startSegmentId": "sec_insecurity_hotspots"},
    {"id": "sec_nigeria_crisis", "title": "3. Nghiên cứu tình huống: Nigeria", "startSegmentId": "sec_nigeria_crisis"},
    {"id": "sec_sustainable_food", "title": "4. Chiến lược bền vững & Tưới tiêu", "startSegmentId": "sec_sustainable_food"},
    {"id": "card_exam_strategy", "title": "Chiến lược làm bài thi", "startSegmentId": "exam_strategy"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Header
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #15803d 0%, #16a34a 60%, #22c55e 100%);',
        '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #15803d 0%, #16a34a 60%, #22c55e 100%); cursor:pointer;'
    )

    # Sec 1
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Defining Food Security & Measuring Global Hunger\n        </h2>',
        '<h2 id="sec-food-security" class="lecture-interactive-card" data-lecture-section="sec_food_security" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Defining Food Security & Measuring Global Hunger\n        </h2>'
    )

    # Sec 2
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Interactive Food Insecurity Hotspots & Theoretical Models\n        </h2>',
        '<h2 id="sec-insecurity-hotspots" class="lecture-interactive-card" data-lecture-section="sec_insecurity_hotspots" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Interactive Food Insecurity Hotspots & Theoretical Models\n        </h2>'
    )

    # Malthus vs Boserup card
    target_mb = '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px; margin: 24px 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">'
    repl_mb = '<div id="card-malthus-boserup" class="lecture-interactive-card" data-lecture-section="malthus_boserup" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px; margin: 24px 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">'
    html = html.replace(target_mb, repl_mb)

    # Sec 3 (Detailed Example Nigeria)
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Detailed Specific Example: The Food Crisis in Nigeria\n        </h2>',
        '<h2 id="sec-nigeria-crisis" class="lecture-interactive-card" data-lecture-section="sec_nigeria_crisis" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Detailed Specific Example: The Food Crisis in Nigeria\n        </h2>'
    )

    # Sec 4 (Sustainable Strategies)
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Sustainable Strategies: Soil Conservation & Advanced Irrigation\n        </h2>',
        '<h2 id="sec-sustainable-food" class="lecture-interactive-card" data-lecture-section="sec_sustainable_food" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Sustainable Strategies: Soil Conservation & Advanced Irrigation\n        </h2>'
    )

    # Exam Hint Box
    target_hint = '<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 1px solid #86efac; border-left: 6px solid #16a34a; border-radius: 10px; padding: 20px; margin-top: 32px;">'
    repl_hint = '<div id="card-exam-strategy" class="lecture-interactive-card" data-lecture-section="exam_strategy" style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 1px solid #86efac; border-left: 6px solid #16a34a; border-radius: 10px; padding: 20px; margin-top: 32px; cursor:pointer;">'
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
