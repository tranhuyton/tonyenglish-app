import os
import sys
import re
import json
import asyncio
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = '3_2'
LECTURE_ID = '93a28707-1b95-4ed2-a3ff-4789143118cd'
COURSE_TITLE = 'IGCSE Geography (0460)'
LECTURE_TITLE = '3.2 Threats to the Antarctic Ecosystem & Global Management'

SEGMENTS = [
    {
        "id": "intro",
        "title": "Giới thiệu Bài 3.2: Các hiểm họa đối với Nam Cực & Quản trị toàn cầu",
        "selector": "#sec-header",
        "en": "Lesson 3.2: Threats to the Antarctic Ecosystem and Global Management. In this lesson, we explore human pressures on Antarctica, including climate change, overfishing, tourism, and international governance under the Antarctic Treaty System.",
        "vi": "Bài ba chấm hai: Các hiểm họa đối với Hệ sinh thái Nam Cực và Quản trị toàn cầu. Trong bài học này, chúng ta sẽ tìm hiểu các áp lực từ con người lên Nam Cực, bao gồm biến đổi khí hậu, đánh bắt quá mức, du lịch và cơ chế quản lý quốc tế theo Hiệp ước Nam Cực."
    },
    {
        "id": "sec_climate_threats",
        "title": "1. Biến đổi khí hậu & Băng biển suy giảm",
        "selector": "#sec-climate-threats",
        "en": "Section 1: Climate Change, Sea Ice Decline, and Glacial Instability. Rising atmospheric and oceanic temperatures cause drastic sea ice reduction and destabilize coastal ice shelves, triggering catastrophic breeding failures for emperor penguins.",
        "vi": "Phần một: Biến đổi khí hậu, Băng biển suy giảm và Nguy cơ mất ổn định sông băng. Nhiệt độ không khí và đại dương tăng làm thu hẹp nghiêm trọng diện tích băng biển và gây mất ổn định các thềm băng ven bờ, khiến các mùa sinh sản của chim cánh cụt hoàng đế sụp đổ hoàn toàn."
    },
    {
        "id": "hotspot_peninsula",
        "title": "Bán đảo Nam Cực: Điểm nóng ấm lên & Du lịch",
        "selector": "#hotspot-peninsula",
        "en": "Antarctic Peninsula Hotspot. Experiencing rapid warming of nearly three degrees Celsius in fifty years, triggering the collapse of the Larsen A and B ice shelves and drawing ninety-five percent of polar cruise tourism.",
        "vi": "Điểm nóng Bán đảo Nam Cực. Chịu mức tăng nhiệt kỷ lục gần ba độ C trong năm mươi năm qua, làm sụp đổ các thềm băng Larsen A và B, đồng thời thu hút tới chín mươi lăm phần trăm lượng khách du lịch tàu biển."
    },
    {
        "id": "hotspot_rothera",
        "title": "Trạm nghiên cứu Rothera (Vương quốc Anh)",
        "selector": "#hotspot-rothera",
        "en": "Rothera Research Station. A premier scientific station operated by the British Antarctic Survey on Adelaide Island, pioneering zero-solid-waste export protocols and modern biological sewage processing.",
        "vi": "Trạm nghiên cứu Rô-thê-ra. Trạm nghiên cứu khoa học tiên tiến do Cục Khảo sát Nam Cực của Anh vận hành trên đảo A-đơ-lết, đi đầu trong việc xuất khẩu một trăm phần trăm rác thải rắn và xử lý nước thải sinh học hiện đại."
    },
    {
        "id": "hotspot_thwaites",
        "title": "Sông băng Thwaites: Sông băng Ngày tận thế",
        "selector": "#hotspot-thwaites",
        "en": "Thwaites Glacier, the Doomsday Glacier. Grounded deep below sea level, its marine ice sheet base is being vigorously melted by warm circulating ocean currents, threatening up to three metres of global sea level rise.",
        "vi": "Sông băng Thwaites, mang tên Sông băng Ngày tận thế. Có phần đáy nằm sâu dưới mực nước biển, chân sông băng đang bị các dòng hải lưu ấm làm tan chảy dữ dội, đe dọa làm dâng mực nước biển toàn cầu lên tới ba mét."
    },
    {
        "id": "hotspot_ross_mpa",
        "title": "Khu bảo tồn Biển Ross & Trạm McMurdo",
        "selector": "#hotspot-ross-mpa",
        "en": "McMurdo Station and the Ross Sea Marine Protected Area. Established in 2016 across 1.55 million square kilometres, this sanctuary strictly prohibits commercial fishing to protect pristine polar biodiversity.",
        "vi": "Trạm Mác-Mơ-đô và Khu bảo tồn biển Biển Rốt. Được thành lập năm hai nghìn không trăm mười sáu trên diện tích một phẩy năm mươi lăm triệu ki-lô-mét vuông, khu bảo tồn này nghiêm cấm hoàn toàn hoạt động đánh bắt thương mại để bảo tồn tính đa dạng sinh học nguyên sơ."
    },
    {
        "id": "hotspot_trawling",
        "title": "Vùng đánh bắt nhuyễn thể công nghiệp (CCAMLR Vùng 48)",
        "selector": "#hotspot-trawling",
        "en": "Commercial Krill Trawling in CCAMLR Area 48. Fleets concentrate in biologically productive channels along the peninsula, catching hundreds of thousands of tonnes of krill annually and disrupting local predator foraging.",
        "vi": "Đánh bắt nhuyễn thể thương mại tại Vùng 48. Các đội tàu tập trung tại các luồng lạch giàu sinh vật dọc bán đảo, đánh bắt hàng trăm nghìn tấn nhuyễn thể mỗi năm và làm gián đoạn nguồn thức ăn của động vật ăn thịt địa phương."
    },
    {
        "id": "hotspot_ozone",
        "title": "Lỗ thủng tầng Ozone Nam Cực (South Pole)",
        "selector": "#hotspot-ozone",
        "en": "Antarctic Ozone Hole over South Pole. Human emissions of chlorofluorocarbons created a massive seasonal stratospheric ozone hole, allowing harmful ultraviolet-B radiation to penetrate down to ocean surfaces and damage phytoplankton.",
        "vi": "Lỗ thủng tầng Ô-zôn trên bầu trời Cực Nam. Khí thải nhân tạo đã tạo ra một lỗ thủng tầng ô-zôn rộng lớn theo mùa, khiến tia cực tím B độc hại xuyên xuống mặt đại dương gây tổn hại đến thực vật phù du."
    },
    {
        "id": "thwaites_glacier",
        "title": "Hiểm họa mất ổn định dải băng biển (MISI)",
        "selector": "#card-thwaites-glacier",
        "en": "Marine Ice Sheet Instability. Thwaites glacier's reverse bed slope slopes downwards towards the interior. As warm ocean currents erode its marine ice shelf and grounding line, backward ice retreat accelerates irreversibly.",
        "vi": "Nguy cơ mất ổn định của Dải băng biển. Sườn nền đá của sông băng Thwaites dốc ngược vào sâu trong lục địa. Khi dòng nước ấm làm mòn thềm băng và điểm tiếp giáp đáy, quá trình băng tan lùi sâu sẽ diễn ra với tốc độ không thể đảo ngược."
    },
    {
        "id": "sec_overfishing",
        "title": "2. Đánh bắt quá mức & Khai thác tài nguyên biển",
        "selector": "#sec-overfishing",
        "en": "Section 2: Commercial Overfishing and Marine Exploitation. Historical seal hunting and whale slaughters decimated populations. Today, industrial krill harvesting and toothfish longlining dominate commercial operations.",
        "vi": "Phần hai: Đánh bắt quá mức và Khai thác tài nguyên biển. Trong lịch sử, hoạt động săn hải cẩu và cá voi đã tàn phá các quần thể hoang dã. Ngày nay, việc khai thác nhuyễn thể quy mô công nghiệp và câu cá răng biển sâu đang là tâm điểm chú ý."
    },
    {
        "id": "krill_harvesting",
        "title": "Công nghệ hút chân không nhuyễn thể & Tranh chấp sinh thái",
        "selector": "#card-krill-harvesting",
        "en": "Industrial Krill Harvesting Pressures. Modern super-trawlers use continuous underwater vacuum pumps to hoover up krill for aquaculture fishmeal and omega-3 pills, directly depriving breeding penguin colonies of food.",
        "vi": "Áp lực khai thác nhuyễn thể công nghiệp. Các siêu tàu đánh cá hiện đại dùng máy bơm hút chân không liên tục dưới đáy biển để gom nhuyễn thể làm thức ăn thủy sản và thực phẩm chức năng, trực tiếp cướp đi nguồn thức ăn của các đàn chim cánh cụt."
    },
    {
        "id": "toothfish_seabird",
        "title": "Cá tuyết răng & Hải âu chết vì dây câu ngầm",
        "selector": "#card-toothfish-seabird",
        "en": "Patagonian Toothfish and Seabird Bycatch. High market prices fuel illegal, unreported, and unregulated fishing. Submerged longline hooks also accidentally drown tens of thousands of wandering albatrosses and petrels.",
        "vi": "Cá răng và Thảm họa hải âu chết nghẹn dây câu. Giá trị kinh tế đắt đỏ thúc đẩy nạn đánh bắt bất hợp pháp. Hàng nghìn lưỡi câu ngầm rải dưới nước còn vô tình làm chết đuối hàng vạn cá thể chim hải âu bay lượn săn mồi."
    },
    {
        "id": "sec_research",
        "title": "3. Nghiên cứu khoa học & Quản lý dấu chân sinh thái",
        "selector": "#sec-research",
        "en": "Section 3: Scientific Research and Environmental Footprint. Over seventy international research bases host thousands of scientists, creating localized environmental challenges through fuel storage, aircraft emissions, and sewage.",
        "vi": "Phần ba: Nghiên cứu khoa học và Quản lý dấu chân môi trường. Hơn bảy mươi trạm nghiên cứu quốc tế đón hàng nghìn nhà khoa học, mang lại những thách thức môi trường cục bộ từ việc tích trữ nhiên liệu, khí thải máy bay và nước thải."
    },
    {
        "id": "rothera_case",
        "title": "Điển cứu Trạm Rothera (BAS): Tiêu chuẩn sinh thái",
        "selector": "#card-rothera-case",
        "en": "Case Study: Rothera Research Station Modernization. The British Antarctic Survey demonstrates sustainable stewardship through total solid waste repatriation, closed biological sewage treatment, and mandatory wildlife disturbance buffers.",
        "vi": "Nghiên cứu điển hình: Nâng cấp trạm nghiên cứu Rô-thê-ra. Cục Khảo sát Nam Cực của Anh là hình mẫu quản lý bền vững thông qua việc chở toàn bộ rác thải rắn về nước, xử lý nước thải sinh học khép kín và duy trì khoảng cách an toàn với động vật hoang dã."
    },
    {
        "id": "sec_tourism",
        "title": "4. Áp lực du lịch & Rủi ro an toàn sinh học",
        "selector": "#sec-tourism",
        "en": "Section 4: Tourism Pressures and Biosecurity Challenges. Over one hundred thousand cruise passengers visit the Antarctic Peninsula each summer, creating severe crowding, wildlife stress, and potential biosecurity hazards.",
        "vi": "Phần bốn: Áp lực từ hoạt động du lịch và Thách thức an toàn sinh học. Hơn một trăm nghìn du khách trên các tàu du lịch đổ về Bán đảo Nam Cực mỗi mùa hè, gây ra tình trạng quá tải cục bộ, làm xáo trộn đời sống động vật và tiềm ẩn nguy cơ an toàn sinh học."
    },
    {
        "id": "tourism_threats",
        "title": "Hiểm họa tràn dầu & Xâm nhập của cỏ dại",
        "selector": "#card-tourism-threats",
        "en": "Tourism Threats and Invasive Species. Heavy cruise ships navigating uncharted pack ice risk catastrophic oil spills. Visitors also inadvertently transport invasive seeds, such as annual bluegrass, lodged in velcro straps and boot soles.",
        "vi": "Hiểm họa tràn dầu và Sinh vật ngoại lai. Các tàu biển trọng tải lớn di chuyển giữa các dải băng trôi đối mặt nguy cơ tràn dầu thảm khốc. Du khách cũng vô tình mang theo các hạt giống cỏ dại xâm lấn dính trong khóa dán và đế giày bảo hộ."
    },
    {
        "id": "sec_governance",
        "title": "5. Quản trị toàn cầu: Hệ thống Hiệp ước Nam Cực (ATS)",
        "selector": "#sec-governance",
        "en": "Section 5: Global Governance: The Antarctic Treaty System. Entering into force in 1961, the Antarctic Treaty neutralised territorial disputes, banned military activity and nuclear waste, and reserved the continent for science and peace.",
        "vi": "Phần năm: Quản trị toàn cầu và Hệ thống Hiệp ước Nam Cực. Có hiệu lực từ năm một nghìn chín trăm sáu mươi mốt, Hiệp ước Nam Cực đã hóa giải các tranh chấp lãnh thổ, cấm mọi hoạt động quân sự và rác thải hạt nhân, dành trọn lục địa cho khoa học và hòa bình."
    },
    {
        "id": "treaty_madrid",
        "title": "Nghị định thư Madrid (1991): Cấm khai thác mỏ vô thời hạn",
        "selector": "#card-treaty-madrid",
        "en": "The 1991 Madrid Protocol on Environmental Protection. Designates Antarctica as a natural reserve devoted to peace and science, instituting an indefinite ban on all commercial mineral extraction and oil exploration.",
        "vi": "Nghị định thư Madrid năm một nghìn chín trăm chín mươi mốt. Quy định Nam Cực là khu bảo tồn thiên nhiên dành riêng cho hòa bình và khoa học, thiết lập lệnh cấm vô thời hạn đối với mọi hoạt động khai thác khoáng sản và thăm dò dầu khí thương mại."
    },
    {
        "id": "geopolitical_2041",
        "title": "Câu hỏi địa chính trị năm 2041 & Tương lai",
        "selector": "#card-geopolitical-2041",
        "en": "The 2041 Geopolitical Dilemma. In 2041, any treaty consultative member can request a formal review of the mining prohibition. Global resource scarcity may challenge the consensus that has safeguarded Antarctica for decades.",
        "vi": "Thách thức địa chính trị năm hai nghìn không trăm bốn mươi mốt. Đến năm hai nghìn không trăm bốn mươi mốt, bất kỳ quốc gia thành viên nào cũng có quyền yêu cầu xem xét lại lệnh cấm khai mỏ. Tình trạng khan hiếm tài nguyên toàn cầu có thể thách thức sự đồng thuận đã bảo vệ Nam Cực suốt nhiều thập kỷ."
    },
    {
        "id": "summary_takeaways",
        "title": "📌 Tổng kết & Khái niệm thi IGCSE trọng tâm",
        "selector": "#card-summary-takeaways",
        "en": "IGCSE Summary and Key Takeaways. Managing fragile polar biomes requires multi-scale strategies: mitigating global greenhouse emissions, enforcing strict catch limits through CCAMLR, and maintaining diplomatic solidarity under the Antarctic Treaty.",
        "vi": "Tổng kết và Các khái niệm trọng tâm bài thi. Quản lý các quần xã sinh vật vùng cực đòi hỏi những chiến lược đa tầng: cắt giảm khí thải nhà kính toàn cầu, thực thi hạn ngạch đánh bắt nghiêm ngặt và duy trì sự đoàn kết ngoại giao dưới ngọn cờ Hiệp ước Nam Cực."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 7},
    "sec_climate_threats": {"start": 1, "end": 8},
    "sec_overfishing": {"start": 9, "end": 11},
    "sec_research": {"start": 12, "end": 13},
    "sec_tourism": {"start": 14, "end": 15},
    "sec_governance": {"start": 16, "end": 19}
}

