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
# P1: MOTION, FORCES & ENERGY
# =====================================================================
P1_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề P1: Chuyển động, Lực & Năng lượng",
        "selector": "#sec-header",
        "en": "Welcome to Topic P1: Motion, Forces and Energy. Classical mechanics describes how physical quantities are measured, how objects accelerate and collide, how forces cause extension and turning effects, and how energy is stored, transferred, and conserved throughout the universe.",
        "vi": "Chào mừng các bạn đến với Chuyên đề P1: Chuyển động, Lực và Năng lượng. Cơ học cổ điển nghiên cứu các phép đo đại lượng vật lý, quy luật chuyển động và va chạm, tác dụng làm biến dạng và quay của lực, cùng các dạng dự trữ, truyền tải và bảo toàn năng lượng trong tự nhiên."
    },
    {
        "id": "sec_quantities",
        "title": "1. Đại lượng Vật lý & Kỹ thuật Đo lường (Physical Quantities Overview)",
        "selector": "#sec-quantities",
        "en": "Section 1 covers physical measurement: Using rulers, measuring cylinders, and stopwatches accurately while avoiding parallax error. It also contrasts scalar quantities having magnitude only with vector quantities having both magnitude and direction.",
        "vi": "Mục một bao gồm kỹ thuật đo lường vật lý: Sử dụng thước thẳng, ống đong và đồng hồ bấm giây chính xác, tránh lỗi thị sai. Đồng thời phân biệt đại lượng vô hướng chỉ có độ lớn với đại lượng vecto có cả độ lớn và hướng."
    },
    {
        "id": "sec_measuring_instruments",
        "title": "📏 Measuring Instruments & Multiples (Dụng cụ Đo & Đo Bội số)",
        "selector": "#sec-measuring-instruments",
        "en": "To measure tiny quantities accurately, measure a large multiple and divide. For example, measure the thickness of 500 sheets of paper and divide by 500, or time 20 pendulum oscillations and divide by 20 to reduce reaction time error.",
        "vi": "Để đo các đại lượng rất nhỏ một cách chính xác, hãy đo một tập hợp nhiều lần rồi chia đều. Ví dụ đo độ dày của 500 trang giấy rồi chia cho 500, hoặc bấm thời gian 20 dao động con lắc rồi chia cho 20 để giảm thiểu sai số thời gian phản ứng."
    },
    {
        "id": "sec_scalars_vectors",
        "title": "🧭 Scalars vs Vectors (Vô hướng vs Vecto)",
        "selector": "#sec-scalars-vectors",
        "en": "Scalars have magnitude only: distance, speed, time, mass, energy, and temperature. Vectors have both magnitude and direction: force, weight, velocity, acceleration, and gravitational field strength.",
        "vi": "Đại lượng vô hướng chỉ có độ lớn: quãng đường, tốc độ, thời gian, khối lượng, năng lượng và nhiệt độ. Đại lượng vecto có cả độ lớn và phương chiều: lực, trọng lượng, vận tốc, gia tốc và cường độ trọng trường."
    },
    {
        "id": "sec_kinematics",
        "title": "2. Đồ thị Động học & Chuyển động (Motion & Kinematics Graphs Overview)",
        "selector": "#sec-kinematics",
        "en": "Section 2 investigates speed, velocity, and acceleration. On a distance-time graph, gradient represents speed. On a speed-time graph, gradient represents acceleration, and the area under the graph equals distance travelled.",
        "vi": "Mục hai nghiên cứu tốc độ, vận tốc và gia tốc. Trên đồ thị quãng đường - thời gian, độ dốc biểu diễn tốc độ. Trên đồ thị tốc độ - thời gian, độ dốc biểu diễn gia tốc và diện tích hình phẳng dưới đồ thị biểu diễn quãng đường đi được."
    },
    {
        "id": "sec_kinematics_graphs",
        "title": "📈 Graph Interpretation & Area Under Curve (Phân tích Đồ thị)",
        "selector": "#sec-kinematics-graphs",
        "en": "Key rules for speed-time graphs: A horizontal line indicates constant speed with zero acceleration. A constant upward slope indicates uniform acceleration. The area under the line, calculated by summing triangles and rectangles, gives total distance travelled.",
        "vi": "Quy tắc vàng cho đồ thị tốc độ - thời gian: Đường nằm ngang biểu thị tốc độ không đổi với gia tốc bằng 0. Đoạn thẳng dốc lên biểu thị gia tốc không đổi. Diện tích bên dưới đồ thị, tính bằng tổng diện tích các hình tam giác và hình chữ nhật, chính là tổng quãng đường di chuyển."
    },
    {
        "id": "sec_free_fall",
        "title": "🪂 Free Fall & Terminal Velocity (Rơi Tự do & Tốc độ Giới hạn)",
        "selector": "#sec-free-fall",
        "en": "In a vacuum, all falling objects accelerate downwards at 9.8 meters per second squared due to gravity. In air, air resistance opposes weight. As speed increases, drag increases until upward drag equals downward weight, resulting in zero net force and constant terminal velocity.",
        "vi": "Trong chân không, mọi vật rơi tự do đều tăng tốc xuống dưới với gia tốc 9.8 mét trên giây bình phương do trọng lực. Trong không khí, lực cản không khí cản trở chuyển động. Khi tốc độ tăng, lực cản tăng theo cho đến khi lực cản hướng lên cân bằng với trọng lượng hướng xuống, hợp lực bằng 0 và vật đạt tốc độ giới hạn không đổi."
    },
    {
        "id": "sec_density",
        "title": "3. Khối lượng, Trọng lượng & Khối lượng Riêng (Mass, Weight & Density Overview)",
        "selector": "#sec-density",
        "en": "Section 3 defines mass as the measure of matter in a body, and weight as the gravitational force acting on that mass: Weight equals mass times gravitational field strength g.",
        "vi": "Mục ba định nghĩa khối lượng là lượng vật chất tạo nên vật thể, và trọng lượng là lực hấp dẫn tác dụng lên khối lượng đó: Trọng lượng bằng khối lượng nhân cường độ trọng trường g."
    },
    {
        "id": "sec_density_calc",
        "title": "⚖️ Density Determination (Xác định Khối lượng Riêng)",
        "selector": "#sec-density-calc",
        "en": "Density rho equals mass divided by volume. For irregular solid objects, volume is determined using the displacement method in a measuring cylinder containing water.",
        "vi": "Khối lượng riêng rho bằng khối lượng chia thể tích. Đối với vật thể rắn có hình dạng bất kỳ, thể tích được đo bằng phương pháp choán chỗ chất lỏng trong ống đong chứa nước."
    },
    {
        "id": "sec_forces",
        "title": "4. Lực, Định luật Hooke, Momen & Áp suất (Forces, Moments & Pressure Overview)",
        "selector": "#sec-forces",
        "en": "Section 4 examines forces: Resultant force equals mass times acceleration (F = ma). Hooke's law states that force is directly proportional to extension up to the limit of proportionality (F = kx).",
        "vi": "Mục bốn phân tích các loại lực: Hợp lực bằng khối lượng nhân gia tốc theo định luật hai Newton (F = ma). Định luật Hooke khẳng định lực kéo tỉ lệ thuận với độ dãn của lò xo cho đến giới hạn đàn hồi (F = kx)."
    },
    {
        "id": "sec_moments_pressure",
        "title": "⚙️ Moments & Pressure (Momen Lực & Áp suất)",
        "selector": "#sec-moments-pressure",
        "en": "The moment of a force equals force times perpendicular distance to pivot. For equilibrium, clockwise moments equal anticlockwise moments. Pressure equals force divided by contact area.",
        "vi": "Momen của lực bằng lực nhân khoảng cách vuông góc từ giá của lực đến trục quay. Ở trạng thái cân bằng, tổng momen quay theo chiều kim đồng hồ bằng tổng momen quay ngược chiều. Áp suất bằng áp lực chia cho diện tích tiếp xúc."
    },
    {
        "id": "sec_energy_stores",
        "title": "5. Các Dạng Năng lượng & Đường truyền (Energy Stores & Pathways Overview)",
        "selector": "#sec-energy-stores",
        "en": "Section 5 details eight energy stores: kinetic, gravitational, chemical, elastic, nuclear, electrostatic, magnetic, and thermal. Energy is transferred between stores via mechanical work, electrical work, heating, and radiation.",
        "vi": "Mục năm phân loại tám kho dự trữ năng lượng: động năng, thế năng trọng trường, hóa năng, thế năng đàn hồi, năng lượng hạt nhân, tĩnh điện, từ trường và nhiệt năng. Năng lượng luân chuyển qua bốn con đường: công cơ học, công điện, truyền nhiệt và bức xạ."
    },
    {
        "id": "sec_ke_gpe",
        "title": "6. Động năng & Thế năng Trọng trường (Kinetic & Gravitational Energy)",
        "selector": "#sec-ke-gpe",
        "en": "Section 6 calculates mechanical energy: Kinetic energy equals half mass times velocity squared. Gravitational potential energy equals mass times g times change in height.",
        "vi": "Mục sáu tính toán cơ năng: Động năng bằng một nửa khối lượng nhân bình phương vận tốc. Thế năng trọng trường bằng khối lượng nhân g nhân độ cao thay đổi."
    },
    {
        "id": "sec_work_power",
        "title": "7. Công, Công suất & Hiệu suất (Work, Power & Efficiency Overview)",
        "selector": "#sec-work-power",
        "en": "Section 7 establishes: Work done equals force times distance in the direction of force. Power is the rate of transferring energy or doing work. Efficiency equals useful energy output divided by total energy input, expressed as a percentage.",
        "vi": "Mục bảy thiết lập: Công cơ học bằng lực nhân quãng đường dịch chuyển theo phương của lực. Công suất là tốc độ thực hiện công hay tốc độ tiêu thụ năng lượng. Hiệu suất bằng năng lượng có ích sinh ra chia cho tổng năng lượng đầu vào, tính theo phần trăm."
    },
    {
        "id": "sec_energy_resources",
        "title": "8. Nguồn Năng lượng Tái tạo & Không tái tạo (Energy Resources Overview)",
        "selector": "#sec-energy-resources",
        "en": "Section 8 compares energy sources: Fossil fuels and nuclear are non-renewable reliable sources with high environmental impact. Solar, wind, hydroelectric, and tidal are clean renewable sources derived mostly from the Sun's radiation.",
        "vi": "Mục tám so sánh các nguồn năng lượng: Nhiên liệu hóa thạch và hạt nhân là nguồn không tái tạo có độ ổn định cao nhưng tác động đến môi trường. Năng lượng mặt trời, gió, thủy điện và thủy triều là các nguồn năng lượng tái tạo sạch mà phần lớn có nguồn gốc từ bức xạ của Mặt Trời."
    }
]

