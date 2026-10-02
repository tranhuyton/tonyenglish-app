import os
import sys
import asyncio
import json

sys.path.insert(0, os.path.dirname(__file__))
from audio_lecture_engine import process_lecture_audio

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

COURSE_TITLE = "Cambridge IGCSE Co-ordinated Sciences"

# =====================================================================
# B15: REPRODUCTION
# =====================================================================
B15_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B15: Sinh sản ở Sinh vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic B15: Reproduction. Reproduction is the fundamental life process ensuring species continuation. In this topic, we study asexual versus sexual reproduction, flowering plant anatomy, human reproductive systems, the menstrual cycle, and sexually transmitted infections.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B15: Sinh sản ở Sinh vật. Sinh sản là đặc tính sống cốt lõi đảm bảo sự duy trì nòi giống. Trong chuyên đề này, chúng ta sẽ học về sinh sản vô tính và hữu tính, cấu tạo hoa, hệ sinh dục người, chu kỳ kinh nguyệt và các bệnh lây truyền qua đường tình dục."
    },
    {
        "id": "sec_reproduction_modes",
        "title": "1. Sinh sản Vô tính & Hữu tính (Reproduction Modes Overview)",
        "selector": "#sec-reproduction-modes",
        "en": "Section 1 contrasts asexual and sexual reproduction: Asexual reproduction produces genetically identical clones from one parent via mitosis. Sexual reproduction involves the fusion of haploid gamete nuclei to produce genetically varied offspring.",
        "vi": "Mục một so sánh sinh sản vô tính và hữu tính: Sinh sản vô tính tạo ra các cá thể con giống hệt nhau về di truyền từ một cá thể mẹ qua nguyên phân. Sinh sản hữu tính là sự kết hợp giữa hai nhân giao tử đơn bội để tạo ra thế hệ con mang biến dị di truyền."
    },
    {
        "id": "sec_asexual_repro",
        "title": "🌱 Asexual Reproduction (Sinh sản Vô tính)",
        "selector": "#sec-asexual-repro",
        "en": "Asexual reproduction: Requires only one parent. All offspring are clones. Advantage: Extremely rapid population growth to colonize favourable habitats without needing to find a mate. Disadvantage: Zero genetic diversity; all individuals are equally susceptible to disease or environmental changes.",
        "vi": "Sinh sản vô tính: Chỉ cần một cá thể bố mẹ. Toàn bộ con non là dòng vô tính. Ưu điểm: Tăng nhanh số lượng cá thể để chiếm lĩnh môi trường sống thuận lợi mà không cần tìm bạn tình. Nhược điểm: Không có sự đa dạng di truyền; mọi cá thể đều dễ bị tiêu diệt cùng lúc khi gặp dịch bệnh hoặc môi trường biến đổi."
    },
    {
        "id": "sec_sexual_repro",
        "title": "👶 Sexual Reproduction (Sinh sản Hữu tính)",
        "selector": "#sec-sexual-repro",
        "en": "Sexual reproduction: Involves two parents and the fusion of haploid gamete nuclei (sperm/pollen and egg) to form a diploid zygote. Advantage: High genetic variation among offspring, providing adaptability to changing environments and diseases. Disadvantage: Requires finding a mate and expends substantial energy.",
        "vi": "Sinh sản hữu tính: Cần hai cá thể bố mẹ và sự kết hợp giữa các nhân giao tử đơn bội (tinh trùng/hạt phấn và trứng) tạo thành hợp tử lưỡng bội. Ưu điểm: Tạo ra sự đa dạng di truyền cao, giúp loài thích nghi với sự thay đổi của môi trường và dịch bệnh. Nhược điểm: Phải tìm bạn đời và tiêu tốn nhiều thời gian, năng lượng."
    },
    {
        "id": "sec_flowering_plants",
        "title": "2. Sinh sản ở Cây có Hoa (Flowering Plants Overview)",
        "selector": "#sec-flowering-plants",
        "en": "Section 2 investigates flower anatomy: Sepals protect unopened flower buds; colorful petals attract insect pollinators; male stamens consist of anthers producing pollen and filaments; female carpels consist of stigmas, styles, and ovaries containing ovules.",
        "vi": "Mục hai khảo sát cấu tạo của hoa: Đài hoa bảo vệ nụ hoa; cánh hoa sặc sỡ thu hút côn trùng thụ phấn; nhị đực gồm bao phấn sản xuất hạt phấn và chỉ nhị; nhụy cái gồm đầu nhụy, vòi nhụy và bầu nhụy chứa noãn."
    },
    {
        "id": "sec_pollination_modes",
        "title": "🐝 Insect vs Wind Pollination (Thụ phấn nhờ Côn trùng & Gió)",
        "selector": "#sec-pollination-modes",
        "en": "Pollination adaptations: Insect-pollinated flowers have large colourful petals, sweet scent, nectar, and sticky spiky pollen. Wind-pollinated flowers have small dull green petals, no nectar, feathery stigmas hanging outside the flower, and produce huge quantities of light smooth pollen.",
        "vi": "Thích nghi thụ phấn: Hoa thụ phấn nhờ côn trùng có cánh hoa lớn sặc sỡ, hương thơm ngọt, mật hoa và hạt phấn có gai dính. Hoa thụ phấn nhờ gió có cánh hoa nhỏ màu xanh lục nhạt, không có mật, đầu nhụy hình lông chim thò ra ngoài và tạo ra lượng lớn hạt phấn nhẹ, nhẵn."
    },
    {
        "id": "sec_human_reproduction",
        "title": "3. Sinh sản ở Người & Chu kỳ Kinh nguyệt (Human Reproduction Overview)",
        "selector": "#sec-human-reproduction",
        "en": "Section 3 investigates human reproduction: Male testes produce sperm; female ovaries produce ova. Fertilization takes place in the oviduct. The menstrual cycle is controlled by pituitary and ovarian hormones.",
        "vi": "Mục ba nghiên cứu sinh sản ở người: Tinh hoàn nam sản sinh tinh trùng; buồng trứng nữ sản sinh trứng. Sự thụ tinh diễn ra ở ống dẫn trứng. Chu kỳ kinh nguyệt được điều hòa nhịp nhàng bởi các hormone tuyến yên và buồng trứng."
    },
    {
        "id": "sec_menstrual_cycle",
        "title": "📅 The Menstrual Cycle (Chu kỳ Kinh nguyệt 28 Ngày)",
        "selector": "#sec-menstrual-cycle",
        "en": "The menstrual cycle lasts approximately 28 days: Days 1 to 5: Menstruation occurs as the uterus lining breaks down and sheds. Days 6 to 13: Oestrogen causes the uterus lining to thicken and repair. Day 14: Ovulation occurs as an egg is released from an ovary follicle into the oviduct. Days 15 to 28: Progesterone maintains the thick spongy uterus lining ready for embryo implantation.",
        "vi": "Chu kỳ kinh nguyệt kéo dài khoảng 28 ngày: Ngày 1 đến 5: Hành kinh do niêm mạc tử cung thoái hóa và bong tróc. Ngày 6 đến 13: Oestrogen kích thích niêm mạc tử cung dày lên và tái tạo. Ngày 14: Rụng trứng từ nang buồng trứng vào ống dẫn trứng. Ngày 15 đến 28: Progesterone duy trì niêm mạc tử cung dày xốp sẵn sàng đón phôi làm tổ."
    },
    {
        "id": "sec_stis_hiv",
        "title": "4. Bệnh Lây qua Đường Tình dục & HIV (STIs & HIV Overview)",
        "selector": "#sec-stis-hiv",
        "en": "Section 4 covers sexually transmitted infections: An STI is an infection that is transmitted through body fluids during sexual contact. Human Immunodeficiency Virus (HIV) destroys white blood cells called lymphocytes, severely reducing antibody production and leading to Acquired Immune Deficiency Syndrome (AIDS).",
        "vi": "Mục bốn phân tích các bệnh lây qua đường tình dục (STI): Là các bệnh truyền nhiễm lây lan qua dịch cơ thể khi quan hệ tình dục. Virus HIV tấn công và phá hủy các tế bào bạch cầu lympho, làm suy giảm nghiêm trọng khả năng tiết kháng thể và dẫn đến Hội chứng suy giảm miễn dịch mắc phải (AIDS)."
    }
]

