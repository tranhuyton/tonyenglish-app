import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 4.3 ID
LID = '8f0fd09a-d6e6-438f-a2ab-ddc1447e0b00'
CODE = '4_3'
TITLE = '4.3. Quality management'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 8 AUDIO SEGMENTS FOR LESSON 4.3
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.3: Quản lý Chất lượng",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.3: Quality Management. In this lesson, we define what quality means for goods and services, evaluate the commercial significance of quality standards, and contrast Quality Control, Quality Assurance, and Total Quality Management.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.3: Quản lý Chất lượng. Trong bài học này, chúng ta sẽ định nghĩa chất lượng trong hàng hóa và dịch vụ, đánh giá tầm quan trọng thương mại của các tiêu chuẩn chất lượng, và so sánh Kiểm soát chất lượng (QC), Đảm bảo chất lượng (QA) cùng Quản lý chất lượng toàn diện (TQM)."
    },
    {
        "id": "sec_what_is_quality",
        "title": "1. Khái niệm Chất lượng & Tiêu chuẩn",
        "selector": "#sec-what-is-quality",
        "en": "Section 1 defines quality as producing goods or services that meet or exceed customer expectations, free from faults or defects. Establishing consistent quality builds enduring brand loyalty, protects reputation, enables premium pricing, and prevents costly customer returns.",
        "vi": "Mục một định nghĩa chất lượng là việc sản xuất ra hàng hóa hoặc dịch vụ đáp ứng hoặc vượt trên kỳ vọng của khách hàng, hoàn toàn không có lỗi hỏng. Duy trì chất lượng ổn định giúp xây dựng lòng trung thành thương hiệu, bảo vệ uy tín, cho phép định giá cao và ngăn chặn chi phí đổi trả hàng tốn kém."
    },
    {
        "id": "card_importance_quality",
        "title": "🌟 Tầm quan trọng của Chất lượng & Chứng nhận ISO",
        "selector": "#card-importance-quality",
        "en": "Consistent quality creates sustainable brand equity and commands premium prices, whereas poor quality triggers customer defection, warranty rework expenses, and viral negative social reviews. Consumers verify quality through international benchmark badges such as the ISO 9001 standard.",
        "vi": "Chất lượng ổn định tạo nên giá trị thương hiệu bền vững và cho phép bán giá cao, trong khi chất lượng kém dẫn đến mất khách hàng, chi phí sửa chữa bảo hành tốn kém và những đánh giá tiêu cực trên mạng xã hội. Người tiêu dùng xác minh chất lượng thông qua các chứng nhận tiêu chuẩn quốc tế như ISO 9001."
    },
    {
        "id": "sec_quality_methods",
        "title": "2. Các Phương pháp Quản lý Chất lượng",
        "selector": "#sec-quality-methods",
        "en": "Section 2 introduces the three operational frameworks for managing quality: Quality Control at the end of the line, Quality Assurance embedded across all production stages, and Total Quality Management engaging every employee.",
        "vi": "Mục hai giới thiệu ba phương pháp vận hành quản lý chất lượng: Kiểm soát chất lượng (QC) kiểm tra ở cuối dây chuyền, Đảm bảo chất lượng (QA) lồng ghép ở mọi công đoạn sản xuất, và Quản lý chất lượng toàn diện (TQM) huy động sự tham gia của mọi nhân viên."
    },
    {
        "id": "card_qc",
        "title": "1. Kiểm soát Chất lượng (Quality Control - QC)",
        "selector": "#card-qc",
        "en": "Quality Control inspects finished goods at the end of production. While QC requires minimal training and catches defects before dispatch, it is purely reactive, fails to isolate root causes, and incurs high scrap costs when completed goods must be discarded.",
        "vi": "Kiểm soát chất lượng (QC) kiểm tra thành phẩm ở khâu cuối cùng của quá trình sản xuất. Mặc dù QC ít đòi hỏi đào tạo phức tạp và chặn được hàng lỗi trước khi giao, đây là phương pháp mang tính đối phó thụ động, không tìm ra nguyên nhân gốc rễ và gây lãng phí chi phí phế phẩm lớn khi phải vứt bỏ cả sản phẩm hoàn chỉnh."
    },
    {
        "id": "card_qa",
        "title": "2. Đảm bảo Chất lượng (Quality Assurance - QA)",
        "selector": "#card-qa",
        "en": "Quality Assurance establishes rigorous standards checked at every manufacturing stage. QA is proactive, catching defects immediately to prevent scrap, but demands extensive worker compliance and setup costs across each operational process.",
        "vi": "Đảm bảo chất lượng (QA) thiết lập các tiêu chuẩn nghiêm ngặt và kiểm tra tại từng công đoạn sản xuất. QA mang tính chủ động, phát hiện lỗi ngay tức thì để tránh lãng phí, nhưng đòi hỏi sự tuân thủ kỷ luật cao của công nhân và chi phí đầu tư ban đầu cho từng quy trình vận hành."
    },
    {
        "id": "card_tqm",
        "title": "3. Quản lý Chất lượng Toàn diện (Total Quality Management - TQM)",
        "selector": "#card-tqm",
        "en": "Total Quality Management instills a company-wide culture of continuous improvement aiming for zero defects. In TQM, the next worker along the line is treated as an internal customer, eliminating wastage through quality circles, though requiring comprehensive training investments.",
        "vi": "Quản trị chất lượng toàn diện (TQM) xây dựng văn hóa cải tiến liên tục trong toàn thể công ty nhằm hướng tới mục tiêu 0% phế phẩm. Trong TQM, người công nhân ở khâu tiếp theo được đối xử như một khách hàng nội bộ, loại bỏ lãng phí thông qua các nhóm chất lượng, dù đòi hỏi chi phí đào tạo nhân sự rất lớn."
    },
    {
        "id": "sec_recommend_quality",
        "title": "3. Chiến lược làm bài thi Cambridge: Ma trận So sánh & Đề xuất QC vs QA vs TQM",
        "selector": "#sec-recommend-quality",
        "en": "Section 3 synthesizes Cambridge evaluation strategy. Recommend QA or TQM when product failure risks life safety or catastrophic brand damage, such as automotive brakes or aerospace components. Recommend QC only for low-cost, simple items where comprehensive QA training costs exceed occasional scrap expenses.",
        "vi": "Mục ba tổng hợp chiến lược làm bài thi Cambridge. Hãy đề xuất QA hoặc TQM khi lỗi sản phẩm đe dọa đến an toàn tính mạng hoặc hủy hoại uy tín thương hiệu nghiêm trọng, như hệ thống phanh ô tô hay linh kiện hàng không. Chỉ khuyến nghị QC cho các mặt hàng đơn giản, giá trị thấp nơi chi phí đào tạo QA vượt quá chi phí loại bỏ vài sản phẩm lỗi."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_what_is_quality": {"start": 1, "end": 2},
    "sec_quality_methods": {"start": 3, "end": 6},
    "sec_recommend_quality": {"start": 7, "end": 7}
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
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 4</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.3 Quality Management (Quản lý Chất lượng)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. WHAT IS QUALITY? -->
    <div style="margin-bottom: 50px;">
        <div id="sec-what-is-quality" class="lecture-interactive-card" data-lecture-section="sec_what_is_quality" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">✨ 1. WHAT IS QUALITY?</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                <b>Quality</b> means producing a good or service which <b>meets customer expectations</b>. The products should be free of faults or defects.
            </div>
        </div>

        <!-- SUB-CARD: IMPORTANCE OF QUALITY -->
        <div id="card-importance-quality" class="lecture-interactive-card" data-lecture-section="card_importance_quality" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">🌟 The Commercial Value of Quality &amp; ISO Certification</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #15803d; font-size: 16px; margin: 0 0 8px 0;">🌟 Why is Quality important?</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 13px; line-height: 1.6;">
                        <li>Establishes a strong brand image in the marketplace.</li>
                        <li>Builds brand loyalty and repeat purchase habits.</li>
                        <li>Enables the business to charge premium pricing.</li>
                        <li>Increases sales revenue and attracts new market segments.</li>
                    </ul>
                </div>

                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #b91c1c; font-size: 16px; margin: 0 0 8px 0;">⚠️ What happens if there is NO Quality?</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 13px; line-height: 1.6;">
                        <li>Customers permanently switch to competing brands.</li>
                        <li>Heavy scrap and warranty replacement costs accumulate.</li>
                        <li>Negative word-of-mouth damages long-term reputation and sales.</li>
                    </ul>
                </div>
            </div>

            <div style="background: #fffbeb; border: 1px dashed #f59e0b; padding: 14px 18px; border-radius: 8px;">
                <b style="color: #92400e; font-size: 14px;">🔍 Quality Assurance Badges:</b>
                <p style="margin: 4px 0 0 0; font-size: 13px; color: #92400e; line-height: 1.5;">
                    Consumers look for trusted quality marks like <b>ISO</b> (International Organization for Standardization, such as ISO 9001). For service sectors, independent reviews and brand certifications signal dependable service delivery.
                </p>
            </div>
        </div>
    </div>

    <!-- 2. METHODS OF QUALITY MANAGEMENT -->
    <div style="margin-bottom: 50px;">
        <div id="sec-quality-methods" class="lecture-interactive-card" data-lecture-section="sec_quality_methods" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🛠️ 2. METHODS OF QUALITY MANAGEMENT</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                There are three main operational methodologies a business implements to manage and assure quality standards:
            </p>
        </div>

        <!-- SUB-CARD: QC -->
        <div id="card-qc" class="lecture-interactive-card" data-lecture-section="card_qc" style="margin-bottom: 20px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="background: #f8fafc; padding: 18px 22px; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #6d28d9; font-size: 18px; font-weight: 700;">1. Quality Control (QC)</h3>
                    <p style="margin: 3px 0 0 0; font-size: 13.5px; color: #475569;">Checking for quality <b>at the end</b> of the production process.</p>
                </div>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>
            <div style="display: flex; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 250px; padding: 18px 22px; border-right: 1px solid #e2e8f0; background: #f0fdf4;">
                    <h4 style="color: #15803d; margin: 0 0 6px 0; font-size: 14.5px;">✅ Advantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12.5px; line-height: 1.5;">
                        <li>Eliminates faulty items before customers receive them.</li>
                        <li>Inspectors require basic training for end checks.</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; padding: 18px 22px; background: #fef2f2;">
                    <h4 style="color: #b91c1c; margin: 0 0 6px 0; font-size: 14.5px;">❌ Disadvantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12.5px; line-height: 1.5;">
                        <li>Expensive dedicated inspection staff.</li>
                        <li>Catches errors but <b>does not identify root causes</b> during assembly.</li>
                        <li>Scrapping finished products creates substantial financial waste.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: QA -->
        <div id="card-qa" class="lecture-interactive-card" data-lecture-section="card_qa" style="margin-bottom: 20px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="background: #f8fafc; padding: 18px 22px; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #2563eb; font-size: 18px; font-weight: 700;">2. Quality Assurance (QA)</h3>
                    <p style="margin: 3px 0 0 0; font-size: 13.5px; color: #475569;">Setting standards and checking quality <b>throughout</b> the production process.</p>
                </div>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #2563eb; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <div style="display: flex; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 250px; padding: 18px 22px; border-right: 1px solid #e2e8f0; background: #f0fdf4;">
                    <h4 style="color: #15803d; margin: 0 0 6px 0; font-size: 14.5px;">✅ Advantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12.5px; line-height: 1.5;">
                        <li>Proactively prevents errors before they reach assembly milestones.</li>
                        <li>Root causes identified and rectified early, slashing scrap costs.</li>
                        <li>Fosters worker pride and personal quality responsibility.</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; padding: 18px 22px; background: #fef2f2;">
                    <h4 style="color: #b91c1c; margin: 0 0 6px 0; font-size: 14.5px;">❌ Disadvantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12.5px; line-height: 1.5;">
                        <li>Substantial initial setup expenses across every department.</li>
                        <li>Relies heavily on consistent employee adherence to rigorous standards.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: TQM -->
        <div id="card-tqm" class="lecture-interactive-card" data-lecture-section="card_tqm" style="background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="background: #f8fafc; padding: 18px 22px; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #d97706; font-size: 18px; font-weight: 700;">3. Total Quality Management (TQM)</h3>
                    <p style="margin: 3px 0 0 0; font-size: 13.5px; color: #475569;">The <b>continuous improvement</b> of products and processes targeting zero defects.</p>
                </div>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>
            <div style="padding: 14px 22px; background: #fffbeb; font-size: 13px; color: #92400e; border-bottom: 1px solid #fde68a;">
                <b>💡 Core Principle:</b> In TQM, every worker treats the next person on the line as an <b>internal customer</b>. Quality circles meet continuously to eradicate errors before passing items forward.
            </div>
            <div style="display: flex; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 250px; padding: 18px 22px; border-right: 1px solid #e2e8f0; background: #f0fdf4;">
                    <h4 style="color: #15803d; margin: 0 0 6px 0; font-size: 14.5px;">✅ Advantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12.5px; line-height: 1.5;">
                        <li>Quality becomes ingrained in the corporate culture.</li>
                        <li>Eliminates customer complaints, driving stellar brand reputation.</li>
                        <li>Virtually eradicates waste and optimizes production efficiency.</li>
                    </ul>
                </div>
                <div style="flex: 1; min-width: 250px; padding: 18px 22px; background: #fef2f2;">
                    <h4 style="color: #b91c1c; margin: 0 0 6px 0; font-size: 14.5px;">❌ Disadvantages</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12.5px; line-height: 1.5;">
                        <li>Extremely expensive to train every single employee across the company.</li>
                        <li>Fails completely if worker morale or commitment is weak.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. CAMBRIDGE EXAM MATRIX -->
    <div style="margin-bottom: 50px;">
        <div id="sec-recommend-quality" class="lecture-interactive-card" data-lecture-section="sec_recommend_quality" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 3. HOW TO RECOMMEND QC VS QA VS TQM (Cambridge Exam Matrix)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Candidates often face evaluation questions: <i>"Recommend whether this business should replace Quality Control with Quality Assurance."</i>
            </p>

            <div style="overflow-x: auto; background: #ffffff; border-radius: 10px; border: 1px solid #bfdbfe; margin-bottom: 18px;">
                <table style="width: 100%; border-collapse: collapse; min-width: 600px; font-size: 13px;">
                    <thead>
                        <tr style="background: #dbeafe; border-bottom: 2px solid #bfdbfe; color: #1e3a8a;">
                            <th style="padding: 10px 14px; text-align: left;">Feature</th>
                            <th style="padding: 10px 14px; text-align: left;">Quality Control (QC)</th>
                            <th style="padding: 10px 14px; text-align: left;">Quality Assurance (QA)</th>
                            <th style="padding: 10px 14px; text-align: left;">Total Quality Management (TQM)</th>
                        </tr>
                    </thead>
                    <tbody style="color: #334155;">
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold;">When Checked?</td>
                            <td style="padding: 10px 14px;">At the <b>end</b> of production.</td>
                            <td style="padding: 10px 14px;">At <b>every stage</b> of production.</td>
                            <td style="padding: 10px 14px;">Continuous culture in every department.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                            <td style="padding: 10px 14px; font-weight: bold;">Approach</td>
                            <td style="padding: 10px 14px; color: #dc2626;">Reactive (catches errors).</td>
                            <td style="padding: 10px 14px; color: #166534;">Proactive (prevents errors).</td>
                            <td style="padding: 10px 14px; color: #2563eb;">Holistic (zero defects philosophy).</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 14px; font-weight: bold;">Scrap / Waste Cost</td>
                            <td style="padding: 10px 14px; color: #dc2626;">High (whole items discarded).</td>
                            <td style="padding: 10px 14px; color: #166534;">Low (errors caught early).</td>
                            <td style="padding: 10px 14px; color: #166534;">Lowest (waste eliminated).</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
                <b style="color: #1e40af; font-size: 14px;">💡 Recommendation Justification for Exams:</b>
                <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                    Recommend <b>Quality Assurance / TQM</b> when product faults would cause catastrophic safety issues or severe brand damage (e.g. car brakes, aeroplane parts, medical equipment). Recommend <b>Quality Control</b> only for low-cost, simple items where training all workers in QA would exceed the cost of scrapping occasional defective units.
                </p>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.3 Quality Management (Quản lý Chất lượng)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 4.3 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/4_3_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 4.3 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
