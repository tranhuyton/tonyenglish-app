import os
import re
import sys
import subprocess
import shutil

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"F:\Downloads\Chrome\Economics podcast\Final"
en_dir = os.path.join(base_dir, "English")
vi_dir = os.path.join(base_dir, "Vietnamese")

# 39 Chapters definition: (num, book_title, en_file, vi_file)
chapters = [
    # Section 1: The basic economic problem
    (1, "The nature of the economic problem", "25-Finite Resources and Infinite Human Wants.mp3", "02-Sự thật về hàng hóa miễn phí.mp3"),
    (2, "The factors of production", "37-How Factors of Production Shape the Economy.mp3", "04-Bản chất bốn yếu tố sản xuất.mp3"),
    (3, "Opportunity cost", "33-The Hidden Cost of Every Choice.mp3", "39-Khan hiếm và chi phí cơ hội.mp3"),
    (4, "Production possibility curve", "28-Opportunity Cost and the Production Possibility Curve.mp3", "01-Sự đánh đổi trên đường PPC.mp3"),
    # Section 2: The allocation of resources
    (5, "Microeconomics and macroeconomics", "36-How Micro and Macroeconomics Really Work.mp3", "03-Kinh tế vi mô và vĩ mô.mp3"),
    (6, "The role of markets in allocating resources", "35-How Prices Balance Supply and Demand.mp3", "26-Nền kinh tế không cần bếp trưởng.mp3"),
    (7, "Demand", "27-The Mechanics of Effective Demand.mp3", "15-Ai đang thao túng nhu cầu.mp3"),
    (8, "Supply", "15-How Price Signals Drive Economic Supply.mp3", "05-Sức mạnh độ co giãn nguồn cung.mp3"),
    (9, "Price determination", "23-How Supply and Demand Set Prices.mp3", "37-Sự thật đằng sau mỗi nhãn giá.mp3"),
    (10, "Price changes", "11-How Supply and Demand Drive Prices.mp3", "12-Tín hiệu giá và độ co giãn.mp3"),
    (11, "Price elasticity of demand", "31-How Companies Weaponize Price Elasticity.mp3", "36-Độ co giãn cầu trong định giá.mp3"),
    (12, "Price elasticity of supply", "16-Why Price Elasticity Makes Housing Skyrocket.mp3", "38-Độ co giãn nguồn cung PES.mp3"),
    (13, "Market economic system", "20-How Pure Free Markets Really Work.mp3", "24-Cơ chế giá chi phối thị trường.mp3"),
    (14, "Market failure", "12-The Hidden Costs of Market Failure.mp3", "25-Vì sao thị trường thất bại.mp3"),
    (15, "Mixed economic system", "26-The Mechanics of Mixed Economies.mp3", "14-Kinh tế hỗn hợp trong thực tế.mp3"),
    # Section 3: Microeconomic decision makers
    (16, "Money and banking", "01-How Banks Actually Create Money.mp3", "13-Cách ngân hàng nhân bản tiền.mp3"),
    (17, "Households", "03-How Macroeconomics Shapes Household Budgets.mp3", "09-Khi tiết kiệm bóp nghẹt kinh tế.mp3"),
    (18, "Workers", "30-Why Farmers Earn Less Than Bankers.mp3", "08-Yếu tố quyết định mức lương.mp3"),
    (19, "Trade unions", "24-How Trade Unions Wield Economic Power.mp3", "31-Sức mạnh kinh tế của công đoàn.mp3"),
    (20, "Firms", "34-How Businesses Scale Across Economic Sectors.mp3", "32-Logic đằng sau quyết định kinh doanh.mp3"),
    (21, "Firms and production", "29-Why Factories Choose Humans Over Robots.mp3", "23-Bài toán kinh tế trong sản xuất.mp3"),
    (22, "Firms' costs, revenue and objectives", "39-Why High Revenue Doesn't Guarantee Profit.mp3", "17-Chi phí doanh thu và lợi nhuận.mp3"),
    (23, "Market structure", "22-From Wet Markets to Corporate Monopolies.mp3", "21-Đế chế độc quyền khóa kéo YKK.mp3"),
    # Section 4: Government and the macro economy
    (24, "The role of government", "09-Why Governments Cannot Fix The Economy.mp3", "16-Cách chính phủ điều hành kinh tế.mp3"),
    (25, "The macroeconomic aims of government", "04-The Math Behind Government Spending Choices.mp3", "29-Nghệ thuật đánh đổi vĩ mô.mp3"),
    (26, "Fiscal policy", "13-How Fiscal Policy Shapes the Economy.mp3", "11-Bàn cờ chính sách tài khóa.mp3"),
    (27, "Monetary policy", "38-How Central Banks Control the Economy.mp3", "34-Cách chính sách tiền tệ vận hành.mp3"),
    (28, "Supply-side policy", "19-How Supply Side Policy Expands Economic Capacity.mp3", "20-Chính sách trọng cung và tăng trưởng.mp3"),
    (29, "Economic growth", "18-Why GDP Growth Can Be Misleading.mp3", "22-Bản chất của tăng trưởng kinh tế.mp3"),
    (30, "Employment and unemployment", "06-How Governments Measure and Fix Unemployment.mp3", "27-Góc khuất con số thất nghiệp.mp3"),
    (31, "Inflation and deflation", "07-How Inflation Erases Your Debt.mp3", "06-Bản chất lạm phát và giảm phát.mp3"),
    # Section 5: Economic development
    (32, "Living standards", "08-Why GDP Misrepresents Living Standards.mp3", "19-Mức sống không chỉ là GDP.mp3"),
    (33, "Poverty", "32-Absolute and Relative Poverty in Economics.mp3", "18-Cơ chế kinh tế của nghèo đói.mp3"),
    (34, "Population", "17-When Nations Run Out of Workers.mp3", "33-Bài toán dân số tối ưu.mp3"),
    (35, "Differences in economic development between countries", "02-Why Wealth Does Not Equal Development.mp3", "10-GDP tăng sao dân vẫn nghèo.mp3"),
    # Section 6: International trade and globalisation
    (36, "International specialisation", "10-Why Nations Bet Everything on One Industry.mp3", "28-Cạm bãy chuyên môn hóa quốc tế.mp3".replace("bãy", "bẫy")),
    (37, "Globalisation, free trade and protection", "05-How Free Trade and Tariffs Work.mp3", "35-Sự giằng co thương mại toàn cầu.mp3"),
    (38, "Foreign exchange rates", "21-How Foreign Exchange Rates Shape Economies.mp3", "30-Tỷ giá hối đoái và túi tiền.mp3"),
    (39, "Current account of balance of payments", "14-How Current Accounts Shape Global Wealth.mp3", "07-Nghịch lý tài khoản vãng lai.mp3"),
]