P1_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề P1", "selector": "#sec-header"},
    "sec_quantities": {"start": 1, "end": 3, "title": "1. Đại lượng Vật lý & Đo lường", "selector": "#sec-quantities"},
    "sec_kinematics": {"start": 4, "end": 6, "title": "2. Đồ thị Động học & Chuyển động", "selector": "#sec-kinematics"},
    "sec_density": {"start": 7, "end": 8, "title": "3. Khối lượng, Trọng lượng & Khối lượng Riêng", "selector": "#sec-density"},
    "sec_forces": {"start": 9, "end": 10, "title": "4. Lực, Momen & Áp suất", "selector": "#sec-forces"},
    "sec_energy_stores": {"start": 11, "end": 11, "title": "5. Kho Năng lượng & Đường truyền", "selector": "#sec-energy-stores"},
    "sec_ke_gpe": {"start": 12, "end": 12, "title": "6. Động năng & Thế năng", "selector": "#sec-ke-gpe"},
    "sec_work_power": {"start": 13, "end": 13, "title": "7. Công, Công suất & Hiệu suất", "selector": "#sec-work-power"},
    "sec_energy_resources": {"start": 14, "end": 14, "title": "8. So sánh Nguồn Năng lượng", "selector": "#sec-energy-resources"}
}


