# -*- coding: utf-8 -*-
"""
Batch 4 Builder: Topics 14, 15, 16, 17
- Topic 14: Coordination and response
- Topic 15: Drugs
- Topic 16: Reproduction
- Topic 17: Inheritance
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
# TOPIC 14: Coordination and response
# ==============================================================================
T14_ID = 'c9abc870-7cbd-4c7e-b6c9-2d6237ff7670'
T14_CODE = '14'
T14_TITLE = 'Topic 14: Coordination and response'

T14_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 14: Điều hòa Hoạt động & Đáp ứng Sinh học",
        "selector": "#sec-header",
        "en": "Welcome to Topic 14: Coordination and Response. Organisms detect changes in their internal and external environment and respond to maintain homeostasis and survival. In this lesson, we study the human nervous system, reflex arcs, synapse neurochemistry, sense organs including the eye and pupil accommodation, endocrine adrenaline regulation, skin thermoregulation, and plant auxin tropisms.",
        "vi": "Chào mừng các bạn đến với Bài 14: Điều hòa Hoạt động & Đáp ứng Sinh học. Sinh vật cảm nhận sự biến đổi của môi trường nội bào và ngoại cảnh để đáp ứng duy trì cân bằng nội môi và sinh tồn. Trong bài học này, chúng ta sẽ học về hệ thần kinh, cung phản xạ, chất truyền tin sinap, giải phẫu mắt và phản xạ điều tiết, hoocmôn adrenaline, điều hòa thân nhiệt ở da và hướng động auxin ở thực vật."
    },
    {
        "id": "sec_nervous_reflexes",
        "title": "1. Hệ Thần kinh & Cung Phản xạ (Reflex Arc)",
        "selector": "#sec-nervous-reflexes",
        "en": "Section 1: The nervous system consists of the central nervous system—the brain and spinal cord—and the peripheral nervous system. A reflex action is an involuntary, rapid, automatic response to a stimulus that protects the body from injury.",
        "vi": "Mục 1: Hệ thần kinh gồm hệ thần kinh trung ương—não bộ và tủy sống—cùng hệ thần kinh ngoại biên. Phản xạ là phản ứng tự động, nhanh chóng và vô thức của cơ thể đối với kích thích nhằm bảo vệ cơ thể khỏi tổn thương."
    },
    {
        "id": "card_reflex_arc",
        "title": "⚡ Chuỗi Cung Phản Xạ (Reflex Arc Sequence)",
        "selector": "#card-reflex-arc",
        "en": "The reflex arc pathway: Stimulus is detected by a receptor, triggering electrical impulses along a sensory neurone into the spinal cord. In the CNS, the impulse passes across a synapse to a relay neurone, then along a motor neurone to an effector muscle or gland, producing an immediate protective response.",
        "vi": "Đường truyền cung phản xạ: Kích thích được thụ thể tiếp nhận, khởi phát xung điện truyền dọc nơ-ron cảm giác vào tủy sống. Tại thần kinh trung ương, xung điện qua khe sinap truyền sang nơ-ron trung gian, rồi theo nơ-ron vận động đến cơ quan đáp ứng (cơ hoặc tuyến) tạo phản xạ tức thì."
    },
    {
        "id": "card_synapse",
        "title": "🌉 Khe Sinap & Dẫn truyền Xung 1 Chiều",
        "selector": "#card-synapse",
        "en": "Synapse structure and function: A synapse is a junction between two neurones. When an impulse reaches the presynaptic knob, neurotransmitter chemical molecules are released from vesicles into the synaptic cleft. They diffuse across the gap and bind to receptor proteins on the postsynaptic membrane, triggering a new impulse unidirectionally.",
        "vi": "Cấu tạo và hoạt động của sinap: Sinap là điểm tiếp xúc giữa hai nơ-ron. Khi xung điện đến cúc tận cùng trước sinap, chất truyền tin hóa học được giải phóng từ các bọc vào khe sinap. Chúng khuếch tán qua khe gắn vào thụ thể màng sau sinap, khởi phát xung điện mới truyền theo đúng một chiều."
    },
    {
        "id": "sec_eye_anatomy",
        "title": "2. Cơ quan Thị giác: Cấu tạo Mắt & Cơ chế Điều tiết",
        "selector": "#sec-eye-anatomy",
        "en": "Section 2: The human eye: Light passes through the transparent cornea, pupil aperture controlled by the iris, and flexible convex lens onto the photoreceptor retina. The fovea contains the highest density of cone cells providing sharp colour vision.",
        "vi": "Mục 2: Cơ quan thị giác: Ánh sáng đi qua giác mạc trong suốt, lỗ đồng tử điều khiển bởi mống mắt, thấu kính đàn hồi và hội tụ lên võng mạc. Điểm vàng (fovea) chứa mật độ tế bào nón cao nhất mang lại thị lực sắc nét và nhìn màu chuẩn xác."
    },
    {
        "id": "card_eye_accommodation",
        "title": "👁️ Phản xạ Điều tiết của Thể Thủy tinh (Accommodation)",
        "selector": "#card-eye-accommodation",
        "en": "Accommodation reflex: When viewing a near object, ciliary muscles contract, suspensory ligaments become slack, allowing the lens to become thicker and more convex, refracting light strongly. When viewing a distant object, ciliary muscles relax, suspensory ligaments pull tight, stretching the lens thin.",
        "vi": "Cơ chế điều tiết mắt: Khi nhìn vật ở gần, cơ thể mi co lại, dây chằng treo giãn chùng, thấu kính phồng dày hình cầu khúc xạ ánh sáng mạnh. Khi nhìn vật ở xa, cơ thể mi giãn ra, dây chằng treo căng kéo làm thấu kính dẹt mỏng để hội tụ chuẩn xác lên võng mạc."
    },
    {
        "id": "sec_endocrine_system",
        "title": "3. Hệ Nội tiết & Hooc-môn (Adrenaline Focus)",
        "selector": "#sec-endocrine-system",
        "en": "Section 3: The endocrine system consists of glands that secrete hormones directly into the bloodstream. Hormones are chemical messengers transported by blood plasma that alter the metabolic activity of specific target organs.",
        "vi": "Mục 3: Hệ nội tiết gồm các tuyến nội tiết tiết hoocmôn trực tiếp vào máu. Hoocmôn là những chất truyền tin hóa học được huyết tương vận chuyển đến tác động và điều chỉnh hoạt động của các cơ quan đích chuyên biệt."
    },
    {
        "id": "card_adrenaline",
        "title": "🔥 Hoocmôn Adrenaline (Fight or Flight Response)",
        "selector": "#card-adrenaline",
        "en": "Adrenaline function: Secreted by adrenal glands in fear or stress, it triggers the 'fight or flight' response: increasing heart rate and stroke volume, accelerating breathing rate, dilating pupils, and stimulating liver glycogenolysis to raise blood glucose for muscular ATP respiration.",
        "vi": "Tác dụng của Adrenaline: Tiết ra từ tuyến thượng thận khi sợ hãi hoặc căng thẳng, kích hoạt phản ứng 'Chiến-hay-Biến': tăng nhịp tim và lưu lượng máu, tăng nhịp thở, giãn đồng tử và kích thích gan phân giải glycogen thành glucose cung cấp năng lượng ATP cho cơ bắp hoạt động."
    },
    {
        "id": "sec_homeostasis",
        "title": "4. Cân bằng Nội môi: Đường huyết & Điều nhiệt",
        "selector": "#sec-homeostasis",
        "en": "Section 4: Homeostasis is the maintenance of a constant internal environment within narrow physiological limits. Negative feedback restores variable parameters back towards set point levels.",
        "vi": "Mục 4: Cân bằng nội môi là sự duy trì môi trường bên trong cơ thể ổn định trong giới hạn sinh lý hẹp. Cơ chế điều hòa ngược âm tính (negative feedback) giúp đưa các chỉ số sinh lý dao động trở lại mức điểm chuẩn."
    },
    {
        "id": "card_blood_glucose",
        "title": "🩸 Điều hòa Đường huyết bởi Insulin và Glucagon",
        "selector": "#card-blood-glucose",
        "en": "Blood glucose regulation: When blood glucose rises after a meal, the pancreas secretes insulin, stimulating liver and muscle cells to absorb glucose and convert it into insoluble glycogen. When blood glucose drops during fasting, the pancreas secretes glucagon, stimulating liver cells to break glycogen back into glucose.",
        "vi": "Điều hòa đường huyết: Khi nồng độ glucose trong máu tăng cao sau bữa ăn, tuyến tụy tiết insulin kích thích tế bào gan và cơ hấp thu glucose chuyển thành glycogen dự trữ. Khi đường huyết hạ thấp lúc đói, tuyến tụy tiết glucagon kích thích gan phân giải glycogen thành glucose giải phóng vào máu."
    },
    {
        "id": "card_thermoregulation_skin",
        "title": "🌡️ Điều hòa Thân nhiệt ở Da (Thermoregulation)",
        "selector": "#card-thermoregulation-skin",
        "en": "Skin thermoregulation: In hot conditions, arterioles near the skin surface dilate (vasodilation) and sweat glands secrete sweat, dissipating latent heat of vaporization. In cold conditions, arterioles constrict (vasoconstriction) redirecting blood to core organs, hair erector muscles contract, and skeletal muscles shiver.",
        "vi": "Điều hòa thân nhiệt ở da: Khi trời nóng, tiểu động mạch dưới da giãn (vasodilation) và tuyến mồ hôi tiết mồ hôi tỏa nhiệt bay hơi. Khi trời lạnh, tiểu động mạch co lại (vasoconstriction) dồn máu về nội tạng trung tâm, cơ dựng lông co tạo lớp khí cách nhiệt và cơ vân run rẩy sinh nhiệt."
    },
    {
        "id": "sec_plant_tropisms",
        "title": "🌱 5. Hướng động ở Thực vật & Hooc-môn Auxin",
        "selector": "#sec-plant-tropisms",
        "en": "Section 5: Plant tropisms: A tropism is a growth response towards or away from a directional stimulus. Plant shoots exhibit positive phototropism and negative gravitropism. The plant hormone auxin is produced at the shoot tip, diffuses down, and accumulates on the shaded side, stimulating cell elongation so the shoot bends towards light.",
        "vi": "Mục 5: Hướng động ở thực vật: Hướng động là phản ứng sinh trưởng định hướng đối với kích thích từ một phía. Ngọn cây có tính hướng sáng dương và hướng trọng lực âm. Hoocmôn thực vật auxin được sản sinh ở đỉnh ngọn, khuếch tán xuống dưới và tập trung ở phía bị che tối, kích thích kéo dài tế bào khiến ngọn cây uốn cong về phía ánh sáng."
    }
]

T14_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_nervous_reflexes": {"start": 1, "end": 3},
    "sec-nervous-reflexes": {"start": 1, "end": 3},
    "sec_eye_anatomy": {"start": 4, "end": 5},
    "sec-eye-anatomy": {"start": 4, "end": 5},
    "sec_endocrine_system": {"start": 6, "end": 7},
    "sec-endocrine-system": {"start": 6, "end": 7},
    "sec_homeostasis": {"start": 8, "end": 10},
    "sec-homeostasis": {"start": 8, "end": 10},
    "sec_plant_tropisms": {"start": 11, "end": 11},
    "sec-plant-tropisms": {"start": 11, "end": 11}
}

def transform_topic14_html():
    with open('scripts/raw_bio_topics/t14_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t14_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 14: Coordination &amp; Response</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Nervous Reflexes, Synapses, Eye Accommodation, Hormones, Thermoregulation &amp; Auxin</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 14: Điều hòa Hoạt động &amp; Đáp ứng Sinh học</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Hệ thần kinh, Cung phản xạ, Cấu tạo mắt, Hoocmôn, Điều nhiệt da &amp; Hướng động Auxin</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🧠 1. THE NERVOUS SYSTEM &amp; REFLEX ACTIONS<', ' id="sec-nervous-reflexes" class="lecture-interactive-card" data-lecture-section="sec_nervous_reflexes">🧠 1. THE NERVOUS SYSTEM &amp; REFLEX ACTIONS<')
    p1 = p1.replace('>The Sequence of a Reflex Arc<', ' id="card-reflex-arc" class="lecture-interactive-card" data-lecture-section="card_reflex_arc">The Sequence of a Reflex Arc<')
    p1 = p1.replace('>🌉 Structure and Function of a Synapse<', ' id="card-synapse" class="lecture-interactive-card" data-lecture-section="card_synapse">🌉 Structure and Function of a Synapse<')
    p1 = p1.replace('>👁️ 2. SENSE ORGANS: THE HUMAN EYE<', ' id="sec-eye-anatomy" class="lecture-interactive-card" data-lecture-section="sec_eye_anatomy">👁️ 2. SENSE ORGANS: THE HUMAN EYE<')
    p1 = p1.replace('>Interactive Eye Anatomy<', ' id="card-eye-accommodation" class="lecture-interactive-card" data-lecture-section="card_eye_accommodation">Interactive Eye Anatomy<')
    p1 = p1.replace('>🧪 3. HORMONES &amp; THE ENDOCRINE SYSTEM<', ' id="sec-endocrine-system" class="lecture-interactive-card" data-lecture-section="sec_endocrine_system">🧪 3. HORMONES &amp; THE ENDOCRINE SYSTEM<')
    p1 = p1.replace('>🔥 Adrenaline (\'Fight or Flight\' Hormone)<', ' id="card-adrenaline" class="lecture-interactive-card" data-lecture-section="card_adrenaline">🔥 Adrenaline (\'Fight or Flight\' Hormone)<')
    p1 = p1.replace('>🌡️ 4. HOMEOSTASIS: GLUCOSE &amp; THERMOREGULATION<', ' id="sec-homeostasis" class="lecture-interactive-card" data-lecture-section="sec_homeostasis">🌡️ 4. HOMEOSTASIS: GLUCOSE &amp; THERMOREGULATION<')
    p1 = p1.replace('>🩸 Control of Blood Glucose by Insulin and Glucagon<', ' id="card-blood-glucose" class="lecture-interactive-card" data-lecture-section="card_blood_glucose">🩸 Control of Blood Glucose by Insulin and Glucagon<')
    p1 = p1.replace('>Interactive Skin Map (Thermoregulation)<', ' id="card-thermoregulation-skin" class="lecture-interactive-card" data-lecture-section="card_thermoregulation_skin">Interactive Skin Map (Thermoregulation)<')
    p1 = p1.replace('>🌱 5. TROPIC RESPONSES &amp; AUXIN CONTROL<', ' id="sec-plant-tropisms" class="lecture-interactive-card" data-lecture-section="sec_plant_tropisms">🌱 5. TROPIC RESPONSES &amp; AUXIN CONTROL<')

    # P2 replacements
    p2 = p2.replace('>🧠 1. HỆ THẦN KINH &amp; CUNG PHẢN XẠ (NERVOUS SYSTEM &amp; REFLEX ACTIONS)<', ' id="sec-nervous-reflexes" class="lecture-interactive-card" data-lecture-section="sec_nervous_reflexes">🧠 1. HỆ THẦN KINH &amp; CUNG PHẢN XẠ (NERVOUS SYSTEM &amp; REFLEX ACTIONS)<')
    p2 = p2.replace('>Chuỗi Cung Phản Xạ (Reflex Arc)<', ' id="card-reflex-arc" class="lecture-interactive-card" data-lecture-section="card_reflex_arc">Chuỗi Cung Phản Xạ (Reflex Arc)<')
    p2 = p2.replace('>🌉 Khe Sinap (Synapse) &amp; Dẫn truyền 1 chiều<', ' id="card-synapse" class="lecture-interactive-card" data-lecture-section="card_synapse">🌉 Khe Sinap (Synapse) &amp; Dẫn truyền 1 chiều<')
    p2 = p2.replace('>👁️ 2. GIẢI PHẪU VÀ SINH LÝ MẮT (THE HUMAN EYE)<', ' id="sec-eye-anatomy" class="lecture-interactive-card" data-lecture-section="sec_eye_anatomy">👁️ 2. GIẢI PHẪU VÀ SINH LÝ MẮT (THE HUMAN EYE)<')
    p2 = p2.replace('>Interactive Eye Anatomy (Sơ đồ Mắt tương tác)<', ' id="card-eye-accommodation" class="lecture-interactive-card" data-lecture-section="card_eye_accommodation">Interactive Eye Anatomy (Sơ đồ Mắt tương tác)<')
    p2 = p2.replace('>🧪 3. HOOCMÔN &amp; HỆ NỘI TIẾT (ENDOCRINE SYSTEM)<', ' id="sec-endocrine-system" class="lecture-interactive-card" data-lecture-section="sec_endocrine_system">🧪 3. HOOCMÔN &amp; HỆ NỘI TIẾT (ENDOCRINE SYSTEM)<')
    p2 = p2.replace('>🔥 Adrenaline (Hoocmôn Chiến-hay-Biến)<', ' id="card-adrenaline" class="lecture-interactive-card" data-lecture-section="card_adrenaline">🔥 Adrenaline (Hoocmôn Chiến-hay-Biến)<')
    p2 = p2.replace('>🌡️ 4. CÂN BẰNG NỘI MÔI (HOMEOSTASIS)<', ' id="sec-homeostasis" class="lecture-interactive-card" data-lecture-section="sec_homeostasis">🌡️ 4. CÂN BẰNG NỘI MÔI (HOMEOSTASIS)<')
    p2 = p2.replace('>🩸 Điều hòa Đường huyết bởi Insulin và Glucagon<', ' id="card-blood-glucose" class="lecture-interactive-card" data-lecture-section="card_blood_glucose">🩸 Điều hòa Đường huyết bởi Insulin và Glucagon<')
    p2 = p2.replace('>Interactive Skin Map (Sơ đồ điều hòa thân nhiệt ở Da)<', ' id="card-thermoregulation-skin" class="lecture-interactive-card" data-lecture-section="card_thermoregulation_skin">Interactive Skin Map (Sơ đồ điều hòa thân nhiệt ở Da)<')
    p2 = p2.replace('>🌱 5. HƯỚNG ĐỘNG Ở THỰC VẬT &amp; HOOCMÔN AUXIN<', ' id="sec-plant-tropisms" class="lecture-interactive-card" data-lecture-section="sec_plant_tropisms">🌱 5. HƯỚNG ĐỘNG Ở THỰC VẬT &amp; HOOCMÔN AUXIN<')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 14 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 14 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 15: Drugs
# ==============================================================================
T15_ID = 'f87b29a1-56a3-4668-a249-ed9f118d31d8'
T15_CODE = '15'
T15_TITLE = 'Topic 15: Drugs'

T15_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 15: Thuốc và Chất Dược lý (Drugs)",
        "selector": "#sec-header",
        "en": "Welcome to Topic 15: Drugs. In biology, a drug is defined as any substance taken into the body that modifies or affects chemical reactions in the body. In this lesson, we study medicinal drugs versus drugs of abuse, antibiotics and why they are totally ineffective against viruses, and the development and prevention of antibiotic resistance including MRSA.",
        "vi": "Chào mừng các bạn đến với Bài 15: Thuốc và Chất Dược lý (Drugs). Trong sinh học, thuốc được định nghĩa là bất kỳ chất nào đưa vào cơ thể làm thay đổi hoặc ảnh hưởng đến các phản ứng hóa sinh trong cơ thể. Trong bài học này, chúng ta sẽ học về thuốc chữa bệnh và chất gây nghiện lạm dụng, kháng sinh và lý do kháng sinh vô dụng với virus, cùng cơ chế hình thành vi khuẩn kháng kháng sinh như MRSA."
    },
    {
        "id": "sec_what_is_drug",
        "title": "1. Định nghĩa Thuốc & Phân loại Dược phẩm",
        "selector": "#sec-what-is-drug",
        "en": "Section 1: What is a drug? Drugs are classified into medicinal drugs prescribed to treat symptoms or cure diseases, and recreational drugs taken for non-medical psychological reasons. Many drugs can cause psychological and physical dependence leading to addiction and withdrawal symptoms.",
        "vi": "Mục 1: Thuốc là gì? Thuốc được chia thành thuốc điều trị dùng theo đơn để chữa triệu chứng hay bệnh tật, và chất kích thích lạm dụng cho mục đích giải trí phi y khoa. Nhiều loại thuốc có thể gây lệ thuộc tâm lý và thể chất dẫn đến nghiện và hội chứng cai thuốc."
    },
    {
        "id": "sec_antibiotics",
        "title": "2. Kháng sinh & Lý do Vô dụng trước Virus",
        "selector": "#sec-antibiotics",
        "en": "Section 2: Antibiotics are chemical substances produced by microorganisms that kill bacteria or inhibit their growth by disrupting bacterial cell wall synthesis or protein translation. Crucially, antibiotics are completely ineffective against viruses because viruses have no cell wall, no cellular structure, and rely entirely on host cell machinery to replicate.",
        "vi": "Mục 2: Thuốc kháng sinh là các hoạt chất do vi sinh vật tiết ra có tác dụng tiêu diệt hoặc ức chế vi khuẩn bằng cách phá hủy thành tế bào peptidoglycan hoặc quá trình dịch mã. Cực kỳ quan trọng: Kháng sinh hoàn toàn vô dụng trước virus vì virus không có thành tế bào, không có cấu tạo tế bào và ký sinh hoàn toàn vào tế bào vật chủ để nhân lên."
    },
    {
        "id": "card_antibiotics_viruses",
        "title": "🦠 Kháng sinh Diệt Vi khuẩn vs Bất lực trước Virus",
        "selector": "#card-antibiotics-viruses",
        "en": "Why antibiotics fail against viruses: Penicillin inhibits the enzyme cross-linking bacterial peptidoglycan cell walls, causing bacteria to burst by osmotic lysis. Viruses consist merely of a genetic nucleic acid core inside a protein capsid coat with no target cell wall or metabolic enzymes.",
        "vi": "Tại sao kháng sinh bất lực trước virus: Penicillin ức chế enzyme đan lưới thành tế bào peptidoglycan của vi khuẩn làm vi khuẩn vỡ tan do thẩm thấu. Virus chỉ gồm một lõi axit nucleic nằm trong vỏ capsid protein, không hề có thành tế bào hay enzyme trao đổi chất cho kháng sinh tấn công."
    },
    {
        "id": "sec_antibiotic_resistance",
        "title": "3. Sự Kháng Kháng sinh & Siêu vi khuẩn MRSA",
        "selector": "#sec-antibiotic-resistance",
        "en": "Section 3: Antibiotic resistance: Random DNA mutations in bacteria occasionally grant resistance against a specific antibiotic. When patients overuse antibiotics or fail to complete the full course, susceptible bacteria die while resistant mutants survive, reproduce by binary fission, and pass the resistance gene to offspring by natural selection, spawning superbugs like MRSA.",
        "vi": "Mục 3: Sự kháng kháng sinh: Đột biến gen ngẫu nhiên ở vi khuẩn đôi khi mang lại khả năng kháng lại một loại kháng sinh. Khi bệnh nhân lạm dụng hoặc không uống hết liệu trình, vi khuẩn nhạy cảm bị tiêu diệt trong khi vi khuẩn đột biến sống sót, phân chia nhân đôi và truyền gen kháng thuốc cho đời sau qua chọn lọc tự nhiên, tạo ra các siêu vi khuẩn như MRSA."
    },
    {
        "id": "card_resistance_prevention",
        "title": "🛡️ Biện pháp Hạn chế Vi khuẩn Kháng thuốc",
        "selector": "#card-resistance-prevention",
        "en": "Controlling antibiotic resistance: Doctors must avoid prescribing antibiotics for viral colds, patients must always complete the full prescribed antibiotic course to eliminate all bacteria, hygiene standards in hospitals must be rigorous, and agricultural use of antibiotics as animal growth promoters must be strictly banned.",
        "vi": "Biện pháp kiểm soát kháng thuốc: Bác sĩ không kê đơn kháng sinh cho bệnh cảm cúm do virus, bệnh nhân bắt buộc phải uống hết toàn bộ đơn thuốc dù đã thấy đỡ, nâng cao quy chuẩn khử trùng bệnh viện và cấm triệt để việc trộn kháng sinh vào thức ăn gia súc để kích thích tăng trọng."
    }
]

T15_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_what_is_drug": {"start": 1, "end": 1},
    "sec-what-is-drug": {"start": 1, "end": 1},
    "sec_antibiotics": {"start": 2, "end": 3},
    "sec-antibiotics": {"start": 2, "end": 3},
    "sec_antibiotic_resistance": {"start": 4, "end": 5},
    "sec-antibiotic-resistance": {"start": 4, "end": 5}
}

def transform_topic15_html():
    with open('scripts/raw_bio_topics/t15_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t15_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 15: Drugs</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Medicinal Drugs, Antibiotics vs Viruses, Resistance Selection &amp; The MRSA Crisis</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 15: Thuốc và Chất Dược lý (Drugs)</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Định nghĩa thuốc, Kháng sinh vs Virus, Cơ chế kháng thuốc &amp; Nguy cơ siêu vi khuẩn MRSA</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>💊 1. WHAT IS A DRUG?<', ' id="sec-what-is-drug" class="lecture-interactive-card" data-lecture-section="sec_what_is_drug">💊 1. WHAT IS A DRUG?<')
    p1 = p1.replace('>🦠 2. ANTIBIOTICS (Action on Bacteria vs Viruses)<', ' id="sec-antibiotics" class="lecture-interactive-card" data-lecture-section="sec_antibiotics">🦠 2. ANTIBIOTICS (Action on Bacteria vs Viruses)<')
    p1 = p1.replace('>Why Antibiotics Are Ineffective Against Viruses<', ' id="card-antibiotics-viruses" class="lecture-interactive-card" data-lecture-section="card_antibiotics_viruses">Why Antibiotics Are Ineffective Against Viruses<')
    p1 = p1.replace('>🧬 3. ANTIBIOTIC RESISTANCE &amp; MRSA<', ' id="sec-antibiotic-resistance" class="lecture-interactive-card" data-lecture-section="sec_antibiotic_resistance">🧬 3. ANTIBIOTIC RESISTANCE &amp; MRSA<')
    p1 = p1.replace('>🛡️ How to Limit the Development of Resistant Bacteria<', ' id="card-resistance-prevention" class="lecture-interactive-card" data-lecture-section="card_resistance_prevention">🛡️ How to Limit the Development of Resistant Bacteria<')

    # P2 replacements
    p2 = p2.replace('>💊 1. WHAT IS A DRUG? (Thuốc là gì?)<', ' id="sec-what-is-drug" class="lecture-interactive-card" data-lecture-section="sec_what_is_drug">💊 1. WHAT IS A DRUG? (Thuốc là gì?)<')
    p2 = p2.replace('>🦠 2. ANTIBIOTICS (Kháng sinh &amp; Cơ chế diệt khuẩn)<', ' id="sec-antibiotics" class="lecture-interactive-card" data-lecture-section="sec_antibiotics">🦠 2. ANTIBIOTICS (Kháng sinh &amp; Cơ chế diệt khuẩn)<')
    p2 = p2.replace('>Tại sao Kháng sinh vô dụng với Virus? (Why Antibiotics Do Not Affect Viruses)<', ' id="card-antibiotics-viruses" class="lecture-interactive-card" data-lecture-section="card_antibiotics_viruses">Tại sao Kháng sinh vô dụng với Virus? (Why Antibiotics Do Not Affect Viruses)<')
    p2 = p2.replace('>🧬 3. ANTIBIOTIC RESISTANCE &amp; MRSA (Kháng thuốc Kháng sinh)<', ' id="sec-antibiotic-resistance" class="lecture-interactive-card" data-lecture-section="sec_antibiotic_resistance">🧬 3. ANTIBIOTIC RESISTANCE &amp; MRSA (Kháng thuốc Kháng sinh)<')
    p2 = p2.replace('>🛡️ Các biện pháp kiểm soát và hạn chế vi khuẩn kháng thuốc<', ' id="card-resistance-prevention" class="lecture-interactive-card" data-lecture-section="card_resistance_prevention">🛡️ Các biện pháp kiểm soát và hạn chế vi khuẩn kháng thuốc<')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 15 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 15 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 16: Reproduction
# ==============================================================================
T16_ID = '936affb8-f062-4e39-b415-cc3794fb341e'
T16_CODE = '16'
T16_TITLE = 'Topic 16: Reproduction'

T16_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 16: Sinh sản & Chu kỳ Kinh nguyệt",
        "selector": "#sec-header",
        "en": "Welcome to Topic 16: Reproduction. Reproduction ensures the survival of species: Asexual reproduction produces genetically identical clones from a single parent by mitosis, while Sexual reproduction fuses haploid male and female gametes to create genetically diverse offspring. In this lesson, we study insect and wind plant pollination, human reproductive anatomy, the 28-day menstrual cycle, pregnancy, and STIs including HIV.",
        "vi": "Chào mừng các bạn đến với Bài 16: Sinh sản & Chu kỳ Kinh nguyệt. Sinh sản đảm bảo sự tồn tại của loài: Sinh sản vô tính tạo thế hệ con giống hệt bố mẹ từ một cá thể qua nguyên phân, còn sinh sản hữu tính kết hợp giao tử đực và cái đơn bội tạo biến dị di truyền. Trong bài học này, chúng ta sẽ học về thụ phấn ở hoa, giải phẫu sinh sản người, chu kỳ kinh nguyệt 28 ngày, thai kỳ và bệnh lây qua đường tình dục HIV."
    },
    {
        "id": "sec_asexual_vs_sexual",
        "title": "1. So sánh Sinh sản Vô tính và Hữu tính",
        "selector": "#sec-asexual-vs-sexual",
        "en": "Section 1: Asexual reproduction requires only one parent, producing offspring that are genetically identical clones without gametes or fertilisation. Sexual reproduction involves the fusion of haploid nuclei of male and female gametes during fertilisation to form a diploid zygote, creating genetic diversity that allows populations to adapt to changing environments.",
        "vi": "Mục 1: Sinh sản vô tính chỉ cần một cá thể bố mẹ, tạo con cái là các dòng nhân bản vô tính giống hệt nhau mà không cần giao tử hay thụ tinh. Sinh sản hữu tính là sự hợp nhất nhân đơn bội của giao tử đực và cái trong thụ tinh tạo hợp tử lưỡng bội, tạo biến dị di truyền giúp loài thích nghi với môi trường biến đổi."
    },
    {
        "id": "sec_plant_reproduction",
        "title": "2. Sinh sản Hữu tính ở Thực vật có Hoa (Thụ phấn & Nảy mầm)",
        "selector": "#sec-plant-reproduction",
        "en": "Section 2: Plant reproduction: Flowers feature male stamens with anthers producing pollen grains, and female carpels with stigmas, styles, and ovaries containing ovules. Insect-pollinated flowers have large colourful petals, scent, and sticky pollen. Wind-pollinated flowers have exposed dangling anthers and large feathery stigmas.",
        "vi": "Mục 2: Sinh sản ở thực vật có hoa: Hoa gồm nhị đực với bao phấn sản sinh hạt phấn, và nhụy cái gồm đầu nhụy, vòi nhụy và bầu nhụy chứa noãn. Hoa thụ phấn nhờ côn trùng có cánh hoa sặc sỡ, hương thơm và hạt phấn dính. Hoa thụ phấn nhờ gió có bao phấn thò ra ngoài đung đưa và đầu nhụy hình lông chim xòe rộng."
    },
    {
        "id": "card_seed_germination",
        "title": "🌱 3 Điều kiện Nảy mầm của Hạt ('WOW' Rule)",
        "selector": "#card-seed-germination",
        "en": "Seed germination conditions: Remember the acronym WOW: Water to activate metabolic enzymes and mobilize food reserves; Oxygen for cellular aerobic respiration to release ATP; and Warmth for optimum enzyme catalytic activity. Light is not required for germination of most seeds.",
        "vi": "Điều kiện nảy mầm của hạt: Ghi nhớ quy tắc WOW: Nước (Water) để hoạt hóa enzyme và hòa tan chất dinh dưỡng dự trữ; Oxy (Oxygen) để hô hấp tế bào hiếu khí giải phóng năng lượng ATP; và Nhiệt độ ấm (Warmth) cho enzyme hoạt động tối ưu. Ánh sáng không phải là điều kiện bắt buộc để hạt nảy mầm."
    },
    {
        "id": "sec_human_reproduction",
        "title": "3. Sinh sản ở Người: Thụ tinh, Nhau thai & Dây rốn",
        "selector": "#sec-human-reproduction",
        "en": "Section 3: Human reproduction: Fertilisation occurs in the oviduct when a sperm fertilizes an egg. The resulting embryo implants into the uterine endometrium. The placenta and umbilical cord transport oxygen, glucose, amino acids, and maternal antibodies to the fetus while removing carbon dioxide and urea, keeping fetal and maternal blood separate to prevent immune rejection and capillary damage.",
        "vi": "Mục 3: Sinh sản ở người: Thụ tinh diễn ra tại ống dẫn trứng khi tinh trùng kết hợp với trứng. Phôi làm tổ tại niêm mạc tử cung. Nhau thai và dây rốn vận chuyển oxy, glucose, axit amin và kháng thể mẹ sang thai nhi đồng thời đào thải CO2 và urê, giữ hai dòng máu tách biệt để chống đào thải miễn dịch và chênh lệch áp lực."
    },
    {
        "id": "sec_menstrual_cycle",
        "title": "4. Chu kỳ Kinh nguyệt & Sự Phối hợp Hooc-môn",
        "selector": "#sec-menstrual-cycle",
        "en": "Section 4: Menstrual cycle hormones: Pituitary FSH stimulates follicle development. Developing follicles secrete Oestrogen, which repairs the uterine lining and triggers an LH surge. LH causes ovulation at Day 14. The remaining corpus luteum secretes Progesterone, maintaining the thick lining for implantation.",
        "vi": "Mục 4: Điều hòa chu kỳ kinh nguyệt: FSH từ tuyến yên kích thích nang trứng phát triển. Nang trứng tiết Oestrogen làm dày niêm mạc tử cung và kích hoạt đỉnh LH. LH gây rụng trứng vào ngày 14. Hoàng thể còn lại tiết Progesterone giúp duy trì niêm mạc tử cung xốp dày sẵn sàng đón phôi làm tổ."
    },
    {
        "id": "card_stis_hiv",
        "title": "🛡️ 5. Bệnh Lây qua Đường Tình dục (STIs & HIV/AIDS)",
        "selector": "#card-stis-hiv",
        "en": "STIs and HIV: Human Immunodeficiency Virus is transmitted through direct contact of body fluids during unprotected intercourse or sharing contaminated hypodermic needles. HIV infects and destroys lymphocytes, collapsing the immune system into AIDS, leaving patients vulnerable to opportunistic pathogens.",
        "vi": "Bệnh tình dục và HIV: Virus gây suy giảm miễn dịch ở người HIV lây truyền qua tiếp xúc trực tiếp dịch cơ thể khi quan hệ không an toàn hoặc dùng chung kim tiêm dính máu. HIV tấn công và phá hủy tế bào lympho làm sụp đổ hệ miễn dịch chuyển sang giai đoạn AIDS khiến cơ thể mất khả năng chống đỡ các mầm bệnh cơ hội."
    }
]

T16_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_asexual_vs_sexual": {"start": 1, "end": 1},
    "sec-asexual-vs-sexual": {"start": 1, "end": 1},
    "sec_plant_reproduction": {"start": 2, "end": 3},
    "sec-plant-reproduction": {"start": 2, "end": 3},
    "sec_human_reproduction": {"start": 4, "end": 4},
    "sec-human-reproduction": {"start": 4, "end": 4},
    "sec_menstrual_cycle": {"start": 5, "end": 6},
    "sec-menstrual-cycle": {"start": 5, "end": 6}
}

def transform_topic16_html():
    with open('scripts/raw_bio_topics/t16_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t16_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 16: Reproduction</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Asexual vs Sexual, Flower Pollination, Human Reproduction, Menstrual Hormones &amp; HIV</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 16: Sinh sản &amp; Chu kỳ Kinh nguyệt</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Vô tính vs Hữu tính, Thụ phấn hoa, Sinh sản người, Điều hòa hormone kinh nguyệt &amp; HIV</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🔄 1. ASEXUAL VS SEXUAL REPRODUCTION<', ' id="sec-asexual-vs-sexual" class="lecture-interactive-card" data-lecture-section="sec_asexual_vs_sexual">🔄 1. ASEXUAL VS SEXUAL REPRODUCTION<')
    p1 = p1.replace('>🌺 2. SEXUAL REPRODUCTION IN PLANTS<', ' id="sec-plant-reproduction" class="lecture-interactive-card" data-lecture-section="sec_plant_reproduction">🌺 2. SEXUAL REPRODUCTION IN PLANTS<')
    p1 = p1.replace('>🚨 EXAM TIP: Environmental Conditions for Seed Germination ("WOW")<', ' id="card-seed-germination" class="lecture-interactive-card" data-lecture-section="card_seed_germination">🚨 EXAM TIP: Environmental Conditions for Seed Germination ("WOW")<')
    p1 = p1.replace('>👶 3. HUMAN REPRODUCTION<', ' id="sec-human-reproduction" class="lecture-interactive-card" data-lecture-section="sec_human_reproduction">👶 3. HUMAN REPRODUCTION<')
    p1 = p1.replace('>📈 4. THE MENSTRUAL CYCLE &amp; HORMONAL CONTROL<', ' id="sec-menstrual-cycle" class="lecture-interactive-card" data-lecture-section="sec_menstrual_cycle">📈 4. THE MENSTRUAL CYCLE &amp; HORMONAL CONTROL<')
    p1 = p1.replace('>🛡️ 5. SEXUALLY TRANSMITTED INFECTIONS', ' id="card-stis-hiv" class="lecture-interactive-card" data-lecture-section="card_stis_hiv">🛡️ 5. SEXUALLY TRANSMITTED INFECTIONS')

    # P2 replacements
    p2 = p2.replace('>🔄 1. ASEXUAL VS SEXUAL REPRODUCTION (Sinh sản Vô tính vs Hữu tính)<', ' id="sec-asexual-vs-sexual" class="lecture-interactive-card" data-lecture-section="sec_asexual_vs_sexual">🔄 1. ASEXUAL VS SEXUAL REPRODUCTION (Sinh sản Vô tính vs Hữu tính)<')
    p2 = p2.replace('>🌺 2. SEXUAL REPRODUCTION IN PLANTS (Sinh sản ở Thực vật)<', ' id="sec-plant-reproduction" class="lecture-interactive-card" data-lecture-section="sec_plant_reproduction">🌺 2. SEXUAL REPRODUCTION IN PLANTS (Sinh sản ở Thực vật)<')
    p2 = p2.replace('>🚨 BẪY ĐỀ THI: 3 Điều kiện bắt buộc để Hạt nảy mầm (Germination - WOW)<', ' id="card-seed-germination" class="lecture-interactive-card" data-lecture-section="card_seed_germination">🚨 BẪY ĐỀ THI: 3 Điều kiện bắt buộc để Hạt nảy mầm (Germination - WOW)<')
    p2 = p2.replace('>👶 3. HUMAN REPRODUCTION (Sinh sản ở người)<', ' id="sec-human-reproduction" class="lecture-interactive-card" data-lecture-section="sec_human_reproduction">👶 3. HUMAN REPRODUCTION (Sinh sản ở người)<')
    p2 = p2.replace('>📈 4. THE MENSTRUAL CYCLE (Chu kỳ Kinh nguyệt &amp; Điều hòa Hormone)<', ' id="sec-menstrual-cycle" class="lecture-interactive-card" data-lecture-section="sec_menstrual_cycle">📈 4. THE MENSTRUAL CYCLE (Chu kỳ Kinh nguyệt &amp; Điều hòa Hormone)<')
    p2 = p2.replace('>🛡️ 5. SEXUALLY TRANSMITTED INFECTIONS', ' id="card-stis-hiv" class="lecture-interactive-card" data-lecture-section="card_stis_hiv">🛡️ 5. SEXUALLY TRANSMITTED INFECTIONS')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 16 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 16 P2 div diff != 0"

    return p1, p2

# ==============================================================================
# TOPIC 17: Inheritance
# ==============================================================================
T17_ID = '77f1f7b8-f30e-4b0b-89e2-2e2482242791'
T17_CODE = '17'
T17_TITLE = 'Topic 17: Inheritance'

T17_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Topic 17: Cơ chế Di truyền (Inheritance)",
        "selector": "#sec-header",
        "en": "Welcome to Topic 17: Inheritance. Inheritance is the transmission of genetic information from generation to generation. In this lesson, we study chromosomes and the genetic code, the stages of protein synthesis, mitosis versus meiosis cell divisions, stem cells, monohybrid crosses with Punnett squares, ABO blood codominance, and pedigree diagrams.",
        "vi": "Chào mừng các bạn đến với Bài 17: Cơ chế Di truyền (Inheritance). Di truyền là sự truyền đạt thông tin di truyền qua các thế hệ. Trong bài học này, chúng ta sẽ học về nhiễm sắc thể và mã di truyền, các giai đoạn tổng hợp protein, phân bào nguyên phân và giảm phân, tế bào gốc, lai đơn tính với bảng Punnett, đồng trội nhóm máu ABO và sơ đồ phả hệ."
    },
    {
        "id": "sec_genetic_code",
        "title": "1. Cấu trúc Di truyền: Nhiễm sắc thể, Gen & Allele",
        "selector": "#sec-genetic-code",
        "en": "Section 1: Genetic hierarchy: A chromosome is a thread-like structure of DNA carrying genes. A gene is a length of DNA coding for a protein. An allele is an alternative version of a gene. A diploid nucleus has two complete sets of chromosomes, while a haploid gamete nucleus contains a single set.",
        "vi": "Mục 1: Trật tự di truyền: Nhiễm sắc thể là cấu trúc sợi dạng chuỗi của DNA mang các gen. Gen là một đoạn DNA mã hóa cho một phân tử protein. Allele là các trạng thái biểu hiện khác nhau của cùng một gen. Nhân lưỡng bội chứa hai bộ nhiễm sắc thể hoàn chỉnh, còn nhân đơn bội ở giao tử chỉ chứa một bộ đơn."
    },
    {
        "id": "card_protein_synthesis",
        "title": "⚙️ Quá trình Tổng hợp Protein (Transcription & Translation)",
        "selector": "#card-protein-synthesis",
        "en": "Protein synthesis mechanism: In the nucleus, the DNA code is transcribed into a complementary single-stranded messenger RNA molecule. mRNA travels out through nuclear pores to a ribosome in the cytoplasm. The ribosome reads the mRNA triplet codon sequence, linking specific amino acids together into a polypeptide protein chain.",
        "vi": "Cơ chế tổng hợp protein: Tại nhân tế bào, mã DNA được phiên mã thành phân tử mARN sợi đơn bổ sung. mARN đi qua lỗ màng nhân ra tế bào chất đến ribosome. Ribosome đọc trình tự bộ ba mã sao (codon) trên mARN và liên kết các axit amin tương ứng thành chuỗi polypeptide hoàn chỉnh."
    },
    {
        "id": "sec_cell_division",
        "title": "2. Phân bào: Nguyên phân (Mitosis) & Giảm phân (Meiosis)",
        "selector": "#sec-cell-division",
        "en": "Section 2: Nuclear divisions: Mitosis is nuclear division producing two genetically identical diploid cells for growth, tissue repair, and asexual reproduction. Meiosis is reduction division producing four genetically distinct haploid gametes, halving chromosome number for sexual reproduction.",
        "vi": "Mục 2: Phân chia nhân: Nguyên phân là phân bào tạo ra hai tế bào con lưỡng bội giống hệt nhau về mặt di truyền phục vụ sinh trưởng, phục hồi mô tổn thương và sinh sản vô tính. Giảm phân là phân bào giảm nhiễm tạo ra bốn giao tử đơn bội biến dị di truyền, giảm một nửa số nhiễm sắc thể phục vụ sinh sản hữu tính."
    },
    {
        "id": "card_stem_cells",
        "title": "💡 Tế bào Gốc (Stem Cells)",
        "selector": "#card-stem-cells",
        "en": "Stem cells: Unspecialised cells that retain the ability to divide indefinitely by mitosis and differentiate into distinct specialised cell types. Embryonic stem cells can form any body cell, whereas adult bone marrow stem cells differentiate primarily into blood cells.",
        "vi": "Tế bào gốc: Những tế bào chưa biệt hóa duy trì khả năng phân chia nguyên phân liên tục và có thể biệt hóa thành các loại tế bào chuyên trách khác nhau. Tế bào gốc phôi có thể phát triển thành bất kỳ loại tế bào nào, trong khi tế bào gốc tủy xương người lớn chủ yếu biệt hóa thành các tế bào máu."
    },
    {
        "id": "sec_monohybrid_inheritance",
        "title": "3. Di truyền Đơn gen, Bảng lai Punnett & Giới tính",
        "selector": "#sec-monohybrid-inheritance",
        "en": "Section 3: Monohybrid inheritance: Genotype is the genetic makeup; phenotype is the observable feature. A heterozygous cross between two carriers yields a classic three-to-one phenotypic ratio. Sex is determined by XX in human females and XY in human males, giving a fifty percent probability of each sex at conception.",
        "vi": "Mục 3: Di truyền đơn gen: Kiểu gen là tổ hợp các gen; kiểu hình là đặc điểm biểu hiện ra ngoài quan sát được. Phép lai giữa hai cá thể dị hợp tử tạo tỉ lệ phân ly kiểu hình kinh điển 3 trội : 1 lặn. Giới tính được quyết định bởi cặp XX ở nữ và XY ở nam, cho xác suất 50% nam : 50% nữ trong mỗi lần thụ thai."
    },
    {
        "id": "card_codominance_blood",
        "title": "🩸 4. Đồng trội, Nhóm Máu ABO & Sơ đồ Phả hệ",
        "selector": "#card-codominance-blood",
        "en": "Codominance and Pedigrees: Codominance occurs when both alleles are expressed in the phenotype, as in blood group AB where alleles IA and IB are codominant over recessive Io. Pedigree family tree diagrams trace inherited phenotypes across generations to determine carrier probabilities and autosomal dominant versus recessive patterns.",
        "vi": "Đồng trội và Sơ đồ Phả hệ: Hiện tượng đồng trội xảy ra khi cả hai allele đều biểu hiện ra kiểu hình, như nhóm máu AB khi allele IA và IB cùng trội so với allele lặn Io. Sơ đồ phả hệ gia đình theo dõi sự di truyền kiểu hình qua các thế hệ để tính xác suất người lành mang gen và xác định quy luật di truyền trội hay lặn."
    }
]

T17_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_genetic_code": {"start": 1, "end": 2},
    "sec-genetic-code": {"start": 1, "end": 2},
    "sec_cell_division": {"start": 3, "end": 4},
    "sec-cell-division": {"start": 3, "end": 4},
    "sec_monohybrid_inheritance": {"start": 5, "end": 6},
    "sec-monohybrid-inheritance": {"start": 5, "end": 6}
}

def transform_topic17_html():
    with open('scripts/raw_bio_topics/t17_p1.html', 'r', encoding='utf-8') as f:
        p1 = f.read()
    with open('scripts/raw_bio_topics/t17_p2.html', 'r', encoding='utf-8') as f:
        p2 = f.read()

    header_p1 = '''<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; border-radius: 14px; padding: 25px 30px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15); cursor: pointer; border: 1px solid #334155;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px;">
        <div>
            <span style="display: inline-block; background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; margin-bottom: 8px;">Cambridge IGCSE Biology (0610)</span>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Topic 17: Inheritance</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Genetic Code, Protein Synthesis, Mitosis vs Meiosis, Punnett Squares &amp; Blood Codominance</p>
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
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #f8fafc;">Chuyên đề 17: Cơ chế Di truyền (Inheritance)</h1>
            <p style="margin: 6px 0 0 0; color: #94a3b8; font-size: 15px;">Mã di truyền, Tổng hợp protein, Nguyên phân/Giảm phân, Bảng Punnett &amp; Nhóm máu ABO</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 8px 16px; font-weight: 600; font-size: 14px; color: #34d399;">
            <span>🎧 Bấm vào bất kỳ thẻ nào để nghe giảng</span>
        </div>
    </div>
</div>'''

    p1 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p1, p1, count=1, flags=re.DOTALL) if 'id="sec-header"' in p1 else header_p1 + '\n' + p1
    p2 = re.sub(r'<div id="sec-header"[^>]*>.*?</div>', header_p2, p2, count=1, flags=re.DOTALL) if 'id="sec-header"' in p2 else header_p2 + '\n' + p2

    # P1 replacements
    p1 = p1.replace('>🧬 1. CHROMOSOMES, DNA &amp; PROTEIN SYNTHESIS<', ' id="sec-genetic-code" class="lecture-interactive-card" data-lecture-section="sec_genetic_code">🧬 1. CHROMOSOMES, DNA &amp; PROTEIN SYNTHESIS<')
    p1 = p1.replace('>⚙️ How Proteins Are Made (Interactive Diagram)<', ' id="card-protein-synthesis" class="lecture-interactive-card" data-lecture-section="card_protein_synthesis">⚙️ How Proteins Are Made (Interactive Diagram)<')
    p1 = p1.replace('>➗ 2. CELL DIVISION (Mitosis vs Meiosis) &amp; STEM CELLS<', ' id="sec-cell-division" class="lecture-interactive-card" data-lecture-section="sec_cell_division">➗ 2. CELL DIVISION (Mitosis vs Meiosis) &amp; STEM CELLS<')
    p1 = p1.replace('>💡 Stem Cells (Cambridge Syllabus 17.2.5)<', ' id="card-stem-cells" class="lecture-interactive-card" data-lecture-section="card_stem_cells">💡 Stem Cells (Cambridge Syllabus 17.2.5)<')
    p1 = p1.replace('>🧮 3. MONOHYBRID INHERITANCE &amp; PUNNETT SQUARE<', ' id="sec-monohybrid-inheritance" class="lecture-interactive-card" data-lecture-section="sec_monohybrid_inheritance">🧮 3. MONOHYBRID INHERITANCE &amp; PUNNETT SQUARE<')
    p1 = p1.replace('>🩸 4. CODOMINANCE, BLOOD GROUPS &amp; PEDIGREE DIAGRAMS<', ' id="card-codominance-blood" class="lecture-interactive-card" data-lecture-section="card_codominance_blood">🩸 4. CODOMINANCE, BLOOD GROUPS &amp; PEDIGREE DIAGRAMS<')

    # P2 replacements
    p2 = p2.replace('id="sec-genetic-code-vi"', 'id="sec-genetic-code"')
    p2 = p2.replace('>⚙️ Quá trình Tổng hợp Protein (Interactive Protein Synthesis)<', ' id="card-protein-synthesis" class="lecture-interactive-card" data-lecture-section="card_protein_synthesis">⚙️ Quá trình Tổng hợp Protein (Interactive Protein Synthesis)<')
    p2 = p2.replace('>➗ 2. CELL DIVISION (Nguyên phân vs Giảm phân) &amp; TẾ BÀO GỐC<', ' id="sec-cell-division" class="lecture-interactive-card" data-lecture-section="sec_cell_division">➗ 2. CELL DIVISION (Nguyên phân vs Giảm phân) &amp; TẾ BÀO GỐC<')
    p2 = p2.replace('>💡 Stem Cells (Tế bào gốc)<', ' id="card-stem-cells" class="lecture-interactive-card" data-lecture-section="card_stem_cells">💡 Stem Cells (Tế bào gốc)<')
    p2 = p2.replace('>🧮 3. MONOHYBRID INHERITANCE (Di truyền đơn gen) &amp; BẢNG LAI PUNNETT<', ' id="sec-monohybrid-inheritance" class="lecture-interactive-card" data-lecture-section="sec_monohybrid_inheritance">🧮 3. MONOHYBRID INHERITANCE (Di truyền đơn gen) &amp; BẢNG LAI PUNNETT<')
    p2 = p2.replace('>🩸 4. CODOMINANCE, NHÓM MÁU ABO &amp; PHẢ HỆ (Pedigree Diagrams)<', ' id="card-codominance-blood" class="lecture-interactive-card" data-lecture-section="card_codominance_blood">🩸 4. CODOMINANCE, NHÓM MÁU ABO &amp; PHẢ HỆ (Pedigree Diagrams)<')

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

    assert p1.count('<div') - p1.count('</div>') == 0, f"Topic 17 P1 div diff != 0"
    assert p2.count('<div') - p2.count('</div>') == 0, f"Topic 17 P2 div diff != 0"

    return p1, p2

async def build_batch4():
    tasks = [
        ("Topic 14", T14_CODE, T14_ID, T14_TITLE, T14_SEGMENTS, T14_MAJOR_SECTIONS, transform_topic14_html),
        ("Topic 15", T15_CODE, T15_ID, T15_TITLE, T15_SEGMENTS, T15_MAJOR_SECTIONS, transform_topic15_html),
        ("Topic 16", T16_CODE, T16_ID, T16_TITLE, T16_SEGMENTS, T16_MAJOR_SECTIONS, transform_topic16_html),
        ("Topic 17", T17_CODE, T17_ID, T17_TITLE, T17_SEGMENTS, T17_MAJOR_SECTIONS, transform_topic17_html)
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
    asyncio.run(build_batch4())
