import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "7_1"
LECTURE_ID = "556bc6b6-1555-49a9-a043-35f059b44559"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "7.1 Where People Live"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 7.1: Nơi con người sinh sống",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 7.1: Where People Live. In this lecture, we examine the spatial organization of human settlements: defining urban versus rural spaces, analyzing site and situation factors, mastering Walter Christaller's Central Place Theory and the Settlement Hierarchy, understanding global urbanization rates, and tracking the four phases of the Urbanisation Cycle.",
        "vi": "Chào mừng các em đến với bài bảy chấm một: Nơi con người sinh sống. Trong bài học này, chúng ta sẽ khảo sát sự phân bố không gian của các điểm định cư: phân biệt khu vực nông thôn và đô thị, phân tích các yếu tố vị trí điểm và vị trí thế, nắm vững Lý thuyết Điểm Trung tâm của Walter Christaller và Hệ thống cấp bậc định cư, tìm hiểu tốc độ đô thị hóa toàn cầu, và theo dõi bốn giai đoạn của chu kỳ đô thị hóa."
    },
    {
        "id": "sec_site_situation",
        "title": "1. Điểm định cư đô thị và nông thôn: Vị trí điểm và vị trí thế",
        "selector": "#sec-site-situation",
        "en": "Section 1 classifies settlements by their functional character. Rural settlements in the countryside focus on primary industries like agriculture and fishing, featuring low population densities. Urban settlements in towns and cities are dominated by secondary manufacturing and tertiary services, functioning as regional commercial hubs.",
        "vi": "Mục một phân loại các điểm định cư theo chức năng. Điểm định cư nông thôn tập trung vào các ngành kinh tế cấp một như nông nghiệp và đánh bắt thủy sản, với mật độ dân số thấp. Điểm định cư đô thị tại các thị trấn và thành phố chủ yếu phát triển công nghiệp chế biến và dịch vụ thương mại, đóng vai trò là hạt nhân kinh tế của cả vùng."
    },
    {
        "id": "site_situation_factors",
        "title": "Phân biệt Vị trí điểm (Site) và Vị trí thế (Situation)",
        "selector": "#card-site-factors",
        "en": "Site refers to the actual physical terrain on which a settlement is built, such as dry-point elevated ground to avoid flooding, wet-point water access, defensive hilltops, or river bridging points. Situation describes the settlement's geographic location relative to surrounding regions, trade networks, and valley crossroads.",
        "vi": "Vị trí điểm Site là địa hình vật lý thực tế nơi điểm định cư được xây dựng, ví dụ như gò đất cao tránh ngập, nơi có nguồn nước ngọt, đỉnh đồi phòng thủ, hay điểm bắc cầu qua sông. Còn vị trí thế Situation mô tả mối tương quan vị trí của điểm định cư đó đối với các vùng lân cận, mạng lưới giao thương và các trục thung lũng xung quanh."
    },
    {
        "id": "sec_settlement_hierarchy",
        "title": "2. Hệ thống cấp bậc định cư và Lý thuyết Điểm Trung tâm",
        "selector": "#sec-settlement-hierarchy",
        "en": "Section 2 investigates the Settlement Hierarchy. Across any territory, there are vast numbers of small hamlets and villages offering basic services, fewer medium-sized towns, and only a tiny handful of major cities and conurbations providing specialized functions.",
        "vi": "Mục hai nghiên cứu Hệ thống cấp bậc định cư. Trên bất kỳ vùng lãnh thổ nào, số lượng thôn xóm và làng mạc cung cấp dịch vụ cơ bản luôn rất lớn, số lượng thị trấn ít hơn, và chỉ có một số rất ít các thành phố lớn hoặc chùm đô thị cung cấp các dịch vụ chuyên sâu cao cấp."
    },
    {
        "id": "hierarchy_model",
        "title": "Mô hình kim tự tháp hệ thống định cư",
        "selector": "#card-hierarchy-model",
        "en": "As you move up the settlement hierarchy: settlement size increases, the sphere of influence widens, and services become higher-order, while the total frequency of such settlements sharply decreases.",
        "vi": "Càng lên cao trong hệ thống cấp bậc định cư: quy mô dân số càng lớn, vùng ảnh hưởng càng mở rộng, các dịch vụ càng chuyên môn hóa cao cấp, trong khi số lượng các điểm định cư thuộc cấp đó lại giảm mạnh."
    },
    {
        "id": "central_place_theory",
        "title": "Ba nguyên lý của Lý thuyết Điểm Trung tâm",
        "selector": "#card-central-place-theory",
        "en": "Christaller's Central Place Theory rests on three concepts: Range is the maximum distance consumers will travel for a good; Threshold Population is the minimum customer base needed for a service to remain viable; and Sphere of Influence is the geographic catchment area served.",
        "vi": "Lý thuyết Điểm Trung tâm của Christaller dựa trên ba nguyên lý: Phạm vi tiếp cận là khoảng cách tối đa người mua sẵn sàng di chuyển; Dân số ngưỡng là lượng khách hàng tối thiểu để một dịch vụ duy trì sinh lời; và Vùng ảnh hưởng là lưu vực địa lý mà điểm trung tâm đó phục vụ."
    },
    {
        "id": "sec_settlement_patterns",
        "title": "3. Hình thái và phân bố không gian của điểm định cư",
        "selector": "#sec-settlement-patterns",
        "en": "Section 3 outlines three distinct morphological patterns: Nucleated settlements cluster tightly around a central church, green, or crossroad; Linear settlements stretch along a road, river, or narrow valley floor; and Dispersed settlements consist of isolated farmsteads scattered across rugged pastoral highlands.",
        "vi": "Mục ba khái quát ba dạng hình thái định cư: Định cư tập trung quây quần quanh nhà thờ, quảng trường hoặc ngã tư đường; Định cư tuyến tính trải dài dọc theo con đường, bờ sông hoặc đáy thung lũng hẹp; và Định cư phân tán gồm các trang trại nằm rải rác trên vùng đồi núi chăn thả rộng lớn."
    },
    {
        "id": "sec_urbanisation_rate",
        "title": "4. Tiến trình và tốc độ đô thị hóa toàn cầu",
        "selector": "#sec-urbanisation-rate",
        "en": "Section 4 tracks global urban expansion. In 2008, the world's urban population exceeded fifty percent for the first time in history.",
        "vi": "Mục bốn theo dõi sự mở rộng đô thị trên toàn cầu. Vào năm 2008, lần đầu tiên trong lịch sử nhân loại, dân số đô thị toàn cầu đã chính thức vượt qua mốc năm mươi phần trăm."
    },
    {
        "id": "urban_rate_vs_level",
        "title": "Phân biệt Tỉ lệ đô thị hóa và Tốc độ đô thị hóa",
        "selector": "#card-urban-rate-vs-level",
        "en": "Examiners test the critical distinction between level and rate: Level of Urbanisation is the percentage already in cities, which is high in HICs but growing very slowly; while Rate of Urbanisation is the annual growth velocity, which is highest in developing nations due to intense rural-to-urban migration.",
        "vi": "Đề thi đặc biệt chú trọng phân biệt giữa mức độ và tốc độ: Mức độ đô thị hóa là tỉ lệ phần trăm dân số sống ở thành thị, rất cao ở các nước phát triển nhưng tăng rất chậm; còn Tốc độ đô thị hóa là vận tốc gia tăng hàng năm, hiện đang diễn ra nhanh nhất tại các nước đang phát triển do dòng di cư ồ ạt từ nông thôn ra thành thị."
    },
    {
        "id": "sec_urbanisation_cycle",
        "title": "5. Chu kỳ đô thị hóa bốn giai đoạn không gian",
        "selector": "#sec-urbanisation-cycle",
        "en": "Section 5 details the four evolutionary phases of the urban cycle: initial Urbanisation inward to the core; Suburbanisation outward to green suburban edges; Counter-urbanisation leaping across greenbelts into rural villages; and Re-urbanisation regenerating brownfield docklands back into luxury inner-city living.",
        "vi": "Mục năm phân tích bốn giai đoạn tiến hóa của chu kỳ đô thị: giai đoạn Đô thị hóa hướng tâm vào lõi trung tâm; giai đoạn Đô thị hóa ngoại ô ly tâm ra vùng ven; giai đoạn Phản đô thị hóa nhảy cóc qua vành đai xanh về các làng quê; và giai đoạn Tái đô thị hóa hồi sinh các khu công nghiệp và bến cảng cũ thành căn hộ cao cấp tại trung tâm."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược làm bài thi IGCSE về Đô thị hóa",
        "selector": "#card-exam-strategy",
        "en": "In your exam answers: master Christaller's terms range, threshold, and sphere of influence; clearly explain site versus situation; and describe the push and pull forces operating across each of the four urbanisation cycle phases.",
        "vi": "Khi làm bài thi IGCSE: các em hãy vận dụng thành thạo các thuật ngữ phạm vi, dân số ngưỡng và vùng ảnh hưởng; giải thích rành mạch vị trí điểm và vị trí thế; đồng thời phân tích rõ các lực đẩy và lực kéo diễn ra trong từng giai đoạn của chu kỳ đô thị hóa."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_site_situation": {"start": 1, "end": 2},
    "sec_settlement_hierarchy": {"start": 3, "end": 5},
    "sec_settlement_patterns": {"start": 6, "end": 6},
    "sec_urbanisation_rate": {"start": 7, "end": 8},
    "sec_urbanisation_cycle": {"start": 9, "end": 10}
}

