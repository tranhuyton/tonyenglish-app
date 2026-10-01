import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 5.4 ID
LID = '5421db93-9d7b-4241-b362-171974092a30'
CODE = '5_4'
TITLE = '5.4. Statement of financial position'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 7 AUDIO SEGMENTS FOR LESSON 5.4
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 5.4: Bảng Cân đối Kế toán (Statement of Financial Position)",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 5.4: Statement of Financial Position. In this chapter, formerly known as the Balance Sheet, we examine how a business records its assets, liabilities, and shareholder equity on a specific calendar date.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 5.4: Bảng Cân đối Kế toán. Trong bài học này, chúng ta sẽ khảo sát cách doanh nghiệp ghi nhận tài sản, nợ phải trả và vốn chủ sở hữu tại một thời điểm nhất định."
    },
    {
        "id": "sec_balance_sheet",
        "title": "1. Bản chất của Bảng Cân đối Kế toán",
        "selector": "#sec-balance-sheet",
        "en": "Section 1 defines the Statement of Financial Position as a financial snapshot recording the net worth of an enterprise. It balances Total Assets perfectly against Total Liabilities plus Shareholders' Equity.",
        "vi": "Mục một định nghĩa Bảng cân đối kế toán là bức tranh chụp nhanh tình hình tài chính của doanh nghiệp tại một thời điểm. Bảng này luôn bảo đảm nguyên tắc Tổng tài sản luôn bằng Tổng nợ phải trả cộng Vốn chủ sở hữu."
    },
    {
        "id": "card_assets",
        "title": "🟢 Tài sản: Tài sản Dài hạn và Tài sản Ngắn hạn (Assets)",
        "selector": "#card-assets",
        "en": "Assets represent items of value owned by the business. Non-current assets are tangible resources held for longer than one year, such as land, factories, and vehicles. Current assets are short-term resources converted into cash within twelve months: inventory, trade receivables, and bank balances.",
        "vi": "Tài sản là những nguồn lực có giá trị thuộc quyền sở hữu của doanh nghiệp. Tài sản dài hạn (Non-current assets) có thời gian sử dụng trên một năm như đất đai, nhà xưởng, xe cộ. Tài sản ngắn hạn (Current assets) chuyển hóa thành tiền trong vòng 12 tháng: hàng tồn kho, khoản phải thu khách hàng và tiền gửi ngân hàng."
    },
    {
        "id": "card_liabilities",
        "title": "🔴 Nợ phải trả: Nợ Ngắn hạn và Nợ Dài hạn (Liabilities)",
        "selector": "#card-liabilities",
        "en": "Liabilities represent debts owed to external creditors. Current liabilities must be settled within one year, including trade payables and bank overdrafts. Non-current liabilities represent long-term obligations repayable after more than a year, such as bank mortgages and debentures.",
        "vi": "Nợ phải trả là các nghĩa vụ tài chính mà doanh nghiệp nợ bên thứ ba. Nợ ngắn hạn (Current liabilities) phải trả trong vòng một năm như nợ nhà cung cấp và thấu chi ngân hàng. Nợ dài hạn (Non-current liabilities) là các khoản vay có thời hạn thanh toán trên một năm như vay thế chấp và trái phiếu dài hạn."
    },
    {
        "id": "sec_using_balance_sheet",
        "title": "2. Sử dụng Báo cáo để Đánh giá Khả năng Thanh toán",
        "selector": "#sec-using-balance-sheet",
        "en": "Section 2 investigates net current assets, or working capital. If current liabilities exceed current assets, the business exhibits negative working capital, signaling impending cash default and vulnerability to sudden supplier liquidations.",
        "vi": "Mục hai nghiên cứu tài sản ngắn hạn thuần, tức vốn lưu động. Nếu nợ ngắn hạn vượt quá tài sản ngắn hạn, doanh nghiệp rơi vào tình trạng vốn lưu động âm, cảnh báo nguy cơ mất khả năng trả nợ và đối mặt nguy cơ bị nhà cung cấp siết nợ phát mại."
    },
    {
        "id": "card_packer_sports",
        "title": "📊 Ví dụ Minh họa: Đọc hiểu Bảng Cân đối Kế toán Packer Sports",
        "selector": "#card-packer-sports",
        "en": "Reviewing the Packer Sports balance sheet: Total assets of thirty-nine thousand dollars are predominantly tied up in non-current machinery. Current assets of fifteen thousand easily cover five thousand in short-term debts. However, long-term bank loans of twenty thousand exceed shareholder equity, demonstrating elevated financial gearing.",
        "vi": "Phân tích bảng cân đối kế toán Packer Sports: Tổng tài sản ba mươi chín ngàn đô phần lớn tập trung ở máy móc nhà xưởng dài hạn. Tài sản ngắn hạn mười lăm ngàn thừa sức chi trả năm ngàn nợ ngắn hạn. Tuy nhiên khoản vay ngân hàng dài hạn hai mươi ngàn vượt xa vốn chủ sở hữu, cho thấy tỷ lệ đòn bẩy nợ (gearing) ở mức cao rủi ro."
    },
    {
        "id": "sec_interpret_balance_sheet",
        "title": "3. Phân tích Bảng Cân đối Kế toán theo chuẩn Cambridge",
        "selector": "#sec-interpret-balance-sheet",
        "en": "Section 3 evaluates capital employed and shareholder funds. Candidates must evaluate capital structure: high debt gearing exposes the firm to interest rate surges, while healthy equity reserves provide solid financial resilience.",
        "vi": "Mục ba đánh giá vốn hoạt động (capital employed) và vốn chủ sở hữu. Thí sinh cần phân tích cơ cấu vốn: tỷ lệ nợ vay quá cao khiến doanh nghiệp dễ tổn thương trước biến động lãi suất, trong khi nguồn vốn chủ sở hữu dồi dào tạo nền tảng tài chính vững chắc."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_balance_sheet": {"start": 1, "end": 3},
    "sec_using_balance_sheet": {"start": 4, "end": 5},
    "sec_interpret_balance_sheet": {"start": 6, "end": 6}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.4 Statement of Financial Position (Bảng Cân đối Kế toán)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. THE STATEMENT OF FINANCIAL POSITION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-balance-sheet" class="lecture-interactive-card" data-lecture-section="sec_balance_sheet" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📊 1. THE STATEMENT OF FINANCIAL POSITION</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                The Statement of Financial Position (Balance Sheet) shows the financial structure of a business <b>at a specific calendar date</b>. <br>
                <b>Golden Accounting Balance: Total Assets = Total Liabilities + Total Equity</b> (Net Assets = Total Equity).
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <!-- SUB-CARD: ASSETS -->
            <div id="card-assets" class="lecture-interactive-card" data-lecture-section="card_assets" style="background: #ffffff; border: 1.5px solid #bbf7d0; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <div style="background: #f0fdf4; padding: 16px 20px; border-bottom: 1px solid #bbf7d0; display: flex; align-items: center; justify-content: space-between;">
                    <h3 style="margin: 0; color: #15803d; font-size: 18px; font-weight: 700;">🟢 ASSETS (What the Business Owns)</h3>
                    <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #15803d; padding: 4px 10px; border-radius: 6px; border: 1px solid #bbf7d0;">Nghe thẻ này</span>
                </div>
                <div style="padding: 18px 20px;">
                    <b style="color: #065f46; font-size: 15px;">1. Non-Current Assets:</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13px; color: #475569;">Retained for long-term operational use (&gt; 12 months).</p>
                    <ul style="margin: 0 0 14px 0; padding-left: 18px; color: #475569; font-size: 13px; line-height: 1.5;">
                        <li><i>Tangible:</i> Freehold land, factory buildings, machinery, transport fleets.</li>
                        <li><i>Intangible:</i> Registered patents, brand trademarks, accumulated goodwill.</li>
                    </ul>

                    <b style="color: #065f46; font-size: 15px;">2. Current Assets:</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13px; color: #475569;">Liquid resources converted to cash within 12 months.</p>
                    <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 13px; line-height: 1.5;">
                        <li>Cash in hand &amp; commercial bank accounts (most liquid).</li>
                        <li>Trade Receivables (debtors owing settlement).</li>
                        <li>Inventories (raw materials and unsold finished goods).</li>
                    </ul>
                </div>
            </div>

            <!-- SUB-CARD: LIABILITIES -->
            <div id="card-liabilities" class="lecture-interactive-card" data-lecture-section="card_liabilities" style="background: #ffffff; border: 1.5px solid #fecaca; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <div style="background: #fef2f2; padding: 16px 20px; border-bottom: 1px solid #fecaca; display: flex; align-items: center; justify-content: space-between;">
                    <h3 style="margin: 0; color: #b91c1c; font-size: 18px; font-weight: 700;">🔴 LIABILITIES (What the Business Owes)</h3>
                    <span style="font-size: 11px; font-weight: 700; background: #fff1f2; color: #b91c1c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fecaca;">Nghe thẻ này</span>
                </div>
                <div style="padding: 18px 20px;">
                    <b style="color: #7f1d1d; font-size: 15px;">1. Non-Current Liabilities:</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13px; color: #475569;">Long-term borrowing repayable after more than 12 months.</p>
                    <ul style="margin: 0 0 14px 0; padding-left: 18px; color: #475569; font-size: 13px; line-height: 1.5;">
                        <li>Commercial mortgages secured on corporate real estate.</li>
                        <li>Long-term corporate bank loans and debentures.</li>
                    </ul>

                    <b style="color: #7f1d1d; font-size: 15px;">2. Current Liabilities:</b>
                    <p style="margin: 4px 0 8px 0; font-size: 13px; color: #475569;">Short-term debts due for settlement within 12 months.</p>
                    <ul style="margin: 0; padding-left: 18px; color: #475569; font-size: 13px; line-height: 1.5;">
                        <li>Trade Payables (money owed to raw material suppliers).</li>
                        <li>Bank Overdraft facilities and short-term debt repayments.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. USING THE STATEMENT TO MAKE DECISIONS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-using-balance-sheet" class="lecture-interactive-card" data-lecture-section="sec_using_balance_sheet" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📈 2. USING THE STATEMENT TO MAKE DECISIONS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                The statement provides directors with vital indicators of working capital solvency, liquidity cover, and overall debt gearing.
            </p>
        </div>

        <!-- SUB-CARD: PACKER SPORTS WORKED EXAMPLE -->
        <div id="card-packer-sports" class="lecture-interactive-card" data-lecture-section="card_packer_sports" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #6d28d9; font-weight: 700;">📑 Worked Case: Packer Sports Limited Balance Sheet</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>

            <div style="overflow-x: auto; margin-bottom: 18px; border-radius: 8px; border: 1px solid #e2e8f0;">
                <table style="width: 100%; min-width: 500px; border-collapse: collapse; background: #ffffff; font-size: 13.5px; text-align: left;">
                    <thead>
                        <tr style="background-color: #0f172a; color: #ffffff;">
                            <th colspan="2" style="padding: 12px 16px; font-size: 15px;">Statement of Financial Position as at 31 December 2023</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background: #f1f5f9;">
                            <td colspan="2" style="padding: 8px 16px; font-weight: bold; color: #15803d;">ASSETS</td>
                        </tr>
                        <tr>
                            <td style="padding: 7px 16px 7px 28px; color: #475569;">Non-Current Assets (Property, plant, machinery)</td>
                            <td style="padding: 7px 16px; text-align: right; font-weight: 600;">$24,250</td>
                        </tr>
                        <tr>
                            <td style="padding: 7px 16px 7px 28px; color: #475569;">Current Assets (Cash, debtors, inventory)</td>
                            <td style="padding: 7px 16px; text-align: right; border-bottom: 1px solid #cbd5e1; font-weight: 600;">$15,545</td>
                        </tr>
                        <tr style="font-weight: bold; background: #f8fafc;">
                            <td style="padding: 9px 16px;">Total Assets</td>
                            <td style="padding: 9px 16px; text-align: right; color: #0f172a;">$39,795</td>
                        </tr>

                        <tr style="background: #f1f5f9;">
                            <td colspan="2" style="padding: 8px 16px; font-weight: bold; color: #b91c1c;">LIABILITIES</td>
                        </tr>
                        <tr>
                            <td style="padding: 7px 16px 7px 28px; color: #475569;">Current Liabilities (Overdraft, supplier trade payables)</td>
                            <td style="padding: 7px 16px; text-align: right; font-weight: 600;">$5,060</td>
                        </tr>
                        <tr>
                            <td style="padding: 7px 16px 7px 28px; color: #475569;">Non-Current Liabilities (Long-term bank mortgages)</td>
                            <td style="padding: 7px 16px; text-align: right; border-bottom: 1px solid #cbd5e1; font-weight: 600;">$20,000</td>
                        </tr>
                        <tr style="font-weight: bold; background: #f8fafc;">
                            <td style="padding: 9px 16px;">Total Liabilities</td>
                            <td style="padding: 9px 16px; text-align: right; color: #b91c1c;">$25,060</td>
                        </tr>

                        <tr style="font-weight: bold; background: #eff6ff;">
                            <td style="padding: 10px 16px; color: #1e40af;">NET ASSETS (Total Assets - Total Liabilities)</td>
                            <td style="padding: 10px 16px; text-align: right; color: #1e40af;">$14,735</td>
                        </tr>

                        <tr style="background: #f1f5f9;">
                            <td colspan="2" style="padding: 8px 16px; font-weight: bold; color: #6d28d9;">EQUITY (SHAREHOLDERS' FUNDS)</td>
                        </tr>
                        <tr>
                            <td style="padding: 7px 16px 7px 28px; color: #475569;">Share Capital</td>
                            <td style="padding: 7px 16px; text-align: right; font-weight: 600;">$1,500</td>
                        </tr>
                        <tr>
                            <td style="padding: 7px 16px 7px 28px; color: #475569;">Retained Earnings Reserve</td>
                            <td style="padding: 7px 16px; text-align: right; border-bottom: 1px solid #cbd5e1; font-weight: 600;">$13,235</td>
                        </tr>
                        <tr style="font-weight: bold; background: #f5f3ff;">
                            <td style="padding: 10px 16px; color: #6d28d9;">TOTAL EQUITY</td>
                            <td style="padding: 10px 16px; text-align: right; color: #6d28d9; border-bottom: 3px double #6d28d9;">$14,735</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 8px;">
                    <b style="color: #15803d; font-size: 14px;">🟢 Liquidity Strength:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #166534; line-height: 1.5;">
                        Current assets ($15,545) exceed current debts ($5,060) by over 3 to 1, providing exceptional working capital security.
                    </p>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 14px; border-radius: 8px;">
                    <b style="color: #b91c1c; font-size: 14px;">⚠️ High Gearing Risk:</b>
                    <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #991b1b; line-height: 1.5;">
                        Long-term loan debt ($20,000) exceeds total equity ($14,735). The firm is highly geared, making further bank loan approvals difficult.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-interpret-balance-sheet" class="lecture-interactive-card" data-lecture-section="sec_interpret_balance_sheet" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 3. INTERPRETING THE STATEMENT OF FINANCIAL POSITION (Cambridge Exam Guide)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                <i>Cambridge syllabus rule:</i> Full balance sheet construction will not be examined. Instead, candidates must interpret figures and evaluate financial health.
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #1e40af; font-size: 15px;">Capital Employed:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        <code>Capital Employed = Shareholders' Funds + Non-Current Liabilities</code><br/>
                        Measures total long-term funding invested in commercial assets.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #047857; font-size: 15px;">Working Capital Risk:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        <code>Working Capital = Current Assets - Current Liabilities</code><br/>
                        If negative, the business cannot pay short-term bills and faces immediate insolvency risk.
                    </p>
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.4 Statement of Financial Position (Bảng Cân đối Kế toán)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 5.4 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/5_4_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 5.4 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
