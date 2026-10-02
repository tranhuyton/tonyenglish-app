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
# B7: HUMAN NUTRITION
# =====================================================================
B7_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B7: Dinh dưỡng Người & Hệ Tiêu hóa",
        "selector": "#sec-header",
        "en": "Welcome to Topic B7: Human Nutrition and Digestive System. Heterotrophic animals must ingest, digest, absorb, and assimilate food to survive. In this topic, we study balanced diets, deficiency diseases, the anatomy of the alimentary canal, and chemical digestion by digestive enzymes.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B7: Dinh dưỡng Người và Hệ Tiêu hóa. Động vật dị dưỡng phải thu nhận, tiêu hóa, hấp thu và đồng hóa thức ăn để tồn tại. Trong chuyên đề này, chúng ta sẽ học về chế độ ăn cân bằng, bệnh thiếu hụt dinh dưỡng, giải phẫu ống tiêu hóa và quá trình tiêu hóa hóa học nhờ enzyme."
    },
    {
        "id": "sec_balanced_diet",
        "title": "1. Chế độ Ăn Cân bằng & Nhu cầu Dinh dưỡng (Balanced Diet Overview)",
        "selector": "#sec-balanced-diet",
        "en": "Section 1 defines a balanced diet: A balanced diet provides all seven essential food groups in correct quantities and proportions for metabolic health, repair, and energy: carbohydrates, fats, proteins, vitamins, minerals, fibre, and water.",
        "vi": "Mục một định nghĩa chế độ ăn cân bằng: Một khẩu phần ăn cân bằng cung cấp đầy đủ cả 7 nhóm dưỡng chất thiết yếu với số lượng và tỷ lệ hợp lý cho chuyển hóa, phục hồi và năng lượng: carbohydrate, chất béo, protein, vitamin, khoáng chất, chất xơ và nước."
    },
    {
        "id": "sec_diet_nutrients",
        "title": "🥗 Seven Food Groups & Functions (Bảy Nhóm Dinh dưỡng)",
        "selector": "#sec-diet-nutrients",
        "en": "The seven food groups: Carbohydrates provide immediate energy. Fats provide long-term energy storage and insulation. Proteins build muscle and synthesise enzymes. Fibre stimulates peristalsis in intestines. Water acts as a universal solvent and reaction medium.",
        "vi": "Bảy nhóm chất dinh dưỡng: Carbohydrate cung cấp năng lượng tức thì. Chất béo dự trữ năng lượng lâu dài và cách nhiệt. Protein xây dựng cơ bắp và tổng hợp enzyme. Chất xơ kích thích nhu động ruột. Nước đóng vai trò là dung môi và môi trường diễn ra mọi phản ứng sống."
    },
    {
        "id": "sec_diet_deficiencies",
        "title": "⚠️ Nutritional Deficiency Diseases (Bệnh Thiếu hụt Dinh dưỡng)",
        "selector": "#sec-diet-deficiencies",
        "en": "Deficiency diseases: Lack of Vitamin C causes scurvy with bleeding gums and poor wound healing. Lack of Vitamin D or calcium causes rickets with soft, deformed bones. Lack of iron impairs haemoglobin synthesis, causing anaemia with chronic fatigue. Protein deficiency leads to kwashiorkor.",
        "vi": "Các bệnh thiếu hụt: Thiếu vitamin C gây bệnh scorbut làm chảy máu chân răng và vết thương lâu lành. Thiếu vitamin D hoặc canxi gây bệnh còi xương làm xương mềm và biến dạng. Thiếu sắt cản trở tạo hemoglobin gây bệnh thiếu máu mệt mỏi. Thiếu hụt protein gây bệnh kwashiorkor."
    },
    {
        "id": "sec_food_processing",
        "title": "2. Năm Giai đoạn Tiêu hóa Thức ăn (5 Stages of Food Processing)",
        "selector": "#sec-food-processing",
        "en": "Section 2 presents the five stages of food processing: 1. Ingestion is taking substances into the mouth. 2. Digestion breaks down large insoluble food molecules into small soluble molecules. 3. Absorption moves small nutrients across the intestinal wall into the blood. 4. Assimilation is the uptake and use of absorbed nutrients by body cells. 5. Egestion passes out undigested food as faeces through the anus.",
        "vi": "Mục hai trình bày 5 giai đoạn tiêu hóa thức ăn: Một là Ăn vào (Ingestion) qua miệng. Hai là Tiêu hóa (Digestion) phân giải thức ăn lớn không tan thành phân tử nhỏ tan được. Ba là Hấp thu (Absorption) đưa chất dinh dưỡng qua niêm mạc ruột vào máu. Bốn là Đồng hóa (Assimilation) khi tế bào hấp thụ và sử dụng dưỡng chất. Năm là Tống phân (Egestion) thải thức ăn không tiêu hóa ra ngoài qua hậu môn."
    },
    {
        "id": "sec_digestive_system",
        "title": "3. Giải phẫu Ống Tiêu hóa (Alimentary Canal Anatomy Overview)",
        "selector": "#sec-digestive-system",
        "en": "Section 3 examines the human alimentary canal: Mouth, oesophagus, stomach, small intestine, and large intestine, assisted by accessory organs including the liver, gallbladder, and pancreas.",
        "vi": "Mục ba khảo sát ống tiêu hóa ở người: Miệng, thực quản, dạ dày, ruột non và ruột già, cùng các tuyến phụ trợ gồm gan, túi mật và tuyến tụy."
    },
    {
        "id": "sec_organ_mouth",
        "title": "👄 Mouth & Oesophagus (Miệng & Thực quản)",
        "selector": "#sec-organ-mouth",
        "en": "In the mouth, teeth chew food for mechanical digestion while salivary amylase begins chemical digestion of starch. The tongue forms a bolus swallowed into the oesophagus, where peristaltic waves of muscle contraction push food down to the stomach.",
        "vi": "Tại khoang miệng, răng nhai nghiền thức ăn để tiêu hóa cơ học trong khi amylase nước bọt bắt đầu tiêu hóa hóa học tinh bột. Lưỡi viên thức ăn thành viên nuốt xuống thực quản, nơi các làn sóng nhu động cơ đẩy thức ăn xuống dạ dày."
    },
    {
        "id": "sec_organ_stomach",
        "title": "🍲 Stomach Mechanics & Gastric Juice (Dạ dày & Dịch vị)",
        "selector": "#sec-organ-stomach",
        "en": "The stomach churns food mechanically. Its lining secretes gastric juice containing protease enzyme pepsin, which breaks down proteins, and hydrochloric acid at pH 2, which kills ingested bacteria and creates the optimum acidic pH for pepsin.",
        "vi": "Dạ dày co bóp nhào trộn thức ăn cơ học. Niêm mạc tiết dịch vị chứa enzyme protease pepsin giúp phân cắt protein, và acid clohydric ở pH 2 giúp diệt vi khuẩn đồng thời tạo môi trường acid tối ưu cho pepsin hoạt động."
    },
    {
        "id": "sec_organ_liver_pancreas",
        "title": "🥑 Liver, Gallbladder & Pancreas (Gan, Túi mật & Tuyến tụy)",
        "selector": "#sec-organ-liver-pancreas",
        "en": "The liver produces bile stored in the gallbladder. The pancreas secretes pancreatic juice into the duodenum containing amylase, trypsin, lipase, and sodium hydrogencarbonate to neutralise stomach acid.",
        "vi": "Gan sản xuất dịch mật được dự trữ trong túi mật. Tuyến tụy tiết dịch tụy vào tá tràng chứa enzyme amylase, trypsin, lipase và muối kiềm hydrogencarbonate giúp trung hòa acid dạ dày."
    },
    {
        "id": "sec_organ_intestines",
        "title": "🌾 Small & Large Intestines (Ruột non & Ruột già)",
        "selector": "#sec-organ-intestines",
        "en": "The small intestine (duodenum and ileum) completes digestion and absorbs nutrients into blood. The large intestine (colon) reabsorbs water and mineral ions, turning remaining waste into semi-solid faeces stored in the rectum.",
        "vi": "Ruột non (tá tràng và hồi tràng) hoàn tất quá trình tiêu hóa và hấp thu chất dinh dưỡng vào máu. Ruột già (đại tràng) tái hấp thu nước và muối khoáng, chuyển bã cặn thành phân bán rắn tích trữ ở trực tràng."
    },
    {
        "id": "sec_chemical_digestion",
        "title": "4. Tiêu hóa Hóa học, Enzyme & Mật (Enzymes & Bile Overview)",
        "selector": "#sec-chemical-digestion",
        "en": "Section 4 covers chemical digestion: Enzymes break bonds in large insoluble molecules into small soluble molecules so they can be absorbed into blood capillaries.",
        "vi": "Mục bốn phân tích tiêu hóa hóa học: Các enzyme bẻ gãy liên kết trong phân tử lớn không tan thành phân tử nhỏ hòa tan được để có thể hấp thu vào mao mạch máu."
    },
    {
        "id": "sec_enzymes_action",
        "title": "🧪 Digestive Enzymes Action (Hành động của các Enzyme)",
        "selector": "#sec-enzymes-action",
        "en": "Enzyme actions: Amylase digests starch into maltose; maltase digests maltose into glucose. Proteases (pepsin and trypsin) digest proteins into amino acids. Lipase digests lipids into fatty acids and glycerol.",
        "vi": "Cơ chế enzyme: Amylase thủy phân tinh bột thành maltose; maltase phân giải maltose thành glucose. Protease (pepsin và trypsin) phân giải protein thành amino acid. Lipase phân giải chất béo thành acid béo và glycerol."
    },
    {
        "id": "sec_bile_role",
        "title": "🥑 Essential Roles of Bile (Vai trò Thiết yếu của Dịch Mật)",
        "selector": "#sec-bile-role",
        "en": "Bile roles: Bile is an alkaline fluid produced by the liver. It neutralises acidic chyme entering the duodenum from the stomach, providing optimum pH 8 for intestinal enzymes. It also emulsifies large lipid globules into tiny droplets, greatly increasing surface area for lipase action.",
        "vi": "Vai trò của dịch mật: Dịch mật là dịch kiềm do gan tiết ra. Mật trung hòa dưỡng trấp acid từ dạ dày xuống tá tràng, tạo môi trường pH 8 tối ưu cho enzyme ruột. Mật còn nhũ tương hóa giọt mỡ lớn thành hàng triệu hạt mỡ li ti, làm tăng diện tích bề mặt tiếp xúc cho enzyme lipase."
    },
    {
        "id": "sec_villi_absorption",
        "title": "🔬 Small Intestine Villi Adaptations (Cấu tạo Thích nghi của Lông Ruột)",
        "selector": "#sec-villi-absorption",
        "en": "Villi adaptations: Millions of microscopic finger-like projections called villi and microvilli create an enormous surface area. Each villus has a thin one-cell-thick epithelium, a rich blood capillary network for absorbing glucose and amino acids, and a central lacteal vessel for absorbing fatty acids and glycerol.",
        "vi": "Cấu tạo thích nghi của lông ruột: Hàng triệu nhung mao và vi nhung mao hình ngón tay tạo nên diện tích hấp thu khổng lồ. Mỗi nhung mao có lớp biểu mô mỏng chỉ một lớp tế bào, mạng lưới mao mạch máu dày đặc để hấp thu glucose và amino acid, cùng mạch bạch huyết (lacteal) trung tâm để hấp thu acid béo và glycerol."
    }
]

