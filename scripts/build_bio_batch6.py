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
# TOPIC 19: Organisms and their environment
# ==============================================================================
async def build_19():
    lid = '7b2384dd-b79d-47fe-b36b-7abf36784f06'
    code = '19'
    title = 'Topic 19: Organisms and their environment'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🌍 1. KEY ECOLOGICAL DEFINITIONS
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-ecological-definitions" class="lecture-interactive-card" data-lecture-section="sec_ecological_definitions" style="cursor: pointer; ')
    
    # h2[1]: ⛓️ 2. FOOD CHAINS & ENERGY FLOW
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-food-chains-energy" class="lecture-interactive-card" data-lecture-section="sec_food_chains_energy" style="cursor: pointer; ')
    
    # h2[2]: ♻️ 3. THE CARBON CYCLE
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-carbon-cycle" class="lecture-interactive-card" data-lecture-section="sec_carbon_cycle" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 19 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 19: Sinh vật và Môi trường Sinh thái",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 19: Organisms and their environment. Ecology explores the intricate relationships between living organisms and physical habitats. In this lesson, we study core ecological definitions, food chains, webs, and trophic energy loss, and analyze the carbon cycle.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 19: Sinh vật và Môi trường Sinh thái. Sinh thái học khám phá mối quan hệ tương tác phức tạp giữa sinh vật sống và sinh cảnh tự nhiên. Trong bài học này, chúng ta sẽ khảo sát các định nghĩa sinh thái cốt lõi, chuỗi thức ăn, lưới thức ăn, quy luật thất thoát năng lượng và vòng tuần hoàn cacbon."
        },
        {
            "id": "sec_ecological_definitions",
            "title": "1. Thuật ngữ Sinh thái: Quần thể, Quần xã & Hệ sinh thái",
            "selector": "#sec-ecological-definitions",
            "en": "Section 1 defines ecological foundations: A Population is a group of organisms of one species living in the same area at the same time. A Community is all of the populations of different species in an ecosystem. An Ecosystem is a unit containing a community of organisms and their abiotic environment, interacting together.",
            "vi": "Mục một định nghĩa các khái niệm nền tảng: Quần thể (Population) là tập hợp các cá thể thuộc cùng một loài cùng sinh sống trong một sinh cảnh tại một thời điểm xác định. Quần xã (Community) là tập hợp tất cả các quần thể thuộc các loài khác nhau cùng tồn tại trong một hệ sinh thái. Hệ sinh thái (Ecosystem) là một chỉnh thể bao gồm quần xã sinh vật và môi trường vô sinh (abiotic) tương tác chặt chẽ với nhau."
        },
        {
            "id": "sec_food_chains_energy",
            "title": "2. Chuỗi Thức ăn, Lưới Thức ăn & Dòng Năng lượng (Quy tắc 10%)",
            "selector": "#sec-food-chains-energy",
            "en": "Section 2 investigates energy flow: The primary source of energy is sunlight, converted into organic chemical energy by photosynthetic producers. Energy passes along trophic levels from primary consumers to apex predators. However, approximately 90% of energy is lost at each transfer as heat through respiration, locomotion, excretion, and uneaten tissue. Because only roughly 10% is incorporated into new biomass, food chains rarely exceed four to five links.",
            "vi": "Mục hai nghiên cứu dòng năng lượng: Nguồn năng lượng sơ cấp cho mọi hệ sinh thái là ánh sáng mặt trời, được sinh vật sản xuất quang hợp chuyển thành hóa năng dự trữ. Năng lượng truyền qua các bậc dinh dưỡng từ sinh vật tiêu thụ bậc một đến các loài săn mồi đỉnh. Tuy nhiên, khoảng 90% năng lượng bị thất thoát ở mỗi bậc dinh dưỡng dưới dạng nhiệt từ hô hấp, vận động, bài tiết và các phần không ăn được. Vì chỉ có khoảng 10% năng lượng được tích lũy thành sinh khối mới, nên các chuỗi thức ăn trong tự nhiên hiếm khi dài quá 4 đến 5 mắt xích."
        },
        {
            "id": "sec_carbon_cycle",
            "title": "3. Vòng tuần hoàn Cacbon (The Carbon Cycle)",
            "selector": "#sec-carbon-cycle",
            "en": "Section 3 details the Carbon Cycle: Atmospheric carbon dioxide is removed solely by plant photosynthesis. Carbon returns to the atmosphere through three major avenues: cellular respiration by plants, animals, and decomposers; combustion of fossil fuels; and microbial decomposition of dead organic matter. Human combustion of coal, oil, and gas, coupled with deforestation, disrupts this equilibrium and drives global climate change.",
            "vi": "Mục ba phân tích chi tiết Vòng tuần hoàn Cacbon: Khí CO2 trong khí quyển chỉ được hấp thu duy nhất qua quá trình quang hợp của thực vật. Cacbon được hoàn trả lại khí quyển qua 3 con đường chính: hô hấp tế bào của thực vật, động vật và vi sinh vật; quá trình đốt cháy nhiên liệu hóa thạch; và sự phân hủy xác sinh vật của vi khuẩn và nấm. Hoạt động đốt than đá, dầu mỏ và nạn phá rừng của con người đang làm mất cân bằng vòng tuần hoàn này, dẫn đến biến đổi khí hậu toàn cầu."
        }
    ]

    major_sections = [
        {"id": "sec_ecological_definitions", "title": "1. Thuật ngữ Sinh thái học"},
        {"id": "sec_food_chains_energy", "title": "2. Chuỗi Thức ăn & Quy tắc 10%"},
        {"id": "sec_carbon_cycle", "title": "3. Vòng tuần hoàn Cacbon"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 19 successfully built!")


# ==============================================================================
# TOPIC 20: Human influences on ecosystems
# ==============================================================================
async def build_20():
    lid = '7777b4df-68dd-4600-b4ba-a4ce56ecc6ac'
    code = '20'
    title = 'Topic 20: Human influences on ecosystems'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🌾 1. FOOD SUPPLY & AGRICULTURE
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-agriculture" class="lecture-interactive-card" data-lecture-section="sec_agriculture" style="cursor: pointer; ')
    
    # h2[1]: 🚜 2. HABITAT DESTRUCTION
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-deforestation" class="lecture-interactive-card" data-lecture-section="sec_deforestation" style="cursor: pointer; ')
    
    # h2[2]: ☠️ 3. POLLUTION
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-eutrophication" class="lecture-interactive-card" data-lecture-section="sec_eutrophication" style="cursor: pointer; ')
    
    # h2[3]: 🌍 4. CLIMATE CHANGE & ACID RAIN
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-climate-acid-rain" class="lecture-interactive-card" data-lecture-section="sec_climate_acid_rain" style="cursor: pointer; ')
    
    # h2[4]: 🛡️ 5. CONSERVATION
    t_h2_4 = str(h2s[4])
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-conservation" class="lecture-interactive-card" data-lecture-section="sec_conservation" style="cursor: pointer; ')
    
    # h2[5]: 🧬 6. ENDANGERED SPECIES & CAPTIVE BREEDING
    t_h2_5 = str(h2s[5])
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-captive-breeding" class="lecture-interactive-card" data-lecture-section="sec_captive_breeding" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 20 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 20: Tác động của Con người lên Hệ sinh thái",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 20: Human influences on ecosystems. Expanding human populations exert unprecedented pressures on the biosphere. In this comprehensive lesson, we analyze modern agriculture, deforestation, the exact stages of eutrophication, global warming and acid rain, and wildlife conservation programmes.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 20: Tác động của Con người lên Hệ sinh thái. Dân số nhân loại gia tăng đang tạo áp lực chưa từng có lên sinh quyển. Trong bài học này, chúng ta sẽ khảo sát nông nghiệp hiện đại, nạn phá rừng, các bước diễn biến của hiện tượng phú dưỡng, biến đổi khí hậu, mưa axit và các chương trình bảo tồn loài nguy cấp."
        },
        {
            "id": "sec_agriculture",
            "title": "1. Nông nghiệp & Cung ứng Lương thực (Monoculture)",
            "selector": "#sec-agriculture",
            "en": "Section 1 examines agricultural intensification: Monocultures cultivate a single crop over vast areas, which drastically reduces biodiversity and creates ideal conditions for pest infestations, demanding heavy pesticide applications. Intensive livestock farming increases food yields but raises animal welfare concerns, disease transmission risks, and high greenhouse gas emissions like methane.",
            "vi": "Mục một phân tích thâm canh nông nghiệp: Độc canh (Monoculture) gieo trồng duy nhất một giống cây trên diện tích bạt ngàn, làm suy giảm nghiêm trọng đa dạng sinh học và tạo điều kiện cho sâu bệnh bùng phát, buộc nông dân phải dùng nhiều thuốc trừ sâu hóa học. Chăn nuôi gia súc tập trung giúp tăng sản lượng thịt sữa nhưng gây lo ngại về đạo đức động vật, nguy cơ lây lan dịch bệnh và phát thải lượng lớn khí methane."
        },
        {
            "id": "sec_deforestation",
            "title": "2. Phá hủy Môi trường sống & Nạn Phá rừng (Deforestation)",
            "selector": "#sec-deforestation",
            "en": "Section 2 investigates Deforestation: Forests are felled for agricultural land, timber, and urban expansion. Ecological damages include topsoil erosion when tree roots no longer bind soil particles; severe flooding because rainfall runs off rapidly; destruction of natural habitats driving species extinction; and loss of massive carbon sinks, elevating atmospheric carbon dioxide levels.",
            "vi": "Mục hai nghiên cứu Nạn phá rừng (Deforestation): Rừng bị đốn hạ để lấy đất trồng trọt, khai thác gỗ và mở rộng đô thị. Hậu quả sinh thái nghiêm trọng gồm xói mòn lớp đất mặt màu mỡ do mất mạng lưới rễ cây giữ đất; gia tăng lũ lụt do nước mưa chảy tràn; phá hủy môi trường sống dẫn đến tuyệt chủng giống loài; và làm mất đi bể hấp thu carbon khổng lồ, khiến lượng CO2 trong khí quyển tăng vọt."
        },
        {
            "id": "sec_eutrophication",
            "title": "3. Ô nhiễm Nước & Hiện tượng Phú dưỡng (Eutrophication)",
            "selector": "#sec-eutrophication",
            "en": "Section 3 details the classic five-step Eutrophication sequence: First, excess mineral fertilizers or untreated sewage leach into lakes and rivers. Second, algae rapidly proliferate into an algal bloom, blanketing the water surface and blocking sunlight. Third, submerged aquatic plants cannot photosynthesize and die. Fourth, aerobic bacteria multiply rapidly as they decompose the dead vegetation, consuming all dissolved oxygen. Fifth, aquatic animals like fish suffocate from lack of oxygen.",
            "vi": "Mục ba mô tả 5 bước kinh điển của Hiện tượng Phú dưỡng (Eutrophication): Bước 1: Phân bón hóa học dư thừa chứa nitrat và photphat hoặc nước thải chưa xử lý rửa trôi xuống sông hồ. Bước 2: Tảo sinh sôi nở hoa bùng phát (algal bloom), che phủ kín mặt nước ngăn ánh sáng mặt trời. Bước 3: Các loài thực vật thủy sinh dưới đáy không thể quang hợp và chết dần. Bước 4: Vi khuẩn phân hủy hiếu khí tăng sinh theo cấp số nhân để tiêu thụ xác thực vật, hút cạn toàn bộ oxy hòa tan trong nước. Bước 5: Các loài cá và động vật thủy sinh ngạt thở và chết hàng loạt do thiếu dưỡng khí."
        },
        {
            "id": "sec_climate_acid_rain",
            "title": "4. Biến đổi Khí hậu & Mưa Axit",
            "selector": "#sec-climate-acid-rain",
            "en": "Section 4 covers atmospheric pollution: The enhanced greenhouse effect results from elevated carbon dioxide from fossil fuel combustion and methane from livestock and rice paddy decomposition, trapping thermal infrared radiation within the atmosphere and driving global warming. Acid rain is produced when sulfur dioxide from coal power plants and nitrogen oxides from vehicles dissolve into rain clouds, forming dilute sulfuric and nitric acids that lower lake pH and damage tree foliage.",
            "vi": "Mục bốn phân tích ô nhiễm khí quyển: Hiệu ứng nhà kính tăng cường do khí CO2 từ đốt cháy nhiên liệu hóa thạch và khí methane từ chăn nuôi gia súc giữ lại bức xạ hồng ngoại, gây hiện tượng nóng lên toàn cầu. Mưa axit hình thành khi khí sulfur dioxide SO2 từ các nhà máy nhiệt điện than và oxit nitơ từ khói xe hòa tan vào nước mưa tạo thành axit sunfuric và axit nitric loãng, làm chua hóa nguồn nước sông hồ và hủy hoại tán lá rừng."
        },
        {
            "id": "sec_conservation",
            "title": "5. Bảo tồn Đa dạng Sinh học & Động vật Nguy cấp",
            "selector": "#sec-conservation",
            "en": "Section 5 presents Conservation strategies: Sustainable development satisfies current human needs without compromising the ability of future generations to meet their needs. Conservation programmes preserve biodiversity, prevent species extinction, protect vulnerable habitats in national parks, maintain seed banks for crop security, and use captive breeding, artificial insemination, and in vitro fertilization to restore endangered populations.",
            "vi": "Mục năm trình bày các chiến lược Bảo tồn: Phát triển bền vững đáp ứng nhu cầu hiện tại mà không làm tổn hại đến khả năng đáp ứng nhu cầu của các thế hệ tương lai. Các chương trình bảo tồn giúp duy trì đa dạng sinh học, ngăn chặn nguy cơ tuyệt chủng, thành lập các vườn quốc gia bảo vệ sinh cảnh, xây dựng ngân hàng hạt giống và áp dụng kỹ thuật thụ tinh nhân tạo và thụ tinh trong ống nghiệm (IVF) để nhân giống động vật hoang dã nguy cấp."
        },
        {
            "id": "sec_captive_breeding",
            "title": "6. Kỹ thuật Nhân giống Động vật Nguy cấp (Captive Breeding)",
            "selector": "#sec-captive_breeding",
            "en": "Section 6 highlights assisted reproductive technologies for endangered fauna: Artificial Insemination (AI) transfers collected sperm into female reproductive tracts, avoiding transportation stress between zoos. In Vitro Fertilisation (IVF) fertilizes harvested ova in laboratory vessels before implanting embryos into surrogate females. These techniques expand gene pools and minimize genetic inbreeding risks in dwindling populations.",
            "vi": "Mục sáu nêu bật các công nghệ hỗ trợ sinh sản cho động vật nguy cấp: Thụ tinh nhân tạo (Artificial Insemination) đưa tinh trùng vào đường sinh sản của con cái mà không cần phải vận chuyển động vật giữa các vườn thú. Thụ tinh trong ống nghiệm (IVF) kết hợp trứng và tinh trùng trong phòng thí nghiệm rồi cấy phôi vào con cái mang thai hộ. Các công nghệ này giúp đa dạng hóa vốn gen và hạn chế tối đa nguy cơ suy thoái do giao phối cận huyết ở các quần thể số lượng nhỏ."
        }
    ]

    major_sections = [
        {"id": "sec_agriculture", "title": "1. Nông nghiệp Thâm canh & Độc canh"},
        {"id": "sec_deforestation", "title": "2. Nạn Phá rừng & Mất Bể chứa Carbon"},
        {"id": "sec_eutrophication", "title": "3. Phú dưỡng Nguồn nước (Eutrophication)"},
        {"id": "sec_climate_acid_rain", "title": "4. Biến đổi Khí hậu & Mưa Axit"},
        {"id": "sec_conservation", "title": "5. Chiến lược Bảo tồn Đa dạng Sinh học"},
        {"id": "sec_captive_breeding", "title": "6. Nhân giống Bảo tồn (AI & IVF)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 20 successfully built!")


# ==============================================================================
# TOPIC 21: Biotechnology and Genetic Engineering
# ==============================================================================
async def build_21():
    lid = '55023dc0-7fdc-46ea-a3e9-9a049306d086'
    code = '21'
    title = 'Topic 21: Biotechnology and Genetic Engineering'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🦠 1. TẠI SAO LẠI DÙNG VI KHUẨN?
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-why-bacteria" class="lecture-interactive-card" data-lecture-section="sec_why_bacteria" style="cursor: pointer; ')
    
    # h2[1]: 🏭 2. THE INDUSTRIAL FERMENTER
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-industrial-fermenter" class="lecture-interactive-card" data-lecture-section="sec_industrial_fermenter" style="cursor: pointer; ')
    
    # h2[2]: 🧬 3. GENETIC ENGINEERING (Kỹ thuật di truyền)
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-genetic-engineering" class="lecture-interactive-card" data-lecture-section="sec_genetic_engineering" style="cursor: pointer; ')
    
    # h2[3]: 🌾 4. CÂY TRỒNG BIẾN ĐỔI GEN (GM CROPS)
    t_h2_3 = str(h2s[3])
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-gm-crops" class="lecture-interactive-card" data-lecture-section="sec_gm_crops" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 21 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 21: Công nghệ Sinh học & Kỹ thuật Di truyền",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 21: Biotechnology and Genetic Engineering. In this cutting-edge final chapter, we explore industrial microbiology, fermenter design, recombinant DNA technology for human insulin production, and the benefits and hazards of genetically modified crops.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 21: Công nghệ Sinh học và Kỹ thuật Di truyền. Trong bài học kết thúc toàn bộ khóa học này, chúng ta sẽ khảo sát ứng dụng vi sinh vật công nghiệp, cấu tạo nồi lên men, công nghệ DNA tái tổ hợp sản xuất insulin người và các cơ hội cùng thách thức của cây trồng biến đổi gen."
        },
        {
            "id": "sec_why_bacteria",
            "title": "1. Ứng dụng Vi sinh vật trong Công nghệ Sinh học",
            "selector": "#sec-why-bacteria",
            "en": "Section 1 explains why bacteria are ideal organisms in biotechnology: Bacteria reproduce extremely rapidly via binary fission, possess simple nutritional requirements, share universal genetic code with humans, contain circular plasmids ideal for gene insertion, and produce complex proteins without animal ethical objections.",
            "vi": "Mục một giải thích vì sao vi khuẩn là đối tượng lý tưởng trong công nghệ sinh học: Vi khuẩn phân chia nhân đôi cực nhanh, nhu cầu dinh dưỡng đơn giản, sử dụng chung mã di truyền phổ quát với con người, sở hữu các plasmid dạng vòng dễ chèn gen ngoại lai và có thể sản xuất protein phức tạp mà không vướng phải các rào cản đạo đức như thử nghiệm trên động vật."
        },
        {
            "id": "sec_industrial_fermenter",
            "title": "2. Nồi lên men Công nghiệp (The Industrial Fermenter)",
            "selector": "#sec-industrial-fermenter",
            "en": "Section 2 investigates industrial fermenter engineering: Steam sterilization cleans the vessel beforehand to kill unwanted microbes that would compete for nutrients. A cooling water jacket circulates cold water to dissipate excess metabolic heat from respiration, maintaining optimum temperature. Stirring paddles maintain uniform suspension and nutrient access. Probes constantly monitor pH and temperature, while a sterile air sparger supplies oxygen for aerobic respiration.",
            "vi": "Mục hai nghiên cứu cấu tạo kỹ thuật của nồi lên men công nghiệp: Khử trùng bằng luồng hơi nước áp suất cao trước khi nuôi cấy để diệt sạch vi sinh vật tạp nhiễm cạnh tranh dinh dưỡng. Áo làm mát tuần hoàn nước lạnh hấp thu nhiệt lượng tỏa ra từ quá trình hô hấp tế bào để giữ nhiệt độ tối ưu. Cánh khuấy khuấy đều giúp vi sinh vật tiếp xúc liên tục với chất dinh dưỡng. Các đầu dò cảm biến liên tục đo pH và nhiệt độ, kết hợp với sục khí vô trùng cung cấp oxy cho hô hấp hiếu khí."
        },
        {
            "id": "sec_genetic_engineering",
            "title": "3. Kỹ thuật Di truyền & Sản xuất Insulin người (Recombinant DNA)",
            "selector": "#sec-genetic-engineering",
            "en": "Section 3 details the four-step recombinant insulin protocol: Step 1: The human insulin gene is isolated and cut out using a specific restriction endonuclease enzyme, creating complementary sticky ends. Step 2: A bacterial plasmid vector is cut open using the same restriction enzyme. Step 3: The human gene and open plasmid are joined together using DNA ligase enzyme to create a recombinant plasmid. Step 4: The recombinant plasmid is inserted into a host bacterium, which multiplies in fermenters to mass-produce human insulin.",
            "vi": "Mục ba mô tả quy trình 4 bước tạo insulin tái tổ hợp: Bước 1: Phân lập và cắt đoạn gen mã hóa insulin người bằng enzyme giới hạn cắt nối đặc hiệu (restriction enzyme), để lại các đầu dính so le. Bước 2: Dùng chính enzyme giới hạn đó để cắt mở vòng plasmid của vi khuẩn. Bước 3: Nối đoạn gen người vào plasmid nhờ enzyme nối DNA ligase tạo thành plasmid tái tổ hợp. Bước 4: Chuyển plasmid tái tổ hợp vào tế bào vi khuẩn chủ, nuôi cấy nhân dòng trong nồi lên men để sản xuất hàng loạt hormone insulin người phục vụ bệnh nhân tiểu đường."
        },
        {
            "id": "sec_gm_crops",
            "title": "4. Cây trồng Biến đổi Gen (Genetically Modified Crops)",
            "selector": "#sec-gm-crops",
            "en": "Section 4 weighs the advantages and disadvantages of Genetically Modified (GM) crops: Advantages include higher yields, drought tolerance, enhanced nutritional value like vitamin A in Golden Rice, and insect resistance like Bt maize reducing pesticide expenditure. Disadvantages include risks of herbicide-resistance genes transferring to wild weed relatives creating superweeds, potential human allergenicity, and financial dependency on multinational seed patents.",
            "vi": "Mục bốn cân nhắc lợi ích và rủi ro của Cây trồng biến đổi gen (GM crops): Lợi ích gồm tăng năng suất cây trồng, tăng khả năng chịu hạn mặn, nâng cao giá trị dinh dưỡng như gạo Vàng giàu tiền chất vitamin A chống mù lòa và giống ngô Bt mang gen diệt sâu giúp giảm phun thuốc hóa học. Rủi ro tiềm ẩn gồm nguy cơ phát tán gen kháng thuốc diệt cỏ sang cỏ dại bản địa tạo ra siêu cỏ dại khó diệt, nguy cơ dị ứng thực phẩm và sự lệ thuộc kinh tế vào các tập đoàn hạt giống độc quyền."
        }
    ]

    major_sections = [
        {"id": "sec_why_bacteria", "title": "1. Ứng dụng Vi sinh vật trong Công nghệ"},
        {"id": "sec_industrial_fermenter", "title": "2. Cấu tạo Nồi lên men Công nghiệp"},
        {"id": "sec_genetic_engineering", "title": "3. Kỹ thuật Di truyền & Insulin Tái tổ hợp"},
        {"id": "sec_gm_crops", "title": "4. Cây trồng Biến đổi Gen (GM Crops)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 21 successfully built!")


# ==============================================================================
# MAIN BATCH 6 RUNNER (TOPICS 19 -> 21)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING BIOLOGY BATCH 6: TOPICS 19 -> 21")
    print("*******************************************************\n")
    
    await build_19()
    await asyncio.sleep(2)
    
    await build_20()
    await asyncio.sleep(2)
    
    await build_21()
    
    print("\n*******************************************************")
    print("BIOLOGY BATCH 6 COMPLETE: TOPICS 19 -> 21 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
