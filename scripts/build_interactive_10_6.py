import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_6"
LECTURE_ID = "fb30c141-db3a-49e8-aa55-028c913640d4"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.6 The Impacts of Energy Production: Environmental & Geopolitical Trade-offs"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_fossil_impacts'],
    old_segments['sec_nuclear_power'],
    old_segments['sec_renewable_tradeoffs'],
    {
        "id": "tab_emissions",
        "title": "Tác động phát điện: Phát thải nhà kính vòng đời (g CO2e/kWh)",
        "selector": "#btn-tab-emissions",
        "en": "Lifecycle Greenhouse Gas Emissions: Examining total emissions per kilowatt-hour across construction, operation, and decommissioning. Coal is the most polluting at 820 grams of CO2 equivalent per kilowatt-hour, followed by Oil at 720 grams and Natural Gas at 490 grams. Conversely, Solar PV emits 48 grams, Geothermal 38 grams, Hydro 24 grams, while Nuclear and Wind boast the lowest lifecycle footprints at just 11 to 12 grams.",
        "vi": "Phát thải khí nhà kính theo vòng đời: Đánh giá tổng lượng phát thải trên mỗi kilowatt-giờ điện xuyên suốt quá trình xây dựng, vận hành và phá dỡ nhà máy. Than đá gây ô nhiễm nặng nề nhất với tám trăm hai mươi gam CO2 tương đương trên mỗi kilowatt-giờ, tiếp theo là dầu mỏ bảy trăm hai mươi gam và khí đốt bốn trăm chín mươi gam. Ngược lại, điện mặt trời chỉ phát thải bốn mươi tám gam, địa nhiệt ba mươi tám gam, thủy điện hai mươi tư gam, trong khi điện hạt nhân và điện gió có dấu chân carbon thấp nhất chỉ từ mười một đến mười hai gam."
    },
    {
        "id": "tab_ecosystem",
        "title": "Tác động phát điện: Hệ sinh thái địa phương & Môi trường đất",
        "selector": "#btn-tab-ecosystem",
        "en": "Local Ecosystem and Land Impacts: Coal and oil extraction causes open-cast strip mining, wiping out topsoil and native biodiversity. Combustion releases sulfur dioxide and nitrogen oxides that cause Acid Rain with a pH below 4.5, destroying northern forests and poisoning aquatic ecosystems. Meanwhile, large hydroelectric dams flood fertile river valleys and displace communities, while solar farms require extensive land areas.",
        "vi": "Tác động tới hệ sinh thái địa phương và cảnh quan: Khai thác than và dầu bằng phương pháp mỏ lộ thiên phá hủy hoàn toàn thảm thực vật, tầng đất mặt và đa dạng sinh học bản địa. Quá trình đốt nhiên liệu hóa thạch thải ra khí lưu huỳnh đioxit và oxit nitơ tạo nên mưa axit có độ pH dưới bốn phẩy năm, tàn phá rừng lá kim và làm chua độc các hồ nước ngọt. Trong khi đó, các đập thủy điện lớn nhấn chìm thung lũng màu mỡ làm di dời dân cư, còn điện mặt trời đòi hỏi quỹ đất mặt rất lớn."
    },
    {
        "id": "tab_reliability",
        "title": "Tác động phát điện: Độ tin cậy lưới điện (Phụ tải nền vs Gián đoạn)",
        "selector": "#btn-tab-reliability",
        "en": "Grid Reliability: Baseload Power versus Intermittency. Baseload power stations—including nuclear, geothermal, and coal—provide steady, continuous 24/7 electricity to meet minimum base demand. In contrast, solar and wind are weather-dependent intermittent sources that fluctuate with daylight and wind speed, requiring massive grid-scale battery storage, pumped hydroelectricity, or rapid-dispatch natural gas peaker plants to maintain grid stability.",
        "vi": "Độ tin cậy của lưới điện: Nguồn điện phụ tải nền so với Năng lượng gián đoạn. Các nhà máy điện phụ tải nền gồm hạt nhân, địa nhiệt và than đá cung cấp nguồn điện liên tục hai mươi tư trên bảy ổn định để đáp ứng nhu cầu tối thiểu của xã hội. Trái lại, điện mặt trời và điện gió là nguồn năng lượng gián đoạn phụ thuộc vào thời tiết và nắng gió, đòi hỏi pin lưu trữ quy mô lớn, thủy điện tích năng hoặc nhà máy tua bin khí linh hoạt để duy trì ổn định lưới điện."
    },
    {
        "id": "tab_sweden",
        "title": "Nghiên cứu điển hình: Mô hình Thụy Điển - 4 Trụ cột khử carbon",
        "selector": "#btn-tab-sweden",
        "en": "Sweden Decarbonisation Case Study: Catalyzed by the 1973 global oil shock when Sweden imported 75 percent of its energy as oil, the nation enacted a decisive strategy. During the 1980s, Sweden constructed 12 nuclear reactors and harnessed northern mountain rivers for hydropower. In 1991, it introduced the world's first carbon tax of over 130 dollars per tonne, and expanded municipal district heating using biomass forestry waste, achieving over 60 percent renewable energy share.",
        "vi": "Nghiên cứu điển hình Mô hình Thụy Điển: Khởi nguồn từ cú sốc dầu mỏ năm 1973 khi Thụy Điển phải nhập khẩu tới bảy mươi lăm phần trăm năng lượng dưới dạng dầu, quốc gia này đã ban hành chiến lược chuyển đổi mang tính quyết định. Trong thập niên 1980, Thụy Điển đã xây dựng mười hai lò phản ứng hạt nhân và tận dụng các dòng sông miền bắc để phát triển thủy điện. Năm 1991, Thụy Điển áp dụng thuế carbon đầu tiên trên thế giới với mức hơn một trăm ba mươi đô la một tấn, đồng thời mở rộng mạng lưới sưởi ấm đô thị bằng phế phẩm lâm nghiệp sinh khối, đưa tỷ lệ năng lượng tái tạo vượt trên sáu mươi phần trăm."
    },
    old_segments['sec_global_trends'],
    old_segments['sec_sweden_casestudy'],
    old_segments['exam_strategy']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_fossil_impacts": {"start": 1, "end": 1},
    "sec_nuclear_power": {"start": 2, "end": 2},
    "sec_renewable_tradeoffs": {"start": 3, "end": 7},
    "sec_global_trends": {"start": 8, "end": 8},
    "sec_sweden_casestudy": {"start": 9, "end": 9},
    "card_exam_strategy": {"start": 10, "end": 10}
}

async def main():
    print(f"--- Updating Audio & Manifest for {LECTURE_CODE} ---")
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    html = res.data[0]['content_html']

    # Update tab buttons with class="lecture-interactive-card" and data-lecture-section
    tabs = [
        ('emissions', 'tab_emissions'),
        ('ecosystem', 'tab_ecosystem'),
        ('reliability', 'tab_reliability'),
        ('sweden', 'tab_sweden'),
    ]
    for key, sec_key in tabs:
        pat = rf'(<button\s+[^>]*id="btn-tab-{key}"[^>]*)'
        repl = rf'<button id="btn-tab-{key}" class="lecture-interactive-card" data-lecture-section="{sec_key}" onclick="setTab106(\'{key}\')"'
        html = re.sub(rf'<button\s+(?:onclick="setTab106\(\'{key}\'\)"\s+)?id="btn-tab-{key}"(?:\s+onclick="setTab106\(\'{key}\'\)")?', repl, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive impact tabs updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
