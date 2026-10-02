import os
import sys
import asyncio
import json

# Import audio lecture engine
sys.path.insert(0, os.path.dirname(__file__))
from audio_lecture_engine import process_lecture_audio

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

COURSE_TITLE = "Cambridge IGCSE Co-ordinated Sciences"

# =====================================================================
# B3: MOVEMENT INTO AND OUT OF CELLS
# =====================================================================
B3_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B3: Vận chuyển Chất qua Màng Tế bào",
        "selector": "#sec-header",
        "en": "Welcome to Topic B3: Movement into and out of cells. Living cells constantly exchange nutrients, gases, and wastes across plasma membranes. In this lesson, we master the principles of diffusion, investigate water potential and osmosis in plant and animal tissues, and examine active transport mechanisms.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B3: Vận chuyển các chất qua màng tế bào. Tế bào sống liên tục trao đổi chất dinh dưỡng, khí và chất thải qua màng sinh chất. Trong bài học này, chúng ta sẽ làm chủ hiện tượng khuếch tán, thế nước và thẩm thấu trong tế bào thực vật và động vật, cùng cơ chế vận chuyển chủ động."
    },
    {
        "id": "sec_diffusion",
        "title": "1. Khuyếch tán: Định nghĩa & Nguyên lý (Diffusion Overview)",
        "selector": "#sec-diffusion",
        "en": "Section 1 defines Diffusion: the net movement of particles from a region of higher concentration to a region of lower concentration down a concentration gradient, as a result of their random kinetic movement. Energy for diffusion comes from the kinetic energy of random movement of molecules, requiring no ATP.",
        "vi": "Mục một định nghĩa Khuyếch tán: là sự chuyển động tịnh của các hạt từ nơi có nồng độ cao đến nơi có nồng độ thấp hơn xuôi theo chiều gradient nồng độ, bắt nguồn từ chuyển động nhiệt hỗn loạn của phân tử. Năng lượng cho khuếch tán đến từ động năng tự nhiên của các phân tử và không tiêu tốn ATP."
    },
    {
        "id": "sec_diff_temp",
        "title": "🌡️ Temperature (Nhiệt độ)",
        "selector": "#sec-diff-temp",
        "en": "Temperature factor: At higher temperatures, particles gain more kinetic energy and move faster. This causes more frequent collisions and crossing of membranes, significantly increasing the rate of diffusion.",
        "vi": "Yếu tố Nhiệt độ: Ở nhiệt độ cao hơn, các hạt thu nhận thêm động năng và chuyển động nhanh hơn. Điều này làm tăng tần suất va chạm và tốc độ di chuyển qua màng, giúp tốc độ khuếch tán tăng lên rõ rệt."
    },
    {
        "id": "sec_diff_sa",
        "title": "📐 Surface Area (Diện tích Bề mặt)",
        "selector": "#sec-diff-sa",
        "en": "Surface Area factor: A larger membrane surface area provides more space and pathways for solute particles to cross per unit of time, thereby increasing the rate of diffusion.",
        "vi": "Yếu tố Diện tích bề mặt: Diện tích bề mặt màng càng lớn thì càng có nhiều khoảng không gian để các hạt đi qua trong mỗi đơn vị thời gian, từ đó làm tăng tốc độ khuếch tán."
    },
    {
        "id": "sec_diff_gradient",
        "title": "⚡ Concentration Gradient (Độ dốc Nồng độ)",
        "selector": "#sec-diff-gradient",
        "en": "Concentration Gradient factor: A steeper concentration gradient, meaning a greater difference in concentration between the two regions, accelerates net particle movement and increases the diffusion rate.",
        "vi": "Yếu tố Độ dốc nồng độ: Gradient nồng độ càng dốc, nghĩa là sự chênh lệch nồng độ giữa hai vùng càng lớn, thì chuyển động tịnh của các phân tử càng diễn ra nhanh chóng, làm tăng tốc độ khuếch tán."
    },
    {
        "id": "sec_diff_dist",
        "title": "📏 Diffusion Distance (Khoảng cách Khuếch tán)",
        "selector": "#sec-diff-dist",
        "en": "Diffusion Distance factor: A shorter diffusion distance, such as across thin cell membranes or one-cell-thick capillary walls, allows particles to travel much faster, increasing the rate of diffusion.",
        "vi": "Yếu tố Khoảng cách khuếch tán: Khoảng cách khuếch tán càng ngắn, ví dụ như qua màng tế bào mỏng hay thành mao mạch chỉ dày một lớp tế bào, thì các hạt di chuyển qua càng nhanh, làm tăng tốc độ khuếch tán."
    },
    {
        "id": "sec_diff_importance",
        "title": "🌿 Biological Importance of Diffusion (Tầm quan trọng Sinh học)",
        "selector": "#sec-diff-importance",
        "en": "Diffusion is essential for living organisms: Oxygen diffuses into blood and carbon dioxide diffuses out in lungs alveoli. In plant leaves, carbon dioxide enters stomata for photosynthesis while oxygen exits. In the digestive system, digested glucose and amino acids diffuse across villi epithelium into blood capillaries.",
        "vi": "Khuếch tán đóng vai trò sinh tử với sinh vật: Khí oxy khuếch tán vào máu và khí CO2 khuếch tán ra tại phế nang phổi. Ở lá cây, CO2 khuếch tán qua khí khổng để quang hợp trong khi oxy khuếch tán ra ngoài. Tại hệ tiêu hóa, glucose và amino acid đã tiêu hóa khuếch tán qua biểu mô lông ruột non vào mao mạch máu."
    },
    {
        "id": "sec_osmosis",
        "title": "2. Thẩm thấu & Thế nước (Osmosis & Water Potential Overview)",
        "selector": "#sec-osmosis",
        "en": "Section 2 investigates Osmosis: the net movement of water molecules from a region of higher water potential to a region of lower water potential through a partially permeable membrane. Pure water has the highest water potential at zero kilopascals; adding solute particles lowers water potential to negative values.",
        "vi": "Mục hai nghiên cứu hiện tượng Thẩm thấu: là sự chuyển động tịnh của các phân tử nước từ nơi có thế nước cao đến nơi có thế nước thấp hơn qua một màng thấm chọn lọc. Nước tinh khiết có thế nước cao nhất bằng 0 kPa; việc hòa tan thêm chất tan sẽ làm giảm thế nước xuống các giá trị âm."
    },
    {
        "id": "sec_os_pure",
        "title": "🚰 Pure Water / Hypotonic Solution (Thế nước cao)",
        "selector": "#sec-os-pure",
        "en": "In pure water or dilute solution with high water potential: Water enters plant cells by osmosis. The vacuole swells and pushes cytoplasm against the rigid cell wall, creating turgor pressure; the cell becomes turgid, supporting plant stems. In contrast, animal red blood cells lack cell walls; excessive water entry causes them to swell and burst, known as cell lysis.",
        "vi": "Trong nước tinh khiết hoặc dung dịch nhược trương có thế nước cao: Nước thẩm thấu đi vào tế bào thực vật. Không bào trương lên ép tế bào chất vào thành tế bào cứng cáp, tạo nên áp suất trương nước; tế bào trở nên trương chắc giúp nâng đỡ thân cây. Ngược lại, hồng cầu động vật không có thành tế bào nên khi nước tràn vào quá nhiều sẽ bị vỡ tung, gọi là tan tế bào."
    },
    {
        "id": "sec_os_equal",
        "title": "⚖️ Equal Solution / Isotonic (Cân bằng Thế nước)",
        "selector": "#sec-os-equal",
        "en": "In an isotonic solution with identical water potential: Water molecules move into and out of the cell at equal rates, resulting in zero net osmosis. Plant and animal cells retain their normal shape and volume.",
        "vi": "Trong dung dịch đẳng trương có thế nước bằng nhau: Các phân tử nước đi vào và đi ra khỏi tế bào với tốc độ ngang bằng nhau, dẫn đến không có sự chuyển động tịnh của nước. Tế bào thực vật và động vật duy trì nguyên vẹn hình dạng và thể tích bình thường."
    },
    {
        "id": "sec_os_salt",
        "title": "🧂 Concentrated Solution / Hypertonic (Thế nước thấp)",
        "selector": "#sec-os-salt",
        "en": "In concentrated salt or sugar solution with lower water potential: Water leaves cells by osmosis. In plant cells, the cytoplasm shrinks away from the cell wall, causing plasmolysis; the tissue becomes limp and flaccid, causing the plant to wilt. In animal red blood cells, water loss causes them to shrivel and crenate.",
        "vi": "Trong dung dịch ưu trương đậm đặc muối hoặc đường có thế nước thấp: Nước thẩm thấu thoát ra ngoài tế bào. Ở tế bào thực vật, tế bào chất co cụm tách rời khỏi thành tế bào, gây hiện tượng co nguyên sinh; mô thực vật mất sức trương và cây bị héo. Ở tế bào hồng cầu động vật, sự mất nước làm tế bào co rúm lại và nhăn nheo."
    },
    {
        "id": "sec_active_transport",
        "title": "3. Vận chuyển Chủ động (Active Transport Overview)",
        "selector": "#sec-active-transport",
        "en": "Section 3 covers Active Transport: the movement of particles through a cell membrane from a region of lower concentration to a region of higher concentration against a concentration gradient, using energy released from respiration.",
        "vi": "Mục ba nghiên cứu Vận chuyển Chủ động: là quá trình vận chuyển các hạt qua màng tế bào từ nơi có nồng độ thấp đến nơi có nồng độ cao ngược chiều gradient nồng độ, đòi hỏi tiêu tốn năng lượng giải phóng từ quá trình hô hấp tế bào."
    },
    {
        "id": "sec_active_carrier",
        "title": "⚡ Carrier Proteins & ATP Mechanism (Cơ chế Protein Vận chuyển)",
        "selector": "#sec-active-carrier",
        "en": "Mechanism: Active transport is carried out by specific carrier proteins embedded in the cell membrane. Solute particles bind to the carrier protein, which uses energy from ATP hydrolysis to change its conformational shape and release the particle on the other side of the membrane.",
        "vi": "Cơ chế: Vận chuyển chủ động được thực hiện bởi các protein mang đặc hiệu gắn trên màng tế bào. Hạt chất tan gắn vào protein mang, protein này dùng năng lượng từ thủy phân ATP để thay đổi hình thể không gian và giải phóng hạt chất sang phía bên kia màng tế bào."
    },
    {
        "id": "sec_active_importance",
        "title": "🌱 Biological Importance of Active Transport (Ứng dụng Sinh học)",
        "selector": "#sec-active-importance",
        "en": "Biological importance: Root hair cells use active transport to absorb nitrate and mineral ions from soil even when concentrations in the soil solution are far lower than inside the root. In human intestines, epithelial cells actively absorb glucose into the blood even when intestinal lumen concentrations drop low.",
        "vi": "Tầm quan trọng sinh học: Tế bào lông hút ở rễ dùng vận chuyển chủ động để hút ion nitrat và khoáng chất từ đất ngay cả khi nồng độ dinh dưỡng trong đất thấp hơn nhiều so với dịch bào bên trong rễ. Ở ruột non người, tế bào niêm mạc chủ động hấp thu glucose vào máu ngay cả khi nồng độ glucose trong lòng ruột đã giảm xuống rất thấp."
    }
]