B15_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_reproduction_modes": {"start": 1, "end": 3},
    "sec-reproduction-modes": {"start": 1, "end": 3},
    "sec_asexual_repro": {"start": 2, "end": 2},
    "sec-asexual-repro": {"start": 2, "end": 2},
    "sec_sexual_repro": {"start": 3, "end": 3},
    "sec-sexual-repro": {"start": 3, "end": 3},
    "sec_flowering_plants": {"start": 4, "end": 5},
    "sec-flowering-plants": {"start": 4, "end": 5},
    "sec_pollination_modes": {"start": 5, "end": 5},
    "sec-pollination-modes": {"start": 5, "end": 5},
    "sec_human_reproduction": {"start": 6, "end": 7},
    "sec-human-reproduction": {"start": 6, "end": 7},
    "sec_menstrual_cycle": {"start": 7, "end": 7},
    "sec-menstrual-cycle": {"start": 7, "end": 7},
    "sec_stis_hiv": {"start": 8, "end": 8},
    "sec-stis-hiv": {"start": 8, "end": 8}
}

# =====================================================================
# B16: INHERITANCE
# =====================================================================
B16_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B16: Di truyền học",
        "selector": "#sec-header",
        "en": "Welcome to Topic B16: Inheritance. Inheritance is the transmission of genetic information from generation to generation. In this topic, we study chromosomes, genes, monohybrid crosses using Punnett squares, and sex determination.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B16: Di truyền học. Di truyền là sự truyền đạt thông tin di truyền từ thế hệ này sang thế hệ khác. Trong chuyên đề này, chúng ta sẽ học về nhiễm sắc thể, gen, phép lai một cặp tính trạng qua khung Punnett và cơ chế xác định giới tính."
    },
    {
        "id": "sec_genetic_code",
        "title": "1. Nhiễm sắc thể, Gen & Alen (Genetic Code Overview)",
        "selector": "#sec-genetic-code",
        "en": "Section 1 defines key genetic concepts: A chromosome is a thread-like structure of DNA carrying genetic information in the form of genes. A gene is a length of DNA that codes for a specific protein. An allele is an alternative form of a gene.",
        "vi": "Mục một định nghĩa các khái niệm di truyền cốt lõi: Nhiễm sắc thể là cấu trúc dạng sợi chứa phân tử DNA mang thông tin di truyền dưới dạng các gen. Gen là một đoạn phân tử DNA mã hóa cho một loại protein xác định. Alen là các trạng thái biểu hiện khác nhau của cùng một gen."
    },
    {
        "id": "sec_mitosis_meiosis",
        "title": "➗ Mitosis vs Meiosis (Nguyên phân & Giảm phân)",
        "selector": "#sec-mitosis-meiosis",
        "en": "Mitosis versus meiosis: Mitosis is nuclear division giving rise to genetically identical diploid cells with 46 chromosomes for growth, tissue repair, and asexual reproduction. Meiosis is reduction division halving chromosome number to produce four genetically different haploid gametes with 23 chromosomes for sexual reproduction.",
        "vi": "So sánh nguyên phân và giảm phân: Nguyên phân là phân chia tế bào tạo ra các tế bào lưỡng bội giống hệt nhau về di truyền với 46 nhiễm sắc thể để sinh trưởng, tái tạo mô và sinh sản vô tính. Giảm phân là phân chia giảm nhiễm làm giảm một nửa số lượng nhiễm sắc thể để tạo ra bốn giao tử đơn bội khác nhau về di truyền với 23 nhiễm sắc thể cho sinh sản hữu tính."
    },
    {
        "id": "sec_monohybrid_inheritance",
        "title": "2. Di truyền Đơn tính & Khung Punnett (Monohybrid Crosses Overview)",
        "selector": "#sec-monohybrid-inheritance",
        "en": "Section 2 investigates monohybrid inheritance: Homozygous individuals have two identical alleles for a particular gene (BB or bb). Heterozygous individuals have two different alleles (Bb). A dominant allele is expressed in both homozygotes and heterozygotes. A recessive allele is only expressed when homozygous recessive.",
        "vi": "Mục hai nghiên cứu di truyền đơn tính: Cá thể đồng hợp mang hai alen giống hệt nhau của cùng một gen (BB hoặc bb). Cá thể dị hợp mang hai alen khác nhau (Bb). Alen trội được biểu hiện ra kiểu hình ở cả trạng thái đồng hợp trội và dị hợp. Alen lặn chỉ được biểu hiện khi ở trạng thái đồng hợp lặn."
    },
    {
        "id": "sec_punnett_summary",
        "title": "📊 Punnett Summary: 3:1 Ratio (Tỷ lệ Kiểu hình 3:1)",
        "selector": "#sec-punnett-summary",
        "en": "Summary of heterozygous monohybrid cross: Crossing two heterozygous tall parents (Tt × Tt) produces a genotypic ratio of 1 TT : 2 Tt : 1 tt, yielding a classic phenotypic ratio of 3 tall plants to 1 short plant (75% tall, 25% short).",
        "vi": "Tổng kết phép lai phân tích một cặp tính trạng: Lai hai cá thể bố mẹ dị hợp thân cao (Tt × Tt) cho tỷ lệ kiểu gen 1 TT : 2 Tt : 1 tt, dẫn đến tỷ lệ kiểu hình kinh điển là 3 thân cao : 1 thân lùn (75% cao, 25% lùn)."
    },
    {
        "id": "sec_pedigree-sex",
        "title": "3. Phả hệ & Xác định Giới tính (Pedigree Charts & Sex Determination Overview)",
        "selector": "#sec-pedigree-sex",
        "en": "Section 3 covers sex determination and pedigree charts: Pedigree charts track phenotypes across generations to deduce genotypes. Squares represent males, circles represent females, and shading indicates individuals affected by the genetic trait.",
        "vi": "Mục ba trình bày sơ đồ phả hệ và cơ chế xác định giới tính: Sơ đồ phả hệ theo dõi kiểu hình qua các thế hệ để suy luận kiểu gen. Hình vuông biểu thị nam, hình tròn biểu thị nữ và hình tô đậm biểu thị cá thể mang tính trạng bệnh."
    },
    {
        "id": "sec_sex_determination",
        "title": "👦👧 Sex Determination in Humans (Xác định Giới tính 50:50)",
        "selector": "#sec-sex-determination",
        "en": "Sex determination in humans: The 23rd chromosome pair determines biological sex. Females are homogametic XX; males are heterogametic XY. Crossing XX and XY always results in a 1:1 ratio, meaning a 50% chance of a boy and 50% chance of a girl at each fertilisation.",
        "vi": "Cơ chế xác định giới tính ở người: Cặp nhiễm sắc thể số 23 quyết định giới tính sinh học. Nữ giới mang cặp đồng giao tử XX; nam giới mang cặp dị giao tử XY. Phép lai XX và XY luôn cho tỷ lệ 1:1, nghĩa là xác suất 50% sinh con trai và 50% sinh con gái trong mỗi lần thụ tinh."
    }
]