B7_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_balanced_diet": {"start": 1, "end": 3},
    "sec-balanced-diet": {"start": 1, "end": 3},
    "sec_diet_nutrients": {"start": 2, "end": 2},
    "sec-diet-nutrients": {"start": 2, "end": 2},
    "sec_diet_deficiencies": {"start": 3, "end": 3},
    "sec-diet-deficiencies": {"start": 3, "end": 3},
    "sec_food_processing": {"start": 4, "end": 4},
    "sec-food-processing": {"start": 4, "end": 4},
    "sec_digestive_system": {"start": 5, "end": 9},
    "sec-digestive-system": {"start": 5, "end": 9},
    "sec_organ_mouth": {"start": 6, "end": 6},
    "sec-organ-mouth": {"start": 6, "end": 6},
    "sec_organ_stomach": {"start": 7, "end": 7},
    "sec-organ-stomach": {"start": 7, "end": 7},
    "sec_organ_liver_pancreas": {"start": 8, "end": 8},
    "sec-organ-liver-pancreas": {"start": 8, "end": 8},
    "sec_organ_intestines": {"start": 9, "end": 9},
    "sec-organ-intestines": {"start": 9, "end": 9},
    "sec_chemical_digestion": {"start": 10, "end": 13},
    "sec-chemical-digestion": {"start": 10, "end": 13},
    "sec_enzymes_action": {"start": 11, "end": 11},
    "sec-enzymes-action": {"start": 11, "end": 11},
    "sec_bile_role": {"start": 12, "end": 12},
    "sec-bile-role": {"start": 12, "end": 12},
    "sec_villi_absorption": {"start": 13, "end": 13},
    "sec-villi-absorption": {"start": 13, "end": 13}
}

