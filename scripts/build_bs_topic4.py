import sys
import os
import json
import asyncio
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb, process_lecture_audio, update_supabase_page

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# LECTURE 4.1: Production of goods and services
# ==============================================================================
async def build_4_1():
    lid = '1e280547-ce64-44c2-8fcf-997f7d61cacf'
    code = '4_1'
    title = '4.1. Production of goods and services'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-production-productivity" class="lecture-interactive-card" data-lecture-section="sec_production_productivity" style="cursor: pointer; ')
    
    t_h3_prod = str(h3s[1])
    r_h3_prod = t_h3_prod.replace('<h3', '<h3 id="card-productivity" class="lecture-interactive-card" data-lecture-section="card_productivity" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-inventory" class="lecture-interactive-card" data-lecture-section="sec_inventory" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-lean-production" class="lecture-interactive-card" data-lecture-section="sec_lean_production" style="cursor: pointer; ')
    
    t_h3_lean = str(h3s[3])
    r_h3_lean = t_h3_lean.replace('<h3', '<h3 id="card-lean-methods" class="lecture-interactive-card" data-lecture-section="card_lean_methods" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-methods-production" class="lecture-interactive-card" data-lecture-section="sec_methods_production" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-tech-production" class="lecture-interactive-card" data-lecture-section="sec_tech_production" style="cursor: pointer; ')
    
    t_h2_6 = str(h2s[5])
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-recommend-production" class="lecture-interactive-card" data-lecture-section="sec_recommend_production" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_prod, r_h3_prod, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h3_lean, r_h3_lean, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)\
                   .replace(t_h2_6, r_h2_6, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.1: Sản xuất Hàng hóa và Dịch vụ",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.1: Production of Goods and Services. In this opening chapter of Topic 4, Operations Management, we explore productivity metrics, inventory control, lean production techniques, job, batch, and flow production methods, and modern manufacturing automation.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.1: Sản xuất Hàng hóa và Dịch vụ. Trong bài mở đầu của Chủ đề bốn về Quản trị Vận hành, chúng ta sẽ khảo sát các chỉ số đo lường năng suất, quản lý hàng tồn kho, phương pháp sản xuất tinh gọn (lean), các hình thức sản xuất đơn chiếc, theo lô, liên tục và tự động hóa nhà máy."
        },
        {
            "id": "sec_production_productivity",
            "title": "1. Sản xuất và Năng suất lao động",
            "selector": "#sec-production-productivity",
            "en": "Section 1 distinguishes production—the absolute volume of output produced—from productivity, which measures output per unit of input over time. Boosting labour productivity drives down average unit costs, enhancing price competitiveness and widening profit margins.",
            "vi": "Mục một phân biệt giữa sản lượng sản xuất (production) – tổng số lượng hàng hóa tạo ra – với năng suất (productivity), là sản lượng tính trên một đơn vị đầu vào theo thời gian. Nâng cao năng suất lao động giúp kéo giảm chi phí sản xuất trên mỗi đơn vị sản phẩm, gia tăng năng lực cạnh tranh về giá và mở rộng biên lợi nhuận."
        },
        {
            "id": "card_productivity",
            "title": "Công thức tính Năng suất và Giải pháp nâng cao",
            "selector": "#card-productivity",
            "en": "Productivity equals Total Output divided by Total Inputs such as labour hours or capital machines. Ways to increase productivity include: upgrading employee training, modernizing machinery, automating repetitive tasks, and motivating staff through productivity-linked incentives.",
            "vi": "Năng suất được tính bằng Tổng sản lượng đầu ra chia cho Tổng đầu vào như giờ công lao động hoặc số máy móc. Các giải pháp nâng cao năng suất gồm: đào tạo chuyên môn cho công nhân, hiện đại hóa máy móc thiết bị, tự động hóa các khâu lặp đi lặp lại và khuyến khích tài chính gắn liền với năng suất."
        },
        {
            "id": "sec_inventory",
            "title": "2. Quản lý Hàng tồn kho",
            "selector": "#sec-inventory",
            "en": "Section 2 investigates inventory management: raw materials, work-in-progress, and finished goods. Holding buffer inventories ensures smooth operations against delivery delays but locks up working capital in storage, insurance, and obsolescence risks.",
            "vi": "Mục hai nghiên cứu quản trị hàng tồn kho: nguyên vật liệu thô, sản phẩm dở dang trên dây chuyền và thành phẩm hoàn chỉnh. Duy trì lượng hàng dự trữ giúp sản xuất liên tục không bị gián đoạn nhưng gây ứ đọng vốn lưu động, tốn chi phí thuê kho bãi, bảo hiểm và đối mặt rủi ro hàng hóa lỗi thời."
        },
        {
            "id": "sec_lean_production",
            "title": "3. Sản xuất Tinh gọn (Lean Production)",
            "selector": "#sec-lean-production",
            "en": "Section 3 explores Lean Production: operational philosophies aimed at cutting waste and eliminating non-value-adding activities across seven dimensions: overproduction, waiting, transportation, unnecessary inventory, excessive motion, overprocessing, and defects.",
            "vi": "Mục ba tìm hiểu Sản xuất tinh gọn (Lean Production): triết lý vận hành nhằm cắt giảm lãng phí và loại bỏ các hoạt động không tạo ra giá trị gia tăng trên bảy khía cạnh: sản xuất thừa, thời gian chờ đợi, vận chuyển không cần thiết, tồn kho dư thừa, thao tác thừa, xử lý quá mức và hàng lỗi hỏng."
        },
        {
            "id": "card_lean_methods",
            "title": "Các Kỹ thuật Lean cốt lõi: JIT và Kaizen",
            "selector": "#card-lean-methods",
            "en": "Key lean techniques include Just-In-Time (JIT)—where materials arrive exactly as required on the assembly line, eliminating warehouse storage entirely; and Kaizen, continuous Japanese incremental improvement driven by frontline employee feedback circles.",
            "vi": "Các kỹ thuật tinh gọn cốt lõi gồm Sản xuất đúng thời điểm (Just-In-Time - JIT) – nguyên vật liệu được giao đúng lúc cần ráp vào dây chuyền, xóa bỏ hoàn toàn chi phí lưu kho; và Kaizen, triết lý cải tiến liên tục từng bước nhỏ của Nhật Bản dựa trên sự đóng góp ý kiến của chính những người công nhân đứng máy."
        },
        {
            "id": "sec_methods_production",
            "title": "4. Ba Phương pháp Sản xuất: Job, Batch và Flow",
            "selector": "#sec-methods-production",
            "en": "Section 4 compares three core manufacturing methods: Job production crafts single customized items like wedding dresses; Batch production creates identical groups of products before resetting equipment, as in bakeries; Flow continuous mass production runs non-stop assembly lines like car factories, yielding massive economies of scale.",
            "vi": "Mục bốn so sánh ba phương pháp sản xuất: Sản xuất đơn chiếc (Job) làm theo yêu cầu cá nhân hóa như may váy cưới; Sản xuất theo lô (Batch) tạo ra từng mẻ sản phẩm giống nhau trước khi chuyển đổi máy móc như tiệm bánh; Sản xuất liên tục (Flow) vận hành dây chuyền tự động hàng loạt 24/7 như lắp ráp ô tô, đạt hiệu quả quy mô tối đa."
        },
        {
            "id": "sec_tech_production",
            "title": "5. Công nghệ trong Sản xuất: CAD, CAM và CIM",
            "selector": "#sec-tech-production",
            "en": "Section 5 evaluates technological innovation: Computer-Aided Design (CAD) for digital prototyping; Computer-Aided Manufacturing (CAM) utilizing industrial robots; and Computer-Integrated Manufacturing (CIM) unifying entire factories under integrated software controllers.",
            "vi": "Mục năm đánh giá sự đổi mới công nghệ: Thiết kế có sự trợ giúp của máy tính (CAD) giúp phác thảo mẫu kỹ thuật số 3D; Sản xuất có sự trợ giúp của máy tính (CAM) sử dụng robot công nghiệp; và Sản xuất tích hợp máy tính (CIM) đồng bộ hóa toàn bộ nhà máy dưới sự điều khiển của hệ thống phần mềm trung tâm."
        },
        {
            "id": "sec_recommend_production",
            "title": "6. Chiến lược làm bài thi Cambridge: Đề xuất Phương pháp Sản xuất",
            "selector": "#sec-recommend-production",
            "en": "Section 6 details the Cambridge evaluation strategy for production methods. Candidates must analyze market demand volume, product customization requirements, and capital budget before justifying the optimal manufacturing method.",
            "vi": "Mục sáu hướng dẫn chiến lược trả lời câu hỏi Cambridge về phương pháp sản xuất. Thí sinh phải phân tích quy mô nhu cầu thị trường, mức độ tùy biến sản phẩm theo yêu cầu khách hàng và ngân sách đầu tư thiết bị trước khi đưa ra khuyến nghị lựa chọn phương án tối ưu."
        }
    ]
    
    major_sections = [
        {"id": "sec_production_productivity", "title": "1. Năng suất lao động (Productivity)"},
        {"id": "sec_inventory", "title": "2. Quản lý Tồn kho"},
        {"id": "sec_lean_production", "title": "3. Sản xuất Tinh gọn (Lean, JIT, Kaizen)"},
        {"id": "sec_methods_production", "title": "4. Ba Phương pháp Sản xuất (Job, Batch, Flow)"},
        {"id": "sec_tech_production", "title": "5. Công nghệ Sản xuất (CAD, CAM, CIM)"},
        {"id": "sec_recommend_production", "title": "6. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 4.1 successfully built!")


# ==============================================================================
# LECTURE 4.2: Costs, scale of production and break-even analysis
# ==============================================================================
async def build_4_2():
    lid = '66589390-767c-4aab-957b-a970fa1a976e'
    code = '4_2'
    title = '4.2. Costs, scale of production and break-even analysis'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-costs" class="lecture-interactive-card" data-lecture-section="sec_costs" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-scale-production" class="lecture-interactive-card" data-lecture-section="sec_scale_production" style="cursor: pointer; ')
    
    t_h3_scale = str(h3s[0])
    r_h3_scale = t_h3_scale.replace('<h3', '<h3 id="card-economies-scale" class="lecture-interactive-card" data-lecture-section="card_economies_scale" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-break-even" class="lecture-interactive-card" data-lecture-section="sec_break_even" style="cursor: pointer; ')
    
    t_h3_calc = str(h3s[3])
    r_h3_calc = t_h3_calc.replace('<h3', '<h3 id="card-calc-breakeven" class="lecture-interactive-card" data-lecture-section="card_calc_breakeven" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-breakeven-shifts" class="lecture-interactive-card" data-lecture-section="sec_breakeven_shifts" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_scale, r_h3_scale, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h3_calc, r_h3_calc, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.2: Chi phí, Quy mô sản xuất và Điểm hòa vốn",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.2: Costs, Scale of Production and Break-Even Analysis. In this analytical lesson, we classify business costs, explore economies and diseconomies of scale, construct break-even charts, and compute margins of safety.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.2: Chi phí, Quy mô sản xuất và Phân tích Điểm hòa vốn. Trong bài học mang tính định lượng này, chúng ta sẽ phân loại chi phí kinh doanh, tìm hiểu lợi thế và bất lợi thế kinh tế theo quy mô, vẽ biểu đồ hòa vốn và tính biên độ an toàn."
        },
        {
            "id": "sec_costs",
            "title": "1. Phân loại Chi phí Kinh doanh",
            "selector": "#sec-costs",
            "en": "Section 1 categorizes enterprise costs: Fixed Costs—such as factory rent and insurance—do not change with output in the short run; Variable Costs—such as raw materials and direct wages—vary in direct proportion to output. Total Cost is the sum of fixed and variable costs, and Average Cost is total cost divided by output.",
            "vi": "Mục một phân loại chi phí doanh nghiệp: Chi phí cố định (Fixed Costs) như tiền thuê mặt bằng, bảo hiểm không biến động theo sản lượng trong ngắn hạn; Chi phí biến đổi (Variable Costs) như nguyên vật liệu thô, lương sản phẩm tăng giảm tỷ lệ thuận với sản lượng. Tổng chi phí bằng chi phí cố định cộng chi phí biến đổi, và Chi phí bình quân bằng tổng chi phí chia cho sản lượng."
        },
        {
            "id": "sec_scale_production",
            "title": "2. Lợi thế Kinh tế theo Quy mô (Economies of Scale)",
            "selector": "#sec-scale-production",
            "en": "Section 2 investigates economies of scale: factors that cause average unit costs to fall as business output expands. Five main internal economies of scale exist: Purchasing discounts on bulk orders, Marketing cost spreading, Financial lower borrowing interest rates, Technical specialized machinery, and Managerial specialist executives.",
            "vi": "Mục hai nghiên cứu lợi thế kinh tế theo quy mô (economies of scale): các yếu tố làm giảm chi phí đơn vị bình quân khi quy mô sản xuất mở rộng. Năm lợi thế nội bộ chính gồm: Mua hàng số lượng lớn được chiết khấu cao, Tiếp thị phân bổ trên lượng bán lớn, Tài chính vay ngân hàng lãi suất thấp, Kỹ thuật đầu tư máy móc tự động hóa chuyên sâu, và Quản lý thuê các giám đốc chuyên nghiệp."
        },
        {
            "id": "card_economies_scale",
            "title": "Bất lợi thế theo Quy mô (Diseconomies of Scale)",
            "selector": "#card-economies-scale",
            "en": "However, if a business expands beyond optimal capacity, diseconomies of scale set in: poor communication across bloated hierarchies, low employee morale in impersonal mega-factories, and slow coordination problems that drive average costs back up.",
            "vi": "Tuy nhiên, nếu doanh nghiệp mở rộng vượt quá công suất tối ưu, bất lợi thế theo quy mô sẽ xuất hiện: giao tiếp đình trệ qua các tầng nấc quản lý cồng kềnh, tinh thần làm việc sa sút do công nhân thấy mình bị biến thành mắt xích vô danh và việc điều phối chậm trễ đẩy chi phí bình quân tăng trở lại."
        },
        {
            "id": "sec_break_even",
            "title": "3. Phân tích Điểm hòa vốn (Break-even Analysis)",
            "selector": "#sec-break-even",
            "en": "Section 3 defines the Break-Even Point: the exact level of sales output where total revenue perfectly equals total costs, yielding zero profit and zero loss. The Margin of Safety measures the amount by which current actual sales exceed the break-even output level.",
            "vi": "Mục ba định nghĩa Điểm hòa vốn (Break-Even Point): mức sản lượng bán ra mà tại đó tổng doanh thu vừa vặn bù đắp toàn bộ tổng chi phí, không có lãi và cũng không bị lỗ. Biên độ an toàn (Margin of Safety) là khoảng chênh lệch mà mức doanh số thực tế hiện tại vượt trên mức sản lượng hòa vốn."
        },
        {
            "id": "card_calc_breakeven",
            "title": "Công thức tính Điểm hòa vốn và Đóng góp biên",
            "selector": "#card-calc-breakeven",
            "en": "The Cambridge mathematical formula computes Break-Even Output as: Total Fixed Costs divided by Contribution per unit. Contribution per unit equals Selling Price minus Variable Cost per unit.",
            "vi": "Công thức toán học chuẩn Cambridge tính Sản lượng hòa vốn bằng: Tổng chi phí cố định chia cho Đóng góp biên trên mỗi đơn vị sản phẩm (Contribution per unit). Trong đó, Đóng góp biên bằng Giá bán trừ đi Chi phí biến đổi của một sản phẩm."
        },
        {
            "id": "sec_breakeven-shifts",
            "title": "4. Biến động Điểm hòa vốn và Ra quyết định Quản trị",
            "selector": "#sec-breakeven-shifts",
            "en": "Section 4 analyzes shifts on the break-even chart. Raising selling prices steepens the total revenue line, lowering the break-even point. Increasing fixed costs shifts the total cost line upwards, raising the break-even point. Managers use break-even charts to model 'what-if' pricing scenarios and assess launch viability.",
            "vi": "Mục bốn phân tích các dịch chuyển trên đồ thị hòa vốn. Tăng giá bán làm dốc hơn đường tổng doanh thu, kéo giảm sản lượng hòa vốn. Tăng chi phí cố định đẩy đường tổng chi phí lên cao, làm tăng sản lượng hòa vốn cần bán. Ban giám đốc dùng biểu đồ hòa vốn để mô phỏng các kịch bản định giá và đánh giá tính khả thi trước khi ra mắt sản phẩm."
        }
    ]
    
    major_sections = [
        {"id": "sec_costs", "title": "1. Phân loại Chi phí"},
        {"id": "sec_scale_production", "title": "2. Lợi thế & Bất lợi thế Quy mô"},
        {"id": "sec_break_even", "title": "3. Điểm hòa vốn & Biên an toàn"},
        {"id": "sec_breakeven-shifts", "title": "4. Ra quyết định Quản trị dựa trên Hòa vốn"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 4.2 successfully built!")


# ==============================================================================
# LECTURE 4.3: Quality management
# ==============================================================================
async def build_4_3():
    lid = '8f0fd09a-d6e6-438f-a2ab-ddc1447e0b00'
    code = '4_3'
    title = '4.3. Quality management'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-what-is-quality" class="lecture-interactive-card" data-lecture-section="sec_what_is_quality" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-quality-methods" class="lecture-interactive-card" data-lecture-section="sec_quality_methods" style="cursor: pointer; ')
    
    t_h3_qc = str(h3s[0])
    r_h3_qc = t_h3_qc.replace('<h3', '<h3 id="card-qc" class="lecture-interactive-card" data-lecture-section="card_qc" style="cursor: pointer; ')
    
    t_h3_qa = str(h3s[1])
    r_h3_qa = t_h3_qa.replace('<h3', '<h3 id="card-qa" class="lecture-interactive-card" data-lecture-section="card_qa" style="cursor: pointer; ')
    
    t_h3_tqm = str(h3s[2])
    r_h3_tqm = t_h3_tqm.replace('<h3', '<h3 id="card-tqm" class="lecture-interactive-card" data-lecture-section="card_tqm" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-recommend-quality" class="lecture-interactive-card" data-lecture-section="sec_recommend_quality" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_qc, r_h3_qc, 1)\
                   .replace(t_h3_qa, r_h3_qa, 1)\
                   .replace(t_h3_tqm, r_h3_tqm, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.3: Quản trị chất lượng",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.3: Quality Management. In this chapter, we define quality standards, explore why defect prevention matters, compare Quality Control, Quality Assurance, and Total Quality Management, and provide Cambridge evaluation frameworks.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.3: Quản trị chất lượng. Trong bài học này, chúng ta sẽ định nghĩa các tiêu chuẩn chất lượng, tầm quan trọng của việc ngăn ngừa lỗi sản phẩm, so sánh Kiểm soát chất lượng (QC), Đảm bảo chất lượng (QA) và Quản trị chất lượng toàn diện (TQM)."
        },
        {
            "id": "sec_what_is_quality",
            "title": "1. Khái niệm và Tầm quan trọng của Chất lượng",
            "selector": "#sec-what-is-quality",
            "en": "Section 1 defines Quality as delivering goods or services that satisfy or exceed customer expectations, operate reliably without faults, and conform strictly to design specifications. Superior quality fosters customer brand loyalty, reduces expensive warranty claims, and prevents devastating social media complaints.",
            "vi": "Mục một định nghĩa Chất lượng là việc cung cấp sản phẩm hoặc dịch vụ thỏa mãn hoặc vượt trên mong đợi của khách hàng, hoạt động tin cậy không lỗi hỏng và chuẩn xác theo quy chuẩn thiết kế. Chất lượng vượt trội giúp giữ chân khách hàng trung thành, giảm chi phí bồi thường bảo hành và ngăn chặn các khủng hoảng truyền thông."
        },
        {
            "id": "sec_quality_methods",
            "title": "2. Ba Phương pháp Quản trị Chất lượng",
            "selector": "#sec-quality-methods",
            "en": "Section 2 outlines the three accepted methods of quality management examined in the Cambridge syllabus: Quality Control (QC), Quality Assurance (QA), and Total Quality Management (TQM).",
            "vi": "Mục hai tổng hợp ba phương pháp quản trị chất lượng trong chương trình Cambridge: Kiểm soát chất lượng (QC), Đảm bảo chất lượng (QA) và Quản trị chất lượng toàn diện (TQM)."
        },
        {
            "id": "card_qc",
            "title": "Kiểm soát Chất lượng (Quality Control - QC)",
            "selector": "#card-qc",
            "en": "Quality Control inspects completed finished goods at the end of the production line to weed out defective items before dispatch. While simple to organize, QC is fundamentally reactive, results in massive scrap material waste, and does not identify root causes of manufacturing errors.",
            "vi": "Kiểm soát chất lượng (QC) là hoạt động kiểm tra thành phẩm ở cuối dây chuyền sản xuất để loại bỏ các sản phẩm lỗi trước khi giao hàng. Dù dễ thực hiện, QC mang tính đối phó thụ động, gây lãng phí nguyên vật liệu phế phẩm rất lớn và không giải quyết được tận gốc nguyên nhân gây lỗi."
        },
        {
            "id": "card_qa",
            "title": "Đảm bảo Chất lượng (Quality Assurance - QA)",
            "selector": "#card-qa",
            "en": "Quality Assurance establishes strict quality standards at every progressive stage of the production process—from raw material inspection through machine calibration to packaging. Workers 'get it right first time', dramatically reducing scrap rework costs.",
            "vi": "Đảm bảo chất lượng (QA) thiết lập tiêu chuẩn kiểm soát nghiêm ngặt ở từng công đoạn sản xuất – từ khâu nhập nguyên liệu, căn chỉnh máy móc đến đóng gói. Công nhân hướng tới mục tiêu 'làm đúng ngay từ lần đầu tiên', giúp cắt giảm tối đa chi phí sửa chữa phế phẩm."
        },
        {
            "id": "card_tqm",
            "title": "Quản trị Chất lượng Toàn diện (Total Quality Management - TQM)",
            "selector": "#card-tqm",
            "en": "Total Quality Management embeds a continuous commitment to excellence across the entire corporate culture. Every worker treats the next employee in the workflow as an internal customer, fostering zero-defect mentalities and collective empowerment.",
            "vi": "Quản trị chất lượng toàn diện (TQM) đưa cam kết chất lượng thành văn hóa doanh nghiệp lan tỏa đến mọi phòng ban. Mỗi nhân viên coi người ở khâu tiếp theo là một 'khách hàng nội bộ', xây dựng tư duy không chấp nhận lỗi sai (zero-defects) và trao quyền tự chủ cho toàn bộ tập thể."
        },
        {
            "id": "sec_recommend_quality",
            "title": "3. Chiến lược làm bài thi Cambridge: Đề xuất Phương pháp Quản trị Chất lượng",
            "selector": "#sec-recommend-quality",
            "en": "Section 3 presents the Cambridge Quality Recommendation Matrix. Candidates must weigh implementation expenses, staff training disruption, and defect tolerances before justifying the most appropriate quality system.",
            "vi": "Mục ba cung cấp Ma trận đề xuất giải pháp chất lượng Cambridge. Thí sinh cần cân nhắc giữa chi phí triển khai, thời gian đào tạo lại nhân viên và yêu cầu dung sai lỗi trước khi kết luận hệ thống quản trị chất lượng phù hợp nhất cho doanh nghiệp."
        }
    ]
    
    major_sections = [
        {"id": "sec_what_is_quality", "title": "1. Khái niệm Chất lượng"},
        {"id": "sec_quality_methods", "title": "2. So sánh QC, QA và TQM"},
        {"id": "sec_recommend_quality", "title": "3. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 4.3 successfully built!")


# ==============================================================================
# LECTURE 4.4: Location decisions
# ==============================================================================
async def build_4_4():
    lid = '95eb54ae-44d4-42f6-9d1d-c5c729a69954'
    code = '4_4'
    title = '4.4. Location decisions'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_1 = str(h2s[0])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-location-decisions" class="lecture-interactive-card" data-lecture-section="sec_location_decisions" style="cursor: pointer; ')
    
    t_h2_2 = str(h2s[1])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-factors-location" class="lecture-interactive-card" data-lecture-section="sec_factors_location" style="cursor: pointer; ')
    
    t_h3_sectors = str(h3s[0])
    r_h3_sectors = t_h3_sectors.replace('<h3', '<h3 id="card-location-sectors" class="lecture-interactive-card" data-lecture-section="card_location_sectors" style="cursor: pointer; ')
    
    t_h2_3 = str(h2s[2])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-international-location" class="lecture-interactive-card" data-lecture-section="sec_international_location" style="cursor: pointer; ')
    
    t_h2_4 = str(h2s[3])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-legal-location" class="lecture-interactive-card" data-lecture-section="sec_legal_location" style="cursor: pointer; ')
    
    t_h2_5 = str(h2s[4])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-recommend-location" class="lecture-interactive-card" data-lecture-section="sec_recommend_location" style="cursor: pointer; ')

    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h3_sectors, r_h3_sectors, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.4: Quyết định Địa điểm kinh doanh",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.4: Location Decisions. In this concluding chapter of Topic 4, we evaluate the strategic determinants of choosing business premises for manufacturing, service, and retail firms, analyze overseas offshoring factors, and assess government regional incentives.",
            "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.4: Quyết định Địa điểm kinh doanh. Trong bài kết thúc Chủ đề bốn, chúng ta sẽ phân tích các yếu tố chiến lược khi lựa chọn địa điểm đặt cơ sở sản xuất, dịch vụ và bán lẻ, các lý do dịch chuyển nhà máy ra nước ngoài và chính sách hỗ trợ phát triển vùng của chính phủ."
        },
        {
            "id": "sec_location_decisions",
            "title": "1. Tầm quan trọng Chiến lược của Địa điểm",
            "selector": "#sec-location-decisions",
            "en": "Section 1 explains why choosing a location is an irreversible, high-stakes decision. Site selection dictates fixed premises rent, proximity to customers, logistics shipping costs, and access to skilled labour pools.",
            "vi": "Mục một giải thích lý do lựa chọn địa điểm là quyết định chiến lược dài hạn khó có thể đảo ngược. Địa điểm quyết định mức chi phí thuê mặt bằng, cự ly tiếp cận khách hàng, chi phí vận tải giao nhận hàng hóa và khả năng tuyển dụng lao động có tay nghề."
        },
        {
            "id": "sec_factors_location",
            "title": "2. Các Yếu tố ảnh hưởng đến Địa điểm",
            "selector": "#sec-factors-location",
            "en": "Section 2 investigates site selection criteria across industries: Manufacturing plants locate near raw material deposits or transport hubs to minimize freight charges; Service firms locate near target corporate clients; and Retail stores locate in high-footfall shopping arcades with convenient parking.",
            "vi": "Mục hai nghiên cứu các tiêu chí chọn vị trí theo từng ngành nghề: Nhà máy sản xuất ưu tiên đặt gần nguồn nguyên liệu thô hoặc đầu mối giao thông cảng biển để giảm cước vận chuyển; Doanh nghiệp dịch vụ đặt văn phòng gần khách hàng doanh nghiệp; còn Cửa hàng bán lẻ bắt buộc phải ở nơi có mật độ người qua lại đông đúc và bãi đỗ xe thuận tiện."
        },
        {
            "id": "card_location_sectors",
            "title": "So sánh Địa điểm theo Loại hình Doanh nghiệp",
            "selector": "#card-location-sectors",
            "en": "Different business sectors prioritize different location variables: heavy industrial factories require expansive cheap land and heavy power grids, whereas boutique retail fashion brands prioritize affluent customer demographics and prestige street visibility.",
            "vi": "Mỗi loại hình doanh nghiệp ưu tiên những yếu tố mặt bằng khác nhau: nhà máy công nghiệp nặng cần quỹ đất rộng giá rẻ và lưới điện công suất lớn, trong khi thương hiệu thời trang cao cấp lại chú trọng vào mức thu nhập của cư dân khu vực và vị trí mặt tiền đắc địa trên phố sầm uất."
        },
        {
            "id": "sec_international_location",
            "title": "3. Đặt Cơ sở Sản xuất tại Nước ngoài (Offshoring)",
            "selector": "#sec-international-location",
            "en": "Section 3 analyzes multinational overseas relocation: seeking lower wage rates in emerging economies, bypassing import trade tariffs by manufacturing inside regional trade blocs, and securing access to rapidly growing foreign consumer markets.",
            "vi": "Mục ba phân tích việc mở rộng địa điểm ra nước ngoài: tận dụng giá nhân công rẻ tại các nước đang phát triển, vượt qua hàng rào thuế quan nhập khẩu bằng cách sản xuất trực tiếp bên trong các khối thương mại tự do, và tiếp cận thị trường tiêu dùng mới đang tăng trưởng nhanh chóng."
        },
        {
            "id": "sec_legal_location",
            "title": "4. Quy hoạch Pháp lý và Trợ cấp của Chính phủ",
            "selector": "#sec-legal-location",
            "en": "Section 4 explores statutory planning controls: zoning laws restricting industrial pollution near residential housing, and government regional development grants offering tax holidays and rent subsidies to encourage factories to open in high-unemployment areas.",
            "vi": "Mục bốn tìm hiểu sự can thiệp của chính phủ: luật quy hoạch phân vùng cấm xây dựng nhà máy gây ô nhiễm gần khu dân cư, cùng các chính sách ưu đãi tài chính và miễn giảm thuế nhằm thu hút doanh nghiệp đặt cơ sở sản xuất tại các vùng có tỷ lệ thất nghiệp cao."
        },
        {
            "id": "sec_recommend_location",
            "title": "5. Chiến lược làm bài thi Cambridge: Đề xuất Địa điểm Kinh doanh",
            "selector": "#sec-recommend-location",
            "en": "Section 5 presents the Cambridge Location Evaluation Formula. Candidates must contrast short-term rental costs against long-term revenue potential and logistical convenience to arrive at a well-reasoned, contextualized recommendation.",
            "vi": "Mục năm cung cấp Công thức đánh giá Địa điểm thi Cambridge. Thí sinh phải so sánh giữa chi phí thuê ngắn hạn với tiềm năng doanh thu dài hạn và sự thuận tiện trong chuỗi cung ứng logistics để đưa ra kết luận thuyết phục nhất gắn liền với tình huống đề bài."
        }
    ]
    
    major_sections = [
        {"id": "sec_location_decisions", "title": "1. Tầm quan trọng Địa điểm"},
        {"id": "sec_factors_location", "title": "2. Tiêu chí chọn Địa điểm theo Ngành"},
        {"id": "sec_international_location", "title": "3. Địa điểm Quốc tế (Offshoring)"},
        {"id": "sec_legal_location", "title": "4. Pháp lý & Trợ cấp Vùng của Chính phủ"},
        {"id": "sec_recommend_location", "title": "5. Chiến lược làm bài thi Cambridge"}
    ]
    
    await process_lecture_audio(code, lid, "Cambridge IGCSE Business Studies", title, segments, major_sections, subject='business')
    update_supabase_page(lid, new_html)
    print("✅ Lecture 4.4 successfully built!")


# ==============================================================================
# MAIN BATCH RUNNER FOR TOPIC 4
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING TOPIC 4 BUILD: ALL 4 LECTURES (4.1 -> 4.4)")
    print("*******************************************************\n")
    
    await build_4_1()
    await asyncio.sleep(2)
    
    await build_4_2()
    await asyncio.sleep(2)
    
    await build_4_3()
    await asyncio.sleep(2)
    
    await build_4_4()
    
    print("\n*******************************************************")
    print("TOPIC 4 COMPLETE: ALL 4 LECTURES PROCESSED SUCCESSFULLY!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
