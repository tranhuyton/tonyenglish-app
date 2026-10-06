import os
import sys

base_dir = r"F:\Downloads\Chrome\Economics podcast\Final"
en_dir = os.path.join(base_dir, "English")
vi_dir = os.path.join(base_dir, "Vietnamese")

chapters = [
    # Section 1
    (1, "The nature of the economic problem", "25-Finite Resources and Infinite Human Wants.mp3", "02-Sự thật về hàng hóa miễn phí.mp3"),
    (2, "The factors of production", "37-How Factors of Production Shape the Economy.mp3", "04-Bản chất bốn yếu tố sản xuất.mp3"),
    (3, "Opportunity cost", "33-The Hidden Cost of Every Choice.mp3", "39-Khan hiếm và chi phí cơ hội.mp3"),
    (4, "Production possibility curve", "28-Opportunity Cost and the Production Possibility Curve.mp3", "01-Sự đánh đổi trên đường PPC.mp3"),
    # Section 2
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
    # Section 3
    (16, "Money and banking", "01-How Banks Actually Create Money.mp3", "13-Cách ngân hàng nhân bản tiền.mp3"),
    (17, "Households", "03-How Macroeconomics Shapes Household Budgets.mp3", "09-Khi tiết kiệm bóp nghẹt kinh tế.mp3"),
    (18, "Workers", "30-Why Farmers Earn Less Than Bankers.mp3", "08-Yếu tố quyết định mức lương.mp3"),
    (19, "Trade unions", "24-How Trade Unions Wield Economic Power.mp3", "31-Sức mạnh kinh tế của công đoàn.mp3"),
    (20, "Firms", "34-How Businesses Scale Across Economic Sectors.mp3", "32-Logic đằng sau quyết định kinh doanh.mp3"),
    (21, "Firms and production", "29-Why Factories Choose Humans Over Robots.mp3", "23-Bài toán kinh tế trong sản xuất.mp3"),
    (22, "Firms' costs, revenue and objectives", "39-Why High Revenue Doesn't Guarantee Profit.mp3", "17-Chi phí doanh thu và lợi nhuận.mp3"),
    (23, "Market structure", "22-From Wet Markets to Corporate Monopolies.mp3", "21-Đế chế độc quyền khóa kéo YKK.mp3"),
    # Section 4
    (24, "The role of government", "09-Why Governments Cannot Fix The Economy.mp3", "16-Cách chính phủ điều hành kinh tế.mp3"),
    (25, "The macroeconomic aims of government", "04-The Math Behind Government Spending Choices.mp3", "29-Nghệ thuật đánh đổi vĩ mô.mp3"),
    (26, "Fiscal policy", "13-How Fiscal Policy Shapes the Economy.mp3", "11-Bàn cờ chính sách tài khóa.mp3"),
    (27, "Monetary policy", "38-How Central Banks Control the Economy.mp3", "34-Cách chính sách tiền tệ vận hành.mp3"),
    (28, "Supply-side policy", "19-How Supply Side Policy Expands Economic Capacity.mp3", "20-Chính sách trọng cung và tăng trưởng.mp3"),
    (29, "Economic growth", "18-Why GDP Growth Can Be Misleading.mp3", "22-Bản chất của tăng trưởng kinh tế.mp3"),
    (30, "Employment and unemployment", "06-How Governments Measure and Fix Unemployment.mp3", "27-Góc khuất con số thất nghiệp.mp3"),
    (31, "Inflation and deflation", "07-How Inflation Erases Your Debt.mp3", "06-Bản chất lạm phát và giảm phát.mp3"),
    # Section 5
    (32, "Living standards", "08-Why GDP Misrepresents Living Standards.mp3", "19-Mức sống không chỉ là GDP.mp3"),
    (33, "Poverty", "32-Absolute and Relative Poverty in Economics.mp3", "18-Cơ chế kinh tế của nghèo đói.mp3"),
    (34, "Population", "17-When Nations Run Out of Workers.mp3", "33-Bài toán dân số tối ưu.mp3"),
    (35, "Differences in economic development between countries", "02-Why Wealth Does Not Equal Development.mp3", "10-GDP tăng sao dân vẫn nghèo.mp3"),
    # Section 6
    (36, "International specialisation", "10-Why Nations Bet Everything on One Industry.mp3", "28-Cạm bẫy chuyên môn hóa quốc tế.mp3"),
    (37, "Globalisation, free trade and protection", "05-How Free Trade and Tariffs Work.mp3", "35-Sự giằng co thương mại toàn cầu.mp3"),
    (38, "Foreign exchange rates", "21-How Foreign Exchange Rates Shape Economies.mp3", "30-Tỷ giá hối đoái và túi tiền.mp3"),
    (39, "Current account of balance of payments", "14-How Current Accounts Shape Global Wealth.mp3", "07-Nghịch lý tài khoản vãng lai.mp3"),
]

print(f"Total mapped chapters: {len(chapters)}")

en_mapped = [c[2] for c in chapters]
vi_mapped = [c[3] for c in chapters]

assert len(en_mapped) == len(set(en_mapped)), "Duplicate EN files mapped!"
assert len(vi_mapped) == len(set(vi_mapped)), "Duplicate VI files mapped!"

en_actual = [f for f in os.listdir(en_dir) if f.endswith(".mp3")]
vi_actual = [f for f in os.listdir(vi_dir) if f.endswith(".mp3")]

print(f"Actual EN files on disk: {len(en_actual)}")
print(f"Actual VI files on disk: {len(vi_actual)}")

diff_en = set(en_actual) - set(en_mapped)
diff_vi = set(vi_actual) - set(vi_mapped)

if diff_en:
    print(f"Unmapped EN files: {diff_en}")
else:
    print("ALL 39 EN files are 100% mapped!")

if diff_vi:
    print(f"Unmapped VI files: {diff_vi}")
else:
    print("ALL 39 VI files are 100% mapped!")
