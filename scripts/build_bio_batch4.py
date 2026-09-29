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
# TOPIC 13: Excretion in humans
# ==============================================================================
async def build_13():
    lid = 'b8f0539e-9361-4ba4-a96e-74c106494ebe'
    code = '13'
    title = 'Topic 13: Excretion in humans'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🚽 1. EXCRETION & THE LIVER (Bài tiết và Gan)
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-excretion-liver" class="lecture-interactive-card" data-lecture-section="sec_excretion_liver" style="cursor: pointer; ')
    
    # h2[1]: 🩸 2. THE KIDNEYS (Cấu tạo Thận)
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-kidneys" class="lecture-interactive-card" data-lecture-section="sec_kidneys" style="cursor: pointer; ')
    
    # h2[2]: 🏥 3. KIDNEY FAILURE (Suy thận)
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-kidney-failure" class="lecture-interactive-card" data-lecture-section="sec_kidney_failure" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 13 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 13: Hệ Bài tiết ở Người & Cấu tạo Thận",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 13: Excretion in humans. Accumulation of metabolic wastes threatens cell viability. In this lesson, we study excretion definition, liver deamination of excess amino acids, nephron filtration and selective reabsorption in kidneys, and dialysis treatments for kidney failure.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 13: Hệ Bài tiết ở Người và Cấu tạo Thận. Sự tích tụ chất thải chuyển hóa đe dọa sự sống tế bào. Trong bài học này, chúng ta sẽ khảo sát định nghĩa bài tiết, quá trình khử amin tại gan, cơ chế lọc và tái hấp thu chọn lọc ở nephron thận cùng phương pháp chạy thận nhân tạo."
        },
        {
            "id": "sec_excretion_liver",
            "title": "1. Bài tiết & Quá trình Khử amin tại Gan (Deamination)",
            "selector": "#sec-excretion-liver",
            "en": "Section 1 defines Excretion: the removal of toxic materials and substances in excess of requirements from an organism. Excess dietary amino acids cannot be stored. The liver undergoes Deamination: the removal of the nitrogen-containing amino group from amino acids to form urea, while the remaining carbohydrate portion is converted into glycogen or respired for energy.",
            "vi": "Mục một định nghĩa Bài tiết: là quá trình đào thải các chất thải độc hại từ chuyển hóa tế bào và các chất dư thừa ra khỏi cơ thể. Cơ thể không thể dự trữ axit amin thừa. Gan thực hiện quá trình Khử amin (Deamination): tách nhóm amin chứa nitơ ra khỏi phân tử axit amin để tổng hợp thành ure bài tiết qua thận, phần còn lại chuyển thành glycogen dự trữ hoặc dùng cho hô hấp tế bào."
        },
        {
            "id": "sec_kidneys",
            "title": "2. Cấu tạo và Chức năng của Thận (Nephron & Filtration)",
            "selector": "#sec-kidneys",
            "en": "Section 2 investigates kidney anatomy: Blood enters via the renal artery into microscopic nephrons. Ultrafiltration occurs under high pressure across glomerulus capillaries into the Bowman's capsule, squeezing out water, glucose, urea, and salts, leaving large blood cells and proteins behind. In the kidney tubule, selective reabsorption retrieves all glucose by active transport, together with essential water by osmosis and salts, leaving urea and excess water to drain as urine via ureters into the bladder.",
            "vi": "Mục hai nghiên cứu giải phẫu và chức năng thận: Máu theo động mạch thận đi vào hàng triệu đơn vị thận (nephron). Quá trình Siêu lọc (Ultrafiltration) diễn ra dưới áp lực máu cao qua búi mao mạch cuộn vào nang Bowman, ép nước, glucose, ure và muối khoáng vào ống thận, giữ lại tế bào máu và protein lớn. Tiếp theo, quá trình Tái hấp thu chọn lọc vận chuyển chủ động 100% glucose, một phần nước qua thẩm thấu và muối khoáng cần thiết trở lại máu, phần nước tiểu chứa ure theo niệu quản đổ về bàng quang."
        },
        {
            "id": "sec_kidney_failure",
            "title": "3. Suy thận: Chạy thận Nhân tạo & Ghép thận",
            "selector": "#sec-kidney-failure",
            "en": "Section 3 compares treatments for kidney failure: Hemodialysis filters blood across a cellulose partially permeable membrane bathed in dialysis fluid with precise concentrations of glucose and ions but zero urea, driving urea out of blood by diffusion down its gradient. Kidney transplants provide permanent filtration, but require tissue matching and lifelong immunosuppressive drugs to prevent immune rejection.",
            "vi": "Mục ba so sánh các giải pháp điều trị suy thận: Chạy thận nhân tạo (Dialysis) lọc máu qua màng bán thấm ngâm trong dịch lọc có nồng độ glucose và muối khoáng chuẩn nhưng không chứa ure, giúp ure khuếch tán ra khỏi máu theo chênh lệch nồng độ. Ghép thận mang lại giải pháp lâu dài hơn, nhưng đòi hỏi sự tương thích mô kháng nguyên và người bệnh phải uống thuốc ức chế miễn dịch suốt đời để chống đào thải cơ quan ghép."
        }
    ]

    major_sections = [
        {"id": "sec_excretion_liver", "title": "1. Bài tiết & Khử Amin tại Gan"},
        {"id": "sec_kidneys", "title": "2. Siêu lọc & Tái hấp thu ở Thận"},
        {"id": "sec_kidney_failure", "title": "3. Điều trị Suy thận & Ghép thận"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 13 successfully built!")


# ==============================================================================
# TOPIC 14: Coordination and response
# ==============================================================================
async def build_14():
    lid = 'c9abc870-7cbd-4c7e-b6c9-2d6237ff7670'
    code = '14'
    title = 'Topic 14: Coordination and response'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 50px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🧠 1. NERVOUS SYSTEM & REFLEXES
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-nervous-reflexes" class="lecture-interactive-card" data-lecture-section="sec_nervous_reflexes" style="cursor: pointer; ')
    
    # h2[1]: 👁️ 2. SENSE ORGANS: THE EYE
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-eye-anatomy" class="lecture-interactive-card" data-lecture-section="sec_eye_anatomy" style="cursor: pointer; ')
    
    # h2[2]: 🧪 3. HORMONES & THE ENDOCRINE SYSTEM
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-endocrine-system" class="lecture-interactive-card" data-lecture-section="sec_endocrine_system" style="cursor: pointer; ')
    
    # h2[3]: 🌡️ 4. HOMEOSTASIS
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-homeostasis" class="lecture-interactive-card" data-lecture-section="sec_homeostasis" style="cursor: pointer; ')
    
    # h2[4]: 🌱 5. TROPIC RESPONSES
    t_h2_4 = str(h2s[4])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-plant-tropisms" class="lecture-interactive-card" data-lecture-section="sec_plant_tropisms" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 14 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 14: Điều hòa Hoạt động & Đáp ứng Sinh học",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 14: Coordination and response. Organisms maintain internal equilibrium and respond to dynamic external environments. In this rich chapter, we explore nervous reflexes, eye anatomy and accommodation, endocrine hormones, homeostasis and thermoregulation, and plant tropisms mediated by auxin.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 14: Điều hòa Hoạt động và Đáp ứng Sinh học. Sinh vật liên tục duy trì cân bằng nội môi và thích ứng với biến đổi của môi trường. Trong bài học này, chúng ta sẽ khảo sát phản xạ thần kinh, giải phẫu mắt và phản xạ điều tiết, hệ nội tiết, cân bằng thân nhiệt nội môi và tính hướng động ở thực vật qua hormone auxin."
        },
        {
            "id": "sec_nervous_reflexes",
            "title": "1. Hệ Thần kinh & Cung Phản xạ (Reflex Arc)",
            "selector": "#sec-nervous-reflexes",
            "en": "Section 1 outlines the nervous system: The Central Nervous System comprises the brain and spinal cord. Reflex arcs deliver rapid, automatic, and protective responses along a dedicated pathway: Stimulus excites Receptors, firing electrical impulses along Sensory Neurones across synapses to Relay Neurones in the spinal cord, onward through Motor Neurones to Effector muscles or glands.",
            "vi": "Mục một trình bày hệ thần kinh: Hệ thần kinh trung ương gồm não bộ và tủy sống. Cung phản xạ (Reflex Arc) mang lại các phản ứng tự động, cực nhanh và bảo vệ cơ thể theo một cung đường khép kín: Kích thích tác động lên Thụ thể, phát xung điện truyền qua Nơron hướng tâm cảm giác, vượt qua khe synapse đến Nơron trung gian tại tủy sống, truyền tiếp qua Nơron ly tâm vận động đến Cơ quan đáp ứng (cơ hoặc tuyến)."
        },
        {
            "id": "sec_eye_anatomy",
            "title": "2. Cơ quan Thị giác: Cấu tạo Mắt & Cơ chế Điều tiết",
            "selector": "#sec-eye-anatomy",
            "en": "Section 2 investigates eye anatomy and accommodation: The pupil reflex protects the retina from damage: In bright light, circular iris muscles contract and radial muscles relax, constricting the pupil. Accommodation focuses on near versus distant objects: For near objects, ciliary muscles contract, suspensory ligaments slacken, allowing the lens to become thicker and more convex, refracting light rays strongly onto the retina.",
            "vi": "Mục hai nghiên cứu cấu tạo mắt và phản xạ điều tiết: Phản xạ đồng tử bảo vệ võng mạc: Khi ánh sáng mạnh, cơ vòng mống mắt co, cơ nan hoa giãn làm co nhỏ con ngươi. Cơ chế điều tiết nhìn gần - nhìn xa: Khi nhìn vật ở gần, cơ thể mi co lại, các dây chằng treo giãn chùng ra, làm thể thủy tinh phồng dày và lồi hơn, khúc xạ ánh sáng mạnh hơn hội tụ chính xác trên võng mạc."
        },
        {
            "id": "sec_endocrine_system",
            "title": "3. Hệ Nội tiết & Hooc-môn (Adrenaline Focus)",
            "selector": "#sec-endocrine-system",
            "en": "Section 3 defines a Hormone: a chemical substance produced by an endocrine gland, carried by blood plasma, which alters the activity of one or more specific target organs. Adrenaline, released by adrenal glands during flight-or-flight emergencies, increases heart rate, dilates breathing airways, and stimulates glycogen breakdown into glucose, equipping muscles for rapid action.",
            "vi": "Mục ba định nghĩa Hooc-môn (Hormone): là chất hóa học do tuyến nội tiết tiết ra, vận chuyển qua huyết tương trong máu, làm biến đổi hoạt động sinh lý của một hoặc nhiều cơ quan đích xác định. Hooc-môn Adrenaline do tuyến thượng thận tiết ra trong trạng thái chiến-hay-chạy (fight or flight), làm tăng nhịp tim, giãn phế quản và chuyển hóa glycogen ở gan thành glucose cung cấp năng lượng tức thì cho cơ bắp."
        },
        {
            "id": "sec_homeostasis",
            "title": "4. Cân bằng Nội môi: Đường huyết & Điều nhiệt",
            "selector": "#sec-homeostasis",
            "en": "Section 4 defines Homeostasis: the maintenance of a constant internal environment via negative feedback. Blood glucose homeostasis is governed by the pancreas: High glucose triggers insulin release to store glucose as glycogen in liver cells; low glucose triggers glucagon to release stored glucose. Thermoregulation in skin counters cold via vasoconstriction, shivering, and erecting hairs, and counters heat via vasodilation and sweat evaporation.",
            "vi": "Mục bốn định nghĩa Cân bằng nội môi (Homeostasis): là sự duy trì môi trường bên trong cơ thể luôn ổn định thông qua cơ chế điều hòa ngược âm tính. Kiểm soát đường huyết do tuyến tụy đảm nhận: Khi đường huyết tăng cao, tụy tiết insulin chuyển glucose thành glycogen dự trữ tại gan; khi đường huyết hạ, tụy tiết glucagon chuyển ngược glycogen thành glucose. Điều hòa thân nhiệt tại da đối phó với trời lạnh bằng co mạch ngoại vi, run cơ và dựng lông; đối phó với trời nóng bằng giãn mạch và thoát mồ hôi."
        },
        {
            "id": "sec_plant_tropisms",
            "title": "5. Hướng động ở Thực vật & Hooc-môn Auxin",
            "selector": "#sec-plant-tropisms",
            "en": "Section 5 examines Plant Tropisms: directional growth responses to stimuli. Phototropism is response to light; gravitropism is response to gravity. Auxin, synthesized at shoot tips, stimulates cell elongation. In shoots, unilateral light drives auxin to the shaded side, causing shaded cells to elongate more rapidly than illuminated cells, bending the shoot towards the light.",
            "vi": "Mục năm nghiên cứu Tính hướng động ở thực vật: là phản ứng sinh trưởng định hướng trước kích thích môi trường. Hướng sáng (Phototropism) hướng về ánh sáng; hướng trọng lực (Gravitropism) theo chiều trọng trường. Hooc-môn thực vật Auxin sinh ra ở đỉnh chồi kích thích tế bào dãn dài. Khi chiếu sáng từ một phía, auxin di chuyển tập trung ở phía bóng râm, kích thích các tế bào bên tối sinh trưởng dài nhanh hơn bên sáng, làm ngọn cây uốn cong về phía có ánh sáng."
        }
    ]

    major_sections = [
        {"id": "sec_nervous_reflexes", "title": "1. Hệ Thần kinh & Cung Phản xạ"},
        {"id": "sec_eye_anatomy", "title": "2. Cấu tạo Mắt & Phản xạ Điều tiết"},
        {"id": "sec_endocrine_system", "title": "3. Hệ Nội tiết & Adrenaline"},
        {"id": "sec_homeostasis", "title": "4. Cân bằng Nội môi & Điều nhiệt"},
        {"id": "sec_plant_tropisms", "title": "5. Hướng động & Hooc-môn Auxin"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 14 successfully built!")


# ==============================================================================
# TOPIC 15: Drugs
# ==============================================================================
async def build_15():
    lid = 'f87b29a1-56a3-4668-a249-ed9f118d31d8'
    code = '15'
    title = 'Topic 15: Drugs'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 💊 1. WHAT IS A DRUG?
    t_h2_0 = str(h2s[0]).replace('<br/>', '<br>') if '<br/>' in str(h2s[0]) and str(h2s[0]) not in html else str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-what-is-drug" class="lecture-interactive-card" data-lecture-section="sec_what_is_drug" style="cursor: pointer; ')
    
    # h2[1]: 🦠 2. ANTIBIOTICS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-antibiotics" class="lecture-interactive-card" data-lecture-section="sec_antibiotics" style="cursor: pointer; ')
    
    # h2[2]: 🧬 3. ANTIBIOTIC RESISTANCE & MRSA
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-antibiotic-resistance" class="lecture-interactive-card" data-lecture-section="sec_antibiotic_resistance" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 15 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 15: Thuốc và Chất Dược lý (Drugs)",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 15: Drugs. Pharmacological substances profoundly alter human physiology. In this topic, we unpack the definition of drugs, medicinal versus recreational uses, antibiotic mechanisms against bacterial cell walls, the critical reason antibiotics cannot destroy viruses, and the global crisis of MRSA antibiotic resistance.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 15: Thuốc và Chất Dược lý. Các chất dược lý có tác động sâu sắc đến sinh lý cơ thể người. Trong bài học này, chúng ta sẽ tìm hiểu định nghĩa thuốc, thuốc điều trị và chất gây nghiện, cơ chế tiêu diệt vi khuẩn của kháng sinh, lý do vì sao kháng sinh vô dụng trước virus cùng hiểm họa kháng kháng sinh của siêu vi khuẩn MRSA."
        },
        {
            "id": "sec_what_is_drug",
            "title": "1. Định nghĩa Thuốc & Phân loại Dược phẩm",
            "selector": "#sec-what-is-drug",
            "en": "Section 1 defines a Drug: any substance taken into the body that modifies or affects chemical reactions in the body. Medicinal drugs, like analgesics and antibiotics, treat symptoms or cure infections. Misused recreational drugs, including alcohol and tobacco, trigger psychological addiction, physical tolerance, withdrawal symptoms, and severe long-term organ pathology like liver cirrhosis.",
            "vi": "Mục một định nghĩa Thuốc (Drug): là bất kỳ chất nào khi đưa vào cơ thể làm biến đổi hoặc ảnh hưởng đến các phản ứng hóa học chuyển hóa bên trong cơ thể. Thuốc chữa bệnh như thuốc giảm đau và kháng sinh giúp điều trị triệu chứng hoặc tiêu diệt mầm bệnh. Các chất gây nghiện bị lạm dụng như rượu và thuốc lá dẫn đến nghiện ngập tâm thần, hiện tượng lờn thuốc, hội chứng cai và hủy hoại cơ quan nội tạng lâu dài như xơ gan."
        },
        {
            "id": "sec_antibiotics",
            "title": "2. Kháng sinh & Lý do Vô dụng trước Virus",
            "selector": "#sec-antibiotics",
            "en": "Section 2 investigates Antibiotics: chemical substances that kill or inhibit bacteria without harming human host cells. For instance, penicillin disrupts bacterial cell wall synthesis during binary fission, causing osmotic lysis. Crucial Cambridge exam fact: Antibiotics are completely ineffective against viruses because viruses have no cell wall, no cell membrane, and no cell machinery, reproducing solely inside host cells.",
            "vi": "Mục hai nghiên cứu Thuốc kháng sinh (Antibiotics): là các hợp chất hóa học tiêu diệt hoặc ức chế vi khuẩn mà không làm tổn hại đến tế bào cơ thể người. Ví dụ, penicillin ngăn chặn vi khuẩn tổng hợp thành tế bào khi phân chia, khiến vi khuẩn trương phồng và vỡ do áp suất thẩm thấu. Điểm thi Cambridge then chốt: Kháng sinh hoàn toàn vô dụng trước virus vì virus không có thành tế bào, không có màng sinh chất và không có bộ máy trao đổi chất độc lập, chúng chỉ nhân lên ký sinh bên trong tế bào vật chủ."
        },
        {
            "id": "sec_antibiotic_resistance",
            "title": "3. Sự Kháng Kháng sinh & Siêu vi khuẩn MRSA",
            "selector": "#sec-antibiotic-resistance",
            "en": "Section 3 analyzes Antibiotic Resistance: Random genetic mutations produce rare resistant bacteria. When antibiotics are overused or patients fail to finish prescribed courses, non-resistant strains perish while resistant mutants survive and multiply unchecked—an acute example of natural selection. Strains like MRSA resist multiple antibiotics. Prevention mandates completing full courses and strictly limiting unnecessary prescriptions.",
            "vi": "Mục ba phân tích Hiện tượng Kháng Kháng sinh: Các đột biến gen ngẫu nhiên tạo ra các cá thể vi khuẩn kháng thuốc. Khi kháng sinh bị lạm dụng hoặc bệnh nhân tự ý bỏ thuốc không uống hết liều, các vi khuẩn nhạy cảm sẽ bị tiêu diệt trong khi vi khuẩn đột biến kháng thuốc sống sót và sinh sôi nhanh chóng—đây là minh chứng sống động của chọn lọc tự nhiên. Các chủng siêu vi khuẩn như MRSA kháng được hầu hết các loại kháng sinh thông thường. Biện pháp phòng ngừa đòi hỏi phải uống đủ liều theo đơn và hạn chế tối đa kê đơn kháng sinh không cần thiết."
        }
    ]

    major_sections = [
        {"id": "sec_what_is_drug", "title": "1. Định nghĩa Thuốc & Phân loại"},
        {"id": "sec_antibiotics", "title": "2. Kháng sinh & Vì sao Vô dụng với Virus"},
        {"id": "sec_antibiotic_resistance", "title": "3. Kháng Kháng sinh & Siêu vi khuẩn MRSA"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 15 successfully built!")


# ==============================================================================
# TOPIC 16: Reproduction
# ==============================================================================
async def build_16():
    lid = '936affb8-f062-4e39-b415-cc3794fb341e'
    code = '16'
    title = 'Topic 16: Reproduction'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🔄 1. ASEXUAL VS SEXUAL REPRODUCTION
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-asexual-vs-sexual" class="lecture-interactive-card" data-lecture-section="sec_asexual_vs_sexual" style="cursor: pointer; ')
    
    # h2[1]: 🌺 2. SEXUAL REPRODUCTION IN PLANTS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-plant-reproduction" class="lecture-interactive-card" data-lecture-section="sec_plant_reproduction" style="cursor: pointer; ')
    
    # h2[2]: 👶 3. HUMAN REPRODUCTION
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-human-reproduction" class="lecture-interactive-card" data-lecture-section="sec_human_reproduction" style="cursor: pointer; ')
    
    # h2[3]: 📈 4. THE MENSTRUAL CYCLE
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-menstrual-cycle" class="lecture-interactive-card" data-lecture-section="sec_menstrual_cycle" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 16 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 16: Sinh sản & Chu kỳ Kinh nguyệt",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 16: Reproduction. Reproduction ensures the perpetuation of species. In this comprehensive lesson, we contrast asexual and sexual reproduction, examine flower adaptations and pollination, study human reproductive physiology and placental exchange, and master the hormonal control of the menstrual cycle.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 16: Sinh sản và Chu kỳ Kinh nguyệt. Sinh sản đảm bảo sự trường tồn của loài. Trong bài học này, chúng ta sẽ so sánh sinh sản vô tính và hữu tính, cấu tạo hoa và sự thụ phấn, sinh lý sinh sản người và vai trò nhau thai, cùng cơ chế điều hòa hormone trong chu kỳ kinh nguyệt."
        },
        {
            "id": "sec_asexual_vs_sexual",
            "title": "1. So sánh Sinh sản Vô tính và Hữu tính",
            "selector": "#sec-asexual_vs_sexual",
            "en": "Section 1 contrasts reproduction modes: Asexual reproduction involves a single parent, produces genetically identical offspring (clones) via mitosis without gamete fusion, allowing rapid colonisation of favorable habitats. Sexual reproduction involves the fusion of haploid male and female gamete nuclei to form a diploid zygote via fertilisation, creating genetic variation that equips populations to adapt to fluctuating environments.",
            "vi": "Mục một so sánh hai hình thức sinh sản: Sinh sản vô tính chỉ có một cơ thể mẹ, tạo ra các thế hệ con giống hệt nhau về mặt di truyền (dòng vô tính) qua nguyên phân mà không có sự kết hợp giao tử, giúp nhân giống cực nhanh trong điều kiện thuận lợi. Sinh sản hữu tính là sự dung hợp nhân giữa giao tử đơn bội đực và cái qua thụ tinh để tạo thành hợp tử lưỡng bội, tạo ra biến dị di truyền phong phú giúp quần thể thích nghi với môi trường sống biến động."
        },
        {
            "id": "sec_plant_reproduction",
            "title": "2. Sinh sản Hữu tính ở Thực vật có Hoa (Thụ phấn & Nảy mầm)",
            "selector": "#sec-plant-reproduction",
            "en": "Section 2 investigates flowering plant reproduction: Male stamens consist of anthers producing pollen grains and filaments; female carpels feature sticky stigmas, styles, and ovaries enclosing ovules. Insect-pollinated flowers have bright petals, scent, and sticky pollen; wind-pollinated flowers feature dangling exposed anthers and feathery stigmas. Seed germination requires WOW conditions: Water to activate enzymes, Oxygen for aerobic respiration, and Warmth for optimum enzyme kinetics.",
            "vi": "Mục hai nghiên cứu sinh sản ở thực vật hạt kín: Nhị đực gồm bao phấn sinh hạt phấn và chỉ nhị; nhụy cái gồm đầu nhụy dính, vòi nhụy và bầu nhụy chứa noãn. Hoa thụ phấn nhờ côn trùng có cánh hoa sặc sỡ, hương thơm và hạt phấn có gai dính; hoa thụ phấn nhờ gió có bao phấn lòng thòng đu đưa ngoài hoa và đầu nhụy hình lông chim đón gió. Hạt nảy mầm đòi hỏi 3 điều kiện thiết yếu WOW: Nước (Water) để kích hoạt enzyme, Oxy (Oxygen) để hô hấp hiếu khí và Độ ấm (Warmth) để enzyme hoạt động ở nhiệt độ tối ưu."
        },
        {
            "id": "sec_human_reproduction",
            "title": "3. Sinh sản ở Người: Thụ tinh, Nhau thai & Dây rốn",
            "selector": "#sec-human-reproduction",
            "en": "Section 3 analyzes human development: Fertilisation occurs in the oviduct when a sperm nucleus fuses with an ovum nucleus. The zygote undergoes cleavage into an embryo that implants into the uterine lining. The placenta connects fetus to uterus, facilitating diffusion of oxygen, glucose, and antibodies from mother to fetus, and removing fetal urea and carbon dioxide, while shielding the delicate fetal circulation from maternal blood pressure.",
            "vi": "Mục ba phân tích quá trình phát triển phôi thai: Thụ tinh diễn ra tại 1/3 trên của ống dẫn trứng khi nhân tinh trùng dung hợp với nhân trứng. Hợp tử phân chia nhiều lần tạo phôi nang rồi làm tổ trong lớp niêm mạc tử cung. Nhau thai liên kết thai nhi với cơ thể mẹ, cho phép oxy, glucose và kháng thể khuếch tán từ máu mẹ sang thai nhi, đồng thời đào thải ure và CO2 từ phôi thai, bảo vệ hệ tuần hoàn mong manh của thai nhi khỏi áp lực máu cao của mẹ."
        },
        {
            "id": "sec_menstrual_cycle",
            "title": "4. Chu kỳ Kinh nguyệt & Sự Phối hợp Hooc-môn",
            "selector": "#sec-menstrual-cycle",
            "en": "Section 4 details the 28-day menstrual cycle: Pituitary FSH stimulates follicle development in the ovary and triggers oestrogen release. Oestrogen repairs and thickens the endometrium wall, stimulating a surge of pituitary LH which triggers ovulation at day 14. The ruptured follicle becomes the corpus luteum, secreting progesterone to maintain the thickened lining for implantation. If fertilisation fails, progesterone levels plummet, triggering menstruation.",
            "vi": "Mục bốn phân tích chu kỳ kinh nguyệt 28 ngày: Tuyến yên tiết FSH kích thích nang trứng phát triển và tiết oestrogen. Oestrogen làm dày niêm mạc tử cung và kích thích tuyến yên bùng nổ tiết LH gây rụng trứng vào khoảng ngày thứ 14. Vỏ nang trứng vỡ biến thành thể vàng tiết progesterone để duy trì niêm mạc dày xốp đón phôi thai. Nếu trứng không được thụ tinh, thể vàng thoái hóa, nồng độ progesterone tụt dốc kích hoạt sự bong tróc niêm mạc gây ra hành kinh."
        }
    ]

    major_sections = [
        {"id": "sec_asexual_vs_sexual", "title": "1. Sinh sản Vô tính vs Hữu tính"},
        {"id": "sec_plant_reproduction", "title": "2. Thụ phấn & Nảy mầm ở Thực vật"},
        {"id": "sec_human_reproduction", "title": "3. Thụ tinh, Nhau thai & Dây rốn"},
        {"id": "sec_menstrual_cycle", "title": "4. Chu kỳ Kinh nguyệt & Hormone"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 16 successfully built!")


# ==============================================================================
# MAIN BATCH 4 RUNNER (TOPICS 13 -> 16)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING BIOLOGY BATCH 4: TOPICS 13 -> 16")
    print("*******************************************************\n")
    
    await build_13()
    await asyncio.sleep(2)
    
    await build_14()
    await asyncio.sleep(2)
    
    await build_15()
    await asyncio.sleep(2)
    
    await build_16()
    
    print("\n*******************************************************")
    print("BIOLOGY BATCH 4 COMPLETE: TOPICS 13 -> 16 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
