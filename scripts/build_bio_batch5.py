# -*- coding: utf-8 -*-
"""
Batch 5 Builder: Topics 18, 19, 20, 21
- Topic 18: Variation and selection
- Topic 19: Organisms and their environment
- Topic 20: Human influences on ecosystems
- Topic 21: Biotechnology and Genetic Engineering
"""

import os
import sys
import re
import json
import asyncio
from bs4 import BeautifulSoup
from audio_lecture_engine import process_lecture_audio, sb

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC 18: Variation and selection
# ==============================================================================
T18_ID = '89750884-8439-4cda-916a-56bf5524741b'
T18_CODE = '18'
T18_TITLE = 'Topic 18: Variation and selection'

T18_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 18: Biến dị, Thích nghi & Chọn lọc Tự nhiên",
        "selector": "#sec-header",
        "en": "Welcome to Topic 18: Variation and Selection. Biological variation is the differences between individuals of the same species. In this lesson, we distinguish continuous from discontinuous variation, investigate gene mutations and mutagenic agents, analyze adaptive morphological features in desert xerophytes and aquatic hydrophytes, and master the mechanism of natural selection and selective breeding.",
        "vi": "Chào mừng các bạn đến với Bài 18: Biến dị và Chọn lọc. Biến dị sinh học là những sai khác giữa các cá thể trong cùng một loài. Trong bài học này, chúng ta sẽ phân biệt biến dị liên tục và không liên tục, tìm hiểu đột biến gen và các tác nhân gây đột biến, phân tích đặc điểm thích nghi hình thái ở thực vật chịu hạn sa mạc và thực vật thủy sinh, cùng cơ chế chọn lọc tự nhiên và chọn lọc nhân tạo."
    },
    {
        "id": "sec_variation_mutation",
        "title": "1. Biến dị Liên tục, Không liên tục & Đột biến (Mutation)",
        "selector": "#sec-variation-mutation",
        "en": "Section 1: Variation and mutation: Continuous variation results in a range of phenotypes between two extremes, influenced by both multiple genes and environmental factors, such as human height and body mass. Discontinuous variation produces distinct, non-overlapping phenotypic categories caused solely by genes, such as ABO blood groups.",
        "vi": "Mục 1: Biến dị và đột biến: Biến dị liên tục tạo ra một dải kiểu hình liên tục giữa hai cực trị, chịu tác động của nhiều gen và môi trường, như chiều cao và cân nặng ở người. Biến dị không liên tục tạo ra các nhóm kiểu hình phân biệt rõ rệt không chồng lấn do gen quy định hoàn toàn, như các nhóm máu hệ ABO."
    },
    {
        "id": "card_mutation",
        "title": "⚠️ Đột biến Gen & Các Tác nhân Gây Đột biến (Mutagens)",
        "selector": "#card-mutation",
        "en": "Mutation and mutagens: A mutation is a spontaneous genetic change in a gene or chromosome that forms new alleles. Mutation frequency is increased by exposure to ionizing radiation such as ultraviolet rays, X-rays, and gamma rays, as well as mutagenic chemicals like heavy metals and tobacco tar.",
        "vi": "Đột biến gen và tác nhân gây đột biến: Đột biến là sự thay đổi di truyền ngẫu nhiên trong cấu trúc của gen hoặc nhiễm sắc thể tạo ra các alen mới. Tần số đột biến gia tăng mạnh khi tiếp xúc với bức xạ ion hóa như tia cực tím UV, tia X, tia phóng xạ gamma, và các hóa chất gây đột biến như kim loại nặng và hắc ín thuốc lá."
    },
    {
        "id": "card_sources_variation",
        "title": "🧬 4 Nguồn gốc Tạo Biến dị Di truyền",
        "selector": "#card-sources-variation",
        "en": "Sources of genetic variation: Genetic variation in populations arises from four primary sources: mutation producing novel alleles, crossing over between homologous chromosomes during meiosis, independent random assortment of chromosomes into gametes, and random fertilisation between haploid gametes.",
        "vi": "Bốn nguồn gốc tạo biến dị di truyền: Biến dị di truyền trong quần thể xuất phát từ bốn nguồn chính: đột biến sinh ra các alen mới, trao đổi chéo giữa các nhiễm sắc thể tương đồng trong giảm phân, sự phân ly độc lập ngẫu nhiên của các nhiễm sắc thể vào giao tử, và sự thụ tinh ngẫu nhiên giữa các giao tử đơn bội."
    },
    {
        "id": "sec_adaptive_features",
        "title": "2. Đặc điểm Thích nghi: Thực vật Chịu hạn & Thủy sinh",
        "selector": "#sec-adaptive-features",
        "en": "Section 2: Adaptive features are inherited functional, structural, or behavioral characteristics of an organism that increase its fitness and chances of survival and reproduction in its natural environment.",
        "vi": "Mục 2: Đặc điểm thích nghi là các đặc tính di truyền về hình thái, sinh lý hoặc tập tính của sinh vật giúp gia tăng độ thích nghi sinh học và nâng cao cơ hội sống sót, sinh sản trong môi trường tự nhiên của chúng."
    },
    {
        "id": "card_xerophytes",
        "title": "🌵 Thích nghi ở Thực vật Chịu hạn (Xerophytes)",
        "selector": "#card-xerophytes",
        "en": "Xerophyte adaptations: Desert plants conserve water through sunken stomata creating localized humid microclimates, thick waxy cuticles preventing epidermal evaporation, rolled leaves trapping moist air, reduced leaves forming protective spines, succulent fleshy stems storing water, and deep taproots reaching underground water tables.",
        "vi": "Thích nghi ở thực vật chịu hạn (Xerophytes): Cây sa mạc tiết kiệm nước nhờ khí khổng thụt sâu tạo vi khí hậu ẩm, lớp cutin sáp dày ngăn bay hơi biểu bì, lá cuộn tròn giữ không khí ẩm, lá tiêu giảm biến thành gai nhọn, thân mọng nước dự trữ nước, và hệ rễ cọc đâm sâu xuống mạch nước ngầm ngầm dưới lòng đất."
    },
    {
        "id": "card_hydrophytes",
        "title": "🪷 Thích nghi ở Thực vật Thủy sinh (Hydrophytes)",
        "selector": "#card-hydrophytes",
        "en": "Hydrophyte adaptations: Aquatic plants living submerged or floating in water feature extensive aerenchyma air spaces providing buoyancy and internal oxygen diffusion pathways, stomata restricted exclusively to upper leaf surfaces in floating leaves, highly reduced cuticles, and thin vestigial root systems.",
        "vi": "Thích nghi ở thực vật thủy sinh (Hydrophytes): Thực vật sống ngập hoặc nổi trên mặt nước sở hữu các khoang khí xốp aerenchyma tạo sức nổi và dẫn khí oxy bên trong, khí khổng chỉ tập trung ở mặt trên của lá nổi, lớp cutin tiêu giảm mỏng manh, và hệ thống rễ rất nhỏ làm nhiệm vụ neo giữ."
    },
    {
        "id": "sec_natural_selection",
        "title": "3. Chọn lọc Tự nhiên vs Chọn lọc Nhân tạo",
        "selector": "#sec-natural-selection",
        "en": "Section 3: Natural and artificial selection: Natural selection is the process where individuals with favorable phenotypic adaptations are more likely to survive, reproduce, and pass on their advantageous alleles to the next generation, driving evolutionary adaptation.",
        "vi": "Mục 3: Chọn lọc tự nhiên và nhân tạo: Chọn lọc tự nhiên là quá trình các cá thể sở hữu kiểu hình thích nghi thuận lợi có xác suất sống sót, sinh sản cao hơn và truyền lại các alen ưu thế cho thế hệ con cháu, thúc đẩy sự tiến hóa thích nghi của loài."
    },
    {
        "id": "card_natural_selection_steps",
        "title": "🌿 5 Bước Cốt lõi của Chọn lọc Tự nhiên",
        "selector": "#card-natural-selection-steps",
        "en": "The 5 steps of natural selection: First, overproduction of offspring. Second, struggle for existence due to limited resources. Third, phenotypic variation within the population. Fourth, survival of the fittest possessing advantageous alleles. Fifth, differential reproduction passing advantageous alleles to offspring, increasing allele frequency over generations.",
        "vi": "Năm bước cốt lõi của chọn lọc tự nhiên: Thứ nhất, sinh vật sinh sản quá mức tạo ra số lượng con non lớn. Thứ hai, xảy ra đấu tranh sinh tồn do tài nguyên môi trường có hạn. Thứ ba, biến dị di truyền tồn tại sẵn trong quần thể. Thứ tư, các cá thể thích nghi nhất sở hữu alen có lợi sẽ sống sót. Thứ năm, sinh sản phân hóa giúp truyền alen có lợi cho đời sau, làm tăng tần số alen thích nghi qua các thế hệ."
    }
]

