import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "10_4"
LECTURE_ID = "199a26cd-1226-4ff7-b063-f7df7fa7b5ba"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "10.4 How Our Energy is Produced: Energy Mix & Systems"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_energy_taxonomy'],
    old_segments['sec_fuelwood_crisis'],
    old_segments['sec_energy_ladder'],
    {
        "id": "ladder_biomass",
        "title": "Nấc thang năng lượng: Bậc 1 - Sinh khối truyền thống",
        "selector": "#rung-biomass",
        "en": "Energy Ladder Rung 1: Traditional Biomass, including fuelwood, animal dung, and agricultural waste. Predominantly used by over 2.5 billion people in rural low-income countries. While free to gather in nature, it carries immense labor opportunity costs for women and children, delivers under 10 percent thermal efficiency, and produces toxic indoor smoke causing acute respiratory diseases and childhood pneumonia.",
        "vi": "Bậc một trên thang năng lượng: Sinh khối truyền thống, bao gồm củi đốt, phân gia súc và phế phẩm nông nghiệp. Đây là nguồn năng lượng chính của hơn hai tỷ rưỡi người dân tại các vùng nông thôn nghèo. Dù có thể nhặt tự do trong tự nhiên nhưng nó cướp đi lượng lớn thời gian lao động học tập của phụ nữ và trẻ em, hiệu suất nhiệt chỉ đạt dưới mười phần trăm và khói độc trong nhà gây ra các bệnh hô hấp cấp tính và viêm phổi ở trẻ nhỏ."
    },
    {
        "id": "ladder_transition",
        "title": "Nấc thang năng lượng: Bậc 2 - Nhiên liệu chuyển tiếp (Than củi, dầu hỏa)",
        "selector": "#rung-transition",
        "en": "Energy Ladder Rung 2: Transition Fuels, comprising charcoal, kerosene, and coal briquettes. Common in rapidly urbanizing informal settlements. Charcoal offers 20 to 30 percent thermal efficiency and less direct smoke, but traditional earth-kiln production loses 80 percent of original wood energy, accelerating severe deforestation around expanding peri-urban zones.",
        "vi": "Bậc hai trên thang năng lượng: Nhiên liệu chuyển tiếp, bao gồm than củi, dầu hỏa và than bánh. Phổ biến tại các khu ổ chuột đang đô thị hóa nhanh chóng. Than củi cho hiệu suất nhiệt hai mươi đến ba mươi phần trăm và ít khói trực tiếp hơn, nhưng các lò hầm đất truyền thống làm thất thoát tới tám mươi phần trăm năng lượng của gỗ, đẩy nhanh nạn phá rừng quanh các vùng ven đô."
    },
    {
        "id": "ladder_grid",
        "title": "Nấc thang năng lượng: Bậc 3 - Lưới điện tập trung & Khí dầu mỏ hóa lỏng (LPG)",
        "selector": "#rung-grid",
        "en": "Energy Ladder Rung 3: Centralized Grid Electricity and Liquefied Petroleum Gas (LPG). Characterized by high connection fees and recurring utility bills, it delivers clean, instantaneous heat at 50 to 60 percent efficiency with zero indoor air pollution, transforming household productivity, though power generation relies predominantly on central fossil fuel plants.",
        "vi": "Bậc ba trên thang năng lượng: Lưới điện quốc gia tập trung và Khí dầu mỏ hóa lỏng LPG. Dù đòi hỏi phí đấu nối ban đầu và hóa đơn tiền điện hàng tháng, hệ thống mang lại nguồn nhiệt sạch tiện lợi tức thì với hiệu suất năm mươi đến sáu mươi phần trăm và không gây ô nhiễm không khí trong nhà, giúp nâng cao năng suất gia đình dù việc phát điện vẫn dựa chủ yếu vào nhiên liệu hóa thạch."
    },
    {
        "id": "ladder_renewables",
        "title": "Nấc thang năng lượng: Bậc 4 - Năng lượng tái tạo sạch phi tập trung",
        "selector": "#rung-renewables",
        "en": "Energy Ladder Rung 4: Zero-Carbon Clean Renewables and Microgrids. Comprising rooftop solar photovoltaics, micro-hydro turbines, and advanced battery storage. This summit of the ladder eliminates transmission losses and allows developing rural communities to leapfrog expensive fossil fuel power plants directly into clean, resilient energy autonomy.",
        "vi": "Bậc bốn trên thang năng lượng: Năng lượng tái tạo sạch phi tập trung và lưới điện vi mô. Bao gồm các tấm pin mặt trời mái nhà, tuabin thủy điện nhỏ và hệ thống pin lưu trữ hiện đại. Đỉnh cao của thang năng lượng này loại bỏ hoàn toàn tổn thất đường truyền và cho phép các cộng đồng nông thôn nhảy cóc qua giai đoạn nhà máy điện hóa thạch đắt đỏ để tiến thẳng tới tự chủ năng lượng sạch bền vững."
    },
    old_segments['exam_strategy']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_energy_taxonomy": {"start": 1, "end": 1},
    "sec_fuelwood_crisis": {"start": 2, "end": 2},
    "sec_energy_ladder": {"start": 3, "end": 7},
    "card_exam_strategy": {"start": 8, "end": 8}
}

async def main():
    print(f"--- Updating Audio & Manifest for {LECTURE_CODE} ---")
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    html = res.data[0]['content_html']

    # Update SVG rungs with id, class="rung-box lecture-interactive-card", data-lecture-section
    rungs = [
        ('biomass', 'rung-biomass', 'ladder_biomass'),
        ('transition', 'rung-transition', 'ladder_transition'),
        ('grid', 'rung-grid', 'ladder_grid'),
        ('renewables', 'rung-renewables', 'ladder_renewables'),
    ]
    for key, rid, sec_key in rungs:
        pat = rf'<g\s+class="rung-box"\s+onclick="selectRung\(\'{key}\'\)"'
        repl = rf'<g id="{rid}" class="rung-box lecture-interactive-card" data-lecture-section="{sec_key}" onclick="selectRung(\'{key}\')" style="cursor:pointer;"'
        html = re.sub(pat, repl, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive energy ladder updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
