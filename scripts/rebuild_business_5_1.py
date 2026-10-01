import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 5.1 ID
LID = '7b510a8f-757c-4856-9c68-65f98bf96836'
CODE = '5_1'
TITLE = '5.1. Business Finance: Needs and Sources'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 13 AUDIO SEGMENTS FOR LESSON 5.1
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 5.1: Nhu cầu và Nguồn vốn Doanh nghiệp",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 5.1: Business Finance: Needs and Sources. In this opening chapter of Topic 5, Financial Information and Decisions, we examine why enterprises require capital, compare short-term versus long-term financing needs, evaluate internal versus external capital sources, and analyze microfinance and venture capital.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 5.1: Nhu cầu và Nguồn vốn Doanh nghiệp. Trong bài mở đầu của Chủ đề năm về Tài chính và Ra quyết định Doanh nghiệp, chúng ta sẽ phân tích lý do doanh nghiệp cần vốn, phân biệt nhu cầu vốn ngắn hạn và dài hạn, đánh giá các nguồn vốn nội bộ và bên ngoài, cùng các hình thức tài chính vi mô và vốn mạo hiểm."
    },
    {
        "id": "sec_need_finance",
        "title": "1. Nhu cầu Vốn của Doanh nghiệp",
        "selector": "#sec-need-finance",
        "en": "Section 1 outlines the primary commercial reasons for raising finance: initial startup capital to acquire premises and capital equipment; working capital to finance day-to-day trading inventories and trade credit; and business expansion capital to construct new factories or acquire competitor businesses.",
        "vi": "Mục một tổng hợp các lý do chính để huy động vốn: vốn khởi nghiệp ban đầu để mua sắm cơ sở vật chất và máy móc thiết bị; vốn lưu động để duy trì vòng quay hàng ngày như mua hàng tồn kho và cho khách nợ; và vốn mở rộng kinh doanh để xây dựng nhà máy mới hoặc mua lại doanh nghiệp đối thủ."
    },
    {
        "id": "card_finance_needs",
        "title": "💰 Ba Mục Đích Cốt Lõi: Khởi Nghiệp, Mở Rộng & Vốn Lưu Động",
        "selector": "#card-finance-needs",
        "en": "Enterprises require capital for three fundamental horizons: Start-up capital pays for fixed non-current premises and opening inventories before trading starts. Expansion capital funds R&D projects and larger production facilities. Working capital ensures immediate cash liquidity to satisfy day-to-day payroll, inventory replenishment, and utility overheads.",
        "vi": "Doanh nghiệp cần vốn cho ba mục đích nền tảng: Vốn khởi nghiệp chi trả cho tài sản cố định ban đầu và lượng hàng tồn kho khai trương trước khi có doanh thu. Vốn mở rộng tài trợ cho các dự án nghiên cứu R&D và xây dựng phân xưởng lớn hơn. Vốn lưu động duy trì thanh khoản tiền mặt sẵn sàng để trả lương nhân viên, bù đắp hàng tồn kho và thanh toán hóa đơn vận hành mỗi ngày."
    },
    {
        "id": "sec_short_long_term",
        "title": "2. Nhu cầu Vốn Ngắn hạn và Dài hạn",
        "selector": "#sec-short-long-term",
        "en": "Section 2 matches financing durations to asset life. Short-term finance, under one year, bridges immediate liquidity deficits via bank overdrafts and trade credit. Long-term finance, extending beyond five years, funds major capital assets through bank mortgages, debentures, and issuing equity share capital.",
        "vi": "Mục hai ghép nối thời hạn vay vốn với tuổi thọ của tài sản. Vốn ngắn hạn dưới một năm bù đắp thiếu hụt thanh khoản tạm thời qua thấu chi ngân hàng và tín dụng thương mại. Vốn dài hạn trên năm năm tài trợ cho các tài sản cố định lớn thông qua các khoản vay thế chấp ngân hàng, trái phiếu doanh nghiệp và phát hành cổ phiếu mới."
    },
    {
        "id": "card_short_term",
        "title": "⚡ Các Nguồn Vốn Ngắn Hạn (< 1 năm): Overdraft, Trade Credit, Debt Factoring",
        "selector": "#card-short-term",
        "en": "Short-term instruments solve working capital timing mismatches. Bank overdrafts provide flexible revolving credit lines where interest accrues only on overdrawn balances. Trade credit defers supplier settlements interest-free for 30 to 90 days. Debt factoring liquidates unpaid customer invoices into immediate cash at a modest factoring discount.",
        "vi": "Các công cụ ngắn hạn giải quyết sự lệch pha về thời gian của vốn lưu động. Thấu chi ngân hàng cung cấp hạn mức tín dụng linh hoạt và chỉ tính lãi trên số tiền rút vượt. Tín dụng thương mại cho phép hoãn trả tiền nhà cung cấp từ 30 đến 90 ngày hoàn toàn không lãi suất. Bán nợ (Debt Factoring) chuyển đổi các hóa đơn khách hàng chưa trả thành tiền mặt ngay lập tức với một khoản chiết khấu nhỏ."
    },
    {
        "id": "card_long_term",
        "title": "🏗️ Các Nguồn Vốn Dài Hạn (> 1 năm): Vay Ngân Hàng, Thuê Tài Chính, Cổ Phiếu & Trái Phiếu",
        "selector": "#card-long-term",
        "en": "Long-term instruments fund durable capital acquisitions. Bank loans provide structured, predictable amortized instalments. Hire purchase and leasing eliminate upfront asset capital expenditure while preserving cash reserves. Issuing equity shares raises substantial non-repayable capital for limited companies without incurring debt obligations, while debentures secure long-term loan capital backed by business collateral.",
        "vi": "Các nguồn vốn dài hạn tài trợ cho tài sản cố định có độ bền cao. Vay ngân hàng cung cấp lịch trình trả nợ định kỳ cố định dễ dự báo. Thuê mua và thuê tài chính giúp loại bỏ chi phí mua sắm ban đầu khổng lồ để bảo toàn quỹ tiền mặt. Phát hành cổ phiếu huy động nguồn vốn cổ phần vĩnh viễn không cần trả nợ cho các công ty TNHH và công ty đại chúng, trong khi trái phiếu (debentures) huy động các khoản vay dài hạn có tài sản thế chấp."
    },
    {
        "id": "sec_internal_external",
        "title": "3. Nguồn vốn Nội bộ và Nguồn vốn Bên ngoài",
        "selector": "#sec-internal-external",
        "en": "Section 3 classifies finance by origin. Internal finance comes from retained operating profits, sale of redundant non-current assets, and managing working capital tightly. External finance originates from commercial lenders, leasing companies, new equity investors, and government grants.",
        "vi": "Mục ba phân loại vốn theo xuất xứ. Vốn nội bộ bắt nguồn từ lợi nhuận giữ lại qua các năm, thanh lý tài sản cố định dư thừa và siết chặt quản lý vốn lưu động. Vốn bên ngoài đến từ các ngân hàng thương mại, công ty cho thuê tài chính, cổ đông góp vốn mới và các gói trợ cấp của chính phủ."
    },
    {
        "id": "card_internal_sources",
        "title": "🏠 Ưu nhược điểm của Nguồn vốn Nội bộ (Internal Finance)",
        "selector": "#card-internal-sources",
        "en": "Internal finance incurs zero interest charges, requires no debt collateral, and maintains 100% owner control. However, newly formed startups lack retained earnings, and selling essential factory machinery permanently degrades production capacity.",
        "vi": "Vốn nội bộ không phát sinh chi phí lãi vay, không cần thế chấp tài sản và duy trì trọn vẹn quyền kiểm soát của chủ sở hữu. Tuy nhiên, các công ty mới thành lập chưa có lợi nhuận tích lũy, và việc bán máy móc thiết bị thiết yếu có thể làm suy giảm nghiêm trọng năng lực sản xuất."
    },
    {
        "id": "card_external_sources",
        "title": "🌍 Các Kênh Vốn Bên ngoài Cốt lõi (External Finance)",
        "selector": "#card-external-sources",
        "en": "External financing channels include: Bank overdrafts offering flexible emergency cash; Trade credit providing 30 to 60 days of interest-free supplier financing; Hire purchase and leasing avoiding massive upfront capital outlay; and Share issues raising vast equity without debt repayment deadlines.",
        "vi": "Các kênh vốn bên ngoài cốt lõi gồm: Thấu chi ngân hàng (Bank overdraft) cung ứng tiền mặt linh hoạt trong tình huống khẩn cấp; Tín dụng thương mại (Trade credit) cho phép nợ tiền nhà cung cấp 30 đến 60 ngày không lãi suất; Thuê mua và thuê tài chính giúp tránh chi khoản tiền vốn ban đầu quá lớn; và Phát hành cổ phiếu huy động nguồn vốn khổng lồ mà không phải chịu áp lực trả nợ gốc."
    },
    {
        "id": "sec_alternative_sources",
        "title": "4. Các Nguồn vốn Hiện đại: Crowdfunding và Venture Capital",
        "selector": "#sec-alternative-sources",
        "en": "Section 4 explores innovative financing: Crowdfunding raises micro-contributions from thousands of online backers; Microfinance delivers small loans to impoverished entrepreneurs in developing nations; and Venture Capital provides equity funding and mentorship to high-risk, high-growth technology ventures.",
        "vi": "Mục bốn tìm hiểu các nguồn vốn đổi mới sáng tạo: Gọi vốn cộng đồng (Crowdfunding) huy động hàng ngàn khoản tiền nhỏ từ công chúng trực tuyến; Tài chính vi mô (Microfinance) cung cấp các khoản vay nhỏ cho người nghèo khởi nghiệp tại các nước đang phát triển; và Quỹ đầu tư mạo hiểm (Venture Capital) rót vốn cổ phần kèm cố vấn chiến lược cho các startup công nghệ tăng trưởng nhanh."
    },
    {
        "id": "card_crowdfunding_micro",
        "title": "💡 So Sánh Chi Tiết: Crowdfunding vs Microfinance",
        "selector": "#card-crowdfunding-micro",
        "en": "Crowdfunding mobilizes voluntary backing from global online communities on platforms like Kickstarter, testing product market demand with zero loan debt, yet exposing project ideas to public imitators. Microfinance provides crucial financial lifelines to unbanked grassroots entrepreneurs in emerging economies, unlocking micro-enterprise self-sufficiency.",
        "vi": "Gọi vốn cộng đồng huy động sự ủng hộ tự nguyện từ cộng đồng mạng toàn cầu trên các nền tảng như Kickstarter, giúp đo lường nhu cầu thị trường mà không tạo gánh nặng nợ vay, nhưng có thể để lộ ý tưởng kinh doanh cho đối thủ sao chép. Tài chính vi mô cung cấp đòn bẩy vốn nhỏ thiết yếu cho các cá nhân khó tiếp cận ngân hàng tại các nền kinh tế đang phát triển, mở ra con đường tự chủ tài chính cho các hộ kinh doanh cá thể."
    },
    {
        "id": "sec_choosing_finance",
        "title": "5. Tiêu chí Lựa chọn Nguồn vốn Phù hợp",
        "selector": "#sec-choosing-finance",
        "en": "Section 5 presents the selection matrix: purpose and duration of finance, total amount required, legal business structure (sole traders cannot issue shares), interest rate expense, and owner appetite for debt gearing versus equity dilution.",
        "vi": "Mục năm cung cấp ma trận lựa chọn nguồn vốn: mục đích và thời hạn sử dụng vốn, tổng số tiền cần huy động, loại hình pháp lý (doanh nghiệp tư nhân không được phát hành cổ phiếu), chi phí lãi suất vay và mức độ sẵn sàng chấp nhận đòn bẩy nợ so với việc bị pha loãng quyền sở hữu công ty."
    },
    {
        "id": "sec_recommend_finance",
        "title": "6. Chiến lược làm bài thi Cambridge: Đề xuất Nguồn vốn",
        "selector": "#sec-recommend-finance",
        "en": "Section 6 details the Cambridge evaluation strategy for finance questions. Candidates must evaluate gearing risks: borrowing excessively increases default bankruptcy risks if trading conditions deteriorate, while equity issues permanently surrender future dividend yields to incoming shareholders.",
        "vi": "Mục sáu hướng dẫn chiến lược trả lời câu hỏi thi Cambridge về nguồn vốn. Thí sinh phải phân tích rủi ro tỷ lệ đòn bẩy tài chính (gearing): vay nợ quá nhiều làm tăng nguy cơ vỡ nợ phá sản khi thị trường biến động tiêu cực, trong khi phát hành cổ phiếu mới sẽ vĩnh viễn chia sẻ cổ tức tương lai cho các cổ đông mới."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_need_finance": {"start": 1, "end": 2},
    "sec_short_long_term": {"start": 3, "end": 5},
    "sec_internal_external": {"start": 6, "end": 8},
    "sec_alternative_sources": {"start": 9, "end": 10},
    "sec_choosing_finance": {"start": 11, "end": 11},
    "sec_recommend_finance": {"start": 12, "end": 12}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.1 Business Finance: Needs and Sources (Nhu cầu &amp; Nguồn vốn)</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. THE NEED FOR BUSINESS FINANCE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-need-finance" class="lecture-interactive-card" data-lecture-section="sec_need_finance" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💰 1. THE NEED FOR BUSINESS FINANCE</h2>
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 14px 18px; border-radius: 4px; font-size: 15px; color: #1e40af; margin-bottom: 10px;">
                All businesses need finance (often called <b>capital</b>) to get started, grow, and fund their continuing day-to-day operations.
            </div>
        </div>

        <!-- SUB-CARD: 3 CORE NEEDS FOR FINANCE -->
        <div id="card-finance-needs" class="lecture-interactive-card" data-lecture-section="card_finance_needs" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">🚀 The Three Core Purposes for Business Finance</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #2563eb; font-size: 16px; margin: 0 0 8px 0;">🚀 Starting a Business</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #1e40af; font-size: 13px; line-height: 1.6;">
                        <li><b>Start-up capital</b> buys fixed assets (vehicles, machinery) and initial inventory.</li>
                        <li>Required sums are calculated in the founding <b>business plan</b>.</li>
                        <li>Crucial before trading revenue begins flowing into accounts.</li>
                    </ul>
                </div>

                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #059669; font-size: 16px; margin: 0 0 8px 0;">📈 Expanding a Business</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 13px; line-height: 1.6;">
                        <li>Funds major <b>capital expenditure</b> to expand factory output.</li>
                        <li>Covers long-term investments in <b>Research &amp; Development (R&amp;D)</b>.</li>
                        <li>Enables acquiring competitor companies or entering overseas markets.</li>
                    </ul>
                </div>

                <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #d97706; font-size: 16px; margin: 0 0 8px 0;">🔄 Working Capital</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #92400e; font-size: 13px; line-height: 1.6;">
                        <li>Cash dedicated to <b>day-to-day trading</b> (raw materials, employee wages, utilities).</li>
                        <li>Guarantees immediate liquidity to meet short-term liabilities.</li>
                        <li>Prevents insolvency crises caused by customers paying on delayed credit.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. SHORT-TERM VS LONG-TERM FINANCE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-short-long-term" class="lecture-interactive-card" data-lecture-section="sec_short_long_term" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⏱️ 2. SHORT-TERM vs LONG-TERM FINANCE</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Financial controllers match the lifespan of the asset being funded with the duration of the borrowing facility.
            </p>
        </div>

        <!-- SUB-CARD: SHORT TERM FINANCE -->
        <div id="card-short-term" class="lecture-interactive-card" data-lecture-section="card_short_term" style="margin-bottom: 20px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="background: #f8fafc; padding: 18px 22px; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #6d28d9; font-size: 18px; font-weight: 700;">⚡ Short-term Finance (Repaid within 1 Year)</h3>
                    <p style="margin: 3px 0 0 0; font-size: 13.5px; color: #475569;">Used to bridge working capital deficits, seasonal troughs, and unexpected emergency bills.</p>
                </div>
                <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 4px 10px; border-radius: 6px; border: 1px solid #ddd6fe;">Nghe thẻ này</span>
            </div>
            <div style="padding: 18px 22px; overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; min-width: 580px; text-align: left; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #f3e8ff; border-bottom: 2px solid #d8b4fe;">
                            <th style="padding: 10px 14px; color: #6b21a8; width: 25%;">Source</th>
                            <th style="padding: 10px 14px; color: #6b21a8; width: 37.5%;">✅ Advantages</th>
                            <th style="padding: 10px 14px; color: #6b21a8; width: 37.5%;">❌ Disadvantages</th>
                        </tr>
                    </thead>
                    <tbody style="color: #475569;">
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Bank Overdraft</td>
                            <td style="padding: 10px 14px;">Highly flexible. Interest is only charged on the exact overdrawn sum.</td>
                            <td style="padding: 10px 14px;">High variable interest rates. Bank may call in repayment at short notice.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Trade Credit</td>
                            <td style="padding: 10px 14px;">Interest-free supplier credit for 30–90 days. Sell goods before paying bills.</td>
                            <td style="padding: 10px 14px;">Suppliers withhold discounts or delay shipments if accounts are settled late.</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Debt Factoring</td>
                            <td style="padding: 10px 14px;">Immediate cash injection from selling unpaid customer receivables.</td>
                            <td style="padding: 10px 14px;">Factoring agency retains 5%–10% of invoice face value as commission fee.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- SUB-CARD: LONG TERM FINANCE -->
        <div id="card-long-term" class="lecture-interactive-card" data-lecture-section="card_long_term" style="background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="background: #f8fafc; padding: 18px 22px; border-bottom: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <h3 style="margin: 0; color: #059669; font-size: 18px; font-weight: 700;">🏗️ Long-term Finance (Spread over more than 1 Year)</h3>
                    <p style="margin: 3px 0 0 0; font-size: 13.5px; color: #475569;">Finances durable fixed assets like factory premises, commercial fleets, and heavy equipment.</p>
                </div>
                <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 4px 10px; border-radius: 6px; border: 1px solid #a7f3d0;">Nghe thẻ này</span>
            </div>
            <div style="padding: 18px 22px; overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; min-width: 580px; text-align: left; font-size: 13px;">
                    <thead>
                        <tr style="background-color: #d1fae5; border-bottom: 2px solid #6ee7b7;">
                            <th style="padding: 10px 14px; color: #047857; width: 25%;">Source</th>
                            <th style="padding: 10px 14px; color: #047857; width: 37.5%;">✅ Advantages</th>
                            <th style="padding: 10px 14px; color: #047857; width: 37.5%;">❌ Disadvantages</th>
                        </tr>
                    </thead>
                    <tbody style="color: #475569;">
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Bank Loan</td>
                            <td style="padding: 10px 14px;">Predictable monthly repayments. Retains 100% owner equity control.</td>
                            <td style="padding: 10px 14px;">Fixed interest burden; commercial bank requires physical property collateral.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Hire Purchase / Leasing</td>
                            <td style="padding: 10px 14px;">Avoids massive upfront capital outlay. Lessor updates equipment regularly.</td>
                            <td style="padding: 10px 14px;">Total rental payments exceed original purchase cost; business does not own asset under lease.</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #e2e8f0;">
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Share Issue (Equity)</td>
                            <td style="padding: 10px 14px;">Permanent capital with zero repayment debt and no mandatory interest charges.</td>
                            <td style="padding: 10px 14px;">Dilutes existing owner voting control; available strictly to Ltd / Plc companies.</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px 14px; font-weight: bold; color: #0f172a;">Debentures</td>
                            <td style="padding: 10px 14px;">Ultra-long term debt (up to 25 years) with no ownership equity dilution.</td>
                            <td style="padding: 10px 14px;">Mandatory coupon interest must be paid regardless of annual profit or loss.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- 3. INTERNAL VS EXTERNAL SOURCES -->
    <div style="margin-bottom: 50px;">
        <div id="sec-internal-external" class="lecture-interactive-card" data-lecture-section="sec_internal_external" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #ec4899; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🔄 3. INTERNAL vs EXTERNAL SOURCES</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Finance is classified according to whether funds originate inside existing operational accounts or are drawn from outside financial providers.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <!-- SUB-CARD: INTERNAL SOURCES -->
            <div id="card-internal-sources" class="lecture-interactive-card" data-lecture-section="card_internal_sources" style="background: #ffffff; border: 1.5px solid #fbcfe8; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <div style="background: #fdf2f8; padding: 18px 22px; border-bottom: 1px solid #fbcfe8; display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <h3 style="margin: 0; color: #be185d; font-size: 18px; font-weight: 700;">🏠 Internal Finance</h3>
                        <p style="margin: 3px 0 0 0; font-size: 13px; color: #831843;">Capital sourced entirely from <b>within</b> the company.</p>
                    </div>
                    <span style="font-size: 11px; font-weight: 700; background: #fff1f2; color: #be185d; padding: 4px 10px; border-radius: 6px; border: 1px solid #fbcfe8;">Nghe thẻ này</span>
                </div>
                <div style="padding: 18px 22px;">
                    <ul style="margin: 0 0 16px 0; padding-left: 18px; color: #475569; font-size: 13px; line-height: 1.6;">
                        <li><b>Owner's Capital:</b> Personal savings introduced at founding.</li>
                        <li><b>Retained Profit:</b> Reinvesting cumulative annual profits (0% interest).</li>
                        <li><b>Sale of Assets:</b> Selling surplus land/machinery (or sale and leaseback).</li>
                        <li><b>Working Capital Optimization:</b> Speeding up invoice collections from debtors.</li>
                    </ul>
                    <div style="font-size: 12.5px; background: #fdf2f8; padding: 10px 14px; border-radius: 8px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Zero interest, no debt default risk, retains 100% control.<br/>
                        <b style="color: #dc2626;">❌ Cons:</b> Startup firms lack retained profit; asset sales permanently diminish capacity.
                    </div>
                </div>
            </div>

            <!-- SUB-CARD: EXTERNAL SOURCES -->
            <div id="card-external-sources" class="lecture-interactive-card" data-lecture-section="card_external_sources" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; overflow: hidden; box-shadow: 0 3px 10px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
                <div style="background: #eff6ff; padding: 18px 22px; border-bottom: 1px solid #bfdbfe; display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <h3 style="margin: 0; color: #1d4ed8; font-size: 18px; font-weight: 700;">🌍 External Finance</h3>
                        <p style="margin: 3px 0 0 0; font-size: 13px; color: #1e40af;">Capital injected from external market institutions.</p>
                    </div>
                    <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
                </div>
                <div style="padding: 18px 22px;">
                    <ul style="margin: 0 0 16px 0; padding-left: 18px; color: #475569; font-size: 13px; line-height: 1.6;">
                        <li>Required when internal profit pools cannot finance large-scale projects.</li>
                        <li><b>Commercial Banks:</b> Overdraft facilities, mortgages, and fixed-term loans.</li>
                        <li><b>Suppliers &amp; Factors:</b> Trade credit, hire purchase, and debtor factoring.</li>
                        <li><b>Capital Markets:</b> New equity share issues and corporate debentures.</li>
                        <li><b>Government Grants:</b> Regional incentives (strict job creation conditions).</li>
                    </ul>
                    <div style="font-size: 12.5px; background: #eff6ff; padding: 10px 14px; border-radius: 8px;">
                        <b style="color: #1e40af;">💡 Exam Tip:</b> Always weigh gearing debt risk against owner voting power dilution.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. ALTERNATIVE SOURCES -->
    <div style="margin-bottom: 50px;">
        <div id="sec-alternative-sources" class="lecture-interactive-card" data-lecture-section="sec_alternative_sources" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f59e0b; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💡 4. ALTERNATIVE SOURCES OF FINANCE</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Modern digital platforms and fintech institutions offer specialized funding pathways beyond traditional banking.
            </p>
        </div>

        <!-- SUB-CARD: CROWDFUNDING & MICROFINANCE -->
        <div id="card-crowdfunding-micro" class="lecture-interactive-card" data-lecture-section="card_crowdfunding_micro" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">🌐 Crowdfunding vs Microfinance vs Venture Capital</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #d97706; font-size: 16px; margin: 0 0 8px 0;">🌐 Crowdfunding</h4>
                    <p style="margin: 0 0 10px 0; font-size: 13px; color: #92400e;">
                        Online portal aggregation (e.g. Kickstarter) raising small sums from thousands of individuals.
                    </p>
                    <div style="font-size: 12.5px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Tests public market demand; zero mandatory bank interest.<br/>
                        <b style="color: #dc2626;">❌ Cons:</b> "All-or-nothing" targets; exposes IP design to competitors.
                    </div>
                </div>

                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 16px;">
                    <h4 style="color: #15803d; font-size: 16px; margin: 0 0 8px 0;">🌱 Microfinance</h4>
                    <p style="margin: 0 0 10px 0; font-size: 13px; color: #166534;">
                        Micro-loans offered to low-income entrepreneurs in developing economies excluded from traditional banking.
                    </p>
                    <div style="font-size: 12.5px;">
                        <b style="color: #16a34a;">✅ Pros:</b> Unlocks financial inclusion and female entrepreneur empowerment.<br/>
                        <b style="color: #dc2626;">❌ Cons:</b> Very small capital limits; inadequate for high-tech capital ventures.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. CHOOSING THE BEST TYPE OF FINANCE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-choosing-finance" class="lecture-interactive-card" data-lecture-section="sec_choosing_finance" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #99f6e4; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <h2 style="color: #0f766e; margin: 0; font-size: 22px; font-weight: 700;">🎯 5. CHOOSING THE BEST TYPE OF FINANCE</h2>
                <span style="font-size: 11px; font-weight: 700; background: #f0fdfa; color: #0f766e; padding: 4px 10px; border-radius: 6px; border: 1px solid #99f6e4;">Nghe thẻ này</span>
            </div>
            <div style="background: #f0fdfa; border-left: 4px solid #0d9488; padding: 14px 18px; border-radius: 4px; font-size: 14.5px; color: #0f766e; margin-bottom: 16px;">
                Managers evaluate six key dimensions before selecting their funding combination:
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 16px;">
                <div style="background: #ffffff; border: 1px solid #ccfbf1; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b>1. Purpose &amp; Duration:</b> Short-term needs = Overdraft. Long-term equipment = Bank Loan or Leasing.
                </div>
                <div style="background: #ffffff; border: 1px solid #ccfbf1; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b>2. Amount Needed:</b> Small sums = Credit card / Trade credit. Millions = Share Issue.
                </div>
                <div style="background: #ffffff; border: 1px solid #ccfbf1; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b>3. Legal Structure:</b> Sole traders cannot issue shares; only Plcs trade openly on stock markets.
                </div>
                <div style="background: #ffffff; border: 1px solid #ccfbf1; padding: 12px 16px; border-radius: 8px; font-size: 13px;">
                    <b>4. Control vs Gearing:</b> Borrowing keeps owner control but increases debt interest risk.
                </div>
            </div>
        </div>
    </div>

    <!-- 6. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-recommend-finance" class="lecture-interactive-card" data-lecture-section="sec_recommend_finance" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 6. HOW TO RECOMMEND &amp; JUSTIFY SOURCES OF FINANCE (Cambridge Exam Guide)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Exam questions frequently ask: <i>"Recommend and justify the most suitable source of finance for this business in the given circumstances."</i>
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 18px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #1e40af; font-size: 15px;">Short-term Liquidity Gaps:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Recommend <b>Bank Overdraft</b> or <b>Trade Credit</b>. Quick and flexible for cash deficits, avoiding permanent ownership dilution.
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #10b981; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #047857; font-size: 15px;">Long-term Capital Purchases:</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Recommend <b>Retained Profit</b> (0% interest, no equity surrender) or a <b>Long-term Bank Loan</b> (repayments spread over 5–10 years).
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 10px; border-left: 4px solid #f59e0b; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                    <b style="color: #b45309; font-size: 15px;">Large Scale Expansion (Ltd / Plc):</b>
                    <p style="margin: 6px 0 0 0; font-size: 13px; color: #334155; line-height: 1.5;">
                        Recommend <b>Share Issues</b>. Injects vast permanent capital without adding high debt gearing or interest payment obligations.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">5.1 Business Finance: Needs and Sources (Nhu cầu &amp; Nguồn vốn)</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 5.1 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/5_1_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 5.1 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
