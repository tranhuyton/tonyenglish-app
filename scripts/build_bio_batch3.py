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
# TOPIC 10: Diseases and immunity
# ==============================================================================
async def build_10():
    lid = '62278d87-97ea-4fa5-aa46-748bca28db68'
    code = '10'
    title = 'Topic 10: Diseases and immunity'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🦠 1. PATHOGENS (Mầm bệnh)
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-pathogens" class="lecture-interactive-card" data-lecture-section="sec_pathogens" style="cursor: pointer; ')
    
    # h2[1]: 🛡️ 2. BODY'S DEFENCES AGAINST PATHOGENS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-body-defences" class="lecture-interactive-card" data-lecture-section="sec_body_defences" style="cursor: pointer; ')
    
    # h2[2]: 💉 3. ACTIVE AND PASSIVE IMMUNITY
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-immunity-vaccines" class="lecture-interactive-card" data-lecture-section="sec_immunity_vaccines" style="cursor: pointer; ')
    
    # h2[3]: 🌍 4. CONTROLLING THE SPREAD OF DISEASE
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-control-disease" class="lecture-interactive-card" data-lecture-section="sec_control_disease" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 10 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 10: Bệnh tật và Hệ Miễn dịch",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 10: Diseases and immunity. Pathogens pose constant threats to organism survival. In this critical topic, we examine pathogen transmission, primary non-specific body defences, active and passive immunity, vaccination mechanisms, and sanitary disease control.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 10: Bệnh tật và Hệ Miễn dịch. Các mầm bệnh luôn là mối đe dọa thường trực đối với cơ thể sống. Trong bài học này, chúng ta sẽ khảo sát con đường lây truyền mầm bệnh, các hàng rào phòng thủ tự nhiên của cơ thể, miễn dịch chủ động và thụ động, cơ chế tiêm chủng vaccine cùng các biện pháp kiểm soát vệ sinh dịch bệnh."
        },
        {
            "id": "sec_pathogens",
            "title": "1. Mầm bệnh & Các Con đường Lây truyền (Pathogens)",
            "selector": "#sec-pathogens",
            "en": "Section 1 defines a Pathogen: a disease-causing organism, encompassing viruses, bacteria, fungi, and protoctists. Transmissible diseases spread between hosts via direct contact—through blood, bodily fluids, or touch; or indirect transmission—via airborne respiratory droplets, contaminated food and drinking water, or animal insect vectors like mosquitoes.",
            "vi": "Mục một định nghĩa Mầm bệnh (Pathogen): là sinh vật gây bệnh, bao gồm virus, vi khuẩn, nấm và sinh vật đơn bào. Bệnh truyền nhiễm lây lan giữa các vật chủ qua tiếp xúc trực tiếp—qua máu, dịch tiết sinh học hoặc va chạm thể xác; hoặc qua đường gián tiếp—qua các giọt bắn đường hô hấp trong không khí, thức ăn và nguồn nước nhiễm bẩn, hoặc qua vật chủ trung gian truyền bệnh như muỗi."
        },
        {
            "id": "sec_body_defences",
            "title": "2. Các Hàng rào Phòng vệ của Cơ thể (Body Defences)",
            "selector": "#sec-body-defences",
            "en": "Section 2 investigates human protective barriers: Mechanical barriers include unbroken skin and nose hairs. Chemical barriers include sticky mucus secreted by goblet cells to trap dust and pathogens, swallowed into the stomach where hydrochloric acid destroys bacterial cell walls. Cellular defences feature phagocytes performing phagocytosis to engulf and digest microbes, and lymphocytes producing antibodies.",
            "vi": "Mục hai nghiên cứu các hàng rào bảo vệ của cơ thể: Hàng rào cơ học gồm làn da nguyên vẹn và lớp lông mũi cản bụi. Hàng rào hóa học gồm chất nhầy do tế bào hình đài tiết ra để giữ chặt mầm bệnh và bụi bẩn, sau đó được nuốt xuống dạ dày nơi axit clohydric HCl tiêu diệt vi khuẩn. Hàng rào tế bào gồm các đại thực bào thực hiện quá trình thực bào để nuốt trọn và phân giải vi khuẩn, cùng các tế bào lympho sản sinh kháng thể."
        },
        {
            "id": "sec_immunity_vaccines",
            "title": "3. Miễn dịch Chủ động, Thụ động & Cơ chế Vaccine",
            "selector": "#sec-immunity-vaccines",
            "en": "Section 3 compares immunity types: Active immunity is defense acquired by infection or vaccination, stimulating lymphocytes to produce specific antibodies and long-lived memory cells for permanent protection. Passive immunity provides short-term defense via imported antibodies—such as maternal antibodies crossed through the placenta or breast milk—giving immediate protection without generating memory cells.",
            "vi": "Mục ba so sánh các hình thức miễn dịch: Miễn dịch chủ động là khả năng phòng vệ có được sau khi nhiễm bệnh hoặc tiêm chủng, kích thích tế bào lympho sản xuất kháng thể đặc hiệu và các tế bào nhớ (memory cells) tồn tại lâu dài mang lại sự bảo vệ bền vững. Miễn dịch thụ động là sự bảo vệ ngắn hạn nhờ nhận kháng thể từ bên ngoài—như kháng thể của mẹ truyền qua nhau thai hoặc sữa mẹ—giúp cơ thể chống đỡ tức thì nhưng không tạo ra tế bào nhớ."
        },
        {
            "id": "sec_control_disease",
            "title": "4. Kiểm soát Sự lây lan của Dịch bệnh",
            "selector": "#sec-control-disease",
            "en": "Section 4 outlines public disease control: Clean water supplies treated with chlorine eliminate waterborne pathogens like cholera. Effective sewage treatment prevents wastewater contamination of drinking reservoirs. Rigorous personal hygiene—regular handwashing and thorough cooking of food—breaks transmission chains. Proper waste disposal and refrigeration deny breeding conditions for flies and bacterial colonies.",
            "vi": "Mục bốn phác thảo các biện pháp kiểm soát dịch bệnh cộng đồng: Cung cấp nguồn nước sạch được khử trùng bằng clo giúp loại bỏ các vi khuẩn gây bệnh tả đường ruột. Xử lý nước thải triệt để ngăn ngừa nguy cơ nhiễm bẩn nguồn nước sinh hoạt. Vệ sinh cá nhân nghiêm ngặt—rửa tay thường xuyên bằng xà phòng và ăn chín uống sôi—giúp bẻ gãy mắt xích lây truyền. Xử lý rác thải đúng cách và bảo quản thực phẩm trong tủ lạnh ngăn chặn ruồi nhặng và vi khuẩn sinh sôi."
        }
    ]

    major_sections = [
        {"id": "sec_pathogens", "title": "1. Mầm bệnh & Con đường lây truyền"},
        {"id": "sec_body_defences", "title": "2. Hàng rào Phòng vệ Cơ thể"},
        {"id": "sec_immunity_vaccines", "title": "3. Miễn dịch & Cơ chế Vaccine"},
        {"id": "sec_control_disease", "title": "4. Kiểm soát Lây lan Dịch bệnh"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 10 successfully built!")


# ==============================================================================
# TOPIC 11: Gas exchange in humans
# ==============================================================================
async def build_11():
    lid = 'da59c2b3-124f-4e25-8537-74059e74f9b0'
    code = '11'
    title = 'Topic 11: Gas exchange in humans'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🫁 1. FEATURES OF GAS EXCHANGE SURFACE
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-alveoli-features" class="lecture-interactive-card" data-lecture-section="sec_alveoli_features" style="cursor: pointer; ')
    
    # h2[1]: 🗺️ 2. PARTS OF THE RESPIRATORY SYSTEM
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-respiratory-anatomy" class="lecture-interactive-card" data-lecture-section="sec_respiratory_anatomy" style="cursor: pointer; ')
    
    # h2[2]: 🌬️ 3. VENTILATION (Cơ chế thông khí)
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-ventilation-breathing" class="lecture-interactive-card" data-lecture-section="sec_ventilation_breathing" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 11 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 11: Trao đổi Khí ở Người",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 11: Gas exchange in humans. Supplying oxygen and purging metabolic carbon dioxide requires specialized respiratory surfaces. In this lesson, we analyze alveoli adaptations, the anatomy of the respiratory tract, goblet and ciliated cells, ventilation mechanics, and the effects of exercise.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 11: Trao đổi Khí ở Người. Việc cung cấp oxy và loại bỏ carbon dioxide đòi hỏi bề mặt trao đổi khí chuyên hóa cao. Trong bài học này, chúng ta sẽ phân tích cấu tạo thích nghi của phế nang, giải phẫu đường hô hấp, tế bào lông rung và tế bào tiết nhầy, cơ chế thông khí hít vào - thở ra cùng tác động của vận động thể chất."
        },
        {
            "id": "sec_alveoli_features",
            "title": "1. Đặc điểm Thích nghi của Bề mặt Trao đổi Khí (Phế nang)",
            "selector": "#sec-alveoli-features",
            "en": "Section 1 examines alveoli adaptations for rapid gas exchange: Millions of microscopic alveoli provide an immense surface area. The alveolar wall is only one-cell thick, as are surrounding capillary walls, creating an ultra-short diffusion distance. A thin layer of moisture dissolves gases for diffusion. A dense network of blood capillaries maintains a steep concentration gradient.",
            "vi": "Mục một phân tích cấu tạo thích nghi của phế nang để tối ưu trao đổi khí: Hàng triệu phế nang li ti tạo nên diện tích bề mặt tiếp xúc khổng lồ. Thành phế nang và thành mao mạch bao quanh đều chỉ dày duy nhất một lớp tế bào, tạo ra khoảng cách khuếch tán cực ngắn. Lớp màng ẩm mỏng trên bề mặt giúp hòa tan khí oxy trước khi khuếch tán. Mạng mao mạch dày đặc liên tục đưa máu đi qua để duy trì độ dốc chênh lệch nồng độ cao."
        },
        {
            "id": "sec_respiratory_anatomy",
            "title": "2. Cấu tạo Hệ Hô hấp & Tế bào Lông rung",
            "selector": "#sec-respiratory-anatomy",
            "en": "Section 2 traces air pathway: Larynx, trachea supported by C-shaped cartilage rings, branching into two bronchi, multiple bronchioles, ending in alveolar clusters. The airway epithelium features goblet cells that secrete sticky mucus to trap inhaled dust and pathogens, and ciliated epithelial cells whose coordinated beating sweeps contaminated mucus upward towards the throat to be swallowed.",
            "vi": "Mục hai theo dõi luồng không khí: Khí quản được nâng đỡ bởi các vòng sụn hình chữ C chống xẹp lún, phân nhánh thành hai phế quản chính, các tiểu phế quản rồi tận cùng ở các chùm phế nang. Lớp biểu mô đường thở chứa tế bào hình đài tiết chất nhầy kết dính giữ bụi và vi khuẩn, cùng các tế bào biểu mô có lông rung phối hợp đập nhịp nhàng quét ngược lớp chất nhầy bẩn lên họng để nuốt xuống dạ dày."
        },
        {
            "id": "sec_ventilation_breathing",
            "title": "3. Cơ chế Thông khí (Hít vào - Thở ra) & Luyện tập",
            "selector": "#sec-ventilation-breathing",
            "en": "Section 3 analyzes ventilation mechanics: During inspiration, external intercostal muscles contract, ribs move up and out, diaphragm contracts and flattens; thorax volume increases, decreasing thoracic pressure below atmospheric pressure, drawing air into lungs. During expiration, external intercostals relax, ribs drop down and in, diaphragm relaxes and domes up; thorax volume decreases, raising internal pressure to force air out. During exercise, muscle cells respire faster, releasing carbon dioxide that lowers blood pH, triggering the brain to increase breathing rate and tidal depth.",
            "vi": "Mục ba phân tích cơ chế thông khí: Khi hít vào, cơ liên sườn ngoài co kéo xương sườn nâng lên và nở ra ngoài, cơ hoành co phẳng xuống; thể tích lồng ngực tăng làm áp suất bên trong giảm thấp hơn áp suất khí quyển, hút không khí tràn vào phổi. Khi thở ra, cơ liên sườn ngoài giãn, xương sườn hạ xuống, cơ hoành giãn cong lên hình vòm; thể tích khoang ngực giảm làm áp suất tăng ép đẩy khí ra ngoài. Khi vận động mạnh, hô hấp tế bào tăng tiết nhiều CO2 làm giảm pH máu, kích thích não bộ tăng nhịp thở và độ sâu của mỗi nhịp thở."
        }
    ]

    major_sections = [
        {"id": "sec_alveoli_features", "title": "1. Cấu tạo Thích nghi của Phế nang"},
        {"id": "sec_respiratory_anatomy", "title": "2. Giải phẫu Hệ Hô hấp & Lông rung"},
        {"id": "sec_ventilation_breathing", "title": "3. Cơ chế Hít vào - Thở ra & Vận động"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 11 successfully built!")


# ==============================================================================
# TOPIC 12: Respiration
# ==============================================================================
async def build_12():
    lid = 'fb098b77-64fa-463a-9829-64f5c9055de5'
    code = '12'
    title = 'Topic 12: Respiration'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    t_sec1 = '<span style="color: #0f172a; font-size: 26px; border-bottom: 3px solid #0ea5e9; padding-bottom: 10px;">⚡ 1. RESPIRATION (Hô hấp tế bào)</span>'
    r_sec1 = '<span id="sec-respiration-concept" class="lecture-interactive-card" data-lecture-section="sec_respiration_concept" style="color: #0f172a; font-size: 26px; border-bottom: 3px solid #0ea5e9; padding-bottom: 10px; cursor: pointer;">⚡ 1. RESPIRATION (Hô hấp tế bào)</span>'
    
    h3s = soup.find_all('h3')
    
    # h3[0]: 🔋 Uses of energy produced:
    t_h3_0 = str(h3s[0])
    r_h3_0 = t_h3_0.replace('<h3', '<h3 id="sec-energy-uses" class="lecture-interactive-card" data-lecture-section="sec_energy_uses" style="cursor: pointer; ')
    
    # h3[1]: 🌡️ Ảnh hưởng của nhiệt độ đến Hô hấp ở Nấm men (Yeast)
    t_h3_1 = str(h3s[1])
    r_h3_1 = t_h3_1.replace('<h3', '<h3 id="sec-yeast-respiration" class="lecture-interactive-card" data-lecture-section="sec_yeast_respiration" style="cursor: pointer; ')
    
    # h3[2]: 📊 Comparing Aerobic and Anaerobic Respiration
    t_h3_2 = str(h3s[2])
    r_h3_2 = t_h3_2.replace('<h3', '<h3 id="sec-aerobic-vs-anaerobic" class="lecture-interactive-card" data-lecture-section="sec_aerobic_vs_anaerobic" style="cursor: pointer; ')
    
    # h3[3]: ⚠️ Oxygen Debt (Nợ Oxy)
    t_h3_3 = str(h3s[3])
    r_h3_3 = t_h3_3.replace('<h3', '<h3 id="sec-oxygen-debt" class="lecture-interactive-card" data-lecture-section="sec_oxygen_debt" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_sec1, r_sec1, 1)\
                   .replace(t_h3_0, r_h3_0, 1)\
                   .replace(t_h3_1, r_h3_1, 1)\
                   .replace(t_h3_2, r_h3_2, 1)\
                   .replace(t_h3_3, r_h3_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 12 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 12: Hô hấp Tế bào (Respiration)",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 12: Respiration. Cellular respiration is the universal metabolic biochemical reaction sustaining every living cell. In this lesson, we study aerobic respiration, cellular energy uses, yeast fermentation, anaerobic respiration in muscles, and the physiological concept of oxygen debt.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 12: Hô hấp Tế bào. Hô hấp tế bào là phản ứng sinh hóa chuyển hóa năng lượng phổ quát nuôi dưỡng từng tế bào sống. Trong bài học này, chúng ta sẽ khảo sát hô hấp hiếu khí, các mục đích sử dụng năng lượng, lên men ở nấm men, hô hấp kị khí ở cơ vân và hiện tượng nợ dưỡng khí oxy."
        },
        {
            "id": "sec_respiration_concept",
            "title": "1. Bản chất của Hô hấp Tế bào & Phương trình Hiếu khí",
            "selector": "#sec-respiration-concept",
            "en": "Section 1 defines Respiration: the chemical reactions in cells that break down nutrient molecules and release energy for metabolism. Never confuse respiration with breathing! Aerobic respiration uses oxygen to break down glucose completely into carbon dioxide and water, releasing massive amounts of ATP energy: C6H12O6 plus six O2 yields six CO2 plus six H2O.",
            "vi": "Mục một định nghĩa Hô hấp tế bào: là chuỗi phản ứng hóa học diễn ra trong tế bào phân giải các phân tử chất dinh dưỡng để giải phóng năng lượng cho quá trình trao đổi chất. Tuyệt đối không nhầm lẫn hô hấp tế bào với động tác hít thở! Hô hấp hiếu khí sử dụng oxy để oxy hóa hoàn toàn glucose thành CO2 và nước, giải phóng lượng lớn năng lượng ATP: C6H12O6 cộng 6 O2 tạo ra 6 CO2 và 6 H2O."
        },
        {
            "id": "sec_energy_uses",
            "title": "Các Mục đích Sử dụng Năng lượng trong Cơ thể",
            "selector": "#sec-energy-uses",
            "en": "This section outlines biological uses of energy: Muscle contraction for locomotion; protein synthesis from amino acids; cell division by mitosis for tissue growth and repair; active transport of ions against concentration gradients; transmission of electrical nerve impulses; and maintaining constant internal body temperature in warm-blooded mammals.",
            "vi": "Phần này phác thảo các mục đích sử dụng năng lượng sinh học: Co cơ phục vụ vận động; tổng hợp protein từ các axit amin; phân chia tế bào nguyên phân giúp cơ thể tăng trưởng và làm lành vết thương; vận chuyển chủ động các chất ngược gradien nồng độ; dẫn truyền xung thần kinh; và duy trì thân nhiệt ổn định ở động vật hằng nhiệt."
        },
        {
            "id": "sec_yeast_respiration",
            "title": "Hô hấp Kị khí ở Nấm men (Lên men Rượu)",
            "selector": "#sec-yeast-respiration",
            "en": "This section explores anaerobic respiration in yeast: In the absence of oxygen, yeast cells respire glucose into ethanol and carbon dioxide, releasing a small amount of energy: C6H12O6 yields two C2H5OH plus two CO2. This fermentation underpins commercial bread making, where carbon dioxide bubbles cause dough to rise, and brewing alcoholic beverages.",
            "vi": "Phần này tìm hiểu hô hấp kị khí ở nấm men: Khi thiếu oxy, nấm men phân giải glucose thành rượu ethanol và khí carbon dioxide, giải phóng một lượng nhỏ năng lượng: C6H12O6 tạo ra 2 C2H5OH cộng 2 CO2. Quá trình lên men này là nền tảng của ngành làm bánh mì, trong đó bọt khí CO2 làm bột nở phồng xốp, và ngành công nghiệp sản xuất bia rượu."
        },
        {
            "id": "sec_aerobic_vs_anaerobic",
            "title": "So sánh Hô hấp Hiếu khí & Kị khí ở Cơ vân",
            "selector": "#sec-aerobic-vs-anaerobic",
            "en": "This section contrasts respiration modes: Aerobic respiration requires oxygen, breaks down glucose completely, and releases large energy yields. Anaerobic respiration in human muscle cells occurs during vigorous exercise when oxygen delivery falls behind demand. Glucose is incompletely broken down into lactic acid: C6H12O6 yields two lactic acid molecules, releasing significantly less energy per glucose.",
            "vi": "Phần này so sánh hai hình thức hô hấp: Hô hấp hiếu khí cần oxy, phân giải hoàn toàn glucose và giải phóng năng lượng lớn. Hô hấp kị khí ở cơ vân người xảy ra khi vận động cường độ cao mà lượng oxy cung cấp không đáp ứng kịp nhu cầu. Glucose bị phân giải dở dang thành axit lactic: C6H12O6 tạo ra 2 phân tử axit lactic, giải phóng ít năng lượng hơn rất nhiều trên mỗi phân tử glucose."
        },
        {
            "id": "sec_oxygen_debt",
            "title": "Hiện tượng Nợ Dưỡng khí (Oxygen Debt)",
            "selector": "#sec-oxygen-debt",
            "en": "Section 1.4 details Oxygen Debt: Lactic acid accumulation in muscles lowers tissue pH and causes muscle fatigue and cramp. During recovery after vigorous sprinting, heavy deep breathing persists to intake extra oxygen. This oxygen transports in blood to the liver, where it aerotoxically oxidizes toxic lactic acid back into carbon dioxide and water or converts it back into stored glycogen.",
            "vi": "Mục này phân tích Hiện tượng Nợ Oxy (Oxygen Debt): Sự tích tụ axit lactic làm giảm pH mô cơ, gây mỏi cơ và chuột rút. Sau khi chạy nước rút, ta vẫn phải tiếp tục thở dốc và sâu để bù đắp lượng oxy thiếu hụt. Lượng oxy này theo máu đưa axit lactic về gan để oxy hóa thành CO2 và nước hoặc tái tạo lại thành glycogen dự trữ."
        }
    ]

    major_sections = [
        {"id": "sec_respiration_concept", "title": "1. Hô hấp Tế bào & Phương trình Hiếu khí"},
        {"id": "sec_energy_uses", "title": "Mục đích sử dụng Năng lượng ATP"},
        {"id": "sec_yeast_respiration", "title": "Lên men Rượu ở Nấm men"},
        {"id": "sec_aerobic_vs_anaerobic", "title": "Hiếu khí vs Kị khí ở Cơ vân"},
        {"id": "sec_oxygen_debt", "title": "Hiện tượng Nợ Dưỡng khí (Oxygen Debt)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 12 successfully built!")


# ==============================================================================
# MAIN BATCH 3 RUNNER (TOPICS 10 -> 12)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING BIOLOGY BATCH 3: TOPICS 10 -> 12")
    print("*******************************************************\n")
    
    await build_10()
    await asyncio.sleep(2)
    
    await build_11()
    await asyncio.sleep(2)
    
    await build_12()
    
    print("\n*******************************************************")
    print("BIOLOGY BATCH 3 COMPLETE: TOPICS 10 -> 12 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
