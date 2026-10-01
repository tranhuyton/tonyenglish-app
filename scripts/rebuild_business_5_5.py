import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 5.5 ID
LID = 'd7564fe9-d338-4abc-acf3-affd8cca23fa'
CODE = '5_5'
TITLE = '5.5. Analysis of accounts'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 9 AUDIO SEGMENTS FOR LESSON 5.5
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 5.5: Phân tích Báo cáo Tài chính qua Chỉ số",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 5.5: Analysis of Accounts. In this analytical capstone of Topic 5, we calculate and interpret profitability ratios—Gross Profit Margin, Net Profit Margin, and Return on Capital Employed—and liquidity ratios—Current Ratio and Acid Test Ratio—to evaluate company health.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 5.5: Phân tích Báo cáo Tài chính. Trong bài tổng kết Chủ đề năm, chúng ta sẽ tính toán và phân tích các chỉ số sinh lời: Biên lợi nhuận gộp, Biên lợi nhuận ròng, Tỷ suất sinh lời trên vốn (ROCE) cùng các chỉ số thanh toán: Tỷ số hiện hành và Tỷ số thanh toán nhanh (Acid Test)."
    },
    {
        "id": "sec_profitability_liquidity",
        "title": "1. Khái niệm Khả năng Sinh lời và Tính Thanh khoản",
        "selector": "#sec-profitability-liquidity",
        "en": "Section 1 contrasts profitability against liquidity. Profitability measures financial efficiency in generating returns relative to sales or capital invested. Liquidity measures the ability of a business to settle immediate short-term debts without selling non-current factory assets.",
        "vi": "Mục một đối chiếu khả năng sinh lời với tính thanh khoản. Khả năng sinh lời đo lường hiệu quả tạo ra lợi nhuận so với doanh thu hoặc đồng vốn đầu tư. Tính thanh khoản đo lường năng lực của doanh nghiệp trong việc thanh toán các khoản nợ ngắn hạn mà không phải bán tháo tài sản nhà xưởng dài hạn."
    },
    {
        "id": "sec_profitability_ratios",
        "title": "2. Ba Chỉ số Khả năng Sinh lời Chuẩn Cambridge",
        "selector": "#sec-profitability-ratios",
        "en": "Section 2 details three vital profitability metrics: Gross Profit Margin equals Gross Profit divided by Revenue multiplied by 100. Profit Margin for the year equals Profit for the year divided by Revenue times 100. Return on Capital Employed (ROCE) equals Operating Profit divided by Capital Employed times 100, measuring how efficiently capital produces earnings.",
        "vi": "Mục hai trình bày ba chỉ số sinh lời chuẩn Cambridge: Biên lợi nhuận gộp bằng Lợi nhuận gộp chia Doanh thu nhân 100. Biên lợi nhuận ròng bằng Lợi nhuận ròng chia Doanh thu nhân 100. Tỷ suất sinh lời trên vốn (ROCE) bằng Lợi nhuận thuần từ hoạt động kinh doanh chia cho Vốn hoạt động nhân 100, đo lường hiệu quả đồng vốn bỏ ra."
    },
    {
        "id": "card_gpm_npm",
        "title": "📊 Biên Lợi Nhuận Gộp (GPM) & Biên Lợi Nhuận Ròng (NPM)",
        "selector": "#card-gpm-npm",
        "en": "Gross Profit Margin reveals trading markup over direct production costs: improve it by raising selling prices or finding cheaper component suppliers. Net Profit Margin shows operational efficiency after overhead deductions: improve it by trimming administrative staff and cutting high premises rent.",
        "vi": "Biên lợi nhuận gộp (GPM) phản ánh tỷ lệ lãi gộp trên giá vốn trực tiếp: cải thiện bằng cách tăng giá bán hoặc đàm phán giảm giá nguyên vật liệu đầu vào. Biên lợi nhuận ròng (NPM) cho thấy hiệu quả vận hành sau khi trừ chi phí gián tiếp: cải thiện bằng cách tinh giản bộ máy hành chính và chuyển văn phòng sang nơi có tiền thuê rẻ hơn."
    },
    {
        "id": "card_roce",
        "title": "🎯 Tỷ Suất Sinh Lời Trên Vốn (ROCE - Return on Capital Employed)",
        "selector": "#card-roce",
        "en": "ROCE divides Operating Profit by Capital Employed multiplied by 100. It measures the fundamental productivity of every dollar invested by owners and long-term debenture lenders. In Cambridge exams, always compare ROCE against prevailing commercial bank deposit interest rates.",
        "vi": "ROCE bằng Lợi nhuận thuần chia cho Vốn hoạt động (Vốn chủ sở hữu cộng Nợ dài hạn) nhân 100. Chỉ số này đo lường năng suất sinh lời thực tế của từng đồng vốn mà cổ đông và chủ nợ dài hạn đã rót vào công ty. Trong bài thi Cambridge, luôn so sánh ROCE với lãi suất tiền gửi ngân hàng hiện hành để đánh giá hiệu quả."
    },
    {
        "id": "sec_liquidity_ratios",
        "title": "3. Hai Chỉ số Khả năng Thanh toán (Liquidity Ratios)",
        "selector": "#sec-liquidity-ratios",
        "en": "Section 3 calculates liquidity: The Current Ratio equals Current Assets divided by Current Liabilities, with 1.5 to 2.0 considered healthy. The Acid Test Ratio excludes illiquid inventory: Current Assets minus Inventory divided by Current Liabilities. An Acid Test below 1.0 indicates severe working capital vulnerability.",
        "vi": "Mục ba tính toán khả năng thanh toán: Tỷ số hiện hành bằng Tài sản ngắn hạn chia Nợ ngắn hạn, mức lý tưởng là từ 1,5 đến 2,0. Tỷ số thanh toán nhanh (Acid Test) loại bỏ hàng tồn kho khó bán: bằng Tài sản ngắn hạn trừ Hàng tồn kho, tất cả chia cho Nợ ngắn hạn. Tỷ số Acid Test dưới 1,0 cảnh báo nguy cơ cạn kiệt thanh khoản nghiêm trọng."
    },
    {
        "id": "card_current_acid_ratios",
        "title": "💧 Tỷ Số Hiện Hành (Current Ratio) & Tỷ Số Thanh Toán Nhanh (Acid Test Ratio)",
        "selector": "#card-current-acid-ratios",
        "en": "Current Ratio compares all short-term resources against short-term debts, ideal at 1.5 to 2.0. Acid Test Ratio removes unsold stock because inventory cannot be liquidated instantly in an emergency. If Acid Test falls below 1.0, the business lacks liquid cash to cover immediate creditor demands.",
        "vi": "Tỷ số hiện hành so sánh toàn bộ tài sản ngắn hạn với nợ ngắn hạn, mức chuẩn là 1,5 đến 2,0. Tỷ số Acid Test loại trừ hàng tồn kho vì không thể bán tháo lấy tiền ngay trong tình huống khẩn cấp. Nếu Acid Test tụt xuống dưới 1,0, doanh nghiệp không có đủ tiền mặt thanh khoản để trang trải các khoản nợ nhà cung cấp đến hạn."
    },
    {
        "id": "sec_stakeholders_accounts",
        "title": "4. Cách các Bên liên quan Sử dụng Báo cáo Tài chính",
        "selector": "#sec-stakeholders-accounts",
        "en": "Section 4 investigates how stakeholders analyze accounts: Shareholders assess dividend yields and capital growth; Banks evaluate debt service coverage before approving loans; Suppliers audit liquidity before offering credit; and Employees evaluate job security and wage negotiation leverage.",
        "vi": "Mục bốn phân tích cách các bên liên quan đọc báo cáo tài chính: Cổ đông đánh giá tỷ suất cổ tức và tăng trưởng vốn; Ngân hàng kiểm tra khả năng trả nợ trước khi duyệt vay; Nhà cung cấp kiểm tra thanh khoản trước khi cho nợ tiền; và Người lao động đánh giá sự ổn định việc làm để thương lượng tăng lương."
    },
    {
        "id": "sec_evaluate_ratios",
        "title": "5. Hạn chế của Phân tích Báo cáo và Chiến lược thi Cambridge",
        "selector": "#sec-evaluate-ratios",
        "en": "Section 5 presents ratio limitations: accounts record historical data rather than future performance, inflation distorts asset values, creative accounting masks problems, and ratios ignore qualitative factors such as staff morale and customer loyalty.",
        "vi": "Mục năm chỉ ra các giới hạn của chỉ số tài chính: báo cáo chỉ phản ánh số liệu lịch sử trong quá khứ, lạm phát làm sai lệch giá trị tài sản, thủ thuật kế toán có thể che giấu rủi ro và các chỉ số hoàn toàn bỏ qua các yếu tố định tính quan trọng như tinh thần nhân viên và lòng trung thành của khách hàng.",
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_profitability_liquidity": {"start": 1, "end": 1},
    "sec_profitability_ratios": {"start": 2, "end": 4},
    "sec_liquidity_ratios": {"start": 5, "end": 6},
    "sec_stakeholders_accounts": {"start": 7, "end": 7},
    "sec_evaluate_ratios": {"start": 8, "end": 8}
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
                <span style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.8px;">Cambridge IGCSE Business Studies (0450) • Unit 5</span>
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.5 Analysis of Accounts (Phân tích Báo cáo Tài chính)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. PROFITABILITY & LIQUIDITY -->
    <div style="margin-bottom: 50px;">
        <div id="sec-profitability-liquidity" class="lecture-interactive-card" data-lecture-section="sec_profitability_liquidity" style="padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">⚖️ 1. PROFITABILITY &amp; LIQUIDITY</h2>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h3 style="margin: 0 0 8px 0; color: #15803d; font-size: 16px; font-weight: 700;">📈 Profitability (Khả năng sinh lời)</h3>
                    <p style="margin: 0; font-size: 13px; color: #166534; line-height: 1.5;">
                        Measures financial efficiency: how effectively revenue or invested capital generates profits. Expressed as a percentage (%). Used by shareholders to compare investment returns.
                    </p>
                </div>

                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 16px;">
                    <h3 style="margin: 0 0 8px 0; color: #1d4ed8; font-size: 16px; font-weight: 700;">💧 Liquidity (Khả năng thanh toán)</h3>
                    <p style="margin: 0; font-size: 13px; color: #1e40af; line-height: 1.5;">
                        Measures the ability to settle short-term debts (bills, wages, suppliers) promptly. An illiquid business faces legal shutdown even if balance sheet profits are high.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. PROFITABILITY RATIOS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-profitability-ratios" class="lecture-interactive-card" data-lecture-section="sec_profitability_ratios" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📊 2. PROFITABILITY RATIOS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Three key profitability ratios assess trading margins and capital productivity: Gross Profit Margin, Net Profit Margin, and Return on Capital Employed (ROCE).
            </p>
        </div>

        <!-- SUB-CARD: GPM & NPM -->
        <div id="card-gpm-npm" class="lecture-interactive-card" data-lecture-section="card_gpm_npm" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #6d28d9; font-weight: 700;">📊 Gross Profit Margin vs Net Profit Margin</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">1. Gross Profit Margin (GPM)</b>
                    <div style="background: #ffffff; border: 1px dashed #cbd5e1; padding: 8px 12px; border-radius: 6px; margin: 8px 0; font-weight: bold; font-size: 13.5px; color: #2563eb; text-align: center;">
                        GPM = (Gross Profit / Sales Revenue) × 100%
                    </div>
                    <p style="margin: 0; font-size: 12.5px; color: #475569; line-height: 1.5;">
                        Shows gross markup on goods sold. <b>How to improve:</b> Increase product prices or negotiate cheaper raw material purchase contracts.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                    <b style="color: #0f172a; font-size: 15px;">2. Net Profit Margin (NPM)</b>
                    <div style="background: #ffffff; border: 1px dashed #cbd5e1; padding: 8px 12px; border-radius: 6px; margin: 8px 0; font-weight: bold; font-size: 13.5px; color: #059669; text-align: center;">
                        NPM = (Profit for Year / Sales Revenue) × 100%
                    </div>
                    <p style="margin: 0; font-size: 12.5px; color: #475569; line-height: 1.5;">
                        Shows bottom-line percentage after all overheads. <b>How to improve:</b> Reduce administrative staff, relocate to cheaper rent premises, or cut utility waste.
                    </p>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: ROCE -->
        <div id="card-roce" class="lecture-interactive-card" data-lecture-section="card_roce" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">🎯 3. Return on Capital Employed (ROCE)</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="background: #fff7ed; border: 1px dashed #f97316; padding: 12px 18px; border-radius: 8px; font-weight: bold; font-size: 15px; color: #c2410c; text-align: center; margin-bottom: 14px;">
                ROCE = (Operating Profit / Capital Employed) × 100%
            </div>
            <p style="margin: 0 0 10px 0; font-size: 13.5px; color: #475569; line-height: 1.5;">
                Measures how much operating profit is generated for every $100 of capital employed (Shareholders' funds + Non-current liabilities).
            </p>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px 14px; border-radius: 4px; font-size: 13px; color: #1e40af;">
                <b>💡 Exam Benchmark:</b> Always compare ROCE to bank savings interest rates. If a bank pays 6% guaranteed interest and company ROCE is only 4%, the investment is severely underperforming!
            </div>
        </div>
    </div>

    <!-- 3. LIQUIDITY RATIOS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-liquidity-ratios" class="lecture-interactive-card" data-lecture-section="sec_liquidity_ratios" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #10b981; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💧 3. LIQUIDITY RATIOS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Liquidity ratios evaluate whether a firm holds sufficient liquid assets to settle short-term creditor claims without forced liquidation.
            </p>
        </div>

        <!-- SUB-CARD: CURRENT & ACID TEST RATIOS -->
        <div id="card-current-acid-ratios" class="lecture-interactive-card" data-lecture-section="card_current_acid_ratios" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #059669; font-weight: 700;">💧 Current Ratio vs Acid Test Ratio</h3>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15px;">1. Current Ratio (CR)</b>
                    <div style="background: #ffffff; border: 1px dashed #bbf7d0; padding: 8px 12px; border-radius: 6px; margin: 8px 0; font-weight: bold; font-size: 13.5px; color: #15803d; text-align: center;">
                        Current Ratio = Current Assets / Current Liabilities
                    </div>
                    <p style="margin: 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Expressed as <b>X : 1</b>. Benchmark: <b>1.5 : 1 to 2.0 : 1</b>. Below 1:1 indicates negative working capital and insolvency danger.
                    </p>
                </div>

                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15px;">2. Acid Test Ratio (Quick Ratio)</b>
                    <div style="background: #ffffff; border: 1px dashed #bbf7d0; padding: 8px 12px; border-radius: 6px; margin: 8px 0; font-weight: bold; font-size: 13.5px; color: #15803d; text-align: center;">
                        Acid Test = (Current Assets - Inventory) / Current Liabilities
                    </div>
                    <p style="margin: 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Excludes inventory because stock cannot be converted into cash instantly. Benchmark: <b>1.0 : 1</b>.
                    </p>
                </div>
            </div>

            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #475569;">
                <b>🔧 How to Improve Liquidity:</b> Reduce customer trade credit terms to collect cash faster; negotiate longer supplier payment windows (60–90 days); sell off surplus stock for instant cash.
            </div>
        </div>
    </div>

    <!-- 4. HOW STAKEHOLDERS USE ACCOUNTS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-stakeholders-accounts" class="lecture-interactive-card" data-lecture-section="sec_stakeholders_accounts" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <h2 style="color: #be185d; margin: 0; font-size: 22px; font-weight: 700;">👥 4. HOW STAKEHOLDERS USE ACCOUNTS</h2>
                <span style="font-size: 11px; font-weight: 700; background: #fff1f2; color: #be185d; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14px; color: #475569; margin: 0 0 16px 0;">
                Limited company accounts are audited and published annually for distinct user groups:
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b style="color: #9d174d;">Shareholders / Investors:</b> Audit ROCE and dividend payout ratios to assess management performance and capital growth.
                </div>
                <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b style="color: #9d174d;">Bank Lenders:</b> Audit liquidity ratios (Acid Test) and gearing to judge insolvency risk before extending loans.
                </div>
                <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b style="color: #9d174d;">Suppliers:</b> Check working capital to decide whether to provide 30-to-60 day trade credit.
                </div>
                <div style="background: #fdf2f8; border: 1px solid #fbcfe8; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b style="color: #9d174d;">Employees &amp; Trade Unions:</b> Review operating profits to argue for annual wage increases and evaluate job security.
                </div>
            </div>
        </div>
    </div>

    <!-- 5. CAMBRIDGE EXAM EVALUATION & RATIO LIMITATIONS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-evaluate-ratios" class="lecture-interactive-card" data-lecture-section="sec_evaluate_ratios" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 5. EVALUATING RATIOS &amp; LIMITATIONS (Cambridge Exam Matrix)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Cambridge evaluation questions ask: <i>"Evaluate whether financial ratio analysis provides an accurate assessment of this company's performance."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #ffffff; padding: 14px 16px; border-radius: 8px; border-left: 4px solid #ef4444; font-size: 13px; color: #334155;">
                    <b>1. Historical Data Only:</b> Accounts report past events; they do not guarantee future sales or profits.
                </div>
                <div style="background: #ffffff; padding: 14px 16px; border-radius: 8px; border-left: 4px solid #ef4444; font-size: 13px; color: #334155;">
                    <b>2. Inflation Distortion:</b> Inflation inflates recent asset values, distorting comparisons across different years.
                </div>
                <div style="background: #ffffff; padding: 14px 16px; border-radius: 8px; border-left: 4px solid #ef4444; font-size: 13px; color: #334155;">
                    <b>3. Window Dressing:</b> Companies use legal accounting tricks to make year-end liquidity look healthier than normal.
                </div>
                <div style="background: #ffffff; padding: 14px 16px; border-radius: 8px; border-left: 4px solid #ef4444; font-size: 13px; color: #334155;">
                    <b>4. Ignores Qualitative Factors:</b> Ratios completely omit staff motivation, customer satisfaction, and ethical reputation.
                </div>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.5 Analysis of Accounts (Phân tích Báo cáo Tài chính)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 5.5 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/5_5_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 5.5 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
