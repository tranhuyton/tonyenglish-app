import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_1"
LECTURE_ID = "362104be-aedc-4cbe-87b2-29034e93cc9c"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.1 How Our Food is Produced: Agricultural Systems"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_farming_classification'],
    old_segments['sec_agricultural_ipo'],
    old_segments['ipo_framework'],
    old_segments['sec_ipo_explorer'],
    {
        "id": "farm_prairies",
        "title": "Hệ thống canh tác: Đồng bằng lúa mì Canada (Quảng canh thương mại)",
        "selector": "#fbtn-prairies",
        "en": "Canadian Prairies Commercial Wheat Farming: This is an extensive commercial arable system operating on thousands of hectares. It relies heavily on high capital inputs including massive combine harvesters, GPS-guided tractors, and chemical fertilizers, resulting in very high output per worker but lower yield per hectare. All wheat is sold on the global export market.",
        "vi": "Đại quảng canh lúa mì thương mại tại thảo nguyên Canada: Đây là hệ thống canh tác cây lương thực thương mại quy mô lớn trên hàng nghìn héc-ta. Trang trại sử dụng lượng vốn cơ giới hóa khổng lồ gồm máy gặt đập liên hợp, máy kéo định vị vệ tinh và phân bón hóa học, mang lại sản lượng rất cao trên mỗi lao động nhưng năng suất trên mỗi héc-ta ở mức trung bình. Toàn bộ lúa mì được bán ra thị trường xuất khẩu toàn cầu."
    },
    {
        "id": "farm_ganges",
        "title": "Hệ thống canh tác: Ruộng lúa nước sông Hằng & Sri Lanka (Thâm canh tự cung tự cấp)",
        "selector": "#fbtn-ganges",
        "en": "Ganges Valley and Sri Lanka Wet Rice Cultivation: An intensive subsistence arable system practiced on small, fragmented plots under one hectare. It requires high labor inputs from family members using water buffalo and monsoonal flood irrigation, achieving high yields per hectare with zero mechanization. Virtually all harvested rice is consumed locally by the farming household.",
        "vi": "Thâm canh lúa nước tại thung lũng sông Hằng và Sri Lanka: Hệ thống trồng trọt tự cung tự cấp thâm canh trên các thửa ruộng nhỏ hẹp dưới một héc-ta. Quy trình đòi hỏi sức lao động chân tay rất lớn của các thành viên trong gia đình kết hợp sức trâu kéo và nước lũ mùa mưa, đạt năng suất lúa rất cao trên mỗi héc-ta dù hầu như không cơ giới hóa. Gần như toàn bộ lúa gạo thu hoạch được dùng để nuôi sống gia đình nông dân tại chỗ."
    },
    {
        "id": "farm_sahel",
        "title": "Hệ thống canh tác: Du mục chăn thả vùng Sahel (Quảng canh tự cung tự cấp)",
        "selector": "#fbtn-sahel",
        "en": "African Sahel Nomadic Pastoral Herding: An extensive subsistence pastoral system across marginal semi-arid grasslands. Pastoralists migrate seasonally following erratic rainfall to find grazing for zebu cattle, camels, and goats. Output per hectare is extremely low, and the system is acutely vulnerable to prolonged droughts and desertification.",
        "vi": "Chăn thả gia súc du mục vùng Sahel châu Phi: Hệ thống chăn nuôi tự cung tự cấp quảng canh trên các đồng cỏ bán khô hạn cằn cỗi. Người du mục di chuyển theo mùa lần theo những cơn mưa hiếm hoi để tìm nguồn cỏ cho bò u, lạc đà và dê. Năng suất trên mỗi héc-ta cực kỳ thấp và hệ thống này đặc biệt dễ bị tổn thương trước hạn hán kéo dài và quá trình sa mạc hóa."
    },
    {
        "id": "farm_vertical",
        "title": "Hệ thống canh tác: Nông nghiệp thẳng đứng công nghệ cao (Thâm canh thương mại)",
        "selector": "#fbtn-vertical",
        "en": "Indoor Controlled-Environment Vertical Farming: An ultra-intensive commercial arable system built in urban warehouses. Crops grow on vertical stacked shelving using nutrient-rich water mists and tuned LED lights. This system slashes water consumption by 95 percent, eliminates pesticides, and produces year-round yields immune to weather fluctuations, though it requires immense initial capital investment.",
        "vi": "Nông nghiệp thẳng đứng trong nhà công nghệ cao: Hệ thống trồng trọt thương mại siêu thâm canh đặt trong các nhà kho đô thị. Cây trồng phát triển trên các giá tầng xếp chồng thẳng đứng nhờ màng sương giàu dinh dưỡng và ánh sáng đèn LED chuyên dụng. Mô hình này tiết kiệm đến chín mươi lăm phần trăm lượng nước, hoàn toàn không dùng thuốc trừ sâu và cho năng suất quanh năm bất chấp thời tiết, dù đòi hỏi chi phí đầu tư ban đầu rất lớn."
    },
    old_segments['sec_hightech_farming'],
    old_segments['exam_strategy']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_farming_classification": {"start": 1, "end": 1},
    "sec_agricultural_ipo": {"start": 2, "end": 3},
    "sec_ipo_explorer": {"start": 4, "end": 8},
    "sec_hightech_farming": {"start": 9, "end": 9},
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

    # Update buttons with class="lecture-interactive-card" and data-lecture-section
    buttons = [
        ('fbtn-prairies', 'farm_prairies'),
        ('fbtn-ganges', 'farm_ganges'),
        ('fbtn-sahel', 'farm_sahel'),
        ('fbtn-vertical', 'farm_vertical'),
    ]
    for bid, sec_key in buttons:
        # replace button tag
        pat = rf'(<button\s+id="{bid}"\s+onclick="[^"]*")'
        repl = rf'<button id="{bid}" class="lecture-interactive-card" data-lecture-section="{sec_key}" onclick="selectFarm(\'{bid.replace("fbtn-", "")}\')"'
        html = re.sub(pat, repl, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive farm explorer updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
