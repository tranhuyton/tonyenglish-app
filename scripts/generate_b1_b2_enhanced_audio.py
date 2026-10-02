import os
import sys
import asyncio
import json
import re

# Import audio lecture engine
sys.path.insert(0, os.path.dirname(__file__))
from audio_lecture_engine import process_lecture_audio

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==========================================
# B1 SEGMENTS DEFINITION
# ==========================================
B1_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B1: Đặc điểm Sinh vật sống & Phân loại học",
        "selector": "#sec-header",
        "en": "Welcome to Cambridge IGCSE Co-ordinated Sciences Biology, Topic B1: Characteristics of living organisms. In this foundational topic, we study the seven characteristics shared by all living things, captured in the mnemonic MRS GREN, and examine the classification of living organisms into the Five Kingdoms.",
        "vi": "Chào mừng các bạn đến với môn Sinh học Cambridge IGCSE, Chuyên đề B1: Đặc điểm của sinh vật sống và Phân loại học. Trong bài học nền tảng này, chúng ta sẽ khám phá 7 đặc tính phổ quát của sự sống qua quy tắc MRS GREN và hệ thống phân loại Năm Giới sinh vật."
    },
    {
        "id": "sec_mrsgren",
        "title": "1. Bảy Đặc tính của Sự sống (Quy tắc MRS GREN)",
        "selector": "#sec-mrsgren",
        "en": "Section 1 introduces the seven fundamental life processes shared by all living organisms. Remember them using the acronym MRS GREN: Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, and Nutrition. Cambridge examinations require precise, verbatim definitions for each of these processes.",
        "vi": "Mục một giới thiệu 7 đặc tính sống cơ bản của mọi sinh vật, được ghi nhớ qua cụm từ viết tắt MRS GREN: Vận động, Hô hấp tế bào, Cảm ứng, Tăng trưởng, Sinh sản, Bài tiết và Dinh dưỡng. Đề thi Cambridge yêu cầu học sinh phải nắm vững định nghĩa chuẩn xác từng từ cho mỗi quá trình."
    },
    {
        "id": "sec_movement",
        "title": "🏃 Movement (Vận động)",
        "selector": "#sec-movement",
        "en": "Movement is defined as an action by an organism or part of an organism causing a change of position or place. Animals move their entire bodies by locomotion, such as walking, running, flying, or swimming. In contrast, most plants are anchored, but move parts of their structure slowly in response to environmental stimuli, such as shoots bending towards light.",
        "vi": "Vận động được định nghĩa là hành động của một sinh vật hoặc một phần cơ thể sinh vật làm thay đổi vị trí hoặc chỗ ở. Động vật có thể di chuyển toàn bộ cơ thể bằng cách vận động như đi bộ, chạy, bay hoặc bơi. Ngược lại, thực vật thường cố định nhưng vẫn vận động chậm các bộ phận để đáp ứng các kích thích từ môi trường, ví dụ như ngọn cây uốn cong về phía có ánh sáng."
    },
    {
        "id": "sec_respiration",
        "title": "💨 Respiration (Hô hấp tế bào)",
        "selector": "#sec-respiration",
        "en": "Respiration is defined as the chemical reactions in cells that break down nutrient molecules and release energy for metabolism. Crucially for Cambridge exams, remember that cellular respiration is a biochemical reaction occurring in all living cells twenty-four hours a day, and is completely different from breathing or ventilation.",
        "vi": "Hô hấp tế bào được định nghĩa là chuỗi phản ứng hóa học diễn ra trong tế bào giúp phân giải các phân tử dinh dưỡng để giải phóng năng lượng cho quá trình chuyển hóa. Điểm trọng tâm thi cử Cambridge: Hô hấp tế bào là phản ứng hóa sinh diễn ra liên tục 24/7 ở mọi tế bào sống, và khác biệt hoàn toàn với quá trình hít thở thông khí của phổi."
    },
    {
        "id": "sec_sensitivity",
        "title": "👀 Sensitivity (Cảm ứng)",
        "selector": "#sec-sensitivity",
        "en": "Sensitivity is defined as the ability to detect and respond to changes in the internal or external environment. Sense organs contain receptor cells that detect environmental stimuli such as light, temperature, sound, and chemicals, while effectors such as muscles and glands carry out appropriate responses.",
        "vi": "Cảm ứng là khả năng nhận biết và phản ứng trước những thay đổi từ môi trường bên trong hoặc bên ngoài cơ thể. Các cơ quan cảm giác chứa tế bào thụ thể để phát hiện kích thích như ánh sáng, nhiệt độ, âm thanh và hóa chất, trong khi các cơ quan phản ứng như cơ bắp và tuyến sẽ thực hiện các đáp ứng tương ứng."
    },
    {
        "id": "sec_growth",
        "title": "🌱 Growth (Sinh trưởng & Tăng trưởng)",
        "selector": "#sec-growth",
        "en": "Growth is defined as a permanent increase in size and dry mass. Organisms grow through cell division via mitosis, followed by cell enlargement and differentiation. In Cambridge examinations, dry mass specifically means the mass of an organism after all water has been removed by gentle drying.",
        "vi": "Sinh trưởng được định nghĩa là sự gia tăng vĩnh viễn về kích thước và khối lượng khô. Sinh vật lớn lên nhờ sự phân chia tế bào qua quá trình nguyên phân, sau đó tế bào dài ra và biệt hóa. Trong các kỳ thi Cambridge, khối lượng khô chỉ khối lượng của sinh vật sau khi đã loại bỏ hoàn toàn lượng nước qua quá trình sấy."
    },
    {
        "id": "sec_reproduction",
        "title": "👶 Reproduction (Sinh sản)",
        "selector": "#sec-reproduction",
        "en": "Reproduction is defined as the processes that make more of the same kind of organism. Asexual reproduction involves only one parent and produces genetically identical offspring or clones. Sexual reproduction involves two parents and the fusion of haploid gamete nuclei to produce genetically varied offspring.",
        "vi": "Sinh sản được định nghĩa là các quá trình tạo ra nhiều cá thể mới cùng loài. Sinh sản vô tính chỉ cần một cá thể bố mẹ, tạo ra các cá thể con giống hệt nhau về mặt di truyền hay dòng vô tính. Sinh sản hữu tính cần hai cá thể bố mẹ và sự dung hợp của các nhân giao tử đơn bội để tạo ra thế hệ con có sự đa dạng di truyền."
    },
    {
        "id": "sec_excretion",
        "title": "🚽 Excretion (Bài tiết)",
        "selector": "#sec-excretion",
        "en": "Excretion is defined as the removal of the waste products of metabolism and substances in excess of requirements. Key examples include carbon dioxide excreted by the lungs, and urea and excess mineral salts filtered and excreted by the kidneys.",
        "vi": "Bài tiết được định nghĩa là quá trình đào thải các chất thải độc hại sinh ra từ quá trình trao đổi chất và các chất dư thừa so với nhu cầu của cơ thể. Các ví dụ điển hình bao gồm khí carbon dioxide được đào thải qua phổi, cùng với urê và các muối khoáng dư thừa được lọc và bài tiết qua thận."
    },
    {
        "id": "sec_nutrition",
        "title": "🍽️ Nutrition (Dinh dưỡng)",
        "selector": "#sec-nutrition",
        "en": "Nutrition is defined as the taking in of materials for energy, growth, and development. Plants are autotrophic organisms that synthesise their own organic nutrients through photosynthesis using light, carbon dioxide, and water. Animals are heterotrophic and must ingest pre-formed organic compounds by eating other living organisms.",
        "vi": "Dinh dưỡng được định nghĩa là việc thu nhận các chất vật chất để cung cấp năng lượng, phục vụ cho sự sinh trưởng và phát triển. Thực vật là sinh vật tự dưỡng, tự tổng hợp chất hữu cơ qua quang hợp từ ánh sáng, CO2 và nước. Động vật là sinh vật dị dưỡng, phải thu nhận dinh dưỡng bằng cách tiêu thụ các sinh vật khác."
    },
    {
        "id": "sec_excretion_warning",
        "title": "⚠️ Cảnh báo Đề thi: Excretion vs. Egestion",
        "selector": "#sec-excretion-warning",
        "en": "Cambridge Exam Warning: Never confuse excretion with egestion! Excretion is the removal of metabolic waste products created inside cells, such as urea in urine and carbon dioxide from respiration. In contrast, egestion is passing out undigested food as faeces through the anus, material that was never absorbed into body cells or involved in metabolism.",
        "vi": "Cảnh báo đề thi Cambridge: Tuyệt đối không được nhầm lẫn giữa Bài tiết (Excretion) và Tống phân (Egestion)! Bài tiết là việc đào thải các chất cặn bã sinh ra bên trong tế bào như urê trong nước tiểu và CO2 từ hô hấp. Ngược lại, tống phân chỉ là sự thải thức ăn không tiêu hóa được dưới dạng phân qua hậu môn, chất này chưa từng được hấp thu vào tế bào hay tham gia chuyển hóa."
    },
    {
        "id": "sec_five_kingdoms",
        "title": "2. Phân loại Sinh vật sống: Năm Giới Sinh học",
        "selector": "#sec-five-kingdoms",
        "en": "Section 2 covers biological classification into the Five Kingdoms: Animals are multicellular heterotrophs lacking cell walls. Plants are multicellular autotrophs with cellulose walls and chloroplasts. Fungi have chitin cell walls and feed saprotrophically via hyphae. Protoctists are mostly unicellular eukaryotes. Prokaryotes, including bacteria, are unicellular organisms without a true nucleus, possessing circular DNA loops and plasmids.",
        "vi": "Mục hai nghiên cứu phân loại sinh giới thành Năm Giới: Giới Động vật gồm sinh vật đa bào dị dưỡng không có thành tế bào. Giới Thực vật là sinh vật đa bào tự dưỡng có thành cellulose và lục lạp. Giới Nấm có thành chitin và dinh dưỡng hoại sinh qua hệ sợi. Giới Nguyên sinh gồm các sinh vật nhân thực đơn bào. Giới Khởi sinh như vi khuẩn là sinh vật đơn bào không có màng nhân thật, mang phân tử DNA vòng trần và plasmid."
    }
]

