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

LECTURE_ID = "d38db7a8-e92e-450c-a034-b9d46dc10a7f"
AUDIO_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'geography', '2_1')
SCRATCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'scratch', 'audio_temp_2_1')
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

EN_VOICE = 'en-GB-RyanNeural'       # Authentic Male British English
VI_VOICE = 'vi-VN-HoaiMyNeural'     # Authentic Northern Vietnamese (Hanoi accent, 100% natural, pristine)

# TUYỆT ĐỐI 100% TIẾNG VIỆT THUẦN TÚY TRONG PHẦN 'vi':
SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 2.1",
        "selector": "#sec-header",
        "en": "Lesson 2.1: The physical processes that shape the coast. In this lesson, we study coastal erosion, transportation, deposition, longshore drift, and wave dynamics.",
        "vi": "Bài hai chấm một: Các quá trình vật lý định hình bờ biển. Trong bài học này, chúng ta sẽ nghiên cứu về xói mòn, vận chuyển, bồi tụ bờ biển, hiện tượng trôi dạt ven bờ và động lực học của sóng."
    },
    {
        "id": "sec_factors",
        "title": "Các yếu tố ảnh hưởng quá trình bờ biển",
        "selector": "#sec-factors",
        "en": "Section 1: Factors Affecting Coastal Processes. Coastal landforms are shaped by waves, local geology, sea level changes, and human engineering.",
        "vi": "Phần một: Các yếu tố tác động đến quá trình bờ biển. Địa hình bờ biển được định hình bởi sóng biển, cấu trúc địa chất địa phương, sự biến đổi mực nước biển và các công trình nhân tạo."
    },
    {
        "id": "factor_waves",
        "title": "Yếu tố 1: Sóng và Dòng chảy",
        "selector": "#card-factor-waves",
        "en": "Waves and Currents. Waves are the primary coastal shaping agent. Coastal energy determines whether destructive erosion or constructive deposition prevails.",
        "vi": "Sóng và Dòng chảy ven bờ. Sóng biển là tác nhân chính điêu khắc bờ biển. Năng lượng của sóng sẽ quyết định quá trình xói mòn phá hủy hay bồi tụ kiến tạo chiếm ưu thế."
    },
    {
        "id": "factor_geology",
        "title": "Yếu tố 2: Cấu tạo Địa chất địa phương",
        "selector": "#card-factor-geology",
        "en": "Local Geology and Lithology. Hard crystalline rocks such as granite resist wave attack, while weaker clays and chalk suffer rapid cliff retreat.",
        "vi": "Cấu tạo địa chất địa phương. Các loại đá kết tinh cứng như đá hoa cương có khả năng chống chọi mạnh mẽ với sóng biển, trong khi các tầng đá mềm như đất sét và đá phấn bị xói lở nhanh chóng."
    },
    {
        "id": "factor_sealevel",
        "title": "Yếu tố 3: Biến đổi Mực nước biển",
        "selector": "#card-factor-sealevel",
        "en": "Sea Level Changes. Eustatic global sea level changes and local isostatic movements reshape coastlines, with modern climate change accelerating coastal retreat.",
        "vi": "Biến đổi mực nước biển. Mực nước biển dâng do băng tan toàn cầu và các biến động nâng hạ địa chất cục bộ đang làm biến đổi đường bờ biển và đẩy nhanh nguy cơ ngập lụt ven bờ."
    },
    {
        "id": "factor_human",
        "title": "Yếu tố 4: Tác động của Con người",
        "selector": "#card-factor-human",
        "en": "Human Activity. Coastal defense engineering, harbor construction, and dredging alter natural sediment transport and reshape shorelines.",
        "vi": "Tác động của con người. Việc xây dựng các công trình kè chắn sóng biển, cảng biển và nạo vét luồng lạch làm thay đổi dòng luân chuyển trầm tích tự nhiên và biến đổi hình thái bờ biển."
    },
    {
        "id": "sec_erosion",
        "title": "Phần 2: Bốn kiểu Xói mòn bờ biển",
        "selector": "#sec-erosion",
        "en": "Section 2: Coastal Erosion Processes. High energy waves continually attack cliff faces through four fundamental erosional mechanisms.",
        "vi": "Phần hai: Bốn cơ chế xói mòn bờ biển. Sóng biển mang năng lượng cao liên tục tấn công vào các vách đá ven biển qua bốn cơ chế xói mòn nền tảng."
    },
    {
        "id": "erosion_overview",
        "title": "Tác động thủy lực trên bờ san hô (Figure 2.2)",
        "selector": "#card-erosion-overview",
        "en": "Hydraulic Action on Coral Coasts. As seen in Figure 2.2, pounding waves force trapped air into joints and crevices with explosive power.",
        "vi": "Tác động thủy lực trên bờ biển san hô. Như thể hiện ở hình hai chấm hai, những con sóng dữ dội nén bọt khí vào các khe nứt đá với sức ép khổng lồ tạo nên lực nổ đánh bật các mảng đá."
    },
    {
        "id": "erosion_hydraulic",
        "title": "Thủy lực học (Hydraulic Action)",
        "selector": "#card-erosion-hydraulic",
        "en": "Hydraulic Action in detail. The physical force of crashing waves traps air in cliff fissures. Receding water triggers violent air expansion, shattering rock faces.",
        "vi": "Chi tiết Tác động thủy lực. Áp lực vật lý của những đợt sóng va đập nén chặt không khí vào các kẽ nứt của vách đá. Khi sóng rút, áp suất bung nở đột ngột làm vỡ vụn các khối đá."
    },
    {
        "id": "erosion_abrasion",
        "title": "Mài mòn cơ học (Corrasion / Abrasion)",
        "selector": "#card-erosion-abrasion",
        "en": "Corrasion and Abrasion in detail. Waves throw hurled sand, shingle, and pebbles like sandpaper against cliffs, carving deep wave-cut notches.",
        "vi": "Chi tiết Mài mòn cơ học. Sóng biển ném cát sỏi và đá cuội vào chân vách đá giống như một tờ giấy ráp khổng lồ, khoét sâu các hàm ếch bờ biển."
    },
    {
        "id": "erosion_attrition",
        "title": "Va đập tự vỡ (Attrition)",
        "selector": "#card-erosion-attrition",
        "en": "Attrition in detail. Transported boulders and pebbles crash into one another, progressively fracturing jagged rocks into smooth, rounded pebbles and sand.",
        "vi": "Chi tiết Quá trình va đập tự vỡ vụn. Các tảng đá và sỏi cuội va đập liên hoàn vào nhau dưới tác động của sóng, mài nhẵn các góc cạnh sắc nhọn thành những viên sỏi tròn bóng và hạt cát mịn."
    },
    {
        "id": "erosion_solution",
        "title": "Hòa tan hóa học (Corrosion / Solution)",
        "selector": "#card-erosion-solution",
        "en": "Corrosion and Solution in detail. Weak carbonic acid in seawater chemically dissolves vulnerable carbonate minerals in limestone and chalk cliffs.",
        "vi": "Chi tiết Xói mòn hòa tan hóa học. Tính axit nhẹ của nước biển phản ứng và hòa tan các khoáng chất canxi cacbonat trong các vách đá vôi và vách đá phấn."
    },
    {
        "id": "sec_transport",
        "title": "Phần 3: Vận chuyển trầm tích bờ biển",
        "selector": "#sec-transport",
        "en": "Section 3: Coastal Transportation. Marine currents transport weathered rock fragments through bedload rolling and water column suspension.",
        "vi": "Phần ba: Vận chuyển trầm tích bờ biển. Các dòng hải lưu vận chuyển các mảnh vụn đá qua hình thức lăn trượt dưới đáy và lơ lửng trong tầng nước."
    },
    {
        "id": "transport_bedload",
        "title": "Vận chuyển đáy (Traction & Saltation)",
        "selector": "#card-transport-bedload",
        "en": "Bedload Transport. Heavy boulders roll along the seabed by traction, while medium sand grains bounce along through saltation hops.",
        "vi": "Vận chuyển đáy biển. Các tảng đá nặng trượt lăn dọc đáy biển nhờ lực kéo, trong khi các hạt cát vừa nhảy cóc liên tục theo dòng chuyển động."
    },
    {
        "id": "transport_suspended",
        "title": "Vận chuyển lơ lửng & hòa tan (Suspension & Solution)",
        "selector": "#card-transport-suspended",
        "en": "Suspended and Solution Load. Fine clay drifts suspended in turbulent currents, while dissolved minerals travel invisibly across the ocean.",
        "vi": "Vận chuyển lơ lửng và hòa tan. Các hạt sét mịn trôi lơ lửng trong dòng nước xiết, còn các ion khoáng chất hòa tan di chuyển vô hình trong đại dương."
    },
    {
        "id": "sec_deposition",
        "title": "Phần 4: Quá trình Bồi tụ bờ biển",
        "selector": "#sec-deposition",
        "en": "Section 4: Coastal Deposition. When wave velocity and energy decline, transported sediments drop in order of mass, forming beaches and sandbars.",
        "vi": "Phần bốn: Quá trình Bồi tụ bờ biển. Khi vận tốc và động năng của sóng suy giảm, trầm tích lắng xuống theo thứ tự trọng lượng, kiến tạo nên các bãi biển và cồn cát."
    },
    {
        "id": "deposition_conditions",
        "title": "Điều kiện bồi tụ & Trình tự lắng đọng",
        "selector": "#card-deposition-conditions",
        "en": "Conditions Favouring Deposition. Sheltered bays, gentle coastal slopes, and constructive wave patterns encourage sediment deposition, dropping boulders first and fine mud last.",
        "vi": "Các điều kiện thuận lợi cho bồi tụ. Vùng vịnh kín gió, bờ biển thoai thoải và sóng bồi tụ giúp lắng đọng trầm tích, trong đó đá tảng chìm xuống trước và bùn mịn lắng đọng sau cùng."
    },
    {
        "id": "sec_longshore_drift",
        "title": "Phần 5: Hiện tượng trôi dạt ven bờ (Longshore Drift)",
        "selector": "#sec-longshore-drift",
        "en": "Section 5: Longshore Drift. Prevailing winds generate angled wave approaches, driving zigzag sediment migration parallel to the shoreline.",
        "vi": "Phần năm: Hiện tượng trôi dạt cát ven bờ. Gió thịnh hành đẩy sóng vỗ vào bờ theo góc nghiêng, tạo nên dòng chuyển dịch trầm tích hình chữ chi dọc theo dải bờ biển."
    },
    {
        "id": "lsd_diagram",
        "title": "Cơ chế: Sóng tràn chéo & Sóng rút thẳng",
        "selector": "#card-lsd-diagram",
        "en": "Swash and Backwash Mechanism. Angled swash carries sand diagonally up the beach face, while gravity drags backwash straight down perpendicular to the shore.",
        "vi": "Cơ chế Sóng tràn và Sóng rút. Đợt sóng tràn đẩy cát sỏi chéo lên bờ biển, sau đó trọng lực kéo đợt sóng rút thẳng góc xuống đáy biển, tạo ra chuyển động dích dắc liên tục."
    },
    {
        "id": "lsd_groynes",
        "title": "Quản lý bằng Đê chắn cát (Groynes)",
        "selector": "#card-lsd-groynes",
        "en": "Management with Groynes. Wooden or rock groynes built perpendicular to the shore trap sediment on the updrift side, but starve downdrift beaches.",
        "vi": "Quản lý bằng đê chắn cát vuông góc. Các hàng cọc gỗ hoặc bờ đá xây vuông góc với bờ biển giúp giữ cát ở phía đón dòng trôi, nhưng lại khiến bãi biển phía sau bị thiếu hụt cát trầm trọng."
    },
    {
        "id": "sec_wave_types",
        "title": "Phần 6: Sóng bồi tụ và Sóng phá hủy",
        "selector": "#sec-wave-types",
        "en": "Section 6: Wave Types. Constructive waves build beaches through gentle deposition, whereas destructive waves scour sediment away.",
        "vi": "Phần sáu: Phân loại Sóng biển. Sóng bồi tụ xây đắp bãi biển nhờ lực tràn bờ nhẹ nhàng, trong khi sóng phá hủy cào xới và cuốn trôi cát ra xa."
    },
    {
        "id": "wave_constructive",
        "title": "Đặc điểm Sóng bồi tụ (Constructive Waves)",
        "selector": "#card-wave-constructive",
        "en": "Constructive Waves. Characterised by long wavelength, low wave height, gentle beach slopes, and a dominant swash stronger than the backwash.",
        "vi": "Đặc điểm Sóng bồi tụ. Có bước sóng dài, chiều cao sóng thấp, độ dốc bãi biển thoai thoải và đợt sóng tràn lên bờ mạnh hơn hẳn đợt sóng rút lui."
    },
    {
        "id": "wave_destructive",
        "title": "Đặc điểm Sóng phá hủy (Destructive Waves)",
        "selector": "#card-wave-destructive",
        "en": "Destructive Waves. Featuring high wave heights, steep frequency, circular particle orbits, and a violent backwash that scours sediment from the shore.",
        "vi": "Đặc điểm Sóng phá hủy. Chiều cao sóng lớn, tần số dồn dập, chuyển động hạt tròn và đợt sóng rút xuống cực mạnh cuốn sạch cát sỏi khỏi bờ biển."
    },
    {
        "id": "wave_comparison",
        "title": "Bảng đối chiếu hai loại sóng",
        "selector": "#card-wave-comparison",
        "en": "Wave Comparison Summary. Constructive waves deposit sediment to build flat beaches, whereas stormy destructive waves erode steep gravel profiles.",
        "vi": "Bảng tổng kết so sánh Sóng biển. Sóng bồi tụ bồi lắng cát tạo nên các bãi cát rộng thoải, trong khi sóng bão phá hủy xói lở tạo nên các bờ biển dốc đứng."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec_factors": {"start": 1, "end": 5},
    "sec_erosion": {"start": 6, "end": 11},
    "sec_transport": {"start": 12, "end": 14},
    "sec_deposition": {"start": 15, "end": 16},
    "sec_longshore_drift": {"start": 17, "end": 19},
    "sec_wave_types": {"start": 20, "end": 23}
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
    print(f"[{index + 1}/{total}] 2.1 Audio: {seg['title']} ({seg_id})...")

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
    seg["audioUrl"] = f"/audio/lectures/geography/2_1/{seg_id}.mp3"
    print(f"   => Xong: {seg_id}.mp3 ({dur}s)")

async def main():
    total = len(SEGMENTS)
    print(f"🚀 BẮT ĐẦU TẠO {total} PHÂN ĐOẠN AUDIO CHO BÀI 2.1:")
    
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
        "lectureTitle": "2.1 The physical processes that shape the coast",
        "totalDuration": total_duration,
        "majorSections": MAJOR_SECTIONS,
        "segments": SEGMENTS
    }

    manifest_path = os.path.join(AUDIO_OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)

    print(f"🎉 Đã ghi manifest: {manifest_path} (Tổng: {total_duration}s)")

    # Update Supabase HTML for 2.1
    with open('.env', 'r', encoding='utf-8') as f:
        env = f.read()
    url = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
    key = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
    sb = create_client(url, key)

    with open("scratch/lectures/2_1_p1_interactive.html", "r", encoding="utf-8") as f:
        updated_html = f.read()

    res = sb.table('lecture_pages').update({'content_html': updated_html}).eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
    print("✅ Đã cập nhật HTML trang 1 Bài 2.1 lên Supabase!")

if __name__ == '__main__':
    asyncio.run(main())
