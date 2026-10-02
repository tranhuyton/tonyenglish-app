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
# C9: METALS
# =====================================================================
C9_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C9: Kim loại, Dãy Hoạt động & Luyện kim",
        "selector": "#sec-header",
        "en": "Welcome to Topic C9: Metals. Metals are essential materials underpinning global infrastructure. In this lesson, we analyze physical and chemical properties of metals and alloys, master the reactivity series and displacement reactions, investigate the extraction of iron in the blast furnace, and explore vital uses of metals.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C9: Kim loại, Dãy Hoạt động Hóa học và Luyện kim. Kim loại là nền tảng của mọi công trình kỹ thuật. Trong bài học này, chúng ta sẽ khảo sát tính chất của kim loại và hợp kim, làm chủ dãy hoạt động hóa học và phản ứng thế, tìm hiểu quy trình luyện gang thép trong lò cao, cùng các ứng dụng thực tế quan trọng."
    },
    {
        "id": "sec_properties_alloys",
        "title": "1. Tính chất Vật lý của Kim loại & Cấu trúc Hợp kim (Properties & Alloys Overview)",
        "selector": "#sec-properties-alloys",
        "en": "Section 1 reviews metallic properties: good thermal and electrical conductivity, malleability, ductility, and high density. It explains why alloys are engineered to improve strength.",
        "vi": "Mục một tổng kết tính chất kim loại: dẫn nhiệt và dẫn điện tốt, dễ dát mỏng, dễ uốn dẻo và khối lượng riêng cao. Đồng thời giải thích cơ chế tạo hợp kim để tăng cường độ cứng."
    },
    {
        "id": "sec_alloys_hardness",
        "title": "🛡️ Why are Alloys Harder? (Tại sao Hợp kim Cứng hơn?)",
        "selector": "#sec-alloys-hardness",
        "en": "In pure metals, identical atoms are arranged in regular layers that slide easily over one another when force is applied. In an alloy, atoms of different sizes disrupt the regular lattice layers, preventing them from sliding easily and making the alloy much harder.",
        "vi": "Trong kim loại nguyên chất, các nguyên tử cùng kích thước xếp thành các lớp đều đặn dễ trượt qua nhau khi có ngoại lực tác dụng. Trong hợp kim, sự hiện diện của các nguyên tử có kích thước khác nhau làm biến dạng mạng tinh thể, cản trở các lớp trượt qua nhau, giúp hợp kim cứng hơn rất nhiều."
    },
    {
        "id": "sec_reactivity_series",
        "title": "2. Dãy Hoạt động Hóa học & Phản ứng Thế (The Reactivity Series Overview)",
        "selector": "#sec-reactivity-series",
        "en": "Section 2 establishes the Reactivity Series: ordering metals from most reactive to least reactive based on their tendency to form positive ions by losing electrons.",
        "vi": "Mục hai thiết lập Dãy Hoạt động Hóa học: sắp xếp các kim loại từ mạnh nhất đến yếu nhất dựa trên xu hướng nhường electron tạo cation dương."
    },
    {
        "id": "sec_reactivity_mnemonic",
        "title": "🧠 Reactivity Series Mnemonic (Mẹo nhớ Dãy Hoạt động)",
        "selector": "#sec-reactivity-mnemonic",
        "en": "Remember the mnemonic: Please Send Charlie's Monkeys And Cute Zebras In Heavy Lead Cages Securely Guarded. Potassium, Sodium, Calcium, Magnesium, Aluminium, Carbon, Zinc, Iron, Hydrogen, Copper, Silver, Gold.",
        "vi": "Mẹo nhớ kinh điển tiếng Việt: Khi Nào Bạn Cần May Áo Giáp Sắt Nhớ Sang Phố Hỏi Cửa Hàng Á Phi Âu. Tương ứng Kali, Natri, Canxi, Magie, Nhôm, Cacbon, Kẽm, Sắt, Chì, Hydro, Đồng, Bạc, Vàng."
    },
    {
        "id": "sec_displacement_reactions",
        "title": "⚔️ Displacement Reactions (Phản ứng Thế Kim loại)",
        "selector": "#sec-displacement-reactions",
        "en": "In a displacement reaction, a more reactive metal displaces a less reactive metal from its aqueous solution or metal oxide. For example, zinc displaces copper from copper sulfate solution, forming colorless zinc sulfate and brown copper metal.",
        "vi": "Trong phản ứng thế, kim loại hoạt động mạnh hơn sẽ đẩy kim loại kém hoạt động hơn ra khỏi dung dịch muối hoặc oxit kim loại. Ví dụ kẽm đẩy đồng ra khỏi dung dịch đồng sunfat, làm mất màu xanh và giải phóng kim loại đồng màu nâu đỏ."
    },
    {
        "id": "sec_extraction_metals",
        "title": "3. Phương pháp Luyện kim & Lò cao (Extraction of Metals Overview)",
        "selector": "#sec-extraction-metals",
        "en": "Section 3 covers metal extraction: Metals less reactive than carbon, such as iron and zinc, are extracted by reduction using carbon or carbon monoxide. Highly reactive metals above carbon require electrolysis.",
        "vi": "Mục ba trình bày phương pháp luyện kim: Kim loại kém hoạt động hơn cacbon như sắt và kẽm được điều chế bằng phản ứng nhiệt luyện khử bởi cacbon hoặc CO. Các kim loại hoạt động mạnh đứng trên cacbon bắt buộc phải dùng phương pháp điện phân nóng chảy."
    },
    {
        "id": "sec_blast_furnace",
        "title": "🏭 Blast Furnace Iron Extraction (Luyện Sắt trong Lò cao)",
        "selector": "#sec-blast-furnace",
        "en": "In the blast furnace, iron(III) oxide haematite is reduced to molten iron. Coke burns in hot air producing carbon monoxide, the primary reducing agent. Limestone thermal decomposition generates calcium oxide, which reacts with acidic silica impurities to form molten slag.",
        "vi": "Trong lò cao, quặng sắt hematit Fe2O3 được khử thành sắt nóng chảy. Than cốc cháy tạo khí CO đóng vai trò chất khử chính. Đá vôi bị nhiệt phân sinh ra canxi oxit, kết hợp với tạp chất cát silic dioxit có tính axit để tạo thành xỉ canxi silicat nổi lên trên."
    },
    {
        "id": "sec_uses_metals",
        "title": "4. Ứng dụng Thực tiễn của Kim loại (Uses of Metals Overview)",
        "selector": "#sec-uses-metals",
        "en": "Section 4 relates properties to everyday uses: Aluminium, copper, and various steels are matched precisely to their technological roles.",
        "vi": "Mục bốn liên hệ tính chất với ứng dụng đời sống: Nhôm, đồng và các loại thép được ứng dụng chuẩn xác vào các vai trò kỹ thuật khác nhau."
    },
    {
        "id": "sec_metal_uses_cases",
        "title": "🛠️ Specific Uses of Metals & Alloys (Các Ứng dụng Đặc thù)",
        "selector": "#sec-metal-uses-cases",
        "en": "Aluminium is used for aircraft bodies due to low density and strength, and food packaging due to protective oxide layer. Copper is used for electrical wiring due to excellent electrical conductivity. Mild steel is used for car bodies and machinery. Stainless steel is used for cutlery and chemical plant equipment due to rust resistance.",
        "vi": "Nhôm dùng làm thân máy bay nhờ khối lượng riêng thấp và bền, làm bao bì thực phẩm nhờ màng oxit bảo vệ không độc. Đồng dùng làm dây dẫn điện nhờ độ dẫn điện xuất sắc. Thép mềm dùng làm khung xe hơi và máy móc. Thép không gỉ dùng làm dao kéo và bồn chứa hóa chất nhờ khả năng chống gỉ tuyệt đối."
    }
]

