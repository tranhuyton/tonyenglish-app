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
# C5: CHEMICAL ENERGETICS
# =====================================================================
C5_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C5: Nhiệt Hóa học & Năng lượng Liên kết",
        "selector": "#sec-header",
        "en": "Welcome to Topic C5: Chemical Energetics. Chemical reactions involve energy transfers between the reacting system and surroundings. In this topic, we investigate exothermic and endothermic reactions, interpret reaction energy profiles and activation energy, and calculate overall enthalpy changes from bond energies.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C5: Nhiệt Hóa học và Năng lượng Liên kết. Phản ứng hóa học luôn đi kèm sự truyền năng lượng giữa hệ phản ứng và môi trường xung quanh. Trong bài học này, chúng ta sẽ khảo sát phản ứng tỏa nhiệt và thu nhiệt, đọc hiểu giản đồ năng lượng phản ứng cùng năng lượng hoạt hóa, và tính toán biến thiên enthalpy từ năng lượng liên kết."
    },
    {
        "id": "sec_exo_endo",
        "title": "1. Phản ứng Tỏa nhiệt & Thu nhiệt (Exothermic vs Endothermic Overview)",
        "selector": "#sec-exo-endo",
        "en": "Section 1 compares Exothermic and Endothermic reactions: In an exothermic reaction, thermal energy is transferred to the surroundings, causing temperature to rise. In an endothermic reaction, thermal energy is absorbed from the surroundings, causing temperature to fall.",
        "vi": "Mục một so sánh Phản ứng Tỏa nhiệt và Thu nhiệt: Trong phản ứng tỏa nhiệt, nhiệt năng được giải phóng ra môi trường làm nhiệt độ xung quanh tăng lên. Trong phản ứng thu nhiệt, nhiệt năng bị hấp thụ từ môi trường khiến nhiệt độ xung quanh hạ xuống."
    },
    {
        "id": "sec_exothermic",
        "title": "🔥 Exothermic Reactions (Phản ứng Tỏa nhiệt)",
        "selector": "#sec-exothermic",
        "en": "Exothermic reactions have negative enthalpy change Delta H. Products have lower chemical energy than reactants because energy is released as heat. Examples include combustion of fuels, neutralisation, and respiration.",
        "vi": "Phản ứng tỏa nhiệt có biến thiên enthalpy Delta H mang giá trị âm. Các chất sản phẩm có năng lượng hóa học thấp hơn chất phản ứng vì năng lượng đã giải phóng ra ngoài dưới dạng nhiệt. Ví dụ gồm sự đốt cháy nhiên liệu, phản ứng trung hòa axit-bazơ và quá trình hô hấp."
    },
    {
        "id": "sec_endothermic",
        "title": "❄️ Endothermic Reactions (Phản ứng Thu nhiệt)",
        "selector": "#sec-endothermic",
        "en": "Endothermic reactions have positive enthalpy change Delta H. Products have higher chemical energy than reactants. Examples include photosynthesis, thermal decomposition of calcium carbonate, and sherbet reactions.",
        "vi": "Phản ứng thu nhiệt có biến thiên enthalpy Delta H mang giá trị dương. Các chất sản phẩm có mức năng lượng hóa học cao hơn chất ban đầu. Các ví dụ điển hình bao gồm quá trình quang hợp, phản ứng nhiệt phân đá vôi canxi cacbonat và phản ứng tạo bọt sủi."
    },
    {
        "id": "sec_reaction_profiles",
        "title": "2. Giản đồ Năng lượng Phản ứng (Reaction Energy Profiles Overview)",
        "selector": "#sec-reaction-profiles",
        "en": "Section 2 illustrates Reaction Profiles: showing the relative enthalpy levels of reactants and products against progress of reaction.",
        "vi": "Mục hai minh họa Giản đồ Năng lượng Phản ứng: thể hiện mức enthalpy tương đối của các chất phản ứng và sản phẩm theo tiến trình phản ứng."
    },
    {
        "id": "sec_energy_profiles",
        "title": "📈 Energy Profiles & Activation Energy (Giản đồ Năng lượng & Ea)",
        "selector": "#sec-energy-profiles",
        "en": "Activation energy Ea is the minimum energy that colliding particles must possess to react, shown as an arrow from reactant energy level to the peak of the curve. Enthalpy change Delta H is the vertical distance between reactants and products.",
        "vi": "Năng lượng hoạt hóa Ea là năng lượng tối thiểu mà các hạt va chạm phải có để phản ứng xảy ra, biểu diễn bằng mũi tên từ mức năng lượng chất phản ứng lên đến đỉnh đường cong. Biến thiên enthalpy Delta H là khoảng cách thẳng đứng giữa mức năng lượng chất phản ứng và chất sản phẩm."
    },
    {
        "id": "sec_bond_energies",
        "title": "3. Năng lượng Liên kết & Tính toán Enthalpy (Bond Energies Overview)",
        "selector": "#sec-bond-energies",
        "en": "Section 3 explains chemical bond energetics: Chemical reactions proceed by breaking reactant bonds and forming new product bonds.",
        "vi": "Mục ba giải thích năng lượng liên kết hóa học: Phản ứng hóa học diễn ra qua hai giai đoạn bẻ gãy liên kết ở chất phản ứng và hình thành các liên kết mới ở chất sản phẩm."
    },
    {
        "id": "sec_mex_bendo",
        "title": "🧠 Rule: BENDO - MEX (Bẻ gãy Thu nhiệt - Tạo thành Tỏa nhiệt)",
        "selector": "#sec-mex-bendo",
        "en": "Remember the IGCSE rule BENDO - MEX: Breaking bonds is Endothermic, requiring energy input. Making bonds is Exothermic, releasing energy output.",
        "vi": "Mẹo nhớ kinh điển BENDO - MEX: Bẻ gãy liên kết là quá trình Thu nhiệt (BENDO - Breaking is Endothermic) cần cung cấp năng lượng. Tạo thành liên kết mới là quá trình Tỏa nhiệt (MEX - Making is Exothermic) giải phóng năng lượng ra ngoài."
    },
    {
        "id": "sec_calc_enthalpy",
        "title": "🧮 Calculating Overall Enthalpy Change (Tính toán ΔH)",
        "selector": "#sec-calc-enthalpy",
        "en": "Overall enthalpy change Delta H equals the sum of energy required to break all reactant bonds minus the sum of energy released when all product bonds form. If bond making releases more energy than bond breaking requires, the reaction is exothermic.",
        "vi": "Biến thiên enthalpy tổng thể Delta H bằng tổng năng lượng cần để phá vỡ các liên kết ban đầu trừ đi tổng năng lượng giải phóng khi hình thành các liên kết mới. Nếu năng lượng tỏa ra khi tạo liên kết lớn hơn năng lượng cần để bẻ gãy liên kết, phản ứng là tỏa nhiệt."
    }
]