# =====================================================================
# B8: TRANSPORT IN PLANTS
# =====================================================================
B8_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B8: Vận chuyển ở Thực vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic B8: Transport in Plants. Plants possess specialized vascular tissues, xylem and phloem, to transport water, minerals, and synthesized organic solutes throughout roots, stems, and leaves.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B8: Vận chuyển ở Thực vật. Cây cối sở hữu các mô mạch chuyên hóa gồm mạch gỗ (xylem) và mạch rây (phloem) để vận chuyển nước, ion khoáng và các chất hữu cơ tổng hợp khắp rễ, thân và lá."
    },
    {
        "id": "sec_xylem_phloem",
        "title": "1. Mạch Gỗ & Mạch Rây (Xylem & Phloem Overview)",
        "selector": "#sec-xylem-phloem",
        "en": "Section 1 compares xylem and phloem: Xylem vessels conduct water and mineral ions unidirectionally upwards. Phloem sieve tubes translocate sucrose and amino acids bidirectionally between sources and sinks.",
        "vi": "Mục một so sánh mạch gỗ và mạch rây: Mạch gỗ dẫn nước và ion khoáng một chiều từ dưới lên trên. Mạch rây vận chuyển đường sucrose và amino acid hai chiều giữa cơ quan nguồn và cơ quan chứa."
    },
    {
        "id": "sec_xylem_tissue",
        "title": "💧 Xylem Structure & Adaptations (Cấu trúc Mạch Gỗ)",
        "selector": "#sec-xylem-tissue",
        "en": "Xylem adaptations: Composed of dead cells with no cytoplasm or organelles, forming a hollow lumen. End walls are completely broken down into continuous uninterrupted pipelines. Cell walls are heavily thickened with waterproof lignin, preventing inward collapse and providing mechanical support.",
        "vi": "Cấu tạo mạch gỗ: Gồm các tế bào chết không chứa bào quan, tạo nên lòng ống rỗng thông suốt. Thành ngăn ngang bị tiêu biến tạo đường ống dẫn liên tục. Thành tế bào được tẩm lignin dày chống thấm nước, giúp ống không bị bẹp dưới lực hút căng và nâng đỡ thân cây."
    },
    {
        "id": "sec_phloem_tissue",
        "title": "🍯 Phloem Characteristics (Đặc tính Mạch Rây)",
        "selector": "#sec-phloem-tissue",
        "en": "Phloem characteristics: Composed of living cells containing thin strands of cytoplasm. Transports sucrose and amino acids bidirectionally: downwards from leaves to roots or upwards from storage tubers to developing buds.",
        "vi": "Đặc tính mạch rây: Gồm các tế bào sống chứa dải tế bào chất mỏng. Vận chuyển đường sucrose và amino acid hai chiều: đi xuống từ lá đến rễ hoặc đi lên từ củ dự trữ đến các chồi non đang đâm lộc."
    },
    {
        "id": "sec_vascular_position",
        "title": "2. Vị trí Bó Mạch ở Cây Hai Lá Mầm (Position in Dicot Organs Overview)",
        "selector": "#sec-vascular-position",
        "en": "Section 2 examines dicot organ transverse sections: Remember the golden rule: Xylem is rigid and lignified, positioned towards the center or inside. Phloem is softer, positioned towards the outside or periphery.",
        "vi": "Mục hai khảo sát lát cắt ngang các cơ quan cây hai lá mầm: Quy tắc vàng: Mạch gỗ cứng cáp nằm hướng vào phía trong hoặc trung tâm. Mạch rây mềm hơn nằm hướng ra phía ngoài ngoại vi."
    },
    {
        "id": "sec_pos_roots",
        "title": "🌱 Vascular Bundle in Roots (Bó Mạch ở Rễ)",
        "selector": "#sec-pos-roots",
        "en": "In roots: Xylem forms a solid central X-shaped or star-shaped core to withstand tugging forces. Phloem bundles sit neatly between the arms of the xylem core.",
        "vi": "Ở rễ: Mạch gỗ tạo thành lõi trung tâm hình chữ X hoặc hình sao vững chắc giúp chống lại lực kéo nhổ. Các bó mạch rây nằm xen kẽ giữa các cánh tay của lõi mạch gỗ."
    },
    {
        "id": "sec_pos_stems",
        "title": "🎋 Vascular Bundle in Stems (Bó Mạch ở Thân)",
        "selector": "#sec-pos-stems",
        "en": "In stems: Vascular bundles are arranged in a regular circular ring around the cortex. Xylem is located on the inner side of each bundle, while phloem is on the outer side.",
        "vi": "Ở thân: Các bó mạch xếp thành một vòng tròn đồng đều xung quanh lớp vỏ. Mạch gỗ nằm ở phía trong của mỗi bó, còn mạch rây nằm ở phía ngoài."
    },
    {
        "id": "sec_pos_leaves",
        "title": "🍃 Vascular Bundle in Leaves (Bó Mạch ở Lá)",
        "selector": "#sec-pos-leaves",
        "en": "In leaves: Vascular bundles form the midrib and veins. Xylem is located in the upper half of each vein near the upper epidermis, while phloem is in the lower half.",
        "vi": "Ở lá: Các bó mạch tạo nên gân chính và gân phụ. Mạch gỗ nằm ở nửa trên của gân gần biểu bì trên, trong khi mạch rây nằm ở nửa dưới."
    },
    {
        "id": "sec_transpiration",
        "title": "3. Hút Nước & Thoát Hơi Nước (Transpiration & Water Uptake Overview)",
        "selector": "#sec-transpiration",
        "en": "Section 3 investigates water uptake and transpiration: Water enters root hairs by osmosis, crosses the cortex, travels up xylem vessels by transpiration pull, and evaporates from leaf mesophyll cells out through open stomata.",
        "vi": "Mục ba nghiên cứu sự hút nước và thoát hơi nước: Nước thẩm thấu vào lông hút, đi qua vỏ rễ, leo lên mạch gỗ nhờ lực hút thoát hơi nước và bốc hơi từ tế bào mô giậu qua khí khổng ra ngoài."
    },
    {
        "id": "sec_transpiration_pull",
        "title": "🌬️ Transpiration Pull & Cohesion (Lực Hút Thoát Hơi Nước)",
        "selector": "#sec-transpiration-pull",
        "en": "Transpiration pull mechanism: Evaporation of water vapour from leaf mesophyll cells lowers water potential, generating a suction force called transpiration pull. Strong cohesive hydrogen bonds between water molecules pull a continuous unbroken water column up xylem vessels.",
        "vi": "Cơ chế lực hút thoát hơi nước: Nước bốc hơi từ tế bào mô lá làm giảm thế nước, sinh ra lực hút thoát hơi nước. Lực liên kết hydro gắn kết giữa các phân tử nước kéo một cột nước liên tục không đứt đoạn đi lên dọc mạch gỗ."
    },
    {
        "id": "sec_transpiration_factors",
        "title": "📊 Factors Affecting Transpiration Rate (Các Yếu tố Ảnh hưởng)",
        "selector": "#sec-transpiration-factors",
        "en": "Factors affecting transpiration: Higher temperature increases kinetic energy and rate. Higher wind speed blows away humid air, increasing rate. Higher light opens stomata, increasing rate. Higher humidity decreases concentration gradient, reducing transpiration rate.",
        "vi": "Các yếu tố ảnh hưởng: Nhiệt độ tăng làm tăng động năng và tăng thoát hơi nước. Gió mạnh thổi bay hơi ẩm xung quanh lá làm tăng thoát nước. Ánh sáng mạnh mở khí khổng làm tăng thoát nước. Độ ẩm không khí tăng làm giảm chênh lệch nồng độ, khiến tốc độ thoát hơi nước giảm."
    },
    {
        "id": "sec_translocation",
        "title": "4. Vận Chuyển Dòng Luyện (Translocation Overview)",
        "selector": "#sec-translocation",
        "en": "Section 4 examines translocation: the movement of sucrose and amino acids in phloem from regions of production (sources) to regions of storage or utilization (sinks).",
        "vi": "Mục bốn phân tích vận chuyển dòng luyện: là sự di chuyển của sucrose và amino acid trong mạch rây từ nơi sản xuất (cơ quan nguồn) đến nơi dự trữ hoặc tiêu thụ (cơ quan chứa)."
    },
    {
        "id": "sec_sources_sinks",
        "title": "🔄 Sources and Sinks (Cơ quan Nguồn & Cơ quan Chứa)",
        "selector": "#sec-sources-sinks",
        "en": "Sources and sinks: In summer, mature green leaves photosynthesise excess sugars, acting as sources, while roots and growing fruits act as sinks. In early spring, underground tubers hydrolyse stored starch into sucrose, acting as sources supplying growing young shoots and bud sinks.",
        "vi": "Nguồn và chứa: Vào mùa hè, lá xanh quang hợp tạo nhiều đường đóng vai trò là nguồn, còn rễ và quả non là cơ quan chứa. Vào đầu mùa xuân, củ dưới đất phân giải tinh bột thành sucrose đóng vai trò là nguồn cung cấp dinh dưỡng cho các chồi non đang mọc."
    }
]