def transform_html(raw_html):
    html = raw_html

    # Intro banner
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25);">',
        '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 60%, #14b8a6 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(13, 148, 136, 0.25); cursor:pointer;">'
    )

    # Section 1 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    1. Urban and Rural Settlements: Site and Situation Factors\n  </h2>',
        '<h2 id="sec-site-situation" class="lecture-interactive-card" data-lecture-section="sec_site_situation" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    1. Urban and Rural Settlements: Site and Situation Factors\n  </h2>'
    )

    # Site vs Situation box
    html = html.replace(
        '<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:18px; margin:18px 0;">',
        '<div id="card-site-factors" class="lecture-interactive-card" data-lecture-section="site_situation_factors" style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:18px; margin:18px 0; cursor:pointer;">'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    2. The Settlement Hierarchy & Central Place Theory\n  </h2>',
        '<h2 id="sec-settlement-hierarchy" class="lecture-interactive-card" data-lecture-section="sec_settlement_hierarchy" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    2. The Settlement Hierarchy & Central Place Theory\n  </h2>'
    )

    # Hierarchy Vector Card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#0d9488; border-radius:50%;"></span>\n    Interactive Vector Model: The Urban Settlement Hierarchy & Central Place Matrix',
        '<div id="card-hierarchy-model" class="lecture-interactive-card" data-lecture-section="hierarchy_model" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#0d9488; border-radius:50%;"></span>\n    Interactive Vector Model: The Urban Settlement Hierarchy & Central Place Matrix'
    )

    # Central Place Theory box
    html = html.replace(
        '<div style="display:flex; flex-direction:column; gap:14px; margin:20px 0;">',
        '<div id="card-central-place-theory" class="lecture-interactive-card" data-lecture-section="central_place_theory" style="display:flex; flex-direction:column; gap:14px; margin:20px 0; cursor:pointer;">'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    3. Settlement Patterns and Morphologies\n  </h2>',
        '<h2 id="sec-settlement-patterns" class="lecture-interactive-card" data-lecture-section="sec_settlement_patterns" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    3. Settlement Patterns and Morphologies\n  </h2>'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    4. The Process and Global Rate of Urbanisation\n  </h2>',
        '<h2 id="sec-urbanisation-rate" class="lecture-interactive-card" data-lecture-section="sec_urbanisation_rate" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    4. The Process and Global Rate of Urbanisation\n  </h2>'
    )

    # Level vs Rate callout box
    html = html.replace(
        '<div style="background:#fef2f2; border-left:4px solid #ef4444; padding:16px; border-radius:8px; margin:18px 0;">',
        '<div id="card-urban-rate-vs-level" class="lecture-interactive-card" data-lecture-section="urban_rate_vs_level" style="background:#fef2f2; border-left:4px solid #ef4444; padding:16px; border-radius:8px; margin:18px 0; cursor:pointer;">'
    )

    # Section 5 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    5. The Cycle of Urbanisation: 4 Spatial Phases\n  </h2>',
        '<h2 id="sec-urbanisation-cycle" class="lecture-interactive-card" data-lecture-section="sec_urbanisation_cycle" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    5. The Cycle of Urbanisation: 4 Spatial Phases\n  </h2>'
    )

    # Exam strategy card
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); border:1px solid #99f6e4; border-left:6px solid #0d9488; border-radius:10px; padding:20px; margin:32px 0;">',
        '<div id="card-exam-strategy" class="lecture-interactive-card" data-lecture-section="exam_strategy" style="background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%); border:1px solid #99f6e4; border-left:6px solid #0d9488; border-radius:10px; padding:20px; margin:32px 0; cursor:pointer;">'
    )

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