T18_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_variation_mutation": {"start": 1, "end": 3},
    "sec-variation-mutation": {"start": 1, "end": 3},
    "sec_adaptive_features": {"start": 4, "end": 6},
    "sec-adaptive-features": {"start": 4, "end": 6},
    "sec_natural_selection": {"start": 7, "end": 8},
    "sec-natural-selection": {"start": 7, "end": 8}
}

def transform_topic18_html():
    with open('scripts/raw_bio_topics/t18_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t18_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 18: Variation &amp; Selection</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Continuous vs Discontinuous, Mutagens, Xerophytes/Hydrophytes &amp; Natural Selection</p>
        </div>
        <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #60a5fa;">
            <span>🎧 Click any card to listen</span>
        </div>
    </div>
</div>'''

    header_p2 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 18: Biến dị &amp; Chọn lọc Tự nhiên</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Biến dị liên tục/không liên tục, Đột biến, Cây sa mạc/thủy sinh &amp; Chọn lọc tự nhiên</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header[^>]*"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'sec-header' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>⚠️ Mutation &amp; Mutagens<', ' id="card-mutation" class="lecture-interactive-card" data-lecture-section="card_mutation">⚠️ Mutation &amp; Mutagens<')
    p1 = p1.replace('>🧬 4 Sources of Genetic Variation<', ' id="card-sources-variation" class="lecture-interactive-card" data-lecture-section="card_sources_variation">🧬 4 Sources of Genetic Variation<')
    p1 = p1.replace('>1. Desert Plants (Xerophytes)<', ' id="card-xerophytes" class="lecture-interactive-card" data-lecture-section="card_xerophytes">1. Desert Plants (Xerophytes)<')
    p1 = p1.replace('>2. Aquatic Plants (Hydrophytes - e.g. Water Lily)<', ' id="card-hydrophytes" class="lecture-interactive-card" data-lecture-section="card_hydrophytes">2. Aquatic Plants (Hydrophytes - e.g. Water Lily)<')
    p1 = p1.replace('>🌿 The 5 Steps of Natural Selection<', ' id="card-natural-selection-steps" class="lecture-interactive-card" data-lecture-section="card_natural_selection_steps">🌿 The 5 Steps of Natural Selection<')

    # P2 replacements
    p2 = p2.replace('id="sec-variation-mutation-vi"', 'id="sec-variation-mutation"')
    p2 = p2.replace('id="sec-adaptive-features-vi"', 'id="sec-adaptive-features"')
    p2 = p2.replace('id="sec-natural-selection-vi"', 'id="sec-natural-selection"')
    p2 = p2.replace('>⚠️ Mutation (Đột biến gen &amp; Tác nhân)<', ' id="card-mutation" class="lecture-interactive-card" data-lecture-section="card_mutation">⚠️ Mutation (Đột biến gen &amp; Tác nhân)<')
    p2 = p2.replace('>🧬 4 Nguồn gốc tạo Biến dị Di truyền<', ' id="card-sources-variation" class="lecture-interactive-card" data-lecture-section="card_sources_variation">🧬 4 Nguồn gốc tạo Biến dị Di truyền<')
    p2 = p2.replace('>1. Thực vật sa mạc (Xerophytes - Thực vật chịu hạn)<', ' id="card-xerophytes" class="lecture-interactive-card" data-lecture-section="card_xerophytes">1. Thực vật sa mạc (Xerophytes - Thực vật chịu hạn)<')
    p2 = p2.replace('>2. Thực vật thủy sinh (Hydrophytes - VD: Hoa súng)<', ' id="card-hydrophytes" class="lecture-interactive-card" data-lecture-section="card_hydrophytes">2. Thực vật thủy sinh (Hydrophytes - VD: Hoa súng)<')
    p2 = p2.replace('>🌿 5 Bước cốt lõi của Chọn lọc Tự nhiên (Natural Selection)<', ' id="card-natural-selection-steps" class="lecture-interactive-card" data-lecture-section="card_natural_selection_steps">🌿 5 Bước cốt lõi của Chọn lọc Tự nhiên (Natural Selection)<')

    d1 = p1.count('<div') - p1.count('</div>')
    if d1 > 0: p1 += '</div>' * d1
    elif d1 < 0:
        for _ in range(-d1):
            idx = p1.rfind('</div>')
            if idx != -1: p1 = p1[:idx] + p1[idx+6:]

    d2 = p2.count('<div') - p2.count('</div>')
    if d2 > 0: p2 += '</div>' * d2
    elif d2 < 0:
        for _ in range(-d2):
            idx = p2.rfind('</div>')
            if idx != -1: p2 = p2[:idx] + p2[idx+6:]

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 18 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 18 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 19: Organisms and their environment
# ==============================================================================
T19_ID = '7b2384dd-b79d-47fe-b36b-7abf36784f06'
T19_CODE = '19'
T19_TITLE = 'Topic 19: Organisms and their environment'

T19_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 19: Sinh vật và Môi trường Sinh thái",
        "selector": "#sec-header",
        "en": "Welcome to Topic 19: Organisms and their Environment. Ecology is the scientific study of interactions among organisms and between organisms and their abiotic physical environment. In this lesson, we define ecological levels, analyze energy transfer efficiency across trophic levels, construct ecological pyramids, trace the carbon cycle and microbial nitrogen cycle, and evaluate factors governing population sigmoid growth curves.",
        "vi": "Chào mừng các bạn đến với Bài 19: Sinh vật và Môi trường Sinh thái. Sinh thái học là ngành khoa học nghiên cứu mối tương tác giữa các sinh vật với nhau và giữa sinh vật với môi trường vật lý vô sinh. Trong bài học này, chúng ta sẽ định nghĩa các cấp độ sinh thái, phân tích hiệu suất truyền năng lượng qua các bậc dinh dưỡng, xây dựng tháp sinh thái, chu trình carbon và chu trình nitơ của vi sinh vật, cùng các giai đoạn tăng trưởng quần thể hình chữ S."
    },
    {
        "id": "sec_ecological_definitions",
        "title": "1. Thuật ngữ Sinh thái: Quần thể, Quần xã & Hệ sinh thái",
        "selector": "#sec-ecological-definitions",
        "en": "Section 1: Ecological definitions: A producer makes its own organic nutrients using sunlight energy through photosynthesis. A consumer obtains its energy by feeding on other organisms. Herbivores feed on plants; carnivores feed on other animals; decomposers obtain energy from dead organic waste.",
        "vi": "Mục 1: Các thuật ngữ sinh thái cốt lõi: Sinh vật sản xuất tự tổng hợp chất hữu cơ bằng năng lượng ánh sáng mặt trời qua quang hợp. Sinh vật tiêu thụ nhận năng lượng bằng cách ăn các sinh vật khác. Động vật ăn cỏ ăn thực vật; động vật ăn thịt ăn động vật khác; sinh vật phân giải lấy năng lượng từ xác và chất thải hữu cơ."
    },
    {
        "id": "card_eco_definitions",
        "title": "🌱 Sinh vật Sản xuất vs 🦊 Tiêu thụ vs 🪱 Phân giải",
        "selector": "#card-eco-definitions",
        "en": "Trophic classifications: Primary consumers are herbivores. Secondary and tertiary consumers are carnivores. Decomposers secrete extracellular digestive enzymes to break down complex dead organic macromolecules into simple inorganic mineral ions returned to the soil.",
        "vi": "Phân loại bậc dinh dưỡng: Sinh vật tiêu thụ bậc một là động vật ăn cỏ. Sinh vật tiêu thụ bậc hai và bậc ba là động vật ăn thịt. Sinh vật phân giải tiết enzyme ngoại bào phân giải các đại phân tử hữu cơ từ xác chết thành các ion khoáng vô cơ đơn giản trả lại cho đất."
    },
    {
        "id": "card_eco_levels",
        "title": "🏕️ Quần thể vs Quần xã vs Hệ sinh thái",
        "selector": "#card-eco-levels",
        "en": "Levels of ecological organization: A population is a group of organisms of one species living in the same area at the same time. A community is all the populations of different species living in an ecosystem. An ecosystem is a unit containing a community of organisms interacting with their abiotic environment.",
        "vi": "Các cấp độ tổ chức sinh thái: Quần thể là tập hợp các cá thể cùng một loài cùng sinh sống trong một sinh cảnh tại một thời điểm. Quần xã là tập hợp tất cả các quần thể thuộc các loài khác nhau cùng chung sống trong một hệ sinh thái. Hệ sinh thái là một hệ thống hoàn chỉnh gồm quần xã sinh vật tương tác mật thiết với môi trường vô sinh."
    },
    {
        "id": "sec_food_chains_energy",
        "title": "2. Chuỗi Thức ăn, Lưới Thức ăn & Dòng Năng lượng (Quy tắc 10%)",
        "selector": "#sec-food-chains-energy",
        "en": "Section 2: Food chains and energy flow: The sun is the principal source of energy input to biological ecosystems. Energy flows unidirectionally through food chains and food webs, being dissipated continually as metabolic heat.",
        "vi": "Mục 2: Chuỗi thức ăn và dòng năng lượng: Mặt trời là nguồn năng lượng sơ cấp khởi nguồn cho mọi hệ sinh thái sinh học. Năng lượng truyền một chiều qua chuỗi và lưới thức ăn, liên tục bị tiêu hao ra môi trường dưới dạng nhiệt trao đổi chất."
    },
    {
        "id": "card_energy_flow_10pct",
        "title": "📉 Quy tắc 10% & Giới hạn Độ dài Chuỗi Thức ăn",
        "selector": "#card-energy-flow-10pct",
        "en": "The 10 percent energy rule: Approximately 90 percent of energy is lost between successive trophic levels through cellular respiration, heat dissipation, incomplete digestion excreted in feces, and uneaten biomass. Consequently, food chains rarely exceed four or five trophic levels.",
        "vi": "Quy tắc 10 phần trăm năng lượng: Khoảng 90 phần trăm năng lượng bị thất thoát giữa các bậc dinh dưỡng kế tiếp qua hô hấp tế bào, tỏa nhiệt, thức ăn không tiêu hóa đào thải qua phân và các bộ phận không bị ăn. Do đó, chuỗi thức ăn hiếm khi vượt quá bốn đến năm bậc dinh dưỡng."
    },
    {
        "id": "sec_nutrient_cycles",
        "title": "3. Chu trình Dinh dưỡng (Cacbon & Nitơ)",
        "selector": "#sec-nutrient-cycles",
        "en": "Section 3: Nutrient cycles: Unlike energy which flows linearly and dissipates, chemical nutrients like carbon and nitrogen cycle continuously between living organisms and the abiotic environment.",
        "vi": "Mục 3: Chu trình dinh dưỡng: Khác với năng lượng chỉ truyền một chiều và tiêu hao, các nguyên tố hóa học như cacbon và nitơ tuần hoàn liên tục không ngừng giữa sinh vật sống và môi trường vô sinh."
    },
    {
        "id": "card_carbon_cycle",
        "title": "♻️ Vòng tuần hoàn Cacbon (The Carbon Cycle)",
        "selector": "#card-carbon-cycle",
        "en": "The carbon cycle: Carbon dioxide is removed from the atmosphere exclusively by photosynthesis in plants and algae. Carbon is returned to the atmosphere by cellular respiration of plants, animals, and decomposers, and by combustion of fossil fuels.",
        "vi": "Chu trình cacbon: Khí CO2 chỉ được loại bỏ khỏi khí quyển duy nhất thông qua quá trình quang hợp của thực vật và tảo. Khí CO2 được trả lại khí quyển thông qua hô hấp tế bào của thực vật, động vật, sinh vật phân giải và qua quá trình đốt cháy nhiên liệu hóa thạch."
    },
    {
        "id": "card_nitrogen_cycle",
        "title": "🧪 Chu trình Nitơ & 4 Nhóm Vi khuẩn Cốt lõi",
        "selector": "#card-nitrogen-cycle",
        "en": "The nitrogen cycle and 4 bacterial roles: Nitrogen gas in air is inert and unusable by plants. Nitrogen-fixing bacteria in soil and root nodules convert nitrogen gas into ammonium ions. Nitrifying bacteria oxidize ammonium into nitrites then nitrates absorbed by plant roots. Decomposing bacteria convert protein urea in waste into ammonium. Denitrifying bacteria in anaerobic waterlogged soil convert nitrates back into atmospheric nitrogen gas.",
        "vi": "Chu trình nitơ và bốn nhóm vi khuẩn cốt lõi: Khí nitơ trong khí quyển trơ và thực vật không thể hấp thụ trực tiếp. Vi khuẩn cố định đạm trong đất và nốt sần rễ cây họ Đậu chuyển khí nitơ thành ion amoni. Vi khuẩn nitrat hóa oxy hóa amoni thành nitrit rồi thành nitrat cho rễ cây hấp thụ. Vi khuẩn phân giải biến protein và urê thành amoni. Vi khuẩn phản nitrat hóa trong đất ngập úng kỵ khí biến nitrat thành khí nitơ trả lại khí quyển."
    },
    {
        "id": "sec_populations",
        "title": "4. Động lực học Quần thể & Đường cong Tăng trưởng Sigmoid",
        "selector": "#sec-populations",
        "en": "Section 4: Population dynamics: Population size is determined by the balance between birth rate, death rate, immigration, and emigration. Populations exhibiting exponential growth eventually face limiting factors forming a sigmoid curve.",
        "vi": "Mục 4: Động lực học quần thể: Kích thước quần thể được quyết định bởi sự cân bằng giữa mức sinh sản, mức tử vong, nhập cư và xuất cư. Quần thể tăng trưởng ban đầu theo cấp số nhân nhưng sau đó chịu sự kìm hãm của các yếu tố giới hạn tạo thành đường cong chữ S (Sigmoid)."
    },
    {
        "id": "card_population_sigmoid",
        "title": "📈 Các Pha của Đường cong Tăng trưởng Chữ S (Sigmoid)",
        "selector": "#card-population-sigmoid",
        "en": "Phases of the sigmoid growth curve: The lag phase is slow initial growth as organisms adapt to conditions. The exponential log phase shows rapid multiplying with birth rate far exceeding death rate. The stationary phase occurs when birth rate equals death rate as carrying capacity is reached due to food shortage or disease. The death phase ensues when toxins accumulate and death rate exceeds birth rate.",
        "vi": "Các pha của đường cong sinh trưởng chữ S: Pha tiềm phát (lag phase) số lượng tăng chậm do sinh vật đang thích nghi. Pha lũy thừa (exponential phase) số lượng bùng nổ do tỷ lệ sinh vượt xa tỷ lệ chết. Pha cân bằng (stationary phase) đạt sức chứa môi trường khi tỷ lệ sinh bằng tỷ lệ chết do thiếu thức ăn hoặc bệnh tật. Pha tử vong (death phase) xảy ra khi độc tố tích tụ khiến tỷ lệ chết vượt tỷ lệ sinh."
    }
]

T19_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_ecological_definitions": {"start": 1, "end": 3},
    "sec-ecological-definitions": {"start": 1, "end": 3},
    "sec_food_chains_energy": {"start": 4, "end": 5},
    "sec-food-chains-energy": {"start": 4, "end": 5},
    "sec_nutrient_cycles": {"start": 6, "end": 8},
    "sec-nutrient-cycles": {"start": 6, "end": 8},
    "sec_carbon_cycle": {"start": 6, "end": 8},
    "sec-carbon-cycle": {"start": 6, "end": 8},
    "sec_populations": {"start": 9, "end": 10},
    "sec-populations": {"start": 9, "end": 10}
}

def transform_topic19_html():
    with open('scripts/raw_bio_topics/t19_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t19_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 19: Organisms &amp; Environment</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Ecology Terms, Energy 10% Rule, Carbon &amp; Nitrogen Cycles &amp; Sigmoid Population Growth</p>
        </div>
        <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #60a5fa;">
            <span>🎧 Click any card to listen</span>
        </div>
    </div>
</div>'''

    header_p2 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 19: Sinh vật &amp; Môi trường Sinh thái</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Khái niệm sinh thái, Quy tắc 10% năng lượng, Chu trình Cacbon/Nitơ &amp; Đường cong Sigmoid</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header[^>]*"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'sec-header' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>Producer &amp; Consumer<', ' id="card-eco-definitions" class="lecture-interactive-card" data-lecture-section="card_eco_definitions">Producer &amp; Consumer<')
    p1 = p1.replace('>Population, Community &amp; Ecosystem<', ' id="card-eco-levels" class="lecture-interactive-card" data-lecture-section="card_eco_levels">Population, Community &amp; Ecosystem<')
    p1 = p1.replace('>📉 The 10% Rule &amp; Why Food Chains Are Short<', ' id="card-energy-flow-10pct" class="lecture-interactive-card" data-lecture-section="card_energy_flow_10pct">📉 The 10% Rule &amp; Why Food Chains Are Short<')
    p1 = p1.replace('>The Carbon Cycle<', ' id="card-carbon-cycle" class="lecture-interactive-card" data-lecture-section="card_carbon_cycle">The Carbon Cycle<')
    p1 = p1.replace('>The Nitrogen Cycle &amp; 4 Bacterial Roles (Supplement)<', ' id="card-nitrogen-cycle" class="lecture-interactive-card" data-lecture-section="card_nitrogen_cycle">The Nitrogen Cycle &amp; 4 Bacterial Roles (Supplement)<')
    p1 = p1.replace('>Factors Affecting Population Growth<', ' id="card-population-sigmoid" class="lecture-interactive-card" data-lecture-section="card_population_sigmoid">Factors Affecting Population Growth<')

    # P2 replacements
    p2 = p2.replace('id="sec-ecological-definitions-vi"', 'id="sec-ecological-definitions"')
    p2 = p2.replace('id="sec-food-chains-energy-vi"', 'id="sec-food-chains-energy"')
    p2 = p2.replace('id="sec-nutrient-cycles-vi"', 'id="sec-nutrient-cycles"')
    p2 = p2.replace('id="sec-populations-vi"', 'id="sec-populations"')
    p2 = p2.replace('>Sinh vật Sản xuất &amp; Tiêu thụ<', ' id="card-eco-definitions" class="lecture-interactive-card" data-lecture-section="card_eco_definitions">Sinh vật Sản xuất &amp; Tiêu thụ<')
    p2 = p2.replace('>Quần thể, Quần xã &amp; Hệ sinh thái<', ' id="card-eco-levels" class="lecture-interactive-card" data-lecture-section="card_eco_levels">Quần thể, Quần xã &amp; Hệ sinh thái<')
    p2 = p2.replace('>📉 Quy tắc 10% &amp; Tại sao Chuỗi thức ăn lại rất ngắn?<', ' id="card-energy-flow-10pct" class="lecture-interactive-card" data-lecture-section="card_energy_flow_10pct">📉 Quy tắc 10% &amp; Tại sao Chuỗi thức ăn lại rất ngắn?<')
    p2 = p2.replace('>Vòng tuần hoàn Cacbon (The Carbon Cycle)<', ' id="card-carbon-cycle" class="lecture-interactive-card" data-lecture-section="card_carbon_cycle">Vòng tuần hoàn Cacbon (The Carbon Cycle)<')
    p2 = p2.replace('>Chu trình Nitrogen &amp; 4 Nhóm Vi khuẩn (Supplement)<', ' id="card-nitrogen-cycle" class="lecture-interactive-card" data-lecture-section="card_nitrogen_cycle">Chu trình Nitrogen &amp; 4 Nhóm Vi khuẩn (Supplement)<')
    p2 = p2.replace('>Các yếu tố điều hòa Kích thước Quần thể<', ' id="card-population-sigmoid" class="lecture-interactive-card" data-lecture-section="card_population_sigmoid">Các yếu tố điều hòa Kích thước Quần thể<')

    d1 = p1.count('<div') - p1.count('</div>')
    if d1 > 0: p1 += '</div>' * d1
    elif d1 < 0:
        for _ in range(-d1):
            idx = p1.rfind('</div>')
            if idx != -1: p1 = p1[:idx] + p1[idx+6:]

    d2 = p2.count('<div') - p2.count('</div>')
    if d2 > 0: p2 += '</div>' * d2
    elif d2 < 0:
        for _ in range(-d2):
            idx = p2.rfind('</div>')
            if idx != -1: p2 = p2[:idx] + p2[idx+6:]

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 19 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 19 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 20: Human influences on ecosystems
# ==============================================================================
T20_ID = '7777b4df-68dd-4600-b4ba-a4ce56ecc6ac'
T20_CODE = '20'
T20_TITLE = 'Topic 20: Human influences on ecosystems'

T20_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 20: Tác động của Con người lên Hệ sinh thái",
        "selector": "#sec-header",
        "en": "Welcome to Topic 20: Human Influences on Ecosystems. Human activities increasingly disrupt ecological balances on a global scale. In this lesson, we evaluate agricultural impacts of monocultures and intensive livestock, mechanisms and consequences of deforestation, aquatic eutrophication cascades, enhanced greenhouse effect, acid rain, and modern conservation strategies for endangered species.",
        "vi": "Chào mừng các bạn đến với Bài 20: Tác động của Con người lên Hệ sinh thái. Hoạt động của loài người đang làm xáo trộn các cân bằng sinh thái trên quy mô toàn cầu. Trong bài học này, chúng ta sẽ đánh giá tác động của độc canh nông nghiệp và chăn nuôi thâm canh, cơ chế và hậu quả của nạn phá rừng, chuỗi phản ứng phú dưỡng nguồn nước, hiệu ứng nhà kính tăng cường, mưa axit và các chiến lược bảo tồn đa dạng sinh học hiện đại."
    },
    {
        "id": "sec_agriculture",
        "title": "1. Nông nghiệp & Cung ứng Lương thực (Monoculture)",
        "selector": "#sec-agriculture",
        "en": "Section 1: Food supply and modern agriculture: Growing human populations demand increased food production through agricultural machinery, chemical fertilizers, synthetic insecticides, herbicides, and selective breeding.",
        "vi": "Mục 1: Cung ứng lương thực và nông nghiệp hiện đại: Dân số gia tăng nhanh đòi hỏi tăng sản lượng lương thực thông qua cơ giới hóa máy móc, phân bón hóa học, thuốc trừ sâu tổng hợp, thuốc diệt cỏ và chọn lọc nhân tạo giống cây trồng vật nuôi."
    },
    {
        "id": "card_monoculture_livestock",
        "title": "🌽 Độc canh Quy mô lớn & Chăn nuôi Thâm canh",
        "selector": "#card-monoculture-livestock",
        "en": "Monocultures and intensive livestock: Monoculture is growing a single crop species over large land areas, causing severe biodiversity loss, rapid pest population surges, and soil nutrient depletion. Intensive livestock farming confines animals in high densities, risking antibiotic resistance transmission, high greenhouse gas emissions, and massive slurry pollution.",
        "vi": "Độc canh và chăn nuôi thâm canh: Độc canh là trồng duy nhất một loài cây trên diện tích lớn, làm suy giảm đa dạng sinh học, bùng phát sâu bệnh và thoái hóa cạn kiệt dinh dưỡng đất. Chăn nuôi thâm canh nuôi nhốt gia súc mật độ cao dẫn đến nguy cơ kháng kháng sinh lây lan, phát thải khí nhà kính và ô nhiễm chất thải phân chuồng nghiêm trọng."
    },
    {
        "id": "sec_deforestation",
        "title": "2. Phá hủy Môi trường sống & Nạn Phá rừng (Deforestation)",
        "selector": "#sec-deforestation",
        "en": "Section 2: Habitat destruction and deforestation: Clearing forests for agriculture, livestock grazing, timber extraction, and urban expansion destroys habitats, driving biodiversity loss and climate instability.",
        "vi": "Mục 2: Phá hủy môi trường sống và nạn phá rừng: Chặt phá rừng lấy đất canh tác, chăn thả gia súc, khai thác gỗ và mở rộng đô thị phá hủy nơi cư trú tự nhiên, làm mất đa dạng sinh học và gây mất ổn định khí hậu."
    },
    {
        "id": "card_deforestation_impacts",
        "title": "🔥 Hậu quả của Phá rừng: Xói mòn, Lũ lụt & CO2",
        "selector": "#card-deforestation-impacts",
        "en": "Deforestation impacts: Tree clearance reduces photosynthesis while combustion of felled timber releases massive carbon dioxide, accelerating global warming. The absence of tree root networks leads to topsoil erosion by heavy rainfall, siltation of riverbeds, and downstream flash flooding.",
        "vi": "Hậu quả của nạn phá rừng: Mất cây xanh làm giảm hấp thụ CO2 qua quang hợp, trong khi đốt gỗ giải phóng lượng lớn CO2 đẩy nhanh biến đổi khí hậu. Mất hệ rễ cây giữ đất khiến đất mặt bị mưa xói mòn rửa trôi, bồi lấp lòng sông gây sạt lở và lũ quét ngập lụt vùng hạ lưu."
    },
    {
        "id": "sec_eutrophication",
        "title": "3. Ô nhiễm Nước & Hiện tượng Phú dưỡng (Eutrophication)",
        "selector": "#sec-eutrophication",
        "en": "Section 3: Pollution and eutrophication: Runoff of synthetic inorganic nitrate and phosphate fertilizers or untreated sewage into aquatic freshwater ecosystems causes deadly eutrophication.",
        "vi": "Mục 3: Ô nhiễm nguồn nước và hiện tượng phú dưỡng: Sự rửa trôi phân bón hóa học chứa nitrat, photphat hoặc nước thải chưa qua xử lý vào các hệ sinh thái nước ngọt gây nên hiện tượng phú dưỡng độc hại."
    },
    {
        "id": "card_eutrophication_stages",
        "title": "☠️ 5 Giai đoạn của Hiện tượng Phú dưỡng",
        "selector": "#card-eutrophication-stages",
        "en": "The 5 stages of eutrophication: First, fertilizer nutrients leach into lakes. Second, algae rapidly multiply forming dense surface algal blooms that block sunlight. Third, submerged plants die from lack of light. Fourth, aerobic decomposing bacteria feed on dead vegetation, reproducing explosively and consuming dissolved oxygen. Fifth, severe hypoxia leads to mass death of fish and aquatic invertebrates.",
        "vi": "Năm giai đoạn của hiện tượng phú dưỡng: Thứ nhất, phân bón giàu nitrat rửa trôi vào hồ. Thứ hai, tảo sinh sôi bùng nổ tạo màng tảo xanh dày đặc che khuất ánh sáng. Thứ ba, thực vật thủy sinh dưới đáy chết do thiếu sáng không quang hợp được. Thứ tư, vi khuẩn hiếu khí phân hủy xác thực vật bùng nổ tiêu thụ cạn kiệt oxy hòa tan. Thứ năm, sự thiếu oxy nghiêm trọng làm cá và các động vật thủy sinh chết hàng loạt ngạt thở."
    },
    {
        "id": "sec_climate_acid_rain",
        "title": "4. Biến đổi Khí hậu & Mưa Axit",
        "selector": "#sec-climate-acid-rain",
        "en": "Section 4: Climate change and acid rain: Burning fossil fuels produces carbon dioxide and methane that trap outgoing thermal infrared radiation, amplifying the greenhouse effect. Sulfur dioxide and nitrogen oxides dissolve in atmospheric moisture forming dilute sulfuric and nitric acids, which leach toxic aluminium ions from soil and lower freshwater pH.",
        "vi": "Mục 4: Biến đổi khí hậu và mưa axit: Đốt nhiên liệu hóa thạch phát thải CO2 và mêtan giữ lại bức xạ nhiệt hồng ngoại làm tăng hiệu ứng nhà kính và biến đổi khí hậu toàn cầu. Khí lưu huỳnh đioxit và oxit nitơ hòa tan vào hơi nước tạo mưa axit sunfuric và nitric, làm chua hóa nguồn nước và rửa trôi ion nhôm độc hại vào sông hồ làm chết cá."
    },
    {
        "id": "card_greenhouse_acid_rain",
        "title": "🌍 Hiệu ứng Nhà kính Tăng cường & Biện pháp Khắc phục",
        "selector": "#card-greenhouse-acid-rain",
        "en": "Mitigating atmospheric pollution: Solutions require transitioning to renewable energy, installing catalytic converters in vehicles, utilizing scrubbers in power stations to desulfurize flue gases, and reforestation to restore natural carbon sinks.",
        "vi": "Biện pháp giảm thiểu ô nhiễm khí quyển: Các giải pháp cấp thiết gồm chuyển đổi sang năng lượng tái tạo, lắp bộ lọc xúc tác cho khí thải xe cộ, sử dụng tháp lọc khí để khử lưu huỳnh tại nhà máy nhiệt điện, và tích cực trồng rừng khôi phục bể hấp thụ carbon tự nhiên."
    },
    {
        "id": "sec_conservation",
        "title": "5. Bảo tồn Đa dạng Sinh học & Quản lý Tài nguyên Bền vững",
        "selector": "#sec-conservation",
        "en": "Section 5: Conservation and sustainable resources: Conservation is the maintenance of biodiversity through the preservation and restoration of natural habitats and sustainable management of natural resources.",
        "vi": "Mục 5: Bảo tồn đa dạng sinh học và tài nguyên bền vững: Bảo tồn là việc duy trì sự đa dạng sinh học thông qua bảo vệ và phục hồi các môi trường sống tự nhiên, đồng thời quản lý khai thác bền vững các nguồn tài nguyên."
    },
    {
        "id": "card_sustainable_resources",
        "title": "🌲 Quản lý Bền vững Tài nguyên Rừng & Thủy sản",
        "selector": "#card-sustainable-resources",
        "en": "Sustainable resource management: Sustainable harvesting meets human needs today without compromising the availability of resources for future generations. Forestry employs quotas, selective felling, and replanting. Fisheries enforce fishing quotas, restricted mesh sizes allowing young fish to escape, and marine protected areas during breeding seasons.",
        "vi": "Quản lý tài nguyên bền vững: Phát triển bền vững đáp ứng nhu cầu hiện tại mà không làm tổn hại đến khả năng đáp ứng nhu cầu của các thế hệ tương lai. Lâm nghiệp áp dụng hạn ngạch khai thác, đốn hạ có chọn lọc và trồng rừng thay thế. Ngư nghiệp áp đặt hạn ngạch đánh bắt, quy định kích thước mắt lưới mắt lớn để cá non thoát được, và lập khu bảo tồn biển trong mùa sinh sản."
    },
    {
        "id": "card_captive_breeding_methods",
        "title": "🐼 Quản lý Loài Nguy cấp & Kỹ thuật Nhân giống Nuôi nhốt",
        "selector": "#card-captive-breeding-methods",
        "en": "Endangered species management and captive breeding: Endangered species are protected in national parks and botanic gardens. Captive breeding programs in zoos maintain genetic diversity using studbooks, in vitro fertilization, and embryo transfer, with ultimate reintroduction into protected wild habitats.",
        "vi": "Quản lý loài nguy cấp và nhân giống nuôi nhốt: Các loài có nguy cơ tuyệt chủng được bảo vệ trong các vườn quốc gia và vườn thực vật. Các chương trình nhân giống nuôi nhốt trong thảo cầm viên duy trì đa dạng di truyền qua sổ theo dõi phả hệ, thụ tinh trong ống nghiệm và chuyển phôi, hướng tới tái thả cá thể trở lại môi trường hoang dã an toàn."
    }
]