C9_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C9", "selector": "#sec-header"},
    "sec_properties_alloys": {"start": 1, "end": 2, "title": "1. Tính chất & Hợp kim", "selector": "#sec-properties-alloys"},
    "sec_reactivity_series": {"start": 3, "end": 5, "title": "2. Dãy Hoạt động & Phản ứng Thế", "selector": "#sec-reactivity-series"},
    "sec_extraction_metals": {"start": 6, "end": 7, "title": "3. Luyện kim & Lò cao", "selector": "#sec-extraction-metals"},
    "sec_uses_metals": {"start": 8, "end": 9, "title": "4. Ứng dụng Thực tiễn", "selector": "#sec-uses-metals"}
}


# =====================================================================
# C10: CHEMISTRY OF THE ENVIRONMENT
# =====================================================================
C10_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C10: Hóa học Môi trường, Nước & Không khí",
        "selector": "#sec-header",
        "en": "Welcome to Topic C10: Chemistry of the Environment. Environmental chemistry investigates vital natural resources. In this topic, we examine water purification and testing, explore the composition of clean air, pollutants, and catalytic converters, and study rust prevention and synthetic NPK fertilizers.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C10: Hóa học Môi trường, Nguồn Nước và Không khí. Hóa học môi trường nghiên cứu các tài nguyên sinh thái thiết yếu. Trong bài học này, chúng ta sẽ tìm hiểu quy trình xử lý và kiểm tra độ tinh khiết của nước, thành phần không khí sạch, các chất ô nhiễm và bộ chuyển đổi xúc tác, cùng biện pháp chống rỉ sét và phân bón NPK."
    },
    {
        "id": "sec_water_chemistry",
        "title": "1. Hóa học Nguồn nước: Nhận biết & Xử lý (Water Chemistry Overview)",
        "selector": "#sec-water-chemistry",
        "en": "Section 1 addresses Water: Chemical tests for water and the industrial treatment stages converting raw river water into safe drinking water.",
        "vi": "Mục một đề cập đến Nguồn nước: Các phản ứng hóa học nhận biết nước và quy trình xử lý công nghiệp biến nước sông tự nhiên thành nước sinh hoạt an toàn."
    },
    {
        "id": "sec_water_treatment",
        "title": "🚰 Water Purification & Tests (Quy trình Xử lý & Nhận biết Nước)",
        "selector": "#sec-water-treatment",
        "en": "Water treatment involves sedimentation and filtration to remove insoluble solids, carbon treatment for odor, and chlorination to kill harmful microbes. Water presence is tested using anhydrous cobalt(II) chloride which turns from blue to pink, or anhydrous copper(II) sulfate turning white to blue. Pure water boils precisely at 100 degrees Celsius.",
        "vi": "Xử lý nước gồm lắng đọng và lọc cát để loại bỏ chất rắn không tan, lọc than hoạt tính khử mùi và khử trùng bằng clo để tiêu diệt vi khuẩn. Nhận biết nước bằng coban hai clorua khan đổi từ xanh sang hồng hoặc đồng hai sunfat khan từ trắng sang xanh. Nước cất tinh khiết sôi chính xác ở 100 độ C."
    },
    {
        "id": "sec_air_pollution",
        "title": "2. Thành phần Khí quyển & Chất Ô nhiễm (Air & Pollution Overview)",
        "selector": "#sec-air-pollution",
        "en": "Section 2 analyzes atmospheric composition and dangerous pollutants: Clean dry air is approximately 78 percent nitrogen, 21 percent oxygen, with argon, carbon dioxide, and other gases.",
        "vi": "Mục hai phân tích thành phần khí quyển và các chất ô nhiễm nguy hiểm: Không khí khô sạch chứa khoảng 78 phần trăm nitơ, 21 phần trăm oxy, còn lại là argon, carbon dioxide và các khí khác."
    },
    {
        "id": "sec_clean_air_composition",
        "title": "🌬️ Clean Air Composition (Thành phần Không khí Sạch)",
        "selector": "#sec-clean-air-composition",
        "en": "Clean air consists of 78% nitrogen, 21% oxygen, 0.9% argon, and 0.04% carbon dioxide. Oxygen supports respiration and combustion, while nitrogen is an unreactive diluent.",
        "vi": "Không khí sạch bao gồm 78% nitơ, 21% oxy, 0.9% argon và 0.04% carbon dioxide. Khí oxy duy trì hô hấp và sự cháy, trong khi khí nitơ đóng vai trò chất đệm trơ về mặt hóa học."
    },
    {
        "id": "sec_pollutants_catalytic",
        "title": "🚗 Pollutants & Catalytic Converters (Chất Ô nhiễm & Xúc tác Ô tô)",
        "selector": "#sec-pollutants-catalytic",
        "en": "Carbon monoxide from incomplete combustion causes poisoning. Sulfur dioxide and nitrogen oxides cause acid rain. Catalytic converters in car exhausts use platinum or rhodium to convert carbon monoxide and nitrogen oxides into harmless carbon dioxide and nitrogen.",
        "vi": "Khí CO do đốt cháy không hoàn toàn gây ngộ độc máu. Khí SO2 và NOx gây mưa axit phá hủy rừng và các công trình. Bộ chuyển đổi xúc tác trên ô tô dùng bạch kim và rodi biến khí độc CO và NOx thành CO2 và N2 vô hại."
    },
    {
        "id": "sec_rusting_fertilizers",
        "title": "3. Rỉ sét & Phân bón NPK (Rusting & Fertilizers Overview)",
        "selector": "#sec-rusting-fertilizers",
        "en": "Section 3 investigates the corrosion of iron and the role of synthetic chemical fertilizers in agricultural crop yields.",
        "vi": "Mục ba nghiên cứu sự ăn mòn kim loại sắt và vai trò của phân bón hóa học tổng hợp trong năng suất cây trồng."
    },
    {
        "id": "sec_rust_prevention",
        "title": "🛡️ Rusting & Prevention Methods (Cơ chế & Chống Rỉ sét)",
        "selector": "#sec-rust-prevention",
        "en": "Rusting of iron requires both oxygen and water, forming hydrated iron(III) oxide. Prevention methods include barrier methods like painting and greasing, galvanising with zinc, and sacrificial protection where more reactive zinc corrodes preferentially.",
        "vi": "Sự rỉ sét của sắt bắt buộc phải có đồng thời cả oxy và nước, tạo ra sắt ba oxit ngậm nước. Các biện pháp phòng chống gồm phương pháp rào cản như sơn hoặc bôi dầu mỡ, mạ kẽm (galvanising) và bảo vệ bằng vật hiến sinh nơi kẽm hoạt động mạnh hơn sẽ bị ăn mòn trước để bảo vệ sắt."
    },
    {
        "id": "sec_npk_fertilizers",
        "title": "🌱 NPK Fertilizers (Phân bón NPK)",
        "selector": "#sec-npk-fertilizers",
        "en": "NPK fertilizers provide three essential elements: Nitrogen for healthy leafy shoot growth, Phosphorus for root development, and Potassium for flowering and disease resistance.",
        "vi": "Phân bón NPK cung cấp ba nguyên tố dinh dưỡng khoáng đa lượng: Nitơ giúp phát triển thân lá xanh tốt, Photpho kích thích bộ rễ phát triển khỏe mạnh, và Kali giúp ra hoa đậu quả và tăng sức đề kháng sâu bệnh."
    }
]

