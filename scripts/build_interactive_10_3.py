import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_3"
LECTURE_ID = "96d7f427-3b6d-43e3-84dc-f8f052f20033"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.3 The Challenges of Food Supply: Food Insecurity & Solutions"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_food_security'],
    old_segments['sec_insecurity_hotspots'],
    {
        "id": "hunger_nigeria",
        "title": "Điểm nóng mất an ninh lương thực: Nigeria (Xung đột & lạm phát)",
        "selector": "#pin-hunger-nigeria",
        "en": "Nigeria Food Crisis: A complex humanitarian emergency driven by armed conflict and macroeconomic shocks. In Borno state, Boko Haram attacks displaced over two million farmers from fertile croplands. Desertification pushes Fulani pastoralists southward into violent clash with crop farmers, while currency devaluation tripled the price of imported fertilizers.",
        "vi": "Khủng hoảng lương thực tại Nigeria: Tình trạng khẩn cấp nhân đạo phức tạp bắt nguồn từ xung đột vũ trang và các cú sốc kinh tế vĩ mô. Tại bang Borno, các cuộc tấn công của nhóm khủng bố Boko Haram đã buộc hơn hai triệu nông dân phải bỏ hoang đồng ruộng màu mỡ. Quá trình sa mạc hóa đẩy người du mục chăn thả Fulani xuống phía nam gây xung đột đẫm máu với nông dân trồng trọt, trong khi đồng nội tệ mất giá đã làm tăng gấp ba chi phí phân bón nhập khẩu."
    },
    {
        "id": "hunger_haiti",
        "title": "Điểm nóng mất an ninh lương thực: Haiti (Thiên tai & nghịch lý viện trợ)",
        "selector": "#pin-hunger-haiti",
        "en": "Haiti Hazard Vulnerability & Aid Dilemma: Consecutive disasters—including the devastating 2010 earthquake and Hurricane Matthew—wrecked rural irrigation infrastructure. While emergency international food shipments save lives during famines, prolonged dumping of subsidized foreign rice undercut local peasant farmers, bankrupting domestic agriculture and worsening chronic dependence.",
        "vi": "Điểm nóng thiên tai và nghịch lý viện trợ tại Haiti: Những thảm họa liên tiếp gồm trận động đất kinh hoàng năm 2010 và bão Matthew đã phá hủy hoàn toàn hệ thống kênh mương tưới tiêu nông thôn. Mặc dù hàng cứu trợ lương thực khẩn cấp quốc tế giúp cứu sống hàng triệu người lúc đói kém, nhưng việc viện trợ gạo ngoại giá rẻ kéo dài đã bóp chết nông dân bản địa, phá hủy nền sản xuất nông nghiệp trong nước và làm trầm trọng thêm sự lệ thuộc."
    },
    {
        "id": "hunger_peru",
        "title": "Điểm nóng thích ứng lương thực: Peru (Bậc thang Andes & bản địa)",
        "selector": "#pin-hunger-peru",
        "en": "Peru Andean Terracing and Indigenous Adaptation: Smallholder mountain farmers in the Andes preserve centuries-old Incan stone terraces known as andenes. Terraces convert steep, erosion-prone mountain slopes into stable agricultural platforms, and dark stone retaining walls absorb solar heat during high-altitude days to protect potato and quinoa crops from freezing nighttime frosts.",
        "vi": "Thích ứng bản địa vùng núi Andes Peru: Nông dân miền núi Peru duy trì các bậc thang đá hàng trăm năm tuổi của nền văn minh Inca được gọi là andenes. Ruộng bậc thang biến các sườn dốc dễ xói mòn thành các thềm canh tác ổn định, đồng thời các bức tường đá tối màu hấp thụ nhiệt mặt trời vào ban ngày để sưởi ấm bảo vệ cây khoai tây và hạt diêm mạch khỏi sương giá băng giá ban đêm."
    },
    {
        "id": "hunger_spain",
        "title": "Điểm nóng quản lý nước: Tây Ban Nha (Tưới chính xác & nhiễm mặn)",
        "selector": "#pin-hunger-spain",
        "en": "Spain Precision Irrigation and Soil Salinisation: In arid southern Spain, traditional furrow and excessive spray irrigation caused severe water table rise and rapid surface evaporation, leaving toxic salt crusts that sterilize productive soils. Farmers are now adopting computer-controlled subsurface drip systems and treated wastewater reuse to conserve water without inducing salinisation.",
        "vi": "Tưới tiêu chính xác và chống mặn hóa đất tại Tây Ban Nha: Tại miền nam khô hạn của Tây Ban Nha, kỹ thuật tưới tràn và tưới phun quá mức từng làm mực nước ngầm dâng cao và bốc hơi cực nhanh, để lại các lớp muối độc làm chai cứng đất trồng. Hiện nay nông dân đang chuyển đổi sang hệ thống tưới nhỏ giọt ngầm dưới rễ điều khiển bằng máy tính và tái sử dụng nước thải đã qua xử lý nhằm bảo tồn nguồn nước mà không gây mặn hóa đất."
    },
    {
        "id": "hunger_vietnam",
        "title": "Điểm nóng an ninh lương thực: Việt Nam (Đồng bằng sông Cửu Long & xâm nhập mặn)",
        "selector": "#pin-hunger-vietnam",
        "en": "Vietnam Mekong Delta Rice Security: The Mekong Delta produces over 50 percent of Vietnam's national rice output and 90 percent of rice exports. However, upstream hydropower dams holding back freshwater combined with rising sea levels cause sea salinity to penetrate up to 70 kilometers inland during dry seasons, driving farmers to rotate seasonal rice with brackish-water shrimp aquaculture.",
        "vi": "An ninh lương thực Đồng bằng sông Cửu Long Việt Nam: Vựa lúa này cung cấp hơn năm mươi phần trăm tổng sản lượng lúa cả nước và chín mươi phần trăm lượng gạo xuất khẩu của Việt Nam. Tuy nhiên, các đập thủy điện thượng nguồn giữ nước ngọt kết hợp với biến đổi khí hậu nước biển dâng khiến xâm nhập mặn lấn sâu tới bảy mươi ki-lô-mét vào nội đồng trong mùa khô, buộc nông dân phải thích ứng bằng mô hình luân canh một vụ lúa một vụ tôm nước lợ."
    },
    old_segments['malthus_boserup'],
    old_segments['sec_nigeria_crisis'],
    old_segments['sec_sustainable_food'],
    old_segments['exam_strategy']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_food_security": {"start": 1, "end": 1},
    "sec_insecurity_hotspots": {"start": 2, "end": 7},
    "card_malthus_boserup": {"start": 8, "end": 8},
    "sec_nigeria_crisis": {"start": 9, "end": 9},
    "sec_sustainable_food": {"start": 10, "end": 10},
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

    # Update SVG pins with id, class="h-pin lecture-interactive-card", data-lecture-section
    pins = [
        ('nigeria', 'pin-hunger-nigeria', 'hunger_nigeria'),
        ('haiti', 'pin-hunger-haiti', 'hunger_haiti'),
        ('peru', 'pin-hunger-peru', 'hunger_peru'),
        ('spain', 'pin-hunger-spain', 'hunger_spain'),
        ('vietnam', 'pin-hunger-vietnam', 'hunger_vietnam'),
    ]
    for key, pid, sec_key in pins:
        pat = rf'<g\s+class="h-pin"\s+onclick="showHungerCase\(\'{key}\'\)"'
        repl = rf'<g id="{pid}" class="h-pin lecture-interactive-card" data-lecture-section="{sec_key}" onclick="showHungerCase(\'{key}\')" style="cursor:pointer;"'
        html = re.sub(pat, repl, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive hunger map updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