# =====================================================================
# P2: THERMAL PHYSICS
# =====================================================================
P2_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề P2: Vật lý Nhiệt & Thuyết Động học",
        "selector": "#sec-header",
        "en": "Welcome to Topic P2: Thermal Physics. Thermal physics investigates heat energy and temperature from the microscopic viewpoint of particle motion. In this topic, we study kinetic particle models of matter, Brownian motion, gas pressure, thermal expansion, evaporation, and the three heat transfer mechanisms: conduction, convection, and radiation.",
        "vi": "Chào mừng các bạn đến với Chuyên đề P2: Vật lý Nhiệt và Thuyết Động học. Vật lý nhiệt nghiên cứu nhiệt năng và nhiệt độ dưới góc nhìn vi mô của các hạt chuyển động. Trong bài học này, chúng ta sẽ khảo sát mô hình hạt động học, chuyển động Brown, áp suất chất khí, sự nở vì nhiệt, sự bay hơi, cùng ba cơ chế truyền nhiệt: dẫn nhiệt, đối lưu và bức xạ."
    },
    {
        "id": "sec_kinetic_model",
        "title": "1. Mô hình Động học Hạt của Vật chất (Kinetic Particle Model Overview)",
        "selector": "#sec-kinetic-model",
        "en": "Section 1 reviews the three states of matter in terms of particle arrangement, separation, and motion. Brownian motion provides direct experimental evidence that tiny particles are constantly bombarded by fast-moving invisible molecules.",
        "vi": "Mục một tổng kết ba thể của vật chất dựa trên cách sắp xếp, khoảng cách và chuyển động của hạt. Hiện tượng chuyển động Brown là bằng chứng thực nghiệm trực tiếp chứng minh các hạt siêu nhỏ liên tục bị va đập bởi các phân tử vô hình chuyển động hỗn loạn."
    },
    {
        "id": "sec_brownian_pressure",
        "title": "🎈 Brownian Motion & Gas Pressure (Chuyển động Brown & Áp suất Khí)",
        "selector": "#sec-brownian-pressure",
        "en": "Gas pressure is caused by continuous random collisions of gas molecules against container walls, exerting force per unit area. Increasing temperature increases molecular kinetic energy and collision frequency, thereby raising gas pressure.",
        "vi": "Áp suất chất khí sinh ra do các phân tử khí liên tục va chạm hỗn loạn vào thành bình, tạo ra lực tác dụng lên một đơn vị diện tích. Khi tăng nhiệt độ, động năng và tần số va chạm của các phân tử tăng lên, làm tăng áp suất chất khí."
    },
    {
        "id": "sec_expansion",
        "title": "2. Sự Nở vì Nhiệt & Sự Bay hơi (Thermal Expansion & Evaporation Overview)",
        "selector": "#sec-expansion",
        "en": "Section 2 investigates thermal expansion: Solids expand slightly, liquids expand moderately, and gases expand significantly when heated. Evaporation occurs at any temperature from liquid surfaces, causing cooling.",
        "vi": "Mục hai nghiên cứu sự nở vì nhiệt: Chất rắn nở rất ít, chất lỏng nở vừa phải và chất khí nở nhiều nhất khi bị đun nóng. Sự bay hơi diễn ra ở mọi nhiệt độ trên bề mặt chất lỏng và mang lại hiệu ứng làm mát."
    },
    {
        "id": "sec_evaporation_cooling",
        "title": "❄️ Evaporation & Cooling Effect (Cơ chế Bay hơi & Làm mát)",
        "selector": "#sec-evaporation-cooling",
        "en": "During evaporation, the most energetic molecules escape from the liquid surface. The average kinetic energy of the remaining molecules decreases, lowering liquid temperature. Factors increasing evaporation rate are higher temperature, greater surface area, and wind draught.",
        "vi": "Trong quá trình bay hơi, các phân tử có động năng lớn nhất sẽ thoát ra khỏi bề mặt chất lỏng. Động năng trung bình của các phân tử còn lại giảm xuống khiến nhiệt độ chất lỏng hạ đi. Các yếu tố thúc đẩy tốc độ bay hơi gồm nhiệt độ cao, diện tích bề mặt lớn và có gió thổi qua."
    },
    {
        "id": "sec_heat_transfer",
        "title": "3. Ba Cơ chế Truyền Nhiệt (Thermal Energy Transfers Overview)",
        "selector": "#sec-heat-transfer",
        "en": "Section 3 analyzes thermal energy transfer: Conduction through solids via lattice vibration and delocalised free electrons in metals, Convection in fluids via density changes, and Radiation via infrared electromagnetic waves through vacuum.",
        "vi": "Mục ba phân tích ba cơ chế truyền nhiệt: Dẫn nhiệt trong chất rắn nhờ dao động mạng tinh thể và các electron tự do trong kim loại, Đối lưu trong chất lưu nhờ chênh lệch khối lượng riêng, và Bức xạ nhiệt dưới dạng sóng điện từ hồng ngoại truyền qua được chân không."
    },
    {
        "id": "sec_convection_radiation",
        "title": "🔥 Convection & Radiation Emitters (Đối lưu & Bức xạ)",
        "selector": "#sec-convection-radiation",
        "en": "In convection, heated fluid expands, becomes less dense, and rises, while cooler dense fluid sinks to form a convection current. In radiation, dull black surfaces are the best absorbers and best emitters, while shiny silver surfaces reflect infrared radiation.",
        "vi": "Trong hiện tượng đối lưu, chất lưu bị đun nóng sẽ nở ra, nhẹ hơn và nổi lên trên, trong khi chất lưu lạnh nặng hơn chìm xuống tạo thành dòng đối lưu tuần hoàn. Trong bức xạ, bề mặt đen mờ là vật hấp thụ và bức xạ nhiệt tốt nhất, còn bề mặt sáng bạc phản xạ bức xạ hồng ngoại tốt nhất."
    }
]

