import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_2"
LECTURE_ID = "76dcafbf-e6b8-47f1-8618-be1b14e975ed"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.2 The Global Patterns of Food Supply and Demand"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_calorie_patterns'],
    old_segments['nutrition_transition'],
    old_segments['sec_food_map'],
    {
        "id": "food_usa",
        "title": "Điểm nóng bản đồ: Bắc Mỹ (>3,600 kcal/ngày)",
        "selector": "#pin-food-usa",
        "en": "North America Food Hotspot: Average intake exceeds 3,600 kilocalories per person per day. Driven by intensive corporate agribusiness and corn-soy rotations, the region produces vast food surpluses and massive grain exports. However, diet is characterized by high meat consumption and high carbon footprints per calorie due to fossil fuel mechanization and long food miles.",
        "vi": "Điểm nóng bản đồ Bắc Mỹ: Mức tiêu thụ trung bình vượt quá ba nghìn sáu trăm calo mỗi người một ngày. Nhờ nền nông nghiệp tập đoàn thâm canh cao và mô hình luân canh ngô đậu tương, khu vực tạo ra thặng dư lương thực khổng lồ và xuất khẩu ngũ cốc đứng đầu thế giới. Tuy nhiên, khẩu phần ăn tại đây thâm dụng thịt và dấu chân carbon cao trên mỗi calo do cơ giới hóa hóa thạch và quãng đường vận chuyển thực phẩm dài."
    },
    {
        "id": "food_netherlands",
        "title": "Điểm nóng bản đồ: Hà Lan (Nghịch lý đổi mới nông công nghiệp)",
        "selector": "#pin-food-netherlands",
        "en": "The Netherlands Innovation Paradox: The world's second-largest agricultural exporter by value, generating over 100 billion euros annually from a tiny land area of just 41,500 square kilometers. Dutch agriculture relies on extreme agro-industrial intensification, featuring ten thousand hectares of geothermal-heated glasshouses that use twenty times less water per kilogram of tomatoes than open-field cultivation.",
        "vi": "Nghịch lý đổi mới nông công nghiệp Hà Lan: Nước xuất khẩu nông nghiệp lớn thứ hai thế giới theo giá trị, thu về hơn một trăm tỷ euro mỗi năm dù diện tích đất đai vỏn vẹn bốn mươi mốt nghìn năm trăm ki-lô-mét vuông. Nông nghiệp Hà Lan dựa vào thâm canh công nghệ cao cực độ với mười nghìn héc-ta nhà kính sưởi bằng địa nhiệt, tiêu tốn lượng nước ít hơn hai mươi lần cho mỗi ki-lô-gam cà chua so với canh tác ngoài đồng ruộng."
    },
    {
        "id": "food_sahel",
        "title": "Điểm nóng bản đồ: Châu Phi hạ Sahara (Thâm hụt calo & tổn thất sau thu hoạch)",
        "selector": "#pin-food-sahel",
        "en": "Sub-Saharan Africa Caloric Deficit Hotspot: Average consumption languishes between 1,900 and 2,150 kilocalories daily, below minimum metabolic requirements. The region suffers from severe post-harvest losses of up to 40 percent due to inadequate cold storage and pest infestation, rendering communities acutely vulnerable to climate droughts and global food price volatility.",
        "vi": "Điểm nóng thâm hụt calo châu Phi hạ Sahara: Mức tiêu thụ trung bình chỉ đạt từ một nghìn chín trăm đến hai nghìn một trăm năm mươi calo mỗi ngày, dưới mức chuẩn trao đổi chất tối thiểu. Khu vực chịu tổn thất sau thu hoạch nặng nề lên tới bốn mươi phần trăm do thiếu kho lạnh bảo quản và côn trùng phá hoại, khiến người dân dễ bị tổn thương nghiêm trọng trước các đợt hạn hán khí hậu và biến động giá lương thực thế giới."
    },
    {
        "id": "food_brazil",
        "title": "Điểm nóng bản đồ: Brazil (Siêu cường đậu tương và thịt bò Cerrado)",
        "selector": "#pin-food-brazil",
        "en": "Brazil Cerrado Agribusiness Superpower: By applying agricultural lime and phosphorus to acidic savanna soils, Brazil transformed the Cerrado biome into the world's premier soy and cattle production belt, exporting millions of tons to China and Europe. However, this massive commercial expansion creates severe deforestation and biodiversity trade-offs along the Amazon frontier.",
        "vi": "Siêu cường nông nghiệp Cerrado Brazil: Bằng cách bón vôi và phốt pho cải tạo đất trảng cỏ xavan chua phèn, Brazil đã biến vùng Cerrado thành vành đai sản xuất đậu tương và thịt bò hàng đầu thế giới, xuất khẩu hàng triệu tấn sang Trung Quốc và châu Âu. Tuy nhiên, sự mở rộng thương mại ồ ạt này tạo ra sự đánh đổi nghiêm trọng giữa phát triển kinh tế và nạn phá rừng phá hủy đa dạng sinh học ven rừng Amazon."
    },
    {
        "id": "food_china",
        "title": "Điểm nóng bản đồ: Đông Á / Trung Quốc (Chuyển dịch dinh dưỡng nhanh chóng)",
        "selector": "#pin-food-china",
        "en": "East Asia Rapid Nutrition Transition: Driven by four decades of historic income growth, China's diet has fundamentally shifted from traditional rice and coarse grains toward meat, dairy, and ultra-processed foods. China now consumes half the world's pork, necessitating massive grain imports from Brazil and the United States to feed domestic livestock herds.",
        "vi": "Chuyển dịch dinh dưỡng thần tốc tại Đông Á và Trung Quốc: Thúc đẩy bởi bốn thập kỷ tăng trưởng thu nhập lịch sử, chế độ ăn uống của người dân Trung Quốc đã chuyển dịch căn bản từ lúa gạo và ngũ cốc thô truyền thống sang thịt, sữa và thực phẩm chế biến sẵn. Hiện Trung Quốc tiêu thụ một nửa lượng thịt lợn của toàn thế giới, đòi hỏi nhập khẩu ngũ cốc khổng lồ từ Brazil và Hoa Kỳ để làm thức ăn chăn nuôi gia súc."
    },
    old_segments['sec_meat_demand'],
    old_segments['sec_food_waste'],
    old_segments['exam_strategy']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_calorie_patterns": {"start": 1, "end": 2},
    "sec_food_map": {"start": 3, "end": 8},
    "sec_meat_demand": {"start": 9, "end": 9},
    "sec_food_waste": {"start": 10, "end": 10},
    "card_exam_strategy": {"start": 11, "end": 11}
}

async def main():
    print(f"--- Updating Audio & Manifest for {LECTURE_CODE} ---")
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    html = res.data[0]['content_html']

    # Update SVG pins with id, class="food-pin lecture-interactive-card", data-lecture-section
    pins = [
        ('usa', 'pin-food-usa', 'food_usa'),
        ('netherlands', 'pin-food-netherlands', 'food_netherlands'),
        ('sahel', 'pin-food-sahel', 'food_sahel'),
        ('brazil', 'pin-food-brazil', 'food_brazil'),
        ('china', 'pin-food-china', 'food_china'),
    ]
    for key, pid, sec_key in pins:
        pat = rf'<g\s+class="food-pin"\s+onclick="showFoodCase\(\'{key}\'\)"'
        repl = rf'<g id="{pid}" class="food-pin lecture-interactive-card" data-lecture-section="{sec_key}" onclick="showFoodCase(\'{key}\')" style="cursor:pointer;"'
        html = re.sub(pat, repl, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive food map updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
