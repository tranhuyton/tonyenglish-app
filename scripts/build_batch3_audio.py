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
# B11: GAS EXCHANGE IN HUMANS
# =====================================================================
B11_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B11: Trao đổi Khí ở Người",
        "selector": "#sec-header",
        "en": "Welcome to Topic B11: Gas Exchange in Humans. Cellular respiration requires a continuous supply of oxygen and the removal of metabolic carbon dioxide. In this topic, we study gas exchange surfaces, respiratory anatomy, ventilation mechanics, and the effects of physical exercise.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B11: Trao đổi Khí ở Người. Hô hấp tế bào đòi hỏi nguồn cung cấp oxy liên tục và sự đào thải carbon dioxide chuyển hóa. Trong chuyên đề này, chúng ta sẽ học về bề mặt trao đổi khí, giải phẫu hệ hô hấp, cơ chế thông khí và tác động của hoạt động thể lực."
    },
    {
        "id": "sec_gas_exchange_surfaces",
        "title": "1. Đặc điểm Bề mặt Trao đổi Khí (Gas Exchange Surfaces Overview)",
        "selector": "#sec-gas-exchange-surfaces",
        "en": "Section 1 examines gas exchange surfaces: In humans, gas exchange takes place across microscopic alveoli in the lungs. To maximize diffusion rate, gas exchange surfaces have five key adaptations.",
        "vi": "Mục một khảo sát bề mặt trao đổi khí: Ở người, sự trao đổi khí diễn ra qua các phế nang vi thể trong phổi. Để tối đa hóa tốc độ khuếch tán, bề mặt trao đổi khí có 5 đặc điểm thích nghi cốt lõi."
    },
    {
        "id": "sec_gas_adaptations",
        "title": "🫁 Five Adaptations of Alveoli (Năm Thích nghi của Phế nang)",
        "selector": "#sec-gas-adaptations",
        "en": "Five alveolar adaptations: 1. Enormous surface area of ~70 m² provided by millions of alveoli. 2. Extremely thin diffusion barrier only one cell thick (under 1 µm). 3. Dense capillary network maintaining a steep concentration gradient. 4. Constant ventilation renewing fresh air. 5. Moist lining dissolving gases for rapid diffusion.",
        "vi": "Năm đặc điểm thích nghi của phế nang: Một là diện tích bề mặt khổng lồ khoảng 70 mét vuông từ hàng triệu phế nang. Hai là màng khuếch tán cực mỏng chỉ dày một lớp tế bào. Ba là mạng lưới mao mạch dày đặc duy trì gradient nồng độ dốc. Bốn là cử động thông khí liên tục làm mới không khí. Năm là lớp dịch ẩm hòa tan khí để khuếch tán nhanh."
    },
    {
        "id": "sec_respiratory_system",
        "title": "2. Cấu tạo Hệ Hô hấp & Bảo vệ Đường thở (Respiratory Anatomy Overview)",
        "selector": "#sec-respiratory-system",
        "en": "Section 2 investigates the anatomy of the respiratory tract: Trachea, bronchi, bronchioles, alveoli, lungs, ribs, intercostal muscles, and the diaphragm, protected by mucus and cilia.",
        "vi": "Mục hai nghiên cứu giải phẫu đường hô hấp: Khí quản, phế quản, tiểu phế quản, phế nang, phổi, lồng xương sườn, cơ liên sườn và cơ hoành, được bảo vệ bởi chất nhầy và lông rung."
    },
    {
        "id": "sec_resp_trachea_cartilage",
        "title": "🛡️ Trachea & Cartilage Rings (Khí quản & Vòng sụn chữ C)",
        "selector": "#sec-resp-trachea-cartilage",
        "en": "The trachea is reinforced with C-shaped rings of cartilage. Cartilage keeps the airway permanently open and prevents the trachea from collapsing inwards when pressure drops during inhalation.",
        "vi": "Khí quản được gia cố bằng các vòng sụn hình chữ C. Sụn giữ cho đường thở luôn mở và ngăn không cho khí quản bị xẹp xuống khi áp suất giảm trong lúc hít vào."
    },
    {
        "id": "sec_resp_goblet_cilia",
        "title": "🧹 Goblet Cells & Cilia (Tế bào Hình đài & Biểu mô Lông rung)",
        "selector": "#sec-resp-goblet-cilia",
        "en": "Airway defense: Goblet cells secrete sticky mucus to trap inhaled dust, bacteria, and airborne pathogens. Ciliated epithelial cells beat rhythmically in synchronized waves to sweep the mucus up to the pharynx, where it is safely swallowed into stomach acid.",
        "vi": "Hàng rào bảo vệ đường thở: Tế bào hình đài tiết chất nhầy dính giữ lại bụi bẩn, vi khuẩn và mầm bệnh từ không khí. Các tế bào biểu mô lông rung chuyển động nhịp nhàng quét lớp nhầy lên họng để nuốt xuống dạ dày tiêu diệt bằng acid."
    },
    {
        "id": "sec_ventilation_mechanics",
        "title": "3. Cơ chế Thông khí & Khí Hít vào/Thở ra (Ventilation Mechanics Overview)",
        "selector": "#sec-ventilation-mechanics",
        "en": "Section 3 investigates breathing movements and gas composition: Muscle contractions alter thoracic volume, changing internal lung pressure to draw air in or expel it out.",
        "vi": "Mục ba khảo sát cử động hô hấp và thành phần khí: Sự co giãn của các cơ làm thay đổi thể tích khoang ngực, biến đổi áp suất bên trong phổi để hút không khí vào hoặc đẩy ra ngoài."
    },
    {
        "id": "sec_inhalation_exhalation",
        "title": "⚖️ Mechanics of Breathing (Cơ chế Hít vào & Thở ra)",
        "selector": "#sec-inhalation-exhalation",
        "en": "Breathing mechanics: During inhalation, external intercostal muscles contract, ribs move up and out, diaphragm contracts and flattens; thorax volume increases, pressure drops below atmospheric, drawing air in. During exhalation, external intercostals relax, ribs move down and in, diaphragm relaxes and curves up; thorax volume decreases, pressure rises, pushing air out.",
        "vi": "Cơ chế hít thở: Khi hít vào, cơ liên sườn ngoài co kéo xương sườn nâng lên và nở ra, cơ hoành co phẳng xuống; thể tích khoang ngực tăng, áp suất giảm hút khí vào. Khi thở ra, cơ liên sườn ngoài giãn xương sườn hạ xuống, cơ hoành giãn cong lên hình vòm; thể tích khoang ngực giảm, áp suất tăng đẩy khí ra."
    },
    {
        "id": "sec_inspired_expired",
        "title": "📊 Composition of Air & Exercise (Thành phần Khí & Thể dục)",
        "selector": "#sec-inspired-expired",
        "en": "Gas comparison: Inspired air contains 21% oxygen, 0.04% carbon dioxide, and variable water vapour. Expired air contains 16% oxygen, 4% carbon dioxide, and saturated water vapour. During exercise, muscle cells respire faster; the brain detects increased CO₂ in blood and stimulates faster, deeper breathing.",
        "vi": "So sánh thành phần khí: Khí hít vào chứa 21% oxy, 0.04% CO2 và hơi nước thay đổi. Khí thở ra chứa 16% oxy, 4% CO2 và bão hòa hơi nước. Khi vận động thể thao, cơ bắp hô hấp mạnh hơn; não phát hiện CO2 tăng trong máu sẽ kích thích thở nhanh hơn và sâu hơn."
    }
]

