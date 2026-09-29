import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC C9: Metals
# ==============================================================================
async def build_c9():
    lid = 'd34bbfa2-7449-4192-b471-3a6a8ba49257'
    code = 'c9'
    title = 'C9: Metals'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-properties-alloys" class="lecture-interactive-card" data-lecture-section="sec_properties_alloys" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-reactivity-series" class="lecture-interactive-card" data-lecture-section="sec_reactivity_series" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-extraction-metals" class="lecture-interactive-card" data-lecture-section="sec_extraction_metals" style="cursor: pointer; ')
    
    t_h2_4 = h2s[4]
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-uses-metals" class="lecture-interactive-card" data-lecture-section="sec_uses_metals" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C9 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C9: Kim loại, Dãy Hoạt động & Luyện kim",
            "selector": "#sec-header",
            "en": "Welcome to Topic C9: Metals. Metals are indispensable structural and functional materials in modern civilization. In this comprehensive lesson, we study physical properties and alloy structures, master the Reactivity Series and displacement reactions, analyze iron extraction in the Blast Furnace, and explore practical uses of aluminum, copper, and steel.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C9: Kim loại, Dãy Hoạt động Hóa học và Công nghệ Luyện kim. Kim loại là vật liệu kết cấu tối quan trọng của nền văn minh hiện đại. Trong bài học này, chúng ta sẽ khảo sát tính chất vật lý và cấu trúc hợp kim, làm chủ dãy hoạt động hóa học và phản ứng nhiệt nhôm, phân tích lò cao luyện gang thép và ứng dụng thực tiễn của nhôm, đồng và thép."
        },
        {
            "id": "sec_properties_alloys",
            "title": "1. Tính chất Vật lý của Kim loại & Cấu trúc Hợp kim (Alloys)",
            "selector": "#sec-properties-alloys",
            "en": "Section 1 contrasts pure metals and alloys: Pure metals consist of uniform layers of positive ions that easily slide over each other under stress, rendering pure metals ductile and malleable. An Alloy is a mixture of a metal with other elements, such as brass (copper and zinc) or steel (iron and carbon). In alloys, different-sized atoms disrupt the regular lattice layers, preventing layers from sliding easily, which significantly increases hardness and tensile strength while improving corrosion resistance.",
            "vi": "Mục một so sánh kim loại nguyên chất và hợp kim: Kim loại nguyên chất gồm các lớp ion dương đều đặn dễ dàng trượt lên nhau khi bị tác dụng lực, khiến kim loại dẻo và dễ dát mỏng. Hợp kim (Alloy) là hỗn hợp của kim loại với các nguyên tố khác, như đồng thau (đồng và kẽm) hay thép (sắt và cacbon). Trong hợp kim, các nguyên tử có kích thước khác nhau làm biến dạng mạng tinh thể trật tự, ngăn cản các lớp ion trượt qua nhau, giúp hợp kim cứng hơn, chịu lực kéo tốt hơn và chống ăn mòn vượt trội."
        },
        {
            "id": "sec_reactivity_series",
            "title": "2. Dãy Hoạt động Hóa học & Phản ứng Đẩy Kim loại",
            "selector": "#sec-reactivity-series",
            "en": "Section 2 investigates the Reactivity Series: ranking metals by their tendency to form positive cations by losing electrons: Potassium, Sodium, Calcium, Magnesium, Aluminium, Carbon, Zinc, Iron, Hydrogen, Copper, Silver, and Gold. A more reactive metal will displace a less reactive metal from its aqueous salt solution or solid metal oxide, releasing thermal energy in exothermic displacement reactions, like magnesium displacing copper from copper(II) sulfate.",
            "vi": "Mục hai nghiên cứu Dãy Hoạt động Hóa học: sắp xếp kim loại theo khả năng nhường electron tạo cation dương: Kali, Natri, Canxi, Magie, Nhôm, Cacbon, Kẽm, Sắt, Hydro, Đồng, Bạc và Vàng. Một kim loại hoạt động mạnh hơn sẽ đẩy kim loại yếu hơn ra khỏi dung dịch muối của nó hoặc khử oxit kim loại ở nhiệt độ cao, giải phóng nhiệt lượng lớn trong phản ứng thế, ví dụ như magie đẩy đồng ra khỏi dung dịch đồng(II) sunfat."
        },
        {
            "id": "sec_extraction_metals",
            "title": "3. Phương pháp Luyện kim & Lò cao Luyện Sắt (Blast Furnace)",
            "selector": "#sec-extraction-metals",
            "en": "Section 3 details metallurgical extraction: Metals higher than carbon in the series, like aluminium, must be extracted by expensive molten electrolysis. Metals below carbon, like iron and zinc, are economically extracted by chemical reduction with carbon or carbon monoxide. In the iron Blast Furnace, haematite ore, coke, and limestone are fed at the top with hot air blown at the bottom. Coke burns exothermically to carbon dioxide, then reduces to carbon monoxide gas, which reduces iron(III) oxide into molten iron running to the bottom. Limestone thermally decomposes to calcium oxide, which reacts with acidic silica sand impurities to form molten slag.",
            "vi": "Mục ba chi tiết hóa công nghệ luyện kim: Các kim loại đứng trước cacbon như nhôm phải được tách bằng điện phân nóng chảy tốn kém. Các kim loại đứng sau cacbon như sắt và kẽm được khử bằng than cốc hoặc khí cacbon monoxit CO giá rẻ trong lò luyện kim. Trong Lò cao luyện sắt (Blast Furnace), quặng hematit Fe2O3, than cốc C và đá vôi CaCO3 được nạp từ trên đỉnh lò trong khi luồng gió nóng thổi từ đáy. Than cốc cháy tạo CO2 rồi bị khử thành CO; khí CO khử quặng hematit thành sắt nóng chảy chìm xuống đáy lò. Đá vôi bị nhiệt phân thành vôi sống CaO, phản ứng với tạp chất cát silic tạo xỉ lỏng nổi lên trên bề mặt sắt lỏng."
        },
        {
            "id": "sec_uses_metals",
            "title": "4. Ứng dụng Thực tiễn của Kim loại & Hợp kim Thép",
            "selector": "#sec-uses-metals",
            "en": "Section 4 covers industrial utilities: Aluminium is used in aircraft manufacture due to low density and corrosion resistance from its protective oxide layer, and in overhead power cables due to low density and good conductivity. Copper is used in electrical wiring due to excellent electrical conductivity and ductility, and in cooking utensils due to high thermal conductivity and unreactivity with water. Mild steel with low carbon is malleable for car bodies; High-carbon steel is hard for cutting tools; Stainless steel alloyed with chromium and nickel resists corrosion for cutlery and chemical plant reactors.",
            "vi": "Mục bốn phân tích ứng dụng công nghiệp: Nhôm được chế tạo vỏ máy bay nhờ khối lượng riêng nhẹ và màng oxit Al2O3 bảo vệ chống ăn mòn, đồng thời làm dây cáp điện cao thế trên cao nhờ trọng lượng nhẹ và dẫn điện tốt. Đồng làm lõi dây điện gia dụng nhờ tính dẫn điện tuyệt vời và dễ uốn dẻo, làm xoong chảo nhờ dẫn nhiệt nhanh và không phản ứng với nước sôi. Thép mềm (Mild steel) ít cacbon dễ dập uốn làm khung xe ô tô; Thép cacbon cao cứng chắc làm lưỡi dao cắt gọt; Thép không gỉ (Inox) pha crom và niken chống rỉ sét tuyệt đối làm dao thìa dĩa và bồn phản ứng hóa chất."
        }
    ]

    major_sections = [
        {"id": "sec_properties_alloys", "title": "1. Tính chất Kim loại & Cấu trúc Hợp kim"},
        {"id": "sec_reactivity_series", "title": "2. Dãy Hoạt động Hóa học & Phản ứng Thế"},
        {"id": "sec_extraction_metals", "title": "3. Luyện kim & Lò cao Luyện Sắt"},
        {"id": "sec_uses_metals", "title": "4. Ứng dụng Thực tiễn của Kim loại & Thép"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C9 successfully built!")


# ==============================================================================
# TOPIC C10: Chemistry of the environment
# ==============================================================================
async def build_c10():
    lid = '9d61f516-a24c-4485-8490-8485604130ec'
    code = 'c10'
    title = 'C10: Chemistry of the environment'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-water-chemistry" class="lecture-interactive-card" data-lecture-section="sec_water_chemistry" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-air-pollution" class="lecture-interactive-card" data-lecture-section="sec_air_pollution" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-rusting-fertilizers" class="lecture-interactive-card" data-lecture-section="sec_rusting_fertilizers" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C10 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C10: Hóa học Môi trường, Nước & Không khí",
            "selector": "#sec-header",
            "en": "Welcome to Topic C10: Chemistry of the environment. Environmental chemistry investigates natural balances and human-induced pollutants. In this chapter, we study water treatment and chemical testing, composition of clean air and atmospheric pollutants, greenhouse climate forcing, rust prevention, and synthetic agricultural fertilizers.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C10: Hóa học Môi trường, Nước và Không khí. Hóa học môi trường nghiên cứu các cân bằng tự nhiên và tác nhân ô nhiễm do con người. Trong bài học này, chúng ta sẽ khảo sát quy trình xử lý nước và nhận biết nước tinh khiết, thành phần không khí sạch và các chất ô nhiễm khí quyển, hiệu ứng nhà kính, chống rỉ sét sắt và phân bón hóa học NPK."
        },
        {
            "id": "sec_water_chemistry",
            "title": "1. Hóa học Nguồn nước: Nhận biết Nước & Xử lý Nước sinh hoạt",
            "selector": "#sec-water-chemistry",
            "en": "Section 1 covers water chemistry: Chemical testing for water uses anhydrous copper(II) sulfate, turning from white to blue, or anhydrous cobalt(II) chloride paper, turning from blue to pink. Water purity is confirmed physically by a sharp boiling point at 100 degrees Celsius and melting point at zero degrees. Water treatment plants prepare drinking water via sedimentation of coarse debris, filtration through sand and gravel beds to remove insolubles, carbon adsorption to eliminate odours, and chlorination to disinfect and kill harmful bacteria.",
            "vi": "Mục một phân tích hóa học nguồn nước: Thử nghiệm hóa học nhận biết sự có mặt của nước dùng tinh thể đồng(II) sunfat khan CuSO4 chuyển từ màu trắng sang màu xanh lam, hoặc giấy tẩm coban(II) clorua khan CoCl2 chuyển từ xanh lam sang hồng phấn. Độ tinh khiết của nước được xác định bằng điểm sôi cố định đúng 100 độ C và đông đặc ở 0 độ C. Quy trình xử lý nước sinh hoạt gồm lắng cặn thô, lọc qua nhiều lớp cát sỏi để loại bỏ chất rắn lơ lửng, lọc than hoạt tính khử mùi và sục khí clo để khử trùng tiêu diệt vi khuẩn gây bệnh."
        },
        {
            "id": "sec_air_pollution",
            "title": "2. Thành phần Khí quyển & Các Chất Ô nhiễm Không khí",
            "selector": "#sec-air-pollution",
            "en": "Section 2 investigates clean air and atmospheric pollution: Clean, dry air contains approximately 78% nitrogen, 21% oxygen, 0.9% argon, and 0.04% carbon dioxide. Common air pollutants include: Carbon monoxide from incomplete combustion of carbonaceous fuels, poisoning blood by irreversibly binding to hemoglobin; Sulfur dioxide from combustion of fossil fuels containing sulfur impurities, producing acid rain; Oxides of nitrogen from vehicle engines triggering photochemical smog and acid rain; and Methane and Carbon dioxide driving the enhanced greenhouse effect and global warming.",
            "vi": "Mục hai khảo sát không khí sạch và các chất gây ô nhiễm khí quyển: Không khí khô sạch gồm 78% nitơ N2, 21% oxy O2, 0.9% agon và 0.04% CO2. Các chất ô nhiễm không khí nguy hiểm gồm: Khí CO từ đốt cháy không hoàn toàn nhiên liệu, liên kết chặt với hemoglobin gây ngạt thở; Khí SO2 từ đốt cháy than đá chứa tạp chất lưu huỳnh gây mưa axit; Các oxit nitơ NOx sinh ra từ buồng đốt động cơ xe hơi gây sương mù quang hóa và mưa axit; cùng khí Methane CH4 và CO2 gây hiệu ứng nhà kính tăng cường và biến đổi khí hậu toàn cầu."
        },
        {
            "id": "sec_rusting_fertilizers",
            "title": "3. Sự Rỉ sét của Sắt & Phân bón Hóa học (NPK Fertilizers)",
            "selector": "#sec-rusting-fertilizers",
            "en": "Section 3 covers corrosion and fertilizers: Rusting of iron is the formation of hydrated iron(III) oxide, requiring both oxygen and water simultaneously. Rust prevention methods include barrier methods like painting, greasing, and plastic coating; Sacrificial protection attaching blocks of more reactive zinc or magnesium; and Galvanizing: dipping steel in molten zinc, which shields physically and protects sacrificially even if scratched. Agricultural NPK fertilizers supply three vital macronutrients: Nitrogen for leafy vegetative growth and amino acid synthesis; Phosphorus for root development; and Potassium for flower and fruit disease resistance.",
            "vi": "Mục ba phân tích sự rỉ sét và phân bón hóa học: Sự rỉ sét của sắt là quá trình hình thành oxit sắt(III) ngậm nước, bắt buộc phải có đồng thời cả oxy và nước. Các phương pháp chống rỉ sét gồm: Phương pháp rào cản ngăn tiếp xúc (sơn, tra dầu mỡ, phủ nhựa); Bảo vệ hy sinh bằng cách gắn các khối kim loại hoạt động mạnh hơn như kẽm hoặc magie; và Mạ kẽm (Galvanizing): nhúng thép vào kẽm nóng chảy vừa tạo lớp vỏ bảo vệ vừa bảo vệ hy sinh ngay cả khi lớp mạ bị trầy xước. Phân bón NPK cung cấp 3 nguyên tố đa lượng tối cần thiết cho cây trồng: Nitơ (N) kích thích phát triển thân lá và tổng hợp protein; Photpho (P) phát triển bộ rễ; và Kali (K) kích thích ra hoa đậu quả và tăng sức đề kháng sâu bệnh."
        }
    ]

    major_sections = [
        {"id": "sec_water_chemistry", "title": "1. Hóa học Nguồn nước & Xử lý Nước sạch"},
        {"id": "sec_air_pollution", "title": "2. Thành phần Khí quyển & Ô nhiễm Không khí"},
        {"id": "sec_rusting_fertilizers", "title": "3. Chống Rỉ sét & Phân bón Hóa học NPK"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C10 successfully built!")


# ==============================================================================
# TOPIC C11: Organic chemistry
# ==============================================================================
async def build_c11():
    lid = '69b82c81-05a0-40a8-816f-c21a882cef54'
    code = 'c11'
    title = 'C11: Organic chemistry'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-homologous-series" class="lecture-interactive-card" data-lecture-section="sec_homologous_series" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-hydrocarbons-alkanes-alkenes" class="lecture-interactive-card" data-lecture-section="sec_hydrocarbons_alkanes_alkenes" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-polymers" class="lecture-interactive-card" data-lecture-section="sec_polymers" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C11 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C11: Hóa học Hữu cơ & Polymer",
            "selector": "#sec-header",
            "en": "Welcome to Topic C11: Organic chemistry. Carbon forms the structural backbone of life and synthetic materials. In this lesson, we study homologous series and IUPAC nomenclature, compare saturated alkanes and unsaturated alkenes, analyze catalytic cracking and addition reactions, and examine addition polymerization yielding plastics.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C11: Hóa học Hữu cơ và Vật liệu Polymer. Nguyên tử carbon tạo nên bộ khung xương của sự sống và các vật liệu tổng hợp hiện đại. Trong bài học này, chúng ta sẽ khảo sát dãy đồng đẳng và danh pháp IUPAC, so sánh ankan no và anken không no, phản ứng cracking và phản ứng cộng, cùng phản ứng trùng hợp tạo chất dẻo polymer."
        },
        {
            "id": "sec_homologous_series",
            "title": "1. Dãy Đồng đẳng & Danh pháp Hóa học Hữu cơ",
            "selector": "#sec-homologous-series",
            "en": "Section 1 defines a Homologous series: a family of organic compounds with the same functional group, the same general formula, similar chemical properties, and a regular gradation in physical properties such as boiling point as chain length increases, differing by a CH2 unit. Organic prefixes designate carbon chain length: meth for one carbon, eth for two, prop for three, and but for four carbons. Structural isomerism occurs when compounds share the same molecular formula but have different structural arrangements.",
            "vi": "Mục một định nghĩa Dãy Đồng đẳng (Homologous series): là tập hợp các hợp chất hữu cơ có cùng nhóm chức, cùng công thức phân tử tổng quát, có tính chất hóa học tương tự nhau, có quy luật biến đổi tính chất vật lý đều đặn (như nhiệt độ sôi tăng dần theo chiều dài mạch carbon) và hơn kém nhau một hay nhiều nhóm CH2. Các tiền tố IUPAC chỉ số nguyên tử carbon: met (1C), et (2C), prop (3C), but (4C). Đồng phân cấu tạo là các chất có cùng công thức phân tử nhưng khác nhau về trật tự liên kết giữa các nguyên tử."
        },
        {
            "id": "sec_hydrocarbons_alkanes_alkenes",
            "title": "2. Hydrocacbon: Ankan No vs Anken Không no & Cracking",
            "selector": "#sec-hydrocarbons-alkanes-alkenes",
            "en": "Section 2 contrasts Alkanes and Alkenes: Alkanes have the general formula C_n H_{2n+2}; they are saturated hydrocarbons containing only single covalent C-C bonds, generally unreactive except for combustion and photochemical halogen substitution under ultraviolet light. Alkenes have general formula C_n H_{2n}; they are unsaturated hydrocarbons containing a reactive carbon-carbon double bond, undergoing addition reactions. Bromine water distinguishes them: orange-brown bromine water remains unchanged with alkanes, but is rapidly decolourised to colourless by alkenes. Catalytic Cracking breaks large alkane molecules into smaller, more valuable alkanes and alkenes at high temperature using a zeolite catalyst.",
            "vi": "Mục hai so sánh Ankan và Anken: Ankan có công thức tổng quát CnH2n+2; là hydrocacbon no chỉ chứa các liên kết đơn C-C bền vững, khá trơ về mặt hóa học trừ phản ứng cháy và phản ứng thế halogen dưới ánh sáng tử ngoại UV. Anken có công thức tổng quát CnH2n; là hydrocacbon không no chứa liên kết đôi C=C kém bền, dễ tham gia phản ứng cộng. Nước brom dùng để phân biệt hai loại: dung dịch nước brom màu nâu cam không đổi màu khi gặp ankan, nhưng bị anken làm mất màu trong suốt tức thì. Quá trình Cracking nhiệt xúc tác bẻ gãy các phân tử ankan mạch dài nặng nề thành các ankan mạch ngắn giá trị cao và anken dùng cho công nghiệp polymer."
        },
        {
            "id": "sec_polymers",
            "title": "3. Phản ứng Trùng hợp & Chất dẻo Polymer (Plastics)",
            "selector": "#sec-polymers",
            "en": "Section 3 investigates Addition Polymerization: Monomers containing carbon-carbon double bonds, like ethene, react together under high pressure and catalyst; the double bonds break and link into extremely long continuous chains called addition polymers, like poly(ethene). Synthetic plastics are lightweight, durable, and chemically inert, but their non-biodegradable nature causes acute ecological pollution in landfills and oceans, emitting toxic gases when incinerated.",
            "vi": "Mục ba nghiên cứu Phản ứng Trùng hợp (Addition Polymerization): Các phân tử monome nhỏ chứa liên kết đôi C=C như etilen, dưới điều kiện áp suất và xúc tác, bẻ gãy liên kết đôi để liên kết hàng nghìn phân tử lại với nhau tạo thành đại phân tử chuỗi dài polymer như polyetylen (PE). Chất dẻo tổng hợp nhẹ, bền, cách điện tốt nhưng không bị vi sinh vật phân hủy sinh học, gây tích tụ rác thải nhựa đe dọa sinh thái đại dương và phát thải khí độc khi bị đốt cháy."
        }
    ]

    major_sections = [
        {"id": "sec_homologous_series", "title": "1. Dãy Đồng đẳng & Danh pháp IUPAC"},
        {"id": "sec_hydrocarbons_alkanes_alkenes", "title": "2. Ankan No vs Anken Không no & Cracking"},
        {"id": "sec_polymers", "title": "3. Trùng hợp & Vật liệu Polymer (Plastics)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C11 successfully built!")


# ==============================================================================
# TOPIC C12: Experimental techniques and Chemical analysis
# ==============================================================================
async def build_c12():
    lid = 'd51b5192-ff57-48a0-bcd9-d4f8a7d10757'
    code = 'c12'
    title = 'C12: Experimental techniques and Chemical analysis'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-separation-techniques" class="lecture-interactive-card" data-lecture-section="sec_separation_techniques" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-gas-identification" class="lecture-interactive-card" data-lecture-section="sec_gas_identification" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-ion-identification" class="lecture-interactive-card" data-lecture-section="sec_ion_identification" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C12 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C12: Phương pháp Tách chất & Nhận biết Hóa học",
            "selector": "#sec-header",
            "en": "Welcome to Topic C12: Experimental techniques and Chemical analysis. Practical chemistry requires precise separation and qualitative identification. In this final chemistry chapter, we master laboratory apparatus and separation techniques, qualitative gas identification tests, and systematic identification of cations and anions.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C12: Kỹ thuật Thực nghiệm và Phân tích Hóa học Định tính. Hóa học thực nghiệm đòi hỏi kỹ năng tách chất và nhận biết chính xác. Trong bài học kết thúc phần hóa học này, chúng ta sẽ khảo sát dụng cụ và các phương pháp tách chất, thuốc thử nhận biết chất khí, cùng hệ thống nhận biết các cation kim loại và anion phi kim."
        },
        {
            "id": "sec_separation_techniques",
            "title": "1. Các Kỹ thuật Tách chất trong Phòng Thí nghiệm",
            "selector": "#sec-separation-techniques",
            "en": "Section 1 reviews physical separation techniques: Filtration separates an insoluble solid from a liquid using porous filter paper. Crystallisation recovers a soluble solute from its solution by gentle evaporation to crystallisation point followed by cooling. Simple distillation separates a liquid solvent from a non-volatile dissolved solute using boiling and condenser cooling. Fractional distillation separates miscible liquids with different boiling points using a fractionating column. Paper chromatography separates mixtures of soluble dyes based on differential partition between stationary paper and mobile solvent phases; retention factor R_f equals distance travelled by substance divided by distance travelled by solvent front.",
            "vi": "Mục một tổng kết các phương pháp tách chất: Phương pháp Lọc (Filtration) tách chất rắn không tan ra khỏi chất lỏng bằng giấy lọc. Kết tinh (Crystallisation) thu hồi chất tan từ dung dịch bằng cách cô cạn nhẹ đến độ bão hòa rồi để nguội cho tinh thể xuất hiện. Chưng cất đơn (Simple distillation) tách dung môi lỏng ra khỏi chất tan không bay hơi bằng cách đun sôi và ngưng tụ qua ống sinh hàn. Chưng cất phân đoạn (Fractional distillation) tách các chất lỏng trộn lẫn vào nhau có nhiệt độ sôi khác nhau qua cột phân đoạn. Sắc ký giấy (Paper chromatography) tách hỗn hợp phẩm nhuộm dựa vào độ tan và độ bám dính khác nhau giữa pha tĩnh giấy và pha động dung môi; hệ số lưu giữ Rf bằng khoảng cách dịch chuyển của chất chia cho khoảng cách dịch chuyển của mức dung môi."
        },
        {
            "id": "sec_gas_identification",
            "title": "2. Phương pháp Nhận biết các Chất Khí Thông dụng",
            "selector": "#sec-gas-identification",
            "en": "Section 2 reviews qualitative gas testing: Ammonia (NH3) is a pungent alkaline gas turning damp red litmus paper blue. Carbon dioxide (CO2) turns limewater milky white by forming insoluble calcium carbonate precipitate. Chlorine (Cl2) is a pale yellow-green choking gas that bleaches damp litmus paper white. Hydrogen (H2) ignites with a squeaky pop when tested with a lighted splint. Oxygen (O2) relights a glowing wooden splint.",
            "vi": "Mục hai tổng hợp các phản ứng nhận biết chất khí: Khí Amoniac NH3 có mùi khai nồng, tính kiềm làm quỳ tím ẩm hóa xanh. Khí Carbon dioxide CO2 làm đục nước vôi trong do tạo kết tủa trắng canxi cacbonat CaCO3. Khí Clo Cl2 màu vàng lục mùi hắc làm mất màu tẩy trắng giấy quỳ tím ẩm. Khí Hydro H2 cháy phát ra tiếng nổ 'bốp' nhỏ khi đưa que đóm đang cháy vào miệng ống nghiệm. Khí Oxy O2 làm que đóm tàn đỏ bùng cháy sáng trở lại."
        },
        {
            "id": "sec_ion_identification",
            "title": "3. Nhận biết Ion Kim loại (Cations) & Anion Phi kim",
            "selector": "#sec-ion-identification",
            "en": "Section 3 details ion identification protocols: Aqueous sodium hydroxide and aqueous ammonia test for metal cations by precipitate color and solubility: Copper(II) yields a light blue precipitate, insoluble in excess NaOH, dissolving in excess ammonia to form a deep royal blue solution. Iron(II) gives a dirty green precipitate; Iron(III) produces a red-brown precipitate. Flame tests distinguish cations: Lithium burns crimson-red, Sodium yellow-orange, Potassium lilac-violet, Calcium orange-red, Copper(II) blue-green. For anions: Halides test with dilute nitric acid and aqueous silver nitrate: Chloride gives white precipitate, Bromide cream, Iodide yellow. Sulfate tests with dilute nitric acid and aqueous barium nitrate, producing a dense white precipitate.",
            "vi": "Mục ba chi tiết hóa quy trình nhận biết ion: Thuốc thử dung dịch NaOH và NH3 nhận biết Cation kim loại qua màu kết tủa hiđroxit: Ion đồng(II) Cu2+ tạo kết tủa xanh lam nhạt, không tan trong NaOH dư nhưng tan trong NH3 dư tạo dung dịch phức chất màu xanh thẫm hoàng gia. Ion sắt(II) Fe2+ tạo kết tủa xanh rêu bẩn; Ion sắt(III) Fe3+ tạo kết tủa nâu đỏ. Thử màu ngọn lửa (Flame test): Liti ngọn lửa đỏ thẫm, Natri vàng cam, Kali tím nhạt, Canxi đỏ cam, Đồng xanh lục lam. Nhận biết Anion: Nhóm halogenua thử bằng axit nitric HNO3 loãng và bạc nitrat AgNO3: Clorua tạo kết tủa trắng, Bromua kết tủa vàng nhạt (kem), Iotua kết tủa vàng đậm. Ion Sunfat SO4(2-) thử bằng axit nitric loãng và bari nitrat Ba(NO3)2 tạo kết tủa trắng không tan."
        }
    ]

    major_sections = [
        {"id": "sec_separation_techniques", "title": "1. Các Kỹ thuật Tách chất trong Phòng Thí nghiệm"},
        {"id": "sec_gas_identification", "title": "2. Nhận biết các Chất Khí Thông dụng"},
        {"id": "sec_ion_identification", "title": "3. Nhận biết Cation Kim loại & Anion Phi kim"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C12 successfully built!")


# ==============================================================================
# MAIN BATCH 7 RUNNER (TOPICS C9 -> C12)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 7: TOPICS C9 -> C12")
    print("*******************************************************\n")
    
    await build_c9()
    await asyncio.sleep(2)
    
    await build_c10()
    await asyncio.sleep(2)
    
    await build_c11()
    await asyncio.sleep(2)
    
    await build_c12()
    
    print("\n*******************************************************")
    print("BATCH 7 COMPLETE: TOPICS C9 -> C12 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