P2_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề P2", "selector": "#sec-header"},
    "sec_kinetic_model": {"start": 1, "end": 2, "title": "1. Mô hình Động học Hạt", "selector": "#sec-kinetic-model"},
    "sec_expansion": {"start": 3, "end": 4, "title": "2. Nở vì Nhiệt & Bay hơi", "selector": "#sec-expansion"},
    "sec_heat_transfer": {"start": 5, "end": 6, "title": "3. Ba Cơ chế Truyền Nhiệt", "selector": "#sec-heat-transfer"}
}


# =====================================================================
# P3: PROPERTIES OF WAVES
# =====================================================================
P3_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề P3: Tính chất của Sóng, Ánh sáng & Âm thanh",
        "selector": "#sec-header",
        "en": "Welcome to Topic P3: Properties of Waves. Waves transfer energy without transferring matter. In this lesson, we study transverse and longitudinal waves, the wave equation, reflection, refraction, diffraction, converging lenses, dispersion, the electromagnetic spectrum, and sound waves.",
        "vi": "Chào mừng các bạn đến với Chuyên đề P3: Tính chất của Sóng, Ánh sáng và Âm thanh. Sóng truyền năng lượng từ nơi này sang nơi khác mà không mang theo vật chất. Trong bài học này, chúng ta sẽ học sóng ngang và sóng dọc, phương trình sóng, phản xạ, khúc xạ, nhiễu xạ, thấu kính hội tụ, tán sắc ánh sáng, thang sóng điện từ và sóng âm."
    },
    {
        "id": "sec_wave_properties",
        "title": "1. Tính chất Đại cương của Sóng (General Wave Properties Overview)",
        "selector": "#sec-wave-properties",
        "en": "Section 1 defines wave terms: Amplitude is maximum displacement from rest position. Wavelength is distance between consecutive crests. Frequency is number of complete waves per second, measured in Hertz.",
        "vi": "Mục một định nghĩa các đại lượng sóng: Biên độ là độ dịch chuyển cực đại khỏi vị trí cân bằng. Bước sóng là khoảng cách giữa hai đỉnh sóng liên tiếp. Tần số là số dao động toàn phần trong một giây, đo bằng đơn vị Hertz."
    },
    {
        "id": "sec_transverse_longitudinal",
        "title": "🌊 Transverse vs Longitudinal Waves (Sóng Ngang vs Sóng Dọc)",
        "selector": "#sec-transverse-longitudinal",
        "en": "In a transverse wave, particle vibration is perpendicular to the direction of wave travel, like light and water ripples. In a longitudinal wave, particle vibration is parallel to wave travel, forming compressions and rarefactions, like sound waves.",
        "vi": "Trong sóng ngang, các phần tử dao động vuông góc với phương truyền sóng, ví dụ sóng ánh sáng và sóng mặt nước. Trong sóng dọc, các phần tử dao động song song với phương truyền sóng, tạo thành các vùng nén và dãn liên tiếp, ví dụ sóng âm."
    },
    {
        "id": "sec_wave_equation",
        "title": "2. Phương trình Sóng & Hiện tượng Sóng (Wave Equation & Behaviors Overview)",
        "selector": "#sec-wave-equation",
        "en": "Section 2 introduces the fundamental wave speed equation: Wave speed v equals frequency f multiplied by wavelength lambda. It also investigates reflection, refraction, and diffraction.",
        "vi": "Mục hai giới thiệu phương trình tốc độ truyền sóng cốt lõi: Tốc độ sóng v bằng tần số f nhân bước sóng lambda. Đồng thời phân tích các hiện tượng phản xạ, khúc xạ và nhiễu xạ qua khe hẹp."
    },
    {
        "id": "sec_reflection_refraction",
        "title": "🪞 Reflection, Refraction & Diffraction (Phản xạ, Khúc xạ & Nhiễu xạ)",
        "selector": "#sec-reflection-refraction",
        "en": "In reflection, angle of incidence equals angle of reflection. In refraction, waves slow down and bend towards normal when entering denser media. In diffraction, waves spread around obstacles or through gaps, with maximum spreading when gap width equals wavelength.",
        "vi": "Trong phản xạ, góc tới bằng góc phản xạ. Trong khúc xạ, sóng giảm tốc độ và bẻ cong về phía pháp tuyến khi đi vào môi trường chiết quang hơn. Trong nhiễu xạ, sóng lan tỏa khi đi qua khe hẹp hoặc vòng qua vật cản, đạt độ lan tỏa cực đại khi độ rộng khe xấp xỉ bằng bước sóng."
    },
    {
        "id": "sec_light",
        "title": "3. Ánh sáng, Thấu kính Hội tụ & Tán sắc (Light, Lenses & Dispersion Overview)",
        "selector": "#sec-light",
        "en": "Section 3 investigates optics: Law of reflection in plane mirrors, critical angle and total internal reflection, converging lenses forming real or virtual images, and white light dispersion through a glass prism.",
        "vi": "Mục ba nghiên cứu quang hình học: Định luật phản xạ gương phẳng, góc giới hạn và phản xạ toàn phần trong cáp quang, thấu kính hội tụ tạo ảnh thật hoặc ảnh ảo, cùng hiện tượng tán sắc ánh sáng trắng qua lăng kính thủy tinh."
    },
    {
        "id": "sec_em_spectrum",
        "title": "4. Thang Sóng Điện từ (The Electromagnetic Spectrum Overview)",
        "selector": "#sec-em-spectrum",
        "en": "Section 4 covers the EM spectrum: Radio waves, Microwaves, Infrared, Visible light, Ultraviolet, X-rays, and Gamma rays. All travel at 300 million meters per second in a vacuum.",
        "vi": "Mục bốn tổng hợp Thang Sóng Điện từ: Sóng vô tuyến, Vi sóng, Tia hồng ngoại, Ánh sáng nhìn thấy, Tia tử ngoại, Tia X và Tia gamma. Tất cả đều truyền đi với tốc độ 300 triệu mét trên giây trong chân không."
    },
    {
        "id": "sec_sound",
        "title": "5. Sóng Âm & Tiếng vang (Sound Waves & Echoes Overview)",
        "selector": "#sec-sound",
        "en": "Section 5 examines sound: Longitudinal waves produced by vibrating sources requiring a material medium. Approximate speed in air is 330 to 350 meters per second. Human hearing ranges from 20 Hertz to 20,000 Hertz.",
        "vi": "Mục năm phân tích sóng âm: Là sóng dọc sinh ra từ các vật dao động, bắt buộc phải có môi trường vật chất để lan truyền. Tốc độ âm trong không khí vào khoảng 330 đến 350 mét trên giây. Dải tần số tai người nghe được từ 20 Hertz đến 20,000 Hertz."
    }
]

