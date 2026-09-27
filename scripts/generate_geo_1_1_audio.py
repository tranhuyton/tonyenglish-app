import asyncio
import os
import sys
import subprocess
import json
import edge_tts

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

OUTPUT_DIR = os.path.join("public", "audio", "lectures", "geography", "1_1")
os.makedirs(OUTPUT_DIR, exist_ok=True)

TEMP_DIR = os.path.join("scratch", "temp_tts")
os.makedirs(TEMP_DIR, exist_ok=True)

VOICE_EN = "en-GB-RyanNeural"     # Anh-Anh Nam chuẩn Cambridge
VOICE_VI = "vi-VN-NamMinhNeural"  # Tiếng Việt Nam tự nhiên, ấm áp

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 1.1",
        "selector": "#sec-header",
        "en": "Lesson 1.1: The main hydrological characteristics and processes that operate in rivers and drainage basins.",
        "vi": "Bài 1.1: Các đặc điểm thủy văn và quá trình vận hành trong các con sông và lưu vực thoát nước."
    },
    {
        "id": "drainage_basin",
        "title": "1. Khái niệm Lưu vực sông (Drainage Basin)",
        "selector": "#sec-drainage-basin",
        "en": "Part 1: Rivers and Drainage Basins. A drainage basin is the area of land drained by a river and all its tributaries. It is an open system with inputs such as precipitation, and outputs such as evaporation and river discharge to the sea. The boundary of a drainage basin is called the watershed, usually following a ridge of high ground.",
        "vi": "Phần 1: Các con sông và Lưu vực sông. Lưu vực sông là toàn bộ diện tích đất được một con sông chính và tất cả các phụ lưu của nó thoát nước. Đây là một hệ thống mở với đầu vào như lượng mưa, và đầu ra như bốc hơi hoặc nước đổ ra biển. Ranh giới bao quanh lưu vực sông được gọi là đường phân thủy, thường men theo các sống núi hoặc vùng đồi cao."
    },
    {
        "id": "source",
        "title": "Source - Nguồn sông",
        "selector": "#term-source",
        "en": "Source. Where the river begins — usually on high ground, such as a bog or spring.",
        "vi": "Nguồn sông. Nơi dòng sông bắt đầu hình thành — thường xuất phát từ vùng núi cao, đầm lầy hoặc mạch nước ngầm."
    },
    {
        "id": "mouth",
        "title": "Mouth - Cửa sông",
        "selector": "#term-mouth",
        "en": "Mouth. Where the river meets the sea, a lake, or another river.",
        "vi": "Cửa sông. Điểm cuối nơi con sông đổ vào biển, đại dương, hồ nước hoặc nhập vào một dòng sông khác."
    },
    {
        "id": "tributary",
        "title": "Tributary - Phụ lưu / Nhánh sông",
        "selector": "#term-tributary",
        "en": "Tributary. A smaller river or stream that flows into the main river.",
        "vi": "Phụ lưu. Một dòng sông hoặc con suối nhỏ hơn chảy hòa vào dòng sông chính."
    },
    {
        "id": "confluence",
        "title": "Confluence - Ngã ba sông / Hợp lưu",
        "selector": "#term-confluence",
        "en": "Confluence. The point where two rivers join together.",
        "vi": "Ngã ba sông hay điểm hợp lưu. Là nơi hai dòng sông gặp nhau và hợp làm một dòng chảy."
    },
    {
        "id": "watershed",
        "title": "Watershed - Đường phân thủy",
        "selector": "#term-watershed",
        "en": "Watershed. The boundary or ridge separating one drainage basin from another.",
        "vi": "Đường phân thủy. Ranh giới tự nhiên hoặc sống núi ngăn cách giữa hai lưu vực sông liền kề."
    },
    {
        "id": "floodplain",
        "title": "Flood plain - Đồng bằng ngập lũ",
        "selector": "#term-floodplain",
        "en": "Flood plain. Flat land beside the river, flooded when discharge is high.",
        "vi": "Đồng bằng ngập lũ. Vùng đất bằng phẳng nằm dọc hai bên bờ sông, bị ngập chìm khi lưu lượng nước sông dâng cao."
    },
    {
        "id": "bradshaw_model",
        "title": "2. Mô hình Bradshaw (Bradshaw Model)",
        "selector": "#sec-bradshaw",
        "en": "Part 2: The Bradshaw Model. The Bradshaw Model shows how river characteristics change systematically from source to mouth as discharge increases. Downstream, discharge, channel width, depth, and velocity increase, while gradient, particle size, and channel roughness decrease.",
        "vi": "Phần 2: Mô hình Bradshaw. Mô hình Bradshaw mô tả quy luật biến đổi của dòng sông từ thượng lưu ra cửa biển khi lưu lượng tăng dần. Càng xuôi dòng, lưu lượng, bề rộng lòng sông, độ sâu và vận tốc trung bình đều tăng; trong khi độ dốc, kích thước đất đá và độ gồ ghề của đáy sông sẽ giảm dần."
    },
    {
        "id": "water_cycle",
        "title": "3. Chu trình nước trong lưu vực",
        "selector": "#sec-water-cycle",
        "en": "Part 3: The Drainage Basin Water Cycle. The water cycle consists of inputs like precipitation, stores like interception and groundwater, transfers like surface runoff, throughflow, and percolation, and outputs like evapotranspiration.",
        "vi": "Phần 3: Chu trình nước trong lưu vực sông. Chu trình nước bao gồm đầu vào là lượng mưa, các nơi lưu trữ như tán lá chắn và nước ngầm, các dòng chuyển dịch như dòng mặt, dòng trong đất và thấm sâu, cùng đầu ra là quá trình thoát bốc hơi."
    },
    {
        "id": "fluvial_processes",
        "title": "4. Các quá trình sông ngòi (Fluvial Processes)",
        "selector": "#sec-fluvial-processes",
        "en": "Part 4: Fluvial Processes. Fluvial processes include four types of erosion: hydraulic action, abrasion, attrition, and solution; alongside four types of transportation: traction, saltation, suspension, and solution.",
        "vi": "Phần 4: Các quá trình sông ngòi. Bao gồm 4 hình thức xói mòn: tác động thủy lực, mài mòn cơ học, va đập nghiền nhỏ và hòa tan; cùng 4 hình thức vận chuyển trầm tích: lăn kéo đáy, nhảy cóc, lơ lửng và hòa tan."
    }
]