B3_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_diffusion": {"start": 1, "end": 6},
    "sec-diffusion": {"start": 1, "end": 6},
    "sec_diff_temp": {"start": 2, "end": 2},
    "sec-diff-temp": {"start": 2, "end": 2},
    "sec_diff_sa": {"start": 3, "end": 3},
    "sec-diff-sa": {"start": 3, "end": 3},
    "sec_diff_gradient": {"start": 4, "end": 4},
    "sec-diff-gradient": {"start": 4, "end": 4},
    "sec_diff_dist": {"start": 5, "end": 5},
    "sec-diff-dist": {"start": 5, "end": 5},
    "sec_diff_importance": {"start": 6, "end": 6},
    "sec-diff-importance": {"start": 6, "end": 6},
    "sec_osmosis": {"start": 7, "end": 10},
    "sec-osmosis": {"start": 7, "end": 10},
    "sec_os_pure": {"start": 8, "end": 8},
    "sec-os-pure": {"start": 8, "end": 8},
    "sec_os_equal": {"start": 9, "end": 9},
    "sec-os-equal": {"start": 9, "end": 9},
    "sec_os_salt": {"start": 10, "end": 10},
    "sec-os-salt": {"start": 10, "end": 10},
    "sec_active_transport": {"start": 11, "end": 13},
    "sec-active-transport": {"start": 11, "end": 13},
    "sec_active_carrier": {"start": 12, "end": 12},
    "sec-active-carrier": {"start": 12, "end": 12},
    "sec_active_importance": {"start": 13, "end": 13},
    "sec-active-importance": {"start": 13, "end": 13}
}

