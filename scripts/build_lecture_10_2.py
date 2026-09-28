import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_2"
LECTURE_ID = "76dcafbf-e6b8-47f1-8618-be1b14e975ed"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.2 Global Patterns of Food Supply and Demand"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 10.2: Bức tranh toàn cầu về Cung và Cầu Lương thực",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 10.2: Global Patterns of Food Supply and Demand. In this lecture, we examine global caloric distribution: contrasting undernourishment in Sub-Saharan Africa against hyper-affluent overconsumption in North America, analyzing the meat-intensive Nutrition Transition, calculating the ecological footprint of livestock feed conversion, and exposing the structural contrasts of post-harvest versus consumer food waste.",
        "vi": "Chào mừng các em đến với bài mười chấm hai: Bức tranh toàn cầu về Cung và Cầu Lương thực. Trong bài giảng này, chúng ta sẽ khảo sát sự phân bố calo toàn cầu: đối chiếu nạn suy dinh dưỡng tại châu Phi cận Sahara với tình trạng dư thừa calo tại Bắc Mỹ, phân tích sự chuyển dịch dinh dưỡng sang thịt, tính toán dấu chân sinh thái chuyển đổi thức ăn chăn nuôi, và bóc tách nghịch lý lãng phí thực phẩm sau thu hoạch so với lãng phí ở khâu tiêu dùng."
    },
    {
        "id": "sec_calorie_patterns",
        "title": "1. Phân bố nguồn cung calo toàn cầu và Sự chuyển dịch dinh dưỡng",
        "selector": "#sec-calorie-patterns",
        "en": "Section 1 charts daily per capita calorie intake worldwide. The United Nations FAO establishes an absolute minimum threshold of 2,100 calories per day for adult survival. Yet global averages range from under 1,800 calories across impoverished nations to over 3,800 calories in high-income economies.",
        "vi": "Mục một phác thảo mức tiêu thụ calo bình quân đầu người hàng ngày trên toàn thế giới. Tổ chức Lương thực và Nông nghiệp Liên Hợp Quốc FAO thiết lập ngưỡng sinh tồn tối thiểu là hai nghìn một trăm calo mỗi ngày cho một người trưởng thành. Tuy nhiên, mức bình quân thực tế dao động từ dưới một nghìn tám trăm calo tại các quốc gia nghèo đói tới hơn ba nghìn tám trăm calo tại các nước phát triển."
    },
    {
        "id": "nutrition_transition",
        "title": "Hiện tượng chuyển dịch dinh dưỡng và Bệnh lý phồn vinh",
        "selector": "#card-nutrition-transition",
        "en": "As national disposable incomes rise across emerging economies, populations undergo Bennett's Law and the Nutrition Transition: shifting from traditional plant-based starchy diets towards energy-dense animal proteins, fats, and ultra-processed sugars.",
        "vi": "Khi thu nhập khả dụng tăng lên tại các nền kinh tế mới nổi, cơ cấu bữa ăn chuyển dịch theo Quy luật Bennett và sự chuyển dịch dinh dưỡng: từ chế độ ăn truyền thống giàu tinh bột từ thực vật sang tiêu thụ nhiều đạm động vật, chất béo và đường tinh luyện."
    },
    {
        "id": "sec_food_map",
        "title": "2. Bản đồ tương tác: Động lực hệ thống lương thực và Điểm nóng toàn cầu",
        "selector": "#sec-food-map",
        "en": "Section 2 investigates global food supply dynamics: revealing intense export flows of wheat, corn, and soy from the Americas to Asia, alongside severe structural food insecurity hotspots across the Horn of Africa and the Sahel.",
        "vi": "Mục hai khảo sát động lực của hệ thống lương thực toàn cầu: chỉ ra các dòng xuất khẩu ồ ạt lúa mì, ngô và đậu tương từ châu Mỹ sang châu Á, song song với các điểm nóng khủng hoảng an ninh lương thực nghiêm trọng tại vùng sừng châu Phi và dải Sahel."
    },
    {
        "id": "sec_meat_demand",
        "title": "3. Công nghiệp hóa nông nghiệp và Cái giá môi trường của nhu cầu tiêu thụ thịt",
        "selector": "#sec-meat-demand",
        "en": "Section 3 evaluates the ecological burden of animal agriculture. Livestock occupies nearly 80 percent of global farmland while providing less than 20 percent of calories. Producing one kilogram of beef requires up to 15,000 liters of water and 10 kilograms of grain feed.",
        "vi": "Mục ba đánh giá gánh nặng sinh thái của ngành chăn nuôi đại gia súc. Chăn nuôi chiếm tới gần tám mươi phần trăm tổng diện tích đất nông nghiệp toàn cầu nhưng chỉ cung cấp chưa đầy hai mươi phần trăm lượng calo. Để sản xuất một kilôgam thịt bò cần tới mười lăm nghìn lít nước ngọt và mười kilôgam ngũ cốc thức ăn gia súc."
    },
    {
        "id": "sec_food_waste",
        "title": "4. Địa lý lãng phí thực phẩm và Các tập đoàn nông nghiệp đa quốc gia",
        "selector": "#sec-food-waste",
        "en": "Section 4 contrasts food waste across development stages: Low-income nations lose up to 40 percent of harvests early in the supply chain due to lack of cold storage and poor roads, whereas high-income societies waste vast volumes at retail and household levels due to aesthetic standards and expired shelf-life dates.",
        "vi": "Mục bốn đối chiếu sự lãng phí lương thực theo từng nấc thang phát triển: Các nước nghèo thất thoát tới bốn mươi phần trăm sản lượng ngay sau thu hoạch do thiếu kho lạnh bảo quản và đường xá yếu kém, trong khi xã hội giàu có lại vứt bỏ khối lượng khổng lồ tại siêu thị và gia đình do tiêu chuẩn thẩm mỹ ngoại hình và hạn dùng hết hạn."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 10.2",
        "selector": "#card-exam-strategy",
        "en": "In exam questions on food supply disparities, synthesize physical factors like monsoonal droughts with economic drivers like global trade barriers, commodity market speculation, and the diversion of edible corn crops into biofuel ethanol.",
        "vi": "Trong các câu hỏi thi về chênh lệch nguồn cung lương thực, các em hãy kết hợp cả yếu tố tự nhiên như hạn hán do biến động gió mùa với các động lực kinh tế như hàng rào thuế quan thương mại, nạn đầu cơ giá nông sản và việc chuyển đổi ngô thực phẩm sang sản xuất nhiên liệu sinh học ethanol."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_calorie_patterns", "title": "1. Phân bố nguồn cung calo toàn cầu", "startSegmentId": "sec_calorie_patterns"},
    {"id": "sec_food_map", "title": "2. Bản đồ động lực hệ thống lương thực", "startSegmentId": "sec_food_map"},
    {"id": "sec_meat_demand", "title": "3. Canh tác gia súc & Cái giá môi trường", "startSegmentId": "sec_meat_demand"},
    {"id": "sec_food_waste", "title": "4. Địa lý lãng phí lương thực & Agribusiness", "startSegmentId": "sec_food_waste"},
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
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Global Calorie Supply Patterns & The Nutrition Transition\n        </h2>',
        '<h2 id="sec-calorie-patterns" class="lecture-interactive-card" data-lecture-section="sec_calorie_patterns" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Global Calorie Supply Patterns & The Nutrition Transition\n        </h2>'
    )

    # Nutrition transition card
    target_nt = '<div style="background: #f0fdf4; border-left: 4px solid #16a34a; border-radius: 8px; padding: 16px 20px; margin: 20px 0;">'
    repl_nt = '<div id="card-nutrition-transition" class="lecture-interactive-card" data-lecture-section="nutrition_transition" style="background: #f0fdf4; border-left: 4px solid #16a34a; border-radius: 8px; padding: 16px 20px; margin: 20px 0; cursor:pointer;">'
    html = html.replace(target_nt, repl_nt)

    # Sec 2
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Interactive Map: Global Food System Dynamics & Hotspots\n        </h2>',
        '<h2 id="sec-food-map" class="lecture-interactive-card" data-lecture-section="sec_food_map" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Interactive Map: Global Food System Dynamics & Hotspots\n        </h2>'
    )

    # Sec 3
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Agro-Industrialisation & Environmental Costs of Meat Demand\n        </h2>',
        '<h2 id="sec-meat-demand" class="lecture-interactive-card" data-lecture-section="sec_meat_demand" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Agro-Industrialisation & Environmental Costs of Meat Demand\n        </h2>'
    )

    # Sec 4
    html = html.replace(
        '<h2 style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0;">\n          Food Waste Geography & Multinational Agribusiness Corporations\n        </h2>',
        '<h2 id="sec-food-waste" class="lecture-interactive-card" data-lecture-section="sec_food_waste" style="font-size: 20px; font-weight: 800; color: #1e293b; margin: 0; cursor:pointer;">\n          Food Waste Geography & Multinational Agribusiness Corporations\n        </h2>'
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
