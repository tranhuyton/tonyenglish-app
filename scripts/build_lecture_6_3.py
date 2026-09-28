import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "6_3"
LECTURE_ID = "33c91ae9-b13f-49d7-b29f-0c3b794d192d"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "6.3 Causes and Impacts of International Migration"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 6.3: Nguyên nhân và tác động của Di cư quốc tế",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 6.3: Causes and Impacts of International Migration. In this lecture, we investigate the spatial movement of people: distinguishing voluntary economic migrants from forced refugees, mastering Everett Lee's Push-Pull Model, evaluating bilateral source versus destination impacts, and analyzing major case studies including the Mexico to United States corridor and the Syrian refugee displacement.",
        "vi": "Chào mừng các em đến với bài sáu chấm ba: Nguyên nhân và tác động của Di cư quốc tế. Trong bài giảng này, chúng ta sẽ khảo sát sự dịch chuyển không gian của con người: phân biệt người di cư kinh tế tự nguyện với người tị nạn cưỡng bức, nắm vững Mô hình Đẩy và Kéo của Everett Lee, đánh giá tác động hai chiều giữa nước xuất cư và nhập cư, đồng thời phân tích các nghiên cứu tình huống điển hình như hành lang Mexico - Hoa Kỳ và cuộc khủng hoảng tị nạn Syria."
    },
    {
        "id": "sec_migration_typology",
        "title": "1. Phân loại di cư và Khung pháp lý",
        "selector": "#sec-migration-typology",
        "en": "Section 1 categorizes migration along three axes: internal versus international crossing sovereign borders, voluntary chosen for prosperity versus forced fleeing conflict, and permanent settlement versus temporary seasonal guest work.",
        "vi": "Mục một phân loại di cư theo ba tiêu chí: di cư nội địa so với quốc tế vượt qua biên giới chủ quyền, di cư tự nguyện vì mưu cầu kinh tế so với di cư cưỡng bức để trốn chạy hiểm nguy, và định cư vĩnh viễn so với làm việc thời vụ ngắn hạn."
    },
    {
        "id": "legal_distinctions",
        "title": "Phân biệt Người di cư, Người tị nạn và IDP",
        "selector": "#card-legal-distinctions",
        "en": "International law draws strict distinctions: Economic Migrants move voluntarily seeking prosperity and retain national protection; Refugees are forced outside their home country due to well-founded fear of persecution and are protected by the 1951 Refugee Convention against non-refoulement; while Internally Displaced Persons are displaced within their own borders without formal international legal status.",
        "vi": "Luật pháp quốc tế phân định rạch ròi: Người di cư kinh tế chủ động di chuyển để tìm kiếm cơ hội và vẫn được nhà nước của họ bảo hộ; Người tị nạn bị cưỡng bức rời khỏi quê hương do lo sợ bị đàn áp và được Công ước Geneva năm 1951 bảo vệ với nguyên tắc không cưỡng ép hồi hương; còn Người mất nhà cửa nội địa IDP phải sơ tán ngay bên trong biên giới nước mình mà không có quy chế bảo vệ quốc tế tương đương."
    },
    {
        "id": "sec_push_pull",
        "title": "2. Mô hình Đẩy - Kéo và Trở ngại can thiệp",
        "selector": "#sec-push-pull",
        "en": "Section 2 examines Everett Lee's Push-Pull Model. Push factors operate at the origin forcing people away, such as drought, unemployment, and persecution. Pull factors operate at destinations attracting migrants, including high wages, political freedom, and healthcare. Intervening obstacles are physical, financial, or political barriers like militarized border walls, desert crossings, and visa quotas.",
        "vi": "Mục hai tìm hiểu Mô hình Đẩy - Kéo của Everett Lee. Lực đẩy xuất phát từ nơi đi buộc con người phải rời bỏ, như hạn hán, thất nghiệp và xung đột. Lực kéo xuất phát từ nơi đến thu hút người di cư, bao gồm mức lương cao, tự do chính trị và y tế hiện đại. Trở ngại can thiệp là các rào cản địa lý, tài chính hoặc luật pháp như hàng rào biên giới kiên cố, sa mạc khắc nghiệt và hạn ngạch thị thực."
    },
    {
        "id": "push_pull_factors",
        "title": "Chi tiết các lực Đẩy và lực Kéo",
        "selector": "#card-push-pull-factors",
        "en": "Economic push-pull disparities often exceed five to one in wages, while social networks and historical diaspora chains generate self-reinforcing migration momentum.",
        "vi": "Sự chênh lệch về tiền lương giữa hai đầu di cư thường vượt quá tỉ lệ năm trên một, trong khi mạng lưới cộng đồng kiều bào đồng hương tạo ra quán tính di cư tự củng cố mạnh mẽ."
    },
    {
        "id": "sec_bilateral_impacts",
        "title": "3. Tác động hai chiều: Nước xuất cư vs Nước nhập cư",
        "selector": "#sec-bilateral-impacts",
        "en": "Section 3 evaluates bilateral trade-offs across four domains: economic, social, political, and environmental. Source countries benefit from massive financial remittances but suffer brain drain and an aging population. Destination countries gain vital labor to sustain pensions and fill shortages, but face pressure on housing, schools, and cultural friction.",
        "vi": "Mục ba đánh giá tác động hai chiều trên bốn phương diện: kinh tế, xã hội, chính trị và môi trường. Quốc gia xuất cư hưởng lợi từ nguồn kiều hối khổng lồ nhưng chịu tổn thất do chảy máu chất xám và già hóa dân số. Quốc gia nhập cư có thêm nguồn lao động dồi dào để bù đắp thâm hụt lương hưu, nhưng chịu áp lực lớn về nhà ở, trường học và bất đồng văn hóa."
    },
    {
        "id": "sec_mexico_usa",
        "title": "4. Nghiên cứu tình huống: Hành lang Mexico - Hoa Kỳ",
        "selector": "#sec-mexico-usa",
        "en": "Section 4 analyzes the world's largest bilateral migration corridor. Over 11.5 million Mexican-born individuals reside in the United States, initiated historically by the wartime Bracero Program.",
        "vi": "Mục bốn phân tích hành lang di cư song phương lớn nhất thế giới. Hơn mười một phẩy năm triệu người gốc Mexico đang cư trú tại Hoa Kỳ, bắt nguồn lịch sử từ Chương trình Bracero thời Thế chiến thứ hai."
    },
    {
        "id": "mexico_usa_details",
        "title": "Chi tiết kinh tế và kiều hối hành lang Mexico - Mỹ",
        "selector": "#card-mexico-usa-details",
        "en": "Mexican workers supply essential labor to US agriculture, construction, and hospitality while replenishing the payroll tax base. In return, remittances to Mexico exceed sixty billion dollars annually, surpassing foreign direct investment. However, strict border militarization has increased smuggling costs and trapped workers permanently inside the US.",
        "vi": "Lao động Mexico cung cấp nhân lực thiết yếu cho nông nghiệp, xây dựng và dịch vụ của Mỹ, đồng thời đóng góp lớn vào quỹ an sinh xã hội. Ngược lại, kiều hối gửi về Mexico vượt sáu mươi tỷ đô la mỗi năm, cao hơn cả đầu tư trực tiếp nước ngoài. Tuy nhiên, việc tăng cường quân sự hóa biên giới đã đẩy chi phí buôn người lên cao và khiến người di cư chuyển sang ở lại vĩnh viễn thay vì về thăm quê."
    },
    {
        "id": "sec_syria_crisis",
        "title": "5. Nghiên cứu tình huống Di cư cưỡng bức: Khủng hoảng tị nạn Syria",
        "selector": "#sec-syria-crisis",
        "en": "Section 5 examines the 2011 Syrian civil war, which forcibly displaced over thirteen million people. Turkey absorbed 3.7 million refugees, and in Lebanon refugees reached one in four of the population, triggering massive economic strain. In Europe, Germany's 2015 open door policy integrated one million asylum seekers, while the EU-Turkey deal erected externalized border checks.",
        "vi": "Mục năm khảo sát cuộc nội chiến Syria năm 2011, khiến hơn mười ba triệu người phải di dời cưỡng bức. Thổ Nhĩ Kỳ tiếp nhận ba phẩy bảy triệu người tị nạn, và tại Liban người tị nạn chiếm tới một phần tư dân số, gây tê liệt hạ tầng. Tại châu Âu, chính sách mở cửa của Đức năm 2015 đã tiếp nhận một triệu người, trong khi thỏa ước giữa EU và Thổ Nhĩ Kỳ siết chặt kiểm soát biên giới trên biển."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược làm bài thi IGCSE về Di cư",
        "selector": "#card-exam-strategy",
        "en": "To maximize examination marks: explicitly classify migration as voluntary or forced; structure bilateral impact essays into balanced origin and destination pros and cons; and name specific intervening obstacles alongside quantified case evidence.",
        "vi": "Để đạt điểm tối đa trong bài thi: các em hãy phân loại rõ di cư là tự nguyện hay cưỡng bức; trình bày cân đối các tác động tích cực và tiêu cực cho cả nước đi và nước đến; đồng thời nêu rõ các trở ngại can thiệp cụ thể kèm theo số liệu thực tế."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_migration_typology": {"start": 1, "end": 2},
    "sec_push_pull": {"start": 3, "end": 4},
    "sec_bilateral_impacts": {"start": 5, "end": 5},
    "sec_mexico_usa": {"start": 6, "end": 7},
    "sec_syria_crisis": {"start": 8, "end": 9}
}