B16_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_genetic_code": {"start": 1, "end": 2},
    "sec-genetic-code": {"start": 1, "end": 2},
    "sec_mitosis_meiosis": {"start": 2, "end": 2},
    "sec-mitosis-meiosis": {"start": 2, "end": 2},
    "sec_monohybrid_inheritance": {"start": 3, "end": 4},
    "sec-monohybrid-inheritance": {"start": 3, "end": 4},
    "sec_punnett_summary": {"start": 4, "end": 4},
    "sec-punnett-summary": {"start": 4, "end": 4},
    "sec_pedigree-sex": {"start": 5, "end": 6},
    "sec-pedigree-sex": {"start": 5, "end": 6},
    "sec_sex_determination": {"start": 6, "end": 6},
    "sec-sex-determination": {"start": 6, "end": 6}
}

# =====================================================================
# B17: VARIATION AND SELECTION
# =====================================================================
B17_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B17: Biến dị & Chọn lọc Tự nhiên",
        "selector": "#sec-header",
        "en": "Welcome to Topic B17: Variation and Selection. Differences between individuals of the same species drive biological evolution. In this topic, we analyze continuous versus discontinuous variation, adaptive features in xerophytes and hydrophytes, and natural selection.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B17: Biến dị và Chọn lọc. Sự sai khác giữa các cá thể cùng loài là động lực thúc đẩy tiến hóa sinh học. Trong chuyên đề này, chúng ta sẽ phân tích biến dị liên tục và không liên tục, cấu tạo thích nghi của cây sa mạc và cây dưới nước, cùng thuyết chọn lọc tự nhiên."
    },
    {
        "id": "sec_variation_mutation",
        "title": "1. Các Loại Biến dị & Đột biến (Variation & Mutation Overview)",
        "selector": "#sec-variation-mutation",
        "en": "Section 1 contrasts types of variation: Variation is the differences between individuals of the same species. Mutation is a random change in the base sequence of DNA, producing new alleles. The rate of mutation increases with exposure to ionising radiation and mutagenic chemicals.",
        "vi": "Mục một phân biệt các loại biến dị: Biến dị là sự sai khác giữa các cá thể cùng loài. Đột biến là sự biến đổi ngẫu nhiên trong trình tự nucleotide của DNA tạo ra alen mới. Tần số đột biến tăng vọt khi tiếp xúc với bức xạ ion hóa và hóa chất gây đột biến."
    },
    {
        "id": "sec_continuous_discontinuous",
        "title": "📊 Continuous vs Discontinuous Variation (Biến dị Liên tục & Không liên tục)",
        "selector": "#sec-continuous-discontinuous",
        "en": "Continuous vs discontinuous variation: Continuous variation shows a smooth range of phenotypes without distinct categories, caused by multiple genes and environment (e.g. height, mass). Discontinuous variation produces clear-cut distinct categories with no intermediates, caused solely by genes (e.g. ABO blood groups).",
        "vi": "Biến dị liên tục và không liên tục: Biến dị liên tục biểu hiện một dải liên tục không có ranh giới rõ rệt, do nhiều gen và môi trường chi phối (ví dụ chiều cao, cân nặng). Biến dị không liên tục tạo ra các nhóm riêng biệt không có dạng trung gian, hoàn toàn do gen quy định (ví dụ nhóm máu ABO)."
    },
    {
        "id": "sec_adaptive_features",
        "title": "2. Cấu tạo Thích nghi: Cây Sa mạc & Thủy sinh (Adaptive Features Overview)",
        "selector": "#sec-adaptive-features",
        "en": "Section 2 investigates structural adaptations: An adaptive feature is an inherited feature that helps an organism to survive and reproduce in its environment. We contrast xerophytes living in deserts with hydrophytes living in water.",
        "vi": "Mục hai khảo sát các cấu tạo thích nghi: Cấu tạo thích nghi là đặc điểm di truyền giúp sinh vật sống sót và sinh sản trong môi trường sống của nó. Chúng ta so sánh cây chịu hạn sống ở sa mạc với cây thủy sinh sống trong nước."
    },
    {
        "id": "sec_xerophytes_hydrophytes",
        "title": "🌵 Xerophytes vs Hydrophytes Adaptations (Thích nghi Cây Sa mạc & Thủy sinh)",
        "selector": "#sec-xerophytes-hydrophytes",
        "en": "Plant adaptations: Xerophytes conserve water using thick waxy cuticles, sunken stomata, rolled leaves, spines, and deep extensive roots. Hydrophytes thrive in water with large buoyant air spaces (aerenchyma), stomata on upper leaf surfaces, thin cuticles, and reduced roots.",
        "vi": "Thích nghi ở thực vật: Cây sa mạc tiết kiệm nước nhờ lớp cutin dày, khí khổng thụt sâu trong hố, lá cuộn hoặc tiêu giảm thành gai và rễ cắm sâu. Cây thủy sinh thích nghi trong nước nhờ các khoang khí lớn giúp cây nổi, khí khổng ở mặt trên lá, lớp cutin mỏng và hệ rễ tiêu giảm."
    },
    {
        "id": "sec_natural_selection",
        "title": "3. Chọn lọc Tự nhiên & Chọn giống Nhân tạo (Natural Selection Overview)",
        "selector": "#sec-natural-selection",
        "en": "Section 3 covers natural and artificial selection: Natural selection operates in nature to adapt populations to changing habitats. Selective breeding is artificial selection carried out by humans to produce economically desirable characteristics in livestock and crops over successive generations.",
        "vi": "Mục ba trình bày chọn lọc tự nhiên và chọn giống nhân tạo: Chọn lọc tự nhiên diễn ra trong tự nhiên giúp quần thể thích nghi với môi trường sống. Chọn giống nhân tạo do con người chủ động tuyển chọn các tính trạng mong muốn qua nhiều thế hệ cây trồng và vật nuôi."
    },
    {
        "id": "sec_natural_selection_stages",
        "title": "🌿 5 Stages of Natural Selection (5 Giai đoạn Chọn lọc Tự nhiên)",
        "selector": "#sec-natural-selection-stages",
        "en": "The 5 stages of natural selection: 1. Overproduction of offspring. 2. Genetic variation among individuals. 3. Struggle for existence and competition for limited resources. 4. Survival of the fittest with advantageous alleles. 5. Inheritance: survivors reproduce and pass favourable alleles to the next generation.",
        "vi": "Năm giai đoạn của chọn lọc tự nhiên: Một là sinh sản quá mức con non. Hai là biến dị di truyền giữa các cá thể. Ba là đấu tranh sinh tồn và cạnh tranh tài nguyên. Bốn là sống sót của các cá thể thích nghi nhất mang alen có lợi. Năm là di truyền: các cá thể sống sót sinh sản và truyền alen có lợi cho đời sau."
    }
]

