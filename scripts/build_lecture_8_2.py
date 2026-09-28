import asyncio
import os
import re
import sys
from pathlib import Path

sys.path.append('scripts')
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "8_2"
LECTURE_ID = "9cf90212-43f4-4b28-8014-fd6c130db8ef"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "8.2 The World is Developing Unevenly"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 8.2: Thế giới đang phát triển không đồng đều",
        "selector": "#sec-header",
        "en": "Welcome to Lesson 8.2: The World is Developing Unevenly. In this lecture, we investigate the global development divide: classifying countries along the income continuum, dissecting physical versus historical causes of disparity, contrasting Rostow's Modernisation Theory against Frank's Dependency Theory, and evaluating strategic policy levers to shatter the vicious cycle of poverty.",
        "vi": "Chào mừng các em đến với bài tám chấm hai: Thế giới đang phát triển không đồng đều. Trong bài giảng này, chúng ta sẽ khảo sát sự phân hóa phát triển toàn cầu: phân loại các quốc gia trên thang bậc thu nhập, bóc tách các nguyên nhân địa lý tự nhiên và lịch sử, đối chiếu Thuyết hiện đại hóa của Rostow với Thuyết phụ thuộc của Frank, và đánh giá các đòn bẩy chính sách nhằm phá vỡ vòng luẩn quẩn của đói nghèo."
    },
    {
        "id": "sec_uneven_continuum",
        "title": "1. Thang bậc phát triển và Phân loại thu nhập",
        "selector": "#sec-uneven-continuum",
        "en": "Section 1 classifies global economies across the development spectrum: Low-Income Countries with GNI per capita below 1,145 dollars, Middle-Income Economies including emerging Newly Industrialised Countries, and High-Income Nations with per capita income exceeding 14,005 dollars.",
        "vi": "Mục một phân loại các nền kinh tế trên thang bậc phát triển: Các nước thu nhập thấp với GNI bình quân dưới một nghìn một trăm bốn mươi lăm đô la, các nền kinh tế thu nhập trung bình bao gồm các nước mới công nghiệp hóa, và các quốc gia thu nhập cao với mức thu nhập bình quân vượt mười bốn nghìn không trăm lẻ năm đô la."
    },
    {
        "id": "sec_underlying_causes",
        "title": "2. Nguyên nhân sâu xa của sự phát triển không đồng đều",
        "selector": "#sec-underlying-causes",
        "en": "Section 2 investigates why disparities persist. Uneven development is not accidental; it is driven by a complex interplay of physical geography, colonial exploitation, corrupt governance, and unequal international terms of trade.",
        "vi": "Mục hai nghiên cứu lý do tại sao sự chênh lệch lại dai dẳng. Sự phát triển không đều không phải là ngẫu nhiên; nó được thúc đẩy bởi sự đan xen phức tạp giữa địa lý tự nhiên, sự bóc lột thời thuộc địa, quản trị tham nhũng và các điều khoản thương mại quốc tế bất bình đẳng."
    },
    {
        "id": "physical_factors",
        "title": "A. Các yếu tố tự nhiên và Địa lý",
        "selector": "#card-physical-factors",
        "en": "Physical barriers severely hamper economic progress: landlocked geography imposes massive transit tariffs, tropical disease burdens sap labor productivity, steep mountainous relief inflates infrastructure costs, and climate vulnerability to droughts destroys harvests.",
        "vi": "Các rào cản tự nhiên cản trở nghiêm trọng sự tiến bộ kinh tế: địa lý không giáp biển làm tăng vọt chi phí vận tải, gánh nặng bệnh tật nhiệt đới làm suy kiệt năng suất lao động, địa hình đồi núi dốc đứng đẩy chi phí hạ tầng lên cao, và hạn hán do biến đổi khí hậu tàn phá mùa màng."
    },
    {
        "id": "historical_factors",
        "title": "B. Các yếu tố lịch sử, chính trị và kinh tế",
        "selector": "#card-historical-factors",
        "en": "Historical legacies cast long shadows: colonial extraction stripped raw resources while deliberately suppressing local manufacturing, corrupt governance misallocates national wealth, and unfavorable terms of trade keep primary commodity exporters poor.",
        "vi": "Di sản lịch sử để lại những vết hằn sâu sắc: chính sách bóc lột thuộc địa đã vắt kiệt tài nguyên thô và kìm hãm công nghiệp bản địa, quản trị yếu kém làm thất thoát ngân sách quốc gia, và điều kiện thương mại bất lợi khiến các nước xuất khẩu nông sản thô mãi mắc kẹt trong nghèo đói."
    },
    {
        "id": "sec_dev_theories",
        "title": "3. Các lý thuyết phát triển: Hiện đại hóa vs Phụ thuộc",
        "selector": "#sec-dev-theories",
        "en": "Section 3 contrasts two competing development paradigms: Walt Rostow's free-market Modernisation Model against André Gunder Frank's neo-Marxist Dependency Theory.",
        "vi": "Mục ba đối chiếu hai trường phái phát triển đối lập: Mô hình Hiện đại hóa kinh tế thị trường của Walt Rostow so với Thuyết Phụ thuộc tân Mác-xít của André Gunder Frank."
    },
    {
        "id": "dev_theories_svg",
        "title": "Sơ đồ đối chiếu: Mô hình Rostow và Thuyết phụ thuộc của Frank",
        "selector": "#card-dev-theories-svg",
        "en": "This diagram contrasts Rostow's optimistic five-stage escalator from traditional society to high mass consumption, against Frank's structural model where wealthy core nations systematically extract capital from dependent peripheries.",
        "vi": "Sơ đồ này đối chiếu thang năm giai đoạn lạc quan của Rostow từ xã hội truyền thống lên tiêu dùng đại chúng, với mô hình cấu trúc của Frank nơi các quốc gia trung tâm giàu có bòn rút có hệ thống tư bản từ các vùng ngoại vi phụ thuộc."
    },
    {
        "id": "sec_poverty_cycle",
        "title": "4. Vòng luẩn quẩn của đói nghèo và Giải pháp phá vỡ rào cản",
        "selector": "#sec-poverty-cycle",
        "en": "Section 4 explores the vicious self-reinforcing trap of poverty, and examines concrete policy levers that allow developing economies to achieve sustained take-off.",
        "vi": "Mục bốn phân tích vòng xoáy tự củng cố của nghèo đói, và xem xét các đòn bẩy chính sách cụ thể giúp các nền kinh tế đang phát triển bứt phá để cất cánh bền vững."
    },
    {
        "id": "poverty_cycle_svg",
        "title": "Sơ đồ vòng luẩn quẩn nghèo đói và Đòn bẩy can thiệp",
        "selector": "#card-poverty-cycle-svg",
        "en": "This flowchart traces the negative feedback loop: low income yields low savings, suppressing capital investment, which locks in low productivity. Target investments in STEM education, transport infrastructure, and female empowerment break this cycle.",
        "vi": "Lưu đồ này chỉ ra vòng phản hồi tiêu cực: thu nhập thấp dẫn tới tiết kiệm thấp, kìm hãm đầu tư vốn, làm năng suất mãi ở mức thấp. Các khoản đầu tư mục tiêu vào giáo dục khoa học, hạ tầng giao thông và trao quyền cho phụ nữ sẽ bẻ gãy mắt xích này."
    },
    {
        "id": "exam_summary",
        "title": "Tổng kết trọng tâm ôn thi Cambridge IGCSE: Chủ đề 8.2",
        "selector": "#card-exam-summary",
        "en": "When answering exam questions on uneven development, always evaluate multiple causal categories: synthesize physical constraints like landlocked borders with historical-political factors like colonial rail networks oriented purely toward export ports.",
        "vi": "Khi làm bài thi về phát triển không đồng đều, các em luôn cần phân tích đa chiều: kết hợp các yếu tố bất lợi tự nhiên như không có đường ra biển với các yếu tố lịch sử chính trị như hệ thống đường sắt thời thuộc địa chỉ phục vụ xuất khẩu tài nguyên thô ra cảng."
    }
]