C5_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C5", "selector": "#sec-header"},
    "sec_exo_endo": {"start": 1, "end": 3, "title": "1. Phản ứng Tỏa nhiệt & Thu nhiệt", "selector": "#sec-exo-endo"},
    "sec_reaction_profiles": {"start": 4, "end": 5, "title": "2. Giản đồ Năng lượng & Ea", "selector": "#sec-reaction-profiles"},
    "sec_bond_energies": {"start": 6, "end": 8, "title": "3. Năng lượng Liên kết & Tính ΔH", "selector": "#sec-bond-energies"}
}


# =====================================================================
# C6: CHEMICAL REACTIONS
# =====================================================================
C6_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C6: Tốc độ Phản ứng, Cân bằng & Oxy hóa Khử",
        "selector": "#sec-header",
        "en": "Welcome to Topic C6: Chemical Reactions. In this topic, we differentiate physical and chemical changes, investigate rates of reaction using collision theory, explore reversible reactions and dynamic equilibrium in the Haber process, and examine redox processes and tests.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C6: Các phản ứng hóa học. Trong bài học này, chúng ta sẽ phân biệt biến đổi vật lý và hóa học, khảo sát tốc độ phản ứng bằng thuyết va chạm hạt, tìm hiểu phản ứng thuận nghịch và cân bằng động trong quy trình Haber, cùng bản chất và thuốc thử phản ứng oxy hóa - khử."
    },
    {
        "id": "sec_physical_chemical",
        "title": "1. Biến đổi Vật lý vs Biến đổi Hóa học (Physical vs Chemical Changes Overview)",
        "selector": "#sec-physical-chemical",
        "en": "Section 1 contrasts physical changes with chemical reactions: Physical changes are easily reversible and form no new substances. Chemical reactions form new substances with different properties and are difficult to reverse.",
        "vi": "Mục một đối chiếu biến đổi vật lý và biến đổi hóa học: Biến đổi vật lý dễ đảo ngược và không tạo ra chất mới. Biến đổi hóa học hình thành nên các chất mới có tính chất hoàn toàn khác và rất khó đảo ngược."
    },
    {
        "id": "sec_phys_chem_diff",
        "title": "🧪 Physical vs Chemical Differences (So sánh Bản chất)",
        "selector": "#sec-phys-chem-diff",
        "en": "In physical changes such as melting ice, particles change only arrangement and energy. In chemical reactions such as combustion or rusting, chemical bonds are broken and rearranged into entirely new chemical compounds.",
        "vi": "Trong biến đổi vật lý như băng tan, các hạt chỉ thay đổi cách sắp xếp và năng lượng mà không đổi bản chất. Trong phản ứng hóa học như sự cháy hay rỉ sét, các liên kết hóa học bị bẻ gãy và sắp xếp lại tạo thành các hợp chất hoàn toàn mới."
    },
    {
        "id": "sec_chem_observations",
        "title": "🔍 4 Observations of Chemical Reaction (4 Dấu hiệu Phản ứng)",
        "selector": "#sec-chem-observations",
        "en": "Four key experimental signs indicating a chemical reaction: permanent colour change, gas evolution with effervescence, formation of an insoluble precipitate, and significant temperature change.",
        "vi": "Bốn dấu hiệu thực nghiệm đặc trưng cho biết phản ứng hóa học xảy ra: sự thay đổi màu sắc vĩnh viễn, sự thoát khí sủi bọt, sự hình thành kết tủa không tan và sự thay đổi nhiệt độ rõ rệt."
    },
    {
        "id": "sec_rate_of_reaction",
        "title": "2. Tốc độ Phản ứng & Thuyết Va chạm (Rate of Reaction Overview)",
        "selector": "#sec-rate-of-reaction",
        "en": "Section 2 investigates Reaction Rates: Rate of reaction is the change in concentration, mass, or volume of reactants or products per unit of time.",
        "vi": "Mục hai nghiên cứu Tốc độ phản ứng: Tốc độ phản ứng là sự biến thiên nồng độ, khối lượng hoặc thể tích của chất phản ứng hoặc sản phẩm trong một đơn vị thời gian."
    },
    {
        "id": "sec_collision_theory",
        "title": "💥 Collision Theory (Thuyết Va chạm)",
        "selector": "#sec-collision-theory",
        "en": "Collision theory dictates that for particles to react, they must collide with each other with energy equal to or greater than the activation energy Ea, and in the correct orientation. Only successful collisions lead to reaction.",
        "vi": "Thuyết va chạm chỉ ra rằng để phản ứng xảy ra, các hạt phải va chạm với nhau với năng lượng bằng hoặc lớn hơn năng lượng hoạt hóa Ea và theo đúng hướng không gian. Chỉ các va chạm hiệu quả mới dẫn đến phản ứng hóa học."
    },
    {
        "id": "sec_rate_factors",
        "title": "🚀 4 Factors Affecting Rate (4 Yếu tố Tăng tốc độ Phản ứng)",
        "selector": "#sec-rate-factors",
        "en": "Four factors increase reaction rate: higher concentration or pressure increases collision frequency; higher temperature increases both collision frequency and particle kinetic energy; larger surface area increases accessible sites; and catalysts provide alternative pathways with lower activation energy.",
        "vi": "Bốn yếu tố làm tăng tốc độ phản ứng: tăng nồng độ hoặc áp suất làm tăng tần số va chạm; tăng nhiệt độ vừa làm tăng tần số va chạm vừa làm tăng động năng hạt; tăng diện tích tiếp xúc tạo thêm vị trí va chạm; và chất xúc tác mở ra con đường phản ứng mới có năng lượng hoạt hóa thấp hơn."
    },
    {
        "id": "sec_reversible_equilibrium",
        "title": "3. Phản ứng Thuận nghịch & Cân bằng Động (Reversible & Equilibrium Overview)",
        "selector": "#sec-reversible-equilibrium",
        "en": "Section 3 introduces Reversible Reactions, indicated by the double arrow symbol. In a closed system, reversible reactions can reach dynamic equilibrium.",
        "vi": "Mục ba giới thiệu Phản ứng Thuận nghịch, biểu thị bằng dấu mũi tên hai chiều. Trong một hệ kín, phản ứng thuận nghịch có thể đạt tới trạng thái cân bằng động."
    },
    {
        "id": "sec_dynamic_equilibrium",
        "title": "⚖️ Dynamic Equilibrium (Trạng thái Cân bằng Động)",
        "selector": "#sec-dynamic-equilibrium",
        "en": "At dynamic equilibrium: the rates of the forward and reverse reactions are exactly equal, and the concentrations of reactants and products remain constant.",
        "vi": "Tại trạng thái cân bằng động: tốc độ của phản ứng thuận và phản ứng nghịch hoàn toàn bằng nhau, và nồng độ của các chất phản ứng cùng chất sản phẩm được giữ không đổi theo thời gian."
    },
    {
        "id": "sec_haber_process",
        "title": "🏭 Haber Process: N₂ + 3H₂ ⇌ 2NH₃ (Quy trình Haber)",
        "selector": "#sec-haber-process",
        "en": "The Haber process synthesises ammonia: Nitrogen from air and hydrogen from natural gas react at 450 degrees Celsius, 200 atmospheres of pressure, over an iron catalyst.",
        "vi": "Quy trình Haber tổng hợp amoniac: Khí nitơ từ không khí và khí hydro từ khí tự nhiên phản ứng ở nhiệt độ 450 độ C, áp suất 200 atm trên xúc tác sắt để tạo amoniac."
    },
    {
        "id": "sec_redox_reactions",
        "title": "4. Bản chất Phản ứng Oxy hóa - Khử & Thuốc thử (Redox Reactions Overview)",
        "selector": "#sec-redox-reactions",
        "en": "Section 4 covers Redox: Oxidation is Gain of oxygen, Loss of electrons, or Increase in oxidation number. Reduction is Loss of oxygen, Gain of electrons, or Decrease in oxidation number.",
        "vi": "Mục bốn phân tích Phản ứng Oxy hóa - Khử: Quá trình oxy hóa là sự kết hợp oxy, mất electron hoặc tăng số oxy hóa. Quá trình khử là sự mất oxy, nhận electron hoặc giảm số oxy hóa."
    },
    {
        "id": "sec_redox_definitions",
        "title": "🔄 Redox Definitions: OIL RIG (Khái niệm Cốt lõi)",
        "selector": "#sec-redox-definitions",
        "en": "In terms of electrons: Oxidation Is Loss of electrons, Reduction Is Gain of electrons. An oxidising agent oxidises another substance and is itself reduced. A reducing agent reduces another substance and is itself oxidised.",
        "vi": "Theo quan điểm electron: Oxy hóa là Mất electron, Khử là Nhận electron (OIL RIG). Chất oxy hóa làm oxy hóa chất khác và bản thân nó bị khử. Chất khử làm khử chất khác và bản thân nó bị oxy hóa."
    },
    {
        "id": "sec_redox_tests",
        "title": "🧪 Tests for Oxidising & Reducing Agents (Thuốc thử Nhận biết)",
        "selector": "#sec-redox-tests",
        "en": "Chemical tests: Acidified aqueous potassium manganate(VII) is an oxidising agent that turns from purple to colourless when reduced. Aqueous potassium iodide is a reducing agent that turns from colourless to brown iodine solution when oxidised.",
        "vi": "Thuốc thử hóa học: Dung dịch thuốc tím kali pemanganat trong môi trường axit là chất oxy hóa mạnh đổi từ màu tím sang không màu khi bị khử. Dung dịch kali iotua KI là chất khử đổi từ không màu sang màu nâu của dung dịch iot khi bị oxy hóa."
    }
]