B11_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_gas_exchange_surfaces": {"start": 1, "end": 2},
    "sec-gas-exchange-surfaces": {"start": 1, "end": 2},
    "sec_gas_adaptations": {"start": 2, "end": 2},
    "sec-gas-adaptations": {"start": 2, "end": 2},
    "sec_respiratory_system": {"start": 3, "end": 5},
    "sec-respiratory-system": {"start": 3, "end": 5},
    "sec_resp_trachea_cartilage": {"start": 4, "end": 4},
    "sec-resp-trachea-cartilage": {"start": 4, "end": 4},
    "sec_resp_goblet_cilia": {"start": 5, "end": 5},
    "sec-resp-goblet-cilia": {"start": 5, "end": 5},
    "sec_ventilation_mechanics": {"start": 6, "end": 8},
    "sec-ventilation-mechanics": {"start": 6, "end": 8},
    "sec_inhalation_exhalation": {"start": 7, "end": 7},
    "sec-inhalation-exhalation": {"start": 7, "end": 7},
    "sec_inspired_expired": {"start": 8, "end": 8},
    "sec-inspired-expired": {"start": 8, "end": 8}
}

# =====================================================================
# B12: RESPIRATION
# =====================================================================
B12_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B12: Hô hấp Tế bào & Năng lượng Sinh học",
        "selector": "#sec-header",
        "en": "Welcome to Topic B12: Respiration and Bioenergetics. Respiration is the fundamental biochemical process releasing usable ATP energy in all living cells. In this topic, we contrast aerobic and anaerobic respiration and examine oxygen debt.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B12: Hô hấp Tế bào và Năng lượng Sinh học. Hô hấp là chuỗi phản ứng sinh hóa cốt lõi giải phóng năng lượng ATP trong mọi tế bào sống. Trong chuyên đề này, chúng ta sẽ so sánh hô hấp hiếu khí, kỵ khí và hiện tượng nợ oxy."
    },
    {
        "id": "sec_bioenergetics",
        "title": "1. Hô hấp Tế bào & Ứng dụng Năng lượng (Bioenergetics Overview)",
        "selector": "#sec-bioenergetics",
        "en": "Section 1 defines respiration: The chemical reactions in cells that break down nutrient molecules and release energy for metabolism.",
        "vi": "Mục một định nghĩa hô hấp tế bào: Là chuỗi phản ứng hóa học trong tế bào phân giải phân tử dinh dưỡng để giải phóng năng lượng cho các hoạt động trao đổi chất."
    },
    {
        "id": "sec_respiration_def",
        "title": "🔋 Seven Vital Uses of ATP Energy (Bảy Ứng dụng của Năng lượng)",
        "selector": "#sec-respiration-def",
        "en": "Uses of released energy: 1. Muscle contraction. 2. Protein synthesis. 3. Cell division for growth. 4. Active transport of ions. 5. Growth and repair of tissues. 6. Transmission of nerve impulses. 7. Maintenance of a constant body temperature in mammals.",
        "vi": "Bảy ứng dụng của năng lượng giải phóng: 1. Co cơ vận động. 2. Tổng hợp protein. 3. Phân chia tế bào lớn lên. 4. Vận chuyển chủ động qua màng. 5. Tăng trưởng và phục hồi mô. 6. Dẫn truyền xung thần kinh. 7. Duy trì thân nhiệt ổn định ở động vật có vú."
    },
    {
        "id": "sec_aerobic_respiration",
        "title": "2. Hô hấp Hiếu khí & Phương trình Hóa học (Aerobic Respiration Overview)",
        "selector": "#sec-aerobic-respiration",
        "en": "Section 2 investigates aerobic respiration: The chemical reactions in cells that use oxygen to break down nutrient molecules to release energy. Word equation: glucose plus oxygen yields carbon dioxide plus water. Balanced chemical equation: C₆H₁₂O₆ + 6O₂ produces 6CO₂ + 6H₂O, releasing large amounts of ATP.",
        "vi": "Mục hai phân tích hô hấp hiếu khí: Là phản ứng hóa học trong tế bào sử dụng oxy để phân giải chất dinh dưỡng giải phóng năng lượng. Phương trình chữ: glucose cộng oxy tạo ra carbon dioxide cộng nước. Phương trình hóa học: C6H12O6 cộng 6O2 tạo ra 6CO2 cộng 6H2O, giải phóng lượng lớn ATP."
    },
    {
        "id": "sec_anaerobic_respiration",
        "title": "3. Hô hấp Kỵ khí, Lên men & Nợ Oxy (Anaerobic Respiration Overview)",
        "selector": "#sec-anaerobic-respiration",
        "en": "Section 3 investigates anaerobic respiration: The chemical reactions in cells that break down nutrient molecules to release energy without using oxygen, yielding much less energy per glucose molecule.",
        "vi": "Mục ba nghiên cứu hô hấp kỵ khí: Là phản ứng hóa học phân giải chất dinh dưỡng giải phóng năng lượng mà không dùng oxy, tạo ra ít năng lượng hơn nhiều trên mỗi phân tử glucose."
    },
    {
        "id": "sec_anaerobic_muscles",
        "title": "🏃 Anaerobic Respiration in Muscles (Hô hấp Kỵ khí ở Cơ bắp)",
        "selector": "#sec-anaerobic-muscles",
        "en": "In human muscle cells during vigorous exercise: When oxygen supply cannot meet muscle demands, glucose is broken down anaerobically into lactic acid. Word equation: glucose yields lactic acid. Lactic acid accumulation causes muscle fatigue and cramps.",
        "vi": "Ở cơ bắp người khi vận động gắng sức: Khi lượng oxy hít vào không đủ đáp ứng, glucose bị phân giải kỵ khí thành acid lactic. Phương trình chữ: glucose tạo ra acid lactic. Sự tích tụ acid lactic làm mỏi cơ và chuột rút."
    },
    {
        "id": "sec_anaerobic_yeast",
        "title": "🍞 Anaerobic Respiration in Yeast (Lên men Rượu ở Nấm men)",
        "selector": "#sec-anaerobic-yeast",
        "en": "In yeast (fermentation): Glucose is broken down into alcohol (ethanol) and carbon dioxide. Word equation: glucose yields alcohol plus carbon dioxide. Equation: C₆H₁₂O₆ yields 2C₂H₅OH + 2CO₂. Used commercially in breadmaking (CO₂ causes dough to rise) and brewing alcohol.",
        "vi": "Ở nấm men (lên men rượu): Glucose bị phân giải thành cồn ethanol và carbon dioxide. Phương trình: C6H12O6 tạo ra 2 C2H5OH cộng 2 CO2. Ứng dụng trong làm bánh mì (khí CO2 làm nở bột) và sản xuất bia rượu."
    },
    {
        "id": "sec_oxygen_debt",
        "title": "🩸 Oxygen Debt (Hiện tượng Nợ Oxy)",
        "selector": "#sec-oxygen-debt",
        "en": "Oxygen debt: After vigorous sprinting, deep breathing continues to repay the oxygen debt. Blood transports accumulated lactic acid from muscles to the liver, where extra oxygen is consumed to oxidise lactic acid aerobically into carbon dioxide and water.",
        "vi": "Nợ oxy: Sau khi chạy nước rút, ta tiếp tục thở gấp để trả nợ oxy. Máu vận chuyển acid lactic tích tụ từ cơ bắp về gan, nơi oxy bổ sung được dùng để oxy hóa hiếu khí acid lactic thành CO2 và nước."
    }
]

