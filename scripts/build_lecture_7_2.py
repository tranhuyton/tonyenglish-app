import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "7_2"
LECTURE_ID = "30bae547-a9b0-4c09-8850-ce22b96cfea2"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "7.2 The Opportunities and Challenges of Urbanisation"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 7.2: Cơ hội và Thách thức của Đô thị hóa",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 7.2: The Opportunities and Challenges of Urbanisation. In this lecture, we explore the dual nature of rapid city growth: examining economic agglomeration and service accessibility, contrasting classic land use models, investigating rural-urban fringe conflicts, and analyzing the extreme socio-economic divide of squatter settlements through Rio de Janeiro's Favela-Bairro upgrade program.",
        "vi": "Chào mừng các em đến với bài bảy chấm hai: Cơ hội và Thách thức của Đô thị hóa. Trong bài học này, chúng ta sẽ khám phá tính chất hai mặt của sự phát triển đô thị nhanh chóng: khảo sát hiệu ứng tích tụ kinh tế và tiếp cận dịch vụ, đối chiếu các mô hình sử dụng đất kinh điển, tìm hiểu xung đột lợi ích ở vùng ven đô thị, và phân tích sự phân hóa kinh tế xã hội gay gắt của các khu nhà ổ chuột thông qua dự án nâng cấp Favela-Bairro tại Rio de Janeiro."
    },
    {
        "id": "sec_opportunities",
        "title": "1. Cơ hội kinh tế và xã hội của đô thị hóa",
        "selector": "#sec-opportunities",
        "en": "Section 1 examines why cities function as engines of human progress. Urban agglomeration concentrates capital, talent, and infrastructure, sparking positive cumulative causation and multiplier effects that raise living standards.",
        "vi": "Mục một phân tích lý do tại sao các thành phố đóng vai trò là đầu tàu phát triển của nhân loại. Sự tích tụ đô thị tập trung vốn, nhân tài và cơ sở hạ tầng, kích hoạt hiệu ứng nhân tử và chuỗi tăng trưởng tích lũy giúp nâng cao chất lượng sống."
    },
    {
        "id": "economic_drivers",
        "title": "Động lực kinh tế và Hiệu ứng nhân tử",
        "selector": "#card-economic-drivers",
        "en": "Cities attract foreign direct investment and foster innovation through dense business clustering, offering formal employment with higher median wages, diverse career pathways, and substantial local tax revenues.",
        "vi": "Đô thị thu hút vốn đầu tư trực tiếp nước ngoài và thúc đẩy đổi mới sáng tạo nhờ cụm doanh nghiệp tập trung, mang lại cơ hội việc làm chính thức với thu nhập cao hơn, lộ trình nghề nghiệp đa dạng và nguồn thu ngân sách dồi dào."
    },
    {
        "id": "social_benefits",
        "title": "Lợi ích xã hội và Chất lượng cuộc sống",
        "selector": "#card-social-benefits",
        "en": "Urban residents enjoy superior access to specialized healthcare, tertiary education, piped water, reliable electricity networks, and rich cultural amenities rarely available in peripheral rural areas.",
        "vi": "Cư dân đô thị được tiếp cận vượt trội với dịch vụ y tế chuyên sâu, giáo dục đại học, mạng lưới nước máy và điện lưới ổn định, cùng các tiện ích văn hóa phong phú vốn rất hiếm thấy ở các vùng nông thôn xa xôi."
    },
    {
        "id": "sec_hic_challenges",
        "title": "2. Thách thức ở các nước phát triển HIC: Mô hình đất đai, Vết loang và Sang trọng hóa",
        "selector": "#sec-hic-challenges",
        "en": "Section 2 examines spatial challenges in high-income cities: suburban sprawl gobbling countryside, urban decay in the inner city, and the social controversies of gentrification.",
        "vi": "Mục hai khảo sát các thách thức không gian tại các thành phố phát triển: vết loang đô thị xâm lấn nông thôn, suy thoái lõi nội đô cũ, và những tranh cãi xã hội xoay quanh hiện tượng sang trọng hóa đô thị."
    },
    {
        "id": "land_use_models",
        "title": "Bảng so sánh ba mô hình sử dụng đất đô thị",
        "selector": "#card-land-use-models",
        "en": "This matrix compares the three foundational urban land-use models: Burgess's Concentric Zone Model driven by bid-rent distance decay, Hoyt's Sector Model shaped by transport arteries, and Harris and Ullman's Multiple Nuclei Model reflecting decentralized suburban clusters.",
        "vi": "Bảng này đối chiếu ba mô hình sử dụng đất đô thị kinh điển: Mô hình các vòng tròn đồng tâm của Burgess dựa trên cự ly đến trung tâm, Mô hình hình quạt của Hoyt định hình theo các trục giao thông, và Mô hình đa nhân của Harris và Ullman phản ánh sự phân tán của các cụm đô thị vệ tinh."
    },
    {
        "id": "rural_urban_fringe",
        "title": "Vùng ven đô thị và Xung đột lợi ích",
        "selector": "#sec-rural-urban-fringe",
        "en": "The rural-urban fringe is a zone of intense competition between agricultural conservation, retail parks, science campuses, and new housing estates seeking cheap land and motorway links.",
        "vi": "Vùng ven đô thị là khu vực cạnh tranh gay gắt giữa bảo tồn đất nông nghiệp, xây dựng trung tâm mua sắm, khu công nghệ cao và các khu đô thị mới nhằm tận dụng quỹ đất giá rẻ và kết nối cao tốc."
    },
    {
        "id": "gentrification",
        "title": "Hiện tượng Sang trọng hóa và Phân tầng xã hội",
        "selector": "#sec-gentrification",
        "en": "Gentrification revitalizes derelict inner-city architecture and attracts affluent professionals, but simultaneously drives up property rents, displacing long-standing low-income communities as seen in Cape Town.",
        "vi": "Sang trọng hóa giúp cải tạo các khu nhà cũ nát ở nội đô và thu hút giới tri thức thượng lưu, nhưng đồng thời đẩy giá thuê nhà lên cao, làm bật bãi các cộng đồng người nghèo cư trú lâu đời như bài học tại Cape Town."
    },
    {
        "id": "sec_lic_challenges",
        "title": "3. Thách thức ở các nước đang phát triển: Khu ổ chuột và Favela",
        "selector": "#sec-lic-challenges",
        "en": "Section 3 addresses the severe urban crisis in developing nations, where rapid rural exodus overwhelms planning infrastructure, spawning massive spontaneous squatter settlements.",
        "vi": "Mục ba đề cập đến cuộc khủng hoảng đô thị nghiêm trọng tại các quốc gia đang phát triển, nơi dòng người di cư ồ ạt từ nông thôn làm tê liệt năng lực quy hoạch, hình thành nên các khu định cư tự phát và ổ chuột khổng lồ."
    },
    {
        "id": "inequality_lorenz",
        "title": "Bất bình đẳng thu nhập và Đường cong Lorenz tại Rio",
        "selector": "#card-inequality-lorenz",
        "en": "Figure 7.7 displays Rio de Janeiro's extreme Lorenz curve: the top 10 percent command over half of total city wealth, while the bottom 40 percent share less than 10 percent, creating severe spatial segregation.",
        "vi": "Hình bảy chấm bảy minh họa đường cong Lorenz về sự bất bình đẳng cùng cực ở Rio de Janeiro: mười phần trăm người giàu nhất nắm giữ hơn một nửa tổng tài sản thành phố, trong khi bốn mươi phần trăm dân số nghèo nhất chỉ sở hữu dưới mười phần trăm, tạo nên sự phân tầng không gian gay gắt."
    },
    {
        "id": "sec_squatter_management",
        "title": "4. Quản lý khu ổ chuột: Dự án nâng cấp Favela-Bairro",
        "selector": "#sec-squatter-management",
        "en": "Section 4 highlights progressive urban policy: moving away from violent bulldozing towards site-and-service infrastructure upgrades and community integration.",
        "vi": "Mục bốn nêu bật bước chuyển trong chính sách đô thị tiến bộ: từ bỏ việc cưỡng chế giải tỏa bằng máy ủi để chuyển sang nâng cấp hạ tầng tại chỗ và hòa nhập cộng đồng."
    },
    {
        "id": "favela_bairro_svg",
        "title": "Sơ đồ cắt ngang: Hiểm họa ổ chuột và Dự án Favela-Bairro",
        "selector": "#card-favela-bairro-svg",
        "en": "This cutaway diagram highlights how the Favela-Bairro scheme transformed fragile hillside slums through reinforced retaining walls, paved drainage channels, legal electricity grids, and aerial cable car transit.",
        "vi": "Sơ đồ cắt ngang này minh họa cách dự án Favela-Bairro chuyển hóa các khu sườn dốc hiểm trở thông qua kè bê tông chống sạt lở, cống thoát nước kiên cố, điện lưới hợp pháp và hệ thống cáp treo trên không."
    },
    {
        "id": "favela_bairro_details",
        "title": "Chi tiết dự án nâng cấp Favela-Bairro tại Rio de Janeiro",
        "selector": "#card-favela-bairro-details",
        "en": "With 300 million dollars in investment, the Favela-Bairro project upgraded over 140 favelas, cutting waterborne illnesses by 60 percent, integrating informal residents into municipal tax rolls, and providing vital job training centers.",
        "vi": "Với số vốn đầu tư ba trăm triệu đô la, dự án Favela-Bairro đã nâng cấp hơn một trăm bốn mươi khu ổ chuột, giảm sáu mươi phần trăm các bệnh truyền nhiễm qua nước, đưa người dân vào hệ thống quản lý chính thức và mở các trung tâm đào tạo nghề thiết thực."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược thi cử Cambridge IGCSE: Chủ đề 7.2",
        "selector": "#card-exam-strategy",
        "en": "In exam questions on squatter settlements, always provide balanced arguments: evaluate both structural achievements like landslide prevention alongside ongoing hurdles such as municipal maintenance funding and drug cartel violence.",
        "vi": "Khi làm các bài thi về khu ổ chuột, các em luôn cần lập luận hai mặt cân bằng: đánh giá cả thành quả kiến tạo hạ tầng như chống sạt lở đất đi kèm với những thách thức còn tồn tại như kinh phí bảo trì của chính quyền và vấn nạn tội phạm ma túy."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_opportunities", "title": "1. Cơ hội kinh tế & xã hội", "startSegmentId": "sec_opportunities"},
    {"id": "sec_hic_challenges", "title": "2. Thách thức ở HIC & Mô hình đất đai", "startSegmentId": "sec_hic_challenges"},
    {"id": "sec_lic_challenges", "title": "3. Thách thức ở LIC & Khu ổ chuột", "startSegmentId": "sec_lic_challenges"},
    {"id": "sec_squatter_management", "title": "4. Quản lý ổ chuột & Favela-Bairro", "startSegmentId": "sec_squatter_management"},
    {"id": "card_exam_strategy", "title": "Chiến lược làm bài thi", "startSegmentId": "exam_strategy"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    1. Economic & Social Opportunities of Urbanisation\n  </h2>',
        '<h2 id="sec-opportunities" class="lecture-interactive-card" data-lecture-section="sec_opportunities" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    1. Economic & Social Opportunities of Urbanisation\n  </h2>'
    )

    # Economic Drivers card
    html = html.replace(
        '<div style="background:#f0fdfa; border-left:4px solid #0d9488; padding:18px; border-radius:8px; margin:18px 0;">\n    <div style="font-weight:700; color:#0f766e; font-size:16px; margin-bottom:8px;">Economic Drivers & Multiplier Effect:</div>',
        '<div id="card-economic-drivers" class="lecture-interactive-card" data-lecture-section="economic_drivers" style="background:#f0fdfa; border-left:4px solid #0d9488; padding:18px; border-radius:8px; margin:18px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#0f766e; font-size:16px; margin-bottom:8px;">Economic Drivers & Multiplier Effect:</div>'
    )

    # Social Benefits card
    html = html.replace(
        '<div style="background:#eff6ff; border-left:4px solid #3b82f6; padding:18px; border-radius:8px; margin:18px 0;">\n    <div style="font-weight:700; color:#1d4ed8; font-size:16px; margin-bottom:8px;">Social & Quality of Life Benefits:</div>',
        '<div id="card-social-benefits" class="lecture-interactive-card" data-lecture-section="social_benefits" style="background:#eff6ff; border-left:4px solid #3b82f6; padding:18px; border-radius:8px; margin:18px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#1d4ed8; font-size:16px; margin-bottom:8px;">Social & Quality of Life Benefits:</div>'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    2. Challenges in HICs: Urban Land Use Models, Sprawl & Gentrification\n  </h2>',
        '<h2 id="sec-hic-challenges" class="lecture-interactive-card" data-lecture-section="sec_hic_challenges" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    2. Challenges in HICs: Urban Land Use Models, Sprawl & Gentrification\n  </h2>'
    )

    # Land use models table card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#0d9488; border-radius:50%;"></span>\n    Urban Land Use Models Comparison: Burgess vs. Hoyt vs. Harris-Ullman',
        '<div id="card-land-use-models" class="lecture-interactive-card" data-lecture-section="land_use_models" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#0d9488; border-radius:50%;"></span>\n    Urban Land Use Models Comparison: Burgess vs. Hoyt vs. Harris-Ullman'
    )

    # Rural-Urban Fringe heading
    html = html.replace(
        '<h3 style="color:#0f766e; font-size:18px; margin-top:24px; margin-bottom:12px;">The Rural-Urban Fringe & Conflict of Interests</h3>',
        '<h3 id="sec-rural-urban-fringe" class="lecture-interactive-card" data-lecture-section="rural_urban_fringe" style="color:#0f766e; font-size:18px; margin-top:24px; margin-bottom:12px; cursor:pointer;">The Rural-Urban Fringe & Conflict of Interests</h3>'
    )

    # Gentrification heading
    html = html.replace(
        '<h3 style="color:#0f766e; font-size:18px; margin-top:24px; margin-bottom:12px;">Gentrification vs. Social Segregation: Case Study Cape Town</h3>',
        '<h3 id="sec-gentrification" class="lecture-interactive-card" data-lecture-section="gentrification" style="color:#0f766e; font-size:18px; margin-top:24px; margin-bottom:12px; cursor:pointer;">Gentrification vs. Social Segregation: Case Study Cape Town</h3>'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    3. Challenges in LICs & NEEs: Squatter Settlements & Favelas\n  </h2>',
        '<h2 id="sec-lic-challenges" class="lecture-interactive-card" data-lecture-section="sec_lic_challenges" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    3. Challenges in LICs & NEEs: Squatter Settlements & Favelas\n  </h2>'
    )

    # Inequality Lorenz card
    html = html.replace(
        '<div style="margin:24px 0; text-align:center;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t7_fig_7_7.png?v=3"',
        '<div id="card-inequality-lorenz" class="lecture-interactive-card" data-lecture-section="inequality_lorenz" style="margin:24px 0; text-align:center; cursor:pointer;">\n    <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/t7_fig_7_7.png?v=3"'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    4. Managing Squatter Settlements: The Favela-Bairro Upgrade Scheme\n  </h2>',
        '<h2 id="sec-squatter-management" class="lecture-interactive-card" data-lecture-section="sec_squatter_management" style="color:#0f766e; border-bottom:2px solid #ccfbf1; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    4. Managing Squatter Settlements: The Favela-Bairro Upgrade Scheme\n  </h2>'
    )

    # Favela-Bairro SVG card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#dc2626; border-radius:50%;"></span>\n    Comparative Cutaway: Squatter Settlement Hazards vs. The Favela-Bairro Upgrade Scheme',
        '<div id="card-favela-bairro-svg" class="lecture-interactive-card" data-lecture-section="favela_bairro_svg" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#0f766e; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#dc2626; border-radius:50%;"></span>\n    Comparative Cutaway: Squatter Settlement Hazards vs. The Favela-Bairro Upgrade Scheme'
    )

    # Favela-Bairro details card
    html = html.replace(
        '<div style="background:#fdf4ff; border-left:4px solid #a855f7; padding:18px; border-radius:8px; margin:20px 0;">\n    <div style="font-weight:700; color:#581c87; font-size:16px; margin-bottom:8px;">Core Components of the $300 Million Favela-Bairro Program:</div>',
        '<div id="card-favela-bairro-details" class="lecture-interactive-card" data-lecture-section="favela_bairro_details" style="background:#fdf4ff; border-left:4px solid #a855f7; padding:18px; border-radius:8px; margin:20px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#581c87; font-size:16px; margin-bottom:8px;">Core Components of the $300 Million Favela-Bairro Program:</div>'
    )

    # Exam Strategy card
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