# =====================================================================
# B4: BIOLOGICAL MOLECULES
# =====================================================================
B4_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B4: Các Phân tử Sinh học",
        "selector": "#sec-header",
        "en": "Welcome to Topic B4: Biological Molecules. All living organisms are constructed from organic biomolecules: carbohydrates, lipids, proteins, and nucleic acids. In this lesson, we master their chemical composition, building blocks, and the qualitative food tests used to detect them.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B4: Các phân tử sinh học. Mọi sinh vật sống đều được cấu tạo từ các đại phân tử hữu cơ: carbohydrate, lipid, protein và acid nucleic. Trong bài học này, chúng ta sẽ nắm vững thành phần hóa học, đơn phân cấu tạo và các phản ứng thử nghiệm định tính phát hiện dinh dưỡng."
    },
    {
        "id": "sec_biomolecules",
        "title": "1. Cấu trúc Hóa học của các Phân tử Sinh học (Biomolecules Overview)",
        "selector": "#sec-biomolecules",
        "en": "Section 1 examines the chemical elements and structural units of biomolecules. Carbohydrates and lipids contain Carbon, Hydrogen, and Oxygen. Proteins additionally contain Nitrogen and some Sulfur. DNA contains Carbon, Hydrogen, Oxygen, Nitrogen, and Phosphorus.",
        "vi": "Mục một khảo sát các nguyên tố hóa học và đơn vị cấu tạo của các phân tử sinh học. Carbohydrate và lipid chứa Carbon, Hydro và Oxy. Protein có thêm Nitơ và một số chứa Lưu huỳnh. Phân tử DNA chứa Carbon, Hydro, Oxy, Nitơ và Photpho."
    },
    {
        "id": "sec_carbohydrates",
        "title": "🍞 Carbohydrates (Đường & Tinh bột)",
        "selector": "#sec-carbohydrates",
        "en": "Carbohydrates are composed of Carbon, Hydrogen, and Oxygen. Simple monomers like glucose are monosaccharides used immediately for respiration. Monomers bond together to form large insoluble storage polymers: starch in plants and glycogen in animals, or cellulose for plant cell walls.",
        "vi": "Carbohydrate được cấu tạo từ Carbon, Hydro và Oxy. Các đơn phân đơn giản như glucose là monosaccharide được dùng ngay cho hô hấp tế bào. Các đơn phân liên kết lại tạo thành polymer dự trữ không tan: tinh bột ở thực vật và glycogen ở động vật, hoặc cellulose tạo thành tế bào thực vật."
    },
    {
        "id": "sec_lipids",
        "title": "🥑 Fats & Oils / Lipids (Chất béo)",
        "selector": "#sec-lipids",
        "en": "Lipids (fats and oils) are made of Carbon, Hydrogen, and Oxygen. Each lipid molecule is synthesised from one glycerol molecule chemically bonded to three fatty acid chains. Lipids provide high-density long-term energy storage, thermal insulation, and buoyancy.",
        "vi": "Lipid (chất béo và dầu) cấu tạo từ Carbon, Hydro và Oxy. Mỗi phân tử chất béo được tổng hợp từ một phân tử glycerol liên kết hóa học với ba chuỗi acid béo. Chất béo giúp dự trữ năng lượng đậm đặc lâu dài, cách nhiệt giữ ấm cơ thể và tạo sức nổi."
    },
    {
        "id": "sec_proteins",
        "title": "🥩 Proteins (Chất đạm)",
        "selector": "#sec-proteins",
        "en": "Proteins are composed of Carbon, Hydrogen, Oxygen, and Nitrogen, with some containing sulfur. They are polymers of 20 different amino acids joined by peptide bonds. The specific sequence of amino acids folds into a precise 3D shape, enabling proteins to function as enzymes, antibodies, hemoglobin, and keratin.",
        "vi": "Protein được cấu tạo từ Carbon, Hydro, Oxy và Nitơ, một số chứa lưu huỳnh. Chúng là polymer của 20 loại amino acid khác nhau nối với nhau bằng liên kết peptide. Trình tự amino acid đặc thù sẽ cuộn gập thành hình thể không gian 3 chiều chuẩn xác, giúp protein hoạt động như enzyme, kháng thể, hemoglobin hay keratin."
    },
    {
        "id": "sec_dna",
        "title": "🧬 DNA Structure (Cấu trúc DNA)",
        "selector": "#sec-dna",
        "en": "DNA consists of two polynucleotide strands coiled into a double helix. The strands are cross-linked by complementary base pairs: Adenine always pairs with Thymine (A with T), and Cytosine always pairs with Guanine (C with G).",
        "vi": "Cấu trúc DNA gồm hai chuỗi polynucleotide cuộn xoắn thành chuỗi xoắn kép đều đặn. Hai chuỗi được liên kết bắt chéo bởi các cặp bazơ bổ sung: Adenine luôn liên kết với Thymine (A với T), và Cytosine luôn liên kết với Guanine (C với G)."
    },
    {
        "id": "sec_water",
        "title": "💧 Role of Water (Dung môi Sinh học)",
        "selector": "#sec-water",
        "en": "Water acts as a vital universal biological solvent. It dissolves metabolic waste products like urea for excretion in urine, and transports nutrients, mineral ions, and hormones through blood plasma and plant vascular bundles.",
        "vi": "Nước đóng vai trò là dung môi sinh học phổ quát tối quan trọng. Nước hòa tan các chất cặn bã chuyển hóa như urê để bài tiết qua nước tiểu, đồng thời vận chuyển chất dinh dưỡng, ion khoáng và hormone qua huyết tương máu và bó mạch thực vật."
    },
    {
        "id": "sec_food_tests",
        "title": "2. Thí nghiệm Định tính Thực phẩm (Qualitative Food Tests Overview)",
        "selector": "#sec-food-tests",
        "en": "Section 2 presents qualitative food tests examined in Cambridge Paper 4 and Paper 6. Remember each specific reagent, temperature requirement, and diagnostic color change.",
        "vi": "Mục hai trình bày các thí nghiệm định tính dinh dưỡng thường xuất hiện trong đề thi Paper 4 và Paper 6 của Cambridge. Hãy ghi nhớ thuốc thử, điều kiện nhiệt độ và màu sắc chỉ thị chuẩn xác của từng phép thử."
    },
    {
        "id": "sec_test_sugar",
        "title": "🍬 Benedict's Test for Reducing Sugars",
        "selector": "#sec-test-sugar",
        "en": "Reducing Sugars: Add Benedict's reagent and heat in a hot water bath at 80°C for 3 to 5 minutes. Initial color is blue. A positive result turns green, yellow, orange, and finally forms a brick-red precipitate.",
        "vi": "Đường khử: Cho thuốc thử Benedict và đun cách thủy trong nồi nước nóng ở 80°C từ 3 đến 5 phút. Màu ban đầu là xanh lam. Khi có đường khử, dung dịch chuyển dần sang xanh lá, vàng, cam và kết tủa đỏ gạch."
    },
    {
        "id": "sec_test_starch",
        "title": "🍞 Iodine Test for Starch",
        "selector": "#sec-test-starch",
        "en": "Starch: Add drops of iodine solution directly at room temperature. Initial color is yellow-brown. A positive result turns blue-black.",
        "vi": "Tinh bột: Nhỏ trực tiếp vài giọt dung dịch iod ở nhiệt độ phòng. Màu ban đầu là vàng nâu. Phản ứng dương tính sẽ chuyển thành màu xanh đen đặc trưng."
    },
    {
        "id": "sec_test_protein",
        "title": "🥩 Biuret Test for Proteins",
        "selector": "#sec-test-protein",
        "en": "Proteins: Add Biuret reagent (potassium hydroxide followed by dilute copper sulfate) at room temperature. Initial color is pale blue. A positive result turns violet or purple.",
        "vi": "Protein: Cho thuốc thử Biuret (dung dịch KOH và đồng sunfat loãng) ở nhiệt độ phòng. Màu ban đầu là xanh lam nhạt. Phản ứng dương tính sẽ chuyển sang màu tím hoặc tím hoa cà."
    },
    {
        "id": "sec_test_lipid",
        "title": "🥑 Ethanol Emulsion Test for Lipids",
        "selector": "#sec-test-lipid",
        "en": "Lipids: Dissolve sample in pure ethanol, shake well, then pour the liquid into cold water. Initial solution is clear and colourless. A positive result forms a cloudy white emulsion.",
        "vi": "Lipid (Chất béo): Hòa tan mẫu thử vào cồn ethanol tinh khiết, lắc đều, sau đó rót dịch lọc vào nước lạnh. Dung dịch ban đầu trong suốt không màu. Khi có chất béo, hỗn hợp sẽ xuất hiện lớp nhũ tương màu trắng đục như sữa."
    },
    {
        "id": "sec_test_vitc",
        "title": "🍋 DCPIP Test for Vitamin C",
        "selector": "#sec-test-vitc",
        "en": "Vitamin C: Add sample drop by drop to blue DCPIP solution. Initial color is dark blue. A positive result rapidly decolourises the DCPIP solution, turning it completely colourless.",
        "vi": "Vitamin C: Nhỏ từng giọt dịch mẫu vào dung dịch DCPIP màu xanh lam. Khi có vitamin C, dung dịch DCPIP bị mất màu nhanh chóng và trở nên trong suốt không màu."
    }
]

