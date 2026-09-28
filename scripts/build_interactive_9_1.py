import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "9_1"
LECTURE_ID = "6c14f92b-774a-45d1-a68d-2e9fe5e0b85d"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "9.1 Changing Employment Structures"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_four_sectors'],
    old_segments['four_sectors_grid'],
    old_segments['sec_employment_map'],
    old_segments['employment_map_svg'],
    {
        "id": "emp_mali",
        "title": "Cơ cấu lao động: Mali (Quốc gia thu nhập thấp - LIC)",
        "selector": "#pin-emp-mali",
        "en": "Mali Employment Structure: Classified as a low-income country in the pre-industrial stage. 80 percent of the labor force works in the primary sector—dominated by smallholder subsistence farming, cotton cultivation, and artisanal mining. Low levels of mechanization mean farming requires vast human labor, leaving only 10 percent in secondary processing and 10 percent in basic tertiary services.",
        "vi": "Cơ cấu việc làm tại Mali: Điển hình cho quốc gia thu nhập thấp ở giai đoạn tiền công nghiệp. Có tới tám mươi phần trăm lực lượng lao động làm việc trong khu vực một sơ khai, chủ yếu là làm nông tự cung tự cấp, trồng bông và khai thác thủ công. Do mức độ cơ giới hóa rất thấp, sản xuất nông nghiệp cần lượng lớn sức người, khiến khu vực hai sản xuất công nghiệp chỉ chiếm mười phần trăm và dịch vụ sơ cấp mười phần trăm."
    },
    {
        "id": "emp_vietnam",
        "title": "Cơ cấu lao động: Việt Nam (Quốc gia mới công nghiệp hóa - MIC / NIC)",
        "selector": "#pin-emp-vietnam",
        "en": "Vietnam Employment Structure: An exemplary middle-income country experiencing rapid industrialization. Primary employment has steadily dropped to 35 percent, while secondary manufacturing and construction has surged to 30 percent, driven by massive foreign direct investment in electronics and apparel export factories. The tertiary service sector has expanded in tandem to 35 percent.",
        "vi": "Cơ cấu việc làm tại Việt Nam: Hình mẫu cho quốc gia thu nhập trung bình và mới công nghiệp hóa nhanh chóng. Tỷ lệ lao động nông nghiệp đã giảm đều đặn xuống còn ba mươi lăm phần trăm, trong khi khu vực hai gồm chế biến chế tạo và xây dựng tăng vọt lên ba mươi phần trăm nhờ dòng vốn đầu tư trực tiếp nước ngoài khổng lồ vào các nhà máy lắp ráp điện tử và dệt may xuất khẩu. Khu vực ba dịch vụ cũng mở rộng song hành đạt ba mươi lăm phần trăm."
    },
    {
        "id": "emp_usa",
        "title": "Cơ cấu lao động: Hoa Kỳ (Kinh tế hậu công nghiệp - HIC)",
        "selector": "#pin-emp-usa",
        "en": "United States Employment Structure: A mature high-income post-industrial economy. The primary sector employs barely 2 percent of the workforce due to colossal agricultural mechanization and GPS combine harvesters. Secondary manufacturing accounts for only 15 percent due to foreign outsourcing, while an overwhelming 83 percent of jobs are in tertiary and quaternary knowledge services such as corporate finance, healthcare, and software engineering.",
        "vi": "Cơ cấu việc làm tại Hoa Kỳ: Nền kinh tế hậu công nghiệp phát triển thu nhập cao. Khu vực nông nghiệp sơ cấp chỉ còn chiếm vẻn vẹn hai phần trăm lao động nhờ cơ giới hóa quy mô lớn và máy gặt định vị vệ tinh. Khu vực hai công nghiệp chế tạo chỉ chiếm mười lăm phần trăm do xu hướng gia công sản xuất ở nước ngoài, trong khi có tới tám mươi ba phần trăm lao động tập trung vào khu vực dịch vụ bậc ba và kinh tế tri thức bậc bốn như tài chính, y tế và phần mềm."
    },
    {
        "id": "emp_uk",
        "title": "Cơ cấu lao động: Vương quốc Anh (Kinh tế hậu công nghiệp - HIC)",
        "selector": "#pin-emp-uk",
        "en": "United Kingdom Employment Structure: A pioneering post-industrial nation shaped by late-twentieth-century deindustrialization. Primary agriculture employs merely 1 percent of workers, and secondary manufacturing has contracted to 18 percent. Over 81 percent of workers are employed in tertiary and high-tech quaternary sectors, including London's global financial hub, international higher education, and biomedical research.",
        "vi": "Cơ cấu việc làm tại Vương quốc Anh: Quốc gia hậu công nghiệp tiên phong được định hình bởi làn sóng phi công nghiệp hóa cuối thế kỷ hai mươi. Nông nghiệp chỉ chiếm vỏn vẹn một phần trăm lao động và công nghiệp chế tạo thu hẹp còn mười tám phần trăm. Hơn tám mươi mốt phần trăm người lao động làm việc trong khu vực dịch vụ bậc ba và công nghệ cao bậc bốn, nổi bật là trung tâm tài chính toàn cầu Luân Đôn, giáo dục đại học quốc tế và nghiên cứu y sinh học."
    },
    old_segments['sec_clark_fisher'],
    old_segments['clark_fisher_svg'],
    old_segments['triangular_graph'],
    old_segments['sec_product_chain'],
    old_segments['product_chain_svg']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_four_sectors": {"start": 1, "end": 2},
    "sec_employment_map": {"start": 3, "end": 8},
    "sec_clark_fisher": {"start": 9, "end": 10},
    "card_triangular_graph": {"start": 11, "end": 11},
    "sec_product_chain": {"start": 12, "end": 13}
}

async def main():
    print(f"--- Updating Audio & Manifest for {LECTURE_CODE} ---")
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    html = res.data[0]['content_html']

    # Update SVG points with id, class="map-point lecture-interactive-card", data-lecture-section
    points = [
        ('Mali', 'pin-emp-mali', 'emp_mali'),
        ('Vietnam', 'pin-emp-vietnam', 'emp_vietnam'),
        ('USA', 'pin-emp-usa', 'emp_usa'),
        ('UK', 'pin-emp-uk', 'emp_uk'),
    ]
    for country, pid, sec_key in points:
        pat = rf'(<circle\s+class="map-point"\s+[^>]*data-country="{country}"[^>]*>)'
        repl = rf'<circle id="{pid}" class="map-point lecture-interactive-card" data-lecture-section="{sec_key}" \1'
        # simpler clean regex replacement
        html = re.sub(
            rf'<circle\s+class="map-point"(\s+[^>]*data-country="{country}"[^>]*)>',
            rf'<circle id="{pid}" class="map-point lecture-interactive-card" data-lecture-section="{sec_key}"\1>',
            html
        )

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive employment map updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