B12_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_bioenergetics": {"start": 1, "end": 2},
    "sec-bioenergetics": {"start": 1, "end": 2},
    "sec_respiration_def": {"start": 2, "end": 2},
    "sec-respiration-def": {"start": 2, "end": 2},
    "sec_aerobic_respiration": {"start": 3, "end": 3},
    "sec-aerobic-respiration": {"start": 3, "end": 3},
    "sec_anaerobic_respiration": {"start": 4, "end": 7},
    "sec-anaerobic-respiration": {"start": 4, "end": 7},
    "sec_anaerobic_muscles": {"start": 5, "end": 5},
    "sec-anaerobic-muscles": {"start": 5, "end": 5},
    "sec_anaerobic_yeast": {"start": 6, "end": 6},
    "sec-anaerobic-yeast": {"start": 6, "end": 6},
    "sec_oxygen_debt": {"start": 7, "end": 7},
    "sec-oxygen-debt": {"start": 7, "end": 7}
}

# =====================================================================
# B13: COORDINATION AND RESPONSE
# =====================================================================
B13_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B13: Điều hòa, Phản xạ & Cân bằng Nội môi",
        "selector": "#sec-header",
        "en": "Welcome to Topic B13: Coordination and Response. Organisms detect internal and external stimuli and execute coordinated responses via the nervous and endocrine systems, maintaining physiological homeostasis.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B13: Điều hòa, Phản xạ và Cân bằng Nội môi. Sinh vật nhận biết kích thích môi trường và thực hiện các đáp ứng phối hợp nhịp nhàng thông qua hệ thần kinh và hệ nội tiết để duy trì cân bằng nội môi."
    },
    {
        "id": "sec_nervous_reflex",
        "title": "1. Hệ Thần kinh & Cung Phản xạ (Nervous System & Reflex Arc Overview)",
        "selector": "#sec-nervous-reflex",
        "en": "Section 1 examines the nervous system: The central nervous system consists of the brain and spinal cord. Reflex arcs provide rapid, involuntary, automatic protection against hazards.",
        "vi": "Mục một khảo sát hệ thần kinh: Hệ thần kinh trung ương gồm não bộ và tủy sống. Cung phản xạ mang lại các phản ứng tự động, tức thì và không chủ ý để bảo vệ cơ thể khỏi nguy hiểm."
    },
    {
        "id": "sec_reflex_arc_path",
        "title": "⚡ Reflex Arc Pathway (Đường dẫn truyền Cung Phản xạ)",
        "selector": "#sec-reflex-arc-path",
        "en": "Reflex arc pathway: Stimulus detected by receptor ➔ Sensory neurone transmits electrical impulses to CNS ➔ Relay neurone in spinal cord grey matter ➔ Motor neurone conducts impulse to effector ➔ Effector (muscle contracts or gland secretes) carries out immediate response.",
        "vi": "Đường dẫn truyền cung phản xạ: Kích thích được thụ thể phát hiện ➔ Nơ-ron cảm giác truyền xung điện về tủy sống ➔ Nơ-ron trung gian xử lý tại chất xám ➔ Nơ-ron vận động dẫn truyền xung đến cơ quan đáp ứng ➔ Cơ bắp co hoặc tuyến tiết dịch thực hiện phản xạ tức thì."
    },
    {
        "id": "sec_endocrine_system",
        "title": "2. Tuyến Nội tiết & Hormone (Endocrine System Overview)",
        "selector": "#sec-endocrine-system",
        "en": "Section 2 investigates hormones: A hormone is a chemical substance produced by an endocrine gland and carried by the blood, which alters the activity of one or more specific target organs.",
        "vi": "Mục hai nghiên cứu hormone: Hormone là chất hóa học do tuyến nội tiết tiết ra và được máu vận chuyển đi khắp cơ thể, làm biến đổi hoạt động của một hoặc nhiều cơ quan đích xác định."
    },
    {
        "id": "sec_endocrine_glands",
        "title": "🧪 Key Hormones: Adrenaline & Insulin (Adrenaline & Insulin)",
        "selector": "#sec-endocrine-glands",
        "en": "Key hormones: Adrenal glands secrete adrenaline in 'fight or flight' situations, accelerating heart rate, dilating pupils, and boosting blood glucose. The pancreas secretes insulin to lower blood glucose by converting it to glycogen, and glucagon to raise glucose levels.",
        "vi": "Các hormone chính: Tuyến thượng thận tiết adrenaline trong tình huống khẩn cấp, làm tim đập nhanh, giãn đồng tử và tăng đường huyết. Tuyến tụy tiết insulin để hạ đường huyết chuyển thành glycogen dự trữ, và glucagon để nâng đường huyết khi đói."
    },
    {
        "id": "sec_homeostasis",
        "title": "3. Cân bằng Nội môi & Điều nhiệt Da (Homeostasis & Thermoregulation Overview)",
        "selector": "#sec-homeostasis",
        "en": "Section 3 investigates homeostasis: The maintenance of a constant internal environment, such as regulating core body temperature at 37°C and stabilizing blood glucose levels.",
        "vi": "Mục ba nghiên cứu cân bằng nội môi: Là sự duy trì ổn định của môi trường bên trong cơ thể, ví dụ như điều hòa thân nhiệt ở 37°C và ổn định nồng độ glucose trong máu."
    },
    {
        "id": "sec_skin_thermo",
        "title": "🌡️ Skin Thermoregulation Mechanics (Cơ chế Điều nhiệt của Da)",
        "selector": "#sec-skin-thermo",
        "en": "Skin temperature control: When hot, arterioles undergo vasodilation to increase blood flow to surface capillaries for heat radiation, sweat glands secrete sweat which evaporates to cool the skin, and hair muscles relax so hairs lie flat. When cold, vasoconstriction diverts blood away from the skin surface, shivering generates metabolic heat, and hair muscles contract causing hairs to stand erect trapping an insulating layer of warm air.",
        "vi": "Cơ chế điều nhiệt của da: Khi trời nóng, tiểu động mạch giãn (vasodilation) tăng lưu lượng máu đến mao mạch dưới da để tỏa nhiệt, tuyến mồ hôi tiết mồ hôi bốc hơi làm mát da, lông nằm rạp. Khi trời lạnh, tiểu động mạch co (vasoconstriction) hạn chế mất nhiệt, run cơ sinh nhiệt, lông dựng đứng giữ lớp khí ấm cách nhiệt."
    }
]