P3_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề P3", "selector": "#sec-header"},
    "sec_wave_properties": {"start": 1, "end": 2, "title": "1. Tính chất Đại cương của Sóng", "selector": "#sec-wave-properties"},
    "sec_wave_equation": {"start": 3, "end": 4, "title": "2. Phương trình Sóng & Nhiễu xạ", "selector": "#sec-wave-equation"},
    "sec_light": {"start": 5, "end": 5, "title": "3. Ánh sáng, Thấu kính & Tán sắc", "selector": "#sec-light"},
    "sec_em_spectrum": {"start": 6, "end": 6, "title": "4. Thang Sóng Điện từ", "selector": "#sec-em-spectrum"},
    "sec_sound": {"start": 7, "end": 7, "title": "5. Sóng Âm & Tiếng vang", "selector": "#sec-sound"}
}


# =====================================================================
# P4: ELECTRICITY & MAGNETISM
# =====================================================================
P4_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề P4: Điện học & Từ học",
        "selector": "#sec-header",
        "en": "Welcome to Topic P4: Electricity and Magnetism. In this lesson, we study electric charge, current, electromotive force, Ohm's law, series and parallel circuits, potential dividers, electrical safety, electromagnetic induction, electric motors, and transformers.",
        "vi": "Chào mừng các bạn đến với Chuyên đề P4: Điện học và Từ học. Trong bài học này, chúng ta sẽ khảo sát điện tích, dòng điện, suất điện động, định luật Ohm, mạch điện nối tiếp và song song, mạch phân áp, an toàn điện, hiện tượng cảm ứng điện từ, động cơ điện và máy biến áp."
    },
    {
        "id": "sec_electrical_quantities",
        "title": "1. Đại lượng Điện & Định luật Ohm (Electrical Quantities Overview)",
        "selector": "#sec-electrical-quantities",
        "en": "Section 1 defines current as rate of charge flow: Q equals I times t. Potential difference V is energy per unit charge (V = W / Q). Ohm's law states V equals I times R for an ohmic conductor at constant temperature.",
        "vi": "Mục một định nghĩa cường độ dòng điện là tốc độ dòng điện tích dịch chuyển: Q bằng I nhân t. Hiệu điện thế V là năng lượng trên một đơn vị điện tích (V = W / Q). Định luật Ohm khẳng định V bằng I nhân R đối với dây dẫn kim loại ở nhiệt độ không đổi."
    },
    {
        "id": "sec_resistance_factors",
        "title": "📏 Resistance & Wire Dimensions (Điện trở & Dây dẫn)",
        "selector": "#sec-resistance-factors",
        "en": "Resistance of a metallic wire is directly proportional to its length and inversely proportional to its cross-sectional area. Doubling wire length doubles resistance; doubling wire diameter quadruples cross-sectional area, reducing resistance to one quarter.",
        "vi": "Điện trở của một đoạn dây kim loại tỉ lệ thuận với chiều dài và tỉ lệ nghịch với tiết diện dây. Chiều dài dây tăng gấp đôi thì điện trở tăng gấp đôi; đường kính dây tăng gấp đôi thì tiết diện tăng gấp bốn, làm điện trở giảm đi bốn lần."
    },
    {
        "id": "sec_electric_circuits",
        "title": "2. Mạch Điện Nối tiếp, Song song & Mạch Phân áp (Circuits Overview)",
        "selector": "#sec-electric-circuits",
        "en": "Section 2 explores circuit laws: In series, current is identical everywhere and total resistance equals R1 plus R2. In parallel, voltage is identical across branches and combined resistance is smaller than any individual branch.",
        "vi": "Mục hai khám phá quy luật mạch điện: Trong mạch nối tiếp, cường độ dòng điện như nhau tại mọi điểm và điện trở tương đương bằng tổng R1 cộng R2. Trong mạch song song, hiệu điện thế như nhau ở mọi nhánh và điện trở tương đương luôn nhỏ hơn điện trở của từng nhánh con."
    },
    {
        "id": "sec_potential_dividers",
        "title": "💡 Potential Dividers & Sensors (Mạch Phân áp & Cảm biến LDR, Thermistor)",
        "selector": "#sec-potential-dividers",
        "en": "A potential divider uses two resistors in series to divide voltage. In light dependent resistors (LDR), light increases conductivity, dropping resistance. In negative temperature coefficient thermistors, higher temperature drops resistance.",
        "vi": "Mạch phân áp gồm hai điện trở mắc nối tiếp để chia hiệu điện thế nguồn. Với quang điện trở LDR, khi có ánh sáng chiếu vào, điện trở giảm mạnh. Với nhiệt điện trở thermistor, khi nhiệt độ tăng cao, điện trở của nó giảm xuống."
    },
    {
        "id": "sec_electromagnetic_effects",
        "title": "3. Tác dụng Điện từ: Cảm ứng, Động cơ & Biến áp (EM Effects Overview)",
        "selector": "#sec-electromagnetic-effects",
        "en": "Section 3 covers electromagnetic effects: A moving conductor cutting magnetic field lines induces an e.m.f. The motor effect uses Fleming's left-hand rule. Transformers change alternating voltages via ratio Vp over Vs equals Np over Ns.",
        "vi": "Mục ba nghiên cứu tác dụng điện từ: Dây dẫn chuyển động cắt các đường sức từ sẽ sinh ra suất điện động cảm ứng. Lực từ tác dụng lên dòng điện tuân theo quy tắc bàn tay trái Fleming. Máy biến áp biến đổi điện áp xoay chiều dựa trên tỉ số điện áp bằng tỉ số số vòng dây."
    }
]

