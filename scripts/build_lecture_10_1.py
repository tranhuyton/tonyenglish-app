import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_1"
LECTURE_ID = "362104be-aedc-4cbe-87b2-29034e93cc9c"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.1 How Our Food is Produced: Agricultural Systems"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10.1: Hệ thống sản xuất nông nghiệp",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 10.1: How Our Food is Produced: Agricultural Systems. In this lecture, we explore global food production: mastering the three axes of farming classification, understanding the Input-Process-Output systems model, comparing smallholder rice paddies in Sri Lanka against extensive wheat prairies in Canada, and examining the high-tech revolution of vertical farming and aeroponics.",
        "vi": "Chào mừng các em đến với bài mười chấm một: Hệ thống sản xuất nông nghiệp. Trong bài giảng này, chúng ta sẽ khảo sát nền nông nghiệp sản xuất lương thực toàn cầu: nắm vững ba trục phân loại canh tác, hiểu rõ mô hình hệ thống Đầu vào - Quá trình - Đầu ra IPO, so sánh ruộng lúa nước quy mô nhỏ ở Sri Lanka với cánh đồng lúa mì quảng canh bạt ngàn tại Canada, và khám phá cuộc cách mạng công nghệ cao với nông nghiệp thẳng đứng và khí canh."
    },
    {
        "id": "sec_farming_classification",
        "title": "1. Phân loại các loại hình canh tác nông nghiệp",
        "selector": "#sec-farming-classification",
        "en": "Section 1 establishes the tripartite taxonomy of agriculture along three distinct axes: Arable crop cultivation versus Pastoral livestock rearing, Commercial farming for profit versus Subsistence farming for household survival, and Intensive high-input farming versus Extensive low-density operations.",
        "vi": "Mục một thiết lập hệ thống phân loại nông nghiệp theo ba trục riêng biệt: Canh tác cây trồng trồng trọt so với Chăn nuôi gia súc đồng cỏ, Canh tác thương mại vì lợi nhuận so với Nông nghiệp tự cung tự cấp duy trì sự sống gia đình, và Canh tác thâm canh vốn cao so với Quảng canh trên diện tích rộng."
    },
    {
        "id": "sec_agricultural_ipo",
        "title": "2. Khung hệ thống nông nghiệp: Đầu vào - Quá trình - Đầu ra",
        "selector": "#sec-agricultural-ipo",
        "en": "Section 2 investigates farming through an open systems model: Physical inputs like rainfall and fertile soil combine with Human inputs like labor and tractors, undergo agricultural processes like ploughing and harvesting, to yield positive outputs of food and cash alongside negative waste.",
        "vi": "Mục hai nghiên cứu nông nghiệp dưới góc nhìn mô hình hệ thống mở: Đầu vào tự nhiên như lượng mưa và đất phì nhiêu kết hợp với Đầu vào nhân tạo như sức lao động và máy móc, trải qua các quá trình canh tác như cày bừa gieo cấy gặt hái, để tạo ra đầu ra hữu ích là lương thực và tiền mặt song hành với chất thải dư thừa."
    },
    {
        "id": "ipo_framework",
        "title": "Sơ đồ hệ thống Đầu vào - Quá trình - Đầu ra (IPO)",
        "selector": "#card-ipo-framework",
        "en": "Figure 10.8 maps this systemic loop: showing how agricultural profits are reinvested back into seed varieties and mechanization, creating positive feedback loops that raise annual crop yields.",
        "vi": "Hình mười chấm tám phác họa chu trình hệ thống này: minh họa cách lợi nhuận nông nghiệp được tái đầu tư trở lại vào giống cây trồng và cơ giới hóa, tạo nên vòng phản hồi tích cực giúp nâng cao năng suất thu hoạch hàng năm."
    },
    {
        "id": "sec_ipo_explorer",
        "title": "3. Nghiên cứu tình huống đối chiếu: Lúa nước Sri Lanka vs Lúa mì Canada",
        "selector": "#sec-ipo-explorer",
        "en": "Section 3 compares contrasting agricultural case studies: labor-intensive subsistence wet rice cultivation in Sri Lanka relying on family monsoonal labor, versus capital-intensive extensive commercial wheat farming in the Canadian Prairies employing combine harvesters across thousands of hectares.",
        "vi": "Mục ba đối chiếu hai nghiên cứu tình huống nông nghiệp điển hình: thâm canh lúa nước tự cung tự cấp thâm dụng lao động tại Sri Lanka phụ thuộc sức người và mưa mùa, so với đại quảng canh lúa mì thương mại thâm dụng tư bản ở vùng đồng bằng Canada sử dụng máy gặt đập liên hợp cơ giới hóa trên diện tích bạt ngàn."
    },
    {
        "id": "sec_hightech_farming",
        "title": "4. Biên giới công nghệ cao: Thủy canh, Khí canh và Nông nghiệp thẳng đứng",
        "selector": "#sec-hightech-farming",
        "en": "Section 4 showcases modern controlled-environment agriculture: soil-less hydroponics, mist-based aeroponics, and indoor vertical farms that slash water usage by 95 percent and produce year-round harvests insulated from climate shocks.",
        "vi": "Mục bốn giới thiệu nông nghiệp môi trường kiểm soát hiện đại: thủy canh không cần đất, khí canh nuôi rễ bằng màng sương dinh dưỡng, và các trang trại thẳng đứng nhiều tầng trong nhà giúp tiết kiệm chín mươi lăm phần trăm lượng nước và cho thu hoạch quanh năm không phụ thuộc vào thời tiết."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 10.1",
        "selector": "#card-exam-strategy",
        "en": "In exam 7-mark case study questions on agricultural systems, always classify the farm precisely along all three axes, categorize inputs into physical versus human, describe specific processes, and identify both commercial outputs and environmental byproducts.",
        "vi": "Trong các câu hỏi tình huống bảy điểm về hệ thống nông nghiệp, các em hãy luôn phân loại chính xác trang trại theo cả ba trục, tách bạch đầu vào tự nhiên và con người, mô tả chi tiết các công đoạn canh tác, và chỉ rõ sản phẩm thu hoạch thương mại đi kèm với phụ phẩm môi trường."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_farming_classification", "title": "1. Phân loại canh tác nông nghiệp", "startSegmentId": "sec_farming_classification"},
    {"id": "sec_agricultural_ipo", "title": "2. Khung hệ thống IPO nông nghiệp", "startSegmentId": "sec_agricultural_ipo"},
    {"id": "sec_ipo_explorer", "title": "3. Đối chiếu Sri Lanka & Canada", "startSegmentId": "sec_ipo_explorer"},
    {"id": "sec_hightech_farming", "title": "4. Nông nghiệp công nghệ cao", "startSegmentId": "sec_hightech_farming"},
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
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Classification of Farming Types & Operational Scales\n        </h2>',
        '<h2 id="sec-farming-classification" class="lecture-interactive-card" data-lecture-section="sec_farming_classification" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Classification of Farming Types & Operational Scales\n        </h2>'
    )

    # Sec 2
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          The Agricultural System: Input-Process-Output (IPO) Framework\n        </h2>',
        '<h2 id="sec-agricultural-ipo" class="lecture-interactive-card" data-lecture-section="sec_agricultural_ipo" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          The Agricultural System: Input-Process-Output (IPO) Framework\n        </h2>'
    )

    # IPO Figure 10.8 card
    target_f8 = '<div style="margin: 22px 0; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 18px; text-align: center;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t10_fig_10_8.png'
    repl_f8 = '<div id="card-ipo-framework" class="lecture-interactive-card" data-lecture-section="ipo_framework" style="margin: 22px 0; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 18px; text-align: center; cursor:pointer;">\n      <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t10_fig_10_8.png'
    html = html.replace(target_f8, repl_f8)

    # Sec 3
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Interactive Agricultural System Explorer: Case Studies & IPO Mechanics\n        </h2>',
        '<h2 id="sec-ipo-explorer" class="lecture-interactive-card" data-lecture-section="sec_ipo_explorer" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Interactive Agricultural System Explorer: Case Studies & IPO Mechanics\n        </h2>'
    )

    # Sec 4
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          High-Tech Frontiers: Hydroponics, Aeroponics & Vertical Farming\n        </h2>',
        '<h2 id="sec-hightech-farming" class="lecture-interactive-card" data-lecture-section="sec_hightech_farming" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          High-Tech Frontiers: Hydroponics, Aeroponics & Vertical Farming\n        </h2>'
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
