import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC B16: Inheritance
# ==============================================================================
async def build_b16():
    lid = 'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce'
    code = 'b16'
    title = 'B16: Inheritance'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-genetic-code" class="lecture-interactive-card" data-lecture-section="sec_genetic_code" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-monohybrid-inheritance" class="lecture-interactive-card" data-lecture-section="sec_monohybrid_inheritance" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-pedigree-sex" class="lecture-interactive-card" data-lecture-section="sec_pedigree-sex" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B16 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B16: Di truyền học & Quy luật Phân ly",
            "selector": "#sec-header",
            "en": "Welcome to Topic B16: Inheritance. Inheritance is the transmission of genetic information from generation to generation. In this chapter, we decode chromosomes, genes, and alleles, contrast mitosis and meiosis, master monohybrid Punnett squares, and analyze pedigree charts and sex determination.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B16: Di truyền học và Quy luật Phân ly. Di truyền học nghiên cứu sự truyền đạt thông tin di truyền qua các thế hệ. Trong bài học này, chúng ta sẽ giải mã nhiễm sắc thể, gen và allele, so sánh nguyên phân và giảm phân, làm chủ bảng lai Punnett đơn gen, cùng sơ đồ phả hệ và cơ chế xác định giới tính."
        },
        {
            "id": "sec_genetic_code",
            "title": "1. Mã Di truyền: Nhiễm sắc thể, Gen & Allele",
            "selector": "#sec-genetic-code",
            "en": "Section 1 establishes core genetic foundations: A Chromosome is a thread-like structure of DNA carrying genetic information in the form of genes. A Gene is a length of DNA that codes for a specific protein. An Allele is an alternative version of a gene. A Haploid nucleus contains a single set of unpaired chromosomes, twenty-three in human gametes; a Diploid nucleus contains two complete sets, forty-six chromosomes in human somatic cells. Mitosis produces two genetically identical diploid daughter cells for growth and repair. Meiosis produces four genetically diverse haploid daughter cells for gamete formation.",
            "vi": "Mục một thiết lập các khái niệm di truyền nền tảng: Nhiễm sắc thể (Chromosome) là cấu trúc sợi DNA mang thông tin di truyền dưới dạng các gen. Gen là một đoạn phân tử DNA mã hóa cho một chuỗi polypeptide hoặc protein đặc thù. Allele là các trạng thái biểu hiện khác nhau của cùng một gen. Nhân đơn bội (Haploid) chứa một bộ nhiễm sắc thể đơn, gồm 23 chiếc ở giao tử người; Nhân lưỡng bội (Diploid) chứa hai bộ nhiễm sắc thể tương đồng, gồm 46 chiếc ở tế bào sinh dưỡng. Nguyên phân (Mitosis) tạo ra 2 tế bào con lưỡng bội giống hệt nhau phục vụ sinh trưởng và tái tạo mô. Giảm phân (Meiosis) tạo ra 4 tế bào con đơn bội mang biến dị tổ hợp phong phú để hình thành giao tử."
        },
        {
            "id": "sec_monohybrid_inheritance",
            "title": "2. Di truyền Đơn gen & Bảng lai Punnett (Punnett Square)",
            "selector": "#sec-monohybrid-inheritance",
            "en": "Section 2 investigates monohybrid inheritance: Genotype is the genetic makeup of an organism in terms of alleles present. Phenotype is the observable physical features of an organism. Homozygous organisms have two identical alleles for a particular gene, while Heterozygous organisms possess two different alleles. A Dominant allele is expressed if present; a Recessive allele is expressed only when homozygous. In a monohybrid cross between two heterozygous parents, the theoretical phenotypic ratio among offspring is three dominant to one recessive, yielding a one-to-two-to-one genotypic ratio.",
            "vi": "Mục hai nghiên cứu quy luật di truyền đơn gen: Kiểu gen (Genotype) là tổ hợp toàn bộ các allele của một cơ thể sinh vật. Kiểu hình (Phenotype) là tập hợp các đặc điểm hình thái và sinh lý quan sát được. Đồng hợp tử (Homozygous) mang hai allele giống hệt nhau, trong khi Dị hợp tử (Heterozygous) mang hai allele khác nhau của cùng một gen. Allele trội biểu hiện kiểu hình ngay cả khi ở trạng thái dị hợp; allele lặn chỉ biểu hiện kiểu hình khi ở trạng thái đồng hợp lặn. Trong phép lai giữa hai bố mẹ dị hợp tử, tỷ lệ phân ly kiểu hình lý thuyết ở đời con là 3 trội : 1 lặn, tương ứng tỷ lệ phân ly kiểu gen 1 đồng hợp trội : 2 dị hợp : 1 đồng hợp lặn."
        },
        {
            "id": "sec_pedigree-sex",
            "title": "3. Sơ đồ Phả hệ & Cơ chế Xác định Giới tính",
            "selector": "#sec-pedigree-sex",
            "en": "Section 3 analyzes pedigree charts and sex determination: Human diploid cells contain twenty-two pairs of autosomes and one pair of sex chromosomes. Human females possess two homologous X chromosomes, while males possess one X and one smaller Y chromosome. During meiosis, all ova receive an X chromosome, whereas half of spermatozoa carry an X and half carry a Y, producing a strict one-to-one sex ratio at fertilization. Pedigree diagrams track phenotypic inheritance across multiple family generations.",
            "vi": "Mục ba phân tích sơ đồ phả hệ và cơ chế xác định giới tính: Bộ nhiễm sắc thể lưỡng bội ở người gồm 22 cặp nhiễm sắc thể thường và 1 cặp nhiễm sắc thể giới tính. Nữ giới mang cặp nhiễm sắc thể giới tính tương đồng XX, trong khi nam giới mang cặp dị hình XY. Trong giảm phân, mọi trứng đều mang nhiễm sắc thể X, trong khi một nửa tinh trùng mang X và một nửa mang Y, tạo ra tỷ lệ giới tính xấp xỉ 1 nam : 1 nữ khi thụ tinh. Sơ đồ phả hệ giúp theo dõi quy luật di truyền và xác suất xuất hiện bệnh di truyền qua các thế hệ gia đình."
        }
    ]

    major_sections = [
        {"id": "sec_genetic_code", "title": "1. Khái niệm Nhiễm sắc thể, Gen & Allele"},
        {"id": "sec_monohybrid_inheritance", "title": "2. Di truyền Đơn gen & Bảng lai Punnett"},
        {"id": "sec_pedigree-sex", "title": "3. Phả hệ & Xác định Giới tính (XX/XY)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B16 successfully built!")


# ==============================================================================
# TOPIC B17: Variation and selection
# ==============================================================================
async def build_b17():
    lid = '24f0deeb-3cd9-4b82-b253-5a070ca31275'
    code = 'b17'
    title = 'B17: Variation and selection'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-variation-mutation" class="lecture-interactive-card" data-lecture-section="sec_variation_mutation" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-adaptive-features" class="lecture-interactive-card" data-lecture-section="sec_adaptive_features" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-natural-selection" class="lecture-interactive-card" data-lecture-section="sec_natural_selection" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B17 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B17: Biến dị, Thích nghi & Chọn lọc Tự nhiên",
            "selector": "#sec-header",
            "en": "Welcome to Topic B17: Variation and selection. Biological variation is the raw substrate of evolutionary change. In this chapter, we classify continuous and discontinuous variation, examine mutation causes, analyze xerophyte and hydrophyte adaptations, and study natural selection versus selective breeding.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B17: Biến dị, Thích nghi và Chọn lọc Tự nhiên. Biến dị sinh học là nguyên liệu thô thúc đẩy tiến hóa. Trong bài học này, chúng ta sẽ phân biệt biến dị liên tục và không liên tục, nguyên nhân gây đột biến, cấu tạo thích nghi của thực vật chịu hạn và thủy sinh, cùng cơ chế chọn lọc tự nhiên và chọn giống nhân tạo."
        },
        {
            "id": "sec_variation_mutation",
            "title": "1. Biến dị Liên tục, Không liên tục & Đột biến (Mutation)",
            "selector": "#sec-variation-mutation",
            "en": "Section 1 classifies biological variation: Continuous variation produces a smooth quantitative spectrum of phenotypes influenced by multiple genes and environmental factors, forming a bell-shaped normal distribution curve like human height and body mass. Discontinuous variation produces distinct qualitative categories determined purely by genetics without intermediate phenotypes, like human ABO blood groups. A Mutation is a spontaneous change in the base sequence of DNA, forming the primary source of novel alleles, accelerated by ionizing radiation and mutagenic chemicals.",
            "vi": "Mục một phân loại các dạng biến dị: Biến dị liên tục là dải kiểu hình định lượng liên tục chịu sự tác động đồng thời của nhiều gen và môi trường, tạo thành đồ thị phân bố chuẩn hình chuông như chiều cao và cân nặng ở người. Biến dị không liên tục phân thành các nhóm kiểu hình định tính rõ rệt hoàn toàn do gen quy định mà không có dạng trung gian, như nhóm máu ABO. Đột biến (Mutation) là sự biến đổi đột ngột trong trình tự nucleotide của phân tử DNA, là nguồn gốc sơ cấp tạo ra các allele mới, gia tăng khi tiếp xúc với tia phóng xạ ion hóa và hóa chất độc hại."
        },
        {
            "id": "sec_adaptive_features",
            "title": "2. Đặc điểm Thích nghi: Thực vật Sa mạc (Xerophytes) & Thủy sinh (Hydrophytes)",
            "selector": "#sec-adaptive-features",
            "en": "Section 2 investigates Adaptive Features: inherited functional characteristics that increase an organism's survival and reproductive fitness in a specific environment. Xerophytes thrive in arid habitats through thick waxy cuticles, sunken stomata in protective pits trapping humid air, rolled leaves, and extensive root systems. Hydrophytes flourish in aquatic habitats with thin cuticles, stomata situated on upper leaf surfaces for atmospheric gas access, and extensive aerenchyma air tissues providing buoyancy.",
            "vi": "Mục hai nghiên cứu Đặc điểm thích nghi: là những đặc tính hình thái hoặc sinh lý di truyền giúp sinh vật sống sót và sinh sản tối ưu trong sinh cảnh của chúng. Thực vật chịu hạn (Xerophytes) sống ở sa mạc khô cằn có lớp cutin sáp dày, khí khổng nằm sâu trong các hốc để giữ ẩm, lá cuộn tròn hoặc tiêu biến thành gai và rễ cắm rất sâu. Thực vật thủy sinh (Hydrophytes) sống dưới nước có lớp cutin rất mỏng, khí khổng nằm ở mặt trên của lá để trao đổi khí trực tiếp với khí quyển và mô chứa khí (aerenchyma) xốp giúp cây nổi trên mặt nước."
        },
        {
            "id": "sec_natural_selection",
            "title": "3. Chọn lọc Tự nhiên vs Chọn giống Nhân tạo",
            "selector": "#sec-natural-selection",
            "en": "Section 3 outlines Natural Selection: Organisms produce more offspring than the environment can sustain, creating a struggle for existence. Random mutations yield phenotypic variation. Individuals with advantageous adaptive features have higher survival and reproductive success, passing advantageous alleles to successive generations, causing progressive adaptation. In contrast, Selective Breeding involves humans selecting individuals exhibiting desirable economic traits over many generations to produce domestic crops and livestock.",
            "vi": "Mục ba phác thảo Chọn lọc Tự nhiên: Sinh vật sinh ra số lượng con non nhiều hơn mức môi trường có thể nuôi sống, dẫn đến đấu tranh sinh tồn. Các đột biến ngẫu nhiên tạo nên biến dị kiểu hình phong phú. Những cá thể sở hữu đặc điểm thích nghi có ưu thế sinh tồn cao hơn, sống sót đến tuổi sinh sản và truyền lại các allele có lợi cho đời sau, dẫn đến sự tiến hóa thích nghi của quần thể. Ngược lại, Chọn giống Nhân tạo do con người chủ động chọn lọc và lai phối các cá thể mang tính trạng mong muốn qua nhiều thế hệ để phục vụ mục đích kinh tế."
        }
    ]

    major_sections = [
        {"id": "sec_variation_mutation", "title": "1. Biến dị Liên tục, Không liên tục & Đột biến"},
        {"id": "sec_adaptive_features", "title": "2. Thực vật Sa mạc vs Thủy sinh"},
        {"id": "sec_natural_selection", "title": "3. Chọn lọc Tự nhiên vs Chọn giống Nhân tạo"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B17 successfully built!")


# ==============================================================================
# TOPIC B18: Organisms and their environment
# ==============================================================================
async def build_b18():
    lid = 'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0'
    code = 'b18'
    title = 'B18: Organisms and their environment'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-ecological-definitions" class="lecture-interactive-card" data-lecture-section="sec_ecological_definitions" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-food-chains-energy" class="lecture-interactive-card" data-lecture-section="sec_food_chains_energy" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-carbon-cycle" class="lecture-interactive-card" data-lecture-section="sec_carbon_cycle" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B18 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B18: Sinh thái học & Vòng tuần hoàn Cacbon",
            "selector": "#sec-header",
            "en": "Welcome to Topic B18: Organisms and their environment. Ecology investigates interactions between organisms and physical habitats. In this lesson, we study key ecological definitions, analyze trophic levels and energy loss along food webs, and trace the global carbon cycle.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B18: Sinh vật và Môi trường Sinh thái. Sinh thái học khám phá mối tương tác phức tạp giữa sinh vật sống và sinh cảnh tự nhiên. Trong bài học này, chúng ta sẽ khảo sát các khái niệm sinh thái học nền tảng, bậc dinh dưỡng và dòng năng lượng trong chuỗi thức ăn, cùng vòng tuần hoàn cacbon toàn cầu."
        },
        {
            "id": "sec_ecological_definitions",
            "title": "1. Khái niệm Sinh thái: Quần thể, Quần xã & Hệ sinh thái",
            "selector": "#sec-ecological-definitions",
            "en": "Section 1 defines ecological foundations: A Population is a group of organisms of one species living in the same area at the same time. A Community is all of the populations of different species in an ecosystem. An Ecosystem is a unit containing a community of organisms and their abiotic physical environment, interacting together as a functional system.",
            "vi": "Mục một định nghĩa các khái niệm nền tảng: Quần thể (Population) là tập hợp các cá thể thuộc cùng một loài cùng sinh sống trong một sinh cảnh tại một thời điểm xác định. Quần xã (Community) là tập hợp tất cả các quần thể thuộc các loài khác nhau cùng tồn tại trong một hệ sinh thái. Hệ sinh thái (Ecosystem) là một chỉnh thể bao gồm quần xã sinh vật và môi trường vô sinh (abiotic) tương tác chặt chẽ với nhau."
        },
        {
            "id": "sec_food_chains_energy",
            "title": "2. Chuỗi Thức ăn, Bậc Dinh dưỡng & Quy luật 10% Năng lượng",
            "selector": "#sec-food-chains-energy",
            "en": "Section 2 investigates energy flow: The principal energy source for almost all ecosystems is sunlight, harnessed by photosynthetic producers. Energy passes along trophic levels from primary consumers to apex predators. Crucially, approximately 90% of energy is lost at each trophic transfer as heat from cellular respiration, kinetic movement, excretion of metabolic wastes, and uneaten organic tissues. Because only roughly 10% of energy is converted into new biomass, food chains rarely exceed four to five links.",
            "vi": "Mục hai nghiên cứu dòng năng lượng: Nguồn năng lượng sơ cấp cho mọi hệ sinh thái là ánh sáng mặt trời, được sinh vật sản xuất quang hợp chuyển thành hóa năng dự trữ. Năng lượng truyền qua các bậc dinh dưỡng từ sinh vật tiêu thụ bậc một đến các loài săn mồi đỉnh. Điểm mấu chốt: khoảng 90% năng lượng bị thất thoát ở mỗi bậc dinh dưỡng dưới dạng nhiệt từ hô hấp, vận động, bài tiết và các phần không ăn được. Vì chỉ có khoảng 10% năng lượng được tích lũy thành sinh khối mới, nên các chuỗi thức ăn trong tự nhiên hiếm khi dài quá 4 đến 5 mắt xích."
        },
        {
            "id": "sec_carbon_cycle",
            "title": "3. Vòng Tuần hoàn Cacbon Toàn cầu (The Carbon Cycle)",
            "selector": "#sec-carbon-cycle",
            "en": "Section 3 details the Carbon Cycle: Atmospheric carbon dioxide is removed solely by plant photosynthesis. Carbon returns to the atmosphere through three major avenues: cellular respiration by plants, animals, and decomposers; combustion of fossil fuels; and microbial decomposition of dead organic matter. Human combustion of fossil fuels and extensive deforestation disrupt this equilibrium, increasing greenhouse gas concentrations and accelerating global climate change.",
            "vi": "Mục ba phân tích chi tiết Vòng tuần hoàn Cacbon: Khí CO2 trong khí quyển chỉ được hấp thu duy nhất qua quá trình quang hợp của thực vật. Cacbon được hoàn trả lại khí quyển qua 3 con đường chính: hô hấp tế bào của thực vật, động vật và vi sinh vật; quá trình đốt cháy nhiên liệu hóa thạch; và sự phân hủy xác sinh vật của vi khuẩn và nấm. Hoạt động đốt than đá, dầu mỏ và nạn phá rừng của con người đang làm mất cân bằng vòng tuần hoàn này, dẫn đến biến đổi khí hậu toàn cầu."
        }
    ]

    major_sections = [
        {"id": "sec_ecological_definitions", "title": "1. Khái niệm Sinh thái học"},
        {"id": "sec_food_chains_energy", "title": "2. Chuỗi Thức ăn & Quy tắc 10%"},
        {"id": "sec_carbon_cycle", "title": "3. Vòng tuần hoàn Cacbon"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B18 successfully built!")


# ==============================================================================
# TOPIC B19: Human influences on ecosystems
# ==============================================================================
async def build_b19():
    lid = '298327a8-455a-44d5-9a4c-164e2653c456'
    code = 'b19'
    title = 'B19: Human influences on ecosystems'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-agriculture" class="lecture-interactive-card" data-lecture-section="sec_agriculture" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-deforestation" class="lecture-interactive-card" data-lecture-section="sec_deforestation" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-eutrophication" class="lecture-interactive-card" data-lecture-section="sec_eutrophication" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-conservation" class="lecture-interactive-card" data-lecture-section="sec_conservation" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic B19 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề B19: Tác động của Con người lên Hệ sinh thái",
            "selector": "#sec-header",
            "en": "Welcome to Topic B19: Human influences on ecosystems. Expanding human activity exerts severe pressure on the biosphere. In this final biology chapter, we examine agricultural monocultures, deforestation, the exact stages of aquatic eutrophication, and modern biodiversity conservation strategies.",
            "vi": "Chào mừng các bạn đến với Chuyên đề B19: Tác động của Con người lên Hệ sinh thái. Hoạt động của con người đang gây áp lực nghiêm trọng lên sinh quyển. Trong bài học kết thúc phần sinh học này, chúng ta sẽ khảo sát độc canh nông nghiệp, nạn phá rừng, chuỗi diễn biến phú dưỡng nguồn nước và các chiến lược bảo tồn đa dạng sinh học."
        },
        {
            "id": "sec_agriculture",
            "title": "1. Nông nghiệp Thâm canh & Độc canh (Monoculture)",
            "selector": "#sec-agriculture",
            "en": "Section 1 analyzes modern agriculture: Monoculture is the continuous cultivation of a single crop over vast areas. Monocultures drastically reduce biodiversity and create ideal conditions for pest explosions, requiring heavy chemical insecticide and herbicide applications. Intensive livestock farming increases meat yields but raises animal welfare concerns and high greenhouse emissions.",
            "vi": "Mục một phân tích nông nghiệp thâm canh: Độc canh (Monoculture) gieo trồng duy nhất một giống cây trên diện tích bạt ngàn, làm suy giảm nghiêm trọng đa dạng sinh học và tạo điều kiện cho sâu bệnh bùng phát, buộc nông dân phải dùng nhiều thuốc trừ sâu hóa học. Chăn nuôi gia súc tập trung giúp tăng sản lượng thịt sữa nhưng gây lo ngại về đạo đức động vật và phát thải lượng lớn khí nhà kính."
        },
        {
            "id": "sec_deforestation",
            "title": "2. Phá hủy Môi trường sống & Nạn Phá rừng (Deforestation)",
            "selector": "#sec-deforestation",
            "en": "Section 2 investigates Deforestation: Forests are felled for agricultural land, timber, and roads. Ecological consequences include topsoil erosion when tree roots no longer bind soil particles; severe flooding because rain runs off rapidly without canopy interception; destruction of wildlife habitats driving species extinction; and loss of massive carbon sinks, elevating atmospheric carbon dioxide levels.",
            "vi": "Mục hai nghiên cứu Nạn phá rừng (Deforestation): Rừng bị đốn hạ để lấy đất trồng trọt, khai thác gỗ và mở đường. Hậu quả sinh thái nghiêm trọng gồm xói mòn lớp đất mặt màu mỡ do mất mạng lưới rễ cây giữ đất; gia tăng lũ lụt do nước mưa chảy tràn; phá hủy môi trường sống dẫn đến tuyệt chủng giống loài; và làm mất đi bể hấp thu carbon khổng lồ, khiến lượng CO2 trong khí quyển tăng vọt."
        },
        {
            "id": "sec_eutrophication",
            "title": "3. Ô nhiễm Nguồn nước & Hiện tượng Phú dưỡng (Eutrophication)",
            "selector": "#sec-eutrophication",
            "en": "Section 3 details the five-step Eutrophication sequence: First, excess mineral fertilizers or untreated sewage leach into waterways. Second, algae rapidly proliferate into an algal bloom, blanketing the water surface and blocking sunlight. Third, submerged aquatic plants cannot photosynthesize and die. Fourth, aerobic bacteria multiply exponentially as they decompose dead vegetation, consuming all dissolved oxygen. Fifth, aquatic animals like fish suffocate and die from severe lack of oxygen.",
            "vi": "Mục ba mô tả 5 bước của Hiện tượng Phú dưỡng (Eutrophication): Bước 1: Phân bón hóa học dư thừa chứa nitrat và photphat hoặc nước thải chưa xử lý rửa trôi xuống sông hồ. Bước 2: Tảo sinh sôi nở hoa bùng phát (algal bloom), che phủ kín mặt nước ngăn ánh sáng mặt trời. Bước 3: Các loài thực vật thủy sinh dưới đáy không thể quang hợp và chết dần. Bước 4: Vi khuẩn phân hủy hiếu khí tăng sinh theo cấp số nhân để tiêu thụ xác thực vật, hút cạn toàn bộ oxy hòa tan trong nước. Bước 5: Các loài cá và động vật thủy sinh ngạt thở và chết hàng loạt do thiếu dưỡng khí."
        },
        {
            "id": "sec_conservation",
            "title": "4. Bảo tồn Đa dạng Sinh học (Conservation of Biodiversity)",
            "selector": "#sec-conservation",
            "en": "Section 4 covers Conservation strategies: Sustainable development meets current human needs without compromising the ability of future generations to meet theirs. Conservation programmes preserve biodiversity, prevent species extinction, protect vulnerable habitats in national parks, maintain seed banks for agricultural security, and utilize captive breeding to replenish endangered wildlife populations.",
            "vi": "Mục bốn trình bày các chiến lược Bảo tồn: Phát triển bền vững đáp ứng nhu cầu hiện tại mà không làm tổn hại đến khả năng đáp ứng nhu cầu của các thế hệ tương lai. Các chương trình bảo tồn giúp duy trì đa dạng sinh học, ngăn chặn nguy cơ tuyệt chủng, thành lập các vườn quốc gia bảo vệ sinh cảnh, xây dựng ngân hàng hạt giống và áp dụng kỹ thuật nhân giống bảo tồn để phục hồi các quần thể động vật hoang dã nguy cấp."
        }
    ]

    major_sections = [
        {"id": "sec_agriculture", "title": "1. Nông nghiệp Thâm canh & Độc canh"},
        {"id": "sec_deforestation", "title": "2. Nạn Phá rừng & Mất Bể chứa Carbon"},
        {"id": "sec_eutrophication", "title": "3. Hiện tượng Phú dưỡng (Eutrophication)"},
        {"id": "sec_conservation", "title": "4. Chiến lược Bảo tồn Đa dạng Sinh học"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic B19 successfully built!")


# ==============================================================================
# MAIN BATCH 4 RUNNER (TOPICS B16 -> B19)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 4: TOPICS B16 -> B19")
    print("*******************************************************\n")
    
    await build_b16()
    await asyncio.sleep(2)
    
    await build_b17()
    await asyncio.sleep(2)
    
    await build_b18()
    await asyncio.sleep(2)
    
    await build_b19()
    
    print("\n*******************************************************")
    print("BATCH 4 COMPLETE: TOPICS B16 -> B19 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
