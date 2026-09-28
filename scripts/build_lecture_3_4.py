import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '3_4'
LECTURE_ID = 'c5ce49f0-7b81-4843-a477-3ee46e41928e'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '3.4 Threats to Tropical Rainforests & Sustainable Management'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 3.4: Hiểm họa đối với Rừng mưa nhiệt đới & Quản lý bền vững",
        "selector": "#sec-header",
        "en": "Lesson 3.4: Threats to Tropical Rainforests and Sustainable Management. In this lesson, we examine economic causes of deforestation, severe environmental impacts, the Amazon tipping point, and sustainable management strategies.",
        "vi": "Bài ba chấm bốn: Các hiểm họa đối với Rừng mưa nhiệt đới và Chiến lược quản lý bền vững. Trong bài học này, chúng ta sẽ tìm hiểu các nguyên nhân kinh tế dẫn đến nạn phá rừng, các tác động môi trường nghiêm trọng, điểm bùng phát A-ma-dôn và các chiến lược bảo tồn bền vững."
    },
    {
        "id": "sec_deforestation_drivers",
        "title": "1. Nguyên nhân kinh tế chính gây mất rừng (Drivers of Deforestation)",
        "selector": "#sec-deforestation-drivers",
        "en": "Section 1: Primary Economic Drivers of Deforestation. Large-scale commercial cattle ranching, soybean cultivation, commercial logging, mining, and hydroelectric infrastructure drive the loss of millions of hectares of virgin forest annually.",
        "vi": "Phần một: Các nguyên nhân kinh tế hàng đầu gây mất rừng. Chăn nuôi gia súc quy mô lớn, trồng đậu tương công nghiệp, khai thác gỗ thương mại, khai khoáng và xây đập thủy điện là những tác nhân chính hủy hoại hàng triệu héc-ta rừng nguyên sinh mỗi năm."
    },
    {
        "id": "driver_cattle",
        "title": "Chăn nuôi đại gia súc ở Amazon (Cattle Ranching - 80%)",
        "selector": "#driver-cattle",
        "en": "Cattle Ranching in the Brazilian Amazon. Responsible for eighty percent of Amazonian deforestation. Pastures are cleared via slash-and-burn to supply global beef and leather markets, degrading fragile soils within five to eight years.",
        "vi": "Chăn nuôi đại gia súc ở lưu vực A-ma-dôn. Chiếm tới tám mươi phần trăm diện tích rừng bị phá tại Bra-xin. Rừng bị phát quang đốt trụi để làm đồng cỏ cung cấp thịt bò và da cho thị trường toàn cầu, khiến đất bị thoái hóa chỉ sau năm đến tám năm."
    },
    {
        "id": "driver_palmoil",
        "title": "Độc canh cọ dầu tại Borneo & Sumatra (Palm Oil)",
        "selector": "#driver-palmoil",
        "en": "Oil Palm Monoculture in Borneo and Sumatra. Peat swamp forests are clear-felled and drained, obliterating critical habitat for endangered orangutans, releasing gigatonnes of subterranean carbon into the atmosphere.",
        "vi": "Độc canh cọ dầu tại đảo Boóc-nê-ô và Su-ma-tra. Rừng đầm lầy than bùn bị đốn hạ và tháo cạn nước, xóa sổ sinh cảnh sống còn của đười ươi, đồng thời giải phóng hàng tỷ tấn các-bon tích tụ dưới lòng đất vào khí quyển."
    },
    {
        "id": "driver_logging",
        "title": "Khai thác gỗ & Nông nghiệp nương rẫy tại Congo",
        "selector": "#driver-logging",
        "en": "Commercial Logging and Smallholder Agriculture in the Congo Basin. Selective logging builds logging roads that open up remote forest interiors to charcoal production and slash-and-burn farming.",
        "vi": "Khai thác gỗ thương mại và Nông nghiệp nương rẫy ở lưu vực Công-gô. Việc khai thác gỗ chọn lọc mở ra các tuyến đường xẻ ngang lõi rừng, tạo điều kiện cho hoạt động đốn củi đốt than và canh tác du canh lấn chiếm."
    },
    {
        "id": "driver_infrastructure",
        "title": "Thủy điện & Giao thông (Sarawak & BR-163 Highway)",
        "selector": "#driver-infrastructure",
        "en": "Hydroelectric Mega-Dams and Highway Corridors. Projects like Batang Ai Dam and the Trans-Amazonian Highway flood hundreds of square kilometres of forest and initiate fishbone deforestation along road corridors.",
        "vi": "Các siêu đập thủy điện và Tuyến quốc lộ xuyên rừng. Các công trình như đập Batang Ai và đường cao tốc xuyên A-ma-dôn nhấn chìm hàng trăm ki-lô-mét vuông rừng và tạo ra mô hình phá rừng hình xương cá dọc theo hành lang giao thông."
    },
    {
        "id": "sec_environmental_impacts",
        "title": "2. Tác động môi trường nghiêm trọng của việc mất rừng",
        "selector": "#sec-environmental-impacts",
        "en": "Section 2: Severe Environmental Impacts of Forest Clearance. Deforestation eliminates biological diversity, disrupts global carbon sequestration, and triggers catastrophic soil erosion and siltation.",
        "vi": "Phần hai: Những tác động môi trường nghiêm trọng của việc phá rừng. Mất rừng làm suy giảm đa dạng sinh học, phá vỡ khả năng hấp thụ các-bon toàn cầu và gây ra xói mòn đất cùng bồi lắng phù sa thảm khốc."
    },
    {
        "id": "impact_erosion",
        "title": "Xói mòn đất & Mất tầng mùn (Soil Erosion & Leaching)",
        "selector": "#card-impact-erosion",
        "en": "Soil Erosion and Nutrient Leaching. Stripped of canopy interception, heavy torrential rain strikes bare ground directly. Topsoil washes into rivers, transforming fertile land into hardened laterite scrub.",
        "vi": "Xói mòn đất và Rửa trôi tầng mùn. Khi mất đi tầng tán che chắn, những cơn mưa xối xả đập trực tiếp xuống mặt đất trống. Lớp đất mặt màu mỡ bị cuốn trôi ra sông ngòi, biến đất rừng thành những vùng đất đá ong cằn cỗi."
    },
    {
        "id": "impact_carbon",
        "title": "Phát thải khí nhà kính & Mất bồn chứa Carbon",
        "selector": "#card-impact-carbon",
        "en": "Loss of Carbon Sinks and Global Warming. Tropical rainforests absorb billions of tonnes of carbon dioxide annually. Burning cleared vegetation releases massive carbon pulses, converting forests from net carbon sinks into net carbon sources.",
        "vi": "Mất bồn chứa Các-bon và Gia tăng hiệu ứng nhà kính. Rừng mưa hấp thụ hàng tỷ tấn khí các-bô-níc mỗi năm. Việc đốt phá cây rừng giải phóng một lượng lớn khí thải, biến rừng từ bể hấp thụ thành nguồn phát thải các-bon ròng."
    },
    {
        "id": "sec_tipping_point",
        "title": "3. Điểm bùng phát Amazon & Vòng lặp Xavan hóa (Tipping Point)",
        "selector": "#sec-tipping-point",
        "en": "Section 3: The Amazon Tipping Point and Savannification. Scientists project that exceeding twenty to twenty-five percent total deforestation could cause the hydrological cycle to collapse, irreversibly shifting fifty percent of the rainforest into dry savannah.",
        "vi": "Phần ba: Điểm bùng phát A-ma-dôn và Vòng xoáy Xavan hóa. Các nhà khoa học cảnh báo nếu tỷ lệ mất rừng vượt quá hai mươi đến hai mươi lăm phần trăm, vòng tuần hoàn nước sẽ sụp đổ, khiến một nửa diện tích rừng nhiệt đới biến thành đồng cỏ xavan khô hạn không thể phục hồi."
    },
    {
        "id": "loop_transpiration",
        "title": "Mất thoát hơi nước & Hạn hán kéo dài (Savannification Loop)",
        "selector": "#step-lost-transpiration",
        "en": "Lost Evapotranspiration and Diminished Rainfall. Over half of Amazonian rainfall is recycled from tree transpiration. Clearing trees deprives the atmosphere of aerial moisture, triggering severe extended droughts and forest fires.",
        "vi": "Mất thoát hơi nước và Suy giảm lượng mưa. Hơn một nửa lượng mưa ở A-ma-dôn bắt nguồn từ hơi nước do cây rừng bốc thoát. Chặt phá cây cối làm khô cạn bầu khí quyển, gây ra hạn hán kéo dài và cháy rừng lan rộng."
    },
    {
        "id": "sec_management",
        "title": "4. Chiến lược quản lý & Bảo tồn bền vững",
        "selector": "#sec-management",
        "en": "Section 4: Sustainable Management and Conservation Strategies. Safeguarding tropical rainforests requires integrating local selective harvesting with international financial frameworks like REDD-plus and debt-for-nature swaps.",
        "vi": "Phần bốn: Các chiến lược quản lý và Bảo tồn bền vững. Bảo vệ rừng mưa nhiệt đới đòi hỏi sự kết hợp giữa khai thác chọn lọc tại địa phương với các cơ chế tài chính quốc tế như chương trình giảm phát thải mất rừng và đổi nợ lấy bảo tồn thiên nhiên."
    },
    {
        "id": "strat_selective",
        "title": "Khai thác gỗ chọn lọc (Selective Logging) & Chứng chỉ FSC",
        "selector": "#strat-selective-logging",
        "en": "Selective Logging and FSC Certification. Only mature commercial trees over sixty centimetres in diameter are felled, leaving seedlings and canopy cover intact to regenerate the stand naturally.",
        "vi": "Khai thác gỗ chọn lọc và Chứng chỉ rừng quốc tế. Chỉ những cây gỗ trưởng thành có đường kính trên sáu mươi xăng-ti-mét mới được đốn hạ, giữ nguyên cây non và tầng tán để rừng tự tái sinh tự nhiên."
    },
    {
        "id": "strat_agroforestry",
        "title": "Nông lâm kết hợp (Agroforestry) & Trồng trọt dưới bóng râm",
        "selector": "#strat-agroforestry",
        "en": "Agroforestry Systems. Farmers cultivate cash crops such as cacao, coffee, and vanilla beneath native rainforest canopy trees, preserving soil fertility and animal biodiversity while securing resilient livelihoods.",
        "vi": "Mô hình Nông lâm kết hợp. Nông dân canh tác các loại cây có giá trị cao như ca-cao, cà phê và vani dưới bóng mát của tán rừng tự nhiên, vừa bảo vệ độ phì nhiêu của đất vừa tạo sinh kế lâu dài."
    },
    {
        "id": "strat_ecotourism",
        "title": "Du lịch sinh thái (Ecotourism - Danum Valley)",
        "selector": "#strat-ecotourism",
        "en": "Sustainable Ecotourism. Initiatives like Sabah's Danum Valley charge conservation entry fees, reinvesting tourist revenues directly into antipoaching ranger patrols and local community schools.",
        "vi": "Du lịch sinh thái bền vững. Các mô hình như Thung lũng Danum thu phí bảo tồn, tái đầu tư doanh thu du lịch trực tiếp vào các đội tuần tra kiểm lâm chống săn trộm và hỗ trợ giáo dục cộng đồng địa phương."
    },
    {
        "id": "strat_debt_redd",
        "title": "Đổi nợ lấy thiên nhiên (Debt-for-Nature) & Quỹ REDD+",
        "selector": "#strat-debt-redd",
        "en": "Debt-for-Nature Swaps and REDD-Plus. High-income nations cancel developing country sovereign debts in exchange for guaranteed legal forest reserves, creating powerful economic incentives to keep forests standing.",
        "vi": "Đổi nợ lấy thiên nhiên và Quỹ tín chỉ các-bon. Các nước phát triển xóa một phần nợ cho các quốc gia đang phát triển để đổi lấy cam kết thành lập các khu bảo tồn rừng pháp lý, tạo động lực kinh tế to lớn để giữ rừng."
    },
    {
        "id": "strat_indigenous",
        "title": "Quyền đất đai người bản địa (Indigenous Reserves)",
        "selector": "#strat-indigenous",
        "en": "Indigenous Territorial Rights. Satellite data proves that legally demarcated indigenous territories experience significantly lower deforestation rates than state parks, as indigenous tribes actively patrol ancestral lands.",
        "vi": "Quyền đất đai của các bộ tộc bản địa. Dữ liệu vệ tinh chứng minh rằng các vùng đất của người bản địa được pháp luật công nhận có tỷ lệ mất rừng thấp hơn đáng kể so với cả các vườn quốc gia, do các bộ tộc chủ động tuần tra bảo vệ lãnh thổ tổ tiên."
    },
    {
        "id": "summary_insights",
        "title": "📌 Tổng kết thi IGCSE: Cân bằng phát triển & Bảo tồn",
        "selector": "#card-summary-insights",
        "en": "IGCSE Core Summary. Successful rainforest conservation cannot rely on protectionism alone; it requires economic viability for local populations combined with decisive international carbon financing.",
        "vi": "Tổng kết trọng tâm bài thi. Bảo tồn rừng mưa thành công không thể chỉ dựa vào các lệnh cấm đoán thuần túy; nó đòi hỏi phải đảm bảo kinh tế cho người dân bản địa song hành cùng các nguồn tài chính các-bon quốc tế."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 5},
    "sec_deforestation_drivers": {"start": 1, "end": 5},
    "sec_environmental_impacts": {"start": 6, "end": 8},
    "sec_tipping_point": {"start": 9, "end": 10},
    "sec_management": {"start": 11, "end": 17}
}

