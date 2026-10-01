import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Lecture 4.2 ID
LID = '66589390-767c-4aab-957b-a970fa1a976e'
CODE = '4_2'
TITLE = '4.2. Costs, scale of production and break-even analysis'
COURSE_TITLE = 'Cambridge IGCSE Business Studies'

# ==============================================================================
# 1. DEFINE ALL 9 AUDIO SEGMENTS FOR LESSON 4.2
# ==============================================================================
segments = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 4.2: Chi phí, Quy mô sản xuất & Điểm hòa vốn",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Business Studies, Chapter 4.2: Costs, Scale of Production, and Break-Even Analysis. In this lesson, we classify business costs, evaluate internal and external economies and diseconomies of scale, interpret break-even charts, and master margin of safety calculations.",
        "vi": "Chào mừng các bạn đến với môn Kinh doanh Cambridge IGCSE, Bài 4.2: Chi phí, Quy mô sản xuất và Phân tích điểm hòa vốn. Trong bài học này, chúng ta sẽ phân loại các loại chi phí doanh nghiệp, đánh giá lợi thế và bất lợi kinh tế theo quy mô, giải thích biểu đồ hòa vốn và thực hiện các phép tính biên độ an toàn."
    },
    {
        "id": "sec_costs",
        "title": "1. Khái niệm và Phân loại Chi phí (Costs)",
        "selector": "#sec-costs",
        "en": "Section 1 examines business costs. Fixed costs—such as factory rent and insurance premiums—remain constant regardless of production volumes in the short run. Variable costs—like raw materials and piece-rate wages—fluctuate directly with output. Accurate cost data underpins pricing, break-even targets, and location appraisals.",
        "vi": "Mục một phân tích các khoản chi phí của doanh nghiệp. Chi phí cố định – như tiền thuê nhà xưởng và phí bảo hiểm – không thay đổi theo mức sản lượng trong ngắn hạn. Chi phí biến đổi – như nguyên vật liệu và tiền lương trả theo sản phẩm – biến động trực tiếp theo số lượng làm ra. Dữ liệu chi phí chính xác là nền tảng để định giá, tính điểm hòa vốn và lựa chọn địa điểm."
    },
    {
        "id": "card_cost_concepts",
        "title": "💵 Phân biệt Chi phí Cố định, Biến đổi & Công thức Tính Chi phí Đơn vị",
        "selector": "#card-cost-concepts",
        "en": "Fixed costs do not change with output in the short run and must be paid even if production is zero, such as factory rent and insurance. Variable costs alter in direct proportion to production volumes, including raw materials and piece-rate wages. Total cost combines fixed and variable expenses, while average unit cost divides total cost by units produced.",
        "vi": "Chi phí cố định không thay đổi theo mức sản lượng trong ngắn hạn và vẫn phải trả ngay cả khi không sản xuất, như tiền thuê nhà xưởng và bảo hiểm. Chi phí biến đổi thay đổi trực tiếp theo số lượng sản phẩm làm ra, bao gồm nguyên vật liệu và tiền lương trả theo sản phẩm. Tổng chi phí là tổng của chi phí cố định và chi phí biến đổi, trong khi chi phí đơn vị lấy tổng chi phí chia cho số sản phẩm sản xuất."
    },
    {
        "id": "sec_scale_production",
        "title": "2. Quy mô Sản xuất (Scale of Production)",
        "selector": "#sec-scale-production",
        "en": "Section 2 investigates scale of production. The central economic principle dictates that expanding scale initially reduces average unit costs via economies of scale. However, growing beyond optimal capacity triggers bureaucratic diseconomies that drive unit costs back up.",
        "vi": "Mục hai khảo sát quy mô sản xuất. Nguyên lý kinh tế trọng tâm chỉ ra rằng việc mở rộng quy mô ban đầu sẽ kéo giảm chi phí trung bình trên mỗi sản phẩm nhờ lợi thế quy mô. Tuy nhiên, nếu phát triển vượt quá quy mô tối ưu sẽ làm phát sinh các bất lợi về bộ máy cồng kềnh, khiến chi phí đơn vị tăng ngược trở lại."
    },
    {
        "id": "card_economies_scale",
        "title": "📉 5 Loại Lợi thế Kinh tế theo Quy mô (Economies of Scale)",
        "selector": "#card-economies-scale",
        "en": "Firms enjoy five core internal economies of scale: purchasing bulk-buying discounts; marketing economies via dedicated transport and spread advertising; financial economies through preferential bank loan rates; managerial specialization; and technical economies operating large-scale automated lines.",
        "vi": "Doanh nghiệp được hưởng năm lợi thế quy mô nội bộ chính: mua sỉ nguyên vật liệu được chiết khấu cao; tiếp thị tiết kiệm nhờ sở hữu xe vận tải riêng và chi phí quảng bá chia đều; tài chính ưu đãi với lãi suất vay ngân hàng thấp hơn; chuyên môn hóa bộ máy quản lý; và kỹ thuật vận hành các dây chuyền tự động hóa quy mô lớn."
    },
    {
        "id": "card_diseconomies_scale",
        "title": "📈 Bất lợi Quy mô (Diseconomies of Scale) & Giải pháp",
        "selector": "#card-diseconomies-scale",
        "en": "Diseconomies of scale occur when excessive business expansion drives average unit costs upward due to bureaucratic inefficiencies: communication breakdowns across sprawling departments, worker demotivation from feeling impersonal, and slow decision-making along long chains of command. Businesses counteract this by devolving into autonomous operational divisions.",
        "vi": "Bất lợi kinh tế theo quy mô xảy ra khi doanh nghiệp mở rộng quá lớn khiến chi phí trung bình trên mỗi sản phẩm tăng ngược trở lại do bộ máy cồng kềnh: giao tiếp đứt gãy giữa các phòng ban, người lao động mất động lực vì cảm thấy xa cách lãnh đạo, và quyết định chậm trễ qua nhiều cấp bậc quản lý. Doanh nghiệp khắc phục điều này bằng cách phân quyền thành các đơn vị vận hành tự chủ nhỏ hơn."
    },
    {
        "id": "sec_break_even",
        "title": "3. Phân tích Điểm Hòa vốn & Biểu đồ Hòa vốn (Break-even Chart)",
        "selector": "#sec-break-even",
        "en": "Section 3 examines break-even analysis: identifying the exact output where Total Revenue equals Total Costs, yielding zero operating profit and zero loss. The Break-Even Chart visually models fixed costs, total costs, total revenue, and the safety buffer separating expected sales from break-even output.",
        "vi": "Mục ba nghiên cứu phân tích điểm hòa vốn: xác định mức sản lượng chính xác mà tại đó Tổng doanh thu bằng Tổng chi phí, tức lợi nhuận bằng không và không bị lỗ. Biểu đồ hòa vốn trực quan hóa đường chi phí cố định, tổng chi phí, tổng doanh thu và biên độ an toàn giữa mức doanh số dự kiến so với điểm hòa vốn."
    },
    {
        "id": "card_calc_breakeven",
        "title": "🧮 Công thức Tính Điểm Hòa vốn & Số dư Đảm phí (Contribution)",
        "selector": "#card-calc-breakeven",
        "en": "Break-even output is calculated mathematically in two steps: first calculate Contribution per unit (Selling Price minus Variable Cost per unit); second, divide Total Fixed Costs by Contribution per unit. Margin of safety measures actual or planned unit sales minus the break-even output.",
        "vi": "Mức sản lượng hòa vốn được tính theo công thức hai bước: đầu tiên tính Số dư đảm phí trên mỗi đơn vị sản phẩm (Giá bán trừ Chi phí biến đổi một sản phẩm); sau đó lấy Tổng chi phí cố định chia cho Số dư đảm phí đơn vị. Biên độ an toàn bằng sản lượng tiêu thụ thực tế hoặc dự kiến trừ đi sản lượng hòa vốn."
    },
    {
        "id": "sec_breakeven-shifts",
        "title": "4. Chiến lược làm bài thi Cambridge: Biến động Điểm Hòa vốn & Ra Quyết định",
        "selector": "#sec-breakeven-shifts",
        "en": "Section 4 highlights Cambridge examination technique regarding cost variations. Raising selling prices steepens the total revenue slope and lowers the break-even volume, expanding the safety margin. Conversely, escalating supplier prices or factory overheads lift the total cost line upward, increasing commercial risk.",
        "vi": "Mục bốn nhấn mạnh chiến lược làm bài thi Cambridge về biến động chi phí. Tăng giá bán làm cho đường tổng doanh thu dốc hơn và hạ thấp sản lượng hòa vốn, giúp mở rộng biên độ an toàn. Ngược lại, chi phí nguyên vật liệu hoặc chi phí cố định leo thang sẽ đẩy đường tổng chi phí lên cao, làm tăng rủi ro kinh doanh."
    }
]