B8_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_xylem_phloem": {"start": 1, "end": 3},
    "sec-xylem-phloem": {"start": 1, "end": 3},
    "sec_xylem_tissue": {"start": 2, "end": 2},
    "sec-xylem-tissue": {"start": 2, "end": 2},
    "sec_phloem_tissue": {"start": 3, "end": 3},
    "sec-phloem-tissue": {"start": 3, "end": 3},
    "sec_vascular_position": {"start": 4, "end": 7},
    "sec-vascular-position": {"start": 4, "end": 7},
    "sec_pos_roots": {"start": 5, "end": 5},
    "sec-pos-roots": {"start": 5, "end": 5},
    "sec_pos_stems": {"start": 6, "end": 6},
    "sec-pos-stems": {"start": 6, "end": 6},
    "sec_pos_leaves": {"start": 7, "end": 7},
    "sec-pos-leaves": {"start": 7, "end": 7},
    "sec_transpiration": {"start": 8, "end": 10},
    "sec-transpiration": {"start": 8, "end": 10},
    "sec_transpiration_pull": {"start": 9, "end": 9},
    "sec-transpiration-pull": {"start": 9, "end": 9},
    "sec_transpiration_factors": {"start": 10, "end": 10},
    "sec-transpiration-factors": {"start": 10, "end": 10},
    "sec_translocation": {"start": 11, "end": 12},
    "sec-translocation": {"start": 11, "end": 12},
    "sec_sources_sinks": {"start": 12, "end": 12},
    "sec-sources-sinks": {"start": 12, "end": 12}
}

