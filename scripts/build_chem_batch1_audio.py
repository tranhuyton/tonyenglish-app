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
# C1: STATES OF MATTER
# =====================================================================
C1_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C1: Các Trạng thái của Vật chất & Thuyết Động học",
        "selector": "#sec-header",
        "en": "Welcome to Topic C1: States of Matter. Matter exists in three physical states: solid, liquid, and gas. In this topic, we explore the kinetic particle theory, examine state changes and heating curves, understand gas volume behaviors under changing temperature and pressure, and investigate molecular diffusion and the effect of relative molecular mass.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C1: Các trạng thái của vật chất. Vật chất tồn tại ở ba thể: rắn, lỏng và khí. Trong bài học này, chúng ta sẽ khám phá thuyết động học phân tử, đồ thị gia nhiệt, sự biến đổi thể tích chất khí theo nhiệt độ và áp suất, cùng hiện tượng khuếch tán và ảnh hưởng của khối lượng phân tử tương đối."
    },
    {
        "id": "sec_states_particles",
        "title": "1. Ba Trạng thái của Vật chất & Thuyết Động học Hạt (States & Particle Theory)",
        "selector": "#sec-states-particles",
        "en": "Section 1 presents the Kinetic Particle Theory: all matter is composed of tiny moving particles. The physical state of any substance is governed by particle arrangement, separation, and the forces of attraction between them.",
        "vi": "Mục một trình bày Thuyết Động học Hạt: mọi vật chất đều cấu tạo từ các hạt chuyển động không ngừng. Trạng thái vật lý của chất được quyết định bởi cách sắp xếp hạt, khoảng cách giữa các hạt và lực hút tương tác giữa chúng."
    },
    {
        "id": "sec_solid",
        "title": "🧊 Solid (Chất rắn)",
        "selector": "#sec-solid",
        "en": "In a solid, particles are tightly packed in a regular repeating lattice. They vibrate only about fixed positions and are held by very strong attractive forces, giving solids a fixed shape, fixed volume, high density, and incompressibility.",
        "vi": "Trong chất rắn, các hạt được sắp xếp khít chặt trong một mạng tinh thể tuần hoàn. Chúng chỉ dao động quanh vị trí cân bằng cố định và được giữ bởi lực hút rất mạnh, giúp chất rắn có hình dạng và thể tích cố định, khối lượng riêng cao và không thể nén được."
    },
    {
        "id": "sec_liquid",
        "title": "💧 Liquid (Chất lỏng)",
        "selector": "#sec-liquid",
        "en": "In a liquid, particles are closely packed but arranged randomly without a regular pattern. They can slide and roll past one another freely. Held by moderate forces, liquids have a fixed volume, adapt to the container shape, and are virtually incompressible.",
        "vi": "Trong chất lỏng, các hạt ở sát nhau nhưng sắp xếp hỗn loạn, không có trật tự cố định. Chúng có thể trượt và lăn qua nhau tự do. Lực liên kết vừa phải giúp chất lỏng có thể tích cố định, chảy theo hình dạng bình chứa và hầu như không thể bị nén."
    },
    {
        "id": "sec_gas",
        "title": "💨 Gas (Chất khí)",
        "selector": "#sec-gas",
        "en": "In a gas, particles are separated by large empty spaces in a completely random arrangement. They move rapidly in all directions with negligible attractive forces, having no fixed shape or volume, low density, and being easily compressed.",
        "vi": "Trong chất khí, các hạt cách nhau bởi những khoảng trống rất lớn và phân bố hoàn toàn hỗn loạn. Chúng chuyển động hỗn loạn với tốc độ rất cao theo mọi hướng với lực hút không đáng kể, không có hình dạng hay thể tích cố định, khối lượng riêng thấp và rất dễ bị nén."
    },
    {
        "id": "sec_heating_curves",
        "title": "2. Sự Chuyển pha & Đồ thị Gia nhiệt (Changes of State & Heating Curves)",
        "selector": "#sec-heating-curves",
        "en": "Section 2 examines Changes of State: physical processes where substances absorb or release thermal energy without altering chemical identity. Melting, boiling, evaporating, condensing, freezing, and sublimation are key phase changes.",
        "vi": "Mục hai khảo sát Sự Chuyển pha: là các quá trình biến đổi vật lý mà chất hấp thụ hoặc giải phóng nhiệt năng mà không làm thay đổi bản chất hóa học. Nóng chảy, sôi, bay hơi, ngưng tụ, đông đặc và thăng hoa là các chuyển pha cốt lõi."
    },
    {
        "id": "sec_boiling_evap",
        "title": "⚠️ Boiling vs. Evaporation (Sôi vs Bay hơi)",
        "selector": "#sec-boiling-evap",
        "en": "Crucial exam distinction: Boiling occurs at a precise, fixed boiling point throughout the entire liquid with bubble formation. Evaporation occurs at any temperature below the boiling point, taking place strictly at the liquid surface, leaving behind cooler liquid.",
        "vi": "Bẫy đề thi quan trọng: Sự sôi diễn ra ở nhiệt độ sôi xác định trong toàn bộ khối chất lỏng với các bọt khí nổi lên. Ngược lại, sự bay hơi diễn ra ở bất kỳ nhiệt độ nào dưới nhiệt độ sôi và chỉ xảy ra duy nhất trên bề mặt thoáng, khiến phần chất lỏng còn lại bị giảm nhiệt độ."
    },
    {
        "id": "sec_heating_plateau",
        "title": "📈 Heating Curves & Temperature Plateaus (Đồ thị Gia nhiệt)",
        "selector": "#sec-heating-plateau",
        "en": "During melting and boiling, the heating curve displays horizontal flat plateaus where temperature remains constant. The thermal energy supplied is used to overcome intermolecular attractive forces rather than increasing particle kinetic energy.",
        "vi": "Trong quá trình nóng chảy và sôi, đường gia nhiệt xuất hiện các đoạn nằm ngang nơi nhiệt độ không hề tăng. Lượng nhiệt cung cấp lúc này được sử dụng hoàn toàn để phá vỡ lực hút giữa các hạt phân tử thay vì làm tăng động năng của chúng."
    },
    {
        "id": "sec_gas_behavior",
        "title": "3. Ảnh hưởng của Nhiệt độ & Áp suất lên Thể tích Khí (Gas Behavior)",
        "selector": "#sec-gas-behavior",
        "en": "Section 3 explains gas laws: Gas volume changes predictably when temperature or external pressure is varied.",
        "vi": "Mục ba giải thích các định luật chất khí: Thể tích chất khí thay đổi theo quy luật rõ ràng khi ta thay đổi nhiệt độ hoặc áp suất bên ngoài."
    },
    {
        "id": "sec_gas_temp",
        "title": "🌡️ Effect of Temperature (Ảnh hưởng của Nhiệt độ)",
        "selector": "#sec-gas-temp",
        "en": "When temperature increases, gas particles gain kinetic energy, moving faster and colliding with walls more frequently and forcefully. To maintain constant pressure, the gas expands: Volume is directly proportional to absolute Temperature.",
        "vi": "Khi nhiệt độ tăng, các hạt khí nhận thêm động năng, chuyển động nhanh hơn và va đập vào thành bình thường xuyên hơn với lực mạnh hơn. Để áp suất không đổi, chất khí phải nở ra: Thể tích tỷ lệ thuận với nhiệt độ tuyệt đối."
    },
    {
        "id": "sec_gas_pressure",
        "title": "🗜️ Effect of Pressure (Ảnh hưởng của Áp suất)",
        "selector": "#sec-gas-pressure",
        "en": "When pressure on a gas increases at constant temperature, particles are forced closer together, decreasing the empty spaces between them. Consequently, gas volume is inversely proportional to pressure.",
        "vi": "Khi tăng áp suất lên chất khí ở nhiệt độ không đổi, các hạt bị ép lại gần nhau hơn, làm giảm khoảng trống giữa các hạt. Do đó, thể tích chất khí tỷ lệ nghịch với áp suất tác dụng."
    },
    {
        "id": "sec_diffusion_mass",
        "title": "4. Hiện tượng Khuếch tán & Ảnh hưởng của Khối lượng Phân tử (Diffusion & Mr)",
        "selector": "#sec-diffusion-mass",
        "en": "Section 4 covers Diffusion: the net movement of particles from a region of higher concentration to lower concentration down a concentration gradient by random movement.",
        "vi": "Mục bốn phân tích Hiện tượng Khuếch tán: là sự chuyển động tịnh của các hạt từ nơi có nồng độ cao đến nơi có nồng độ thấp hơn xuôi theo gradient nồng độ do chuyển động nhiệt hỗn loạn."
    },
    {
        "id": "sec_diff_factors",
        "title": "⚡ Factors Affecting Diffusion (Các yếu tố ảnh hưởng)",
        "selector": "#sec-diff-factors",
        "en": "Higher temperature increases particle kinetic energy and accelerates diffusion. Steeper concentration gradient also raises diffusion rate.",
        "vi": "Nhiệt độ càng cao thì động năng hạt càng lớn, giúp khuếch tán diễn ra càng nhanh. Độ chênh lệch nồng độ càng lớn thì tốc độ khuếch tán tịnh cũng càng tăng."
    },
    {
        "id": "sec_diff_mr",
        "title": "🔬 NH₃ vs HCl Diffusion Tube Experiment (Thí nghiệm Ống Khuếch tán)",
        "selector": "#sec-diff-mr",
        "en": "In the glass tube experiment, ammonia gas with relative molecular mass 17 travels faster than hydrogen chloride gas with molecular mass 36.5. Consequently, they meet and react to form a white ring of solid ammonium chloride closer to the HCl end.",
        "vi": "Trong thí nghiệm ống thủy tinh, khí amoniac có khối lượng phân tử 17 nhẹ hơn nên khuếch tán nhanh hơn khí hiđro clorua có khối lượng 36.5. Kết quả là chúng gặp nhau và tạo thành vòng khói trắng amoni clorua ở vị trí gần đầu ống chứa HCl hơn."
    }
]