major_sections = {
    "intro": {"start": 0, "end": 0},
    "sec_costs": {"start": 1, "end": 2},
    "sec_scale_production": {"start": 3, "end": 5},
    "sec_break_even": {"start": 6, "end": 7},
    "sec_breakeven-shifts": {"start": 8, "end": 8}
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
                <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.2 Costs, Scale of Production &amp; Break-Even Analysis</h1>
            </div>
            <div style="font-size: 13px; color: #475569; background: #ffffff; padding: 7px 16px; border-radius: 20px; border: 1px solid #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 6px;">
                <span>🎙️</span> Bấm vào thẻ để nghe giảng chi tiết
            </div>
        </div>
    </div>

    <!-- 1. COSTS -->
    <div style="margin-bottom: 50px;">
        <div id="sec-costs" class="lecture-interactive-card" data-lecture-section="sec_costs" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #3b82f6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">💵 1. COSTS</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                Cost intelligence allows businesses to calculate profit margins, establish competitive selling prices, and evaluate whether to proceed with or cease operational ventures.
            </p>
        </div>

        <!-- SUB-CARD: COST CONCEPTS & FORMULAS -->
        <div id="card-cost-concepts" class="lecture-interactive-card" data-lecture-section="card_cost_concepts" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #1e40af; font-weight: 700;">💵 Fixed vs Variable Costs &amp; Unit Cost Formulas</h3>
                <span style="font-size: 11px; font-weight: 700; background: #eff6ff; color: #1d4ed8; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #2563eb; font-size: 16px; margin: 0 0 8px 0;">🛡️ Fixed Costs (Overheads)</h4>
                    <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Costs that <b>do not vary</b> with output produced or sold in the short run. Incurred even when output is 0.<br><br><i>E.g.: Factory rent, insurance, management salaries.</i></p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px;">
                    <h4 style="color: #059669; font-size: 16px; margin: 0 0 8px 0;">📈 Variable Costs</h4>
                    <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Costs that <b>directly vary</b> in proportion to output produced or sold.<br><br><i>E.g.: Raw materials, direct packaging, piece-rate wages.</i></p>
                </div>
            </div>

            <div style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: center; align-items: center; background: #f8fafc; padding: 18px; border-radius: 8px; border: 1.5px dashed #94a3b8; margin-bottom: 16px;">
                <div style="flex: 1; min-width: 240px; text-align: center;">
                    <p style="margin: 0; font-size: 15px; color: #334155; font-weight: bold;">TOTAL COST =</p>
                    <div style="font-size: 14.5px; color: #1e40af; margin-top: 4px; font-weight: 600;">Total Fixed Costs + Total Variable Costs</div>
                    <div style="font-size: 12px; color: #64748b; margin-top: 2px;">(Or: Average Cost × Output)</div>
                </div>
                <div style="width: 2px; background: #cbd5e1; height: 45px;"></div>
                <div style="flex: 1; min-width: 240px; text-align: center;">
                    <p style="margin: 0; font-size: 15px; color: #334155; font-weight: bold;">AVERAGE COST (Unit Cost) =</p>
                    <div style="font-size: 14.5px; color: #1e40af; margin-top: 4px; font-weight: 600;">Total Cost / Total Output</div>
                </div>
            </div>

            <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 12px 16px; border-radius: 4px; font-size: 13px; color: #92400e;">
                <b>Why is cost data important?</b> Businesses utilize cost data to establish profitable selling prices, calculate break-even hurdles, decide whether to accept special orders, and choose between alternative operational factory locations.
            </div>
        </div>
    </div>

    <!-- 2. SCALE OF PRODUCTION -->
    <div style="margin-bottom: 50px;">
        <div id="sec-scale-production" class="lecture-interactive-card" data-lecture-section="sec_scale_production" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #8b5cf6; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">⚖️ 2. SCALE OF PRODUCTION</h2>
            <p style="font-size: 15px; color: #475569; margin: 0; line-height: 1.6;">
                <b>The Golden Rule:</b> As output expands, average unit costs initially fall due to internal economies of scale, before excessive growth triggers managerial diseconomies.
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <!-- SUB-CARD: ECONOMIES OF SCALE -->
            <div id="card-economies-scale" class="lecture-interactive-card" data-lecture-section="card_economies_scale" style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 14px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 3px 10px rgba(0,0,0,0.02);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <h3 style="margin: 0; color: #15803d; font-size: 18px; font-weight: 700;">📉 Economies of Scale</h3>
                    <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #15803d; padding: 4px 10px; border-radius: 6px; border: 1px solid #bbf7d0;">Nghe thẻ này</span>
                </div>
                <p style="margin: 0 0 12px 0; font-size: 13.5px; color: #166534;">Factors that lead to a <b>reduction in average unit costs</b> as business size and output expand:</p>
                <ul style="margin: 0; padding-left: 18px; color: #14532d; font-size: 12.5px; line-height: 1.6;">
                    <li><b>Purchasing economies:</b> Buying raw materials in bulk unlocks massive volume discounts.</li>
                    <li><b>Marketing economies:</b> Operating own logistics fleet; advertising budget spreads over huge sales volume.</li>
                    <li><b>Financial economies:</b> Commercial banks lend at lower interest rates to large, credit-worthy enterprises.</li>
                    <li><b>Managerial economies:</b> Hiring dedicated functional specialist managers drives operational efficiency.</li>
                    <li><b>Technical economies:</b> Investing in high-speed automated flow production lines.</li>
                </ul>
            </div>

            <!-- SUB-CARD: DISECONOMIES OF SCALE -->
            <div id="card-diseconomies-scale" class="lecture-interactive-card" data-lecture-section="card_diseconomies_scale" style="background: #fef2f2; border: 1.5px solid #fecaca; border-radius: 14px; padding: 22px; cursor: pointer; transition: all 0.2s; box-shadow: 0 3px 10px rgba(0,0,0,0.02);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                    <h3 style="margin: 0; color: #b91c1c; font-size: 18px; font-weight: 700;">📈 Diseconomies of Scale</h3>
                    <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #b91c1c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fecaca;">Nghe thẻ này</span>
                </div>
                <p style="margin: 0 0 12px 0; font-size: 13.5px; color: #991b1b;">Factors that cause <b>average unit costs to rise</b> when a firm expands past optimal capacity:</p>
                <ul style="margin: 0; padding-left: 18px; color: #7f1d1d; font-size: 12.5px; line-height: 1.6;">
                    <li><b>Poor communication:</b> Sprawling departments distort information and slow message transmission.</li>
                    <li><b>Low morale:</b> Frontline workers feel detached from distant senior executives, lowering productivity.</li>
                    <li><b>Slow decision-making:</b> Excessive hierarchy chains delay responses to changing market trends.</li>
                </ul>
                <p style="margin: 12px 0 0 0; font-size: 12px; color: #7f1d1d; font-style: italic;">*To combat this, multinational corporations decentralise operations into autonomous business units.</p>
            </div>
        </div>
    </div>

    <!-- 3. BREAK-EVEN -->
    <div style="margin-bottom: 50px;">
        <div id="sec-break-even" class="lecture-interactive-card" data-lecture-section="sec_break_even" style="margin-bottom: 20px; padding: 22px 24px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s;">
            <h2 style="color: #0f172a; border-bottom: 3px solid #f97316; padding-bottom: 12px; margin-bottom: 14px; display: inline-block; font-size: 24px; line-height: 1.2; margin-top: 0;">🎯 3. BREAK-EVEN ANALYSIS</h2>
            <div style="background: #fff7ed; border-left: 4px solid #ea580c; padding: 14px 18px; border-radius: 4px; font-size: 14.5px; color: #9a3412; margin-bottom: 16px;">
                The <b>Break-even level of output</b> is the production quantity required to cover all costs: <b>Total Revenue = Total Costs</b> <i>(zero profit, zero loss)</i>.
            </div>
            <p style="font-size: 14px; color: #475569; margin: 0 0 16px 0;">
                <b>Chart Model:</b> Max capacity: 2000 units • Price: $8/unit • Fixed Costs: $5,000 • Variable Costs: $3/unit.<br>
                <b>At 2000 units:</b> Total Revenue = $16,000 • Total Cost = $5,000 + ($3 × 2000) = $11,000.
            </p>

            <!-- Chart SVG -->
            <div style="margin-bottom: 20px; overflow-x: auto; text-align: center;">
                <svg viewBox="0 0 600 400" width="100%" style="max-width: 580px; background:#ffffff; border-radius:12px; border:1px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.02); display: block; margin: 0 auto; font-family: Arial, sans-serif;">
                    <line x1="80" y1="280" x2="550" y2="280" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="80" y1="200" x2="550" y2="200" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="80" y1="120" x2="550" y2="120" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="80" y1="40" x2="550" y2="40" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="200" y1="360" x2="200" y2="40" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="320" y1="360" x2="320" y2="40" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="440" y1="360" x2="440" y2="40" stroke="#f1f5f9" stroke-width="1"></line>
                    <line x1="80" y1="360" x2="560" y2="360" stroke="#334155" stroke-width="2"></line>
                    <line x1="80" y1="20" x2="80" y2="360" stroke="#334155" stroke-width="2"></line>
                    <text x="320" y="395" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Output (Units)</text>
                    <text x="25" y="190" transform="rotate(-90 25,190)" text-anchor="middle" font-size="14" font-weight="bold" fill="#334155">Costs / Revenue ($)</text>

                    <text x="80" y="380" text-anchor="middle" font-size="12" fill="#64748b">0</text>
                    <text x="200" y="380" text-anchor="middle" font-size="12" fill="#64748b">500</text>
                    <text x="320" y="380" text-anchor="middle" font-size="12" fill="#64748b">1000</text>
                    <text x="440" y="380" text-anchor="middle" font-size="12" fill="#64748b">1500</text>
                    <text x="550" y="380" text-anchor="middle" font-size="12" fill="#64748b">2000</text>

                    <text x="70" y="284" text-anchor="end" font-size="12" fill="#64748b">4000</text>
                    <text x="70" y="204" text-anchor="end" font-size="12" fill="#64748b">8000</text>
                    <text x="70" y="124" text-anchor="end" font-size="12" fill="#64748b">12000</text>
                    <text x="70" y="44" text-anchor="end" font-size="12" fill="#64748b">16000</text>

                    <line x1="80" y1="260" x2="550" y2="260" stroke="#f59e0b" stroke-width="3"></line>
                    <text x="560" y="264" font-size="12" font-weight="bold" fill="#d97706">Fixed Cost</text>

                    <line x1="80" y1="360" x2="550" y2="240" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4,4"></line>
                    <text x="560" y="244" font-size="12" font-weight="bold" fill="#2563eb">Variable Cost</text>

                    <line x1="80" y1="260" x2="550" y2="140" stroke="#dc2626" stroke-width="3"></line>
                    <text x="560" y="144" font-size="12" font-weight="bold" fill="#b91c1c">Total Cost</text>

                    <line x1="80" y1="360" x2="550" y2="40" stroke="#10b981" stroke-width="3"></line>
                    <text x="560" y="44" font-size="12" font-weight="bold" fill="#059669">Total Revenue</text>

                    <circle cx="320" cy="200" r="6" fill="#0f172a"></circle>
                    <line x1="320" y1="200" x2="320" y2="360" stroke="#64748b" stroke-dasharray="3,3" stroke-width="2"></line>
                    <line x1="80" y1="200" x2="320" y2="200" stroke="#64748b" stroke-dasharray="3,3" stroke-width="2"></line>

                    <rect x="250" y="150" width="140" height="25" fill="#f8fafc" stroke="#cbd5e1" rx="4"></rect>
                    <text x="320" y="167" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f172a">Break-even Point</text>

                    <path d="M 320 340 L 550 340" stroke="#8b5cf6" stroke-width="2" fill="none"></path>
                    <polygon points="550,340 540,335 540,345" fill="#8b5cf6"></polygon>
                    <polygon points="320,340 330,335 330,345" fill="#8b5cf6"></polygon>
                    <rect x="380" y="315" width="110" height="20" fill="#f3e8ff" rx="4"></rect>
                    <text x="435" y="329" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">Margin of Safety</text>

                    <text x="430" y="110" font-size="14" font-weight="bold" fill="#059669">PROFIT</text>
                    <text x="210" y="280" font-size="14" font-weight="bold" fill="#dc2626">LOSS</text>
                </svg>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px;">
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 15px;">
                    <h4 style="color: #15803d; font-size: 15px; margin: 0 0 6px 0;">✅ Advantages of Break-even Charts</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #166534; font-size: 12.5px; line-height: 1.5;">
                        <li>Shows instant expected profit/loss at any output target.</li>
                        <li>Models what-if simulations when prices or expenses change.</li>
                        <li>Identifies the exact <b>Margin of Safety</b>.</li>
                    </ul>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 15px;">
                    <h4 style="color: #b91c1c; font-size: 15px; margin: 0 0 6px 0;">❌ Limitations of Break-even Charts</h4>
                    <ul style="margin: 0; padding-left: 18px; color: #991b1b; font-size: 12.5px; line-height: 1.5;">
                        <li>Assumes 100% of manufactured units are sold immediately.</li>
                        <li>Fixed costs step upward as capacity milestones are passed.</li>
                        <li>Linear lines ignore overtime wages and supplier discounts.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SUB-CARD: CALCULATING BREAK-EVEN -->
        <div id="card-calc-breakeven" class="lecture-interactive-card" data-lecture-section="card_calc_breakeven" style="padding: 22px 24px; background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h3 style="margin: 0; font-size: 18px; color: #c2410c; font-weight: 700;">🧮 Calculating Break-even &amp; Contribution Formulas</h3>
                <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 4px 10px; border-radius: 6px; border: 1px solid #fed7aa;">Nghe thẻ này</span>
            </div>

            <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 18px; text-align: center;">
                <p style="margin: 0 0 8px 0; font-size: 14px; color: #334155; font-weight: bold;">Step 1: Calculate Contribution per Unit</p>
                <div style="font-size: 16px; color: #db2777; font-weight: bold; background: #fdf2f8; padding: 8px 16px; border-radius: 6px; display: inline-block; margin-bottom: 16px;">
                    Contribution = Selling price – Variable cost per unit
                </div>

                <p style="margin: 0 0 8px 0; font-size: 14px; color: #334155; font-weight: bold;">Step 2: Calculate Break-even Output</p>
                <div style="font-size: 16px; color: #db2777; font-weight: bold; background: #fdf2f8; padding: 8px 16px; border-radius: 6px; display: inline-block;">
                    <span style="border-bottom: 2px solid #db2777; padding-bottom: 2px;">Total Fixed Costs</span><br>
                    <span style="padding-top: 2px; display: inline-block;">Contribution per unit</span>
                </div>

                <div style="background: #dcfce7; padding: 10px; border-radius: 6px; margin-top: 14px; font-size: 13px; color: #065f46; display: inline-block;">
                    <b>Margin of Safety:</b> Planned Output – Break-even Output<br>
                    <i>(Example: 2,000 units planned – 1,000 break-even = <b>1,000 units safety margin!</b>)</i>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. CAMBRIDGE EXAM GUIDE -->
    <div style="margin-bottom: 50px;">
        <div id="sec-breakeven-shifts" class="lecture-interactive-card" data-lecture-section="sec_breakeven-shifts" style="padding: 24px 26px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; box-shadow: 0 3px 10px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
                <h2 style="color: #1e3a8a; margin: 0; font-size: 20px; font-weight: 700;">
                    🎯 4. BREAK-EVEN SHIFTS &amp; BUSINESS DECISION MAKING (Cambridge Exam Guide)
                </h2>
                <span style="font-size: 11px; font-weight: 700; background: #ffffff; color: #1e3a8a; padding: 4px 10px; border-radius: 6px; border: 1px solid #bfdbfe;">Nghe thẻ này</span>
            </div>
            <p style="font-size: 14.5px; color: #1e40af; margin-bottom: 18px; line-height: 1.5;">
                Paper 1 and Paper 2 regularly test what happens to the break-even chart and margin of safety when prices or costs change:
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-bottom: 18px;">
                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #10b981;">
                    <b style="color: #047857; font-size: 14.5px;">📈 If Selling Price Increases:</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        • Total Revenue line becomes <b>steeper</b>.<br/>
                        • Break-even point <b>falls</b> (fewer units needed to break even).<br/>
                        • Margin of safety <b>increases</b> (assuming demand does not drop).
                    </p>
                </div>

                <div style="background: #ffffff; padding: 16px; border-radius: 8px; border-left: 4px solid #ef4444;">
                    <b style="color: #b91c1c; font-size: 14.5px;">📉 If Fixed or Variable Costs Rise:</b>
                    <p style="margin: 6px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                        • Total Cost line shifts <b>upwards</b>.<br/>
                        • Break-even point <b>rises</b> (more units must be sold to cover costs).<br/>
                        • Margin of safety <b>decreases</b>, escalating operational insolvency risk.
                    </p>
                </div>
            </div>

            <div style="background: #ffffff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px;">
                <b style="color: #1e40af; font-size: 14px;">💡 Cambridge Exam Rule on Break-Even Limitations:</b>
                <p style="margin: 4px 0 0 0; font-size: 12.5px; color: #334155; line-height: 1.5;">
                    Never assume that calculating a break-even point guarantees profits! Break-even only shows what output <i>must</i> be sold. If consumer demand drops below break-even, the business will make an operating loss.
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
            <h1 style="margin: 4px 0 0 0; font-size: 26px; color: #0f172a; font-weight: 800; line-height: 1.2;">4.2 Costs, Scale of Production &amp; Break-Even Analysis</h1>
        </div>
    </div>"""
    pattern = r'(<div style="font-family: \'Segoe UI\', Arial, sans-serif; width: 100%; margin: 20px auto; color: #334155; line-height: 1.6; box-sizing: border-box;">)'
    new_p2 = re.sub(pattern, r'\1\n\n    ' + header_banner, original_p2, count=1)
    return new_p2

async def main():
    print(f"=== Rebuilding Business Studies 4.2 Audio and HTML ===")
    
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
    with open('scripts/raw_pages/4_2_p2.html', 'r', encoding='utf-8') as f:
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
    
    print("\n✅ REBUILD 4.2 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