B17_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_variation_mutation": {"start": 1, "end": 2},
    "sec-variation-mutation": {"start": 1, "end": 2},
    "sec_continuous_discontinuous": {"start": 2, "end": 2},
    "sec-continuous-discontinuous": {"start": 2, "end": 2},
    "sec_adaptive_features": {"start": 3, "end": 4},
    "sec-adaptive-features": {"start": 3, "end": 4},
    "sec_xerophytes_hydrophytes": {"start": 4, "end": 4},
    "sec-xerophytes-hydrophytes": {"start": 4, "end": 4},
    "sec_natural_selection": {"start": 5, "end": 6},
    "sec-natural-selection": {"start": 5, "end": 6},
    "sec_natural_selection_stages": {"start": 6, "end": 6},
    "sec-natural-selection-stages": {"start": 6, "end": 6}
}

# =====================================================================
# B18: ORGANISMS AND THEIR ENVIRONMENT
# =====================================================================
B18_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B18: Sinh vật & Môi trường",
        "selector": "#sec-header",
        "en": "Welcome to Topic B18: Organisms and their Environment. Ecology examines the complex interrelationships between organisms and their physical habitats. In this topic, we study ecological definitions, food chains, energy losses, and the global carbon cycle.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B18: Sinh vật và Môi trường. Sinh thái học nghiên cứu mối quan hệ tương hỗ phức tạp giữa các sinh vật và môi trường sống của chúng. Trong chuyên đề này, chúng ta sẽ học về các thuật ngữ sinh thái, chuỗi thức ăn, sự thất thoát năng lượng và chu trình carbon toàn cầu."
    },
    {
        "id": "sec_ecological_definitions",
        "title": "1. Các Khái niệm Sinh thái Cốt lõi (Ecological Definitions Overview)",
        "selector": "#sec-ecological-definitions",
        "en": "Section 1 defines fundamental ecological terms: A population is a group of organisms of one species living in the same area at the same time. A community is all the populations of different species in an ecosystem. An ecosystem is a unit containing a community of organisms and their non-living environment interacting together.",
        "vi": "Mục một định nghĩa các thuật ngữ sinh thái cơ bản: Quần thể là tập hợp các cá thể cùng một loài sống trong cùng một khu vực tại cùng một thời điểm. Quần xã là tập hợp tất cả các quần thể thuộc các loài khác nhau cùng sinh sống. Hệ sinh thái là một thể thống nhất bao gồm quần xã sinh vật và môi trường vô sinh tác động qua lại lẫn nhau."
    },
    {
        "id": "sec_food_chains_energy",
        "title": "2. Chuỗi Thức ăn & Dòng Năng lượng (Food Chains & Energy Flow Overview)",
        "selector": "#sec-food-chains-energy",
        "en": "Section 2 investigates food chains and energy flow: The Sun is the principal source of energy input to biological systems. Energy flows unidirectionally through trophic levels: producer ➔ primary consumer ➔ secondary consumer ➔ tertiary consumer.",
        "vi": "Mục hai nghiên cứu chuỗi thức ăn và dòng năng lượng: Mặt trời là nguồn cung cấp năng lượng chủ yếu cho sinh giới. Năng lượng truyền một chiều qua các bậc dinh dưỡng: sinh vật sản xuất ➔ sinh vật tiêu thụ bậc một ➔ bậc hai ➔ bậc ba."
    },
    {
        "id": "sec_energy_loss_rule",
        "title": "📉 The 10% Energy Loss Rule (Quy tắc Thất thoát Năng lượng 90%)",
        "selector": "#sec-energy-loss-rule",
        "en": "The 10% rule in food chains: Only approximately 10% of energy is transferred from one trophic level to the next. Roughly 90% of energy is lost at each step due to metabolic heat during respiration, uneaten body parts, and energy lost in excretion and egestion.",
        "vi": "Quy tắc 10% trong chuỗi thức ăn: Chỉ có khoảng 10% năng lượng được truyền từ bậc dinh dưỡng này sang bậc kế tiếp. Khoảng 90% năng lượng bị thất thoát ở mỗi mắt xích do nhiệt chuyển hóa khi hô hấp, các bộ phận không ăn được và chất bài tiết, phân."
    },
    {
        "id": "sec_carbon_cycle",
        "title": "3. Chu trình Carbon Toàn cầu (The Global Carbon Cycle Overview)",
        "selector": "#sec-carbon-cycle",
        "en": "Section 3 covers the carbon cycle: Photosynthesis is the only biological process that removes carbon dioxide from the atmosphere. Respiration by plants, animals, and decomposers, alongside the combustion of fossil fuels, returns carbon dioxide back into the atmosphere.",
        "vi": "Mục ba phân tích chu trình carbon toàn cầu: Quang hợp là quá trình sinh học duy nhất giúp hấp thụ khí CO2 ra khỏi khí quyển. Hô hấp ở thực vật, động vật và vi sinh vật phân giải, cùng hoạt động đốt cháy nhiên liệu hóa thạch, sẽ giải phóng CO2 trả lại vào khí quyển."
    },
    {
        "id": "sec_carbon_processes",
        "title": "♻️ 4 Key Carbon Cycle Processes (4 Quá trình Chu trình Carbon)",
        "selector": "#sec-carbon-processes",
        "en": "Four processes driving the global carbon cycle: 1. Photosynthesis removes carbon dioxide from the atmosphere. 2. Respiration by all living organisms releases carbon dioxide. 3. Decomposition breaks down organic matter releasing carbon dioxide. 4. Combustion of fossil fuels burns coal, oil, and gas releasing immense volumes of carbon dioxide.",
        "vi": "Bốn quá trình thúc đẩy chu trình carbon toàn cầu: Một là quang hợp hấp thụ CO2 từ khí quyển. Hai là hô hấp của các sinh vật sống giải phóng CO2. Ba là phân hủy xác sinh vật giải phóng CO2. Bốn là đốt cháy nhiên liệu hóa thạch than đá, dầu mỏ và khí đốt thải ra lượng lớn khí CO2."
    }
]

