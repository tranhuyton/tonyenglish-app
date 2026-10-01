import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 3.2 ID
LID = '356dede8-277a-441a-ad73-ef9384973eb7'
CODE = '3_2'
TITLE = '3.2. Market research'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 12 AUDIO SEGMENTS FOR LESSON 3.2
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 3.2: Nghiên cứu thị trường",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 3.2: Market Research. In this lesson, we explore product-oriented versus market-oriented business approaches, examine primary and secondary data collection techniques, evaluate sampling methods, and assess the accuracy of market intelligence.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 3.2: Nghiên cứu thị trường. Trong bài học này, chúng ta sẽ tìm hiểu định hướng sản phẩm và định hướng thị trường, các phương pháp thu thập dữ liệu sơ cấp và thứ cấp, kỹ thuật chọn mẫu cùng phương pháp đánh giá độ tin cậy của số liệu."
    },
    {
        "id": "sec_business_orientation",
        "title": "1. Định hướng Doanh nghiệp: Sản phẩm hay Thị trường",
        "selector": "#sec-business-orientation",
        "en": "Section 1 contrasts Product-Oriented businesses—which focus primarily on manufacturing excellence and technical innovation before trying to sell—against Market-Oriented businesses, which conduct comprehensive consumer research first to ensure new goods align precisely with customer preferences.",
        "vi": "Mục một đối chiếu Doanh nghiệp định hướng sản phẩm (Product-Oriented) – tập trung vào kỹ thuật và chất lượng sản phẩm trước khi bán – với Doanh nghiệp định hướng thị trường (Market-Oriented), luôn nghiên cứu nhu cầu khách hàng trước để bảo đảm sản phẩm mới đáp ứng đúng kỳ vọng của người tiêu dùng."
    },
    {
        "id": "card_product_market_orientation",
        "title": "🧭 Doanh nghiệp Định hướng Sản phẩm vs Định hướng Thị trường",
        "selector": "#card-product-market-orientation",
        "en": "Product-oriented firms focus on technical design and manufacturing capabilities, risking high launch failure if consumer demand does not materialize. In contrast, market-oriented businesses continuously conduct customer research to identify unmet desires before manufacturing, sharply lowering commercial failure rates and increasing long-term brand loyalty.",
        "vi": "Doanh nghiệp định hướng sản phẩm chú trọng vào năng lực thiết kế kỹ thuật và sản xuất, tiềm ẩn rủi ro thất bại cao nếu thị trường không có nhu cầu. Ngược lại, doanh nghiệp định hướng thị trường liên tục khảo sát khách hàng để tìm ra các nhu cầu chưa được đáp ứng trước khi sản xuất, giúp giảm thiểu rủi ro thất bại và gia tăng lòng trung thành thương hiệu."
    },
    {
        "id": "sec_market_research_intro",
        "title": "2. Vai trò của Nghiên cứu Thị trường",
        "selector": "#sec-market-research-intro",
        "en": "Section 2 introduces Market Research: the systematic gathering, recording, and analysis of data about the market for goods and services. Research minimizes commercial launch risks, identifies market gaps, reveals customer willingness to pay, and gauges competitive strengths.",
        "vi": "Mục hai giới thiệu về Nghiên cứu thị trường: quá trình thu thập, ghi chép và phân tích có hệ thống thông tin về thị trường hàng hóa và dịch vụ. Nghiên cứu giúp hạn chế rủi ro ra mắt sản phẩm mới, phát hiện khoảng trống thị trường, xác định mức giá sẵn sàng chi trả và đánh giá đối thủ cạnh tranh."
    },
    {
        "id": "card_quant_qual_data",
        "title": "🔢 Dữ liệu Định lượng (Quantitative) vs Dữ liệu Định tính (Qualitative)",
        "selector": "#card-quant-qual-data",
        "en": "Market data is gathered in two fundamental forms: Quantitative data provides numerical measurements and statistics such as sales volumes and percentages; Qualitative data reveals in-depth consumer opinions, emotional motivations, and underlying reasons why customers prefer one brand over another.",
        "vi": "Dữ liệu thị trường được thu thập dưới hai hình thức căn bản: Dữ liệu định lượng (Quantitative data) cung cấp các con số đo lường và thống kê số liệu như sản lượng bán và tỷ lệ phần trăm; Dữ liệu định tính (Qualitative data) đi sâu vào ý kiến, cảm xúc và lý do thực sự vì sao khách hàng lại yêu thích một thương hiệu này hơn thương hiệu khác."
    },
    {
        "id": "sec_primary_research",
        "title": "3. Nghiên cứu Sơ cấp (Field Research)",
        "selector": "#sec-primary-research",
        "en": "Section 3 examines Primary Research: gathering original first-hand data directly from respondents via questionnaires, focus groups, interviews, and direct observation. Primary data is up-to-date, directly relevant, and exclusive to the firm, but is expensive and time-consuming to execute.",
        "vi": "Mục ba phân tích Nghiên cứu sơ cấp (Primary Research): thu thập dữ liệu gốc lần đầu từ đối tượng khảo sát thông qua bảng câu hỏi, nhóm thảo luận tập trung, phỏng vấn sâu và quan sát thực tế. Dữ liệu sơ cấp có tính cập nhật cao, liên quan trực tiếp và mang tính độc quyền nhưng tốn kém chi phí và thời gian."
    },
    {
        "id": "card_primary_methods",
        "title": "🛠️ Các Phương pháp Nghiên cứu Sơ cấp (Bảng hỏi, Phỏng vấn, Thảo luận nhóm, Quan sát)",
        "selector": "#card-primary-methods",
        "en": "Primary research employs questionnaires for broad sampling, face-to-face interviews to probe complex answers, focus groups to test product prototypes, and observational auditing to track footfall patterns without survey bias.",
        "vi": "Nghiên cứu sơ cấp sử dụng bảng câu hỏi để khảo sát số đông, phỏng vấn trực tiếp để làm rõ các câu trả lời phức tạp, nhóm thảo luận tập trung (focus groups) để trải nghiệm sản phẩm mẫu và quan sát thực tế để đếm lưu lượng khách hàng mà không bị định kiến phỏng vấn."
    },
    {
        "id": "sec_secondary_research",
        "title": "4. Nghiên cứu Thứ cấp (Desk Research)",
        "selector": "#sec-secondary-research",
        "en": "Section 4 covers Secondary Research: gathering second-hand data already published by internal records, government census bureaus, trade journals, or commercial research agencies. Secondary research is cheap and instantly accessible, but may be outdated, biased, or too general.",
        "vi": "Mục bốn trình bày Nghiên cứu thứ cấp (Secondary Research): khai thác dữ liệu đã được công bố từ hồ sơ nội bộ, số liệu thống kê chính phủ, tạp chí chuyên ngành hoặc báo cáo thị trường. Nghiên cứu thứ cấp chi phí thấp và tra cứu tức thì nhưng số liệu có thể bị lỗi thời hoặc không khớp với mục tiêu nghiên cứu cụ thể."
    },
    {
        "id": "card_secondary_sources",
        "title": "🏢 Nguồn Dữ liệu Thứ cấp: Nội bộ vs Bên ngoài",
        "selector": "#card-secondary-sources",
        "en": "Secondary research divides into Internal Sources—including historical sales ledgers, customer service complaints, and finance budgets—and External Sources—such as government national statistics, industry journals, trade association analyses, and business media reports.",
        "vi": "Nghiên cứu thứ cấp chia thành Nguồn nội bộ – bao gồm nhật ký bán hàng quá khứ, khiếu nại chăm sóc khách hàng và báo cáo tài chính – cùng Nguồn bên ngoài – như thống kê dân số chính phủ, tạp chí thương mại ngành, báo cáo hiệp hội ngành nghề và truyền thông kinh doanh."
    },
    {
        "id": "sec_accuracy_presentation",
        "title": "5. Độ chính xác và Trình bày Dữ liệu",
        "selector": "#sec-accuracy-presentation",
        "en": "Section 5 analyzes data presentation via tally tables, bar charts, pie charts, and line graphs, while identifying sources of inaccuracy including sample bias, leading questions, respondent dishonesty, and obsolete secondary archives.",
        "vi": "Mục năm phân tích cách trình bày dữ liệu bằng bảng kiểm đếm, biểu đồ cột, biểu đồ tròn và đồ thị đường thẳng, đồng thời nhận diện các yếu tố gây sai lệch số liệu gồm mẫu khảo sát thiên lệch, câu hỏi dẫn dắt, câu trả lời thiếu trung thực và số liệu lưu trữ cũ đã lỗi thời."
    },
    {
        "id": "sec_sampling_methods",
        "title": "6. Kỹ thuật Chọn mẫu: Chọn mẫu Ngẫu nhiên vs Theo Hạn ngạch",
        "selector": "#sec-sampling-methods",
        "en": "Section 6 contrasts sampling techniques: Random Sampling gives every population member an equal mathematical chance of selection, eliminating researcher bias; Quota Sampling selects predetermined proportions matching target market demographics (such as age and gender), ensuring exact consumer representation.",
        "vi": "Mục sáu so sánh các kỹ thuật chọn mẫu: Chọn mẫu ngẫu nhiên (Random Sampling) trao cơ hội ngang nhau cho mọi thành viên trong tập số liệu, loại bỏ định kiến của người khảo sát; Chọn mẫu theo hạn ngạch (Quota Sampling) lựa chọn tỷ lệ định trước khớp với đặc tính khách hàng mục tiêu (như độ tuổi và giới tính), bảo đảm tính đại diện chuẩn xác cho phân khúc."
    },
    {
        "id": "sec_recommend_research",
        "title": "7. Chiến lược làm bài thi Cambridge: Đề xuất Phương pháp Nghiên cứu Thị trường",
        "selector": "#sec-recommend-research",
        "en": "Section 7 outlines Cambridge evaluation technique for recommending market research methods. Candidates must evaluate context: innovative new products require primary qualitative feedback; tight budgets and fast deadlines necessitate secondary desk data. Formulate a balanced recommendation mitigating costs against precision.",
        "vi": "Mục bảy tổng hợp phương pháp làm bài thi Cambridge khi đề xuất phương án nghiên cứu thị trường. Thí sinh phải bám sát bối cảnh: sản phẩm đột phá mới cần nghiên cứu sơ cấp định tính; ngân sách hạn hẹp và tiến độ gấp rút đòi hỏi số liệu thứ cấp có sẵn. Luôn đưa ra kết luận cân đối giữa chi phí đầu tư và độ chính xác của thông tin."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_business_orientation": {"start": 1, "end": 2},
    "sec_market_research_intro": {"start": 3, "end": 4},
    "sec_primary_research": {"start": 5, "end": 6},
    "sec_secondary_research": {"start": 7, "end": 8},
    "sec_accuracy_presentation": {"start": 9, "end": 9},
    "sec_sampling_methods": {"start": 10, "end": 10},
    "sec_recommend_research": {"start": 11, "end": 11}
}