# =====================================================================
# B9: TRANSPORT IN ANIMALS
# =====================================================================
B9_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B9: Hệ Tuần hoàn & Máu ở Động vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic B9: Transport in Animals. Mammals require a double circulatory system comprising a four-chambered heart, specialized blood vessels, and blood components to distribute oxygen and nutrients while removing metabolic wastes.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B9: Hệ Tuần hoàn và Máu ở Động vật. Động vật có vú cần hệ tuần hoàn kép với trái tim bốn ngăn, hệ mạch chuyên hóa và các thành phần máu để phân phối oxy và dưỡng chất đồng thời thu gom chất thải chuyển hóa."
    },
    {
        "id": "sec_circulation_system",
        "title": "1. Hệ Tuần hoàn Kép (Circulatory Systems Overview)",
        "selector": "#sec-circulation-system",
        "en": "Section 1 introduces circulatory systems: Mammals have a double circulation where blood passes through the heart twice during one complete circuit: the pulmonary circulation to the lungs and the systemic circulation to body tissues. Double circulation maintains high arterial pressure for active endothermic lifestyles.",
        "vi": "Mục một giới thiệu hệ tuần hoàn: Động vật có vú có hệ tuần hoàn kép, trong đó máu đi qua tim hai lần trong một vòng tuần hoàn hoàn chỉnh: vòng tuần hoàn phổi và vòng tuần hoàn hệ thống đến các cơ quan. Tuần hoàn kép duy trì áp lực máu cao đáp ứng lối sống hoạt động nhiều."
    },
    {
        "id": "sec_heart_anatomy",
        "title": "2. Cấu tạo & Hoạt động của Tim (Mammalian Heart Structure Overview)",
        "selector": "#sec-heart-anatomy",
        "en": "Section 2 investigates the mammalian heart: Four chambers (right and left atria, right and left ventricles), separated by the muscular septum to prevent mixing of oxygenated and deoxygenated blood.",
        "vi": "Mục hai khảo sát trái tim thú: Gồm bốn ngăn (tâm nhĩ phải và trái, tâm thất phải và trái), được ngăn cách bởi vách liên thất cơ bắp giúp ngăn ngừa sự pha trộn giữa máu giàu oxy và máu nghèo oxy."
    },
    {
        "id": "sec_heart_structure",
        "title": "❤️ Heart Chambers & Valves (Các Ngăn Tim & Van Tim)",
        "selector": "#sec-heart-structure",
        "en": "Heart chambers and valves: Atria receive blood and pump it into ventricles. The left ventricle has a much thicker muscular wall than the right because it must pump blood at high pressure throughout the entire body. Atrioventricular and semilunar valves prevent backflow of blood.",
        "vi": "Các ngăn và van tim: Tâm nhĩ nhận máu và đẩy xuống tâm thất. Tâm thất trái có thành cơ dày hơn hẳn tâm thất phải vì phải co bóp tống máu với áp lực cao đi khắp toàn bộ cơ thể. Các van nhĩ thất và van bán nguyệt ngăn dòng máu chảy ngược."
    },
    {
        "id": "sec_heart_bloodflow",
        "title": "🩸 Pathway of Blood Flow (Hành trình Dòng máu qua Tim)",
        "selector": "#sec-heart-bloodflow",
        "en": "Pathway of blood: Deoxygenated blood returns via the vena cava to the right atrium, passes to the right ventricle, and is pumped via pulmonary arteries to the lungs. Oxygenated blood returns via pulmonary veins to the left atrium, passes to the left ventricle, and is pumped out through the aorta to the body.",
        "vi": "Hành trình máu: Máu nghèo oxy về tĩnh mạch chủ vào tâm nhĩ phải, xuống tâm thất phải rồi được bơm qua động mạch phổi lên phổi. Máu giàu oxy trở về theo tĩnh mạch phổi vào tâm nhĩ trái, xuống tâm thất trái rồi được tống qua động mạch chủ đi khắp cơ thể."
    },
    {
        "id": "sec_chd",
        "title": "3. Bệnh Mạch Vành (Coronary Heart Disease Overview)",
        "selector": "#sec-chd",
        "en": "Section 3 examines Coronary Heart Disease: Blockage of coronary arteries supplying oxygen to heart muscle cells, leading to angina or myocardial infarction.",
        "vi": "Mục ba nghiên cứu Bệnh động mạch vành: Sự tắc nghẽn các nhánh động mạch vành nuôi dưỡng cơ tim do mảng xơ vữa, dẫn đến thiếu oxy gây cơn đau thắt ngực hoặc nhồi máu cơ tim."
    },
    {
        "id": "sec_chd_causes",
        "title": "🍔 CHD Risk Factors & Prevention (Nguyên nhân & Phòng ngừa)",
        "selector": "#sec-chd-causes",
        "en": "CHD risk factors include high saturated fat diet, smoking, chronic stress, lack of exercise, and genetic predisposition. Preventive measures include regular aerobic exercise, a diet rich in unsaturated fats, and stopping smoking.",
        "vi": "Các yếu tố nguy cơ của bệnh mạch vành gồm: ăn nhiều chất béo bão hòa, hút thuốc lá, căng thẳng kéo dài, ít vận động và di truyền. Biện pháp phòng tránh gồm tập thể dục đều đặn, ăn nhiều chất béo không bão hòa và cai thuốc lá."
    },
    {
        "id": "sec_vessels_blood",
        "title": "4. Mạch Máu & Thành phần Máu (Blood Vessels & Blood Overview)",
        "selector": "#sec-vessels_blood",
        "en": "Section 4 covers blood vessels and blood components: Arteries carry blood away from the heart under high pressure; veins return blood under low pressure; capillaries exchange nutrients and wastes with tissue fluid.",
        "vi": "Mục bốn phân tích mạch máu và thành phần máu: Động mạch dẫn máu rời khỏi tim dưới áp lực cao; tĩnh mạch dẫn máu về tim dưới áp lực thấp; mao mạch trao đổi dưỡng chất và chất thải với dịch mô."
    },
    {
        "id": "sec_vessels_types",
        "title": "🧪 Arteries, Veins & Capillaries (So sánh Ba Loại Mạch Máu)",
        "selector": "#sec-vessels_types",
        "en": "Vessel comparison: Arteries have thick muscular elastic walls and narrow lumens to withstand high pressure. Veins have thinner walls, wide lumens, and semilunar valves to ensure one-way flow. Capillaries are microscopic, one-cell-thick vessels allowing rapid diffusion.",
        "vi": "So sánh mạch máu: Động mạch có thành cơ dày đàn hồi và lòng hẹp để chịu áp lực cao. Tĩnh mạch có thành mỏng hơn, lòng rộng và có van bán nguyệt đảm bảo dòng máu chảy một chiều. Mao mạch có kích thước vi thể với thành mỏng chỉ một lớp tế bào giúp khuếch tán nhanh chóng."
    },
    {
        "id": "sec_blood_components",
        "title": "🔬 Blood Composition & Clotting (Thành phần Máu & Cơ chế Đông máu)",
        "selector": "#sec-blood-components",
        "en": "Blood composition: Red blood cells contain haemoglobin for oxygen transport. White blood cells defend against pathogens: phagocytes engulf pathogens, lymphocytes produce antibodies. Platelets release clotting factors converting soluble fibrinogen into an insoluble fibrin mesh, trapping blood cells to form a scab.",
        "vi": "Thành phần máu: Hồng cầu chứa hemoglobin để chở oxy. Bạch cầu bảo vệ cơ thể: thực bào nuốt mầm bệnh, tế bào lympho tiết kháng thể. Tiểu cầu kích hoạt đông máu chuyển fibrinogen hòa tan thành mạng lưới sợi fibrin không tan, giam giữ tế bào máu tạo thành vảy cầm máu."
    }
]

