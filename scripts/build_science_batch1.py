import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC B1: Characteristics of living organisms
# ==============================================================================
async def build_b1():
    lid = '1231b474-8a99-4330-b45d-fdda19a802fe'
    code = 'b1'
    title = 'B1: Characteristics of living organisms'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-mrsgren" class="lecture-interactive-card" data-lecture-section="sec_mrsgren" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-five-kingdoms" class="lecture-interactive-card" data-lecture-section="sec_five_kingdoms" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B1 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B1: Đặc điểm Sinh vật sống & Phân loại học",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Co-ordinated Sciences Biology, Topic B1: Characteristics of living organisms. Biology is the scientific study of life. In this introductory chapter, we analyze the seven universal characteristics of living organisms encapsulated in MRS GREN, and explore classification across the Five Biological Kingdoms.",
            "vi": "Chào mừng các bạn đến với phần Sinh học trong môn Khoa học Phối hợp Cambridge IGCSE, Chuyên đề B1: Đặc điểm của sinh vật sống và Phân loại học. Sinh học là khoa học nghiên cứu sự sống. Trong bài mở đầu này, chúng ta sẽ phân tích 7 đặc tính phổ quát của sinh vật sống qua quy tắc MRS GREN và hệ thống phân loại 5 giới sinh vật."
        },
        {
            "id": "sec_mrsgren",
            "title": "1. Bảy Đặc tính của Sự sống (Quy tắc MRS GREN)",
            "selector": "#sec-mrsgren",
            "en": "Section 1 outlines the seven vital characteristics of life, remembered by the acronym MRS GREN: Movement causes an organism to change position or place. Respiration breaks down nutrient molecules in cells to release energy for metabolism. Sensitivity detects internal or external stimuli and makes responses. Growth increases dry mass and size permanently. Reproduction generates more of the same kind. Excretion removes toxic waste products of metabolism. Nutrition provides nutrients for energy, growth, and tissue repair. Crucially for Cambridge exams, excretion removes metabolic wastes like urea and carbon dioxide, whereas egestion expels undigested food as feces through the anus.",
            "vi": "Mục một khái quát 7 đặc tính sống cơ bản được ghi nhớ qua cụm từ MRS GREN: Vận động (Movement) là sự thay đổi vị trí của cơ thể hoặc bộ phận. Hô hấp tế bào (Respiration) bẻ gãy phân tử dinh dưỡng để giải phóng năng lượng ATP. Cảm ứng (Sensitivity) là khả năng phát hiện kích thích và phản ứng lại. Sinh trưởng (Growth) gia tăng vĩnh viễn về kích thước và khối lượng khô. Sinh sản (Reproduction) tạo ra thế hệ cá thể mới. Bài tiết (Excretion) đào thải các chất thải độc hại sinh ra từ quá trình chuyển hóa tế bào. Dinh dưỡng (Nutrition) hấp thu các chất cần thiết để phát triển và sửa chữa mô. Điểm nhấn thi cử: bài tiết thải chất chuyển hóa như urê và CO2, khác hoàn toàn với sự tống phân (egestion) thải thức ăn không tiêu hóa qua hậu môn."
        },
        {
            "id": "sec_five_kingdoms",
            "title": "2. Phân loại Sinh vật sống: Năm Giới Sinh học",
            "selector": "#sec-five-kingdoms",
            "en": "Section 2 explores biological classification and binomial nomenclature: Organisms are grouped using shared morphology, anatomy, and DNA base sequences. In the binomial naming system, each species has a two-part Latin name: Genus capitalized, species in lowercase, italicized in print. All living organisms are classified into Five Kingdoms: Animals are multicellular heterotrophs lacking cell walls. Plants are multicellular autotrophs with cellulose walls and chloroplasts. Fungi have chitin walls and feed saprotrophically via hyphae. Protoctists are mostly unicellular eukaryotes. Prokaryotes lack true nuclei and membrane-bound organelles, possessing circular DNA.",
            "vi": "Mục hai khảo sát phân loại học và danh pháp kép Linnaeus: Sinh vật được xếp nhóm dựa vào hình thái, giải phẫu học và trình tự DNA. Hệ thống danh pháp kép đặt tên mỗi loài gồm hai từ tiếng Latin: Tên Chi viết hoa, tên loài viết thường, in nghiêng khi in ấn. Toàn bộ sinh giới chia thành 5 Giới: Giới Động vật là sinh vật đa bào dị dưỡng không có thành tế bào. Giới Thực vật là sinh vật đa bào tự dưỡng có thành cellulose và lục lạp. Giới Nấm có thành chitin và dinh dưỡng hoại sinh qua hệ sợi nấm. Giới Nguyên sinh gồm các sinh vật nhân thực đơn bào. Giới Khởi sinh (Prokaryotes) gồm vi khuẩn không có màng nhân và các bào quan có màng, chứa phân tử DNA vòng trần."
        }
    ]

    major_sections = [
        {"id": "sec_mrsgren", "title": "1. Bảy Đặc tính Sự sống (MRS GREN)"},
        {"id": "sec_five_kingdoms", "title": "2. Phân loại Năm Giới Sinh học"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B1 successfully built!")


# ==============================================================================
# TOPIC B2: Cells and organisms
# ==============================================================================
async def build_b2():
    lid = '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c'
    code = 'b2'
    title = 'B2: Cells and organisms'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-cell-comparison" class="lecture-interactive-card" data-lecture-section="sec_cell_comparison" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-organelles" class="lecture-interactive-card" data-lecture-section="sec_organelles" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-specialised-cells" class="lecture-interactive-card" data-lecture-section="sec_specialised_cells" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B2 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B2: Tế bào học & Cấu trúc Sinh vật",
            "selector": "#sec-header",
            "en": "Welcome to Topic B2: Cells and organisms. The cell is the fundamental structural and functional unit of all living things. In this chapter, we contrast plant, animal, and bacterial cell ultrastructure, map organelle functions, analyze specialised cells, and solve specimen magnification equations.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B2: Tế bào và Cơ thể sống. Tế bào là đơn vị cấu trúc và chức năng cơ bản của mọi sinh vật. Trong bài học này, chúng ta sẽ so sánh cấu trúc tế bào thực vật, động vật và vi khuẩn, chức năng các bào quan, tế bào chuyên hóa và công thức tính độ phóng đại qua kính hiển vi."
        },
        {
            "id": "sec_cell_comparison",
            "title": "1. So sánh Tế bào Thực vật, Động vật & Vi khuẩn",
            "selector": "#sec-cell-comparison",
            "en": "Section 1 contrasts cellular ultrastructures: Animal cells contain a nucleus, cytoplasm, cell membrane, mitochondria, and ribosomes. Plant cells share these organelles but uniquely possess a rigid cellulose cell wall for structural support, permanent large central sap vacuole to maintain turgor pressure, and chloroplasts containing chlorophyll for photosynthesis. Bacterial cells are prokaryotic: they lack a true nucleus, enclosing genetic material in circular chromosomes and independent plasmid rings.",
            "vi": "Mục một so sánh cấu trúc siêu vi của các tế bào: Tế bào động vật gồm nhân, tế bào chất, màng sinh chất, ty thể và ribosome. Tế bào thực vật có đủ các thành phần trên, đồng thời có thêm thành tế bào cellulose vững chắc, không bào trung tâm lớn chứa dịch tế bào tạo áp suất trương nước và lục lạp chứa diệp lục để quang hợp. Tế bào vi khuẩn là tế bào nhân sơ: không có màng nhân bao bọc, vật chất di truyền tồn tại dưới dạng một phân tử DNA vòng lớn và các vòng plasmid độc lập."
        },
        {
            "id": "sec_organelles",
            "title": "2. Bản đồ Bào quan & Chức năng Tế bào",
            "selector": "#sec-organelles",
            "en": "Section 2 details organelle biochemistry: The Nucleus contains genetic material in chromosomes and orchestrates cellular activities. Cytoplasm is an aqueous jelly where metabolic reactions take place. The Cell Membrane is partially permeable, regulating molecular entry and exit. Mitochondria are the powerhouses of the cell where aerobic respiration generates ATP. Ribosomes synthesize polypeptides and proteins from amino acids.",
            "vi": "Mục hai chi tiết hóa chức năng các bào quan: Nhân tế bào (Nucleus) lưu trữ thông tin di truyền trên nhiễm sắc thể và điều khiển mọi hoạt động sống. Tế bào chất (Cytoplasm) là môi trường bán lỏng diễn ra các phản ứng hóa sinh. Màng tế bào (Cell Membrane) có tính thấm chọn lọc, kiểm soát dòng vật chất ra vào. Ty thể (Mitochondria) là nhà máy năng lượng nơi diễn ra hô hấp hiếu khí tạo ATP. Ribosome là nơi tổng hợp chuỗi polypeptide và protein từ các axit amin."
        },
        {
            "id": "sec_specialised_cells",
            "title": "3. Tế bào Chuyên hóa & Đặc điểm Thích nghi",
            "selector": "#sec-specialised-cells",
            "en": "Section 3 investigates specialised cell adaptations: Ciliated epithelial cells line the trachea with tiny hair-like cilia that beat synchronously to waft mucus and trapped pathogens away from lungs. Root hair cells possess extended cytoplasmic projections that maximize surface area for rapid water and ion absorption. Xylem vessels have hollow, dead lumens reinforced with lignin to transport water and withstand negative pressure. Red blood cells have biconcave shape and no nucleus to pack hemoglobin for oxygen transport.",
            "vi": "Mục ba nghiên cứu các tế bào chuyên hóa: Tế bào biểu mô có lông rung lót khí quản có hàng trăm lông mao đập nhịp nhàng để quét dịch nhầy và bụi bẩn ra khỏi đường hô hấp. Tế bào lông hút ở rễ kéo dài bề mặt bào tương giúp tối đa hóa diện tích hấp thu nước và ion khoáng. Mạch gỗ (Xylem) gồm các tế bào chết rỗng ruột tẩm lignin dày chắc để vận chuyển dòng nước liên tục dưới lực hút thoát hơi nước. Tế bào hồng cầu hình đĩa lõm hai mặt, không nhân để tối ưu dung tích chứa hemoglobin vận chuyển oxy."
        },
        {
            "id": "sec_magnification",
            "title": "4. Công thức Độ phóng đại (I = A × M)",
            "selector": "#sec-magnification",
            "en": "Section 4 covers microscopy calculations using the formula triangle I = A × M, where Image size equals Actual size multiplied by Magnification. Always measure image dimensions in millimeters, then multiply by one thousand to convert into micrometers before computing actual biological cell sizes.",
            "vi": "Mục bốn hướng dẫn tính toán độ phóng đại qua tam giác công thức: I = A nhân M (Kích thước ảnh I bằng Kích thước thực tế A nhân Độ phóng đại M). Quy tắc sống còn trong bài thi Cambridge: Luôn đo kích thước ảnh trên đề bài bằng milimét (mm), sau đó nhân với một nghìn để đổi sang micromét (µm) trước khi tính toán kích thước thực của mẫu vật."
        }
    ]

    major_sections = [
        {"id": "sec_cell_comparison", "title": "1. So sánh Tế bào Thực vật, Động vật & Vi khuẩn"},
        {"id": "sec_organelles", "title": "2. Chức năng các Bào quan"},
        {"id": "sec_specialised_cells", "title": "3. Tế bào Chuyên hóa"},
        {"id": "sec_magnification", "title": "4. Công thức Độ phóng đại (I = A × M)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B2 successfully built!")


# ==============================================================================
# TOPIC B3: Movement into and out of cells
# ==============================================================================
async def build_b3():
    lid = '9a23109e-ad73-4fcf-a599-9605cc4906eb'
    code = 'b3'
    title = 'B3: Movement into and out of cells'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-diffusion" class="lecture-interactive-card" data-lecture-section="sec_diffusion" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-osmosis" class="lecture-interactive-card" data-lecture-section="sec_osmosis" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-active-transport" class="lecture-interactive-card" data-lecture-section="sec_active_transport" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B3 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B3: Vận chuyển Chất qua Màng Tế bào",
            "selector": "#sec-header",
            "en": "Welcome to Topic B3: Movement into and out of cells. Living cells constantly exchange nutrients, gases, and wastes across plasma membranes. In this lesson, we master the principles of diffusion, investigate water potential and osmosis in plant and animal tissues, and examine active transport mechanisms.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B3: Vận chuyển các chất qua màng tế bào. Tế bào sống liên tục trao đổi chất dinh dưỡng, khí và chất thải qua màng sinh chất. Trong bài học này, chúng ta sẽ làm chủ hiện tượng khuếch tán, thế nước và thẩm thấu trong tế bào thực vật và động vật, cùng cơ chế vận chuyển chủ động."
        },
        {
            "id": "sec_diffusion",
            "title": "1. Khuyếch tán & Các Yếu tố Ảnh hưởng (Diffusion)",
            "selector": "#sec-diffusion",
            "en": "Section 1 defines Diffusion: the net movement of particles from a region of higher concentration to a region of lower concentration down a concentration gradient, as a result of their random kinetic movement. Factors accelerating diffusion rate include steeper concentration gradients, higher temperature boosting kinetic energy, larger surface area, and shorter diffusion distance.",
            "vi": "Mục một định nghĩa Khuyếch tán (Diffusion): là sự chuyển động tịnh của các hạt từ vùng có nồng độ cao đến vùng có nồng độ thấp hơn xuôi theo chiều gradient nồng độ, bắt nguồn từ chuyển động nhiệt hỗn loạn của phân tử. Các yếu tố làm tăng tốc độ khuếch tán gồm: độ dốc gradient nồng độ càng lớn, nhiệt độ càng cao làm tăng động năng phân tử, diện tích bề mặt càng lớn và khoảng cách khuếch tán càng ngắn."
        },
        {
            "id": "sec_osmosis",
            "title": "2. Thẩm thấu, Thế nước & Thí nghiệm Tế bào (Osmosis)",
            "selector": "#sec-osmosis",
            "en": "Section 2 examines Osmosis: the net movement of water molecules from a region of higher water potential to a region of lower water potential through a partially permeable membrane. In pure water, plant cells absorb water by osmosis and become turgid, with internal turgor pressure pressing against the rigid cell wall to support non-woody plant stems. In concentrated salt or sugar solutions, plant cells lose water, the cytoplasm shrinks away from the cell wall, and the cell becomes flaccid and undergoes plasmolysis.",
            "vi": "Mục hai phân tích hiện tượng Thẩm thấu (Osmosis): là sự chuyển động tịnh của phân tử nước từ vùng có thế nước cao (dung dịch loãng) đến vùng có thế nước thấp hơn (dung dịch đặc) qua màng thấm chọn lọc. Khi ở trong nước tinh khiết, tế bào thực vật hút nước qua thẩm thấu và trở nên trương chắc (turgid), áp suất trương nước ép vào thành tế bào giúp nâng đỡ thân cây mềm. Ngược lại, trong dung dịch ưu trương, tế bào mất nước làm khối bào tương co cụm tách rời khỏi thành tế bào, gây hiện tượng co nguyên sinh (plasmolysis)."
        },
        {
            "id": "sec_active_transport",
            "title": "3. Vận chuyển Chủ động (Active Transport)",
            "selector": "#sec-active-transport",
            "en": "Section 3 investigates Active Transport: the movement of particles through a cell membrane from a region of lower concentration to a region of higher concentration against a concentration gradient, using energy released from respiration. Membrane-spanning carrier proteins bind specific solute molecules and utilize ATP energy to change conformational shape, pumping ions like nitrates into plant root hair cells even when soil concentrations are exceptionally low.",
            "vi": "Mục ba nghiên cứu Vận chuyển Chủ động (Active Transport): là quá trình vận chuyển các hạt qua màng tế bào từ nơi có nồng độ thấp đến nơi có nồng độ cao ngược chiều gradient nồng độ, đòi hỏi tiêu tốn năng lượng giải phóng từ hô hấp tế bào. Các protein vận chuyển đặc hiệu trên màng liên kết với ion và sử dụng năng lượng ATP để thay đổi hình dạng cấu thể, bơm các ion khoáng như nitrat vào tế bào lông hút của rễ cây ngay cả khi nồng độ dinh dưỡng trong đất xung quanh cực kỳ loãng."
        }
    ]

    major_sections = [
        {"id": "sec_diffusion", "title": "1. Khuyếch tán (Diffusion)"},
        {"id": "sec_osmosis", "title": "2. Thẩm thấu & Thế nước (Osmosis)"},
        {"id": "sec_active_transport", "title": "3. Vận chuyển Chủ động (Active Transport)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B3 successfully built!")


# ==============================================================================
# TOPIC B4: Biological molecules
# ==============================================================================
async def build_b4():
    lid = '757409b3-5cec-4e1f-8877-18d81e440103'
    code = 'b4'
    title = 'B4: Biological molecules'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    # h2[2] is the main section 1: CẤU TRÚC PHÂN TỬ
    t_h2_0 = h2s[2]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-biomolecules" class="lecture-interactive-card" data-lecture-section="sec_biomolecules" style="cursor: pointer; ')
    
    # h2[3] is the main section 2: CHEMICAL FOOD TESTS
    t_h2_1 = h2s[3]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-food-tests" class="lecture-interactive-card" data-lecture-section="sec_food_tests" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B4 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B4: Phân tử Sinh học & Phòng Thí nghiệm",
            "selector": "#sec-header",
            "en": "Welcome to Topic B4: Biological molecules. All living organisms are assembled from organic chemical building blocks. In this lesson, we study the chemical composition and monomer units of carbohydrates, lipids, proteins, and DNA, and master biochemical food tests used in laboratory examinations.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B4: Các phân tử sinh học và Phân tích hóa sinh. Mọi cơ thể sống đều được cấu thành từ các đại phân tử hữu cơ. Trong bài học này, chúng ta sẽ khảo sát thành phần nguyên tố, đơn phân cấu tạo của carbohydrate, lipid, protein, chuỗi xoắn kép DNA và các phản ứng thử nghiệm thực phẩm tiêu chuẩn."
        },
        {
            "id": "sec_biomolecules",
            "title": "1. Cấu trúc Hóa học: Carbohydrate, Lipid, Protein & DNA",
            "selector": "#sec-biomolecules",
            "en": "Section 1 details macromolecular structures: Carbohydrates contain carbon, hydrogen, and oxygen. Simple sugars like glucose link into large storage polymers: starch and glycogen, or structural cellulose. Lipids contain carbon, hydrogen, and oxygen, formed from one glycerol molecule joined to three fatty acid chains. Proteins contain carbon, hydrogen, oxygen, nitrogen, and sometimes sulfur; they are polymers of twenty different amino acids whose specific sequence dictates three-dimensional folding and enzyme active site specificity. DNA is a double helix constructed from nucleotide chains paired by complementary nitrogenous bases: Adenine pairs with Thymine, and Cytosine pairs with Guanine.",
            "vi": "Mục một chi tiết hóa cấu trúc các đại phân tử sinh học: Carbohydrate gồm carbon, hydro và oxy. Các đường đơn như glucose liên kết tạo thành đại phân tử dự trữ tinh bột, glycogen hoặc cellulose cấu trúc. Lipid chứa carbon, hydro và oxy, cấu tạo từ một phân tử glycerol gắn với 3 chuỗi axit béo. Protein chứa carbon, hydro, oxy, nitơ và lưu huỳnh; được cấu tạo từ 20 loại axit amin khác nhau, trong đó trình tự axit amin quyết định sự cuộn gập không gian 3 chiều và hình thù trung tâm hoạt động của enzyme. DNA là chuỗi xoắn kép cấu tạo từ các nucleotide liên kết theo nguyên tắc bổ sung: Adenine bắt cặp với Thymine, và Cytosine bắt cặp với Guanine."
        },
        {
            "id": "sec_food_tests",
            "title": "2. Thử nghiệm Hóa sinh Thực phẩm (Qualitative Food Tests)",
            "selector": "#sec-food-tests",
            "en": "Section 2 reviews standard Cambridge food test protocols: To test for reducing sugars like glucose, add Benedict's reagent and heat in an 80-degree water bath; a positive result changes from blue to green, yellow, orange, and finally brick-red precipitate. To test for starch, add iodine solution; positive turns from yellow-brown to blue-black. To test for proteins, add Biuret reagent; positive turns from pale blue to purple or violet. To test for lipids, dissolve sample in ethanol, then pour into water; positive produces a cloudy white emulsion. To test for vitamin C, add DCPIP; positive decolourises the blue dye.",
            "vi": "Mục hai tổng hợp các quy trình thử nghiệm hóa sinh thực phẩm: Để thử đường khử như glucose, nhỏ thuốc thử Benedict và đun cách thủy ở 80 độ C; kết quả dương tính chuyển từ xanh lam sang xanh lục, vàng, cam và kết tủa đỏ gạch. Để thử tinh bột, nhỏ dung dịch iot; kết quả dương tính chuyển từ nâu vàng sang xanh đen. Để thử protein, dùng thuốc thử Biuret; kết quả dương tính chuyển từ xanh lam nhạt sang màu tím biếc. Để thử lipid, hòa tan mẫu vào cồn ethanol rồi đổ vào nước cất; dương tính tạo lớp nhũ tương trắng đục như sữa. Để thử vitamin C, nhỏ thuốc thử DCPIP; dương tính làm mất màu xanh của dung dịch."
        }
    ]

    major_sections = [
        {"id": "sec_biomolecules", "title": "1. Cấu trúc Hóa học Carbohydrate, Lipid, Protein & DNA"},
        {"id": "sec_food_tests", "title": "2. Thử nghiệm Hóa sinh Thực phẩm"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B4 successfully built!")


# ==============================================================================
# TOPIC B5: Enzymes
# ==============================================================================
async def build_b5():
    lid = '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e'
    code = 'b5'
    title = 'B5: Enzymes'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-enzyme-nature" class="lecture-interactive-card" data-lecture-section="sec_enzyme_nature" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-lock-and-key" class="lecture-interactive-card" data-lecture-section="sec_lock_and_key" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-temp-ph" class="lecture-interactive-card" data-lecture-section="sec_temp_ph" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B5 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B5: Enzyme & Động học Xúc tác Sinh học",
            "selector": "#sec-header",
            "en": "Welcome to Topic B5: Enzymes. Enzymes are the biological catalysts that drive every biochemical reaction essential for life. In this topic, we examine enzyme protein structure, model catalytic mechanisms via the Lock and Key hypothesis, and analyze rate curves under changing temperatures and pH conditions.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B5: Enzyme và Động học Xúc tác Sinh học. Enzyme là các chất xúc tác sinh học điều khiển mọi phản ứng trao đổi chất duy trì sự sống. Trong bài học này, chúng ta sẽ khảo sát bản chất protein của enzyme, mô hình xúc tác chìa khóa và ổ khóa, cùng đồ thị động học chịu ảnh hưởng của nhiệt độ và độ pH."
        },
        {
            "id": "sec_enzyme_nature",
            "title": "1. Bản chất & Đặc tính của Enzyme (Properties of Enzymes)",
            "selector": "#sec-enzyme-nature",
            "en": "Section 1 defines Enzymes: biological catalysts composed of globular proteins that increase the rate of chemical reactions without being modified or used up in the reaction. Because enzymes remain chemically unaltered, small quantities can catalyze the turnover of thousands of substrate molecules per second.",
            "vi": "Mục một định nghĩa Enzyme: là các chất xúc tác sinh học có bản chất protein hình cầu, làm tăng tốc độ các phản ứng sinh hóa mà không bị tiêu hao hay biến đổi sau phản ứng. Nhờ không bị tiêu tốn trong phản ứng, một lượng nhỏ enzyme có thể xúc tác chuyển hóa hàng nghìn phân tử cơ chất trong mỗi giây."
        },
        {
            "id": "sec_lock_and_key",
            "title": "2. Cơ chế Hoạt động: Thuyết Ổ khóa và Chìa khóa (Lock & Key)",
            "selector": "#sec-lock-and-key",
            "en": "Section 2 investigates catalytic mechanisms: Each enzyme possesses a specifically shaped 3D active site. Under the Lock and Key hypothesis, only a substrate molecule with a complementary geometric shape fits into the active site, forming a temporary enzyme-substrate complex. The enzyme lowers the reaction's activation energy, converting substrate into products which leave the active site, freeing it for subsequent cycles.",
            "vi": "Mục hai nghiên cứu cơ chế xúc tác: Mỗi enzyme sở hữu một trung tâm hoạt động (active site) có cấu trúc không gian 3 chiều đặc thù. Theo thuyết Chìa khóa và Ổ khóa, chỉ cơ chất có hình dạng hình học tương thích bổ sung mới có thể gắn khớp vào trung tâm hoạt động, tạo thành phức hệ enzyme - cơ chất tạm thời. Enzyme làm giảm năng lượng hoạt hóa của phản ứng, biến đổi cơ chất thành sản phẩm rồi giải phóng sản phẩm, trả lại trung tâm hoạt động nguyên vẹn cho chu trình tiếp theo."
        },
        {
            "id": "sec_temp_ph",
            "title": "3. Ảnh hưởng của Nhiệt độ & Độ pH lên Hoạt tính Enzyme",
            "selector": "#sec-temp-ph",
            "en": "Section 3 analyzes environmental factors: As temperature rises from low levels, kinetic energy increases, yielding more frequent successful collisions between enzyme active sites and substrates, accelerating the rate up to an optimum temperature, typically around 37 degrees Celsius in humans. Beyond the optimum, excessive thermal vibrations break hydrogen and ionic bonds holding the tertiary structure, causing denaturation: the active site permanently alters its shape, substrate can no longer bind, and activity plummets to zero. Similarly, deviations from the optimum pH disrupt ionic charges and denature the active site.",
            "vi": "Mục ba phân tích các yếu tố môi trường: Khi nhiệt độ tăng từ mức thấp, động năng phân tử gia tăng, làm tăng tần suất va chạm hiệu quả giữa trung tâm hoạt động và cơ chất, đẩy tốc độ phản ứng lên mức nhiệt độ tối ưu (khoảng 37 độ C ở cơ thể người). Vượt qua điểm tối ưu, dao động nhiệt quá mạnh phá vỡ các liên kết hydro và ion duy trì cấu trúc bậc ba, dẫn đến hiện tượng biến tính (denaturation): trung tâm hoạt động biến dạng vĩnh viễn, cơ chất không thể gắn vào và hoạt tính tụt dốc về 0. Tương tự, sự lệch khỏi độ pH tối ưu sẽ làm thay đổi điện tích các nhóm ion và gây biến tính trung tâm hoạt động."
        }
    ]

    major_sections = [
        {"id": "sec_enzyme_nature", "title": "1. Bản chất & Đặc tính của Enzyme"},
        {"id": "sec_lock_and_key", "title": "2. Thuyết Ổ khóa và Chìa khóa"},
        {"id": "sec_temp_ph", "title": "3. Ảnh hưởng của Nhiệt độ & pH"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B5 successfully built!")


# ==============================================================================
# MAIN BATCH 1 RUNNER (TOPICS B1 -> B5)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 1: TOPICS B1 -> B5")
    print("*******************************************************\n")
    
    await build_b1()
    await asyncio.sleep(2)
    
    await build_b2()
    await asyncio.sleep(2)
    
    await build_b3()
    await asyncio.sleep(2)
    
    await build_b4()
    await asyncio.sleep(2)
    
    await build_b5()
    
    print("\n*******************************************************")
    print("BATCH 1 COMPLETE: TOPICS B1 -> B5 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