C6_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C6", "selector": "#sec-header"},
    "sec_physical_chemical": {"start": 1, "end": 3, "title": "1. Biến đổi Vật lý vs Hóa học", "selector": "#sec-physical-chemical"},
    "sec_rate_of_reaction": {"start": 4, "end": 6, "title": "2. Tốc độ Phản ứng & Va chạm", "selector": "#sec-rate-of-reaction"},
    "sec_reversible_equilibrium": {"start": 7, "end": 9, "title": "3. Cân bằng Động & Haber", "selector": "#sec-reversible-equilibrium"},
    "sec_redox_reactions": {"start": 10, "end": 12, "title": "4. Phản ứng Oxy hóa - Khử", "selector": "#sec-redox-reactions"}
}


# =====================================================================
# C7: ACIDS, BASES AND SALTS
# =====================================================================
C7_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C7: Axit, Bazơ & Phương pháp Điều chế Muối",
        "selector": "#sec-header",
        "en": "Welcome to Topic C7: Acids, Bases and Salts. In this lesson, we study the chemical characteristics of acids and alkalis, master the pH scale and indicators, analyze the three core acid reactions, and master laboratory salt preparation techniques including titration and precipitation.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C7: Axit, Bazơ và Muối. Trong bài học này, chúng ta sẽ khảo sát đặc tính hóa học của axit và kiềm, làm chủ thang đo pH và chất chỉ thị màu, phân tích ba phản ứng đặc trưng của axit, cùng các phương pháp điều chế muối trong phòng thí nghiệm như chuẩn độ và kết tủa."
    },
    {
        "id": "sec_acids_bases",
        "title": "1. Axit, Bazơ, Kiềm & Thang đo pH (Acids, Bases & pH Overview)",
        "selector": "#sec-acids-bases",
        "en": "Section 1 defines acids and bases: An acid is a proton donor producing hydrogen ions H+ in water. A base is a proton acceptor; a soluble base is called an alkali, producing hydroxide ions OH- in water.",
        "vi": "Mục một định nghĩa axit và bazơ: Axit là chất nhường proton tạo ra ion H+ trong nước. Bazơ là chất nhận proton; bazơ tan trong nước được gọi là Kiềm (Alkali), tạo ra ion OH- trong dung dịch."
    },
    {
        "id": "sec_acids_bases_def",
        "title": "🔴 Acids vs Bases vs Alkalis (Axit vs Bazơ vs Kiềm)",
        "selector": "#sec-acids-bases-def",
        "en": "Critical distinction: All alkalis are bases, but not all bases are alkalis. Common bases include copper(II) oxide and iron(III) hydroxide which are insoluble in water, whereas sodium hydroxide is an alkali.",
        "vi": "Phân biệt then chốt: Mọi chất kiềm đều là bazơ, nhưng không phải mọi bazơ đều là kiềm. Các bazơ không tan trong nước như đồng hai oxit CuO hay sắt ba hidroxit không phải là kiềm, trong khi natri hidroxit tan tốt trong nước là kiềm."
    },
    {
        "id": "sec_ph_scale",
        "title": "🌈 The pH Scale & Indicators (Thang đo pH & Chỉ thị)",
        "selector": "#sec-ph-scale",
        "en": "The pH scale ranges from 0 to 14: pH less than 7 indicates acidic solutions, pH 7 is neutral, and pH greater than 7 indicates alkaline solutions. Litmus turns red in acid and blue in alkali. Universal indicator gives a full colour spectrum from red to purple.",
        "vi": "Thang đo pH chạy từ 0 đến 14: pH nhỏ hơn 7 là môi trường axit, pH bằng 7 là trung tính, và pH lớn hơn 7 là môi trường kiềm. Quỳ tím chuyển đỏ trong axit và chuyển xanh trong kiềm. Chỉ thị vạn năng đổi màu liên tục từ đỏ qua xanh lá đến tím."
    },
    {
        "id": "sec_acid_reactions",
        "title": "2. Ba Phản ứng Đặc trưng của Axit (Characteristic Reactions of Acids Overview)",
        "selector": "#sec-acid-reactions",
        "en": "Section 2 details the three essential reactions of dilute acids in Cambridge IGCSE: reacting with metals, metal oxides and hydroxides, and metal carbonates.",
        "vi": "Mục hai chi tiết hóa ba phản ứng nền tảng của dung dịch axit loãng: tác dụng với kim loại, tác dụng với bazơ hoặc oxit bazơ, và tác dụng với muối cacbonat."
    },
    {
        "id": "sec_three_acid_reactions",
        "title": "💥 3 Acid Reactions: Metal, Base & Carbonate (3 Dạng Phản ứng)",
        "selector": "#sec-three-acid-reactions",
        "en": "Reaction 1: Acid plus Metal yields Salt plus Hydrogen gas. Reaction 2: Acid plus Base yields Salt plus Water in neutralisation. Reaction 3: Acid plus Metal Carbonate yields Salt plus Water plus Carbon Dioxide gas, turning limewater cloudy.",
        "vi": "Phản ứng 1: Axit tác dụng với Kim loại tạo Muối và khí Hydro sủi bọt. Phản ứng 2: Axit tác dụng với Bazơ tạo Muối và Nước gọi là phản ứng trung hòa. Phản ứng 3: Axit tác dụng với Muối Cacbonat tạo Muối, Nước và khí Carbon dioxide làm đục nước vôi trong."
    },
    {
        "id": "sec_salt_preparation",
        "title": "3. Kỹ thuật Điều chế Muối (Salt Preparation Methods Overview)",
        "selector": "#sec-salt-preparation",
        "en": "Section 3 covers preparation of soluble and insoluble salts in the laboratory, guided by solubility rules.",
        "vi": "Mục ba hướng dẫn các phương pháp điều chế muối tan và muối không tan trong phòng thí nghiệm dựa trên quy tắc độ tan."
    },
    {
        "id": "sec_solubility_rules",
        "title": "🧠 SNAP Solubility Rule (Quy tắc Độ tan SNAP)",
        "selector": "#sec-solubility-rules",
        "en": "Remember SNAP rule: All Sodium, Nitrate, Ammonium, and Potassium salts are completely soluble in water. All sulfates are soluble except barium, lead, and calcium. All chlorides are soluble except silver and lead.",
        "vi": "Mẹo nhớ SNAP: Tất cả các muối của Sodium, Nitrate, Ammonium và Potassium đều tan hoàn toàn trong nước. Hầu hết các muối sunfat đều tan trừ bari, chì và canxi. Hầu hết các muối clorua đều tan trừ bạc và chì."
    },
    {
        "id": "sec_salt_methods",
        "title": "🧂 3 Salt Methods: Titration, Excess Solid & Precipitation (3 Phương pháp)",
        "selector": "#sec-salt-methods",
        "en": "Method 1: Titration is used for soluble salts prepared from acid plus soluble alkali. Method 2: Excess insoluble solid added to acid, filtered, then crystallised. Method 3: Precipitation mixes two soluble solutions to produce an insoluble salt precipitate.",
        "vi": "Phương pháp 1: Chuẩn độ dùng cho muối tan tạo từ axit và kiềm tan. Phương pháp 2: Cho dư chất rắn không tan vào axit, lọc bỏ phần dư rồi kết tinh dịch lọc. Phương pháp 3: Kết tủa trộn hai dung dịch muối tan vào nhau để thu được muối kết tủa không tan."
    }
]