T20_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_agriculture": {"start": 1, "end": 2},
    "sec-agriculture": {"start": 1, "end": 2},
    "sec_deforestation": {"start": 3, "end": 4},
    "sec-deforestation": {"start": 3, "end": 4},
    "sec_eutrophication": {"start": 5, "end": 6},
    "sec-eutrophication": {"start": 5, "end": 6},
    "sec_climate_acid_rain": {"start": 7, "end": 8},
    "sec-climate-acid-rain": {"start": 7, "end": 8},
    "sec_conservation": {"start": 9, "end": 11},
    "sec-conservation": {"start": 9, "end": 11}
}

def transform_topic20_html():
    with open('scripts/raw_bio_topics/t20_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t20_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 20: Human Influences on Ecosystems</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Monocultures, Deforestation Impacts, Eutrophication, Climate Change &amp; Conservation</p>
        </div>
        <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #60a5fa;">
            <span>🎧 Click any card to listen</span>
        </div>
    </div>
</div>'''

    header_p2 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 20: Tác động của Con người lên Hệ sinh thái</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Độc canh nông nghiệp, Phá rừng, Hiện tượng Phú dưỡng, Mưa axit &amp; Chiến lược Bảo tồn</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header[^>]*"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'sec-header' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🌽 Large-Scale Monocultures<', ' id="card-monoculture-livestock" class="lecture-interactive-card" data-lecture-section="card_monoculture_livestock">🌽 Large-Scale Monocultures<')
    p1 = p1.replace('>🔥 Increase in Atmospheric $CO_2$<', ' id="card-deforestation-impacts" class="lecture-interactive-card" data-lecture-section="card_deforestation_impacts">🔥 Increase in Atmospheric $CO_2$<')
    p1 = p1.replace('>1. Leaching of Nitrates &amp; Phosphates<', ' id="card-eutrophication-stages" class="lecture-interactive-card" data-lecture-section="card_eutrophication_stages">1. Leaching of Nitrates &amp; Phosphates<')
    p1 = p1.replace('>Enhanced Greenhouse Effect<', ' id="card-greenhouse-acid-rain" class="lecture-interactive-card" data-lecture-section="card_greenhouse_acid_rain">Enhanced Greenhouse Effect<')
    p1 = p1.replace('>Sustainable Resource Management<', ' id="card-sustainable-resources" class="lecture-interactive-card" data-lecture-section="card_sustainable_resources">Sustainable Resource Management<')
    p1 = p1.replace('>Endangered Species Management &amp; Captive Breeding<', ' id="card-captive-breeding-methods" class="lecture-interactive-card" data-lecture-section="card_captive_breeding_methods">Endangered Species Management &amp; Captive Breeding<')

    # P2 replacements
    p2 = p2.replace('id="sec-agriculture-vi"', 'id="sec-agriculture"')
    p2 = p2.replace('id="sec-deforestation-vi"', 'id="sec-deforestation"')
    p2 = p2.replace('id="sec-eutrophication-vi"', 'id="sec-eutrophication"')
    p2 = p2.replace('id="sec-climate-acid-rain-vi"', 'id="sec-climate-acid-rain"')
    p2 = p2.replace('id="sec-conservation-vi"', 'id="sec-conservation"')
    p2 = p2.replace('>🌽 Độc canh quy mô lớn (Monocultures)<', ' id="card-monoculture-livestock" class="lecture-interactive-card" data-lecture-section="card_monoculture_livestock">🌽 Độc canh quy mô lớn (Monocultures)<')
    p2 = p2.replace('>🔥 Gia tăng khí CO₂ trong Khí quyển<', ' id="card-deforestation-impacts" class="lecture-interactive-card" data-lecture-section="card_deforestation_impacts">🔥 Gia tăng khí CO₂ trong Khí quyển<')
    p2 = p2.replace('>1. Leaching (Rửa trôi phân bón)<', ' id="card-eutrophication-stages" class="lecture-interactive-card" data-lecture-section="card_eutrophication_stages">1. Leaching (Rửa trôi phân bón)<')
    p2 = p2.replace('>Hiệu ứng Nhà kính Nhân tạo (Enhanced Greenhouse Effect)<', ' id="card-greenhouse-acid-rain" class="lecture-interactive-card" data-lecture-section="card_greenhouse_acid_rain">Hiệu ứng Nhà kính Nhân tạo (Enhanced Greenhouse Effect)<')
    p2 = p2.replace('>Quản lý Tài nguyên Bền vững (Sustainable Resources)<', ' id="card-sustainable-resources" class="lecture-interactive-card" data-lecture-section="card_sustainable_resources">Quản lý Tài nguyên Bền vững (Sustainable Resources)<')
    p2 = p2.replace('>Nhân giống nuôi nhốt &amp; Nguy cơ từ Quần thể Quá nhỏ<', ' id="card-captive-breeding-methods" class="lecture-interactive-card" data-lecture-section="card_captive_breeding_methods">Nhân giống nuôi nhốt &amp; Nguy cơ từ Quần thể Quá nhỏ<')

    d1 = p1.count('<div') - p1.count('</div>')
    if d1 > 0: p1 += '</div>' * d1
    elif d1 < 0:
        for _ in range(-d1):
            idx = p1.rfind('</div>')
            if idx != -1: p1 = p1[:idx] + p1[idx+6:]

    d2 = p2.count('<div') - p2.count('</div>')
    if d2 > 0: p2 += '</div>' * d2
    elif d2 < 0:
        for _ in range(-d2):
            idx = p2.rfind('</div>')
            if idx != -1: p2 = p2[:idx] + p2[idx+6:]

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 20 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 20 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 21: Biotechnology and Genetic Engineering
# ==============================================================================
T21_ID = '55023dc0-7fdc-46ea-a3e9-9a049306d086'
T21_CODE = '21'
T21_TITLE = 'Topic 21: Biotechnology and Genetic Engineering'

T21_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 21: Công nghệ Sinh học & Kỹ thuật Di truyền",
        "selector": "#sec-header",
        "en": "Welcome to Topic 21: Biotechnology and Genetic Engineering. Biotechnology is the application of biological organisms, systems, or processes to manufacturing and service industries. In this lesson, we study bacterial and yeast physiology, commercial enzyme applications including pectinase and lactase, industrial fermenter engineering, and recombinant DNA technology producing human insulin and genetically modified crops.",
        "vi": "Chào mừng các bạn đến với Bài 21: Công nghệ Sinh học và Kỹ thuật Di truyền. Công nghệ sinh học là ứng dụng các sinh vật, hệ thống sinh học vào công nghiệp sản xuất và dịch vụ đời sống. Trong bài học này, chúng ta sẽ học về vi khuẩn và nấm men, ứng dụng enzyme công nghiệp như pectinase và lactase, thiết kế bồn lên men công nghiệp, cùng kỹ thuật tái tổ hợp ADN sản xuất insulin người và cây trồng chuyển gen."
    },
    {
        "id": "sec_why_bacteria",
        "title": "1. Ứng dụng Vi sinh vật trong Công nghệ Sinh học",
        "selector": "#sec-why-bacteria",
        "en": "Section 1: Microorganisms in biotechnology: Bacteria and fungi are ideal for industrial use because they reproduce extremely rapidly, possess simple nutritional requirements, synthesize complex organic molecules, share the universal genetic code, and raise fewer ethical concerns than using animals.",
        "vi": "Mục 1: Vi sinh vật trong công nghệ sinh học: Vi khuẩn và nấm rất lý tưởng trong công nghiệp vì tốc độ sinh sản cực nhanh, nhu cầu dinh dưỡng đơn giản, khả năng tổng hợp các phân tử hữu cơ phức tạp, dùng chung mã di truyền phổ quát và ít vấp phải vấn đề đạo đức so với sử dụng động vật."
    },
    {
        "id": "card_bacteria_yeast_role",
        "title": "🧫 Ưu thế của Vi khuẩn & Lên men Rượu ở Nấm men",
        "selector": "#card-bacteria-yeast-role",
        "en": "Yeast anaerobic respiration: Yeast respires anaerobically via alcohol fermentation, converting glucose into ethanol and carbon dioxide. Carbon dioxide bubbles trapped in dough cause bread to rise, while ethanol is used in brewing beer and making wine.",
        "vi": "Hô hấp kỵ khí ở nấm men: Nấm men hô hấp kỵ khí qua lên men rượu, chuyển hóa glucose thành rượu ethanol và khí CO2. Khí CO2 tạo bọt khí nở xốp bột làm bánh mì phồng xốp, còn ethanol được ứng dụng trong sản xuất bia và rượu vang."
    },
    {
        "id": "sec_biotech_enzymes",
        "title": "2. Ứng dụng Enzyme trong Công nghệ Sinh học",
        "selector": "#sec-biotech-enzymes",
        "en": "Section 2: Enzymes in biotechnology: Enzymes act as biological catalysts functioning at mild temperatures and pressures, lowering industrial operational energy costs.",
        "vi": "Mục 2: Enzyme trong công nghệ sinh học: Enzyme là chất xúc tác sinh học hoạt động hiệu quả ở nhiệt độ và áp suất ôn hòa, giúp tiết kiệm đáng kể chi phí năng lượng trong vận hành công nghiệp."
    },
    {
        "id": "card_biotech_enzymes",
        "title": "🧪 Enzyme Pectinase, Bột giặt Sinh học & Sữa Lactose-Free",
        "selector": "#card-biotech-enzymes",
        "en": "Commercial enzyme applications: Pectinase breaks down plant cell wall pectin, increasing juice yield and clarity. Biological washing powders contain proteases and lipases that digest blood and grease stains at low temperatures. Lactase breaks milk sugar lactose into glucose and galactose, producing lactose-free milk for lactose-intolerant people.",
        "vi": "Các ứng dụng enzyme thương mại: Pectinase phân giải pectin ở thành tế bào thực vật giúp tăng sản lượng nước ép và làm trong nước trái cây. Bột giặt sinh học chứa protease và lipase phân giải vết bẩn protein máu và dầu mỡ ở nhiệt độ giặt thấp. Lactase phân giải đường lactose thành glucose và galactose, sản xuất sữa không chứa lactose cho người không dung nạp đường sữa."
    },
    {
        "id": "sec_industrial_fermenter",
        "title": "3. Nồi lên men Công nghiệp (The Industrial Fermenter)",
        "selector": "#sec-industrial-fermenter",
        "en": "Section 3: The industrial fermenter: A fermenter is a large stainless-steel vessel providing optimal aseptic conditions for mass microorganism culture producing antibiotics, enzymes, or recombinant proteins.",
        "vi": "Mục 3: Bồn lên men công nghiệp: Bồn lên men là một thiết bị inox lớn cung cấp môi trường vô trùng và các điều kiện tối ưu để nuôi cấy vi sinh vật số lượng lớn nhằm thu hoạch kháng sinh, enzyme hoặc protein tái tổ hợp."
    },
    {
        "id": "card_fermenter_engineering",
        "title": "🏭 Thiết kế Bồn Lên men & Tiệt trùng Hơi nước Nóng",
        "selector": "#card-fermenter-engineering",
        "en": "Fermenter components and sterile conditions: Cooling water jackets remove metabolic heat, preventing enzyme denaturation. Stirring impellers ensure uniform nutrient and oxygen distribution. Sterile air inlets supply oxygen for aerobic respiration. Probes monitor temperature and pH, adjusted with automated acid or alkali additions. Fermenters are steam-sterilized before inoculation to eliminate contaminating microorganisms that would compete for nutrients or destroy the yield.",
        "vi": "Cấu tạo bồn lên men và khử trùng vô trùng: Áo làm mát dẫn nước giải nhiệt trao đổi chất, ngăn ngừa biến tính enzyme. Cánh khuấy đảo trộn liên tục đảm bảo dưỡng chất và oxy phân tán đồng đều. Luồng khí vô trùng cung cấp oxy cho hô hấp hiếu khí. Các đầu dò theo dõi nhiệt độ và độ pH, tự động bơm thêm axit hoặc kiềm điều chỉnh. Bồn lên men phải được tiệt trùng bằng hơi nước nóng trước khi cấy giống để tiêu diệt mọi vi sinh vật tạp nhiễm cạnh tranh thức ăn hoặc làm hỏng mẻ nuôi."
    },
    {
        "id": "sec_genetic_engineering",
        "title": "4. Kỹ thuật Di truyền & Sản xuất Insulin Người",
        "selector": "#sec-genetic-engineering",
        "en": "Section 4: Genetic engineering: Genetic engineering is the artificial modification of an organism's genome by transferring a specific gene from another organism.",
        "vi": "Mục 4: Kỹ thuật di truyền: Kỹ thuật di truyền là sự can thiệp biến đổi nhân tạo hệ gen của sinh vật bằng cách chuyển một gen mong muốn từ sinh vật này sang sinh vật khác."
    },
    {
        "id": "card_insulin_production",
        "title": "🧬 5 Bước Sản xuất Insulin Người bằng ADN Tái tổ hợp",
        "selector": "#card-insulin-production",
        "en": "5 steps of human insulin production: First, human insulin gene is isolated and cut using a restriction enzyme. Second, bacterial plasmid DNA is cut with the same restriction enzyme, creating complementary sticky ends. Third, DNA ligase joins the human gene with plasmid forming recombinant DNA. Fourth, recombinant plasmid is inserted into host bacterium. Fifth, transgenic bacteria multiply in fermenters, expressing and secreting identical human insulin.",
        "vi": "Năm bước sản xuất insulin người: Thứ nhất, phân lập gen mã hóa insulin người và cắt bằng enzyme giới hạn restriction enzyme. Thứ hai, cắt plasmid của vi khuẩn bằng chính enzyme giới hạn đó để tạo các đầu dính bổ sung. Thứ ba, dùng enzyme nối DNA ligase gắn gen người vào plasmid tạo ADN tái tổ hợp. Thứ tư, chuyển plasmid tái tổ hợp vào vi khuẩn chủ. Thứ năm, vi khuẩn chuyển gen nhân lên trong bồn lên men, biểu hiện và tiết ra insulin người tinh khiết."
    },
    {
        "id": "card_gm_crops_pros_cons",
        "title": "🌾 Cây trồng Chuyển Gen (GM Crops): Lợi ích & Quan ngại",
        "selector": "#card-gm-crops-pros-cons",
        "en": "GM crops benefits and concerns: Genetically modified crops can carry genes for herbicide resistance allowing selective weed control, insect resistance reducing pesticide use, and biofortification like Golden Rice producing Vitamin A. Concerns include potential gene transfer to wild weeds creating superweeds, disruption of food chains, pest resistance evolution, and socioeconomic dependence on multinational seed corporations.",
        "vi": "Lợi ích và mối lo ngại về cây trồng chuyển gen (GM crops): Cây trồng GM có thể mang gen kháng thuốc diệt cỏ giúp làm cỏ chọn lọc, gen kháng sâu bệnh giúp giảm thuốc trừ sâu hóa học, và tăng giá trị dinh dưỡng như Gạo Vàng tổng hợp Vitamin A. Mối lo ngại gồm nguy cơ phát tán gen sang cỏ dại tạo cỏ siêu kháng thuốc, xáo trộn chuỗi thức ăn tự nhiên, sâu hại tiến hóa kháng độc tố và sự phụ thuộc kinh tế vào các tập đoàn hạt giống."
    }
]

T21_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_why_bacteria": {"start": 1, "end": 2},
    "sec-why-bacteria": {"start": 1, "end": 2},
    "sec_biotech_enzymes": {"start": 3, "end": 4},
    "sec-biotech-enzymes": {"start": 3, "end": 4},
    "sec_industrial_fermenter": {"start": 5, "end": 6},
    "sec-industrial-fermenter": {"start": 5, "end": 6},
    "sec_genetic_engineering": {"start": 7, "end": 9},
    "sec-genetic-engineering": {"start": 7, "end": 9}
}

def transform_topic21_html():
    with open('scripts/raw_bio_topics/t21_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t21_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 21: Biotechnology &amp; Genetic Engineering</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Bacteria/Yeast, Enzymes (Pectinase/Lactase), Industrial Fermenter &amp; Insulin Recombinant DNA</p>
        </div>
        <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #60a5fa;">
            <span>🎧 Click any card to listen</span>
        </div>
    </div>
</div>'''

    header_p2 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 21: Công nghệ Sinh học &amp; Kỹ thuật Di truyền</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Vi khuẩn/Nấm men, Enzyme sinh học, Bồn lên men công nghiệp &amp; Tái tổ hợp ADN sản xuất Insulin</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header[^>]*"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'sec-header' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>Why Bacteria Are Ideal for Biotechnology<', ' id="card-bacteria-yeast-role" class="lecture-interactive-card" data-lecture-section="card_bacteria_yeast_role">Why Bacteria Are Ideal for Biotechnology<')
    p1 = p1.replace('>Pectinase in Fruit Juice Production<', ' id="card-biotech-enzymes" class="lecture-interactive-card" data-lecture-section="card_biotech_enzymes">Pectinase in Fruit Juice Production<')
    p1 = p1.replace('>❄️ Water Jacket (Temperature Control)<', ' id="card-fermenter-engineering" class="lecture-interactive-card" data-lecture-section="card_fermenter_engineering">❄️ Water Jacket (Temperature Control)<')
    p1 = p1.replace('>5 Steps of Bacterial Production of Human Insulin (Supplement)<', ' id="card-insulin-production" class="lecture-interactive-card" data-lecture-section="card_insulin_production">5 Steps of Bacterial Production of Human Insulin (Supplement)<')
    p1 = p1.replace('>Advantages of GM Crops<', ' id="card-gm-crops-pros-cons" class="lecture-interactive-card" data-lecture-section="card_gm_crops_pros_cons">Advantages of GM Crops<')

    # P2 replacements
    p2 = p2.replace('id="sec-why-bacteria-vi"', 'id="sec-why-bacteria"')
    p2 = p2.replace('id="sec-biotech-enzymes-vi"', 'id="sec-biotech-enzymes"')
    p2 = p2.replace('id="sec-industrial-fermenter-vi"', 'id="sec-industrial-fermenter"')
    p2 = p2.replace('id="sec-genetic-engineering-vi"', 'id="sec-genetic-engineering"')
    p2 = p2.replace('>5 Ưu thế Vàng của Vi khuẩn (Bacteria)<', ' id="card-bacteria-yeast-role" class="lecture-interactive-card" data-lecture-section="card_bacteria_yeast_role">5 Ưu thế Vàng của Vi khuẩn (Bacteria)<')
    p2 = p2.replace('>Enzyme Pectinase ép nước trái cây<', ' id="card-biotech-enzymes" class="lecture-interactive-card" data-lecture-section="card_biotech_enzymes">Enzyme Pectinase ép nước trái cây<')
    p2 = p2.replace('>❄️ Water Jacket (Vỏ làm mát điều nhiệt)<', ' id="card-fermenter-engineering" class="lecture-interactive-card" data-lecture-section="card_fermenter_engineering">❄️ Water Jacket (Vỏ làm mát điều nhiệt)<')
    p2 = p2.replace('>5 Bước Chuyển Gen Sản Xuất Insulin Người ở Vi Khuẩn (Supplement)<', ' id="card-insulin-production" class="lecture-interactive-card" data-lecture-section="card_insulin_production">5 Bước Chuyển Gen Sản Xuất Insulin Người ở Vi Khuẩn (Supplement)<')
    p2 = p2.replace('>Ưu điểm của Cây trồng GM (GM Crops)<', ' id="card-gm-crops-pros-cons" class="lecture-interactive-card" data-lecture-section="card_gm_crops_pros_cons">Ưu điểm của Cây trồng GM (GM Crops)<')

    d1 = p1.count('<div') - p1.count('</div>')
    if d1 > 0: p1 += '</div>' * d1
    elif d1 < 0:
        for _ in range(-d1):
            idx = p1.rfind('</div>')
            if idx != -1: p1 = p1[:idx] + p1[idx+6:]

    d2 = p2.count('<div') - p2.count('</div>')
    if d2 > 0: p2 += '</div>' * d2
    elif d2 < 0:
        for _ in range(-d2):
            idx = p2.rfind('</div>')
            if idx != -1: p2 = p2[:idx] + p2[idx+6:]

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 21 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 21 P2 div diff != 0"

    return p1, p2

async def build_batch5():
    tasks = [
        ("Topic 18", T18_CODE, T18_ID, T18_TITLE, T18_SEGMENTS, T18_MAJOR_SECTIONS, transform_topic18_html),
        ("Topic 19", T19_CODE, T19_ID, T19_TITLE, T19_SEGMENTS, T19_MAJOR_SECTIONS, transform_topic19_html),
        ("Topic 20", T20_CODE, T20_ID, T20_TITLE, T20_SEGMENTS, T20_MAJOR_SECTIONS, transform_topic20_html),
        ("Topic 21", T21_CODE, T21_ID, T21_TITLE, T21_SEGMENTS, T21_MAJOR_SECTIONS, transform_topic21_html)
    ]
    
    for name, code, lid, title, segs, major, trans_fn in tasks:
        print(f"\n==========================================")
        print(f"STARTING {name}: {title}")
        print(f"==========================================")
        p1_html, p2_html = trans_fn()
        
        soup1 = BeautifulSoup(p1_html, 'html.parser')
        soup2 = BeautifulSoup(p2_html, 'html.parser')
        for s in segs:
            sel = s['selector']
            if not soup1.select(sel):
                raise ValueError(f"Missing selector '{sel}' in P1 for {name}")
            if not soup2.select(sel):
                raise ValueError(f"Missing selector '{sel}' in P2 for {name}")
        print(f"✅ Pre-flight check: All {len(segs)} selectors verified in P1 and P2 for {name}!")

        manifest = await process_lecture_audio(
            lecture_code=code,
            lecture_id=lid,
            course_title='Cambridge IGCSE Biology (0610)',
            lecture_title=title,
            segments=segs,
            major_sections=major,
            subject='biology'
        )

        print(f"Updating Supabase pages for {name}...")
        sb.table('lecture_pages').update({'content_html': p1_html}).eq('lecture_id', lid).eq('page_number', 1).execute()
        sb.table('lecture_pages').update({'content_html': p2_html}).eq('lecture_id', lid).eq('page_number', 2).execute()
        print(f"✅ {name} Supabase updated and manifest written successfully!")

if __name__ == '__main__':
    asyncio.run(build_batch5())