C10_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C10", "selector": "#sec-header"},
    "sec_water_chemistry": {"start": 1, "end": 2, "title": "1. Hóa học Nguồn nước & Xử lý", "selector": "#sec-water-chemistry"},
    "sec_air_pollution": {"start": 3, "end": 5, "title": "2. Khí quyển & Ô nhiễm", "selector": "#sec-air-pollution"},
    "sec_rusting_fertilizers": {"start": 6, "end": 8, "title": "3. Chống Rỉ sét & Phân bón NPK", "selector": "#sec-rusting-fertilizers"}
}


# =====================================================================
# C11: ORGANIC CHEMISTRY
# =====================================================================
C11_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C11: Hóa học Hữu cơ & Polymer",
        "selector": "#sec-header",
        "en": "Welcome to Topic C11: Organic Chemistry. Carbon's ability to form four stable covalent bonds creates an extraordinary variety of molecules. In this lesson, we study homologous series and IUPAC naming, explore alkanes, alkenes, cracking, and addition polymerisation.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C11: Hóa học Hữu cơ và Hợp chất Polymer. Khả năng tạo 4 liên kết cộng hóa trị bền vững của carbon tạo nên muôn vàn hợp chất hữu cơ. Trong bài học này, chúng ta sẽ khảo sát dãy đồng đẳng và danh pháp quốc tế, làm chủ ankan, anken, phản ứng bẻ gãy mạch cracking và phản ứng trùng hợp tạo chất dẻo."
    },
    {
        "id": "sec_homologous_series",
        "title": "1. Dãy Đồng đẳng & Danh pháp Hóa học Hữu cơ (Homologous Series Overview)",
        "selector": "#sec-homologous-series",
        "en": "Section 1 defines a Homologous Series: a family of organic compounds with the same functional group, same general formula, similar chemical properties, and a graduation in physical properties.",
        "vi": "Mục một định nghĩa Dãy Đồng đẳng: là tập hợp các hợp chất hữu cơ có cùng nhóm chức, cùng công thức phân tử chung, tính chất hóa học tương tự nhau và tính chất vật lý biến đổi có quy luật."
    },
    {
        "id": "sec_naming_prefixes",
        "title": "🔢 Naming Prefixes: Meth, Eth, Prop, But (Tiền tố Danh pháp Carbon)",
        "selector": "#sec-naming-prefixes",
        "en": "Carbon chain prefixes in Cambridge IGCSE: Meth- for one carbon, Eth- for two carbons, Prop- for three carbons, and But- for four carbons. The suffix indicates family: -ane for alkanes and -ene for alkenes.",
        "vi": "Tiền tố chỉ mạch carbon trong IGCSE: Meth- cho 1 carbon, Eth- cho 2 carbon, Prop- cho 3 carbon, và But- cho 4 carbon. Hậu tố chỉ họ chất: -ane cho ankan và -ene cho anken."
    },
    {
        "id": "sec_hydrocarbons_alkanes_alkenes",
        "title": "2. Hydrocacbon: Ankan vs Anken & Cracking (Hydrocarbons Overview)",
        "selector": "#sec-hydrocarbons-alkanes-alkenes",
        "en": "Section 2 explores hydrocarbons containing only carbon and hydrogen, contrasting saturated alkanes with unsaturated alkenes.",
        "vi": "Mục hai tìm hiểu về hydrocacbon chỉ chứa carbon và hydro, đối chiếu ankan no với anken không no."
    },
    {
        "id": "sec_alkanes_alkenes_diff",
        "title": "⛽ Saturated Alkanes vs Unsaturated Alkenes (Ankan No vs Anken Không No)",
        "selector": "#sec-alkanes-alkenes-diff",
        "en": "Alkanes have general formula CnH2n+2 with only single C-C bonds, making them saturated and relatively unreactive except for combustion. Alkenes have general formula CnH2n containing a C=C double bond, making them unsaturated and reactive.",
        "vi": "Ankan có công thức chung CnH2n+2 chỉ chứa các liên kết đơn C-C nên là hydrocacbon no, khá trơ về mặt hóa học ngoại trừ phản ứng cháy. Anken có công thức CnH2n chứa liên kết đôi C=C nên là hydrocacbon không no và hoạt động hóa học hơn."
    },
    {
        "id": "sec_cracking_bromine",
        "title": "⚡ Cracking & The Bromine Water Test (Cracking & Thuốc thử Brom)",
        "selector": "#sec-cracking-bromine",
        "en": "Cracking breaks long-chain alkanes into smaller, more useful short-chain alkanes and alkenes using high temperature and a catalyst. Alkenes are identified using aqueous bromine: orange-brown bromine water is rapidly decolourised to colourless by alkenes, whereas alkanes show no reaction without UV light.",
        "vi": "Phản ứng cracking bẻ gãy các phân tử ankan mạch dài thành ankan mạch ngắn có giá trị cao hơn cùng các anken nhờ nhiệt độ cao và xúc tác. Nhận biết anken bằng nước brom: dung dịch brom màu nâu cam bị mất màu nhanh chóng khi tác dụng với anken, trong khi ankan không phản ứng trong bóng tối."
    },
    {
        "id": "sec_polymers",
        "title": "3. Phản ứng Trùng hợp & Chất dẻo Polymer (Polymers Overview)",
        "selector": "#sec-polymers",
        "en": "Section 3 investigates Polymers: large macromolecules formed from small repeating units called monomers.",
        "vi": "Mục ba khảo sát Chất dẻo Polymer: là các đại phân tử khổng lồ được tạo nên từ sự liên kết của hàng ngàn đơn vị nhỏ lặp đi lặp lại gọi là monome."
    },
    {
        "id": "sec_addition_polymers",
        "title": "🔗 Addition Polymerisation: Poly(ethene) (Trùng hợp Cộng)",
        "selector": "#sec-addition-polymers",
        "en": "In addition polymerisation, alkene double bonds break open, linking thousands of monomer units into a single long polymer chain without forming any byproduct. For example, ethene monomers polymerise to form poly(ethene), widely used for plastic bags and containers.",
        "vi": "Trong phản ứng trùng hợp cộng, liên kết đôi của các phân tử anken mở ra để liên kết hàng ngàn phân tử monome lại thành một mạch polymer dài duy nhất mà không sinh ra sản phẩm phụ. Ví dụ các monome etilen trùng hợp tạo thành polyetilen, ứng dụng rộng rãi làm túi ni lông và chai nhựa."
    }
]