C1_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C1", "selector": "#sec-header"},
    "sec_states_particles": {"start": 1, "end": 4, "title": "1. Ba Trạng thái & Thuyết Động học Hạt", "selector": "#sec-states-particles"},
    "sec_heating_curves": {"start": 5, "end": 7, "title": "2. Sự Chuyển pha & Đồ thị Gia nhiệt", "selector": "#sec-heating-curves"},
    "sec_gas_behavior": {"start": 8, "end": 10, "title": "3. Nhiệt độ & Áp suất Khí", "selector": "#sec-gas-behavior"},
    "sec_diffusion_mass": {"start": 11, "end": 13, "title": "4. Khuếch tán & Khối lượng Phân tử", "selector": "#sec-diffusion-mass"}
}


# =====================================================================
# C2: ATOMS, ELEMENTS AND COMPOUNDS
# =====================================================================
C2_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C2: Nguyên tử, Nguyên tố & Hợp chất",
        "selector": "#sec-header",
        "en": "Welcome to Topic C2: Atoms, elements and compounds. Matter is constructed from atomic building blocks. In this comprehensive lesson, we decode subatomic particles and isotopes, explore the periodic table, distinguish elements, compounds, and mixtures, examine ionic and covalent bonding, and analyze giant covalent lattices and metallic structures.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C2: Nguyên tử, Nguyên tố và Hợp chất. Vật chất được cấu tạo từ các nguyên tử. Trong bài học này, chúng ta sẽ khảo sát hạt hạ nguyên tử và đồng vị, bảng tuần hoàn, phân biệt đơn chất, hợp chất và hỗn hợp, làm chủ liên kết ion và cộng hóa trị, cùng cấu trúc mạng tinh thể khổng lồ và kim loại."
    },
    {
        "id": "sec_periodic_table",
        "title": "🌐 IGCSE Periodic Table Hub (Bảng tuần hoàn 20 Nguyên tố)",
        "selector": "#sec-periodic-table",
        "en": "The Periodic Table arranges elements by increasing proton number. For Cambridge IGCSE, mastering the first 20 elements from Hydrogen to Calcium is essential, including their electron configurations and group properties.",
        "vi": "Bảng tuần hoàn sắp xếp các nguyên tố theo số proton tăng dần. Với chương trình IGCSE, nắm vững 20 nguyên tố đầu tiên từ Hydrogen đến Calcium là bắt buộc, bao gồm cấu hình electron và tính chất của các nhóm."
    },
    {
        "id": "sec_atomic_structure",
        "title": "1. Cấu tạo Nguyên tử & Đồng vị (Atomic Structure & Isotopes Overview)",
        "selector": "#sec-atomic-structure",
        "en": "Section 1 details atomic architecture: An atom consists of a tiny dense nucleus containing protons and neutrons, surrounded by electrons in electron shells.",
        "vi": "Mục một chi tiết hóa cấu tạo nguyên tử: Nguyên tử gồm hạt nhân trung tâm đặc chứa proton và neutron, được bao quanh bởi các electron chuyển động trên các lớp vỏ."
    },
    {
        "id": "sec_subatomic_particles",
        "title": "⚛️ Subatomic Particles (Hạt Hạ nguyên tử)",
        "selector": "#sec-subatomic-particles",
        "en": "Subatomic particle properties: Protons carry relative charge plus one and mass one. Neutrons carry zero charge and mass one. Electrons carry relative charge minus one and negligible mass of 1 over 1840.",
        "vi": "Tính chất hạt hạ nguyên tử: Proton mang điện tích cộng một, khối lượng tương đối bằng một. Neutron không mang điện, khối lượng bằng một. Electron mang điện tích trừ một, khối lượng không đáng kể xấp xỉ một phần 1840."
    },
    {
        "id": "sec_calculating_particles",
        "title": "🧮 Calculating Particles & Notation (Tính toán Hạt & Ký hiệu)",
        "selector": "#sec-calculating-particles",
        "en": "Atomic notation: Proton number Z equals the number of protons and electrons in a neutral atom. Nucleon number A is the total number of protons plus neutrons. Neutrons equal A minus Z.",
        "vi": "Ký hiệu nguyên tử: Số hiệu nguyên tử Z bằng số proton và bằng số electron trong nguyên tử trung hòa. Số khối A là tổng số proton và neutron. Do đó, số neutron bằng A trừ Z."
    },
    {
        "id": "sec_isotopes",
        "title": "⚖️ Isotopes (Đồng vị)",
        "selector": "#sec-isotopes",
        "en": "Isotopes are atoms of the same element having the same number of protons but different numbers of neutrons. They exhibit identical chemical properties because they have the same outer shell electron configuration.",
        "vi": "Đồng vị là các nguyên tử của cùng một nguyên tố có cùng số proton nhưng khác nhau về số neutron. Chúng có tính chất hóa học giống hệt nhau vì có cùng cấu hình electron lớp ngoài cùng."
    },
    {
        "id": "sec_elements_compounds",
        "title": "2. Đơn chất, Hợp chất & Liên kết (Elements, Compounds & Bonding Overview)",
        "selector": "#sec-elements-compounds",
        "en": "Section 2 explores substances and chemical bonding: Distinguishing pure elements, chemically bonded compounds, and physical mixtures.",
        "vi": "Mục hai tìm hiểu về các chất và liên kết hóa học: Phân biệt đơn chất tinh khiết, hợp chất liên kết hóa học và hỗn hợp vật lý."
    },
    {
        "id": "sec_elem_comp_mix",
        "title": "🥗 Element, Compound & Mixture (Đơn chất, Hợp chất, Hỗn hợp)",
        "selector": "#sec-elem-comp-mix",
        "en": "An element contains only one type of atom. A compound contains two or more different elements chemically combined in fixed ratios. A mixture contains two or more substances physically mixed without chemical bonds and can be separated by physical methods.",
        "vi": "Đơn chất chỉ chứa một loại nguyên tử. Hợp chất chứa từ hai nguyên tố khác nhau trở lên liên kết hóa học theo tỷ lệ cố định. Hỗn hợp chứa nhiều chất trộn lẫn vật lý không có liên kết hóa học và có thể tách rời bằng các phương pháp cơ học."
    },
    {
        "id": "sec_ionic_bonding",
        "title": "⚡ Ionic Bonding (Liên kết Ion)",
        "selector": "#sec-ionic-bonding",
        "en": "Ionic bonding occurs between metals and non-metals via electron transfer. Metals lose electrons to form positive cations, while non-metals gain electrons to form negative anions, creating strong electrostatic attraction.",
        "vi": "Liên kết ion xảy ra giữa kim loại và phi kim thông qua sự nhường nhận electron. Kim loại nhường electron tạo cation dương, phi kim nhận electron tạo anion âm, hút nhau bằng lực hút tĩnh điện rất mạnh."
    },
    {
        "id": "sec_covalent_bonding",
        "title": "🤝 Covalent Bonding (Liên kết Cộng hóa trị)",
        "selector": "#sec-covalent-bonding",
        "en": "Covalent bonding occurs between non-metal atoms via sharing pairs of electrons to achieve stable noble gas electron configurations.",
        "vi": "Liên kết cộng hóa trị hình thành giữa các nguyên tử phi kim thông qua việc dùng chung các cặp electron để đạt cấu hình electron bền vững của khí hiếm."
    },
    {
        "id": "sec_lattices_macromolecules",
        "title": "3. Cấu trúc Mạng Tinh thể & Đại phân tử (Lattices & Macromolecules Overview)",
        "selector": "#sec-lattices-macromolecules",
        "en": "Section 3 investigates giant structures: Metallic bonding and giant covalent macromolecules including diamond, graphite, and silicon dioxide.",
        "vi": "Mục ba nghiên cứu cấu trúc mạng tinh thể khổng lồ: Liên kết kim loại và các đại phân tử cộng hóa trị như kim cương, than chì và silic đioxit."
    },
    {
        "id": "sec_metallic_bonding",
        "title": "🛡️ Metallic Bonding (Liên kết Kim loại)",
        "selector": "#sec-metallic-bonding",
        "en": "Metallic bonding is an electrostatic attraction between a regular lattice of positive metal ions and a sea of delocalised electrons, explaining high electrical conductivity and malleability.",
        "vi": "Liên kết kim loại là lực hút tĩnh điện giữa mạng tinh thể ion dương kim loại và biển electron tự do di chuyển hỗn loạn, giải thích tính dẫn điện tốt và tính dễ dát mỏng của kim loại."
    },
    {
        "id": "sec_giant_covalent",
        "title": "💎 Giant Covalent: Diamond vs Graphite vs SiO₂ (Đại phân tử Khổng lồ)",
        "selector": "#sec-giant-covalent",
        "en": "In Diamond, each carbon atom forms 4 strong covalent bonds in a tetrahedral lattice, making it extremely hard. In Graphite, each carbon bonds to 3 others in layers with delocalised electrons, making it soft, slippery, and electrically conductive. Silicon dioxide has a similar rigid tetrahedral structure to diamond.",
        "vi": "Trong Kim cương, mỗi nguyên tử carbon tạo 4 liên kết cộng hóa trị tứ diện rất cứng. Trong Than chì, mỗi carbon chỉ liên kết với 3 carbon khác tạo thành các lớp trượt với electron tự do, giúp than chì mềm và dẫn điện tốt. Silic đioxit có mạng tinh thể tứ diện tương tự như kim cương."
    }
]

