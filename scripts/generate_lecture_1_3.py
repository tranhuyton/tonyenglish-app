import asyncio
import edge_tts
import subprocess
import os
import json
import sys
import glob
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

LECTURE_ID = "fea9a6ec-9ff0-456a-9185-4076073b04c1"
AUDIO_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'geography', '1_3')
SCRATCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'scratch', 'audio_temp_1_3')
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

EN_VOICE = 'en-GB-RyanNeural'       # Authentic Male British English
VI_VOICE = 'vi-VN-HoaiMyNeural'     # Authentic Northern Vietnamese (Hanoi accent, 100% natural, pristine)

# TUYỆT ĐỐI 100% TIẾNG VIỆT THUẦN TÚY TRONG PHẦN 'vi':
SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.3",
        "selector": "#sec-header",
        "en": "Lesson 1.3: Rivers present opportunities and hazards for people. In this lesson, we explore how human societies benefit from rivers and how we manage the risks they pose.",
        "vi": "Bài một chấm ba: Sông ngòi đem lại cơ hội và hiểm họa cho con người. Trong bài học này, chúng ta sẽ tìm hiểu cách các xã hội loài người thụ hưởng lợi ích từ những dòng sông cũng như cách ứng phó và kiểm soát các nguy cơ do chúng gây ra."
    },
    {
        "id": "svg_overview",
        "title": "Tổng quan: Cơ hội & Hiểm họa sông ngòi",
        "selector": "#sec-svg-overview",
        "en": "Living Near Rivers: Opportunities and Hazards Overview. Rivers sustain human civilizations through water, food, power, and transport, but they also bring devastating floods and pollution.",
        "vi": "Tổng quan về Cơ hội và Hiểm họa khi sinh sống ven sông. Sông ngòi nuôi dưỡng các nền văn minh nhân loại bằng nguồn nước ngọt, lương thực, năng lượng và giao thông, song cũng tiềm ẩn hiểm họa lũ lụt khốc liệt và ô nhiễm môi trường."
    },
    {
        "id": "icon_water_supply",
        "title": "Nguồn cấp nước (Water Supply)",
        "selector": "#icon-water-supply",
        "en": "Water Supply. Rivers provide an indispensable perennial source of fresh water for domestic drinking, cooking, sanitation, industrial manufacturing, and agricultural irrigation.",
        "vi": "Nguồn cung cấp nước ngọt. Sông ngòi cung cấp nguồn nước ngọt quanh năm không thể thiếu cho sinh hoạt ăn uống, vệ sinh, sản xuất công nghiệp và tưới tiêu nông nghiệp."
    },
    {
        "id": "icon_agriculture",
        "title": "Nông nghiệp & Phù sa (Agriculture)",
        "selector": "#icon-agriculture",
        "en": "Agriculture and Fertile Soils. Floodwaters deposit nutrient-rich alluvium across valley floors, creating exceptionally fertile soils that have supported civilization since ancient antiquity.",
        "vi": "Nông nghiệp và Đất đai màu mỡ. Dòng nước lũ bồi đắp các lớp phù sa giàu dinh dưỡng khắp vùng đồng bằng ngập lũ, tạo nên những dải đất phì nhiêu nuôi sống các nền văn minh từ thời cổ đại."
    },
    {
        "id": "icon_fishing",
        "title": "Đánh bắt thủy sản (Fishing)",
        "selector": "#icon-fishing",
        "en": "Fishing and Aquatic Food. Freshwater ecosystems and inland wetlands provide essential dietary protein and sustain livelihoods for millions of artisanal fishing communities worldwide.",
        "vi": "Đánh bắt và Thủy sản nước ngọt. Các hệ sinh thái sông và vùng đất ngập nước nội địa cung cấp nguồn đạm dinh dưỡng thiết yếu và tạo kế sinh nhai cho hàng triệu ngư dân trên toàn thế giới."
    },
    {
        "id": "icon_transport",
        "title": "Giao thông thủy & Thương mại (Transport)",
        "selector": "#icon-transport",
        "en": "Transport and Trade. Navigable rivers act as natural commercial waterways, lowering freight shipping costs and fostering the expansion of major inland and estuarine port cities.",
        "vi": "Giao thông thủy và Thương mại. Các dòng sông cho phép tàu thuyền lưu thông đóng vai trò như những tuyến đường cao tốc tự nhiên, giảm chi phí vận chuyển hàng hóa và thúc đẩy sự hưng thịnh của các đô thị cảng."
    },
    {
        "id": "icon_tourism",
        "title": "Du lịch & Nghỉ dưỡng (Tourism)",
        "selector": "#icon-tourism",
        "en": "Tourism and Recreation. Picturesque river gorges, waterfalls, and meandering valleys attract tourism, recreational water sports, and drive high-value riverside property development.",
        "vi": "Du lịch và Nghỉ dưỡng. Cảnh quan hẻm vực kỳ vĩ, thác nước và các thung lũng uốn khúc thơ mộng thu hút khách du lịch, phát triển thể thao dưới nước và làm gia tăng giá trị bất động sản ven sông."
    },
    {
        "id": "icon_hep",
        "title": "Thủy điện & Công nghiệp (HEP & Industry)",
        "selector": "#icon-hep",
        "en": "Hydroelectric Power and Industry. Dams exploit gravitational water potential to generate renewable electricity and support multipurpose industrial development schemes.",
        "vi": "Thủy điện và Công nghiệp. Các con đập ngăn sông khai thác thế năng và động năng của dòng nước để sản xuất điện năng tái tạo sạch, đồng thời phục vụ các dự án công nghiệp đa mục tiêu."
    },
    {
        "id": "icon_flooding",
        "title": "Hiểm họa Lũ lụt (Flooding)",
        "selector": "#icon-flooding",
        "en": "Flooding Hazard. When river discharge exceeds bankfull capacity, water inundates adjacent land, threatening human life, destroying property, and disrupting economic activity.",
        "vi": "Hiểm họa Lũ lụt. Khi lưu lượng nước vượt quá dung tích chứa của lòng sông, nước lũ tràn bờ nhấn chìm các vùng đất xung quanh, đe dọa sinh mạng, tàn phá tài sản và đình trệ các hoạt động kinh tế."
    },
    {
        "id": "icon_pollution",
        "title": "Ô nhiễm nước sông (River Pollution)",
        "selector": "#icon-pollution",
        "en": "River Pollution. Industrial chemical effluents, agricultural fertiliser runoff, and untreated sewage contaminate river water, triggering eutrophication and devastating ecosystems.",
        "vi": "Ô nhiễm Môi trường nước sông. Nước thải công nghiệp, hóa chất nông nghiệp dư thừa và nước thải sinh hoạt chưa qua xử lý làm ô nhiễm nguồn nước, gây hiện tượng phì dưỡng và hủy hoại hệ sinh thái."
    },
    {
        "id": "icon_management",
        "title": "Chiến lược chống lũ (Flood Management)",
        "selector": "#icon-management",
        "en": "Flood Management Strategies. Communities protect vulnerable floodplains using a blend of hard engineering physical structures and sustainable soft engineering nature-based techniques.",
        "vi": "Chiến lược Quản lý và Phòng chống lũ lụt. Con người bảo vệ các vùng đồng bằng ngập lũ thông qua sự kết hợp giữa các công trình công trình cứng truyền thống và các biện pháp công trình mềm bền vững thuận theo tự nhiên."
    },
    {
        "id": "sec_opportunities",
        "title": "Phần 1: Các cơ hội sinh sống ven sông",
        "selector": "#sec-opportunities",
        "en": "Section 1: Opportunities of Living Near Rivers. Since the dawn of human history, river valleys have served as magnets for civilization, providing vital resources for survival and economic growth.",
        "vi": "Phần một: Các cơ hội khi định cư ven sông. Từ thuở bình minh của lịch sử, các thung lũng sông đã luôn là thỏi nam châm thu hút dân cư, mang lại nguồn tài nguyên thiết yếu cho sinh tồn và phát triển thịnh vượng."
    },
    {
        "id": "opp_overview",
        "title": "Cái nôi của các nền văn minh cổ đại",
        "selector": "#card-opp-overview",
        "en": "Historical River Civilizations. The world's earliest great societies, including Egypt along the Nile, Mesopotamia between the Tigris and Euphrates, and the Indus Valley, all flourished because of reliable river water and fertile floodplains.",
        "vi": "Các nền văn minh sông ngòi cổ đại. Những nền văn minh rực rỡ đầu tiên của nhân loại như Ai Cập cổ đại bên dòng sông Nin, Lưỡng Hà giữa sông Ti-gơ-rơ và Ơ-phơ-rát, hay nền văn minh lưu vực sông Ấn, đều đơm hoa kết trái nhờ nguồn nước ngọt dồi dào và phù sa châu thổ."
    },
    {
        "id": "opp_water",
        "title": "Nguồn cấp nước sinh hoạt và sản xuất",
        "selector": "#card-opp-water",
        "en": "Water Supply Reliability. Rivers maintain continuous freshwater discharge essential for large human settlements, sanitation infrastructure, and modern industrial cooling and processing systems.",
        "vi": "Nguồn cấp nước ổn định. Sông ngòi duy trì dòng chảy nước ngọt liên tục, đáp ứng nhu cầu sinh hoạt của các đại đô thị, mạng lưới vệ sinh cũng như hệ thống làm mát và xử lý trong công nghiệp hiện đại."
    },
    {
        "id": "opp_agri",
        "title": "Nông nghiệp & Đồng bằng phù sa sông Nin",
        "selector": "#card-opp-agri",
        "en": "Agriculture and Alluvial Floodplains. Annual river floods deposit fine mineral-rich alluvium. As illustrated by the Nile valley in Figure 1.34, this creates lush, narrow green ribbons of intense cultivation amidst surrounding arid desert terrain.",
        "vi": "Nông nghiệp và Đất phù sa châu thổ. Các đợt lũ hàng năm bồi lắng lớp phù sa mịn màng chứa nhiều khoáng chất màu mỡ. Tiêu biểu như thung lũng sông Nin ở hình một chấm ba tư, tạo nên một dải xanh nông nghiệp trù phú nổi bật giữa lòng sa mạc cằn cỗi."
    },
    {
        "id": "opp_fishing",
        "title": "Khai thác và nuôi trồng thủy sản",
        "selector": "#card-opp-fishing",
        "en": "Productive Fisheries and Aquaculture. Natural river habitats and flood-fed inland wetlands support rich fish stocks. Freshwater aquaculture is now the fastest growing food production sector globally.",
        "vi": "Khai thác Thủy sản và Nuôi trồng thủy sản. Môi trường sông ngòi tự nhiên và vùng ngập nước trù phú cung cấp lượng cá dồi dào, đưa ngành nuôi trồng thủy sản nước ngọt trở thành một trong những lĩnh vực sản xuất lương thực tăng trưởng nhanh nhất."
    },
    {
        "id": "opp_transport",
        "title": "Giao thông thủy nội địa & Cửa ngõ thương mại",
        "selector": "#card-opp-transport",
        "en": "Inland Navigation and Global Hubs. Rivers offer low friction bulk cargo transport. Many global metropolises, including London, Shanghai, and Cairo, developed at strategic river crossing and estuarine shipping points.",
        "vi": "Giao thông thủy nội địa và Cửa ngõ thương mại. Sông ngòi cho phép vận chuyển hàng hóa khối lượng lớn với chi phí ma sát thấp. Nhiều đại đô thị lớn trên thế giới như Luân Đôn, Thượng Hải hay Cai-rô đều được hình thành tại các vị trí vượt sông và cửa biển chiến lược."
    },
    {
        "id": "opp_hep",
        "title": "Thủy điện & Dự án đa mục tiêu sông Danube",
        "selector": "#card-opp-hep",
        "en": "Hydroelectric Power and Multipurpose Schemes. As shown in Figure 1.35 on the River Danube, multipurpose barrages harness water flow to generate clean electricity while regulating river levels for navigation and flood protection.",
        "vi": "Thủy điện và Các dự án đa mục tiêu. Như mô tả ở hình một chấm ba lăm trên sông Đa-nuýp, các âu thuyền và đập nước đa mục tiêu vừa khai thác dòng chảy để phát điện sạch, vừa điều tiết mực nước phục vụ giao thông thủy và cắt lũ an toàn."
    },
    {
        "id": "opp_tourism",
        "title": "Du lịch, thể thao & Bất động sản ven sông",
        "selector": "#card-opp-tourism",
        "en": "Tourism, Leisure, and Waterfront Living. Spectacular river scenery stimulates boat excursions, kayaking, angling, and walking trails, driving local service economies and attracting premium residential developments.",
        "vi": "Du lịch, Thể thao giải trí và Đô thị ven sông. Phong cảnh sông nước ngoạn mục thúc đẩy các tour du thuyền, chèo thuyền vượt ghềnh, câu cá dã ngoại, tạo động lực phát triển kinh tế dịch vụ và nâng tầm các khu đô thị sinh thái."
    },
    {
        "id": "sec_floods",
        "title": "Phần 2: Hiểm họa Lũ lụt (Floods)",
        "selector": "#sec-floods",
        "en": "Section 2: The Hazard of Floods. Flooding happens when river discharge exceeds the carrying capacity of the channel, causing catastrophic overflow onto the adjoining floodplains.",
        "vi": "Phần hai: Hiểm họa Lũ lụt. Hiện tượng ngập lụt xảy ra khi lưu lượng nước trên sông vượt quá khả năng thoát lũ của lòng máng, làm dòng nước tràn qua bờ đê và tàn phá vùng đồng bằng xung quanh."
    },
    {
        "id": "causes_natural",
        "title": "Các nguyên nhân tự nhiên gây lũ",
        "selector": "#card-causes-natural",
        "en": "Natural Causes of River Flooding. Prolonged, intense rainfall saturates soil, triggering high surface runoff. Rapid spring snowmelt rapidly swells headwaters, while steep relief and impermeable bedrock hasten peak discharge.",
        "vi": "Các nguyên nhân tự nhiên gây lũ. Những đợt mưa lớn kéo dài làm bão hòa đất dẫn đến dòng chảy tràn mặt đất tăng vọt. Hiện tượng tuyết tan nhanh vào mùa xuân, cùng với địa hình đồi núi dốc và các tầng đá ngầm không thấm nước làm đỉnh lũ dâng cao nhanh chóng."
    },
    {
        "id": "causes_human",
        "title": "Các tác nhân nhân tạo làm trầm trọng lũ",
        "selector": "#card-causes-human",
        "en": "Human Causes of River Flooding. Urbanisation covers soil with impermeable tarmac and concrete drains, accelerating overland flow. Deforestation eliminates tree interception, while building on floodplains reduces natural flood storage.",
        "vi": "Các nguyên nhân nhân tạo gây lũ. Quá trình đô thị hóa phủ kín mặt đất bằng bê tông và hệ thống cống thoát nước, đẩy nhanh dòng chảy bề mặt. Nạn phá rừng làm mất đi tán cây giữ nước, và việc xây dựng lấn chiếm đồng bằng ngập lũ làm mất đi các túi chứa lũ tự nhiên."
    },
    {
        "id": "flood_impacts",
        "title": "Phân loại tác động của lũ (Cấp 1, 2, 3)",
        "selector": "#card-flood-impacts",
        "en": "Classification of Flood Impacts. Primary impacts are immediate direct damage, including drowning and collapsed bridges. Secondary impacts follow shortly, such as contaminated water and cholera outbreaks. Tertiary impacts are long-term consequences, including soil degradation and insurance losses.",
        "vi": "Phân loại tác động của lũ lụt. Tác động cấp một là thiệt hại trực tiếp ngay tức thì như chết đuối và sập cầu cống. Tác động cấp hai xuất hiện ngay sau đó như ô nhiễm nguồn nước và dịch bệnh bùng phát. Tác động cấp ba là những hệ lụy lâu dài như thoái hóa đất nông nghiệp và tổn thất kinh tế kéo dài."
    },
    {
        "id": "sec_management",
        "title": "Phần 3: Quản lý và phòng chống lũ lụt",
        "selector": "#sec-management",
        "en": "Section 3: River Flood Management. River engineering strategies seek to minimize flood damage, divided into heavy structural hard engineering and nature-based soft engineering approaches.",
        "vi": "Phần ba: Quản lý và Phòng chống lũ lụt. Các chiến lược công trình hướng đến việc giảm thiểu tối đa rủi ro ngập lụt, được chia thành giải pháp công trình cứng quy mô lớn và giải pháp công trình mềm hài hòa với thiên nhiên."
    },
    {
        "id": "hard_eng",
        "title": "Giải pháp công trình cứng (Hard Engineering)",
        "selector": "#card-hard-eng",
        "en": "Hard Engineering Strategies. Hard engineering uses massive man-made barriers, such as upstream storage dams, concrete embankments, channel straightening, and movable tidal barriers like the Thames Barrier in Figure 1.38. While protective, they are costly and can worsen flooding downstream.",
        "vi": "Các giải pháp công trình cứng. Giải pháp này sử dụng các công trình nhân tạo kiên cố như đập tích nước thượng lưu, đê bê tông, nắn thẳng lòng sông và đập chắn triều di động như Đập chắn sông Thêm ở hình một chấm ba tám. Dù đem lại hiệu quả bảo vệ tức thì nhưng chi phí rất đắt đỏ và có thể đẩy nguy cơ ngập lụt xuống vùng hạ lưu."
    },
    {
        "id": "soft_eng",
        "title": "Giải pháp công trình mềm (Soft Engineering)",
        "selector": "#card-soft-eng",
        "en": "Soft Engineering Strategies. Soft engineering works symbiotically with nature. It includes real-time flood warning systems, floodplain land-use zoning, catchment afforestation to delay runoff, and restored river meanders that naturally slow down torrents.",
        "vi": "Các giải pháp công trình mềm. Giải pháp mềm hoạt động dựa trên sự thích ứng và tôn trọng tự nhiên. Bao gồm hệ thống dự báo cảnh báo lũ sớm, quy hoạch phân vùng sử dụng đất, trồng rừng đầu nguồn để giữ nước và phục hồi các khúc uốn tự nhiên nhằm làm chậm tốc độ dòng chảy."
    },
    {
        "id": "suds",
        "title": "Hệ thống thoát nước đô thị bền vững (SuDS)",
        "selector": "#card-suds",
        "en": "Sustainable Drainage Systems (SuDS). As illustrated in Figure 1.40, SuDS replicate natural infiltration in urban settings using permeable paving, green vegetative roofs, swales, retention ponds, and underground attenuation tanks to mitigate runoff.",
        "vi": "Hệ thống thoát nước đô thị bền vững. Như được minh họa ở hình một chấm bốn mươi, hệ thống này tái tạo cơ chế thấm lọc tự nhiên trong đô thị nhờ vỉa hè thấm nước, mái nhà phủ thảm thực vật, mương dẫn nước sinh thái và các hồ điều hòa tạm thời."
    },
    {
        "id": "key_terms",
        "title": "Tổng kết Thuật ngữ cốt lõi (Key Terms)",
        "selector": "#sec-key-terms",
        "en": "Key Vocabulary Summary. Essential terminology includes alluvium, floodplains, hydroelectric power, channelisation, and levées. Mastering these technical definitions is essential for Cambridge examination precision.",
        "vi": "Tổng kết Từ vựng trọng tâm. Các thuật ngữ cốt lõi bao gồm phù sa, đồng bằng ngập lũ, thủy điện, nắn chỉnh luồng lạch và đê tự nhiên. Nắm vững các khái niệm chuẩn xác này là chìa khóa để đạt điểm tối đa trong kỳ thi quốc tế."
    },
    {
        "id": "exam_focus",
        "title": "Trọng tâm bài thi IGCSE Geography",
        "selector": "#card-exam-focus",
        "en": "Examination Strategy Focus. Be prepared to contrast physical and human causes of floods, explain the operational mechanisms of SuDS, and evaluate the trade-offs between hard and soft engineering with named case study examples.",
        "vi": "Trọng tâm ôn luyện thi cử. Hãy sẵn sàng phân tích so sánh giữa nguyên nhân tự nhiên và nhân tạo gây ngập lụt, giải thích rõ cơ chế vận hành của hệ thống thoát nước bền vững, đồng thời đánh giá ưu nhược điểm của công trình cứng và mềm qua các ví dụ thực tiễn."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "svg_overview": {"start": 1, "end": 10},
    "sec_opportunities": {"start": 11, "end": 18},
    "sec_floods": {"start": 19, "end": 22},
    "sec_management": {"start": 23, "end": 26},
    "key_terms": {"start": 27, "end": 28}
}

