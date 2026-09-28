import asyncio
import os
import re
from pathlib import Path
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "5_1"
LECTURE_ID = "7c30919a-5d22-425a-a167-21e5de07d203"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "5.1 The Natural and Human Causes of Climate Change"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Introduction to Climate Change",
        "en": "Welcome to Topic 5.1: The Natural and Human Causes of Climate Change. In this lecture, we investigate the fundamental mechanisms driving Earth's climate system. We distinguish weather from climate, analyze geological and instrumental evidence, unpick Milankovitch orbital cycles and volcanic cooling, and examine the physics of the human-enhanced greenhouse effect.",
        "vi": "Chào mừng các em đến với bài năm chấm một: Các nguyên nhân tự nhiên và nhân tạo của biến đổi khí hậu. Trong bài giảng này, chúng ta sẽ khảo sát các cơ chế nền tảng điều khiển hệ thống khí hậu Trái Đất. Chúng ta sẽ phân biệt thời tiết và khí hậu, phân tích các bằng chứng địa chất và quan trắc thực tế, tìm hiểu chu kỳ quỹ đạo và làm mát do núi lửa, đồng thời khám phá bản chất vật lý của hiệu ứng nhà kính tăng cường do con người gây ra."
    },
    {
        "id": "sec_weather_climate",
        "title": "1. Weather, Climate & Climate Change Definitions",
        "en": "Section 1 establishes core scientific definitions. Weather describes the day-to-day conditions of the atmosphere at a specific place and time, such as temperature, precipitation, and wind. Climate is the long-term statistical average of weather over a standardized period of at least thirty consecutive years. Climate change is a statistically significant, sustained shift in mean climate or climate variability persisting over decades or longer.",
        "vi": "Mục một thiết lập các định nghĩa khoa học cốt lõi. Thời tiết mô tả các trạng thái diễn ra từng ngày của khí quyển tại một địa điểm và thời điểm cụ thể, như nhiệt độ, lượng mưa và gió. Khí hậu là giá trị trung bình thống kê dài hạn của thời tiết trong một khoảng thời gian chuẩn hóa ít nhất ba mươi năm liên tục. Còn biến đổi khí hậu là sự thay đổi đáng kể và kéo dài về trạng thái trung bình hoặc mức độ dao động của khí hậu, duy trì qua nhiều thập kỷ hoặc dài hơn."
    },
    {
        "id": "def_weather",
        "title": "Weather Concept",
        "en": "Weather refers to dynamic, short-term atmospheric states. It fluctuates hour by hour and day by day, influenced by moving high and low-pressure air masses, fronts, and local geography.",
        "vi": "Thời tiết biểu thị các trạng thái khí quyển ngắn hạn và luôn biến động. Nó thay đổi theo từng giờ và từng ngày dưới ảnh hưởng của các khối khí áp cao, áp thấp, frông thời tiết và địa hình địa phương."
    },
    {
        "id": "def_climate",
        "title": "Climate Concept (30-Year Baseline)",
        "en": "Climate requires at least thirty years of continuous meteorological data. This standard baseline smooths out temporary annual extremes, enabling geographers to establish true expected regional averages and seasonal patterns.",
        "vi": "Khí hậu đòi hỏi chuỗi số liệu khí tượng liên tục trong ít nhất ba mươi năm. Mốc chuẩn này giúp loại bỏ các hiện tượng cực đoan tạm thời hàng năm, giúp các nhà địa lý xác định chính xác mức trung bình khu vực và các quy luật theo mùa."
    },
    {
        "id": "def_climate_change",
        "title": "Climate Change Definition",
        "en": "Climate change represents a statistically robust trend that departs permanently or semi-permanently from established long-term averages, whether driven by natural astronomical cycles or anthropogenic forcing.",
        "vi": "Biến đổi khí hậu thể hiện một xu hướng thay đổi rõ rệt về mặt thống kê, lệch hẳn khỏi các mức trung bình dài hạn đã được thiết lập, dù nguyên nhân do chu kỳ thiên văn tự nhiên hay do tác động của con người."
    },
    {
        "id": "sec_evidence",
        "title": "2. Empirical Evidence for Global Climate Change",
        "en": "Section 2 reviews multiple independent lines of observational evidence. Instrumental records demonstrate that global surface temperatures have risen by one point one to one point two degrees Celsius since pre-industrial times. The past decade has recorded the highest global average temperatures since systematic thermometer records began in 1880.",
        "vi": "Mục hai tổng hợp các bằng chứng quan trắc độc lập. Số liệu đo đạc thực tế chỉ ra nhiệt độ bề mặt toàn cầu đã tăng khoảng một phẩy một đến một phẩy hai độ C kể từ thời kỳ tiền công nghiệp. Thập kỷ vừa qua ghi nhận mức nhiệt trung bình toàn cầu cao nhất kể từ khi hệ thống đo đạc bằng nhiệt kế bắt đầu từ năm 1880."
    },
    {
        "id": "evidence_ice_cores",
        "title": "Ice Core Proxies (800,000 Year Record)",
        "en": "Antarctic and Greenland ice cores trap ancient atmospheric gas bubbles. For eight hundred thousand years across glacial and interglacial cycles, carbon dioxide naturally oscillated between 180 and 280 parts per million. Following industrialization, carbon dioxide abruptly spiked past 420 parts per million, proving modern concentrations are unprecedented in human history.",
        "vi": "Các lõi băng ở Nam Cực và đảo Grin-lân lưu giữ những bọt khí cổ đại trong khí quyển. Suốt tám trăm nghìn năm qua qua các chu kỳ băng hà và gian băng, nồng độ khí các-bô-níc dao động tự nhiên trong khoảng một trăm tám mươi đến hai trăm tám mươi phần triệu. Nhưng sau khi công nghiệp hóa bắt đầu, nồng độ này đã vọt qua mốc bốn trăm hai mươi phần triệu, chứng minh mức độ hiện nay là chưa từng có trong lịch sử loài người."
    },
    {
        "id": "evidence_arctic_sea_ice",
        "title": "Arctic Sea Ice Decline",
        "en": "Satellite telemetry reveals that Arctic sea ice extent at its September minimum has contracted by over twelve percent per decade since 1979. Thick multi-year sea ice is being replaced by fragile, thin seasonal ice.",
        "vi": "Dữ liệu vệ tinh chỉ ra diện tích băng biển Bắc Cực vào thời điểm tối thiểu tháng chín đã sụt giảm hơn mười hai phần trăm mỗi thập kỷ kể từ năm 1979. Lớp băng vĩnh cửu dày nhiều năm đang dần bị thay thế bởi lớp băng mỏng chỉ tồn tại theo mùa."
    },
    {
        "id": "evidence_historical_proxies",
        "title": "Historical Proxies & Little Ice Age",
        "en": "Historical records, agricultural harvest dates, and artwork provide cultural climate proxies. Pieter Bruegel's famous painting, The Hunters in the Snow from 1565, documents harsh frozen conditions in Western Europe during the Little Ice Age between 1300 and 1850.",
        "vi": "Ghi chép lịch sử, thời gian thu hoạch mùa màng và các tác phẩm nghệ thuật cung cấp bằng chứng gián tiếp về khí hậu trong quá khứ. Bức tranh nổi tiếng Thợ săn trong tuyết vẽ năm 1565 đã ghi lại điều kiện băng giá khắc nghiệt tại Tây Âu trong thời kỳ tiểu băng hà kéo dài từ năm 1300 đến năm 1850."
    },
    {
        "id": "sec_natural_drivers",
        "title": "3. Natural Drivers of Climate Change",
        "en": "Section 3 examines natural climate drivers. Throughout the Quaternary period, Earth naturally cycled between glacial ice ages and warm interglacials. The pacing of these long cycles is governed by Milankovitch orbital mechanics, punctuated by volcanic eruptions and solar variations.",
        "vi": "Mục ba xem xét các yếu tố tự nhiên thúc đẩy biến đổi khí hậu. Trong suốt kỷ Đệ Tứ, Trái Đất liên tục trải qua các chu kỳ tự nhiên giữa các thời kỳ băng hà lạnh giá và các thời kỳ gian băng ấm áp. Nhịp điệu của các chu kỳ dài này được điều khiển bởi quỹ đạo của Trái Đất, kết hợp với các đợt phun trào núi lửa và biến thiên năng lượng Mặt Trời."
    },
    {
        "id": "milan_eccentricity",
        "title": "Milankovitch Cycle 1: Eccentricity (~100,000 Years)",
        "en": "Eccentricity describes the cyclical stretching of Earth's orbit from nearly circular to slightly elliptical over roughly one hundred thousand years. In high eccentricity, Earth receives twenty-three percent more solar radiation at perihelion than at aphelion, pacing major glacial-interglacial cycles.",
        "vi": "Độ lệch tâm mô tả sự biến đổi hình dạng quỹ đạo Trái Đất từ gần tròn sang hình elip dẹt theo chu kỳ khoảng một trăm nghìn năm. Khi quỹ đạo dẹt nhất, Trái Đất nhận được nhiều bức xạ Mặt Trời hơn hai mươi ba phần trăm ở điểm cận nhật so với điểm viễn nhật, tạo ra nhịp điệu cho các chu kỳ băng hà lớn."
    },
    {
        "id": "milan_obliquity",
        "title": "Milankovitch Cycle 2: Obliquity (~41,000 Years)",
        "en": "Obliquity is the variation in Earth's axial tilt between 22.1 and 24.5 degrees every forty-one thousand years. A smaller tilt produces milder winters and cooler summers, preventing polar snow from melting and initiating ice sheet expansion.",
        "vi": "Độ nghiêng trục tự quay biến đổi trong khoảng hai mươi hai phẩy một đến hai mươi tư phẩy năm độ theo chu kỳ bốn mươi mốt nghìn năm. Khi góc nghiêng nhỏ hơn, mùa đông bớt giá buốt và mùa hè mát mẻ hơn, khiến tuyết ở vùng cực không kịp tan vào mùa hè và bắt đầu hình thành nên các dải băng lục địa."
    },
    {
        "id": "milan_precession",
        "title": "Milankovitch Cycle 3: Precession (~23,000 Years)",
        "en": "Precession is the slow wobble of Earth's axis like a spinning top over nineteen to twenty-three thousand years. This wobble alters which hemisphere experiences summer closest to the Sun, shifting regional seasonal extremes over millennia.",
        "vi": "Hiện tượng tiến động là sự lắc lư chậm của trục quay Trái Đất giống như một con quay, diễn ra trong khoảng mười chín nghìn đến hai mươi ba nghìn năm. Sự lắc lư này làm thay đổi thời điểm bán cầu nào trải qua mùa hè khi ở gần Mặt Trời nhất, làm thay đổi mức độ khắc nghiệt của các mùa qua hàng thiên niên kỷ."
    },
    {
        "id": "volcanic_cooling",
        "title": "Volcanic Eruptions & Sulfate Aerosols",
        "en": "Violent explosive eruptions inject millions of tons of sulfur dioxide straight into the stratosphere. There, it forms highly reflective sulfate aerosols that scatter incoming solar radiation back into space, causing global temporary cooling of half a degree Celsius for one to three years, as seen after Mount Pinatubo in 1991.",
        "vi": "Các vụ phun trào núi lửa dữ dội đẩy hàng triệu tấn khí lưu huỳnh đi-ô-xít thẳng lên tầng bình lưu. Tại đây, nó phản ứng tạo thành các hạt sương son khí sun-phát phản xạ mạnh bức xạ Mặt Trời ngược vào không gian, gây ra hiện tượng làm mát toàn cầu giảm khoảng không phẩy năm độ C trong một đến ba năm, điển hình như sau vụ núi lửa Pi-na-tu-bo năm 1991."
    },
    {
        "id": "sec_human_causes",
        "title": "4. The Enhanced Greenhouse Effect (EGHE)",
        "en": "Section 4 contrasts the natural greenhouse effect with human-induced enhanced warming. Naturally, atmospheric gases trap infrared heat to keep Earth at a hospitable fifteen degrees Celsius. Human emissions thicken this thermal blanket, trapping excess heat and forcing mean global temperatures upward.",
        "vi": "Mục bốn phân biệt giữa hiệu ứng nhà kính tự nhiên và hiện tượng nóng lên do con người làm gia tăng. Trong tự nhiên, các chất khí giữ lại nhiệt hồng ngoại để duy trì Trái Đất ở mức nhiệt độ thuận lợi khoảng mười lăm độ C. Nhưng khí thải nhân tạo đã làm lớp chăn giữ nhiệt này dày lên đáng kể, giữ lại quá nhiều nhiệt và đẩy nhiệt độ trung bình toàn cầu tăng lên."
    },
    {
        "id": "gh_natural",
        "title": "Natural Greenhouse Effect Baseline (+15°C)",
        "en": "Under natural conditions, water vapor, carbon dioxide, and methane absorb part of the outgoing terrestrial infrared heat, maintaining a global average surface temperature of fifteen degrees Celsius. Without this natural insulation, Earth would freeze at minus eighteen degrees Celsius.",
        "vi": "Dưới điều kiện tự nhiên, hơi nước, khí các-bô-níc và mê-tan hấp thụ một phần nhiệt hồng ngoại do mặt đất phát ra, duy trì nhiệt độ trung bình toàn cầu ở mức mười lăm độ C. Nếu không có lớp cách nhiệt tự nhiên này, Trái Đất sẽ đóng băng ở âm mười tám độ C."
    },
    {
        "id": "gh_enhanced",
        "title": "Enhanced Greenhouse Effect (+16.2°C)",
        "en": "The enhanced greenhouse effect occurs because burning fossil fuels and deforestation increase greenhouse gas concentrations. Less longwave heat escapes into space, and intense back-radiation warms the atmosphere and oceans, driving rapid contemporary climate disruption.",
        "vi": "Hiệu ứng nhà kính tăng cường xảy ra do việc đốt nhiên liệu hóa thạch và chặt phá rừng làm tăng mạnh nồng độ các khí nhà kính. Nhiệt lượng sóng dài thoát ra ngoài vũ trụ bị giảm bớt, trong khi bức xạ nhiệt ngược trở lại mặt đất tăng mạnh, làm ấm nhanh khí quyển và các đại dương."
    },
    {
        "id": "gh_gases_breakdown",
        "title": "The Four Key Anthropogenic Gases",
        "en": "Four gases dominate human climate forcing. Carbon dioxide has a long atmospheric lifetime and accounts for the largest radiative forcing. Methane has twenty-eight to thirty-six times the global warming potential of CO2 over a century. Nitrous oxide is nearly three hundred times more potent, and synthetic halocarbons can be thousands of times more potent per molecule.",
        "vi": "Bốn loại khí chính chi phối tác động khí hậu do con người gây ra. Khí các-bô-níc tồn tại rất lâu trong khí quyển và chiếm phần lớn tác động giữ nhiệt. Khí mê-tan có tiềm năng gây nóng lên toàn cầu cao gấp hai mươi tám đến ba mươi sáu lần các-bô-níc trong một thế kỷ. Khí ni-tơ oxit mạnh gấp gần ba trăm lần, còn các hợp chất nhân tạo chứa halogen có thể giữ nhiệt gấp hàng nghìn lần trên mỗi phân tử."
    },
    {
        "id": "sec_takeaways",
        "title": "5. IGCSE Core Takeaways",
        "en": "To summarize Topic 5.1: natural cycles operate over tens of thousands of years, whereas human-driven greenhouse emissions have caused unprecedented warming in just 150 years. Understanding the physical mechanism of radiative heat trapping and the differing potencies of greenhouse gases is essential for answering IGCSE exam questions.",
        "vi": "Tổng kết lại bài năm chấm một: các chu kỳ tự nhiên diễn ra qua hàng chục nghìn năm, trong khi khí thải nhà kính do con người tạo ra đã gây ra hiện tượng nóng lên chưa từng thấy chỉ trong vòng một trăm năm mươi năm. Nắm vững cơ chế vật lý giữ nhiệt bức xạ và tiềm năng giữ nhiệt khác nhau của các loại khí nhà kính là điều cốt lõi để làm tốt các câu hỏi thi."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 4},
    "sec_weather_climate": {"start": 1, "end": 4},
    "sec_evidence": {"start": 5, "end": 8},
    "sec_natural_drivers": {"start": 9, "end": 13},
    "sec_human_causes": {"start": 14, "end": 17},
    "sec_takeaways": {"start": 18, "end": 18}
}

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>1</div>\s*<h2[^>]*>Weather, Climate & the Concept of Climate Change</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_weather_climate" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Weather card
    html = re.sub(
        r'(<div style="background:\s*#f8fafc;\s*border-top:\s*4px solid #38bdf8;[^"]*">\s*<h4[^>]*>Weather</h4>)',
        r'<div class="lecture-interactive-card" data-lecture-section="def_weather" style="background: #f8fafc; border-top: 4px solid #38bdf8; border-radius: 8px; padding: 16px; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; cursor: pointer;"><h4 style="margin: 0 0 6px 0; color: #0284c7; font-size: 16px;">Weather</h4>',
        html,
        count=1
    )

    # Climate card
    html = re.sub(
        r'(<div style="background:\s*#f8fafc;\s*border-top:\s*4px solid #0284c7;[^"]*">\s*<h4[^>]*>Climate</h4>)',
        r'<div class="lecture-interactive-card" data-lecture-section="def_climate" style="background: #f8fafc; border-top: 4px solid #0284c7; border-radius: 8px; padding: 16px; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; cursor: pointer;"><h4 style="margin: 0 0 6px 0; color: #0369a1; font-size: 16px;">Climate</h4>',
        html,
        count=1
    )

    # Climate Change card
    html = re.sub(
        r'(<div style="background:\s*#f8fafc;\s*border-top:\s*4px solid #f97316;[^"]*">\s*<h4[^>]*>Climate Change</h4>)',
        r'<div class="lecture-interactive-card" data-lecture-section="def_climate_change" style="background: #f8fafc; border-top: 4px solid #f97316; border-radius: 8px; padding: 16px; border-left: 1px solid #e2e8f0; border-right: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0; cursor: pointer;"><h4 style="margin: 0 0 6px 0; color: #c2410c; font-size: 16px;">Climate Change</h4>',
        html,
        count=1
    )

    # Section 2: Evidence
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>2</div>\s*<h2[^>]*>Empirical Evidence for Global Climate Change</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_evidence" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Ice cores
    html = re.sub(
        r'(<li style="margin-bottom:\s*10px;">\s*<strong>Antarctic and Greenland Ice Core Proxies:</strong>)',
        r'<li class="lecture-interactive-card" data-lecture-section="evidence_ice_cores" style="margin-bottom: 10px; cursor: pointer;"><strong>Antarctic and Greenland Ice Core Proxies:</strong>',
        html,
        count=1
    )

    # Arctic Sea Ice
    html = re.sub(
        r'(<li style="margin-bottom:\s*10px;">\s*<strong>Cryospheric Retreat & Arctic Sea Ice:</strong>)',
        r'<li class="lecture-interactive-card" data-lecture-section="evidence_arctic_sea_ice" style="margin-bottom: 10px; cursor: pointer;"><strong>Cryospheric Retreat & Arctic Sea Ice:</strong>',
        html,
        count=1
    )

    # Historical proxies
    html = re.sub(
        r'(<li style="margin-bottom:\s*10px;">\s*<strong>Historical Proxies & Cultural Evidence:</strong>)',
        r'<li class="lecture-interactive-card" data-lecture-section="evidence_historical_proxies" style="margin-bottom: 10px; cursor: pointer;"><strong>Historical Proxies & Cultural Evidence:</strong>',
        html,
        count=1
    )

    # Section 3: Natural Drivers
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>3</div>\s*<h2[^>]*>Natural Drivers of Climate Change</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_natural_drivers" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Milankovitch buttons
    html = html.replace(
        'onclick="setMilankovitch(\'eccentricity\')"',
        'onclick="setMilankovitch(\'eccentricity\'); window.playLectureSection && window.playLectureSection(\'milan_eccentricity\', event);" class="lecture-interactive-card" data-lecture-section="milan_eccentricity"'
    )
    html = html.replace(
        'onclick="setMilankovitch(\'obliquity\')"',
        'onclick="setMilankovitch(\'obliquity\'); window.playLectureSection && window.playLectureSection(\'milan_obliquity\', event);" class="lecture-interactive-card" data-lecture-section="milan_obliquity"'
    )
    html = html.replace(
        'onclick="setMilankovitch(\'precession\')"',
        'onclick="setMilankovitch(\'precession\'); window.playLectureSection && window.playLectureSection(\'milan_precession\', event);" class="lecture-interactive-card" data-lecture-section="milan_precession"'
    )

    # Volcanic cooling
    html = re.sub(
        r'(<h3 style="color:\s*#0369a1;\s*font-size:\s*18px;\s*margin-top:\s*24px;">Volcanic Eruptions & Sulfate Aerosol Cooling</h3>)',
        r'<div class="lecture-interactive-card" data-lecture-section="volcanic_cooling" style="cursor: pointer;"><h3 style="color: #0369a1; font-size: 18px; margin-top: 24px;">Volcanic Eruptions & Sulfate Aerosol Cooling</h3>',
        html,
        count=1
    )
    # close volcanic wrapper before Section 4
    html = html.replace(
        '<!-- SECTION 4: HUMAN CAUSES & THE ENHANCED GREENHOUSE EFFECT -->',
        '</div><!-- SECTION 4: HUMAN CAUSES & THE ENHANCED GREENHOUSE EFFECT -->'
    )

    # Section 4: Human causes
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>4</div>\s*<h2[^>]*>Human Forcing: The Enhanced Greenhouse Effect \(EGHE\)</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_human_causes" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Greenhouse buttons
    html = html.replace(
        'onclick="toggleGreenhouse(\'natural\')"',
        'onclick="toggleGreenhouse(\'natural\'); window.playLectureSection && window.playLectureSection(\'gh_natural\', event);" class="lecture-interactive-card" data-lecture-section="gh_natural"'
    )
    html = html.replace(
        'onclick="toggleGreenhouse(\'enhanced\')"',
        'onclick="toggleGreenhouse(\'enhanced\'); window.playLectureSection && window.playLectureSection(\'gh_enhanced\', event);" class="lecture-interactive-card" data-lecture-section="gh_enhanced"'
    )

    # Gases table
    html = re.sub(
        r'(<h3 style="color:\s*#0369a1;\s*font-size:\s*18px;\s*margin-top:\s*24px;">The Anthropogenic Greenhouse Gases</h3>)',
        r'<div class="lecture-interactive-card" data-lecture-section="gh_gases_breakdown" style="cursor: pointer;"><h3 style="color: #0369a1; font-size: 18px; margin-top: 24px;">The Anthropogenic Greenhouse Gases</h3>',
        html,
        count=1
    )
    # close table wrapper before Section 5
    html = html.replace(
        '<!-- SECTION 5: IGCSE SUMMARY & KEY EXAM TAKEAWAYS -->',
        '</div><!-- SECTION 5: IGCSE SUMMARY & KEY EXAM TAKEAWAYS -->'
    )

    # Section 5: Summary
    html = re.sub(
        r'(<div style="background:\s*linear-gradient\(135deg,\s*#f0f9ff 0%,\s*#e0f2fe 100%\);[^"]*">)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_takeaways" style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1px solid #bae6fd; border-radius: 14px; padding: 24px 28px; margin-bottom: 24px; cursor: pointer;">',
        html,
        count=1
    )

    return html

async def main():
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )

    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_html = f.read()

    new_html = transform_html(raw_html)

    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")

    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == "__main__":
    asyncio.run(main())