C11_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C11", "selector": "#sec-header"},
    "sec_homologous_series": {"start": 1, "end": 2, "title": "1. Dãy Đồng đẳng & Danh pháp", "selector": "#sec-homologous-series"},
    "sec_hydrocarbons_alkanes_alkenes": {"start": 3, "end": 5, "title": "2. Ankan, Anken & Cracking", "selector": "#sec-hydrocarbons-alkanes-alkenes"},
    "sec_polymers": {"start": 6, "end": 7, "title": "3. Phản ứng Trùng hợp Polymer", "selector": "#sec-polymers"}
}


# =====================================================================
# C12: EXPERIMENTAL TECHNIQUES & CHEMICAL ANALYSIS
# =====================================================================
C12_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C12: Phương pháp Tách chất & Nhận biết Hóa học",
        "selector": "#sec-header",
        "en": "Welcome to Topic C12: Experimental Techniques and Chemical Analysis. Analytical chemistry provides essential tools for purifying and identifying unknown substances. In this lesson, we study filtration, crystallisation, distillation, paper chromatography, identification of common gases, and characteristic testing for cations and anions.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C12: Phương pháp Tách chất và Nhận biết Hóa học. Hóa phân tích cung cấp các công cụ thiết yếu để tinh chế và xác định chất chưa biết. Trong bài học này, chúng ta sẽ học lọc, kết tinh, chưng cất, sắc ký giấy, nhận biết các chất khí thông dụng, cùng thuốc thử đặc trưng cho các cation kim loại và anion phi kim."
    },
    {
        "id": "sec_separation_techniques",
        "title": "1. Các Kỹ thuật Tách chất trong Phòng Thí nghiệm (Separation Techniques Overview)",
        "selector": "#sec-separation-techniques",
        "en": "Section 1 details physical purification methods: Filtration separates insoluble solids from liquids, crystallisation isolates soluble solutes, distillation separates liquid mixtures by boiling points, and chromatography separates dissolved mixtures.",
        "vi": "Mục một chi tiết hóa các phương pháp tách chất vật lý: Phương pháp lọc tách chất rắn không tan khỏi chất lỏng, kết tinh thu hồi chất tan, chưng cất tách các chất lỏng dựa trên nhiệt độ sôi, và sắc ký tách các hỗn hợp chất tan."
    },
    {
        "id": "sec_filtration_crystallisation",
        "title": "⚗️ Filtration, Distillation & Crystallisation (Các Phương pháp Tách chất)",
        "selector": "#sec-filtration-crystallisation",
        "en": "Simple distillation separates a pure liquid solvent from a solution with large boiling point difference. Fractional distillation separates miscible liquids with close boiling points using a fractionating column filled with glass beads.",
        "vi": "Chưng cất đơn tách dung môi lỏng tinh khiết khỏi dung dịch dựa trên độ chênh lệch nhiệt độ sôi lớn. Chưng cất phân đoạn dùng cột cất phân đoạn chứa các hạt thủy tinh để tách các chất lỏng hòa tan vào nhau có nhiệt độ sôi gần sát nhau."
    },
    {
        "id": "sec_chromatography_rf",
        "title": "📝 Paper Chromatography & Rf Value (Sắc ký Giấy & Chỉ số Rf)",
        "selector": "#sec-chromatography-rf",
        "en": "In paper chromatography, the baseline must be drawn in pencil because ink contains dyes that would dissolve and interfere. The solvent level must sit below the baseline. Rf value equals distance travelled by substance divided by distance travelled by solvent front.",
        "vi": "Trong sắc ký giấy, vạch xuất phát bắt buộc phải kẻ bằng bút chì vì mực bút bi chứa phẩm nhuộm sẽ tan vào dung môi làm loang mẫu. Mực dung môi phải nằm dưới vạch xuất phát. Giá trị Rf bằng khoảng cách di chuyển của chất chia cho khoảng cách di chuyển của mức dung môi."
    },
    {
        "id": "sec_gas_identification",
        "title": "2. Phương pháp Nhận biết các Chất Khí (Identification of Gases Overview)",
        "selector": "#sec-gas-identification",
        "en": "Section 2 provides standard Cambridge qualitative tests for identifying five essential laboratory gases: hydrogen, oxygen, carbon dioxide, chlorine, and ammonia.",
        "vi": "Mục hai cung cấp các phản ứng thử định tính chuẩn mực để nhận biết năm chất khí phòng thí nghiệm: hydro, oxy, carbon dioxide, clo và amoniac."
    },
    {
        "id": "sec_gas_tests",
        "title": "💨 5 Gas Tests: H₂, O₂, CO₂, Cl₂, NH₃ (Nhận biết 5 Chất Khí)",
        "selector": "#sec-gas-tests",
        "en": "Hydrogen pops with a lighted splint. Oxygen relights a glowing splint. Carbon dioxide turns limewater milky cloudy. Chlorine bleaches damp blue litmus paper white. Ammonia turns damp red litmus paper blue.",
        "vi": "Khí hydro làm nổ que đóm cháy tạo tiếng pop. Khí oxy làm que đóm tàn đỏ bùng cháy trở lại. Khí carbon dioxide làm vẩn đục nước vôi trong. Khí clo làm mất màu quỳ tím ẩm (tẩy trắng). Khí amoniac có tính kiềm làm quỳ tím ẩm hóa xanh."
    },
    {
        "id": "sec_ion_identification",
        "title": "3. Nhận biết Cation & Anion (Identification of Ions Overview)",
        "selector": "#sec-ion-identification",
        "en": "Section 3 covers chemical identification of cations using aqueous sodium hydroxide and ammonia, and anions using precipitation reagents.",
        "vi": "Mục ba hướng dẫn cách nhận biết các ion kim loại cation bằng dung dịch kiềm NaOH và amoniac, cùng nhận biết các ion phi kim anion bằng phản ứng kết tủa."
    },
    {
        "id": "sec_cation_tests",
        "title": "➕ Cation Testing: Cu²⁺, Fe²⁺, Fe³⁺, NH₄⁺ (Nhận biết Ion Kim loại)",
        "selector": "#sec-cation-tests",
        "en": "With aqueous NaOH: Copper(II) gives a light blue precipitate insoluble in excess. Iron(II) gives a green precipitate turning red-brown. Iron(III) gives a red-brown precipitate. Ammonium produces ammonia gas upon gentle warming, turning damp red litmus blue.",
        "vi": "Với dung dịch NaOH: Ion Đồng 2+ tạo kết tủa xanh lam không tan trong kiềm dư. Ion Sắt 2+ tạo kết tủa xanh rêu hóa nâu đỏ ngoài không khí. Ion Sắt 3+ tạo kết tủa nâu đỏ. Ion Amoni khi đun nóng nhẹ giải phóng khí amoniac làm xanh giấy quỳ tím ẩm."
    },
    {
        "id": "sec_anion_tests",
        "title": "➖ Anion Testing: CO₃²⁻, Cl⁻, Br⁻, NO₃⁻, SO₄²⁻ (Nhận biết Anion)",
        "selector": "#sec-anion-tests",
        "en": "Anion tests: Carbonate reacts with dilute acid producing CO2 bubbles. Halides with nitric acid and silver nitrate produce precipitates: chloride gives white AgCl, bromide gives cream AgBr. Sulfate with nitric acid and barium nitrate gives a white precipitate of BaSO4. Nitrate warmed with NaOH and aluminium foil releases ammonia gas.",
        "vi": "Nhận biết anion: Cacbonat tác dụng axit sủi bọt khí CO2. Halide tác dụng bạc nitrat tạo kết tủa: clorua cho kết tủa trắng AgCl, bromua cho kết tủa vàng nhạt AgBr. Sunfat tác dụng bari nitrat cho kết tủa trắng BaSO4 không tan trong axit. Nitrat đun với NaOH và vụn nhôm giải phóng khí amoniac."
    }
]

