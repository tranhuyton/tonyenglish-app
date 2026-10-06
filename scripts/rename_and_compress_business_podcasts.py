import os
import sys
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"F:\Downloads\Chrome\Business podcast\Cambridge IGCSE and O Level Business Studies"
vi_dir = os.path.join(base_dir, "Vietnamese")
en_dir = os.path.join(base_dir, "English")

# Mapping: chapter number (1..29) -> original filename
vi_mapping = {
    1: "01-Tại sao in tiền không xóa nghèo.mp3",
    2: "29-Phân loại doanh nghiệp trong kinh tế.mp3",
    3: "12-Doanh nghiệp bonsai hay tập đoàn.mp3",
    4: "16-Cấu trúc pháp lý của doanh nghiệp.mp3",
    5: "28-Lợi nhuận hay trách nhiệm xã hội.mp3",
    6: "15-Tiền không mua được sự tận tâm.mp3",
    7: "06-Dòng chảy quyền lực trong doanh nghiệp.mp3",
    8: "20-Bài toán rủi ro nhân sự.mp3",
    9: "08-Ảo giác đã gửi là đã hiểu.mp3",
    10: "17-Marketing không phải chiếc loa phóng thanh.mp3",
    11: "22-Cách doanh nghiệp đọc vị khách hàng.mp3",
    12: "21-Toan tính chiến lược sản phẩm.mp3",
    13: "04-Nghệ thuật định giá sản phẩm.mp3",
    14: "11-Chiến lược chọn kênh phân phối.mp3",
    15: "10-Chiến lược xúc tiến thương mại.mp3",
    16: "19-Mô hình 4P thời thuật toán.mp3",
    17: "26-Bàn mixer chiến lược marketing.mp3",
    18: "13-Sản xuất tinh gọn và năng suất.mp3",
    19: "02-Phép toán sinh tồn của doanh nghiệp.mp3",
    20: "18-Chất lượng từ QC đến TQM.mp3",
    21: "03-Ván cờ chọn địa điểm kinh doanh.mp3",
    22: "23-Đông khách nhưng vẫn phá sản.mp3",
    23: "24-Tại sao có lãi vẫn phá sản.mp3",
    24: "27-Vì sao có lãi vẫn phá sản.mp3",
    25: "09-Sự thật Bảng cân đối kế toán.mp3",
    26: "07-Sự thật sau con số lợi nhuận.mp3",
    27: "25-Bắt mạch vĩ mô để sinh tồn.mp3",
    28: "14-Cái giá đắt của đồ giá rẻ.mp3",
    29: "05-Sự thật đằng sau giá hàng hóa.mp3"
}

en_mapping = {
    1: "02-How Businesses Create Value From Scarcity.mp3",
    2: "20-How Economic Sectors and Ownership Work.mp3",
    3: "18-Why Scaling Can Destroy Your Business.mp3",
    4: "14-How business structures balance risk and capital.mp3",
    5: "26-How stakeholder conflicts shape business goals.mp3",
    6: "19-Why Money Doesn't Actually Motivate Workers.mp3",
    7: "24-How Corporate Hierarchies Actually Work.mp3",
    8: "08-The Hidden Machinery of Corporate HR.mp3",
    9: "28-How Business Communication Breaks Down.mp3",
    10: "03-How Companies Segment and Target You.mp3",
    11: "06-How Businesses Map Consumer Desires.mp3",
    12: "22-The Science of Product Survival.mp3",
    13: "10-The Hidden Psychology of Product Pricing.mp3",
    14: "21-How Product Distribution Channels Actually Work.mp3",
    15: "09-Why Good Products Never Sell Themselves.mp3",
    16: "23-How Algorithmic Pricing Targets Your Wallet.mp3",
    17: "29-Why Nokia Failed and Nike Succeeded.mp3",
    18: "16-The Hidden Mechanics of Modern Manufacturing.mp3",
    19: "25-The Hidden Math of Corporate Survival.mp3",
    20: "17-What Quality Means in Business Operations.mp3",
    21: "11-The Hidden Logic Of Business Geography.mp3",
    22: "05-Funding Business Growth Without Losing Control.mp3",
    23: "27-Why Profitable Businesses Go Bankrupt.mp3",
    24: "01-How Profitable Companies Go Bankrupt.mp3",
    25: "12-Why Profitable Companies Go Bankrupt.mp3",
    26: "07-Why Profitable Companies Go Bankrupt.mp3",
    27: "04-How Macroeconomics Dictates Business Survival.mp3",
    28: "15-Who Really Pays for Corporate Profit.mp3",
    29: "13-How Tariffs, Multinationals, and Exchange Rates Work.mp3"
}

def clean_base_name(filename):
    # Strip leading digits and hyphens/spaces
    # e.g. "01-Tại sao..." -> "Tại sao..."
    # e.g. "14-How business..." -> "How business..."
    parts = filename.split('-', 1)
    if len(parts) > 1 and parts[0].strip().isdigit():
        return parts[1].strip()
    return filename

def process_folder(folder_path, mapping, lang_code):
    print(f"\n================ Processing {lang_code.upper()} ================")
    # Step 1: Verify all files exist
    for ch, orig in mapping.items():
        p = os.path.join(folder_path, orig)
        if not os.path.exists(p):
            print(f"ERROR: Missing file {orig} in {folder_path}!")
            return False

    # Step 2: Check sizes and compress if > 45MB
    for ch, orig in mapping.items():
        p = os.path.join(folder_path, orig)
        sz_mb = os.path.getsize(p) / (1024 * 1024)
        if sz_mb > 45:
            print(f"Compressing large file (>45MB): {orig} ({sz_mb:.2f} MB)...")
            tmp_out = p + ".comp.mp3"
            cmd = f'ffmpeg -i "{p}" -b:a 192k -y "{tmp_out}" -loglevel error'
            subprocess.run(cmd, shell=True, check=True)
            new_sz = os.path.getsize(tmp_out) / (1024 * 1024)
            print(f"Compressed from {sz_mb:.2f} MB to {new_sz:.2f} MB.")
            os.remove(p)
            os.rename(tmp_out, p)

    # Step 3: Rename to temporary names to avoid collision
    temp_names = {}
    for ch, orig in mapping.items():
        base = clean_base_name(orig)
        tmp_name = f"__temp_{ch:02d}__{base}"
        src = os.path.join(folder_path, orig)
        dst = os.path.join(folder_path, tmp_name)
        os.rename(src, dst)
        temp_names[ch] = (tmp_name, f"{ch:02d}-{base}")

    # Step 4: Rename to final names
    for ch, (tmp_name, final_name) in temp_names.items():
        src = os.path.join(folder_path, tmp_name)
        dst = os.path.join(folder_path, final_name)
        os.rename(src, dst)
        print(f"Ch {ch:02d} -> {final_name}")

    print(f"Successfully renamed all 29 files in {folder_path}!")
    return True

ok_vi = process_folder(vi_dir, vi_mapping, "vi")
ok_en = process_folder(en_dir, en_mapping, "en")

if ok_vi and ok_en:
    print("\nALL 58 FILES SUCCESSFULLY COMPRESSED & RENAMED!")
