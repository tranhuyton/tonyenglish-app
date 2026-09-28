import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "6_2"
LECTURE_ID = "5390b0d7-995c-4c18-a092-b5cdd4eda49a"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "6.2 Population Structures Change Over Time"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 6.2: Cơ cấu dân số biến đổi theo thời gian",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 6.2: Population Structures Change Over Time. In this lecture, we examine the age and gender architecture of nations. We analyze the three functional age cohorts, master the Dependency Ratio formula, interpret population pyramids across DTM stages, and contrast the youthful population challenge of The Gambia against the hyper-aged society of Japan and India's regional disparities.",
        "vi": "Chào mừng các em đến với bài sáu chấm hai: Cơ cấu dân số biến đổi theo thời gian. Trong bài học này, chúng ta sẽ khảo sát cấu trúc độ tuổi và giới tính của các quốc gia. Chúng ta sẽ phân tích ba nhóm tuổi chức năng, thành thạo công thức tính tỉ số phụ thuộc, đọc tháp dân số qua các giai đoạn DTM, và so sánh thách thức dân số trẻ ở Gambia với xã hội siêu già hóa ở Nhật Bản cùng sự phân hóa vùng miền tại Ấn Độ."
    },
    {
        "id": "sec_structure_dependency",
        "title": "1. Cơ cấu dân số và Tỉ số phụ thuộc",
        "selector": "#sec-structure-dependency",
        "en": "Section 1 establishes the structural framework of demography. A population is divided into three functional cohorts: Young Dependents aged under 15, the Economically Active labor force aged 15 to 64 who pay income taxes, and Elderly Dependents aged 65 and over who draw on pensions and healthcare.",
        "vi": "Mục một thiết lập khuôn khổ phân tích cơ cấu dân số. Dân số được chia làm ba nhóm tuổi chức năng: Nhóm phụ thuộc trẻ dưới mười lăm tuổi, nhóm lao động từ mười lăm đến sáu mươi tư tuổi đóng thuế thu nhập, và nhóm phụ thuộc già từ sáu mươi lăm tuổi trở lên hưởng lương hưu và chăm sóc y tế."
    },
    {
        "id": "age_cohorts",
        "title": "Ba nhóm tuổi chức năng trong dân số",
        "selector": "#card-age-cohorts",
        "en": "The relative size of these three cohorts dictates a country's economic vitality and government fiscal allocations between schools, job creation, and elderly healthcare.",
        "vi": "Quy mô tương đối của ba nhóm tuổi này quyết định sức sống kinh tế của một quốc gia và sự phân bổ ngân sách nhà nước giữa trường học, tạo việc làm và dịch vụ y tế cho người cao tuổi."
    },
    {
        "id": "dependency_formula",
        "title": "Công thức tính tỉ số phụ thuộc",
        "selector": "#card-dependency-formula",
        "en": "The Dependency Ratio measures the burden supported by the working population. It equals the percentage of population aged 0 to 14 plus the percentage aged 65 and over, divided by the percentage of working age 15 to 64, multiplied by 100. It can be split into Youth Dependency and Old-Age Dependency.",
        "vi": "Tỉ số phụ thuộc đo lường gánh nặng kinh tế đặt lên lực lượng lao động. Tỉ số này bằng tổng phần trăm dân số từ không đến mười bốn tuổi cộng phần trăm trên sáu mươi lăm tuổi, chia cho phần trăm độ tuổi lao động từ mười lăm đến sáu mươi tư, nhân với một trăm. Chỉ số này có thể tách riêng thành tỉ số phụ thuộc trẻ và tỉ số phụ thuộc già."
    },
    {
        "id": "pyramid_anatomy",
        "title": "Giải phẫu tháp dân số",
        "selector": "#card-pyramid-anatomy",
        "en": "This diagram illustrates the anatomy of an age-sex population pyramid: males on the left, females on the right, five-year age bands stacked along the vertical central axis, and horizontal tiers delineating the three functional dependent and active cohorts.",
        "vi": "Sơ đồ này minh họa giải phẫu của một tháp dân số theo tuổi và giới tính: nam giới bên trái, nữ giới bên phải, các dải độ tuổi năm năm xếp dọc theo trục trung tâm, và các tầng ngang phân định rõ ba nhóm phụ thuộc và lao động."
    },
    {
        "id": "sec_pyramid_stages",
        "title": "2. Phân tích tháp dân số qua các giai đoạn DTM",
        "selector": "#sec-pyramid-stages",
        "en": "Section 2 traces how population pyramids transform from expansive triangles with wide bases in Stage 2 like Niger, to transitional beehives in Stage 3 like Pakistan, columnar stationary rectangles in Stage 4 like Canada, and constrictive inverted urns in Stage 5 like Japan.",
        "vi": "Mục hai theo dõi sự biến đổi hình thái tháp dân số: từ dạng tam giác đáy rộng mở rộng ở giai đoạn hai như Niger, sang dạng tổ ong chuyển tiếp ở giai đoạn ba như Pakistan, dạng cột ổn định ở giai đoạn bốn như Canada, và dạng thắt đáy thu hẹp ở giai đoạn năm như Nhật Bản."
    },
    {
        "id": "pyramid_comparison_table",
        "title": "Bảng đối chiếu nhân khẩu học bốn quốc gia",
        "selector": "#card-pyramid-comparison-table",
        "en": "Comparing Niger, Pakistan, Canada, and Japan highlights extreme demographic divergence: Niger has nearly half its population under age 15, whereas Japan has thirty percent of its citizens aged 65 and over.",
        "vi": "Bảng đối chiếu giữa Niger, Pakistan, Canada và Nhật Bản làm nổi bật sự phân hóa nhân khẩu sâu sắc: Niger có gần một nửa dân số dưới mười lăm tuổi, trong khi Nhật Bản có tới ba mươi phần trăm công dân từ sáu mươi lăm tuổi trở lên."
    },
    {
        "id": "pyramid_anomalies",
        "title": "Cách đọc các vết lõm, phình to và bất đối xứng",
        "selector": "#card-pyramid-anomalies",
        "en": "Demographers examine structural anomalies: indentations left by past wars or famines, bulges caused by baby booms or male guest-worker migration in Gulf oil states, and the universal female longevity advantage in elderly cohorts.",
        "vi": "Các nhà địa lý phân tích các bất thường cấu trúc: các vết lõm do chiến tranh hoặc nạn đói trong quá khứ, các chỗ phình to do bùng nổ trẻ sơ sinh hoặc nhập cư lao động nam giới tại các nước Vùng Vịnh, cùng ưu thế tuổi thọ tự nhiên của phụ nữ ở các nhóm tuổi già."
    },
    {
        "id": "sec_youthful_gambia",
        "title": "3. Thách thức dân số trẻ và Nghiên cứu tình huống: Gambia",
        "selector": "#sec-youthful-gambia",
        "en": "Section 3 investigates the youthful population crisis. When over forty percent of citizens are under fifteen, severe public finance strains emerge across primary schooling, pediatric health, deforestation for firewood, and youth unemployment.",
        "vi": "Mục ba tìm hiểu cuộc khủng hoảng dân số trẻ. Khi hơn bốn mươi phần trăm dân số dưới mười lăm tuổi, những áp lực tài chính công gay gắt sẽ xuất hiện trong giáo dục tiểu học, y tế nhi khoa, nạn phá rừng lấy củi đun và thất nghiệp thanh niên."
    },
    {
        "id": "case_study_matrix",
        "title": "Ma trận đối chiếu Gambia và Nhật Bản",
        "selector": "#card-case-study-matrix",
        "en": "This interactive matrix contrasts the opposing challenges: The Gambia struggling with classroom shortages and infant mortality versus Japan confronting pension deficits and deserted rural towns.",
        "vi": "Ma trận so sánh này đối chiếu hai thái cực thách thức: Gambia đối mặt với tình trạng thiếu lớp học và tử vong trẻ sơ sinh, trong khi Nhật Bản đối mặt với thâm hụt quỹ lương hưu và các thị trấn nông thôn bị bỏ hoang."
    },
    {
        "id": "gambia_details",
        "title": "Chi tiết nghiên cứu tình huống Cộng hòa Gambia",
        "selector": "#card-gambia-details",
        "en": "In The Gambia, a high fertility rate of over five children per woman doubles the population in twenty-four years. Schools operate mandatory two-shift days with class sizes over fifty pupils, forests around the capital are decimated for fuel, and youth flock into informal urban settlements.",
        "vi": "Tại Gambia, mức sinh cao trên năm con trên một phụ nữ khiến dân số tăng gấp đôi chỉ trong hai mươi tư năm. Các trường học phải chia làm hai ca học với sĩ số trên năm mươi học sinh một lớp, rừng quanh thủ đô bị đốn hạ để lấy chất đốt, và thanh niên đổ xô vào các khu nhà ổ chuột ven đô."
    },
    {
        "id": "sec_ageing_crisis",
        "title": "4. Cuộc khủng hoảng già hóa dân số và Nghiên cứu tình huống: Nhật Bản",
        "selector": "#sec-ageing-crisis",
        "en": "Section 4 evaluates demographic aging. When sub-replacement fertility combines with life expectancy exceeding eighty years, societies face shrinking workforces, surging healthcare costs, and unsustainable pension commitments.",
        "vi": "Mục bốn đánh giá cuộc khủng hoảng già hóa dân số. Khi mức sinh dưới ngưỡng thay thế kết hợp cùng tuổi thọ vượt tám mươi năm, xã hội phải đối mặt với lực lượng lao động suy giảm, chi phí y tế tăng vọt và quỹ lương hưu mất cân đối nghiêm trọng."
    },
    {
        "id": "japan_details",
        "title": "Chi tiết xã hội siêu già hóa tại Nhật Bản",
        "selector": "#card-japan-details",
        "en": "Japan's total population shrinks by hundreds of thousands annually. With barely two workers per retiree, public debt has ballooned beyond 260% of GDP. To adapt, Japan is pioneering robotic eldercare, automated transport, and raising retirement ages to seventy.",
        "vi": "Dân số Nhật Bản sụt giảm hàng trăm nghìn người mỗi năm. Với tỉ lệ chỉ còn hai người lao động gánh một người về hưu, nợ công đã phình to vượt hai trăm sáu mươi phần trăm GDP. Để thích ứng, Nhật Bản đang tiên phong ứng dụng robot chăm sóc người già, tự động hóa và nâng tuổi nghỉ hưu lên bảy mươi."
    },
    {
        "id": "sec_india_disparities",
        "title": "5. Phân hóa nhân khẩu học vùng miền tại Ấn Độ",
        "selector": "#sec-india-disparities",
        "en": "Section 5 highlights spatial disparities within India. Northern states like Bihar and Uttar Pradesh retain high fertility of 2.4 to 3.0 children per woman due to agrarian dependence and lower female literacy. In stark contrast, southern states like Kerala achieved near-universal female literacy and comprehensive healthcare, dropping fertility below replacement to 1.8.",
        "vi": "Mục năm làm nổi bật sự phân hóa không gian bên trong Ấn Độ. Các bang miền Bắc như Bihar và Uttar Pradesh duy trì mức sinh cao từ hai phẩy bốn đến ba phẩy không do phụ thuộc nông nghiệp và học vấn phụ nữ còn thấp. Trái lại, các bang miền Nam như Kerala đã phổ cập giáo dục cho phụ nữ và mạng lưới y tế hoàn thiện, đưa mức sinh xuống dưới ngưỡng thay thế chỉ còn một phẩy tám con."
    },
    {
        "id": "exam_strategy",
        "title": "Chiến lược làm bài thi IGCSE về Cơ cấu dân số",
        "selector": "#card-exam-strategy",
        "en": "When answering exam questions: quote specific cohort categories Young, Active, and Elderly; show full workings when calculating the Dependency Ratio; and explicitly link pyramid shapes to their corresponding DTM stage.",
        "vi": "Khi làm bài thi IGCSE: các em hãy gọi tên chính xác ba nhóm tuổi gồm Phụ thuộc trẻ, Lao động và Phụ thuộc già; trình bày đầy đủ các bước tính Tỉ số phụ thuộc; và nêu rõ hình thái tháp dân số tương ứng với giai đoạn nào của mô hình DTM."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_structure_dependency": {"start": 1, "end": 4},
    "sec_pyramid_stages": {"start": 5, "end": 7},
    "sec_youthful_gambia": {"start": 8, "end": 10},
    "sec_ageing_crisis": {"start": 11, "end": 12},
    "sec_india_disparities": {"start": 13, "end": 14}
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
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    1. Population Structure, Cohorts & The Dependency Ratio\n  </h2>',
        '<h2 id="sec-structure-dependency" class="lecture-interactive-card" data-lecture-section="sec_structure_dependency" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:36px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    1. Population Structure, Cohorts & The Dependency Ratio\n  </h2>'
    )

    # Cohorts grid
    html = html.replace(
        '<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin:20px 0;">',
        '<div id="card-age-cohorts" class="lecture-interactive-card" data-lecture-section="age_cohorts" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin:20px 0; cursor:pointer;">'
    )

    # Dependency formula card
    html = html.replace(
        '<div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:18px; margin:18px 0; text-align:center;">',
        '<div id="card-dependency-formula" class="lecture-interactive-card" data-lecture-section="dependency_formula" style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:18px; margin:18px 0; text-align:center; cursor:pointer;">'
    )

    # Anatomy vector diagram card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#4c1d95; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#7c3aed; border-radius:50%;"></span>\n    Interactive Vector Diagram: Anatomy of a Population Pyramid & The Three Cohort Tiers',
        '<div id="card-pyramid-anatomy" class="lecture-interactive-card" data-lecture-section="pyramid_anatomy" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#4c1d95; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#7c3aed; border-radius:50%;"></span>\n    Interactive Vector Diagram: Anatomy of a Population Pyramid & The Three Cohort Tiers'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    2. Interpreting Population Pyramids Across DTM Stages\n  </h2>',
        '<h2 id="sec-pyramid-stages" class="lecture-interactive-card" data-lecture-section="sec_pyramid_stages" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    2. Interpreting Population Pyramids Across DTM Stages\n  </h2>'
    )

    # Pyramid comparison table
    html = html.replace(
        '<div style="overflow-x:auto; margin:20px 0;">\n    <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border-radius:8px; overflow:hidden; border:1px solid #e2e8f0;">',
        '<div id="card-pyramid-comparison-table" class="lecture-interactive-card" data-lecture-section="pyramid_comparison_table" style="overflow-x:auto; margin:20px 0; cursor:pointer;">\n    <table style="width:100%; border-collapse:collapse; font-size:14px; text-align:left; background:#ffffff; border-radius:8px; overflow:hidden; border:1px solid #e2e8f0;">'
    )

    # Pyramid anomalies heading
    html = html.replace(
        '<h3 style="color:#6d28d9; font-size:18px; margin-top:24px; margin-bottom:12px;">Reading Anomalies, Indents and Asymmetries</h3>',
        '<h3 id="card-pyramid-anomalies" class="lecture-interactive-card" data-lecture-section="pyramid_anomalies" style="color:#6d28d9; font-size:18px; margin-top:24px; margin-bottom:12px; cursor:pointer;">Reading Anomalies, Indents and Asymmetries</h3>'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    3. The Youthful Population Challenge & Case Study: The Gambia\n  </h2>',
        '<h2 id="sec-youthful-gambia" class="lecture-interactive-card" data-lecture-section="sec_youthful_gambia" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    3. The Youthful Population Challenge & Case Study: The Gambia\n  </h2>'
    )

    # Case study matrix card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05);">\n  <div style="font-weight:700; font-size:17px; color:#4c1d95; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#f59e0b; border-radius:50%;"></span>\n    Demographic Case Study Matrix: Youthful Population (The Gambia) vs. Ageing Society (Japan & EU)',
        '<div id="card-case-study-matrix" class="lecture-interactive-card" data-lecture-section="case_study_matrix" style="background:#ffffff; border:1px solid #e2e8f0; border-radius:12px; padding:20px; margin:24px 0; box-shadow:0 4px 6px -1px rgba(0,0,0,0.05); cursor:pointer;">\n  <div style="font-weight:700; font-size:17px; color:#4c1d95; margin-bottom:6px; display:flex; align-items:center; gap:8px;">\n    <span style="display:inline-block; width:10px; height:10px; background:#f59e0b; border-radius:50%;"></span>\n    Demographic Case Study Matrix: Youthful Population (The Gambia) vs. Ageing Society (Japan & EU)'
    )

    # Gambia details card
    html = html.replace(
        '<div style="background:#fdf4ff; border-left:4px solid #a855f7; padding:16px; border-radius:8px; margin:18px 0;">\n    <div style="font-weight:700; color:#581c87; margin-bottom:8px;">Key Socio-Economic Impacts in The Gambia:</div>',
        '<div id="card-gambia-details" class="lecture-interactive-card" data-lecture-section="gambia_details" style="background:#fdf4ff; border-left:4px solid #a855f7; padding:16px; border-radius:8px; margin:18px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#581c87; margin-bottom:8px;">Key Socio-Economic Impacts in The Gambia:</div>'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    4. The Ageing Population Crisis & Case Study: The European Union & Japan\n  </h2>',
        '<h2 id="sec-ageing-crisis" class="lecture-interactive-card" data-lecture-section="sec_ageing_crisis" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    4. The Ageing Population Crisis & Case Study: The European Union & Japan\n  </h2>'
    )

    # Japan details card
    html = html.replace(
        '<div style="background:#eff6ff; border-left:4px solid #3b82f6; padding:16px; border-radius:8px; margin:18px 0;">\n    <div style="font-weight:700; color:#1d4ed8; margin-bottom:8px;">Structural Ramifications for Japan:</div>',
        '<div id="card-japan-details" class="lecture-interactive-card" data-lecture-section="japan_details" style="background:#eff6ff; border-left:4px solid #3b82f6; padding:16px; border-radius:8px; margin:18px 0; cursor:pointer;">\n    <div style="font-weight:700; color:#1d4ed8; margin-bottom:8px;">Structural Ramifications for Japan:</div>'
    )

    # Section 5 Heading
    html = html.replace(
        '<h2 style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700;">\n    5. Regional Demographic Disparities: Case Study of India\n  </h2>',
        '<h2 id="sec-india-disparities" class="lecture-interactive-card" data-lecture-section="sec_india_disparities" style="color:#4c1d95; border-bottom:2px solid #ddd6fe; padding-bottom:8px; margin-top:40px; margin-bottom:18px; font-size:22px; font-weight:700; cursor:pointer;">\n    5. Regional Demographic Disparities: Case Study of India\n  </h2>'
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