def get_duration(file_path):
    cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return round(float(res.stdout.strip()), 2)

async def tts_save_retry(text, voice, out_path, max_retries=6):
    for attempt in range(1, max_retries + 1):
        try:
            comm = edge_tts.Communicate(text, voice, pitch="+0Hz", rate="+0%")
            await comm.save(out_path)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                return
        except Exception as e:
            if attempt == max_retries:
                raise Exception(f"Failed to generate TTS after {max_retries} attempts: {e}")
            await asyncio.sleep(1.5 * attempt)

async def generate_segment_audio(seg, index, total):
    seg_id = seg["id"]
    print(f"[{index + 1}/{total}] 1.3 Audio: {seg['title']} ({seg_id})...")

    en_path = os.path.join(SCRATCH_DIR, f"{seg_id}_en.mp3")
    vi_path = os.path.join(SCRATCH_DIR, f"{seg_id}_vi.mp3")
    combined_path = os.path.join(AUDIO_OUTPUT_DIR, f"{seg_id}.mp3")

    await tts_save_retry(seg["en"], EN_VOICE, en_path)
    await tts_save_retry(seg["vi"], VI_VOICE, vi_path)

    filter_expr = "[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]"
    cmd = [
        'ffmpeg', '-y',
        '-i', en_path,
        '-f', 'lavfi', '-t', '0.4', '-i', 'anullsrc=r=24000:cl=mono',
        '-i', vi_path,
        '-filter_complex', filter_expr,
        '-map', '[out]',
        '-b:a', '128k',
        combined_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    dur = get_duration(combined_path)
    seg["duration"] = dur
    seg["audioUrl"] = f"/audio/lectures/geography/1_3/{seg_id}.mp3"
    print(f"   => Xong: {seg_id}.mp3 ({dur}s)")

async def main():
    total = len(SEGMENTS)
    print(f"🚀 BẮT ĐẦU TẠO {total} PHÂN ĐOẠN AUDIO CHO BÀI 1.3:")
    
    current_start = 0.0
    for i, seg in enumerate(SEGMENTS):
        await generate_segment_audio(seg, i, total)
        seg["startTime"] = round(current_start, 2)
        current_start += seg["duration"]
        seg["endTime"] = round(current_start, 2)

    total_duration = round(current_start, 2)

    manifest_data = {
        "lectureId": LECTURE_ID,
        "courseTitle": "IGCSE-Geography-0460",
        "lectureTitle": "1.3 Rivers present opportunities and hazards for people",
        "totalDuration": total_duration,
        "majorSections": MAJOR_SECTIONS,
        "segments": SEGMENTS
    }

    manifest_path = os.path.join(AUDIO_OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    print(f"🎉 Đã ghi manifest: {manifest_path} (Tổng: {total_duration}s)")

    # Update Supabase HTML for 1.3
    with open('.env', 'r', encoding='utf-8') as f:
        env = f.read()
    url = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
    key = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
    sb = create_client(url, key)

    with open("scratch/lectures/1_3_p1_interactive.html", "r", encoding="utf-8") as f:
        updated_html = f.read()

    res = sb.table('lecture_pages').update({'content_html': updated_html}).eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    print("✅ Đã cập nhật HTML trang 1 Bài 1.3 lên Supabase!")

if __name__ == '__main__':
    asyncio.run(main())
