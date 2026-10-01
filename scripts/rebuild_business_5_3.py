import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 5.3 ID
LID = '71f25939-98d4-4fa3-8227-be8434f64581'
CODE = '5_3'
TITLE = '5.3. Income statements'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 7 AUDIO SEGMENTS FOR LESSON 5.3
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 5.3: Báo cáo Kết quả Hoạt động Kinh doanh",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 5.3: Income Statements. In this financial accounting lesson, we explore why profit matters, clearly distinguish profit from cash flow, deconstruct the line items of an income statement, and use gross and profit for the year to guide management decisions.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 5.3: Báo cáo Kết quả Hoạt động Kinh doanh. Trong bài học kế toán tài chính này, chúng ta sẽ làm rõ tầm quan trọng của lợi nhuận, phân biệt rạch ròi giữa lợi nhuận và dòng tiền, phân tích từng mục trong báo cáo thu nhập và ứng dụng số liệu để ra quyết định quản trị."
    },
    {
        "id": "sec_profit_importance",
        "title": "1. Tầm quan trọng của Lợi nhuận (The Importance of Profit)",
        "selector": "#sec-profit-importance",
        "en": "Section 1 defines profit as total revenue minus total operating costs over a trading period. Profit acts as a reward for enterprise risk-taking, provides vital internal finance for retained reinvestment, and serves as a barometer of managerial competence.",
        "vi": "Mục một định nghĩa lợi nhuận là tổng doanh thu trừ đi tổng chi phí hoạt động trong một kỳ kinh doanh. Lợi nhuận là phần thưởng cho việc chấp nhận rủi ro kinh doanh, cung cấp nguồn vốn nội bộ để tái đầu tư mở rộng và là thước đo chuẩn xác năng lực điều hành của ban giám đốc."
    },
    {
        "id": "card_profit_vs_cash",
        "title": "⚖️ Phân biệt Lợi nhuận đối chiếu với Dòng tiền (Profit vs Cash)",
        "selector": "#card-profit-vs-cash",
        "en": "The golden Cambridge rule: Profit is not Cash! A company can record immense paper profits while simultaneously hurtling toward insolvency if all sales were made on long trade credit terms while immediate supplier invoices demand hard cash.",
        "vi": "Quy tắc vàng Cambridge: Lợi nhuận không đồng nghĩa với Tiền mặt! Một doanh nghiệp có thể ghi nhận khoản lãi khổng lồ trên sổ sách nhưng vẫn hoàn toàn có thể phá sản nếu toàn bộ doanh số bán hàng là cho khách nợ tiền trong khi các hóa đơn nhà cung cấp đòi hỏi tiền mặt thanh toán ngay."
    },
    {
        "id": "sec_income_statement",
        "title": "2. Cấu trúc Báo cáo Thu nhập (Income Statement)",
        "selector": "#sec-income-statement",
        "en": "Section 2 walks through an Income Statement: Revenue minus Cost of Sales gives Gross Profit; subtracting Overheads yields Operating Profit; deducting finance interest costs and corporation tax leaves Profit for the Year.",
        "vi": "Mục hai đi qua cấu trúc Báo cáo thu nhập: Doanh thu trừ Giá vốn hàng bán cho ra Lợi nhuận gộp; trừ tiếp Chi phí quản lý và bán hàng cho ra Lợi nhuận thuần từ hoạt động kinh doanh; sau khi trừ chi phí lãi vay và thuế thu nhập doanh nghiệp sẽ thu được Lợi nhuận ròng của năm."
    },
    {
        "id": "card_income_structure",
        "title": "📑 Trình tự Báo cáo Thu nhập: Từ Doanh Thu đến Lợi Nhuận Giữ Lại",
        "selector": "#card-income-structure",
        "en": "Follow the structured waterfall: Revenue minus direct Cost of Sales equals Gross Profit; minus indirect Overheads equals Net Profit; minus Corporation Tax leaves Profit After Tax; finally minus Dividends yields Retained Profit preserved for reinvestment.",
        "vi": "Theo dõi dòng tính toán tuần tự: Doanh thu trừ Giá vốn hàng bán trực tiếp cho ra Lợi nhuận gộp; trừ tiếp Chi phí quản lý gián tiếp cho ra Lợi nhuận hoạt động; trừ Thuế thu nhập doanh nghiệp còn Lợi nhuận sau thuế; và cuối cùng trừ Cổ tức trả cho cổ đông sẽ ra Lợi nhuận giữ lại để tái đầu tư."
    },
    {
        "id": "card_income_decisions",
        "title": "🧠 Ứng dụng Báo cáo Thu nhập để Ra Quyết định Chiến lược",
        "selector": "#card-income-decisions",
        "en": "Managers analyze income statements by tracking year-on-year trends and benchmarking against direct industry rivals. If gross profit margin slips, managers negotiate bulk raw material discounts; if net margin declines, executive overheads and office expenses are streamlined.",
        "vi": "Ban giám đốc sử dụng báo cáo thu nhập bằng cách theo dõi xu hướng qua các năm và so sánh với các đối thủ cùng ngành. Nếu tỷ suất lợi nhuận gộp sụt giảm, nhà quản trị sẽ đàm phán giảm giá nguyên vật liệu đầu vào; nếu tỷ suất lợi nhuận ròng giảm, các khoản chi phí quản lý doanh nghiệp và văn phòng sẽ được cắt giảm quyết liệt."
    },
    {
        "id": "sec_income_decision",
        "title": "3. Chiến lược làm bài thi Cambridge: Phân tích Lợi nhuận & Đề xuất",
        "selector": "#sec-income-decision",
        "en": "Section 3 evaluates how managers interpret income statements: comparing year-on-year gross margin trends to detect rising raw material supplier prices, and auditing overhead ratios to eliminate administrative waste.",
        "vi": "Mục ba đánh giá cách thức ban quản trị phân tích báo cáo thu nhập: so sánh biên lợi nhuận gộp qua các năm để phát hiện tình trạng nhà cung cấp tăng giá nguyên liệu, và kiểm soát tỷ lệ chi phí quản lý nhằm cắt giảm lãng phí hành chính."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_profit_importance": {"start": 1, "end": 2},
    "sec_income_statement": {"start": 3, "end": 5},
    "sec_income_decision": {"start": 6, "end": 6}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.3 Income Statements (Báo cáo Kết quả Hoạt động Kinh doanh)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. THE IMPORTANCE OF PROFIT -->
    <div style="margin-bottom: 50px;">
        <div id="sec-profit-importance" class="lecture-interactive-card" data-lecture-section="sec_profit_importance" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📈 1. THE IMPORTANCE OF PROFIT</h2>
            <div style="background: #fff7ed; border-left: 4px solid #f97316; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #c2410c; margin-bottom: 14px;">
                <b>Profit = Sales Revenue - Total Costs</b>
            </div>
            <p style="margin: 0; font-size: 14.5px; color: #475569;">
                Profit rewards entrepreneurs for taking commercial risks, supplies internal finance for retained reinvestment, and signals operational success to investors and bank lenders.
            </p>
        </div>

        <!-- SUB-CARD: PROFIT VS CASH -->
        <div id="card-profit-vs-cash" class="lecture-interactive-card" data-lecture-section="card_profit_vs_cash" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">⚖️ Profit vs Cash: The Essential Distinction</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 16px;">
                    <b style="color: #1e40af; font-size: 15.5px;">📈 Accounting Profit</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #1e40af; line-height: 1.5;">
                        Recorded at the moment an invoice is generated, regardless of whether the buyer has actually handed over the money.
                    </p>
                </div>
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <b style="color: #15803d; font-size: 15.5px;">💵 Real Cash Flow</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #166534; line-height: 1.5;">
                        Recorded only when bank funds physically clear. Necessary to settle wages, taxes, and supplier bills due today.
                    </p>
                </div>
            </div>

            <div style="background: #fef2f2; border: 1px dashed #ef4444; padding: 12px 16px; border-radius: 8px; font-size: 13px; color: #991b1b;">
                <b>⚠️ Golden Exam Rule:</b> "A business can be profitable but illiquid." If customers take 90 days to settle debts while staff wages are due on Friday, the business collapses into bankruptcy!
            </div>
        </div>
    </div>

    <!-- 2. THE INCOME STATEMENT -->
    <div style="margin-bottom: 50px;">
        <div id="sec-income-statement" class="lecture-interactive-card" data-lecture-section="sec_income_statement" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">📑 2. THE INCOME STATEMENT (BÁO CÁO THU NHẬP)</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                An <b>Income Statement</b> records trading revenues and operating expenditures incurred over an accounting year, sequentially deriving profit tiers.
            </p>
        </div>

        <!-- SUB-CARD: STRUCTURE -->
        <div id="card-income-structure" class="lecture-interactive-card" data-lecture-section="card_income_structure" style="margin-bottom: 20px; background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="background: #fdf2f8; padding: 18px 22px; border-bottom: 1px solid #fbcfe8; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #be185d; font-size: 18px; font-weight: 700;">The Step-by-Step Structure of an Income Statement</h3>
                    <p style="margin: 3px 0 0 0; font-size: 13px; color: #831843;">From Top-line Sales Revenue down to Retained Reinvestment</p>
                </div>
                <span style="font-size: 11px; font-weight: 700; background: #fff1f2; color: #be185d; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
            </div>
            <div style="padding: 20px 22px;">
                <div style="overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 13.5px;">
                        <tbody>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                                <td style="padding: 10px 14px; font-weight: bold; color: #0f172a; width: 40%;">Sales Revenue</td>
                                <td style="padding: 10px 14px; color: #475569;">Price × Quantity sold across the fiscal year.</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 10px 14px; color: #dc2626; font-weight: bold;">less: Cost of Sales</td>
                                <td style="padding: 10px 14px; color: #475569;">Direct costs of production (raw materials, factory assembly labour).</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #f0fdf4;">
                                <td style="padding: 10px 14px; font-weight: bold; color: #15803d;">= Gross Profit</td>
                                <td style="padding: 10px 14px; color: #166534; font-weight: 600;">Direct profit generated solely from trading product margins.</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 10px 14px; color: #dc2626; font-weight: bold;">less: Expenses (Overheads)</td>
                                <td style="padding: 10px 14px; color: #475569;">Indirect fixed costs: administrative salaries, advertising, premises rent.</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0; background: #eff6ff;">
                                <td style="padding: 10px 14px; font-weight: bold; color: #1e40af;">= Net Profit (Operating Profit)</td>
                                <td style="padding: 10px 14px; color: #1e40af; font-weight: 600;">Profit after all operational running costs are settled.</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #e2e8f0;">
                                <td style="padding: 10px 14px; color: #dc2626; font-weight: bold;">less: Corporation Tax &amp; Dividends</td>
                                <td style="padding: 10px 14px; color: #475569;">Statutory state company tax and dividend payouts to shareholders.</td>
                            </tr>
                            <tr style="background: #fdf2f8;">
                                <td style="padding: 10px 14px; font-weight: bold; color: #be185d;">= Retained Profit</td>
                                <td style="padding: 10px 14px; color: #831843; font-weight: bold;">Profit kept inside the business balance sheet for future expansion.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: DECISION MAKING -->
        <div id="card-income-decisions" class="lecture-interactive-card" data-lecture-section="card_income_decisions" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #0f172a; font-weight: 700;">🧠 Using Income Statements for Managerial Decisions</h3>
                <span style="font-size: 11px; font-weight: 700; background: #f1f5f9; color: #475569; padding: 4px 10px; border-radius: 6px; border: 1px solid #cbd5e1;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #15803d; font-size: 15.5px; margin: 0 0 8px 0;">📈 Assessing Profit Growth</h4>
                    <p style="margin: 0; font-size: 13px; color: #166534; line-height: 1.5;">
                        Compare margins with past years. If revenue grew 15% but net profit fell, investigate why overheads or raw material supplier costs spiked.
                    </p>
                </div>

                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #b91c1c; font-size: 15.5px; margin: 0 0 8px 0;">📉 Diagnosing Trading Losses</h4>
                    <p style="margin: 0; font-size: 13px; color: #991b1b; line-height: 1.5;">
                        Is the loss temporary (e.g. factory relocation) or structural (e.g. dying consumer demand)? Structural losses demand immediate product pivots.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <!-- 3. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-income-decision" class="lecture-interactive-card" data-lecture-section="sec_income_decision" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 3. CAMBRIDGE EXAM GUIDE: PROFIT CALCULATIONS &amp; DECISION MAKING
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                <i>Cambridge 2026 Syllabus:</i> Candidates will not be required to construct full income accounts from scratch, but will be tested on interpreting profit numbers to recommend business solutions.
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 16px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #1e40af; font-size: 15px;">1. Gross Profit Margin:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        <code>Gross Profit = Revenue - Cost of Sales</code>.<br/>
                        To improve Gross Profit: negotiate lower prices with material suppliers or increase selling prices if product brand is strong.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #047857; font-size: 15px;">2. Net Profit (Profit for Year):</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        <code>Net Profit = Gross Profit - Expenses</code>.<br/>
                        To improve Net Profit: relocate to lower-rent suburban premises, cut wasteful administrative costs, and improve staff productivity.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.3 Income Statements (Báo cáo Kết quả Hoạt động Kinh doanh)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 5.3 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/5_3_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 5.3 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
