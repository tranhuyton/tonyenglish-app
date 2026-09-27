import asyncio
import edge_tts
import subprocess
import os
import json
import sys

# Ensure UTF-8 output on Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

AUDIO_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'geography', '1_1')
SCRATCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'scratch', 'audio_temp')
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

EN_VOICE = 'en-GB-RyanNeural'       # Male British English
VI_VOICE = 'vi-VN-HoaiMyNeural'     # Female Northern Vietnamese (Hanoi accent)

SEGMENTS = [
    # --- PHẦN 1: TỔNG QUAN & LƯU VỰC SÔNG (8 MỤC) ---
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.1",
        "selector": "#sec-header",
        "en": "Lesson 1.1: The main hydrological characteristics and processes that operate in rivers and drainage basins.",
        "vi": "Bài 1.1: Các đặc điểm thủy văn và quá trình vận hành chính trong các con sông và lưu vực sông."
    },
    {
        "id": "drainage_basin",
        "title": "1. Khái niệm Lưu vực sông (Drainage Basin)",
        "selector": "#sec-drainage-basin",
        "en": "Part 1: Rivers and Drainage Basins. A drainage basin is the area of land drained by a river and all its tributaries. It is an open system with inputs such as precipitation, and outputs such as evaporation, transpiration, and river discharge to the sea. The boundary of a drainage basin is called the watershed.",
        "vi": "Phần 1: Các con sông và Lưu vực sông. Lưu vực sông là toàn bộ diện tích đất được thoát nước bởi một con sông chính và tất cả các nhánh sông phụ lưu của nó. Đây là một hệ thống mở tuần hoàn, có đầu vào là lượng mưa và đầu ra gồm bốc thoát hơi nước cùng dòng chảy đổ ra biển. Ranh giới phân định lưu vực sông được gọi là đường phân thủy."
    },
    {
        "id": "source",
        "title": "Source - Nguồn sông",
        "selector": "#term-source",
        "en": "Source. The starting point where a river begins, usually situated on high ground, such as an upland mountain spring or peat bog.",
        "vi": "Nguồn sông. Nơi khởi nguồn của một con sông, thường nằm ở các vùng núi cao, đầm lầy hoặc mạch nước ngầm lộ thiên."
    },
    {
        "id": "mouth",
        "title": "Mouth - Cửa sông",
        "selector": "#term-mouth",
        "en": "Mouth. The point where a river concludes its journey, discharging into the sea, a lake, or joining another larger river.",
        "vi": "Cửa sông. Điểm kết thúc của dòng sông, nơi dòng nước đổ vào biển, đại dương, hồ nước hoặc nhập vào một dòng sông lớn hơn."
    },
    {
        "id": "tributary",
        "title": "Tributary - Phụ lưu / Nhánh sông",
        "selector": "#term-tributary",
        "en": "Tributary. A smaller stream or tributary river that joins and flows into the larger main river channel.",
        "vi": "Phụ lưu hay nhánh sông. Là một dòng suối hoặc nhánh sông nhỏ hơn đổ vào dòng sông chính."
    },
    {
        "id": "confluence",
        "title": "Confluence - Hợp lưu / Ngã ba sông",
        "selector": "#term-confluence",
        "en": "Confluence. The exact geographical point where two rivers or streams meet and merge into a single channel.",
        "vi": "Hợp lưu hay ngã ba sông. Là điểm giao nhau nơi hai dòng sông hoặc dòng suối hội tụ thành một dòng duy nhất."
    },
    {
        "id": "watershed",
        "title": "Watershed - Đường phân thủy",
        "selector": "#term-watershed",
        "en": "Watershed. The ridge of high land or topographical boundary separating one drainage basin from an adjacent basin.",
        "vi": "Đường phân thủy. Là sống núi hoặc ranh giới địa hình trên cao phân chia giữa hai lưu vực sông kế cận nhau."
    },
    {
        "id": "floodplain",
        "title": "Flood plain - Đồng bằng ngập lũ",
        "selector": "#term-floodplain",
        "en": "Flood plain. The relatively flat area of land bordering the river channel, which is naturally inundated when river discharge overflows its banks.",
        "vi": "Đồng bằng ngập lũ. Vùng đất tương đối bằng phẳng nằm dọc hai bên bờ sông, thường xuyên bị ngập nước khi lưu lượng sông tràn bờ."
    },

    # --- PHẦN 2: MÔ HÌNH BRADSHAW (3 MỤC CHI TIẾT) ---
    {
        "id": "bradshaw_model",
        "title": "2. Mô hình Bradshaw (Tổng quan & Đồ thị)",
        "selector": "#sec-bradshaw-model",
        "en": "Part 2: The Bradshaw Model. The Bradshaw Model illustrates how river characteristics change systematically from source to mouth as discharge increases downstream. It explains why distinct fluvial landforms develop along the river profile.",
        "vi": "Phần 2: Mô hình Bradshaw. Mô hình Bradshaw mô tả quy luật biến đổi có hệ thống của các đặc tính sông từ thượng lưu ra cửa sông khi lưu lượng nước tăng dần. Mô hình này giúp giải thích sự hình thành của các dạng địa hình sông ngòi từ thượng lưu, trung lưu đến hạ lưu."
    },
    {
        "id": "bradshaw_increase",
        "title": "Bradshaw Model: Các yếu tố TĂNG xuôi dòng",
        "selector": "#card-bradshaw-increase",
        "en": "River characteristics that increase downstream: First, discharge increases because more tributaries join the main river. Second, channel width and depth increase due to lateral erosion and greater water volume. Third, average velocity increases because the channel is deeper and smoother, reducing friction. Finally, load volume increases from ongoing sediment input.",
        "vi": "Các đặc tính TĂNG dần xuôi dòng về hạ lưu: Thứ nhất, lưu lượng nước tăng mạnh do nhiều phụ lưu sáp nhập vào dòng chính. Thứ hai, bề rộng và độ sâu lòng sông mở rộng do xói mòn ngang và khối lượng nước lớn. Thứ ba, vận tốc trung bình thực tế lại tăng lên vì lòng sông sâu và nhẵn hơn, làm giảm ma sát. Cuối cùng, tổng khối lượng trầm tích phù sa tăng lên do được bồi đắp liên tục."
    },
    {
        "id": "bradshaw_decrease",
        "title": "Bradshaw Model: Các yếu tố GIẢM xuôi dòng",
        "selector": "#card-bradshaw-decrease",
        "en": "River characteristics that decrease downstream: First, gradient and slope decrease as the river leaves steep mountain valleys and enters flat coastal plains. Second, particle size of bedload decreases because attrition rounds and smashes stones into finer sand. Third, channel bed roughness decreases as large boulders are replaced by smooth silt. Finally, valley sides become much gentler.",
        "vi": "Các đặc tính GIẢM dần xuôi dòng về hạ lưu: Thứ nhất, độ dốc dòng chảy giảm dần khi sông rời vùng núi hiểm trở về đồng bằng ven biển. Thứ hai, kích thước các hạt sỏi đá giảm mạnh do quá trình va đập mài mòn làm vỡ vụn thành cát và bùn mịn. Thứ ba, độ gồ ghề của đáy sông giảm hẳn khi các tảng đá lớn được thay thế bằng lớp phù sa nhẵn mịn. Cuối cùng, hai bên sườn thung lũng thoai thoải dần và mở rộng ra."
    },

    # --- PHẦN 3: CHU TRÌNH NƯỚC & BẢN ĐỒ TƯƠNG TÁC (7 MỤC CHI TIẾT) ---
    {
        "id": "water_cycle",
        "title": "3. Chu trình nước trong lưu vực (Tổng quan)",
        "selector": "#sec-water-cycle",
        "en": "Part 3: The Drainage Basin Water Cycle. The drainage basin operates as an open hydrological system. Water cycles continuously between the atmosphere, the surface, the soil, and underlying rock strata through inputs, stores, transfers, and outputs.",
        "vi": "Phần 3: Chu trình nước trong lưu vực sông. Lưu vực sông hoạt động như một hệ thống thủy văn mở. Nước luân chuyển liên tục giữa khí quyển, bề mặt đất, tầng đất và tầng đá ngầm thông qua đầu vào, lưu trữ, dòng dịch chuyển và đầu ra."
    },
    {
        "id": "water_precip",
        "title": "🌧️ Precipitation (Lượng mưa đầu vào)",
        "selector": "#water-precip",
        "en": "Precipitation. The primary input into the drainage basin system, including rain, snow, sleet, and hail. The intensity and duration of precipitation dictate whether water soaks into the soil or rapidly becomes surface runoff.",
        "vi": "Precipitation - Lượng mưa đầu vào. Đây là nguồn đầu vào chính cung cấp nước cho toàn bộ lưu vực sông, bao gồm mưa, tuyết, mưa đá và sương. Cường độ và thời gian kéo dài của đợt mưa sẽ quyết định nước thấm vào lòng đất hay nhanh chóng chảy tràn trên mặt đất."
    },
    {
        "id": "water_interception",
        "title": "🌿 Interception (Sự giữ nước tán cây)",
        "selector": "#water-interception",
        "en": "Interception. Precipitation caught by vegetation, including leaves and branches, before reaching the soil. Some evaporates directly back into the atmosphere. Forests can intercept up to thirty-five percent of rainfall, delaying peak discharge and reducing flood risk.",
        "vi": "Interception - Sự giữ nước của tán cây. Lượng mưa bị cành lá thảm thực vật giữ lại trước khi kịp rơi xuống đất. Một phần nước sẽ bốc hơi trực tiếp trở lại không khí. Rừng cây có thể giữ lại tới 35% lượng mưa, giúp làm chậm dòng lũ và giảm nguy cơ ngập lụt."
    },
    {
        "id": "water_runoff",
        "title": "💧 Surface Runoff (Dòng chảy tràn mặt đất)",
        "selector": "#water-runoff",
        "en": "Surface Runoff, or Overland Flow. Water that travels across the land surface when precipitation rate exceeds soil infiltration capacity, or when the ground is fully saturated. This is the fastest route to the river channel, causing rapid rises in discharge and flash flooding.",
        "vi": "Surface Runoff - Dòng chảy tràn mặt đất. Dòng nước chảy trên bề mặt đất khi lượng mưa vượt quá khả năng ngấm của đất, hoặc khi đất đã bão hòa nước. Đây là con đường nhanh nhất đưa nước vào lòng sông, thường gây ra các cơn lũ quét nguy hiểm ở khu vực đô thị và đất dốc."
    },
    {
        "id": "water_infiltration",
        "title": "⬇️ Infiltration & Throughflow (Thấm & Dòng trong đất)",
        "selector": "#water-infiltration",
        "en": "Infiltration and Throughflow. Infiltration is the downward soaking of water into the upper soil from the surface. Throughflow is the lateral downslope movement of water through soil toward the river. Percolation occurs when water seeps deeper into bedrock.",
        "vi": "Infiltration - Quá trình thấm và dòng chảy trong đất. Thấm là quá trình nước từ mặt đất ngấm xuống lớp đất bên trên. Dòng chảy trong đất là nước di chuyển ngang theo sườn dốc qua các tầng đất về phía con sông. Còn ngấm sâu là hiện tượng nước tiếp tục lọc xuống sâu hơn vào tầng đá gốc bên dưới."
    },
    {
        "id": "water_groundwater",
        "title": "🪨 Groundwater Flow (Nước ngầm & Dòng chảy đáy)",
        "selector": "#water-groundwater",
        "en": "Groundwater Flow and Storage. Groundwater is water stored in porous rock aquifers beneath the water table. It migrates very slowly as groundwater flow or baseflow toward the river, sustaining steady river flow even during dry weather.",
        "vi": "Groundwater - Nước ngầm và Lưu trữ ngầm. Nước ngầm là lượng nước tích tụ trong các tầng đá xốp bên dưới mực nước ngầm. Nước ngầm di chuyển rất chậm tạo thành dòng chảy đáy, giúp duy trì dòng chảy ổn định cho các con sông ngay cả trong mùa khô hạn kéo dài."
    },
    {
        "id": "water_et",
        "title": "☀️ Evapotranspiration (Thoát - bốc hơi nước)",
        "selector": "#water-et",
        "en": "Evapotranspiration. The principal output returning water to the atmosphere. It combines surface evaporation from open water and wet soil, with transpiration, where plants release water vapor through microscopic leaf pores during photosynthesis.",
        "vi": "Evapotranspiration - Thoát - bốc hơi nước. Đầu ra chủ yếu đưa hơi nước từ lưu vực sông trở lại bầu khí quyển. Nó là sự kết hợp giữa bốc hơi nước tự do từ bề mặt đất, mặt nước và thoát hơi nước qua khí khổng của lá cây khi quang hợp."
    },
    {
        "id": "water_basin_map",
        "title": "🗺️ Sơ đồ Lưu vực sông Tees (Figure 1.9)",
        "selector": "#card-water-map",
        "en": "Figure 1.9: The Drainage Basin System Map. In the River Tees basin, water enters the high upper course near Cross Fell at over eight hundred meters elevation, passes waterfalls and reservoirs in the middle course, and flows across the flat flood plain to Teesmouth into the North Sea.",
        "vi": "Hình 1.9: Bản đồ hệ thống Lưu vực sông Tees. Nước mưa rơi xuống vùng núi cao thượng lưu gần Cross Fell ở độ cao trên 800 mét, chảy qua các thác nước và hồ chứa ở trung lưu, sau đó uốn lượn qua đồng bằng ngập lũ hạ lưu trước khi đổ ra Biển Bắc tại cửa sông Tees."
    },

    # --- PHẦN 4: CÁC QUÁ TRÌNH SÔNG NGÒI (10 MỤC CHI TIẾT) ---
    {
        "id": "fluvial_processes",
        "title": "4. Các quá trình sông ngòi (Tổng quan)",
        "selector": "#sec-fluvial-processes",
        "en": "Part 4: Fluvial Processes. Rivers continuously shape and sculpt the natural landscape through three fundamental processes: erosion, transportation, and deposition.",
        "vi": "Phần 4: Các quá trình sông ngòi. Sông ngòi liên tục biến đổi cảnh quan tự nhiên thông qua ba quá trình nền tảng: xói mòn, vận chuyển và bồi tụ trầm tích."
    },
    {
        "id": "hydraulic_action",
        "title": "💥 Hydraulic Action (Tác động thủy lực)",
        "selector": "#card-hydraulic-action",
        "en": "Hydraulic Action. The mechanical force of turbulent flowing water on river bed and banks. Water is forced into rock joints and fissures, compressing trapped air. As water retreats, explosive air expansion shatters and fractures the rock face.",
        "vi": "Hydraulic Action - Tác động thủy lực. Là sức ép vật lý của dòng nước chảy xiết va đập vào đáy và bờ sông. Dòng nước nén các bọt khí vào các kẽ nứt đá với áp suất cao. Khi nước rút, bọt khí bung nở làm nứt vỡ và đánh bật các mảng đá, đặc biệt dữ dội trong mùa lũ."
    },
    {
        "id": "abrasion",
        "title": "💥 Corrasion / Abrasion (Mài mòn cơ học)",
        "selector": "#card-abrasion",
        "en": "Corrasion, or Abrasion. The sandpaper-like grinding action where the river uses transported sand, gravel, and boulders to scrape and scour bedrock along the bed and banks. This is the primary mechanism deepening the channel.",
        "vi": "Corrasion hay Abrasion - Quá trình mài mòn cơ học. Dòng sông sử dụng chính đất cát, sỏi đá đang mang theo làm công cụ để chà xát và mài mòn đáy và bờ sông giống như một tờ giấy ráp. Đây là quá trình cốt lõi giúp đào sâu lòng sông và mở rộng lòng máng."
    },
    {
        "id": "attrition",
        "title": "💥 Attrition (Va đập tự vỡ vụn)",
        "selector": "#card-attrition",
        "en": "Attrition. The ongoing collision of rock fragments and boulders carried by the current. As particles crash into each other, sharp angles break off, progressively grinding stones into smaller, rounder, and smoother pebbles and sand downstream.",
        "vi": "Attrition - Quá trình va đập tự vỡ vụn. Các tảng đá và mảnh sỏi vụn cuốn theo dòng nước liên tục va đập vào nhau. Quá trình này bẻ gãy các góc cạnh sắc nhọn, làm cho đá cuội ngày càng trở nên tròn trịa, nhẵn bóng và kích thước nhỏ dần khi xuôi dòng."
    },
    {
        "id": "solution_erosion",
        "title": "💥 Corrosion / Solution (Hòa tan hóa học)",
        "selector": "#card-solution-erosion",
        "en": "Corrosion, or Solution Erosion. The chemical dissolution of soluble rocks, such as limestone and chalk, caused by slightly acidic river water containing dissolved carbon dioxide. This process takes place invisibly and continuously.",
        "vi": "Corrosion hay Solution - Xói mòn hòa tan hóa học. Nước sông có tính axit nhẹ do hòa tan khí carbonic sẽ phản ứng và hòa tan các loại đá vôi và đá phấn có chứa canxi cacbonat. Quá trình hòa tan này diễn ra âm thầm, vô hình nhưng liên tục cuốn trôi khoáng chất."
    },
    {
        "id": "transport_traction",
        "title": "🚚 Traction (Lực kéo lăn tảng đá)",
        "selector": "#card-transport-traction",
        "en": "Traction. The bedload transport process where heavy boulders and large rocks are rolled, pushed, and slid along the river bed by the sheer force of high-velocity water.",
        "vi": "Traction - Vận chuyển bằng lực kéo lăn. Phương thức vận chuyển nơi các tảng đá lớn và nặng được dòng nước chảy xiết đẩy lăn trượt dọc theo đáy sông."
    },
    {
        "id": "transport_saltation",
        "title": "🚚 Saltation (Vận chuyển nhảy cóc)",
        "selector": "#card-transport-saltation",
        "en": "Saltation. The bouncing movement of medium-sized pebbles and coarse sand grains along the river bed in a sequence of short hops, lifted momentarily by water pulses before dropping under gravity.",
        "vi": "Saltation - Vận chuyển nhảy cóc. Chuyển động nhảy cóc của các viên sỏi vừa và hạt cát thô. Dòng nước xoáy nhấc hạt cát lên rồi trọng lực lại kéo rơi xuống, tạo thành chuỗi bước nhảy liên tục trên đáy sông."
    },
    {
        "id": "transport_suspension",
        "title": "🚚 Suspension (Vận chuyển lơ lửng)",
        "selector": "#card-transport-suspension",
        "en": "Suspension. Very fine particles of silt and clay carried aloft within the turbulent water column without touching the bottom, giving the river its characteristic opaque brownish hue.",
        "vi": "Suspension - Vận chuyển lơ lửng. Vận chuyển các hạt phù sa và hạt sét siêu mịn trôi lơ lửng trong dòng nước xiết mà không bị chìm xuống đáy. Chính phù sa lơ lửng này tạo nên màu nâu đục đặc trưng của các dòng sông."
    },
    {
        "id": "transport_solution",
        "title": "🚚 Solution (Vận chuyển hòa tan)",
        "selector": "#card-transport-solution",
        "en": "Solution. Soluble minerals, such as calcium carbonate, dissolved directly in the water and transported invisibly throughout the entire river journey all the way to the ocean.",
        "vi": "Solution - Vận chuyển hòa tan. Các khoáng chất hòa tan hoàn toàn trong nước dưới dạng ion vô hình, như muối canxi và magie. Lượng khoáng hòa tan này không bị lắng đọng mà sẽ theo dòng nước đi thẳng ra biển."
    },
    {
        "id": "deposition",
        "title": "⬇️ Deposition (Bồi tụ phù sa)",
        "selector": "#card-deposition",
        "en": "Deposition. The settling of transported sediment when river velocity, energy, and carrying capacity drop. Heavy boulders settle first, followed by gravel, sand, and fine silt. Characteristic of gentle gradients, meander slip-off slopes, lakes, and estuaries.",
        "vi": "Deposition - Quá trình bồi tụ phù sa. Diễn ra khi vận tốc và động năng của dòng sông suy giảm, không còn đủ sức mang tải trầm tích. Các tảng đá to nặng nhất sẽ lắng xuống trước, kế tiếp là sỏi, cát và cuối cùng là bùn sét mịn, tạo nên các bãi bồi ven sông và đồng bằng châu thổ."
    }
]

