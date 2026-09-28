import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "6_1"
LECTURE_ID = "c6fccfc5-088b-4145-9a23-9cbb2df1cce9"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "6.1 Populations Grow and Decline"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 6.1: Sự tăng trưởng và suy giảm dân số",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 6.1: Populations Grow and Decline. In this lecture, we examine the fundamental mechanisms of human demography: key population indicators, the exponential acceleration of global population milestones, factors governing birth and death rates, the five stages of the Demographic Transition Model, and governmental population policies.",
        "vi": "Chào mừng các em đến với bài sáu chấm một: Sự tăng trưởng và suy giảm dân số. Trong bài giảng này, chúng ta sẽ tìm hiểu các cơ chế nền tảng của nhân khẩu học: các chỉ số dân số cốt lõi, cột mốc tăng trưởng dân số toàn cầu, các yếu tố quyết định tỉ suất sinh và tử, năm giai đoạn của mô hình chuyển tiếp dân số, và các chính sách can thiệp dân số của chính phủ."
    },
    {
        "id": "sec_demographic_concepts",
        "title": "1. Các khái niệm nhân khẩu học cốt lõi",
        "selector": "#sec-demographic-concepts",
        "en": "Section 1 establishes core demographic definitions. The Crude Birth Rate and Crude Death Rate measure annual live births and deaths per one thousand individuals. The Rate of Natural Increase is calculated as the birth rate minus the death rate divided by ten. Other vital metrics include Total Fertility Rate, Replacement Level Fertility at approximately 2.1 children per woman, Infant Mortality Rate, and Life Expectancy.",
        "vi": "Mục một thiết lập các định nghĩa nhân khẩu học cốt lõi. Tỉ suất sinh thô và tỉ suất tử thô đo lường số trẻ sinh sống và số ca tử vong trên một nghìn dân mỗi năm. Tỉ suất gia tăng dân số tự nhiên được tính bằng tỉ suất sinh trừ tỉ suất tử chia cho mười. Các chỉ số quan trọng khác gồm tổng tỉ suất sinh, mức sinh thay thế chuẩn là hai phẩy một con trên một phụ nữ, tỉ suất tử vong ở trẻ sơ sinh và tuổi thọ trung bình."
    },
    {
        "id": "balancing_equation",
        "title": "Phương trình cân bằng dân số",
        "selector": "#card-balancing-equation",
        "en": "The Demographic Balancing Equation states that total population change equals natural change plus net migration. That is, ending population equals starting population plus births minus deaths, plus immigrants minus emigrants.",
        "vi": "Phương trình cân bằng dân số khẳng định: sự thay đổi tổng dân số bằng biến động tự nhiên cộng biến động cơ học. Tức là, dân số cuối kỳ bằng dân số đầu kỳ cộng số sinh trừ số tử, cộng số người nhập cư trừ số người xuất cư."
    },
    {
        "id": "sec_milestones",
        "title": "2. Các mốc tăng trưởng dân số toàn cầu",
        "selector": "#sec-milestones",
        "en": "Section 2 investigates historical population growth. For most of human history, global population remained small. Following the Industrial Revolution, global population expanded exponentially: reaching one billion in 1804, two billion in 1927, and crossing eight billion in 2022. While adding each billion once accelerated down to just eleven years, growth velocity is now gradually decelerating.",
        "vi": "Mục hai khảo sát lịch sử tăng trưởng dân số. Suốt phần lớn lịch sử loài người, quy mô dân số duy trì ở mức nhỏ. Sau Cách mạng Công nghiệp, dân số bùng nổ theo cấp số nhân: đạt một tỷ người năm 1804, hai tỷ năm 1927 và vượt tám tỷ vào năm 2022. Dù thời gian tăng thêm một tỷ người từng rút ngắn chỉ còn mười một năm, hiện nay tốc độ tăng trưởng đang chậm dần lại."
    },
    {
        "id": "milestones_table",
        "title": "Bảng phân tích các mốc một tỷ dân",
        "selector": "#card-milestones-table",
        "en": "This table reveals how industrialization, public sanitation, antibiotics, and the Green Revolution drastically compressed the time required to add one billion people from millennia down to just over a decade.",
        "vi": "Bảng số liệu này minh chứng quá trình công nghiệp hóa, vệ sinh môi trường, kháng sinh và Cách mạng Xanh đã rút ngắn thời gian tăng thêm một tỷ dân từ hàng nghìn năm xuống chỉ còn hơn một thập kỷ."
    },
    {
        "id": "sec_birth_death_factors",
        "title": "3. Các yếu tố quyết định tỉ suất sinh và tử",
        "selector": "#sec-birth-death-factors",
        "en": "Section 3 analyzes the drivers of demographic variation. Fertility and mortality are governed by social traditions, economic structures, healthcare availability, and female education.",
        "vi": "Mục ba phân tích các động lực thúc đẩy sự biến động nhân khẩu. Tỉ suất sinh và tỉ suất tử phụ thuộc chặt chẽ vào truyền thống xã hội, cơ cấu kinh tế, điều kiện chăm sóc y tế và trình độ học vấn của phụ nữ."
    },
    {
        "id": "fertility_factors",
        "title": "Các yếu tố chi phối mức sinh",
        "selector": "#card-fertility-factors",
        "en": "Birth rates vary across four dimensions: social traditions like marriage age, economic factors such as whether children are economic assets on farms or financial liabilities in cities, female empowerment through secondary schooling, and infant mortality where high child loss induces an insurance birth strategy.",
        "vi": "Mức sinh chịu ảnh hưởng bởi bốn nhóm yếu tố: tập quán xã hội như độ tuổi kết hôn, yếu tố kinh tế xem con cái là lực lượng lao động nông nghiệp hay gánh nặng chi phí tại đô thị, giáo dục phụ nữ giúp nâng cao quyền tự quyết, và tỉ lệ tử vong trẻ em cao thúc đẩy tâm lý sinh nhiều con để bù đắp rủi ro."
    },
    {
        "id": "mortality_transition",
        "title": "Chuyển tiếp dịch tễ học và tỉ suất tử",
        "selector": "#card-mortality-transition",
        "en": "The Epidemiological Transition explains falling mortality in three historic phases: pestilence and famine dominated by infectious disease, receding pandemics through clean water and antibiotics, and modern degenerative diseases like cardiovascular illnesses and cancer in aging populations.",
        "vi": "Quá trình chuyển tiếp dịch tễ học giải thích sự sụt giảm tỉ suất tử qua ba giai đoạn: thời kỳ dịch bệnh và nạn đói do bệnh truyền nhiễm, thời kỳ thoái lui dịch bệnh nhờ nước sạch và thuốc kháng sinh, và thời kỳ bệnh thoái hóa mạn tính như tim mạch và ung thư ở xã hội già hóa."
    },
    {
        "id": "sec_dtm",
        "title": "4. Mô hình chuyển tiếp dân số (DTM)",
        "selector": "#sec-dtm",
        "en": "Section 4 introduces the Demographic Transition Model. Originally formulated by Warren Thompson, the DTM tracks how birth rates, death rates, and total population evolve across five developmental stages.",
        "vi": "Mục bốn giới thiệu Mô hình chuyển tiếp dân số DTM. Được xây dựng bởi nhà nhân khẩu học Warren Thompson, mô hình DTM theo dõi sự thay đổi của tỉ suất sinh, tỉ suất tử và tổng dân số qua năm giai đoạn phát triển kinh tế."
    },
    {
        "id": "dtm_stages",
        "title": "Chi tiết năm giai đoạn của mô hình DTM",
        "selector": "#card-dtm-stages",
        "en": "Stage 1 High Stationary features high birth and death rates. Stage 2 Early Expanding brings plunging death rates while births remain high, triggering a population explosion. Stage 3 Late Expanding sees falling birth rates due to urbanization and female careers. Stage 4 Low Stationary reaches equilibrium with low births and deaths. Stage 5 Natural Decrease occurs when birth rates fall below death rates, shrinking the population.",
        "vi": "Giai đoạn một duy trì sinh và tử đều cao. Giai đoạn hai chứng kiến tỉ suất tử giảm mạnh trong khi tỉ suất sinh vẫn cao, gây ra bùng nổ dân số. Giai đoạn ba ghi nhận tỉ suất sinh giảm nhanh do đô thị hóa và giáo dục phụ nữ. Giai đoạn bốn đạt trạng thái ổn định với mức sinh và tử đều thấp. Giai đoạn năm suy giảm tự nhiên khi tỉ suất sinh rơi xuống thấp hơn tỉ suất tử, khiến quy mô dân số thu hẹp."
    },
    {
        "id": "dtm_evaluation",
        "title": "Đánh giá ưu điểm và hạn chế của mô hình DTM",
        "selector": "#card-dtm-evaluation",
        "en": "While the DTM serves as a universal benchmark and illustrates the demographic time-lag, it has notable limitations: its Eurocentric assumption that all nations industrialize identically, its omission of international migration, and its inability to foresee epidemics like HIV and COVID-19 or authoritarian mandates like China's One-Child Policy.",
        "vi": "Dù mô hình DTM là công cụ đối chiếu chuẩn mực và giải thích rõ độ trễ nhân khẩu học, mô hình này vẫn có những hạn chế lớn: mang tính vị châu Âu khi giả định mọi nước đều công nghiệp hóa giống nhau, bỏ qua tác động của di cư quốc tế, và không dự đoán được các đại dịch bất ngờ hay sự can thiệp cưỡng chế như chính sách một con của Trung Quốc."
    },
    {
        "id": "sec_population_policies",
        "title": "5. Chính sách dân số: Giảm sinh và Khuyến sinh",
        "selector": "#sec-population-policies",
        "en": "Section 5 explores state demographic interventions. Governments adopt anti-natalist policies to curb unsustainable expansion, or pro-natalist policies to prevent demographic aging and economic contraction.",
        "vi": "Mục năm khảo sát các chính sách can thiệp dân số của nhà nước. Chính phủ ban hành chính sách giảm sinh nhằm ngăn chặn áp lực bùng nổ quá mức, hoặc chính sách khuyến sinh nhằm khắc phục tình trạng già hóa và suy giảm lực lượng lao động."
    },
    {
        "id": "policy_china_antinatalist",
        "title": "Chính sách một con của Trung Quốc",
        "selector": "#card-policy-china",
        "en": "China's One-Child Policy from 1979 to 2015 utilized strict financial penalties and quotas, averting an estimated 400 million births. However, it generated severe unintended consequences: an acute gender imbalance with millions of surplus men, the four-two-one dependency burden, and an accelerating workforce contraction.",
        "vi": "Chính sách Một Con của Trung Quốc từ năm 1979 đến 2015 sử dụng các chế tài tài chính và giám sát nghiêm ngặt, ngăn chặn khoảng bốn trăm triệu ca sinh. Tuy nhiên, chính sách này để lại nhiều hệ lụy nặng nề: mất cân bằng giới tính trầm trọng với hàng chục triệu nam giới dư thừa, gánh nặng chăm sóc theo mô hình bốn hai một, và lực lượng lao động suy giảm nhanh chóng."
    },
    {
        "id": "policy_france_pronatalist",
        "title": "Chính sách khuyến sinh tại Pháp và Singapore",
        "selector": "#card-policy-france",
        "en": "France's Code de la Famille combats aging through generous child allowances, subsidized state creches, paid parental leave, and tax reductions. By supporting working mothers, France maintains one of the highest fertility rates in Europe, showing family-work balance outperforms pure cash incentives.",
        "vi": "Bộ luật Gia đình của Pháp chống già hóa dân số thông qua trợ cấp nuôi con lũy tiến, hệ thống nhà trẻ công lập chất lượng cao, nghỉ thai sản hưởng nguyên lương và giảm thuế thu nhập. Bằng cách hỗ trợ phụ nữ vừa đi làm vừa sinh con, Pháp duy trì mức sinh cao hàng đầu châu Âu, chứng minh cân bằng công việc và gia đình hiệu quả hơn các khoản thưởng tiền mặt đơn thuần."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược làm bài thi IGCSE về Dân số",
        "selector": "#card-exam-strategy",
        "en": "In Cambridge IGCSE examination questions: always quote precise statistical figures including birth rates, death rates, and natural increase; distinguish natural population change from total change; and explain the specific socio-economic drivers behind demographic transitions.",
        "vi": "Khi làm bài thi IGCSE: các em hãy luôn trích dẫn số liệu thống kê cụ thể gồm tỉ suất sinh, tỉ suất tử và mức gia tăng tự nhiên; phân biệt rõ biến động tự nhiên với biến động tổng dân số; đồng thời giải thích rõ các cơ chế kinh tế xã hội đằng sau sự chuyển dịch nhân khẩu học."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_demographic_concepts": {"start": 1, "end": 2},
    "sec_milestones": {"start": 3, "end": 4},
    "sec_birth_death_factors": {"start": 5, "end": 7},
    "sec_dtm": {"start": 8, "end": 10},
    "sec_population_policies": {"start": 11, "end": 14}
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
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    1. Key Demographic Concepts & The Population Balancing Equation\n  </h2>',
        '<h2 id="sec-demographic-concepts" class="lecture-interactive-card" data-lecture-section="sec_demographic_concepts" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    1. Key Demographic Concepts & The Population Balancing Equation\n  </h2>'
    )

    # Balancing equation card
    html = html.replace(
        '<div style="background:#faf5ff; border:2px dashed #c084fc; border-radius:10px; padding:16px; text-align:center; margin:18px 0;">',
        '<div id="card-balancing-equation" class="lecture-interactive-card" data-lecture-section="balancing_equation" style="background:#faf5ff; border:2px dashed #c084fc; border-radius:10px; padding:16px; text-align:center; margin:18px 0; cursor:pointer;">'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    2. Global Population Growth Milestones & Regional Distribution\n  </h2>',
        '<h2 id="sec-milestones" class="lecture-interactive-card" data-lecture-section="sec_milestones" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    2. Global Population Growth Milestones & Regional Distribution\n  </h2>'
    )

    # Table of Milestones
    html = html.replace(
        '<div style="overflow-x:auto; margin:20px 0;">\n    <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border-radius:8px; overflow:hidden; border:1px solid #e2e8f0;">',
        '<div id="card-milestones-table" class="lecture-interactive-card" data-lecture-section="milestones_table" style="overflow-x:auto; margin:20px 0; cursor:pointer;">\n    <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border-radius:8px; overflow:hidden; border:1px solid #e2e8f0;">'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    3. Factors Driving Variations in Birth & Death Rates\n  </h2>',
        '<h2 id="sec-birth-death-factors" class="lecture-interactive-card" data-lecture-section="sec_birth_death_factors" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    3. Factors Driving Variations in Birth & Death Rates\n  </h2>'
    )

    # Fertility factors grid
    html = html.replace(
        '<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:16px; margin:20px 0;">',
        '<div id="card-fertility-factors" class="lecture-interactive-card" data-lecture-section="fertility_factors" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:16px; margin:20px 0; cursor:pointer;">'
    )

    # Mortality transition
    html = html.replace(
        '<h3 style="color:#6d28d9; font-size:18px; margin-top:24px; margin-bottom:12px;">Factors Influencing Mortality & The Epidemiological Transition</h3>',
        '<h3 id="card-mortality-transition" class="lecture-interactive-card" data-lecture-section="mortality_transition" style="color:#6d28d9; font-size:18px; margin-top:24px; margin-bottom:12px; cursor:pointer;">Factors Influencing Mortality & The Epidemiological Transition</h3>'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    4. The Demographic Transition Model (DTM)\n  </h2>',
        '<h2 id="sec-dtm" class="lecture-interactive-card" data-lecture-section="sec_dtm" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    4. The Demographic Transition Model (DTM)\n  </h2>'
    )

    # DTM stages container
    html = html.replace(
        '<div style="display:flex; flex-direction:column; gap:16px; margin:20px 0;">',
        '<div id="card-dtm-stages" class="lecture-interactive-card" data-lecture-section="dtm_stages" style="display:flex; flex-direction:column; gap:16px; margin:20px 0; cursor:pointer;">'
    )

    # DTM evaluation grid
    html = html.replace(
        '<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:16px; margin:20px 0;">\n    <div style="background:#f0fdf4; border-top:4px solid #22c55e;',
        '<div id="card-dtm-evaluation" class="lecture-interactive-card" data-lecture-section="dtm_evaluation" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(380px, 1fr)); gap:16px; margin:20px 0; cursor:pointer;">\n    <div style="background:#f0fdf4; border-top:4px solid #22c55e;'
    )

    # Section 5 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    5. Population Policies: Anti-Natalist vs. Pro-Natalist Interventions\n  </h2>',
        '<h2 id="sec-population-policies" class="lecture-interactive-card" data-lecture-section="sec_population_policies" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    5. Population Policies: Anti-Natalist vs. Pro-Natalist Interventions\n  </h2>'
    )

    # China One-Child Policy card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #fecaca; border-radius:12px; padding:20px; box-shadow:0 4px 6px -1px rgba(220, 38, 38, 0.05);">',
        '<div id="card-policy-china" class="lecture-interactive-card" data-lecture-section="policy_china_antinatalist" style="background:#ffffff; border:1px solid #fecaca; border-radius:12px; padding:20px; box-shadow:0 4px 6px -1px rgba(220, 38, 38, 0.05); cursor:pointer;">'
    )

    # France Pro-Natalist card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #c7d2fe; border-radius:12px; padding:20px; box-shadow:0 4px 6px -1px rgba(79, 70, 229, 0.05);">',
        '<div id="card-policy-france" class="lecture-interactive-card" data-lecture-section="policy_france_pronatalist" style="background:#ffffff; border:1px solid #c7d2fe; border-radius:12px; padding:20px; box-shadow:0 4px 6px -1px rgba(79, 70, 229, 0.05); cursor:pointer;">'
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