B4_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_biomolecules": {"start": 1, "end": 6},
    "sec-biomolecules": {"start": 1, "end": 6},
    "sec_carbohydrates": {"start": 2, "end": 2},
    "sec-carbohydrates": {"start": 2, "end": 2},
    "sec_lipids": {"start": 3, "end": 3},
    "sec-lipids": {"start": 3, "end": 3},
    "sec_proteins": {"start": 4, "end": 4},
    "sec-proteins": {"start": 4, "end": 4},
    "sec_dna": {"start": 5, "end": 5},
    "sec-dna": {"start": 5, "end": 5},
    "sec_water": {"start": 6, "end": 6},
    "sec-water": {"start": 6, "end": 6},
    "sec_food_tests": {"start": 7, "end": 12},
    "sec-food-tests": {"start": 7, "end": 12},
    "sec_test_sugar": {"start": 8, "end": 8},
    "sec-test-sugar": {"start": 8, "end": 8},
    "sec_test_starch": {"start": 9, "end": 9},
    "sec-test-starch": {"start": 9, "end": 9},
    "sec_test_protein": {"start": 10, "end": 10},
    "sec-test-protein": {"start": 10, "end": 10},
    "sec_test_lipid": {"start": 11, "end": 11},
    "sec-test-lipid": {"start": 11, "end": 11},
    "sec_test_vitc": {"start": 12, "end": 12},
    "sec-test-vitc": {"start": 12, "end": 12}
}