B1_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_mrsgren": {"start": 1, "end": 8},
    "sec-mrsgren": {"start": 1, "end": 8},
    "sec_excretion_warning": {"start": 9, "end": 9},
    "sec-excretion-warning": {"start": 9, "end": 9},
    "sec_five_kingdoms": {"start": 10, "end": 10},
    "sec-five-kingdoms": {"start": 10, "end": 10}
}

# ==========================================
# B2 SEGMENTS DEFINITION
# ==========================================
B2_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B2: Tế bào học & Cấu trúc Sinh vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic B2: Cells and organisms. The cell is the basic structural and functional unit of all living organisms. In this lesson, we compare animal, plant, and bacterial cells, explore cell organelles and their functions, investigate specialized cells and their adaptations, and master magnification formula calculations.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B2: Tế bào và Sinh vật sống. Tế bào là đơn vị cấu trúc và chức năng cơ bản của mọi sinh vật. Trong bài học này, chúng ta sẽ so sánh tế bào thực vật, động vật và vi khuẩn, khám phá cấu trúc các bào quan, tìm hiểu các tế bào chuyên biệt và công thức tính độ phóng đại qua kính hiển vi."
    },
    {
        "id": "sec_cell_comparison",
        "title": "1. So sánh Tế bào Thực vật, Động vật & Vi khuẩn",
        "selector": "#sec-cell-comparison",
        "en": "Section 1 contrasts cellular structures: Animal and plant cells are eukaryotic with a true nucleus containing linear DNA. Animal cells contain cell membranes, cytoplasm, nucleus, mitochondria, and ribosomes. Plant cells have all these plus three unique structures: a rigid cellulose cell wall, a large permanent central vacuole filled with cell sap, and chloroplasts for photosynthesis. Bacterial cells are prokaryotes: they lack a nucleus, having circular DNA loops and plasmids instead, and have a peptidoglycan cell wall.",
        "vi": "Mục một so sánh cấu trúc tế bào: Tế bào thực vật và động vật là tế bào nhân thực có nhân hoàn chỉnh chứa DNA mạch thẳng. Tế bào động vật gồm màng sinh chất, tế bào chất, nhân, ti thể và ribosome. Tế bào thực vật có thêm 3 cấu trúc độc nhất: thành tế bào cellulose vững chắc, không bào trung tâm lớn chứa dịch bào và lục lạp để quang hợp. Tế bào vi khuẩn là tế bào nhân sơ: không có màng nhân, vật chất di truyền là phân tử DNA vòng và plasmid, cùng thành tế bào peptidoglycan."
    },
    {
        "id": "sec_organelles",
        "title": "2. Bản đồ Bào quan Tương tác & Chức năng Bào quan",
        "selector": "#sec-organelles",
        "en": "Section 2 introduces the Interactive Cell Map. Cell organelles are specialized subcellular compartments that perform distinct metabolic jobs. Click or tap any organelle in the cell diagrams or the list below to hear its detailed structure, Cambridge exam keywords, and biological role.",
        "vi": "Mục hai giới thiệu Bản đồ Bào quan Tương tác. Các bào quan là những cấu trúc dưới tế bào chuyên biệt thực hiện các chức năng chuyển hóa riêng biệt. Hãy nhấn hoặc rê chuột vào bất kỳ bào quan nào trên sơ đồ tế bào hoặc danh mục bên dưới để nghe bài giảng chi tiết, từ khóa thi cử Cambridge và vai trò sinh học của bào quan đó."
    },
    {
        "id": "sec_nucleus",
        "title": "🧬 Nucleus (Nhân tế bào)",
        "selector": "#sec-nucleus",
        "en": "The Nucleus is the control center of the cell. It contains genetic material in the form of DNA organized into chromosomes. The nucleus directs cell growth, regulates protein synthesis, and controls cell division. Key exam keyword: Contains genetic material DNA and controls all cell activities.",
        "vi": "Nhân tế bào là trung tâm điều khiển của tế bào. Nhân chứa vật chất di truyền dưới dạng DNA được tổ chức thành các nhiễm sắc thể. Nhân điều khiển sự lớn lên của tế bào, điều hòa tổng hợp protein và điều khiển quá trình phân bào. Từ khóa thi Cambridge: Chứa vật chất di truyền DNA và kiểm soát mọi hoạt động của tế bào."
    },
    {
        "id": "sec_membrane",
        "title": "🛡️ Cell Membrane (Màng tế bào)",
        "selector": "#sec-membrane",
        "en": "The Cell Membrane is a partially permeable lipid bilayer that surrounds the cytoplasm. It forms a selective barrier that regulates which substances enter and leave the cell by diffusion, osmosis, and active transport. Key exam keyword: Partially permeable barrier that controls substance entry and exit.",
        "vi": "Màng tế bào là một màng có tính thấm chọn lọc bao bọc lấy tế bào chất. Màng kiểm soát chặt chẽ các chất đi vào và đi ra khỏi tế bào qua các cơ chế khuếch tán, thẩm thấu và vận chuyển chủ động. Từ khóa thi Cambridge: Màng thấm chọn lọc kiểm soát chất đi vào và ra khỏi tế bào."
    },
    {
        "id": "sec_cytoplasm",
        "title": "💧 Cytoplasm (Tế bào chất)",
        "selector": "#sec-cytoplasm",
        "en": "Cytoplasm is a jelly-like aqueous fluid containing dissolved salts, sugars, amino acids, and suspended organelles. It is the vital site where most biochemical metabolic reactions and enzyme activities occur within the cell. Key exam keyword: Site of cellular chemical reactions and supports organelles.",
        "vi": "Tế bào chất là chất dịch bán lỏng dạng thạch chứa nước, muối khoáng hòa tan, đường, axit amin và các bào quan lơ lửng. Đây là nơi diễn ra phần lớn các phản ứng hóa sinh và trao đổi chất của tế bào. Từ khóa thi Cambridge: Nơi diễn ra các phản ứng hóa học tế bào và nâng đỡ các bào quan."
    },
    {
        "id": "sec_mitochondria",
        "title": "⚡ Mitochondria (Ti thể)",
        "selector": "#sec-mitochondria",
        "en": "Mitochondria are the powerhouses of eukaryotic cells. They are the primary site of aerobic cellular respiration, where glucose and oxygen react to release usable metabolic energy in the form of ATP. Crucial exam tip: Always state that mitochondria release energy, never say they produce or create energy.",
        "vi": "Ti thể là nhà máy năng lượng của tế bào nhân thực. Đây là vị trí chính diễn ra quá trình hô hấp hiếu khí, nơi glucose và oxy phản ứng để giải phóng năng lượng ATP cho tế bào. Bẫy đề thi Cambridge: Luôn nói ti thể giải phóng năng lượng, tuyệt đối không được nói ti thể tạo ra năng lượng."
    },
    {
        "id": "sec_ribosomes",
        "title": "🔬 Ribosomes (Ribosome)",
        "selector": "#sec-ribosomes",
        "en": "Ribosomes are tiny circular structures located throughout the cytoplasm or attached to the rough endoplasmic reticulum. They are responsible for protein synthesis, assembling amino acids into polypeptide chains according to genetic instructions.",
        "vi": "Ribosome là các hạt siêu nhỏ phân bố rải rác trong tế bào chất hoặc gắn trên màng lưới nội chất hạt. Ribosome đảm nhận vai trò tổng hợp protein, liên kết các axit amin thành chuỗi polypeptide theo mã di truyền."
    },
    {
        "id": "sec_cellwall",
        "title": "🧱 Cell Wall (Thành tế bào - Thực vật)",
        "selector": "#sec-cellwall",
        "en": "The Cell Wall is an outer non-living layer found outside the plant cell membrane, composed of rigid criss-crossing cellulose fibres. It is fully permeable, provides mechanical strength, and prevents the plant cell from bursting when water enters by osmosis.",
        "vi": "Thành tế bào là lớp vỏ ngoài không sống bao bọc màng tế bào thực vật, cấu tạo từ các sợi cellulose cứng cáp. Thành có tính thấm hoàn toàn, cung cấp lực chống đỡ cơ học và giúp tế bào thực vật không bị vỡ khi hút no nước nhờ áp suất trương nước."
    },
    {
        "id": "sec_chloroplast",
        "title": "🍃 Chloroplast (Lục lạp - Thực vật)",
        "selector": "#sec-chloroplast",
        "en": "Chloroplasts are photosynthetic organelles present in green plant cells, containing chlorophyll pigments. Chlorophyll absorbs light energy and uses it to convert carbon dioxide and water into glucose and oxygen during photosynthesis.",
        "vi": "Lục lạp là bào quan quang hợp có trong tế bào màu xanh của thực vật, chứa sắc tố diệp lục. Diệp lục hấp thu năng lượng ánh sáng mặt trời để chuyển hóa CO2 và nước thành glucose và oxy trong quá trình quang hợp."
    },
    {
        "id": "sec_vacuole",
        "title": "💧 Permanent Vacuole (Không bào trung tâm - Thực vật)",
        "selector": "#sec-vacuole",
        "en": "The Permanent Vacuole is a large central organelle in plant cells filled with watery cell sap containing dissolved sugars and mineral salts. When full, it pushes outwards against the cell wall, maintaining turgor pressure and keeping plant tissues firm and upright.",
        "vi": "Không bào trung tâm là một khoang lớn ở giữa tế bào thực vật chứa dịch bào gồm nước, đường và muối khoáng. Khi chứa đầy nước, không bào tạo lực đẩy lên thành tế bào giúp duy trì áp suất trương, giữ cho mô thực vật luôn căng cứng và đứng vững."
    },
    {
        "id": "sec_specialised_cells",
        "title": "3. Tổng quan Tế bào Chuyên biệt",
        "selector": "#sec-specialised-cells",
        "en": "Section 3 explores Specialised Cells and their structural adaptations. As multicellular organisms develop, cells differentiate into specific structures to perform specialized physiological functions with high efficiency.",
        "vi": "Mục ba nghiên cứu các Tế bào Chuyên biệt và đặc điểm thích nghi của chúng. Ở sinh vật đa bào, các tế bào biệt hóa thành những hình dạng và cấu trúc đặc thù để thực hiện các chức năng sinh lý chuyên biệt với hiệu suất cao nhất."
    },
    {
        "id": "sec_cell_ciliated",
        "title": "🍃 Ciliated Cell (Tế bào biểu mô lông rung)",
        "selector": "#sec-cell-ciliated",
        "en": "Ciliated epithelial cells line the trachea and bronchi in the respiratory system. They possess hundreds of microscopic hair-like cilia that beat synchronously to sweep mucus containing trapped dust particles and pathogens upwards away from the lungs.",
        "vi": "Tế bào biểu mô lông rung nằm lót trong khí quản và phế quản của đường hô hấp. Bề mặt tế bào có hàng trăm sợi lông mao nhỏ đập nhịp nhàng để quét dịch nhầy chứa bụi bẩn và vi khuẩn ngược lên trên ra khỏi phổi."
    },
    {
        "id": "sec_cell_roothair",
        "title": "🌱 Root Hair Cell (Tế bào lông hút ở rễ)",
        "selector": "#sec-cell-roothair",
        "en": "Root hair cells are located at the root epidermis of plants. They feature a long slender cytoplasmic projection that dramatically increases the surface area to volume ratio for rapid uptake of water by osmosis and mineral ions by active transport.",
        "vi": "Tế bào lông hút nằm ở lớp biểu bì rễ cây. Tế bào có phần bào tương kéo dài thành sợi lông dài giúp tăng diện tích tiếp xúc với đất lên gấp nhiều lần, tối ưu hóa tốc độ hấp thụ nước bằng thẩm thấu và ion khoáng bằng vận chuyển chủ động."
    },
    {
        "id": "sec_cell_xylem",
        "title": "🪵 Xylem Vessel (Mạch gỗ)",
        "selector": "#sec-cell-xylem",
        "en": "Xylem vessels are elongated, dead tubular cells with no end walls, forming a continuous hollow lumen. Their walls are heavily thickened and reinforced with waterproof lignin, allowing them to transport water and dissolved ions under extreme tension while providing mechanical support.",
        "vi": "Mạch gỗ gồm các tế bào chết hình ống kéo dài, không có vách ngăn ngang, tạo thành một đường ống rỗng liên tục. Thành mạch được tẩm chất gỗ lignin không thấm nước dày chắc, giúp dẫn dòng nước và khoáng chất dưới lực căng thoát hơi nước và nâng đỡ thân cây."
    },
    {
        "id": "sec_cell_palisade",
        "title": "☀️ Palisade Mesophyll Cell (Tế bào mô giậu)",
        "selector": "#sec-cell-palisade",
        "en": "Palisade mesophyll cells are located in the upper layer of leaves beneath the upper epidermis. They are tall, columnar cells tightly packed with numerous chloroplasts to absorb the maximum amount of light energy for photosynthesis.",
        "vi": "Tế bào mô giậu nằm ở lớp trên của lá cây ngay dưới lớp biểu bì trên. Tế bào có hình trụ thuôn dài xếp khít nhau và chứa mật độ lục lạp dày đặc nhất, nhằm hấp thu tối đa lượng ánh sáng mặt trời cho quá trình quang hợp."
    },
    {
        "id": "sec_cell_rbc",
        "title": "🩸 Red Blood Cell (Tế bào hồng cầu)",
        "selector": "#sec-cell-rbc",
        "en": "Red blood cells, or erythrocytes, are adapted for efficient oxygen transport. Their biconcave disc shape provides a large surface area for gas diffusion. Crucially, mature red blood cells have no nucleus, maximizing intracellular space to pack millions of hemoglobin molecules.",
        "vi": "Tế bào hồng cầu chuyên trách vận chuyển oxy trong máu. Hình dạng đĩa lõm hai mặt giúp tăng diện tích bề mặt cho oxy khuếch tán. Đặc biệt, hồng cầu trưởng thành không có nhân để dành toàn bộ dung tích tế bào chứa hemoglobin gắn oxy."
    },
    {
        "id": "sec_cell_neurone",
        "title": "⚡ Neurone (Tế bào thần kinh)",
        "selector": "#sec-cell-neurone",
        "en": "Neurones are adapted to transmit electrical nerve impulses across the body. They have a long cytoplasmic axon that transmits impulses over long distances, surrounded by an insulating fatty myelin sheath that speeds up electrical conduction.",
        "vi": "Tế bào thần kinh được thích nghi để truyền các xung điện thần kinh khắp cơ thể. Tế bào có sợi trục dài dẫn truyền xung động đi xa, được bọc bởi bao myelin cách điện giúp tăng tốc độ truyền tín hiệu."
    },
    {
        "id": "sec_magnification",
        "title": "4. Công thức Độ phóng đại (I = A × M)",
        "selector": "#sec-magnification",
        "en": "Section 4 covers microscopy calculations using the formula triangle I = A × M, where Image size equals Actual size multiplied by Magnification. Golden rules for Cambridge examinations: always measure the image with a ruler in millimetres, and remember that one millimetre equals one thousand micrometres. When calculating magnification, make sure Image and Actual sizes are converted to identical units.",
        "vi": "Mục bốn hướng dẫn tính toán độ phóng đại qua tam giác công thức: I = A nhân M (Kích thước ảnh I bằng Kích thước thực tế A nhân Độ phóng đại M). Quy tắc sống còn trong bài thi Cambridge: Luôn đo ảnh bằng thước theo đơn vị milimét, và nhớ rằng 1 milimét bằng 1000 micromét. Khi tính độ phóng đại, phải quy đổi I và A về cùng một đơn vị đo."
    }
]

