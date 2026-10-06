import os
import sys
import json
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"F:\Downloads\Chrome\Business podcast\Cambridge IGCSE and O Level Business Studies"
vi_dir = os.path.join(base_dir, "Vietnamese")
en_dir = os.path.join(base_dir, "English")

# Textbook sections and topics
chapters_meta = [
    # Section 1
    {"ch": 1, "sec": 1, "sec_name_en": "SECTION 1: Understanding business activity", "sec_name_vi": "PHẦN 1: Hiểu về hoạt động kinh doanh", "topic_en": "Business activity", "topic_vi": "Hoạt động kinh doanh", "sub_en": "Needs, wants, scarcity, opportunity cost, and adding value", "sub_vi": "Nhu cầu, sự khan hiếm, chi phí cơ hội và gia tăng giá trị"},
    {"ch": 2, "sec": 1, "sec_name_en": "SECTION 1: Understanding business activity", "sec_name_vi": "PHẦN 1: Hiểu về hoạt động kinh doanh", "topic_en": "Classification of businesses", "topic_vi": "Phân loại doanh nghiệp", "sub_en": "Primary, secondary, tertiary sectors; public vs private sectors", "sub_vi": "Khu vực kinh tế sơ cấp, thứ cấp, dịch vụ; công lập và tư nhân"},
    {"ch": 3, "sec": 1, "sec_name_en": "SECTION 1: Understanding business activity", "sec_name_vi": "PHẦN 1: Hiểu về hoạt động kinh doanh", "topic_en": "Enterprise, business growth and size", "topic_vi": "Khởi sự, tăng trưởng và quy mô doanh nghiệp", "sub_en": "Entrepreneurship, measuring business size, and methods of expansion", "sub_vi": "Khởi sự kinh doanh, đo lường quy mô và phương thức mở rộng"},
    {"ch": 4, "sec": 1, "sec_name_en": "SECTION 1: Understanding business activity", "sec_name_vi": "PHẦN 1: Hiểu về hoạt động kinh doanh", "topic_en": "Types of business organisation", "topic_vi": "Các loại hình tổ chức doanh nghiệp", "sub_en": "Sole traders, partnerships, limited companies, and joint ventures", "sub_vi": "Doanh nghiệp tư nhân, công ty hợp danh, công ty TNHH và cổ phần"},
    {"ch": 5, "sec": 1, "sec_name_en": "SECTION 1: Understanding business activity", "sec_name_vi": "PHẦN 1: Hiểu về hoạt động kinh doanh", "topic_en": "Business objectives and stakeholder objectives", "topic_vi": "Mục tiêu kinh doanh và mục tiêu của các bên liên quan", "sub_en": "Corporate goals, survival, profit, growth, and stakeholder conflicts", "sub_vi": "Mục tiêu doanh nghiệp, sinh tồn, lợi nhuận và xung đột lợi ích"},

    # Section 2
    {"ch": 6, "sec": 2, "sec_name_en": "SECTION 2: People in business", "sec_name_vi": "PHẦN 2: Con người trong doanh nghiệp", "topic_en": "Motivating employees", "topic_vi": "Tạo động lực cho nhân viên", "sub_en": "Motivation theories (Maslow, Taylor, Herzberg) and financial/non-financial incentives", "sub_vi": "Thuyết động lực (Maslow, Taylor, Herzberg) và chế độ đãi ngộ"},
    {"ch": 7, "sec": 2, "sec_name_en": "SECTION 2: People in business", "sec_name_vi": "PHẦN 2: Con người trong doanh nghiệp", "topic_en": "Organisation and management", "topic_vi": "Cơ cấu tổ chức và quản trị", "sub_en": "Organisational structures, chain of command, span of control, and leadership styles", "sub_vi": "Cơ cấu tổ chức, chuỗi mệnh lệnh, tầm hạn quản trị và phong cách lãnh đạo"},
    {"ch": 8, "sec": 2, "sec_name_en": "SECTION 2: People in business", "sec_name_vi": "PHẦN 2: Con người trong doanh nghiệp", "topic_en": "Recruitment, selection and training of employees", "topic_vi": "Tuyển dụng, chọn lọc và đào tạo nhân viên", "sub_en": "Recruitment processes, training methods, legal controls, and dismissal", "sub_vi": "Quy trình tuyển dụng, phương pháp đào tạo và quản lý rủi ro nhân sự"},
    {"ch": 9, "sec": 2, "sec_name_en": "SECTION 2: People in business", "sec_name_vi": "PHẦN 2: Con người trong doanh nghiệp", "topic_en": "Internal and external communication", "topic_vi": "Giao tiếp nội bộ và bên ngoài", "sub_en": "Communication channels, barriers to communication, and effective transmission", "sub_vi": "Kênh truyền thông, rào cản giao tiếp và cách truyền đạt thông điệp hiệu quả"},

    # Section 3
    {"ch": 10, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "Marketing, competition and the customer", "topic_vi": "Marketing, cạnh tranh và khách hàng", "sub_en": "Market orientation, mass vs niche marketing, and market segmentation", "sub_vi": "Định hướng thị trường, thị trường đại trà & ngách, và phân khúc khách hàng"},
    {"ch": 11, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "Market research", "topic_vi": "Nghiên cứu thị trường", "sub_en": "Primary and secondary research, quantitative vs qualitative data, and sampling", "sub_vi": "Nghiên cứu sơ cấp và thứ cấp, dữ liệu định lượng & định tính, và lấy mẫu"},
    {"ch": 12, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "The marketing mix: product", "topic_vi": "Marketing mix: Sản phẩm (Product)", "sub_en": "Product lifecycle, Boston Consulting Group matrix, packaging, and brand identity", "sub_vi": "Vòng đời sản phẩm, ma trận BCG, bao bì đóng gói và nhận diện thương hiệu"},
    {"ch": 13, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "The marketing mix: price", "topic_vi": "Marketing mix: Giá cả (Price)", "sub_en": "Cost-plus, penetration, skimming, dynamic, and psychological pricing strategies", "sub_vi": "Chiến lược định giá: cộng chi phí, thâm nhập, hớt váng và tâm lý học định giá"},
    {"ch": 14, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "The marketing mix: place", "topic_vi": "Marketing mix: Kênh phân phối (Place)", "sub_en": "Distribution channels, wholesalers, retailers, and direct-to-consumer logistics", "sub_vi": "Kênh phân phối, trung gian bán buôn, bán lẻ và hậu cần thương mại"},
    {"ch": 15, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "The marketing mix: promotion", "topic_vi": "Marketing mix: Xúc tiến thương mại (Promotion)", "sub_en": "Advertising, sales promotion, PR, sponsorships, and the promotional mix", "sub_vi": "Quảng cáo, khuyến mại, quan hệ công chúng (PR) và phối thức xúc tiến"},
    {"ch": 16, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "Technology and the marketing mix", "topic_vi": "Công nghệ và Marketing mix", "sub_en": "E-commerce, dynamic algorithmic pricing, and digital marketing strategies", "sub_vi": "Thương mại điện tử, định giá thuật toán động và tiếp thị số hóa"},
    {"ch": 17, "sec": 3, "sec_name_en": "SECTION 3: Marketing", "sec_name_vi": "PHẦN 3: Marketing", "topic_en": "Marketing strategy", "topic_vi": "Chiến lược Marketing toàn diện", "sub_en": "Developing marketing strategies, entering foreign markets, and legal consumer protections", "sub_vi": "Xây dựng chiến lược marketing, thâm nhập thị trường ngoại và luật bảo vệ người tiêu dùng"},

    # Section 4
    {"ch": 18, "sec": 4, "sec_name_en": "SECTION 4: Operations management", "sec_name_vi": "PHẦN 4: Quản trị vận hành", "topic_en": "Production of goods and services", "topic_vi": "Sản xuất hàng hóa và dịch vụ", "sub_en": "Lean production, Kaizen, JIT inventory, job/batch/flow methods, and productivity", "sub_vi": "Sản xuất tinh gọn, Kaizen, JIT, các phương thức sản xuất và năng suất lao động"},
    {"ch": 19, "sec": 4, "sec_name_en": "SECTION 4: Operations management", "sec_name_vi": "PHẦN 4: Quản trị vận hành", "topic_en": "Costs, scale of production and break-even analysis", "topic_vi": "Chi phí, quy mô sản xuất và phân tích hòa vốn", "sub_en": "Fixed vs variable costs, economies of scale, break-even charts, and margin of safety", "sub_vi": "Định phí và biến phí, tính kinh tế theo quy mô, biểu đồ hòa vốn và biên an toàn"},
    {"ch": 20, "sec": 4, "sec_name_en": "SECTION 4: Operations management", "sec_name_vi": "PHẦN 4: Quản trị vận hành", "topic_en": "Achieving quality production", "topic_vi": "Đạt chất lượng trong sản xuất", "sub_en": "Quality control, quality assurance, Total Quality Management (TQM), and ISO standards", "sub_vi": "Kiểm soát chất lượng (QC), đảm bảo chất lượng (QA) và Quản lý chất lượng toàn diện (TQM)"},
    {"ch": 21, "sec": 4, "sec_name_en": "SECTION 4: Operations management", "sec_name_vi": "PHẦN 4: Quản trị vận hành", "topic_en": "Location decisions", "topic_vi": "Quyết định địa điểm kinh doanh", "sub_en": "Factors influencing business location, relocation, and international offshoring", "sub_vi": "Các yếu tố ảnh hưởng tới vị trí nhà máy, văn phòng và xu hướng chuyển dịch địa điểm"},

    # Section 5
    {"ch": 22, "sec": 5, "sec_name_en": "SECTION 5: Financial information and financial decisions", "sec_name_vi": "PHẦN 5: Thông tin và quyết định tài chính", "topic_en": "Business finance: needs and sources", "topic_vi": "Tài chính doanh nghiệp: Nhu cầu và nguồn vốn", "sub_en": "Internal vs external financing, short-term vs long-term capital, and shares vs debt", "sub_vi": "Nguồn vốn nội bộ và bên ngoài, vốn ngắn hạn & dài hạn, vốn cổ phần và vay nợ"},
    {"ch": 23, "sec": 5, "sec_name_en": "SECTION 5: Financial information and financial decisions", "sec_name_vi": "PHẦN 5: Thông tin và quyết định tài chính", "topic_en": "Cash flow forecasting and working capital", "topic_vi": "Dự báo dòng tiền và vốn lưu động", "sub_en": "Cash flow forecasts, cash vs profit, managing working capital, and overcoming insolvencies", "sub_vi": "Lập dự báo dòng tiền, sự khác biệt giữa tiền mặt & lợi nhuận, và giải pháp thanh khoản"},
    {"ch": 24, "sec": 5, "sec_name_en": "SECTION 5: Financial information and financial decisions", "sec_name_vi": "PHẦN 5: Thông tin và quyết định tài chính", "topic_en": "Income statements", "topic_vi": "Báo cáo kết quả hoạt động kinh doanh", "sub_en": "Revenue, cost of sales, gross profit, operating profit, and net profit calculations", "sub_vi": "Doanh thu, giá vốn hàng bán, lợi nhuận gộp, chi phí hoạt động và lợi nhuận ròng"},
    {"ch": 25, "sec": 5, "sec_name_en": "SECTION 5: Financial information and financial decisions", "sec_name_vi": "PHẦN 5: Thông tin và quyết định tài chính", "topic_en": "Statement of financial position", "topic_vi": "Bảng cân đối kế toán (Balance Sheet)", "sub_en": "Non-current assets, current assets, current liabilities, and shareholder equity", "sub_vi": "Tài sản dài hạn, tài sản ngắn hạn, nợ phải trả và vốn chủ sở hữu"},
    {"ch": 26, "sec": 5, "sec_name_en": "SECTION 5: Financial information and financial decisions", "sec_name_vi": "PHẦN 5: Thông tin và quyết định tài chính", "topic_en": "Analysis of accounts", "topic_vi": "Phân tích báo cáo tài chính", "sub_en": "Profitability ratios (ROCE, gross/net margins) and liquidity ratios (current, acid test)", "sub_vi": "Tỷ số khả năng sinh lời (ROCE, biên lợi nhuận) và tỷ số thanh toán hiện hành, nhanh"},

    # Section 6
    {"ch": 27, "sec": 6, "sec_name_en": "SECTION 6: External influences on business issues", "sec_name_vi": "PHẦN 6: Ảnh hưởng bên ngoài tới hoạt động kinh doanh", "topic_en": "Economic issues", "topic_vi": "Các vấn đề kinh tế vĩ mô", "sub_en": "Economic growth, inflation, unemployment, balance of payments, and government policies", "sub_vi": "Tăng trưởng kinh tế, lạm phát, thất nghiệp, cán cân thanh toán và chính sách vĩ mô"},
    {"ch": 28, "sec": 6, "sec_name_en": "SECTION 6: External influences on business issues", "sec_name_vi": "PHẦN 6: Ảnh hưởng bên ngoài tới hoạt động kinh doanh", "topic_en": "Environmental and ethical issues", "topic_vi": "Các vấn đề môi trường và đạo đức kinh doanh", "sub_en": "Social costs and benefits, externalities, sustainable development, and corporate ethics", "sub_vi": "Chi phí & lợi ích xã hội, phát triển bền vững và đạo đức trách nhiệm xã hội (CSR)"},
    {"ch": 29, "sec": 6, "sec_name_en": "SECTION 6: External influences on business issues", "sec_name_vi": "PHẦN 6: Ảnh hưởng bên ngoài tới hoạt động kinh doanh", "topic_en": "Business and the international economy", "topic_vi": "Doanh nghiệp và nền kinh tế quốc tế", "sub_en": "Globalisation, multinational corporations, tariffs, quotas, and exchange rate impacts", "sub_vi": "Toàn cầu hóa, tập đoàn đa quốc gia, thuế quan, hạn ngạch và tác động của tỷ giá hối đoái"}
]

