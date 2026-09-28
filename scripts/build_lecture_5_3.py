import asyncio
import os
import re
from pathlib import Path
from audio_lecture_engine import process_lecture_audio, update_supabase_page

LECTURE_CODE = "5_3"
LECTURE_ID = "36e35bdb-986b-4cd5-b8df-6bb0f93282e5"
COURSE_TITLE = "IGCSE Geography (0460)"
LECTURE_TITLE = "5.3 Responses to Climate Change: Mitigation & Adaptation"

SEGMENTS = [
    {
        "id": "intro",
        "title": "Introduction to Climate Responses",
        "en": "Welcome to Topic 5.3: Responses to Climate Change: Mitigation and Adaptation. In this lecture, we critically evaluate solutions across global and local scales. We distinguish decarbonisation from resilience management, explore an interactive strategy matrix, and investigate an extensive case study of coastal adaptation in the Bengal Delta of Bangladesh.",
        "vi": "Chào mừng các em đến với bài năm chấm ba: Các giải pháp ứng phó với biến đổi khí hậu: Giảm thiểu và thích ứng. Trong bài giảng này, chúng ta sẽ đánh giá đa chiều các giải pháp ở quy mô toàn cầu và địa phương. Chúng ta sẽ phân biệt giữa việc cắt giảm khí thải và quản lý khả năng phục hồi, khám phá ma trận chiến lược tương tác, và nghiên cứu chi tiết bài học thực tế về thích ứng ven biển tại vùng đồng bằng châu thổ sông Hằng ở Băng-la-đét."
    },
    {
        "id": "sec_golden_rule",
        "title": "1. Mitigation vs Adaptation & Global Treaties",
        "en": "Section 1 establishes humanity's two strategic pillars. In IGCSE examinations, you must never confuse them. Mitigation tackles the root causes by reducing greenhouse gas emissions or expanding carbon sinks. Adaptation manages the unavoidable symptoms by adjusting human and ecological systems to reduce vulnerability.",
        "vi": "Mục một thiết lập hai trụ cột chiến lược của nhân loại. Trong các kỳ thi, các em tuyệt đối không được nhầm lẫn giữa hai khái niệm này. Giảm thiểu là giải quyết tận gốc nguyên nhân bằng cách cắt giảm khí thải nhà kính hoặc mở rộng các bể chứa các-bon. Thích ứng là quản lý các triệu chứng không thể tránh khỏi bằng cách điều chỉnh các hệ thống con người và sinh thái để giảm thiểu tổn thương."
    },
    {
        "id": "strat_mitigation_def",
        "title": "Mitigation Definition (Tackling Causes)",
        "en": "Mitigation means taking proactive measures to prevent, reduce, or slow down emissions. Key strategies include switching to renewable energy like solar and wind, deploying carbon capture and storage technology, and large-scale afforestation.",
        "vi": "Giảm thiểu nghĩa là thực hiện các biện pháp chủ động để ngăn chặn, giảm bớt hoặc làm chậm tốc độ phát thải khí nhà kính. Các chiến lược then chốt bao gồm chuyển dịch sang năng lượng tái tạo như điện mặt trời và điện gió, ứng dụng công nghệ thu giữ và lưu trữ các-bon, cùng với việc trồng rừng trên diện rộng."
    },
    {
        "id": "strat_adaptation_def",
        "title": "Adaptation Definition (Managing Symptoms)",
        "en": "Adaptation means adjusting our physical infrastructure, agriculture, and coastal settlements to cope with the reality of higher seas, stronger storms, and frequent droughts. Examples include constructing sea walls, building stilted cyclone shelters, and developing saline-tolerant crops.",
        "vi": "Thích ứng nghĩa là điều chỉnh cơ sở hạ tầng, nông nghiệp và các khu dân cư ven biển để đối phó với thực tế nước biển dâng cao, bão lớn hơn và hạn hán thường xuyên. Các ví dụ tiêu biểu bao gồm việc xây dựng đê kè chắn sóng, xây nhà tránh bão có chân cột bê tông nâng cao, và lai tạo các giống cây trồng chịu mặn."
    },
    {
        "id": "accords_history",
        "title": "Evolution of Global Climate Accords",
        "en": "Global governance has evolved from the 1997 Kyoto Protocol, which suffered from non-ratification by major emitters, to the landmark 2015 Paris Agreement, where 196 nations pledged to pursue limiting warming to 1.5 degrees Celsius via Nationally Determined Contributions. At COP28 in Dubai, nations explicitly agreed to transition away from fossil fuels.",
        "vi": "Quản trị khí hậu toàn cầu đã phát triển từ Nghị định thư Ki-ô-tô năm 1997 vốn bị cản trở do thiếu sự phê chuẩn của các nước phát thải lớn, tiến tới Hiệp định Pa-ri mang tính bước ngoặt năm 2015, nơi một trăm chín mươi sáu quốc gia cam kết nỗ lực giữ mức ấm lên toàn cầu dưới một phẩy năm độ C thông qua các Đóng góp do quốc gia tự quyết định. Tại hội nghị COP28 ở Đu-bai, các quốc gia đã chính thức đồng thuận chuyển dịch khỏi nhiên liệu hóa thạch."
    },
    {
        "id": "sec_strategy_matrix",
        "title": "2. Interactive Strategy Matrix (Fig 5.12)",
        "en": "Section 2 explores the interconnected spectrum of climate solutions, as illustrated in Hodder Figure 5.12. Strategies fall into pure mitigation, pure adaptation, or powerful synergistic overlaps. Click on each strategy button to examine its operational mechanics, financial costs, and geographical trade-offs.",
        "vi": "Mục hai khám phá bức tranh tổng thể các giải pháp khí hậu, như được minh họa trong sách giáo khoa. Các chiến lược được chia thành giảm thiểu thuần túy, thích ứng thuần túy, hoặc các giải pháp kết hợp mang lại lợi ích kép. Hãy bấm vào từng nút chiến lược để kiểm tra cơ chế hoạt động, chi phí tài chính và những đánh đổi về mặt địa lý."
    },
    {
        "id": "strat_renewables",
        "title": "Strategy 1: Renewable Energy Transition",
        "en": "Decarbonising electricity generation replaces fossil-fired thermal plants with solar photovoltaics, offshore wind, and hydroelectric power. High upfront capital costs and grid intermittency are key limitations, requiring international green financing and grid battery storage.",
        "vi": "Khử các-bon ngành phát điện bằng cách thay thế các nhà máy nhiệt điện đốt than bằng pin mặt trời, điện gió ngoài khơi và thủy điện. Chi phí đầu tư ban đầu lớn và tính chập chờn theo thời tiết là những hạn chế chính, đòi hỏi các nguồn tài chính xanh quốc tế và hệ thống pin lưu trữ lưới điện hiện đại."
    },
    {
        "id": "strat_efficiency",
        "title": "Strategy 2: Energy Efficiency & Conservation",
        "en": "Optimising energy use in industrial processing, commercial architecture, and transport significantly reduces fuel demand. It offers an immediate negative abatement cost, saving money rapidly while slashing emissions without awaiting new inventions.",
        "vi": "Tối ưu hóa hiệu quả sử dụng năng lượng trong sản xuất công nghiệp, thiết kế tòa nhà thương mại và giao thông vận tải giúp giảm đáng kể nhu cầu nhiên liệu. Giải pháp này giúp tiết kiệm chi phí nhanh chóng và cắt giảm khí thải ngay lập tức mà không cần phải chờ đợi những phát minh mới."
    },
    {
        "id": "strat_ccs",
        "title": "Strategy 3: Carbon Capture & Storage (CCS)",
        "en": "CCS captures CO2 at industrial smokestacks, compresses it into a supercritical liquid, and injects it deep underground into depleted gas fields or saline aquifers. It allows heavy industries to decarbonise, but remains capital-intensive and carries risks of underground geological leakage.",
        "vi": "Công nghệ thu giữ và lưu trữ các-bon tiến hành bắt khí các-bô-níc ngay tại các ống khói công nghiệp, nén thành thể lỏng siêu tới hạn rồi bơm sâu xuống lòng đất vào các mỏ khí đã cạn kiệt hoặc tầng ngậm nước mặn. Công nghệ này giúp các ngành công nghiệp nặng khử các-bon, nhưng chi phí rất cao và tiềm ẩn nguy cơ rò rỉ địa chất dưới lòng đất."
    },
    {
        "id": "strat_coastal",
        "title": "Strategy 4: Coastal Hard Engineering",
        "en": "Building massive concrete sea walls, surge barriers, and rock groynes physically blocks rising sea levels and storm surges. While highly effective at safeguarding valuable urban assets, hard defences are extraordinarily expensive, alter coastal sediment drift, and cannot be afforded by poor developing nations.",
        "vi": "Xây dựng các bức tường bê tông chắn biển, đập ngăn triều và kè đá giúp ngăn chặn trực tiếp mực nước biển dâng và triều cường do bão. Dù bảo vệ rất hiệu quả các đô thị giá trị cao, các công trình cứng này vô cùng tốn kém, làm thay đổi quá trình bồi tụ trầm tích ven bờ và vượt quá khả năng tài chính của các quốc gia đang phát triển nghèo."
    },
    {
        "id": "strat_agri",
        "title": "Strategy 5: Agricultural Crop Adaptation",
        "en": "Selective breeding and biotechnology create genetically resilient crop varieties capable of thriving in saline soil or withstanding severe drought. This safeguards smallholder food security, though patent licensing and seed distribution costs can constrain poor rural farmers.",
        "vi": "Chọn giống chọn lọc và công nghệ sinh học giúp tạo ra các giống cây trồng khỏe mạnh có khả năng phát triển trên đất nhiễm mặn hoặc chịu được hạn hán gay gắt. Giải pháp này bảo vệ an ninh lương thực cho các hộ nông dân nhỏ, mặc dù chi phí bản quyền và phân phối hạt giống có thể là rào cản đối với người nông dân nghèo."
    },
    {
        "id": "strat_overlap",
        "title": "Strategy 6: Green Urban Infrastructure (Dual Benefit)",
        "en": "Urban afforestation, bioswales, and green roofs represent synergistic dual-benefit interventions. They absorb and sequester carbon dioxide for mitigation, while simultaneously cooling urban heat islands and absorbing torrential stormwater runoff for adaptation.",
        "vi": "Trồng cây xanh đô thị, làm rãnh thoát nước sinh học và lợp mái nhà xanh là các giải pháp kết hợp mang lại lợi ích kép. Chúng vừa hấp thụ và lưu trữ khí các-bô-níc để giảm thiểu biến đổi khí hậu, vừa giúp làm mát hiệu ứng đảo nhiệt đô thị và thấm hút nước mưa ngập úng để thích ứng."
    },
    {
        "id": "sec_bangladesh_case",
        "title": "3. Bangladesh Coastal Case Study Overview",
        "en": "Section 3 examines Bangladesh as our premier named case study. Contributing less than half a percent of global emissions, Bangladesh suffers immense climate injustice. Two-thirds of its territory is under five meters elevation, exposing ninety million people to catastrophic floods and cyclone storm surges.",
        "vi": "Mục ba đi sâu vào bài học thực tế tiêu biểu tại Băng-la-đét. Mặc dù chỉ đóng góp chưa đầy nửa phần trăm lượng khí thải toàn cầu, Băng-la-đét phải gánh chịu sự bất công khí hậu nặng nề. Hai phần ba diện tích lãnh thổ nằm dưới năm mét độ cao, khiến chín mươi triệu người thường xuyên đối mặt với lũ lụt thảm khốc và triều cường do bão."
    },
    {
        "id": "bd_mangrove",
        "title": "Transect 1: Sundarbans Mangrove Green Belt",
        "en": "The Sundarbans mangrove forest acts as a natural living buffer. Its dense tangle of stilt roots dissipates over sixty percent of wave energy during cyclone storm surges, trapping coastal mud and preventing catastrophic shoreline retreat.",
        "vi": "Rừng ngập mặn Xun-đa-ban đóng vai trò như một vành đai bảo vệ tự nhiên sống động. Mạng lưới rễ chống dày đặc của cây đước làm tiêu hao hơn sáu mươi phần trăm năng lượng sóng trong các đợt triều cường do bão, giữ lại bùn đất ven bờ và ngăn chặn sự xói lở bờ biển nghiêm trọng."
    },
    {
        "id": "bd_polder",
        "title": "Transect 2: Coastal Embankments & Polders",
        "en": "Bangladesh has constructed thousands of kilometers of earthen embankments called polders. These dykes encircle low-lying islands, shielding farmland and villages from daily high tides and saline sea inundation.",
        "vi": "Băng-la-đét đã đắp hàng nghìn cây số đê đất được gọi là các pôn-đơ. Các bờ đê này bao bọc những dải đất trũng thấp, che chở cho các cánh đồng trồng trọt và làng mạc khỏi triều cường hàng ngày và nạn ngập mặn từ biển."
    },
    {
        "id": "bd_shelter",
        "title": "Transect 3: Multi-Purpose Stilted Cyclone Shelters",
        "en": "Over two thousand reinforced concrete cyclone shelters are raised on tall stilts above surge levels. Powered by rooftop solar panels, they serve as everyday primary schools, but convert rapidly into life-saving emergency refuges for thousands of coastal residents during cyclone landfalls.",
        "vi": "Hơn hai nghìn nhà tránh bão bằng bê tông cốt thép kiên cố được xây dựng trên các chân cột nâng cao vượt qua mực nước triều cường. Được cấp điện bởi pin mặt trời trên mái, ngày thường chúng hoạt động như trường tiểu học, nhưng lập tức chuyển đổi thành nơi trú ẩn khẩn cấp cứu sống hàng nghìn người dân ven biển khi bão đổ bộ."
    },
    {
        "id": "bd_crops",
        "title": "Transect 4: Floating Gardens (Baira) & Saline Crops",
        "en": "To adapt to prolonged monsoon flooding and salinisation, local communities weave floating organic rafts called baira from water hyacinths to grow vegetables on floodwaters, alongside cultivating new salt-tolerant rice varieties.",
        "vi": "Để thích ứng với tình trạng lũ lụt kéo dài vào mùa gió mùa và đất bị nhiễm mặn, người dân địa phương đã bện các bè hữu cơ nổi gọi là bai-ra từ cây bèo tây để trồng rau ngay trên mặt nước ngập, kết hợp với việc gieo trồng các giống lúa mới có khả năng chịu mặn cao."
    },
    {
        "id": "bd_shs",
        "title": "Transect 5: Solar Home Systems & Rainwater Harvesting",
        "en": "In off-grid coastal villages, decentralized solar home systems provide clean, resilient electricity. Rainwater harvesting tanks capture precious monsoon rain, securing clean drinking water when groundwater aquifers become poisoned by coastal seawater intrusion.",
        "vi": "Tại các ngôi làng ven biển xa xôi chưa có lưới điện quốc gia, các hệ thống điện mặt trời gia đình phân tán cung cấp nguồn điện sạch và an toàn. Các bể thu trữ nước mưa hứng trọn nguồn nước mưa quý giá trong mùa mưa, đảm bảo nước uống sạch cho người dân khi các túi nước ngầm đã bị nhiễm mặn nghiêm trọng."
    },
    {
        "id": "bd_policy_framework",
        "title": "Bangladesh Climate Strategy (BCCSAP & NDCs)",
        "en": "Under the Bangladesh Climate Change Strategy and Action Plan, Bangladesh combines domestic adaptation financing with national pledges to reduce greenhouse emissions by 21.75% by 2030, showing global leadership in resilient sustainable development.",
        "vi": "Dưới Chiến lược và Kế hoạch Hành động Biến đổi Khí hậu Quốc gia, Băng-la-đét kết hợp nguồn tài chính thích ứng trong nước với cam kết cắt giảm hai mươi mốt phẩy bảy mươi lăm phần trăm lượng khí thải vào năm 2030, thể hiện vai trò dẫn đầu toàn cầu về phát triển bền vững và kiên cường."
    }
]