C7_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C7", "selector": "#sec-header"},
    "sec_acids_bases": {"start": 1, "end": 3, "title": "1. Axit, Bazơ & Thang đo pH", "selector": "#sec-acids-bases"},
    "sec_acid_reactions": {"start": 4, "end": 5, "title": "2. Ba Phản ứng Đặc trưng của Axit", "selector": "#sec-acid-reactions"},
    "sec_salt_preparation": {"start": 6, "end": 8, "title": "3. Kỹ thuật Điều chế Muối", "selector": "#sec-salt-preparation"}
}


# =====================================================================
# C8: THE PERIODIC TABLE
# =====================================================================
C8_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C8: Bảng Tuần hoàn các Nguyên tố Hóa học",
        "selector": "#sec-header",
        "en": "Welcome to Topic C8: The Periodic Table. The periodic table is a master map of chemical elements organized by atomic structure. In this lesson, we study periods and groups, contrast Group 1 alkali metals with Group 7 halogens, and investigate transition elements and noble gases.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C8: Bảng Tuần hoàn các Nguyên tố Hóa học. Bảng tuần hoàn là bản đồ nguyên tố sắp xếp theo cấu tạo nguyên tử. Trong bài học này, chúng ta sẽ tìm hiểu chu kỳ và nhóm, so sánh kim loại kiềm Nhóm 1 và halogen Nhóm 7, cùng các kim loại chuyển tiếp và khí hiếm."
    },
    {
        "id": "sec_arrangement_elements",
        "title": "1. Cấu trúc Bảng Tuần hoàn: Chu kỳ & Phân nhóm (Arrangement Overview)",
        "selector": "#sec-arrangement-elements",
        "en": "Section 1 explains table layout: Elements are arranged in order of increasing proton number. Horizontal rows are Periods, and vertical columns are Groups.",
        "vi": "Mục một giải thích cách bố trí bảng tuần hoàn: Các nguyên tố sắp xếp theo thứ tự số proton tăng dần. Các hàng ngang là Chu kỳ, và các cột dọc là Nhóm."
    },
    {
        "id": "sec_periods_groups",
        "title": "🗺️ Periods & Groups (Chu kỳ & Phân nhóm)",
        "selector": "#sec-periods-groups",
        "en": "The period number indicates the number of occupied electron shells. The group number indicates the number of valence electrons in the outer energy shell, explaining why elements in the same group share similar chemical properties.",
        "vi": "Số thứ tự chu kỳ cho biết số lớp electron của nguyên tử. Số thứ tự của nhóm cho biết số electron ở lớp vỏ ngoài cùng, giải thích vì sao các nguyên tố trong cùng một nhóm lại có tính chất hóa học rất tương đồng nhau."
    },
    {
        "id": "sec_group_trends",
        "title": "2. Kim loại Kiềm Nhóm I vs Halogen Nhóm VII (Group Trends Overview)",
        "selector": "#sec-group-trends",
        "en": "Section 2 contrasts Group 1 alkali metals and Group 7 halogens, demonstrating opposite reactivity trends down each group.",
        "vi": "Mục hai đối chiếu kim loại kiềm Nhóm 1 và halogen Nhóm 7, làm rõ quy luật biến đổi độ hoạt động hóa học ngược chiều nhau khi đi từ trên xuống dưới trong nhóm."
    },
    {
        "id": "sec_group1_metals",
        "title": "🔵 Group I: Alkali Metals (Kim loại Kiềm)",
        "selector": "#sec-group1-metals",
        "en": "Group 1 metals are soft, have low densities, and low melting points. Reactivity increases down the group from lithium to potassium and caesium as the single outer electron is further from the nucleus and more easily lost.",
        "vi": "Kim loại Nhóm 1 rất mềm, khối lượng riêng thấp và nhiệt độ nóng chảy thấp. Độ hoạt động hóa học tăng dần từ trên xuống dưới từ liti đến kali và xesi do electron lớp ngoài cùng càng xa hạt nhân nên càng dễ bị mất đi."
    },
    {
        "id": "sec_group7_halogens",
        "title": "🟣 Group VII: Halogens (Phi kim Halogen)",
        "selector": "#sec-group7-halogens",
        "en": "Group 7 halogens exist as diatomic molecules. Going down the group, colours darken from yellow fluorine to black solid iodine, and melting points increase. Reactivity decreases down the group because incoming electrons are attracted less strongly by the nucleus.",
        "vi": "Halogen Nhóm 7 tồn tại dưới dạng phân tử hai nguyên tử. Đi từ trên xuống, màu sắc đậm dần từ flo vàng đến iot đen và nhiệt độ nóng chảy tăng lên. Tuy nhiên, độ hoạt động hóa học lại giảm dần do lực hút electron của hạt nhân yếu đi."
    },
    {
        "id": "sec_transition_noblegases",
        "title": "3. Kim loại Chuyển tiếp & Khí hiếm (Transition & Noble Gases Overview)",
        "selector": "#sec-transition-noblegases",
        "en": "Section 3 examines transition metals in the central block and noble gases in Group 8 or zero.",
        "vi": "Mục ba khảo sát các kim loại chuyển tiếp ở khối trung tâm và các khí hiếm ở Nhóm 8 hoặc nhóm 0."
    },
    {
        "id": "sec_transition_elements",
        "title": "🛡️ Transition Elements (Kim loại Chuyển tiếp)",
        "selector": "#sec-transition-elements",
        "en": "Transition elements are hard, dense metals with high melting points. They form colored compounds, exhibit variable oxidation states, and act as valuable industrial catalysts.",
        "vi": "Kim loại chuyển tiếp là các kim loại cứng, khối lượng riêng lớn và có nhiệt độ nóng chảy cao. Chúng tạo ra các hợp chất có màu sắc rực rỡ, có nhiều trạng thái oxy hóa khác nhau và thường đóng vai trò làm chất xúc tác công nghiệp quan trọng."
    },
    {
        "id": "sec_noble_gases",
        "title": "🎈 Group VIII / 0: Noble Gases (Khí Hiếm)",
        "selector": "#sec-noble-gases",
        "en": "Noble gases are monatomic unreactive gases with complete outer electron shells, used in advertising signs and inert atmospheric shielding.",
        "vi": "Khí hiếm là các khí đơn nguyên tử trơ về mặt hóa học do có lớp vỏ electron ngoài cùng bão hòa bền vững, được ứng dụng làm đèn quảng cáo neon và tạo môi trường khí bảo vệ trơ."
    }
]