C2_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C2", "selector": "#sec-header"},
    "sec_periodic_table": {"start": 1, "end": 1, "title": "Bảng tuần hoàn 20 Nguyên tố", "selector": "#sec-periodic-table"},
    "sec_atomic_structure": {"start": 2, "end": 5, "title": "1. Cấu tạo Nguyên tử & Đồng vị", "selector": "#sec-atomic-structure"},
    "sec_elements_compounds": {"start": 6, "end": 9, "title": "2. Đơn chất, Hợp chất & Liên kết", "selector": "#sec-elements-compounds"},
    "sec_lattices_macromolecules": {"start": 10, "end": 12, "title": "3. Mạng Tinh thể & Đại phân tử", "selector": "#sec-lattices-macromolecules"}
}


# =====================================================================
# C3: STOICHIOMETRY
# =====================================================================
C3_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C3: Hóa học Định lượng & Khái niệm Mol",
        "selector": "#sec-header",
        "en": "Welcome to Topic C3: Stoichiometry. Chemical reactions obey the law of conservation of mass. In this lesson, we master chemical formulas and state symbols, navigate mole calculations involving mass, gas volume, and solutions, and determine empirical formulas and reaction yields.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C3: Hóa học Định lượng và Khái niệm Mol. Phản ứng hóa học tuân theo định luật bảo toàn khối lượng. Trong bài học này, chúng ta sẽ làm chủ công thức hóa học, ký hiệu trạng thái, các tam giác tính toán số mol theo khối lượng, thể tích khí và dung dịch, cùng công thức đơn giản nhất và hiệu suất phản ứng."
    },
    {
        "id": "sec_formulas_equations",
        "title": "1. Công thức & Phương trình Hóa học (Formulas & Equations Overview)",
        "selector": "#sec-formulas-equations",
        "en": "Section 1 establishes chemical language: Relative atomic mass Ar from the periodic table, calculating relative molecular mass Mr, and writing balanced equations with state symbols.",
        "vi": "Mục một thiết lập ngôn ngữ hóa học: Khối lượng nguyên tử tương đối Ar từ bảng tuần hoàn, tính khối lượng phân tử Mr, và viết phương trình hóa học cân bằng kèm ký hiệu trạng thái."
    },
    {
        "id": "sec_atomic_mass",
        "title": "📌 Relative Atomic & Molecular Masses (Ar & Mr)",
        "selector": "#sec-atomic-mass",
        "en": "Relative atomic mass Ar is the average mass of naturally occurring atoms of an element compared to 1/12th of Carbon-12. Relative molecular mass Mr is the sum of relative atomic masses in a molecule.",
        "vi": "Khối lượng nguyên tử tương đối Ar là khối lượng trung bình của các nguyên tử nguyên tố so với một phần 12 khối lượng nguyên tử Carbon 12. Khối lượng phân tử tương đối Mr bằng tổng các Ar của mọi nguyên tử có trong công thức."
    },
    {
        "id": "sec_state_symbols",
        "title": "📌 State Symbols & Balancing (Ký hiệu Trạng thái & Cân bằng)",
        "selector": "#sec-state-symbols",
        "en": "State symbols indicate physical states: solid (s), liquid (l), gas (g), and aqueous solution (aq). Pure water is liquid, while dissolved acids, alkalis, and salts are aqueous.",
        "vi": "Ký hiệu trạng thái thể hiện pha vật lý: rắn (s), lỏng (l), khí (g) và dung dịch trong nước (aq). Nước cất là chất lỏng (l), trong khi axit, kiềm và muối tan trong nước phải mang ký hiệu (aq)."
    },
    {
        "id": "sec_mole_concept",
        "title": "2. Khái niệm Mol & Tam giác Tính toán (The Mole Concept Overview)",
        "selector": "#sec-mole-concept",
        "en": "Section 2 introduces The Mole: one mole contains 6.02 times 10 to the 23rd power particles, Avogadro's constant. It bridges atomic particles with macroscopic grams.",
        "vi": "Mục hai giới thiệu Khái niệm Mol: một mol chứa 6.02 nhân 10 mũ 23 hạt, gọi là hằng số Avogadro. Mol là cầu nối chuyển đổi giữa số hạt vi mô và khối lượng gam vĩ mô."
    },
    {
        "id": "sec_mole_mass",
        "title": "📐 Mole & Mass: n = m / Mr (Mol & Khối lượng)",
        "selector": "#sec-mole-mass",
        "en": "The Mass triangle: Moles n equals mass in grams divided by relative molecular mass Mr. Mass equals moles times Mr.",
        "vi": "Tam giác khối lượng: Số mol n bằng khối lượng m tính bằng gam chia cho khối lượng mol Mr. Ngược lại, khối lượng m bằng số mol nhân Mr."
    },
    {
        "id": "sec_mole_gas",
        "title": "📐 Mole & Gas Volume: V = n × 24 dm³ (Thể tích Khí rtp)",
        "selector": "#sec-mole-gas",
        "en": "The Gas Volume triangle: One mole of any gas occupies 24 cubic decimetres at room temperature and pressure. Moles equals volume in dm³ divided by 24.",
        "vi": "Tam giác thể tích khí: Một mol của bất kỳ chất khí nào đều chiếm 24 đềximét khối ở điều kiện phòng. Số mol bằng thể tích khí tính theo dm³ chia cho 24."
    },
    {
        "id": "sec_mole_conc",
        "title": "📐 Mole & Solution Concentration: c = n / V (Nồng độ Dung dịch)",
        "selector": "#sec-mole-conc",
        "en": "The Solution triangle: Concentration c in mol per dm³ equals moles divided by solution volume in dm³. Volume in cm³ must always be divided by 1000 to convert to dm³.",
        "vi": "Tam giác nồng độ dung dịch: Nồng độ c tính bằng mol trên dm³ bằng số mol chia cho thể tích dung dịch tính bằng dm³. Nếu thể tích cho bằng cm³, bắt buộc phải chia cho 1000 để đổi ra dm³."
    },
    {
        "id": "sec_empirical_yield",
        "title": "3. Công thức Thực nghiệm & Hiệu suất (Empirical Formula & Yield Overview)",
        "selector": "#sec-empirical-yield",
        "en": "Section 3 covers empirical formula determination and calculating percentage yield and percentage purity in industrial and laboratory syntheses.",
        "vi": "Mục ba phân tích cách tìm công thức thực nghiệm đơn giản nhất cùng tính toán hiệu suất phản ứng và độ tinh khiết trong thực nghiệm."
    },
    {
        "id": "sec_empirical_formula",
        "title": "🧪 Empirical vs Molecular Formula (Công thức Thực nghiệm)",
        "selector": "#sec-empirical-formula",
        "en": "Empirical formula gives the simplest whole number ratio of atoms of each element in a compound, calculated by dividing mass or percentage by Ar and simplifying ratios.",
        "vi": "Công thức thực nghiệm biểu thị tỷ lệ số nguyên tử nguyên giản nhất của các nguyên tố trong hợp chất, tính bằng cách lấy khối lượng hoặc phần trăm chia cho Ar rồi rút gọn tỷ lệ về các số nguyên nhỏ nhất."
    },
    {
        "id": "sec_yield_purity",
        "title": "⚖️ Percentage Yield & Purity (Hiệu suất & Độ tinh khiết)",
        "selector": "#sec-yield-purity",
        "en": "Percentage yield equals actual mass obtained divided by theoretical maximum mass times 100 percent. Percentage purity equals mass of pure substance divided by total mass of sample times 100 percent.",
        "vi": "Hiệu suất phản ứng bằng khối lượng thực tế thu được chia cho khối lượng lý thuyết tối đa nhân 100 phần trăm. Độ tinh khiết bằng khối lượng chất tinh khiết chia cho khối lượng toàn bộ mẫu nhân 100 phần trăm."
    }
]

