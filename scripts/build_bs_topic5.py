import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# LECTURE 5.1: Business Finance: Needs and Sources
# ==============================================================================
async def build_5_1():
    lid = '7b510a8f-757c-4856-9c68-65f98bf96836'
    code = '5_1'
    title = '5.1. Business Finance: Needs and Sources'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-need-finance" class="lecture-interactive-card" data-lecture-section="sec_need_finance" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-short-long-term" class="lecture-interactive-card" data-lecture-section="sec_short_long_term" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-internal-external" class="lecture-interactive-card" data-lecture-section="sec_internal_external" style="cursor: pointer; ')
    
    t_h3_int = str(h3s[2])
    r_h3_int = t_h3_int.replace('<h3', '<h3 id="card-internal-sources" class="lecture-interactive-card" data-lecture-section="card_internal_sources" style="cursor: pointer; ')
    
    t_h3_ext = str(h3s[3])
    r_h3_ext = t_h3_ext.replace('<h3', '<h3 id="card-external-sources" class="lecture-interactive-card" data-lecture-section="card_external_sources" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-alternative-sources" class="lecture-interactive-card" data-lecture-section="sec_alternative_sources" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-choosing-finance" class="lecture-interactive-card" data-lecture-section="sec_choosing_finance" style="cursor: pointer; ')
    
    t_h2_6 = str(h2s[5])
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-recommend-finance" class="lecture-interactive-card" data-lecture-section="sec_recommend_finance" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h3_int, r_h3_int, 1)\
                   .replace(t_h3_ext, r_h3_ext, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)\
                   .replace(t_h2_6, r_h2_6, 1)

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
            "id": "sec_short_long_term",
            "title": "2. Nhu cầu Vốn Ngắn hạn và Dài hạn",
            "selector": "#sec-short-long-term",
            "en": "Section 2 matches financing durations to asset life. Short-term finance, under one year, bridges immediate liquidity deficits via bank overdrafts and trade credit. Long-term finance, extending beyond five years, funds major capital assets through bank mortgages, debentures, and issuing equity share capital.",
            "vi": "Mục hai ghép nối thời hạn vay vốn với tuổi thọ của tài sản. Vốn ngắn hạn dưới một năm bù đắp thiếu hụt thanh khoản tạm thời qua thấu chi ngân hàng và tín dụng thương mại. Vốn dài hạn trên năm năm tài trợ cho các tài sản cố định lớn thông qua các khoản vay thế chấp ngân hàng, trái phiếu doanh nghiệp và phát hành cổ phiếu mới."
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
            "title": "Ưu nhược điểm của Nguồn vốn Nội bộ",
            "selector": "#card-internal-sources",
            "en": "Internal finance incurs zero interest charges, requires no debt collateral, and maintains 100% owner control. However, newly formed startups lack retained earnings, and selling essential factory machinery permanently degrades production capacity.",
            "vi": "Vốn nội bộ không phát sinh chi phí lãi vay, không cần thế chấp tài sản và duy trì trọn vẹn quyền kiểm soát của chủ sở hữu. Tuy nhiên, các công ty mới thành lập chưa có lợi nhuận tích lũy, và việc bán máy móc thiết bị thiết yếu có thể làm suy giảm nghiêm trọng năng lực sản xuất."
        },
        {
            "id": "card_external_sources",
            "title": "Các Kênh Vốn Bên ngoài Cốt lõi",
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
    
    major_sections = [
        {"id": "sec_need_finance", "title": "1. Nhu cầu Vốn Doanh nghiệp"},
        {"id": "sec_short_long_term", "title": "2. Thời hạn Vốn (Ngắn hạn & Dài hạn)"},
        {"id": "sec_internal_external", "title": "3. Nguồn vốn Nội bộ và Bên ngoài"},
        {"id": "sec_alternative_sources", "title": "4. Vốn Thay thế (Crowdfunding, Venture Capital)"},
        {"id": "sec_choosing_finance", "title": "5. Tiêu chí Lựa chọn & Chiến lược thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 5.1 successfully built!")


# ==============================================================================
# LECTURE 5.2: Cash flow forecasting and working capital
# ==============================================================================
async def build_5_2():
    lid = 'dc0411df-d831-468a-9a7d-16fb4009290d'
    code = '5_2'
    title = '5.2. Cash flow forecasting and working capital'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-cash-flow-forecasts" class="lecture-interactive-card" data-lecture-section="sec_cash_flow_forecasts" style="cursor: pointer; ')
    
    t_h3_cycle = str(h3s[0])
    r_h3_cycle = t_h3_cycle.replace('<h3', '<h3 id="card-cashflow-cycle" class="lecture-interactive-card" data-lecture-section="card_cashflow_cycle" style="cursor: pointer; ')
    
    t_h3_formulas = str(h3s[1])
    r_h3_formulas = t_h3_formulas.replace('<h3', '<h3 id="card-cashflow-formulas" class="lecture-interactive-card" data-lecture-section="card_cashflow_formulas" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-working-capital" class="lecture-interactive-card" data-lecture-section="sec_working_capital" style="cursor: pointer; ')
    
    t_h2_6 = str(h2s[5])
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-overcome-cashflow" class="lecture-interactive-card" data-lecture-section="sec_overcome_cashflow" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_cycle, r_h3_cycle, 1)\
                   .replace(t_h3_formulas, r_h3_formulas, 1)\
                   .replace(t_h2_5, r_h2_5, 1)\
                   .replace(t_h2_6, r_h2_6, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5.2: Dự báo Dòng tiền và Vốn lưu động",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 5.2: Cash Flow Forecasting and Working Capital. In this vital chapter, we unpack the cash flow cycle, construct cash flow forecasts, calculate closing balances, define working capital, and implement corrective measures to overcome liquidity insolvency.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 5.2: Dự báo Dòng tiền và Vốn lưu động. Trong bài học then chốt này, chúng ta sẽ khảo sát chu chuyển dòng tiền, lập bảng dự báo dòng tiền, tính số dư cuối kỳ, quản trị vốn lưu động và các biện pháp giải quyết khủng hoảng thanh khoản."
        },
        {
            "id": "sec_cash_flow_forecasts",
            "title": "1. Bản chất của Dự báo Dòng tiền",
            "selector": "#sec-cash-flow-forecasts",
            "en": "Section 1 defines a Cash Flow Forecast as an estimate of future cash inflows and cash outflows of a business on a month-by-month basis. Forecasting anticipates cash deficits well in advance, allowing managers to arrange bank overdrafts before payroll defaults occur.",
            "vi": "Mục một định nghĩa Bảng dự báo dòng tiền là ước tính các khoản tiền mặt thực thu vào và chi ra của doanh nghiệp theo từng tháng trong tương lai. Dự báo giúp phát hiện sớm nguy cơ thiếu hụt tiền mặt để chủ động xin hạn mức thấu chi ngân hàng trước khi xảy ra chậm lương nhân viên."
        },
        {
            "id": "card_cashflow_cycle",
            "title": "Vòng chu chuyển Dòng tiền (The Cash Flow Cycle)",
            "selector": "#card-cashflow-cycle",
            "en": "The Cash Flow Cycle shows how cash is converted into raw materials, transformed into work-in-progress, delivered to trade credit customers as trade receivables, and eventually recollected as cash. The longer this cycle takes, the greater the working capital tied up.",
            "vi": "Vòng chu chuyển dòng tiền mô tả quá trình tiền mặt được dùng để mua nguyên liệu, đưa vào sản xuất dở dang, bán cho khách hàng nợ tiền (khoản phải thu) và cuối cùng thu hồi lại thành tiền mặt. Chu kỳ này càng kéo dài thì lượng vốn lưu động bị ứ đọng càng lớn."
        },
        {
            "id": "card_cashflow_formulas",
            "title": "Công thức Tính toán Dòng tiền Chuẩn Cambridge",
            "selector": "#card-cashflow-formulas",
            "en": "Master three core formulas: Net Cash Flow equals Total Cash Inflows minus Total Cash Outflows; Closing Bank Balance equals Opening Bank Balance plus Net Cash Flow; and Opening Balance of month two always equals Closing Balance of month one.",
            "vi": "Nắm vững ba công thức tính cốt lõi: Dòng tiền thuần (Net Cash Flow) bằng Tổng thu trừ Tổng chi; Số dư cuối kỳ bằng Số dư đầu kỳ cộng Dòng tiền thuần; và Số dư đầu kỳ của tháng sau luôn bằng chính Số dư cuối kỳ của tháng trước."
        },
        {
            "id": "sec_working_capital",
            "title": "2. Vai trò Sống còn của Vốn lưu động (Working Capital)",
            "selector": "#sec-working-capital",
            "en": "Section 2 defines Working Capital as Current Assets minus Current Liabilities. Known as the lifeblood of day-to-day operations, adequate working capital guarantees prompt settlement of supplier bills and prevents bankruptcy due to sudden illiquidity.",
            "vi": "Mục hai định nghĩa Vốn lưu động bằng Tài sản ngắn hạn trừ Nợ ngắn hạn. Được ví như mạch máu nuôi dưỡng hoạt động thường nhật, vốn lưu động đầy đủ bảo đảm thanh toán đúng hạn cho nhà cung cấp và ngăn ngừa nguy cơ phá sản do mất khả năng thanh toán tức thời."
        },
        {
            "id": "sec_overcome_cashflow",
            "title": "3. Giải pháp Khắc phục Khủng hoảng Dòng tiền",
            "selector": "#sec-overcome-cashflow",
            "en": "Section 3 evaluates methods to overcome cash flow crises: negotiating extended supplier trade credit, factoring debtor invoices for immediate 80% cash advances, selling off obsolete inventory at discount, and delaying non-essential capital equipment investments.",
            "vi": "Mục ba đánh giá các giải pháp ứng phó khủng hoảng dòng tiền: đàm phán kéo dài thời hạn nợ với nhà cung cấp, bán các hóa đơn nợ cho công ty bao thanh toán (debt factoring) để lấy ngay tiền mặt, giảm giá xả hàng tồn kho ứ đọng và hoãn mua sắm các thiết bị máy móc chưa thực sự cần thiết."
        }
    ]
    
    major_sections = [
        {"id": "sec_cash_flow_forecasts", "title": "1. Bản chất & Chu kỳ Dòng tiền"},
        {"id": "sec_working_capital", "title": "2. Quản trị Vốn lưu động (Working Capital)"},
        {"id": "sec_overcome_cashflow", "title": "3. Giải pháp Xử lý Khủng hoảng Dòng tiền"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 5.2 successfully built!")


# ==============================================================================
# LECTURE 5.3: Income statements
# ==============================================================================
async def build_5_3():
    lid = '71f25939-98d4-4fa3-8227-be8434f64581'
    code = '5_3'
    title = '5.3. Income statements'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-profit-importance" class="lecture-interactive-card" data-lecture-section="sec_profit_importance" style="cursor: pointer; ')
    
    t_h3_pc = str(h3s[5])
    r_h3_pc = t_h3_pc.replace('<h3', '<h3 id="card-profit-vs-cash" class="lecture-interactive-card" data-lecture-section="card_profit_vs_cash" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-income-statement" class="lecture-interactive-card" data-lecture-section="sec_income_statement" style="cursor: pointer; ')
    
    t_h3_struct = str(h3s[6])
    r_h3_struct = t_h3_struct.replace('<h3', '<h3 id="card-income-structure" class="lecture-interactive-card" data-lecture-section="card_income_structure" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-income-decision" class="lecture-interactive-card" data-lecture-section="sec_income_decision" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h3_pc, r_h3_pc, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h3_struct, r_h3_struct, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

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
            "title": "1. Tầm quan trọng của Lợi nhuận",
            "selector": "#sec-profit-importance",
            "en": "Section 1 defines profit as total revenue minus total operating costs over a trading period. Profit acts as a reward for enterprise risk-taking, provides vital internal finance for retained reinvestment, and serves as a barometer of managerial competence.",
            "vi": "Mục một định nghĩa lợi nhuận là tổng doanh thu trừ đi tổng chi phí hoạt động trong một kỳ kinh doanh. Lợi nhuận là phần thưởng cho việc chấp nhận rủi ro kinh doanh, cung cấp nguồn vốn nội bộ để tái đầu tư mở rộng và là thước đo chuẩn xác năng lực điều hành của ban giám đốc."
        },
        {
            "id": "card_profit_vs_cash",
            "title": "Phân biệt Lợi nhuận đối chiếu với Dòng tiền (Profit vs Cash)",
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
            "title": "Phân bổ Lợi nhuận ròng: Cổ tức và Lợi nhuận giữ lại",
            "selector": "#card-income-structure",
            "en": "Profit for the Year is allocated between Dividends distributed to reward shareholders, and Retained Profit plowed back into the corporate balance sheet to finance future growth.",
            "vi": "Lợi nhuận ròng sau thuế được phân bổ thành Cổ tức (Dividends) chi trả để tri ân cổ đông, và Lợi nhuận giữ lại (Retained Profit) được giữ lại trên bảng cân đối kế toán để tài trợ cho các dự án tăng trưởng trong tương lai."
        },
        {
            "id": "sec_income_decision",
            "title": "3. Sử dụng Báo cáo Thu nhập để Ra Quyết định Quản trị",
            "selector": "#sec-income-decision",
            "en": "Section 3 evaluates how managers interpret income statements: comparing year-on-year gross margin trends to detect rising raw material supplier prices, and auditing overhead ratios to eliminate administrative waste.",
            "vi": "Mục ba đánh giá cách thức ban quản trị phân tích báo cáo thu nhập: so sánh biên lợi nhuận gộp qua các năm để phát hiện tình trạng nhà cung cấp tăng giá nguyên liệu, và kiểm soát tỷ lệ chi phí quản lý nhằm cắt giảm lãng phí hành chính."
        }
    ]
    
    major_sections = [
        {"id": "sec_profit_importance", "title": "1. Tầm quan trọng Lợi nhuận"},
        {"id": "card_profit_vs_cash", "title": "2. Phân biệt Lợi nhuận và Tiền mặt"},
        {"id": "sec_income_statement", "title": "3. Cấu trúc Báo cáo Thu nhập"},
        {"id": "sec_income_decision", "title": "4. Ra Quyết định dựa trên Báo cáo"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 5.3 successfully built!")


# ==============================================================================
# LECTURE 5.4: Statement of financial position
# ==============================================================================
async def build_5_4():
    lid = '5421db93-9d7b-4241-b362-171974092a30'
    code = '5_4'
    title = '5.4. Statement of financial position'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-balance-sheet" class="lecture-interactive-card" data-lecture-section="sec_balance_sheet" style="cursor: pointer; ')
    
    t_h3_assets = str(h3s[0])
    r_h3_assets = t_h3_assets.replace('<h3', '<h3 id="card-assets" class="lecture-interactive-card" data-lecture-section="card_assets" style="cursor: pointer; ')
    
    t_h3_liab = str(h3s[1])
    r_h3_liab = t_h3_liab.replace('<h3', '<h3 id="card-liabilities" class="lecture-interactive-card" data-lecture-section="card_liabilities" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-using-balance-sheet" class="lecture-interactive-card" data-lecture-section="sec_using_balance_sheet" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-interpret-balance-sheet" class="lecture-interactive-card" data-lecture-section="sec_interpret_balance_sheet" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_assets, r_h3_assets, 1)\
                   .replace(t_h3_liab, r_h3_liab, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

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
            "title": "Tài sản: Tài sản Dài hạn và Tài sản Ngắn hạn",
            "selector": "#card-assets",
            "en": "Assets represent items of value owned by the business. Non-current assets are tangible resources held for longer than one year, such as land, factories, and vehicles. Current assets are short-term resources converted into cash within twelve months: inventory, trade receivables, and bank balances.",
            "vi": "Tài sản là những nguồn lực có giá trị thuộc quyền sở hữu của doanh nghiệp. Tài sản dài hạn (Non-current assets) có thời gian sử dụng trên một năm như đất đai, nhà xưởng, xe cộ. Tài sản ngắn hạn (Current assets) chuyển hóa thành tiền trong vòng 12 tháng: hàng tồn kho, khoản phải thu khách hàng và tiền gửi ngân hàng."
        },
        {
            "id": "card_liabilities",
            "title": "Nợ phải trả: Nợ Ngắn hạn và Nợ Dài hạn",
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
            "id": "sec_interpret_balance_sheet",
            "title": "3. Phân tích Bảng Cân đối Kế toán theo chuẩn Cambridge",
            "selector": "#sec-interpret-balance-sheet",
            "en": "Section 3 evaluates capital employed and shareholder funds. Candidates must evaluate capital structure: high debt gearing exposes the firm to interest rate surges, while healthy equity reserves provide solid financial resilience.",
            "vi": "Mục ba đánh giá vốn hoạt động (capital employed) và vốn chủ sở hữu. Thí sinh cần phân tích cơ cấu vốn: tỷ lệ nợ vay quá cao khiến doanh nghiệp dễ tổn thương trước biến động lãi suất, trong khi nguồn vốn chủ sở hữu dồi dào tạo nền tảng tài chính vững chắc."
        }
    ]
    
    major_sections = [
        {"id": "sec_balance_sheet", "title": "1. Bản chất Bảng Cân đối Kế toán"},
        {"id": "card_assets", "title": "2. Tài sản Dài hạn & Ngắn hạn"},
        {"id": "card_liabilities", "title": "3. Nợ Dài hạn & Ngắn hạn"},
        {"id": "sec_using_balance_sheet", "title": "4. Phân tích Thanh khoản & Vốn chủ sở hữu"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 5.4 successfully built!")


# ==============================================================================
# LECTURE 5.5: Analysis of accounts
# ==============================================================================
async def build_5_5():
    lid = 'd7564fe9-d338-4abc-acf3-affd8cca23fa'
    code = '5_5'
    title = '5.5. Analysis of accounts'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-profitability-liquidity" class="lecture-interactive-card" data-lecture-section="sec_profitability_liquidity" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-profitability-ratios" class="lecture-interactive-card" data-lecture-section="sec_profitability_ratios" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-liquidity-ratios" class="lecture-interactive-card" data-lecture-section="sec_liquidity_ratios" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-stakeholders-accounts" class="lecture-interactive-card" data-lecture-section="sec_stakeholders_accounts" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-evaluate-ratios" class="lecture-interactive-card" data-lecture-section="sec_evaluate_ratios" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

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
            "id": "sec_liquidity_ratios",
            "title": "3. Hai Chỉ số Khả năng Thanh toán (Liquidity Ratios)",
            "selector": "#sec-liquidity-ratios",
            "en": "Section 3 calculates liquidity: The Current Ratio equals Current Assets divided by Current Liabilities, with 1.5 to 2.0 considered healthy. The Acid Test Ratio excludes illiquid inventory: Current Assets minus Inventory divided by Current Liabilities. An Acid Test below 1.0 indicates severe working capital vulnerability.",
            "vi": "Mục ba tính toán khả năng thanh toán: Tỷ số hiện hành bằng Tài sản ngắn hạn chia Nợ ngắn hạn, mức lý tưởng là từ 1,5 đến 2,0. Tỷ số thanh toán nhanh (Acid Test) loại bỏ hàng tồn kho khó bán: bằng Tài sản ngắn hạn trừ Hàng tồn kho, tất cả chia cho Nợ ngắn hạn. Tỷ số Acid Test dưới 1,0 cảnh báo nguy cơ cạn kiệt thanh khoản nghiêm trọng."
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
            "vi": "Mục năm chỉ ra các giới hạn của chỉ số tài chính: báo cáo chỉ phản ánh số liệu lịch sử trong quá khứ, lạm phát làm sai lệch giá trị tài sản, thủ thuật kế toán có thể che giấu rủi ro và các chỉ số hoàn toàn bỏ qua các yếu tố định tính quan trọng như tinh thần nhân viên và lòng trung thành của khách hàng."
        }
    ]
    
    major_sections = [
        {"id": "sec_profitability_liquidity", "title": "1. Khái niệm Sinh lời & Thanh khoản"},
        {"id": "sec_profitability_ratios", "title": "2. Chỉ số Sinh lời (Gross Margin, Profit Margin, ROCE)"},
        {"id": "sec_liquidity_ratios", "title": "3. Chỉ số Thanh khoản (Current & Acid-Test Ratio)"},
        {"id": "sec_stakeholders_accounts", "title": "4. Các Bên liên quan & Giới hạn Báo cáo"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 5.5 successfully built!")


# ==============================================================================
# MAIN BATCH RUNNER FOR TOPIC 5
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING TOPIC 5 BUILD: ALL 5 LECTURES (5.1 -> 5.5)")
    print("*******************************************************\n")
    
    await build_5_1()
    await asyncio.sleep(2)
    
    await build_5_2()
    await asyncio.sleep(2)
    
    await build_5_3()
    await asyncio.sleep(2)
    
    await build_5_4()
    await asyncio.sleep(2)
    
    await build_5_5()
    
    print("\n*******************************************************")
    print("TOPIC 5 COMPLETE: ALL 5 LECTURES PROCESSED SUCCESSFULLY!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
