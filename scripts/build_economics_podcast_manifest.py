import os
import sys
import json
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"F:\Downloads\Chrome\Economics podcast\Final"
vi_dir = os.path.join(base_dir, "Vietnamese")
en_dir = os.path.join(base_dir, "English")

chapters_meta = [
    # Section 1
    {"ch": 1, "sec": 1, "sec_name_en": "SECTION 1: The basic economic problem", "sec_name_vi": "PHẦN 1: Vấn đề kinh tế cơ bản", "topic_en": "The nature of the economic problem", "topic_vi": "Bản chất của vấn đề kinh tế", "sub_en": "Finite resources, infinite wants, and free goods", "sub_vi": "Nguồn lực hữu hạn, nhu cầu vô hạn và hàng hóa tự do"},
    {"ch": 2, "sec": 1, "sec_name_en": "SECTION 1: The basic economic problem", "sec_name_vi": "PHẦN 1: Vấn đề kinh tế cơ bản", "topic_en": "The factors of production", "topic_vi": "Các yếu tố sản xuất", "sub_en": "Land, labour, capital, enterprise and mobility", "sub_vi": "Đất đai, lao động, tư bản và doanh nhân"},
    {"ch": 3, "sec": 1, "sec_name_en": "SECTION 1: The basic economic problem", "sec_name_vi": "PHẦN 1: Vấn đề kinh tế cơ bản", "topic_en": "Opportunity cost", "topic_vi": "Chi phí cơ hội", "sub_en": "The definition and significance of opportunity cost", "sub_vi": "Định nghĩa và ý nghĩa của chi phí cơ hội"},
    {"ch": 4, "sec": 1, "sec_name_en": "SECTION 1: The basic economic problem", "sec_name_vi": "PHẦN 1: Vấn đề kinh tế cơ bản", "topic_en": "Production possibility curve", "topic_vi": "Đường giới hạn khả năng sản xuất PPC", "sub_en": "Definition, drawing and shifts in the PPC", "sub_vi": "Đường cong PPC, sự đánh đổi và dịch chuyển"},

    # Section 2
    {"ch": 5, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Microeconomics and macroeconomics", "topic_vi": "Kinh tế vi mô và kinh tế vĩ mô", "sub_en": "Decision makers, individual markets, and whole economies", "sub_vi": "Các chủ thể kinh tế, thị trường riêng lẻ và tổng thể nền kinh tế"},
    {"ch": 6, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "The role of markets in allocating resources", "topic_vi": "Vai trò của thị trường trong phân bổ nguồn lực", "sub_en": "The market mechanism and resource allocation", "sub_vi": "Cơ chế thị trường và phân bổ nguồn lực"},
    {"ch": 7, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Demand", "topic_vi": "Cầu thị trường", "sub_en": "Effective demand, price changes, and demand curves", "sub_vi": "Cầu hiệu dụng, tín hiệu giá và đường cầu"},
    {"ch": 8, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Supply", "topic_vi": "Cung thị trường", "sub_en": "Supply curves, price signals, and determinants of supply", "sub_vi": "Đường cung, tín hiệu giá và các yếu tố quyết định nguồn cung"},
    {"ch": 9, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Price determination", "topic_vi": "Xác định giá cả thị trường", "sub_en": "Market equilibrium, market clearing price, and shortages/surpluses", "sub_vi": "Cân bằng thị trường, mức giá cân bằng và dư thừa/thiếu hụt"},
    {"ch": 10, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Price changes", "topic_vi": "Sự biến động giá cả", "sub_en": "Causes and consequences of price changes, disequilibrium", "sub_vi": "Nguyên nhân và hệ quả của thay đổi giá, mất cân bằng thị trường"},
    {"ch": 11, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Price elasticity of demand", "topic_vi": "Độ co giãn của cầu theo giá (PED)", "sub_en": "Calculation, determinants, and significance of PED", "sub_vi": "Cách tính, các yếu tố quyết định và ý nghĩa của PED"},
    {"ch": 12, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Price elasticity of supply", "topic_vi": "Độ co giãn của cung theo giá (PES)", "sub_en": "Calculation, determinants, and significance of PES", "sub_vi": "Cách tính, các yếu tố quyết định và ý nghĩa của PES"},
    {"ch": 13, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Market economic system", "topic_vi": "Hệ thống kinh tế thị trường", "sub_en": "Features, advantages, and disadvantages of pure market economies", "sub_vi": "Đặc điểm, ưu điểm và nhược điểm của nền kinh tế thị trường tự do"},
    {"ch": 14, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Market failure", "topic_vi": "Thất bại của thị trường", "sub_en": "Causes, negative externalities, merit and demerit goods", "sub_vi": "Nguyên nhân, ngoại tác tiêu cực, hàng hóa công và ngoại tác"},
    {"ch": 15, "sec": 2, "sec_name_en": "SECTION 2: The allocation of resources", "sec_name_vi": "PHẦN 2: Phân bổ nguồn lực", "topic_en": "Mixed economic system", "topic_vi": "Hệ thống kinh tế hỗn hợp", "sub_en": "Public and private sectors, government intervention, and price controls", "sub_vi": "Khu vực công & tư, sự can thiệp của chính phủ và giá trần/giá sàn"},

    # Section 3
    {"ch": 16, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Money and banking", "topic_vi": "Tiền tệ và hệ thống ngân hàng", "sub_en": "Functions of money, central banks, and commercial banks", "sub_vi": "Chức năng của tiền tệ, ngân hàng trung ương và ngân hàng thương mại"},
    {"ch": 17, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Households", "topic_vi": "Hộ gia đình", "sub_en": "Influences on spending, saving, and borrowing", "sub_vi": "Các yếu tố ảnh hưởng tới tiêu dùng, tiết kiệm và vay nợ"},
    {"ch": 18, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Workers", "topic_vi": "Người lao động", "sub_en": "Factors affecting choice of occupation and wage determination", "sub_vi": "Yếu tố lựa chọn nghề nghiệp và xác định mức tiền lương"},
    {"ch": 19, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Trade unions", "topic_vi": "Công đoàn", "sub_en": "Roles, collective bargaining, and influence on wages", "sub_vi": "Vai trò của công đoàn, thương lượng tập thể và bảo vệ người lao động"},
    {"ch": 20, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Firms", "topic_vi": "Doanh nghiệp", "sub_en": "Classification of firms, economic sectors, and business size", "sub_vi": "Phân loại doanh nghiệp, các khu vực kinh tế và quy mô"},
    {"ch": 21, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Firms and production", "topic_vi": "Doanh nghiệp và sản xuất", "sub_en": "Labour-intensive vs capital-intensive, productivity, and economies of scale", "sub_vi": "Thâm dụng lao động vs vốn, năng suất và hiệu quả quy mô"},
    {"ch": 22, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Firms' costs, revenue and objectives", "topic_vi": "Chi phí, doanh thu và mục tiêu của doanh nghiệp", "sub_en": "Fixed, variable, average costs, total revenue, and profit", "sub_vi": "Định phí, biến phí, doanh thu và tối đa hóa lợi nhuận"},
    {"ch": 23, "sec": 3, "sec_name_en": "SECTION 3: Microeconomic decision makers", "sec_name_vi": "PHẦN 3: Các chủ thể quyết định vi mô", "topic_en": "Market structure", "topic_vi": "Cấu trúc thị trường", "sub_en": "Competitive markets, monopoly characteristics, and market power", "sub_vi": "Thị trường cạnh tranh hoàn hảo, độc quyền và sức mạnh thị trường"},

    # Section 4
    {"ch": 24, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "The role of government", "topic_vi": "Vai trò của chính phủ", "sub_en": "Government as producer, employer, and regulator", "sub_vi": "Chính phủ với vai trò nhà sản xuất, người sử dụng lao động và điều tiết kinh tế"},
    {"ch": 25, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "The macroeconomic aims of government", "topic_vi": "Các mục tiêu kinh tế vĩ mô của chính phủ", "sub_en": "Economic growth, low unemployment, price stability, and conflicts", "sub_vi": "Tăng trưởng kinh tế, giảm thất nghiệp, ổn định giá và xung đột mục tiêu"},
    {"ch": 26, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "Fiscal policy", "topic_vi": "Chính sách tài khóa", "sub_en": "Taxation, government spending, budget balance, and fiscal measures", "sub_vi": "Thuế, chi tiêu công, cân đối ngân sách và các biện pháp tài khóa"},
    {"ch": 27, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "Monetary policy", "topic_vi": "Chính sách tiền tệ", "sub_en": "Interest rates, money supply, exchange rates, and central bank tools", "sub_vi": "Lãi suất, cung tiền, tỷ giá và công cụ của ngân hàng trung ương"},
    {"ch": 28, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "Supply-side policy", "topic_vi": "Chính sách trọng cung", "sub_en": "Measures to increase productive capacity and aggregate supply", "sub_vi": "Các biện pháp gia tăng năng lực sản xuất và tổng cung"},
    {"ch": 29, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "Economic growth", "topic_vi": "Tăng trưởng kinh tế", "sub_en": "Measuring GDP, causes, consequences, and recession", "sub_vi": "Đo lường GDP, nguyên nhân, hệ quả tăng trưởng và suy thoái kinh tế"},
    {"ch": 30, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "Employment and unemployment", "topic_vi": "Việc làm và thất nghiệp", "sub_en": "Measurement, causes, types of unemployment, and policies", "sub_vi": "Đo lường, nguyên nhân, các dạng thất nghiệp và chính sách giải quyết"},
    {"ch": 31, "sec": 4, "sec_name_en": "SECTION 4: Government and the macro economy", "sec_name_vi": "PHẦN 4: Chính phủ và kinh tế vĩ mô", "topic_en": "Inflation and deflation", "topic_vi": "Lạm phát và giảm phát", "sub_en": "CPI measurement, causes of inflation, deflation, and consequences", "sub_vi": "Đo lường chỉ số CPI, nguyên nhân lạm phát, giảm phát và hệ quả"},

    # Section 5
    {"ch": 32, "sec": 5, "sec_name_en": "SECTION 5: Economic development", "sec_name_vi": "PHẦN 5: Phát triển kinh tế", "topic_en": "Living standards", "topic_vi": "Tiêu chuẩn mức sống", "sub_en": "Real GDP per capita, HDI, and limitations of measures", "sub_vi": "GDP bình quân đầu người thực tế, chỉ số phát triển con người HDI"},
    {"ch": 33, "sec": 5, "sec_name_en": "SECTION 5: Economic development", "sec_name_vi": "PHẦN 5: Phát triển kinh tế", "topic_en": "Poverty", "topic_vi": "Đói nghèo", "sub_en": "Absolute and relative poverty, causes, and alleviation policies", "sub_vi": "Nghèo tuyệt đối và tương đối, nguyên nhân và chính sách xóa đói giảm nghèo"},
    {"ch": 34, "sec": 5, "sec_name_en": "SECTION 5: Economic development", "sec_name_vi": "PHẦN 5: Phát triển kinh tế", "topic_en": "Population", "topic_vi": "Dân số", "sub_en": "Birth rates, death rates, migration, and dependency ratio", "sub_vi": "Tỷ lệ sinh, tử, di cư và tỷ lệ phụ thuộc dân số"},
    {"ch": 35, "sec": 5, "sec_name_en": "SECTION 5: Economic development", "sec_name_vi": "PHẦN 5: Phát triển kinh tế", "topic_en": "Differences in economic development between countries", "topic_vi": "Khác biệt về phát triển kinh tế giữa các quốc gia", "sub_en": "Developed vs developing economies, sectoral distribution, and disparities", "sub_vi": "Nền kinh tế phát triển và đang phát triển, cơ cấu ngành và chênh lệch"},

    # Section 6
    {"ch": 36, "sec": 6, "sec_name_en": "SECTION 6: International trade and globalisation", "sec_name_vi": "PHẦN 6: Thương mại quốc tế và toàn cầu hóa", "topic_en": "International specialisation", "topic_vi": "Chuyên môn hóa quốc tế", "sub_en": "Absolute and comparative advantage, benefits, and risks", "sub_vi": "Lợi thế tuyệt đối và so sánh, lợi ích và rủi ro của chuyên môn hóa"},
    {"ch": 37, "sec": 6, "sec_name_en": "SECTION 6: International trade and globalisation", "sec_name_vi": "PHẦN 6: Thương mại quốc tế và toàn cầu hóa", "topic_en": "Globalisation, free trade and protection", "topic_vi": "Toàn cầu hóa, tự do thương mại và bảo hộ", "sub_en": "Benefits of trade, tariffs, import quotas, and protectionism", "sub_vi": "Lợi ích thương mại, thuế quan, hạn ngạch và các rào cản bảo hộ"},
    {"ch": 38, "sec": 6, "sec_name_en": "SECTION 6: International trade and globalisation", "sec_name_vi": "PHẦN 6: Thương mại quốc tế và toàn cầu hóa", "topic_en": "Foreign exchange rates", "topic_vi": "Tỷ giá hối đoái", "sub_en": "Floating and fixed exchange rates, determination, and currency fluctuation", "sub_vi": "Tỷ giá thả nổi & cố định, cơ chế xác định và tác động biến động tiền tệ"},
    {"ch": 39, "sec": 6, "sec_name_en": "SECTION 6: International trade and globalisation", "sec_name_vi": "PHẦN 6: Thương mại quốc tế và toàn cầu hóa", "topic_en": "Current account of balance of payments", "topic_vi": "Cán cân vãng lai trong cán cân thanh toán", "sub_en": "Components of balance of payments, deficits, surpluses, and stability policies", "sub_vi": "Các thành phần cán cân thanh toán, thâm hụt, thặng dư và biện pháp điều chỉnh"}
]

def get_duration(filepath):
    cmd = f'ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{filepath}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    sec = int(float(res.stdout.strip()))
    m = sec // 60
    s = sec % 60
    return sec, f"{m}:{s:02d}"

def main():
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
            "audioUrlVi": f"{SUPABASE_STORAGE_URL}/audio/podcast/economics-0455/{storage_fn}",
            "audioUrlEn": f"{SUPABASE_STORAGE_URL}/audio/podcast/economics-0455-en/{storage_fn}",
            "durationViSec": dur_v_sec,
            "durationEnSec": dur_e_sec,
            "durationViStr": dur_v_str,
            "durationEnStr": dur_e_str
        }
        manifest.append(entry)
        print(f"[{ch:02d}] {m['topic_en']} | VI: {dur_v_str} | EN: {dur_e_str}")

    with open("scripts/economics_0455_podcast_manifest.json", "w", encoding="utf-8") as out:
        json.dump(manifest, out, ensure_ascii=False, indent=2)

    print("\nManifest saved successfully to scripts/economics_0455_podcast_manifest.json!")

if __name__ == "__main__":
    main()
