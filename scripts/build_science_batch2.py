import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC B6: Plant Nutrition
# ==============================================================================
async def build_b6():
    lid = '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1'
    code = 'b6'
    title = 'B6: Plant Nutrition'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-photosynthesis" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-glucose-minerals" class="lecture-interactive-card" data-lecture-section="sec_glucose_minerals" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-leaf-anatomy" class="lecture-interactive-card" data-lecture-section="sec_leaf_anatomy" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-limiting-factors" class="lecture-interactive-card" data-lecture-section="sec_limiting_factors" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B6 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B6: Quang hợp & Dinh dưỡng Thực vật",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Co-ordinated Sciences Biology, Topic B6: Plant Nutrition. Photosynthesis is the fundamental biological process synthesizing organic fuel on Earth. In this chapter, we explore balanced photosynthetic equations, glucose utilization and mineral nutrition, leaf anatomy adaptations, and limiting factor experiments.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B6: Dinh dưỡng Thực vật và Quang hợp. Quang hợp là quá trình sinh học nền tảng chuyển hóa năng lượng mặt trời thành năng lượng hóa học cho sinh quyển. Trong bài học này, chúng ta sẽ khảo sát phương trình quang hợp, chuyển hóa glucose và khoáng chất, giải phẫu thích nghi của lá, cùng các thí nghiệm về nhân tố giới hạn."
        },
        {
            "id": "sec_photosynthesis",
            "title": "1. Quá trình Quang hợp & Phương trình Hóa học",
            "selector": "#sec-photosynthesis",
            "en": "Section 1 defines Photosynthesis: the process by which plants synthesize carbohydrates from raw materials using energy from light. Chlorophyll inside chloroplasts absorbs solar energy, transferring it into chemical bonds. The balanced chemical equation is: six molecules of carbon dioxide react with six molecules of water in the presence of light and chlorophyll to produce one molecule of glucose and six molecules of oxygen gas.",
            "vi": "Mục một định nghĩa Quang hợp: là quá trình thực vật tổng hợp carbohydrate từ các nguyên liệu thô sử dụng năng lượng ánh sáng. Sắc tố diệp lục trong lục lạp hấp thu năng lượng photon mặt trời và chuyển hóa thành hóa năng trong các liên kết hóa học. Phương trình hóa học cân bằng: 6 phân tử carbon dioxide kết hợp với 6 phân tử nước, dưới tác dụng của ánh sáng và diệp lục, tạo ra 1 phân tử glucose và giải phóng 6 phân tử khí oxy."
        },
        {
            "id": "sec_glucose_minerals",
            "title": "2. Chuyển hóa Glucose & Dinh dưỡng Khoáng Thực vật",
            "selector": "#sec-glucose-minerals",
            "en": "Section 2 investigates glucose fate and mineral ions: Glucose produced in photosynthesis is oxidized in respiration for energy, converted into insoluble starch for compact storage, polymerized into cellulose for cell wall construction, converted into sucrose for phloem transport, or combined with mineral ions. Plants absorb Magnesium ions to synthesize the green pigment chlorophyll; magnesium deficiency causes chlorosis, resulting in yellow leaves. Plants absorb Nitrate ions to supply nitrogen for synthesizing amino acids and proteins; nitrate deficiency severely stunting plant growth.",
            "vi": "Mục hai nghiên cứu sự chuyển hóa glucose và các ion khoáng thiết yếu: Glucose sinh ra được dùng ngay trong hô hấp tế bào để tạo năng lượng, chuyển hóa thành tinh bột không tan để dự trữ trong rễ và củ, tổng hợp thành cellulose để xây dựng thành tế bào, chuyển thành đường sucrose để vận chuyển qua mạch rây, hoặc kết hợp với ion khoáng. Thực vật hấp thu ion Magie để tổng hợp diệp lục; thiếu magie gây bệnh vàng lá (chlorosis). Thực vật hấp thu ion Nitrat để cung cấp nitơ tổng hợp các axit amin và protein; thiếu nitrat làm cây còi cọc nghiêm trọng."
        },
        {
            "id": "sec_leaf_anatomy",
            "title": "3. Giải phẫu Thích nghi của Lá Cây Hai lá mầm",
            "selector": "#sec-leaf-anatomy",
            "en": "Section 3 examines dicotyledonous leaf adaptations: The transparent waxy cuticle reduces evaporation while allowing sunlight penetration. The upper epidermis protects inner layers. The palisade mesophyll consists of densely packed columnar cells packed with chloroplasts near the upper surface to maximize light absorption. The spongy mesophyll contains loose cells with large interconnected air spaces, accelerating internal carbon dioxide and water vapor diffusion toward stomata guarded by specialized guard cells on the lower epidermis.",
            "vi": "Mục ba phân tích giải phẫu thích nghi của lá cây hai lá mầm: Lớp cutin sáp trong suốt phía trên chống mất nước nhưng cho ánh sáng xuyên qua. Biểu bì trên bảo vệ các mô bên trong. Mô giậu (Palisade mesophyll) gồm các tế bào hình trụ xếp sát nhau chứa mật độ lục lạp dày đặc nhất nằm ngay dưới mặt trên để tối đa hóa sự hấp thu ánh sáng. Mô khuyết (Spongy mesophyll) gồm các tế bào xếp xốp rỗng với các khoảng gian bào lớn giúp khí CO2 và hơi nước khuếch tán nhanh chóng đến các khí khổng được đóng mở bởi cặp tế bào hình hạt đậu ở biểu bì dưới."
        },
        {
            "id": "sec_limiting_factors",
            "title": "4. Nhân tố Giới hạn & Dung dịch Chỉ thị Màu",
            "selector": "#sec-limiting-factors",
            "en": "Section 4 covers Limiting Factors: environmental factors that are in shortest supply and directly restrict the rate of a physiological process. The three principal limiting factors of photosynthesis are light intensity, carbon dioxide concentration, and ambient temperature. Hydrogencarbonate indicator reveals gas exchange: in darkness, respiration dominates releasing carbon dioxide, turning indicator yellow; in bright light, photosynthesis exceeds respiration, consuming carbon dioxide and turning indicator purple; at compensation point, it remains orange-red.",
            "vi": "Mục bốn phân tích Nhân tố Giới hạn: là yếu tố ở mức thấp nhất và trực tiếp kiềm chế tốc độ của quá trình quang hợp. Ba nhân tố giới hạn chính gồm cường độ ánh sáng, nồng độ CO2 và nhiệt độ môi trường. Dung dịch chỉ thị hydrogencarbonate phản ánh sự trao đổi khí: trong bóng tối chỉ có hô hấp thải CO2 làm dung dịch hóa vàng; dưới ánh sáng mạnh quang hợp vượt trội hô hấp làm cạn CO2 khiến dung dịch hóa tím; tại điểm bù ánh sáng dung dịch giữ nguyên màu đỏ cam ban đầu."
        }
    ]

    major_sections = [
        {"id": "sec_photosynthesis", "title": "1. Quá trình Quang hợp & Phương trình"},
        {"id": "sec_glucose_minerals", "title": "2. Chuyển hóa Glucose & Khoáng chất"},
        {"id": "sec_leaf_anatomy", "title": "3. Cấu tạo Thích nghi của Lá cây"},
        {"id": "sec_limiting_factors", "title": "4. Nhân tố Giới hạn & Thí nghiệm"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B6 successfully built!")


# ==============================================================================
# TOPIC B7: Human nutrition
# ==============================================================================
async def build_b7():
    lid = 'cbebf582-244c-48bf-a586-c6c1922d8e20'
    code = 'b7'
    title = 'B7: Human nutrition'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-balanced-diet" class="lecture-interactive-card" data-lecture-section="sec_balanced_diet" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-food-processing" class="lecture-interactive-card" data-lecture-section="sec_food_processing" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-digestive-system" class="lecture-interactive-card" data-lecture-section="sec_digestive_system" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-chemical-digestion" class="lecture-interactive-card" data-lecture-section="sec_chemical_digestion" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B7 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B7: Dinh dưỡng Người & Hệ Tiêu hóa",
            "selector": "#sec-header",
            "en": "Welcome to Topic B7: Human nutrition. The human body requires a steady influx of nutrients to sustain metabolic life. In this comprehensive lesson, we analyze dietary requirements and malnutrition disorders, trace the five stages of food processing, map alimentary canal anatomy, and examine chemical digestion by enzymes and bile.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B7: Dinh dưỡng ở Người và Hệ Tiêu hóa. Cơ thể người đòi hỏi nguồn dinh dưỡng liên tục để duy trì các hoạt động chuyển hóa. Trong bài học này, chúng ta sẽ khảo sát tháp dinh dưỡng cân bằng và các bệnh suy dinh dưỡng, 5 giai đoạn chế biến thức ăn, giải phẫu ống tiêu hóa và quá trình tiêu hóa hóa học bằng enzyme và dịch mật."
        },
        {
            "id": "sec_balanced_diet",
            "title": "1. Khẩu phần Ăn Cân bằng & Bệnh Thiếu hụt Dinh dưỡng",
            "selector": "#sec-balanced-diet",
            "en": "Section 1 details dietary components: A balanced diet provides all seven essential food groups in correct proportions: carbohydrates for rapid energy, lipids for long-term insulation and storage, proteins for tissue growth and repair, vitamins, minerals, dietary fibre to stimulate peristalsis, and water as a universal solvent. Nutritional deficiencies cause distinct disorders: Vitamin C deficiency causes scurvy with bleeding gums; Vitamin D and Calcium deficiencies cause rickets with soft, bent bones; Iron deficiency causes anaemia due to reduced hemoglobin; severe protein starvation causes kwashiorkor.",
            "vi": "Mục một chi tiết hóa các thành phần dinh dưỡng: Một chế độ ăn cân bằng cung cấp đủ 7 nhóm dưỡng chất với tỷ lệ hợp lý: carbohydrate cung cấp năng lượng nhanh, lipid dự trữ năng lượng và cách nhiệt, protein xây dựng và tái tạo mô, vitamin, khoáng chất, chất xơ kích thích nhu động ruột và nước làm dung môi sinh học. Thiếu hụt dinh dưỡng dẫn đến các bệnh lý đặc trưng: Thiếu vitamin C gây bệnh scorbut chảy máu chân răng; thiếu vitamin D và canxi gây bệnh còi xương mềm xương; thiếu sắt gây thiếu máu do giảm hemoglobin; suy dinh dưỡng protein trầm trọng gây bệnh phù kwashiorkor."
        },
        {
            "id": "sec_food_processing",
            "title": "2. Năm Giai đoạn Xử lý Thức ăn trong Cơ thể",
            "selector": "#sec-food-processing",
            "en": "Section 2 distinguishes the five sequential stages of human food processing: Ingestion is taking substances into the body through the mouth. Mechanical digestion breaks food into smaller pieces without chemical change, while Chemical digestion breaks large insoluble molecules into small soluble molecules. Absorption transfers digested food molecules across the intestinal wall into blood and lymph. Assimilation incorporates absorbed food into cell structures for metabolism. Egestion expels undigested waste as faeces through the anus.",
            "vi": "Mục hai phân biệt 5 giai đoạn tuần tự trong quá trình tiêu hóa: Thu nhận thức ăn (Ingestion) là đưa thức ăn vào miệng. Tiêu hóa cơ học (Mechanical digestion) nghiền nhỏ thức ăn mà không biến đổi hóa học, trong khi Tiêu hóa hóa học (Chemical digestion) thủy phân các đại phân tử không tan thành các phân tử nhỏ hòa tan được. Hấp thu (Absorption) chuyển các phân tử dưỡng chất qua thành ruột non vào máu và bạch huyết. Đồng hóa (Assimilation) vận chuyển và tích hợp dưỡng chất vào cấu trúc tế bào. Thải bã (Egestion) tống xuất cặn bã thức ăn không tiêu hóa ra ngoài qua hậu môn."
        },
        {
            "id": "sec_digestive_system",
            "title": "3. Giải phẫu Ống Tiêu hóa & Nhu động Ruột (Peristalsis)",
            "selector": "#sec-digestive-system",
            "en": "Section 3 outlines the alimentary canal: Food is chewed in the mouth, lubricated by saliva, and pushed along the esophagus by peristalsis: alternating waves of contraction and relaxation of circular and longitudinal muscles. In the stomach, muscular churning mixes food with hydrochloric acid, killing ingested pathogens and providing optimum pH 2 for pepsin. In the small intestine, pancreatic juice and bile neutralize acid and finish digestion, while millions of microvilli-lined villi maximize absorption area.",
            "vi": "Mục ba mô tả giải phẫu ống tiêu hóa: Thức ăn được nhai nghiền ở khoang miệng, làm mềm nhờ nước bọt và được đẩy dọc thực quản nhờ nhu động ruột (peristalsis) - các làn sóng co thắt luân phiên của lớp cơ vòng và cơ dọc. Tại dạ dày, sự co bóp cơ học hòa trộn thức ăn với axit clohidric HCl, tiêu diệt vi khuẩn gây bệnh và tạo pH 2 tối ưu cho enzyme pepsin hoạt động. Tại ruột non, dịch tụy và dịch mật trung hòa axit và hoàn tất tiêu hóa, nơi hàng triệu lông nhung (villi) và vi nhung mao tối đa hóa diện tích hấp thu vào máu."
        },
        {
            "id": "sec_chemical_digestion",
            "title": "4. Tiêu hóa Hóa học: Hệ Enzyme Tiêu hóa & Vai trò Dịch Mật",
            "selector": "#sec-chemical-digestion",
            "en": "Section 4 details chemical breakdown: Amylase digests starch into maltose, and maltase breaks maltose into glucose. Proteases like pepsin in the stomach and trypsin in the small intestine break proteins down into amino acids. Lipase breaks down fats into glycerol and fatty acids. Bile, produced by the liver and stored in the gall bladder, contains no enzymes; its alkaline salts neutralize acidic gastric chyme and physically emulsify large lipid droplets into tiny droplets, dramatically increasing surface area for lipase action.",
            "vi": "Mục bốn phân tích chi tiết quá trình tiêu hóa hóa học: Enzyme Amylase thủy phân tinh bột thành maltose, sau đó maltase bẻ gãy maltose thành glucose. Các enzyme Protease như pepsin trong dạ dày và trypsin trong ruột non phân giải protein thành các axit amin. Enzyme Lipase phân giải chất béo thành glycerol và các axit béo. Dịch mật do gan tiết ra và dự trữ ở túi mật không chứa enzyme; muối mật có tính kiềm giúp trung hòa vị trấp axit từ dạ dày và nhũ hóa các giọt mỡ lớn thành các vi giọt li ti, giúp tăng diện tích bề mặt tiếp xúc lên hàng trăm lần cho enzyme lipase hoạt động."
        }
    ]

    major_sections = [
        {"id": "sec_balanced_diet", "title": "1. Khẩu phần Ăn Cân bằng & Bệnh Thiếu hụt"},
        {"id": "sec_food_processing", "title": "2. Năm Giai đoạn Xử lý Thức ăn"},
        {"id": "sec_digestive_system", "title": "3. Giải phẫu Ống Tiêu hóa & Nhu động"},
        {"id": "sec_chemical_digestion", "title": "4. Tiêu hóa Hóa học & Dịch Mật"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B7 successfully built!")


# ==============================================================================
# TOPIC B8: Transport in plants
# ==============================================================================
async def build_b8():
    lid = 'e2819423-13ed-47a2-bd80-9a083989e8bd'
    code = 'b8'
    title = 'B8: Transport in plants'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    # Target content headers [2], [3], [4], [5]
    t_h2_0 = h2s[2]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-xylem-phloem" class="lecture-interactive-card" data-lecture-section="sec_xylem_phloem" style="cursor: pointer; ')
    
    t_h2_1 = h2s[3]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-vascular-position" class="lecture-interactive-card" data-lecture-section="sec_vascular_position" style="cursor: pointer; ')
    
    t_h2_2 = h2s[4]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-transpiration" class="lecture-interactive-card" data-lecture-section="sec_transpiration" style="cursor: pointer; ')
    
    t_h2_3 = h2s[5]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-translocation" class="lecture-interactive-card" data-lecture-section="sec_translocation" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B8 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B8: Hệ Vận chuyển ở Thực vật",
            "selector": "#sec-header",
            "en": "Welcome to Topic B8: Transport in plants. Multicellular plants require specialized vascular plumbing to transport water from roots and photoassimilates from leaves. In this lesson, we contrast xylem and phloem structure, examine vascular bundles across dicot organs, explore the transpiration stream, and investigate phloem translocation from source to sink.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B8: Vận chuyển ở Thực vật. Cây đa bào cần hệ mạch dẫn chuyên biệt để vận chuyển dòng nước từ rễ và các chất hữu cơ từ lá. Trong bài học này, chúng ta sẽ so sánh cấu tạo mạch gỗ và mạch rây, phân bố bó mạch ở các cơ quan cây hai lá mầm, dòng thoát hơi nước và cơ chế vận chuyển chất hữu cơ từ nguồn đến đích."
        },
        {
            "id": "sec_xylem_phloem",
            "title": "1. Cấu trúc Mạch gỗ (Xylem) & Mạch rây (Phloem)",
            "selector": "#sec-xylem-phloem",
            "en": "Section 1 contrasts vascular tissues: Xylem vessels consist of dead, elongated cells joined end-to-end with hollow lumens, devoid of cytoplasm or end walls. Cell walls are heavily thickened and impregnated with impermeable lignin, providing tensile strength to withstand negative transpirational tension and structurally support the plant stem. Phloem consists of living sieve tube elements connected by perforated sieve plates, supported metabolically by adjacent companion cells containing dense mitochondria.",
            "vi": "Mục một so sánh cấu tạo hai mô mạch dẫn: Mạch gỗ (Xylem) gồm các tế bào chết hình ống kéo dài nối đầu với nhau tạo thành ống rỗng liên tục, không chứa tế bào chất hay vách ngăn ngang. Thành tế bào được tẩm lignin dày chắc không thấm nước, tạo sức bền chịu được lực kéo căng âm của dòng thoát hơi nước và nâng đỡ thân cây. Mạch rây (Phloem) gồm các tế bào sống tạo thành ống rây nối với nhau qua các bản rây có lỗ, được hỗ trợ chuyển hóa tích cực bởi các tế bào kèm bên cạnh chứa mật độ ty thể cao."
        },
        {
            "id": "sec_vascular_position",
            "title": "2. Vị trí Phân bố Bó mạch ở Rễ, Thân & Lá Cây",
            "selector": "#sec-vascular-position",
            "en": "Section 2 examines anatomical distribution: In dicot roots, the vascular bundle forms a tight central cylinder, with xylem arranged in an X-shaped central cross to anchor the plant and resist upward pulling forces, with phloem located in the pockets between the arms. In dicot stems, vascular bundles are arranged in a regular peripheral ring around the outer cortex, with xylem located toward the interior and phloem toward the exterior, resisting bending forces from wind. In leaves, vascular bundles form veins, with xylem situated on the upper surface.",
            "vi": "Mục hai khảo sát vị trí phân bố bó mạch: Ở rễ cây hai lá mầm, bó mạch tập trung thành một trụ đặc ở chính giữa, với mạch gỗ xếp thành hình chữ thập ở trung tâm giúp cây bám chắc vào đất chống lại lực kéo bật gốc, xen kẽ là các bó mạch rây. Ở thân cây hai lá mầm, các bó mạch xếp thành một vòng tròn đồng tâm ở ngoại vi, mạch gỗ quay vào trong lõi và mạch rây quay ra phía vỏ, giúp thân cây mềm dẻo chống lại lực uốn cong của gió bão. Ở lá cây, các bó mạch tạo thành gân lá với mạch gỗ nằm ở phía trên."
        },
        {
            "id": "sec_transpiration",
            "title": "3. Dòng Thoát hơi nước & Lực kéo Thoát hơi nước (Transpiration)",
            "selector": "#sec-transpiration",
            "en": "Section 3 investigates Transpiration: the loss of water vapor from plant leaves by evaporation from the surfaces of mesophyll cells into air spaces, followed by diffusion out through open stomata down a water potential gradient. This creates a transpirational pull, drawing a continuous column of water upwards through xylem vessels by cohesive hydrogen bonding between water molecules and adhesive forces to xylem walls. Environmental factors accelerating transpiration include higher temperatures, faster wind speed, brighter light opening stomata, and drier ambient air with lower humidity.",
            "vi": "Mục ba nghiên cứu Thoát hơi nước (Transpiration): là sự mất hơi nước từ lá cây qua quá trình bay hơi từ bề mặt tế bào mô giậu vào các khoảng gian bào, sau đó khuếch tán ra ngoài qua lỗ khí khổng xuôi theo gradient thế nước. Quá trình này tạo ra lực kéo thoát hơi nước (transpirational pull), kéo theo một cột nước liên tục dâng lên trong mạch gỗ nhờ lực liên kết hydro giữa các phân tử nước (cohesion) và lực bám dính vào thành mạch (adhesion). Các yếu tố môi trường đẩy nhanh tốc độ thoát hơi nước gồm nhiệt độ cao, gió mạnh thổi bạt lớp ẩm, ánh sáng kích thích mở khí khổng và độ ẩm không khí xung quanh thấp."
        },
        {
            "id": "sec_translocation",
            "title": "4. Vận chuyển Chất hữu cơ: Từ Nguồn đến Đích (Translocation)",
            "selector": "#sec-translocation",
            "en": "Section 4 explains Translocation: the movement of sucrose and amino acids in phloem from regions of production, called Sources, to regions of utilization or storage, called Sinks. In spring, photosynthetic leaves act as primary sources exporting sucrose to growing flower buds and root storage sinks. In early spring before bud burst, storage organs like potato tubers act as sources converting starch back into sucrose, translocating it to growing shoots acting as sinks.",
            "vi": "Mục bốn phân tích Vận chuyển Chất hữu cơ (Translocation): là quá trình vận chuyển đường sucrose và axit amin trong mạch rây từ nơi sản xuất (Nguồn - Sources) đến nơi tiêu thụ hoặc dự trữ (Đích - Sinks). Vào mùa hè, lá quang hợp đóng vai trò là cơ quan Nguồn vận chuyển sucrose đến nụ hoa và rễ củ. Vào đầu mùa xuân khi cây chưa ra lá, các cơ quan dự trữ như củ khoai tây lại chuyển hóa tinh bột ngược thành sucrose và đóng vai trò là Nguồn, vận chuyển dưỡng chất nuôi các chồi non đóng vai trò là Đích."
        }
    ]

    major_sections = [
        {"id": "sec_xylem_phloem", "title": "1. Cấu tạo Mạch gỗ & Mạch rây"},
        {"id": "sec_vascular_position", "title": "2. Phân bố Bó mạch ở Rễ, Thân & Lá"},
        {"id": "sec_transpiration", "title": "3. Thoát hơi nước (Transpiration Stream)"},
        {"id": "sec_translocation", "title": "4. Vận chuyển Từ Nguồn đến Đích (Translocation)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B8 successfully built!")


# ==============================================================================
# TOPIC B9: Transport in animals
# ==============================================================================
async def build_b9():
    lid = 'a79dd569-671f-4559-84a3-eee1e6018172'
    code = 'b9'
    title = 'B9: Transport in animals'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-circulation-system" class="lecture-interactive-card" data-lecture-section="sec_circulation_system" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-heart-anatomy" class="lecture-interactive-card" data-lecture-section="sec_heart_anatomy" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-chd" class="lecture-interactive-card" data-lecture-section="sec_chd" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-vessels-blood" class="lecture-interactive-card" data-lecture-section="sec_vessels_blood" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B9 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B9: Hệ Tuần hoàn Động vật & Tim mạch",
            "selector": "#sec-header",
            "en": "Welcome to Topic B9: Transport in animals. Large multicellular mammals require a rapid internal convective system to circulate oxygen, glucose, hormones, and wastes. In this chapter, we contrast single and double circulation, examine the mammalian heart anatomy and cardiac cycle, explore Coronary Heart Disease pathogenesis, and investigate blood vessels and blood components.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B9: Hệ Tuần hoàn ở Động vật và Tim mạch. Động vật có vú đa bào cần hệ tuần hoàn đối lưu nhanh chóng để vận chuyển oxy, glucose, hormone và chất thải. Trong bài học này, chúng ta sẽ so sánh vòng tuần hoàn đơn và kép, giải phẫu tim người, bệnh mạch vành (CHD) cùng cấu trúc mạch máu và các thành phần tế bào máu."
        },
        {
            "id": "sec_circulation_system",
            "title": "1. Tuần hoàn Đơn vs Tuần hoàn Kép (Circulatory Systems)",
            "selector": "#sec-circulation-system",
            "en": "Section 1 compares circulatory architectures: Fish possess a single circulatory system, where blood pumps once through a two-chambered heart to gill capillaries, losing pressure before slowly irrigating systemic tissues. Mammals possess a double circulatory system: blood passes twice through a four-chambered heart in one complete circuit. The pulmonary circuit pumps deoxygenated blood under low pressure to lungs, while the systemic circuit re-pumps newly oxygenated blood under high pressure to body organs, maximizing metabolic rate.",
            "vi": "Mục một so sánh các hệ tuần hoàn: Cá có hệ tuần hoàn đơn, máu chỉ đi qua quả tim 2 ngăn một lần trong một chu trình, máu qua mao mạch mang bị sụt giảm áp lực nghiêm trọng trước khi chảy chậm đến các mô. Động vật có vú sở hữu hệ tuần hoàn kép: máu đi qua tim 4 ngăn hai lần trong một vòng tuần hoàn hoàn chỉnh. Vòng tuần hoàn phổi bơm máu nghèo oxy dưới áp lực thấp đến phổi trao đổi khí, sau đó vòng tuần hoàn hệ thống bơm máu giàu oxy dưới áp lực rất cao đến toàn cơ thể, đảm bảo tốc độ trao đổi chất tối đa."
        },
        {
            "id": "sec_heart_anatomy",
            "title": "2. Cấu tạo Tim Người & Chu kỳ Hoạt động của Tim",
            "selector": "#sec-heart-anatomy",
            "en": "Section 2 investigates mammalian heart anatomy: The right side receives deoxygenated blood from the vena cava into the right atrium, pumping it through the tricuspid atrioventricular valve into the right ventricle, and out the pulmonary artery to lungs. The left side receives oxygenated blood from pulmonary veins into the left atrium, through the bicuspid valve into the thick, highly muscular left ventricle, which contracts powerfully to force blood out the aorta to the systemic circulation. Crucially, the left ventricle wall is three times thicker than the right because it must generate sufficient hydrostatic pressure to overcome systemic peripheral resistance throughout the body.",
            "vi": "Mục hai khảo sát giải phẫu tim người: Nửa tim bên phải nhận máu nghèo oxy từ tĩnh mạch chủ vào tâm nhĩ phải, đẩy qua van ba lá xuống tâm thất phải rồi bơm qua động mạch phổi lên phổi. Nửa tim bên trái nhận máu giàu oxy từ tĩnh mạch phổi vào tâm nhĩ trái, đẩy qua van hai lá xuống tâm thất trái có thành cơ rất dày, co bóp cực mạnh để tống máu vào động mạch chủ đi nuôi toàn thân. Điểm mấu chốt thi cử: thành tâm thất trái dày gấp 3 lần thành tâm thất phải vì phải tạo ra áp lực thủy tĩnh cực lớn để thắng lực cản ngoại vi của toàn bộ hệ thống mạch máu trong cơ thể."
        },
        {
            "id": "sec_chd",
            "title": "3. Bệnh Động mạch Vành (Coronary Heart Disease - CHD)",
            "selector": "#sec-chd",
            "en": "Section 3 analyzes Coronary Heart Disease: The heart muscle is supplied with oxygenated blood by coronary arteries branching off the aorta. Blockage of coronary arteries by fatty atheroma plaques restricts arterial diameter, causing ischemia and angina chest pain. If a thrombus clot forms, blood supply stops completely, causing myocardial infarction or heart attack. Major risk factors include diets high in saturated fats and salt, chronic cigarette smoking, obesity, lack of exercise, high stress, and genetic predisposition.",
            "vi": "Mục ba phân tích Bệnh động mạch vành (CHD): Cơ tim được nuôi dưỡng trực tiếp bởi các nhánh động mạch vành tách ra từ động mạch chủ. Sự tích tụ các mảng xơ vữa mỡ (atheroma) làm hẹp lòng mạch vành, làm thiếu máu cục bộ gây đau thắt ngực. Nếu hình thành cục máu đông bít kín hoàn toàn mạch máu, vùng cơ tim phía sau sẽ chết do hoại tử gây nhồi máu cơ tim. Các yếu tố nguy cơ hàng đầu gồm chế độ ăn nhiều mỡ bão hòa và muối, hút thuốc lá mãn tính, béo phì, lười vận động, căng thẳng và yếu tố di truyền."
        },
        {
            "id": "sec_vessels_blood",
            "title": "4. Mạch máu & Thành phần Máu (Blood Vessels & Components)",
            "selector": "#sec-vessels-blood",
            "en": "Section 4 contrasts vascular types and blood elements: Arteries carry blood away from heart under high fluctuating pressure with thick walls rich in elastic fibers and smooth muscle, and narrow lumens. Veins return blood to heart under low pressure with thinner walls, wide lumens, and semilunar valves to prevent backflow. Capillaries connect arteries and veins, having walls only one endothelial cell thick to minimize diffusion distance. Blood consists of 55% liquid plasma transporting dissolved nutrients, urea, carbon dioxide, and hormones; Red Blood Cells with hemoglobin transporting oxygen; White Blood Cells: phagocytes that ingest pathogens and lymphocytes producing antibodies; and Platelets that initiate blood clotting to seal wounds.",
            "vi": "Mục bốn so sánh các loại mạch và thành phần máu: Động mạch dẫn máu rời khỏi tim dưới áp lực rất cao với thành mạch dày giàu sợi đàn hồi và lớp cơ trơn, lòng mạch hẹp. Tĩnh mạch dẫn máu về tim dưới áp lực thấp với thành mỏng hơn, lòng mạch rộng và có các van bán nguyệt một chiều ngăn máu chảy ngược. Mao mạch nối giữa tiểu động mạch và tiểu tĩnh mạch với thành chỉ dày duy nhất một lớp tế bào nội mô để tối thiểu hóa khoảng cách khuếch tán. Máu gồm 55% huyết tương lỏng vận chuyển chất dinh dưỡng, urê, CO2 và hormone; hồng cầu chứa hemoglobin vận chuyển oxy; bạch cầu gồm thực bào bắt nuốt vi khuẩn và tế bào lympho tiết kháng thể; cùng tiểu cầu khởi phát đông máu bịt kín vết thương."
        }
    ]

    major_sections = [
        {"id": "sec_circulation_system", "title": "1. Vòng Tuần hoàn Đơn vs Kép"},
        {"id": "sec_heart_anatomy", "title": "2. Cấu tạo Tim & Chu kỳ Tim"},
        {"id": "sec_chd", "title": "3. Bệnh Động mạch Vành (CHD)"},
        {"id": "sec_vessels_blood", "title": "4. Mạch máu & Thành phần Máu"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B9 successfully built!")


# ==============================================================================
# TOPIC B10: Diseases and immunity
# ==============================================================================
async def build_b10():
    lid = '04d34896-13fb-411b-9e13-2bc3f9725136'
    code = 'b10'
    title = 'B10: Diseases and immunity'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-pathogens" class="lecture-interactive-card" data-lecture-section="sec_pathogens" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-immune-response" class="lecture-interactive-card" data-lecture-section="sec_immune_response" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-vaccination" class="lecture-interactive-card" data-lecture-section="sec_vaccination" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B10 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B10: Bệnh truyền nhiễm & Hệ Miễn dịch",
            "selector": "#sec-header",
            "en": "Welcome to Topic B10: Diseases and immunity. Living organisms constantly defend against microscopic invaders. In this lesson, we study pathogen transmission and bodily defenses, analyze antigen-antibody specificity and phagocytosis, and examine the cellular mechanics of vaccination and herd immunity.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B10: Bệnh truyền nhiễm và Hệ Miễn dịch. Cơ thể sống liên tục phải đối phó với sự xâm lăng của vi sinh vật gây bệnh. Trong bài học này, chúng ta sẽ khảo sát con đường lây truyền và hàng rào phòng thủ cơ thể, cơ chế kháng nguyên - kháng thể, hiện tượng thực bào và nguyên lý tiêm chủng vắc-xin cùng miễn dịch cộng đồng."
        },
        {
            "id": "sec_pathogens",
            "title": "1. Mầm bệnh, Đường lây truyền & Hàng rào Phòng thủ Cơ thể",
            "selector": "#sec-pathogens",
            "en": "Section 1 defines disease transmission: A Pathogen is a disease-causing organism, such as bacteria, viruses, fungi, or protoctists. A Transmissible disease is an illness whose pathogen can pass from one host to another directly via bodily fluids, or indirectly via contaminated surfaces, food, airborne respiratory droplets, or animal vectors. Mechanical defenses include unbroken skin and nostril hairs. Chemical defenses include hydrochloric acid in gastric juice destroying ingested microbes and lysozyme enzymes in tears.",
            "vi": "Mục một định nghĩa mầm bệnh và cơ chế lây truyền: Mầm bệnh (Pathogen) là sinh vật gây bệnh, bao gồm vi khuẩn, virus, nấm và sinh vật nguyên sinh. Bệnh truyền nhiễm là bệnh mà mầm bệnh có thể lây từ vật chủ này sang vật chủ khác trực tiếp qua tiếp xúc dịch thể hoặc gián tiếp qua bề mặt nhiễm bẩn, thức ăn, giọt bắn đường hô hấp hoặc sinh vật trung gian truyền bệnh. Hàng rào cơ học gồm lớp da nguyên vẹn và lông mũi cản bụi. Hàng rào hóa học gồm axit clohidric HCl trong dịch vị dạ dày tiêu diệt vi sinh vật và enzyme lysozyme trong nước mắt."
        },
        {
            "id": "sec_immune_response",
            "title": "2. Kháng nguyên, Kháng thể & Phản ứng Miễn dịch (Phagocytosis)",
            "selector": "#sec-immune-response",
            "en": "Section 2 investigates cellular immunity: Pathogens possess unique surface marker proteins called Antigens. Phagocytes provide non-specific defense by engulfing pathogens into vacuoles through phagocytosis and digesting them with intracellular lysosomal enzymes. Lymphocytes provide specific humoral defense: each lymphocyte produces specific Y-shaped Antibodies whose binding sites are precisely complementary to foreign antigens. Antibodies neutralize pathogens, cause them to agglutinate in clumps, and flag them for destruction by phagocytes.",
            "vi": "Mục hai nghiên cứu cơ chế miễn dịch tế bào: Mầm bệnh mang trên bề mặt các phân tử protein đặc thù gọi là Kháng nguyên (Antigens). Bạch cầu thực bào (Phagocytes) tạo hàng rào miễn dịch không đặc hiệu bằng cách bao vây và bắt nuốt mầm bệnh qua quá trình thực bào (phagocytosis), tiêu hóa chúng bằng enzyme lysozyme nội bào. Bạch cầu lympho (Lymphocytes) tạo miễn dịch dịch thể đặc hiệu: mỗi tế bào lympho sản sinh các phân tử Kháng thể (Antibodies) hình chữ Y có vị trí liên kết tương thích bổ sung chính xác với kháng nguyên lạ. Kháng thể vô hiệu hóa độc tố, làm kết tụ mầm bệnh thành từng cụm và đánh dấu để đại thực bào đến tiêu hủy."
        },
        {
            "id": "sec_vaccination",
            "title": "3. Cơ chế Tiêm chủng Vắc-xin & Miễn dịch Cộng đồng (Herd Immunity)",
            "selector": "#sec-vaccination",
            "en": "Section 3 explains active immunization: A Vaccine contains weakened, killed, or fragmented pathogens possessing harmless antigens. When injected, lymphocytes recognize these antigens, undergo clonal proliferation, and produce antibodies while establishing a population of long-lived Memory Cells. If the host encounters the live virulent pathogen later, memory cells rapidly differentiate, synthesizing massive quantities of specific antibodies before the pathogen can cause clinical symptoms. High vaccination rates create Herd Immunity, shielding vulnerable individuals who cannot be vaccinated.",
            "vi": "Mục ba giải thích cơ chế tiêm chủng chủ động: Vắc-xin chứa mầm bệnh đã bị làm yếu, bị bất hoạt hoặc các mảnh kháng nguyên vô hại. Khi tiêm vào cơ thể, bạch cầu lympho nhận diện kháng nguyên, tăng sinh dòng vô tính tiết kháng thể và đồng thời biệt hóa thành quần thể Tế bào Ghi nhớ (Memory Cells) tồn tại lâu dài. Khi cơ thể tái nhiễm mầm bệnh sống ngoài tự nhiên, các tế bào ghi nhớ lập tức nhân lên cực nhanh, sản xuất lượng kháng thể khổng lồ tiêu diệt mầm bệnh trước khi kịp phát tác triệu chứng. Tỷ lệ tiêm chủng cao tạo nên Miễn dịch Cộng đồng (Herd Immunity), bảo vệ những người có hệ miễn dịch yếu không thể tiêm phòng."
        }
    ]

    major_sections = [
        {"id": "sec_pathogens", "title": "1. Mầm bệnh & Hàng rào Phòng thủ"},
        {"id": "sec_immune_response", "title": "2. Kháng nguyên, Kháng thể & Thực bào"},
        {"id": "sec_vaccination", "title": "3. Cơ chế Tiêm chủng Vắc-xin"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B10 successfully built!")


# ==============================================================================
# MAIN BATCH 2 RUNNER (TOPICS B6 -> B10)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 2: TOPICS B6 -> B10")
    print("*******************************************************\n")
    
    await build_b6()
    await asyncio.sleep(2)
    
    await build_b7()
    await asyncio.sleep(2)
    
    await build_b8()
    await asyncio.sleep(2)
    
    await build_b9()
    await asyncio.sleep(2)
    
    await build_b10()
    
    print("\n*******************************************************")
    print("BATCH 2 COMPLETE: TOPICS B6 -> B10 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
