import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 5.2 ID
LID = 'dc0411df-d831-468a-9a7d-16fb4009290d'
CODE = '5_2'
TITLE = '5.2. Cash flow forecasting and working capital'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 9 AUDIO SEGMENTS FOR LESSON 5.2
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 5.2: Dự báo Dòng tiền và Vốn lưu động",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 5.2: Cash Flow Forecasting and Working Capital. In this vital chapter, we unpack the cash flow cycle, construct cash flow forecasts, calculate closing balances, define working capital, and implement corrective measures to overcome liquidity insolvency.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 5.2: Dự báo Dòng tiền và Vốn lưu động. Trong bài học then chốt này, chúng ta sẽ khảo sát chu chuyển dòng tiền, lập bảng dự báo dòng tiền, tính số dư cuối kỳ, quản trị vốn lưu động và các biện pháp giải quyết khủng hoảng thanh khoản."
    },
    {
        "id": "sec_cash_and_cycle",
        "title": "1. Bản chất Dòng tiền & Vòng Chu chuyển Dòng tiền",
        "selector": "#sec-cash-and-cycle",
        "en": "Section 1 establishes the distinction between liquid cash and accounting profit. Cash is the actual money in the bank available immediately to settle bills. Profit is revenue minus total expenses. A profitable business can still go bankrupt if cash is depleted before trade debts are recollected.",
        "vi": "Mục một thiết lập sự khác biệt then chốt giữa tiền mặt và lợi nhuận kế toán. Tiền mặt là lượng tiền khả dụng trong ngân hàng để thanh toán tức thì các hóa đơn. Lợi nhuận là doanh thu trừ tổng chi phí. Một doanh nghiệp có lãi trên sổ sách vẫn có thể bị phá sản nếu cạn sạch tiền mặt trước khi thu hồi được các khoản nợ bán chịu."
    },
    {
        "id": "card_cash_vs_profit",
        "title": "💵 Tiền Mặt vs Lợi Nhuận: Vì sao Doanh nghiệp có lãi vẫn phá sản?",
        "selector": "#card-cash-vs-profit",
        "en": "Profit does not equal cash in hand. When goods are sold on credit, revenue and paper profits register immediately, yet cash has not been received. If cash outflows for wages and rent fall due before debtors settle, the business experiences insolvency collapse despite record sales profits.",
        "vi": "Lợi nhuận không đồng nghĩa với tiền mặt trong tay. Khi bán hàng trả chậm, doanh thu và lợi nhuận trên giấy tờ được ghi nhận ngay, nhưng tiền mặt thực tế chưa về tài khoản. Nếu các khoản chi tiền mặt cho tiền lương và tiền thuê nhà đến hạn trước khi khách trả nợ, doanh nghiệp sẽ rơi vào tình trạng vỡ nợ thanh khoản dù lợi nhuận bán hàng cao kỷ lục."
    },
    {
        "id": "card_cashflow_cycle",
        "title": "🔄 Vòng Chu chuyển Dòng tiền (The Cash Flow Cycle)",
        "selector": "#card-cashflow-cycle",
        "en": "The Cash Flow Cycle shows how cash is converted into raw materials, transformed into work-in-progress, delivered to trade credit customers as trade receivables, and eventually recollected as cash. The longer this cycle takes, the greater the working capital tied up.",
        "vi": "Vòng chu chuyển dòng tiền mô tả quá trình tiền mặt được dùng để mua nguyên liệu, đưa vào sản xuất dở dang, bán cho khách hàng nợ tiền (khoản phải thu) và cuối cùng thu hồi lại thành tiền mặt. Chu kỳ này càng kéo dài thì lượng vốn lưu động bị ứ đọng càng lớn."
    },
    {
        "id": "sec_cash_flow_forecasts",
        "title": "2. Bảng Dự báo Dòng tiền & Phương pháp Tính toán",
        "selector": "#sec-cash-flow-forecasts",
        "en": "Section 2 defines a Cash Flow Forecast as an estimate of future cash inflows and cash outflows on a month-by-month basis. Forecasting anticipates cash deficits well in advance, allowing managers to arrange bank overdrafts before payroll defaults occur.",
        "vi": "Mục hai định nghĩa Bảng dự báo dòng tiền là ước tính các khoản tiền mặt thực thu vào và chi ra của doanh nghiệp theo từng tháng trong tương lai. Dự báo giúp phát hiện sớm nguy cơ thiếu hụt tiền mặt để chủ động xin hạn mức thấu chi ngân hàng trước khi xảy ra chậm lương nhân viên."
    },
    {
        "id": "card_cashflow_formulas",
        "title": "🧮 Công thức Tính toán Dòng tiền Chuẩn Cambridge",
        "selector": "#card-cashflow-formulas",
        "en": "Master three core formulas: Net Cash Flow equals Total Cash Inflows minus Total Cash Outflows; Closing Bank Balance equals Opening Bank Balance plus Net Cash Flow; and Opening Balance of month two always equals Closing Balance of month one.",
        "vi": "Nắm vững ba công thức tính cốt lõi: Dòng tiền thuần (Net Cash Flow) bằng Tổng thu trừ Tổng chi; Số dư cuối kỳ bằng Số dư đầu kỳ cộng Dòng tiền thuần; và Số dư đầu kỳ của tháng sau luôn bằng chính Số dư cuối kỳ của tháng trước."
    },
    {
        "id": "sec_working_capital",
        "title": "3. Vai trò Sống còn của Vốn lưu động (Working Capital)",
        "selector": "#sec-working-capital",
        "en": "Section 3 defines Working Capital as Current Assets minus Current Liabilities. Known as the lifeblood of day-to-day operations, adequate working capital guarantees prompt settlement of supplier bills and prevents bankruptcy due to sudden illiquidity.",
        "vi": "Mục ba định nghĩa Vốn lưu động bằng Tài sản ngắn hạn trừ Nợ ngắn hạn. Được ví như mạch máu nuôi dưỡng hoạt động thường nhật, vốn lưu động đầy đủ bảo đảm thanh toán đúng hạn cho nhà cung cấp và ngăn ngừa nguy cơ phá sản do mất khả năng thanh toán tức thời."
    },
    {
        "id": "card_working_capital_balance",
        "title": "⚖️ Cân Bằng Vốn Lưu Động: Thiếu Hụt vs Dư Thừa Vốn Lưu Động",
        "selector": "#card-working-capital-balance",
        "en": "Working capital requires delicate balance: a deficit forces clearance stock discounting at severe losses and emergency high-interest overdraft loans, while an excess ties up unproductive liquid funds that could otherwise earn capital returns or finance growth assets.",
        "vi": "Vốn lưu động đòi hỏi sự cân bằng tinh tế: thiếu hụt vốn lưu động buộc doanh nghiệp phải bán tháo hàng tồn kho chịu lỗ nặng và vay thấu chi lãi suất cao, trong khi dư thừa vốn lưu động lại làm đóng băng các nguồn vốn nhàn rỗi lẽ ra có thể đem lại lợi tức sinh lời hoặc tài trợ mở rộng cơ sở vật chất."
    },
    {
        "id": "sec_overcome_cashflow",
        "title": "4. Chiến lược thi Cambridge: Giải pháp Khắc phục Khủng hoảng Dòng tiền",
        "selector": "#sec-overcome-cashflow",
        "en": "Section 4 evaluates methods to overcome cash flow crises: negotiating extended supplier trade credit, factoring debtor invoices for immediate 80% cash advances, selling off obsolete inventory at discount, and delaying non-essential capital equipment investments.",
        "vi": "Mục bốn đánh giá các giải pháp ứng phó khủng hoảng dòng tiền: đàm phán kéo dài thời hạn nợ với nhà cung cấp, bán các hóa đơn nợ cho công ty bao thanh toán (debt factoring) để lấy ngay tiền mặt, giảm giá xả hàng tồn kho ứ đọng và hoãn mua sắm các thiết bị máy móc chưa thực sự cần thiết."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_cash_and_cycle": {"start": 1, "end": 3},
    "sec_cash_flow_forecasts": {"start": 4, "end": 5},
    "sec_working_capital": {"start": 6, "end": 7},
    "sec_overcome_cashflow": {"start": 8, "end": 8}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.2 Cash Flow Forecasting and Working Capital (Dự báo Dòng tiền &amp; Vốn lưu động)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. THE CASH FLOW CYCLE & CASH VS PROFIT -->
    <div style="margin-bottom: 50px;">
        <div id="sec-cash-and-cycle" class="lecture-interactive-card" data-lecture-section="sec_cash_and_cycle" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💰 1. CASH FLOW &amp; THE CASH FLOW CYCLE</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                Cash is the lifeblood of a business. Without continuous cash liquidity, even highly profitable companies face rapid insolvency liquidation.
            </div>
        </div>

        <!-- SUB-CARD: CASH VS PROFIT -->
        <div id="card-cash-vs-profit" class="lecture-interactive-card" data-lecture-section="card_cash_vs_profit" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">💵 Cash vs Profit: Why Profitable Businesses Fail</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15.5px;">💵 What is Cash?</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #166534; line-height: 1.5;">
                        Physical money in hand and accessible commercial bank balances. Used to immediately settle supplier invoices, electricity overheads, and employee wages.
                    </p>
                </div>

                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 16px;">
                    <b style="color: #1e40af; font-size: 15.5px;">📈 What is Profit?</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #1e40af; line-height: 1.5;">
                        Total Sales Revenue minus Total Operational Costs over a trading period. Sits as an accounting figure; does not mean cash is physically received yet!
                    </p>
                </div>
            </div>

            <div style="margin-top: 14px; background: #fffbeb; border: 1px dashed #f59e0b; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #92400e;">
                <b>⚠️ The Insolvency Trap:</b> A business selling $100,000 goods on 60-day credit shows high paper profit, but if it runs out of cash to pay workers next week, it collapses!
            </div>
        </div>

        <!-- SUB-CARD: THE CASH FLOW CYCLE -->
        <div id="card-cashflow-cycle" class="lecture-interactive-card" data-lecture-section="card_cashflow_cycle" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">🔄 The 4-Stage Cash Flow Cycle</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <p style="font-size: 14px; color: #475569; margin: 0 0 16px 0;">
                The chronological progression from paying cash out for manufacturing inputs to collecting cash receipts from customers:
            </p>

            <div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center; background: #fff7ed; padding: 18px; border-radius: 10px; border: 1px solid #ffedd5;">
                <div style="background: #ffffff; color: #c2410c; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: bold; border: 1px solid #fed7aa; text-align: center;">
                    1. Cash Outflow<br/><span style="font-weight: normal; font-size: 11.5px; color: #78716c;">(Buy Raw Materials)</span>
                </div>
                <span style="color: #ea580c; font-weight: bold; font-size: 18px;">➔</span>
                <div style="background: #ffffff; color: #c2410c; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: bold; border: 1px solid #fed7aa; text-align: center;">
                    2. Production<br/><span style="font-weight: normal; font-size: 11.5px; color: #78716c;">(Goods Produced)</span>
                </div>
                <span style="color: #ea580c; font-weight: bold; font-size: 18px;">➔</span>
                <div style="background: #ffffff; color: #c2410c; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: bold; border: 1px solid #fed7aa; text-align: center;">
                    3. Credit Sales<br/><span style="font-weight: normal; font-size: 11.5px; color: #78716c;">(Trade Debtors)</span>
                </div>
                <span style="color: #ea580c; font-weight: bold; font-size: 18px;">➔</span>
                <div style="background: #ffffff; color: #15803d; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: bold; border: 1px solid #bbf7d0; text-align: center;">
                    4. Cash Inflow<br/><span style="font-weight: normal; font-size: 11.5px; color: #166534;">(Customer Settles)</span>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. CASH-FLOW FORECASTS & WORKED EXAMPLE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-cash-flow-forecasts" class="lecture-interactive-card" data-lecture-section="sec_cash_flow_forecasts" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📊 2. CASH-FLOW FORECASTS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                A cash-flow forecast predicts expected cash inflows and outflows monthly over a future timeframe, anticipating bank overdraft requirements.
            </p>
        </div>

        <!-- SUB-CARD: FORMULAS AND TABLE -->
        <div id="card-cashflow-formulas" class="lecture-interactive-card" data-lecture-section="card_cashflow_formulas" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #6d28d9; font-weight: 700;">🧮 Cash Flow Calculations &amp; Worked Example</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1.5px dashed #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 12px; color: #64748b; font-weight: bold; text-transform: uppercase;">Formula 1: Net Cash Flow</span>
                    <p style="margin: 4px 0 0 0; color: #0f172a; font-weight: 700; font-size: 14.5px;">Net Cash Flow = Cash Inflows - Cash Outflows</p>
                </div>
                <div style="background: #f8fafc; border: 1.5px dashed #cbd5e1; padding: 14px; border-radius: 8px; text-align: center;">
                    <span style="font-size: 12px; color: #64748b; font-weight: bold; text-transform: uppercase;">Formula 2: Closing Balance</span>
                    <p style="margin: 4px 0 0 0; color: #0f172a; font-weight: 700; font-size: 14.5px;">Closing Balance = Opening Balance + Net Cash Flow</p>
                </div>
            </div>

            <div style="overflow-x: auto; margin-bottom: 16px;">
                <table style="width: 100%; border-collapse: collapse; text-align: center; font-size: 13.5px; border: 1px solid #e2e8f0;">
                    <thead>
                        <tr style="background-color: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                            <th style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Item ($000s)</th>
                            <th style="padding: 10px; border-right: 1px solid #e2e8f0;">April</th>
                            <th style="padding: 10px; border-right: 1px solid #e2e8f0;">May</th>
                            <th style="padding: 10px;">June</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Cash Inflows</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0;">23</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0;">24</td>
                            <td style="padding: 10px;">30</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Cash Outflows</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0; font-weight: bold; color: #2563eb;">13</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0;">28</td>
                            <td style="padding: 10px;">81</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                            <td style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0; font-weight: bold;">Net Cash Flow</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0;">10</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0; font-weight: bold; color: #dc2626;">(4)</td>
                            <td style="padding: 10px; color: #dc2626;">(51)</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0;">Opening Balance</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0;">30</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0;">40</td>
                            <td style="padding: 10px;">36</td>
                        </tr>
                        <tr style="background: #f1f5f9;">
                            <td style="padding: 10px; text-align: left; border-right: 1px solid #e2e8f0; font-weight: bold;">Closing Balance</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0; font-weight: bold;">40</td>
                            <td style="padding: 10px; border-right: 1px solid #e2e8f0; font-weight: bold;">36</td>
                            <td style="padding: 10px; font-weight: bold; color: #dc2626;">(15)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="background: #fef2f2; border: 1px dashed #ef4444; border-radius: 8px; padding: 12px 16px; font-size: 13px; color: #7f1d1d;">
                <b>💡 Exam Tip:</b> Closing balance of April ($40) becomes the Opening balance of May ($40). Negative figures are placed in brackets: e.g. <b>(15)</b>.
            </div>
        </div>
    </div>

    <!-- 3. WORKING CAPITAL -->
    <div style="margin-bottom: 50px;">
        <div id="sec-working-capital" class="lecture-interactive-card" data-lecture-section="sec_working_capital" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #14b8a6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚙️ 3. WORKING CAPITAL (VỐN LƯU ĐỘNG)</h2>
            <div style="background: #f0fdfa; border-left: 4px solid #0d9488; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #0f766e; margin-bottom: 10px;">
                <b>Working Capital = Current Assets - Current Liabilities</b>
            </div>
            <p style="margin: 0; font-size: 14px; color: #475569;">
                Represents net liquid capital deployed to finance everyday trading operations.
            </p>
        </div>

        <!-- SUB-CARD: WORKING CAPITAL BALANCE -->
        <div id="card-working-capital-balance" class="lecture-interactive-card" data-lecture-section="card_working_capital_balance" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #99f6e4; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #0f766e; font-weight: 700;">⚖️ Current Assets, Liabilities &amp; Balance Optimization</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f0fdfa; color: #0f766e; padding: 4px 10px; border-radius: 6px; border: 1px solid #99f6e4;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #15803d; font-size: 15.5px; margin: 0 0 8px 0;">🟢 Current Assets</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 13px; line-height: 1.6;">
                        <li><b>Cash at Bank:</b> Most liquid asset.</li>
                        <li><b>Trade Receivables (Debtors):</b> Customers owing payment.</li>
                        <li><b>Inventories (Stock):</b> Raw materials and finished goods.</li>
                    </ul>
                </div>

                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #b91c1c; font-size: 15.5px; margin: 0 0 8px 0;">🔴 Current Liabilities</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 13px; line-height: 1.6;">
                        <li><b>Trade Payables (Creditors):</b> Money owed to suppliers.</li>
                        <li><b>Bank Overdraft:</b> Short-term callable borrowing.</li>
                        <li><b>Short-term Loan Repayments:</b> Due within 12 months.</li>
                    </ul>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px;">
                <div style="background: #fff1f2; border: 1px solid #fecdd3; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #9f1239;">
                    <b>⚠️ Danger of Working Capital Deficit:</b> Inability to pay supplier debts triggers legal action and sudden insolvency shutdown.
                </div>
                <div style="background: #fefce8; border: 1px solid #fef08a; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #854d0e;">
                    <b>💤 Inefficiency of Working Capital Excess:</b> Idle cash yields 0% growth; excess inventory incurs heavy warehousing and obsolescence costs.
                </div>
            </div>
        </div>
    </div>

    <!-- 4. CAMBRIDGE EXAM GUIDE: OVERCOMING CASH FLOW CRISES -->
    <div style="margin-bottom: 50px;">
        <div id="sec-overcome-cashflow" class="lecture-interactive-card" data-lecture-section="sec_overcome_cashflow" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 4. HOW TO OVERCOME CASH FLOW PROBLEMS (Cambridge Exam Strategy)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Exam questions regularly require students to: <i>"Recommend the two best methods this business can use to overcome its negative cash flow problem."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #1e40af; font-size: 15px;">1. Arrange a Bank Overdraft</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Supplies rapid emergency cash for payroll, but variable interest is punitive and the facility can be revoked by the bank.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #047857; font-size: 15px;">2. Extend Supplier Trade Credit</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Renegotiate credit terms from 30 to 60 days. Preserves internal cash balances, though suppliers may forfeit discounts.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #f59e0b; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #b45309; font-size: 15px;">3. Speed Up Debtor Collections</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Offer 5% discounts for prompt cash payment, or sell customer invoices to a debt factoring firm for immediate cash advances.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #ec4899; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #be185d; font-size: 15px;">4. Postpone Capital Expenditure</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Delay acquiring expensive vehicles or machinery, or opt for operating leasing to eliminate large lump-sum cash outflows.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.2 Cash Flow Forecasting and Working Capital (Dự báo Dòng tiền &amp; Vốn lưu động)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 5.2 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/5_2_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 5.2 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