def clean_name(filename):
    # Remove leading number and hyphen/spaces: e.g. "25-Finite..." -> "Finite..."
    name = re.sub(r'^\d+[-_\s.]*', '', filename)
    return name

def process_language(lang_name, folder_path, file_tuples):
    print(f"\n==========================================")
    print(f"Processing {lang_name} in {folder_path}")
    print(f"==========================================")
    
    # Create a staging folder
    staging_dir = os.path.join(folder_path, "__renamed_staging__")
    os.makedirs(staging_dir, exist_ok=True)
    
    # Process each file to staging
    for num, book_title, src_filename in file_tuples:
        src_path = os.path.join(folder_path, src_filename)
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"Source file not found: {src_path}")
        
        base_clean = clean_name(src_filename)
        new_filename = f"{num:02d}-{base_clean}"
        dst_path = os.path.join(staging_dir, new_filename)
        
        file_size_mb = os.path.getsize(src_path) / (1024 * 1024)
        print(f"[{num:02d}] {src_filename} ({file_size_mb:.1f} MB) -> {new_filename}")
        
        # If file is > 42 MB, compress using ffmpeg to 160k
        if file_size_mb > 42.0:
            print(f"    Compressing {src_filename} ({file_size_mb:.1f} MB > 42 MB) to 160k MP3...")
            cmd = f'ffmpeg -i "{src_path}" -b:a 160k -y "{dst_path}" -loglevel error'
            subprocess.run(cmd, shell=True, check=True)
            compressed_mb = os.path.getsize(dst_path) / (1024 * 1024)
            print(f"    Compressed successfully: {compressed_mb:.1f} MB")
        else:
            shutil.copy2(src_path, dst_path)
            
    # Now verify all 39 files are in staging
    staged_files = [f for f in os.listdir(staging_dir) if f.endswith(".mp3")]
    if len(staged_files) != 39:
        raise ValueError(f"Expected 39 staged files, found {len(staged_files)}")
        
    # Remove original mp3 files in folder_path
    for num, book_title, src_filename in file_tuples:
        p = os.path.join(folder_path, src_filename)
        if os.path.exists(p):
            os.remove(p)
            
    # Move staged files to folder_path
    for f in staged_files:
        shutil.move(os.path.join(staging_dir, f), os.path.join(folder_path, f))
        
    os.rmdir(staging_dir)
    print(f"Finished {lang_name}! 39 files renamed and compressed.")

# Build tuples for EN and VI
en_tuples = [(c[0], c[1], c[2]) for c in chapters]
vi_tuples = [(c[0], c[1], c[3]) for c in chapters]

# Execute
process_language("English", en_dir, en_tuples)
process_language("Vietnamese", vi_dir, vi_tuples)

print("\nALL 78 FILES SUCCESSFULLY PROCESSED, RENAMED AND COMPRESSED!")