def transform_html(raw_html):
    html = raw_html

    # Intro banner
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 60%, #7c3aed 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(109, 40, 217, 0.25);">',
        '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #4c1d95 0%, #6d28d9 60%, #7c3aed 100%); color:#ffffff; padding:32px 28px; border-radius:16px; margin-bottom:32px; box-shadow:0 10px 25px -5px rgba(109, 40, 217, 0.25); cursor:pointer;">'
    )

    # Section 1 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    1. Typology of Migration & Legal Classifications\n  </h2>',
        '<h2 id="sec-migration-typology" class="lecture-interactive-card" data-lecture-section="sec_migration_typology" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    1. Typology of Migration & Legal Classifications\n  </h2>'
    )

    # Legal distinctions table
    html = html.replace(
        '<div style="overflow-x:auto; margin:18px 0;">\n    <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border-radius:8px; overflow:hidden; border:1px solid #e2e8f0;">',
        '<div id="card-legal-distinctions" class="lecture-interactive-card" data-lecture-section="legal_distinctions" style="overflow-x:auto; margin:18px 0; cursor:pointer;">\n    <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border-radius:8px; overflow:hidden; border:1px solid #e2e8f0;">'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    2. The Push-Pull Model & Intervening Obstacles\n  </h2>',
        '<h2 id="sec-push-pull" class="lecture-interactive-card" data-lecture-section="sec_push_pull" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    2. The Push-Pull Model & Intervening Obstacles\n  </h2>'
    )

    # Push-pull factors grid
    html = html.replace(
        '<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:18px; margin:20px 0;">\n    <div style="background:#fef2f2; border-left:4px solid #ef4444;',
        '<div id="card-push-pull-factors" class="lecture-interactive-card" data-lecture-section="push_pull_factors" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:18px; margin:20px 0; cursor:pointer;">\n    <div style="background:#fef2f2; border-left:4px solid #ef4444;'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    3. Bilateral Impacts: Source Country vs. Destination Country\n  </h2>',
        '<h2 id="sec-bilateral-impacts" class="lecture-interactive-card" data-lecture-section="sec_bilateral_impacts" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    3. Bilateral Impacts: Source Country vs. Destination Country\n  </h2>'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    4. Bilateral Case Study: Mexico to the United States Migration Corridor\n  </h2>',
        '<h2 id="sec-mexico-usa" class="lecture-interactive-card" data-lecture-section="sec_mexico_usa" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    4. Bilateral Case Study: Mexico to the United States Migration Corridor\n  </h2>'
    )

    # Mexico-US details card
    html = html.replace(
        '<div style="background:#fdf4ff; border-left:4px solid #a855f7; padding:18px; border-radius:8px; margin:20px 0;">\n    <div style="font-weight:700; color:#581c87; font-size:16px; margin-bottom:8px;">In-Depth Dynamics of the Mexico–US Corridor:</div>',
        '<div id="card-mexico-usa-details" class="lecture-interactive-card" data-lecture-section="mexico_usa_details" style="background:#fdf4ff; border-left:4px solid #a855f7; padding:18px; border-radius:8px; margin:20px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#581c87; font-size:16px; margin-bottom:8px;">In-Depth Dynamics of the Mexico–US Corridor:</div>'
    )

    # Section 5 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    5. Forced Migration Case Study: The Syrian Refugee Crisis & Management Frameworks\n  </h2>',
        '<h2 id="sec-syria-crisis" class="lecture-interactive-card" data-lecture-section="sec_syria_crisis" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    5. Forced Migration Case Study: The Syrian Refugee Crisis & Management Frameworks\n  </h2>'
    )

    # Exam strategy card
    html = html.replace(
        '<div style="background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%); border:1px solid #c4b5fd; border-left:6px solid #7c3aed; border-radius:10px; padding:20px; margin:32px 0;">',
        '<div id="card-exam-strategy" class="lecture-interactive-card" data-lecture-section="exam_strategy" style="background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%); border:1px solid #c4b5fd; border-left:6px solid #7c3aed; border-radius:10px; padding:20px; margin:32px 0; cursor:pointer;">'
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