def transform_html(raw_html):
    html = raw_html
    
    # 1. Header
    html = re.sub(
        r'(<div style="display:flex; gap:8px; align-items:center; margin-bottom:12px;">[\s\S]*?)(<h1 style="[^"]*">)',
        r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; border-radius:12px; padding:12px 16px; margin-bottom:16px; transition:all 0.2s ease;">\1\2',
        html, count=1
    )
    # close after key learning objectives
    html = re.sub(
        r'(🎯 Key Learning Objectives[\s\S]*?</ul>\s*</div>)',
        r'\1</div>',
        html, count=1
    )
    
    # 2. Section 1: Economic Drivers
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*1\. Primary Economic Drivers \(Causes\) of Deforestation\s*</h2>)',
        r'<div id="sec-deforestation-drivers" class="lecture-interactive-card" data-lecture-section="sec_deforestation_drivers" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*2\. Severe Environmental Impacts)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Driver hotspots in SVG 1
    html = html.replace('<g class="driver-hotspot" transform="translate(240, 240)">', '<g id="driver-cattle" class="driver-hotspot" data-lecture-section="driver_cattle" style="cursor:pointer;" transform="translate(240, 240)">')
    html = html.replace('<g class="driver-hotspot" transform="translate(740, 260)">', '<g id="driver-palmoil" class="driver-hotspot" data-lecture-section="driver_palmoil" style="cursor:pointer;" transform="translate(740, 260)">')
    html = html.replace('<g class="driver-hotspot" transform="translate(490, 250)">', '<g id="driver-logging" class="driver-hotspot" data-lecture-section="driver_logging" style="cursor:pointer;" transform="translate(490, 250)">')
    html = html.replace('<g class="driver-hotspot" transform="translate(710, 240)">', '<g id="driver-infrastructure" class="driver-hotspot" data-lecture-section="driver_infrastructure" style="cursor:pointer;" transform="translate(710, 240)">')
    
    # 3. Section 2: Impacts
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*2\. Severe Environmental Impacts of Forest Clearance\s*</h2>)',
        r'<div id="sec-environmental-impacts" class="lecture-interactive-card" data-lecture-section="sec_environmental_impacts" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*3\. The Amazon Tipping Point)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Impact cards
    html = html.replace(
        '<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:20px 0;">\n        <h4 style="margin:0 0 8px 0; color:#1e40af; font-size:16px; font-weight:700;">🌊 Soil Erosion, Nutrient Depletion & River Siltation</h4>',
        '<div id="card-impact-erosion" class="lecture-interactive-card" data-lecture-section="impact_erosion" style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:20px 0; cursor:pointer;">\n        <h4 style="margin:0 0 8px 0; color:#1e40af; font-size:16px; font-weight:700;">🌊 Soil Erosion, Nutrient Depletion & River Siltation</h4>'
    )
    html = html.replace(
        '<div style="background:#fef2f2; border:1px solid #fecaca; border-left:5px solid #dc2626; border-radius:10px; padding:18px; margin:20px 0;">\n        <h4 style="margin:0 0 8px 0; color:#991b1b; font-size:16px; font-weight:700;">🔥 Greenhouse Gas Emissions & Altered Microclimates</h4>',
        '<div id="card-impact-carbon" class="lecture-interactive-card" data-lecture-section="impact_carbon" style="background:#fef2f2; border:1px solid #fecaca; border-left:5px solid #dc2626; border-radius:10px; padding:18px; margin:20px 0; cursor:pointer;">\n        <h4 style="margin:0 0 8px 0; color:#991b1b; font-size:16px; font-weight:700;">🔥 Greenhouse Gas Emissions & Altered Microclimates</h4>'
    )
    
    # 4. Section 3: Tipping Point
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*3\. The Amazon Tipping Point & Savannification Feedback Loop\s*</h2>)',
        r'<div id="sec-tipping-point" class="lecture-interactive-card" data-lecture-section="sec_tipping_point" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*4\. Sustainable Management)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Step in SVG 2
    html = html.replace('<g class="loop-step" transform="translate(620, 40)">', '<g id="step-lost-transpiration" class="loop-step" data-lecture-section="loop_transpiration" style="cursor:pointer;" transform="translate(620, 40)">')
    
    # 5. Section 4: Management
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*4\. Sustainable Management & Conservation Strategies\s*</h2>)',
        r'<div id="sec-management" class="lecture-interactive-card" data-lecture-section="sec_management" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    # SVG 3 strategy cards
    html = html.replace('<g class="strat-card" transform="translate(20, 50)">', '<g id="strat-selective-logging" class="strat-card" data-lecture-section="strat_selective" style="cursor:pointer;" transform="translate(20, 50)">')
    html = html.replace('<g class="strat-card" transform="translate(195, 50)">', '<g id="strat-agroforestry" class="strat-card" data-lecture-section="strat_agroforestry" style="cursor:pointer;" transform="translate(195, 50)">')
    html = html.replace('<g class="strat-card" transform="translate(370, 50)">', '<g id="strat-ecotourism" class="strat-card" data-lecture-section="strat_ecotourism" style="cursor:pointer;" transform="translate(370, 50)">')
    html = html.replace('<g class="strat-card" transform="translate(545, 50)">', '<g id="strat-debt-redd" class="strat-card" data-lecture-section="strat_debt_redd" style="cursor:pointer;" transform="translate(545, 50)">')
    html = html.replace('<g class="strat-card" transform="translate(720, 50)">', '<g id="strat-indigenous" class="strat-card" data-lecture-section="strat_indigenous" style="cursor:pointer;" transform="translate(720, 50)">')
    
    # close section 4 before summary
    html = re.sub(
        r'(\s*)(<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0;">\s*<h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Geographical Insights</h3>)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Summary card
    html = html.replace(
        '<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0;">\n        <h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Geographical Insights</h3>',
        '<div id="card-summary-insights" class="lecture-interactive-card" data-lecture-section="summary_insights" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;">\n        <h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Geographical Insights</h3>'
    )
    
    return html

async def main():
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )
    
    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
    
    new_html = transform_html(raw_html)
    
    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")
    
    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == '__main__':
    asyncio.run(main())
