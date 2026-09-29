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
# TOPIC 17: Inheritance
# ==============================================================================
async def build_17():
    lid = '77f1f7b8-f30e-4b0b-89e2-2e2482242791'
    code = '17'
    title = 'Topic 17: Inheritance'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🧬 1. CẤU TRÚC DI TRUYỀN (The Genetic Code)
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-genetic-code" class="lecture-interactive-card" data-lecture-section="sec_genetic_code" style="cursor: pointer; ')
    
    # h2[1]: ➗ 2. CELL DIVISION (Phân bào)
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-cell-division" class="lecture-interactive-card" data-lecture-section="sec_cell_division" style="cursor: pointer; ')
    
    # h2[2]: 🧮 3. MONOHYBRID INHERITANCE (Di truyền đơn gen)
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-monohybrid-inheritance" class="lecture-interactive-card" data-lecture-section="sec_monohybrid_inheritance" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 17 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 17: Cơ chế Di truyền (Inheritance)",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 17: Inheritance. Inheritance is the transmission of genetic information from generation to generation. In this central topic, we explore chromosome and gene structures, contrast mitosis and meiosis, decipher genetic terminology, and master monohybrid Punnett crosses and sex determination.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 17: Cơ chế Di truyền. Di truyền học nghiên cứu sự truyền đạt thông tin di truyền qua các thế hệ. Trong bài học này, chúng ta sẽ khảo sát cấu trúc nhiễm sắc thể và gen, so sánh nguyên phân và giảm phân, làm chủ các thuật ngữ di truyền, bảng lai Punnett và cơ chế xác định giới tính."
        },
        {
            "id": "sec_genetic_code",
            "title": "1. Cấu trúc Di truyền: Nhiễm sắc thể, Gen & Allele",
            "selector": "#sec-genetic-code",
            "en": "Section 1 defines key genetics terms: A Chromosome is a thread-like structure of DNA carrying genetic information in the form of genes. A Gene is a length of DNA coding for a specific protein. An Allele is an alternative form of a gene. A Haploid nucleus contains a single set of unpaired chromosomes (23 in humans). A Diploid nucleus contains two sets of homologous chromosomes (46 in humans).",
            "vi": "Mục một định nghĩa các thuật ngữ di truyền then chốt: Nhiễm sắc thể là cấu trúc dạng sợi cấu tạo từ phân tử DNA mang thông tin di truyền dưới dạng các gen. Gen là một đoạn phân tử DNA mã hóa cho một loại protein xác định. Allele là các trạng thái biểu hiện khác nhau của cùng một gen. Nhân đơn bội (haploid) chứa một bộ nhiễm sắc thể đơn không bắt cặp (ở người n = 23). Nhân lưỡng bội (diploid) chứa hai bộ nhiễm sắc thể tương đồng (ở người 2n = 46)."
        },
        {
            "id": "sec_cell_division",
            "title": "2. Phân bào: Nguyên phân (Mitosis) & Giảm phân (Meiosis)",
            "selector": "#sec-cell-division",
            "en": "Section 2 contrasts cell divisions: Mitosis is nuclear division giving rise to genetically identical cells in which chromosome number is maintained; it is essential for growth, tissue repair, and asexual reproduction. Meiosis is reduction division in which chromosome number is halved from diploid to haploid, producing four genetically distinct gametes for sexual reproduction and driving genetic variation.",
            "vi": "Mục hai so sánh hai hình thức phân bào: Nguyên phân (Mitosis) là quá trình phân chia nhân tạo ra hai tế bào con có bộ nhiễm sắc thể giống hệt nhau và giống tế bào mẹ; đóng vai trò cốt lõi trong tăng trưởng cơ thể, làm lành vết thương và sinh sản vô tính. Giảm phân (Meiosis) là phân bào giảm nhiễm làm giảm một nửa số lượng nhiễm sắc thể từ lưỡng bội thành đơn bội, tạo ra 4 giao tử có kiểu gen khác nhau phục vụ sinh sản hữu tính và tạo biến dị tổ hợp."
        },
        {
            "id": "sec_monohybrid_inheritance",
            "title": "3. Di truyền Đơn gen, Bảng lai Punnett & Giới tính",
            "selector": "#sec-monohybrid-inheritance",
            "en": "Section 3 investigates Monohybrid Inheritance: Genotype is the genetic makeup of an organism in terms of alleles (e.g. homozygous BB or heterozygous Bb). Phenotype is the observable physical features. In a cross between two heterozygous parents, the expected phenotypic ratio is three dominant to one recessive. Sex is determined by sex chromosomes: Human females are XX, males are XY, yielding a constant 50% probability of having a son or daughter.",
            "vi": "Mục ba nghiên cứu Quy luật di truyền đơn gen: Kiểu gen (Genotype) là tổ hợp các allele của sinh vật (như đồng hợp BB, bb hoặc dị hợp Bb). Kiểu hình (Phenotype) là các đặc điểm hình thái quan sát được bên ngoài. Khi cho hai cá thể bố mẹ dị hợp lai với nhau, tỉ lệ phân ly kiểu hình kinh điển ở đời con là 3 trội : 1 lặn. Giới tính ở người do cặp nhiễm sắc thể giới tính quyết định: Nữ giới mang cặp đồng dạng XX, nam giới mang cặp dị dạng XY, xác suất sinh con trai hoặc con gái luôn bằng 50%."
        }
    ]

    major_sections = [
        {"id": "sec_genetic_code", "title": "1. Nhiễm sắc thể, Gen & Allele"},
        {"id": "sec_cell_division", "title": "2. Nguyên phân (Mitosis) vs Giảm phân (Meiosis)"},
        {"id": "sec_monohybrid_inheritance", "title": "3. Bảng lai Punnett & Xác định Giới tính"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 17 successfully built!")


# ==============================================================================
# TOPIC 18: Variation and selection
# ==============================================================================
async def build_18():
    lid = '89750884-8439-4cda-916a-56bf5524741b'
    code = '18'
    title = 'Topic 18: Variation and selection'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    soup = BeautifulSoup(html, 'html.parser')
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = soup.find_all('h2')
    
    # h2[0]: 🧬 1. VARIATION & MUTATION
    t_h2_0 = str(h2s[0])
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-variation-mutation" class="lecture-interactive-card" data-lecture-section="sec_variation_mutation" style="cursor: pointer; ')
    
    # h2[1]: 🌵 2. ADAPTIVE FEATURES
    t_h2_1 = str(h2s[1])
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-adaptive-features" class="lecture-interactive-card" data-lecture-section="sec_adaptive_features" style="cursor: pointer; ')
    
    # h2[2]: 🧬 3. SELECTION
    t_h2_2 = str(h2s[2])
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-natural-selection" class="lecture-interactive-card" data-lecture-section="sec_natural_selection" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic 18 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 18: Biến dị, Thích nghi & Chọn lọc Tự nhiên",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Biology, Topic 18: Variation and selection. Biological diversity powers evolutionary change. In this chapter, we compare continuous and discontinuous variation, examine mutation causes, analyze xerophyte and hydrophyte adaptations, and study the mechanics of natural selection versus artificial selective breeding.",
            "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Bài 18: Biến dị, Thích nghi và Chọn lọc Tự nhiên. Đa dạng sinh học là động lực thúc đẩy tiến hóa. Trong bài học này, chúng ta sẽ phân biệt biến dị liên tục và không liên tục, nguyên nhân gây đột biến, cấu tạo thích nghi của thực vật chịu hạn và thủy sinh, cùng cơ chế chọn lọc tự nhiên và chọn giống nhân tạo."
        },
        {
            "id": "sec_variation_mutation",
            "title": "1. Biến dị Liên tục, Không liên tục & Đột biến (Mutation)",
            "selector": "#sec-variation-mutation",
            "en": "Section 1 classifies biological variation: Continuous variation results in a quantitative spectrum of phenotypes influenced by multiple genes and environmental factors, producing normal bell-curve distributions like human height and mass. Discontinuous variation produces distinct, non-overlapping categories determined purely by genes, like ABO blood groups. A Mutation is a genetic change that forms the ultimate source of all novel alleles, accelerated by ionizing radiation and mutagenic chemicals.",
            "vi": "Mục một phân loại các dạng biến dị: Biến dị liên tục là dải kiểu hình định lượng liên tục chịu sự chi phối của nhiều gen kết hợp với yếu tố môi trường, tạo thành đồ thị phân bố chuẩn hình chuông như chiều cao và cân nặng. Biến dị không liên tục phân chia thành các nhóm kiểu hình định tính rõ rệt hoàn toàn do gen quy định, như nhóm máu ABO. Đột biến (Mutation) là sự biến đổi đột ngột trong cấu trúc vật chất di truyền, là nguồn gốc phát sinh các allele mới, gia tăng khi tiếp xúc với tia phóng xạ ion hóa và hóa chất gây đột biến."
        },
        {
            "id": "sec_adaptive_features",
            "title": "2. Đặc điểm Thích nghi: Thực vật Chịu hạn & Thủy sinh",
            "selector": "#sec-adaptive-features",
            "en": "Section 2 investigates Adaptive Features: inherited functional characteristics that enhance survival and reproduction in specific habitats. Xerophytes thrive in arid deserts with thick waxy cuticles, sunken stomata in pits to trap humid air, rolled leaves, and extensive root systems. Hydrophytes flourish in aquatic habitats with thin cuticles, stomata located on upper leaf surfaces for atmospheric gas access, and extensive internal air spaces (aerenchyma) for buoyancy.",
            "vi": "Mục hai nghiên cứu Đặc điểm thích nghi: là những đặc tính hình thái hoặc sinh lý di truyền giúp sinh vật sống sót và sinh sản tối ưu trong sinh cảnh của chúng. Thực vật chịu hạn (Xerophytes) sống ở sa mạc khô cằn có lớp cutin sáp dày, khí khổng nằm sâu trong các hốc để giữ ẩm, lá cuộn tròn hoặc tiêu biến thành gai và rễ cắm rất sâu. Thực vật thủy sinh (Hydrophytes) sống dưới nước có lớp cutin rất mỏng, khí khổng nằm ở mặt trên của lá để trao đổi khí trực tiếp với khí quyển và mô chứa khí (aerenchyma) xốp giúp cây nổi trên mặt nước."
        },
        {
            "id": "sec_natural_selection",
            "title": "3. Chọn lọc Tự nhiên vs Chọn lọc Nhân tạo",
            "selector": "#sec-natural-selection",
            "en": "Section 3 outlines Natural Selection: Organisms produce more offspring than the environment can support, triggering a struggle for survival. Random mutations generate phenotypic variation. Individuals with advantageous adaptations are more likely to survive, reproduce, and pass their favorable alleles to successive generations, causing adaptation and evolution. In contrast, Artificial Selection involves humans selectively breeding individuals showing desired economic traits over many generations.",
            "vi": "Mục ba phác thảo Chọn lọc Tự nhiên: Sinh vật có xu hướng sinh ra nhiều con non hơn mức môi trường có thể nuôi sống, dẫn đến đấu tranh sinh tồn cạnh tranh nguồn tài nguyên. Các cá thể mang biến dị thích nghi có ưu thế sinh tồn cao hơn, sống sót đến tuổi sinh sản và truyền lại các allele có lợi cho thế hệ sau, dẫn đến sự tiến hóa thích nghi của quần thể. Ngược lại, Chọn giống Nhân tạo (Artificial Selection) do con người chủ động chọn và lai các cá thể mang tính trạng mong muốn qua nhiều thế hệ để phục vụ mục đích kinh tế."
        }
    ]

    major_sections = [
        {"id": "sec_variation_mutation", "title": "1. Biến dị Liên tục, Không liên tục & Đột biến"},
        {"id": "sec_adaptive_features", "title": "2. Thực vật Sa mạc vs Thủy sinh"},
        {"id": "sec_natural_selection", "title": "3. Chọn lọc Tự nhiên vs Chọn giống Nhân tạo"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Biology", title, segments, major_sections, subject='biology')
    update_supabase_page(lid, new_html)
    print("✅ Topic 18 successfully built!")


# ==============================================================================
# MAIN BATCH 5 RUNNER (TOPICS 17 -> 18)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING BIOLOGY BATCH 5: TOPICS 17 -> 18")
    print("*******************************************************\n")
    
    await build_17()
    await asyncio.sleep(2)
    
    await build_18()
    
    print("\n*******************************************************")
    print("BIOLOGY BATCH 5 COMPLETE: TOPICS 17 -> 18 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
