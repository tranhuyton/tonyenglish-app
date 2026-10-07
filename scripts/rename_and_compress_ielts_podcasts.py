import os
import re
import sys
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"F:\Downloads\Chrome\IELTS Premium-studio"

folder_mappings = {
    "Writing Task 1": [
        (1, "14-Cấu trúc bất biến Dynamic Chart IELTS.mp3"),
        (2, "15-Tư duy logic viết Task 1 IELTS.mp3"),
        (3, "13-Cấu trúc bất biến IELTS Process.mp3"),
        (4, "16-Cách viết bài IELTS Outdoor Map.mp3"),
        (5, "12-Cách viết Indoor Map IELTS.mp3"),
        (6, "11-Chiến thuật viết Mixed Charts IELTS.mp3"),
    ],
    "Writing Task 2": [
        (1, "21-Chiến thuật viết Discussion Essay IELTS.mp3"),
        (2, "18-Công thức viết Opinion Essay IELTS.mp3"),
        (3, "19-Cấu trúc bất biến bài IELTS Writing.mp3"),
        (4, "20-Cấu trúc bất biến IELTS Writing.mp3"),
        (5, "17-Chiến thuật xử lý IELTS Two Part.mp3"),
    ],
    "Reading": [
        (1, "26-Bẫy True False Not Given IELTS.mp3"),
        (2, "22-Bẫy dạng điền từ IELTS Reading.mp3"),
        (3, "25-Tư duy định vị IELTS Reading.mp3"),
        (4, "24-Chiến thuật làm bài Matching Headings.mp3"),
        (5, "23-Phá bẫy Multiple Choice IELTS Reading.mp3"),
        (6, "27-Chiến thuật IELTS Reading trả lời ngắn.mp3"),
    ],
    "Listening": [
        (1, "31-Bẫy chữ cái và con số IELTS.mp3"),
        (2, "29-Bẫy Form Completion trong IELTS Listening.mp3"),
        (3, "28-Chiến thuật xử gọn IELTS Map Labelling.mp3"),
        (4, "35-Tháo bẫy Short Answer Questions IELTS.mp3"),
        (5, "30-Chiến thuật làm Diagram IELTS Listening.mp3"),
        (6, "34-Né bẫy IELTS Listening Completion.mp3"),
        (7, "33-Né bẫy trắc nghiệm IELTS Listening.mp3"),
        (8, "32-Thoát bẫy Matching trong IELTS Listening.mp3"),
        (9, "36-Chiến thuật làm bài Summary Completion IELTS.mp3"),
    ],
    "Speaking Part 2": [
        (1, "04-Bí quyết tả người IELTS Speaking.mp3"),
        (2, "08-Template Modern Flat cho IELTS Speaking.mp3"),
        (3, "05-Cấu trúc 4 giai đoạn IELTS Speaking.mp3"),
        (4, "07-Template Cuộc đua xe đạp IELTS Speaking.mp3"),
        (5, "02-Cấu trúc 4 bước Template Bái Đính.mp3"),
        (6, "10-Bản thiết kế Template 6 Thầy Tôn.mp3"),
        (7, "03-Cấu trúc 4 Stage Template Korean BBQ.mp3"),
        (8, "06-Cấu trúc 4 giai đoạn bài nói.mp3"),
        (9, "09-Template Speaking Cặp đôi hạnh phúc.mp3"),
        (10, "01-9 template bẻ lái Speaking Part 2.mp3"),
    ]
}

def clean_prefix(fname):
    return re.sub(r'^\d+[-_\s.]*', '', fname)

for folder, items in folder_mappings.items():
    folder_path = os.path.join(base_dir, folder)
    print(f"\n==========================================")
    print(f"Processing '{folder}' ({len(items)} files)...")
    print(f"==========================================")

    staging_dir = os.path.join(folder_path, "__renamed_staging__")
    os.makedirs(staging_dir, exist_ok=True)

    for num, src_fn in items:
        src_path = os.path.join(folder_path, src_fn)
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"Missing file: {src_path}")

        base_clean = clean_prefix(src_fn)
        dst_fn = f"{num:02d}-{base_clean}"
        dst_path = os.path.join(staging_dir, dst_fn)

        size_mb = os.path.getsize(src_path) / (1024 * 1024)
        print(f"[{num:02d}] {src_fn} ({size_mb:.1f} MB) -> {dst_fn}")

        if size_mb > 40.0:
            print(f"    Compressing {src_fn} ({size_mb:.1f} MB > 40 MB) to 160k MP3...")
            cmd = f'ffmpeg -i "{src_path}" -b:a 160k -y "{dst_path}" -loglevel error'
            subprocess.run(cmd, shell=True, check=True)
            comp_mb = os.path.getsize(dst_path) / (1024 * 1024)
            print(f"    Compressed successfully: {comp_mb:.1f} MB")
        else:
            shutil.copy2(src_path, dst_path)

    staged_files = [f for f in os.listdir(staging_dir) if f.endswith(".mp3")]
    if len(staged_files) != len(items):
        raise ValueError(f"Expected {len(items)} staged files, found {len(staged_files)}")

    # Remove old files in folder
    for num, src_fn in items:
        p = os.path.join(folder_path, src_fn)
        if os.path.exists(p):
            os.remove(p)

    # Move staged to folder
    for f in staged_files:
        shutil.move(os.path.join(staging_dir, f), os.path.join(folder_path, f))

    os.rmdir(staging_dir)
    print(f"Finished {folder}! All {len(items)} files renamed and compressed.")

print("\n🎉 ALL 36 IELTS PREMIUM AUDIO FILES PROCESSED SUCCESSFULLY!")