C3_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C3", "selector": "#sec-header"},
    "sec_formulas_equations": {"start": 1, "end": 3, "title": "1. Công thức & Phương trình", "selector": "#sec-formulas-equations"},
    "sec_mole_concept": {"start": 4, "end": 7, "title": "2. Khái niệm Mol & Tam giác Tính toán", "selector": "#sec-mole-concept"},
    "sec_empirical_yield": {"start": 8, "end": 10, "title": "3. Công thức Thực nghiệm & Hiệu suất", "selector": "#sec-empirical-yield"}
}


# =====================================================================
# C4: ELECTROCHEMISTRY
# =====================================================================
C4_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề C4: Điện hóa học & Điện phân",
        "selector": "#sec-header",
        "en": "Welcome to Topic C4: Electrochemistry. Electricity can drive non-spontaneous chemical reactions. In this lesson, we study the fundamental components of electrolysis cells, explore molten versus aqueous electrolysis and discharge rules, and investigate electroplating and hydrogen-oxygen fuel cells.",
        "vi": "Chào mừng các bạn đến với Chuyên đề C4: Điện hóa học và Quá trình Điện phân. Dòng điện có thể thúc đẩy các phản ứng hóa học không tự phát. Trong bài học này, chúng ta sẽ tìm hiểu cấu tạo bình điện phân, so sánh điện phân nóng chảy và dung dịch, cùng các ứng dụng mạ điện và pin nhiên liệu hydro-oxy."
    },
    {
        "id": "sec_electrolysis_basics",
        "title": "1. Cơ chế Điện phân & Cấu tạo Bình điện phân (Basics of Electrolysis Overview)",
        "selector": "#sec-electrolysis-basics",
        "en": "Section 1 defines Electrolysis: the breakdown of an ionic compound, molten or in aqueous solution, by the passage of electricity.",
        "vi": "Mục một định nghĩa Quá trình Điện phân: là sự phân hủy một hợp chất ion ở trạng thái nóng chảy hoặc trong dung dịch nước dưới tác dụng của dòng điện một chiều."
    },
    {
        "id": "sec_cell_components",
        "title": "⚡ Electrolysis Cell Anatomy: Anode & Cathode (Cấu tạo Bình điện phân)",
        "selector": "#sec-cell-components",
        "en": "An electrolysis cell comprises a power supply, electrolyte containing mobile ions, and two electrodes: Positive Anode attracts negative anions, while Negative Cathode attracts positive cations.",
        "vi": "Cấu tạo bình điện phân gồm nguồn điện một chiều, chất điện ly chứa các ion chuyển động tự do và hai điện cực: Anode cực dương hút anion âm, còn Cathode cực âm hút cation dương."
    },
    {
        "id": "sec_oil_rig",
        "title": "🧠 OIL RIG & Redox at Electrodes (Oxy hóa - Khử tại Điện cực)",
        "selector": "#sec-oil-rig",
        "en": "Remember OIL RIG: Oxidation Is Loss of electrons, which occurs at the positive Anode. Reduction Is Gain of electrons, which occurs at the negative Cathode.",
        "vi": "Mẹo nhớ kinh điển OIL RIG: Quá trình Oxy hóa là sự Mất electron xảy ra tại cực dương Anode. Quá trình Khử là sự Nhận electron xảy ra tại cực âm Cathode."
    },
    {
        "id": "sec_molten_aqueous",
        "title": "2. Điện phân Nóng chảy vs Dung dịch (Molten vs Aqueous Electrolysis Overview)",
        "selector": "#sec-molten-aqueous",
        "en": "Section 2 compares molten and aqueous electrolysis: In aqueous solutions, water partially dissociates into H+ and OH- ions, competing with solute ions at both electrodes.",
        "vi": "Mục hai so sánh điện phân nóng chảy và dung dịch: Trong dung dịch, nước phân ly một phần ra ion H+ và OH-, tạo ra sự cạnh tranh phóng điện tại cả hai điện cực."
    },
    {
        "id": "sec_molten_lead_bromide",
        "title": "🔥 Molten Lead(II) Bromide Electrolysis (Điện phân PbBr₂ Nóng chảy)",
        "selector": "#sec-molten-lead-bromide",
        "en": "During electrolysis of molten lead(II) bromide: Lead ions gain electrons at the cathode to form silvery molten lead metal. Bromide ions lose electrons at the anode to produce reddish-brown bromine gas.",
        "vi": "Khi điện phân chì hai bromua nóng chảy: Ion chì Pb2+ nhận electron tại cathode tạo thành kim loại chì lỏng màu bạc. Ion bromua Br- mất electron tại anode sinh ra khí brom màu nâu đỏ."
    },
    {
        "id": "sec_aqueous_discharge",
        "title": "📜 Aqueous Discharge Rules (Quy tắc Phóng điện Dung dịch)",
        "selector": "#sec-aqueous-discharge",
        "en": "Discharge rules: At the cathode, hydrogen gas is discharged unless the metal is less reactive than hydrogen, such as copper. At the anode, halide ions produce halogen gas if concentrated; otherwise, hydroxide ions produce oxygen gas.",
        "vi": "Quy tắc phóng điện: Tại cathode, khí hydrogen thoát ra trừ khi kim loại kém hoạt động hơn hydro như đồng hay bạc. Tại anode, ion halide phóng điện tạo halogen nếu đậm đặc; nếu không, ion hydroxide OH- sẽ phóng điện tạo khí oxygen."
    },
    {
        "id": "sec_electroplating_cells",
        "title": "3. Mạ điện & Pin Nhiên liệu (Electroplating & Fuel Cells Overview)",
        "selector": "#sec-electroplating_cells",
        "en": "Section 3 examines industrial electrochemical applications: Electroplating metals for corrosion resistance and aesthetics, and clean hydrogen-oxygen fuel cells.",
        "vi": "Mục ba nghiên cứu các ứng dụng công nghiệp: Kỹ thuật mạ điện kim loại chống ăn mòn và tăng tính thẩm mỹ, cùng pin nhiên liệu hydro-oxy sạch."
    },
    {
        "id": "sec_electroplating",
        "title": "🛡️ Electroplating Principles (Nguyên lý Mạ điện)",
        "selector": "#sec-electroplating",
        "en": "To electroplate an object: Connect the object to the negative cathode, use the pure plating metal as the positive anode, and use an electrolyte containing soluble ions of the plating metal.",
        "vi": "Để mạ điện một vật: Nối vật cần mạ vào cực âm cathode, dùng miếng kim loại mạ tinh khiết làm cực dương anode và dùng dung dịch muối tan của kim loại mạ làm chất điện ly."
    },
    {
        "id": "sec_fuel_cells",
        "title": "💧 Hydrogen-Oxygen Fuel Cell (Pin Nhiên liệu Hydro-Oxy)",
        "selector": "#sec-fuel-cells",
        "en": "The hydrogen-oxygen fuel cell combines hydrogen and oxygen to produce electricity with water as the only byproduct, offering zero greenhouse gas emissions and high efficiency.",
        "vi": "Pin nhiên liệu hydro-oxy kết hợp khí hydro và oxy để tạo ra dòng điện với chất thải duy nhất là nước tinh khiết, mang lại hiệu suất cao và không phát thải khí nhà kính."
    }
]