# =====================================================================
# B5: ENZYMES
# =====================================================================
B5_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B5: Enzyme & Xúc tác Sinh học",
        "selector": "#sec-header",
        "en": "Welcome to Topic B5: Enzymes. Enzymes are biological catalysts that accelerate every biochemical reaction in living cells without being consumed. In this topic, we study the lock and key model and examine the critical impacts of temperature and pH on enzyme activity.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B5: Enzyme và Xúc tác Sinh học. Enzyme là các chất xúc tác sinh học giúp đẩy nhanh mọi phản ứng hóa sinh trong tế bào sống mà không bị biến đổi hay tiêu hao. Trong chuyên đề này, chúng ta sẽ tìm hiểu mô hình ổ khóa và chìa khóa, cùng tác động then chốt của nhiệt độ và độ pH lên hoạt tính enzyme."
    },
    {
        "id": "sec_enzyme_nature",
        "title": "1. Bản chất & Đặc tính của Enzyme (Nature of Enzymes Overview)",
        "selector": "#sec-enzyme-nature",
        "en": "Section 1 defines catalysts and enzymes: A catalyst is a substance that increases the rate of a chemical reaction and is not changed by the reaction. Enzymes are proteins that are involved in all metabolic reactions, where they function as biological catalysts.",
        "vi": "Mục một định nghĩa chất xúc tác và enzyme: Chất xúc tác là chất làm tăng tốc độ phản ứng hóa học và không bị thay đổi sau phản ứng. Enzyme là các protein tham gia vào mọi phản ứng trao đổi chất, đóng vai trò là chất xúc tác sinh học."
    },
    {
        "id": "sec_enzyme_properties",
        "title": "⭐ Key Properties of Enzymes (Đặc tính Trọng tâm)",
        "selector": "#sec-enzyme-properties",
        "en": "Key enzyme properties: All enzymes are proteins. They are highly specific, catalyzing only one particular reaction. They remain completely unchanged after the reaction and can be reused repeatedly. They work by lowering the activation energy needed for reactions to occur.",
        "vi": "Các đặc tính cốt lõi của enzyme: Mọi enzyme đều có bản chất là protein. Chúng có tính đặc hiệu cao, chỉ xúc tác cho một phản ứng duy nhất. Chúng hoàn toàn không đổi sau phản ứng và có thể tái sử dụng nhiều lần. Chúng hoạt động bằng cách hạ thấp năng lượng hoạt hóa cần thiết cho phản ứng."
    },
    {
        "id": "sec_lock_and_key",
        "title": "2. Cơ chế Hoạt động: Mô hình Ổ khóa và Chìa khóa (Lock & Key Overview)",
        "selector": "#sec-lock-and-key",
        "en": "Section 2 explains the Lock and Key hypothesis: The active site of an enzyme possesses a complementary 3D shape into which only a specific substrate molecule can fit, like a key into a lock.",
        "vi": "Mục hai giải thích thuyết Ổ khóa và Chìa khóa: Trung tâm hoạt động của enzyme có cấu trúc không gian 3 chiều bổ sung chuẩn xác, chỉ cho phép phân tử cơ chất đặc hiệu khớp khít vào, tương tự như chiếc chìa khóa cắm vào đúng ổ khóa."
    },
    {
        "id": "sec_lock_key_mechanism",
        "title": "🔬 Three Stages of Lock & Key Mechanism (Ba Bước Phản ứng)",
        "selector": "#sec-lock-key-mechanism",
        "en": "Reaction stages: First, the substrate approaches the complementary active site. Second, the substrate binds to form a temporary enzyme-substrate complex where chemical bonds are broken or made. Third, the products leave the active site, leaving the enzyme completely unchanged and ready for the next substrate.",
        "vi": "Ba giai đoạn phản ứng: Bước một, cơ chất tiến vào trung tâm hoạt động bổ sung. Bước hai, cơ chất liên kết tạo thành phức hệ enzyme-cơ chất tạm thời, nơi các liên kết hóa học được bẻ gãy hoặc tạo mới. Bước ba, sản phẩm rời khỏi trung tâm hoạt động, trả lại phân tử enzyme nguyên vẹn sẵn sàng đón cơ chất tiếp theo."
    },
    {
        "id": "sec_temp_ph",
        "title": "3. Ảnh hưởng của Nhiệt độ & Độ pH (Temperature & pH Overview)",
        "selector": "#sec-temp-ph",
        "en": "Section 3 investigates environmental impacts on enzyme kinetics: Temperature alters kinetic energy and causes thermal denaturation, while pH extremes disrupt ionic bonds maintaining the active site shape.",
        "vi": "Mục ba nghiên cứu tác động của môi trường lên động học enzyme: Nhiệt độ làm thay đổi động năng phân tử và gây biến tính nhiệt, trong khi độ pH cực đoan làm phá vỡ các liên kết ion duy trì hình thể trung tâm hoạt động."
    },
    {
        "id": "sec_temp_effect",
        "title": "🔥 Temperature Effect & Denaturation (Nhiệt độ & Biến tính)",
        "selector": "#sec-temp-effect",
        "en": "Temperature effects: At low temperatures, molecules have low kinetic energy and collide infrequently. As temperature rises to the optimum around 37°C in humans, reaction rate reaches maximum. Above optimum, excessive thermal vibration breaks bonds holding the tertiary structure; the active site permanently changes shape and denatures, halting the reaction.",
        "vi": "Tác động nhiệt độ: Ở nhiệt độ thấp, phân tử có động năng thấp nên ít va chạm. Khi nhiệt độ tăng đến mức tối ưu khoảng 37°C ở người, tốc độ phản ứng đạt cực đại. Vượt qua nhiệt độ tối ưu, các dao động nhiệt phá vỡ liên kết cấu trúc bậc 3; trung tâm hoạt động biến đổi vĩnh viễn hình dạng và enzyme bị biến tính, khiến phản ứng ngừng trệ."
    },
    {
        "id": "sec_ph_effect",
        "title": "🧪 Optimum pH in Human Digestion (Độ pH Tối ưu trong Tiêu hóa)",
        "selector": "#sec-ph-effect",
        "en": "pH effects: Each enzyme has an optimum pH. For example, stomach pepsin operates optimally in acidic conditions at pH 2, while intestinal amylase and lipase require alkaline conditions around pH 8. Deviations from optimum pH alter ionic charges and denature the active site.",
        "vi": "Tác động độ pH: Mỗi enzyme có một mức pH tối ưu riêng. Ví dụ, pepsin dạ dày hoạt động tối ưu trong môi trường acid mạnh ở pH 2, trong khi amylase và lipase ruột non lại cần môi trường kiềm khoảng pH 8. Độ pH lệch xa mức tối ưu sẽ làm thay đổi điện tích và biến tính trung tâm hoạt động."
    }
]

