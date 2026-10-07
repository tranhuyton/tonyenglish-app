import os
import sys
import json
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"F:\Downloads\Chrome\IELTS Premium-studio"
SUPABASE_STORAGE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets"

skills_meta = {
    "task1": {
        "folder": "Writing Task 1",
        "moduleId": "4d5cce14-0b7e-44c3-91a9-c05eccdc01e3",
        "moduleName": "Luyện thi Viết : Task 1",
        "lectureTitle": "Podcast Viết Task 1",
        "storageFolder": "audio/podcast/ielts-premium/task1",
        "themeColor": "#0f766e",
        "themeBg": "linear-gradient(135deg, #134e4a 0%, #0f766e 50%, #0d9488 100%)",
        "badge": "6 TẬP PODCAST TASK 1",
        "desc": "Chiến thuật ghép khung bất biến, từ vựng xu hướng và phân tích dữ liệu chuyên sâu cho tất cả các dạng biểu đồ IELTS Writing Task 1.",
        "episodes": [
            {
                "ch": 1,
                "title": "Task 1 Dynamic Chart (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật ghép khung với từ vựng chỉ xu hướng tăng, giảm, dao động, chạm mốc và từ nối mô tả sự thay đổi qua các mốc thời gian.",
                "file": "01-Cấu trúc bất biến Dynamic Chart IELTS.mp3"
            },
            {
                "ch": 2,
                "title": "Task 1 Static Chart (thầy Tôn - tonyenglish.vn)",
                "sub": "Phương pháp ghép khung với từ vựng so sánh hơn, so sánh nhất, nhóm hạng mục, tỷ trọng cho bài không có mốc thời gian.",
                "file": "02-Tư duy logic viết Task 1 IELTS.mp3"
            },
            {
                "ch": 3,
                "title": "Task 1 Process (thầy Tôn - tonyenglish.vn)",
                "sub": "Bí quyết ghép khung quy trình tự nhiên/nhân tạo với câu bị động (Passive Voice), từ nối thứ tự các bước và động từ chuyển hóa giai đoạn.",
                "file": "03-Cấu trúc bất biến IELTS Process.mp3"
            },
            {
                "ch": 4,
                "title": "Task 1 Outdoor Map (thầy Tôn - tonyenglish.vn)",
                "sub": "Kỹ thuật ghép khung bản đồ quy hoạch khu vực với từ vựng mở rộng, phá bỏ, thay thế và hướng phương vị (Bắc-Nam-Đông-Tây).",
                "file": "04-Cách viết bài IELTS Outdoor Map.mp3"
            },
            {
                "ch": 5,
                "title": "Task 1 Indoor Map (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật ghép khung sơ đồ mặt bằng/nội thất không gian hẹp với từ vựng chỉ vị trí đối diện, kế bên, góc phòng và cải tạo mặt bằng.",
                "file": "05-Cách viết Indoor Map IELTS.mp3"
            },
            {
                "ch": 6,
                "title": "Task 1 Mixed Charts (thầy Tôn - tonyenglish.vn)",
                "sub": "Phương pháp xử lý biểu đồ kết hợp, cách chia Body 1 & Body 2 cho 2 biểu đồ riêng biệt và kỹ thuật viết Overview 2 ý song song.",
                "file": "06-Chiến thuật viết Mixed Charts IELTS.mp3"
            }
        ]
    },
    "task2": {
        "folder": "Writing Task 2",
        "moduleId": "fe69b202-583e-4aee-9bd6-31a7f95d331e",
        "moduleName": "Luyện thi Viết : Task 2",
        "lectureTitle": "Podcast Viết Task 2",
        "storageFolder": "audio/podcast/ielts-premium/task2",
        "themeColor": "#7e22ce",
        "themeBg": "linear-gradient(135deg, #581c87 0%, #7e22ce 50%, #9333ea 100%)",
        "badge": "5 TẬP PODCAST TASK 2",
        "desc": "Bộ khung cấu trúc bất biến kết hợp hệ thống trụ ý Idea Pillars độc quyền của thầy Tôn, xử lý triệt để 5 dạng bài luận IELTS Writing Task 2.",
        "episodes": [
            {
                "ch": 1,
                "title": "Discussion Essay Task 2 ghép Framework & Idea Pillars",
                "sub": "Thảo luận cách nhận diện dạng bài thảo luận 2 quan điểm, phương pháp chia 2 Body cân bằng và kỹ thuật ghép trụ ý Idea Pillars (Freedom, Cost, Job, Health...) vào từng góc nhìn.",
                "file": "01-Chiến thuật viết Discussion Essay IELTS.mp3"
            },
            {
                "ch": 2,
                "title": "Opinion Essay Task 2 ghép Framework & Idea Pillars",
                "sub": "Phân tích chiến thuật chọn nghiêng hẳn (100%) hoặc trung lập (balanced/partially agree), cách dùng khung cấu trúc bất biến để bảo vệ quan điểm cá nhân chặt chẽ.",
                "file": "02-Công thức viết Opinion Essay IELTS.mp3"
            },
            {
                "ch": 3,
                "title": "Advantage & Disadvantage Essay Task 2",
                "sub": "Phân biệt dạng bài Lợi ích / Tác hại thuần túy và dạng Outweigh, cách ghép khung phân tích mặt tích cực - tiêu cực với hệ thống trụ ý Idea Pillars tương ứng.",
                "file": "03-Cấu trúc bất biến bài IELTS Writing.mp3"
            },
            {
                "ch": 4,
                "title": "Problem & Solution Essay Task 2",
                "sub": "Chiến thuật ghép cấu trúc Nguyên nhân - Giải pháp với các trụ giải pháp vĩ mô (Macro Solution Pillars: Chính phủ, Pháp luật) và vi mô (Micro Solution Pillars: Giáo dục, Cá nhân, Nhà trường).",
                "file": "04-Cấu trúc bất biến IELTS Writing.mp3"
            },
            {
                "ch": 5,
                "title": "Two-Part Questions Essay Task 2",
                "sub": "Phương pháp xử lý dạng câu hỏi đôi / trực tiếp, cách dùng khung cấu trúc trả lời lần lượt từng câu hỏi ở Body 1 & Body 2 kết hợp linh hoạt các trụ ý.",
                "file": "05-Chiến thuật xử lý IELTS Two Part.mp3"
            }
        ]
    },
    "reading": {
        "folder": "Reading",
        "moduleId": "65bda52c-a4f3-4bfe-bb81-ccc9b20dc7f7",
        "moduleName": "Luyện thi Đọc",
        "lectureTitle": "Podcast Luyện Đọc",
        "storageFolder": "audio/podcast/ielts-premium/reading",
        "themeColor": "#15803d",
        "themeBg": "linear-gradient(135deg, #14532d 0%, #15803d 50%, #16a34a 100%)",
        "badge": "6 TẬP PODCAST READING",
        "desc": "Tư duy định vị thông tin, bóc tách các bẫy phổ biến và chiến thuật xử lý tốc độ cho 6 dạng bài IELTS Reading then chốt.",
        "episodes": [
            {
                "ch": 1,
                "title": "True/False/Not Given IELTS Reading (thầy Tôn - tonyenglish.vn)",
                "sub": "Kỹ thuật phân biệt False vs Not Given, chiến lược quét từ khóa định vị và nhận diện bẫy suy diễn thông tin.",
                "file": "01-Bẫy True False Not Given IELTS.mp3"
            },
            {
                "ch": 2,
                "title": "Completion Types IELTS Reading (thầy Tôn - tonyenglish.vn)",
                "sub": "Bẫy ngữ pháp, giới hạn số từ (word limit), dự đoán loại từ và kỹ thuật dò tìm từ đồng nghĩa (paraphrasing).",
                "file": "02-Bẫy dạng điền từ IELTS Reading.mp3"
            },
            {
                "ch": 3,
                "title": "Matching Information & Features IELTS Reading (thầy Tôn - tonyenglish.vn)",
                "sub": "Tư duy định vị quét tên riêng, mốc thời gian, nối đặc điểm với danh sách đối tượng nghiên cứu.",
                "file": "03-Tư duy định vị IELTS Reading.mp3"
            },
            {
                "ch": 4,
                "title": "Matching Headings IELTS Reading (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật nắm bắt Topic Sentence, phân biệt ý chính đoạn văn với ví dụ minh họa chi tiết.",
                "file": "04-Chiến thuật làm bài Matching Headings.mp3"
            },
            {
                "ch": 5,
                "title": "Multiple Choice IELTS Reading (thầy Tôn - tonyenglish.vn)",
                "sub": "Phương pháp loại trừ phương án nhiễu, bẫy từ khóa lặp lại nguyên văn và bẫy tuyệt đối hóa.",
                "file": "05-Phá bẫy Multiple Choice IELTS Reading.mp3"
            },
            {
                "ch": 6,
                "title": "Short Answer Questions IELTS Reading (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật định vị câu trả lời ngắn, trích xuất nguyên văn cụm từ chính xác từ bài đọc.",
                "file": "06-Chiến thuật IELTS Reading trả lời ngắn.mp3"
            }
        ]
    },
    "listening": {
        "folder": "Listening",
        "moduleId": "2db0cf32-3ea1-4fe2-afc7-37b8dae49afd",
        "moduleName": "Luyện thi Nghe",
        "lectureTitle": "Podcast Luyện Nghe",
        "storageFolder": "audio/podcast/ielts-premium/listening",
        "themeColor": "#c2410c",
        "themeBg": "linear-gradient(135deg, #7c2d12 0%, #c2410c 50%, #ea580c 100%)",
        "badge": "9 TẬP PODCAST LISTENING",
        "desc": "Chiến lược nhận diện cạm bẫy âm thanh, kỹ thuật nghe bắt từ khóa và xử lý toàn diện 9 dạng câu hỏi IELTS Listening.",
        "episodes": [
            {
                "ch": 1,
                "title": "Letters & Numbers IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Bẫy đánh vần tên riêng, chữ cái dễ nhầm (A-E-I, J-G, H-8), số điện thoại, mã bưu chính và đơn vị tiền tệ.",
                "file": "01-Bẫy chữ cái và con số IELTS.mp3"
            },
            {
                "ch": 2,
                "title": "Form Completion IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật nghe bắt thông tin Section 1, bẫy sửa lại thông tin (self-correction) và định dạng ngày tháng.",
                "file": "02-Bẫy Form Completion trong IELTS Listening.mp3"
            },
            {
                "ch": 3,
                "title": "Map Labelling IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật xử gọn sơ đồ bản đồ, xác định điểm xuất phát, phương hướng và từ chỉ vị trí không gian.",
                "file": "03-Chiến thuật xử gọn IELTS Map Labelling.mp3"
            },
            {
                "ch": 4,
                "title": "Short Answer Questions IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Kỹ thuật bắt từ khóa then chốt, tháo gỡ bẫy từ gây nhiễu và kiểm soát giới hạn số từ cho phép.",
                "file": "04-Tháo bẫy Short Answer Questions IELTS.mp3"
            },
            {
                "ch": 5,
                "title": "Diagram & Flow-chart IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Kỹ thuật theo dõi quy trình từng bước, nhận diện các từ nối chuyển giao giai đoạn trong bài nghe.",
                "file": "05-Chiến thuật làm Diagram IELTS Listening.mp3"
            },
            {
                "ch": 6,
                "title": "Note, Table & Sentence Completion IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Dự đoán loại từ cần điền, kỹ thuật bám sát cấu trúc ngữ pháp và nhận diện từ đồng nghĩa tức thời.",
                "file": "06-Né bẫy IELTS Listening Completion.mp3"
            },
            {
                "ch": 7,
                "title": "Multiple Choice IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật đọc trước đáp án Section 2 & 3, nhận diện bẫy nói về cả 3 phương án để đánh lừa.",
                "file": "07-Né bẫy trắc nghiệm IELTS Listening.mp3"
            },
            {
                "ch": 8,
                "title": "Matching IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Phương pháp ghi chú nhanh, ghép cặp thông tin nhân vật, ý kiến với danh sách lựa chọn rút gọn.",
                "file": "08-Thoát bẫy Matching trong IELTS Listening.mp3"
            },
            {
                "ch": 9,
                "title": "Summary Completion IELTS Listening (thầy Tôn - tonyenglish.vn)",
                "sub": "Chiến thuật chinh phục tóm tắt Section 4, bám sát dàn ý bài giảng học thuật của diễn giả.",
                "file": "09-Chiến thuật làm bài Summary Completion IELTS.mp3"
            }
        ]
    },
    "speaking": {
        "folder": "Speaking Part 2",
        "moduleId": "5a9c8837-eb63-4492-af17-dbb0f39a90b1",
        "moduleName": "Luyện thi Nói",
        "lectureTitle": "Podcast Luyện Nói",
        "storageFolder": "audio/podcast/ielts-premium/speaking",
        "themeColor": "#be185d",
        "themeBg": "linear-gradient(135deg, #831843 0%, #be185d 50%, #db2777 100%)",
        "badge": "10 TẬP PODCAST SPEAKING PART 2",
        "desc": "Chiến thuật 9 Templates bẻ lái độc quyền của thầy Tôn, giúp thí sinh làm chủ mọi chủ đề IELTS Speaking Part 2 một cách tự tin và lưu loát.",
        "episodes": [
            {
                "ch": 1,
                "title": "Template 1 - Mr. John (Mô tả người / Thầy giáo / Người ngưỡng mộ) [1]",
                "sub": "Cấu trúc 4 giai đoạn mô tả ngoại hình, tính cách, kỷ niệm sâu sắc và tác động tích cực đến bản thân.",
                "file": "01-Bí quyết tả người IELTS Speaking.mp3"
            },
            {
                "ch": 2,
                "title": "Template 2 - A Modern Flat (Mô tả địa điểm / Căn hộ / Tòa nhà hiện đại) [1]",
                "sub": "Kỹ thuật mô tả kiến trúc không gian, tiện nghi hiện đại, vị trí và cảm giác thoải mái khi ở đó.",
                "file": "02-Template Modern Flat cho IELTS Speaking.mp3"
            },
            {
                "ch": 3,
                "title": "Template 3 - The Bicycle (Mô tả đồ vật / Phương tiện / Món đồ yêu thích) [1]",
                "sub": "Chiến thuật kể câu chuyện nguồn gốc món đồ, công dụng hàng ngày, giá trị tinh thần và kỷ niệm.",
                "file": "03-Cấu trúc 4 giai đoạn IELTS Speaking.mp3"
            },
            {
                "ch": 4,
                "title": "Template 4 - Bicycle Racing (Mô tả sự kiện / Cuộc thi / Môn thể thao) [1]",
                "sub": "Cách xây dựng cao trào sự kiện, không khí hồi hộp, sự chuẩn bị và bài học vượt qua giới hạn.",
                "file": "04-Template Cuộc đua xe đạp IELTS Speaking.mp3"
            },
            {
                "ch": 5,
                "title": "Template 5 - Bai Dinh Temple (Mô tả địa điểm lịch sử / Văn hóa / Chuyến đi) [1]",
                "sub": "Khung miêu tả danh lam thắng cảnh, kiến trúc cổ kính, không khí trang nghiêm và ý nghĩa lịch sử.",
                "file": "05-Cấu trúc 4 bước Template Bái Đính.mp3"
            },
            {
                "ch": 6,
                "title": "Template 6 - Autumn Weather (Mô tả thời tiết / Mùa yêu thích / Thời điểm) [1]",
                "sub": "Bản thiết kế mô tả khí hậu, sắc thái thiên nhiên mùa thu Hà Nội, tâm trạng thư thái và hoạt động ngoài trời.",
                "file": "06-Bản thiết kế Template 6 Thầy Tôn.mp3"
            },
            {
                "ch": 7,
                "title": "Template 7 - Korean BBQ (Mô tả món ăn / Bữa ăn / Ẩm thực) [1]",
                "sub": "Cấu trúc 4 giai đoạn miêu tả hương vị, nguyên liệu, trải nghiệm ẩm thực ấm cúng bên người thân.",
                "file": "07-Cấu trúc 4 Stage Template Korean BBQ.mp3"
            },
            {
                "ch": 8,
                "title": "Template 8 - The Bamboo (Mô tả cây cối / Thực vật / Biểu tượng) [1]",
                "sub": "Nghệ thuật miêu tả cây tre Việt Nam: đặc tính kiên cường, công dụng truyền thống và biểu tượng văn hóa.",
                "file": "08-Cấu trúc 4 giai đoạn bài nói.mp3"
            },
            {
                "ch": 9,
                "title": "Template 9 - The Happy Couple (Mô tả mối quan hệ / Cặp đôi / Kỷ niệm) [1]",
                "sub": "Khung kể chuyện tình cảm hạnh phúc của bố mẹ/ông bà, những thử thách đã qua và cảm hứng yêu thương.",
                "file": "09-Template Speaking Cặp đôi hạnh phúc.mp3"
            },
            {
                "ch": 10,
                "title": "Hướng dẫn Ghép 9 Templates với các Chủ đề Speaking Part 2 (Tư duy bẻ lái đề bài và ứng biến linh hoạt) [1]",
                "sub": "Tư duy bẻ lái đề bài linh hoạt (topic shifting), cách liên kết mọi đề thi bất ngờ về 9 khung tủ vững chắc.",
                "file": "10-9 template bẻ lái Speaking Part 2.mp3"
            }
        ]
    }
}

