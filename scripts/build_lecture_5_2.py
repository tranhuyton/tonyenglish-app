import asyncio
import os
import re
from pathlib import Path
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "5_2"
LECTURE_ID = "23eee2fb-427c-4843-8d2d-ec296188730d"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "5.2 The Impacts of Climate Change at Multiple Scales"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Introduction to Climate Impacts",
        "en": "Welcome to Topic 5.2: The Impacts of Climate Change at Multiple Scales. In this lecture, we evaluate the uneven geographical consequences of global warming. We explore global thermal trajectories, examine an interactive world vulnerability map, unpack the physical mechanics of sea level rise, and evaluate systemic cascades on agriculture, marine life, and human health.",
        "vi": "Chào mừng các em đến với bài năm chấm hai: Các tác động của biến đổi khí hậu ở nhiều quy mô khác nhau. Trong bài giảng này, chúng ta sẽ đánh giá những hệ quả địa lý không đồng đều của hiện tượng ấm lên toàn cầu. Chúng ta sẽ khám phá xu hướng nhiệt độ toàn cầu, khảo sát bản đồ tương tác về các điểm nóng tổn thương trên thế giới, tìm hiểu cơ chế vật lý của mực nước biển dâng, và phân tích các tác động dây chuyền tới nông nghiệp, sinh vật biển và sức khỏe con người."
    },
    {
        "id": "sec_global_trends",
        "title": "1. Global Temperature Trends & IPCC Scenarios",
        "en": "Section 1 reviews instrumental thermal records. The Intergovernmental Panel on Climate Change confirms that global surface temperatures have risen by 1.1 to 1.2 degrees Celsius above pre-industrial levels. Crucially, every year since 1980 has been warmer than the twentieth-century average, with warming accelerating faster over the past 50 years than in any other half-century of the past two millennia.",
        "vi": "Mục một xem xét các ghi chép nhiệt độ thực tế. Ủy ban Liên chính phủ về Biến đổi Khí hậu khẳng định nhiệt độ bề mặt Trái Đất đã tăng từ một phẩy một đến một phẩy hai độ C so với thời tiền công nghiệp. Đáng chú ý, mọi năm kể từ năm 1980 đều nóng hơn mức trung bình của thế kỷ hai mươi, và tốc độ nóng lên trong năm mươi năm qua diễn ra nhanh hơn bất kỳ giai đoạn nửa thế kỷ nào trong hai nghìn năm qua."
    },
    {
        "id": "sec_hotspots_map",
        "title": "2. Multi-Scale Vulnerability Hotspots Map",
        "en": "Section 2 investigates regional vulnerability. Climate impacts vary widely based on latitude, elevation, proximity to the ocean, and local economic resilience. Click on any glowing hotspot pin on the map to explore specific regional and localized case studies.",
        "vi": "Mục hai khảo sát tính dễ bị tổn thương theo từng khu vực. Tác động của khí hậu rất khác nhau tùy thuộc vào vĩ độ, độ cao, khoảng cách tới biển và năng lực thích ứng kinh tế của địa phương. Hãy bấm vào từng điểm ghim phát sáng trên bản đồ để khám phá các bài học thực tế chi tiết."
    },
    {
        "id": "hotspot_arctic",
        "title": "Hotspot 1: Arctic & Greenland Cryosphere",
        "en": "The Arctic is experiencing Arctic amplification, warming up to four times faster than the global average. As reflective white sea ice melts, it exposes dark ocean water, dropping the surface albedo from 0.85 to 0.07. This positive feedback accelerates solar absorption, while Greenland loses 270 billion tonnes of ice annually.",
        "vi": "Vùng Bắc Cực đang trải qua hiện tượng khuếch đại cực, nóng lên nhanh gấp bốn lần mức trung bình toàn cầu. Khi băng tuyết màu trắng phản xạ nhiệt bị tan biến, bề mặt đại dương sẫm màu lộ ra, làm độ phản xạ suất giảm mạnh từ không phẩy tám mươi lăm xuống còn không phẩy không bảy. Vòng phản hồi thuận này làm tăng khả năng hấp thụ nhiệt từ Mặt Trời, trong khi dải băng Grin-lân mất khoảng hai trăm bảy mươi tỷ tấn băng mỗi năm."
    },
    {
        "id": "hotspot_himalaya",
        "title": "Hotspot 2: Himalayan Cryosphere (The Third Pole)",
        "en": "The Himalayan glaciers form the Third Pole, supplying meltwater to ten major Asian river systems that sustain 1.9 billion people. As glaciers retreat rapidly, initial melting forms dangerous moraine-dammed lakes that can burst in catastrophic floods. In the long term, depleted dry-season river flow threatens regional food and hydropower security.",
        "vi": "Các dòng sông băng Hi-ma-lay-a tạo thành Cực thứ ba của Trái Đất, cung cấp nguồn nước ngọt cho mười hệ thống sông lớn ở châu Á nuôi sống một phẩy chín tỷ người. Khi sông băng tan nhanh, ban đầu chúng tích tụ thành các hồ chứa nước có bờ đập bằng đất đá moraine rất dễ vỡ, gây lũ quét kinh hoàng. Về lâu dài, dòng chảy vào mùa khô cạn kiệt sẽ đe dọa nghiêm trọng an ninh lương thực và thủy điện khu vực."
    },
    {
        "id": "hotspot_bangladesh",
        "title": "Hotspot 3: Bangladesh Ganges-Brahmaputra Delta",
        "en": "Two-thirds of Bangladesh lies under five meters above sea level. Rising sea levels combine with powerful cyclone storm surges, driving saltwater over one hundred kilometers inland and destroying fertile paddy fields. Over fifty percent of informal slum dwellers in Dhaka are climate refugees displaced by coastal erosion.",
        "vi": "Hai phần ba diện tích Bangladesh nằm ở độ cao dưới năm mét so với mực nước biển. Nước biển dâng kết hợp với triều cường do bão nhiệt đới đẩy nước mặn xâm nhập sâu hơn một trăm cây số vào đất liền, phá hủy các ruộng lúa màu mỡ. Hơn năm mươi phần trăm cư dân tại các khu ổ chuột ở thủ đô Đắc-ca là những người tị nạn khí hậu bị mất nhà cửa do xói lở bờ biển."
    },
    {
        "id": "hotspot_maldives",
        "title": "Hotspot 4: Maldives & Small Island States",
        "en": "Eighty percent of the Maldives landmass lies less than one meter above sea level. A one-meter sea level rise would submerge most of the archipelago. Coral bleaching strips away the natural living wave barriers, and seawater contaminates the islands' thin freshwater lens, threatening national sovereignty.",
        "vi": "Tám mươi phần trăm diện tích đất đai của quần đảo Môn-đi-vơ nằm ở độ cao dưới một mét so với mặt nước biển. Mực nước biển dâng một mét sẽ nhấn chìm gần như toàn bộ quần đảo này. Hiện tượng tẩy trắng san hô phá hủy bức tường chắn sóng tự nhiên, đồng thời nước mặn ngấm vào làm nhiễm mặn túi nước ngọt mong manh dưới lòng đất, đe dọa trực tiếp sự tồn vong của quốc gia."
    },
    {
        "id": "hotspot_sahel",
        "title": "Hotspot 5: The African Sahel & Southern Africa",
        "en": "In the Sahel and Southern Africa, prolonged droughts and soaring temperatures drive desertification. Lake Chad has shrunk by ninety percent since 1960. By 2050, up to thirty percent of maize-growing areas and half of bean-growing lands in Southern Africa are projected to fail, triggering acute food shortages.",
        "vi": "Tại vùng Sa-hel và miền nam châu Phi, những đợt hạn hán kéo dài và nhiệt độ tăng vọt đang đẩy nhanh quá trình sa mạc hóa. Hồ Sát đã bị thu hẹp tới chín mươi phần trăm diện tích kể từ năm 1960. Dự báo đến năm 2050, ba mươi phần trăm diện tích trồng ngô và một nửa diện tích trồng đậu ở Nam Phi sẽ mất trắng, châm ngòi cho các cuộc khủng hoảng lương thực nghiêm trọng."
    },
    {
        "id": "hotspot_gbr",
        "title": "Hotspot 6: Great Barrier Reef Marine Ecosystem",
        "en": "The Great Barrier Reef has experienced multiple widespread mass bleaching events. When sea surface temperatures rise just one degree Celsius above the summer average, corals expel their vital symbiotic zooxanthellae algae, turning bone-white and starving, which shatters the marine food web.",
        "vi": "Rạn san hô Great Barrier ở nước Úc đã hứng chịu nhiều đợt tẩy trắng hàng loạt trên diện rộng. Khi nhiệt độ mặt nước biển chỉ cần tăng thêm một độ C so với mức cực đại mùa hè, san hô sẽ trục xuất các vi tảo cộng sinh ra ngoài, biến thành màu trắng bợt và chết đói, làm sụp đổ toàn bộ chuỗi thức ăn sinh vật biển."
    },
    {
        "id": "hotspot_amazon",
        "title": "Hotspot 7: Amazon Basin Savannisation Risk",
        "en": "The Amazon rainforest absorbs five percent of annual fossil emissions. Severe droughts desiccate the forest understory, rendering it highly flammable. Extensive fires push the biome toward a catastrophic tipping point where closed-canopy rainforest permanently converts into degraded dry savanna.",
        "vi": "Rừng mưa nhiệt đới A-ma-dôn hấp thụ khoảng năm phần trăm lượng khí thải nhiên liệu hóa thạch toàn cầu mỗi năm. Những trận hạn hán gay gắt làm khô kiệt thảm thực vật tầng dưới, khiến rừng rất dễ bắt lửa. Các vụ cháy rừng trên diện rộng đang đẩy khu rừng tới điểm giới hạn nguy hiểm, có nguy cơ biến rừng mưa thường xanh rậm rạp vĩnh viễn thành hoang mạc xavan khô cằn."
    },
    {
        "id": "hotspot_mediterranean",
        "title": "Hotspot 8: Mediterranean Basin & California",
        "en": "Expanding subtropical high-pressure ridges push storm tracks poleward, drying out Mediterranean regions and the American Southwest. Chronic water deficits, extended wildfire seasons, and agricultural crop failures create severe socio-economic strain across southern Europe and California.",
        "vi": "Sự mở rộng của các khối áp cao cận nhiệt đới đã đẩy các luồng bão lên phía cực, làm khô hạn khu vực Địa Trung Hải và vùng tây nam nước Mỹ. Tình trạng thiếu nước kéo dài, mùa cháy rừng tăng thêm nhiều tháng và mất mùa nông nghiệp đang gây ra áp lực kinh tế xã hội nặng nề tại Nam Âu và bang Ca-li-phoóc-ni-a."
    },
    {
        "id": "sec_sea_level",
        "title": "3. Sea Level Rise: Drivers & Human Exposure",
        "en": "Section 3 examines global sea level rise. Global mean sea level has risen by twenty-one to twenty-four centimeters since 1880, with the rate accelerating to 3.6 millimeters per year. Over 260 million people live in vulnerable coastal flood zones, sixty percent of them in tropical delta regions.",
        "vi": "Mục ba phân tích hiện tượng mực nước biển dâng toàn cầu. Mực nước biển trung bình đã dâng từ hai mươi mốt đến hai mươi tư xăng-ti-mét kể từ năm 1880, với tốc độ tăng tốc đạt ba phẩy sáu mi-li-mét mỗi năm. Hơn hai trăm sáu mươi triệu người đang sống trong các vùng đất ven biển có nguy cơ ngập lụt, với sáu mươi phần trăm trong số đó tập trung ở các vùng đồng bằng châu thổ nhiệt đới."
    },
    {
        "id": "slr_thermal_expansion",
        "title": "Driver A: Thermal Expansion (Steric Effect)",
        "en": "Water expands in volume as it absorbs heat. Because the oceans have absorbed over ninety percent of excess atmospheric thermal energy, expanding warmer water molecules account for roughly forty percent of modern sea level rise.",
        "vi": "Nước biển nở ra khi hấp thụ nhiệt độ. Bởi vì các đại dương đã hấp thụ hơn chín mươi phần trăm lượng nhiệt dư thừa của khí quyển, sự giãn nở nhiệt của các phân tử nước ấm đã đóng góp khoảng bốn mươi phần trăm vào tổng mức nước biển dâng hiện nay."
    },
    {
        "id": "slr_melting_ice",
        "title": "Driver B: Melting Land Ice",
        "en": "Melting continental glaciers and the vast ice sheets of Greenland and West Antarctica transfer millions of tons of solid freshwater ice into the ocean, adding physical mass to the marine system and contributing fifty-five percent of sea level rise.",
        "vi": "Sự tan chảy của các dòng sông băng trên lục địa cùng các dải băng khổng lồ tại đảo Grin-lân và Tây Nam Cực đã chuyển hàng triệu tấn băng nước ngọt vào lòng biển, bổ sung khối lượng nước khổng lồ và đóng góp năm mươi lăm phần trăm vào hiện tượng nước biển dâng."
    },
    {
        "id": "slr_terrestrial_storage",
        "title": "Driver C: Terrestrial Storage Depletion",
        "en": "Over-pumping deep underground aquifers for intensive agricultural irrigation transfers groundwater into rivers and oceans, accounting for the remaining five percent of annual sea level increases.",
        "vi": "Việc khai thác quá mức các túi nước ngầm sâu phục vụ tưới tiêu nông nghiệp quy mô lớn đã đưa lượng nước ngầm này ra sông ngòi và cuối cùng đổ vào biển, đóng góp năm phần trăm còn lại vào mức tăng mực nước biển hàng năm."
    },
    {
        "id": "sec_systemic_impacts",
        "title": "4. Systemic Cascades: Food, Ocean, Health & Migration",
        "en": "Section 4 highlights the cascading nature of climate disruptions. Reduced crop yields threaten tropical food security, absorbing excess CO2 turns oceans 30% more acidic, warmer temperatures spread mosquito-borne diseases like malaria and dengue, and severe weather creates millions of displaced climate refugees.",
        "vi": "Mục bốn làm nổi bật tính chất dây chuyền của các đợt gián đoạn khí hậu. Năng suất cây trồng sụt giảm đe dọa an ninh lương thực nhiệt đới, đại dương hấp thụ quá nhiều khí các-bô-níc khiến độ axit tăng thêm ba mươi phần trăm, nhiệt độ ấm hơn làm bùng phát các bệnh truyền nhiễm qua muỗi như sốt rét và sốt xuất huyết, đồng thời thời tiết cực đoan tạo ra hàng triệu người tị nạn khí hậu."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 1},
    "sec_global_trends": {"start": 1, "end": 1},
    "sec_hotspots_map": {"start": 2, "end": 10},
    "sec_sea_level": {"start": 11, "end": 14},
    "sec_systemic_impacts": {"start": 15, "end": 15}
}

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>1</div>\s*<h2[^>]*>Global Temperature Trends & IPCC Emissions Scenarios</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_global_trends" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Section 2: Hotspots Map Header
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*14px;">\s*<div[^>]*>2</div>\s*<h2[^>]*>Interactive Geographic Map: Multi-Scale Climate Vulnerability Hotspots</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_hotspots_map" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Hotspot pins onclick replacement
    pins = [
        ("arctic", "hotspot_arctic"),
        ("himalaya", "hotspot_himalaya"),
        ("bangladesh", "hotspot_bangladesh"),
        ("maldives", "hotspot_maldives"),
        ("sahel", "hotspot_sahel"),
        ("gbr", "hotspot_gbr"),
        ("amazon", "hotspot_amazon"),
        ("mediterranean", "hotspot_mediterranean")
    ]
    for key, sec_id in pins:
        old_pattern = f"onclick=\"showHotspot('{key}')\""
        new_pattern = f"onclick=\"showHotspot('{key}'); window.playLectureSection && window.playLectureSection('{sec_id}', event);\" class=\"hotspot-pin lecture-interactive-card\" data-lecture-section=\"{sec_id}\""
        html = html.replace(old_pattern, new_pattern)

    # Section 3: Sea level
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>3</div>\s*<h2[^>]*>Sea Level Rise: Physical Drivers & Exposure Vulnerability</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_sea_level" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Driver A
    html = re.sub(
        r'(<div style="background:\s*#f0fdfa;\s*border:\s*1px solid #99f6e4;[^"]*">)',
        r'<div class="lecture-interactive-card" data-lecture-section="slr_thermal_expansion" style="background: #f0fdfa; border: 1px solid #99f6e4; border-radius: 10px; padding: 16px; cursor: pointer;">',
        html,
        count=1
    )

    # Driver B
    html = re.sub(
        r'(<div style="background:\s*#f0f9ff;\s*border:\s*1px solid #bae6fd;[^"]*">)',
        r'<div class="lecture-interactive-card" data-lecture-section="slr_melting_ice" style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 10px; padding: 16px; cursor: pointer;">',
        html,
        count=1
    )

    # Driver C
    html = re.sub(
        r'(<div style="background:\s*#fdf4ff;\s*border:\s*1px solid #f5d0fe;[^"]*">)',
        r'<div class="lecture-interactive-card" data-lecture-section="slr_terrestrial_storage" style="background: #fdf4ff; border: 1px solid #f5d0fe; border-radius: 10px; padding: 16px; cursor: pointer;">',
        html,
        count=1
    )

    # Section 4: Systemic impacts
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>4</div>\s*<h2[^>]*>Systemic Human & Biospheric Cascades</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_systemic_impacts" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    return html

async def main():
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_html = f.read()

    new_html = transform_html(raw_html)

    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")

    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == "__main__":
    asyncio.run(main())