B5_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_enzyme_nature": {"start": 1, "end": 2},
    "sec-enzyme-nature": {"start": 1, "end": 2},
    "sec_enzyme_properties": {"start": 2, "end": 2},
    "sec-enzyme-properties": {"start": 2, "end": 2},
    "sec_lock_and_key": {"start": 3, "end": 4},
    "sec-lock-and-key": {"start": 3, "end": 4},
    "sec_lock_key_mechanism": {"start": 4, "end": 4},
    "sec-lock-key-mechanism": {"start": 4, "end": 4},
    "sec_temp_ph": {"start": 5, "end": 7},
    "sec-temp-ph": {"start": 5, "end": 7},
    "sec_temp_effect": {"start": 6, "end": 6},
    "sec-temp-effect": {"start": 6, "end": 6},
    "sec_ph_effect": {"start": 7, "end": 7},
    "sec-ph-effect": {"start": 7, "end": 7}
}

# =====================================================================
# B6: PLANT NUTRITION & PHOTOSYNTHESIS
# =====================================================================
B6_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề B6: Quang hợp & Dinh dưỡng Thực vật",
        "selector": "#sec-header",
        "en": "Welcome to Topic B6: Plant Nutrition. Plants are autotrophic organisms that manufacture their own food through photosynthesis. In this topic, we master the photosynthetic equations, the fate of synthesized glucose, essential mineral ions, leaf anatomy adaptations, and limiting factors.",
        "vi": "Chào mừng các bạn đến với Chuyên đề B6: Dinh dưỡng Thực vật và Quang hợp. Thực vật là sinh vật tự dưỡng, tự tổng hợp thức ăn qua quang hợp. Trong chuyên đề này, chúng ta sẽ làm chủ phương trình quang hợp, số phận của phân tử glucose, ion khoáng thiết yếu, cấu trúc thích nghi của lá cây và các yếu tố giới hạn."
    },
    {
        "id": "sec_photosynthesis",
        "title": "1. Quá trình & Phương trình Quang hợp (Photosynthesis Overview)",
        "selector": "#sec-photosynthesis",
        "en": "Section 1 defines photosynthesis: the process by which plants synthesise carbohydrates from raw materials (carbon dioxide and water) using light energy. Word equation: carbon dioxide plus water in the presence of light and chlorophyll produces glucose plus oxygen. Balanced chemical equation: 6CO₂ + 6H₂O yields C₆H₁₂O₆ + 6O₂.",
        "vi": "Mục một định nghĩa quang hợp: là quá trình thực vật tổng hợp carbohydrate từ nguyên liệu vô cơ (carbon dioxide và nước) bằng năng lượng ánh sáng. Phương trình chữ: carbon dioxide cộng nước, với ánh sáng và diệp lục, tạo ra glucose cộng oxy. Phương trình hóa học cân bằng: 6CO2 cộng 6H2O tạo ra C6H12O6 cộng 6O2."
    },
    {
        "id": "sec_glucose_minerals",
        "title": "2. Sử dụng Glucose & Khoáng chất Thiết yếu (Glucose & Minerals Overview)",
        "selector": "#sec-glucose-minerals",
        "en": "Section 2 covers the utilisation of glucose and essential plant minerals: Glucose is converted into storage starch, structural cellulose, sucrose for phloem transport, or oxidised in respiration. Plants absorb nitrate ions for amino acid synthesis and magnesium ions to build chlorophyll.",
        "vi": "Mục hai phân tích việc sử dụng glucose và các khoáng chất thiết yếu: Glucose được chuyển hóa thành tinh bột dự trữ, cellulose tạo thành tế bào, sucrose vận chuyển trong mạch rây hoặc oxy hóa trong hô hấp. Cây hấp thu ion nitrat để tổng hợp amino acid và ion magie để tạo diệp lục."
    },
    {
        "id": "sec_glucose_uses",
        "title": "🍬 Fate of Glucose in Plants (Số phận Phân tử Glucose)",
        "selector": "#sec-glucose-uses",
        "en": "Uses of glucose: Starch is an insoluble storage polymer stored in chloroplasts and tubers without exerting osmotic effects. Cellulose builds cell walls. Respiration breaks down glucose to release energy. Sucrose is the transport carbohydrate translocated in phloem sieve tubes. Nectar attracts pollinators.",
        "vi": "Số phận của glucose: Tinh bột là polymer dự trữ không tan trong lục lạp và củ rễ, không gây áp suất thẩm thấu. Cellulose xây dựng thành tế bào. Hô hấp tế bào phân giải glucose để giải phóng ATP. Sucrose là dạng đường vận chuyển trong mạch rây. Mật hoa thu hút côn trùng thụ phấn."
    },
    {
        "id": "sec_minerals",
        "title": "🌾 Essential Mineral Ions (Ion Khoáng Thiết yếu)",
        "selector": "#sec-minerals",
        "en": "Essential mineral ions: Nitrate ions supply nitrogen to build amino acids and proteins; deficiency causes stunted growth and yellow older leaves. Magnesium ions are the central atom in chlorophyll; deficiency causes chlorosis, resulting in yellow leaves with green veins.",
        "vi": "Ion khoáng thiết yếu: Ion nitrat cung cấp nguyên tố nitơ để tổng hợp amino acid và protein; thiếu nitrat cây bị còi cọc và vàng lá già. Ion magie là nguyên tử trung tâm của phân tử diệp lục; thiếu magie cây bị bệnh úa vàng (chlorosis) làm lá mất màu xanh."
    },
    {
        "id": "sec_leaf_anatomy",
        "title": "3. Cấu tạo Giải phẫu Lá cây (Leaf Anatomy Overview)",
        "selector": "#sec-leaf-anatomy",
        "en": "Section 3 examines dicotyledonous leaf adaptations: The broad, thin blade maximizes sunlight capture and shortens gas diffusion pathways.",
        "vi": "Mục ba khảo sát giải phẫu thích nghi của lá cây hai lá mầm: Phiến lá rộng và mỏng giúp hấp thu tối đa ánh sáng mặt trời và rút ngắn quãng đường khuếch tán khí."
    },
    {
        "id": "sec_leaf_cuticle",
        "title": "💧 Cuticle & Upper Epidermis (Lớp Cutin & Biểu bì Trên)",
        "selector": "#sec-leaf-cuticle",
        "en": "The waxy cuticle is a waterproof transparent layer that prevents water loss by evaporation. The upper epidermis consists of transparent cells without chloroplasts, letting light penetrate into the palisade layer below.",
        "vi": "Lớp cutin sáp không thấm nước giúp ngăn ngừa mất nước do bốc hơi. Biểu bì trên gồm một lớp tế bào trong suốt không chứa lục lạp, cho phép ánh sáng chiếu xuyên qua thẳng xuống tầng mô giậu bên dưới."
    },
    {
        "id": "sec_leaf_palisade",
        "title": "☀️ Palisade Mesophyll (Mô giậu Quang hợp)",
        "selector": "#sec-leaf-palisade",
        "en": "Palisade mesophyll consists of tall, vertically packed columnar cells containing the highest concentration of chloroplasts. Positioned at the top of the leaf, it is the primary site of photosynthesis.",
        "vi": "Mô giậu gồm các tế bào hình cột xếp khít thẳng đứng chứa mật độ lục lạp cao nhất lá cây. Nằm ngay sát mặt trên của lá, đây là nơi diễn ra phần lớn quá trình quang hợp."
    },
    {
        "id": "sec_leaf_spongy",
        "title": "💨 Spongy Mesophyll (Mô xốp Khí khổng)",
        "selector": "#sec-leaf-spongy",
        "en": "Spongy mesophyll features loosely arranged rounded cells with large intercellular air spaces. These air spaces allow rapid diffusion of carbon dioxide and oxygen between stomata and photosynthetic cells.",
        "vi": "Mô xốp gồm các tế bào tròn xếp lỏng lẻo tạo nên nhiều khoảng gian bào lớn. Các khoang khí này cho phép khí CO2 và O2 khuếch tán nhanh chóng giữa khí khổng và các tế bào quang hợp."
    },
    {
        "id": "sec_leaf_vein",
        "title": "🌿 Vascular Bundle (Bó Mạch: Gỗ & Rây)",
        "selector": "#sec-leaf-vein",
        "en": "The vascular bundle contains xylem vessels delivering water and mineral ions from roots to mesophyll cells, and phloem sieve tubes translocating sucrose and amino acids away from the leaf to growing sinks.",
        "vi": "Bó mạch dẫn gồm mạch gỗ (xylem) vận chuyển nước và ion khoáng từ rễ lên mô lá, và mạch rây (phloem) vận chuyển đường sucrose và amino acid từ lá đến các cơ quan dự trữ và sinh trưởng."
    },
    {
        "id": "sec_leaf_stomata",
        "title": "🚪 Stomata & Guard Cells (Khí khổng & Tế bào Khí khổng)",
        "selector": "#sec-leaf-stomata",
        "en": "Stomata are microscopic pores mainly on the lower epidermis, bordered by paired guard cells. Guard cells swell with water to open stomata for gas exchange and shrink to close them, preventing excessive transpiration.",
        "vi": "Khí khổng là các lỗ hiển vi tập trung ở biểu bì dưới, được đóng mở bởi cặp tế bào hình hạt đậu. Tế bào hạt đậu trương nước làm mở khí khổng để trao đổi khí và xẹp lại khi mất nước để hạn chế thoát hơi nước."
    },
    {
        "id": "sec_limiting_factors",
        "title": "4. Yếu tố Giới hạn & Chất Chỉ thị (Limiting Factors Overview)",
        "selector": "#sec-limiting-factors",
        "en": "Section 4 investigates environmental factors that limit the rate of photosynthesis: light intensity, carbon dioxide concentration, and temperature, alongside hydrogencarbonate indicator experiments.",
        "vi": "Mục bốn phân tích các yếu tố môi trường giới hạn tốc độ quang hợp: cường độ ánh sáng, nồng độ CO2 và nhiệt độ, cùng thí nghiệm chất chỉ thị hydrogencarbonate."
    },
    {
        "id": "sec_limiting_detail",
        "title": "☀️ Limiting Factors (Các Yếu tố Giới hạn)",
        "selector": "#sec-limiting-detail",
        "en": "A limiting factor is something present in the environment in such short supply that it restricts life processes. Increasing light intensity or carbon dioxide concentration increases photosynthetic rate until another factor becomes limiting. Temperature increases rate up to the optimum before enzymes denature.",
        "vi": "Yếu tố giới hạn là yếu tố có nồng độ thấp nhất trong môi trường gây kìm hãm tốc độ phản ứng. Tăng cường độ ánh sáng hoặc nồng độ CO2 sẽ làm tăng tốc độ quang hợp cho đến khi một yếu tố khác trở thành yếu tố giới hạn. Nhiệt độ làm tăng tốc độ cho tới nhiệt độ tối ưu trước khi enzyme bị biến tính."
    },
    {
        "id": "sec_hydrogencarbonate",
        "title": "🧪 Hydrogencarbonate Indicator (Chỉ thị Hydrogencarbonate)",
        "selector": "#sec-hydrogencarbonate",
        "en": "Hydrogencarbonate indicator detects carbon dioxide levels: In bright light, photosynthesis exceeds respiration, consuming CO2 and turning the indicator purple. In darkness, only respiration occurs, producing CO2 and turning the indicator yellow. In dim light at compensation point, rates are equal and the indicator remains red.",
        "vi": "Chỉ thị hydrogencarbonate phát hiện nồng độ CO2: Khi có ánh sáng mạnh, quang hợp mạnh hơn hô hấp làm giảm CO2, dung dịch hóa tím. Trong bóng tối, chỉ có hô hấp sinh ra CO2, dung dịch hóa vàng. Trong ánh sáng yếu tại điểm bù, tốc độ bằng nhau nên dung dịch giữ màu đỏ."
    }
]