MAJOR_SECTIONS = [
    {"id": "sec_uneven_continuum", "title": "1. Thang bậc phát triển thu nhập", "startSegmentId": "sec_uneven_continuum"},
    {"id": "sec_underlying_causes", "title": "2. Nguyên nhân sâu xa của chênh lệch", "startSegmentId": "sec_underlying_causes"},
    {"id": "sec_dev_theories", "title": "3. Thuyết Hiện đại hóa vs Phụ thuộc", "startSegmentId": "sec_dev_theories"},
    {"id": "sec_poverty_cycle", "title": "4. Vòng luẩn quẩn nghèo đói & Đòn bẩy", "startSegmentId": "sec_poverty_cycle"},
    {"id": "card_exam_summary", "title": "Trọng tâm ôn thi Cambridge", "startSegmentId": "exam_summary"}
]

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px;">1. The Uneven Development Continuum & The Income Ladder</h2>',
        '<h2 id="sec-uneven-continuum" class="lecture-interactive-card" data-lecture-section="sec_uneven_continuum" style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">1. The Uneven Development Continuum & The Income Ladder</h2>'
    )

    # Section 2 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px;">2. Why is Development Uneven? Underlying Causes</h2>',
        '<h2 id="sec-underlying-causes" class="lecture-interactive-card" data-lecture-section="sec_underlying_causes" style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">2. Why is Development Uneven? Underlying Causes</h2>'
    )

    # Physical Factors Heading
    html = html.replace(
        '<h3 style="font-size: 18px; font-weight: 700; color: #1e40af; margin-top: 24px;">A. Physical & Geographical Factors</h3>',
        '<h3 id="card-physical-factors" class="lecture-interactive-card" data-lecture-section="physical_factors" style="font-size: 18px; font-weight: 700; color: #1e40af; margin-top: 24px; cursor:pointer;">A. Physical & Geographical Factors</h3>'
    )

    # Historical Factors Heading
    html = html.replace(
        '<h3 style="font-size: 18px; font-weight: 700; color: #1e40af; margin-top: 24px;">B. Historical, Political & Economic Factors</h3>',
        '<h3 id="card-historical-factors" class="lecture-interactive-card" data-lecture-section="historical_factors" style="font-size: 18px; font-weight: 700; color: #1e40af; margin-top: 24px; cursor:pointer;">B. Historical, Political & Economic Factors</h3>'
    )

    # Section 3 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px;">3. Development Theories: Modernisation vs. Dependency</h2>',
        '<h2 id="sec-dev-theories" class="lecture-interactive-card" data-lecture-section="sec_dev_theories" style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">3. Development Theories: Modernisation vs. Dependency</h2>'
    )

    # Rostow vs Frank SVG Card
    target_rostow = '<div style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">\n  <div style="text-align: center; margin-bottom: 16px;">\n    <span style="background: #fef3c7; color: #b45309; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">Theoretical Models Comparison</span>'
    repl_rostow = '<div id="card-dev-theories-svg" class="lecture-interactive-card" data-lecture-section="dev_theories_svg" style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">\n  <div style="text-align: center; margin-bottom: 16px;">\n    <span style="background: #fef3c7; color: #b45309; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">Theoretical Models Comparison</span>'
    html = html.replace(target_rostow, repl_rostow)

    # Section 4 Heading
    html = html.replace(
        '<h2 style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px;">4. The Vicious Cycle of Poverty & Breaking the Trap</h2>',
        '<h2 id="sec-poverty-cycle" class="lecture-interactive-card" data-lecture-section="sec_poverty_cycle" style="font-size: 24px; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #bfdbfe; padding-bottom: 8px; margin-top: 36px; cursor:pointer;">4. The Vicious Cycle of Poverty & Breaking the Trap</h2>'
    )

    # Vicious Cycle SVG Card
    target_poverty = '<div style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04);">\n  <div style="text-align: center; margin-bottom: 16px;">\n    <span style="background: #fee2e2; color: #b91c1c; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">Structural Dilemma</span>'
    repl_poverty = '<div id="card-poverty-cycle-svg" class="lecture-interactive-card" data-lecture-section="poverty_cycle_svg" style="margin: 28px 0; background: #ffffff; border: 1px solid #fed7aa; border-radius: 12px; padding: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor:pointer;">\n  <div style="text-align: center; margin-bottom: 16px;">\n    <span style="background: #fee2e2; color: #b91c1c; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">Structural Dilemma</span>'
    html = html.replace(target_poverty, repl_poverty)

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