B13_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_nervous_reflex": {"start": 1, "end": 2},
    "sec-nervous-reflex": {"start": 1, "end": 2},
    "sec_reflex_arc_path": {"start": 2, "end": 2},
    "sec-reflex-arc-path": {"start": 2, "end": 2},
    "sec_endocrine_system": {"start": 3, "end": 4},
    "sec-endocrine-system": {"start": 3, "end": 4},
    "sec_endocrine_glands": {"start": 4, "end": 4},
    "sec-endocrine-glands": {"start": 4, "end": 4},
    "sec_homeostasis": {"start": 5, "end": 6},
    "sec-homeostasis": {"start": 5, "end": 6},
    "sec_skin_thermo": {"start": 6, "end": 6},
    "sec-skin-thermo": {"start": 6, "end": 6}
}

# =====================================================================
# B14: DRUGS & ANTIBIOTICS
# =====================================================================
B14_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B14: Thuốc, Kháng sinh & Kháng thuốc",
        "selector": "#sec-header",
        "en": "Welcome to Topic B14: Drugs and Antibiotics. A drug is any substance taken into the body that modifies or affects chemical reactions. In this topic, we examine antibiotics, explain why they are ineffective against viruses, and analyze the development of antibiotic-resistant superbugs like MRSA.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B14: Thuốc, Kháng sinh và Kháng thuốc. Thuốc là bất kỳ chất nào đưa vào cơ thể làm thay đổi hoặc ảnh hưởng đến các phản ứng hóa sinh. Trong chuyên đề này, chúng ta sẽ tìm hiểu về kháng sinh, lý do kháng sinh vô dụng với virus và sự xuất hiện của siêu vi khuẩn kháng thuốc như MRSA."
    },
    {
        "id": "sec_what_is_drug",
        "title": "1. Khái niệm về Thuốc (What is a Drug? Overview)",
        "selector": "#sec-what-is-drug",
        "en": "Section 1 defines a drug: A drug is any substance taken into the body that modifies or affects chemical reactions in the body. Medicinal drugs treat symptoms or cure diseases; non-medicinal drugs alter mood or perception.",
        "vi": "Mục một định nghĩa thuốc: Thuốc là bất kỳ chất nào đưa vào cơ thể làm biến đổi hoặc ảnh hưởng đến các phản ứng hóa học trong cơ thể. Thuốc y tế dùng để điều trị triệu chứng hoặc chữa bệnh; chất kích thích làm thay đổi tâm trạng hoặc tri giác."
    },
    {
        "id": "sec_antibiotics",
        "title": "2. Kháng sinh & Vì sao Vô dụng với Virus (Antibiotics Overview)",
        "selector": "#sec-antibiotics",
        "en": "Section 2 investigates antibiotics: Chemical substances produced by microorganisms (like Penicillium fungus) that kill or inhibit the growth of bacteria. Crucially, antibiotics are completely ineffective against viral diseases like influenza or HIV.",
        "vi": "Mục hai nghiên cứu thuốc kháng sinh: Là các hợp chất hóa học do vi sinh vật (như nấm Penicillium) tiết ra để tiêu diệt hoặc ức chế vi khuẩn. Điểm cốt lõi: Kháng sinh hoàn toàn vô dụng trước các bệnh do virus như cúm hay HIV."
    },
    {
        "id": "sec_antibiotics_target",
        "title": "🦠 Why Antibiotics Don't Affect Viruses (Kháng sinh & Virus)",
        "selector": "#sec-antibiotics-target",
        "en": "Mechanism: Antibiotics target bacterial cellular structures, such as disrupting bacterial peptidoglycan cell walls or inhibiting bacterial protein synthesis. Viruses have no cell walls, no cell membrane, and no independent metabolic machinery; they replicate exclusively inside host human cells, remaining invulnerable to antibiotics.",
        "vi": "Cơ chế: Kháng sinh tấn công vào cấu trúc tế bào vi khuẩn, như phá hủy thành tế bào peptidoglycan hoặc ức chế tổng hợp protein vi khuẩn. Virus không có thành tế bào, không có màng sinh chất và không có bộ máy chuyển hóa độc lập; chúng nhân lên bên trong tế bào chủ nên kháng sinh không thể tác động."
    },
    {
        "id": "sec_mrsa_crisis",
        "title": "3. Kháng Kháng sinh & Siêu vi khuẩn MRSA (Antibiotic Resistance Overview)",
        "selector": "#sec-mrsa-crisis",
        "en": "Section 3 examines antibiotic resistance: Natural selection among bacteria leads to the survival and reproduction of mutant resistant strains when antibiotics are overused.",
        "vi": "Mục ba phân tích hiện tượng kháng kháng sinh: Chọn lọc tự nhiên ở vi khuẩn dẫn đến sự sống sót và sinh sôi của các chủng đột biến kháng thuốc khi kháng sinh bị lạm dụng."
    },
    {
        "id": "sec_resistance_selection",
        "title": "🧬 Natural Selection of Resistance (Chọn lọc Tự nhiên Kháng thuốc)",
        "selector": "#sec-resistance-selection",
        "en": "Mechanism of resistance: 1. Random mutation in bacterial DNA creates a gene conferring resistance. 2. When treated with antibiotic, non-resistant bacteria die, removing competition. 3. The mutant resistant bacterium survives and reproduces rapidly by binary fission. 4. All offspring inherit the resistance gene, forming an antibiotic-resistant strain like MRSA.",
        "vi": "Cơ chế kháng thuốc: 1. Đột biến ngẫu nhiên trong DNA vi khuẩn tạo gen kháng thuốc. 2. Khi dùng kháng sinh, vi khuẩn không kháng bị tiêu diệt, làm mất sự cạnh tranh. 3. Vi khuẩn đột biến kháng thuốc sống sót và sinh sôi nhanh chóng qua phân đôi. 4. Toàn bộ thế hệ con cháu mang gen kháng thuốc, tạo nên chủng siêu vi khuẩn như MRSA."
    }
]

