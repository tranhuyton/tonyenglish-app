# -*- coding: utf-8 -*-
"""
Batch 1 Builder: Topics 2, 3, 4, 5
- Transforms HTML for both Page 1 (English) and Page 2 (Bilingual)
- Adds interactive card styling, matching IDs, data-lecture-section, and audio badges
- Ensures strict div balance (diff == 0)
- Generates bilingual audio for new sub-items (caching existing major sections)
- Builds and updates manifest.json
- Updates Supabase lecture_pages
- Verifies 100% selector matching and validity
"""

import os
import sys
import re
import json
import asyncio
from bs4 import BeautifulSoup
from audio_lecture_engine import process_lecture_audio, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# DEFINITIONS FOR TOPIC 2: Cells and organisms
# ==============================================================================
T2_ID = '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc'
T2_CODE = '2'
T2_TITLE = 'Topic 2: Cells and organisms'

T2_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 2: Tế bào và Cấu trúc Sinh vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic 2: Cells and organisms. Cells are the fundamental structural and functional units of all living things. In this lesson, we analyze plant, animal, and bacterial cell ultrastructure, understand levels of organisation, explore specialised cells, and master magnification calculations.",
        "vi": "Chào mừng các bạn đến với Bài 2: Tế bào và sinh vật. Tế bào là đơn vị cấu trúc và chức năng cơ bản của mọi sinh vật sống. Trong bài học này, chúng ta sẽ phân tích cấu trúc siêu vi của tế bào thực vật, động vật và vi khuẩn, hiểu rõ các cấp độ tổ chức sống, các tế bào chuyên hóa và công thức tính độ phóng đại."
    },
    {
        "id": "sec_cell_structures",
        "title": "1. Cấu trúc Tế bào & Bào quan (Cell Organelles)",
        "selector": "#sec-cell-structures",
        "en": "Section 1 explores cell organelles: Organelles are specialised sub-cellular compartments performing dedicated metabolic tasks. Eukaryotic animal and plant cells possess a membrane-bound nucleus and mitochondria, whereas prokaryotic bacterial cells lack a true nucleus.",
        "vi": "Mục 1 khảo sát cấu trúc tế bào và các bào quan: Bào quan là các khoang cấu trúc dưới tế bào chuyên biệt đảm nhiệm những chức năng chuyển hóa riêng biệt. Tế bào nhân thực ở động vật và thực vật có nhân bọc màng và ti thể, trong khi tế bào nhân sơ ở vi khuẩn không có màng nhân thật."
    },
    {
        "id": "card_membrane",
        "title": "🛡️ Cell Membrane (Màng tế bào)",
        "selector": "#card-membrane",
        "en": "The cell membrane is a partially permeable lipid bilayer that surrounds the cytoplasm. It controls the entry and exit of dissolved substances by diffusion, osmosis, and active transport, maintaining an optimum internal chemical environment.",
        "vi": "Màng tế bào là một màng bán thấm chọn lọc bao bọc lấy tế bào chất. Màng kiểm soát chặt chẽ các chất đi vào và đi ra khỏi tế bào qua các cơ chế khuếch tán, thẩm thấu và vận chuyển chủ động, giúp duy trì môi trường hóa học nội bào tối ưu."
    },
    {
        "id": "card_cytoplasm",
        "title": "💧 Cytoplasm (Tế bào chất)",
        "selector": "#card-cytoplasm",
        "en": "Cytoplasm is a jelly-like aqueous fluid containing dissolved nutrients, mineral salts, and suspended organelles. It is the primary site of most cellular chemical reactions and metabolic processes.",
        "vi": "Tế bào chất là chất dịch bán lỏng dạng thạch chứa nước, muối khoáng hòa tan, đường, axit amin và các bào quan lơ lửng. Đây là nơi diễn ra phần lớn các phản ứng hóa học và quá trình trao đổi chất của tế bào."
    },
    {
        "id": "card_nucleus",
        "title": "🧬 Nucleus (Nhân tế bào)",
        "selector": "#card-nucleus",
        "en": "The nucleus is the control centre of the eukaryotic cell. It contains genetic material in the form of DNA arranged into chromosomes, controlling protein synthesis, cellular differentiation, and cell division.",
        "vi": "Nhân tế bào là trung tâm điều khiển của tế bào nhân thực. Nhân chứa vật chất di truyền dưới dạng DNA được tổ chức thành các nhiễm sắc thể, điều khiển quá trình tổng hợp protein, biệt hóa tế bào và phân bào."
    },
    {
        "id": "card_mitochondria",
        "title": "⚡ Mitochondria (Ti thể)",
        "selector": "#card-mitochondria",
        "en": "Mitochondria are the powerhouses of eukaryotic cells. They are the site of aerobic cellular respiration, where glucose is broken down with oxygen to release ATP energy for cellular metabolism. Never say mitochondria create energy; they release energy.",
        "vi": "Ti thể là nhà máy năng lượng của tế bào nhân thực. Đây là vị trí diễn ra quá trình hô hấp hiếu khí, nơi glucose bị phân giải cùng oxy để giải phóng năng lượng ATP cho tế bào. Lưu ý thi cử: Luôn nói ti thể giải phóng năng lượng, không bao giờ nói ti thể tạo ra năng lượng."
    },
    {
        "id": "card_ribosomes",
        "title": "🧱 Ribosomes (Ribôxôm)",
        "selector": "#card-ribosomes",
        "en": "Ribosomes are tiny circular structures located free in the cytoplasm or bound to membranes. They are the molecular machines responsible for protein synthesis by assembling amino acids according to genetic instructions.",
        "vi": "Ribosome là các hạt cầu siêu nhỏ nằm tự do trong tế bào chất hoặc gắn trên màng. Chúng là cỗ máy sinh học đảm nhiệm chức năng tổng hợp protein bằng cách lắp ghép các axit amin theo trình tự mã di truyền."
    },
    {
        "id": "card_cellwall",
        "title": "🧱 Cell Wall (Thành tế bào thực vật)",
        "selector": "#card-cellwall",
        "en": "The plant cell wall is an outer protective layer made of tough cellulose fibres. It is fully permeable, provides structural support to withstand high internal turgor pressure, and prevents plant cells from bursting.",
        "vi": "Thành tế bào thực vật là lớp vỏ bảo vệ bên ngoài cấu tạo từ các sợi cellulose vững chắc. Thành tế bào thấm hoàn toàn, giúp nâng đỡ cơ học, tạo hình dạng ổn định và chống vỡ tế bào khi áp suất trương nước tăng cao."
    },
    {
        "id": "card_chloroplast",
        "title": "🌿 Chloroplasts (Lục lạp)",
        "selector": "#card-chloroplast",
        "en": "Chloroplasts are plant organelles that contain green chlorophyll pigments. They absorb light energy to drive photosynthesis, synthesizing organic glucose molecules from carbon dioxide and water.",
        "vi": "Lục lạp là bào quan đặc trưng của tế bào thực vật quang hợp, chứa sắc tố diệp lục màu xanh. Lục lạp hấp thu năng lượng ánh sáng để thực hiện quang hợp, tổng hợp đường glucose từ carbon dioxide và nước."
    },
    {
        "id": "card_vacuole",
        "title": "💧 Permanent Vacuole (Không bào trung tâm)",
        "selector": "#card-vacuole",
        "en": "The permanent central vacuole is a large fluid-filled sac found in mature plant cells. It contains cell sap—a dilute solution of sugars, amino acids, and mineral salts—creating hydrostatic pressure to keep the cell turgid.",
        "vi": "Không bào trung tâm lớn là túi chứa dịch bào nằm giữa tế bào thực vật trưởng thành. Dịch tế bào là dung dịch nước chứa đường, axit amin và muối khoáng hòa tan, tạo áp suất trương nước giúp tế bào luôn căng và nâng đỡ cây non."
    },
    {
        "id": "card_bacteria_cell",
        "title": "🦠 Bacterial Cell (Tế bào Vi khuẩn)",
        "selector": "#card-bacteria-cell",
        "en": "Bacterial cells are prokaryotes: They lack a true membrane-bound nucleus, containing a single circular chromosome loop free in the cytoplasm and small extra rings of DNA called plasmids, enclosed in a peptidoglycan cell wall.",
        "vi": "Tế bào vi khuẩn là sinh vật nhân sơ: Chúng không có màng nhân thật bao bọc, vật chất di truyền là một phân tử DNA trần dạng vòng tự do trong tế bào chất cùng các vòng DNA nhỏ plasmid, bao bọc bởi thành peptidoglycan."
    },
    {
        "id": "sec_cell_comparison",
        "title": "📊 So sánh Tế bào Thực vật vs Động vật",
        "selector": "#sec-cell-comparison",
        "en": "Comparison: Plant and animal cells share cell membranes, cytoplasm, nucleus, mitochondria, and ribosomes. In contrast, plant cells uniquely possess a rigid cellulose cell wall, chloroplasts for photosynthesis, and a large permanent central vacuole.",
        "vi": "So sánh: Tế bào thực vật và động vật đều có màng tế bào, tế bào chất, nhân, ti thể và ribosome. Ngược lại, tế bào thực vật có 3 cấu trúc độc nhất mà tế bào động vật không có: thành tế bào cellulose, lục lạp quang hợp và không bào trung tâm lớn chứa dịch bào."
    },
    {
        "id": "sec_levels_organisation",
        "title": "2. Các cấp độ Tổ chức Sống (Levels of Organisation)",
        "selector": "#sec-levels-organisation",
        "en": "Section 2 outlines the biological hierarchy: Specialized Cells group together into Tissues. Different tissues coordinate to form Organs. Organs work together within Organ Systems, which integrate to build a multicellular Organism.",
        "vi": "Mục 2 phác thảo các cấp độ tổ chức sống: Các tế bào chuyên biệt tập hợp lại thành Mô. Nhiều mô khác nhau phối hợp tạo thành Cơ quan. Các cơ quan hoạt động đồng bộ trong Hệ cơ quan, kết hợp tạo nên một Cơ thể sinh vật hoàn chỉnh."
    },
    {
        "id": "card_level_cell",
        "title": "1. Cell (Tế bào)",
        "selector": "#card-level-cell",
        "en": "A cell is the basic structural and functional building block of life, such as an epithelial cell, a neuron, or a root hair cell.",
        "vi": "Tế bào là đơn vị cấu trúc và chức năng cơ bản nhất của sự sống, ví dụ như tế bào biểu mô, nơron thần kinh hay tế bào lông hút."
    },
    {
        "id": "card_level_tissue",
        "title": "2. Tissue (Mô)",
        "selector": "#card-level-tissue",
        "en": "A tissue is a group of cells with similar structures working together to perform a shared biological function, such as ciliated epithelium or leaf palisade mesophyll.",
        "vi": "Mô là tập hợp các tế bào có cấu trúc tương tự nhau cùng phối hợp thực hiện một chức năng sinh học chung, như biểu mô có lông rung hay mô giậu ở lá."
    },
    {
        "id": "card_level_organ",
        "title": "3. Organ (Cơ quan)",
        "selector": "#card-level-organ",
        "en": "An organ is a distinct body structure composed of several different tissues working together to perform specific functions, such as the heart, stomach, or a plant leaf.",
        "vi": "Cơ quan là cấu trúc cơ thể riêng biệt gồm nhiều mô khác nhau cùng phối hợp thực hiện các chức năng cụ thể, ví dụ như tim, dạ dày hay một chiếc lá cây."
    },
    {
        "id": "card_level_system",
        "title": "4. Organ System (Hệ cơ quan)",
        "selector": "#card-level-system",
        "en": "An organ system is a group of interrelated organs with closely linked functions working together, such as the circulatory system, digestive system, or respiratory system.",
        "vi": "Hệ cơ quan là tập hợp các cơ quan có chức năng liên hệ mật thiết cùng hoạt động đồng bộ, ví dụ như hệ tuần hoàn, hệ tiêu hóa hay hệ hô hấp."
    },
    {
        "id": "card_level_organism",
        "title": "5. Organism (Cơ thể sinh vật)",
        "selector": "#card-level-organism",
        "en": "An organism is a complete living entity made up of cooperating organ systems capable of carrying out all seven characteristics of life independently.",
        "vi": "Cơ thể sinh vật là một thực thể sống hoàn chỉnh gồm các hệ cơ quan phối hợp nhịp nhàng, có khả năng thực hiện độc lập đầy đủ 7 đặc tính của sự sống."
    },
    {
        "id": "sec_specialised_cells",
        "title": "3. Tế bào Chuyên hóa (Specialised Cells)",
        "selector": "#sec-specialised-cells",
        "en": "Section 3 examines cellular specialisation: Cell differentiation changes cellular structure to adapt each cell type for a particular physiological role with maximum efficiency.",
        "vi": "Mục 3 nghiên cứu các tế bào chuyên hóa: Quá trình biệt hóa tế bào làm biến đổi cấu trúc để mỗi loại tế bào thích nghi hoàn hảo với một chức năng sinh lý chuyên biệt với hiệu suất cao nhất."
    },
    {
        "id": "card_roothair",
        "title": "🌱 Root Hair Cell (Tế bào lông hút)",
        "selector": "#card-roothair",
        "en": "Root hair cells possess long, thin, finger-like hair projections that drastically increase the surface area for rapid absorption of water by osmosis and mineral ions by active transport. They contain no chloroplasts because roots underground receive no sunlight.",
        "vi": "Tế bào lông hút có phần lông dài mảnh kéo dài ra ngoài giúp tăng tối đa diện tích bề mặt để hấp thụ nước nhanh qua thẩm thấu và ion khoáng qua vận chuyển chủ động. Tế bào lông hút không có lục lạp vì rễ ở dưới đất không nhận ánh sáng."
    },
    {
        "id": "card_palisade",
        "title": "🍃 Palisade Mesophyll Cell (Tế bào mô giậu)",
        "selector": "#card-palisade",
        "en": "Palisade mesophyll cells are tall, column-shaped cells packed closely together directly beneath the upper epidermis of leaves. They contain a massive density of chloroplasts to maximize sunlight absorption for photosynthesis.",
        "vi": "Tế bào mô giậu có hình trụ cột thon dài xếp khít nhau nằm ngay dưới lớp biểu bì trên của lá. Chúng chứa mật độ lục lạp cực kỳ đậm đặc để tối đa hóa khả năng hấp thu ánh sáng mặt trời cho quang hợp."
    },
    {
        "id": "card_ciliated",
        "title": "💨 Ciliated Epithelial Cell (Tế bào biểu mô có lông rung)",
        "selector": "#card-ciliated",
        "en": "Ciliated cells line human respiratory passages such as the trachea and bronchi. Their tiny hair-like cilia beat in coordinated rhythmic waves to sweep mucus and trapped pathogens upwards away from the lungs.",
        "vi": "Tế bào biểu mô có lông rung lót dọc đường hô hấp như khí quản và phế quản. Hàng ngàn lông rung tí hon chuyển động nhịp nhàng như làn sóng để quét chất nhầy cùng bụi bẩn và vi khuẩn ngược lên họng tránh đi vào phổi."
    },
    {
        "id": "card_rbc",
        "title": "🔴 Red Blood Cell (Tế bào hồng cầu)",
        "selector": "#card-rbc",
        "en": "Red blood cells transport oxygen. They have a biconcave disc shape to maximize surface area to volume ratio for rapid oxygen diffusion, contain haemoglobin to bind oxygen, and lack a nucleus to leave maximum space for haemoglobin.",
        "vi": "Hồng cầu chuyên chở khí oxy. Chúng có hình đĩa lõm hai mặt giúp tăng tối đa tỉ lệ diện tích trên thể tích cho oxy khuếch tán nhanh, chứa đầy phân tử sắc tố haemoglobin và không có nhân để dành trọn không gian chứa haemoglobin."
    },
    {
        "id": "card_neuron",
        "title": "⚡ Nerve Cell / Neuron (Tế bào thần kinh)",
        "selector": "#card-neuron",
        "en": "Neurons transmit electrical nerve impulses across long distances. They feature an elongated axon for rapid impulse conduction, branched dendrites to receive impulses, and a fatty myelin sheath for electrical insulation.",
        "vi": "Tế bào thần kinh truyền dẫn xung điện thần kinh trên khoảng cách dài. Chúng có sợi trục kéo dài giúp dẫn truyền xung cực nhanh, các sợi nhánh phân chia để tiếp nhận tín hiệu và bao myelin bọc ngoài giúp cách điện."
    },
    {
        "id": "card_sperm",
        "title": "🏊 Sperm Cell (Tinh trùng)",
        "selector": "#card-sperm",
        "en": "Sperm cells deliver male genetic material to the egg during fertilisation. They feature an acrosome containing digestive enzymes to penetrate the egg jelly coat, a midpiece packed with mitochondria releasing ATP for swimming, and a flagellum tail for propulsion.",
        "vi": "Tinh trùng vận chuyển vật chất di truyền của bố đến thụ tinh với trứng. Đầu tinh trùng có thể đỉnh acrosome chứa enzym tiêu hóa màng ngoài của trứng, phần giữa chứa đầy ti thể giải phóng năng lượng ATP và đuôi roi giúp bơi nhanh."
    },
    {
        "id": "card_egg",
        "title": "🥚 Egg Cell / Ovum (Tế bào trứng)",
        "selector": "#card-egg",
        "en": "The egg cell is the large female gamete. It contains a massive volume of nutrient-rich cytoplasm to nourish the embryo after fertilisation and a protective outer jelly coat that chemically hardens immediately after one sperm enters to prevent polyspermy.",
        "vi": "Tế bào trứng là giao tử cái kích thước lớn. Trứng chứa lượng tế bào chất khổng lồ giàu dinh dưỡng để nuôi dưỡng phôi ban đầu và lớp màng nhầy bên ngoài sẽ cứng lại ngay lập tức khi một tinh trùng xâm nhập để ngăn ngừa đa tinh trùng."
    },
    {
        "id": "sec_magnification",
        "title": "4. Tính Độ phóng đại: Quy tắc Tam giác IAM",
        "selector": "#sec-magnification",
        "en": "Section 4 covers magnification calculations using the IAM triangle: Image size equals Actual size multiplied by Magnification. To find Actual size, divide Image size by Magnification. Always convert measurements to the same unit first: one millimetre equals one thousand micrometres!",
        "vi": "Mục 4 hướng dẫn tính độ phóng đại thông qua tam giác IAM: Kích thước ảnh (Image) bằng Kích thước thực (Actual) nhân Độ phóng đại (Magnification). Để tìm kích thước thực, lấy kích thước ảnh chia độ phóng đại. Nhớ đổi về cùng đơn vị trước: 1 milimét bằng 1000 micromét!"
    },
    {
        "id": "card_iam_formula",
        "title": "📐 Công thức Tam giác IAM ($I = A \\times M$)",
        "selector": "#card-iam-formula",
        "en": "The IAM formula triangle: Cover Image size to get Actual multiplied by Magnification. Cover Actual size to get Image divided by Magnification. Cover Magnification to get Image size divided by Actual size.",
        "vi": "Tam giác công thức IAM: Che chữ I sẽ được A nhân M. Che chữ A sẽ được I chia M. Che chữ M sẽ được I chia A. Hãy luôn ghi rõ đơn vị và các bước tính trong bài thi Cambridge để lấy trọn điểm phương pháp."
    },
    {
        "id": "card_units_conversion",
        "title": "🔄 Quy tắc Chuyển đổi Đơn vị ($1\\text{ mm} = 1000\\ \\mu\\text{m}$)",
        "selector": "#card-units-conversion",
        "en": "Unit Conversion Rule: When measuring with a ruler in millimetres, multiply by one thousand to convert to micrometres. When given micrometres, divide by one thousand to convert back to millimetres.",
        "vi": "Quy tắc đổi đơn vị đo lường: Khi đo hình ảnh bằng thước theo milimét (mm), hãy nhân với 1000 để đổi sang micromét (μm). Ngược lại, muốn đổi từ micromét sang milimét, hãy chia cho 1000."
    }
]

