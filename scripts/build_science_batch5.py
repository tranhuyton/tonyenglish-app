import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC C1: States of matter
# ==============================================================================
async def build_c1():
    lid = '3fc0ef74-3661-4f23-a8a8-9c33d11051f5'
    code = 'c1'
    title = 'C1: States of matter'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-states-particles" class="lecture-interactive-card" data-lecture-section="sec_states_particles" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-heating-curves" class="lecture-interactive-card" data-lecture-section="sec_heating_curves" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-gas-behavior" class="lecture-interactive-card" data-lecture-section="sec_gas_behavior" style="cursor: pointer; ')
    
    t_h2_4 = h2s[4]
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-diffusion-mass" class="lecture-interactive-card" data-lecture-section="sec_diffusion_mass" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C1 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C1: Các Trạng thái của Vật chất & Thuyết Động học",
            "selector": "#sec-header",
            "en": "Welcome to Cambridge IGCSE Co-ordinated Sciences Chemistry, Topic C1: States of matter. Chemistry begins with the kinetic particle model of matter. In this foundation chapter, we explore solid, liquid, and gas particle arrangements, decipher heating curves and latent heat plateaus, analyze gas volume changes under temperature and pressure, and investigate diffusion rates relative to molecular mass.",
            "vi": "Chào mừng các bạn đến với phần Hóa học trong môn Khoa học Phối hợp Cambridge IGCSE, Chuyên đề C1: Các Trạng thái của Vật chất và Thuyết Động học Phân tử. Hóa học khởi đầu từ mô hình hạt động học. Trong bài học nền tảng này, chúng ta sẽ khảo sát sự sắp xếp hạt ở thể rắn, lỏng, khí, giải mã đường cong đun nóng, định luật chất khí và tốc độ khuếch tán phụ thuộc khối lượng phân tử."
        },
        {
            "id": "sec_states_particles",
            "title": "1. Ba Trạng thái của Vật chất & Cấu trúc Hạt",
            "selector": "#sec-states-particles",
            "en": "Section 1 contrasts the three states of matter using the kinetic particle model: In Solids, particles are tightly packed in regular lattice arrangements, vibrating about fixed positions with strong intermolecular forces, giving fixed shape and volume. In Liquids, particles are closely packed but arranged irregularly, sliding past one another with moderate forces, adopting container shape while retaining fixed volume. In Gases, particles are widely separated, moving randomly at high speeds with negligible forces, having neither fixed shape nor fixed volume.",
            "vi": "Mục một so sánh 3 trạng thái vật chất qua thuyết động học: Ở thể Rắn, các hạt xếp khít nhau theo mạng tinh thể trật tự đều đặn, chỉ dao động quanh vị trí cố định nhờ lực hút liên phân tử mạnh, giữ nguyên hình dạng và thể tích xác định. Ở thể Lỏng, các hạt nằm gần nhau nhưng sắp xếp lộn xộn, trượt tự do lên nhau với lực hút trung bình, chiếm hình dạng của đáy bình chứa nhưng giữ thể tích cố định. Ở thể Khí, các hạt cách rất xa nhau, chuyển động hỗn loạn ở tốc độ cao với lực tương tác không đáng kể, không có hình dạng và thể tích cố định."
        },
        {
            "id": "sec_heating_curves",
            "title": "2. Biến đổi Trạng thái & Đồ thị Đun nóng (Heating Curves)",
            "selector": "#sec-heating-curves",
            "en": "Section 2 investigates phase changes: Melting transforms solid to liquid at a fixed melting point; Boiling transforms liquid into gas throughout the bulk at a specific boiling point. Evaporation occurs only at liquid surfaces at any temperature below boiling. Condensation turns gas to liquid, and Freezing turns liquid to solid. On a heating curve, horizontal plateaus indicate phase transitions where absorbed thermal energy overcomes intermolecular attractions rather than increasing kinetic energy, keeping temperature constant.",
            "vi": "Mục hai nghiên cứu chuyển pha trạng thái: Nóng chảy chuyển rắn thành lỏng tại điểm nóng chảy xác định; Sôi chuyển lỏng thành khí trong toàn bộ thể tích chất lỏng tại điểm sôi. Bay hơi chỉ diễn ra trên bề mặt chất lỏng ở mọi nhiệt độ dưới điểm sôi. Ngưng tụ chuyển khí thành lỏng, và Đông đặc chuyển lỏng thành rắn. Trên đồ thị đun nóng, các đoạn nằm ngang biểu thị giai đoạn chuyển thể nơi nhiệt năng hấp thu được dùng để phá vỡ lực liên kết liên phân tử thay vì làm tăng động năng, khiến nhiệt độ không đổi."
        },
        {
            "id": "sec_gas_behavior",
            "title": "3. Ảnh hưởng của Nhiệt độ & Áp suất lên Thể tích Chất khí",
            "selector": "#sec-gas-behavior",
            "en": "Section 3 examines gas behavior: Increasing temperature increases average kinetic energy and velocity of gas particles; if pressure is constant, particles collide more forcefully with container walls, expanding gas volume. If volume is constant, more frequent and energetic collisions increase pressure. Increasing external pressure compresses gas particles closer together, decreasing volume proportionally according to Boyle's law.",
            "vi": "Mục ba phân tích hành vi của chất khí: Tăng nhiệt độ làm tăng động năng trung bình và tốc độ của các phân tử khí; nếu giữ áp suất không đổi, các hạt va đập mạnh hơn làm giãn nở thể tích khí. Nếu thể tích bình kín cố định, các va chạm dồn dập làm áp suất chất khí tăng vọt. Tăng áp suất nén bên ngoài sẽ ép các phân tử khí lại gần nhau hơn, làm giảm thể tích tương ứng theo định luật Boyle."
        },
        {
            "id": "sec_diffusion_mass",
            "title": "4. Khuyếch tán & Khối lượng Phân tử Tương đối (Mr)",
            "selector": "#sec-diffusion-mass",
            "en": "Section 4 covers Diffusion in gases: the random spreading out of particles from regions of higher concentration to lower concentration. The rate of diffusion is inversely proportional to relative molecular mass: lighter gas molecules move with higher average velocity than heavier gas molecules at the same temperature. In the classic reaction tube experiment, ammonia gas with molecular mass seventeen diffuses faster than hydrogen chloride gas with molecular mass 36.5, forming a white ring of ammonium chloride closer to the hydrochloric acid end.",
            "vi": "Mục bốn phân tích hiện tượng khuếch tán khí: là sự chuyển động hỗn loạn của các hạt từ nơi có nồng độ cao đến nơi có nồng độ thấp hơn. Tốc độ khuếch tán tỷ lệ nghịch với khối lượng phân tử tương đối: phân tử khí nhẹ hơn chuyển động với vận tốc trung bình lớn hơn phân tử khí nặng ở cùng nhiệt độ. Trong thí nghiệm ống thủy tinh kinh điển, khí amoniac NH3 có phân tử khối 17 khuếch tán nhanh hơn khí hydro clorua HCl có phân tử khối 36.5, tạo nên vành khói trắng amoni clorua NH4Cl nằm lệch hẳn về phía đầu bông tẩm axit clohidric."
        }
    ]

    major_sections = [
        {"id": "sec_states_particles", "title": "1. Ba Trạng thái của Vật chất & Thuyết Động học"},
        {"id": "sec_heating_curves", "title": "2. Biến đổi Trạng thái & Đồ thị Đun nóng"},
        {"id": "sec_gas_behavior", "title": "3. Nhiệt độ & Áp suất Chất khí"},
        {"id": "sec_diffusion_mass", "title": "4. Khuyếch tán & Khối lượng Phân tử (Mr)"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C1 successfully built!")


# ==============================================================================
# TOPIC C2: Atoms elements and compounds
# ==============================================================================
async def build_c2():
    lid = 'ee4f94c2-382b-4dbb-aaf8-981e7b0d7223'
    code = 'c2'
    title = 'C2: Atoms elements and compounds'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-atomic-structure" class="lecture-interactive-card" data-lecture-section="sec_atomic_structure" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-elements-compounds" class="lecture-interactive-card" data-lecture-section="sec_elements_compounds" style="cursor: pointer; ')
    
    t_h2_4 = h2s[4]
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-lattices-macromolecules" class="lecture-interactive-card" data-lecture-section="sec_lattices_macromolecules" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C2 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C2: Nguyên tử, Nguyên tố & Hợp chất",
            "selector": "#sec-header",
            "en": "Welcome to Topic C2: Atoms, elements and compounds. Matter is constructed from atomic building blocks. In this comprehensive lesson, we decode subatomic particles and isotopes, distinguish elements, compounds, and mixtures, examine ionic and covalent bonding, and analyze giant covalent lattices and metallic structures.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C2: Nguyên tử, Nguyên tố và Hợp chất. Vật chất được cấu tạo từ các viên gạch nguyên tử. Trong bài học này, chúng ta sẽ khảo sát các hạt hạ nguyên tử và đồng vị, phân biệt đơn chất, hợp chất và hỗn hợp, làm chủ liên kết ion và cộng hóa trị, cùng mạng tinh thể khổng lồ và liên kết kim loại."
        },
        {
            "id": "sec_atomic_structure",
            "title": "1. Cấu tạo Nguyên tử, Hạt Hạ nguyên tử & Đồng vị (Isotopes)",
            "selector": "#sec-atomic-structure",
            "en": "Section 1 details atomic architecture: An atom consists of a tiny dense central nucleus containing positively charged protons and neutral neutrons, surrounded by negatively charged electrons orbiting in energy shells. Proton number or atomic number identifies the element and specifies nuclear charge. Mass number or nucleon number is the total sum of protons plus neutrons. Isotopes are atoms of the same element with the same number of protons but different numbers of neutrons, sharing identical chemical properties due to having the same electron configuration.",
            "vi": "Mục một chi tiết hóa cấu tạo nguyên tử: Nguyên tử gồm một hạt nhân cực nhỏ đặc ở trung tâm chứa proton mang điện tích dương và neutron không mang điện, bao quanh bởi đám mây electron mang điện tích âm quay trên các lớp vỏ năng lượng. Số proton hay số hiệu nguyên tử Z đặc trưng cho nguyên tố hóa học. Số khối A là tổng số hạt nucleon (proton cộng neutron). Đồng vị (Isotopes) là các nguyên tử của cùng một nguyên tố có cùng số proton nhưng khác số neutron, có tính chất hóa học giống hệt nhau do có cùng cấu hình electron lớp ngoài cùng."
        },
        {
            "id": "sec_elements_compounds",
            "title": "2. Đơn chất, Hợp chất, Hỗn hợp & Liên kết Hóa học",
            "selector": "#sec-elements-compounds",
            "en": "Section 2 distinguishes chemical categories and bonds: An Element is a pure substance composed of only one type of atom. A Compound consists of two or more different elements chemically bonded in fixed stoichiometric ratios. A Mixture contains substances physically intermingled without chemical bonds. Ionic bonding occurs between metals and non-metals via electrostatic attraction between oppositely charged ions formed by electron transfer. Covalent bonding occurs between non-metals via electrostatic attraction between shared pairs of electrons and adjacent nuclei.",
            "vi": "Mục hai phân biệt các khái niệm hóa học và liên kết: Đơn chất (Element) là chất tinh khiết chỉ chứa một loại nguyên tử. Hợp chất (Compound) gồm hai hay nhiều nguyên tố hóa học liên kết với nhau theo tỷ lệ số học xác định. Hỗn hợp (Mixture) gồm các chất trộn lẫn vật lý mà không có liên kết hóa học. Liên kết ion hình thành giữa kim loại và phi kim qua lực hút tĩnh điện giữa các ion trái dấu sau khi chuyển giao electron. Liên kết cộng hóa trị hình thành giữa các phi kim nhờ lực hút tĩnh điện giữa cặp electron dùng chung và hạt nhân nguyên tử."
        },
        {
            "id": "sec_lattices_macromolecules",
            "title": "3. Mạng Tinh thể, Tinh thể Khổng lồ & Kim loại",
            "selector": "#sec-lattices-macromolecules",
            "en": "Section 3 compares structural lattices: Giant ionic lattices like sodium chloride feature alternating positive and negative ions held by strong electrostatic forces in all directions, yielding high melting points and electrical conductivity only when molten or aqueous. Giant covalent macromolecules like Diamond feature tetrahedral carbon lattices of immense hardness, whereas Graphite forms hexagonal planar layers with delocalized electrons that conduct electricity and slide easily. Metallic bonding consists of an orderly lattice of positive metal ions embedded in a sea of delocalized mobile electrons, conferring high electrical conductivity and malleability.",
            "vi": "Mục ba so sánh các mạng tinh thể: Mạng tinh thể ion khổng lồ như muối ăn NaCl gồm các ion dương và âm xen kẽ hút nhau bằng lực tĩnh điện cực mạnh về mọi hướng, có nhiệt độ nóng chảy rất cao và chỉ dẫn điện khi ở trạng thái nóng chảy hoặc dung dịch. Tinh thể cộng hóa trị khổng lồ như Kim cương gồm mạng tứ diện carbon siêu bền cứng, trong khi Than chì (Graphite) gồm các lớp lục giác có electron tự do giúp dẫn điện và trượt êm dùng làm ruột bút chì. Liên kết kim loại gồm mạng tinh thể các ion dương kim loại ngâm trong biển electron tự do chuyển động hỗn loạn, tạo nên tính dẫn điện, dẫn nhiệt tuyệt vời và tính dát mỏng."
        }
    ]

    major_sections = [
        {"id": "sec_atomic_structure", "title": "1. Cấu tạo Nguyên tử & Đồng vị (Isotopes)"},
        {"id": "sec_elements_compounds", "title": "2. Đơn chất, Hợp chất & Liên kết Hóa học"},
        {"id": "sec_lattices_macromolecules", "title": "3. Mạng Tinh thể Khổng lồ & Kim loại"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C2 successfully built!")


# ==============================================================================
# TOPIC C3: Stoichiometry
# ==============================================================================
async def build_c3():
    lid = 'f0988036-6fd0-4768-993d-a5ea5fe4eb0b'
    code = 'c3'
    title = 'C3: Stoichiometry'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-formulas-equations" class="lecture-interactive-card" data-lecture-section="sec_formulas_equations" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-mole-concept" class="lecture-interactive-card" data-lecture-section="sec_mole_concept" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-empirical-yield" class="lecture-interactive-card" data-lecture-section="sec_empirical_yield" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C3 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C3: Hóa học Định lượng & Khái niệm Mol",
            "selector": "#sec-header",
            "en": "Welcome to Topic C3: Stoichiometry. Stoichiometry is the quantitative language of chemistry. In this central calculation topic, we balance chemical and ionic equations, master the mole concept and molar mass conversions, calculate gas molar volumes and solution concentrations, and compute empirical formulas and percentage yields.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C3: Hóa học Định lượng và Khái niệm Mol. Tính toán lượng chất là ngôn ngữ định lượng của hóa học. Trong bài học tính toán trọng tâm này, chúng ta sẽ cân bằng phương trình hóa học và phương trình ion, làm chủ khái niệm mol, thể tích mol chất khí, nồng độ dung dịch, công thức thực nghiệm và hiệu suất phản ứng."
        },
        {
            "id": "sec_formulas_equations",
            "title": "1. Công thức Hóa học, Phương trình Cân bằng & Phương trình Ion",
            "selector": "#sec-formulas-equations",
            "en": "Section 1 reviews chemical formulas and balancing: Chemical formulas show the number of each type of atom in a compound. Under the Law of Conservation of Mass, atoms are neither created nor destroyed during chemical reactions; equations must have identical atom counts on reactant and product sides. State symbols designate physical phase: s for solid, l for liquid, g for gas, and aq for aqueous solution. Ionic equations omit spectator ions, focusing on species actively transferring electrons or forming precipitates.",
            "vi": "Mục một ôn tập công thức hóa học và cân bằng phương trình: Công thức hóa học biểu thị số lượng từng nguyên tử trong hợp chất. Theo Định luật Bảo toàn Khối lượng, nguyên tử không tự sinh ra và không tự mất đi; số lượng nguyên tử mỗi nguyên tố ở hai vế phương trình phải bằng nhau tuyệt đối. Ký hiệu trạng thái gồm s cho thể rắn, l cho thể lỏng, g cho thể khí và aq cho dung dịch trong nước. Phương trình ion rút gọn triệt tiêu các ion khán giả (spectator ions), chỉ giữ lại các ion trực tiếp tham gia phản ứng tạo kết tủa, khí hoặc chất điện ly yếu."
        },
        {
            "id": "sec_mole_concept",
            "title": "2. Khái niệm Mol & Các Công thức Tính toán Cốt lõi",
            "selector": "#sec-mole-concept",
            "en": "Section 2 establishes the Mole: A mole is the amount of substance containing Avogadro's constant, 6.02 times 10 to the 23rd power particles. The three fundamental calculation triangles are: First, mass equals moles multiplied by molar mass (M_r). Second, volume of any gas at room temperature and pressure (r.t.p.) equals moles multiplied by 24 cubic decimeters. Third, moles of solute in a solution equals concentration in moles per cubic decimeter multiplied by volume in cubic decimeters.",
            "vi": "Mục hai thiết lập khái niệm Mol: Một mol là lượng chất chứa hằng số Avogadro gồm 6.02 nhân 10 mũ 23 hạt vi mô. Ba tam giác công thức tính toán trụ cột gồm: Thứ nhất, Khối lượng chất m bằng số mol n nhân phân tử khối Mr. Thứ hai, Thể tích V của mọi chất khí ở điều kiện phòng (r.t.p.) bằng số mol n nhân 24 decimet khối (hoặc 24000 cm3). Thứ ba, Số mol chất tan n trong dung dịch bằng Nồng độ mol C nhân Thể tích dung dịch V tính bằng decimet khối."
        },
        {
            "id": "sec_empirical_yield",
            "title": "3. Công thức Thực nghiệm, Hiệu suất & Độ Tinh khiết",
            "selector": "#sec-empirical-yield",
            "en": "Section 3 covers advanced stoichiometry: The Empirical formula represents the simplest whole-number ratio of atoms of each element in a compound, calculated by dividing mass percentages by relative atomic masses and scaling to integers. The Molecular formula shows actual atom counts, obtained by dividing molar mass by empirical formula mass. Percentage Yield compares actual product mass obtained to theoretical maximum calculated yield: Actual yield divided by Theoretical yield multiplied by 100%.",
            "vi": "Mục ba hướng dẫn các bài toán định lượng nâng cao: Công thức thực nghiệm (Empirical formula) biểu thị tỷ lệ số nguyên tối giản của các nguyên tử trong hợp chất, tính bằng cách chia phần trăm khối lượng cho nguyên tử khối Ar rồi quy về tỷ lệ nguyên. Công thức phân tử biểu thị số nguyên tử thực tế, tính bằng cách nhân công thức thực nghiệm với tỷ số giữa phân tử khối thực tế và khối lượng công thức thực nghiệm. Hiệu suất phản ứng (Percentage Yield) bằng Khối lượng sản phẩm thực tế thu được chia cho Khối lượng lý thuyết tính theo phương trình rồi nhân 100%."
        }
    ]

    major_sections = [
        {"id": "sec_formulas_equations", "title": "1. Công thức & Phương trình Cân bằng"},
        {"id": "sec_mole_concept", "title": "2. Khái niệm Mol & Tam giác Tính toán"},
        {"id": "sec_empirical_yield", "title": "3. Công thức Thực nghiệm & Hiệu suất Phản ứng"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C3 successfully built!")


# ==============================================================================
# TOPIC C4: Electrochemistry
# ==============================================================================
async def build_c4():
    lid = '4732621b-f827-4b12-934b-3b53e694cc2a'
    code = 'c4'
    title = 'C4: Electrochemistry'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-electrolysis-basics" class="lecture-interactive-card" data-lecture-section="sec_electrolysis_basics" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-molten-aqueous" class="lecture-interactive-card" data-lecture-section="sec_molten_aqueous" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-electroplating-cells" class="lecture-interactive-card" data-lecture-section="sec_electroplating_cells" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic C4 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề C4: Điện hóa học & Điện phân",
            "selector": "#sec-header",
            "en": "Welcome to Topic C4: Electrochemistry. Electrochemistry couples chemical reactivity with electrical current. In this lesson, we study the fundamental components of electrolytic cells, contrast molten versus aqueous solution electrolysis, predict selective discharge products at electrodes, and examine industrial electroplating and hydrogen fuel cells.",
            "vi": "Chào mừng các bạn đến với Chuyên đề C4: Điện hóa học và Hiện tượng Điện phân. Điện hóa học kết nối phản ứng hóa học với dòng điện. Trong bài học này, chúng ta sẽ khảo sát cấu tạo bình điện phân, so sánh điện phân muối nóng chảy và dung dịch nước, quy tắc phóng điện chọn lọc tại điện cực, cùng kỹ thuật mạ điện công nghiệp và pin nhiên liệu hydro."
        },
        {
            "id": "sec_electrolysis_basics",
            "title": "1. Nguyên lý Cơ bản của Hiện tượng Điện phân",
            "selector": "#sec-electrolysis-basics",
            "en": "Section 1 defines Electrolysis: the breakdown of an ionic compound, molten or in aqueous solution, by the passage of electricity. An Electrolyte is a liquid containing mobile free ions that conducts electricity. The positive electrode is the Anode, attracting negatively charged Anions where oxidation occurs as anions lose electrons. The negative electrode is the Cathode, attracting positively charged Cations where reduction occurs as cations gain electrons. Remember the acronym PANIC: Positive Anode, Negative Is Cathode, and OIL RIG: Oxidation Is Loss, Reduction Is Gain of electrons.",
            "vi": "Mục một định nghĩa Điện phân (Electrolysis): là sự phân hủy hợp chất ion ở trạng thái nóng chảy hoặc dung dịch bởi dòng điện một chiều. Chất điện phân (Electrolyte) là chất lỏng chứa các ion tự do chuyển động dẫn điện. Cực dương là Anode, hút các Anion âm về phía nó nơi diễn ra sự oxy hóa (anion nhường electron). Cực âm là Cathode, hút các Cation dương về phía nó nơi diễn ra sự khử (cation nhận electron). Quy tắc ghi nhớ quốc tế: PANIC (Positive Anode, Negative Is Cathode - Cực dương là Anot, Cực âm là Catot) và OIL RIG (Oxidation Is Loss, Reduction Is Gain - Oxy hóa là nhường, Khử là nhận electron)."
        },
        {
            "id": "sec_molten_aqueous",
            "title": "2. Điện phân Nóng chảy vs Điện phân Dung dịch Nước",
            "selector": "#sec-molten-aqueous",
            "en": "Section 2 contrasts molten and aqueous systems: In molten lead(II) bromide, only two ions exist: lead cations reduce at the cathode forming silvery liquid lead metal, while bromide anions oxidize at the anode producing reddish-brown bromine gas fumes. In aqueous solutions, water molecules partially dissociate into hydrogen and hydroxide ions. At the cathode, hydrogen gas discharges unless the metal cation is less reactive than hydrogen, such as copper. At the anode, oxygen gas discharges from hydroxide ions unless concentrated halide ions like chloride, bromide, or iodide are present, discharging halogen gas.",
            "vi": "Mục hai so sánh điện phân nóng chảy và dung dịch: Khi điện phân chì(II) bromua PbBr2 nóng chảy chỉ có 2 loại ion: ion chì Pb2+ bị khử tại catot tạo giọt kim loại chì màu bạc, ion bromua Br- bị oxy hóa tại anot tạo khí brom màu nâu đỏ. Trong dung dịch nước, nước phân ly thêm ion H+ và OH-. Tại catot, khí hydro H2 được ưu tiên giải phóng trừ khi ion kim loại kém hoạt động hơn hydro (như đồng Cu2+). Tại anot, khí oxy O2 được phóng điện từ ion OH- trừ khi có mặt ion halogenua đậm đặc (Cl-, Br-, I-) sẽ ưu tiên tạo khí halogen."
        },
        {
            "id": "sec_electroplating_cells",
            "title": "3. Kỹ thuật Mạ điện & Pin Nhiên liệu Hydro (Fuel Cells)",
            "selector": "#sec-electroplating-cells",
            "en": "Section 3 investigates electrochemical applications: Electroplating coats a metal object with a thin protective or decorative layer of another metal. The object to be plated forms the cathode; the plating metal forms the anode; and the electrolyte contains soluble ions of the plating metal, such as silver nitrate for silver plating spoons. Hydrogen Fuel Cells react hydrogen with oxygen exothermically to produce electricity, with clean water as the sole emission, offering renewable, non-polluting transportation power without greenhouse carbon emissions.",
            "vi": "Mục ba nghiên cứu ứng dụng điện hóa: Mạ điện (Electroplating) phủ một lớp kim loại mỏng lên bề mặt vật dẫn để chống rỉ sét hoặc trang trí. Vật cần mạ luôn được mắc vào cực âm (Cathode); thanh kim loại mạ mắc vào cực dương (Anode); dung dịch điện phân chứa muối tan của kim loại mạ. Pin nhiên liệu Hydro (Hydrogen Fuel Cell) cho khí hydro phản ứng tỏa nhiệt với khí oxy tạo dòng điện, với sản phẩm phụ duy nhất là nước tinh khiết, là nguồn năng lượng tái tạo sạch không phát thải khí nhà kính."
        }
    ]

    major_sections = [
        {"id": "sec_electrolysis_basics", "title": "1. Nguyên lý Cơ bản của Điện phân (PANIC & OIL RIG)"},
        {"id": "sec_molten_aqueous", "title": "2. Điện phân Nóng chảy vs Dung dịch Nước"},
        {"id": "sec_electroplating_cells", "title": "3. Kỹ thuật Mạ điện & Pin Nhiên liệu Hydro"}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print("✅ Topic C4 successfully built!")


# ==============================================================================
# MAIN BATCH 5 RUNNER (TOPICS C1 -> C4)
# ==============================================================================
async def main():
    print("\n*******************************************************")
    print("STARTING CO-ORDINATED SCIENCE BATCH 5: TOPICS C1 -> C4")
    print("*******************************************************\n")
    
    await build_c1()
    await asyncio.sleep(2)
    
    await build_c2()
    await asyncio.sleep(2)
    
    await build_c3()
    await asyncio.sleep(2)
    
    await build_c4()
    
    print("\n*******************************************************")
    print("BATCH 5 COMPLETE: TOPICS C1 -> C4 FINISHED!")
    print("*******************************************************\n")

if __name__ == "__main__":
    asyncio.run(main())