P4_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề P4", "selector": "#sec-header"},
    "sec_electrical_quantities": {"start": 1, "end": 2, "title": "1. Đại lượng Điện & Định luật Ohm", "selector": "#sec-electrical-quantities"},
    "sec_electric_circuits": {"start": 3, "end": 4, "title": "2. Mạch Điện & Mạch Phân áp", "selector": "#sec-electric-circuits"},
    "sec_electromagnetic_effects": {"start": 5, "end": 5, "title": "3. Tác dụng Điện từ & Biến áp", "selector": "#sec-electromagnetic-effects"}
}


# =====================================================================
# P5: NUCLEAR PHYSICS
# =====================================================================
P5_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề P5: Vật lý Hạt nhân & Phóng xạ",
        "selector": "#sec-header",
        "en": "Welcome to Topic P5: Nuclear Physics. Nuclear physics explores the structure of the atomic nucleus and radioactive decay. In this topic, we examine the Rutherford alpha scattering experiment, nuclear notation, alpha, beta, and gamma radiation, decay equations, half-life, and safety precautions.",
        "vi": "Chào mừng các bạn đến với Chuyên đề P5: Vật lý Hạt nhân và Hiện tượng Phóng xạ. Vật lý hạt nhân nghiên cứu cấu trúc hạt nhân nguyên tử và các quá trình phân rã phóng xạ. Trong bài học này, chúng ta sẽ khảo sát thí nghiệm tán xạ hạt alpha của Rutherford, ký hiệu hạt nhân, ba tia phóng xạ alpha, beta, gamma, phương trình phân rã, chu kỳ bán rã và các quy tắc an toàn bức xạ."
    },
    {
        "id": "sec_atomic_model",
        "title": "1. Mẫu Nguyên tử Hạt nhân & Đồng vị (Nuclear Atom Model Overview)",
        "selector": "#sec-atomic-model",
        "en": "Section 1 reviews Rutherford's scattering experiment: Most alpha particles passed straight through gold foil, proving the atom is mostly empty space. A tiny fraction deflected at large angles, proving mass and positive charge are concentrated in a tiny dense central nucleus.",
        "vi": "Mục một ôn lại thí nghiệm tán xạ hạt alpha của Rutherford: Hầu hết các hạt alpha xuyên thẳng qua lá vàng mỏng, chứng minh nguyên tử phần lớn là không gian rỗng. Một tỷ lệ rất nhỏ bị bật ngược lại với góc lớn, chứng minh toàn bộ khối lượng và điện tích dương tập trung ở một hạt nhân cực kỳ nhỏ bé và đậm đặc ở tâm."
    },
    {
        "id": "sec_radioactivity",
        "title": "2. Tính chất Phóng xạ: Alpha, Beta & Gamma (Radiation Types Overview)",
        "selector": "#sec-radioactivity",
        "en": "Section 2 compares radiation types: Alpha particles are helium nuclei with high ionizing power and low penetration stopped by paper. Beta particles are fast electrons with moderate penetration stopped by aluminium. Gamma rays are high-frequency EM waves stopped only by thick lead.",
        "vi": "Mục hai so sánh ba loại tia phóng xạ: Hạt alpha là hạt nhân heli có khả năng ion hóa mạnh nhất nhưng khả năng đâm xuyên yếu nhất, bị chặn lại bởi một tờ giấy. Hạt beta là dòng electron chuyển động nhanh bị chặn bởi miếng nhôm vài milimét. Tia gamma là sóng điện từ tần số cao chỉ bị cản bớt bởi khối chì dày."
    },
    {
        "id": "sec_decay_halflife",
        "title": "3. Phương trình Phân rã & Chu kỳ Bán rã (Decay Equations & Half-Life Overview)",
        "selector": "#sec-decay-halflife",
        "en": "Section 3 balances nuclear decay equations where total nucleon number and proton number are conserved. Half-life is the time taken for half the radioactive nuclei in any sample to decay.",
        "vi": "Mục ba hướng dẫn cân bằng phương trình phân rã hạt nhân bảo toàn số khối nucleon và số proton. Chu kỳ bán rã là khoảng thời gian cần thiết để một nửa số hạt nhân phóng xạ trong mẫu phân rã hết."
    },
    {
        "id": "sec_uses_safety",
        "title": "4. Ứng dụng Thực tiễn & An toàn Bức xạ (Uses & Safety Overview)",
        "selector": "#sec-uses-safety",
        "en": "Section 4 details practical applications: Americium-241 in smoke detectors, Beta emitters for paper thickness control, and Gamma radiation for cancer radiotherapy and medical sterilisation. Safety precautions include lead shielding, forceps handling, and minimised exposure time.",
        "vi": "Mục bốn tổng hợp các ứng dụng thực tế: Đồng vị Americium-241 trong đầu báo khói, nguồn phát hạt beta kiểm soát độ dày giấy công nghiệp, và tia gamma trong xạ trị tiêu diệt khối u và khử trùng y tế. Quy tắc an toàn gồm che chắn bằng chì, gắp bằng kẹp từ xa và hạn chế tối đa thời gian tiếp xúc."
    }
]