B9_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_circulation_system": {"start": 1, "end": 1},
    "sec-circulation-system": {"start": 1, "end": 1},
    "sec_heart_anatomy": {"start": 2, "end": 4},
    "sec-heart-anatomy": {"start": 2, "end": 4},
    "sec_heart_structure": {"start": 3, "end": 3},
    "sec-heart-structure": {"start": 3, "end": 3},
    "sec_heart_bloodflow": {"start": 4, "end": 4},
    "sec-heart-bloodflow": {"start": 4, "end": 4},
    "sec_chd": {"start": 5, "end": 6},
    "sec-chd": {"start": 5, "end": 6},
    "sec_chd_causes": {"start": 6, "end": 6},
    "sec-chd-causes": {"start": 6, "end": 6},
    "sec_vessels_blood": {"start": 7, "end": 9},
    "sec-vessels_blood": {"start": 7, "end": 9},
    "sec_vessels_types": {"start": 8, "end": 8},
    "sec-vessels-types": {"start": 8, "end": 8},
    "sec_blood_components": {"start": 9, "end": 9},
    "sec-blood-components": {"start": 9, "end": 9}
}

# =====================================================================
# B10: DISEASES AND IMMUNITY
# =====================================================================
B10_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B10: Bệnh Truyền nhiễm & Miễn dịch",
        "selector": "#sec-header",
        "en": "Welcome to Topic B10: Diseases and Immunity. Pathogens are disease-causing microorganisms that invade host tissues. In this topic, we study pathogen transmission, the body's mechanical and chemical defences, active versus passive immunity, and the mechanism of cholera.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B10: Bệnh Truyền nhiễm và Miễn dịch. Mầm bệnh là các vi sinh vật gây bệnh xâm nhập vào mô vật chủ. Trong chuyên đề này, chúng ta sẽ học về các con đường lây truyền, hàng rào cơ học và hóa học bảo vệ cơ thể, miễn dịch chủ động và thụ động, cùng cơ chế bệnh dịch tả."
    },
    {
        "id": "sec_pathogens",
        "title": "1. Mầm Bệnh & Bệnh Truyền nhiễm (Pathogens Overview)",
        "selector": "#sec-pathogens",
        "en": "Section 1 defines pathogens and transmissible diseases: A pathogen is a disease-causing organism. A transmissible disease is a disease in which the pathogen can be passed from one host to another, either by direct contact or indirectly via contaminated water, food, air droplets, or vectors.",
        "vi": "Mục một định nghĩa mầm bệnh và bệnh truyền nhiễm: Mầm bệnh là sinh vật gây bệnh. Bệnh truyền nhiễm là bệnh mà trong đó mầm bệnh có thể lây từ vật chủ này sang vật chủ khác qua tiếp xúc trực tiếp hoặc gián tiếp qua nước, thức ăn ô nhiễm, giọt bắn không khí hoặc vật trung gian truyền bệnh."
    },
    {
        "id": "sec_defences",
        "title": "2. Hàng rào Phòng thủ của Cơ thể (Body Defences Overview)",
        "selector": "#sec-defences",
        "en": "Section 2 investigates the body's defence barriers: Mechanical barriers include unbroken skin and nasal hairs. Chemical barriers include sticky mucus trapping microbes and stomach hydrochloric acid destroying swallowed bacteria. Cellular defences include phagocytes engulfing pathogens and lymphocytes releasing specific antibodies.",
        "vi": "Mục hai nghiên cứu các hàng rào phòng thủ: Hàng rào cơ học gồm da nguyên vẹn và lông mũi. Hàng rào hóa học gồm chất nhầy giữ mầm bệnh và acid clohydric dạ dày tiêu diệt vi khuẩn theo thức ăn. Hàng rào tế bào gồm đại thực bào nuốt mầm bệnh và tế bào lympho tiết kháng thể đặc hiệu."
    },
    {
        "id": "sec_immune_response",
        "title": "3. Miễn dịch Chủ động & Thụ động (Active & Passive Immunity Overview)",
        "selector": "#sec-immune_response",
        "en": "Section 3 compares active and passive immunity: Active immunity comes from pathogen infection or vaccination, producing long-lasting memory cells. Passive immunity is the short-term defence acquired from antibodies received from another individual, such as maternal antibodies via placenta or breast milk, leaving no memory cells.",
        "vi": "Mục ba so sánh miễn dịch chủ động và thụ động: Miễn dịch chủ động có được do nhiễm mầm bệnh hoặc tiêm vắc xin, tạo ra tế bào ghi nhớ tồn tại lâu dài. Miễn dịch thụ động là sự bảo vệ ngắn hạn nhận được từ kháng thể của cơ thể khác, như kháng thể mẹ truyền qua nhau thai hoặc sữa mẹ, không để lại tế bào ghi nhớ."
    },
    {
        "id": "sec_disease_control",
        "title": "4. Kiểm soát Sự Lây lan của Bệnh (Controlling Disease Spread)",
        "selector": "#sec-disease-control",
        "en": "Section 4 covers disease control measures: Clean treated water supplies, hygienic food preparation, personal hygiene including handwashing, effective sewage sanitation, and widespread vaccination programs interrupt transmission chains.",
        "vi": "Mục bốn trình bày các biện pháp kiểm soát dịch bệnh: Cung cấp nguồn nước sạch, chế biến thực phẩm hợp vệ sinh, rửa tay thường xuyên, xử lý nước thải và rác thải đúng cách, cùng chương trình tiêm chủng vắc xin diện rộng giúp cắt đứt chuỗi lây truyền."
    },
    {
        "id": "sec_cholera",
        "title": "5. Cơ chế Bệnh Tả & Liệu pháp Bù Nước (Cholera Mechanism & ORT)",
        "selector": "#sec-cholera",
        "en": "Section 5 details cholera: The bacterium Vibrio cholerae produces a toxin causing the intestinal lining to secrete chloride ions into the gut lumen. This osmotic gradient causes massive water loss by osmosis, leading to severe watery diarrhoea, dehydration, and circulatory shock. Treatment requires Oral Rehydration Therapy (ORT) containing water, glucose, and balanced electrolytes.",
        "vi": "Mục năm phân tích bệnh dịch tả: Vi khuẩn Vibrio cholerae tiết độc tố kích thích niêm mạc ruột bài tiết ion clorua vào lòng ruột. Gradient thẩm thấu này hút một lượng nước khổng lồ ra ngoài gây tiêu chảy cấp dữ dội, mất nước và sốc tuần hoàn. Điều trị cứu sống người bệnh bằng liệu pháp bù nước đường uống (ORT) gồm nước, glucose và các muối điện giải cân bằng."
    }
]