B18_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_ecological_definitions": {"start": 1, "end": 1},
    "sec-ecological-definitions": {"start": 1, "end": 1},
    "sec_food_chains_energy": {"start": 2, "end": 3},
    "sec-food-chains-energy": {"start": 2, "end": 3},
    "sec_energy_loss_rule": {"start": 3, "end": 3},
    "sec-energy-loss-rule": {"start": 3, "end": 3},
    "sec_carbon_cycle": {"start": 4, "end": 5},
    "sec-carbon-cycle": {"start": 4, "end": 5},
    "sec_carbon_processes": {"start": 5, "end": 5},
    "sec-carbon-processes": {"start": 5, "end": 5}
}

# =====================================================================
# B19: HUMAN INFLUENCES ON ECOSYSTEMS
# =====================================================================
B19_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B19: Tác động của Con người lên Hệ sinh thái",
        "selector": "#sec-header",
        "en": "Welcome to Topic B19: Human Influences on Ecosystems. Human activities exert immense pressures on global environments. In this topic, we study modern agriculture impacts, deforestation, eutrophication water pollution, and sustainable conservation strategies.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B19: Tác động của Con người lên Hệ sinh thái. Hoạt động của loài người đang gây áp lực to lớn lên môi trường toàn cầu. Trong chuyên đề này, chúng ta sẽ học về tác động của nông nghiệp hiện đại, nạn phá rừng, hiện tượng phú dưỡng nguồn nước và các chiến lược bảo tồn đa dạng sinh học."
    },
    {
        "id": "sec_agriculture",
        "title": "1. Nông nghiệp & Nguồn Cung Thực phẩm (Food Supply & Agriculture Overview)",
        "selector": "#sec-agriculture",
        "en": "Section 1 examines modern agricultural practices: Monocultures and intensive livestock farming increase production yields to meet human food demand, but create severe environmental challenges.",
        "vi": "Mục một phân tích các hoạt động nông nghiệp hiện đại: Trồng độc canh và chăn nuôi gia súc tập trung giúp tăng năng suất để đáp ứng nhu cầu lương thực, nhưng tạo ra các thách thức môi trường nghiêm trọng."
    },
    {
        "id": "sec_monoculture_livestock",
        "title": "🌾 Monocultures & Intensive Livestock (Độc canh & Chăn nuôi)",
        "selector": "#sec-monoculture-livestock",
        "en": "Modern agriculture trade-offs: Monocultures maximize crop yield efficiency but severely reduce biodiversity and cause pest outbreaks. Intensive livestock farming reduces kinetic energy loss to boost meat production but raises severe ethical concerns, antibiotic resistance risks, and methane emissions.",
        "vi": "Mặt trái của nông nghiệp hiện đại: Trồng độc canh tối đa hóa năng suất nhưng làm suy giảm đa dạng sinh học và bùng phát sâu bệnh. Chăn nuôi gia súc tập trung giảm tiêu hao năng lượng vận động để tăng sản lượng thịt nhưng gây lo ngại về đạo đức, kháng kháng sinh và phát thải khí mê-tan."
    },
    {
        "id": "sec_deforestation",
        "title": "2. Phá hủy Môi trường sống & Nạn Phá rừng (Deforestation Overview)",
        "selector": "#sec-deforestation",
        "en": "Section 2 investigates deforestation: Clearing forests for agriculture, timber, and urban growth results in habitat destruction and species extinction, severe soil erosion, increased flooding, and higher atmospheric CO₂ levels exacerbating the enhanced greenhouse effect.",
        "vi": "Mục hai nghiên cứu nạn phá rừng: Việc chặt phá rừng để lấy đất canh tác, khai thác gỗ và phát triển đô thị dẫn đến mất môi trường sống và tuyệt chủng loài, xói mòn đất nghiêm trọng, gia tăng lũ lụt và nâng cao nồng độ CO2 trong khí quyển thúc đẩy hiệu ứng nhà kính."
    },
    {
        "id": "sec_deforestation_effects",
        "title": "🚜 Deforestation Environmental Damages (Hậu quả Nạn Phá rừng)",
        "selector": "#sec-deforestation-effects",
        "en": "Four severe impacts of deforestation: 1. Atmospheric CO₂ rise and enhanced greenhouse effect. 2. Severe topsoil erosion washed away by rain. 3. Increased downstream flooding due to loss of tree water uptake. 4. Irreversible habitat loss driving widespread species extinction.",
        "vi": "Bốn tác động nghiêm trọng của nạn phá rừng: Một là tăng CO2 khí quyển thúc đẩy hiệu ứng nhà kính. Hai là xói mòn lớp đất màu mỡ do mưa trôi. Ba là gia tăng lũ lụt hạ lưu do mất thảm thực vật giữ nước. Bốn là mất môi trường sống dẫn đến tuyệt chủng loài không thể cứu vãn."
    },
    {
        "id": "sec_eutrophication",
        "title": "3. Ô nhiễm Nước & Hiện tượng Phú dưỡng (Eutrophication Overview)",
        "selector": "#sec-eutrophication",
        "en": "Section 3 investigates eutrophication: Artificial nitrate fertilisers leach into waterways ➔ rapid growth of surface algae (algal bloom) blocks sunlight ➔ submerged aquatic plants die ➔ aerobic decomposer bacteria multiply and deplete dissolved oxygen ➔ aquatic animals suffocate and die.",
        "vi": "Mục ba phân tích quá trình phú dưỡng: Phân bón nitrat rửa trôi vào sông hồ ➔ tảo nở hoa bao phủ mặt nước che khuất ánh sáng ➔ thực vật thủy sinh dưới đáy chết ➔ vi khuẩn phân hủy hiếu khí sinh sôi tiêu thụ cạn kiệt lượng oxy hòa tan ➔ cá và động vật thủy sinh bị ngạt thở chết hàng loạt."
    },
    {
        "id": "sec_conservation",
        "title": "4. Bảo tồn Đa dạng Sinh học (Conservation of Biodiversity Overview)",
        "selector": "#sec-conservation",
        "en": "Section 4 covers conservation strategies: A species becomes endangered when its population falls so low that it is at risk of extinction. Conservation methods include establishing protected nature reserves, captive breeding programs, seed banks, reducing fossil fuel reliance, and international treaties.",
        "vi": "Mục bốn trình bày các biện pháp bảo tồn: Một loài trở nên nguy cấp khi số lượng cá thể giảm xuống mức có nguy cơ tuyệt chủng. Các chiến lược bảo tồn bao gồm thành lập khu bảo tồn thiên nhiên, nhân giống nuôi nhốt, ngân hàng hạt giống, giảm phụ thuộc vào nhiên liệu hóa thạch và các công ước quốc tế."
    }
]

