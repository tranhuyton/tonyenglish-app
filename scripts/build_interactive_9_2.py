import asyncio
import os
import re
import sys
import json
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

LECTURE_CODE = "9_2"
LECTURE_ID = "5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "9.2 The Impact of Globalisation and the Role of Transnational Corporations (TNCs)"

# Load existing manifest to reuse existing audio
m_path = f"public/audio/lectures/geography/{LECTURE_CODE}/manifest.json"
with open(m_path, 'r', encoding='utf-8') as f:
    old_manifest = json.load(f)

old_segments = {s['id']: s for s in old_manifest['segments']}

SEGMENTS = [
    old_segments['intro'],
    old_segments['sec_globalisation'],
    old_segments['globalisation_factors'],
    old_segments['sec_what_is_tnc'],
    old_segments['tnc_structure_svg'],
    old_segments['sec_nike_supply_chain'],
    old_segments['nike_map_svg'],
    {
        "id": "nike_hq",
        "title": "Chuỗi cung ứng Nike: Trụ sở chính (Oregon, Hoa Kỳ)",
        "selector": "#node-nike-hq",
        "en": "Nike Global Headquarters, Beaverton, Oregon: The high-value brain of the transnational corporation. Directly employs thousands of specialized professionals in product research, advanced material engineering, brand marketing, and global financial control. Nike captures maximum economic value here by retaining intellectual property and high-margin design while owning zero manufacturing factories.",
        "vi": "Trụ sở chính toàn cầu của Nike tại bang Oregon, Hoa Kỳ: Trung tâm đầu não giá trị cao của tập đoàn đa quốc gia. Nơi đây tập trung hàng nghìn chuyên gia nghiên cứu thiết kế sản phẩm, kỹ thuật vật liệu mới, chiến dịch tiếp thị thương hiệu và quản lý tài chính toàn cầu. Nike giữ lại phần lớn giá trị gia tăng nhờ sở hữu quyền sở hữu trí tuệ và mẫu mã độc quyền dù hoàn toàn không trực tiếp sở hữu bất kỳ nhà máy gia công nào."
    },
    {
        "id": "nike_factories",
        "title": "Chuỗi cung ứng Nike: Nhà máy gia công (Việt Nam & Trung Quốc)",
        "selector": "#node-nike-factories",
        "en": "Nike Subcontracted Factories in Vietnam and China: Nike outsources 100 percent of shoe and apparel assembly to independent supplier factories in developing Asian nations. This spatial separation exploits competitive labor costs, tax holidays in Export Processing Zones, and flexible workforces. It generates vital industrial wages and export revenues for host countries, but historically faced scrutiny regarding worker overtime and shop-floor conditions.",
        "vi": "Nhà máy gia công hợp đồng của Nike tại Việt Nam và Trung Quốc: Nike thuê ngoài một trăm phần trăm công đoạn may và lắp ráp giày cho các nhà máy đối tác độc lập tại châu Á. Chiến lược phân tán không gian này nhằm tận dụng chi phí nhân công cạnh tranh, các ưu đãi thuế tại khu chế xuất và nguồn lao động dồi dào. Mô hình này mang lại thu nhập công nghiệp và kim ngạch xuất khẩu quan trọng cho các nước tiếp nhận, dù từng đối mặt với nhiều giám sát về điều kiện làm việc và giờ làm thêm của công nhân."
    },
    {
        "id": "nike_materials",
        "title": "Chuỗi cung ứng Nike: Vùng nguyên liệu thô (Cao su & Da thuộc)",
        "selector": "#node-nike-materials",
        "en": "Raw Material Sourcing: Rubber plantations in Southeast Asia, petroleum-derived synthetic polymers in Taiwan, and leather tanneries in Brazil supply specialized components to Nike's assembly plants. Raw material prices represent only a minuscule fraction—typically under 5 percent—of the final retail shoe price, illustrating unequal terms of trade between primary commodity suppliers and brand-holding corporations.",
        "vi": "Cung ứng nguyên liệu thô của Nike: Các đồn điền cao su ở Đông Nam Á, polyme nhân tạo gốc dầu mỏ từ Đài Loan và xưởng da thuộc ở Brazil cung cấp linh kiện chuyên biệt tới các nhà máy lắp ráp. Giá trị nguyên liệu thô chỉ chiếm một tỷ lệ rất nhỏ, thường dưới năm phần trăm giá bán lẻ cuối cùng của một đôi giày, minh chứng cho sự bất bình đẳng trong chuỗi giá trị giữa các nhà cung cấp sơ cấp và các tập đoàn sở hữu thương hiệu."
    },
    {
        "id": "nike_sales",
        "title": "Chuỗi cung ứng Nike: Thị trường bán lẻ toàn cầu (Bắc Mỹ, Châu Âu, Châu Á)",
        "selector": "#node-nike-sales",
        "en": "Global Retail & Digital Distribution: Finished footwear is shipped via high-capacity container vessels through mega-ports like Singapore and Rotterdam to flagship retail hubs in North America, Western Europe, and rapidly growing consumer markets in Asia. Massive corporate advertising campaigns featuring elite athlete endorsements allow Nike to sell shoes for well over 100 dollars that cost merely a few dollars to physically assemble.",
        "vi": "Thị trường phân phối và bán lẻ toàn cầu của Nike: Giày hoàn thiện được vận chuyển bằng các tàu container sức chở lớn qua các siêu cảng biển như Singapore và Rotterdam tới các trung tâm bán lẻ tại Bắc Mỹ, Tây Âu và thị trường tiêu dùng đang bùng nổ ở châu Á. Các chiến dịch quảng cáo trị giá hàng tỷ đô la gắn với các vận động viên ngôi sao cho phép Nike bán một đôi giày với giá hơn một trăm đô la dù chi phí nhân công trực tiếp lắp ráp chỉ tốn vài đô la."
    },
    old_segments['sec_tnc_impacts'],
    old_segments['tnc_impacts_list']
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_globalisation": {"start": 1, "end": 2},
    "sec_what_is_tnc": {"start": 3, "end": 4},
    "sec_nike_supply_chain": {"start": 5, "end": 10},
    "sec_tnc_impacts": {"start": 11, "end": 12}
}