def get_duration(file_path):
    cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return round(float(res.stdout.strip()), 2)

async def tts_save_retry(text, voice, out_path, pitch="+0Hz", rate="+0%", max_retries=6):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return
    for attempt in range(1, max_retries + 1):
        try:
            comm = edge_tts.Communicate(text, voice, pitch=pitch, rate=rate)
            await comm.save(out_path)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                return
        except Exception as e:
            if attempt == max_retries:
                raise Exception(f"Failed to generate TTS after {max_retries} attempts: {e}")
            await asyncio.sleep(1.5 * attempt)

async def generate_segment_audio(seg, index, total):
    seg_id = seg["id"]
    print(f"[{index + 1}/{total}] Đang xử lý: {seg['title']} ({seg_id})...")

    en_path = os.path.join(SCRATCH_DIR, f"{seg_id}_en.mp3")
    vi_path = os.path.join(SCRATCH_DIR, f"{seg_id}_vi.mp3")
    combined_path = os.path.join(AUDIO_OUTPUT_DIR, f"{seg_id}.mp3")

    # 1. Generate English with Ryan (British Male)
    await tts_save_retry(seg["en"], EN_VOICE, en_path, pitch="+0Hz", rate="+0%")

    # 2. Generate Northern Male Vietnamese voice (Hanoi accent)
    # Using authentic Hanoi phonetics lowered to masculine fundamental frequency (-70Hz, ~135Hz)
    await tts_save_retry(seg["vi"], VI_VOICE, vi_path, pitch="-70Hz", rate="-3%")

    # 3. Concatenate using ffmpeg filter_complex with 0.4s silence pause & warm chest resonance EQ
    filter_expr = "[2:a]equalizer=f=125:width_type=o:w=1:g=3.5,equalizer=f=3600:width_type=o:w=1:g=-2.5[vi_m];[0:a][1:a][vi_m]concat=n=3:v=0:a=1[out]"
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

    # 4. Measure duration
    dur = get_duration(combined_path)
    seg["duration"] = dur
    seg["audioUrl"] = f"/audio/lectures/geography/1_1/{seg_id}.mp3"
    print(f"   => Xong {seg_id}.mp3: thời lượng {dur}s")

