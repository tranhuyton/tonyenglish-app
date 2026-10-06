# -*- coding: utf-8 -*-
"""
Batch 3 Builder: Topics 10, 11, 12, 13
- Topic 10: Diseases and immunity
- Topic 11: Gas exchange in humans
- Topic 12: Respiration (Fix P1 div diff +1 -> 0)
- Topic 13: Excretion in humans
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
# TOPIC 10: Diseases and immunity
# ==============================================================================
T10_ID = '62278d87-97ea-4fa5-aa46-748bca28db68'
T10_CODE = '10'
T10_TITLE = 'Topic 10: Diseases and immunity'

T10_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 10: Bệnh tật và Hệ Miễn dịch",
        "selector": "#sec-header",
        "en": "Welcome to Topic 10: Diseases and Immunity. A pathogen is a disease-causing organism, and a transmissible disease can be passed from one host to another. In this lesson, we analyze transmission pathways, mechanical and chemical body barriers, active versus passive immunity, vaccination mechanisms, disease control protocols, and the pathophysiology of cholera.",
        "vi": "Chào mừng các bạn đến với Bài 10: Bệnh tật và Hệ Miễn dịch. Mầm bệnh là sinh vật gây bệnh, và bệnh truyền nhiễm là bệnh có thể lây từ vật chủ này sang vật chủ khác. Trong bài học này, chúng ta sẽ khảo sát các con đường lây truyền, hàng rào cơ học và hóa học bảo vệ cơ thể, miễn dịch chủ động và thụ động, cơ chế tiêm chủng vaccine, kiểm soát dịch bệnh và cơ chế bệnh tả."
    },
    {
        "id": "sec_pathogens",
        "title": "1. Mầm bệnh & Các Con đường Lây truyền (Pathogens)",
        "selector": "#sec-pathogens",
        "en": "Section 1: Pathogens include viruses, bacteria, fungi, and protoctists. Transmissible diseases spread via direct contact—through blood, semen, and other body fluids—or indirect contact—via airborne respiratory droplets, contaminated food and water, domestic surfaces, and animal vectors like mosquitoes.",
        "vi": "Mục 1: Mầm bệnh gồm virus, vi khuẩn, nấm và nguyên sinh vật. Bệnh truyền nhiễm lây qua tiếp xúc trực tiếp—như máu, tinh dịch và dịch cơ thể—hoặc tiếp xúc gián tiếp—như các giọt bắn đường hô hấp trong không khí, thức ăn và nguồn nước nhiễm bẩn, bề mặt sinh hoạt và động vật trung gian truyền bệnh như muỗi."
    },
    {
        "id": "card_transmission_modes",
        "title": "🤝 Tiếp xúc Trực tiếp vs 🌬️ Tiếp xúc Gián tiếp",
        "selector": "#card-transmission-modes",
        "en": "Modes of Transmission: Direct contact involves physical transfer of body fluids from person to person, such as HIV transmission via sexual fluids or blood. Indirect contact occurs without person-to-person touch, including airborne inhalation of flu droplets or ingestion of Salmonella from unwashed raw poultry.",
        "vi": "Các phương thức lây truyền: Tiếp xúc trực tiếp là sự truyền dịch cơ thể từ người sang người, như lây truyền HIV qua đường tình dục hoặc truyền máu. Tiếp xúc gián tiếp không qua va chạm cơ thể, gồm hít phải giọt bắn virus cúm trong không khí hoặc ăn phải vi khuẩn Salmonella từ thịt gia cầm chưa chín."
    },
    {
        "id": "card_antigens_antibodies",
        "title": "👾 Kháng nguyên (Antigen) vs 🛡️ Kháng thể (Antibody)",
        "selector": "#card-antigens-antibodies",
        "en": "Antigens vs Antibodies: An antigen is a distinctive chemical marker on the pathogen's surface with a specific 3D shape. An antibody is a complementary protein molecule produced by lymphocytes that binds specifically to the antigen, clumping or neutralizing the pathogen.",
        "vi": "Kháng nguyên vs Kháng thể: Kháng nguyên (Antigen) là phân tử hóa học đặc trưng trên bề mặt mầm bệnh có hình dạng 3 chiều chuyên biệt. Kháng thể (Antibody) là phân tử protein khớp bổ sung do tế bào lympho tiết ra gắn kết đặc hiệu với kháng nguyên, làm ngưng kết hoặc vô hiệu hóa mầm bệnh."
    },
    {
        "id": "sec_body_defences",
        "title": "2. Các Hàng rào Phòng vệ của Cơ thể (Body Defences)",
        "selector": "#sec-body-defences",
        "en": "Section 2: Body defences operate in three tiers: Mechanical barriers like unbroken skin and nasal hairs; Chemical barriers like acidic stomach hydrochloric acid and antimicrobial mucus; and Cellular defences including phagocytosis by white blood cells.",
        "vi": "Mục 2: Hệ thống phòng ngự của cơ thể gồm ba tầng: Hàng rào cơ học như lớp biểu bì da nguyên vẹn và lông mũi; Hàng rào hóa học như axit HCl diệt khuẩn trong dạ dày và chất nhầy đường hô hấp; và Hàng rào tế bào gồm cơ chế thực bào của các bạch cầu."
    },
    {
        "id": "sec_immunity_vaccines",
        "title": "3. Miễn dịch Chủ động, Thụ động & Cơ chế Vaccine",
        "selector": "#sec-immunity-vaccines",
        "en": "Section 3: Immunity classification: Active immunity is defense acquired by the body producing its own antibodies and memory cells after infection or vaccination, conferring long-term protection. Passive immunity is temporary defense gained from external antibodies without memory cells, such as maternal antibodies across the placenta or breast milk.",
        "vi": "Mục 3: Phân loại miễn dịch: Miễn dịch chủ động là khả năng tự sinh kháng thể và tế bào nhớ sau khi nhiễm bệnh hoặc tiêm vaccine, mang lại khả năng bảo vệ lâu dài. Miễn dịch thụ động là sự bảo vệ tạm thời nhờ nhận kháng thể từ bên ngoài mà không tạo tế bào nhớ, như kháng thể mẹ truyền qua nhau thai hoặc sữa mẹ."
    },
    {
        "id": "card_active_vs_passive",
        "title": "🛡️ Miễn dịch Chủ động vs 🍼 Miễn dịch Thụ động",
        "selector": "#card-active-vs-passive",
        "en": "Active vs Passive comparison: Active immunity is slow to develop initially but provides durable long-lasting memory cells. Passive immunity provides immediate fast-acting protection but is short-lived as foreign antibodies are naturally broken down and no memory cells are created.",
        "vi": "So sánh Chủ động vs Thụ động: Miễn dịch chủ động ban đầu phát triển chậm nhưng bền vững nhờ tế bào trí nhớ miễn dịch. Miễn dịch thụ động mang lại hiệu quả bảo vệ tức thì nhưng ngắn hạn vì kháng thể ngoại sinh sẽ bị cơ thể phân hủy tự nhiên và không sinh ra tế bào nhớ."
    },
    {
        "id": "card_vaccination_process",
        "title": "💉 Cơ chế Hoạt động của Vaccine (Vaccination)",
        "selector": "#card-vaccination-process",
        "en": "Vaccination mechanism: A harmless weakened or dead pathogen, or its isolated surface antigens, is injected. Lymphocytes encounter the antigens and produce complementary antibodies and long-lived memory cells. Upon future natural infection, memory cells rapidly produce large quantities of antibodies to neutralize pathogens before symptoms occur.",
        "vi": "Cơ chế tiêm vaccine: Đưa mầm bệnh đã làm suy yếu, đã chết hoặc kháng nguyên bề mặt vào cơ thể. Tế bào lympho nhận diện kháng nguyên, sản xuất kháng thể tương ứng và tạo ra các tế bào nhớ miễn dịch tồn tại lâu dài. Khi mầm bệnh thật xâm nhập trong tương lai, tế bào nhớ lập tức tiết ồ ạt kháng thể tiêu diệt mầm bệnh trước khi kịp phát bệnh."
    },
    {
        "id": "sec_control_disease",
        "title": "4. Kiểm soát Sự lây lan của Dịch bệnh",
        "selector": "#sec-control-disease",
        "en": "Section 4: Public health hygiene controls disease transmission: Supplying chlorinated drinking water, thorough cooking and refrigeration of food, washing hands with soap, proper solid waste disposal in covered bins, and modern sewage treatment plants to destroy waterborne pathogens.",
        "vi": "Mục 4: Vệ sinh y tế cộng đồng kiểm soát lây lan dịch bệnh: Cung cấp nước sạch tiệt trùng clo, nấu chín kỹ và bảo quản lạnh thực phẩm, rửa tay bằng xà phòng, thu gom rác thải trong thùng có nắp đậy và xây dựng nhà máy xử lý nước thải hiện đại để tiêu diệt mầm bệnh truyền qua đường nước."
    },
    {
        "id": "card_cholera_mechanism",
        "title": "⚠️ 5. Cơ chế Bệnh Tả & Liệu pháp Bù nước ORT",
        "selector": "#card-cholera-mechanism",
        "en": "Cholera pathophysiology: Vibrio cholerae bacteria in the small intestine release a protein toxin. The toxin stimulates epithelial cells to actively secrete chloride ions into the gut lumen. This lowers water potential in the lumen, drawing water from blood by osmosis, causing watery diarrhea, fatal dehydration, and loss of salts, treated effectively with Oral Rehydration Therapy.",
        "vi": "Sinh bệnh học bệnh tả: Vi khuẩn Vibrio cholerae tại ruột non tiết ra độc tố protein. Độc tố kích thích tế bào niêm mạc ruột bài tiết ồ ạt ion clorua vào lòng ruột. Điều này làm giảm thế nước trong lòng ruột, kéo nước từ máu thẩm thấu vào ruột gây tiêu chảy xối xả mất nước nghiêm trọng và mất muối khoáng, điều trị hiệu quả bằng Liệu pháp Bù nước ORT."
    }
]

T10_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_pathogens": {"start": 1, "end": 3},
    "sec-pathogens": {"start": 1, "end": 3},
    "sec_body_defences": {"start": 4, "end": 4},
    "sec-body-defences": {"start": 4, "end": 4},
    "sec_immunity_vaccines": {"start": 5, "end": 7},
    "sec-immunity-vaccines": {"start": 5, "end": 7},
    "sec_control_disease": {"start": 8, "end": 9},
    "sec-control-disease": {"start": 8, "end": 9}
}

def transform_topic10_html():
    with open('scripts/raw_bio_topics/t10_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t10_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 10: Diseases &amp; Immunity</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Pathogens, Body Defences, Antigens vs Antibodies, Vaccines &amp; Cholera Mechanism</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 10: Bệnh tật &amp; Hệ Miễn dịch</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Mầm bệnh, Hàng rào phòng thủ, Kháng nguyên/Kháng thể, Vaccine &amp; Cơ chế Bệnh tả</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🦠 1. PATHOGENS AND TRANSMISSIBLE DISEASES<', ' id="sec-pathogens" class="lecture-interactive-card" data-lecture-section="sec_pathogens">🦠 1. PATHOGENS AND TRANSMISSIBLE DISEASES<')
    p1 = p1.replace('>🤝 Direct Contact<', ' id="card-transmission-modes" class="lecture-interactive-card" data-lecture-section="card_transmission_modes">🤝 Direct Contact<')
    p1 = p1.replace('>👾 Antigen<', ' id="card-antigens-antibodies" class="lecture-interactive-card" data-lecture-section="card_antigens_antibodies">👾 Antigen<')
    p1 = p1.replace('>🛡️ 2. BODY\'S DEFENCE MECHANISMS<', ' id="sec-body-defences" class="lecture-interactive-card" data-lecture-section="sec_body_defences">🛡️ 2. BODY\'S DEFENCE MECHANISMS<')
    p1 = p1.replace('>💉 3. ACTIVE AND PASSIVE IMMUNITY<', ' id="sec-immunity-vaccines" class="lecture-interactive-card" data-lecture-section="sec_immunity_vaccines">💉 3. ACTIVE AND PASSIVE IMMUNITY<')
    p1 = p1.replace('>🛡️ Active Immunity<', ' id="card-active-vs-passive" class="lecture-interactive-card" data-lecture-section="card_active_vs_passive">🛡️ Active Immunity<')
    p1 = p1.replace('>💉 Process of Vaccination<', ' id="card-vaccination-process" class="lecture-interactive-card" data-lecture-section="card_vaccination_process">💉 Process of Vaccination<')
    p1 = p1.replace('>🌍 4. CONTROLLING THE SPREAD OF DISEASE<', ' id="sec-control-disease" class="lecture-interactive-card" data-lecture-section="sec_control_disease">🌍 4. CONTROLLING THE SPREAD OF DISEASE<')
    p1 = p1.replace('>⚠️ 5. CHOLERA MECHANISM', ' id="card-cholera-mechanism" class="lecture-interactive-card" data-lecture-section="card_cholera_mechanism">⚠️ 5. CHOLERA MECHANISM')

    # P2 replacements
    p2 = p2.replace('>🦠 1. PATHOGENS AND TRANSMISSIBLE DISEASES<', ' id="sec-pathogens" class="lecture-interactive-card" data-lecture-section="sec_pathogens">🦠 1. PATHOGENS AND TRANSMISSIBLE DISEASES<')
    p2 = p2.replace('>🤝 Direct Contact (Tiếp xúc trực tiếp)<', ' id="card-transmission-modes" class="lecture-interactive-card" data-lecture-section="card_transmission_modes">🤝 Direct Contact (Tiếp xúc trực tiếp)<')
    p2 = p2.replace('>👾 Antigen (Kháng nguyên)<', ' id="card-antigens-antibodies" class="lecture-interactive-card" data-lecture-section="card_antigens_antibodies">👾 Antigen (Kháng nguyên)<')
    p2 = p2.replace('>🛡️ 2. HÀNG RÀO PHÒNG THỦ CỦA CƠ THỂ (BODY\'S DEFENCES)<', ' id="sec-body-defences" class="lecture-interactive-card" data-lecture-section="sec_body_defences">🛡️ 2. HÀNG RÀO PHÒNG THỦ CỦA CƠ THỂ (BODY\'S DEFENCES)<')
    p2 = p2.replace('>💉 3. ACTIVE AND PASSIVE IMMUNITY (MIỄN DỊCH CHỦ ĐỘNG &amp; THỤ ĐỘNG)<', ' id="sec-immunity-vaccines" class="lecture-interactive-card" data-lecture-section="sec_immunity_vaccines">💉 3. ACTIVE AND PASSIVE IMMUNITY (MIỄN DỊCH CHỦ ĐỘNG &amp; THỤ ĐỘNG)<')
    p2 = p2.replace('>🛡️ Active Immunity (Miễn dịch chủ động)<', ' id="card-active-vs-passive" class="lecture-interactive-card" data-lecture-section="card_active_vs_passive">🛡️ Active Immunity (Miễn dịch chủ động)<')
    p2 = p2.replace('>💉 Cơ chế hoạt động của Vaccine (Process of Vaccination)<', ' id="card-vaccination-process" class="lecture-interactive-card" data-lecture-section="card_vaccination_process">💉 Cơ chế hoạt động của Vaccine (Process of Vaccination)<')
    p2 = p2.replace('>🌍 4. KIỂM SOÁT SỰ LÂY LAN CỦA BỆNH (CONTROLLING THE SPREAD)<', ' id="sec-control-disease" class="lecture-interactive-card" data-lecture-section="sec_control_disease">🌍 4. KIỂM SOÁT SỰ LÂY LAN CỦA BỆNH (CONTROLLING THE SPREAD)<')
    p2 = p2.replace('>⚠️ 5. CƠ CHẾ BỆNH TẢ', ' id="card-cholera-mechanism" class="lecture-interactive-card" data-lecture-section="card_cholera_mechanism">⚠️ 5. CƠ CHẾ BỆNH TẢ')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 10 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 10 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 11: Gas exchange in humans
# ==============================================================================
T11_ID = 'da59c2b3-124f-4e25-8537-74059e74f9b0'
T11_CODE = '11'
T11_TITLE = 'Topic 11: Gas exchange in humans'

T11_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 11: Trao đổi Khí ở Người",
        "selector": "#sec-header",
        "en": "Welcome to Topic 11: Gas Exchange in Humans. Cellular aerobic respiration requires a continuous supply of oxygen and prompt removal of carbon dioxide waste. In this lesson, we examine alveoli adaptations, the anatomy of the respiratory tract, the antagonistic muscle mechanism of breathing, composition differences between inspired and expired air, and brainstem regulation.",
        "vi": "Chào mừng các bạn đến với Bài 11: Trao đổi Khí ở Người. Quá trình hô hấp tế bào đòi hỏi nguồn cung cấp oxy liên tục và loại bỏ kịp thời carbon dioxide độc hại. Trong bài học này, chúng ta sẽ khảo sát đặc điểm phế nang, giải phẫu đường hô hấp, cơ chế đối kháng cơ khi hít thở, so sánh khí hít vào và thở ra, cùng cơ chế điều hòa nhịp thở ở thân não."
    },
    {
        "id": "sec_alveoli_features",
        "title": "1. Đặc điểm Thích nghi của Bề mặt Trao đổi Khí (Phế nang)",
        "selector": "#sec-alveoli-features",
        "en": "Section 1: Alveoli adaptations: Millions of microscopic alveoli provide a massive surface area of over seventy square metres. The alveolar and capillary walls are only one cell thick, creating an extremely thin diffusion pathway. A rich capillary network maintains steep concentration gradients, and ventilation continually replenishes oxygen and removes carbon dioxide.",
        "vi": "Mục 1: Đặc điểm thích nghi của phế nang: Hàng triệu phế nang siêu vi tạo diện tích bề mặt trao đổi khí khổng lồ trên 70 mét vuông. Thành phế nang và mao mạch chỉ dày một lớp tế bào tạo khoảng cách khuếch tán siêu mỏng. Mạng lưới mao mạch phong phú duy trì gradien nồng độ dốc, và cử động thông khí liên tục làm mới oxy và đào thải CO2."
    },
    {
        "id": "sec_respiratory_anatomy",
        "title": "2. Cấu tạo Hệ Hô hấp & Tế bào Lông rung",
        "selector": "#sec-respiratory-anatomy",
        "en": "Section 2: Respiratory tract anatomy: Air flows through nasal cavities, larynx, trachea, bronchi, bronchioles, and terminates in alveoli. C-shaped rings of flexible cartilage prevent the trachea and bronchi from collapsing when thoracic pressure drops during inhalation.",
        "vi": "Mục 2: Cấu tạo đường dẫn khí: Không khí đi qua khoang mũi, thanh quản, khí quản, phế quản, tiểu phế quản và kết thúc tại các phế nang. Các vòng sụn hình chữ C đàn hồi giữ cho khí quản và phế quản không bị xẹp xuống khi áp suất trong lồng ngực hạ thấp trong lúc hít vào."
    },
    {
        "id": "card_ciliated_goblet",
        "title": "🛡️ Tế bào Lông rung & Tế bào Tiết nhầy (Goblet Cells)",
        "selector": "#card-ciliated-goblet",
        "en": "Airway cleansing mechanisms: Goblet cells synthesize and secrete sticky mucus to trap inhaled dust particles, pollen, and bacteria. Epithelial ciliated cells possess microscopic cilia that beat in coordinated rhythmic upward waves, sweeping the dirty mucus up to the pharynx to be swallowed safely into stomach acid.",
        "vi": "Cơ chế làm sạch đường thở: Tế bào hình đài (goblet cells) tiết ra chất nhầy quánh dính để giữ lại hạt bụi, phấn hoa và vi khuẩn. Tế bào biểu mô có lông rung cử động nhịp nhàng như làn sóng hướng lên trên, quét chất nhầy bẩn lên họng để nuốt xuống dạ dày diệt khuẩn bằng axit."
    },
    {
        "id": "sec_ventilation_breathing",
        "title": "3. Cơ chế Thông khí (Hít vào - Thở ra) & Luyện tập",
        "selector": "#sec-ventilation-breathing",
        "en": "Section 3: Mechanics of ventilation: During inhalation, external intercostal muscles contract pulling ribs up and out, while the diaphragm contracts and flattens, expanding thorax volume, decreasing internal pressure below atmospheric, drawing air in. During exhalation, external intercostals and diaphragm relax, ribs drop, thorax volume decreases, pressure rises above atmospheric, forcing air out.",
        "vi": "Mục 3: Cơ chế thông khí: Khi hít vào, cơ liên sườn ngoài co kéo xương sườn lên và ra ngoài, cơ hoành co dẹt xuống làm tăng thể tích lồng ngực, áp suất phổi giảm thấp hơn khí quyển hút không khí vào. Khi thở ra, cơ liên sườn ngoài và cơ hoành giãn, xương sườn hạ xuống, thể tích lồng ngực giảm, áp suất tăng cao hơn khí quyển đẩy khí ra ngoài."
    },
    {
        "id": "card_inspired_expired_comparison",
        "title": "📊 So sánh Thành phần: Khí Hít vào vs Khí Thở ra",
        "selector": "#card-inspired-expired-comparison",
        "en": "Inspired vs Expired air composition: Inspired air contains twenty-one percent oxygen, zero point zero four percent carbon dioxide, and variable humidity. Expired air contains sixteen percent oxygen because oxygen diffused into blood, four percent carbon dioxide because CO2 diffused out, and saturated water vapour at body temperature.",
        "vi": "So sánh khí hít vào vs thở ra: Khí hít vào chứa 21% oxy, 0,04% carbon dioxide và độ ẩm thay đổi. Khí thở ra chứa 16% oxy do oxy đã khuếch tán vào máu, 4% carbon dioxide do CO2 khuếch tán từ máu ra ngoài, cùng hơi nước bão hòa ở nhiệt độ cơ thể."
    },
    {
        "id": "card_limewater_test",
        "title": "🧪 Thí nghiệm Nước vôi trong đo CO₂ (Limewater Test)",
        "selector": "#card-limewater-test",
        "en": "Limewater investigation: Breathing in and out through a two-tube apparatus demonstrates gas differences. Expired air bubbled through Tube B turns clear limewater milky white in seconds due to high carbon dioxide precipitating calcium carbonate. Inspired air drawn through Tube A remains clear because atmospheric CO2 is too low to react noticeably.",
        "vi": "Thí nghiệm nước vôi trong: Hít thở qua dụng cụ hai ống nghiệm chứng minh sự khác biệt khí. Khí thở ra sục qua Ống B làm nước vôi trong chuyển đục màu trắng sữa chỉ sau vài giây do nồng độ CO2 cao tạo kết tủa CaCO3. Khí hít vào qua Ống A vẫn trong suốt do lượng CO2 trong khí quyển quá thấp."
    },
    {
        "id": "card_breathing_regulation",
        "title": "🏃 5. Tác động của Vận động & Điều hòa Nhịp thở",
        "selector": "#card-breathing-regulation",
        "en": "Regulation during exercise: Vigorous physical exercise accelerates cellular aerobic respiration in muscles, producing high amounts of carbon dioxide. Dissolved CO2 lowers blood pH. Chemoreceptors in the brainstem detect this acidity and signal respiratory muscles to dramatically increase breathing rate and depth to eliminate CO2.",
        "vi": "Điều hòa khi vận động: Khi tập luyện nặng, hô hấp tế bào ở cơ vân tăng vọt sinh ra nhiều CO2. Khí CO2 hòa tan trong máu tạo axit làm giảm độ pH máu. Thụ thể hóa học ở thân não phát hiện môi trường axit này và kích thích cơ hô hấp tăng mạnh tần số và biên độ thở để nhanh chóng thải trừ CO2."
    }
]

T11_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_alveoli_features": {"start": 1, "end": 1},
    "sec-alveoli-features": {"start": 1, "end": 1},
    "sec_respiratory_anatomy": {"start": 2, "end": 3},
    "sec-respiratory-anatomy": {"start": 2, "end": 3},
    "sec_ventilation_breathing": {"start": 4, "end": 7},
    "sec-ventilation-breathing": {"start": 4, "end": 7}
}

def transform_topic11_html():
    with open('scripts/raw_bio_topics/t11_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t11_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 11: Gas Exchange in Humans</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Alveoli Adaptations, Respiratory Anatomy, Breathing Mechanics, Limewater Test &amp; Brain Control</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 11: Trao đổi Khí ở Người</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Cấu tạo phế nang, Cơ chế hít thở, Tế bào lông rung, Đo CO₂ nước vôi trong &amp; Điều hòa nhịp thở</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🫁 1. FEATURES OF GAS EXCHANGE SURFACES<', ' id="sec-alveoli-features" class="lecture-interactive-card" data-lecture-section="sec_alveoli_features">🫁 1. FEATURES OF GAS EXCHANGE SURFACES<')
    p1 = p1.replace('>🗺️ 2. ANATOMY OF THE RESPIRATORY SYSTEM<', ' id="sec-respiratory-anatomy" class="lecture-interactive-card" data-lecture-section="sec_respiratory_anatomy">🗺️ 2. ANATOMY OF THE RESPIRATORY SYSTEM<')
    p1 = p1.replace('>🛡️ Role of Goblet Cells, Mucus, and Ciliated Cells<', ' id="card-ciliated-goblet" class="lecture-interactive-card" data-lecture-section="card_ciliated_goblet">🛡️ Role of Goblet Cells, Mucus, and Ciliated Cells<')
    p1 = p1.replace('>🌬️ 3. MECHANISM OF VENTILATION (BREATHING)<', ' id="sec-ventilation-breathing" class="lecture-interactive-card" data-lecture-section="sec_ventilation_breathing">🌬️ 3. MECHANISM OF VENTILATION (BREATHING)<')
    p1 = p1.replace('>📊 Composition Differences: Inspired vs Expired Air<', ' id="card-inspired-expired-comparison" class="lecture-interactive-card" data-lecture-section="card_inspired_expired_comparison">📊 Composition Differences: Inspired vs Expired Air<')
    p1 = p1.replace('>🧪 4. INVESTIGATING INSPIRED &amp; EXPIRED AIR (LIMEWATER TEST)<', ' id="card-limewater-test" class="lecture-interactive-card" data-lecture-section="card_limewater_test">🧪 4. INVESTIGATING INSPIRED &amp; EXPIRED AIR (LIMEWATER TEST)<')
    p1 = p1.replace('>🏃 5. PHYSICAL ACTIVITY', ' id="card-breathing-regulation" class="lecture-interactive-card" data-lecture-section="card_breathing_regulation">🏃 5. PHYSICAL ACTIVITY')

    # P2 replacements
    p2 = p2.replace('>🫁 1. ĐẶC ĐIỂM BỀ MẶT TRAO ĐỔI KHÍ (GAS EXCHANGE SURFACES)<', ' id="sec-alveoli-features" class="lecture-interactive-card" data-lecture-section="sec_alveoli_features">🫁 1. ĐẶC ĐIỂM BỀ MẶT TRAO ĐỔI KHÍ (GAS EXCHANGE SURFACES)<')
    p2 = p2.replace('>🗺️ 2. CẤU TẠO HỆ HÔ HẤP (RESPIRATORY SYSTEM)<', ' id="sec-respiratory-anatomy" class="lecture-interactive-card" data-lecture-section="sec_respiratory_anatomy">🗺️ 2. CẤU TẠO HỆ HÔ HẤP (RESPIRATORY SYSTEM)<')
    p2 = p2.replace('>🛡️ Vai trò của Goblet Cells, Mucus và Ciliated Cells<', ' id="card-ciliated-goblet" class="lecture-interactive-card" data-lecture-section="card_ciliated_goblet">🛡️ Vai trò của Goblet Cells, Mucus và Ciliated Cells<')
    p2 = p2.replace('>🌬️ 3. CƠ CHẾ THÔNG KHÍ / HÍT THỞ (VENTILATION)<', ' id="sec-ventilation-breathing" class="lecture-interactive-card" data-lecture-section="sec_ventilation_breathing">🌬️ 3. CƠ CHẾ THÔNG KHÍ / HÍT THỞ (VENTILATION)<')
    p2 = p2.replace('>📊 So sánh thành phần: Khí hít vào (Inspired) vs Khí thở ra (Expired)<', ' id="card-inspired-expired-comparison" class="lecture-interactive-card" data-lecture-section="card_inspired_expired_comparison">📊 So sánh thành phần: Khí hít vào (Inspired) vs Khí thở ra (Expired)<')
    p2 = p2.replace('>🧪 4. THÍ NGHIỆM ĐO KHÍ HÍT VÀO VÀ THỞ RA (BẰNG NƯỚC VÔI TRONG)<', ' id="card-limewater-test" class="lecture-interactive-card" data-lecture-section="card_limewater_test">🧪 4. THÍ NGHIỆM ĐO KHÍ HÍT VÀO VÀ THỞ RA (BẰNG NƯỚC VÔI TRONG)<')
    p2 = p2.replace('>🏃 5. TÁC ĐỘNG CỦA VẬN ĐỘNG', ' id="card-breathing-regulation" class="lecture-interactive-card" data-lecture-section="card_breathing_regulation">🏃 5. TÁC ĐỘNG CỦA VẬN ĐỘNG')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 11 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 11 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 12: Respiration
# ==============================================================================
T12_ID = 'fb098b77-64fa-463a-9829-64f5c9055de5'
T12_CODE = '12'
T12_TITLE = 'Topic 12: Respiration'

T12_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 12: Hô hấp Tế bào (Respiration)",
        "selector": "#sec-header",
        "en": "Welcome to Topic 12: Respiration. Cellular respiration consists of chemical reactions in cells that break down nutrient molecules to release energy for metabolism. In this lesson, we study energy utilization, aerobic respiration, anaerobic pathways in muscles and yeast, temperature investigations, and oxygen debt resolution.",
        "vi": "Chào mừng các bạn đến với Bài 12: Hô hấp Tế bào. Hô hấp tế bào là tập hợp các phản ứng hóa sinh trong tế bào phân giải phân tử dưỡng chất để giải phóng năng lượng cho trao đổi chất. Trong bài học này, chúng ta sẽ học về vai trò năng lượng, hô hấp hiếu khí, hô hấp kị khí ở cơ và nấm men, thí nghiệm nhiệt độ và hiện tượng nợ oxy."
    },
    {
        "id": "sec_respiration_concept",
        "title": "1. Bản chất của Hô hấp Tế bào & Phương trình Hiếu khí",
        "selector": "#sec-respiration-concept",
        "en": "Section 1: The concept of cellular respiration: Aerobic respiration is the chemical reactions in cells that use oxygen to break down nutrient molecules to release energy. The chemical equation is glucose plus six oxygen yields six carbon dioxide plus six water, releasing a large amount of energy stored in ATP molecules.",
        "vi": "Mục 1: Khái niệm hô hấp tế bào: Hô hấp hiếu khí là các phản ứng hóa sinh trong tế bào sử dụng oxy để phân giải phân tử dinh dưỡng giải phóng năng lượng. Phương trình hóa học là: C6H12O6 cộng sáu O2 tạo thành sáu CO2 cộng sáu H2O, giải phóng lượng lớn năng lượng tích trữ trong ATP."
    },
    {
        "id": "sec_energy_uses",
        "title": "Các Mục đích Sử dụng Năng lượng trong Cơ thể",
        "selector": "#sec-energy-uses",
        "en": "Section 1.2 details cellular uses of energy: Muscle contraction for movement, protein synthesis for tissue growth and enzyme production, cell division for tissue repair, active transport across membranes, nerve impulse transmission, and maintaining a constant internal body temperature.",
        "vi": "Mục 1.2 chi tiết các mục đích sử dụng năng lượng: Co cơ để vận động, tổng hợp protein cho sinh trưởng mô và tạo enzyme, phân chia tế bào để phục hồi tổn thương, vận chuyển chủ động qua màng, truyền xung thần kinh và duy trì nhiệt độ cơ thể hằng định."
    },
    {
        "id": "sec_aerobic_vs_anaerobic",
        "title": "2. Hô hấp Hiếu khí & Kị khí (Aerobic vs Anaerobic)",
        "selector": "#sec-aerobic-vs-anaerobic",
        "en": "Section 2 & 3 contrast pathways: Anaerobic respiration is the chemical reactions in cells that break down nutrient molecules to release energy without using oxygen, yielding much less energy per glucose molecule than aerobic respiration.",
        "vi": "Mục 2 và 3 đối chiếu các con đường: Hô hấp kị khí là phản ứng hóa sinh trong tế bào phân giải dưỡng chất giải phóng năng lượng mà không dùng oxy, tạo ra lượng năng lượng trên mỗi phân tử glucose ít hơn rất nhiều so với hô hấp hiếu khí."
    },
    {
        "id": "card_muscle_anaerobic",
        "title": "💪 Hô hấp Kị khí ở Cơ vân khi Vận động Mạnh",
        "selector": "#card-muscle-anaerobic",
        "en": "Anaerobic respiration in human muscles: During vigorous exercise when the heart and lungs cannot deliver oxygen fast enough, muscle cells respire anaerobically. Glucose is partially broken down into lactic acid, producing localized muscle fatigue and cramping.",
        "vi": "Hô hấp kị khí ở cơ vân: Khi vận động nặng vượt quá khả năng cung cấp oxy của tim phổi, tế bào cơ chuyển sang hô hấp kị khí. Glucose bị phân giải dở dang thành axit lactic gây mỏi cơ và đau cơ cục bộ."
    },
    {
        "id": "card_yeast_fermentation",
        "title": "🍞 Lên men ở Nấm men (Alcohol Fermentation)",
        "selector": "#card-yeast-fermentation",
        "en": "Anaerobic respiration in yeast: Yeast respires anaerobically to convert glucose into ethanol and carbon dioxide gas. In bread-making, carbon dioxide bubbles expand dough causing it to rise, while in brewing, ethanol creates alcoholic beverages.",
        "vi": "Hô hấp kị khí ở nấm men: Nấm men lên men chuyển đổi đường glucose thành cồn ethanol và khí carbon dioxide. Trong làm bánh mì, bọt khí CO2 làm bột phồng xốp, còn trong sản xuất bia rượu, ethanol tạo nên nồng độ cồn."
    },
    {
        "id": "sec_yeast_respiration",
        "title": "🌡️ 4. Thí nghiệm Ảnh hưởng của Nhiệt độ đến Hô hấp Nấm men",
        "selector": "#sec-yeast-respiration",
        "en": "Section 4 investigates yeast respiration rate: A layer of liquid paraffin oil floated on the yeast glucose suspension blocks atmospheric oxygen. The rate of respiration is quantified by counting carbon dioxide bubbles produced per minute across a temperature series.",
        "vi": "Mục 4 thí nghiệm tốc độ hô hấp ở nấm men: Lớp dầu paraffin nổi trên bề mặt dung dịch nấm men và đường glucose giúp ngăn oxy khí quyển xâm nhập tạo môi trường kị khí tuyệt đối. Tốc độ hô hấp được đo đếm bằng số bọt khí CO2 thoát ra mỗi phút ở các mức nhiệt độ khác nhau."
    },
    {
        "id": "sec_oxygen_debt",
        "title": "⚠️ 5. Hiện tượng Nợ Oxy (Oxygen Debt)",
        "selector": "#sec-oxygen-debt",
        "en": "Section 5 covers Oxygen Debt: After vigorous anaerobic exercise, lactic acid in muscles diffuses into blood and travels to the liver. Aerobic respiration in the liver oxidizes lactic acid back into glucose. Elevated heart and breathing rates persist after exercise to deliver the extra oxygen required to clear this oxygen debt.",
        "vi": "Mục 5 hiện tượng Nợ Oxy: Sau khi vận động mạnh kị khí, axit lactic từ cơ khuếch tán vào máu và được đưa đến gan. Quá trình hô hấp hiếu khí tại gan oxy hóa axit lactic trở lại thành glucose. Nhịp tim và nhịp thở vẫn duy trì ở mức cao sau khi ngừng chạy để cung cấp lượng oxy phụ trội trả món nợ oxy này."
    }
]

T12_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_respiration_concept": {"start": 1, "end": 1},
    "sec-respiration-concept": {"start": 1, "end": 1},
    "sec_energy_uses": {"start": 2, "end": 2},
    "sec-energy-uses": {"start": 2, "end": 2},
    "sec_aerobic_vs_anaerobic": {"start": 3, "end": 5},
    "sec-aerobic-vs-anaerobic": {"start": 3, "end": 5},
    "sec_yeast_respiration": {"start": 6, "end": 6},
    "sec-yeast-respiration": {"start": 6, "end": 6},
    "sec_oxygen_debt": {"start": 7, "end": 7},
    "sec-oxygen-debt": {"start": 7, "end": 7}
}

def transform_topic12_html():
    with open('scripts/raw_bio_topics/t12_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t12_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 12: Respiration</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Aerobic Respiration, Anaerobic Pathways, Yeast Fermentation, Temperature Effects &amp; Oxygen Debt</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 12: Hô hấp Tế bào (Respiration)</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Hô hấp hiếu khí, Kị khí cơ bắp, Lên men nấm men, Thí nghiệm nhiệt độ &amp; Hiện tượng nợ oxy</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>⚡ 1. THE CONCEPT OF RESPIRATION<', ' id="sec-respiration-concept" class="lecture-interactive-card" data-lecture-section="sec_respiration_concept">⚡ 1. THE CONCEPT OF RESPIRATION<')
    p1 = p1.replace('>🔋 Seven Key Uses of Energy in Living Organisms<', ' id="sec-energy-uses" class="lecture-interactive-card" data-lecture-section="sec_energy_uses">🔋 Seven Key Uses of Energy in Living Organisms<')
    p1 = p1.replace('>🌿 2. AEROBIC RESPIRATION<', ' id="sec-aerobic-vs-anaerobic" class="lecture-interactive-card" data-lecture-section="sec_aerobic_vs_anaerobic">🌿 2. AEROBIC RESPIRATION<')
    p1 = p1.replace('>In Muscles during Vigorous Exercise:<', ' id="card-muscle-anaerobic" class="lecture-interactive-card" data-lecture-section="card_muscle_anaerobic">In Muscles during Vigorous Exercise:<')
    p1 = p1.replace('>In Yeast (Fermentation):<', ' id="card-yeast-fermentation" class="lecture-interactive-card" data-lecture-section="card_yeast_fermentation">In Yeast (Fermentation):<')
    p1 = p1.replace('>🌡️ 4. INVESTIGATING EFFECT OF TEMPERATURE ON RESPINATION IN YEAST<', ' id="sec-yeast-respiration" class="lecture-interactive-card" data-lecture-section="sec_yeast_respiration">🌡️ 4. INVESTIGATING EFFECT OF TEMPERATURE ON RESPINATION IN YEAST<')
    p1 = p1.replace('>⚠️ 5. OXYGEN DEBT', ' id="sec-oxygen-debt" class="lecture-interactive-card" data-lecture-section="sec_oxygen_debt">⚠️ 5. OXYGEN DEBT')

    # P2 replacements
    p2 = p2.replace('>⚡ 1. KHÁI NIỆM HÔ HẤP TẾ BÀO (RESPIRATION)<', ' id="sec-respiration-concept" class="lecture-interactive-card" data-lecture-section="sec_respiration_concept">⚡ 1. KHÁI NIỆM HÔ HẤP TẾ BÀO (RESPIRATION)<')
    p2 = p2.replace('>🔋 7 Vai trò quan trọng của Năng lượng trong cơ thể sống (Uses of Energy)<', ' id="sec-energy-uses" class="lecture-interactive-card" data-lecture-section="sec_energy_uses">🔋 7 Vai trò quan trọng của Năng lượng trong cơ thể sống (Uses of Energy)<')
    p2 = p2.replace('>🌿 2. HÔ HẤP HIẾU KHÍ (AEROBIC RESPIRATION)<', ' id="sec-aerobic-vs-anaerobic" class="lecture-interactive-card" data-lecture-section="sec_aerobic_vs_anaerobic">🌿 2. HÔ HẤP HIẾU KHÍ (AEROBIC RESPIRATION)<')
    p2 = p2.replace('>Ở cơ bắp khi vận động quá sức (In Muscles):<', ' id="card-muscle-anaerobic" class="lecture-interactive-card" data-lecture-section="card_muscle_anaerobic">Ở cơ bắp khi vận động quá sức (In Muscles):<')
    p2 = p2.replace('>Ở Nấm men / Lên men (In Yeast):<', ' id="card-yeast-fermentation" class="lecture-interactive-card" data-lecture-section="card_yeast_fermentation">Ở Nấm men / Lên men (In Yeast):<')
    p2 = p2.replace('>🌡️ 4. THÍ NGHIỆM ẢNH HƯỞNG CỦA NHIỆT ĐỘ ĐẾN HÔ HẤP Ở NẤM MEN (YEAST)<', ' id="sec-yeast-respiration" class="lecture-interactive-card" data-lecture-section="sec_yeast_respiration">🌡️ 4. THÍ NGHIỆM ẢNH HƯỞNG CỦA NHIỆT ĐỘ ĐẾN HÔ HẤP Ở NẤM MEN (YEAST)<')
    p2 = p2.replace('>⚠️ 5. HIỆN TƯỢNG NỢ OXY', ' id="sec-oxygen-debt" class="lecture-interactive-card" data-lecture-section="sec_oxygen_debt">⚠️ 5. HIỆN TƯỢNG NỢ OXY')

    # Div balance (T12 P1 had +1 diff)
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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 12 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 12 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 13: Excretion in humans
# ==============================================================================
T13_ID = 'b8f0539e-9361-4ba4-a96e-74c106494ebe'
T13_CODE = '13'
T13_TITLE = 'Topic 13: Excretion in humans'

T13_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 13: Hệ Bài tiết ở Người & Cấu tạo Thận",
        "selector": "#sec-header",
        "en": "Welcome to Topic 13: Excretion in Humans. Excretion is the removal of the waste products of metabolism and substances in excess of requirements. In this lesson, we study liver deamination of amino acids, the clear distinction between excretion and egestion, gross kidney anatomy and nephron filtration, and modern treatments for kidney failure.",
        "vi": "Chào mừng các bạn đến với Bài 13: Hệ Bài tiết ở Người & Cấu tạo Thận. Bài tiết là sự thải loại các chất cặn bã sinh ra từ trao đổi chất cùng các chất dư thừa khỏi cơ thể. Trong bài học này, chúng ta sẽ học về quá trình khử amin tại gan, phân biệt bài tiết và thải phân, giải phẫu thận và nephron lọc máu, cùng các biện pháp điều trị suy thận."
    },
    {
        "id": "sec_excretion_liver",
        "title": "1. Bài tiết & Quá trình Khử amin tại Gan (Deamination)",
        "selector": "#sec-excretion-liver",
        "en": "Section 1: Excretion is defined as the removal of toxic substances and substances in excess of requirements from an organism. The primary excretory organs are lungs excreting carbon dioxide, kidneys excreting urea, excess water and mineral ions, and skin excreting sweat.",
        "vi": "Mục 1: Bài tiết được định nghĩa là sự đào thải các chất độc hại và các chất dư thừa ra khỏi cơ thể sinh vật. Các cơ quan bài tiết chính gồm phổi bài tiết CO2, thận bài tiết urê, nước và muối khoáng dư thừa, cùng da bài tiết mồ hôi."
    },
    {
        "id": "card_deamination",
        "title": "🥩 Đồng hóa & Khử Amin tại Gan (Deamination)",
        "selector": "#card-deamination",
        "en": "Deamination process: Excess dietary amino acids cannot be stored in the body. In the liver, the nitrogen-containing amino group is chemically removed from each amino acid molecule and converted into toxic ammonia, which is rapidly combined with CO2 into harmless, water-soluble urea excreted by kidneys.",
        "vi": "Quá trình khử amin: Axit amin dư thừa từ thức ăn không thể tích trữ trong cơ thể. Tại gan, nhóm amin chứa nitơ bị tách khỏi phân tử axit amin tạo thành amoniac độc, sau đó nhanh chóng kết hợp với CO2 tạo thành urê tan trong nước và được thận bài tiết ra ngoài."
    },
    {
        "id": "card_egestion_vs_excretion",
        "title": "🚨 BẪY ĐỀ THI: Thải phân (Egestion) vs Bài tiết (Excretion)",
        "selector": "#card-egestion-vs-excretion",
        "en": "Critical Cambridge Exam Warning: Never confuse egestion with excretion! Egestion is the passing out of undigested, unabsorbed food material such as cellulose dietary fibre via the anus as faeces; this material never took part in cellular metabolism. Excretion is the removal of metabolic wastes produced inside living cells.",
        "vi": "Cảnh báo tử huyệt thi cử Cambridge: Tuyệt đối không bao giờ nhầm lẫn giữa thải phân và bài tiết! Thải phân (Egestion) là sự tống chất xơ và bã thức ăn không tiêu hóa không hấp thụ qua hậu môn dưới dạng phân; chúng chưa từng tham gia vào trao đổi chất tế bào. Bài tiết (Excretion) là đào thải các sản phẩm phụ chuyển hóa sinh ra bên trong tế bào sống."
    },
    {
        "id": "sec_kidneys",
        "title": "2. Cấu tạo và Chức năng của Thận (Nephron & Filtration)",
        "selector": "#sec-kidneys",
        "en": "Section 2: Urinary system and kidney anatomy: Oxygenated blood high in urea arrives via the renal artery. The outer renal cortex performs ultrafiltration. The inner renal medulla contains loops of Henle reabsorbing water and salts. Purified blood exits via the renal vein, and collected urine drains through the renal pelvis into the ureter to the bladder.",
        "vi": "Mục 2: Hệ tiết niệu và cấu tạo thận: Máu giàu oxy chứa nhiều urê theo động mạch thận đi vào thận. Vỏ thận (cortex) bên ngoài thực hiện siêu lọc. Tủy thận (medulla) bên trong chứa các quai Henle tái hấp thu nước và muối. Máu đã làm sạch thoát ra theo tĩnh mạch thận, và nước tiểu thu gom tại bể thận chảy qua niệu quản xuống bàng quang."
    },
    {
        "id": "card_kidney_regions",
        "title": "🔍 Sơ đồ Giải phẫu Thận Tương tác (Kidney Anatomy)",
        "selector": "#card-kidney-regions",
        "en": "Kidney anatomy zones: The cortex is dense with Bowman's capsules and glomeruli. The medulla contains collecting ducts and medullary pyramids. The renal pelvis funnels urine down the ureter to be stored temporarily in the muscular bladder before release via the urethra.",
        "vi": "Các phân vùng giải phẫu thận: Vỏ thận tập trung dày đặc các nang Bowman và búi mao mạch cuộn. Tủy thận chứa các ống góp và tháp thận. Bể thận như một chiếc phễu gom nước tiểu dẫn xuống niệu quản để tích trữ tạm thời trong bàng quang trước khi thải ra ngoài qua niệu đạo."
    },
    {
        "id": "sec_kidney_failure",
        "title": "3. Suy thận: Chạy thận Nhân tạo & Ghép thận",
        "selector": "#sec-kidney-failure",
        "en": "Section 3: Treatment of kidney failure: When kidneys fail, toxic urea builds up rapidly to lethal levels. Patients require regular hemodialysis using a dialysis machine or a donor kidney transplant.",
        "vi": "Mục 3: Điều trị suy thận: Khi thận bị suy, lượng urê độc hại tăng vọt nhanh chóng đe dọa tính mạng. Bệnh nhân cần chạy thận nhân tạo định kỳ bằng máy lọc máu hoặc được ghép thận từ người hiến tặng."
    },
    {
        "id": "card_dialysis_machine",
        "title": "💡 Nguyên lý Máy Chạy thận Nhân tạo (Dialysis Machine)",
        "selector": "#card-dialysis-machine",
        "en": "Dialysis mechanism: Patient's blood flows through cellulose dialysis tubing surrounded by dialysis fluid. The tubing is partially permeable: urea, excess water, and salts diffuse out down concentration gradients. The dialysis fluid has identical glucose and amino acid concentrations as normal blood, preventing any net loss of these valuable nutrients.",
        "vi": "Nguyên lý máy lọc máu: Máu bệnh nhân chảy qua ống màng lọc bán thấm cellulose ngâm trong dịch lọc máu. Màng bán thấm cho phép urê, nước và muối dư thừa khuếch tán ra dịch lọc xuôi theo gradien nồng độ. Dịch lọc có nồng độ glucose và axit amin tương đương máu bình thường để chống thất thoát dưỡng chất quý giá của cơ thể."
    }
]

T13_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_excretion_liver": {"start": 1, "end": 3},
    "sec-excretion-liver": {"start": 1, "end": 3},
    "sec_kidneys": {"start": 4, "end": 5},
    "sec-kidneys": {"start": 4, "end": 5},
    "sec_kidney_failure": {"start": 6, "end": 7},
    "sec-kidney-failure": {"start": 6, "end": 7}
}

def transform_topic13_html():
    with open('scripts/raw_bio_topics/t13_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t13_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 13: Excretion in Humans</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Liver Deamination, Excretion vs Egestion, Kidney Anatomy &amp; Dialysis Treatments</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 13: Hệ Bài tiết ở Người &amp; Cấu tạo Thận</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Khử amin ở gan, Bài tiết vs Thải phân, Giải phẫu thận &amp; Máy chạy thận nhân tạo</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🚽 1. EXCRETION AND THE ROLE OF THE LIVER<', ' id="sec-excretion-liver" class="lecture-interactive-card" data-lecture-section="sec_excretion_liver">🚽 1. EXCRETION AND THE ROLE OF THE LIVER<')
    p1 = p1.replace('>🥩 Role of the Liver: Assimilation &amp; Deamination<', ' id="card-deamination" class="lecture-interactive-card" data-lecture-section="card_deamination">🥩 Role of the Liver: Assimilation &amp; Deamination<')
    p1 = p1.replace('>🚨 EXAM WARNING: Egestion vs Excretion<', ' id="card-egestion-vs-excretion" class="lecture-interactive-card" data-lecture-section="card_egestion_vs_excretion">🚨 EXAM WARNING: Egestion vs Excretion<')
    p1 = p1.replace('>🩸 2. THE HUMAN URINARY SYSTEM &amp; KIDNEY ANATOMY<', ' id="sec-kidneys" class="lecture-interactive-card" data-lecture-section="sec_kidneys">🩸 2. THE HUMAN URINARY SYSTEM &amp; KIDNEY ANATOMY<')
    p1 = p1.replace('>Interactive Kidney Anatomy<', ' id="card-kidney-regions" class="lecture-interactive-card" data-lecture-section="card_kidney_regions">Interactive Kidney Anatomy<')
    p1 = p1.replace('>🏥 3. TREATMENT OF KIDNEY FAILURE<', ' id="sec-kidney-failure" class="lecture-interactive-card" data-lecture-section="sec_kidney_failure">🏥 3. TREATMENT OF KIDNEY FAILURE<')
    p1 = p1.replace('>💡 How a Kidney Dialysis Machine Works<', ' id="card-dialysis-machine" class="lecture-interactive-card" data-lecture-section="card_dialysis_machine">💡 How a Kidney Dialysis Machine Works<')

    # P2 replacements
    p2 = p2.replace('>🚽 1. BÀI TIẾT VÀ VAI TRÒ CỦA GAN (EXCRETION &amp; LIVER)<', ' id="sec-excretion-liver" class="lecture-interactive-card" data-lecture-section="sec_excretion_liver">🚽 1. BÀI TIẾT VÀ VAI TRÒ CỦA GAN (EXCRETION &amp; LIVER)<')
    p2 = p2.replace('>🥩 Vai trò của Gan: Đồng hóa &amp; Khử Amin (Deamination)<', ' id="card-deamination" class="lecture-interactive-card" data-lecture-section="card_deamination">🥩 Vai trò của Gan: Đồng hóa &amp; Khử Amin (Deamination)<')
    p2 = p2.replace('>🚨 BẪY ĐỀ THI: Thải phân (Egestion) vs Bài tiết (Excretion)<', ' id="card-egestion-vs-excretion" class="lecture-interactive-card" data-lecture-section="card_egestion_vs_excretion">🚨 BẪY ĐỀ THI: Thải phân (Egestion) vs Bài tiết (Excretion)<')
    p2 = p2.replace('>🩸 2. HỆ TIẾT NIỆU &amp; CẤU TẠO THẬN (KIDNEY ANATOMY)<', ' id="sec-kidneys" class="lecture-interactive-card" data-lecture-section="sec_kidneys">🩸 2. HỆ TIẾT NIỆU &amp; CẤU TẠO THẬN (KIDNEY ANATOMY)<')
    p2 = p2.replace('>Interactive Kidney Anatomy (Sơ đồ giải phẫu Thận tương tác)<', ' id="card-kidney-regions" class="lecture-interactive-card" data-lecture-section="card_kidney_regions">Interactive Kidney Anatomy (Sơ đồ giải phẫu Thận tương tác)<')
    p2 = p2.replace('>🏥 3. ĐIỀU TRỊ SUY THẬN (KIDNEY FAILURE)<', ' id="sec-kidney-failure" class="lecture-interactive-card" data-lecture-section="sec_kidney_failure">🏥 3. ĐIỀU TRỊ SUY THẬN (KIDNEY FAILURE)<')
    p2 = p2.replace('>💡 Nguyên lý máy chạy thận (Dialysis Machine)<', ' id="card-dialysis-machine" class="lecture-interactive-card" data-lecture-section="card_dialysis_machine">💡 Nguyên lý máy chạy thận (Dialysis Machine)<')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 13 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 13 P2 div diff != 0"

    return p1, p2

async def build_batch3():
    tasks = [
        ("Topic 10", T10_CODE, T10_ID, T10_TITLE, T10_SEGMENTS, T10_MAJOR_SECTIONS, transform_topic10_html),
        ("Topic 11", T11_CODE, T11_ID, T11_TITLE, T11_SEGMENTS, T11_MAJOR_SECTIONS, transform_topic11_html),
        ("Topic 12", T12_CODE, T12_ID, T12_TITLE, T12_SEGMENTS, T12_MAJOR_SECTIONS, transform_topic12_html),
        ("Topic 13", T13_CODE, T13_ID, T13_TITLE, T13_SEGMENTS, T13_MAJOR_SECTIONS, transform_topic13_html)
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
    asyncio.run(build_batch3())
