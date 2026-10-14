import os
import sys
import json
import shutil
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"F:\Downloads\Chrome\Maths 0580 explainer\Audio"
VI_DIR = os.path.join(BASE_DIR, "Vietnamese")
EN_DIR = os.path.join(BASE_DIR, "English")

SUPABASE_PUBLIC_BASE = "https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets"

TOPICS_META = [
    {
        "episode": 1,
        "code": "1",
        "sectionNumber": 1,
        "group": "Topic 1: Number",
        "groupVi": "Chủ đề 1: Số học",
        "fileName": "Topic 1 Number.mp3",
        "storageFileName": "ep_01_number.mp3",
        "titleEn": "Topic 1: Number",
        "titleVi": "Chủ đề 1: Số học (Number)",
        "syllabusTitle": "Types of numbers, sets, powers & roots, fractions, decimals, percentages, standard form, estimation, bounds, ratio, proportion, rates & financial mathematics.",
        "syllabusTitleVi": "Phân loại số, tập hợp, lũy thừa & căn thức, phân số, thập phân, phần trăm, dạng chuẩn (Standard Form), làm tròn & giới hạn sai số (Bounds), tỉ lệ và toán tài chính."
    },
    {
        "episode": 2,
        "code": "2",
        "sectionNumber": 2,
        "group": "Topic 2: Algebra and graphs",
        "groupVi": "Chủ đề 2: Đại số & Đồ thị",
        "fileName": "Topic 2 Algebra and Graphs.mp3",
        "storageFileName": "ep_02_algebra_and_graphs.mp3",
        "titleEn": "Topic 2: Algebra and Graphs",
        "titleVi": "Chủ đề 2: Đại số và Đồ thị (Algebra & Graphs)",
        "syllabusTitle": "Algebraic manipulation, factorising, algebraic fractions, indices, linear & quadratic equations, inequalities, sequences, graphs of functions, differentiation & functions.",
        "syllabusTitleVi": "Biến đổi đại số, phân tích nhân tử, phân thức đại số, số mũ, phương trình bậc nhất & bậc hai, bất phương trình, dãy số, đồ thị hàm số, đạo hàm và hàm hợp/hàm ngược."
    },
    {
        "episode": 3,
        "code": "3",
        "sectionNumber": 3,
        "group": "Topic 3: Coordinate geometry",
        "groupVi": "Chủ đề 3: Hình học Tọa độ",
        "fileName": "Topic 3 Coordinate Geometry.mp3",
        "storageFileName": "ep_03_coordinate_geometry.mp3",
        "titleEn": "Topic 3: Coordinate Geometry",
        "titleVi": "Chủ đề 3: Hình học Tọa độ (Coordinate Geometry)",
        "syllabusTitle": "Cartesian coordinates, gradient of linear graphs, length & midpoint of a line segment, equation of straight lines (y = mx + c), parallel and perpendicular lines.",
        "syllabusTitleVi": "Hệ tọa độ Descartes, hệ số góc (Gradient), độ dài và trung điểm đoạn thẳng, phương trình đường thẳng (y = mx + c), hai đường thẳng song song và vuông góc."
    },
    {
        "episode": 4,
        "code": "4",
        "sectionNumber": 4,
        "group": "Topic 4: Geometry",
        "groupVi": "Chủ đề 4: Hình học Phẳng",
        "fileName": "Topic 4 Geometry.mp3",
        "storageFileName": "ep_04_geometry.mp3",
        "titleEn": "Topic 4: Geometry",
        "titleVi": "Chủ đề 4: Hình học Phẳng (Geometry)",
        "syllabusTitle": "Geometrical terms, constructions, scale drawings, similarity & congruence, symmetry, angles in polygons, parallel lines, circle theorems & loci.",
        "syllabusTitleVi": "Thuật ngữ hình học, dựng hình, bản vẽ tỉ lệ, đồng dạng & bằng nhau, đối xứng, góc trong đa giác, các định lý hình tròn (Circle Theorems) và quỹ tích."
    },
    {
        "episode": 5,
        "code": "5",
        "sectionNumber": 5,
        "group": "Topic 5: Mensuration",
        "groupVi": "Chủ đề 5: Đo lường Hình học",
        "fileName": "Topic 5 Mensuration.mp3",
        "storageFileName": "ep_05_mensuration.mp3",
        "titleEn": "Topic 5: Mensuration",
        "titleVi": "Chủ đề 5: Đo lường Hình học (Mensuration)",
        "syllabusTitle": "Units of measure, perimeter & area of 2D shapes, arc length & sector area, surface area & volume of 3D solids (prisms, cylinders, pyramids, cones, spheres) & compound shapes.",
        "syllabusTitleVi": "Đơn vị đo lường, chu vi & diện tích hình phẳng 2D, độ dài cung & diện tích hình quạt, diện tích bề mặt & thể tích khối 3D (lăng trụ, trụ, chóp, nón, cầu) và hình ghép."
    },
    {
        "episode": 6,
        "code": "6",
        "sectionNumber": 6,
        "group": "Topic 6: Trigonometry",
        "groupVi": "Chủ đề 6: Lượng giác",
        "fileName": "Topic 6 Trigonometry.mp3",
        "storageFileName": "ep_06_trigonometry.mp3",
        "titleEn": "Topic 6: Trigonometry",
        "titleVi": "Chủ đề 6: Lượng giác (Trigonometry)",
        "syllabusTitle": "Pythagoras' theorem, right-angled triangle ratios (SOH CAH TOA), bearings, exact trigonometric values, trigonometric graphs, sine & cosine rules, area of triangle & 3D trigonometry.",
        "syllabusTitleVi": "Định lý Pythagoras, tỉ số lượng giác tam giác vuông (SOH CAH TOA), góc phương vị (Bearings), đồ thị lượng giác, định lý Sin & Cosin, diện tích tam giác và lượng giác không gian 3D."
    },
    {
        "episode": 7,
        "code": "7",
        "sectionNumber": 7,
        "group": "Topic 7: Vectors and transformation",
        "groupVi": "Chủ đề 7: Vectơ & Biến hình",
        "fileName": "Topic 7 Vectors and Transformations.mp3",
        "storageFileName": "ep_07_vectors_and_transformations.mp3",
        "titleEn": "Topic 7: Vectors and Transformations",
        "titleVi": "Chủ đề 7: Vectơ và Phép biến hình (Vectors & Transformations)",
        "syllabusTitle": "Vectors in 2D, column vectors, magnitude of a vector, vector geometry, position vectors, and geometric transformations (reflection, rotation, translation, enlargement).",
        "syllabusTitleVi": "Vectơ trong mặt phẳng 2D, vectơ cột, độ lớn của vectơ, hình học vectơ, vectơ vị trí và 4 phép biến hình (đối xứng trục, quay, tịnh tiến, vị tự/phóng to thu nhỏ)."
    },
    {
        "episode": 8,
        "code": "8",
        "sectionNumber": 8,
        "group": "Topic 8: Probability",
        "groupVi": "Chủ đề 8: Xác suất",
        "fileName": "Topic 8 Probability.mp3",
        "storageFileName": "ep_08_probability.mp3",
        "titleEn": "Topic 8: Probability",
        "titleVi": "Chủ đề 8: Xác suất (Probability)",
        "syllabusTitle": "Probability scale, relative & expected frequency, mutually exclusive & independent events, combined events, sample space diagrams, Venn diagrams & tree diagrams.",
        "syllabusTitleVi": "Thang đo xác suất, tần suất tương đối & kỳ vọng, biến cố xung khắc & độc lập, biến cố hợp, bảng không gian mẫu, biểu đồ Venn và sơ đồ hình cây (Tree Diagrams)."
    },
    {
        "episode": 9,
        "code": "9",
        "sectionNumber": 9,
        "group": "Topic 9: Statistic",
        "groupVi": "Chủ đề 9: Thống kê",
        "fileName": "Topic 9 Statistics.mp3",
        "storageFileName": "ep_09_statistics.mp3",
        "titleEn": "Topic 9: Statistics",
        "titleVi": "Chủ đề 9: Thống kê (Statistics)",
        "syllabusTitle": "Classifying & tabulating data, mean, median, mode & range, grouped data, scatter diagrams, cumulative frequency, box-and-whisker plots & histograms.",
        "syllabusTitleVi": "Phân loại bảng dữ liệu, số trung bình (Mean), trung vị (Median), mốt (Mode), khoảng biến thiên, biểu đồ tán xạ (Scatter), tần số tích lũy, biểu đồ hộp (Box Plot) và mật độ tần số (Histogram)."
    }
]