P5_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề P5", "selector": "#sec-header"},
    "sec_atomic_model": {"start": 1, "end": 1, "title": "1. Mẫu Nguyên tử Hạt nhân", "selector": "#sec-atomic-model"},
    "sec_radioactivity": {"start": 2, "end": 2, "title": "2. Ba Loại Tia Phóng xạ", "selector": "#sec-radioactivity"},
    "sec_decay_halflife": {"start": 3, "end": 3, "title": "3. Phương trình Phân rã & Bán rã", "selector": "#sec-decay-halflife"},
    "sec_uses_safety": {"start": 4, "end": 4, "title": "4. Ứng dụng & An toàn Bức xạ", "selector": "#sec-uses-safety"}
}


# =====================================================================
# P6: SPACE PHYSICS
# =====================================================================
P6_SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Chuyên đề P6: Vật lý Không gian & Vũ trụ",
        "selector": "#sec-header",
        "en": "Welcome to Topic P6: Space Physics. In this lesson, we study the Earth, Moon, and Solar System, orbital motion and gravitational force, the lifecycle of stars, nuclear fusion, galaxies, and the expanding universe.",
        "vi": "Chào mừng các bạn đến với Chuyên đề P6: Vật lý Không gian và Vũ trụ. Trong bài học này, chúng ta sẽ học về Trái Đất, Mặt Trăng và Hệ Mặt Trời, chuyển động quỹ đạo và lực hấp dẫn, vòng đời của các ngôi sao, phản ứng nhiệt hạch hạt nhân, thiên hà và sự giãn nở của vũ trụ."
    },
    {
        "id": "sec_earth_solar_system",
        "title": "1. Trái Đất & Hệ Mặt Trời (Earth & Solar System Overview)",
        "selector": "#sec-earth-solar-system",
        "en": "Section 1 reviews planetary motions: Earth rotates on its tilted axis every 24 hours producing day and night, and orbits the Sun every 365 days creating seasons. The Solar System consists of the Sun, eight planets, dwarf planets, asteroids, and comets.",
        "vi": "Mục một tổng kết chuyển động của các thiên thể: Trái Đất tự quay quanh trục nghiêng mỗi 24 giờ tạo nên ngày và đêm, và quay quanh Mặt Trời mỗi 365 ngày tạo nên bốn mùa. Hệ Mặt Trời bao gồm Mặt Trời, tám hành tinh, các hành tinh lùn, tiểu hành tinh và sao chổi."
    },
    {
        "id": "sec_orbital_motion",
        "title": "2. Tốc độ Quỹ đạo & Lực Hấp dẫn (Orbital Speed & Gravity Overview)",
        "selector": "#sec-orbital-motion",
        "en": "Section 2 calculates orbital speed v equals 2 pi r divided by orbital period T. Gravitational force provides the centripetal force keeping planets in elliptical orbits. Planets closer to the Sun experience stronger gravity and travel at higher orbital speeds.",
        "vi": "Mục hai tính tốc độ quỹ đạo v bằng 2 pi r chia chu kỳ quỹ đạo T. Lực hấp dẫn đóng vai trò lực hướng tâm giữ các hành tinh chuyển động trên quỹ đạo elip. Các hành tinh càng gần Mặt Trời chịu lực hút hấp dẫn càng mạnh nên chuyển động với tốc độ quỹ đạo càng lớn."
    },
    {
        "id": "sec_stars_universe",
        "title": "3. Các Ngôi sao & Sự Nở của Vũ trụ (Stars & The Universe Overview)",
        "selector": "#sec-stars-universe",
        "en": "Section 3 investigates stars: Nuclear fusion of hydrogen into helium powers stars during the stable main sequence. The Sun will eventually expand into a red giant and collapse into a white dwarf. Redshift of light from distant galaxies proves the universe is expanding from the Big Bang.",
        "vi": "Mục ba nghiên cứu các ngôi sao: Phản ứng nhiệt hạch tổng hợp hydro thành heli giải phóng năng lượng khổng lồ duy trì sự ổn định của ngôi sao trong giai đoạn dãy chính. Mặt Trời sau này sẽ nở thành sao khổng lồ đỏ rồi co lại thành sao lùn trắng. Hiện tượng dịch chuyển đỏ của ánh sáng từ các thiên hà xa xôi chứng minh vũ trụ đang không ngừng giãn nở từ vụ nổ lớn Big Bang."
    }
]

