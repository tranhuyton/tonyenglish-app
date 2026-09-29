import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page, sb

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# TOPIC P1: Motion, forces & energy
# ==============================================================================
async def build_p1():
    lid = '690ff013-5d01-4c1e-8546-25b3cd056e64'
    code = 'p1'
    title = 'P1: Motion, forces & energy'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-quantities" class="lecture-interactive-card" data-lecture-section="sec_quantities" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-kinematics" class="lecture-interactive-card" data-lecture-section="sec_kinematics" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-density" class="lecture-interactive-card" data-lecture-section="sec_density" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-forces" class="lecture-interactive-card" data-lecture-section="sec_forces" style="cursor: pointer; ')
    
    t_h2_4 = h2s[4]
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-energy-stores" class="lecture-interactive-card" data-lecture-section="sec_energy_stores" style="cursor: pointer; ')
    
    t_h2_5 = h2s[5]
    r_h2_5 = t_h2_5.replace('<h2', '<h2 id="sec-ke-gpe" class="lecture-interactive-card" data-lecture-section="sec_ke_gpe" style="cursor: pointer; ')
    
    t_h2_6 = h2s[6]
    r_h2_6 = t_h2_6.replace('<h2', '<h2 id="sec-work-power" class="lecture-interactive-card" data-lecture-section="sec_work_power" style="cursor: pointer; ')
    
    t_h2_7 = h2s[7]
    r_h2_7 = t_h2_7.replace('<h2', '<h2 id="sec-energy-resources" class="lecture-interactive-card" data-lecture-section="sec_energy_resources" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)\
                   .replace(t_h2_5, r_h2_5, 1)\
                   .replace(t_h2_6, r_h2_6, 1)\
                   .replace(t_h2_7, r_h2_7, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic P1 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề P1: Chuyển động, Lực & Năng lượng",
            "selector": "#sec-header",
            "en": "Welcome to Topic P1: Motion, Forces and Energy, the foundational pillar of IGCSE Physics. In this comprehensive module, we study physical measurement techniques, analyze motion and kinematics graphs, master density and Newton's laws of force, explore Hooke's law, and examine energy stores, kinetic and gravitational potential energy, work, power, and global energy resources.",
            "vi": "Chào mừng các bạn đến với Chuyên đề P1: Chuyển động, Lực và Năng lượng, trụ cột nền tảng của Vật lý IGCSE. Trong bài giảng này, chúng ta sẽ khảo sát các phương pháp đo lường đại lượng vật lý, phân tích đồ thị chuyển động, làm chủ khối lượng riêng và các định luật Newton về lực, định luật Hooke, cùng các dạng dự trữ năng lượng, thế năng trọng trường, công, công suất và các nguồn tài nguyên năng lượng."
        },
        {
            "id": "sec_quantities",
            "title": "1. Đại lượng Vật lý & Phương pháp Đo lường (Physical Quantities & Measurement)",
            "selector": "#sec-quantities",
            "en": "Physical quantities are divided into scalars and vectors. Scalars have magnitude only, such as mass, distance, speed, and time. Vectors have both magnitude and direction, such as weight, displacement, velocity, and force. To measure lengths accurately, we use a ruler for millimeters, vernier calipers for inner and outer diameters down to 0.1 millimeters, and a micrometer screw gauge for fine wires down to 0.01 millimeters. Time is measured using digital stopwatches, often taking multiple oscillations of a pendulum and dividing by the count to reduce human reaction error.",
            "vi": "Đại lượng vật lý được chia thành đại lượng vô hướng và đại lượng có hướng (vectơ). Đại lượng vô hướng chỉ có độ lớn, ví dụ như khối lượng, quãng đường, tốc độ và thời gian. Đại lượng vectơ vừa có độ lớn vừa có hướng, ví dụ như trọng lượng, độ dịch chuyển, vận tốc và lực. Để đo chiều dài chính xác, ta dùng thước kẻ cho milimét, thước cặp kẹp đường kính trong và ngoài chính xác đến 0,1 milimét, và thước pan-me đo dây mảnh đến 0,01 milimét. Thời gian đo bằng đồng hồ bấm giây, thường đo nhiều chu kỳ dao động của con lắc rồi chia ra để triệt tiêu sai số phản xạ con người."
        },
        {
            "id": "sec_kinematics",
            "title": "2. Động học & Phân tích Đồ thị Chuyển động (Motion & Kinematics Graphs)",
            "selector": "#sec-kinematics",
            "en": "Speed is defined as distance divided by time, whereas acceleration is the rate of change of velocity: delta v divided by delta t. On a distance-time graph, the gradient represents speed, and a horizontal line represents a stationary object. On a speed-time graph, the gradient represents acceleration, a horizontal line represents constant speed, and crucially, the area under the line represents the total distance travelled. When falling under gravity, air resistance increases with speed until it equals weight, resulting in zero resultant force and constant terminal velocity.",
            "vi": "Tốc độ được định nghĩa bằng quãng đường chia thời gian, còn gia tốc là tốc độ thay đổi của vận tốc: delta v chia delta t. Trên đồ thị quãng đường - thời gian, độ dốc biểu diễn tốc độ, và đường nằm ngang biểu thị vật đứng yên. Trên đồ thị vận tốc - thời gian, độ dốc biểu diễn gia tốc, đường nằm ngang biểu diễn vận tốc không đổi, và đặc biệt diện tích dưới đường đồ thị biểu diễn tổng quãng đường đi được. Khi rơi tự do dưới trọng lực, lực cản không khí tăng theo tốc độ cho đến khi cân bằng với trọng lượng, tạo ra hợp lực bằng không và vật đạt vận tốc giới hạn không đổi."
        },
        {
            "id": "sec_density",
            "title": "3. Khối lượng, Trọng lượng & Khối lượng riêng (Mass, Weight & Density)",
            "selector": "#sec-density",
            "en": "Mass is the measure of the quantity of matter in an object, measured in kilograms, and remains unchanged anywhere in the universe. Weight is the gravitational force acting on that mass: W equals m times g, where gravitational field strength g is approximately 9.8 Newtons per kilogram on Earth. Density is mass per unit volume: rho equals m divided by V. For regular solids, volume is calculated from dimensions. For irregular objects, we submerge them in water in a measuring cylinder; the volume of displaced liquid equals the volume of the object.",
            "vi": "Khối lượng là thước đo lượng chất chứa trong một vật, đo bằng kilôgam, và không thay đổi ở bất kỳ nơi nào trong vũ trụ. Trọng lượng là lực hấp dẫn tác dụng lên khối lượng đó: W bằng m nhân g, trong đó cường độ trường hấp dẫn g xấp xỉ 9,8 Newton trên kilôgam trên Trái Đất. Khối lượng riêng là khối lượng trên một đơn vị thể tích: rho bằng m chia V. Với vật rắn thông thường, thể tích tính từ kích thước hình học. Với vật rắn không đều, ta nhúng ngập vào ống đong chứa nước; thể tích nước dâng lên đúng bằng thể tích của vật."
        },
        {
            "id": "sec_forces",
            "title": "4. Lực, Định luật Hooke, Mômen & Áp suất (Forces, Hooke's Law, Moments & Pressure)",
            "selector": "#sec-forces",
            "en": "Forces can change the size, shape, and motion of a body. According to Newton's second law, resultant force F equals mass times acceleration: F equals m a. Hooke's law states that extension is directly proportional to force applied: F equals k x, up to the limit of proportionality. The moment of a force is its turning effect: moment equals force times perpendicular distance from the pivot. For an object in rotational equilibrium, total clockwise moments equal total anticlockwise moments. Pressure is force applied per unit area: P equals F divided by A, measured in Pascals.",
            "vi": "Lực có thể làm thay đổi kích thước, hình dạng và chuyển động của vật. Theo định luật II Newton, hợp lực F bằng khối lượng nhân gia tốc: F bằng m nhân a. Định luật Hooke phát biểu rằng độ biến dạng tỉ lệ thuận với lực tác dụng: F bằng k x, cho đến giới hạn đàn hồi. Mômen lực là tác dụng làm quay: mômen bằng lực nhân khoảng cách vuông góc từ trục quay. Khi một vật ở trạng thái cân bằng quay, tổng mômen cùng chiều kim đồng hồ bằng tổng mômen ngược chiều. Áp suất là lực tác dụng vuông góc trên một đơn vị diện tích: P bằng F chia A, đo bằng Pascal."
        },
        {
            "id": "sec_energy_stores",
            "title": "5. Các Dạng Dự trữ Năng lượng & Đường truyền (Energy Stores & Transfer Pathways)",
            "selector": "#sec-energy-stores",
            "en": "The principle of conservation of energy states that energy cannot be created or destroyed, only transferred from one store to another. The primary energy stores include kinetic, gravitational potential, chemical, elastic, nuclear, thermal, electrostatic, and magnetic stores. Energy transfers between these stores via four main pathways: mechanically by forces doing work, electrically by moving charges, by heating through temperature differences, and by radiation through light or sound waves.",
            "vi": "Định luật bảo toàn năng lượng khẳng định năng lượng không thể tự sinh ra hay tự mất đi, mà chỉ chuyển hóa từ dạng này sang dạng khác. Các dạng dự trữ năng lượng chính bao gồm: động năng, thế năng hấp dẫn, hóa năng, thế năng đàn hồi, năng lượng hạt nhân, nhiệt năng, năng lượng tĩnh điện và từ trường. Năng lượng được truyền giữa các kho chứa qua bốn con đường chính: cơ học do lực sinh công, điện học do dòng điện di chuyển, truyền nhiệt do chênh lệch nhiệt độ, và bức xạ qua sóng ánh sáng hoặc âm thanh."
        },
        {
            "id": "sec_ke_gpe",
            "title": "6. Động năng & Thế năng Trọng trường (Kinetic & Gravitational Potential Energy)",
            "selector": "#sec-ke-gpe",
            "en": "Kinetic energy is the energy of a moving object, given by the formula E k equals half m v squared, where m is mass in kilograms and v is speed in meters per second. Notice that doubling speed quadruples kinetic energy. Gravitational potential energy is energy stored due to height in a gravitational field: Delta E p equals m g Delta h, where h is vertical height change. In ideal situations without friction, loss of gravitational potential energy equals gain in kinetic energy, as seen in rollercoasters and falling pendulums.",
            "vi": "Động năng là năng lượng của một vật chuyển động, được tính bằng công thức E k bằng một nửa m v bình phương, trong đó m là khối lượng tính bằng kg và v là vận tốc tính bằng mét trên giây. Lưu ý rằng khi vận tốc tăng gấp đôi thì động năng tăng gấp bốn lần. Thế năng hấp dẫn là năng lượng dự trữ do độ cao trong trường trọng lực: Delta E p bằng m g Delta h, với h là độ cao thẳng đứng. Trong điều kiện lý tưởng không có ma sát, độ giảm thế năng trọng trường chuyển hóa hoàn toàn thành độ tăng động năng, như trong tàu lượn siêu tốc và con lắc đơn."
        },
        {
            "id": "sec_work_power",
            "title": "7. Công cơ học, Công suất & Hiệu suất (Work, Power & Efficiency)",
            "selector": "#sec-work-power",
            "en": "Work is done when a force moves an object through a distance in the direction of the force: W equals F times d, measured in Joules. Power is the rate of doing work or transferring energy: P equals W divided by t, measured in Watts or Joules per second. No mechanical system is 100 percent efficient because energy is dissipated as thermal energy due to friction. Percentage efficiency equals useful energy output divided by total energy input, multiplied by 100 percent.",
            "vi": "Công cơ học được sinh ra khi một lực làm vật dịch chuyển một quãng đường theo phương của lực: W bằng F nhân d, đo bằng Jun. Công suất là tốc độ thực hiện công hay tốc độ truyền năng lượng: P bằng W chia cho t, đo bằng Oát (Watt) hoặc Jun trên giây. Không có hệ cơ học nào đạt hiệu suất 100% vì năng lượng luôn bị tiêu hao thành nhiệt năng do ma sát. Hiệu suất phần trăm bằng năng lượng đầu ra có ích chia cho tổng năng lượng đầu vào, nhân với 100%."
        },
        {
            "id": "sec_energy_resources",
            "title": "8. Đánh giá So sánh Nguồn Tài nguyên Năng lượng (Energy Resources Comparison)",
            "selector": "#sec-energy-resources",
            "en": "Global energy resources are categorized into non-renewable and renewable sources. Non-renewable resources like coal, oil, natural gas, and uranium are finite, reliable, but emit greenhouse gases or create hazardous radioactive waste. Renewable resources like solar, wind, hydroelectric, tidal, and geothermal energy are replenished naturally and produce zero carbon emissions during operation. However, wind and solar are weather-dependent and intermittent, requiring large land areas and energy storage systems to maintain grid stability.",
            "vi": "Các nguồn tài nguyên năng lượng trên thế giới được chia thành nguồn không tái tạo và nguồn tái tạo. Nguồn không tái tạo như than đá, dầu mỏ, khí tự nhiên và uranium là hữu hạn, độ tin cậy cung cấp cao, nhưng phát thải khí nhà kính hoặc tạo chất thải phóng xạ nguy hại. Các nguồn tái tạo như năng lượng mặt trời, gió, thủy điện, thủy triều và địa nhiệt được bổ sung tự nhiên và không phát thải carbon khi vận hành. Tuy nhiên, điện gió và điện mặt trời phụ thuộc vào thời tiết và gián đoạn, đòi hỏi diện tích lớn và hệ thống lưu trữ điện để duy trì ổn định lưới điện."
        }
    ]

    major_sections = [
        {"title": "Giới thiệu P1", "start": 0.0},
        {"title": "1. Đại lượng & Đo lường", "start": 0.0},
        {"title": "2. Động học & Đồ thị", "start": 0.0},
        {"title": "3. Khối lượng & Khối lượng riêng", "start": 0.0},
        {"title": "4. Lực, Hooke & Áp suất", "start": 0.0},
        {"title": "5. Dạng Năng lượng", "start": 0.0},
        {"title": "6. Động năng & Thế năng", "start": 0.0},
        {"title": "7. Công, Công suất & Hiệu suất", "start": 0.0},
        {"title": "8. Nguồn Tài nguyên Năng lượng", "start": 0.0}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences (0654)", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print(f"Completed Topic {code.upper()}!")

# ==============================================================================
# TOPIC P2: Thermal physics
# ==============================================================================
async def build_p2():
    lid = 'dc33ed9d-e328-4f60-8c47-f0dbd103e8c1'
    code = 'p2'
    title = 'P2: Thermal physics'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-kinetic-model" class="lecture-interactive-card" data-lecture-section="sec_kinetic_model" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-expansion" class="lecture-interactive-card" data-lecture-section="sec_expansion" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-heat-transfer" class="lecture-interactive-card" data-lecture-section="sec_heat_transfer" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic P2 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề P2: Nhiệt học (Thermal Physics)",
            "selector": "#sec-header",
            "en": "Welcome to Topic P2: Thermal Physics. Heat energy governs the physical states of all matter in our universe. In this lesson, we study the kinetic particle model of matter and Brownian motion, investigate thermal expansion and the cooling mechanism of evaporation, and master the three fundamental mechanisms of heat transfer: conduction, convection, and thermal radiation.",
            "vi": "Chào mừng các bạn đến với Chuyên đề P2: Vật lý Nhiệt học. Nhiệt năng chi phối mọi trạng thái tồn tại của vật chất trong vũ trụ. Trong bài học này, chúng ta sẽ khảo sát mô hình động học hạt và chuyển động Brown, tìm hiểu hiện tượng giãn nở nhiệt và cơ chế làm mát của sự bay hơi, đồng thời làm chủ ba cơ chế truyền nhiệt cơ bản: dẫn nhiệt, đối lưu và bức xạ nhiệt."
        },
        {
            "id": "sec_kinetic_model",
            "title": "1. Mô hình Động học Hạt của Vật chất (Kinetic Particle Model of Matter)",
            "selector": "#sec-kinetic-model",
            "en": "Matter exists in solids, liquids, and gases. In solids, particles are tightly packed in regular lattice arrangements, vibrating about fixed positions. In liquids, particles are close together but arranged irregularly, sliding past one another. In gases, particles are spaced widely apart, moving rapidly and randomly in straight lines until they collide. Brownian motion, observed when smoke particles in air or pollen grains in water exhibit zig-zag motion, provides direct experimental evidence that unseen fluid molecules are moving randomly at high speeds. Gas pressure is caused by gas particles colliding with the container walls.",
            "vi": "Vật chất tồn tại ở thể rắn, lỏng và khí. Ở thể rắn, các hạt liên kết chặt chẽ trong mạng tinh thể trật tự, dao động quanh vị trí cân bằng cố định. Ở thể lỏng, các hạt ở gần nhau nhưng xếp ngẫu nhiên, trượt tự do qua nhau. Ở thể khí, các hạt cách nhau rất xa, chuyển động nhanh và hỗn loạn theo đường thẳng cho đến khi va chạm. Chuyển động Brown, quan sát được khi các hạt khói trong không khí hay hạt phấn hoa trong nước chuyển động zíc-zắc, là bằng chứng thực nghiệm trực tiếp chứng minh các phân tử môi trường đang chuyển động ngẫu nhiên với vận tốc lớn. Áp suất chất khí sinh ra do các hạt khí va đập vào thành bình chứa."
        },
        {
            "id": "sec_expansion",
            "title": "2. Sự Giãn nở Nhiệt & Cơ chế Bay hơi (Thermal Expansion & Evaporation)",
            "selector": "#sec-expansion",
            "en": "When substances absorb thermal energy, their particles vibrate or move faster, pushing slightly further apart. This causes thermal expansion. Gases expand significantly more than liquids, which expand more than solids. This expansion is utilized in liquid-in-glass thermometers and bimetallic strips. Evaporation occurs at any temperature below the boiling point, exclusively at the surface of a liquid. The fastest, most energetic molecules overcome intermolecular attractive forces and escape into the gas phase. Because the highest energy particles leave, the average kinetic energy of the remaining liquid decreases, causing a cooling effect.",
            "vi": "Khi hấp thụ nhiệt năng, các hạt chuyển động hoặc dao động nhanh hơn, đẩy nhau ra xa hơn một chút. Hiện tượng này gây ra sự giãn nở vì nhiệt. Chất khí giãn nở nhiều hơn chất lỏng, và chất lỏng giãn nở nhiều hơn chất rắn. Sự giãn nở nhiệt được ứng dụng trong nhiệt kế thủy ngân và băng kép cảm biến nhiệt. Sự bay hơi diễn ra ở mọi nhiệt độ dưới điểm sôi, chỉ xảy ra tại bề mặt chất lỏng. Những phân tử có động năng lớn nhất sẽ thắng lực hút liên phân tử để thoát ra ngoài không khí. Do các phân tử năng lượng cao nhất đã thoát đi, động năng trung bình của phần chất lỏng còn lại giảm xuống, tạo ra hiệu ứng làm mát."
        },
        {
            "id": "sec_heat_transfer",
            "title": "3. Các Cơ chế Truyền Nhiệt: Dẫn nhiệt, Đối lưu & Bức xạ (Thermal Energy Transfers)",
            "selector": "#sec-heat-transfer",
            "en": "Thermal energy transfers from hot regions to cooler regions through three processes. Conduction occurs mainly in solids; vibrating lattice ions transfer energy to neighboring ions. In metals, delocalized free electrons diffuse rapidly through the structure, making metals excellent thermal conductors. Convection occurs only in fluids: heated fluid expands, becomes less dense, and rises, while cooler, denser fluid sinks, forming a continuous convection current. Radiation transfers energy via infrared electromagnetic waves and can travel through a vacuum. Dull, black surfaces are the best absorbers and emitters of thermal radiation, whereas shiny, white surfaces are the best reflectors.",
            "vi": "Nhiệt năng truyền từ nơi nóng sang nơi lạnh qua ba quá trình. Dẫn nhiệt xảy ra chủ yếu trong chất rắn; các ion dao động truyền động năng cho các ion kế bên. Trong kim loại, các electron tự do khuếch tán nhanh khắp cấu trúc mạng, biến kim loại thành chất dẫn nhiệt tuyệt vời. Đối lưu chỉ xảy ra trong chất lưu: phần chất lỏng hoặc khí nóng giãn nở, giảm khối lượng riêng và nổi lên, trong khi phần nguội hơn có khối lượng riêng lớn hơn sẽ chìm xuống, tạo thành dòng đối lưu liên tục. Bức xạ truyền nhiệt bằng sóng điện từ hồng ngoại và truyền được qua chân không. Bề mặt đen mờ là vật hấp thụ và phát xạ nhiệt tốt nhất, còn bề mặt sáng bóng là vật phản xạ nhiệt tốt nhất."
        }
    ]

    major_sections = [
        {"title": "Giới thiệu P2", "start": 0.0},
        {"title": "1. Mô hình Động học Hạt", "start": 0.0},
        {"title": "2. Giãn nở Nhiệt & Bay hơi", "start": 0.0},
        {"title": "3. Ba Cơ chế Truyền Nhiệt", "start": 0.0}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences (0654)", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print(f"Completed Topic {code.upper()}!")

# ==============================================================================
# TOPIC P3: Waves
# ==============================================================================
async def build_p3():
    lid = 'eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8'
    code = 'p3'
    title = 'P3: Waves'
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    html = res.data[0]['content_html']
    
    t_header = '<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center;">'
    r_header = '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; padding: 20px; background: #f8fafc; border-radius: 12px; border: 1px dashed #cbd5e1; justify-content: center; align-items: center; cursor: pointer;">'
    
    h2s = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
    
    t_h2_0 = h2s[0]
    r_h2_0 = t_h2_0.replace('<h2', '<h2 id="sec-wave-properties" class="lecture-interactive-card" data-lecture-section="sec_wave_properties" style="cursor: pointer; ')
    
    t_h2_1 = h2s[1]
    r_h2_1 = t_h2_1.replace('<h2', '<h2 id="sec-wave-equation" class="lecture-interactive-card" data-lecture-section="sec_wave_equation" style="cursor: pointer; ')
    
    t_h2_2 = h2s[2]
    r_h2_2 = t_h2_2.replace('<h2', '<h2 id="sec-light" class="lecture-interactive-card" data-lecture-section="sec_light" style="cursor: pointer; ')
    
    t_h2_3 = h2s[3]
    r_h2_3 = t_h2_3.replace('<h2', '<h2 id="sec-em-spectrum" class="lecture-interactive-card" data-lecture-section="sec_em_spectrum" style="cursor: pointer; ')
    
    t_h2_4 = h2s[4]
    r_h2_4 = t_h2_4.replace('<h2', '<h2 id="sec-sound" class="lecture-interactive-card" data-lecture-section="sec_sound" style="cursor: pointer; ')
    
    new_html = html.replace(t_header, r_header, 1)\
                   .replace(t_h2_0, r_h2_0, 1)\
                   .replace(t_h2_1, r_h2_1, 1)\
                   .replace(t_h2_2, r_h2_2, 1)\
                   .replace(t_h2_3, r_h2_3, 1)\
                   .replace(t_h2_4, r_h2_4, 1)

    diff = len(new_html.split('<div')) - len(new_html.split('</div>'))
    if diff != 0:
        print(f"Warning: Topic P3 div diff = {diff}")

    segments = [
        {
            "id": "intro",
            "title": "Giới thiệu Chuyên đề P3: Sóng & Quang học (Waves)",
            "selector": "#sec-header",
            "en": "Welcome to Topic P3: Waves. Waves are the fundamental mechanism by which energy is transferred without transferring matter. In this lesson, we study transverse and longitudinal waves, calculate wave speed using the wave equation, examine light reflection, refraction, and converging lenses, explore the seven bands of the electromagnetic spectrum, and investigate the physics of sound waves and echoes.",
            "vi": "Chào mừng các bạn đến với Chuyên đề P3: Sóng và Quang học. Sóng là cơ chế cơ bản truyền năng lượng từ nơi này sang nơi khác mà không vận chuyển vật chất. Trong bài học này, chúng ta sẽ khảo sát sóng ngang và sóng dọc, tính tốc độ truyền sóng bằng phương trình sóng, nghiên cứu sự phản xạ, khúc xạ ánh sáng và thấu kính hội tụ, khám phá 7 dải sóng trong thang sóng điện từ, và tìm hiểu tính chất sóng âm cùng tiếng vang."
        },
        {
            "id": "sec_wave_properties",
            "title": "1. Tính chất Chung của Sóng (General Wave Properties)",
            "selector": "#sec-wave-properties",
            "en": "A wave is an oscillation that transfers energy from one point to another without transferring matter. Waves are classified into transverse and longitudinal waves. In transverse waves, oscillations are perpendicular to the direction of wave travel, creating crests and troughs, as seen in water waves and all electromagnetic radiation. In longitudinal waves, oscillations are parallel to the direction of wave travel, creating alternating compressions and rarefactions, as in sound waves. Key parameters include amplitude, wavelength lambda, frequency f in Hertz, and wave period T equals one divided by f.",
            "vi": "Sóng là một dao động lan truyền mang năng lượng từ điểm này đến điểm khác mà không truyền theo vật chất. Sóng được chia thành sóng ngang và sóng dọc. Trong sóng ngang, các phần tử dao động vuông góc với phương truyền sóng, tạo thành đỉnh sóng và đáy sóng, như sóng mặt nước và toàn bộ sóng điện từ. Trong sóng dọc, các phần tử dao động song song với phương truyền sóng, tạo thành các vùng nén và vùng dãn xen kẽ, điển hình là sóng âm. Các đại lượng đặc trưng gồm biên độ, bước sóng lambda, tần số f đo bằng Hertz, và chu kỳ T bằng một chia cho f."
        },
        {
            "id": "sec_wave_equation",
            "title": "2. Phương trình Sóng & Hành vi của Sóng (The Wave Equation & Wave Behaviors)",
            "selector": "#sec-wave-equation",
            "en": "The wave equation connects wave speed v, frequency f, and wavelength lambda: v equals f times lambda. Waves exhibit three fundamental behaviors: reflection, refraction, and diffraction. In reflection, waves bounce off a flat boundary with the angle of incidence equal to the angle of reflection. In refraction, when waves enter a medium of different optical or physical density, their speed and wavelength change, causing wavefronts to bend, while frequency remains strictly constant. In diffraction, waves spread out when passing through a gap or around an obstacle; diffraction is most pronounced when the gap width is roughly equal to the wavelength.",
            "vi": "Phương trình truyền sóng liên hệ giữa vận tốc truyền sóng v, tần số f và bước sóng lambda: v bằng f nhân lambda. Sóng thể hiện ba hành vi cơ bản: phản xạ, khúc xạ và nhiễu xạ. Trong phản xạ, sóng dội lại từ mặt chắn với góc tới bằng góc phản xạ. Trong khúc xạ, khi sóng truyền sang một môi trường có mật độ quang học hoặc vật lý khác, vận tốc và bước sóng thay đổi khiến mặt sóng bị bẻ cong, trong khi tần số giữ nguyên tuyệt đối. Trong nhiễu xạ, sóng lan tỏa sang hai bên khi đi qua một khe hẹp hoặc mép vật cản; hiện tượng nhiễu xạ rõ nét nhất khi bề rộng khe xấp xỉ bằng bước sóng."
        },
        {
            "id": "sec_light",
            "title": "3. Quang học: Phản xạ, Khúc xạ & Thấu kính (Light, Lenses & Dispersion)",
            "selector": "#sec-light",
            "en": "Light travels in straight lines at 300,000 kilometers per second in a vacuum. The law of reflection states that the angle of incidence equals the angle of reflection, measured from the normal. Refraction occurs because light slows down when entering denser media like glass or water, bending towards the normal according to Snell's law: n equals sin i divided by sin r. When light travels from a denser medium to an air boundary at an angle greater than the critical angle, total internal reflection occurs, the principle behind fiber-optic communications. A converging lens brings parallel rays together at the principal focus. Triangular glass prisms disperse white light into a rainbow spectrum because different wavelengths refract by different amounts.",
            "vi": "Ánh sáng truyền theo đường thẳng với vận tốc 300.000 kilômét trên giây trong chân không. Định luật phản xạ ánh sáng khẳng định góc tới bằng góc phản xạ, đo so với pháp tuyến. Khúc xạ ánh sáng xảy ra vì ánh sáng giảm tốc độ khi đi vào môi trường chiết quang hơn như thủy tinh hoặc nước, lệch về phía pháp tuyến theo định luật Snell: n bằng sin i chia sin r. Khi ánh sáng truyền từ môi trường chiết quang sang không khí với góc tới lớn hơn góc tới hạn, hiện tượng phản xạ toàn phần sẽ xảy ra, đây là nguyên lý cốt lõi của sợi cáp quang viễn thông. Thấu kính hội tụ gom các tia sáng song song tại tiêu điểm chính. Lăng kính tam giác phân tán ánh sáng trắng thành dải màu cầu vồng vì các bước sóng khác nhau bị khúc xạ với các góc lệch khác nhau."
        },
        {
            "id": "sec_em_spectrum",
            "title": "4. Thang Sóng Điện từ (The Electromagnetic Spectrum)",
            "selector": "#sec-em-spectrum",
            "en": "The electromagnetic spectrum is a continuous family of transverse waves that all travel at the speed of light in vacuum. In order of increasing frequency and decreasing wavelength, the seven bands are: Radio waves, Microwaves, Infrared, Visible light, Ultraviolet, X-rays, and Gamma rays. Radio waves are used for broadcasting and television. Microwaves heat water molecules in cooking and transmit satellite signals. Infrared is used in remote controls and thermal imaging. Ultraviolet causes fluorescence and vitamin D synthesis, but excess exposure causes sunburn and skin cancer. X-rays and Gamma rays are highly penetrating ionizing radiations used in medical imaging and cancer radiotherapy.",
            "vi": "Thang sóng điện từ là một dải liên tục các sóng ngang lan truyền với tốc độ ánh sáng trong chân không. Theo thứ tự tần số tăng dần và bước sóng giảm dần, 7 dải sóng gồm có: Sóng vô tuyến, Vi sóng, Tia hồng ngoại, Ánh sáng nhìn thấy, Tia tử ngoại, Tia X và Tia gamma. Sóng vô tuyến dùng trong phát thanh và truyền hình. Vi sóng kích thích phân tử nước trong lò vi sóng và truyền tín hiệu vệ tinh. Tia hồng ngoại dùng trong điều khiển từ xa và ghi hình ảnh nhiệt. Tia tử ngoại gây phát quang và tổng hợp vitamin D, nhưng phơi nhiễm quá mức gây cháy nắng và ung thư da. Tia X và tia Gamma là bức xạ ion hóa có tính đâm xuyên mạnh, được dùng trong chụp X-quang y tế và xạ trị tiêu diệt khối u ung thư."
        },
        {
            "id": "sec_sound",
            "title": "5. Sóng Âm & Tiếng vang (Sound Waves & Echoes)",
            "selector": "#sec-sound",
            "en": "Sound is produced by vibrating sources and travels as longitudinal mechanical waves through solids, liquids, and gases; sound cannot travel through a vacuum. Sound travels fastest in solids and slowest in gases because closer particles transmit vibrations more quickly. The normal human hearing range extends from 20 Hertz to 20,000 Hertz. Sound waves above 20 kilohertz are called ultrasound, used in medical fetal scans and sonar navigation. Pitch is determined by frequency: higher frequency produces a higher pitch. Loudness is determined by amplitude: larger amplitude carries more energy and sounds louder. An echo is a reflected sound wave, used to measure distances using speed equals two times distance divided by time.",
            "vi": "Âm thanh được tạo ra từ các nguồn dao động và lan truyền dưới dạng sóng cơ học dọc qua chất rắn, chất lỏng và chất khí; âm thanh không thể truyền trong chân không. Âm thanh truyền nhanh nhất trong chất rắn và chậm nhất trong chất khí vì các hạt nằm sát nhau truyền dao động nhanh hơn. Khoảng nghe thông thường của tai người trải từ 20 Hertz đến 20.000 Hertz. Sóng âm có tần số trên 20 kilohertz gọi là siêu âm, ứng dụng trong siêu âm thai nhi y khoa và máy dò sóng âm sonar dưới đáy biển. Độ cao của âm do tần số quyết định: tần số càng lớn âm càng bổng. Độ to của âm do biên độ quyết định: biên độ càng lớn âm nghe càng to. Tiếng vang là sóng âm bị phản xạ trở lại, được dùng để đo khoảng cách theo công thức vận tốc bằng 2 lần quãng đường chia thời gian."
        }
    ]

    major_sections = [
        {"title": "Giới thiệu P3", "start": 0.0},
        {"title": "1. Tính chất Chung của Sóng", "start": 0.0},
        {"title": "2. Phương trình Sóng", "start": 0.0},
        {"title": "3. Quang học & Khúc xạ", "start": 0.0},
        {"title": "4. Thang Sóng Điện từ", "start": 0.0},
        {"title": "5. Sóng Âm & Tiếng vang", "start": 0.0}
    ]

    await process_lecture_audio(code, lid, "Cambridge IGCSE Co-ordinated Sciences (0654)", title, segments, major_sections, subject='science')
    update_supabase_page(lid, new_html)
    print(f"Completed Topic {code.upper()}!")

# ==============================================================================
# MAIN RUNNER
# ==============================================================================
async def main():
    print("Starting Batch 8: P1, P2, P3...")
    await build_p1()
    await build_p2()
    await build_p3()
    print("\nALL TOPICS IN BATCH 8 COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