C8_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C8", "selector": "#sec-header"},
    "sec_arrangement_elements": {"start": 1, "end": 2, "title": "1. Chu kỳ & Phân nhóm", "selector": "#sec-arrangement-elements"},
    "sec_group_trends": {"start": 3, "end": 5, "title": "2. Kim loại Kiềm vs Halogen", "selector": "#sec-group-trends"},
    "sec_transition_noblegases": {"start": 6, "end": 8, "title": "3. Kim loại Chuyển tiếp & Khí hiếm", "selector": "#sec-transition-noblegases"}
}


# =====================================================================
# BATCH 2 AUDIO GENERATION PIPELINE
# =====================================================================
BATCH2_LECTURES = [
    ("c5", "71545c83-4d45-4201-978c-aa58d01b57e5", "C5: Chemical energetics", C5_SEGMENTS, C5_MAJOR_SECTIONS),
    ("c6", "7f2b44b2-ba70-4cfc-85b3-3a0709058b46", "C6: Chemical reactions", C6_SEGMENTS, C6_MAJOR_SECTIONS),
    ("c7", "2c83104c-9413-4ee1-bdf3-2c0da8fd96a6", "C7: Acids bases and salts", C7_SEGMENTS, C7_MAJOR_SECTIONS),
    ("c8", "856f20da-80e8-4c6a-9cd1-dbe8a1f40828", "C8: Periodic table", C8_SEGMENTS, C8_MAJOR_SECTIONS),
]

async def main():
    print("=====================================================================")
    print("STARTING AUDIO GENERATION FOR CHEMISTRY BATCH 2 (C5, C6, C7, C8)")
    print("=====================================================================")
    
    for code, lec_id, title, segments, majors in BATCH2_LECTURES:
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

    print("\n🎉 ALL BATCH 2 (C5-C8) AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
