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

LECTURE_ID = "bade96ee-497d-4d75-8d82-c691133eb9d6"
AUDIO_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'geography', '1_2')
SCRATCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'scratch', 'audio_temp_1_2')
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

EN_VOICE = 'en-GB-RyanNeural'       # Authentic Male British English
VI_VOICE = 'vi-VN-HoaiMyNeural'     # Authentic Northern Vietnamese (Hanoi accent, 100% natural, pristine)

# TUYỆT ĐỐI 100% TIẾNG VIỆT THUẦN TÚY TRONG PHẦN 'vi':
# Không kèm bất kỳ từ tiếng Anh nào.
SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.2",
        "selector": "#sec-header",
        "en": "Lesson 1.2: The main landforms associated with river processes. In this lesson, we explore how rivers shape the landscape from source to mouth.",
        "vi": "Bài một chấm hai: Các dạng địa hình chính gắn liền với các quá trình sông ngòi. Trong bài học này, chúng ta sẽ tìm hiểu cách dòng sông điêu khắc và định hình cảnh quan từ thượng lưu ra đến cửa sông."
    },
    {
        "id": "sec_long_profile",
        "title": "Trắc diện dọc sông (Long Profile)",
        "selector": "#sec-long-profile",
        "en": "Interactive Long Profile. A river's journey is divided into three distinct stages: the upper course, the middle course, and the lower course. Each stage possesses characteristic energy levels and distinctive landforms.",
        "vi": "Trắc diện dọc sông. Hành trình của một dòng sông được chia thành ba giai đoạn rõ rệt: thượng lưu, trung lưu và hạ lưu. Mỗi giai đoạn mang mức năng lượng riêng biệt và tạo nên những dạng địa hình đặc trưng."
    },
    {
        "id": "lp_vshaped",
        "title": "V-shaped Valley (Thung lũng chữ V)",
        "selector": "#lp-vshaped",
        "en": "V-shaped Valley. Formed in the upper course where vertical erosion dominates. The river cuts deeply downward into bedrock, while gravity and weathering cause the valley sides to collapse into a steep V-shape.",
        "vi": "Thung lũng hình chữ V. Hình thành ở vùng thượng lưu nơi xói mòn thẳng đứng chiếm ưu thế. Dòng sông đào sâu xuống tầng đá đáy, trong khi trọng lực và phong hóa làm sạt lở hai bên sườn núi tạo thành hình chữ V dốc đứng."
    },
    {
        "id": "lp_spurs",
        "title": "Interlocking Spurs (Mũi đất lồng nhau)",
        "selector": "#lp-spurs",
        "en": "Interlocking Spurs. Projections of resistant rock jutting out from alternate sides of the valley. Lacking energy to cut through hard rock, the young river winds around them, creating an interlocking jigsaw appearance.",
        "vi": "Các mũi đất lồng vào nhau. Là các dải đá cứng nhô ra so le từ hai bên sườn thung lũng. Do chưa đủ động năng để xuyên phá đá cứng, dòng sông trẻ phải uốn lượn vòng qua chúng, tạo nên hình ảnh các mũi đất khớp vào nhau như mảnh ghép."
    },
    {
        "id": "lp_pothole",
        "title": "Pothole (Ổ xoáy đáy sông)",
        "selector": "#lp-pothole",
        "en": "Pothole. A circular cylindrical hole ground into the bedrock of the riverbed. Pebbles become trapped in small depressions and are swirled around by turbulent eddies, drilling into the rock by abrasion.",
        "vi": "Ổ xoáy đáy sông. Là những chiếc hố hình trụ tròn xoáy sâu vào đá đáy lòng sông. Các viên sỏi bị mắc kẹt trong các chỗ trũng nhỏ và bị dòng nước xoáy tròn mài mòn đá đáy theo cơ chế khoan đá."
    },
    {
        "id": "lp_waterfall",
        "title": "Waterfall & Gorge (Thác nước & Hẻm vực)",
        "selector": "#lp-waterfall",
        "en": "Waterfall and Gorge. A waterfall forms where a hard rock layer overlies softer rock. The soft rock is undercut, leaving an unsupported overhang that collapses into the plunge pool. Upstream retreat carves a steep-sided gorge.",
        "vi": "Thác nước và Hẻm vực. Thác nước hình thành nơi lớp đá cứng nằm đè lên tầng đá mềm hơn. Tầng đá mềm bị khoét rỗng bên dưới, làm mỏm đá cứng nhô ra bị sập xuống hồ xoáy chân thác. Quá trình thác lùi dần về thượng lưu tạo ra một hẻm vực sâu với vách dựng đứng."
    },
    {
        "id": "lp_meander",
        "title": "Meander (Khúc sông uốn khúc)",
        "selector": "#lp-meander",
        "en": "Meander. A pronounced sweeping curve in the river channel. Fast flowing water on the outside bend erodes a steep river cliff, while sluggish flow on the inside bend deposits sediment to build a gentle slip-off slope.",
        "vi": "Khúc sông uốn khúc. Là đoạn uốn cong mềm mại của dòng sông ở trung và hạ lưu. Nước chảy xiết ở bờ lõm bên ngoài gây xói lở tạo vách sông dốc đứng, trong khi nước chảy chậm ở bờ lồi bên trong bồi tụ trầm tích tạo bãi bồi thoai thoải."
    },
    {
        "id": "lp_oxbow",
        "title": "Oxbow Lake (Hồ móng ngựa)",
        "selector": "#lp-oxbow",
        "en": "Oxbow Lake. A crescent-shaped lake formed when the narrow neck of a meander loop is breached during a major flood. Deposition cuts off the old loop from the main river channel, leaving an isolated water body.",
        "vi": "Hồ móng ngựa. Là hồ nước hình bán nguyệt hình thành khi eo đất hẹp của khúc uốn bị dòng nước lũ chọc thủng. Quá trình bồi tụ phù sa sau đó bịt kín hai đầu khúc uốn cũ, tách biệt nó thành một hồ nước độc lập."
    },
    {
        "id": "lp_floodplain",
        "title": "Floodplain & Levée (Đồng bằng ngập lũ & Đê tự nhiên)",
        "selector": "#lp-floodplain",
        "en": "Floodplain and Levée. The floodplain is a broad, flat valley floor blanketed in rich alluvial silt from recurrent floods. Coarser sediments drop first beside the channel margins, constructing raised natural embankments called levées.",
        "vi": "Đồng bằng ngập lũ và đê tự nhiên. Đồng bằng ngập lũ là dải đất bằng phẳng rộng lớn được bồi đắp bởi các lớp phù sa màu mỡ qua các mùa lũ. Các hạt phù sa thô to lắng xuống trước dọc mép sông, dần dần đắp nên các bờ gờ cao tự nhiên gọi là đê tự nhiên."
    },
    {
        "id": "lp_braided",
        "title": "Braided Channel (Lòng sông phân nhánh)",
        "selector": "#lp-braided",
        "en": "Braided Channel. A river network splitting into multiple interwoven channels separated by transient gravel bars. This develops when the river is overloaded with excessive sediment that exceeds its transport capacity.",
        "vi": "Lòng sông phân nhánh bện bện. Một mạng lưới lòng sông bị chia tách thành nhiều luồng lạch đan xen nhau bởi các cồn cát sỏi tạm thời. Hiện tượng này xuất hiện khi con sông phải gánh tải lượng trầm tích khổng lồ vượt quá khả năng vận chuyển."
    },
    {
        "id": "lp_delta",
        "title": "Delta (Đồng bằng châu thổ)",
        "selector": "#lp-delta",
        "en": "Delta. A depositional landform built where a river discharges into a standing body of water, such as a sea or lake. River velocity falls to zero, depositing sediment and branching into a fan of distributary channels.",
        "vi": "Đồng bằng châu thổ cửa sông. Dạng địa hình bồi tụ hình thành nơi dòng sông đổ vào vùng nước tĩnh như biển hoặc hồ. Vận tốc dòng chảy giảm về không, khiến toàn bộ phù sa lắng đọng và sông chia thành các nhánh tỏa ra như một chiếc quạt."
    },
    {
        "id": "sec_upland",
        "title": "Địa hình vùng thượng lưu (Upper Course)",
        "selector": "#sec-upland",
        "en": "Section 1: Upland Landforms of the Upper Course. High altitude, steep relief, and powerful downward gravitational energy characterise this zone, sculpting dramatic rocky landscapes.",
        "vi": "Phần một: Các dạng địa hình vùng thượng lưu. Địa hình vùng núi cao, độ dốc lớn cùng động năng trọng lực hướng xuống mãnh liệt là đặc trưng của khu vực này, tạo nên những cảnh quan đá kỳ vĩ."
    },
    {
        "id": "upland_overview",
        "title": "Quá trình chủ đạo vùng thượng lưu",
        "selector": "#card-upland-overview",
        "en": "Dominant Upper Course Processes. Vertical erosion dominates as the river cuts downward into bedrock. The channel is narrow, steep, and rocky, transporting angular boulders by traction and saltation.",
        "vi": "Các quá trình chủ đạo vùng thượng lưu. Xói mòn thẳng đứng chiếm ưu thế tuyệt đối khi dòng sông đào sâu vào tầng đá đáy. Lòng sông hẹp, dốc và nhiều đá gồ ghề, vận chuyển các tảng đá góc cạnh bằng lực kéo lăn và nhảy cóc."
    },
    {
        "id": "vshaped_spurs",
        "title": "Chi tiết: Thung lũng chữ V & Mũi đất lồng",
        "selector": "#card-vshaped-spurs",
        "en": "V-shaped Valleys and Interlocking Spurs in detail. Vertical hydraulic action and abrasion deepen the river channel. Weathering weakens the valley sides until scree slides down into the water, widening the valley into a V shape. To conserve energy around resistant rock ridges, the river snakes through interlocking spurs.",
        "vi": "Chi tiết Thung lũng chữ V và các mũi đất lồng nhau. Thủy lực và mài mòn khoét sâu lòng sông. Quá trình phong hóa làm sụt lở hai sườn thung lũng, trút đất đá xuống lòng suối và mở rộng thành hình chữ V. Để tiết kiệm năng lượng khi gặp các dải đá cứng, dòng sông uốn lượn mềm mại quanh các mũi đá đan xen."
    },
    {
        "id": "potholes",
        "title": "Chi tiết: Ổ xoáy đáy sông (Potholes)",
        "selector": "#card-potholes",
        "en": "Potholes in detail. High turbulence drives pebbles in relentless circular swirling motions within bedrock depressions. This abrasive drilling action carves deep, polished vertical cylinders that can reach several metres across.",
        "vi": "Chi tiết Ổ xoáy đáy sông. Dòng nước xoáy cuộn mạnh mẽ làm quay tròn các viên sỏi cuội trong các vết lõm trên bề mặt đá. Lực ma sát chà xát này khoan sâu vào đá đáy, tạo ra các hố tròn nhẵn thín có thể sâu tới vài mét."
    },
    {
        "id": "waterfalls_gorges",
        "title": "Chi tiết: Thác nước & Hẻm vực (Waterfalls & Gorges)",
        "selector": "#card-waterfalls-gorges",
        "en": "Waterfalls and Gorges in detail. Differential erosion between resistant caprock and underlying weaker rock creates an undercut notch. Hydraulic action carves a deep plunge pool. When the unsupported overhang collapses, the waterfall retreats upstream, excavating a steep-walled gorge of recession.",
        "vi": "Chi tiết Thác nước và Hẻm vực. Sự xói mòn chênh lệch giữa lớp đá cứng phía trên và lớp đá mềm bên dưới tạo nên một hốc khoét sâu. Thủy lực và sỏi đá xoáy tạo hồ sâu dưới chân thác. Khi mỏm đá phía trên sụp đổ, thác nước lùi dần về thượng lưu, để lại một hẻm vực sâu hun hút với hai vách đá dựng đứng."
    },
    {
        "id": "sec_lowland",
        "title": "Địa hình trung & hạ lưu (Middle & Lower Course)",
        "selector": "#sec-lowland",
        "en": "Section 2: Lowland Landforms of the Middle and Lower Course. Gradient decreases, velocity evens out, and the river broadens through lateral erosion and extensive deposition.",
        "vi": "Phần hai: Các dạng địa hình vùng trung lưu và hạ lưu. Độ dốc giảm dần, dòng nước mở rộng sang hai bên nhờ xói mòn ngang và sự bồi tụ trầm tích diễn ra trên diện rộng."
    },
    {
        "id": "lowland_overview",
        "title": "Quá trình chủ đạo vùng hạ lưu",
        "selector": "#card-lowland-overview",
        "en": "Dominant Lowland Processes. Lateral erosion widens the valley floor in the middle course, while deposition dominates in the lower course as water energy drops. Fertile alluvium blankets the vast floodplains.",
        "vi": "Các quá trình chủ đạo vùng hạ lưu. Xói mòn ngang mở rộng đáy thung lũng ở trung lưu, trong khi quá trình bồi tụ chiếm ưu thế ở hạ lưu do năng lượng dòng chảy giảm. Lớp phù sa màu mỡ phủ khắp các đồng bằng ngập lũ bao la."
    },
    {
        "id": "meanders",
        "title": "Chi tiết: Khúc uốn Meander & Bờ xói - Bờ bồi",
        "selector": "#card-meanders",
        "en": "Meanders in detail. Helical flow pushes maximum velocity toward the outer bank, generating hydraulic undercutting that forms a river cliff. On the inner bank, friction decelerates water, causing sand and gravel deposition to form a slip-off slope or point bar.",
        "vi": "Chi tiết Khúc uốn và bờ xói bờ bồi. Dòng chảy xoắn ốc đẩy vận tốc cực đại sang bờ lõm bên ngoài, tạo lực thủy lực khoét chân bờ tạo vách đứng. Tại bờ lồi bên trong, ma sát làm chậm dòng nước, khiến cát sỏi lắng xuống tạo nên bãi bồi thoai thoải."
    },
    {
        "id": "oxbow_lakes",
        "title": "Chi tiết: Hồ móng ngựa (Oxbow Lakes)",
        "selector": "#card-oxbow-lakes",
        "en": "Oxbow Lakes in detail. Continued erosion of outer banks narrows the meander neck. During flood discharge, the river cuts directly across the neck along the path of steepest gradient. Sediment seals the abandoned loop, which gradually transforms into a marshy meander scar.",
        "vi": "Chi tiết Sự hình thành Hồ móng ngựa. Sự xói mòn liên tục ở hai bờ ngoài làm eo đất của khúc uốn ngày càng thon hẹp. Khi mùa lũ đến, dòng nước tràn qua cắt đứt eo đất theo con đường ngắn nhất. Trầm tích bồi lấp hai đầu khúc uốn cũ, biến nó thành hồ móng ngựa và dần thoái hóa thành đầm lầy."
    },
    {
        "id": "floodplains_levees",
        "title": "Chi tiết: Đồng bằng ngập lũ & Đê tự nhiên",
        "selector": "#card-floodplains-levees",
        "en": "Floodplains and Levées in detail. When a river overspills its channel, water spreading across the floodplain suddenly loses velocity and carrying capacity. The heaviest, coarsest load drops immediately along the channel banks to build raised levées, while fine silt settles across the distant plains.",
        "vi": "Chi tiết Đồng bằng ngập lũ và Đê tự nhiên. Khi sông tràn bờ trong mùa lũ, nước tỏa rộng ra xung quanh bị giảm vận tốc đột ngột và mất sức mang tải. Các hạt bùn cát thô to nhất lập tức rơi xuống sát hai bên bờ xây nên gờ đê tự nhiên, trong khi lớp phù sa mịn màng phủ rộng khắp đồng bằng châu thổ."
    },
    {
        "id": "braided_channels",
        "title": "Chi tiết: Lòng sông phân nhánh (Braided Channels)",
        "selector": "#card-braided-channels",
        "en": "Braided Channels in detail. When sediment supply exceeds channel carrying power, such as downstream of melting glaciers or in seasonal flood regimes, mid-channel bars form, splitting the flow into an interwoven maze of channels.",
        "vi": "Chi tiết Lòng sông phân nhánh. Khi lượng trầm tích cung cấp vượt quá sức chuyên chở của lòng sông, ví dụ như ở hạ lưu vùng băng tan hay mùa lũ thất thường, các cồn cát sỏi nổi lên giữa dòng chia cắt dòng sông thành mạng lưới chằng chịt các luồng lạch."
    },
    {
        "id": "deltas",
        "title": "Chi tiết: Đồng bằng châu thổ (Deltas)",
        "selector": "#card-deltas",
        "en": "Deltas in detail. As the river meets standing sea water, forward velocity drops to zero. Sediment flocculates and settles, choking the mouth and forcing the main channel to split into fan-like distributaries. Exemplified by the Rhône Delta in France.",
        "vi": "Chi tiết Đồng bằng châu thổ. Khi dòng sông chạm vào mặt biển tĩnh lặng, vận tốc tiến về phía trước giảm về không. Phù sa kết tủa và bồi lắng làm tắc nghẽn cửa sông, buộc dòng chính phải tẽ ra thành nhiều nhánh sông con hình nan quạt, tiêu biểu là đồng bằng châu thổ sông Rôn ở Pháp."
    },
    {
        "id": "summary_table",
        "title": "Bảng tổng kết: Các dạng địa hình sông ngòi",
        "selector": "#sec-summary-table",
        "en": "Summary Table: River Landforms. Upper course features such as V-shaped valleys, potholes, and waterfalls arise from vertical erosion. Middle course meanders and oxbow lakes combine lateral erosion and deposition. Lower course floodplains, levées, and deltas are shaped predominantly by deposition.",
        "vi": "Bảng tổng kết Các dạng địa hình sông ngòi. Vùng thượng lưu gồm thung lũng chữ V, ổ xoáy và thác nước hình thành từ xói mòn thẳng đứng. Vùng trung lưu gồm khúc uốn và hồ móng ngựa là sự kết hợp giữa xói mòn ngang và bồi tụ. Vùng hạ lưu gồm đồng bằng ngập lũ, đê tự nhiên và châu thổ được kiến tạo chủ yếu bởi quá trình bồi tụ trầm tích."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_long_profile": {"start": 1, "end": 10},
    "sec_upland": {"start": 11, "end": 15},
    "sec_lowland": {"start": 16, "end": 22},
    "summary_table": {"start": 23, "end": 23}
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
    print(f"[{index + 1}/{total}] 1.2 Audio: {seg['title']} ({seg_id})...")

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
    seg["audioUrl"] = f"/audio/lectures/geography/1_2/{seg_id}.mp3"
    print(f"   => Xong: {seg_id}.mp3 ({dur}s)")

async def main():
    total = len(SEGMENTS)
    print(f"🚀 BẮT ĐẦU TẠO {total} PHÂN ĐOẠN AUDIO CHO BÀI 1.2:")
    
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
        "lectureTitle": "1.2 The main landforms associated with these processes",
        "totalDuration": total_duration,
        "majorSections": MAJOR_SECTIONS,
        "segments": SEGMENTS
    }

    manifest_path = os.path.join(AUDIO_OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    print(f"🎉 Đã ghi manifest: {manifest_path} (Tổng: {total_duration}s)")

    # Update Supabase HTML for 1.2
    with open('.env', 'r', encoding='utf-8') as f:
        env = f.read()
    url = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
    key = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
    sb = create_client(url, key)

    with open("scratch/lectures/1_2_p1_interactive.html", "r", encoding="utf-8") as f:
        updated_html = f.read()

    res = sb.table('lecture_pages').update({'content_html': updated_html}).eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    print("✅ Đã cập nhật HTML trang 1 Bài 1.2 lên Supabase!")

if __name__ == '__main__':
    asyncio.run(main())