def get_duration(path):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', path]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    dur = int(round(float(json.loads(res.stdout)['format']['duration'])))
    m, s = divmod(dur, 60)
    return dur, f"{m}:{s:02d}"

def ensure_compressed(file_path, max_mb=15.0):
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if size_mb > max_mb:
        print(f"  [Compress] {os.path.basename(file_path)} ({size_mb:.1f} MB > {max_mb} MB) -> 80k mono MP3...")
        tmp_path = file_path + ".tmp.mp3"
        cmd = f'ffmpeg -i "{file_path}" -ac 1 -b:a 80k -y "{tmp_path}" -loglevel error'
        subprocess.run(cmd, shell=True, check=True)
        shutil.move(tmp_path, file_path)
        new_mb = os.path.getsize(file_path) / (1024 * 1024)
        print(f"  [Done] Compressed to {new_mb:.1f} MB")

manifest = []
for meta in TOPICS_META:
    fn = meta["fileName"]
    vi_path = os.path.join(VI_DIR, fn)
    en_path = os.path.join(EN_DIR, fn)

    if not os.path.exists(vi_path):
        raise FileNotFoundError(f"Missing VI file: {vi_path}")
    if not os.path.exists(en_path):
        raise FileNotFoundError(f"Missing EN file: {en_path}")

    print(f"Processing Episode {meta['episode']}: {fn}")
    ensure_compressed(vi_path)
    ensure_compressed(en_path)

    dur_vi_sec, dur_vi_str = get_duration(vi_path)
    dur_en_sec, dur_en_str = get_duration(en_path)

    storage_fn = meta["storageFileName"]
    manifest.append({
        "episode": meta["episode"],
        "code": meta["code"],
        "sectionNumber": meta["sectionNumber"],
        "group": meta["group"],
        "groupVi": meta["groupVi"],
        "topic": meta["titleEn"],
        "topicVi": meta["titleVi"],
        "syllabusTitle": meta["syllabusTitle"],
        "syllabusTitleVi": meta["syllabusTitleVi"],
        "titleEn": meta["titleEn"],
        "titleVi": meta["titleVi"],
        "fileNameVi": fn,
        "fileNameEn": fn,
        "storageFileName": storage_fn,
        "audioUrlVi": f"{SUPABASE_PUBLIC_BASE}/audio/podcast/maths-0580/{storage_fn}",
        "audioUrlEn": f"{SUPABASE_PUBLIC_BASE}/audio/podcast/maths-0580-en/{storage_fn}",
        "durationViSec": dur_vi_sec,
        "durationViStr": dur_vi_str,
        "durationEnSec": dur_en_sec,
        "durationEnStr": dur_en_str
    })

out_path = "scripts/maths_0580_podcast_manifest.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(manifest)} episodes to {out_path}!")