async def main():
    total = len(SEGMENTS)
    print(f"🚀 BẮT ĐẦU TẠO 29 PHÂN ĐOẠN AUDIO SONG NGỮ (GIỌNG ANH-ANH + GIỌNG BẮC VIỆT NAM)...")
    
    current_start = 0.0
    for i, seg in enumerate(SEGMENTS):
        await generate_segment_audio(seg, i, total)
        seg["startTime"] = round(current_start, 2)
        current_start += seg["duration"]
        seg["endTime"] = round(current_start, 2)

    total_duration = round(current_start, 2)

    manifest_data = {
        "lectureId": "6286cb6f-b4ac-495b-b2ea-5a2bab09f764",
        "courseTitle": "IGCSE-Geography-0460",
        "lectureTitle": "1.1 The main hydrological characteristics and processes that operate in rivers and drainage basins",
        "totalDuration": total_duration,
        "segments": SEGMENTS
    }

    manifest_path = os.path.join(AUDIO_OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*60)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ 29 PHÂN ĐOẠN AUDIO BÀI GIẢNG!")
    print(f"📁 Thư mục: {AUDIO_OUTPUT_DIR}")
    print(f"⏱️ Tổng thời lượng: {total_duration}s (~{(total_duration/60):.2f} phút)")
    print(f"📄 File manifest: {manifest_path}")
    print("="*60)

if __name__ == '__main__':
    asyncio.run(main())