# ==============================================================================
# 2. GENERATE NEW HTML FOR PAGE 1
# ==============================================================================
def build_page_1_html():
    html = """<div style="font-family: 'Segoe UI', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">

    <!-- TOP HEADER BANNER (NO STUDY RESOURCES) -->
    <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 3</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">3.2 Market Research (Nghiên cứu Thị trường)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. BUSINESS ORIENTATION -->
    <div style="margin-bottom: 45px;">
        <div id="sec-business-orientation" class="lecture-interactive-card" data-lecture-section="sec_business_orientation" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🧭 1. BUSINESS ORIENTATION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                A firm's strategic orientation dictates whether technical design or customer intelligence drives manufacturing decisions.
            </p>
        </div>

        <div id="card-product-market-orientation" class="lecture-interactive-card" data-lecture-section="card_product_market_orientation" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #0f172a; font-size: 18px; margin-top: 0; margin-bottom: 14px;">📦 Product-Oriented vs 🎯 Market-Oriented Business</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #2563eb; font-size: 15px;">📦 Product-Oriented Business:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Firms design and produce products first, then seek consumers to buy them. High risk of unsold inventory if market needs are miscalculated. <i>(e.g., custom tools, early computers).</i></p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15px;">🎯 Market-Oriented Business:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #166534; line-height: 1.5;">Firms carry out market research first to discover what consumers want, then engineer products to satisfy them. Low failure rate and higher customer retention. <i>(e.g., smartphones, cosmetics).</i></p>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. INTRODUCTION TO MARKET RESEARCH -->
    <div style="margin-bottom: 45px;">
        <div id="sec-market-research-intro" class="lecture-interactive-card" data-lecture-section="sec_market_research_intro" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🔍 2. INTRODUCTION TO MARKET RESEARCH</h2>
            <div style="background: #f5f3ff; border-left: 5px solid #7c3aed; padding: 14px 18px; border-radius: 8px; font-size: 15.5px; color: #4c1d95; line-height: 1.6;">
                <b>Market research</b> is the process of collecting, analysing and interpreting information about a product, consumers, and competitors.
            </div>
        </div>

        <div id="card-quant-qual-data" class="lecture-interactive-card" data-lecture-section="card_quant_qual_data" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #6d28d9; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🔢 Quantitative vs 💭 Qualitative Research Data</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🔢 Quantitative Data (Numerical):</b>
                    <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Numerical data represented in statistics, charts, and percentages. Answers: <i>'How many? How often?'</i></p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">💭 Qualitative Data (Opinions):</b>
                    <p style="margin: 6px 0 0 0; font-size: 13.5px; color: #475569; line-height: 1.5;">In-depth opinion, feeling, and judgment-based data. Answers: <i>'Why do customers prefer this brand?'</i></p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. PRIMARY MARKET RESEARCH -->
    <div style="margin-bottom: 45px;">
        <div id="sec-primary-research" class="lecture-interactive-card" data-lecture-section="sec_primary_research" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🥇 3. PRIMARY MARKET RESEARCH (Field Research)</h2>
            <div style="background: #fdf2f8; border-left: 5px solid #db2777; padding: 14px 18px; border-radius: 8px; font-size: 15px; color: #831843; line-height: 1.6;">
                The collection of <b>original, first-hand data</b> directly from respondents for a specific purpose.
            </div>
        </div>

        <div id="card-primary-methods" class="lecture-interactive-card" data-lecture-section="card_primary_methods" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #be185d; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🛠️ Four Primary Research Techniques</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #be185d; font-size: 14.5px;">📝 Questionnaires &amp; Surveys:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Gathers detailed quantitative and qualitative data. Online surveys are fast and cost-effective.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #be185d; font-size: 14.5px;">🎤 Interviews:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Interviewer explains questions and probes deeper; risks interviewer bias and high labor costs.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #be185d; font-size: 14.5px;">👥 Focus Groups:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Target customers test prototypes and discuss features, uncovering rich qualitative insights.</p>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px;">
                    <b style="color: #be185d; font-size: 14.5px;">👀 Observation:</b>
                    <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Counting customer footfall or audit stock; inexpensive and objective, but does not explain motivations.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. SECONDARY MARKET RESEARCH -->
    <div style="margin-bottom: 45px;">
        <div id="sec-secondary-research" class="lecture-interactive-card" data-lecture-section="sec_secondary_research" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🥈 4. SECONDARY MARKET RESEARCH (Desk Research)</h2>
            <div style="background: #fffbeb; border-left: 5px solid #f59e0b; padding: 14px 18px; border-radius: 8px; font-size: 15px; color: #92400e; line-height: 1.6;">
                The collection of information that has <b>already been gathered and published by other parties</b> (second-hand data).
            </div>
        </div>

        <div id="card-secondary-sources" class="lecture-interactive-card" data-lecture-section="card_secondary_sources" style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 12px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            <h3 style="color: #d97706; font-size: 18px; margin-top: 0; margin-bottom: 14px;">🏢 Internal vs 🌍 External Sources of Secondary Data</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🏢 Internal Sources (Already inside the business):</b>
                    <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                        <li>Past sales department reports, customer billing records, and pricing data.</li>
                        <li>Finance budgets, profit-and-loss accounts, and inventory stock turnover logs.</li>
                    </ul>
                </div>
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">🌍 External Sources (Outside the business):</b>
                    <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                        <li>Government national census and economic growth figures.</li>
                        <li>Trade association journals, business newspaper analysis, and market research agencies.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. ACCURACY & DATA PRESENTATION -->
    <div id="sec-accuracy-presentation" class="lecture-interactive-card" data-lecture-section="sec_accuracy_presentation" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📊 5. ACCURACY &amp; DATA PRESENTATION</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #0f766e; font-size: 15px;">Factors Influencing Accuracy:</b>
                <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                    <li><b>Sample size &amp; representativeness:</b> Small or unrepresentative samples distort conclusions.</li>
                    <li><b>Phrasing of questions:</b> Leading questions introduce researcher bias.</li>
                    <li><b>Age of data:</b> Rapid technological and economic shifts make old data obsolete.</li>
                </ul>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #0f766e; font-size: 15px;">Data Presentation Formats:</b>
                <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13px; color: #475569; line-height: 1.5;">
                    <li><b>Tally Tables:</b> Captures raw observations systematically.</li>
                    <li><b>Bar &amp; Pie Charts:</b> Compares total values and proportional segment shares.</li>
                    <li><b>Line Graphs:</b> Illustrates continuous trends and forecasts over time.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 6. SAMPLING METHODS -->
    <div id="sec-sampling-methods" class="lecture-interactive-card" data-lecture-section="sec_sampling_methods" style="margin-bottom: 45px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
        <h2 style="color: #0f172a; border-bottom: 3px solid #6366f1; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🎲 6. SAMPLING METHODS</h2>
        <p style="font-size: 14.5px; color: #475569; margin: 0 0 14px 0;">Businesses survey a representative subgroup (sample) rather than the whole target population:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #4338ca; font-size: 15px;">🎯 Random Sampling:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Every member of the target population has an equal chance of being picked. Unbiased, but may inadvertently pick non-users.</p>
            </div>
            <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                <b style="color: #4338ca; font-size: 15px;">📊 Quota Sampling:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #475569;">Interviewers select fixed quotas matching demographic percentages (e.g. 50 women aged 20-30). Highly representative of target buyers.</p>
            </div>
        </div>
    </div>

    <!-- 7. RECOMMEND AND JUSTIFY (CAMBRIDGE EXAM STRATEGY) -->
    <div id="sec-recommend-research" class="lecture-interactive-card" data-lecture-section="sec_recommend_research" style="margin-bottom: 45px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; padding: 24px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
        <h2 style="color: #1e3a8a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; font-size: 22px; margin-top: 0; display: inline-block;">
            🎯 7. HOW TO RECOMMEND &amp; JUSTIFY MARKET RESEARCH METHODS (Cambridge Exam Strategy)
        </h2>
        <p style="font-size: 15px; color: #1e40af; margin-bottom: 16px; line-height: 1.6;">
            Paper 1 &amp; 2 exam questions require choosing between primary field and secondary desk methods:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
            <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #3b82f6;">
                <b style="color: #1e40af; font-size: 15px;">Recommend Primary Research When:</b>
                <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13px; color: #334155; line-height: 1.5;">
                    <li>Launching an innovative, first-to-market product where no published data exists.</li>
                    <li>Hands-on consumer feedback on taste, touch, or packaging prototypes is required.</li>
                </ul>
            </div>
            <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #f59e0b;">
                <b style="color: #b45309; font-size: 15px;">Recommend Secondary Research When:</b>
                <ul style="margin: 6px 0 0 0; padding-left: 18px; font-size: 13px; color: #334155; line-height: 1.5;">
                    <li>The startup has a strictly limited budget and cannot afford professional field surveyors.</li>
                    <li>Urgent decisions are required immediately using published market data archives.</li>
                </ul>
            </div>
        </div>
    </div>

</div>"""
    return html