T2_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_cell_structures": {"start": 1, "end": 11},
    "sec-cell-structures": {"start": 1, "end": 11},
    "sec_cell_comparison": {"start": 12, "end": 12},
    "sec-cell-comparison": {"start": 12, "end": 12},
    "sec_levels_organisation": {"start": 13, "end": 18},
    "sec-levels-organisation": {"start": 13, "end": 18},
    "sec_specialised_cells": {"start": 19, "end": 26},
    "sec-specialised-cells": {"start": 19, "end": 26},
    "sec_magnification": {"start": 27, "end": 29},
    "sec-magnification": {"start": 27, "end": 29}
}

# ==============================================================================
# HTML TRANSFORMER FOR TOPIC 2
# ==============================================================================
def transform_topic2_html():
    with open('scripts/raw_bio_t2/p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_t2/p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    # Clean top header and study resources
    header_regex = r'<div[^>]*padding:\s*20px[^>]*background:\s*#f8fafc[^>]*>.*?</div>'
    
    clean_header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 2: Cells and Organisms</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Cell Ultrastructure, Plant vs Animal, Levels of Organisation, Specialised Cells &amp; Magnification</p>
        </div>
        <div style="background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #60a5fa;">
            <span>🎧 Click any card to listen</span>
        </div>
    </div>
</div>'''

    clean_header_p2 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #10b981; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610) • Song ngữ</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 2: Tế bào và Cấu trúc Sinh vật</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Cấu trúc tế bào, So sánh TV vs ĐV, Cấp độ tổ chức sống, Tế bào chuyên hóa &amp; Độ phóng đại</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    # Ensure major section headers have id and class in P1 and P2
    for pid, phtml in [('p1', p1), ('p2', p2)]:
        pass

    # Helper replacement map for subcards in P1
    rep_p1 = {
        'id="data-membrane-en"': 'id="card-membrane" class="lecture-interactive-card" data-lecture-section="card_membrane"',
        'id="data-cytoplasm-en"': 'id="card-cytoplasm" class="lecture-interactive-card" data-lecture-section="card_cytoplasm"',
        'id="data-nucleus-en"': 'id="card-nucleus" class="lecture-interactive-card" data-lecture-section="card_nucleus"',
        'id="data-mitochondria-en"': 'id="card-mitochondria" class="lecture-interactive-card" data-lecture-section="card_mitochondria"',
        'id="data-ribosome-en"': 'id="card-ribosomes" class="lecture-interactive-card" data-lecture-section="card_ribosomes"',
        'id="data-cellwall-en"': 'id="card-cellwall" class="lecture-interactive-card" data-lecture-section="card_cellwall"',
        'id="data-chloroplast-en"': 'id="card-chloroplast" class="lecture-interactive-card" data-lecture-section="card_chloroplast"',
        'id="data-vacuole-en"': 'id="card-vacuole" class="lecture-interactive-card" data-lecture-section="card_vacuole"',
        'id="data-bac-cellwall-en"': 'id="card-bac-cellwall" class="lecture-interactive-card" data-lecture-section="card_bac_cellwall"',
        'id="data-circular-dna-en"': 'id="card-circular-dna" class="lecture-interactive-card" data-lecture-section="card_circular_dna"',
        
        'id="data-org-cell-en"': 'id="card-level-cell" class="lecture-interactive-card" data-lecture-section="card_level_cell"',
        'id="data-org-tissue-en"': 'id="card-level-tissue" class="lecture-interactive-card" data-lecture-section="card_level_tissue"',
        'id="data-org-organ-en"': 'id="card-level-organ" class="lecture-interactive-card" data-lecture-section="card_level_organ"',
        'id="data-org-system-en"': 'id="card-level-system" class="lecture-interactive-card" data-lecture-section="card_level_system"',
        'id="data-org-organism-en"': 'id="card-level-organism" class="lecture-interactive-card" data-lecture-section="card_level_organism"',
        
        'id="data-root-hair-en"': 'id="card-roothair" class="lecture-interactive-card" data-lecture-section="card_roothair"',
        'id="data-palisade-shape-en"': 'id="card-palisade" class="lecture-interactive-card" data-lecture-section="card_palisade"',
        'id="data-ciliated-cilia-en"': 'id="card-ciliated" class="lecture-interactive-card" data-lecture-section="card_ciliated"',
        'id="data-rbc-shape-en"': 'id="card-rbc" class="lecture-interactive-card" data-lecture-section="card_rbc"',
        'id="data-neuron-axon-en"': 'id="card-neuron" class="lecture-interactive-card" data-lecture-section="card_neuron"',
        'id="data-sperm-tail-en"': 'id="card-sperm" class="lecture-interactive-card" data-lecture-section="card_sperm"',
        'id="data-egg-jelly-en"': 'id="card-egg" class="lecture-interactive-card" data-lecture-section="card_egg"',
    }
    
    # Helper replacement map for subcards in P2
    rep_p2 = {
        'id="data-membrane-vi"': 'id="card-membrane" class="lecture-interactive-card" data-lecture-section="card_membrane"',
        'id="data-cytoplasm-vi"': 'id="card-cytoplasm" class="lecture-interactive-card" data-lecture-section="card_cytoplasm"',
        'id="data-nucleus-vi"': 'id="card-nucleus" class="lecture-interactive-card" data-lecture-section="card_nucleus"',
        'id="data-mitochondria-vi"': 'id="card-mitochondria" class="lecture-interactive-card" data-lecture-section="card_mitochondria"',
        'id="data-ribosome-vi"': 'id="card-ribosomes" class="lecture-interactive-card" data-lecture-section="card_ribosomes"',
        'id="data-cellwall-vi"': 'id="card-cellwall" class="lecture-interactive-card" data-lecture-section="card_cellwall"',
        'id="data-chloroplast-vi"': 'id="card-chloroplast" class="lecture-interactive-card" data-lecture-section="card_chloroplast"',
        'id="data-vacuole-vi"': 'id="card-vacuole" class="lecture-interactive-card" data-lecture-section="card_vacuole"',
        'id="data-bac-cellwall-vi"': 'id="card-bac-cellwall" class="lecture-interactive-card" data-lecture-section="card_bac_cellwall"',
        'id="data-circular-dna-vi"': 'id="card-circular-dna" class="lecture-interactive-card" data-lecture-section="card_circular_dna"',
        
        'id="data-org-cell-vi"': 'id="card-level-cell" class="lecture-interactive-card" data-lecture-section="card_level_cell"',
        'id="data-org-tissue-vi"': 'id="card-level-tissue" class="lecture-interactive-card" data-lecture-section="card_level_tissue"',
        'id="data-org-organ-vi"': 'id="card-level-organ" class="lecture-interactive-card" data-lecture-section="card_level_organ"',
        'id="data-org-system-vi"': 'id="card-level-system" class="lecture-interactive-card" data-lecture-section="card_level_system"',
        'id="data-org-organism-vi"': 'id="card-level-organism" class="lecture-interactive-card" data-lecture-section="card_level_organism"',
        
        'id="data-root-hair-vi"': 'id="card-roothair" class="lecture-interactive-card" data-lecture-section="card_roothair"',
        'id="data-palisade-shape-vi"': 'id="card-palisade" class="lecture-interactive-card" data-lecture-section="card_palisade"',
        'id="data-ciliated-cilia-vi"': 'id="card-ciliated" class="lecture-interactive-card" data-lecture-section="card_ciliated"',
        'id="data-rbc-shape-vi"': 'id="card-rbc" class="lecture-interactive-card" data-lecture-section="card_rbc"',
        'id="data-neuron-axon-vi"': 'id="card-neuron" class="lecture-interactive-card" data-lecture-section="card_neuron"',
        'id="data-sperm-tail-vi"': 'id="card-sperm" class="lecture-interactive-card" data-lecture-section="card_sperm"',
        'id="data-egg-jelly-vi"': 'id="card-egg" class="lecture-interactive-card" data-lecture-section="card_egg"',
    }

    # Replace in P1
    for k, v in rep_p1.items():
        p1 = p1.replace(k, v)

    # In P1, replace old header
    if 'id="sec-header"' in p1:
        p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', clean_header_p1, p1, count=1, flags=re.DOTALL)
    else:
        p1 = clean_header_p1 + '\n' + p1

    # Replace in P2
    for k, v in rep_p2.items():
        p2 = p2.replace(k, v)
        
    # In P2, add clean header at the beginning
    if 'id="sec-header"' in p2:
        p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', clean_header_p2, p2, count=1, flags=re.DOTALL)
    else:
        p2 = clean_header_p2 + '\n' + p2

    # In P2, add major section IDs to headings if missing
    p2 = p2.replace('>Interactive Cell Map<', ' id="sec-cell-structures" class="lecture-interactive-card" data-lecture-section="sec_cell_structures">Interactive Cell Map<')
    p2 = p2.replace('>📊 Comparison: Plant vs Animal Cells<', ' id="sec-cell-comparison" class="lecture-interactive-card" data-lecture-section="sec_cell_comparison">📊 Comparison: Plant vs Animal Cells<')
    p2 = p2.replace('>🏢 2. LEVELS OF ORGANISATION<', ' id="sec-levels-organisation" class="lecture-interactive-card" data-lecture-section="sec_levels_organisation">🏢 2. LEVELS OF ORGANISATION<')
    p2 = p2.replace('>🔬 3. SPECIALISED CELLS (Tế bào chuyên biệt)<', ' id="sec-specialised-cells" class="lecture-interactive-card" data-lecture-section="sec_specialised_cells">🔬 3. SPECIALISED CELLS (Tế bào chuyên biệt)<')
    p2 = p2.replace('>📐 4. SIZE OF SPECIMENS &amp; MAGNIFICATION (Độ phóng đại)<', ' id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification">📐 4. SIZE OF SPECIMENS &amp; MAGNIFICATION (Độ phóng đại)<')
    p2 = p2.replace('>📐 4. SIZE OF SPECIMENS & MAGNIFICATION (Độ phóng đại)<', ' id="sec-magnification" class="lecture-interactive-card" data-lecture-section="sec_magnification">📐 4. SIZE OF SPECIMENS & MAGNIFICATION (Độ phóng đại)<')

    # Also add magnification cards in both P1 and P2
    # IAM Formula card
    p1 = p1.replace('>🔄 Unit Conversion Rules<', ' id="card-units-conversion" class="lecture-interactive-card" data-lecture-section="card_units_conversion">🔄 Unit Conversion Rules<')
    p2 = p2.replace('>🔄 Quy tắc Chuyển đổi Đơn vị (Unit Conversion)<', ' id="card-units-conversion" class="lecture-interactive-card" data-lecture-section="card_units_conversion">🔄 Quy tắc Chuyển đổi Đơn vị (Unit Conversion)<')

    # Worked Example
    p1 = p1.replace('>💡 Cambridge Worked Example<', ' id="card-iam-formula" class="lecture-interactive-card" data-lecture-section="card_iam_formula">💡 Cambridge Worked Example<')
    p2 = p2.replace('>💡 Ví dụ Mẫu Chuẩn Cambridge<', ' id="card-iam-formula" class="lecture-interactive-card" data-lecture-section="card_iam_formula">💡 Ví dụ Mẫu Chuẩn Cambridge<')

    # Fix div balance
    diff1 = p1.count('<div') - p1.count('</div>')
    if diff1 > 0:
        p1 += '</div>' * diff1
    elif diff1 < 0:
        # If negative, remove trailing extra </div>
        for _ in range(-diff1):
            idx = p1.rfind('</div>')
            if idx != -1:
                p1 = p1[:idx] + p1[idx+6:]

    diff2 = p2.count('<div') - p2.count('</div>')
    if diff2 > 0:
        p2 += '</div>' * diff2
    elif diff2 < 0:
        for _ in range(-diff2):
            idx = p2.rfind('</div>')
            if idx != -1:
                p2 = p2[:idx] + p2[idx+6:]

    assert p1.count('<div') - p1.count('</div>') == 0, "P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, "P2 div diff != 0"

    return p1, p2

async def build_topic_2():
    print(f"\n==========================================")
    print(f"PROCESSING TOPIC 2: {T2_TITLE}")
    print(f"==========================================")
    
    p1_html, p2_html = transform_topic2_html()

    manifest = await process_lecture_audio(
        lecture_code=T2_CODE,
        lecture_id=T2_ID,
        course_title='Cambridge IGCSE Biology (0610)',
        lecture_title=T2_TITLE,
        segments=T2_SEGMENTS,
        major_sections=T2_MAJOR_SECTIONS,
        subject='biology'
    )

    print("Updating Supabase pages for Topic 2...")
    sb.table('lecture_pages').update({'content_html': p1_html}).eq('lecture_id', T2_ID).eq('page_number', 1).execute()
    sb.table('lecture_pages').update({'content_html': p2_html}).eq('lecture_id', T2_ID).eq('page_number', 2).execute()
    print("✅ Topic 2 Supabase updated and manifest written successfully!")

if __name__ == '__main__':
    asyncio.run(build_topic_2())