B11_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_gas_exchange_surfaces": {"start": 1, "end": 2},
    "sec-gas-exchange-surfaces": {"start": 1, "end": 2},
    "sec_gas_adaptations": {"start": 2, "end": 2},
    "sec-gas-adaptations": {"start": 2, "end": 2},
    "sec_respiratory_system": {"start": 3, "end": 5},
    "sec-respiratory-system": {"start": 3, "end": 5},
    "sec_resp_trachea_cartilage": {"start": 4, "end": 4},
    "sec-resp-trachea-cartilage": {"start": 4, "end": 4},
    "sec_resp_goblet_cilia": {"start": 5, "end": 5},
    "sec-resp-goblet-cilia": {"start": 5, "end": 5},
    "sec_ventilation_mechanics": {"start": 6, "end": 8},
    "sec-ventilation-mechanics": {"start": 6, "end": 8},
    "sec_inhalation_exhalation": {"start": 7, "end": 7},
    "sec-inhalation-exhalation": {"start": 7, "end": 7},
    "sec_inspired_expired": {"start": 8, "end": 8},
    "sec-inspired-expired": {"start": 8, "end": 8}
}

B14_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_what_is_drug": {"start": 1, "end": 1},
    "sec-what-is-drug": {"start": 1, "end": 1},
    "sec_antibiotics": {"start": 2, "end": 3},
    "sec-antibiotics": {"start": 2, "end": 3},
    "sec_antibiotics_target": {"start": 3, "end": 3},
    "sec-antibiotics-target": {"start": 3, "end": 3},
    "sec_mrsa_crisis": {"start": 4, "end": 5},
    "sec-mrsa-crisis": {"start": 4, "end": 5},
    "sec_resistance_selection": {"start": 5, "end": 5},
    "sec-resistance-selection": {"start": 5, "end": 5}
}