def get_duration(filepath):
    cmd = f'ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{filepath}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    sec = int(float(res.stdout.strip()))
    m = sec // 60
    s = sec % 60
    return sec, f"{m}:{s:02d}"

compiled = {}

print("Calculating durations and compiling manifest...")
for skill_key, s_data in skills_meta.items():
    print(f"\n--- {s_data['moduleName']} ({len(s_data['episodes'])} episodes) ---")
    folder_path = os.path.join(base_dir, s_data["folder"])
    compiled[skill_key] = {
        "moduleId": s_data["moduleId"],
        "moduleName": s_data["moduleName"],
        "lectureTitle": s_data["lectureTitle"],
        "storageFolder": s_data["storageFolder"],
        "themeColor": s_data["themeColor"],
        "themeBg": s_data["themeBg"],
        "badge": s_data["badge"],
        "desc": s_data["desc"],
        "episodes": []
    }

    for ep in s_data["episodes"]:
        file_path = os.path.join(folder_path, ep["file"])
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        sec, dur_str = get_duration(file_path)
        storage_fn = f"ep_{ep['ch']:02d}.mp3"
        audio_url = f"{SUPABASE_STORAGE_URL}/{s_data['storageFolder']}/{storage_fn}"

        ep_entry = {
            "episode": ep["ch"],
            "code": str(ep["ch"]),
            "title": ep["title"],
            "sub": ep["sub"],
            "localFile": ep["file"],
            "storageFileName": storage_fn,
            "audioUrl": audio_url,
            "durationSec": sec,
            "durationStr": dur_str
        }
        compiled[skill_key]["episodes"].append(ep_entry)
        print(f"  [{ep['ch']:02d}] {dur_str} | {ep['title'][:55]}...")

with open("scripts/ielts_premium_podcast_manifest.json", "w", encoding="utf-8") as out:
    json.dump(compiled, out, ensure_ascii=False, indent=2)

print("\nSaved manifest to scripts/ielts_premium_podcast_manifest.json!")