B6_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0},
    "sec-header": {"start": 0, "end": 0},
    "sec_photosynthesis": {"start": 1, "end": 1},
    "sec-photosynthesis": {"start": 1, "end": 1},
    "sec_glucose_minerals": {"start": 2, "end": 4},
    "sec-glucose-minerals": {"start": 2, "end": 4},
    "sec_glucose_uses": {"start": 3, "end": 3},
    "sec-glucose-uses": {"start": 3, "end": 3},
    "sec_minerals": {"start": 4, "end": 4},
    "sec-minerals": {"start": 4, "end": 4},
    "sec_leaf_anatomy": {"start": 5, "end": 10},
    "sec-leaf-anatomy": {"start": 5, "end": 10},
    "sec_leaf_cuticle": {"start": 6, "end": 6},
    "sec-leaf-cuticle": {"start": 6, "end": 6},
    "sec_leaf_palisade": {"start": 7, "end": 7},
    "sec-leaf-palisade": {"start": 7, "end": 7},
    "sec_leaf_spongy": {"start": 8, "end": 8},
    "sec-leaf-spongy": {"start": 8, "end": 8},
    "sec_leaf_vein": {"start": 9, "end": 9},
    "sec-leaf-vein": {"start": 9, "end": 9},
    "sec_leaf_stomata": {"start": 10, "end": 10},
    "sec-leaf-stomata": {"start": 10, "end": 10},
    "sec_limiting_factors": {"start": 11, "end": 13},
    "sec-limiting-factors": {"start": 11, "end": 13},
    "sec_limiting_detail": {"start": 12, "end": 12},
    "sec-limiting-detail": {"start": 12, "end": 12},
    "sec_hydrogencarbonate": {"start": 13, "end": 13},
    "sec-hydrogencarbonate": {"start": 13, "end": 13}
}


