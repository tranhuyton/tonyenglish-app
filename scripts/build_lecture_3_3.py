import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '3_3'
LECTURE_ID = '7d543b73-837d-4129-afc6-7196df47b6f6'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '3.3 The Characteristics of Tropical Rainforest Ecosystems'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 3.3: Hệ sinh thái Rừng mưa nhiệt đới",
        "selector": "#sec-header",
        "en": "Lesson 3.3: The Characteristics of Tropical Rainforest Ecosystems. In this lesson, we explore equatorial climate regimes, the vertical stratification of vegetation, remarkable plant and animal adaptations, and nutrient cycling via the Gersmehl model.",
        "vi": "Bài ba chấm ba: Đặc điểm của Hệ sinh thái Rừng mưa nhiệt đới. Trong bài học này, chúng ta sẽ tìm hiểu chế độ khí hậu xích đạo, sự phân tầng thẳng đứng của thảm thực vật, các thích nghi phi thường của động thực vật và chu trình dinh dưỡng theo mô hình Gơ-xmen."
    },
    {
        "id": "sec_climate_regime",
        "title": "1. Phân bố toàn cầu & Chế độ khí hậu xích đạo",
        "selector": "#sec-climate-regime",
        "en": "Section 1: Global Distribution and Equatorial Climate Regime. Located in an equatorial belt within ten degrees north and south of the equator. Rainforests thrive under high, constant temperatures averaging twenty-seven degrees Celsius and heavy annual rainfall exceeding two thousand millimetres.",
        "vi": "Phần một: Phân bố toàn cầu và Chế độ khí hậu xích đạo. Nằm trong vành đai xích đạo từ mười độ bắc đến mười độ nam. Rừng mưa phát triển mạnh mẽ dưới nền nhiệt cao và ổn định trung bình hai mươi bảy độ C cùng lượng mưa dồi dào trên hai nghìn mi-li-mét mỗi năm."
    },
    {
        "id": "dist_amazon",
        "title": "Lưu vực sông Amazon (Neotropics): 60% diện tích",
        "selector": "#hotspot-amazon",
        "en": "The Amazon Basin. Covering over six million square kilometres across South America, representing sixty percent of the world's remaining rainforest, harboring ten percent of all known species on Earth.",
        "vi": "Lưu vực sông A-ma-dôn. Trải rộng hơn sáu triệu ki-lô-mét vuông khắp Nam Mỹ, chiếm sáu mươi phần trăm diện tích rừng mưa còn lại của thế giới và là nơi cư trú của mười phần trăm tổng số loài sinh vật đã biết trên Trái Đất."
    },
    {
        "id": "dist_congo",
        "title": "Lưu vực sông Congo (Afrotropics): 18% diện tích",
        "selector": "#hotspot-congo",
        "en": "The Congo Basin. The second-largest rainforest on Earth, spanning nearly two million square kilometres across Central Africa, providing crucial carbon storage and home to lowland gorillas and forest elephants.",
        "vi": "Lưu vực sông Công-gô. Khu rừng mưa lớn thứ hai hành tinh, trải dài gần hai triệu ki-lô-mét vuông qua Trung Phi, đóng vai trò là bể chứa các-bon khổng lồ và là ngôi nhà của loài khỉ đột đất thấp cùng voi rừng."
    },
    {
        "id": "dist_seasia",
        "title": "Đông Nam Á & Vùng đất Sunda: Rừng rậm cổ xưa nhất",
        "selector": "#hotspot-seasia",
        "en": "Southeast Asia and Sundaland. Spanning Indonesia, Malaysia, and Papua New Guinea. These evolutionary ancient rainforests are dominated by giant dipterocarp hardwood trees and endangered orangutans.",
        "vi": "Đông Nam Á và Thềm lục địa Xun-đa. Bao gồm In-đô-nê-xi-a, Ma-lay-xi-a và Pa-pua Niu Ghi-nê. Những cánh rừng cổ xưa này bị thống trị bởi các loài cây họ Dầu thân gỗ khổng lồ cùng loài đười ươi đang bị đe dọa tuyệt chủng."
    },
    {
        "id": "daily_rainfall",
        "title": "Chu kỳ mưa đối lưu hàng ngày (Afternoon Thunderstorms)",
        "selector": "#card-daily-rainfall",
        "en": "The Daily Convectional Rainfall Cycle. Intense morning solar heating triggers rapid ground evaporation and plant transpiration. By midday, towering cumulonimbus clouds form, culminating in heavy torrential thunderstorms and lightning by mid-afternoon.",
        "vi": "Chu kỳ mưa đối lưu hàng ngày. Bức xạ mặt trời gay gắt vào buổi sáng kích hoạt sự bốc hơi nước dữ dội từ mặt đất và thoát hơi nước từ tán cây. Đến trưa, các đám mây vũ tích khổng lồ hình thành, gây ra những trận mưa dông như trút nước kèm sấm sét vào giữa chiều."
    },
    {
        "id": "sec_stratification",
        "title": "2. Phân tầng thẳng đứng của thảm thực vật (Forest Architecture)",
        "selector": "#sec-stratification",
        "en": "Section 2: Rainforest Vertical Stratification and Forest Architecture. Intense competition for solar radiation stratifies the rainforest into distinct vertical storeys, each defining a specialized microclimatic habitat.",
        "vi": "Phần hai: Sự phân tầng thẳng đứng của thảm thực vật. Sự cạnh tranh ánh sáng gay gắt chia rừng mưa nhiệt đới thành các tầng cấu trúc rõ rệt, mỗi tầng là một sinh cảnh vi khí hậu riêng biệt."
    },
    {
        "id": "strata_emergents",
        "title": "Tầng vượt tán (Emergents: 40m - 60m)",
        "selector": "#strata-emergents",
        "en": "The Emergent Layer. Giant pioneer hardwoods such as the Brazil nut and kapok tower up to sixty metres high. Exposed to gale-force winds, intense solar heat, and low humidity, they produce small waxy leaves and umbrella crowns.",
        "vi": "Tầng vượt tán. Các cây gỗ khổng lồ cao tới sáu mươi mét vươn hẳn lên trên tán rừng chính. Phải đối mặt với gió giật, nắng gắt và độ ẩm thấp, chúng phát triển lá nhỏ phủ sáp cùng tán hình chiếc dù."
    },
    {
        "id": "strata_canopy",
        "title": "Tầng tán chính (Canopy: 25m - 35m)",
        "selector": "#strata-canopy",
        "en": "The Canopy Layer. A dense, continuous sea of foliage capturing eighty percent of all incoming sunlight. It houses over seventy percent of rainforest animal biodiversity, including toucans, monkeys, tree frogs, and epiphytic orchids.",
        "vi": "Tầng tán chính. Một mái vòm lá cây rậm rạp và liên tục, chặn lại tám mươi phần trăm lượng ánh sáng mặt trời. Đây là nơi sinh sống của hơn bảy mươi phần trăm động vật rừng nhiệt đới, từ chim tơ-căng, khỉ, ếch cây cho đến các loài phong lan biểu sinh."
    },
    {
        "id": "strata_understory",
        "title": "Tầng dưới tán (Understory: 5m - 15m)",
        "selector": "#strata-understory",
        "en": "The Understory Layer. A dark, humid environment receiving only two to fifteen percent of sunlight. Plants develop broad, dark-green leaves packed with chlorophyll, while lianas climb tree trunks towards the canopy.",
        "vi": "Tầng dưới tán. Một không gian tối tăm và ẩm ướt chỉ nhận được từ hai đến mười lăm phần trăm ánh sáng. Cây cối ở đây phát triển phiến lá bản rộng màu xanh đậm chứa nhiều diệp lục, cùng các loài dây leo bám chặt vào thân gỗ để vươn lên đón sáng."
    },
    {
        "id": "strata_floor",
        "title": "Tầng đáy rừng & Rễ bạnh vè (Forest Floor: 0m - 5m)",
        "selector": "#strata-floor",
        "en": "The Forest Floor and Shrub Layer. Pitch black, receiving less than two percent of sunlight. Giant buttress roots provide surface anchoring on thin soils, while fungi and termites rapidly decompose falling organic matter within weeks.",
        "vi": "Tầng đáy rừng và Rễ bạnh vè. Không gian gần như tối hoàn toàn, chỉ nhận dưới hai phần trăm ánh sáng. Hệ thống rễ bạnh vè khổng lồ giúp giữ vững cây trên tầng đất mỏng, trong khi nấm và mối phân hủy nhanh chóng các xác bã hữu cơ rơi rụng chỉ trong vài tuần."
    },
    {
        "id": "sec_adaptations",
        "title": "3. Thích nghi sinh thái của Động - Thực vật",
        "selector": "#sec-adaptations",
        "en": "Section 3: Plant and Animal Adaptations to Rainforest Niches. High heat and extreme humidity drive evolutionary specialization: drip-tip leaves shed rain rapidly to prevent fungal decay, while buttress roots anchor shallow root networks.",
        "vi": "Phần ba: Thích nghi sinh thái của Động và Thực vật. Nhiệt độ cao và độ ẩm cực lớn thúc đẩy những thích nghi tiến hóa đặc thù: chóp lá nhỏ giọt giúp thoát nước mưa nhanh tránh nấm mốc, còn rễ bạnh vè nâng đỡ mạng lưới rễ nông."
    },
    {
        "id": "adapt_flora_trf",
        "title": "Thích nghi thực vật: Chóp lá nhỏ giọt, Rễ bạnh & Dây leo",
        "selector": "#card-adapt-flora-trf",
        "en": "Botanical Adaptations. Drip-tip leaves channel heavy downpours off the foliage, preventing moss overgrowth. Epiphytes grow on tree branches without soil, absorbing airborne moisture, while strangler figs encase host trees to reach sunlight.",
        "vi": "Thích nghi ở thực vật. Đầu lá thuôn nhọn nhỏ giọt giúp trút nước mưa xối xả, ngăn rêu mốc phát triển. Cây biểu sinh bám trên cành gỗ không cần đất, hút ẩm từ không khí, trong khi cây đa bóp cổ bao bọc lấy cây chủ để vươn lên đón nắng."
    },
    {
        "id": "adapt_fauna_trf",
        "title": "Thích nghi động vật: Đuôi cầm nắm, Ngụy trang & Tiếng kêu",
        "selector": "#card-adapt-fauna-trf",
        "en": "Zoological Adaptations. Tree frogs develop sticky suction pads on toes for vertical climbing. Spider monkeys use strong prehensile tails as a fifth limb, and loud acoustic vocalizations allow parrots and howler monkeys to communicate across dense canopies.",
        "vi": "Thích nghi ở động vật. Ếch cây phát triển các đệm giác hút ở đầu ngón chân để leo trèo thẳng đứng. Khỉ nhện sử dụng đuôi cầm nắm linh hoạt như một chi thứ năm, và tiếng hú vang dội giúp vẹt cùng khỉ rú giao tiếp xuyên qua các tán lá rậm rạp."
    },
    {
        "id": "sec_gersmehl",
        "title": "4. Chu trình dinh dưỡng & Thổ nhưỡng: Mô hình Gersmehl",
        "selector": "#sec-gersmehl",
        "en": "Section 4: Nutrient Cycling and Soil Dynamics: The Gersmehl Model. The tropical rainforest presents a profound ecological paradox: luxuriant, colossal plant biomass flourishing on highly leached, infertile, acidic latosol soils.",
        "vi": "Phần bốn: Chu trình dinh dưỡng và Động thái đất: Mô hình Gơ-xmen. Rừng mưa nhiệt đới thể hiện một nghịch lý sinh thái sâu sắc: sinh khối thực vật khổng lồ tươi tốt lại phát triển trên nền đất đỏ vàng latosol chua, nghèo dinh dưỡng và bị rửa trôi nặng nề."
    },
    {
        "id": "gersmehl_biomass",
        "title": "Kho Sinh khối khổng lồ (Biomass Store - B)",
        "selector": "#node-biomass",
        "en": "The Gigantic Biomass Store. Over seventy-five to eighty percent of all ecosystem nutrients are locked inside living organic matter: giant tree trunks, thick branches, and dense foliage.",
        "vi": "Kho Sinh khối khổng lồ. Hơn bảy mươi lăm đến tám mươi phần trăm tổng lượng chất dinh dưỡng của hệ sinh thái được lưu trữ ngay bên trong vật chất hữu cơ sống: những thân gỗ khổng lồ, cành lá rậm rạp."
    },
    {
        "id": "gersmehl_litter",
        "title": "Kho Thảm mục nhỏ & Phân hủy siêu tốc (Litter Store - L)",
        "selector": "#node-litter",
        "en": "The Small Litter Store and Rapid Decomposition. While leaf fall is continuous all year round, constant high heat and moist soil allow decomposers, fungi, and termites to recycle organic litter within weeks.",
        "vi": "Kho Thảm mục nhỏ và Quá trình phân hủy siêu tốc. Dù lá rụng liên tục quanh năm, nhưng nhiệt độ cao và độ ẩm lớn giúp vi sinh vật, nấm và mối phân hủy xác lá chỉ trong vài tuần."
    },
    {
        "id": "gersmehl_soil",
        "title": "Kho Đất nghèo & Rửa trôi rửa trôi mạnh (Soil Store - S)",
        "selector": "#node-soil",
        "en": "The Poor Soil Store and Extreme Leaching. Heavy daily rainfall continuously leaches soluble nutrients deep underground beyond root reach. Dense shallow root carpets must reabsorb nutrients instantly as soon as litter decays.",
        "vi": "Kho Đất nghèo và Sự rửa trôi rửa trôi mãnh liệt. Những trận mưa xối xả hàng ngày liên tục hòa tan và rửa trôi chất dinh dưỡng xuống sâu khỏi tầng rễ. Mạng lưới rễ nông dày đặc phải hút ngược chất khoáng ngay khi thảm mục vừa phân hủy."
    },
    {
        "id": "summary_concepts",
        "title": "📌 Tổng kết: Các khái niệm địa lý cốt lõi bài 3.3",
        "selector": "#card-summary-concepts",
        "en": "IGCSE Core Summary. Rainforest stability depends entirely on rapid closed-loop nutrient cycling between biomass and litter. If trees are felled and removed, the fragile nutrient cycle collapses instantly, leaving barren, infertile bedrock behind.",
        "vi": "Tổng kết trọng tâm bài thi. Sự ổn định của rừng mưa hoàn toàn phụ thuộc vào chu trình dinh dưỡng vòng tròn khép kín cực nhanh giữa sinh khối và thảm mục. Nếu cây cối bị chặt hạ và mang đi, chu trình mỏng manh này sẽ sụp đổ ngay lập tức, chỉ để lại một vùng đất trơ trọi và cằn cỗi."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 5},
    "sec_climate_regime": {"start": 1, "end": 5},
    "sec_stratification": {"start": 6, "end": 10},
    "sec_adaptations": {"start": 11, "end": 13},
    "sec_gersmehl": {"start": 14, "end": 18}
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
    
    # 2. Section 1: Global Distribution
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*1\. Global Distribution & The Equatorial Climate Regime\s*</h2>)',
        r'<div id="sec-climate-regime" class="lecture-interactive-card" data-lecture-section="sec_climate_regime" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*2\. Rainforest Vertical Stratification)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Hotspots in SVG 1
    html = html.replace('<g class="trf-hotspot" transform="translate(240, 240)">', '<g id="hotspot-amazon" class="trf-hotspot" data-lecture-section="dist_amazon" style="cursor:pointer;" transform="translate(240, 240)">')
    html = html.replace('<g class="trf-hotspot" transform="translate(490, 250)">', '<g id="hotspot-congo" class="trf-hotspot" data-lecture-section="dist_congo" style="cursor:pointer;" transform="translate(490, 250)">')
    html = html.replace('<g class="trf-hotspot" transform="translate(740, 260)">', '<g id="hotspot-seasia" class="trf-hotspot" data-lecture-section="dist_seasia" style="cursor:pointer;" transform="translate(740, 260)">')
    
    # Daily convectional rainfall card
    html = html.replace(
        '<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:20px 0;">\n        <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:16px; font-weight:700;">⚡ The Daily Convectional Rainfall Cycle (Afternoon Thunderstorms)</h4>',
        '<div id="card-daily-rainfall" class="lecture-interactive-card" data-lecture-section="daily_rainfall" style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:20px 0; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:16px; font-weight:700;">⚡ The Daily Convectional Rainfall Cycle (Afternoon Thunderstorms)</h4>'
    )
    
    # 3. Section 2: Stratification
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*2\. Rainforest Vertical Stratification & Forest Architecture\s*</h2>)',
        r'<div id="sec-stratification" class="lecture-interactive-card" data-lecture-section="sec_stratification" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*3\. Plant & Animal Adaptations)',
        r'</div>\1\2',
        html, count=1
    )
    
    # SVG 2 Strata bands
    html = html.replace('<g class="strata-band" transform="translate(200, 30)">', '<g id="strata-emergents" class="strata-band" data-lecture-section="strata_emergents" style="cursor:pointer;" transform="translate(200, 30)">')
    html = html.replace('<g class="strata-band" transform="translate(200, 145)">', '<g id="strata-canopy" class="strata-band" data-lecture-section="strata_canopy" style="cursor:pointer;" transform="translate(200, 145)">')
    html = html.replace('<g class="strata-band" transform="translate(200, 290)">', '<g id="strata-understory" class="strata-band" data-lecture-section="strata_understory" style="cursor:pointer;" transform="translate(200, 290)">')
    html = html.replace('<g class="strata-band" transform="translate(200, 420)">', '<g id="strata-floor" class="strata-band" data-lecture-section="strata_floor" style="cursor:pointer;" transform="translate(200, 420)">')
    
    # 4. Section 3: Adaptations
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*3\. Plant & Animal Adaptations to Rainforest Niches\s*</h2>)',
        r'<div id="sec-adaptations" class="lecture-interactive-card" data-lecture-section="sec_adaptations" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*4\. Nutrient Cycling & Soil Dynamics)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Adaptation cards
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; margin:24px 0;">\n        <div style="background:#0f172a; color:#ffffff; padding:12px 18px; font-weight:700; font-size:15px;">\n            Key Botanical & Anatomical Adaptations in the Rainforest',
        '<div id="card-adapt-flora-trf" class="lecture-interactive-card" data-lecture-section="adapt_flora_trf" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; margin:24px 0; cursor:pointer;">\n        <div style="background:#0f172a; color:#ffffff; padding:12px 18px; font-weight:700; font-size:15px;">\n            Key Botanical & Anatomical Adaptations in the Rainforest'
    )
    
    # 5. Section 4: Gersmehl
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*4\. Nutrient Cycling & Soil Dynamics: The Gersmehl Model\s*</h2>)',
        r'<div id="sec-gersmehl" class="lecture-interactive-card" data-lecture-section="sec_gersmehl" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    # SVG 3 Gersmehl nodes
    html = html.replace('<g class="cycle-node" transform="translate(100, 70)">', '<g id="node-biomass" class="cycle-node" data-lecture-section="gersmehl_biomass" style="cursor:pointer;" transform="translate(100, 70)">')
    html = html.replace('<g class="cycle-node" transform="translate(630, 70)">', '<g id="node-litter" class="cycle-node" data-lecture-section="gersmehl_litter" style="cursor:pointer;" transform="translate(630, 70)">')
    html = html.replace('<g class="cycle-node" transform="translate(365, 340)">', '<g id="node-soil" class="cycle-node" data-lecture-section="gersmehl_soil" style="cursor:pointer;" transform="translate(365, 340)">')
    
    # close section 4 before summary
    html = re.sub(
        r'(\s*)(<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0;">\s*<h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Geographical Concepts</h3>)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Summary card
    html = html.replace(
        '<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0;">\n        <h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Geographical Concepts</h3>',
        '<div id="card-summary-concepts" class="lecture-interactive-card" data-lecture-section="summary_concepts" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;">\n        <h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Geographical Concepts</h3>'
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