def transform_html(raw_html):
    html = raw_html
    
    # 1. Header
    html = re.sub(
        r'(<div style="display:flex; gap:8px; align-items:center; margin-bottom:12px;">[\s\S]*?)(<h1 style="[^"]*">)',
        r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="cursor:pointer; border-radius:12px; padding:12px 16px; margin-bottom:16px; transition:all 0.2s ease;">\1\2',
        html, count=1
    )
    # close after top intro box
    html = re.sub(
        r'(Antarctic Treaty System \(ATS\)\.</strong>\s*</p>\s*</div>)',
        r'\1</div>',
        html, count=1
    )
    
    # 2. Section 1: Climate Threats
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*1\. Climate Change, Sea Ice Decline & Glacial Instability\s*</h2>)',
        r'<div id="sec-climate-threats" class="lecture-interactive-card" data-lecture-section="sec_climate_threats" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 2
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*2\. Commercial Overfishing)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Threat nodes in SVG
    html = html.replace('<g class="threat-node" transform="translate(245, 175)">', '<g id="hotspot-peninsula" class="threat-node" data-lecture-section="hotspot_peninsula" style="cursor:pointer;" transform="translate(245, 175)">')
    html = html.replace('<g class="threat-node" transform="translate(260, 220)">', '<g id="hotspot-rothera" class="threat-node" data-lecture-section="hotspot_rothera" style="cursor:pointer;" transform="translate(260, 220)">')
    html = html.replace('<g class="threat-node" transform="translate(290, 420)">', '<g id="hotspot-thwaites" class="threat-node" data-lecture-section="hotspot_thwaites" style="cursor:pointer;" transform="translate(290, 420)">')
    html = html.replace('<g class="threat-node" transform="translate(430, 480)">', '<g id="hotspot-ross-mpa" class="threat-node" data-lecture-section="hotspot_ross_mpa" style="cursor:pointer;" transform="translate(430, 480)">')
    html = html.replace('<g class="threat-node" transform="translate(320, 160)">', '<g id="hotspot-trawling" class="threat-node" data-lecture-section="hotspot_trawling" style="cursor:pointer;" transform="translate(320, 160)">')
    html = html.replace('<g class="threat-node" transform="translate(460, 330)">', '<g id="hotspot-ozone" class="threat-node" data-lecture-section="hotspot_ozone" style="cursor:pointer;" transform="translate(460, 330)">')
    
    # Thwaites glacier card
    html = re.sub(
        r'(<div style="background:#fff1f2; border:1px solid #fecdd3; border-left:5px solid #e11d48; border-radius:10px; padding:18px; margin:24px 0;">\s*<h3 style="margin:0 0 10px 0; color:#9f1239;[^"]*">🌊 Glacial Instability & The "Doomsday Glacier" \(Thwaites\)</h3>)',
        r'<div id="card-thwaites-glacier" class="lecture-interactive-card" data-lecture-section="thwaites_glacier" style="background:#fff1f2; border:1px solid #fecdd3; border-left:5px solid #e11d48; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;"><h3 style="margin:0 0 10px 0; color:#9f1239; font-size:17px; font-weight:700;">🌊 Glacial Instability & The "Doomsday Glacier" (Thwaites)</h3>',
        html, count=1
    )
    
    # 3. Section 2: Overfishing
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*2\. Commercial Overfishing & Marine Resource Exploitation\s*</h2>)',
        r'<div id="sec-overfishing" class="lecture-interactive-card" data-lecture-section="sec_overfishing" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 3
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*3\. Scientific Research)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Overfishing sub cards
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#15803d; margin-bottom:8px;">🦐 Industrial Krill Fishery Pressures</div>',
        '<div id="card-krill-harvesting" class="lecture-interactive-card" data-lecture-section="krill_harvesting" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#15803d; margin-bottom:8px;">🦐 Industrial Krill Fishery Pressures</div>'
    )
    html = html.replace(
        '<div style="font-size:16px; font-weight:700; color:#b45309; margin-bottom:8px;">🐟 Patagonian Toothfish & Seabird Bycatch</div>',
        '<div id="card-toothfish-seabird" class="lecture-interactive-card" data-lecture-section="toothfish_seabird" style="cursor:pointer;"><div style="font-size:16px; font-weight:700; color:#b45309; margin-bottom:8px;">🐟 Patagonian Toothfish & Seabird Bycatch</div>'
    )
    
    # 4. Section 3: Research
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*3\. Scientific Research & Rothera Case Study\s*</h2>)',
        r'<div id="sec-research" class="lecture-interactive-card" data-lecture-section="sec_research" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 4
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*4\. Tourism Pressures)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Rothera card
    html = html.replace(
        '<div style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:24px 0;">\n        <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:16px; font-weight:700;">🔬 Case Study: How Rothera Station Minimizes Its Ecological Footprint</h4>',
        '<div id="card-rothera-case" class="lecture-interactive-card" data-lecture-section="rothera_case" style="background:#eff6ff; border:1px solid #bfdbfe; border-left:5px solid #2563eb; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#1e40af; font-size:16px; font-weight:700;">🔬 Case Study: How Rothera Station Minimizes Its Ecological Footprint</h4>'
    )
    
    # 5. Section 4: Tourism
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*4\. Tourism Pressures & Biosecurity Challenges\s*</h2>)',
        r'<div id="sec-tourism" class="lecture-interactive-card" data-lecture-section="sec_tourism" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    # close before Section 5
    html = re.sub(
        r'(\s*)(<h2 style="color:#0369a1;[^"]*">\s*5\. Global Governance)',
        r'</div>\1\2',
        html, count=1
    )
    
    # Tourism threats card
    html = html.replace(
        '<div style="background:#fef2f2; border:1px solid #fecaca; border-left:5px solid #dc2626; border-radius:10px; padding:18px; margin:20px 0;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:16px; font-weight:700;">⚠️ Ecological Threats from Tourism</h4>',
        '<div id="card-tourism-threats" class="lecture-interactive-card" data-lecture-section="tourism_threats" style="background:#fef2f2; border:1px solid #fecaca; border-left:5px solid #dc2626; border-radius:10px; padding:18px; margin:20px 0; cursor:pointer;">\n        <h4 style="margin:0 0 10px 0; color:#991b1b; font-size:16px; font-weight:700;">⚠️ Ecological Threats from Tourism</h4>'
    )
    
    # 6. Section 5: Governance
    html = re.sub(
        r'(<h2 style="color:#0369a1;[^"]*">\s*5\. Global Governance: The Antarctic Treaty System \(ATS\)\s*</h2>)',
        r'<div id="sec-governance" class="lecture-interactive-card" data-lecture-section="sec_governance" style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;">\1',
        html, count=1
    )
    
    # Madrid treaty card
    html = html.replace(
        '<div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; margin:20px 0;">\n        <div style="background:#0f172a; color:#ffffff; padding:12px 18px; font-weight:700; font-size:15px;">\n            Key Legal Pillars of the Antarctic Treaty System',
        '<div id="card-treaty-madrid" class="lecture-interactive-card" data-lecture-section="treaty_madrid" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; overflow:hidden; margin:20px 0; cursor:pointer;">\n        <div style="background:#0f172a; color:#ffffff; padding:12px 18px; font-weight:700; font-size:15px;">\n            Key Legal Pillars of the Antarctic Treaty System'
    )
    
    # 2041 card
    html = html.replace(
        '<div style="background:#fffbeb; border:1px solid #fef3c7; border-left:5px solid #d97706; border-radius:10px; padding:18px; margin:24px 0;">\n        <h4 style="margin:0 0 8px 0; color:#92400e; font-size:16px; font-weight:700;">⛏️ The Geopolitical Dilemma: What Happens in 2041?</h4>',
        '<div id="card-geopolitical-2041" class="lecture-interactive-card" data-lecture-section="geopolitical_2041" style="background:#fffbeb; border:1px solid #fef3c7; border-left:5px solid #d97706; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;">\n        <h4 style="margin:0 0 8px 0; color:#92400e; font-size:16px; font-weight:700;">⛏️ The Geopolitical Dilemma: What Happens in 2041?</h4>'
    )
    
    # close section 5 before summary
    html = re.sub(
        r'(\s*)(<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0;">\s*<h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Takeaways</h3>)',
        r'</div>\1\2',
        html, count=1
    )
    
    # summary card
    html = html.replace(
        '<div style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0;">\n        <h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Takeaways</h3>',
        '<div id="card-summary-takeaways" class="lecture-interactive-card" data-lecture-section="summary_takeaways" style="background:#f0fdf4; border:1px solid #bbf7d0; border-left:5px solid #16a34a; border-radius:10px; padding:18px; margin:24px 0; cursor:pointer;">\n        <h3 style="margin:0 0 10px 0; color:#166534; font-size:17px; font-weight:700;">📌 Summary & Key Takeaways</h3>'
    )
    
    return html

async def main():
    manifest = await process_lecture_audio(
        LECTURE_CODE, LECTURE_ID, COURSE_TITLE, LECTURE_TITLE,
        SEGMENTS, MAJOR_SECTIONS
    )
    
    raw_path = f"scratch/lectures/{LECTURE_CODE}_p1.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_html = f.read()
    
    new_html = transform_html(raw_html)
    
    interactive_path = f"scratch/lectures/{LECTURE_CODE}_p1_interactive.html"
    with open(interactive_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Transformed HTML saved to {interactive_path}")
    
    update_supabase_page(LECTURE_ID, new_html)
    print(f"Lecture {LECTURE_CODE} fully processed and uploaded!")

if __name__ == '__main__':
    asyncio.run(main())
