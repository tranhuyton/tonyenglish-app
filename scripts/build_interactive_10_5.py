import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_5"
LECTURE_ID = "a3a8d904-d277-4eef-b8ff-52a913ebc5f6"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.5 The Global Patterns of Energy Supply and Demand"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_consumption_surges'],
    old_segments['sec_fuel_mix_map'],
    {
        "id": "fuel_na",
        "title": "Cơ cấu năng lượng khu vực: Bắc Mỹ (Khí đá phiến & Dầu mỏ)",
        "selector": "#pin-fuel-na",
        "en": "North America Energy Mix: Dominated by Natural Gas at 35 percent and Oil at 36 percent, with Nuclear at 8 percent and Renewables at 13 percent. The horizontal drilling and hydraulic fracturing revolution unlocked vast domestic shale gas in Texas and Pennsylvania, turning the United States into a massive liquefied natural gas exporter, while coal has precipitously declined.",
        "vi": "Cơ cấu năng lượng khu vực Bắc Mỹ: Khí tự nhiên chiếm ba mươi lăm phần trăm và dầu mỏ chiếm ba mươi sáu phần trăm, hạt nhân tám phần trăm và năng lượng tái tạo mười ba phần trăm. Cuộc cách mạng khoan ngang thủy lực cắt phá đã giải phóng trữ lượng khí đá phiến khổng lồ tại Texas và Pennsylvania, biến Hoa Kỳ thành quốc gia xuất khẩu khí tự nhiên hóa lỏng hàng đầu thế giới, trong khi than đá sụt giảm mạnh."
    },
    {
        "id": "fuel_eu",
        "title": "Cơ cấu năng lượng khu vực: Châu Âu (Chuyển dịch xanh & Điện gió/Mặt trời)",
        "selector": "#pin-fuel-eu",
        "en": "Europe Energy Mix: Oil at 34 percent, Natural Gas at 23 percent, Renewables at 18 percent, and Nuclear at 11 percent. Europe leads global decarbonization policy, aggressively decommissioning coal fired power plants, expanding offshore wind farms in the North Sea, and enforcing rigorous industrial carbon taxes under the European Union Emissions Trading Scheme.",
        "vi": "Cơ cấu năng lượng khu vực Châu Âu: Dầu mỏ ba mươi tư phần trăm, khí tự nhiên hai mươi ba phần trăm, năng lượng tái tạo mười tám phần trăm và điện hạt nhân mười một phần trăm. Châu Âu dẫn đầu thế giới về chính sách phi carbon hóa, kiên quyết đóng cửa các nhà máy nhiệt điện than, bùng nổ các trang trại điện gió ngoài khơi Biển Bắc và áp thuế carbon nghiêm ngặt theo hệ thống hạn ngạch khí thải của Liên minh Châu Âu."
    },
    {
        "id": "fuel_cis",
        "title": "Cơ cấu năng lượng khu vực: CIS / Nga (Độc tôn Khí tự nhiên)",
        "selector": "#pin-fuel-cis",
        "en": "CIS and Russia Energy Mix: Natural Gas constitutes a remarkable 54 percent of primary consumption, Oil 21 percent, and Coal 14 percent. Russia possesses the planet's largest conventional natural gas reserves across Western Siberia and the Yamal Peninsula, utilizing vast pipeline networks to supply domestic power and historical exports across Eurasia.",
        "vi": "Cơ cấu năng lượng khu vực CIS và Nga: Khí tự nhiên chiếm tỷ trọng áp đảo đáng kinh ngạc tới năm mươi tư phần trăm tổng tiêu thụ, dầu mỏ hai mươi mốt phần trăm và than đá mười bốn phần trăm. Nước Nga nắm giữ trữ lượng khí tự nhiên truyền thống lớn nhất hành tinh tại Tây Siberia và bán đảo Yamal, vận hành mạng lưới đường ống khổng lồ để phát điện trong nước và xuất khẩu sang khắp lục địa Á - Âu."
    },
    {
        "id": "fuel_me",
        "title": "Cơ cấu năng lượng khu vực: Trung Đông (100% Dầu mỏ & Khí đốt)",
        "selector": "#pin-fuel-me",
        "en": "Middle East Energy Mix: An absolute duopoly of Oil at 50 percent and Natural Gas at 49 percent, with renewables and nuclear contributing under 1 percent. Domestic electricity and fuel are heavily state-subsidized, driving soaring per capita consumption to power massive seawater desalination plants and intensive summer air conditioning.",
        "vi": "Cơ cấu năng lượng khu vực Trung Đông: Thế độc quyền tuyệt đối giữa dầu mỏ năm mươi phần trăm và khí tự nhiên bốn mươi chín phần trăm, năng lượng tái tạo và hạt nhân chỉ chiếm dưới một phần trăm. Điện và xăng dầu sinh hoạt được nhà nước trợ giá rất lớn, thúc đẩy mức tiêu thụ bình quân đầu người tăng vọt để vận hành các nhà máy khử muối nước biển quy mô lớn và hệ thống điều hòa nhiệt độ mùa hè."
    },
    {
        "id": "fuel_ap",
        "title": "Cơ cấu năng lượng khu vực: Châu Á - Thái Bình Dương (Than đá chiếm ưu thế)",
        "selector": "#pin-fuel-ap",
        "en": "Asia-Pacific Energy Mix: Coal anchors the regional grid at 52 percent, followed by Oil at 25 percent and Gas at 8 percent. Massive coal combustion in China and India has powered unprecedented manufacturing industrialization, even as the region simultaneously installs the world's largest capacities of solar panels and wind turbines.",
        "vi": "Cơ cấu năng lượng khu vực Châu Á - Thái Bình Dương: Than đá giữ vai trò xương sống với năm mươi hai phần trăm, tiếp theo là dầu mỏ hai mươi lăm phần trăm và khí đốt tám phần trăm. Việc đốt than ồ ạt tại Trung Quốc và Ấn Độ là động cơ thúc đẩy công nghiệp hóa sản xuất lịch sử, dù hiện nay khu vực này cũng đang lắp đặt công suất điện mặt trời và điện gió mới lớn nhất thế giới."
    },
    {
        "id": "fuel_sa",
        "title": "Cơ cấu năng lượng khu vực: Nam Mỹ (Siêu cường Thủy điện)",
        "selector": "#pin-fuel-sa",
        "en": "South and Central America Energy Mix: Oil at 45 percent, Hydroelectricity at 26 percent, and Natural Gas at 20 percent. Benefiting from the Amazon and Paraná river basins, the continent is a hydroelectric superpower anchored by mega-dams like Itaipu, alongside Brazil's pioneering sugarcane bioethanol transport program.",
        "vi": "Cơ cấu năng lượng khu vực Nam Mỹ: Dầu mỏ bốn mươi lăm phần trăm, thủy điện hai mươi sáu phần trăm và khí tự nhiên hai mươi phần trăm. Nhờ lưu vực màu mỡ của sông Amazon và sông Paraná, lục địa này là siêu cường thủy điện với các siêu đập như Itaipu, song hành với chương trình nhiên liệu sinh học xăng pha cồn từ mía tiên phong của Brazil."
    },
    old_segments['sec_energy_security'],
    old_segments['exam_strategy']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_consumption_surges": {"start": 1, "end": 1},
    "sec_fuel_mix_map": {"start": 2, "end": 8},
    "sec_energy_security": {"start": 9, "end": 9},
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

    # Update SVG pins with id, class="e-pin lecture-interactive-card", data-lecture-section
    pins = [
        ('na', 'pin-fuel-na', 'fuel_na'),
        ('eu', 'pin-fuel-eu', 'fuel_eu'),
        ('cis', 'pin-fuel-cis', 'fuel_cis'),
        ('me', 'pin-fuel-me', 'fuel_me'),
        ('ap', 'pin-fuel-ap', 'fuel_ap'),
        ('sa', 'pin-fuel-sa', 'fuel_sa'),
    ]
    for key, pid, sec_key in pins:
        pat = rf'<g\s+class="e-pin"\s+onclick="showRegionMix\(\'{key}\'\)"'
        repl = rf'<g id="{pid}" class="e-pin lecture-interactive-card" data-lecture-section="{sec_key}" onclick="showRegionMix(\'{key}\')" style="cursor:pointer;"'
        html = re.sub(pat, repl, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive fuel map updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