C12_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C12", "selector": "#sec-header"},
    "sec_separation_techniques": {"start": 1, "end": 3, "title": "1. Các Kỹ thuật Tách chất", "selector": "#sec-separation-techniques"},
    "sec_gas_identification": {"start": 4, "end": 5, "title": "2. Nhận biết các Chất Khí", "selector": "#sec-gas-identification"},
    "sec_ion_identification": {"start": 6, "end": 8, "title": "3. Nhận biết Cation & Anion", "selector": "#sec-ion-identification"}
}


# =====================================================================
# BATCH 3 AUDIO GENERATION PIPELINE
# =====================================================================
BATCH3_LECTURES = [
    ("c9", "d34bbfa2-7449-4192-b471-3a6a8ba49257", "C9: Metals", C9_SEGMENTS, C9_MAJOR_SECTIONS),
    ("c10", "9d61f516-a24c-4485-8490-8485604130ec", "C10: Chemistry of the environment", C10_SEGMENTS, C10_MAJOR_SECTIONS),
    ("c11", "69b82c81-05a0-40a8-816f-c21a882cef54", "C11: Organic chemistry", C11_SEGMENTS, C11_MAJOR_SECTIONS),
    ("c12", "d51b5192-ff57-48a0-bcd9-d4f8a7d10757", "C12: Experimental techniques and Chemical analysis", C12_SEGMENTS, C12_MAJOR_SECTIONS),
]

async def main():
    print("=====================================================================")
    print("STARTING AUDIO GENERATION FOR CHEMISTRY BATCH 3 (C9, C10, C11, C12)")
    print("=====================================================================")
    
    for code, lec_id, title, segments, majors in BATCH3_LECTURES:
        print(f"\n>>> Processing {code.upper()}: {title} ({len(segments)} segments)...")
        await process_lecture_audio(
            lecture_code=code,
            lecture_id=lec_id,
            course_title=COURSE_TITLE,
            lecture_title=title,
            segments=segments,
            major_sections=majors,
            subject='science'
        )
        print(f">>> Finished {code.upper()}!")

    print("\n🎉 ALL BATCH 3 (C9-C12) AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