# ==============================================================================
# 3. GENERATE NEW HTML FOR PAGE 2 (BILINGUAL)
# ==============================================================================
def build_page_2_html(original_p2):
    header_banner = """<div style="margin-bottom: 35px; padding: 22px 26px; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border-radius: 14px; border: 1px solid #e2e8f0; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
        <div>
            <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Song Ngữ Anh - Việt</span>
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">3.2 Market Research (Nghiên cứu Thị trường)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 3.2 Audio and HTML ===")
    
    audio_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'business', CODE)
    os.makedirs(audio_dir, exist_ok=True)

    # 1. Generate audio files and write manifest.json
    print(f"\nGenerating {len(segments)} audio segments...")
    manifest = await process_lecture_audio(CODE, LID, COURSE_TITLE, TITLE, segments, major_sections, subject='business')
    
    # 2. Build Page 1 HTML
    p1_html = build_page_1_html()
    diff1 = len(p1_html.split('<div')) - len(p1_html.split('</div>'))
    print(f"\nPage 1 HTML div diff: {diff1}")
    if diff1 != 0:
        raise ValueError(f"Page 1 has div balance error: {diff1}")
        
    # 3. Build Page 2 HTML
    with open('scripts/raw_pages/3_2_p2.html', 'r', encoding='utf-8') as f:
        orig_p2 = f.read()
    p2_html = build_page_2_html(orig_p2)
    diff2 = len(p2_html.split('<div')) - len(p2_html.split('</div>'))
    print(f"Page 2 HTML div diff: {diff2}")
    if diff2 != 0:
        raise ValueError(f"Page 2 has div balance error: {diff2}")
        
    # 4. Update Supabase
    print("\nUpdating Supabase page 1...")
    res1 = sb.table('lecture_pages').update({'content_html': p1_html}).eq('lecture_id', LID).eq('page_number', 1).execute()
    print(f"Page 1 updated: {len(res1.data)} rows.")
    
    print("Updating Supabase page 2...")
    res2 = sb.table('lecture_pages').update({'content_html': p2_html}).eq('lecture_id', LID).eq('page_number', 2).execute()
    print(f"Page 2 updated: {len(res2.data)} rows.")
    
    print("\n✅ REBUILD 3.2 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