async def main():
    print("=================================================================")
    print("STARTING BATCH 1 AUDIO GENERATION (B3, B4, B5, B6)")
    print("=================================================================")
    
    # Process B3
    await process_lecture_audio(
        lecture_code="b3",
        lecture_id="9a23109e-ad73-4fcf-a599-9605cc4906eb",
        course_title=COURSE_TITLE,
        lecture_title="B3: Movement into and out of cells",
        segments=B3_SEGMENTS,
        major_sections=B3_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B4
    await process_lecture_audio(
        lecture_code="b4",
        lecture_id="757409b3-5cec-4e1f-8877-18d81e440103",
        course_title=COURSE_TITLE,
        lecture_title="B4: Biological molecules",
        segments=B4_SEGMENTS,
        major_sections=B4_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B5
    await process_lecture_audio(
        lecture_code="b5",
        lecture_id="8ab2afa2-59e3-4c56-8971-8d93dec5ad8e",
        course_title=COURSE_TITLE,
        lecture_title="B5: Enzymes",
        segments=B5_SEGMENTS,
        major_sections=B5_MAJOR_SECTIONS,
        subject="science"
    )
    
    # Process B6
    await process_lecture_audio(
        lecture_code="b6",
        lecture_id="1d6a6b7b-ae57-404f-9ad1-58b11219b4d1",
        course_title=COURSE_TITLE,
        lecture_title="B6: Plant nutrition",
        segments=B6_SEGMENTS,
        major_sections=B6_MAJOR_SECTIONS,
        subject="science"
    )
    
    print("\n🎉 BATCH 1 (B3, B4, B5, B6) AUDIO & MANIFESTS GENERATION COMPLETED!")

if __name__ == "__main__":
    asyncio.run(main())
