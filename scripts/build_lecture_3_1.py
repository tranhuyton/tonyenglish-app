import os
import sys
import re
import json
import asyncio
from bs4 import BeautifulSoup
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '3_1'
LECTURE_ID = '1b4caf37-15e4-475a-939c-e6490b366fd0'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '3.1 The Characteristics of the Antarctic Ecosystem'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 3.1: Hệ sinh thái Nam Cực",
        "selector": "#sec-header",
        "en": "Lesson 3.1: The Characteristics of the Antarctic Ecosystem. In this lesson, we explore Earth's southernmost continent, its extreme polar desert climate, its unique marine food web, and the remarkable adaptations of polar life.",
        "vi": "Bài ba chấm một: Đặc điểm của Hệ sinh thái Nam Cực. Trong bài học này, chúng ta sẽ khám phá lục địa cực nam của Trái Đất, khí hậu hoang mạc cực độ khắc nghiệt, lưới thức ăn biển độc đáo và những thích nghi sinh học phi thường của sinh vật vùng cực."
    },
    {
        "id": "sec_geography",
        "title": "Vị trí địa lý & Trữ lượng băng khổng lồ",
        "selector": "#sec-geography",
        "en": "Section 1: Geographic Location and Ice Reservoirs. Situated south of the Antarctic Circle and centered on the South Pole, Antarctica spans 14 million square kilometres, locking up 90 percent of the world's ice and 70 percent of all fresh water.",
        "vi": "Phần một: Vị trí địa lý và Trữ lượng băng khổng lồ. Nằm về phía nam Vòng Cực Nam và lấy Cực Nam làm trung tâm, Nam Cực trải rộng mười bốn triệu ki-lô-mét vuông, lưu giữ chín mươi phần trăm lượng băng và bảy mươi phần trăm lượng nước ngọt của toàn thế giới."
    },
    {
        "id": "map_south_pole",
        "title": "Cực Nam địa lý (90° Nam)",
        "selector": "#pt-south-pole",
        "en": "The Geographic South Pole. Situated at ninety degrees south on the polar plateau at an elevation of 2,835 metres. It experiences six continuous months of sunlight followed by six months of total polar darkness.",
        "vi": "Cực Nam địa lý. Tọa lạc tại chín mươi độ vĩ nam trên cao nguyên băng ở độ cao hai nghìn tám trăm ba mươi lăm mét. Nơi đây trải qua sáu tháng ban ngày liên tục và sáu tháng đêm cực hoàn toàn."
    },
    {
        "id": "map_vostok",
        "title": "Trạm Vostok: Cực lạnh Trái Đất",
        "selector": "#pt-vostok",
        "en": "Vostok Station, the Pole of Cold. Located deep in the interior at an altitude of nearly 3,500 metres. It holds the world record low temperature of minus 89.2 degrees Celsius recorded in July 1983.",
        "vi": "Trạm Vô-xtốc, cực lạnh của Trái Đất. Nằm sâu trong nội địa ở độ cao gần ba nghìn năm trăm mét. Nơi đây nắm giữ kỷ lục nhiệt độ tự nhiên thấp nhất hành tinh, âm tám mươi chín phẩy hai độ C ghi nhận vào tháng bảy năm một nghìn chín trăm tám mươi ba."
    },
    {
        "id": "map_rothera",
        "title": "Trạm nghiên cứu Rothera (Bán đảo)",
        "selector": "#pt-rothera",
        "en": "Rothera Research Station. Located on Adelaide Island off the Antarctic Peninsula, this modern hub operated by the British Antarctic Survey conducts cutting-edge marine and terrestrial biological research.",
        "vi": "Trạm nghiên cứu Rô-thê-ra. Nằm trên đảo A-đơ-lết ngoài khơi Bán đảo Nam Cực, trung tâm hiện đại này do Cục Khảo sát Nam Cực của Anh điều hành, chuyên nghiên cứu sinh học biển và khí hậu tiên tiến."
    },
    {
        "id": "map_mcmurdo",
        "title": "Trạm McMurdo: Cửa ngõ băng Ross",
        "selector": "#pt-mcmurdo",
        "en": "McMurdo Station. The largest human settlement in Antarctica, housing up to 1,200 scientists and support staff near the Ross Ice Shelf, acting as the primary logistical gateway for polar expeditions.",
        "vi": "Trạm Mác-Mơ-đô. Khu định cư lớn nhất tại Nam Cực, có thể chứa tới một nghìn hai trăm nhà khoa học và nhân viên hậu cần gần thềm băng Rốt, đóng vai trò là cửa ngõ hậu cần chính cho các chuyến thám hiểm địa cực."
    },
    {
        "id": "contrast_east_west",
        "title": "So sánh Đông Nam Cực và Tây Nam Cực",
        "selector": "#card-contrast-east-west",
        "en": "Contrast between East and West Antarctica. The East Antarctic Ice Sheet rests on high bedrock and holds 85 percent of all ice in stable cold. West Antarctica rests on bedrock below sea level, leaving its marine ice shelves dangerously vulnerable to warm ocean currents.",
        "vi": "So sánh giữa Đông và Tây Nam Cực. Dải băng Đông Nam Cực nằm trên nền đá lục địa trên cao và lưu giữ tám mươi lăm phần trăm tổng lượng băng ổn định. Ngược lại, Tây Nam Cực có đáy nằm dưới mực nước biển, khiến các thềm băng trôi nổi dễ bị tan chảy trước các dòng hải lưu ấm."
    },
    {
        "id": "sec_climate",
        "title": "Khí hậu cực độ & Bốn động lực nhiệt độ",
        "selector": "#sec-climate",
        "en": "Section 2: Extreme Polar Climate and Temperature Drivers. Antarctica is a hyper-arid cold desert averaging under fifty millimetres of annual precipitation in the interior. Four fundamental physical factors drive its extraordinary cold.",
        "vi": "Phần hai: Khí hậu cực độ và Bốn động lực nhiệt độ. Nam Cực là một hoang mạc lạnh siêu khô hạn với lượng mưa trung bình dưới năm mươi mi-li-mét một năm ở nội địa. Bốn yếu tố vật lý then chốt đã tạo nên cái lạnh tột cùng này."
    },
    {
        "id": "driver_insolation",
        "title": "1. Vĩ độ cao & Góc chiếu bức xạ thấp",
        "selector": "#card-driver-insolation",
        "en": "Low Solar Angle and Extreme Latitude. Solar rays strike at a very low oblique angle, spreading solar energy over a vast area while passing through a thick slice of absorbing atmosphere.",
        "vi": "Góc chiếu bức xạ thấp và Vĩ độ cực cao. Ánh sáng mặt trời chiếu tới mặt đất ở góc xiên rất thấp, làm phân tán năng lượng trên một diện tích rộng lớn đồng thời phải xuyên qua tầng khí quyển dày hấp thụ nhiệt."
    },
    {
        "id": "driver_albedo",
        "title": "2. Suất phản xạ Albedo cực cao (85-90%)",
        "selector": "#card-driver-albedo",
        "en": "Very High Albedo Effect. Pristine snow and ice reflect up to eighty-five to ninety percent of incoming solar radiation back into space, absorbing very little heat even during continuous summer daylight.",
        "vi": "Suất phản xạ An-bê-đô cực cao. Bề mặt băng tuyết nguyên sơ phản xạ tới tám mươi lăm đến chín mươi phần trăm bức xạ mặt trời trở lại vũ trụ, hấp thụ rất ít nhiệt ngay cả trong suốt mùa hè ngày trắng."
    },
    {
        "id": "driver_altitude",
        "title": "3. Độ cao địa hình cực lớn (Lapse Rate)",
        "selector": "#card-driver-altitude",
        "en": "Extreme Altitude and Lapse Rate Cooling. Antarctica is the highest continent on Earth, averaging 2,500 metres. Atmospheric temperature decreases by roughly one degree Celsius for every hundred metres gained.",
        "vi": "Độ cao địa hình cực lớn và Giảm nhiệt theo độ cao. Nam Cực là lục địa có độ cao trung bình lớn nhất thế giới, đạt hai nghìn năm trăm mét. Cứ lên cao một trăm mét, nhiệt độ không khí lại giảm khoảng một độ C."
    },
    {
        "id": "driver_katabatic",
        "title": "4. Áp cao cực & Gió Katabatic",
        "selector": "#card-driver-katabatic",
        "en": "Polar High Pressure and Katabatic Winds. Cold, dense air sinks over the interior plateau and rushes down gravitational slopes towards coasts as violent katabatic winds exceeding two hundred kilometres per hour.",
        "vi": "Áp cao cực và Gió Ca-ta-ba-tíc. Không khí lạnh và đặc chìm xuống trên cao nguyên nội địa, sau đó trôi dốc với vận tốc khủng khiếp hướng ra bờ biển tạo thành các cơn gió Ca-ta-ba-tíc hung dữ vượt quá hai trăm ki-lô-mét một giờ."
    },
    {
        "id": "wind_chill",
        "title": "Hiệu ứng phong hàn (Wind Chill Effect)",
        "selector": "#card-wind-chill",
        "en": "The Wind Chill Effect. Table 3.1 demonstrates that high winds strip body heat exponentially. At minus ten degrees Celsius with a gale-force wind of twenty metres per second, the effective chill temperature plunges to minus thirty-three degrees, freezing skin in sixty seconds.",
        "vi": "Hiệu ứng phong hàn. Bảng ba chấm một cho thấy gió mạnh cuốn đi nhiệt lượng cơ thể theo cấp số nhân. Ở mức âm mười độ C kèm gió bão hai mươi mét một giây, nhiệt độ cảm nhận giảm xuống tới âm ba mươi ba độ, làm đóng băng da thịt trần chỉ trong sáu mươi giây."
    },
    {
        "id": "sec_food_web",
        "title": "Lưới thức ăn biển & Loài chủ chốt Krill",
        "selector": "#sec-food-web",
        "en": "Section 3: Marine Food Web and Keystone Species. The frigid Southern Ocean is remarkably fertile due to cold-water gas retention and nutrient upwelling. The entire marine ecosystem is anchored by a critically short trophic food web.",
        "vi": "Phần ba: Lưới thức ăn biển và Loài chủ chốt. Vùng biển Nam Đại Dương lạnh giá cực kỳ màu mỡ nhờ khả năng hòa tan khí cao và dòng nước trồi giàu dinh dưỡng. Toàn bộ hệ sinh thái biển được nâng đỡ bởi một chuỗi thức ăn ngắn đặc biệt."
    },
    {
        "id": "web_primary_producers",
        "title": "Sinh vật sản xuất: Tảo băng & Thực vật phù du",
        "selector": "#node-primary-producers",
        "en": "Primary Producers. Microscopic diatoms and ice algae bloom beneath melting sea ice in spring, utilizing twenty-four hours of summer sunlight to fuel all Antarctic marine life.",
        "vi": "Sinh vật sản xuất sơ cấp. Tảo cát hiển vi và tảo đáy băng sinh sôi bùng nổ dưới các lớp băng biển tan vào mùa xuân, tận dụng hai mươi bốn giờ ánh sáng mùa hè để nuôi sống toàn bộ sinh vật biển Nam Cực."
    },
    {
        "id": "web_krill",
        "title": "Antarctic Krill: Loài chủ chốt (Keystone Species)",
        "selector": "#node-krill",
        "en": "Antarctic Krill, the Keystone Species. Small crustaceans with an astounding biomass of four hundred to five hundred million tonnes. They feed directly on ice algae and form the central pillar of the entire polar food web.",
        "vi": "Nhuyễn thể Nam Cực, loài sinh vật chủ chốt. Những sinh vật giáp xác nhỏ bé với sinh khối đáng kinh ngạc từ bốn trăm đến năm trăm triệu tấn. Chúng ăn tảo băng và tạo thành trụ cột trung tâm nuôi sống toàn bộ mạng lưới sinh vật."
    },
    {
        "id": "web_secondary",
        "title": "Sinh vật tiêu thụ bậc hai: Cá & Mực",
        "selector": "#node-secondary-consumers",
        "en": "Secondary Consumers. Antarctic toothfish, cod, and glacial squid feed on krill, surviving freezing water through specialized antifreeze blood proteins, serving as vital prey for larger marine animals.",
        "vi": "Sinh vật tiêu thụ bậc hai. Cá tuyết Nam Cực, cá răng và mực biển ăn nhuyễn thể, sống sót trong nước biển đóng băng nhờ các phân tử protein chống đông trong máu, là con mồi quan trọng của các loài thú biển."
    },
    {
        "id": "web_higher",
        "title": "Cá voi tấm sừng & Lối tắt năng lượng (Bypass)",
        "selector": "#node-higher-consumers",
        "en": "Baleen Whales and Higher Consumers. Giant Blue, Humpback, and Minke whales bypass intermediary trophic levels, filtering krill directly through baleen plates. This two-step chain preserves ninety percent of trophic energy.",
        "vi": "Cá voi tấm sừng và Lối tắt năng lượng trực tiếp. Các loài cá voi khổng lồ như cá voi xanh, cá voi lưng gù lọc ăn nhuyễn thể trực tiếp qua các tấm sừng. Chuỗi thức ăn ngắn hai bậc này giữ lại tới chín mươi phần trăm năng lượng sơ cấp."
    },
    {
        "id": "web_apex",
        "title": "Động vật săn mồi đỉnh cao: Hải cẩu báo & Cá voi sát thủ",
        "selector": "#node-apex-predators",
        "en": "Apex Predators. Leopard seals hunt penguins and smaller seals along the ice edge, while pods of highly intelligent Orcas dominate open waters as supreme apex predators with zero natural enemies.",
        "vi": "Động vật săn mồi đỉnh cao. Hải cẩu báo săn chim cánh cụt và hải cẩu nhỏ dọc theo rìa băng, trong khi các đàn cá voi sát thủ thông minh thống trị vùng nước mở với tư cách là chúa tể săn mồi không có thiên địch tự nhiên."
    },
    {
        "id": "krill_keystone",
        "title": "Tầm quan trọng sống còn của loài chủ chốt Krill",
        "selector": "#card-krill-keystone",
        "en": "Significance of Antarctic Krill as a Keystone Organism. Krill bridges microscopic algae to gigantic whales and birds. Any disruption to krill populations from warming sea ice or overharvesting reverberates catastrophically through every higher trophic level.",
        "vi": "Tầm quan trọng sống còn của loài chủ chốt. Nhuyễn thể là cây cầu nối liền tảo hiển vi với những loài cá voi và chim biển khổng lồ. Bất kỳ sự suy giảm nào của loài này do mất băng biển hay đánh bắt quá mức đều gây ra sự sụp đổ thảm khốc cho các bậc dinh dưỡng cao hơn."
    },
    {
        "id": "sec_adaptations",
        "title": "Thích nghi sinh học: Sinh tồn nơi băng giá",
        "selector": "#sec-adaptations",
        "en": "Section 4: Evolutionary Adaptations to Deep Cold. Polar organisms display remarkable anatomical, physiological, and behavioral adaptations to prevent cell rupture and survive sub-zero blizzards.",
        "vi": "Phần bốn: Những thích nghi sinh học để sinh tồn nơi băng giá. Các loài sinh vật vùng cực thể hiện những thích nghi phi thường về cấu tạo, sinh lý và tập tính để ngăn tế bào bị đóng băng và chống chọi lại những trận bão tuyết."
    },
    {
        "id": "adapt_emperor",
        "title": "Chim cánh cụt Hoàng đế (Emperor Penguin)",
        "selector": "#card-adapt-emperor",
        "en": "The Emperor Penguin. Males survive winter blizzards through tight social huddles where central temperatures reach thirty-seven degrees. They possess subcutaneous blubber up to three centimetres thick and counter-current heat exchange systems.",
        "vi": "Chim cánh cụt Hoàng đế. Con trống vượt qua bão tuyết mùa đông nhờ tập tính tụ họp thành khối dày đặc, nơi nhiệt độ trung tâm đạt tới ba mươi bảy độ C. Chúng sở hữu lớp mỡ dày ba xăng-ti-mét cùng hệ thống trao đổi nhiệt ngược dòng ở các chi."
    },
    {
        "id": "adapt_weddell",
        "title": "Hải cẩu Weddell (Weddell Seal)",
        "selector": "#card-adapt-weddell",
        "en": "The Weddell Seal. Living furthest south, they continually scrape ice breathing holes open using specialized teeth. Their blubber accounts for over thirty percent of body weight, and diving bradycardia slows heart rates down to sixteen beats per minute.",
        "vi": "Hải cẩu Oét-đen. Sống ở vĩ độ nam xa nhất, chúng liên tục dùng răng cạo băng để duy trì các lỗ thở trong mùa đông. Lớp mỡ dày chiếm hơn ba mươi phần trăm trọng lượng cơ thể, và phản xạ lặn sâu giúp giảm nhịp tim xuống chỉ còn mười sáu nhịp một phút."
    },
    {
        "id": "adapt_icefish",
        "title": "Cá băng Nam Cực (Antarctic Icefish)",
        "selector": "#card-adapt-icefish",
        "en": "Antarctic Icefish. Their blood contains natural antifreeze glycoproteins that stop microscopic ice crystals from growing. Uniquely, they lack red blood cells, absorbing dissolved oxygen directly through transparent blood plasma.",
        "vi": "Cá băng Nam Cực. Máu của chúng chứa các phân tử protein chống đông tự nhiên, ngăn chặn sự kết tinh của các tinh thể băng hiển vi. Đặc biệt, chúng không hề có hồng cầu, oxy được hòa tan trực tiếp vào huyết tương trong suốt."
    },
    {
        "id": "adapt_flora",
        "title": "Thực vật cực địa & Địa y sống trong đá",
        "selector": "#card-adapt-flora",
        "en": "Terrestrial Flora and Endolithic Lichens. Only two vascular flowering plant species survive on the peninsula. Lichens grow inside the microscopic pores of translucent sandstone rocks, sheltered from lethal drying winds while capturing sunlight.",
        "vi": "Thực vật cực địa và Địa y nội sinh. Chỉ có hai loài thực vật có hoa sinh tồn được ở rìa bán đảo. Địa y phát triển bên trong các khe nứt hiển vi của đá sa thạch, được đá che chắn khỏi gió lạnh làm khô trong khi vẫn hấp thụ ánh sáng để quang hợp."
    },
    {
        "id": "sec_seasonal_cycles",
        "title": "Chu kỳ mùa cực đoan & Sự biến động của Băng biển",
        "selector": "#sec-seasonal-cycles",
        "en": "Section 5: Extreme Seasonal Cycles and Sea Ice Dynamics. Driven by Earth's axial tilt, Antarctica undergoes dramatic oscillations between continuous summer daylight and total winter darkness.",
        "vi": "Phần năm: Chu kỳ mùa cực đoan và Biến động của Băng biển. Do độ nghiêng của trục Trái Đất, Nam Cực dao động mạnh mẽ giữa mùa hè ngày trắng liên tục và mùa đông đêm cực hoàn toàn."
    },
    {
        "id": "season_summer",
        "title": "Mùa hè Nam bán cầu: Bùng nổ sinh học",
        "selector": "#card-season-summer",
        "en": "Austral Summer. Continuous twenty-four hour polar daylight melts sea ice down to three million square kilometres. Massive phytoplankton blooms trigger explosive krill breeding, welcoming millions of migratory whales, seals, and birds.",
        "vi": "Mùa hè Nam bán cầu. Hai mươi bốn giờ ánh sáng ngày cực làm tan băng biển xuống mức tối thiểu khoảng ba triệu ki-lô-mét vuông. Tảo sinh sôi bùng nổ kéo theo sự sinh sản của nhuyễn thể, chào đón hàng triệu cá voi, hải cẩu và chim di cư đổ về."
    },
    {
        "id": "season_winter",
        "title": "Mùa đông Nam bán cầu: Lục địa nhân đôi diện tích",
        "selector": "#card-season-winter",
        "en": "Austral Winter. Total darkness shrouds the continent for six months. Rapid ocean freezing expands sea ice to twenty million square kilometres, doubling Antarctica's apparent size and causing a mass migration of wildlife north.",
        "vi": "Mùa đông Nam bán cầu. Đêm cực tối tăm bao trùm lục địa suốt sáu tháng. Nước biển đóng băng nhanh chóng mở rộng diện tích băng biển lên tới hai mươi triệu ki-lô-mét vuông, làm nhân đôi diện tích bề mặt biểu kiến của Nam Cực và thúc đẩy cuộc di cư lớn ra phương bắc."
    },
    {
        "id": "summary_human",
        "title": "Tổng kết thi IGCSE & Dấu chân con người",
        "selector": "#card-summary-human",
        "en": "IGCSE Core Summary. Antarctica has no permanent native indigenous population. Human presence is strictly confined to scientific researchers and support crews, numbering around five thousand in summer and under one thousand in winter.",
        "vi": "Tổng kết thi và Dấu ấn nhân loại. Nam Cực không có cư dân bản địa sinh sống lâu dài. Sự hiện diện của con người hoàn toàn giới hạn trong giới nghiên cứu khoa học và đội ngũ hỗ trợ, khoảng năm nghìn người vào mùa hè và dưới một nghìn người vào mùa đông."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 6},
    "sec_geography": {"start": 1, "end": 6},
    "sec_climate": {"start": 7, "end": 12},
    "sec_food_web": {"start": 13, "end": 19},
    "sec_adaptations": {"start": 20, "end": 24},
    "sec_seasonal_cycles": {"start": 25, "end": 28}
}