B10_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_pathogens": {"start": 1, "end": 1},
    "sec-pathogens": {"start": 1, "end": 1},
    "sec_defences": {"start": 2, "end": 2},
    "sec-defences": {"start": 2, "end": 2},
    "sec_immune_response": {"start": 3, "end": 3},
    "sec-immune-response": {"start": 3, "end": 3},
    "sec_disease_control": {"start": 4, "end": 4},
    "sec-disease-control": {"start": 4, "end": 4},
    "sec_cholera": {"start": 5, "end": 5},
    "sec-cholera": {"start": 5, "end": 5}
}

async def main():
    print("=================================================================")
    print("STARTING BATCH 2 AUDIO GENERATION (B7, B8, B9, B10)")
    print("=================================================================")
    
    # Process B7
    await process_lecture_audio(
        lecture_code="b7",
        lecture_id="cbebf582-244c-48bf-a586-c6c1922d8e20",
        course_title=COURSE_TITLE,
        lecture_title="B7: Human nutrition",
        segments=B7_SEGMENTS,
        major_sections=B7_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B8
    await process_lecture_audio(
        lecture_code="b8",
        lecture_id="e2819423-13ed-47a2-bd80-9a083989e8bd",
        course_title=COURSE_TITLE,
        lecture_title="B8: Transport in plants",
        segments=B8_SEGMENTS,
        major_sections=B8_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B9
    await process_lecture_audio(
        lecture_code="b9",
        lecture_id="a79dd569-671f-4559-84a3-eee1e6018172",
        course_title=COURSE_TITLE,
        lecture_title="B9: Transport in animals",
        segments=B9_SEGMENTS,
        major_sections=B9_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B10
    await process_lecture_audio(
        lecture_code="b10",
        lecture_id="04d34896-13fb-411b-9e13-2bc3f9725136",
        course_title=COURSE_TITLE,
        lecture_title="B10: Diseases and immunity",
        segments=B10_SEGMENTS,
        major_sections=B10_MAJOR_SECTIONS,
        subject="science"
    )
    
    print("\n🎉 BATCH 2 (B7, B8, B9, B10) AUDIO & MANIFESTS GENERATION COMPLETED!")

if __name__ == "__main__":
    asyncio.run(main())