C4_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề C4", "selector": "#sec-header"},
    "sec_electrolysis_basics": {"start": 1, "end": 3, "title": "1. Cơ chế & Cấu tạo Bình điện phân", "selector": "#sec-electrolysis-basics"},
    "sec_molten_aqueous": {"start": 4, "end": 6, "title": "2. Điện phân Nóng chảy vs Dung dịch", "selector": "#sec-molten-aqueous"},
    "sec_electroplating_cells": {"start": 7, "end": 9, "title": "3. Mạ điện & Pin Nhiên liệu", "selector": "#sec-electroplating-cells"}
}


# =====================================================================
# BATCH 1 AUDIO GENERATION PIPELINE
# =====================================================================
BATCH1_LECTURES = [
    ("c1", "3fc0ef74-3661-4f23-a8a8-9c33d11051f5", "C1: States of matter", C1_SEGMENTS, C1_MAJOR_SECTIONS),
    ("c2", "ee4f94c2-382b-4dbb-aaf8-981e7b0d7223", "C2: Atoms elements and compounds", C2_SEGMENTS, C2_MAJOR_SECTIONS),
    ("c3", "f0988036-6fd0-4768-993d-a5ea5fe4eb0b", "C3: Stoichiometry", C3_SEGMENTS, C3_MAJOR_SECTIONS),
    ("c4", "4732621b-f827-4b12-934b-3b53e694cc2a", "C4: Electrochemistry", C4_SEGMENTS, C4_MAJOR_SECTIONS),
]

async def main():
    print("=====================================================================")
    print("STARTING AUDIO GENERATION FOR CHEMISTRY BATCH 1 (C1, C2, C3, C4)")
    print("=====================================================================")
    
    for code, lec_id, title, segments, majors in BATCH1_LECTURES:
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

    print("\n🎉 ALL BATCH 1 (C1-C4) AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