def get_duration(filepath):
    cmd = f'ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{filepath}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    sec = int(float(res.stdout.strip()))
    m = sec // 60
    s = sec % 60
    return sec, f"{m}:{s:02d}"

vi_files = {int(f[:2]): f for f in os.listdir(vi_dir) if f.endswith(".mp3")}
en_files = {int(f[:2]): f for f in os.listdir(en_dir) if f.endswith(".mp3")}

manifest = []

SUPABASE_STORAGE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/test_assets"

print("Reading durations and compiling manifest...")
for m in chapters_meta:
    ch = m["ch"]
    vf = vi_files[ch]
    ef = en_files[ch]

    v_path = os.path.join(vi_dir, vf)
    e_path = os.path.join(en_dir, ef)

    dur_v_sec, dur_v_str = get_duration(v_path)
    dur_e_sec, dur_e_str = get_duration(e_path)

    # Clean titles
    title_vi = vf.split('-', 1)[1].replace('.mp3', '').strip()
    title_en = ef.split('-', 1)[1].replace('.mp3', '').strip()

    storage_fn = f"ep_{ch:02d}.mp3"

    entry = {
        "episode": ch,
        "code": str(ch),
        "sectionNumber": m["sec"],
        "group": m["sec_name_en"],
        "groupVi": m["sec_name_vi"],
        "topic": m["topic_en"],
        "topicVi": m["topic_vi"],
        "syllabusTitle": m["sub_en"],
        "syllabusTitleVi": m["sub_vi"],
        "titleVi": title_vi,
        "titleEn": title_en,
        "fileNameVi": vf,
        "fileNameEn": ef,
        "storageFileName": storage_fn,
        "audioUrlVi": f"{SUPABASE_STORAGE_URL}/audio/podcast/business-0450/{storage_fn}",
        "audioUrlEn": f"{SUPABASE_STORAGE_URL}/audio/podcast/business-0450-en/{storage_fn}",
        "durationViSec": dur_v_sec,
        "durationEnSec": dur_e_sec,
        "durationViStr": dur_v_str,
        "durationEnStr": dur_e_str
    }
    manifest.append(entry)
    print(f"[{ch:02d}] {m['topic_en']} | VI: {dur_v_str} | EN: {dur_e_str}")

with open("scripts/business_0450_podcast_manifest.json", "w", encoding="utf-8") as out:
    json.dump(manifest, out, ensure_ascii=False, indent=2)

print("\nManifest saved successfully to scripts/business_0450_podcast_manifest.json!")
