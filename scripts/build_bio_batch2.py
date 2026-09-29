import os
import sys
import re
import json
import asyncio
from bs4 import BeautifulSoup
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC 6: Plant Nutrition
# ==============================================================================
async def build_6():
    lid = 'e7d6e813-b7b9-4038-9911-8b886978cd07'
    code = '6'
    title = 'Topic 6: Plant Nutrition'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🌱 1. THE EQUATION OF PHOTOSYNTHESIS
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-photosynthesis" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis" style="cursor: pointer; ')
    
    # h2[1]: ⚠️ 2. MINERAL REQUIREMENTS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-minerals" class="lecture-interactive-card" data-lecture-section="sec_minerals" style="cursor: pointer; ')
    
    # h2[2]: 🔬 3. INTERNAL LEAF STRUCTURE
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-leaf-structure" class="lecture-interactive-card" data-lecture-section="sec_leaf_structure" style="cursor: pointer; ')
    
    # h2[3]: 🥽 4. PAPER 6: INVESTIGATING PHOTOSYNTHESIS
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-photosynthesis-experiments" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis_experiments" style="cursor: pointer; ')
    
    # h2[4]: 📈 5. LIMITING FACTORS
    t_h2_4 = str(h2s[4])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-limiting-factors" class="lecture-interactive-card" data-lecture-section="sec_limiting_factors" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 6 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 6: Dinh dưỡng Thực vật & Quang hợp",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 6: Plant Nutrition. Plants are autotrophic organisms that synthesize their own food through photosynthesis. In this comprehensive lesson, we examine the photosynthesis equation, mineral nutrition, internal leaf adaptations, crucial Paper 6 starch investigations, and limiting factors.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 6: Dinh dưỡng Thực vật và Quang hợp. Thực vật là sinh vật tự dưỡng có khả năng tự tổng hợp chất hữu cơ qua quang hợp. Trong bài học này, chúng ta sẽ khảo sát phương trình quang hợp, nhu cầu khoáng chất, cấu tạo thích nghi của lá, các thí nghiệm tinh bột Paper 6 và các yếu tố giới hạn."
        },
        {
            "id": "sec_photosynthesis",
            "title": "1. Phương trình Quang hợp & Vai trò của Diệp lục",
            "selector": "#sec-photosynthesis",
            "en": "Section 1 defines Photosynthesis: the process by which plants synthesize carbohydrates from raw materials using energy from light. The balanced chemical equation is: six CO2 plus six H2O yields C6H12O6 plus six O2, catalyzed by light and chlorophyll. Chlorophyll in chloroplasts absorbs light energy and transfers it into chemical energy in synthesized glucose.",
            "vi": "Mục một định nghĩa Quang hợp: là quá trình thực vật tổng hợp carbohydrate từ các nguyên liệu thô sử dụng năng lượng ánh sáng. Phương trình hóa học cân bằng là: 6 phân tử CO2 kết hợp với 6 phân tử nước, dưới tác dụng của ánh sáng và chất diệp lục, tạo ra một phân tử glucose C6H12O6 và giải phóng 6 phân tử O2. Diệp lục hấp thụ quang năng và chuyển hóa thành hóa năng dự trữ trong glucose."
        },
        {
            "id": "sec_minerals",
            "title": "2. Nhu cầu Khoáng chất: Nitrat và Magie",
            "selector": "#sec-minerals",
            "en": "Section 2 investigates essential plant mineral ions: Nitrate ions supply nitrogen required to build amino acids and synthesized plant proteins; deficiency results in stunted growth and weak yellowing stems. Magnesium ions form the central core of the chlorophyll molecule; magnesium deficiency leads to chlorosis, turning leaves completely yellow between veins.",
            "vi": "Mục hai nghiên cứu các ion khoáng thiết yếu cho thực vật: Ion Nitrat cung cấp nguyên tố nitơ cần thiết để tạo nên axit amin và tổng hợp protein; thiếu nitrat làm cây còi cọc và thân cây vàng yếu. Ion Magie là nguyên tử trung tâm cấu tạo nên phân tử diệp lục; thiếu magie dẫn đến bệnh vàng lá (chlorosis), khiến phiến lá mất màu xanh chuyển sang màu vàng úa."
        },
        {
            "id": "sec_leaf_structure",
            "title": "3. Cấu tạo Bên trong của Lá (Internal Leaf Structure)",
            "selector": "#sec-leaf-structure",
            "en": "Section 3 analyzes internal leaf adaptations for maximum photosynthesis: The waxy cuticle prevents excessive water evaporation. The upper epidermis is transparent to let sunlight penetrate. The palisade mesophyll contains tightly packed columnar cells rich in chloroplasts. The spongy mesophyll features large air spaces for rapid carbon dioxide diffusion. The lower epidermis houses stomata regulated by guard cells.",
            "vi": "Mục ba phân tích cấu tạo thích nghi giải phẫu của lá: Lớp cutin sáp trong suốt chống thoát hơi nước quá mức. Biểu bì trên cho ánh sáng truyền qua. Tầng mô giậu chứa các tế bào hình trụ xếp thẳng đứng với mật độ lục lạp dày đặc nhất để đón ánh sáng. Tầng mô xốp có nhiều khoang rỗng chứa khí giúp khí CO2 khuếch tán nhanh. Biểu bì dưới chứa nhiều khí khổng được đóng mở bởi tế bào hạt đậu."
        },
        {
            "id": "sec_photosynthesis_experiments",
            "title": "4. Thí nghiệm Thực hành Quang hợp (Paper 6 Focus)",
            "selector": "#sec-photosynthesis-experiments",
            "en": "Section 4 details Paper 6 practical investigations: Before any photosynthesis experiment, plants must be de-starched by keeping them in darkness for forty-eight hours so existing starch is mobilized. To test a leaf for starch: boil in water to kill cells, boil in ethanol using an electric water bath to dissolve green chlorophyll, soften in warm water, then add yellow-brown iodine solution—turning blue-black indicates starch presence.",
            "vi": "Mục bốn trình bày các quy trình thực hành Paper 6: Trước khi làm thí nghiệm, cây phải được khử tinh bột (de-starching) bằng cách để trong bóng tối 48 giờ để tiêu thụ hết tinh bột cũ. Quy trình 4 bước thử tinh bột ở lá: đun sôi lá trong nước để phá hủy tế bào; đun cách thủy trong cồn để tẩy sạch chất diệp lục; nhúng nước ấm để làm mềm lá; và nhỏ dung dịch i-ốt màu nâu vàng—lá đổi sang màu xanh đen chứng tỏ có tinh bột quang hợp."
        },
        {
            "id": "sec_limiting_factors",
            "title": "5. Các Yếu tố Giới hạn Tốc độ Quang hợp",
            "selector": "#sec-limiting-factors",
            "en": "Section 5 examines Limiting Factors: an environmental condition in shortest supply that restricts the rate of a physiological process. The three major limiting factors are light intensity, carbon dioxide concentration, and ambient temperature. Commercial greenhouse growers enrich carbon dioxide, employ artificial lights, and maintain optimum temperatures to maximize crop yield.",
            "vi": "Mục năm phân tích các Yếu tố giới hạn: là điều kiện môi trường ở mức thấp nhất kìm hãm tốc độ của một quá trình sinh lý. Ba yếu tố giới hạn chính của quang hợp gồm cường độ ánh sáng, nồng độ CO2 và nhiệt độ môi trường. Các nhà kính nông nghiệp hiện đại chủ động sục thêm khí CO2, bổ sung đèn LED và duy trì nhiệt độ tối ưu để đạt năng suất cây trồng tối đa."
        }
    ]

    major_sections = [
        {"id": "sec_photosynthesis", "title": "1. Phương trình Quang hợp & Diệp lục"},
        {"id": "sec_minerals", "title": "2. Khoáng chất: Nitrat & Magie"},
        {"id": "sec_leaf_structure", "title": "3. Cấu tạo Bên trong của Lá"},
        {"id": "sec_photosynthesis_experiments", "title": "4. Thí nghiệm Tinh bột (Paper 6)"},
        {"id": "sec_limiting_factors", "title": "5. Các Yếu tố Giới hạn"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 6 successfully built!")


# ==============================================================================
# TOPIC 7: Human nutrition
# ==============================================================================
async def build_7():
    lid = '85f36013-879b-49a8-a531-69c245a9630e'
    code = '7'
    title = 'Topic 7: Human nutrition'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🥩 1. NUTRIENTS & A BALANCED DIET
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-balanced-diet" class="lecture-interactive-card" data-lecture-section="sec_balanced_diet" style="cursor: pointer; ')
    
    # h2[1]: ⚙️ 2. KEY DIGESTIVE PROCESSES
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-digestive-processes" class="lecture-interactive-card" data-lecture-section="sec_digestive_processes" style="cursor: pointer; ')
    
    # h2[2]: 👄 3. TYPES OF TEETH (Physical Digestion)
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-teeth" class="lecture-interactive-card" data-lecture-section="sec_teeth" style="cursor: pointer; ')
    
    # h2[3]: 🗺️ 4. ORGANS OF THE DIGESTIVE SYSTEM
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-digestive-organs" class="lecture-interactive-card" data-lecture-section="sec_digestive_organs" style="cursor: pointer; ')
    
    # h2[4]: 🧪 5. CHEMICAL DIGESTION & ENZYMES
    t_h2_4 = str(h2s[4])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-chemical-digestion" class="lecture-interactive-card" data-lecture-section="sec_chemical_digestion" style="cursor: pointer; ')
    
    # h2[5]: 🔬 6. ABSORPTION & ADAPTATIONS OF VILLI
    t_h2_5 = str(h2s[5])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-absorption-villi" class="lecture-interactive-card" data-lecture-section="sec_absorption_villi" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 7 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 7: Dinh dưỡng ở Người & Hệ Tiêu hóa",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 7: Human nutrition. This major topic explores a balanced diet, the six stages of food processing, mechanical digestion by specialized teeth, organs of the alimentary canal, digestive enzymes and bile, and the absorption adaptations of intestinal villi.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 7: Dinh dưỡng ở Người và Hệ Tiêu hóa. Bài học trọng tâm này nghiên cứu chế độ ăn cân bằng, 6 giai đoạn tiêu hóa thức ăn, vai trò của các loại răng, ống tiêu hóa, các enzyme và dịch mật, cùng cấu tạo thích nghi hấp thu của lông ruột."
        },
        {
            "id": "sec_balanced_diet",
            "title": "1. Chế độ Ăn Cân bằng & 7 Nhóm Dinh dưỡng",
            "selector": "#sec-balanced-diet",
            "en": "Section 1 defines a balanced diet containing all seven nutrient classes in correct proportions: carbohydrates, lipids, proteins, vitamins C and D, mineral calcium and iron, dietary fibre, and water. Deficiency diseases include scurvy from lack of vitamin C, rickets from lack of vitamin D or calcium, and anaemia from lack of iron.",
            "vi": "Mục một định nghĩa chế độ ăn cân bằng cung cấp đủ 7 nhóm dưỡng chất theo tỉ lệ thích hợp: carbohydrate, lipid, protein, vitamin C và D, khoáng chất canxi và sắt, chất xơ và nước. Các bệnh thiếu hụt gồm bệnh scorbut (chảy máu chân răng) do thiếu vitamin C, còi xương do thiếu vitamin D hoặc canxi, và thiếu máu do thiếu sắt."
        },
        {
            "id": "sec_digestive_processes",
            "title": "2. Các Giai đoạn của Quá trình Tiêu hóa",
            "selector": "#sec-digestive-processes",
            "en": "Section 2 outlines the six distinct digestive stages: Ingestion is taking food into the mouth. Mechanical digestion physically breaks down food into smaller pieces without chemical modification. Chemical digestion enzymatically breaks down large insoluble molecules into small soluble molecules. Absorption transports digested molecules into blood. Assimilation incorporates nutrients into cells. Egestion expels undigested waste as faeces.",
            "vi": "Mục hai hệ thống hóa 6 giai đoạn tiêu hóa: Thu nạp thức ăn (Ingestion) qua đường miệng. Tiêu hóa cơ học (Mechanical digestion) nghiền nhỏ thức ăn để tăng diện tích tiếp xúc. Tiêu hóa hóa học (Chemical digestion) sử dụng enzyme thủy phân phân tử lớn không tan thành phân tử nhỏ tan được. Hấp thụ (Absorption) chất dinh dưỡng vào máu. Đồng hóa (Assimilation) biến dưỡng chất thành tế bào cơ thể. Thải phân (Egestion) tống xuất chất cặn bã qua hậu môn."
        },
        {
            "id": "sec_teeth",
            "title": "3. Răng và Tiêu hóa Cơ học (Types of Teeth)",
            "selector": "#sec-teeth",
            "en": "Section 3 examines human dentition: Incisors have chisel-shaped blades for biting and cutting. Canines are pointed for tearing meat. Premolars and molars have broad cusped crowns for chewing and grinding food. Tooth decay occurs when mouth bacteria feed on trapped sugars, producing acidic secretions that dissolve hard enamel and dentine.",
            "vi": "Mục ba phân tích bộ răng người: Răng cửa sắc bén hình lưỡi đục dùng để cắn và cắt thức ăn. Răng nanh nhọn để xé thức ăn. Răng tiền hàm và răng hàm có bề mặt rộng nhiều múi để nghiền nát thức ăn. Sâu răng xảy ra khi vi khuẩn lên men đường đọng lại trên răng tạo ra axit ăn mòn lớp men và ngà răng."
        },
        {
            "id": "sec_digestive_organs",
            "title": "4. Các Cơ quan trong Hệ Tiêu hóa (Alimentary Canal)",
            "selector": "#sec-digestive-organs",
            "en": "Section 4 traces food through the alimentary canal: Food moves along the oesophagus via peristalsis—wave-like rhythmic contractions of circular and longitudinal muscles. The stomach secretes gastric juice with hydrochloric acid that kills harmful microorganisms and establishes an optimum low pH for pepsin protease.",
            "vi": "Mục bốn theo dõi hành trình thức ăn: Thức ăn di chuyển xuống thực quản nhờ nhu động ruột (peristalsis)—các làn sóng co bóp nhịp nhàng của lớp cơ vòng và cơ dọc. Dạ dày tiết dịch vị chứa axit clohydric HCl giúp tiêu diệt vi khuẩn gây bệnh và tạo môi trường axit pH thấp lý tưởng cho enzyme pepsin hoạt động."
        },
        {
            "id": "sec_chemical_digestion",
            "title": "5. Tiêu hóa Hóa học & Các Enzyme Tiêu hóa",
            "selector": "#sec-chemical-digestion",
            "en": "Section 5 details enzyme action: Amylase breaks down starch into maltose; maltase hydrolyzes maltose to glucose. Proteases break down proteins into amino acids. Lipase breaks down fats into fatty acids and glycerol. Bile, synthesized in the liver and stored in the gall bladder, neutralizes acidic stomach chyme and emulsifies large fat droplets into tiny droplets, vastly increasing surface area for lipase.",
            "vi": "Mục năm trình bày hoạt động của các enzyme: Amylase phân giải tinh bột thành maltose; maltase tiếp tục thủy phân maltose thành glucose. Protease phân giải protein thành các axit amin. Lipase phân giải chất béo thành axit béo và glycerol. Dịch mật do gan sản xuất và dự trữ ở túi mật giúp trung hòa axit dịch vị và nhũ tương hóa chất béo thành vô số hạt mỡ nhỏ li ti, làm tăng diện tích tiếp xúc cho enzyme lipase."
        },
        {
            "id": "sec_absorption_villi",
            "title": "6. Hấp thụ và Cấu tạo Thích nghi của Lông ruột (Villi)",
            "selector": "#sec-absorption-villi",
            "en": "Section 6 highlights the ileum adaptations: Millions of finger-like villi with microvilli provide a massive surface area. The epithelium is only one-cell thick for short diffusion distances. Extensive blood capillaries absorb glucose, amino acids, water, and minerals directly into the bloodstream, while central lacteals absorb fatty acids and glycerol into the lymphatic system.",
            "vi": "Mục sáu làm nổi bật sự thích nghi của hồi tràng: Hàng triệu lông ruột (villi) và vi nhung mao (microvilli) tạo ra diện tích hấp thu khổng lồ. Lớp biểu mô mỏng chỉ dày một lớp tế bào giúp rút ngắn khoảng cách khuếch tán. Mạng lưới mao mạch máu dày đặc hấp thu glucose, axit amin, nước và khoáng chất, trong khi mạch dưỡng trấp trung tâm (lacteal) hấp thu axit béo và glycerol vào hệ bạch huyết."
        }
    ]

    major_sections = [
        {"id": "sec_balanced_diet", "title": "1. Chế độ Ăn Cân bằng & 7 Nhóm Chất"},
        {"id": "sec_digestive_processes", "title": "2. Sáu Giai đoạn Tiêu hóa"},
        {"id": "sec_teeth", "title": "3. Răng & Tiêu hóa Cơ học"},
        {"id": "sec_digestive_organs", "title": "4. Ống Tiêu hóa & Nhu động Ruột"},
        {"id": "sec_chemical_digestion", "title": "5. Tiêu hóa Hóa học & Enzyme"},
        {"id": "sec_absorption_villi", "title": "6. Cấu tạo Lông ruột (Villi)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 7 successfully built!")


# ==============================================================================
# TOPIC 8: Transport in plants
# ==============================================================================
async def build_8():
    lid = '37f08657-58e8-4fad-8035-2d935e1259e8'
    code = '8'
    title = 'Topic 8: Transport in plants'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 💧 1. XYLEM AND PHLOEM (VASCULAR TISSUES)
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-vascular-tissues" class="lecture-interactive-card" data-lecture-section="sec_vascular_tissues" style="cursor: pointer; ')
    
    # h2[1]: 🗺️ 2. POSITION IN DICOTYLEDONOUS PLANTS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-vascular-position" class="lecture-interactive-card" data-lecture-section="sec_vascular_position" style="cursor: pointer; ')
    
    # h2[2]: 🌬️ 3. WATER UPTAKE & TRANSPIRATION
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-transpiration" class="lecture-interactive-card" data-lecture-section="sec_transpiration" style="cursor: pointer; ')
    
    # h2[3]: 🍯 4. TRANSLOCATION (PHLOEM TRANSPORT)
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-translocation" class="lecture-interactive-card" data-lecture-section="sec_translocation" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 8 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 8: Sự Vận chuyển Các chất ở Thực vật",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 8: Transport in plants. Vascular plants possess specialized transport tissues to distribute water, minerals, and organic sugars. In this lesson, we study xylem and phloem, their anatomical arrangements in roots and stems, transpiration mechanisms, and translocation between sources and sinks.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 8: Sự Vận chuyển Các chất ở Thực vật. Thực vật bậc cao có hệ thống mô dẫn chuyên hóa để phân phối nước, khoáng chất và đường hữu cơ. Trong bài học này, chúng ta sẽ khảo sát cấu tạo mạch gỗ và mạch rây, vị trí của chúng ở rễ và thân, cơ chế thoát hơi nước và dòng vận chuyển chất hữu cơ giữa nguồn và bể chứa."
        },
        {
            "id": "sec_vascular_tissues",
            "title": "1. Mô Dẫn: Mạch gỗ (Xylem) & Mạch rây (Phloem)",
            "selector": "#sec-vascular-tissues",
            "en": "Section 1 contrasts vascular tissues: Xylem vessels consist of hollow, non-living dead cells with lignified walls that provide mechanical support; they transport water and dissolved mineral ions upward from roots to leaves. Phloem tissues are living cells with perforated sieve plates and companion cells, carrying sucrose and amino acids bidirectionally throughout the plant.",
            "vi": "Mục một so sánh hai loại mô dẫn: Mạch gỗ (Xylem) gồm các tế bào chết rỗng ruột với thành tẩm lignin dày chịu lực tốt; chúng dẫn truyền nước và ion khoáng một chiều từ rễ lên lá. Mạch rây (Phloem) là các tế bào sống có bản rây thủng lỗ kèm theo tế bào đồng hành, vận chuyển đường sucrose và axit amin hai chiều đến khắp các cơ quan của cây."
        },
        {
            "id": "sec_vascular_position",
            "title": "2. Vị trí Mô dẫn ở Rễ, Thân và Lá",
            "selector": "#sec-vascular-position",
            "en": "Section 2 investigates vascular anatomy in dicotyledonous plants: In roots, xylem forms a central star or cross shape, with phloem pockets nestled between the arms to resist pulling forces. In stems, vascular bundles arrange in a perimeter ring near the outer cortex, with xylem located on the inside and phloem on the outside to withstand bending strains.",
            "vi": "Mục hai nghiên cứu sự phân bố mô dẫn ở thực vật hai lá mầm: Ở rễ, mạch gỗ tập trung thành hình chữ thập hoặc hình sao ở chính giữa, xen giữa là các bó mạch rây để tăng khả năng chống chịu lực kéo. Ở thân, các bó mạch xếp thành một vòng tròn đồng tâm gần vỏ ngoài, trong đó mạch gỗ nằm ở phía trong và mạch rây nằm ở phía ngoài để giúp thân đứng vững trước gió bão."
        },
        {
            "id": "sec_transpiration",
            "title": "3. Hút nước & Cơ chế Thoát hơi nước (Transpiration)",
            "selector": "#sec-transpiration",
            "en": "Section 3 defines Transpiration: the loss of water vapour from plant leaves by evaporation of water at the surfaces of mesophyll cells followed by diffusion of water vapour through stomata. This evaporation generates a negative suction tension known as Transpiration Pull, drawing continuous water columns through xylem vessels via cohesion between water molecules.",
            "vi": "Mục ba định nghĩa Thoát hơi nước: là sự mất hơi nước từ lá cây qua quá trình bay hơi từ bề mặt các tế bào thịt lá, sau đó khuếch tán ra ngoài qua khí khổng. Sự bay hơi này tạo ra lực hút thoát hơi nước (Transpiration Pull), kéo theo một cột nước liên tục dâng lên trong mạch gỗ nhờ lực liên kết giữa các phân tử nước và lực bám vào thành mạch."
        },
        {
            "id": "sec_translocation",
            "title": "4. Vận chuyển Chất hữu cơ: Dòng Mạch rây (Translocation)",
            "selector": "#sec-translocation",
            "en": "Section 4 defines Translocation: the movement of sucrose and amino acids in phloem from sources to sinks. Sources are regions of production or release, like photosynthesizing leaves. Sinks are regions of utilization or storage, like growing shoots, developing fruits, and root tubers. Notice the seasonal reversal: In early spring before buds open, root tubers act as sources supplying growing shoots.",
            "vi": "Mục bốn định nghĩa Dòng vận chuyển chất hữu cơ: là sự vận chuyển đường sucrose và axit amin trong mạch rây từ nguồn (sources) đến bể chứa (sinks). Nguồn là nơi sản xuất đường như lá quang hợp. Bể chứa là nơi tiêu thụ hoặc tích trữ như chồi non, hoa quả và củ. Bẫy đề thi mùa vụ: Vào đầu mùa xuân khi lá chưa mọc, củ dưới rễ đóng vai trò là nguồn giải phóng dinh dưỡng nuôi chồi non sinh trưởng."
        }
    ]

    major_sections = [
        {"id": "sec_vascular_tissues", "title": "1. Mạch gỗ (Xylem) & Mạch rây (Phloem)"},
        {"id": "sec_vascular_position", "title": "2. Vị trí Mô dẫn ở Rễ & Thân"},
        {"id": "sec_transpiration", "title": "3. Lực Hút Thoát Hơi Nước"},
        {"id": "sec_translocation", "title": "4. Translocation: Nguồn & Bể chứa"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 8 successfully built!")


# ==============================================================================
# TOPIC 9: Transport in animals
# ==============================================================================
async def build_9():
    lid = 'b50dd00a-e2b4-4dba-8b1d-3f679dadae74'
    code = '9'
    title = 'Topic 9: Transport in animals'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🩸 1. CIRCULATORY SYSTEMS (PUMP, VESSELS & VALVES)
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-circulatory-systems" class="lecture-interactive-card" data-lecture-section="sec_circulatory_systems" style="cursor: pointer; ')
    
    # h2[1]: ❤️ 2. MAMMALIAN HEART STRUCTURE & FUNCTION
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-heart-structure" class="lecture-interactive-card" data-lecture-section="sec_heart_structure" style="cursor: pointer; ')
    
    # h2[2]: 🍔 3. CORONARY HEART DISEASE (CHD)
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-chd" class="lecture-interactive-card" data-lecture-section="sec_chd" style="cursor: pointer; ')
    
    # h2[3]: 🧪 4. BLOOD VESSELS (ARTERIES, VEINS, CAPILLARIES)
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-blood-vessels" class="lecture-interactive-card" data-lecture-section="sec_blood_vessels" style="cursor: pointer; ')
    
    # h2[4]: 🩸 5. BLOOD COMPOSITION & CLOTTING MECHANISM
    t_h2_4 = str(h2s[4])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-blood-composition" class="lecture-interactive-card" data-lecture-section="sec_blood_composition" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 9 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 9: Hệ Tuần hoàn và Máu ở Động vật",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 9: Transport in animals. Large multicellular mammals require a specialized internal transport network. In this lesson, we study double circulatory systems, heart anatomy and cardiac cycle, coronary heart disease, vessel adaptations, and blood clotting mechanisms.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 9: Hệ Tuần hoàn và Máu ở Động vật. Các động vật đa bào bậc cao đòi hỏi một mạng lưới vận chuyển nội tại hiệu quả. Trong bài học này, chúng ta sẽ khảo sát hệ tuần hoàn kép, cấu tạo và chu kỳ hoạt động của tim, bệnh mạch vành CHD, các loại mạch máu và cơ chế đông máu."
        },
        {
            "id": "sec_circulatory_systems",
            "title": "1. Hệ Tuần hoàn Đơn và Kép (Single vs Double Circulation)",
            "selector": "#sec-circulatory-systems",
            "en": "Section 1 compares circulatory plans: Fish possess a single circulatory system where blood flows through a two-chambered heart once for each complete circuit. Mammals have a double circulatory system comprising a pulmonary circuit to the lungs and a systemic circuit to the body, maintaining elevated blood pressure to deliver oxygen and glucose rapidly to active tissues.",
            "vi": "Mục một so sánh hai sơ đồ tuần hoàn: Loài cá có hệ tuần hoàn đơn, máu chỉ đi qua quả tim 2 ngăn một lần trong mỗi vòng tuần hoàn hoàn chỉnh. Động vật có vú sở hữu hệ tuần hoàn kép gồm vòng tuần hoàn phổi và vòng tuần hoàn hệ thống nuôi cơ thể, duy trì áp lực máu cao để vận chuyển oxy và glucose nhanh chóng đến các tế bào hoạt động."
        },
        {
            "id": "sec_heart_structure",
            "title": "2. Cấu tạo và Hoạt động của Tim (Heart Anatomy)",
            "selector": "#sec-heart-structure",
            "en": "Section 2 investigates mammalian heart anatomy: The right atrium receives deoxygenated blood from the vena cava, pumping it through the tricuspid valve into the right ventricle, which ejects it into the pulmonary artery. The left atrium receives oxygenated blood from pulmonary veins, pumping it through the bicuspid valve into the thick-walled left ventricle, which generates powerful pressure to pump blood out through the aorta.",
            "vi": "Mục hai nghiên cứu cấu tạo giải phẫu tim: Tâm nhĩ phải nhận máu giàu CO2 từ tĩnh mạch chủ, bơm qua van 3 lá vào tâm thất phải để đẩy máu lên động mạch phổi. Tâm nhĩ trái nhận máu giàu oxy từ tĩnh mạch phổi, bơm qua van 2 lá vào tâm thất trái có thành cơ rất dày, tạo ra áp lực co bóp cực lớn để đẩy máu qua động mạch chủ đi nuôi toàn bộ cơ thể."
        },
        {
            "id": "sec_chd",
            "title": "3. Bệnh Mạch vành (Coronary Heart Disease - CHD)",
            "selector": "#sec-chd",
            "en": "Section 3 examines Coronary Heart Disease: The coronary arteries supply oxygen and glucose to the contracting heart muscle. If atheroma fatty plaques accumulate inside coronary arteries, blood flow is restricted, depriving cardiac muscle of oxygen and triggering a myocardial infarction or heart attack. Risk factors include high-fat diets, lack of exercise, smoking, chronic stress, and genetics.",
            "vi": "Mục ba phân tích Bệnh mạch vành CHD: Động mạch vành cung cấp oxy và glucose trực tiếp cho cơ tim hoạt động. Nếu các mảng xơ vữa chất béo tích tụ gây hẹp hoặc tắc nghẽn lòng mạch vành, cơ tim sẽ bị thiếu oxy dẫn đến hoại tử và gây ra cơn nhồi máu cơ tim. Các yếu tố nguy cơ chính gồm chế độ ăn nhiều mỡ động vật, lười vận động, hút thuốc lá, căng thẳng kéo dài và yếu tố di truyền."
        },
        {
            "id": "sec_blood_vessels",
            "title": "4. Phân biệt Động mạch, Tĩnh mạch và Mao mạch",
            "selector": "#sec-blood-vessels",
            "en": "Section 4 contrasts blood vessels: Arteries have thick muscular elastic walls and narrow lumens to withstand high pulsatile pressure from the heart. Veins have thinner walls, wide lumens, and semilunar valves that prevent backwards blood flow under low pressure. Capillaries have microscopic one-cell thick permeable walls allowing rapid diffusion of nutrients and metabolic wastes.",
            "vi": "Mục bốn phân biệt các loại mạch máu: Động mạch có thành cơ đàn hồi rất dày và lòng mạch hẹp để chịu được áp lực tống máu cao từ tim. Tĩnh mạch có thành mỏng hơn, lòng mạch rộng và có các van bán nguyệt giúp máu chảy một chiều về tim dưới áp suất thấp. Mao mạch có thành cực mỏng chỉ gồm một lớp tế bào nội mô giúp các chất dinh dưỡng và chất thải khuếch tán trao đổi dễ dàng."
        },
        {
            "id": "sec_blood_composition",
            "title": "5. Thành phần Máu & Cơ chế Đông máu",
            "selector": "#sec-blood-composition",
            "en": "Section 5 breaks down blood components: Plasma transports dissolved glucose, amino acids, urea, carbon dioxide, and hormones. Red blood cells lack nuclei and contain iron-rich haemoglobin for oxygen transport. White blood cells defend against pathogens—phagocytes engulf foreign microbes, while lymphocytes produce specific antibodies. Platelets release clotting factors, converting soluble fibrinogen into an insoluble fibrin mesh that traps blood cells to form a clot.",
            "vi": "Mục năm phân loại các thành phần của máu: Huyết tương vận chuyển các chất tan như glucose, axit amin, ure, CO2 và hormone. Hồng cầu hình đĩa lõm hai mặt không có nhân, chứa huyết sắc tố hemoglobin vận chuyển oxy. Bạch cầu thực bào tiêu hóa mầm bệnh, và tế bào lympho sản xuất kháng thể đặc hiệu. Tiểu cầu kích hoạt chuỗi đông máu, chuyển fibrinogen hòa tan thành mạng lưới sợi fibrin không tan giữ chặt các tế bào máu để bịt kín vết thương."
        }
    ]

    major_sections = [
        {"id": "sec_circulatory_systems", "title": "1. Hệ Tuần hoàn Đơn & Kép"},
        {"id": "sec_heart_structure", "title": "2. Cấu tạo & Hoạt động của Tim"},
        {"id": "sec_chd", "title": "3. Bệnh Mạch vành (CHD)"},
        {"id": "sec_blood_vessels", "title": "4. Động mạch, Tĩnh mạch, Mao mạch"},
        {"id": "sec_blood_composition", "title": "5. Thành phần Máu & Đông máu"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 9 successfully built!")


# ==============================================================================
# MAIN BATCH 2 RUNNER (TOPICS 6 -> 9)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING BIOLOGY BATCH 2: TOPICS 6 -> 9")
    print("*******************************************************\n")
    
    await build_6()
    await asyncio.sleep(2)
    
    await build_7()
    await asyncio.sleep(2)
    
    await build_8()
    await asyncio.sleep(2)
    
    await build_9()
    
    print("\n*******************************************************")
    print("BIOLOGY BATCH 2 COMPLETE: TOPICS 6 -> 9 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