MAJOR_SECTIONS = {
    "intro": {"start": 0, "end": 4},
    "sec_golden_rule": {"start": 1, "end": 4},
    "sec_strategy_matrix": {"start": 5, "end": 11},
    "sec_bangladesh_case": {"start": 12, "end": 18}
}

def transform_html(raw_html: str) -> str:
    html = raw_html

    # Section 1
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>1</div>\s*<h2[^>]*>The Golden Rule & Global Climate Governance</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_golden_rule" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Mitigation card
    html = re.sub(
        r'(<div style="background:\s*#f0fdf4;\s*border:\s*2px solid #86efac;[^"]*">)',
        r'<div class="lecture-interactive-card" data-lecture-section="strat_mitigation_def" style="background: #f0fdf4; border: 2px solid #86efac; border-radius: 12px; padding: 20px; cursor: pointer;">',
        html,
        count=1
    )

    # Adaptation card
    html = re.sub(
        r'(<div style="background:\s*#eff6ff;\s*border:\s*2px solid #93c5fd;[^"]*">)',
        r'<div class="lecture-interactive-card" data-lecture-section="strat_adaptation_def" style="background: #eff6ff; border: 2px solid #93c5fd; border-radius: 12px; padding: 20px; cursor: pointer;">',
        html,
        count=1
    )

    # Accords History
    html = re.sub(
        r'(<h3 style="color:\s*#0f172a;\s*margin:\s*24px 0 12px 0;\s*font-size:\s*18px;\s*font-weight:\s*700;">Evolution of Global Climate Accords</h3>)',
        r'<div class="lecture-interactive-card" data-lecture-section="accords_history" style="cursor: pointer;"><h3 style="color: #0f172a; margin: 24px 0 12px 0; font-size: 18px; font-weight: 700;">Evolution of Global Climate Accords</h3>',
        html,
        count=1
    )
    # close accords wrapper before Fig 5.14
    html = html.replace(
        '<!-- Hodder Fig 5.14 Surface Temp Change -->',
        '</div><!-- Hodder Fig 5.14 Surface Temp Change -->'
    )

    # Section 2: Strategy Matrix
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*14px;">\s*<div[^>]*>2</div>\s*<h2[^>]*>Interactive Strategy Matrix: Mitigation vs Adaptation \(Fig 5.12 Model\)</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_strategy_matrix" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Strategy buttons
    strategies = [
        ("renewables", "strat_renewables"),
        ("efficiency", "strat_efficiency"),
        ("ccs", "strat_ccs"),
        ("coastal", "strat_coastal"),
        ("agri", "strat_agri"),
        ("overlap", "strat_overlap")
    ]
    for key, sec_id in strategies:
        old_pattern = f"onclick=\"selectStrategy('{key}')\""
        new_pattern = f"onclick=\"selectStrategy('{key}'); window.playLectureSection && window.playLectureSection('{sec_id}', event);\" class=\"lecture-interactive-card\" data-lecture-section=\"{sec_id}\""
        html = html.replace(old_pattern, new_pattern)

    # Section 3: Bangladesh case
    html = re.sub(
        r'(<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;[^"]*">\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*18px;">\s*<div[^>]*>3</div>\s*<h2[^>]*>Detailed Named Case Study: Bangladesh \(Bengal Delta\)</h2>)',
        r'<div class="lecture-interactive-card" data-lecture-section="sec_bangladesh_case" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer;">\1',
        html,
        count=1
    )

    # Transect layers
    layers = [
        ("mangrove", "bd_mangrove"),
        ("polder", "bd_polder"),
        ("shelter", "bd_shelter"),
        ("crops", "bd_crops"),
        ("shs", "bd_shs")
    ]
    for key, sec_id in layers:
        old_pattern = f"onclick=\"showBdLayer('{key}')\""
        new_pattern = f"onclick=\"showBdLayer('{key}'); window.playLectureSection && window.playLectureSection('{sec_id}', event);\" class=\"transect-part lecture-interactive-card\" data-lecture-section=\"{sec_id}\""
        html = html.replace(old_pattern, new_pattern)

    # BCCSAP Policy Framework
    html = re.sub(
        r'(<h3 style="color:\s*#0f172a;\s*margin:\s*24px 0 12px 0;\s*font-size:\s*18px;\s*font-weight:\s*700;">Bangladesh Climate Action Architecture: BCCSAP & NDCs</h3>)',
        r'<div class="lecture-interactive-card" data-lecture-section="bd_policy_framework" style="cursor: pointer;"><h3 style="color: #0f172a; margin: 24px 0 12px 0; font-size: 18px; font-weight: 700;">Bangladesh Climate Action Architecture: BCCSAP & NDCs</h3>',
        html,
        count=1
    )
    # close policy wrapper at end of section 3
    html = html.replace(
        '</div>\n\n    <!-- JAVASCRIPT LOGIC',
        '</div></div>\n\n    <!-- JAVASCRIPT LOGIC'
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