def transform_html(raw_html):
    # Add id & data-lecture-section attributes
    html = raw_html
    
    # 1. Header
    html = re.sub(
        r'(<div style="display:flex; gap:8px; align-items:center; margin-bottom:12px;">[\s\S]*?)(<h1 style="[^"]*">)',
        r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; border-radius:12px; padding:12px 16px; margin-bottom:16px; transition:all 0.2s ease;">\1\2',
        html, count=1
    )
    # close after key learning objectives
    html = re.sub(
        r'(🎯 Key Learning Objectives[\s\S]*?</ul>\s*</div>)',
        r'\1</div>',
        html, count=1
    )
    
    # 2. Section 1: Geography
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*1\. Geographic Location & Ice Reservoirs\s*</h2>)',
        r'<div id="sec-geography" class="lecture-interactive-card" data-lecture-section="sec_geography" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*2\. Extreme Polar Climate)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Map points in SVG
    html = html.replace('<g class="polar-point" transform="translate(470, 320)">', '<g id="pt-south-pole" class="polar-point" data-lecture-section="map_south_pole" style="cursor:pointer;" transform="translate(470, 320)">')
    html = html.replace('<g class="polar-point" transform="translate(560, 240)">', '<g id="pt-vostok" class="polar-point" data-lecture-section="map_vostok" style="cursor:pointer;" transform="translate(560, 240)">')
    html = html.replace('<g class="polar-point" transform="translate(265, 205)">', '<g id="pt-rothera" class="polar-point" data-lecture-section="map_rothera" style="cursor:pointer;" transform="translate(265, 205)">')
    html = html.replace('<g class="polar-point" transform="translate(420, 485)">', '<g id="pt-mcmurdo" class="polar-point" data-lecture-section="map_mcmurdo" style="cursor:pointer;" transform="translate(420, 485)">')
    
    # Deep dive: East vs West
    html = html.replace(
        '<div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:18px; margin:20px 0;">\n        <h3 style="margin:0 0 10px 0; color:#0f172a; font-size:17px; font-weight:700;">⚖️ Contrast: East vs. West Antarctica</h3>',
        '<div id="card-contrast-east-west" class="lecture-interactive-card" data-lecture-section="contrast_east_west" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:10px; padding:18px; margin:20px 0; cursor:pointer;">\n        <h3 style="margin:0 0 10px 0; color:#0f172a; font-size:17px; font-weight:700;">⚖️ Contrast: East vs. West Antarctica</h3>'
    )
    
    # 3. Section 2: Climate
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*2\. Extreme Polar Climate & Temperature Drivers\s*</h2>)',
        r'<div id="sec-climate" class="lecture-interactive-card" data-lecture-section="sec_climate" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*3\. Marine Food Web)',
        r'</div>\1\2',
        html, count=1
    )
    
    # 4 Drivers
    html = html.replace(
        '<strong style="color:#1d4ed8; font-size:15px;">1. Extreme Latitude & Low Insolation Angle</strong>',
        '</span><div id="card-driver-insolation" class="lecture-interactive-card" data-lecture-section="driver_insolation" style="cursor:pointer; padding:6px; border-radius:6px;"><strong style="color:#1d4ed8; font-size:15px;">1. Extreme Latitude & Low Insolation Angle</strong>'
    )
    html = html.replace(
        '<strong style="color:#1d4ed8; font-size:15px;">2. Very High Albedo Effect (80-90% Reflection)</strong>',
        '</span><div id="card-driver-albedo" class="lecture-interactive-card" data-lecture-section="driver_albedo" style="cursor:pointer; padding:6px; border-radius:6px;"><strong style="color:#1d4ed8; font-size:15px;">2. Very High Albedo Effect (80-90% Reflection)</strong>'
    )
    html = html.replace(
        '<strong style="color:#1d4ed8; font-size:15px;">3. Extreme Altitude (Lapse Rate Cooling)</strong>',
        '</span><div id="card-driver-altitude" class="lecture-interactive-card" data-lecture-section="driver_altitude" style="cursor:pointer; padding:6px; border-radius:6px;"><strong style="color:#1d4ed8; font-size:15px;">3. Extreme Altitude (Lapse Rate Cooling)</strong>'
    )
    html = html.replace(
        '<strong style="color:#1d4ed8; font-size:15px;">4. Polar High Pressure & Katabatic Winds</strong>',
        '</span><div id="card-driver-katabatic" class="lecture-interactive-card" data-lecture-section="driver_katabatic" style="cursor:pointer; padding:6px; border-radius:6px;"><strong style="color:#1d4ed8; font-size:15px;">4. Polar High Pressure & Katabatic Winds</strong>'
    )
    
    # Wind Chill table card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; margin:24px 0;">\n        <div style="background:#0284c7;',
        '<div id="card-wind-chill" class="lecture-interactive-card" data-lecture-section="wind_chill" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; margin:24px 0; cursor:pointer;">\n        <div style="background:#0284c7;'
    )
    
    # 4. Section 3: Food Web
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*3\. Marine Food Web & Keystone Species\s*</h2>)',
        r'<div id="sec-food-web" class="lecture-interactive-card" data-lecture-section="sec_food_web" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*4\. Evolutionary Adaptations)',
        r'</div>\1\2',
        html, count=1
    )
    
    # SVG food web nodes
    html = html.replace('<g class="web-node" transform="translate(330, 545)"', '<g id="node-primary-producers" class="web-node" data-lecture-section="web_primary_producers" transform="translate(330, 545)"')
    html = html.replace('<g class="web-node" transform="translate(350, 430)"', '<g id="node-krill" class="web-node" data-lecture-section="web_krill" transform="translate(350, 430)"')
    html = html.replace('<g class="web-node" transform="translate(210, 315)"', '<g id="node-secondary-consumers" class="web-node" data-lecture-section="web_secondary" transform="translate(210, 315)"')
    html = html.replace('<g class="web-node" transform="translate(680, 185)"', '<g id="node-higher-consumers" class="web-node" data-lecture-section="web_higher" transform="translate(680, 185)"')
    html = html.replace('<g class="web-node" transform="translate(490, 50)"', '<g id="node-apex-predators" class="web-node" data-lecture-section="web_apex" transform="translate(490, 50)"')
    
    # Keystone card
    html = html.replace(
        '<div style="background:#f0fdf4; border-left:4px solid #16a34a; border-radius:8px; padding:16px; margin:20px 0;">\n        <h4 style="margin:0 0 8px 0; color:#166534; font-size:16px; font-weight:700;">🦐 Why is Antarctic Krill a "Keystone Species"?</h4>',
        '<div id="card-krill-keystone" class="lecture-interactive-card" data-lecture-section="krill_keystone" style="background:#f0fdf4; border-left:4px solid #16a34a; border-radius:8px; padding:16px; margin:20px 0; cursor:pointer;">\n        <h4 style="margin:0 0 8px 0; color:#166534; font-size:16px; font-weight:700;">🦐 Why is Antarctic Krill a "Keystone Species"?</h4>'
    )
    
    # 5. Section 4: Adaptations
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*4\. Evolutionary Adaptations: Surviving the Deep Freeze\s*</h2>)',
        r'<div id="sec-adaptations" class="lecture-interactive-card" data-lecture-section="sec_adaptations" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 5
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*5\. Extreme Seasonal Cycles)',
        r'</div>\1\2',
        html, count=1
    )
    
    # 4 adapt cards
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🐧 Emperor Penguin (Aptenodytes forsteri)</div>',
        '<div id="card-adapt-emperor" class="lecture-interactive-card" data-lecture-section="adapt_emperor" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🐧 Emperor Penguin (Aptenodytes forsteri)</div>'
    )
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🦭 Weddell Seal (Leptonychotes weddellii)</div>',
        '<div id="card-adapt-weddell" class="lecture-interactive-card" data-lecture-section="adapt_weddell" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🦭 Weddell Seal (Leptonychotes weddellii)</div>'
    )
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🐟 Antarctic Icefish (Channichthyidae)</div>',
        '<div id="card-adapt-icefish" class="lecture-interactive-card" data-lecture-section="adapt_icefish" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🐟 Antarctic Icefish (Channichthyidae)</div>'
    )
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🌿 Terrestrial Flora & Lichens</div>',
        '<div id="card-adapt-flora" class="lecture-interactive-card" data-lecture-section="adapt_flora" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#0f172a; margin-bottom:8px;">🌿 Terrestrial Flora & Lichens</div>'
    )
    
    # 6. Section 5: Seasonal Cycles
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*5\. Extreme Seasonal Cycles & Sea Ice Expansion\s*</h2>)',
        r'<div id="sec-seasonal-cycles" class="lecture-interactive-card" data-lecture-section="sec_seasonal_cycles" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#854d0e; margin-bottom:6px;">☀️ Austral Summer (November – February)</div>',
        '<div id="card-season-summer" class="lecture-interactive-card" data-lecture-section="season_summer" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#854d0e; margin-bottom:6px;">☀️ Austral Summer (November – February)</div>'
    )
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#1e293b; margin-bottom:6px;">🌙 Austral Winter (June – August)</div>',
        '<div id="card-season-winter" class="lecture-interactive-card" data-lecture-section="season_winter" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#1e293b; margin-bottom:6px;">🌙 Austral Winter (June – August)</div>'
    )
    
    # Close section 5 before Case Study Spotlight
    html = re.sub(
        r'(\s*)(<!-- Case Study Spotlight Box -->)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Summary box
    html = html.replace(
        '<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:24px 0;">\n        <h4 style="margin:0 0 6px 0; color:#1e40af; font-size:16px; font-weight:700;">📌 IGCSE Exam Tip & Case Study Fact</h4>',
        '<div id="card-summary-human" class="lecture-interactive-card" data-lecture-section="summary_human" style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;">\n        <h4 style="margin:0 0 6px 0; color:#1e40af; font-size:16px; font-weight:700;">📌 IGCSE Exam Tip & Case Study Fact</h4>'
    )
    
    return html

async def main():
    # 1. Process audio & manifest
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )
    
    # 2. Transform HTML
    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
    
    new_html = transform_html(raw_html)
    
    # Save transformed HTML locally for inspection
    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")
    
    # 3. Update Supabase
    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == '__main__':
    asyncio.run(main())
