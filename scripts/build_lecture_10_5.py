import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_5"
LECTURE_ID = "a3a8d904-d277-4eef-b8ff-52a913ebc5f6"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.5 Global Patterns of Energy Supply and Demand"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10.5: Bức tranh toàn cầu về Cung và Cầu Năng lượng",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 10.5: Global Patterns of Energy Supply and Demand. In this lecture, we investigate the global energy balance: analyzing the relentless surge in worldwide primary consumption, mapping regional fuel mix profiles across Europe, Asia-Pacific, and the Middle East, and exploring the geopolitical vulnerability of energy security through the three-stage supply disruption sequence.",
        "vi": "Chào mừng các em đến với bài mười chấm năm: Bức tranh toàn cầu về Cung và Cầu Năng lượng. Trong bài giảng này, chúng ta sẽ khảo sát cán cân năng lượng toàn cầu: phân tích sự gia tăng nhanh chóng của tổng mức tiêu thụ năng lượng sơ cấp trên thế giới, lập bản đồ cơ cấu nhiên liệu theo từng khu vực tại châu Âu, châu Á - Thái Bình Dương và Trung Đông, đồng thời khám phá lỗ hổng địa chính trị của an ninh năng lượng thông qua chuỗi ba giai đoạn gián đoạn nguồn cung."
    },
    {
        "id": "sec_consumption_surges",
        "title": "1. Sự bùng nổ tiêu thụ năng lượng toàn cầu và Thị phần nhiên liệu sơ cấp",
        "selector": "#sec-consumption-surges",
        "en": "Section 1 charts the exponential trajectory of global energy demand over the past half-century. Global energy consumption has nearly tripled since 1970, driven by industrialization in emerging giants like China and India, the proliferation of private automobiles, and massive expansions in high-tech digital computing infrastructure.",
        "vi": "Mục một phác họa quỹ đạo tăng trưởng theo cấp số nhân của nhu cầu năng lượng toàn cầu trong nửa thế kỷ qua. Tổng mức tiêu thụ năng lượng toàn cầu đã tăng gần gấp ba lần kể từ năm 1970, được thúc đẩy bởi quá trình công nghiệp hóa tại các nước mới nổi như Trung Quốc và Ấn Độ, sự gia tăng nhanh chóng của xe hơi cá nhân, cùng sự bùng nổ hạ tầng trung tâm dữ liệu và điện toán số."
    },
    {
        "id": "sec_fuel_mix_map",
        "title": "2. Bản đồ tương tác: Cơ cấu nhiên liệu theo từng khu vực toàn cầu",
        "selector": "#sec-fuel-mix-map",
        "en": "Section 2 investigates regional variations in fuel portfolios: contrasting the Middle East's overwhelming reliance on indigenous oil and natural gas, the Asia-Pacific region's heavy dependence on coal for power generation, and Europe's rapid decarbonization pivoting towards wind, solar, and nuclear power.",
        "vi": "Mục hai khảo sát sự khác biệt sâu sắc trong cơ cấu nhiên liệu giữa các khu vực: đối chiếu sự phụ thuộc gần như tuyệt đối vào dầu mỏ và khí đốt nội địa của Trung Đông, sự phụ thuộc nặng nề vào nhiệt điện than tại khu vực châu Á - Thái Bình Dương, với bước chuyển dịch phi carbon hóa mạnh mẽ của châu Âu hướng tới năng lượng gió, mặt trời và điện hạt nhân."
    },
    {
        "id": "sec_energy_security",
        "title": "3. An ninh năng lượng và Chuỗi gián đoạn nguồn cung ba giai đoạn",
        "selector": "#sec-energy-security",
        "en": "Section 3 models the vulnerability of international supply routes: tracing how physical choke-points like the Strait of Hormuz and the Malacca Strait, political pipeline embargoes, and acute natural disasters trigger immediate physical shortages, secondary industrial shutdowns, and tertiary macroeconomic recessions.",
        "vi": "Mục ba mô hình hóa mức độ tổn thương của các tuyến vận tải năng lượng huyết mạch quốc tế: chỉ rõ cách các điểm nghẽn địa lý như eo biển Hormuz và eo biển Malacca, các lệnh cấm vận đường ống dẫn khí đốt chính trị, cùng thiên tai bất ngờ kích hoạt tình trạng thiếu hụt nhiên liệu vật lý trước mắt, đình trệ sản xuất công nghiệp thứ cấp, và gây ra suy thoái kinh tế vĩ mô trên diện rộng."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 10.5",
        "selector": "#card-exam-strategy",
        "en": "In exam answers assessing energy security risks, always cite specific geopolitical case studies: evaluate how oil-importing economies insulate themselves by establishing strategic petroleum reserves, constructing liquefied natural gas regasification terminals, and aggressively expanding domestic renewable wind and nuclear capacity.",
        "vi": "Trong các câu trả lời thi đánh giá rủi ro an ninh năng lượng, các em hãy luôn trích dẫn các dẫn chứng thực tế cụ thể: phân tích cách các quốc gia nhập khẩu dầu mỏ bảo vệ mình bằng việc xây dựng kho dự trữ dầu chiến lược, xây các cảng tái hóa khí tự nhiên hóa lỏng LNG, và đẩy mạnh phát triển năng lượng gió và điện hạt nhân nội địa."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_consumption_surges", "title": "1. Tiêu thụ năng lượng toàn cầu", "startSegmentId": "sec_consumption_surges"},
    {"id": "sec_fuel_mix_map", "title": "2. Bản đồ cơ cấu nhiên liệu khu vực", "startSegmentId": "sec_fuel_mix_map"},
    {"id": "sec_energy_security", "title": "3. An ninh năng lượng & Gián đoạn nguồn cung", "startSegmentId": "sec_energy_security"},
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
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Global Consumption Surges & Evolving Primary Fuel Shares\n        </h2>',
        '<h2 id="sec-consumption-surges" class="lecture-interactive-card" data-lecture-section="sec_consumption_surges" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Global Consumption Surges & Evolving Primary Fuel Shares\n        </h2>'
    )

    # Sec 2
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Interactive Map: Regional Fuel Mix Profiles (Hodder Fig 10.36)\n        </h2>',
        '<h2 id="sec-fuel-mix-map" class="lecture-interactive-card" data-lecture-section="sec_fuel_mix_map" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Interactive Map: Regional Fuel Mix Profiles (Hodder Fig 10.36)\n        </h2>'
    )

    # Sec 3
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Energy Security & The 3-Stage Interruption Sequence (Fig 10.37)\n        </h2>',
        '<h2 id="sec-energy-security" class="lecture-interactive-card" data-lecture-section="sec_energy_security" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Energy Security & The 3-Stage Interruption Sequence (Fig 10.37)\n        </h2>'
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