def get_audio_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        return float(res.stdout.strip())
    except Exception:
        return 0.0

async def generate_segment(seg, index):
    seg_id = seg["id"]
    print(f"[{index + 1}/{len(SEGMENTS)}] Generating: {seg['title']}...")
    
    en_path = os.path.join(TEMP_DIR, f"{seg_id}_en.mp3")
    vi_path = os.path.join(TEMP_DIR, f"{seg_id}_vi.mp3")
    combined_path = os.path.join(OUTPUT_DIR, f"{seg_id}.mp3")

    # Generate English audio
    tts_en = edge_tts.Communicate(seg["en"], VOICE_EN, rate="+0%")
    await tts_en.save(en_path)

    # Generate Vietnamese audio
    tts_vi = edge_tts.Communicate(seg["vi"], VOICE_VI, rate="+5%")
    await tts_vi.save(vi_path)

    # Combine with ffmpeg (with 400ms pause between English & Vietnamese)
    cmd = [
        "ffmpeg", "-y",
        "-i", en_path,
        "-i", vi_path,
        "-filter_complex",
        "[0:a]adelay=0|0[a0];[1:a]adelay=400|400[a1];[a0][a1]concat=n=2:v=0:a=1[out]",
        "-map", "[out]",
        "-b:a", "64k",
        combined_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

    dur = get_audio_duration(combined_path)
    return {
        "id": seg["id"],
        "title": seg["title"],
        "selector": seg["selector"],
        "en": seg["en"],
        "vi": seg["vi"],
        "audioUrl": f"/audio/lectures/geography/1_1/{seg_id}.mp3",
        "duration": round(dur, 2)
    }

async def main():
    manifest = []
    total_time = 0.0
    for idx, seg in enumerate(SEGMENTS):
        item = await generate_segment(seg, idx)
        item["startTime"] = round(total_time, 2)
        total_time += item["duration"]
        item["endTime"] = round(total_time, 2)
        manifest.append(item)

    manifest_path = os.path.join(OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "lectureId": "6286cb6f-b4ac-495b-b2ea-5a2bab09f764",
            "courseTitle": "IGCSE-Geography-0460",
            "lectureTitle": "1.1 The main hydrological characteristics and processes that operate in rivers and drainage basins",
            "totalDuration": round(total_time, 2),
            "segments": manifest
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✅ All {len(manifest)} segments generated successfully!")
    print(f"Total lecture audio duration: {round(total_time, 2)}s ({round(total_time / 60, 2)} mins)")
    print(f"Manifest written to: {manifest_path}")

if __name__ == "__main__":
    asyncio.run(main())
