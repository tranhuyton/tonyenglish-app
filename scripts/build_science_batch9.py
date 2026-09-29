import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC P4: Electricity and magnetism
# ==============================================================================
async def build_p4():
    lid = '2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69'
    code = 'p4'
    title = 'P4: Electricity and magnetism'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-electrical-quantities" class="lecture-interactive-card" data-lecture-section="sec_electrical_quantities" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-electric-circuits" class="lecture-interactive-card" data-lecture-section="sec_electric_circuits" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-electromagnetic-effects" class="lecture-interactive-card" data-lecture-section="sec_electromagnetic_effects" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic P4 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề P4: Điện học & Từ học (Electricity and Magnetism)",
            "selector": "#sec-header",
            "en": "Welcome to Topic P4: Electricity and Magnetism. Modern technology relies entirely on electrical power and electromagnetism. In this lesson, we study electric charges, current, voltage, and Ohm's law, analyze series and parallel circuits including potential dividers, and explore electromagnetic induction, transformers, and electric motors.",
            "vi": "Chào mừng các bạn đến với Chuyên đề P4: Điện học và Từ học. Toàn bộ nền công nghệ hiện đại đều vận hành dựa trên dòng điện và hiện tượng điện từ. Trong bài giảng này, chúng ta sẽ khảo sát điện tích, cường độ dòng điện, hiệu điện thế và định luật Ohm, phân tích mạch nối tiếp và song song gồm cả mạch chia điện thế, đồng thời khám phá hiện tượng cảm ứng điện từ, máy biến áp và động cơ điện."
        },
        {
            "id": "sec_electrical_quantities",
            "title": "1. Đại lượng Điện & Định luật Ohm (Electrical Quantities & Ohm's Law)",
            "selector": "#sec-electrical-quantities",
            "en": "Electric charge Q is measured in Coulombs, with electrons carrying a negative elementary charge. Electric current I is the rate of flow of charge: I equals Q divided by t, measured in Amperes using an ammeter connected in series. Potential difference or voltage V is the energy transferred per unit charge: V equals W divided by Q, measured in Volts using a voltmeter in parallel. Ohm's law states that for an ohmic conductor at constant temperature, current is directly proportional to potential difference: V equals I times R. Electrical resistance R depends on material, length, and cross-sectional area: longer wires have greater resistance, while thicker wires have lower resistance.",
            "vi": "Điện tích Q được đo bằng Cu-lông (Coulomb), với hạt electron mang điện tích nguyên tố âm. Cường độ dòng điện I là tốc độ chuyển dịch của dòng điện tích: I bằng Q chia cho t, đo bằng Ampe kế mắc nối tiếp trong mạch. Hiệu điện thế V là năng lượng được truyền trên mỗi đơn vị điện tích: V bằng W chia Q, đo bằng Vôn kế mắc song song. Định luật Ohm phát biểu rằng với một dây dẫn thuần trở ở nhiệt độ không đổi, dòng điện tỉ lệ thuận với hiệu điện thế: V bằng I nhân R. Điện trở R phụ thuộc vào vật liệu, chiều dài và tiết diện dây dẫn: dây càng dài điện trở càng lớn, dây càng có tiết diện to thì điện trở càng nhỏ."
        },
        {
            "id": "sec_electric_circuits",
            "title": "2. Mạch Điện & Mạch Phân áp (Electric Circuits & Potential Dividers)",
            "selector": "#sec-electric-circuits",
            "en": "In a series circuit, current is identical at all points, while total voltage is shared: V total equals V 1 plus V 2, and total resistance equals R 1 plus R 2. In a parallel circuit, voltage across each parallel branch is identical, current splits between branches, and total combined resistance is less than the resistance of any individual branch. Electrical power is calculated as P equals I times V, and energy transferred equals P times t. A potential divider divides voltage across two resistors in proportion to their resistances. Using sensing components like thermistors or light-dependent resistors allows circuits to respond automatically to changes in temperature or ambient light.",
            "vi": "Trong đoạn mạch nối tiếp, cường độ dòng điện bằng nhau tại mọi điểm, trong khi tổng hiệu điện thế được chia đều: V tổng bằng V 1 cộng V 2, và điện trở tương đương bằng R 1 cộng R 2. Trong đoạn mạch song song, hiệu điện thế qua mỗi nhánh là như nhau, cường độ dòng điện rẽ vào các nhánh, và điện trở tương đương luôn nhỏ hơn điện trở của bất kỳ nhánh riêng rẽ nào. Công suất điện tính bằng P bằng I nhân V, và điện năng tiêu thụ bằng P nhân t. Mạch phân áp chia hiệu điện thế qua hai điện trở tỉ lệ với giá trị điện trở của chúng. Sử dụng các linh kiện cảm biến như nhiệt điện trở thermistor hay quang điện trở LDR giúp mạch tự động điều khiển theo nhiệt độ hoặc ánh sáng môi trường."
        },
        {
            "id": "sec_electromagnetic_effects",
            "title": "3. Tác dụng Điện từ: Cảm ứng Điện từ & Động cơ (Electromagnetic Effects: Induction & Motors)",
            "selector": "#sec-electromagnetic-effects",
            "en": "A magnetic field exerts a force on a current-carrying conductor; Fleming's left-hand rule determines the direction of motion, field, and current, forming the basis of the DC electric motor. Conversely, electromagnetic induction occurs when a conductor cuts magnetic field lines or when magnetic flux changes, inducing an electromotive force. Transformers consist of two insulated coils wound around a soft iron core. Transformers step alternating voltages up or down according to the turns ratio: V p over V s equals N p over N s. Stepping up voltage for long-distance grid transmission minimizes current, drastically reducing power loss caused by resistance heating in power lines.",
            "vi": "Từ trường tác dụng lực lên một dây dẫn mang dòng điện đặt trong nó; quy tắc bàn tay trái Fleming giúp xác định chiều của lực từ, đường sức từ và dòng điện, tạo nền tảng vận hành của động cơ điện một chiều. Ngược lại, hiện tượng cảm ứng điện từ xảy ra khi một dây dẫn cắt các đường sức từ hoặc khi từ thông biến thiên, sinh ra một suất điện động cảm ứng. Máy biến áp gồm hai cuộn dây cách điện quấn quanh lõi sắt non. Máy biến áp biến đổi hiệu điện thế xoay chiều theo tỉ số vòng dây: V sơ cấp chia V thứ cấp bằng N sơ cấp chia N thứ cấp. Tăng thế khi truyền tải điện năng đi xa giúp giảm tối đa cường độ dòng điện, từ đó triệt tiêu sự hao phí điện năng do tỏa nhiệt trên đường dây."
        }
    ]

    major_sections = [
        {"title": "Giới thiệu P4", "start": 0.0},
        {"title": "1. Đại lượng Điện & Định luật Ohm", "start": 0.0},
        {"title": "2. Mạch Điện & Mạch Phân áp", "start": 0.0},
        {"title": "3. Cảm ứng Điện từ & Động cơ", "start": 0.0}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences (0654)", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print(f"Completed Topic {code.upper()}!")

# ==============================================================================
# TOPIC P5: Nuclear physics
# ==============================================================================
async def build_p5():
    lid = 'a6077865-db01-4785-9ec7-e8b0f531fcdc'
    code = 'p5'
    title = 'P5: Nuclear physics'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-atomic-model" class="lecture-interactive-card" data-lecture-section="sec_atomic_model" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-radioactivity" class="lecture-interactive-card" data-lecture-section="sec_radioactivity" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-decay-halflife" class="lecture-interactive-card" data-lecture-section="sec_decay_halflife" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-uses-safety" class="lecture-interactive-card" data-lecture-section="sec_uses_safety" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic P5 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề P5: Vật lý Hạt nhân (Nuclear Physics)",
            "selector": "#sec-header",
            "en": "Welcome to Topic P5: Nuclear Physics. Deep within the core of every atom lies the nucleus, a dense source of tremendous energy and fundamental radiation. In this lesson, we study the Rutherford nuclear model and isotopes, examine the ionizing and penetrating properties of alpha, beta, and gamma radiation, master nuclear decay equations and half-life calculations, and explore industrial uses, medical applications, and radiation safety.",
            "vi": "Chào mừng các bạn đến với Chuyên đề P5: Vật lý Hạt nhân. Nằm sâu tại trung tâm của mỗi nguyên tử là hạt nhân, nguồn chứa năng lượng khổng lồ và các loại bức xạ cơ bản. Trong bài học này, chúng ta sẽ khảo sát mô hình hạt nhân Rutherford và đồng vị phóng xạ, nghiên cứu khả năng ion hóa và đâm xuyên của bức xạ alpha, beta và gamma, làm chủ phương trình phân rã phóng xạ cùng phép tính chu kỳ bán rã, và tìm hiểu các ứng dụng y tế, công nghiệp cũng như quy tắc an toàn bức xạ."
        },
        {
            "id": "sec_atomic_model",
            "title": "1. Mô hình Hạt nhân của Nguyên tử & Đồng vị (The Nuclear Model & Isotopes)",
            "selector": "#sec-atomic-model",
            "en": "The Rutherford alpha scattering experiment proved that the atom is mostly empty space, with virtually all its mass and positive charge concentrated in a tiny central nucleus. The nucleus contains positive protons and uncharged neutrons, collectively called nucleons. Around the nucleus orbit negative electrons. The atomic or proton number Z defines the chemical element. The nucleon or mass number A is the total number of protons plus neutrons. Isotopes are atoms of the same element having the same number of protons but different numbers of neutrons.",
            "vi": "Thí nghiệm tán xạ hạt alpha của Rutherford đã chứng minh rằng nguyên tử hầu như là khoảng không rỗng, với hầu hết khối lượng và toàn bộ điện tích dương tập trung tại hạt nhân tí hon ở tâm. Hạt nhân gồm các proton mang điện tích dương và các neutron không mang điện, gọi chung là các nuclôn. Chuyển động xung quanh hạt nhân là các electron mang điện tích âm. Số hiệu nguyên tử Z là số proton quyết định nguyên tố hóa học. Số khối A là tổng số proton và neutron. Đồng vị là các nguyên tử của cùng một nguyên tố có cùng số proton nhưng khác nhau về số neutron."
        },
        {
            "id": "sec_radioactivity",
            "title": "2. Hiện tượng Phóng xạ & Khả năng Đâm xuyên (Radioactivity & Penetration Properties)",
            "selector": "#sec-radioactivity",
            "en": "Unstable atomic nuclei undergo spontaneous and random radioactive decay by emitting radiation to achieve stability. Alpha particles are helium nuclei with two protons and two neutrons: they carry a plus two charge, have the highest ionizing power, but possess the weakest penetrating power, stopped by a single sheet of paper or a few centimeters of air. Beta particles are high-speed electrons emitted when a neutron turns into a proton: they carry a minus one charge, have moderate ionizing power, and are stopped by a few millimeters of aluminum. Gamma rays are high-frequency electromagnetic waves with zero charge and zero mass: they have the weakest ionizing power but extreme penetration, requiring thick lead or concrete to absorb.",
            "vi": "Các hạt nhân không bền vững trải qua quá trình phân rã phóng xạ tự phát và ngẫu nhiên bằng cách phát ra bức xạ để đạt cấu hình bền. Hạt alpha là hạt nhân heli gồm hai proton và hai neutron: mang điện tích dương hai, có khả năng ion hóa mạnh nhất, nhưng khả năng đâm xuyên yếu nhất, bị chặn lại bởi một tờ giấy mỏng hoặc vài xentimét không khí. Hạt beta là các electron tốc độ cao phóng ra khi neutron biến thành proton: mang điện tích âm một, khả năng ion hóa trung bình, và bị chặn bởi vài milimét nhôm. Tia gamma là sóng điện từ tần số rất cao, không mang điện và không có khối lượng: có khả năng ion hóa yếu nhất nhưng khả năng đâm xuyên cực mạnh, đòi hỏi các khối chì dày hoặc tường bê tông dày để ngăn chặn."
        },
        {
            "id": "sec_decay_halflife",
            "title": "3. Phương trình Phân rã & Chu kỳ Bán rã (Decay Equations & Half-Life)",
            "selector": "#sec-decay-halflife",
            "en": "In nuclear decay equations, total nucleon number and total proton number must balance on both sides. In alpha decay, nucleon number decreases by four and proton number decreases by two. In beta decay, nucleon number remains unchanged while proton number increases by one. Half-life is defined as the time taken for half the radioactive nuclei in a sample to decay, or the time taken for the activity to halve. Radioactive decay is completely unaffected by temperature, pressure, or chemical bonding. Always subtract background radiation before calculating corrected count rates from detector data.",
            "vi": "Trong phương trình phân rã phóng xạ, tổng số khối và tổng số proton ở hai vế luôn luôn bảo toàn. Trong phân rã alpha, số khối giảm 4 đơn vị và số proton giảm 2 đơn vị. Trong phân rã beta, số khối giữ nguyên không đổi trong khi số proton tăng thêm 1 đơn vị. Chu kỳ bán rã được định nghĩa là thời gian để một nửa số hạt nhân phóng xạ ban đầu bị phân rã, hoặc thời gian để độ phóng xạ giảm đi một nửa. Quá trình phân rã phóng xạ hoàn toàn không bị ảnh hưởng bởi nhiệt độ, áp suất hay liên kết hóa học. Cần luôn trừ bức xạ nền tự nhiên trước khi tính tốc độ đếm thực từ dữ liệu máy đếm bức xạ."
        },
        {
            "id": "sec_uses_safety",
            "title": "4. Ứng dụng Thực tiễn & An toàn Bức xạ (Practical Uses & Safety Precautions)",
            "selector": "#sec-uses-safety",
            "en": "Radioactive isotopes have vital applications. Americium-241, an alpha emitter, is used in domestic smoke detectors. Beta emitters like strontium-90 monitor paper and metal foil thickness in factories. Gamma emitters like cobalt-60 sterilize medical equipment and treat cancerous tumors. Technetium-99m serves as a medical tracer because of its short six-hour half-life. Ionizing radiation damages living cell DNA, causing cell death or cancerous mutations. Safety precautions include using lead-lined shielding, handling radioactive sources with tongs, increasing distance, and minimizing exposure time.",
            "vi": "Các đồng vị phóng xạ có nhiều ứng dụng quan trọng. Americium-241 phát hạt alpha dùng trong đầu báo khói gia đình. Nguồn phát hạt beta như stronti-90 giúp kiểm soát độ dày giấy và màng kim loại trong nhà máy tự động. Nguồn phát tia gamma như coban-60 khử trùng dụng cụ y tế và tiêu diệt tế bào ung thư trong xạ trị. Techneti-99m được dùng làm chất đánh dấu y học nhờ chu kỳ bán rã ngắn chỉ 6 giờ. Bức xạ ion hóa phá hủy cấu trúc DNA trong tế bào sống, gây chết tế bào hoặc đột biến gây ung thư. Quy tắc an toàn bao gồm sử dụng tấm chắn chì bảo vệ, gắp mẫu phóng xạ bằng kẹp dài, giữ khoảng cách xa và giảm tối thiểu thời gian phơi nhiễm."
        }
    ]

    major_sections = [
        {"title": "Giới thiệu P5", "start": 0.0},
        {"title": "1. Mô hình Hạt nhân & Đồng vị", "start": 0.0},
        {"title": "2. Hiện tượng Phóng xạ", "start": 0.0},
        {"title": "3. Phân rã & Chu kỳ Bán rã", "start": 0.0},
        {"title": "4. Ứng dụng & An toàn Bức xạ", "start": 0.0}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences (0654)", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print(f"Completed Topic {code.upper()}!")

# ==============================================================================
# TOPIC P6: Space physics
# ==============================================================================
async def build_p6():
    lid = 'd11f8920-fe86-4cd4-ad9a-e8b669bc687b'
    code = 'p6'
    title = 'P6: Space physics'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-earth-solar-system" class="lecture-interactive-card" data-lecture-section="sec_earth_solar_system" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-orbital-motion" class="lecture-interactive-card" data-lecture-section="sec_orbital_motion" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-stars-universe" class="lecture-interactive-card" data-lecture-section="sec_stars_universe" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic P6 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề P6: Vật lý Không gian & Vũ trụ (Space Physics)",
            "selector": "#sec-header",
            "en": "Welcome to Topic P6: Space Physics, the final chapter of IGCSE Physics. In this inspiring module, we journey across the cosmos. We study Earth's rotation, seasons, and the architecture of the Solar System, calculate orbital speed and analyze gravitational fields, and explore stellar life cycles, nuclear fusion in stars, the expanding universe, and the Big Bang theory.",
            "vi": "Chào mừng các bạn đến với Chuyên đề P6: Vật lý Vũ trụ và Không gian, chương cuối cùng của Vật lý IGCSE. Trong bài học này, chúng ta sẽ bắt đầu chuyến hành trình khám phá vũ trụ bao la. Chúng ta sẽ nghiên cứu sự tự quay của Trái Đất, các mùa trong năm và cấu trúc Hệ Mặt Trời, tính tốc độ quỹ đạo và phân tích lực hấp dẫn, đồng thời tìm hiểu vòng đời của các vì sao, phản ứng nhiệt hạch, sự giãn nở của vũ trụ và thuyết Vụ nổ lớn Big Bang."
        },
        {
            "id": "sec_earth_solar_system",
            "title": "1. Trái Đất & Hệ Mặt Trời (The Earth & The Solar System)",
            "selector": "#sec-earth-solar-system",
            "en": "The Earth rotates on its tilted axis every 24 hours, causing the diurnal cycle of day and night. Earth orbits the Sun once every 365.25 days. The 23.5 degree tilt of Earth's rotational axis explains the changing seasons: when a hemisphere is tilted towards the Sun, solar rays strike the surface more directly and daylight hours are longer, creating summer. The Solar System consists of the central Sun, eight planets, dwarf planets, moons, asteroids, and comets. The four inner rocky planets are Mercury, Venus, Earth, and Mars. The four outer gas and ice giants are Jupiter, Saturn, Uranus, and Neptune.",
            "vi": "Trái Đất tự quay quanh trục nghiêng của mình một vòng mất 24 giờ, tạo nên chu kỳ ngày và đêm luân phiên. Trái Đất quay quanh Mặt Trời một chu kỳ mất 365,25 ngày. Độ nghiêng 23,5 độ của trục Trái Đất giải thích sự thay đổi các mùa trong năm: khi một bán cầu nghiêng về phía Mặt Trời, các tia nắng chiếu thẳng góc hơn và thời gian ban ngày dài hơn, tạo nên mùa hè. Hệ Mặt Trời gồm Mặt Trời ở trung tâm, 8 hành tinh, các hành tinh lùn, vệ tinh tự nhiên, tiểu hành tinh và sao chổi. Bốn hành tinh đất đá bên trong là Thủy tinh, Kim tinh, Trái Đất và Hỏa tinh. Bốn hành tinh khí và băng khổng lồ bên ngoài là Mộc tinh, Thổ tinh, Thiên Vương tinh và Hải Vương tinh."
        },
        {
            "id": "sec_orbital_motion",
            "title": "2. Tốc độ Quỹ đạo & Lực Hấp dẫn (Orbital Speed & Gravitational Force)",
            "selector": "#sec-orbital-motion",
            "en": "Planets, moons, and satellites travel in roughly circular or elliptical orbits held in place by gravitational attraction. Gravitational force acts as the centripetal force directed toward the center of the orbit. For a circular orbit of radius r and orbital period T, the distance travelled in one orbit is the circumference two pi r. Therefore, orbital speed v equals two pi r divided by T. As orbital radius increases, gravitational field strength decreases; consequently, more distant planets travel at significantly lower orbital speeds and have much longer orbital periods.",
            "vi": "Các hành tinh, mặt trăng và vệ tinh chuyển động theo quỹ đạo tròn hoặc elip nhờ lực hút hấp dẫn. Lực hấp dẫn đóng vai trò là lực hướng tâm hướng về tâm quỹ đạo. Đối với một quỹ đạo tròn bán kính r và chu kỳ quỹ đạo T, quãng đường đi được trong một chu kỳ là chu vi hình tròn 2 pi r. Do đó, tốc độ quỹ đạo v bằng 2 pi r chia cho T. Khi bán kính quỹ đạo tăng lên, cường độ trường hấp dẫn giảm dần; kết quả là các hành tinh càng ở xa Mặt Trời thì chuyển động với tốc độ quỹ đạo càng chậm và chu kỳ quay quanh Mặt Trời càng kéo dài."
        },
        {
            "id": "sec_stars_universe",
            "title": "3. Các Vì sao & Sự Giãn nở của Vũ trụ (Stars & The Universe)",
            "selector": "#sec-stars-universe",
            "en": "Stars form from giant nebulae of gas and dust collapsing under gravity. In the core of a star, intense pressure and temperature trigger nuclear fusion, fusing hydrogen into helium and releasing immense energy. For billions of years, a main sequence star remains stable as outward radiation pressure balances inward gravitational collapse. Lower-mass stars expand into red giants, shed outer layers as planetary nebulae, and cool into white dwarfs. Massive stars expand into red supergiants, explode in cataclysmic supernovae, and leave behind neutron stars or black holes. Light from distant galaxies exhibits redshift, showing that galaxies are moving away from us and that the universe has been expanding since the Big Bang approximately 13.8 billion years ago.",
            "vi": "Các ngôi sao được hình thành từ các đám mây tinh vân khổng lồ gồm khí và bụi sụp đổ dưới tác dụng của lực hấp dẫn. Tại lõi của ngôi sao, áp suất và nhiệt độ cực cao kích hoạt phản ứng nhiệt hạch, kết hợp các hạt nhân hydro thành heli và giải phóng nguồn năng lượng khổng lồ. Trong hàng tỷ năm, một ngôi sao trong dãy chính duy trì ổn định nhờ áp suất bức xạ hướng ra ngoài cân bằng chính xác với lực nén hấp dẫn hướng vào trong. Các ngôi sao khối lượng nhỏ nở rộng thành sao khổng lồ đỏ, thổi bay lớp vỏ ngoài thành tinh vân hành tinh và co lại thành sao lùn trắng nguội dần. Các ngôi sao khối lượng cực lớn trở thành sao siêu khổng lồ đỏ, nổ tung trong vụ nổ siêu tân tinh dữ dội, để lại sao neutron hoặc lỗ đen. Ánh sáng từ các thiên hà xa xôi cho thấy hiện tượng dịch chuyển đỏ, chứng minh các thiên hà đang rời xa chúng ta và toàn bộ vũ trụ đang không ngừng giãn nở kể từ Vụ nổ lớn Big Bang khoảng 13,8 tỷ năm trước."
        }
    ]

    major_sections = [
        {"title": "Giới thiệu P6", "start": 0.0},
        {"title": "1. Trái Đất & Hệ Mặt Trời", "start": 0.0},
        {"title": "2. Tốc độ Quỹ đạo & Lực Hấp dẫn", "start": 0.0},
        {"title": "3. Các Vì sao & Vũ trụ", "start": 0.0}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences (0654)", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print(f"Completed Topic {code.upper()}!")

# ==============================================================================
# MAIN RUNNER
# ==============================================================================
async def main():
    print("Starting Batch 9: P4, P5, P6...")
    await build_p4()
    await build_p5()
    await build_p6()
    print("\nALL TOPICS IN BATCH 9 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
