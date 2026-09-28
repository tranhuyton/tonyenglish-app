import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "8_1"
LECTURE_ID = "5ff5f837-df39-4488-bbd2-5138f4faed1e"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "8.1 Measuring Development"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 8.1: Đo lường sự phát triển",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 8.1: Measuring Development. In this lecture, we examine how geographers assess human progress: distinguishing Standard of Living from Quality of Life, evaluating economic versus social single indicators, mastering the multi-dimensional Human Development Index, and analyzing why the historic 1980 Brandt Line collapsed into today's complex multi-polar economic reality.",
        "vi": "Chào mừng các em đến với bài tám chấm một: Đo lường sự phát triển. Trong bài học này, chúng ta sẽ khảo sát cách các nhà địa lý đánh giá sự tiến bộ của con người: phân biệt mức sống vật chất với chất lượng cuộc sống toàn diện, đánh giá các chỉ số đơn lẻ về kinh tế và xã hội, thành thạo Chỉ số Phát triển Con người đa chiều HDI, và phân tích lý do đường ranh giới Brandt năm 1980 đã sụp đổ trước trật tự thế giới đa cực ngày nay."
    },
    {
        "id": "sec_what_is_dev",
        "title": "1. Khái niệm Phát triển và Chất lượng cuộc sống",
        "selector": "#sec-what-is-dev",
        "en": "Section 1 establishes the fundamental difference between economic wealth and human well-being. Standard of living refers purely to material possessions and monetary income, whereas Quality of life encompasses total physical health, social equality, environmental safety, and personal freedom.",
        "vi": "Mục một thiết lập sự khác biệt cốt lõi giữa của cải kinh tế và hạnh phúc con người. Mức sống thuần túy đo lường của cải vật chất và thu nhập tiền tệ, trong khi chất lượng cuộc sống bao quát sức khỏe thể chất, bình đẳng xã hội, an toàn môi trường và tự do cá nhân."
    },
    {
        "id": "sol_qol_table",
        "title": "Bảng phân loại các trụ cột phát triển",
        "selector": "#card-sol-qol-table",
        "en": "This table categorizes development into four interdependent domains: Economic prosperity, Social advancement, Environmental stability, and Political freedom. True sustainable development requires concurrent progress across all four dimensions.",
        "vi": "Bảng này phân loại sự phát triển thành bốn lĩnh vực tương hỗ: Thịnh vượng kinh tế, Tiến bộ xã hội, Ổn định môi trường và Tự do chính trị. Sự phát triển bền vững thực sự đòi hỏi sự tiến bộ đồng thời trên cả bốn phương diện này."
    },
    {
        "id": "sec_single_indicators",
        "title": "2. Các chỉ số phát triển đơn lẻ: Ưu điểm và Hạn chế",
        "selector": "#sec-single-indicators",
        "en": "Section 2 investigates single indicators of development. While simple to calculate, single indicators can be profoundly misleading because national averages conceal stark internal inequalities between billionaire elites and impoverished rural workers.",
        "vi": "Mục hai nghiên cứu các chỉ số phát triển đơn lẻ. Dù dễ tính toán, các chỉ số đơn lẻ có thể gây hiểu lầm nghiêm trọng do số liệu trung bình quốc gia che giấu sự bất bình đẳng gay gắt giữa giới thượng lưu giàu có và tầng lớp lao động nông thôn nghèo khó."
    },
    {
        "id": "economic_indicators",
        "title": "Các chỉ số kinh tế đơn lẻ: GDP, GNI và PPP",
        "selector": "#card-economic-indicators",
        "en": "Economic indicators include Gross Domestic Product, Gross National Income which captures overseas remittances and corporate earnings, and Purchasing Power Parity adjustments which equalize currency purchasing power across different domestic cost levels.",
        "vi": "Các chỉ số kinh tế bao gồm Tổng sản phẩm quốc nội GDP, Tổng thu nhập quốc dân GNI phản ánh cả kiều hối và lợi nhuận đầu tư nước ngoài, cùng hiệu chỉnh Sức mua tương đương PPP nhằm chuẩn hóa giá trị tiền tệ theo mức giá cả sinh hoạt tại từng quốc gia."
    },
    {
        "id": "social_indicators",
        "title": "Các chỉ số xã hội đơn lẻ: Y tế và Giáo dục",
        "selector": "#card-social-indicators",
        "en": "Social indicators reflect essential human welfare, such as Adult Literacy Rate, People per Doctor, and Infant Mortality Rate, which serves as the most sensitive bellwether of maternal nutrition and healthcare access.",
        "vi": "Các chỉ số xã hội phản ánh phúc lợi thiết yếu của con người, như Tỉ lệ người lớn biết chữ, Số dân trên một bác sĩ, và Tỉ lệ tử vong ở trẻ sơ sinh - thước đo nhạy cảm nhất về tình trạng dinh dưỡng của bà mẹ và khả năng tiếp cận dịch vụ y tế."
    },
    {
        "id": "sec_hdi",
        "title": "3. Chỉ số phát triển con người HDI",
        "selector": "#sec-hdi",
        "en": "Section 3 examines the United Nations Human Development Index. Created by Mahbub ul Haq and Amartya Sen, the HDI combines three vital dimensions: Decent Standard of Living, Long and Healthy Life, and Knowledge.",
        "vi": "Mục ba xem xét Chỉ số Phát triển Con người HDI của Liên Hợp Quốc. Được khởi xướng bởi Mahbub ul Haq và Amartya Sen, HDI kết hợp ba chiều kích thiết yếu: Mức sống khá giả, Đời sống dài lâu khỏe mạnh, và Kiến thức tri thức."
    },
    {
        "id": "hdi_architecture",
        "title": "Sơ đồ cấu trúc tính toán chỉ số HDI",
        "selector": "#card-hdi-architecture",
        "en": "This diagram illustrates the mathematical architecture of HDI: combining GNI per capita at PPP, Life Expectancy at birth, and Education measured by Mean and Expected Years of Schooling, synthesized using a geometric mean.",
        "vi": "Sơ đồ này minh họa cấu trúc toán học của HDI: kết hợp GNI bình quân đầu người theo PPP, Kỳ vọng sống khi sinh, và Giáo dục đo bằng Số năm đi học trung bình và kỳ vọng, được tổng hợp bằng phương pháp trung bình nhân."
    },
    {
        "id": "sec_brandt_multipolar",
        "title": "4. Từ Ranh giới Brandt đến Thế giới đa cực",
        "selector": "#sec-brandt-multipolar",
        "en": "Section 4 tracks the shifting geopolitics of global development. The 1980 Brandt Report drew a simplistic north-south line dividing the rich industrialized world from the poor agricultural south, an analytical model that has since completely broken down.",
        "vi": "Mục bốn theo dõi sự biến chuyển địa chính trị của phát triển toàn cầu. Báo cáo Brandt năm 1980 đã vẽ một đường phân chia bắc nam đơn giản hóa giữa thế giới công nghiệp giàu có và phương nam nông nghiệp nghèo nàn, một mô hình phân tích nay đã hoàn toàn lỗi thời."
    },
    {
        "id": "multipolar_evolution",
        "title": "Sơ đồ tiến hóa: Ranh giới Brandt 1980 so với Trật tự đa cực 2020",
        "selector": "#card-multipolar-evolution",
        "en": "This spatial visualization contrasts the 1980 binary division against the 2020s landscape, where Asian Tigers, China, India, and Gulf States have surged into economic powerhouses, invalidating simplistic North-South dichotomies.",
        "vi": "Minh họa không gian này đối chiếu sự phân chia nhị nguyên năm 1980 với cục diện thập niên 2020, nơi các con rồng châu Á, Trung Quốc, Ấn Độ và các quốc gia vùng Vịnh đã vươn lên thành cường quốc kinh tế, phá vỡ hoàn toàn định kiến Bắc - Nam cũ."
    },
    {
        "id": "brandt_failure",
        "title": "Tại sao Ranh giới Brandt thất bại trong phân tích hiện đại",
        "selector": "#card-brandt-failure",
        "en": "The Brandt Line collapsed because it treated the global South as homogeneous, ignored the explosive growth of Newly Industrialized Economies, and was undermined by resource-rich Gulf nations surpassing many European living standards.",
        "vi": "Đường ranh giới Brandt sụp đổ vì đã coi toàn bộ phương Nam là đồng nhất, phớt lờ sự trỗi dậy vũ bão của các nền kinh tế mới công nghiệp hóa, và bị phủ định bởi các quốc gia vùng Vịnh giàu dầu mỏ có mức sống vượt qua nhiều nước châu Âu."
    },
    {
        "id": "exam_summary",
        "title": "Tổng kết trọng tâm ôn thi Cambridge IGCSE: Chủ đề 8.1",
        "selector": "#card-exam-summary",
        "en": "For exam success, always explain why composite indicators like HDI are superior to single GDP metrics, describe the three core pillars of HDI accurately, and cite anomalies like oil-rich states that have high income but lower social index scores.",
        "vi": "Để đạt điểm cao trong kỳ thi, các em luôn cần giải thích tại sao chỉ số tổng hợp HDI vượt trội hơn chỉ số GDP đơn lẻ, mô tả chính xác ba trụ cột của HDI, và dẫn chứng các trường hợp dị biệt như các nước giàu dầu mỏ có thu nhập cao nhưng chỉ số xã hội chưa tương xứng."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_what_is_dev", "title": "1. Khái niệm Phát triển & Chất lượng sống", "startSegmentId": "sec_what_is_dev"},
    {"id": "sec_single_indicators", "title": "2. Các chỉ số phát triển đơn lẻ", "startSegmentId": "sec_single_indicators"},
    {"id": "sec_hdi", "title": "3. Chỉ số phát triển con người HDI", "startSegmentId": "sec_hdi"},
    {"id": "sec_brandt_multipolar", "title": "4. Ranh giới Brandt & Thế giới đa cực", "startSegmentId": "sec_brandt_multipolar"},
    {"id": "card_exam_summary", "title": "Trọng tâm ôn thi Cambridge", "startSegmentId": "exam_summary"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px;">1. What is Development & Quality of Life?</h2>',
        '<h2 id="sec-what-is-dev" class="lecture-interactive-card" data-lecture-section="sec_what_is_dev" style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">1. What is Development & Quality of Life?</h2>'
    )

    # Standard of Living vs Quality of Life table wrapper
    html = html.replace(
        '<div style="margin: 24px 0; overflow-x: auto;">\n    <table style="width: 100%; border-collapse: collapse; font-size: 14px; text-align: left; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">',
        '<div id="card-sol-qol-table" class="lecture-interactive-card" data-lecture-section="sol_qol_table" style="margin: 24px 0; overflow-x: auto; cursor:pointer;">\n    <table style="width: 100%; border-collapse: collapse; font-size: 14px; text-align: left; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;">'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px;">2. Single Indicators of Development: Merits & Limitations</h2>',
        '<h2 id="sec-single-indicators" class="lecture-interactive-card" data-lecture-section="sec_single_indicators" style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">2. Single Indicators of Development: Merits & Limitations</h2>'
    )

    # Economic Indicators Heading
    html = html.replace(
        '<h3 style="font-size: 18px; font-weight: 700; color: #92400e; margin-top: 24px;">Economic Single Indicators</h3>',
        '<h3 id="card-economic-indicators" class="lecture-interactive-card" data-lecture-section="economic_indicators" style="font-size: 18px; font-weight: 700; color: #92400e; margin-top: 24px; cursor:pointer;">Economic Single Indicators</h3>'
    )

    # Social Indicators Heading
    html = html.replace(
        '<h3 style="font-size: 18px; font-weight: 700; color: #92400e; margin-top: 24px;">Social Single Indicators</h3>',
        '<h3 id="card-social-indicators" class="lecture-interactive-card" data-lecture-section="social_indicators" style="font-size: 18px; font-weight: 700; color: #92400e; margin-top: 24px; cursor:pointer;">Social Single Indicators</h3>'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px;">3. The Human Development Index (HDI)</h2>',
        '<h2 id="sec-hdi" class="lecture-interactive-card" data-lecture-section="sec_hdi" style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">3. The Human Development Index (HDI)</h2>'
    )

    # HDI Architecture SVG Card
    html = html.replace(
        '<div style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">',
        '<div id="card-hdi-architecture" class="lecture-interactive-card" data-lecture-section="hdi_architecture" style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">'
    )

    # Section 4 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px;">4. From the Brandt Line to a Multi-Polar World</h2>',
        '<h2 id="sec-brandt-multipolar" class="lecture-interactive-card" data-lecture-section="sec_brandt_multipolar" style="font-size: 24px; font-weight: 800; color: #78350f; border-bottom: 2px solid #fed7aa; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">4. From the Brandt Line to a Multi-Polar World</h2>'
    )

    # Multi-Polar Evolution SVG Card
    html = html.replace(
        '<div style="margin: 28px 0; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">',
        '<div id="card-multipolar-evolution" class="lecture-interactive-card" data-lecture-section="multipolar_evolution" style="margin: 28px 0; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">'
    )

    # Brandt Failure Heading
    html = html.replace(
        '<h3 style="font-size: 18px; font-weight: 700; color: #92400e; margin-top: 24px;">Why the Brandt Line Failed as an Analytical Model:</h3>',
        '<h3 id="card-brandt-failure" class="lecture-interactive-card" data-lecture-section="brandt_failure" style="font-size: 18px; font-weight: 700; color: #92400e; margin-top: 24px; cursor:pointer;">Why the Brandt Line Failed as an Analytical Model:</h3>'
    )

    # Exam Summary Card
    html = html.replace(
        '<div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-top: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">',
        '<div id="card-exam-summary" class="lecture-interactive-card" data-lecture-section="exam_summary" style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-top: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">'
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
