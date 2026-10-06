# -*- coding: utf-8 -*-
"""
Batch 2 Builder: Topics 6, 7, 8, 9
- Topic 6: Plant Nutrition (Div diffs fixed: P1 -1 -> 0, P2 -1 -> 0)
- Topic 7: Human nutrition (Div diffs fixed: P1 -2 -> 0, P2 -2 -> 0)
- Topic 8: Transport in plants (Div diffs: P1 0, P2 0)
- Topic 9: Transport in animals (Div diffs: P1 0, P2 0)
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
# TOPIC 6: Plant Nutrition
# ==============================================================================
T6_ID = 'e7d6e813-b7b9-4038-9911-8b886978cd07'
T6_CODE = '6'
T6_TITLE = 'Topic 6: Plant Nutrition'

T6_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 6: Dinh dưỡng Thực vật & Quang hợp",
        "selector": "#sec-header",
        "en": "Welcome to Topic 6: Plant Nutrition. Plants are autotrophic organisms that synthesize their own organic food using light energy through photosynthesis. In this lesson, we master the balanced chemical equation, examine essential mineral ions, analyze internal leaf ultrastructure, investigate Paper 6 core practicals, and evaluate limiting factors.",
        "vi": "Chào mừng các bạn đến với Bài 6: Dinh dưỡng Thực vật & Quang hợp. Thực vật là sinh vật tự dưỡng có khả năng tự tổng hợp chất hữu cơ nhờ năng lượng ánh sáng qua quá trình quang hợp. Trong bài học này, chúng ta sẽ nắm vững phương trình hóa học, các ion khoáng thiết yếu, giải phẫu cấu tạo lá, các bài thực hành Paper 6 trọng tâm và các yếu tố giới hạn."
    },
    {
        "id": "sec_photosynthesis",
        "title": "1. Phương trình Quang hợp & Vai trò của Diệp lục",
        "selector": "#sec-photosynthesis",
        "en": "Section 1: Photosynthesis is the process by which plants manufacture carbohydrates from raw materials using energy from light. The balanced chemical equation is: six carbon dioxide plus six water molecules yields one glucose molecule plus six oxygen molecules, catalyzed by light and chlorophyll.",
        "vi": "Mục 1: Quang hợp là quá trình thực vật tổng hợp carbohydrate từ các nguyên liệu thô bằng cách sử dụng năng lượng ánh sáng. Phương trình hóa học cân bằng là: sáu phân tử CO2 cộng sáu phân tử H2O tạo ra một phân tử C6H12O6 và sáu phân tử O2, dưới tác dụng xúc tác của ánh sáng và chất diệp lục."
    },
    {
        "id": "card_glucose_fate",
        "title": "🔄 Số phận của Phân tử Glucose (Uses of Glucose)",
        "selector": "#card-glucose-fate",
        "en": "What happens to the synthesized glucose? It is used immediately for cellular respiration to release energy, converted into insoluble starch for compact storage, converted into sucrose for transport through phloem, synthesized into cellulose for tough cell walls, and combined with nitrates to form amino acids and proteins.",
        "vi": "Số phận của đường glucose sau quang hợp: Glucose được dùng ngay cho hô hấp tế bào để giải phóng năng lượng, chuyển hóa thành tinh bột không tan để tích trữ gọn gàng, chuyển thành đường sucrose để vận chuyển trong mạch rây, tổng hợp thành cellulose tạo thành tế bào và kết hợp với nitrat tạo axit amin và protein."
    },
    {
        "id": "sec_minerals",
        "title": "2. Nhu cầu Khoáng chất: Nitrat và Magie",
        "selector": "#sec-minerals",
        "en": "Section 2 examines plant mineral requirements: Plants absorb dissolved mineral ions through root hair cells by active transport. Nitrate ions are needed to build amino acids and proteins; deficiency causes stunted growth. Magnesium ions are needed to synthesize chlorophyll; deficiency causes yellowing between leaf veins called chlorosis.",
        "vi": "Mục 2 khảo sát nhu cầu khoáng chất của thực vật: Cây hấp thụ các ion khoáng hòa tan qua tế bào lông hút bằng vận chuyển chủ động. Ion nitrat cần thiết để tổng hợp axit amin và protein; thiếu nitrat cây còi cọc chậm lớn. Ion magie cần thiết để tổng hợp phân tử diệp lục; thiếu magie lá bị vàng úa gân lá gọi là hiện tượng mất diệp lục (chlorosis)."
    },
    {
        "id": "card_nitrates",
        "title": "🔵 Ion Nitrat (NO₃⁻) & Bệnh Còi cọc",
        "selector": "#card-nitrates",
        "en": "Nitrate ions supply nitrogen to combine with glucose to produce amino acids, which form proteins and enzymes. Nitrate deficiency leads to severely stunted plant growth and pale, yellowing older leaves.",
        "vi": "Ion nitrat cung cấp nguyên tố nitơ kết hợp với glucose để sản sinh các axit amin, từ đó lắp ráp nên protein và enzyme. Thiếu hụt nitrat dẫn đến cây còi cọc nghiêm trọng, thân lùn và lá già chuyển sang màu vàng nhạt."
    },
    {
        "id": "card_magnesium",
        "title": "🟢 Ion Magie (Mg²⁺) & Bệnh Vàng lá Chlorosis",
        "selector": "#card-magnesium",
        "en": "Magnesium ions form the central metallic atom in chlorophyll pigment molecules. A deficiency prevents chlorophyll synthesis, turning leaves pale yellow—a condition known as chlorosis—drastically reducing photosynthetic rate.",
        "vi": "Ion magie tạo nên nguyên tử kim loại trung tâm trong cấu trúc phân tử sắc tố diệp lục. Thiếu hụt magie khiến cây không thể tổng hợp diệp lục, làm phiến lá chuyển màu vàng úa gọi là bệnh chlorosis, kéo tụt tốc độ quang hợp."
    },
    {
        "id": "sec_leaf_structure",
        "title": "3. Cấu tạo Bên trong của Lá (Internal Leaf Structure)",
        "selector": "#sec-leaf-structure",
        "en": "Section 3: Internal leaf architecture is adapted for maximal light interception and rapid gas exchange across specialized tissue layers.",
        "vi": "Mục 3: Cấu tạo giải phẫu lá thích nghi hoàn hảo để hấp thu tối đa ánh sáng mặt trời và trao đổi khí nhanh chóng qua các lớp mô chuyên hóa."
    },
    {
        "id": "card_cuticle",
        "title": "🛡️ Lớp Sáp Cutin (Waxy Cuticle)",
        "selector": "#card-cuticle",
        "en": "The waxy cuticle is a thin, transparent, waterproof outer layer on both leaf surfaces that prevents excessive evaporation of water by transpiration without blocking incoming sunlight.",
        "vi": "Lớp sáp cutin là một màng mỏng trong suốt, chống thấm nước bao bọc mặt ngoài của lá giúp ngăn chặn sự thoát hơi nước quá mức qua biểu bì mà không cản trở ánh sáng mặt trời chiếu vào."
    },
    {
        "id": "card_epidermis",
        "title": "🔍 Lớp Biểu bì trên (Upper Epidermis)",
        "selector": "#card-epidermis",
        "en": "The upper epidermis consists of a single layer of tightly packed cells without chloroplasts. Being completely transparent, it allows light to pass directly into the underlying photosynthetic palisade mesophyll cells.",
        "vi": "Biểu bì trên gồm một lớp tế bào đơn xếp khít nhau và không chứa lục lạp. Với tính chất trong suốt hoàn toàn, nó cho phép ánh sáng truyền thẳng trực tiếp xuống lớp mô giậu quang hợp bên dưới."
    },
    {
        "id": "card_palisade_leaf",
        "title": "🍃 Tế bào Mô giậu (Palisade Mesophyll)",
        "selector": "#card-palisade-leaf",
        "en": "Palisade mesophyll cells are vertically elongated and packed tightly directly beneath the upper epidermis. They contain the highest concentration of chloroplasts to absorb the maximum possible amount of sunlight for photosynthesis.",
        "vi": "Tế bào mô giậu có dạng hình trụ thuôn dài xếp khít nhau nằm ngay sát biểu bì trên. Chúng chứa mật độ lục lạp đậm đặc nhất trong toàn bộ chiếc lá để hấp thụ tối đa năng lượng ánh sáng cho quang hợp."
    },
    {
        "id": "card_spongy_mesophyll",
        "title": "🧽 Tế bào Mô xốp (Spongy Mesophyll)",
        "selector": "#card-spongy-mesophyll",
        "en": "Spongy mesophyll cells are loosely arranged with large interconnected intercellular air spaces. This creates a vast moist internal surface area facilitating rapid diffusion of carbon dioxide into cells and oxygen out.",
        "vi": "Tế bào mô xốp sắp xếp lỏng lẻo với các khoang gian bào chứa khí rộng lớn liên kết nhau. Cấu trúc này tạo diện tích bề mặt ẩm cực lớn giúp carbon dioxide khuếch tán nhanh vào tế bào và giải phóng khí oxy ra ngoài."
    },
    {
        "id": "card_vascular_bundle",
        "title": "🪵 Bó Mạch Dẫn (Vascular Bundle / Vein)",
        "selector": "#card-vascular-bundle",
        "en": "The vascular bundle contains xylem vessels, which deliver water and dissolved minerals to photosynthetic cells, and phloem tubes, which transport synthesized sucrose and amino acids away to other plant organs.",
        "vi": "Bó mạch dẫn gồm mạch gỗ (xylem) đưa nước và muối khoáng hòa tan đến các tế bào quang hợp, và mạch rây (phloem) vận chuyển đường sucrose và axit amin tạo thành đi nuôi dưỡng các bộ phận khác của cây."
    },
    {
        "id": "card_stomata_guard",
        "title": "👄 Khí khổng & Tế bào Khí khổng (Stomata & Guard Cells)",
        "selector": "#card-stomata-guard",
        "en": "Stomata are microscopic pores predominantly on the lower leaf surface, flanked by pairs of guard cells. In light, guard cells absorb water by osmosis, become turgid, and open the stomatal aperture for gas exchange; in darkness or water stress, they lose turgor and close to prevent wilting.",
        "vi": "Khí khổng là những lỗ thở siêu vi phân bố chủ yếu ở mặt dưới lá, bao quanh bởi cặp tế bào hình hạt đậu. Khi có ánh sáng, tế bào khí khổng hút nước trương phình mở lỗ khí để trao đổi khí; khi tối hoặc hạn hán, chúng mất nước xẹp lại đóng lỗ khí để chống mất nước."
    },
    {
        "id": "sec_photosynthesis_experiments",
        "title": "🥽 4. Thí nghiệm Thực hành Quang hợp (Paper 6 Focus)",
        "selector": "#sec-photosynthesis-experiments",
        "en": "Section 4 covers practical investigations: Testing a leaf for starch requires de-starching, boiling in water to break membranes, boiling in ethanol in a water bath to remove green chlorophyll, softening in warm water, and adding yellow-brown iodine solution.",
        "vi": "Mục 4 trình bày các thí nghiệm thực hành trọng tâm: Quy trình kiểm tra tinh bột ở lá bắt buộc phải khử tinh bột, đun lá trong nước sôi để phá vỡ màng tế bào, đun trong cồn cách thủy để tẩy sạch sắc tố diệp lục, ngâm nước ấm làm mềm và nhỏ dung dịch I-ốt nâu vàng."
    },
    {
        "id": "card_destarching",
        "title": "🛑 Khử Tinh bột (De-starching Protocol)",
        "selector": "#card-destarching",
        "en": "De-starching: Before photosynthesis experiments, potted plants must be kept in complete darkness for at least 48 hours. This ensures that any starch present in the leaf before the investigation is completely metabolized, proving that any new starch detected was produced during the experiment.",
        "vi": "Khử tinh bột: Trước khi làm thí nghiệm quang hợp, chậu cây phải được đặt trong bóng tối hoàn toàn ít nhất 48 giờ. Việc này đảm bảo toàn bộ lượng tinh bột có sẵn trong lá bị phân giải hết, chứng minh rằng bất kỳ lượng tinh bột nào phát hiện sau đó đều do quang hợp mới sinh ra."
    },
    {
        "id": "card_starch_test",
        "title": "🧪 Quy trình 4 Bước Thử Tinh bột trên Lá",
        "selector": "#card-starch-test",
        "en": "The 4-step starch test: First, boil the leaf in water for one minute to denature enzymes and kill the cells. Second, boil in ethanol using an electric water bath—never an open flame due to fire hazard—to dissolve green chlorophyll. Third, rinse in warm water to soften the brittle leaf. Fourth, spread on a white tile and add drops of iodine solution; blue-black confirms starch.",
        "vi": "Quy trình 4 bước thử tinh bột: Bước 1, nhúng lá vào nước sôi 1 phút để diệt tế bào và phá hủy màng. Bước 2, đun trong cồn ethanol bằng nồi cách thủy điện (tuyệt đối không dùng ngọn lửa hở vì cồn dễ cháy) để hòa tan diệp lục. Bước 3, nhúng lại vào nước ấm để làm mềm phiến lá giòn. Bước 4, trải lên đĩa sứ trắng và nhỏ dung dịch I-ốt; màu xanh đen xác nhận có tinh bột."
    },
    {
        "id": "card_elodea_experiment",
        "title": "🌿 Thí nghiệm Cây Rong đuôi chồn Elodea",
        "selector": "#card-elodea-experiment",
        "en": "Aquatic plant investigation: An inverted Elodea shoot is submerged in sodium hydrogencarbonate solution. As it photosynthesizes, oxygen gas bubbles are released from the cut stem. Measuring bubbles per minute or collecting oxygen volume in a gas syringe quantifies photosynthetic rate.",
        "vi": "Thí nghiệm cây thủy sinh Elodea: Cành rong đuôi chồn được cắm ngược trong dung dịch natri hydrogencarbonate. Khi quang hợp, các bọt khí oxy thoát ra từ vết cắt của thân. Đếm số bọt khí mỗi phút hoặc thu thể tích oxy bằng ống tiêm đo lường trực tiếp tốc độ quang hợp."
    },
    {
        "id": "card_hydrogencarbonate",
        "title": "🌈 Dung dịch Chỉ thị Hydrogencarbonate",
        "selector": "#card-hydrogencarbonate",
        "en": "Hydrogencarbonate indicator reveals carbon dioxide levels: It is orange-red at normal atmospheric levels. In the light, photosynthesis exceeds respiration, consuming CO2 and turning the indicator purple. In the dark, only respiration occurs, producing CO2 and turning the indicator yellow.",
        "vi": "Dung dịch chỉ thị hydrogencarbonate phản ánh nồng độ CO2: Màu đỏ cam ở nồng độ khí quyển bình thường. Khi có ánh sáng, quang hợp mạnh hơn hô hấp tiêu thụ bớt CO2 làm chỉ thị đổi màu tím. Trong bóng tối, chỉ có hô hấp thải thêm CO2 làm chỉ thị chuyển sang màu vàng."
    },
    {
        "id": "sec_limiting_factors",
        "title": "📈 5. Các Yếu tố Giới hạn Tốc độ Quang hợp",
        "selector": "#sec-limiting-factors",
        "en": "Section 5: A limiting factor is something present in the environment in such short supply that it restricts life processes. The three primary limiting factors of photosynthesis are light intensity, carbon dioxide concentration, and temperature.",
        "vi": "Mục 5: Yếu tố giới hạn là một yếu tố môi trường ở mức thấp đến mức hạn chế tốc độ của quá trình sinh lý. Ba yếu tố giới hạn chính của quang hợp gồm cường độ ánh sáng, nồng độ khí carbon dioxide và nhiệt độ môi trường."
    }
]

T6_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_photosynthesis": {"start": 1, "end": 2},
    "sec-photosynthesis": {"start": 1, "end": 2},
    "sec_minerals": {"start": 3, "end": 5},
    "sec-minerals": {"start": 3, "end": 5},
    "sec_leaf_structure": {"start": 6, "end": 12},
    "sec-leaf-structure": {"start": 6, "end": 12},
    "sec_photosynthesis_experiments": {"start": 13, "end": 17},
    "sec-photosynthesis-experiments": {"start": 13, "end": 17},
    "sec_limiting_factors": {"start": 18, "end": 18},
    "sec-limiting-factors": {"start": 18, "end": 18}
}

def transform_topic6_html():
    with open('scripts/raw_bio_topics/t6_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t6_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 6: Plant Nutrition</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Photosynthesis Equation, Minerals, Leaf Structure, Starch Practicals &amp; Limiting Factors</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 6: Dinh dưỡng Thực vật &amp; Quang hợp</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Phương trình quang hợp, Khoáng chất, Giải phẫu lá, Thực hành Paper 6 &amp; Yếu tố giới hạn</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🌱 1. THE EQUATION OF PHOTOSYNTHESIS<', ' id="sec-photosynthesis" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis">🌱 1. THE EQUATION OF PHOTOSYNTHESIS<')
    p1 = p1.replace('>🔄 What happens to the Glucose?<', ' id="card-glucose-fate" class="lecture-interactive-card" data-lecture-section="card_glucose_fate">🔄 What happens to the Glucose?<')
    p1 = p1.replace('>⚠️ 2. MINERAL REQUIREMENTS<', ' id="sec-minerals" class="lecture-interactive-card" data-lecture-section="sec_minerals">⚠️ 2. MINERAL REQUIREMENTS<')
    p1 = p1.replace('>🔵 Nitrate Ions (NO₃⁻)<', ' id="card-nitrates" class="lecture-interactive-card" data-lecture-section="card_nitrates">🔵 Nitrate Ions (NO₃⁻)<')
    p1 = p1.replace('>🟢 Magnesium Ions (Mg²⁺)<', ' id="card-magnesium" class="lecture-interactive-card" data-lecture-section="card_magnesium">🟢 Magnesium Ions (Mg²⁺)<')
    p1 = p1.replace('>🔬 3. INTERNAL LEAF STRUCTURE<', ' id="sec-leaf-structure" class="lecture-interactive-card" data-lecture-section="sec_leaf_structure">🔬 3. INTERNAL LEAF STRUCTURE<')
    p1 = p1.replace('>1. Waxy Cuticle<', ' id="card-cuticle" class="lecture-interactive-card" data-lecture-section="card_cuticle">1. Waxy Cuticle<')
    p1 = p1.replace('>2. Upper Epidermis<', ' id="card-epidermis" class="lecture-interactive-card" data-lecture-section="card_epidermis">2. Upper Epidermis<')
    p1 = p1.replace('>3. Palisade Mesophyll<', ' id="card-palisade-leaf" class="lecture-interactive-card" data-lecture-section="card_palisade_leaf">3. Palisade Mesophyll<')
    p1 = p1.replace('>4. Spongy Mesophyll<', ' id="card-spongy-mesophyll" class="lecture-interactive-card" data-lecture-section="card_spongy_mesophyll">4. Spongy Mesophyll<')
    p1 = p1.replace('>5. Vascular Bundle (Vein)<', ' id="card-vascular-bundle" class="lecture-interactive-card" data-lecture-section="card_vascular_bundle">5. Vascular Bundle (Vein)<')
    p1 = p1.replace('>6. Stomata &amp; Guard Cells<', ' id="card-stomata-guard" class="lecture-interactive-card" data-lecture-section="card_stomata_guard">6. Stomata &amp; Guard Cells<')
    p1 = p1.replace('>🥽 4. PAPER 6: INVESTIGATING PHOTOSYNTHESIS<', ' id="sec-photosynthesis-experiments" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis_experiments">🥽 4. PAPER 6: INVESTIGATING PHOTOSYNTHESIS<')
    p1 = p1.replace('>🛑 Essential First Step: De-starching<', ' id="card-destarching" class="lecture-interactive-card" data-lecture-section="card_destarching">🛑 Essential First Step: De-starching<')
    p1 = p1.replace('>🧪 The 4-Step Leaf Starch Test Protocol (Paper 6 Focus)<', ' id="card-starch-test" class="lecture-interactive-card" data-lecture-section="card_starch_test">🧪 The 4-Step Leaf Starch Test Protocol (Paper 6 Focus)<')
    p1 = p1.replace('>🧪 4. Aquatic Plant (Elodea) Photosynthesis Rate Investigation (Paper 6 Core)<', ' id="card-elodea-experiment" class="lecture-interactive-card" data-lecture-section="card_elodea_experiment">🧪 4. Aquatic Plant (Elodea) Photosynthesis Rate Investigation (Paper 6 Core)<')
    p1 = p1.replace('>🌈 5. Hydrogencarbonate Indicator &amp; Gas Exchange (Light vs Dark)<', ' id="card-hydrogencarbonate" class="lecture-interactive-card" data-lecture-section="card_hydrogencarbonate">🌈 5. Hydrogencarbonate Indicator &amp; Gas Exchange (Light vs Dark)<')
    p1 = p1.replace('>📈 6. LIMITING FACTORS<', ' id="sec-limiting-factors" class="lecture-interactive-card" data-lecture-section="sec_limiting_factors">📈 6. LIMITING FACTORS<')

    # P2 replacements
    p2 = p2.replace('>🌱 1. THE EQUATION OF PHOTOSYNTHESIS<', ' id="sec-photosynthesis" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis">🌱 1. THE EQUATION OF PHOTOSYNTHESIS<')
    p2 = p2.replace('>🔄 What happens to the Glucose? (Số phận của Glucose)<', ' id="card-glucose-fate" class="lecture-interactive-card" data-lecture-section="card_glucose_fate">🔄 What happens to the Glucose? (Số phận của Glucose)<')
    p2 = p2.replace('>⚠️ 2. MINERAL REQUIREMENTS (Nhu cầu Khoáng)<', ' id="sec-minerals" class="lecture-interactive-card" data-lecture-section="sec_minerals">⚠️ 2. MINERAL REQUIREMENTS (Nhu cầu Khoáng)<')
    p2 = p2.replace('>🔵 Nitrate Ions (NO₃⁻)<', ' id="card-nitrates" class="lecture-interactive-card" data-lecture-section="card_nitrates">🔵 Nitrate Ions (NO₃⁻)<')
    p2 = p2.replace('>🟢 Magnesium Ions (Mg²⁺)<', ' id="card-magnesium" class="lecture-interactive-card" data-lecture-section="card_magnesium">🟢 Magnesium Ions (Mg²⁺)<')
    p2 = p2.replace('>🔬 3. INTERNAL LEAF STRUCTURE (Bản đồ Cấu tạo Lá)<', ' id="sec-leaf-structure" class="lecture-interactive-card" data-lecture-section="sec_leaf_structure">🔬 3. INTERNAL LEAF STRUCTURE (Bản đồ Cấu tạo Lá)<')
    p2 = p2.replace('>1. Waxy Cuticle (Lớp sáp cutin)<', ' id="card-cuticle" class="lecture-interactive-card" data-lecture-section="card_cuticle">1. Waxy Cuticle (Lớp sáp cutin)<')
    p2 = p2.replace('>2. Upper Epidermis (Biểu bì trên)<', ' id="card-epidermis" class="lecture-interactive-card" data-lecture-section="card_epidermis">2. Upper Epidermis (Biểu bì trên)<')
    p2 = p2.replace('>3. Palisade Mesophyll (Mô giậu)<', ' id="card-palisade-leaf" class="lecture-interactive-card" data-lecture-section="card_palisade_leaf">3. Palisade Mesophyll (Mô giậu)<')
    p2 = p2.replace('>4. Spongy Mesophyll (Mô xốp)<', ' id="card-spongy-mesophyll" class="lecture-interactive-card" data-lecture-section="card_spongy_mesophyll">4. Spongy Mesophyll (Mô xốp)<')
    p2 = p2.replace('>5. Vascular Bundle (Gân lá)<', ' id="card-vascular-bundle" class="lecture-interactive-card" data-lecture-section="card_vascular_bundle">5. Vascular Bundle (Gân lá)<')
    p2 = p2.replace('>6. Stomata &amp; Guard Cells (Khí khổng)<', ' id="card-stomata-guard" class="lecture-interactive-card" data-lecture-section="card_stomata_guard">6. Stomata &amp; Guard Cells (Khí khổng)<')
    p2 = p2.replace('>🥽 4. PAPER 6: INVESTIGATING PHOTOSYNTHESIS<', ' id="sec-photosynthesis-experiments" class="lecture-interactive-card" data-lecture-section="sec_photosynthesis_experiments">🥽 4. PAPER 6: INVESTIGATING PHOTOSYNTHESIS<')
    p2 = p2.replace('>🛑 Bước BẮT BUỘC: De-starching (Khử tinh bột)<', ' id="card-destarching" class="lecture-interactive-card" data-lecture-section="card_destarching">🛑 Bước BẮT BUỘC: De-starching (Khử tinh bột)<')
    p2 = p2.replace('>🧪 Các bước Test Tinh bột trên lá (Thường chiếm 4-5 điểm)<', ' id="card-starch-test" class="lecture-interactive-card" data-lecture-section="card_starch_test">🧪 Các bước Test Tinh bột trên lá (Thường chiếm 4-5 điểm)<')
    p2 = p2.replace('>🧪 4. Aquatic Plant (Elodea) Photosynthesis Rate Investigation', ' id="card-elodea-experiment" class="lecture-interactive-card" data-lecture-section="card_elodea_experiment">🧪 4. Aquatic Plant (Elodea) Photosynthesis Rate Investigation')
    p2 = p2.replace('>🌈 5. Hydrogencarbonate Indicator', ' id="card-hydrogencarbonate" class="lecture-interactive-card" data-lecture-section="card_hydrogencarbonate">🌈 5. Hydrogencarbonate Indicator')
    p2 = p2.replace('>📈 6. LIMITING FACTORS', ' id="sec-limiting-factors" class="lecture-interactive-card" data-lecture-section="sec_limiting_factors">📈 6. LIMITING FACTORS')

    # Div balance
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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 6 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 6 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 7: Human nutrition
# ==============================================================================
T7_ID = '85f36013-879b-49a8-a531-69c245a9630e'
T7_CODE = '7'
T7_TITLE = 'Topic 7: Human nutrition'

T7_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 7: Dinh dưỡng ở Người & Hệ Tiêu hóa",
        "selector": "#sec-header",
        "en": "Welcome to Topic 7: Human Nutrition. Heterotrophic human nutrition involves ingesting organic macromolecules, mechanically and chemically breaking them down, absorbing nutrients into blood, assimilating them into tissues, and egesting undigested wastes. In this lesson, we study balanced diets, malnutrition diseases, dental anatomy, alimentary canal organs, digestive enzymes, and villi absorption adaptations.",
        "vi": "Chào mừng các bạn đến với Bài 7: Dinh dưỡng ở Người & Hệ Tiêu hóa. Dinh dưỡng dị dưỡng ở người bao gồm việc lấy thức ăn, biến đổi cơ học và hóa học, hấp thụ chất dinh dưỡng vào máu, đồng hóa vào mô và thải bỏ chất cặn bã. Trong bài học này, chúng ta sẽ học về chế độ ăn cân bằng, bệnh suy dinh dưỡng, giải phẫu răng, các cơ quan tiêu hóa, enzyme tiêu hóa và cấu tạo lông ruột thích nghi cho hấp thụ."
    },
    {
        "id": "sec_balanced_diet",
        "title": "1. Chế độ Ăn Cân bằng & 7 Nhóm Dinh dưỡng",
        "selector": "#sec-balanced-diet",
        "en": "Section 1: A balanced diet contains all seven essential dietary components in correct proportions: carbohydrates, fats, proteins, vitamins, minerals, water, and dietary fibre.",
        "vi": "Mục 1: Chế độ ăn cân bằng chứa đầy đủ 7 nhóm dưỡng chất thiết yếu theo tỷ lệ cân đối: carbohydrate, chất béo, protein, vitamin, khoáng chất, nước và chất xơ."
    },
    {
        "id": "card_diet_carbs_fats_protein",
        "title": "🍞 Carbohydrates, Chất béo & Protein",
        "selector": "#card-diet-carbs-fats-protein",
        "en": "Macronutrients: Carbohydrates supply fast cellular energy. Lipids provide high-density long-term energy storage and insulation. Proteins provide amino acid building blocks for cellular growth and tissue repair.",
        "vi": "Đại dưỡng chất: Carbohydrate cung cấp năng lượng nhanh cho hoạt động tế bào. Lipid dự trữ năng lượng dài hạn đậm đặc và cách nhiệt. Protein cung cấp các axit amin làm vật liệu kiến tạo để sinh trưởng tế bào và phục hồi mô tổn thương."
    },
    {
        "id": "card_diet_water_fibre",
        "title": "💧 Nước & 🥬 Chất xơ (Roughage)",
        "selector": "#card-diet-water-fibre",
        "en": "Water and Dietary Fibre: Water provides the aqueous solvent for metabolic reactions and circulatory transport. Insoluble cellulose fibre provides bulk for intestinal muscles to push against during peristalsis, preventing constipation and bowel disorders.",
        "vi": "Nước và Chất xơ: Nước tạo môi trường dung môi cho các phản ứng sinh hóa và vận chuyển tuần hoàn. Chất xơ cellulose không tan tạo khối bã để cơ thành ruột co bóp trong nhu động ruột (peristalsis), phòng chống táo bón và các bệnh lý đường ruột."
    },
    {
        "id": "card_vitamins_minerals",
        "title": "💊 Vitamin & Khoáng chất Thiết yếu",
        "selector": "#card-vitamins-minerals",
        "en": "Micronutrients: Vitamin C forms collagen protein; deficiency causes scurvy with bleeding gums. Vitamin D and Calcium strengthen bones and teeth; deficiency causes rickets. Iron synthesizes haemoglobin; deficiency causes anaemia.",
        "vi": "Vi chất dinh dưỡng: Vitamin C giúp tổng hợp collagen; thiếu hụt gây bệnh scorbut chảy máu chân răng. Vitamin D và Canxi làm xương và răng chắc khỏe; thiếu hụt gây bệnh còi xương (rickets). Sắt tổng hợp huyết sắc tố hemoglobin; thiếu sắt gây bệnh thiếu máu (anaemia)."
    },
    {
        "id": "card_malnutrition",
        "title": "⚠️ Suy dinh dưỡng Nặng: Kwashiorkor & Marasmus",
        "selector": "#card-malnutrition",
        "en": "Severe Malnutrition: Kwashiorkor is caused by severe protein deficiency, characterized by fluid accumulation in abdominal tissues causing oedema. Marasmus is caused by total calorie starvation, characterized by extreme muscle and fat wasting.",
        "vi": "Suy dinh dưỡng thể nặng: Kwashiorkor do thiếu hụt protein trầm trọng, biểu hiện đặc trưng là ứ dịch gây phù thũng bụng (oedema). Marasmus do thiếu hụt toàn bộ năng lượng calo, biểu hiện là teo cơ và mất hoàn toàn mô mỡ dưới da."
    },
    {
        "id": "sec_digestive_processes",
        "title": "2. 5 Giai đoạn của Quá trình Tiêu hóa",
        "selector": "#sec-digestive-processes",
        "en": "Section 2 outlines the five digestive stages: Ingestion is taking substances into the body through the mouth. Digestion breaks down large insoluble food molecules into small water-soluble molecules. Absorption moves digested food molecules through the intestinal wall into the blood. Assimilation incorporates absorbed food into body cells. Egestion passes out undigested food as faeces through the anus.",
        "vi": "Mục 2 phác thảo 5 giai đoạn tiêu hóa: Ăn (Ingestion) là đưa thức ăn vào miệng. Tiêu hóa (Digestion) phân giải phân tử lớn khó tan thành phân tử nhỏ tan được. Hấp thụ (Absorption) đưa chất tan qua thành ruột vào máu. Đồng hóa (Assimilation) đưa dưỡng chất vào tế bào cơ thể để sử dụng. Thải bã (Egestion) tống cặn bã không tiêu hóa ra ngoài qua hậu môn dưới dạng phân."
    },
    {
        "id": "sec_teeth",
        "title": "3. Răng và Tiêu hóa Cơ học (Types of Teeth)",
        "selector": "#sec-teeth",
        "en": "Section 3 examines dentition: Humans possess incisors for biting, canines for tearing, and premolars and molars with broad ridged surfaces for chewing and grinding food to increase surface area for enzyme action.",
        "vi": "Mục 3 nghiên cứu về bộ răng: Răng cửa dùng để cắn, răng nanh dùng để xé, răng tiền hàm và răng hàm có mặt nhai rộng có gờ dùng để nhai và nghiền nát thức ăn, giúp gia tăng tối đa diện tích bề mặt cho enzyme tiêu hóa tác dụng."
    },
    {
        "id": "card_tooth_structure",
        "title": "🦷 Cấu trúc Giải phẫu của Răng",
        "selector": "#card-tooth-structure",
        "en": "Internal tooth anatomy: The crown is protected by extremely hard enamel overlying softer bone-like dentine. The inner pulp cavity contains sensitive nerve endings and blood capillaries supplying living cells with nutrients. The root is cemented firmly into the jawbone by cement and periodontal fibers.",
        "vi": "Giải phẫu răng bên trong: Thân răng bọc bởi lớp men răng (enamel) cực cứng, bên dưới là lớp ngà răng (dentine) mềm hơn. Tủy răng (pulp cavity) ở giữa chứa đầu dây thần kinh cảm giác và mao mạch máu nuôi tế bào sống. Chân răng được cố định vững chắc vào xương hàm nhờ lớp cement và dây chằng nha chu."
    },
    {
        "id": "card_dental_decay",
        "title": "⚠️ Sâu Răng & Biện pháp Chăm sóc (Tooth Decay)",
        "selector": "#card-dental_decay",
        "en": "Tooth decay pathogenesis: Bacteria feeding on sugary food residues produce acidic metabolic by-products. This acid dissolves calcium phosphate in the protective enamel and dentine, creating cavities that expose nerve endings in the pulp cavity, causing toothache.",
        "vi": "Cơ chế sâu răng: Vi khuẩn trong mảng bám lên men đường dư thừa sinh ra axit. Axit này hòa tan canxi photphat làm mòn lớp men và ngà răng, tạo lỗ sâu ăn sâu vào tủy răng kích thích dây thần kinh gây đau nhức buốt."
    },
    {
        "id": "sec_digestive_organs",
        "title": "4. Các Cơ quan trong Hệ Tiêu hóa (Alimentary Canal)",
        "selector": "#sec-digestive-organs",
        "en": "Section 4 traces food through the alimentary canal: Mouth and salivary glands, bolus transport through oesophagus by peristalsis, protein churning in acidic stomach hydrochloric acid, neutralization and lipid emulsification by liver bile in duodenum, enzyme hydrolysis, nutrient absorption in ileum, water reabsorption in colon, and faecal storage in rectum.",
        "vi": "Mục 4 theo dõi hành trình thức ăn qua ống tiêu hóa: Khoang miệng và tuyến nước bọt, viên thức ăn di chuyển qua thực quản nhờ nhu động, nhào trộn và tiêu hóa protein trong dạ dày chứa axit HCl, trung hòa và nhũ hóa chất béo nhờ dịch mật từ gan ở tá tràng, enzyme phân giải, hấp thu tại ruột non, tái hấp thu nước ở đại tràng và tích trữ phân ở trực tràng."
    },
    {
        "id": "sec_chemical_digestion",
        "title": "5. Tiêu hóa Hóa học & Các Enzyme Tiêu hóa",
        "selector": "#sec-chemical-digestion",
        "en": "Section 5 details enzyme chemistry: Amylase breaks starch into maltose; maltase cleaves maltose into glucose. Proteases include pepsin in acidic stomach and trypsin in alkaline duodenum, breaking proteins into peptides and amino acids. Lipase digests emulsified fats into fatty acids and glycerol. Bile from the liver emulsifies large fat globules into tiny droplets to increase surface area.",
        "vi": "Mục 5 trình bày chi tiết hóa học enzyme: Amylase phân giải tinh bột thành maltose; maltase cắt maltose thành glucose. Protease gồm pepsin trong môi trường axit dạ dày và trypsin trong môi trường kiềm tá tràng, cắt protein thành peptide và axit amin. Lipase tiêu hóa chất béo đã nhũ hóa thành axit béo và glycerol. Dịch mật nhũ hóa giọt mỡ lớn thành hàng triệu giọt li ti để tăng diện tích bề mặt."
    },
    {
        "id": "sec_absorption_villi",
        "title": "6. Hấp thụ và Cấu tạo Thích nghi của Lông ruột (Villi)",
        "selector": "#sec-absorption-villi",
        "en": "Section 6 examines villi adaptations: The small intestine lining is folded into millions of finger-like villi with microvilli, expanding absorption surface area thousands of times. Each villus has a thin one-cell-thick epithelium for short diffusion distance, a dense capillary network absorbing glucose and amino acids, and a central lacteal absorbing fatty acids and glycerol.",
        "vi": "Mục 6 khảo sát các đặc điểm thích nghi của lông ruột: Niêm mạc ruột non gấp nếp thành hàng triệu nhung mao (villi) và vi nhung mao (microvilli), mở rộng diện tích tiếp xúc hấp thụ gấp hàng ngàn lần. Mỗi lông ruột có lớp biểu mô mỏng chỉ dày một lớp tế bào giúp rút ngắn khoảng cách khuếch tán, mạng lưới mao mạch dày đặc hấp thu glucose và axit amin, cùng mạch dưỡng chấp trung tâm (lacteal) chuyên hấp thu axit béo và glycerol."
    }
]

T7_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_balanced_diet": {"start": 1, "end": 5},
    "sec-balanced-diet": {"start": 1, "end": 5},
    "sec_digestive_processes": {"start": 6, "end": 6},
    "sec-digestive-processes": {"start": 6, "end": 6},
    "sec_teeth": {"start": 7, "end": 9},
    "sec-teeth": {"start": 7, "end": 9},
    "sec_digestive_organs": {"start": 10, "end": 10},
    "sec-digestive-organs": {"start": 10, "end": 10},
    "sec_chemical_digestion": {"start": 11, "end": 11},
    "sec-chemical-digestion": {"start": 11, "end": 11},
    "sec_absorption_villi": {"start": 12, "end": 12},
    "sec-absorption-villi": {"start": 12, "end": 12}
}

def transform_topic7_html():
    with open('scripts/raw_bio_topics/t7_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t7_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 7: Human Nutrition</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Balanced Diet, Malnutrition, Teeth, Alimentary Canal, Chemical Digestion &amp; Villi Absorption</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 7: Dinh dưỡng ở Người &amp; Hệ Tiêu hóa</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Chế độ ăn cân bằng, Bệnh suy dinh dưỡng, Răng, Ống tiêu hóa, Enzyme &amp; Hấp thụ lông ruột</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🥩 1. NUTRIENTS &amp; A BALANCED DIET<', ' id="sec-balanced-diet" class="lecture-interactive-card" data-lecture-section="sec_balanced_diet">🥩 1. NUTRIENTS &amp; A BALANCED DIET<')
    p1 = p1.replace('>🍞 Carbohydrates<', ' id="card-diet-carbs-fats-protein" class="lecture-interactive-card" data-lecture-section="card_diet_carbs_fats_protein">🍞 Carbohydrates<')
    p1 = p1.replace('>🍞 Carbohydrate<', ' id="card-diet-carbs-fats-protein" class="lecture-interactive-card" data-lecture-section="card_diet_carbs_fats_protein">🍞 Carbohydrate<')
    p1 = p1.replace('>💧 Water &amp; 🥬 Fibre<', ' id="card-diet-water-fibre" class="lecture-interactive-card" data-lecture-section="card_diet_water_fibre">💧 Water &amp; 🥬 Fibre<')
    p1 = p1.replace('>💊 Vitamins &amp; Minerals (High-Yield Exam Focus)<', ' id="card-vitamins-minerals" class="lecture-interactive-card" data-lecture-section="card_vitamins_minerals">💊 Vitamins &amp; Minerals (High-Yield Exam Focus)<')
    p1 = p1.replace('>⚠️ Severe Protein-Energy Malnutrition (Syllabus Supplement)<', ' id="card-malnutrition" class="lecture-interactive-card" data-lecture-section="card_malnutrition">⚠️ Severe Protein-Energy Malnutrition (Syllabus Supplement)<')
    p1 = p1.replace('>⚙️ 2. KEY DIGESTIVE PROCESSES<', ' id="sec-digestive-processes" class="lecture-interactive-card" data-lecture-section="sec_digestive_processes">⚙️ 2. KEY DIGESTIVE PROCESSES<')
    p1 = p1.replace('>👄 3. TYPES OF TEETH (Physical Digestion)<', ' id="sec-teeth" class="lecture-interactive-card" data-lecture-section="sec_teeth">👄 3. TYPES OF TEETH (Physical Digestion)<')
    p1 = p1.replace('>🦷 Internal Structure of a Human Tooth<', ' id="card-tooth-structure" class="lecture-interactive-card" data-lecture-section="card_tooth_structure">🦷 Internal Structure of a Human Tooth<')
    p1 = p1.replace('>⚠️ Dental Decay (Tooth Decay) &amp; Care<', ' id="card-dental_decay" class="lecture-interactive-card" data-lecture-section="card_dental_decay">⚠️ Dental Decay (Tooth Decay) &amp; Care<')
    p1 = p1.replace('>🗺️ 4. ORGANS OF THE DIGESTIVE SYSTEM<', ' id="sec-digestive-organs" class="lecture-interactive-card" data-lecture-section="sec_digestive_organs">🗺️ 4. ORGANS OF THE DIGESTIVE SYSTEM<')
    p1 = p1.replace('>🧪 5. CHEMICAL DIGESTION &amp; ENZYMES<', ' id="sec-chemical-digestion" class="lecture-interactive-card" data-lecture-section="sec_chemical_digestion">🧪 5. CHEMICAL DIGESTION &amp; ENZYMES<')
    p1 = p1.replace('>🔬 6. ABSORPTION &amp; ADAPTATIONS OF VILLI<', ' id="sec-absorption-villi" class="lecture-interactive-card" data-lecture-section="sec_absorption_villi">🔬 6. ABSORPTION &amp; ADAPTATIONS OF VILLI<')

    # P2 replacements
    p2 = p2.replace('>🥩 1. NUTRIENTS &amp; A BALANCED DIET<', ' id="sec-balanced-diet" class="lecture-interactive-card" data-lecture-section="sec_balanced_diet">🥩 1. NUTRIENTS &amp; A BALANCED DIET<')
    p2 = p2.replace('>🍞 Carbohydrate<', ' id="card-diet-carbs-fats-protein" class="lecture-interactive-card" data-lecture-section="card_diet_carbs_fats_protein">🍞 Carbohydrate<')
    p2 = p2.replace('>💧 Water &amp; 🥬 Fibre<', ' id="card-diet-water-fibre" class="lecture-interactive-card" data-lecture-section="card_diet_water_fibre">💧 Water &amp; 🥬 Fibre<')
    p2 = p2.replace('>💊 Vitamins &amp; Minerals<', ' id="card-vitamins-minerals" class="lecture-interactive-card" data-lecture-section="card_vitamins_minerals">💊 Vitamins &amp; Minerals<')
    p2 = p2.replace('>⚠️ Suy dinh dưỡng Protein - Năng lượng thể nặng (Protein-Energy Malnutrition)<', ' id="card-malnutrition" class="lecture-interactive-card" data-lecture-section="card_malnutrition">⚠️ Suy dinh dưỡng Protein - Năng lượng thể nặng (Protein-Energy Malnutrition)<')
    p2 = p2.replace('>⚙️ 2. KEY DIGESTIVE PROCESSES<', ' id="sec-digestive-processes" class="lecture-interactive-card" data-lecture-section="sec_digestive_processes">⚙️ 2. KEY DIGESTIVE PROCESSES<')
    p2 = p2.replace('>👄 3. TYPES OF TEETH (Physical Digestion)<', ' id="sec-teeth" class="lecture-interactive-card" data-lecture-section="sec_teeth">👄 3. TYPES OF TEETH (Physical Digestion)<')
    p2 = p2.replace('>🦷 Cấu trúc giải phẫu bên trong của Răng (Internal Structure of Tooth)<', ' id="card-tooth-structure" class="lecture-interactive-card" data-lecture-section="card_tooth_structure">🦷 Cấu trúc giải phẫu bên trong của Răng (Internal Structure of Tooth)<')
    p2 = p2.replace('>⚠️ Sâu răng (Dental Decay) &amp; Biện pháp bảo vệ<', ' id="card-dental_decay" class="lecture-interactive-card" data-lecture-section="card_dental_decay">⚠️ Sâu răng (Dental Decay) &amp; Biện pháp bảo vệ<')
    p2 = p2.replace('>🗺️ 4. ORGANS OF THE DIGESTIVE SYSTEM<', ' id="sec-digestive-organs" class="lecture-interactive-card" data-lecture-section="sec_digestive_organs">🗺️ 4. ORGANS OF THE DIGESTIVE SYSTEM<')
    p2 = p2.replace('>🧪 5. CHEMICAL DIGESTION &amp; ENZYMES (Tiêu hóa hóa học &amp; Enzyme)<', ' id="sec-chemical-digestion" class="lecture-interactive-card" data-lecture-section="sec_chemical_digestion">🧪 5. CHEMICAL DIGESTION &amp; ENZYMES (Tiêu hóa hóa học &amp; Enzyme)<')
    p2 = p2.replace('>🔬 6. ABSORPTION &amp; ADAPTATIONS OF VILLI (Hấp thụ &amp; Cấu tạo Nhung mao)<', ' id="sec-absorption-villi" class="lecture-interactive-card" data-lecture-section="sec_absorption_villi">🔬 6. ABSORPTION &amp; ADAPTATIONS OF VILLI (Hấp thụ &amp; Cấu tạo Nhung mao)<')

    # Div balance
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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 7 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 7 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 8: Transport in plants
# ==============================================================================
T8_ID = '37f08657-58e8-4fad-8035-2d935e1259e8'
T8_CODE = '8'
T8_TITLE = 'Topic 8: Transport in plants'

T8_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 8: Sự Vận chuyển Các chất ở Thực vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic 8: Transport in Plants. Multicellular plants require specialized transport systems: Xylem vessels conduct water and dissolved minerals from roots to leaves in a one-way transpiration stream, while Phloem sieve tubes translocate sucrose and amino acids between sources and sinks. In this lesson, we analyze vascular distribution, water uptake, transpiration mechanisms, potometers, and translocation.",
        "vi": "Chào mừng các bạn đến với Bài 8: Sự Vận chuyển Các chất ở Thực vật. Cây đa bào cần hệ thống vận chuyển chuyên biệt: Mạch gỗ dẫn nước và khoáng hòa tan từ rễ lên lá theo dòng thoát hơi nước một chiều, còn Mạch rây vận chuyển đường sucrose và axit amin giữa cơ quan nguồn và cơ quan chứa. Trong bài học này, chúng ta sẽ khảo sát phân bố bó mạch, sự hút nước, thoát hơi nước, áp kế và dòng mạch rây."
    },
    {
        "id": "sec_vascular_tissues",
        "title": "1. Mô Dẫn: Mạch gỗ (Xylem) & Mạch rây (Phloem)",
        "selector": "#sec-vascular-tissues",
        "en": "Section 1: Vascular tissues: Xylem vessels are non-living hollow tubes reinforced with waterproof lignin that transport water and minerals upward and provide structural support. Phloem sieve tubes are living cells with perforated end sieve plates that transport sucrose and amino acids bidirectionally.",
        "vi": "Mục 1: Các mô dẫn: Mạch gỗ gồm các ống rỗng không có chất nguyên sinh được tẩm lignin chống thấm, vận chuyển nước và muối khoáng một chiều đi lên và nâng đỡ cơ học. Mạch rây gồm các tế bào sống có bản rây thủng lỗ ở hai đầu, vận chuyển đường sucrose và axit amin theo hai chiều."
    },
    {
        "id": "card_xylem_tissue",
        "title": "💧 Mô Mạch Gỗ (Xylem Tissue)",
        "selector": "#card-xylem-tissue",
        "en": "Xylem adaptations: Dead hollow cells joined end-to-end with no end cross-walls create an uninterrupted capillary tube for water flow. Thick lignified walls withstand tension without collapsing under high negative hydrostatic pressure.",
        "vi": "Đặc điểm thích nghi của mạch gỗ: Tế bào chết rỗng ruột nối liền đầu với đầu và tiêu biến vách ngăn ngang tạo thành ống mao dẫn thông suốt cho dòng nước chảy. Thành tế bào dày tẩm lignin chịu được lực căng hút mà không bị xẹp dưới áp suất âm."
    },
    {
        "id": "card_phloem_tissue",
        "title": "🍯 Mô Mạch Rây (Phloem Tissue)",
        "selector": "#card-phloem-tissue",
        "en": "Phloem structure: Composed of sieve tube elements with porous sieve plates allowing flow of sap. Each sieve tube element is supported metabolically by an adjacent companion cell packed with mitochondria supplying ATP.",
        "vi": "Cấu tạo mạch rây: Gồm các tế bào ống rây có các bản rây đục lỗ cho dòng nhựa chảy qua. Mỗi tế bào ống rây được hỗ trợ trao đổi chất bởi một tế bào kèm liền kề chứa nhiều ti thể cung cấp năng lượng ATP."
    },
    {
        "id": "sec_vascular_position",
        "title": "2. Vị trí Mô dẫn ở Rễ, Thân và Lá",
        "selector": "#sec-vascular-position",
        "en": "Section 2: Anatomical positions in dicotyledonous plants: In roots, xylem forms a central cross-shape with phloem between the arms. In stems, vascular bundles form an outer ring with xylem inside and phloem outside. In leaves, xylem lies on top towards the upper surface and phloem below.",
        "vi": "Mục 2: Vị trí giải phẫu mô dẫn ở cây hai lá mầm: Ở rễ, mạch gỗ xếp thành hình chữ X ở chính giữa với mạch rây nằm xen giữa các cánh. Ở thân, các bó mạch xếp thành vòng tròn ngoại vi với mạch gỗ ở trong và mạch rây ở ngoài. Ở lá, mạch gỗ nằm bên trên hướng về mặt trên của lá và mạch rây nằm bên dưới."
    },
    {
        "id": "sec_transpiration",
        "title": "3. Hút nước & Cơ chế Thoát hơi nước (Transpiration)",
        "selector": "#sec-transpiration",
        "en": "Section 3: Transpiration is the loss of water vapour from plant leaves by evaporation of water at the surfaces of mesophyll cells followed by diffusion of water vapour through stomata into the atmosphere.",
        "vi": "Mục 3: Thoát hơi nước là sự mất hơi nước từ lá cây thông qua sự bay hơi nước trên bề mặt các tế bào thịt lá mô xốp, tiếp nối bởi sự khuếch tán của hơi nước qua khí khổng ra ngoài khí quyển."
    },
    {
        "id": "card_water_pathway",
        "title": "🛤️ Con đường Vận chuyển Nước trong Cây",
        "selector": "#card-water-pathway",
        "en": "Pathway of water: Soil water enters root hair cells by osmosis, travels across the root cortex cells by osmosis, enters root xylem, ascends stem xylem, moves into leaf mesophyll cells, evaporates into air spaces, and diffuses out through open stomata.",
        "vi": "Con đường vận chuyển nước: Nước trong đất thẩm thấu vào lông hút rễ, đi qua các tế bào vỏ rễ, vào mạch gỗ của rễ, dâng lên mạch gỗ của thân, đi vào tế bào thịt lá, bay hơi vào khoang gian bào và khuếch tán ra ngoài qua lỗ khí khổng."
    },
    {
        "id": "card_transpiration_pull",
        "title": "💨 Lực Hút Thoát Hơi Nước (Transpiration Pull)",
        "selector": "#card-transpiration-pull",
        "en": "Transpiration pull mechanism: Evaporation lowers water potential in mesophyll cells, creating a tension force that draws water from leaf xylem. Due to cohesion between water molecules and adhesion to xylem walls, an unbroken water column is drawn upward from the roots.",
        "vi": "Cơ chế lực hút thoát hơi nước: Sự bay hơi làm giảm thế nước ở tế bào mô giậu, tạo nên lực căng kéo nước từ mạch gỗ ở lá. Nhờ lực liên kết gắn kết (cohesion) giữa các phân tử nước và lực bám dính (adhesion) vào thành mạch gỗ, cột nước liên tục được kéo thẳng từ rễ lên lá."
    },
    {
        "id": "card_potometer_factors",
        "title": "🌡️ 4 Yếu tố Môi trường & Dụng cụ Áp kế Potometer",
        "selector": "#card-potometer-factors",
        "en": "Factors altering transpiration rate: Rate increases with higher temperature, higher light intensity, and higher wind speed. Rate decreases with higher atmospheric humidity. A potometer measures the rate of water uptake by measuring bubble movement over time.",
        "vi": "Các yếu tố ảnh hưởng tốc độ thoát hơi nước: Tốc độ tăng khi nhiệt độ cao hơn, ánh sáng mạnh hơn và tốc độ gió lớn hơn. Tốc độ giảm khi độ ẩm không khí tăng cao. Dụng cụ áp kế potometer đo tốc độ hút nước bằng cách đo quãng đường bọt khí di chuyển theo thời gian."
    },
    {
        "id": "sec_translocation",
        "title": "4. Vận chuyển Chất hữu cơ: Dòng Mạch rây (Translocation)",
        "selector": "#sec-translocation",
        "en": "Section 4: Translocation is the movement of sucrose and amino acids in phloem from sources to sinks. Sources are regions of production like photosynthesizing leaves. Sinks are regions of utilization or storage like roots, tubers, flowers, and developing fruits.",
        "vi": "Mục 4: Dòng mạch rây (Translocation) là sự vận chuyển đường sucrose và axit amin trong mạch rây từ nguồn (source) đến nơi chứa (sink). Nguồn là cơ quan sản xuất như lá quang hợp. Nơi chứa là cơ quan tiêu thụ hoặc dự trữ như rễ, củ, hoa và quả non."
    },
    {
        "id": "card_source_sink_reversal",
        "title": "🚨 BẪY ĐỀ THI: Sự Đổi Vai giữa Nguồn và Nơi chứa theo Mùa",
        "selector": "#card-source-sink-reversal",
        "en": "Seasonal role reversal: In summer, mature leaves are sources synthesizing sucrose, while underground roots and tubers are sinks storing starch. In early spring before new leaves emerge, underground storage organs act as sources, hydrolyzing starch into sucrose transported upward to growing bud sinks.",
        "vi": "Cảnh báo đổi vai theo mùa: Vào mùa hè, lá trưởng thành là nguồn quang hợp tạo đường, còn rễ và củ dưới đất là nơi chứa tích trữ tinh bột. Vào đầu mùa xuân khi chưa có lá, củ dưới đất đóng vai trò là nguồn, phân giải tinh bột thành đường sucrose vận chuyển ngược lên nuôi chồi non mới mọc."
    }
]

T8_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_vascular_tissues": {"start": 1, "end": 3},
    "sec-vascular-tissues": {"start": 1, "end": 3},
    "sec_vascular_position": {"start": 4, "end": 4},
    "sec-vascular-position": {"start": 4, "end": 4},
    "sec_transpiration": {"start": 5, "end": 8},
    "sec-transpiration": {"start": 5, "end": 8},
    "sec_translocation": {"start": 9, "end": 10},
    "sec-translocation": {"start": 9, "end": 10}
}

def transform_topic8_html():
    with open('scripts/raw_bio_topics/t8_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t8_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 8: Transport in Plants</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Xylem &amp; Phloem, Dicot Anatomy, Water Pathway, Transpiration Pull &amp; Translocation</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 8: Sự Vận chuyển Các chất ở Thực vật</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Mạch gỗ &amp; Mạch rây, Vị trí bó mạch, Con đường hút nước, Thoát hơi nước &amp; Dòng mạch rây</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>💧 1. XYLEM AND PHLOEM (VASCULAR TISSUES)<', ' id="sec-vascular-tissues" class="lecture-interactive-card" data-lecture-section="sec_vascular_tissues">💧 1. XYLEM AND PHLOEM (VASCULAR TISSUES)<')
    p1 = p1.replace('>💧 Xylem Tissue<', ' id="card-xylem-tissue" class="lecture-interactive-card" data-lecture-section="card_xylem_tissue">💧 Xylem Tissue<')
    p1 = p1.replace('>🍯 Phloem Tissue<', ' id="card-phloem-tissue" class="lecture-interactive-card" data-lecture-section="card_phloem_tissue">🍯 Phloem Tissue<')
    p1 = p1.replace('>🗺️ 2. POSITION IN DICOTYLEDONOUS PLANTS<', ' id="sec-vascular-position" class="lecture-interactive-card" data-lecture-section="sec_vascular_position">🗺️ 2. POSITION IN DICOTYLEDONOUS PLANTS<')
    p1 = p1.replace('>🌬️ 3. WATER UPTAKE &amp; TRANSPIRATION<', ' id="sec-transpiration" class="lecture-interactive-card" data-lecture-section="sec_transpiration">🌬️ 3. WATER UPTAKE &amp; TRANSPIRATION<')
    p1 = p1.replace('>🛤️ Pathway of Water Through the Plant (Syllabus Sequence):<', ' id="card-water-pathway" class="lecture-interactive-card" data-lecture-section="card_water_pathway">🛤️ Pathway of Water Through the Plant (Syllabus Sequence):<')
    p1 = p1.replace('>2. The Mechanism of Transpiration &amp; Transpiration Pull<', ' id="card-transpiration-pull" class="lecture-interactive-card" data-lecture-section="card_transpiration_pull">2. The Mechanism of Transpiration &amp; Transpiration Pull<')
    p1 = p1.replace('>3. Factors Affecting Transpiration Rate &amp; The Potometer<', ' id="card-potometer-factors" class="lecture-interactive-card" data-lecture-section="card_potometer_factors">3. Factors Affecting Transpiration Rate &amp; The Potometer<')
    p1 = p1.replace('>🍯 4. TRANSLOCATION (PHLOEM TRANSPORT)<', ' id="sec-translocation" class="lecture-interactive-card" data-lecture-section="sec_translocation">🍯 4. TRANSLOCATION (PHLOEM TRANSPORT)<')
    p1 = p1.replace('>🚨 EXAM TRAP: SEASONAL ROLE REVERSAL OF SOURCES AND SINKS<', ' id="card-source-sink-reversal" class="lecture-interactive-card" data-lecture-section="card_source_sink_reversal">🚨 EXAM TRAP: SEASONAL ROLE REVERSAL OF SOURCES AND SINKS<')

    # P2 replacements
    p2 = p2.replace('>💧 1. XYLEM AND PHLOEM (Mạch gỗ &amp; Mạch rây)<', ' id="sec-vascular-tissues" class="lecture-interactive-card" data-lecture-section="sec_vascular_tissues">💧 1. XYLEM AND PHLOEM (Mạch gỗ &amp; Mạch rây)<')
    p2 = p2.replace('>💧 Xylem Tissue (Mạch Gỗ)<', ' id="card-xylem-tissue" class="lecture-interactive-card" data-lecture-section="card_xylem_tissue">💧 Xylem Tissue (Mạch Gỗ)<')
    p2 = p2.replace('>🍯 Phloem Tissue (Mạch Rây)<', ' id="card-phloem-tissue" class="lecture-interactive-card" data-lecture-section="card_phloem_tissue">🍯 Phloem Tissue (Mạch Rây)<')
    p2 = p2.replace('>🗺️ 2. POSITION IN DICOT PLANTS (Vị trí phân bố)<', ' id="sec-vascular-position" class="lecture-interactive-card" data-lecture-section="sec_vascular_position">🗺️ 2. POSITION IN DICOT PLANTS (Vị trí phân bố)<')
    p2 = p2.replace('>🌬️ 3. TRANSPIRATION (Sự thoát hơi nước)<', ' id="sec-transpiration" class="lecture-interactive-card" data-lecture-section="sec_transpiration">🌬️ 3. TRANSPIRATION (Sự thoát hơi nước)<')
    p2 = p2.replace('>🛤️ Con đường vận chuyển nước (Pathway of Water):<', ' id="card-water-pathway" class="lecture-interactive-card" data-lecture-section="card_water_pathway">🛤️ Con đường vận chuyển nước (Pathway of Water):<')
    p2 = p2.replace('>2. The Process of Transpiration<', ' id="card-transpiration-pull" class="lecture-interactive-card" data-lecture-section="card_transpiration_pull">2. The Process of Transpiration<')
    p2 = p2.replace('>3. Factors Affecting Transpiration (The Potometer)<', ' id="card-potometer-factors" class="lecture-interactive-card" data-lecture-section="card_potometer_factors">3. Factors Affecting Transpiration (The Potometer)<')
    p2 = p2.replace('>🍯 4. TRANSLOCATION (Sự vận chuyển chất hữu cơ)<', ' id="sec-translocation" class="lecture-interactive-card" data-lecture-section="sec_translocation">🍯 4. TRANSLOCATION (Sự vận chuyển chất hữu cơ)<')
    p2 = p2.replace('>🚨 CẢNH BÁO BẪY ĐỀ THI: SỰ ĐỔI VAI THEO MÙA<', ' id="card-source-sink-reversal" class="lecture-interactive-card" data-lecture-section="card_source_sink_reversal">🚨 CẢNH BÁO BẪY ĐỀ THI: SỰ ĐỔI VAI THEO MÙA<')

    # Div balance
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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 8 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 8 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 9: Transport in animals
# ==============================================================================
T9_ID = 'b50dd00a-e2b4-4dba-8b1d-3f679dadae74'
T9_CODE = '9'
T9_TITLE = 'Topic 9: Transport in animals'

T9_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 9: Hệ Tuần hoàn và Máu ở Động vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic 9: Transport in Animals. Complex multicellular animals require a circulatory system consisting of a muscular pump, a closed network of vessels, and circulating blood. In this lesson, we compare single and double circulatory systems, examine mammalian heart anatomy and cardiac cycles, analyze coronary heart disease, contrast blood vessels, and explore blood composition and clotting.",
        "vi": "Chào mừng các bạn đến với Bài 9: Hệ Tuần hoàn và Máu ở Động vật. Động vật đa bào phức tạp cần một hệ tuần hoàn gồm một máy bơm cơ học là tim, mạng lưới mạch máu khép kín và máu tuần hoàn. Trong bài học này, chúng ta sẽ so sánh tuần hoàn đơn và kép, cấu tạo tim và chu kỳ tim, bệnh mạch vành, phân biệt các loại mạch máu, thành phần máu và cơ chế đông máu."
    },
    {
        "id": "sec_circulatory_systems",
        "title": "1. Hệ Tuần hoàn Đơn và Kép (Single vs Double Circulation)",
        "selector": "#sec-circulatory-systems",
        "en": "Section 1: Circulatory system types: Fish have a single circulation where blood passes through the two-chambered heart once per complete circuit. Mammals have a double circulation where blood passes through the four-chambered heart twice—once for the pulmonary circulation to the lungs and once for systemic circulation to body organs.",
        "vi": "Mục 1: Các dạng hệ tuần hoàn: Cá có hệ tuần hoàn đơn, máu chỉ đi qua tim hai ngăn một lần trong một vòng tuần hoàn khép kín. Động vật có vú có hệ tuần hoàn kép, máu đi qua tim bốn ngăn hai lần—một lần qua vòng tuần hoàn phổi và một lần qua vòng tuần hoàn lớn đến toàn bộ cơ quan cơ thể."
    },
    {
        "id": "card_single_double_circulation",
        "title": "🐟 Tuần hoàn Đơn (Cá) vs 🦅 Tuần hoàn Kép (Động vật có vú)",
        "selector": "#card-single-double-circulation",
        "en": "Single vs Double Circulation: Double circulation is advantageous because blood is re-pressurized after passing through delicate lung capillaries, ensuring high-pressure delivery of oxygen and glucose to tissues with high metabolic rates.",
        "vi": "So sánh tuần hoàn đơn vs kép: Tuần hoàn kép có ưu thế vượt trội vì máu được bơm tăng áp trở lại sau khi qua mao mạch phổi mỏng manh, đảm bảo cung cấp oxy và glucose với áp lực cao đến các mô có tốc độ trao đổi chất mạnh mẽ."
    },
    {
        "id": "sec_heart_structure",
        "title": "2. Cấu tạo và Hoạt động của Tim (Heart Anatomy)",
        "selector": "#sec-heart-structure",
        "en": "Section 2: Mammalian heart anatomy: Deoxygenated blood returns via the vena cava into the right atrium, passes through the tricuspid atrioventricular valve into the right ventricle, and is pumped via the pulmonary artery to the lungs. Oxygenated blood returns via pulmonary veins into the left atrium, passes through the bicuspid valve into the left ventricle, and is pumped via the aorta to the body.",
        "vi": "Mục 2: Cấu tạo tim động vật có vú: Máu nghèo oxy theo tĩnh mạch chủ trở về tâm nhĩ phải, qua van ba lá xuống tâm thất phải và được bơm theo động mạch phổi lên phổi. Máu giàu oxy theo tĩnh mạch phổi trở về tâm nhĩ trái, qua van hai lá xuống tâm thất trái và được bơm theo động mạch chủ đi nuôi toàn cơ thể."
    },
    {
        "id": "card_cardiac_cycle",
        "title": "🔄 Chu kỳ Tim & Thành Cơ Tâm Thất Trái",
        "selector": "#card-cardiac-cycle",
        "en": "Ventricular wall thickness and cardiac cycle: The left ventricle has much thicker muscular walls than the right ventricle because it must generate high hydrostatic pressure to pump blood around the entire systemic circulation against high peripheral resistance.",
        "vi": "Độ dày thành tâm thất và chu kỳ tim: Tâm thất trái có thành cơ dày hơn rất nhiều so với tâm thất phải vì nó phải tạo áp suất thủy tĩnh cực lớn để bơm máu đi khắp toàn bộ vòng tuần hoàn lớn thắng sức cản ngoại vi."
    },
    {
        "id": "sec_chd",
        "title": "3. Bệnh Mạch vành (Coronary Heart Disease - CHD)",
        "selector": "#sec-chd",
        "en": "Section 3: Coronary Heart Disease: Coronary arteries supply oxygen and glucose to cardiac muscle tissue. Atherosclerosis narrows these arteries with fatty cholesterol plaques, restricting blood flow and causing angina, thrombosis, and myocardial infarction.",
        "vi": "Mục 3: Bệnh mạch vành: Các động mạch vành cung cấp oxy và glucose cho cơ tim hoạt động. Chứng xơ vữa động mạch làm hẹp lòng mạch bởi các mảng bám cholesterol, cản trở lưu thông máu gây đau thắt ngực, huyết khối và nhồi máu cơ tim."
    },
    {
        "id": "card_chd_stages",
        "title": "⚠️ Tiến trình Bệnh Mạch vành & Yếu tố Nguy cơ",
        "selector": "#card-chd-stages",
        "en": "CHD pathogenesis and risk factors: High-saturated fat diet, smoking, chronic stress, obesity, genetic predisposition, and lack of exercise promote atheroma formation. Prevention includes regular aerobic exercise, smoking cessation, and a low-cholesterol diet.",
        "vi": "Tiến trình bệnh mạch vành và yếu tố nguy cơ: Chế độ ăn nhiều chất béo bão hòa, hút thuốc lá, căng thẳng kéo dài, béo phì, yếu tố di truyền và lười vận động thúc đẩy hình thành mảng xơ vữa. Phòng ngừa bao gồm tập thể dục đều đặn, bỏ thuốc lá và ăn ít cholesterol."
    },
    {
        "id": "sec_blood_vessels",
        "title": "4. Phân biệt Động mạch, Tĩnh mạch và Mao mạch",
        "selector": "#sec-blood-vessels",
        "en": "Section 4: Blood vessels comparison: Arteries carry high-pressure blood away from the heart with thick muscular elastic walls and narrow lumens. Veins carry low-pressure blood back to the heart with thin walls, large lumens, and semilunar valves to prevent backflow. Capillaries connect arterioles to venules with walls only one cell thick for rapid diffusion.",
        "vi": "Mục 4: Phân biệt các loại mạch máu: Động mạch dẫn máu áp lực cao từ tim đi với thành cơ dày đàn hồi và lòng hẹp. Tĩnh mạch dẫn máu áp lực thấp về tim với thành mỏng, lòng rộng và có van bán nguyệt chống trào ngược. Mao mạch nối tiểu động mạch với tiểu tĩnh mạch với thành chỉ dày một lớp tế bào cho khuếch tán nhanh."
    },
    {
        "id": "card_vessels_comparison",
        "title": "🔍 So sánh Cấu tạo: Động mạch vs Tĩnh mạch vs Mao mạch",
        "selector": "#card-vessels-comparison",
        "en": "Vessel structure and function relationships: Arteries expand and recoil with pulse waves. Veins rely on skeletal muscle contraction and internal valves. Capillary beds provide a massive total surface area and extremely short diffusion pathways.",
        "vi": "Mối quan hệ cấu trúc và chức năng: Động mạch giãn nở và co hồi theo nhịp đập của tim. Tĩnh mạch dựa vào sự co bóp của cơ bắp xung quanh và các van một chiều. Mạng mao mạch tạo diện tích bề mặt trao đổi chất khổng lồ và khoảng cách khuếch tán cực ngắn."
    },
    {
        "id": "sec_blood_composition",
        "title": "5. Thành phần Máu & Cơ chế Đông máu",
        "selector": "#sec-blood-composition",
        "en": "Section 5: Blood composition: Plasma transports dissolved nutrients, carbon dioxide, urea, hormones, and heat. Red blood cells transport oxygen. Platelets initiate clotting. White blood cells defend against pathogens.",
        "vi": "Mục 5: Thành phần máu: Huyết tương vận chuyển chất dinh dưỡng hòa tan, CO2, urê, hormone và nhiệt. Hồng cầu vận chuyển oxy. Tiểu cầu kích hoạt đông máu. Bạch cầu bảo vệ cơ thể chống mầm bệnh."
    },
    {
        "id": "card_blood_cells",
        "title": "🛡️ Bạch cầu: Đại thực bào vs Tế bào Lympho",
        "selector": "#card-blood-cells",
        "en": "White blood cells defense: Phagocytes have lobed nuclei and engulf pathogens by phagocytosis, digesting them with enzymes. Lymphocytes have large rounded nuclei and secrete specific complementary antibody proteins that neutralize pathogens or mark them for destruction.",
        "vi": "Bạch cầu phòng thủ: Đại thực bào có nhân phân thùy thực hiện thực bào nuốt vi khuẩn và tiêu hóa bằng enzyme. Tế bào lympho có nhân tròn lớn tiết ra các phân tử kháng thể đặc hiệu khớp với kháng nguyên để vô hiệu hóa mầm bệnh."
    },
    {
        "id": "card_blood_clotting",
        "title": "🩸 Cơ chế Đông Máu (Blood Clotting Cascade)",
        "selector": "#card-blood-clotting",
        "en": "Blood clotting cascade: Damaged tissues and platelets release clotting factors that convert soluble plasma protein fibrinogen into an insoluble mesh of fibrous fibrin threads. Fibrin traps red blood cells and platelets to form a scab, preventing blood loss and pathogen entry.",
        "vi": "Cơ chế đông máu: Mô tổn thương và tiểu cầu giải phóng các yếu tố đông máu giúp chuyển đổi protein hòa tan fibrinogen trong huyết tương thành mạng lưới sợi fibrin không tan. Sợi fibrin giữ chặt các tế bào hồng cầu và tiểu cầu tạo thành cục máu đông và vảy sẹo, ngăn ngừa mất máu và chặn vi khuẩn xâm nhập."
    }
]

T9_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_circulatory_systems": {"start": 1, "end": 2},
    "sec-circulatory-systems": {"start": 1, "end": 2},
    "sec_heart_structure": {"start": 3, "end": 4},
    "sec-heart-structure": {"start": 3, "end": 4},
    "sec_chd": {"start": 5, "end": 6},
    "sec-chd": {"start": 5, "end": 6},
    "sec_blood_vessels": {"start": 7, "end": 8},
    "sec-blood-vessels": {"start": 7, "end": 8},
    "sec_blood_composition": {"start": 9, "end": 11},
    "sec-blood-composition": {"start": 9, "end": 11}
}

def transform_topic9_html():
    with open('scripts/raw_bio_topics/t9_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t9_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 9: Transport in Animals</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Single vs Double Circulation, Heart Anatomy, CHD, Blood Vessels &amp; Clotting Cascade</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 9: Hệ Tuần hoàn và Máu ở Động vật</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Tuần hoàn đơn/kép, Cấu tạo tim, Bệnh mạch vành, Các loại mạch máu &amp; Cơ chế đông máu</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🩸 1. CIRCULATORY SYSTEMS (PUMP, VESSELS &amp; VALVES)<', ' id="sec-circulatory-systems" class="lecture-interactive-card" data-lecture-section="sec_circulatory_systems">🩸 1. CIRCULATORY SYSTEMS (PUMP, VESSELS &amp; VALVES)<')
    p1 = p1.replace('>🐟 Single Circulation (Fish)<', ' id="card-single-double-circulation" class="lecture-interactive-card" data-lecture-section="card_single_double_circulation">🐟 Single Circulation (Fish)<')
    p1 = p1.replace('>❤️ 2. MAMMALIAN HEART STRUCTURE &amp; FUNCTION<', ' id="sec-heart-structure" class="lecture-interactive-card" data-lecture-section="sec_heart_structure">❤️ 2. MAMMALIAN HEART STRUCTURE &amp; FUNCTION<')
    p1 = p1.replace('>🔄 Cardiac Cycle &amp; Valves<', ' id="card-cardiac-cycle" class="lecture-interactive-card" data-lecture-section="card_cardiac_cycle">🔄 Cardiac Cycle &amp; Valves<')
    p1 = p1.replace('>🍔 3. CORONARY HEART DISEASE (CHD)<', ' id="sec-chd" class="lecture-interactive-card" data-lecture-section="sec_chd">🍔 3. CORONARY HEART DISEASE (CHD)<')
    p1 = p1.replace('>1. Healthy Coronary Artery<', ' id="card-chd-stages" class="lecture-interactive-card" data-lecture-section="card_chd_stages">1. Healthy Coronary Artery<')
    p1 = p1.replace('>🧪 4. BLOOD VESSELS (ARTERIES, VEINS, CAPILLARIES)<', ' id="sec-blood-vessels" class="lecture-interactive-card" data-lecture-section="sec_blood_vessels">🧪 4. BLOOD VESSELS (ARTERIES, VEINS, CAPILLARIES)<')
    p1 = p1.replace('>🔴 Arteries<', ' id="card-vessels-comparison" class="lecture-interactive-card" data-lecture-section="card_vessels_comparison">🔴 Arteries<')
    p1 = p1.replace('>🩸 5. BLOOD COMPOSITION &amp; CLOTTING MECHANISM<', ' id="sec-blood-composition" class="lecture-interactive-card" data-lecture-section="sec_blood_composition">🩸 5. BLOOD COMPOSITION &amp; CLOTTING MECHANISM<')
    p1 = p1.replace('>🦠 Phagocytes<', ' id="card-blood-cells" class="lecture-interactive-card" data-lecture-section="card_blood_cells">🦠 Phagocytes<')
    p1 = p1.replace('>🩸 Blood Clotting Cascade (Syllabus Core &amp; Supplement)<', ' id="card-blood-clotting" class="lecture-interactive-card" data-lecture-section="card_blood_clotting">🩸 Blood Clotting Cascade (Syllabus Core &amp; Supplement)<')

    # P2 replacements
    p2 = p2.replace('>🩸 1. CIRCULATORY SYSTEMS (Hệ tuần hoàn)<', ' id="sec-circulatory-systems" class="lecture-interactive-card" data-lecture-section="sec_circulatory_systems">🩸 1. CIRCULATORY SYSTEMS (Hệ tuần hoàn)<')
    p2 = p2.replace('>🐟 Single Circulation (Cá)<', ' id="card-single-double-circulation" class="lecture-interactive-card" data-lecture-section="card_single_double_circulation">🐟 Single Circulation (Cá)<')
    p2 = p2.replace('>❤️ 2. STRUCTURE OF THE HEART (Cấu tạo Tim)<', ' id="sec-heart-structure" class="lecture-interactive-card" data-lecture-section="sec_heart_structure">❤️ 2. STRUCTURE OF THE HEART (Cấu tạo Tim)<')
    p2 = p2.replace('>🔄 Cardiac Cycle (Chu kỳ Tim)<', ' id="card-cardiac-cycle" class="lecture-interactive-card" data-lecture-section="card_cardiac_cycle">🔄 Cardiac Cycle (Chu kỳ Tim)<')
    p2 = p2.replace('>🍔 3. CORONARY HEART DISEASE (Bệnh Mạch vành)<', ' id="sec-chd" class="lecture-interactive-card" data-lecture-section="sec_chd">🍔 3. CORONARY HEART DISEASE (Bệnh Mạch vành)<')
    p2 = p2.replace('>1. Normal Coronary Artery<', ' id="card-chd-stages" class="lecture-interactive-card" data-lecture-section="card_chd_stages">1. Normal Coronary Artery<')
    p2 = p2.replace('>🧪 4. BLOOD VESSELS (Các loại Mạch máu)<', ' id="sec-blood-vessels" class="lecture-interactive-card" data-lecture-section="sec_blood_vessels">🧪 4. BLOOD VESSELS (Các loại Mạch máu)<')
    p2 = p2.replace('>🔴 Arteries (Động mạch)<', ' id="card-vessels-comparison" class="lecture-interactive-card" data-lecture-section="card_vessels_comparison">🔴 Arteries (Động mạch)<')
    p2 = p2.replace('>🩸 5. BLOOD COMPOSITION (Thành phần Máu)<', ' id="sec-blood-composition" class="lecture-interactive-card" data-lecture-section="sec_blood_composition">🩸 5. BLOOD COMPOSITION (Thành phần Máu)<')
    p2 = p2.replace('>🦠 Phagocytes (Đại thực bào)<', ' id="card-blood-cells" class="lecture-interactive-card" data-lecture-section="card_blood_cells">🦠 Phagocytes (Đại thực bào)<')
    p2 = p2.replace('>🩸 Cơ chế đông máu (Blood Clotting)<', ' id="card-blood-clotting" class="lecture-interactive-card" data-lecture-section="card_blood_clotting">🩸 Cơ chế đông máu (Blood Clotting)<')

    # Div balance
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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 9 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 9 P2 div diff != 0"

    return p1, p2

async def build_batch2():
    tasks = [
        ("Topic 6", T6_CODE, T6_ID, T6_TITLE, T6_SEGMENTS, T6_MAJOR_SECTIONS, transform_topic6_html),
        ("Topic 7", T7_CODE, T7_ID, T7_TITLE, T7_SEGMENTS, T7_MAJOR_SECTIONS, transform_topic7_html),
        ("Topic 8", T8_CODE, T8_ID, T8_TITLE, T8_SEGMENTS, T8_MAJOR_SECTIONS, transform_topic8_html),
        ("Topic 9", T9_CODE, T9_ID, T9_TITLE, T9_SEGMENTS, T9_MAJOR_SECTIONS, transform_topic9_html)
    ]
    
    for name, code, lid, title, segs, major, trans_fn in tasks:
        print(f"\n==========================================")
        print(f"STARTING {name}: {title}")
        print(f"==========================================")
        p1_html, p2_html = trans_fn()
        
        # Verify selectors locally before synthesis
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
    asyncio.run(build_batch2())