async def main():
    print(f"--- Updating Audio & Manifest for {LECTURE_CODE} ---")
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    html = res.data[0]['content_html']

    # Update Nike SVG nodes with wrapping <g id="..." class="lecture-interactive-card" data-lecture-section="..." style="cursor:pointer;">
    # 1. HQ (Oregon, USA)
    pat_hq = r'(<!-- HQ \(Oregon, USA\) -->\s*<circle cx="150" cy="140"[^>]*>[\s\S]*?<text [^>]*>Design &amp; Marketing</text>)'
    repl_hq = r'<g id="node-nike-hq" class="lecture-interactive-card" data-lecture-section="nike_hq" style="cursor:pointer;">\n    \1\n    </g>'
    if 'node-nike-hq' not in html:
        html = re.sub(pat_hq, repl_hq, html)

    # 2. Factories (Vietnam/China)
    pat_fact = r'(<!-- Manufacturing \(Vietnam/China\) -->\s*<circle cx="620" cy="210"[^>]*>[\s\S]*?<text [^>]*>Low wage manufacturing</text>)'
    repl_fact = r'<g id="node-nike-factories" class="lecture-interactive-card" data-lecture-section="nike_factories" style="cursor:pointer;">\n    \1\n    </g>'
    if 'node-nike-factories' not in html:
        html = re.sub(pat_fact, repl_fact, html)

    # 3. Materials (Brazil/India)
    pat_mat = r'(<!-- Materials \(Brazil/India\) -->\s*<circle cx="280" cy="270"[^>]*>[\s\S]*?<text [^>]*>Raw Materials \(Rubber\)</text>)'
    repl_mat = r'<g id="node-nike-materials" class="lecture-interactive-card" data-lecture-section="nike_materials" style="cursor:pointer;">\n    \1\n    </g>'
    if 'node-nike-materials' not in html:
        html = re.sub(pat_mat, repl_mat, html)

    # 4. Global Sales (Europe)
    pat_sales = r'(<!-- Global Sales \(Europe\) -->\s*<circle cx="400" cy="120"[^>]*>[\s\S]*?<text [^>]*>Sales \(Europe/Global\)</text>)'
    repl_sales = r'<g id="node-nike-sales" class="lecture-interactive-card" data-lecture-section="nike_sales" style="cursor:pointer;">\n    \1\n    </g>'
    if 'node-nike-sales' not in html:
        html = re.sub(pat_sales, repl_sales, html)

    # Check div balance
    open_divs = len(re.findall(r'<div\b', html, re.I))
    close_divs = len(re.findall(r'</div>', html, re.I))
    diff = open_divs - close_divs
    print(f"Lecture {LECTURE_CODE}: Open={open_divs}, Close={close_divs}, Diff={diff}")
    assert diff == 0, f"Div balance mismatch: Diff={diff}"

    update_supabase_page(LECTURE_ID, html)
    print(f"Lecture {LECTURE_CODE} interactive Nike supply chain map updated successfully!\n")

if __name__ == '__main__':
    asyncio.run(main())