B2_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_cell_comparison": {"start": 1, "end": 1},
    "sec-cell-comparison": {"start": 1, "end": 1},
    "sec_organelles": {"start": 2, "end": 10},
    "sec-organelles": {"start": 2, "end": 10},
    "sec_specialised_cells": {"start": 11, "end": 17},
    "sec-specialised-cells": {"start": 11, "end": 17},
    "sec_magnification": {"start": 18, "end": 18},
    "sec-magnification": {"start": 18, "end": 18}
}

async def main():
    print("=== GENERATING ENHANCED AUDIO FOR SCIENCE B1 ===")
    await process_lecture_audio(
        lecture_code="b1",
        lecture_id="1231b474-8a99-4330-b45d-fdda19a802fe",
        course_title="Cambridge IGCSE Co-ordinated Sciences",
        lecture_title="B1: Characteristics of living organisms",
        segments=B1_SEGMENTS,
        major_sections=B1_MAJOR_SECTIONS,
        subject="science"
    )

    print("\n=== GENERATING ENHANCED AUDIO FOR SCIENCE B2 ===")
    await process_lecture_audio(
        lecture_code="b2",
        lecture_id="7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c",
        course_title="Cambridge IGCSE Co-ordinated Sciences",
        lecture_title="B2: Cells and organisms",
        segments=B2_SEGMENTS,
        major_sections=B2_MAJOR_SECTIONS,
        subject="science"
    )

if __name__ == "__main__":
    asyncio.run(main())