async def main():
    print("=================================================================")
    print("STARTING BATCH 3 AUDIO GENERATION (B11, B12, B13, B14)")
    print("=================================================================")
    
    # Process B11
    await process_lecture_audio(
        lecture_code="b11",
        lecture_id="39003a2f-708e-47fe-b8ad-7aae073273a3",
        course_title=COURSE_TITLE,
        lecture_title="B11: Gas exchange in humans",
        segments=B11_SEGMENTS,
        major_sections=B11_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B12
    await process_lecture_audio(
        lecture_code="b12",
        lecture_id="58e65add-a67a-4b90-8b84-52de1a2840be",
        course_title=COURSE_TITLE,
        lecture_title="B12: Respiration",
        segments=B12_SEGMENTS,
        major_sections=B12_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B13
    await process_lecture_audio(
        lecture_code="b13",
        lecture_id="2637d6ee-fd5f-48fc-aa7a-fc794fb3e561",
        course_title=COURSE_TITLE,
        lecture_title="B13: Coordination and response",
        segments=B13_SEGMENTS,
        major_sections=B13_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B14
    await process_lecture_audio(
        lecture_code="b14",
        lecture_id="7ed510d0-acd2-4d0a-9079-1f1e4e4fc463",
        course_title=COURSE_TITLE,
        lecture_title="B14: Drugs",
        segments=B14_SEGMENTS,
        major_sections=B14_MAJOR_SECTIONS,
        subject="science"
    )
    
    print("\n🎉 BATCH 3 (B11, B12, B13, B14) AUDIO & MANIFESTS GENERATION COMPLETED!")

if __name__ == "__main__":
    asyncio.run(main())