B19_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_agriculture": {"start": 1, "end": 2},
    "sec-agriculture": {"start": 1, "end": 2},
    "sec_monoculture_livestock": {"start": 2, "end": 2},
    "sec-monoculture-livestock": {"start": 2, "end": 2},
    "sec_deforestation": {"start": 3, "end": 4},
    "sec-deforestation": {"start": 3, "end": 4},
    "sec_deforestation_effects": {"start": 4, "end": 4},
    "sec-deforestation-effects": {"start": 4, "end": 4},
    "sec_eutrophication": {"start": 5, "end": 5},
    "sec-eutrophication": {"start": 5, "end": 5},
    "sec_conservation": {"start": 6, "end": 6},
    "sec-conservation": {"start": 6, "end": 6}
}

async def main():
    print("=================================================================")
    print("STARTING BATCH 4 AUDIO GENERATION (B15, B16, B17, B18, B19)")
    print("=================================================================")
    
    # Process B15
    await process_lecture_audio(
        lecture_code="b15",
        lecture_id="deb8222d-2b75-42a3-b454-9601fbfa1bd2",
        course_title=COURSE_TITLE,
        lecture_title="B15: Reproduction",
        segments=B15_SEGMENTS,
        major_sections=B15_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B16
    await process_lecture_audio(
        lecture_code="b16",
        lecture_id="d48c8f84-ba93-49d4-bf61-c7890bd6d2ce",
        course_title=COURSE_TITLE,
        lecture_title="B16: Inheritance",
        segments=B16_SEGMENTS,
        major_sections=B16_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B17
    await process_lecture_audio(
        lecture_code="b17",
        lecture_id="24f0deeb-3cd9-4b82-b253-5a070ca31275",
        course_title=COURSE_TITLE,
        lecture_title="B17: Variation and selection",
        segments=B17_SEGMENTS,
        major_sections=B17_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B18
    await process_lecture_audio(
        lecture_code="b18",
        lecture_id="cbeb6b74-e9c2-4a91-b39f-decb63e72ec0",
        course_title=COURSE_TITLE,
        lecture_title="B18: Organisms and their environment",
        segments=B18_SEGMENTS,
        major_sections=B18_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B19
    await process_lecture_audio(
        lecture_code="b19",
        lecture_id="298327a8-455a-44d5-9a4c-164e2653c456",
        course_title=COURSE_TITLE,
        lecture_title="B19: Human influences on ecosystems",
        segments=B19_SEGMENTS,
        major_sections=B19_MAJOR_SECTIONS,
        subject="science"
    )
    
    print("\n🎉 BATCH 4 (B15, B16, B17, B18, B19) AUDIO & MANIFESTS GENERATION COMPLETED!")

if __name__ == "__main__":
    asyncio.run(main())
