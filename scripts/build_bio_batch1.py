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
# TOPIC 1: Characteristics and classification of living organisms
# ==============================================================================
async def build_1():
    lid = '11cfe97d-205e-418b-ae79-e39d7e57e0a8'
    code = '1'
    title = 'Topic 1: Characteristics and classification of living organisms'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-characteristics" class="lecture-interactive-card" data-lecture-section="sec_characteristics" style="cursor: pointer; ')
    
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-mrs-gren" class="lecture-interactive-card" data-lecture-section="sec_mrs_gren" style="cursor: pointer; ')
    
    t_h3_0 = str(h3s[0])
    r_h3_0 = t_h3_0.replace('<h3', '<h3 id="sec-excretion-organs" class="lecture-interactive-card" data-lecture-section="sec_excretion_organs" style="cursor: pointer; ')
    
    t_h3_1 = str(h3s[1])
    r_h3_1 = t_h3_1.replace('<h3', '<h3 id="sec-key-terms" class="lecture-interactive-card" data-lecture-section="sec_key_terms" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_0, r_h3_0, 1)\
                   .replace(t_h3_1, r_h3_1, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 1 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1: Đặc điểm và Phân loại Sinh vật",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 1: Characteristics and classification of living organisms. In this foundational chapter, we explore the seven essential characteristics shared by all living organisms, master the mnemonic MRS GREN, and examine the major human organs of excretion and key exam traps.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 1: Đặc điểm và Phân loại sinh vật sống. Trong bài học nền tảng này, chúng ta sẽ khám phá 7 đặc điểm thiết yếu của sự sống qua câu thần chú kinh điển MRS GREN, phân tích các cơ quan bài tiết chính ở người và làm rõ các bẫy đề thi Cambridge quan trọng."
        },
        {
            "id": "sec_characteristics",
            "title": "1. Bảy đặc điểm cốt lõi của Sự sống (MRS GREN)",
            "selector": "#sec-characteristics",
            "en": "Section 1 presents the universal characteristics of life: Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, and Nutrition. Every organism—from microscopic single-celled bacteria to towering redwood trees—exhibits all seven processes to sustain life.",
            "vi": "Mục một trình bày 7 đặc điểm chung của mọi sinh vật sống: Vận động, Hô hấp tế bào, Cảm ứng, Tăng trưởng, Sinh sản, Bài tiết và Dinh dưỡng. Mọi sinh vật trên Trái Đất—từ vi khuẩn đơn bào siêu nhỏ đến những cây gỗ khổng lồ—đều phải thực hiện đầy đủ 7 quá trình này để duy trì sự sống."
        },
        {
            "id": "sec_mrs_gren",
            "title": "1.2. Định nghĩa Chuẩn Cambridge (MRS GREN Flashcards)",
            "selector": "#sec-mrs-gren",
            "en": "Section 1.2 reinforces precise Cambridge definitions. Movement is an action causing a change of position or place. Respiration is the chemical reactions in cells that break down nutrient molecules and release energy for metabolism. Sensitivity detects and responds to stimuli. Growth is a permanent increase in size and dry mass. Reproduction makes more of the same kind. Excretion removes toxic metabolic waste. Nutrition takes in materials for energy, growth, and development.",
            "vi": "Mục một chấm hai củng cố các định nghĩa chính xác theo chuẩn khảo thí Cambridge. Vận động là hành động làm thay đổi vị trí. Hô hấp là chuỗi phản ứng hóa học trong tế bào phân giải chất dinh dưỡng để giải phóng năng lượng cho quá trình trao đổi chất. Cảm ứng giúp nhận biết và phản ứng với kích thích. Tăng trưởng là sự gia tăng vĩnh viễn về kích thước và khối lượng khô. Sinh sản tạo ra thế hệ mới. Bài tiết đào thải chất thải độc hại từ chuyển hóa. Dinh dưỡng là hấp thu vật chất để cung cấp năng lượng và phát triển."
        },
        {
            "id": "sec_excretion_organs",
            "title": "Các Cơ quan Bài tiết Chính ở Người",
            "selector": "#sec-excretion-organs",
            "en": "This section highlights the three major human excretory organs: The Kidneys filter urea, excess water, and mineral salts into urine. The Lungs excrete carbon dioxide and water vapour produced during cellular respiration. The Skin excretes sweat containing water, mineral salts, and trace amounts of urea.",
            "vi": "Phần này nêu bật ba cơ quan bài tiết chủ chốt ở cơ thể người: Thận lọc và đào thải ure, lượng nước dư thừa và muối khoáng ra ngoài qua nước tiểu. Phổi bài tiết khí carbon dioxide và hơi nước sinh ra từ quá trình hô hấp tế bào. Da bài tiết mồ hôi chứa nước, muối khoáng và một lượng nhỏ ure."
        },
        {
            "id": "sec_key_terms",
            "title": "Thuật ngữ Cốt lõi & Bẫy Đề thi Cambridge",
            "selector": "#sec-key-terms",
            "en": "Section 1.3 tackles critical Cambridge exam traps: Never confuse Excretion with Egestion! Excretion is the removal of metabolic waste substances produced inside cells, such as urea and carbon dioxide. Egestion is merely the passing out of undigested food as faeces through the anus, which has never taken part in cellular metabolism.",
            "vi": "Mục này giải quyết bẫy đề thi kinh điển của Cambridge: Tuyệt đối không được nhầm lẫn giữa Bài tiết (Excretion) và Thải phân (Egestion)! Bài tiết là quá trình loại bỏ các chất thải chuyển hóa sinh ra từ bên trong tế bào, như ure và CO2. Thải phân chỉ đơn thuần là tống xuất thức ăn chưa được tiêu hóa ra khỏi hậu môn, vốn chưa từng tham gia vào phản ứng chuyển hóa tế bào."
        }
    ]

    major_sections = [
        {"id": "sec_characteristics", "title": "1. Bảy đặc điểm cốt lõi (MRS GREN)"},
        {"id": "sec_mrs_gren", "title": "1.2. Định nghĩa chuẩn Cambridge"},
        {"id": "sec_excretion_organs", "title": "Cơ quan bài tiết chính ở người"},
        {"id": "sec_key_terms", "title": "Bẫy thi: Excretion vs Egestion"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 1 successfully built!")


# ==============================================================================
# TOPIC 2: Cells and organisms
# ==============================================================================
async def build_2():
    lid = '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc'
    code = '2'
    title = 'Topic 2: Cells and organisms'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h3s = soup.find_all('h3')
    h2s = soup.find_all('h2')
    
    # h3[0]: Interactive Cell Map
    t_h3_0 = str(h3s[0])
    r_h3_0 = t_h3_0.replace('<h3', '<h3 id="sec-cell-structures" class="lecture-interactive-card" data-lecture-section="sec_cell_structures" style="cursor: pointer; ')
    
    # h3[1]: 📊 Comparison: Plant vs Animal Cells
    t_h3_1 = str(h3s[1])
    r_h3_1 = t_h3_1.replace('<h3', '<h3 id="sec-cell-comparison" class="lecture-interactive-card" data-lecture-section="sec_cell_comparison" style="cursor: pointer; ')
    
    # h2[0]: 🏢 2. LEVELS OF ORGANISATION
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-levels-organisation" class="lecture-interactive-card" data-lecture-section="sec_levels_organisation" style="cursor: pointer; ')
    
    # h2[1]: 🔬 3. SPECIALISED CELLS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-specialised-cells" class="lecture-interactive-card" data-lecture-section="sec_specialised_cells" style="cursor: pointer; ')
    
    # h2[2]: 📐 4. SIZE OF SPECIMENS & MAGNIFICATION
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h3_0, r_h3_0, 1)\
                   .replace(t_h3_1, r_h3_1, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    # Balance div: Topic 2 was missing 1 closing div
    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff == 1:
        new_html += "\n</div>"
        print("Balanced Topic 2 unclosed outer div (diff -> 0)")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2: Tế bào và Cấu trúc Sinh vật",
            "selector": "#sec-header",
            "en": "Welcome to Topic 2: Cells and organisms. Cells are the fundamental structural and functional units of all living things. In this lesson, we analyze plant and animal cell ultrastructure, compare cellular components, understand the hierarchy of organization, examine specialized cell adaptations, and master magnification calculations.",
            "vi": "Chào mừng các bạn đến với Bài 2: Tế bào và sinh vật. Tế bào là đơn vị cấu trúc và chức năng cơ bản của mọi sinh vật sống. Trong bài học này, chúng ta sẽ phân tích cấu trúc siêu vi của tế bào động vật và thực vật, so sánh các bào quan, hiểu rõ các cấp độ tổ chức sống, các tế bào chuyên hóa và công thức tính độ phóng đại."
        },
        {
            "id": "sec_cell_structures",
            "title": "1. Cấu trúc Tế bào & Bào quan (Cell Organelles)",
            "selector": "#sec-cell-structures",
            "en": "Section 1 explores cell organelles: The nucleus contains genetic material (DNA) controlling cellular activities. The cytoplasm is the site of metabolic chemical reactions. The cell membrane is partially permeable, regulating substance entry and exit. Mitochondria conduct aerobic respiration to release ATP energy. Ribosomes carry out protein synthesis.",
            "vi": "Mục một khảo sát các bào quan: Nhân tế bào chứa vật chất di truyền DNA điều khiển mọi hoạt động tế bào. Tế bào chất là môi trường diễn ra các phản ứng hóa học chuyển hóa. Màng tế bào có tính thấm chọn lọc, kiểm soát các chất ra vào. Ty thể thực hiện hô hấp hiếu khí giải phóng năng lượng ATP. Ribosome đảm nhiệm quá trình tổng hợp protein."
        },
        {
            "id": "sec_cell_comparison",
            "title": "So sánh Tế bào Thực vật và Động vật",
            "selector": "#sec-cell-comparison",
            "en": "This section contrasts plant and animal cells. Plant cells possess three unique structures: a rigid cellulose cell wall providing structural support and preventing lysis; chloroplasts containing green chlorophyll pigments for photosynthesis; and a large permanent central vacuole filled with cell sap.",
            "vi": "Phần này so sánh tế bào thực vật và động vật. Tế bào thực vật có 3 cấu trúc độc nhất mà tế bào động vật không có: thành tế bào bằng cellulose giúp duy trì hình dạng và chống vỡ tế bào; lục lạp chứa diệp lục hấp thụ ánh sáng để quang hợp; và một không bào trung tâm lớn chứa dịch tế bào."
        },
        {
            "id": "sec_levels_organisation",
            "title": "2. Các cấp độ Tổ chức Sống (Levels of Organisation)",
            "selector": "#sec-levels-organisation",
            "en": "Section 2 outlines the biological hierarchy: Specialized cells group together to form Tissues, such as muscle tissue or leaf palisade mesophyll. Different tissues coordinate to form Organs, like the heart or stomach. Organs collaborate within Organ Systems, like the digestive or circulatory systems, culminating in a complete Organism.",
            "vi": "Mục hai phác thảo thứ bậc tổ chức sinh học: Các tế bào chuyên hóa tập hợp lại tạo thành Mô, như mô cơ hoặc mô giậu ở lá. Các mô khác nhau phối hợp tạo thành Cơ quan, như tim hoặc dạ dày. Các cơ quan liên kết trong Hệ cơ quan, như hệ tiêu hóa hoặc tuần hoàn, cấu thành một Cơ thể sinh vật hoàn chỉnh."
        },
        {
            "id": "sec_specialised_cells",
            "title": "3. Tế bào Chuyên hóa (Specialised Cells)",
            "selector": "#sec-specialised-cells",
            "en": "Section 3 investigates specialized cells adapted for dedicated physiological roles: Ciliated cells sweep mucus and trapped pathogens out of airways. Root hair cells feature long finger-like projections maximizing surface area for rapid water and mineral absorption. Palisade mesophyll cells pack dense chloroplasts beneath the upper leaf epidermis for maximal light harvesting.",
            "vi": "Mục ba nghiên cứu các tế bào chuyên hóa thích nghi với chức năng riêng biệt: Tế bào biểu mô có lông rung quét chất nhầy và bụi bẩn ra khỏi khí quản. Tế bào lông hút có phần kéo dài như ngón tay giúp tăng tối đa diện tích bề mặt để hấp thụ nước và khoáng chất. Tế bào mô giậu chứa mật độ lục lạp cực cao nằm ngay dưới biểu bì trên để hấp thu tối đa ánh sáng mặt trời."
        },
        {
            "id": "sec_magnification",
            "title": "4. Tính Độ phóng đại: Quy tắc Tam giác IAM",
            "selector": "#sec-magnification",
            "en": "Section 4 covers magnification calculations using the IAM triangle formula: Image size equals Actual size multiplied by Magnification. To find Actual size, divide Image size by Magnification. Remember the golden unit rule: Always convert measurements into the same unit before calculating—one millimetre equals one thousand micrometres!",
            "vi": "Mục bốn hướng dẫn tính độ phóng đại thông qua tam giác IAM: Kích thước ảnh chụp (Image) bằng Kích thước thực (Actual) nhân với Độ phóng đại (Magnification). Để tìm kích thước thực, ta lấy kích thước ảnh chia cho độ phóng đại. Hãy nhớ quy tắc chuyển đổi đơn vị vàng: 1 milimét bằng 1000 micromét!"
        }
    ]

    major_sections = [
        {"id": "sec_cell_structures", "title": "1. Cấu trúc tế bào & bào quan"},
        {"id": "sec_cell_comparison", "title": "So sánh tế bào TV vs ĐV"},
        {"id": "sec_levels_organisation", "title": "2. Các cấp độ tổ chức sống"},
        {"id": "sec_specialised_cells", "title": "3. Tế bào chuyên hóa"},
        {"id": "sec_magnification", "title": "4. Công thức tam giác IAM"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 2 successfully built!")


# ==============================================================================
# TOPIC 3: Movement into and out of cells
# ==============================================================================
async def build_3():
    lid = '0f5013fb-eaf1-4f79-8f41-c6102d2185a2'
    code = '3'
    title = 'Topic 3: Movement into and out of cells'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    # h2[0]: 💨 1. DIFFUSION
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-diffusion" class="lecture-interactive-card" data-lecture-section="sec_diffusion" style="cursor: pointer; ')
    
    # h2[1]: 💧 2. OSMOSIS
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-osmosis" class="lecture-interactive-card" data-lecture-section="sec_osmosis" style="cursor: pointer; ')
    
    # h3[2]: 🔬 TONY ENGLISH INTERACTIVE LAB: OSMOSIS
    t_h3_lab = str(h3s[2])
    r_h3_lab = t_h3_lab.replace('<h3', '<h3 id="sec-osmosis-lab" class="lecture-interactive-card" data-lecture-section="sec_osmosis_lab" style="cursor: pointer; ')
    
    # h3[3]: 📚 Exam Case Studies: Investigating Osmosis
    t_h3_cases = str(h3s[3])
    r_h3_cases = t_h3_cases.replace('<h3', '<h3 id="sec-osmosis-experiments" class="lecture-interactive-card" data-lecture-section="sec_osmosis_experiments" style="cursor: pointer; ')
    
    # h2[2]: ⚡ 3. ACTIVE TRANSPORT
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-active-transport" class="lecture-interactive-card" data-lecture-section="sec_active_transport" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h3_lab, r_h3_lab, 1)\
                   .replace(t_h3_cases, r_h3_cases, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff == 1:
        new_html += "\n</div>"
        print("Balanced Topic 3 unclosed outer div (diff -> 0)")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3: Vận chuyển Các chất qua Màng Tế bào",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 3: Movement into and out of cells. In this essential chapter, we master the three fundamental transport mechanisms: passive Diffusion, water-specific Osmosis, and energy-consuming Active Transport, along with critical laboratory investigations.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 3: Sự vận chuyển các chất qua màng tế bào. Trong bài học quan trọng này, chúng ta sẽ nắm vững ba cơ chế vận chuyển nền tảng: Khuếch tán thụ động, Thẩm thấu của nước và Vận chuyển chủ động cần năng lượng, cùng các thí nghiệm thực hành trọng tâm."
        },
        {
            "id": "sec_diffusion",
            "title": "1. Sự Khuếch tán (Diffusion)",
            "selector": "#sec-diffusion",
            "en": "Section 1 defines Diffusion: the net movement of particles from a region of higher concentration to a region of lower concentration down a concentration gradient, as a result of their random movement. Factors accelerating diffusion include steeper concentration gradients, higher temperatures increasing kinetic energy, shorter diffusion distances, and larger surface area to volume ratios.",
            "vi": "Mục một định nghĩa Khuếch tán: là sự chuyển dời thực của các hạt phân tử từ nơi có nồng độ cao đến nơi có nồng độ thấp theo chiều gradien nồng độ, bắt nguồn từ chuyển động hỗn loạn ngẫu nhiên của các hạt. Các yếu tố làm tăng tốc độ khuếch tán gồm độ dốc gradien nồng độ lớn, nhiệt độ cao làm tăng động năng, khoảng cách khuếch tán ngắn và tỉ lệ diện tích bề mặt trên thể tích lớn."
        },
        {
            "id": "sec_osmosis",
            "title": "2. Hiện tượng Thẩm thấu (Osmosis)",
            "selector": "#sec-osmosis",
            "en": "Section 2 defines Osmosis: the net movement of water molecules from a region of higher water potential to a region of lower water potential through a partially permeable membrane. Pure water possesses the highest water potential of zero. Adding dissolved solutes lowers water potential.",
            "vi": "Mục hai định nghĩa Thẩm thấu: là sự chuyển dời thực của các phân tử nước từ nơi có thế nước cao đến nơi có thế nước thấp qua một màng bán thấm có tính chọn lọc. Nước tinh khiết có thế nước cao nhất bằng không. Khi hòa tan thêm chất tan, thế nước sẽ giảm xuống giá trị âm."
        },
        {
            "id": "sec_osmosis_lab",
            "title": "Tác động của Thẩm thấu lên Tế bào (Osmosis Lab)",
            "selector": "#sec-osmosis-lab",
            "en": "This interactive section contrasts cellular osmosis: In pure water, plant cells absorb water by osmosis and become turgid, with turgor pressure pushing against the cellulose cell wall. In concentrated sugar solution, water leaves plant cells, causing plasmolysis where the cell membrane shrinks away from the wall. Animal cells, lacking walls, swell and burst in pure water (lysis) or shrivel in concentrated solution (crenation).",
            "vi": "Phần này phân tích phản ứng của tế bào trước thẩm thấu: Trong nước tinh khiết, tế bào thực vật hút nước trương lên (turgid), tạo ra áp suất trương nước ép sát vào thành cellulose. Trong dung dịch đặc, tế bào thực vật mất nước co nguyên sinh (plasmolysis), màng sinh chất tách rời khỏi thành. Tế bào động vật do không có thành bảo vệ nên sẽ vỡ tung (lysis) trong nước cất hoặc teo tóp (crenation) trong dung dịch ưu trương."
        },
        {
            "id": "sec_osmosis_experiments",
            "title": "Thí nghiệm Thẩm thấu Đề thi (Paper 6 Focus)",
            "selector": "#sec-osmosis-experiments",
            "en": "Section 2.2 details Paper 6 exam case studies: Investigating osmosis using potato cylinders placed in varying sucrose concentrations. Candidates must calculate percentage change in mass to account for differing initial potato masses. The concentration where potato mass neither increases nor decreases indicates the tissue's internal water potential.",
            "vi": "Mục hai chấm hai đi sâu vào các thí nghiệm Paper 6: Khảo sát thẩm thấu bằng các lõi củ khoai tây ngâm trong các dung dịch đường có nồng độ khác nhau. Thí sinh phải tính phần trăm thay đổi khối lượng để loại trừ sự chênh lệch khối lượng ban đầu. Điểm nồng độ mà tại đó khối lượng khoai tây không đổi chính là nồng độ tương đương với thế nước bên trong tế bào."
        },
        {
            "id": "sec_active_transport",
            "title": "3. Vận chuyển Chủ động (Active Transport)",
            "selector": "#sec-active-transport",
            "en": "Section 3 defines Active Transport: the movement of particles through a cell membrane from a region of lower concentration to a region of higher concentration against a concentration gradient, using energy released from cellular respiration and embedded protein carriers. Classic examples include root hair cells absorbing mineral nitrate ions from dilute soil, and intestinal villi absorbing glucose.",
            "vi": "Mục ba định nghĩa Vận chuyển chủ động: là sự di chuyển của các hạt qua màng tế bào từ nơi có nồng độ thấp đến nơi có nồng độ cao ngược chiều gradien nồng độ, sử dụng năng lượng giải phóng từ hô hấp tế bào và các protein vận chuyển màng. Ví dụ kinh điển gồm rễ cây hút khoáng chất từ đất loãng và lông ruột non hấp thu glucose vào máu."
        }
    ]

    major_sections = [
        {"id": "sec_diffusion", "title": "1. Sự Khuếch tán (Diffusion)"},
        {"id": "sec_osmosis", "title": "2. Hiện tượng Thẩm thấu (Osmosis)"},
        {"id": "sec_osmosis_lab", "title": "Tác động thẩm thấu lên tế bào"},
        {"id": "sec_osmosis_experiments", "title": "Thí nghiệm thẩm thấu (Paper 6)"},
        {"id": "sec_active_transport", "title": "3. Vận chuyển Chủ động"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 3 successfully built!")


# ==============================================================================
# TOPIC 4: Biological molecules
# ==============================================================================
async def build_4():
    lid = '821ff271-c9ae-493a-b14c-e3f4b074a9d9'
    code = '4'
    title = 'Topic 4: Biological molecules'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    h3s = soup.find_all('h3')
    
    # h2[0]: 🧬 1. CHEMICAL ELEMENTS & MOLECULAR STRUCTURE
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-biomolecules" class="lecture-interactive-card" data-lecture-section="sec_biomolecules" style="cursor: pointer; ')
    
    # h3[3]: 🧬 DNA Structure Extended Only
    t_h3_dna = str(h3s[3])
    r_h3_dna = t_h3_dna.replace('<h3', '<h3 id="sec-dna-water" class="lecture-interactive-card" data-lecture-section="sec_dna_water" style="cursor: pointer; ')
    
    # h2[1]: 🧪 2. CHEMICAL FOOD TESTS (Interactive Virtual Lab)
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-food-tests" class="lecture-interactive-card" data-lecture-section="sec_food_tests" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h3_dna, r_h3_dna, 1)\
                   .replace(t_h2_1, r_h2_1, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff == 1:
        new_html += "\n</div>"
        print("Balanced Topic 4 unclosed outer div (diff -> 0)")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4: Các Đại phân tử Sinh học & Xét nghiệm Hóa học",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 4: Biological molecules. All living matter is constructed from organic chemical compounds. In this chapter, we unpack the composition of carbohydrates, lipids, and proteins, examine DNA structure, and explore the core diagnostic food tests.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 4: Các đại phân tử sinh học. Mọi cấu trúc sống đều được hình thành từ các hợp chất hữu cơ. Trong bài học này, chúng ta sẽ tìm hiểu cấu tạo của carbohydrate, lipid và protein, khám phá chuỗi xoắn kép DNA và nắm chắc các phản ứng thử nghiệm thực phẩm trọng tâm."
        },
        {
            "id": "sec_biomolecules",
            "title": "1. Cấu trúc Hóa học: Carbohydrate, Lipid & Protein",
            "selector": "#sec-biomolecules",
            "en": "Section 1 breaks down molecular elements: Carbohydrates contain Carbon, Hydrogen, and Oxygen; simple glucose units link to form starch, glycogen, or cellulose. Lipids contain Carbon, Hydrogen, and Oxygen, formed from one glycerol molecule joined to three fatty acid chains. Proteins contain Carbon, Hydrogen, Oxygen, Nitrogen, and sometimes Sulphur, assembled from chains of twenty different amino acids.",
            "vi": "Mục một phân tích thành phần nguyên tố: Carbohydrate chứa Cacbon, Hydro và Oxy; các đơn phân glucose liên kết tạo thành tinh bột, glycogen hoặc cellulose. Lipid chứa Cacbon, Hydro và Oxy, cấu tạo từ một phân tử glycerol liên kết với 3 chuỗi axit béo. Protein chứa Cacbon, Hydro, Oxy, Nitơ và đôi khi có Lưu huỳnh, được tạo thành từ các chuỗi gồm 20 loại axit amin khác nhau."
        },
        {
            "id": "sec_dna_water",
            "title": "Cấu trúc DNA & Vai trò của Nước",
            "selector": "#sec-dna-water",
            "en": "This section covers DNA structure and water. DNA consists of two strands coiled into a double helix, with cross-links between complementary base pairs: Adenine pairs with Thymine, and Cytosine pairs with Guanine. Water acts as the universal solvent, facilitating metabolic enzymatic reactions, nutrient transport in blood plasma, and plant transpiration.",
            "vi": "Phần này xem xét cấu trúc DNA và vai trò của nước. Phân tử DNA gồm hai mạch polynucleotide xoắn kép, liên kết với nhau theo nguyên tắc bổ sung: Adenin liên kết với Timin, và Guanin liên kết với Xitôzin. Nước đóng vai trò là dung môi hòa tan vạn năng, làm môi trường cho các phản ứng enzyme, vận chuyển chất dinh dưỡng trong huyết tương và điều hòa nhiệt độ qua thoát hơi nước."
        },
        {
            "id": "sec_food_tests",
            "title": "2. Các Thử nghiệm Hóa học Thực phẩm (Food Tests Lab)",
            "selector": "#sec-food-tests",
            "en": "Section 2 details the essential Cambridge food tests: Benedict's test detects reducing sugars by heating in a hot water bath, changing from blue to green, yellow, or brick-red precipitate. Iodine solution tests for starch, turning from brown to blue-black. The Biuret test detects protein, changing from blue to purple or violet. The Ethanol emulsion test detects lipids, forming a cloudy white emulsion. DCPIP tests for Vitamin C, turning from blue to completely colourless.",
            "vi": "Mục hai hệ thống hóa các phép thử nghiệm thực phẩm kinh điển: Thuốc thử Benedict nhận biết đường khử khi đun cách thủy, chuyển từ xanh lam sang kết tủa đỏ gạch. Dung dịch I-ốt nhận biết tinh bột, đổi từ nâu vàng sang xanh đen. Thuốc thử Biuret nhận biết protein, chuyển từ xanh lam sang tím. Thử nghiệm nhũ tương cồn nhận biết chất béo bằng cách tạo vẩn đục màu trắng sữa. Thuốc thử DCPIP nhận biết Vitamin C khi bị mất màu từ xanh lam thành không màu."
        }
    ]

    major_sections = [
        {"id": "sec_biomolecules", "title": "1. Hóa học Carbohydrate, Lipid, Protein"},
        {"id": "sec_dna_water", "title": "Cấu trúc DNA & Tầm quan trọng của Nước"},
        {"id": "sec_food_tests", "title": "2. Các Thử nghiệm Thực phẩm (Food Tests)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 4 successfully built!")


# ==============================================================================
# TOPIC 5: Enzymes
# ==============================================================================
async def build_5():
    lid = 'a5d1775c-6ecb-4d6c-bc50-8aafbf641c1e'
    code = '5'
    title = 'Topic 5: Enzymes'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: ⚡ 1. DEFINITION OF ENZYMES
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-enzyme-definition" class="lecture-interactive-card" data-lecture-section="sec_enzyme_definition" style="cursor: pointer; ')
    
    # h2[1]: 🔑 2. HOW DO ENZYMES WORK? (The Lock and Key Hypothesis)
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-lock-and-key" class="lecture-interactive-card" data-lecture-section="sec_lock_and_key" style="cursor: pointer; ')
    
    # h2[2]: 🌡️ 3. FACTORS AFFECTING ENZYMES: TEMPERATURE & pH
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-factors-temperature-ph" class="lecture-interactive-card" data-lecture-section="sec_factors_temperature_ph" style="cursor: pointer; ')
    
    # h2[3]: 📝 4. EXAM CASE STUDY: The Catalase Experiment (Paper 6 Focus
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-catalase-experiment" class="lecture-interactive-card" data-lecture-section="sec_catalase_experiment" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff == 1:
        new_html += "\n</div>"
        print("Balanced Topic 5 unclosed outer div (diff -> 0)")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5: Enzyme - Chất Xúc tác Sinh học",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 5: Enzymes. Enzymes are the biological catalysts powering all metabolic life processes. In this lesson, we study enzyme action, the Lock and Key hypothesis, the critical effects of temperature and pH, and analyze classic Paper 6 enzyme experiments.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 5: Enzyme - Chất xúc tác sinh học. Enzyme là chất xúc tác sinh học thúc đẩy mọi quá trình trao đổi chất của sự sống. Trong bài học này, chúng ta sẽ tìm hiểu cơ chế hoạt động ổ khóa - chìa khóa, ảnh hưởng quyết định của nhiệt độ và độ pH, cùng các bài thí nghiệm Paper 6 kinh điển."
        },
        {
            "id": "sec_enzyme_definition",
            "title": "1. Định nghĩa & Bản chất của Enzyme",
            "selector": "#sec-enzyme-definition",
            "en": "Section 1 defines an Enzyme: a protein that functions as a biological catalyst to increase the rate of chemical reactions without being changed or used up in the reaction. Enzymes lower activation energy, enabling vital metabolic reactions to occur rapidly at normal body temperature.",
            "vi": "Mục một định nghĩa Enzyme: là một loại protein đóng vai trò như chất xúc tác sinh học làm tăng tốc độ phản ứng hóa học mà không bị biến đổi hay tiêu hao sau phản ứng. Enzyme làm giảm năng lượng hoạt hóa, giúp các phản ứng trao đổi chất quan trọng diễn ra nhanh chóng ở nhiệt độ cơ thể bình thường."
        },
        {
            "id": "sec_lock_and_key",
            "title": "2. Cơ chế Ổ khóa và Chìa khóa (Lock & Key Hypothesis)",
            "selector": "#sec-lock-and-key",
            "en": "Section 2 explains the Lock and Key hypothesis: Each enzyme possesses an active site with a unique 3D complementary shape that binds specifically to one substrate. When the substrate collides and binds, an enzyme-substrate complex forms, breaking down or joining molecules into products which detach, leaving the enzyme ready for another reaction.",
            "vi": "Mục hai giải thích giả thuyết Ổ khóa và Chìa khóa: Mỗi enzyme có một trung tâm hoạt động với cấu hình không gian 3 chiều đặc thù bổ sung khớp với một loại cơ chất xác định. Khi va chạm và liên kết, phức hợp enzyme - cơ chất hình thành, xúc tác tạo thành sản phẩm rồi tách ra, để lại enzyme nguyên vẹn sẵn sàng cho chu trình phản ứng tiếp theo."
        },
        {
            "id": "sec_factors_temperature_ph",
            "title": "3. Ảnh hưởng của Nhiệt độ và pH (Bẫy thi: Denature)",
            "selector": "#sec-factors-temperature-ph",
            "en": "Section 3 investigates temperature and pH: As temperature rises towards the optimum, molecules gain kinetic energy and collide more frequently. Above optimum temperature, violent vibrations break bonds holding the enzyme protein structure, permanently altering the active site shape—the enzyme is Denatured! Remember: Enzymes are chemical molecules, not living things, so never say an enzyme dies!",
            "vi": "Mục ba phân tích ảnh hưởng của nhiệt độ và pH: Khi nhiệt độ tăng đến mức tối ưu, động năng phân tử tăng làm tăng tần số va chạm hiệu quả. Khi vượt quá nhiệt độ tối ưu, các liên kết hydro duy trì cấu trúc bậc cao của enzyme bị phá vỡ, làm biến dạng vĩnh viễn trung tâm hoạt động—hiện tượng này gọi là Biến tính (Denaturation)! Lưu ý bẫy thi: Enzyme là phân tử hóa học không phải sinh vật sống, tuyệt đối không được nói enzyme 'chết'!"
        },
        {
            "id": "sec_catalase_experiment",
            "title": "4. Thí nghiệm Thực hành: Enzyme Catalase (Paper 6 Focus)",
            "selector": "#sec-catalase-experiment",
            "en": "Section 4 covers the classic catalase investigation: Catalase from potato or liver tissue decomposes toxic hydrogen peroxide into water and oxygen gas. The reaction rate is measured by collecting oxygen gas volume using a gas syringe or measuring foam height over time. Control variables include substrate volume, catalase concentration, and temperature.",
            "vi": "Mục bốn phân tích thí nghiệm catalase thực hành: Enzyme catalase từ mô khoai tây hoặc gan phân giải hydrogen peroxide độc hại thành nước và khí oxy. Tốc độ phản ứng được đo bằng thể tích khí oxy thu được qua ống tiêm đo khí hoặc chiều cao cột bọt khí theo thời gian. Các biến kiểm soát gồm thể tích cơ chất, nồng độ catalase và nhiệt độ bể điều nhiệt."
        }
    ]

    major_sections = [
        {"id": "sec_enzyme_definition", "title": "1. Định nghĩa & Bản chất Enzyme"},
        {"id": "sec_lock_and_key", "title": "2. Cơ chế Ổ khóa & Chìa khóa"},
        {"id": "sec_factors_temperature_ph", "title": "3. Nhiệt độ, pH & Biến tính (Denature)"},
        {"id": "sec_catalase_experiment", "title": "4. Thí nghiệm Catalase (Paper 6)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 5 successfully built!")


# ==============================================================================
# MAIN BATCH 1 RUNNER (TOPICS 1 -> 5)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING BIOLOGY BATCH 1: TOPICS 1 -> 5")
    print("*******************************************************\n")
    
    await build_1()
    await asyncio.sleep(2)
    
    await build_2()
    await asyncio.sleep(2)
    
    await build_3()
    await asyncio.sleep(2)
    
    await build_4()
    await asyncio.sleep(2)
    
    await build_5()
    
    print("\n*******************************************************")
    print("BIOLOGY BATCH 1 COMPLETE: TOPICS 1 -> 5 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