P6_MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 0, "title": "Giới thiệu Chuyên đề P6", "selector": "#sec-header"},
    "sec_earth_solar_system": {"start": 1, "end": 1, "title": "1. Trái Đất & Hệ Mặt Trời", "selector": "#sec-earth-solar-system"},
    "sec_orbital_motion": {"start": 2, "end": 2, "title": "2. Tốc độ Quỹ đạo & Trọng lực", "selector": "#sec-orbital-motion"},
    "sec_stars_universe": {"start": 3, "end": 3, "title": "3. Ngôi sao & Vũ trụ Giãn nở", "selector": "#sec-stars-universe"}
}


# =====================================================================
# PHYSICS BATCH PIPELINE
# =====================================================================
PHYSICS_LECTURES = [
    ("p1", "690ff013-5d01-4c1e-8546-25b3cd056e64", "P1: Motion, forces & energy", P1_SEGMENTS, P1_MAJOR_SECTIONS),
    ("p2", "dc33ed9d-e328-4f60-8c47-f0dbd103e8c1", "P2: Thermal physics", P2_SEGMENTS, P2_MAJOR_SECTIONS),
    ("p3", "eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8", "P3: Properties of waves", P3_SEGMENTS, P3_MAJOR_SECTIONS),
    ("p4", "2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69", "P4: Electricity and magnetism", P4_SEGMENTS, P4_MAJOR_SECTIONS),
    ("p5", "a6077865-db01-4785-9ec7-e8b0f531fcdc", "P5: Nuclear physics", P5_SEGMENTS, P5_MAJOR_SECTIONS),
    ("p6", "d11f8920-fe86-4cd4-ad9a-e8b669bc687b", "P6: Space physics", P6_SEGMENTS, P6_MAJOR_SECTIONS),
]

async def main():
    print("=====================================================================")
    print("STARTING AUDIO GENERATION FOR PHYSICS (P1 - P6)")
    print("=====================================================================")
    
    for code, lec_id, title, segments, majors in PHYSICS_LECTURES:
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

    print("\n🎉 ALL PHYSICS (P1-P6) AUDIO & MANIFESTS GENERATED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
