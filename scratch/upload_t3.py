import urllib.request
import json
import re

def to_entities(text):
    return text.encode('ascii', 'xmlcharrefreplace').decode('ascii')

STYLE_WRAPPER = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px">
{content}
</div>
"""

def format_html(content):
    return STYLE_WRAPPER.format(content=content)

def make_request(page_id, html_content):
    url = f"https://ubkvzgwespfvrlpjuxkp.supabase.co/rest/v1/lecture_pages?id=eq.{page_id}"
    headers = {
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    data = json.dumps({"content_html": html_content}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method="PATCH")
    try:
        with urllib.request.urlopen(req) as response:
            print(f"[{page_id}] Status: {response.status}")
    except Exception as e:
        print(f"[{page_id}] Error: {e}")

html_31_p1 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.1 Antarctic Ecosystem</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Location & Climate</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <p>Antarctica is located at the South Pole (90&deg;S) and is characterized by extreme conditions:</p>
    <ul style="margin-top:8px;">
        <li><strong>Coldest:</strong> Average temperature of -57&deg;C. The lowest recorded temperature was -89&deg;C at Vostok Station in 1983.</li>
        <li><strong>Windiest:</strong> Powerful katabatic winds can reach speeds of up to 200km/h, sweeping down from the polar plateau to the coast.</li>
        <li><strong>Driest:</strong> It is classified as a cold desert, receiving less than 200mm of precipitation per year, mostly as snow.</li>
        <li><strong>Ice Sheet:</strong> An enormous ice sheet covers 98% of the land area. This represents 26.5 million cubic kilometers of ice, holding 90% of the world's freshwater.</li>
        <li><strong>Sea Ice:</strong> The extent of sea ice doubles in the winter, growing from 3 million km&sup2; in summer to a massive 18 million km&sup2; in winter.</li>
        <li><strong>Light:</strong> Experiences 24-hour polar day (constant sunlight) in summer and 24-hour polar night (constant darkness) in winter.</li>
    </ul>
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Food Web</h2>
<p>The Antarctic food web is highly dependent on a few key species, making it vulnerable to disruption.</p>

<svg viewBox="0 0 800 500" style="max-width:420px; height:auto; display:block; margin:0 auto; margin-top:24px; margin-bottom:8px;">
    <!-- Simple Food Web SVG Representation -->
    <rect x="0" y="0" width="800" height="500" fill="#f8fafc" />
    <text x="400" y="40" font-size="24" font-weight="bold" text-anchor="middle" fill="#0f172a">Antarctic Food Web</text>
    
    <!-- Producers -->
    <rect x="300" y="400" width="200" height="50" rx="8" fill="#86efac" />
    <text x="400" y="430" font-size="16" text-anchor="middle" fill="#064e3b">Phytoplankton & Ice Algae</text>
    
    <!-- Primary Consumers -->
    <rect x="300" y="300" width="200" height="50" rx="8" fill="#fde047" />
    <text x="400" y="330" font-size="16" text-anchor="middle" fill="#713f12">Antarctic Krill (Keystone)</text>
    
    <rect x="100" y="300" width="150" height="50" rx="8" fill="#fde047" />
    <text x="175" y="330" font-size="16" text-anchor="middle" fill="#713f12">Zooplankton</text>

    <!-- Secondary Consumers -->
    <rect x="100" y="200" width="150" height="50" rx="8" fill="#fdba74" />
    <text x="175" y="230" font-size="16" text-anchor="middle" fill="#7c2d12">Fish & Squid</text>
    
    <rect x="300" y="200" width="200" height="50" rx="8" fill="#fdba74" />
    <text x="400" y="230" font-size="16" text-anchor="middle" fill="#7c2d12">Baleen Whales</text>

    <!-- Tertiary / Apex Consumers -->
    <rect x="100" y="100" width="150" height="50" rx="8" fill="#f87171" />
    <text x="175" y="130" font-size="16" text-anchor="middle" fill="#7f1d1d">Penguins & Seals</text>

    <rect x="550" y="100" width="150" height="50" rx="8" fill="#f87171" />
    <text x="625" y="130" font-size="16" text-anchor="middle" fill="#7f1d1d">Orca (Killer Whale)</text>

    <!-- Arrows -->
    <!-- Phytoplankton to Krill -->
    <path d="M 400 400 L 400 350" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />
    <!-- Phytoplankton to Zooplankton -->
    <path d="M 350 400 L 200 350" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />
    <!-- Krill to Whales -->
    <path d="M 400 300 L 400 250" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />
    <!-- Krill to Fish -->
    <path d="M 350 300 L 225 250" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />
    <!-- Krill to Penguins -->
    <path d="M 300 325 L 175 150" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />
    <!-- Penguins to Orca -->
    <path d="M 250 125 L 550 125" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />

    <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8" />
        </marker>
    </defs>
</svg>
<div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Diagram: Simplified Antarctic Food Web. Arrows indicate energy flow.</div>

<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-top:24px; margin-bottom:24px;">
    <ul style="margin-top:0;">
        <li><strong>Producers:</strong> Ice algae and phytoplankton (especially diatoms) form the base of the food web.</li>
        <li><strong>Primary consumers:</strong> Zooplankton and <strong>Antarctic krill</strong> (<em>Euphausia superba</em>). Krill is a <strong>keystone species</strong>, with an estimated biomass of 500 million tonnes.</li>
        <li><strong>Secondary consumers:</strong> Squid, various fish (like Antarctic cod and silverfish).</li>
        <li><strong>Tertiary consumers:</strong> Penguins (Emperor, Adelie, Chinstrap, Gentoo), seals (leopard, Weddell, crabeater, elephant), and seabirds (petrel, albatross).</li>
        <li><strong>Apex predators:</strong> Orca (killer whale) and leopard seals.</li>
        <li><strong>Direct Pathways:</strong> Humpback and minke whales bypass intermediate trophic levels by feeding directly on massive swarms of krill.</li>
    </ul>
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Adaptations</h2>
<p>Species in Antarctica have evolved unique physical and behavioral adaptations to survive the harsh conditions.</p>

<ul style="margin-top:8px;">
    <li><strong>Emperor Penguin:</strong> 
        <ul>
            <li><strong>Behavioral:</strong> Huddle in groups of thousands during winter to share body heat and protect against -50&deg;C winds, taking turns on the outside edge. They breed in winter so chicks hatch in spring when food is plentiful.</li>
            <li><strong>Physical:</strong> Possess a 3cm thick layer of insulating blubber and densely packed, waterproof feathers. They have a counter-current heat exchange system in their flippers and feet to minimize heat loss. Capable of deep, fast dives (up to 600m for 30 minutes).</li>
        </ul>
    </li>
    <li><strong>Weddell Seal:</strong> Can dive up to 600m for 80 minutes. They have a slow metabolism underwater and anti-freeze proteins in their blood. Pups are born directly on the sea ice.</li>
    <li><strong>Antarctic Krill:</strong> Transparent bodies help them hide from predators. They produce anti-freeze glycoproteins to survive in sub-zero waters and can scrape ice algae directly from the underside of pack ice. They are lipid-rich, storing high energy reserves.</li>
    <li><strong>Plants:</strong> There are no vascular plants in Antarctica (except for two species on the peninsula). The flora consists mainly of mosses and lichens restricted to ice-free areas. They are extremely slow-growing (lichens grow ~1mm/year) and are adapted to withstand frequent freeze-thaw cycles, high UV radiation, and severe desiccation (drying out).</li>
</ul>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">4. Seasonal Changes</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <p>The Antarctic ecosystem undergoes dramatic seasonal shifts driven by light availability.</p>
    <ul style="margin-top:8px;">
        <li><strong>Summer (Nov - Feb):</strong> 24-hour daylight triggers an explosive bloom of phytoplankton. This leads to a massive population boom in krill. Migratory seabirds and whales arrive to feed. The sea ice melts significantly, allowing access to open water, and penguins breed on the newly exposed land and ice-free areas.</li>
        <li><strong>Winter (Jun - Aug):</strong> Characterized by 24 hours of darkness. The sea ice extends massively around the continent. Most seabirds and whales migrate north to warmer waters. Little biological activity occurs under the thick ice. <em>Exception:</em> Emperor penguins breed on the ice during this harshest period.</li>
    </ul>
</div>
"""

html_31_p2 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.1 Antarctic Ecosystem (Bilingual)</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Location & Climate</h2>
<p>Antarctica (90&deg;S), coldest (-57&deg;C avg, -89&deg;C record Vostok Station 1983), windiest (200km/h katabatic winds), driest (classified as cold desert, &lt;200mm precipitation/yr), 24hr polar day/night, ice sheet covers 98% land = 26.5 million km&sup3; ice = 90% world's freshwater. Sea ice doubles in winter (18M km&sup2;&rarr;3M km&sup2; in summer).</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Vị trí & Khí hậu: Nam Cực (90&deg; Nam), lạnh nhất (trung bình -57&deg;C, kỷ lục -89&deg;C tại Trạm Vostok năm 1983), nhiều gió nhất (gió katabatic 200km/h), khô nhất (được phân loại là hoang mạc lạnh, lượng mưa &lt;200mm/năm), ngày/đêm vùng cực kéo dài 24h. Tảng băng (ice sheet) bao phủ 98% diện tích đất liền = 26.5 triệu km&sup3; băng = 90% lượng nước ngọt của thế giới. Băng trên biển (sea ice) tăng gấp đôi vào mùa đông (từ 3 triệu km&sup2; vào mùa hè lên 18 triệu km&sup2;).
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Food Web</h2>
<p>Producers: ice algae + phytoplankton (diatoms). Primary consumers: zooplankton, krill (Euphausia superba — KEYSTONE species, 500M tonnes). Secondary: squid, fish (Antarctic cod, silverfish). Tertiary: penguins (Emperor, Adelie, Chinstrap, Gentoo), seals (leopard, Weddell, crabeater, elephant), petrel, albatross. Apex: Orca (killer whale). Also: Antarctic krill &rarr; humpback whale direct path.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Mạng lưới thức ăn (Food web): Sinh vật sản xuất (producer): tảo băng + tảo phù du (phytoplankton). Sinh vật tiêu thụ bậc 1 (primary consumer): động vật phù du, tôm krill (loài then chốt - keystone species, 500 triệu tấn). Sinh vật tiêu thụ bậc 2: mực, cá. Sinh vật tiêu thụ bậc 3: chim cánh cụt, hải cẩu, hải âu. Động vật ăn thịt bậc cao nhất (Apex predator): Cá voi sát thủ (Orca). Ngoài ra còn có chuỗi thức ăn trực tiếp: Tôm krill Nam Cực &rarr; Cá voi lưng gù.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Adaptations</h2>
<p>Emperor penguin (huddle 1000s together in -50&deg;C wind, take turns outside; thick waterproof feathers; 3cm fat layer; counter-current heat exchange in flippers/feet; fast 30min dives to 600m; breed in winter). Weddell seal (can dive 600m for 80min; slow metabolism; anti-freeze proteins in blood). Antarctic krill (anti-freeze glycoproteins; lipid-rich to store energy; transparent body). Plants: only mosses and lichens; slow-growing; adapted to freeze-thaw, UV, desiccation.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Sự thích nghi (Adaptation): Chim cánh cụt Hoàng đế (tụ tập hàng ngàn con trong gió -50&deg;C, luân phiên đứng vòng ngoài; lông dày không thấm nước; lớp mỡ dưới da - blubber - dày 3cm; trao đổi nhiệt ngược dòng ở chân/cánh chèo; sinh sản vào mùa đông). Hải cẩu Weddell (trao đổi chất chậm; protein chống đông máu). Tôm krill (glycoprotein chống đông; cơ thể trong suốt). Thực vật: chỉ có rêu và địa y; sinh trưởng chậm; thích nghi với chu kỳ đóng băng-tan băng, tia UV và sự khô hạn.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">4. Seasonal changes</h2>
<p>Summer (Nov-Feb): 24hr daylight &rarr; explosive phytoplankton bloom &rarr; krill boom &rarr; seabirds/whales arrive; sea ice melts; penguins breed on land/ice-free areas. Winter (Jun-Aug): 24hr darkness; sea ice extends; most seabirds/whales migrate north; Emperor penguins breed IN winter; little biological activity under ice.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Thay đổi theo mùa: Mùa hè (tháng 11-tháng 2): 24h có ánh sáng &rarr; sự bùng nổ của tảo phù du &rarr; tôm krill tăng mạnh &rarr; chim biển/cá voi di cư đến; băng trên biển tan chảy. Mùa đông (tháng 6-tháng 8): 24h chìm trong bóng tối; lớp băng biển mở rộng; phần lớn chim biển/cá voi di cư về phía bắc; chim cánh cụt Hoàng đế đẻ trứng vào mùa đông; rất ít hoạt động sinh học diễn ra dưới lớp băng.
</div>
"""

html_32_p1 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.2 Threats to Antarctic + Management</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Ozone Depletion</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <p>The ozone layer in the stratosphere absorbs harmful UV-B radiation. Historically, CFCs (chlorofluorocarbons) from fridges and aerosols released chlorine atoms that catalytically destroyed ozone molecules.</p>
    <ul style="margin-top:8px;">
        <li><strong>Impact:</strong> The Antarctic ozone hole was discovered in 1985 and is worst each Southern Hemisphere spring (Sept-Oct). Increased UV-B radiation causes DNA damage in phytoplankton, disrupting the fundamental base of the entire food web.</li>
        <li><strong>Management:</strong> The <strong>Montreal Protocol (1987)</strong> enforced a global ban on CFCs. The ozone hole is now slowly recovering and is projected to heal completely by 2066.</li>
    </ul>
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Climate Change</h2>
<p>The Southern Ocean is warming at twice the global average rate, leading to severe physical and ecological changes:</p>
<ul style="margin-top:8px;">
    <li>The West Antarctic Ice Sheet is losing 150 billion tonnes of ice per year.</li>
    <li><strong>Ice Shelf Collapse:</strong> Dramatic events like the Larsen B ice shelf collapse (3,250km&sup2; in 35 days, 2002) and the Conger Ice Shelf (1200km&sup2;, 2022).</li>
    <li><strong>Ecological Impact:</strong> Declining sea ice leads to habitat loss for penguins. Emperor penguin chicks can drown if the sea ice they are raised on breaks up too early in the season.</li>
    <li><strong>Global Threat:</strong> If all Antarctic land ice were to melt, global sea levels would rise by approximately 58 meters.</li>
</ul>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Commercial Fishing</h2>
<p>Fishing fleets primarily target Antarctic Krill (<em>Euphausia superba</em>) and Patagonian toothfish.</p>
<ul style="margin-top:8px;">
    <li><strong>Krill Fishing:</strong> Over 300,000 tonnes are harvested annually, primarily for omega-3 health supplements, aquaculture feed, and pharmaceuticals. Because krill is a <em>keystone species</em>, overfishing risks collapsing the entire food web.</li>
    <li><strong>Other Issues:</strong> Illegal, Unreported, and Unregulated (IUU) fishing for Patagonian toothfish (marketed as Chilean sea bass). Bottom trawling techniques severely damage delicate seabed ecosystems.</li>
</ul>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">4. Tourism</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <p>Antarctic tourism has grown rapidly, exceeding 75,000 tourists in the 2022 season.</p>
    <ul style="margin-top:8px;">
        <li><strong>Threats:</strong> Risk of fuel oil spills (e.g., MV Explorer sank in 2007 spilling 154,000L of oil), introduction of invasive species via boots and equipment, disturbance to penguin breeding colonies, noise pollution, and physical damage to the seabed from ship anchoring.</li>
        <li><strong>Management:</strong> <strong>IAATO</strong> (International Association of Antarctic Tour Operators) self-regulates the industry. They enforce limits on ship size, the number of landing sites, visitor numbers per site (usually max 100 ashore at once), and mandate strict wildlife viewing distances.</li>
    </ul>
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">5. Scientific Research</h2>
<p>Over 70 research stations operate on the continent. For example, the USA's McMurdo Station hosts up to 1000 people during the summer.</p>
<ul style="margin-top:8px;">
    <li><strong>Impacts:</strong> Localized fuel spills, historical waste dumping in the ocean, physical damage to fragile mosses and lichens (which can take centuries to recover), and light/noise pollution.</li>
    <li><strong>Improvement:</strong> Modern stations are much better managed; waste is strictly sorted, compacted, and shipped back out of Antarctica.</li>
</ul>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">6. International Management</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <ul style="margin-top:0;">
        <li><strong>Antarctic Treaty (1959):</strong> Originally signed by 12 nations (now 56). It designates Antarctica as a scientific preserve, guarantees freedom of scientific investigation, suspends all territorial claims, and strictly bans military activity and nuclear testing.</li>
        <li><strong>Madrid Protocol (1991):</strong> The Protocol on Environmental Protection. Crucially, it established a 50-year ban on all commercial mining (until 2041), sets strict waste management rules, requires Environmental Impact Assessments (EIAs) for all activities, and designates protected areas (ASMAs, ASPAs).</li>
        <li><strong>CCAMLR:</strong> The Commission for the Conservation of Antarctic Marine Living Resources manages fishing, setting precautionary catch limits for krill and establishing large Marine Protected Areas (MPAs).</li>
    </ul>
</div>
"""

html_32_p2 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.2 Threats to Antarctic + Management (Bilingual)</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Ozone Depletion & Climate Change</h2>
<p>Ozone Depletion: CFCs destroy ozone. Antarctic ozone hole worst each Sept-Oct. Increased UV-B radiation damages phytoplankton DNA, disrupting food web. Montreal Protocol 1987 banned CFCs. Climate Change: Southern Ocean warming 2x global avg; West Antarctic Ice Sheet losing 150bn tonnes/yr; ice shelf collapse. Sea ice declining &rarr; penguin habitat loss (chicks drown). 58m global sea level rise if all ice melts.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Suy giảm tầng ozone & Biến đổi khí hậu: CFC phá hủy ozone. Lỗ thủng tầng ozone ở Nam Cực tồi tệ nhất vào tháng 9-10. Bức xạ tia cực tím (UV radiation) tăng làm hỏng DNA của tảo phù du, gây gián đoạn mạng lưới thức ăn. Nghị định thư Montreal 1987 cấm sử dụng CFC. Biến đổi khí hậu: Đại dương Nam ấm lên gấp 2 lần mức trung bình toàn cầu; thềm băng (ice shelf) sụp đổ. Băng biển giảm &rarr; mất môi trường sống của chim cánh cụt. Mực nước biển dâng (sea level rise) 58m nếu toàn bộ băng tan.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Commercial Fishing & Tourism</h2>
<p>Krill fishing (300,000+ tonnes/yr) for omega-3/aquaculture. Overfishing krill collapses entire food web. Tourism: 75,000+ tourists/yr. Ships risk fuel oil spills, invasive species on boots, penguin colony disturbance. IAATO limits ship size, landing sites, visitor numbers, mandatory wildlife guidelines.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Đánh bắt cá thương mại & Du lịch: Đánh bắt tôm krill (krill fishing) hơn 300.000 tấn/năm để làm dầu omega-3 và thức ăn thủy sản. Đánh bắt quá mức tôm krill làm sụp đổ toàn bộ mạng lưới thức ăn. Du lịch: Hơn 75.000 du khách. Rủi ro từ tàu thuyền: tràn dầu mỏ, mang theo loài xâm lấn (invasive species), làm phiền các bầy chim cánh cụt. IAATO giới hạn kích thước tàu và số lượng du khách.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Scientific Research & Management</h2>
<p>Scientific Research: 70+ stations. Impacts: fuel spills, physical damage to mosses (take centuries to recover). Management: Antarctic Treaty (1959): no military use, nuclear testing, territorial claims suspended. Madrid Protocol (1991): 50-year mining ban (until 2041), strict waste rules. CCAMLR: manages fishing, sets krill catch limits.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Nghiên cứu khoa học & Quản lý: Có hơn 70 trạm nghiên cứu. Tác động: tràn dầu, gây thiệt hại vật lý cho rêu. Quản lý: Hiệp ước Nam Cực (Antarctic Treaty 1959): cấm quân sự hóa, thử nghiệm hạt nhân, đình chỉ các yêu sách lãnh thổ. Nghị định thư Madrid 1991: lệnh cấm khai thác mỏ 50 năm, quy tắc xử lý rác thải nghiêm ngặt. Ủy ban bảo tồn sinh vật biển Nam Cực (CCAMLR): quản lý việc đánh bắt cá.
</div>
"""

html_33_p1 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.3 Tropical Rainforest Characteristics</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Location & Climate</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <p>Tropical rainforests are situated in the equatorial zone, roughly between 10&deg;N and 10&deg;S of the equator.</p>
    <ul style="margin-top:8px;">
        <li><strong>Major Regions:</strong> The Amazon in South America (contains 60% of all TRF), the Congo Basin in Africa (18%), and regions in SE Asia like Borneo, Sumatra, and Indonesia (18%).</li>
        <li><strong>Temperature:</strong> Hot all year round, maintaining a consistent 26-28&deg;C. The diurnal (daily) temperature range of about 8&deg;C is actually greater than the seasonal temperature range.</li>
        <li><strong>Precipitation:</strong> Receives high rainfall, between 2000-4000mm annually, with no distinct dry season. Humidity is constantly high (80-90%).</li>
        <li><strong>Mechanism:</strong> The ITCZ (Intertropical Convergence Zone) drives intense convectional rainfall, leading to heavy afternoon thunderstorms almost daily as warm, moist air rapidly rises, cools, and condenses.</li>
    </ul>
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Rainforest Layers</h2>
<p>The rainforest is structurally complex, divided into distinct vertical layers, each offering unique ecological niches.</p>

<svg viewBox="0 0 800 600" style="max-width:420px; height:auto; display:block; margin:0 auto; margin-top:24px; margin-bottom:8px;">
    <rect x="0" y="0" width="800" height="600" fill="#f8fafc" />
    
    <!-- Layers Backgrounds -->
    <rect x="50" y="50" width="700" height="150" fill="#bbf7d0" opacity="0.5"/>
    <text x="70" y="80" font-size="20" font-weight="bold" fill="#166534">Emergent Layer (35-50m)</text>
    <text x="70" y="110" font-size="14" fill="#14532d">Isolated giants (kapok, Brazil nut). Eagles, bats, macaws.</text>

    <rect x="50" y="200" width="700" height="150" fill="#86efac" opacity="0.6"/>
    <text x="70" y="230" font-size="20" font-weight="bold" fill="#166534">Canopy (25-35m)</text>
    <text x="70" y="260" font-size="14" fill="#14532d">Dense interlocking leaves. Intercepts 80% sunlight & 50% rain.</text>
    <text x="70" y="280" font-size="14" fill="#14532d">Home to monkeys, sloths, toucans, epiphytes.</text>

    <rect x="50" y="350" width="700" height="150" fill="#4ade80" opacity="0.7"/>
    <text x="70" y="380" font-size="20" font-weight="bold" fill="#14532d">Understory (5-25m)</text>
    <text x="70" y="410" font-size="14" fill="#064e3b">Dappled light, climbing lianas, jaguars, tree frogs, snakes.</text>

    <rect x="50" y="500" width="700" height="80" fill="#22c55e" opacity="0.8"/>
    <text x="70" y="530" font-size="20" font-weight="bold" fill="#064e3b">Forest Floor (0-5m)</text>
    <text x="70" y="560" font-size="14" fill="#022c22">&lt;1% sunlight. Fungi, decomposers, beetles, tapirs, buttress roots.</text>

    <!-- Simple Tree Graphics -->
    <path d="M 650 580 L 650 100 L 600 80 L 650 50 L 700 80 Z" fill="#15803d"/>
    <path d="M 450 580 L 450 250 L 380 220 L 450 180 L 520 220 Z" fill="#16a34a"/>
    <path d="M 250 580 L 250 400 L 200 380 L 250 350 L 300 380 Z" fill="#22c55e"/>
</svg>
<div style="font-size:13px; color:#94a3b8; font-style:italic; text-align:center; margin-top:8px;">Diagram: The Four Layers of the Tropical Rainforest.</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Biodiversity</h2>
<p>Tropical rainforests house 50% of the world's known species despite covering only 6% of the Earth's land surface.</p>
<ul style="margin-top:8px;">
    <li>The Amazon alone contains over 40,000 plant species, 3,000 fish species, and 1,300 bird species. Millions of insect species remain undiscovered.</li>
    <li><strong>Reasons for high biodiversity:</strong>
        <ul>
            <li><strong>Stability:</strong> The warm, stable climate has persisted for millions of years, allowing extensive time for evolution.</li>
            <li><strong>Productivity:</strong> Constant sunlight and water allow year-round photosynthesis, supporting massive food chains.</li>
            <li><strong>Complexity:</strong> The multi-layered structure creates millions of specialized micro-habitats (niches).</li>
        </ul>
    </li>
</ul>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">4. The Nutrient Cycle</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <p>The rainforest nutrient cycle is rapid but fragile.</p>
    <ul style="margin-top:8px;">
        <li>Heat and humidity cause extremely rapid decomposition of leaf litter by fungi and bacteria (taking days rather than months).</li>
        <li><strong>Crucial Point:</strong> Most nutrients are locked up <em>in the living biomass</em> (plants and animals), not in the soil.</li>
        <li>The soil is thin, highly acidic, and nutrient-poor due to heavy rainfall washing minerals away (a process called <strong>leaching</strong>, resulting in red <em>laterite</em> soil).</li>
        <li>Plants use shallow roots and rely on a vast underground network of mycorrhizal fungi to rapidly reabsorb nutrients the moment they are broken down.</li>
        <li>If the forest is cleared, the nutrient store is destroyed, and the exposed soil washes away in 2-3 years, becoming useless for agriculture.</li>
    </ul>
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">5. Plant and Animal Adaptations</h2>
<ul style="margin-top:8px;">
    <li><strong>Drip Tips:</strong> Pointed leaf tips (e.g., Begonia) and waxy cuticles allow heavy rain to run off quickly, preventing harmful fungal or algae growth on the leaf surface.</li>
    <li><strong>Buttress Roots:</strong> Massive, wide ridges at the base of tall trees (e.g., Silk-cotton tree) provide stability in the shallow, nutrient-poor soil.</li>
    <li><strong>Lianas:</strong> Thick woody vines (e.g., rattan) that root in the soil but use trees to climb rapidly up into the canopy to reach sunlight.</li>
    <li><strong>Epiphytes:</strong> Plants (e.g., orchids, bromeliads) that grow entirely on the branches of other trees high in the canopy to access light, absorbing moisture directly from the humid air.</li>
    <li><strong>Strangler Figs:</strong> Seeds germinate in the canopy, and roots grow downwards, eventually enveloping and killing the host tree to take its place.</li>
    <li><strong>Animal Adaptations:</strong> Incredible camouflage (leafy sea dragons, stick insects), vivid warning colors (poison dart frogs denoting toxicity), nocturnal lifestyles to avoid daytime heat, and highly specialized diets to reduce competition.</li>
</ul>
"""

html_33_p2 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.3 Tropical Rainforest Characteristics (Bilingual)</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Location & Climate</h2>
<p>Location: 10&deg;N–10&deg;S, equatorial zone. Amazon (South America), Congo (Africa), SE Asia. Climate: 26-28&deg;C year-round, 2000-4000mm rainfall/yr, no distinct dry season, humidity 80-90%. ITCZ causes convectional rainfall (afternoon thunderstorms daily).</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Vị trí & Khí hậu: Nằm ở vùng xích đạo (equator). Lưu vực Amazon, Congo, Đông Nam Á. Khí hậu: 26-28&deg;C quanh năm, lượng mưa 2000-4000mm/năm, không có mùa khô rõ rệt. Gió mùa ITCZ gây ra mưa đối lưu (convectional rainfall) với các trận giông bão vào buổi chiều.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Rainforest Layers & Biodiversity</h2>
<p>Layers: Emergent (35-50m, giant trees); Canopy (25-35m, dense leaves intercept 80% sunlight); Understory (5-25m, dappled light); Forest floor (0-5m, &lt;1% sunlight, decomposers). Biodiversity: 50% of world's species on 6% of land. High biodiversity due to stable warm climate, high productivity, and structural complexity (many niches).</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Các tầng rừng & Đa dạng sinh học: Tầng vượt tán (Emergent), tán cây (Canopy) cản 80% ánh sáng, tầng cây bụi (Understory), nền rừng (Forest floor) có sinh vật phân hủy (decomposer). Đa dạng sinh học (biodiversity) cực kỳ cao nhờ khí hậu ấm áp ổn định và cấu trúc phức tạp.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Nutrient Cycle & Adaptations</h2>
<p>Nutrient Cycle: Rapid decomposition. Most nutrients held IN living biomass, NOT in soil. Soil is thin, leached by rain (laterization). Adaptations: Drip tips (pointed leaf tips shed water); buttress roots (support in shallow soil); lianas (woody climbers); epiphytes (grow on other plants); animals use camouflage or vivid warning colors.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Chu trình dinh dưỡng (Nutrient cycle) & Thích nghi: Phân hủy nhanh. Dinh dưỡng chủ yếu nằm ở sinh khối sống, KHÔNG phải trong đất. Đất mỏng, bị rửa trôi khoáng chất (leaching) và quá trình laterit hóa (laterization). Thích nghi: Đầu lá nhọn chảy nước (drip tips); rễ bành (buttress roots) giúp đứng vững; dây leo (liana); thực vật ký sinh trên không (epiphyte).
</div>
"""

html_34_p1 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.4 Threats to Rainforest + Management</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Scale of Deforestation</h2>
<p>Approximately 10 million hectares of tropical rainforest are lost every year, equating to 27 football pitches every minute. Over 17% of the Amazon has already been destroyed, and global rainforest cover has halved since the 1970s. Scientists warn of a tipping point: if 20-25% of the Amazon is lost, it may trigger irreversible "savannification", releasing 140 billion tonnes of stored CO&sub2;.</p>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Causes of Deforestation</h2>
<p><em>Click the panels below to learn about the primary drivers of deforestation:</em></p>

<style>
.cause-panel { background: #f0fdf4; border: 1px solid #22c55e; margin-bottom: 10px; border-radius: 4px; }
.cause-panel summary { padding: 12px; font-weight: bold; cursor: pointer; outline: none; list-style: none; color: #166534; }
.cause-panel summary::-webkit-details-marker { display: none; }
.cause-panel summary::before { content: "▶ "; font-size: 12px; color: #22c55e; display: inline-block; width: 20px; transition: 0.2s; }
.cause-panel[open] summary::before { content: "▼ "; }
.cause-panel p { padding: 0 12px 12px 28px; margin: 0; color: #334155; }
</style>

<details class="cause-panel">
  <summary>Commercial Logging</summary>
  <p>Extraction of valuable hardwoods like mahogany, teak, and rosewood for luxury furniture and construction. Logging operations (often illegal) build deep access roads, which opens up pristine forest to other forms of exploitation.</p>
</details>

<details class="cause-panel">
  <summary>Cattle Ranching</summary>
  <p>The number one cause of deforestation in the Amazon, accounting for 80% of forest loss. Huge tracts of land are cleared (often using fire) to graze cattle. Brazil is the world's biggest beef exporter, driven by global fast food demand.</p>
</details>

<details class="cause-panel">
  <summary>Palm Oil Plantations</summary>
  <p>The primary driver of deforestation in Southeast Asia. Over 50 million hectares have been cleared in Borneo and Sumatra since 1970. Palm oil is highly lucrative and found in 50% of supermarket products (soap, bread, biofuel), pushing species like the Orangutan to the brink of extinction.</p>
</details>

<details class="cause-panel">
  <summary>Soy Farming</summary>
  <p>Vast monocultures of soy in Brazil and Argentina, grown primarily not for human consumption, but as protein-rich feed for livestock (cattle, pigs, chickens) in Europe and China.</p>
</details>

<details class="cause-panel">
  <summary>Subsistence Farming</summary>
  <p>Small-scale "slash and burn" (shifting cultivation) by millions of impoverished farmers to feed their families. While traditionally sustainable at low population densities, the sheer number of farmers today causes widespread cumulative damage.</p>
</details>

<details class="cause-panel">
  <summary>Mining</summary>
  <p>Extraction of iron ore (e.g., the massive Carajás mine in Brazil), gold, copper, and bauxite. Illegal gold miners (garimpeiros) use mercury, which severely pollutes river systems.</p>
</details>

<details class="cause-panel">
  <summary>Dams and Infrastructure</summary>
  <p>Large hydroelectric projects, like the Belo Monte dam in Brazil, flood massive areas of forest and indigenous lands. Infrastructure projects like the Trans-Amazonian Highway fragment habitats.</p>
</details>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Environmental & Social Effects</h2>
<ul style="margin-top:8px;">
    <li><strong>Biodiversity Loss:</strong> Estimated 50-100 species go extinct every day due to habitat destruction.</li>
    <li><strong>Soil Erosion:</strong> Without the tree canopy to intercept rain, heavy downpours wash away the thin topsoil, leading to severe gullying and river siltation.</li>
    <li><strong>Water Cycle Disruption:</strong> Less transpiration from trees means less moisture in the air, leading to reduced regional rainfall and localized droughts.</li>
    <li><strong>Climate Change:</strong> Burning forests releases massive amounts of CO&sub2;, while destroying the trees eliminates a crucial global "carbon sink". Deforestation accounts for about 10% of global greenhouse gas emissions.</li>
    <li><strong>Human Impact:</strong> Displacement of indigenous tribes (e.g., the Yanomami and Kayap&oacute;) who lose their ancestral homes and way of life. Furthermore, humanity loses potential medical breakthroughs; 25% of western drugs are derived from rainforest plants.</li>
</ul>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">4. Management Strategies</h2>
<div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:14px; border-radius:8px; margin-bottom:24px;">
    <table style="width:100%; border-collapse: collapse; margin-top:8px;">
        <tr style="border-bottom:1px solid #cbd5e1; text-align:left;">
            <th style="padding:8px;">Strategy</th>
            <th style="padding:8px;">Description</th>
        </tr>
        <tr style="border-bottom:1px solid #e2e8f0;">
            <td style="padding:8px; font-weight:bold;">National Parks</td>
            <td style="padding:8px;">Legal protection of land. 12% of the Amazon is protected (e.g., Tumucumaque National Park covers 3.8M ha).</td>
        </tr>
        <tr style="border-bottom:1px solid #e2e8f0;">
            <td style="padding:8px; font-weight:bold;">Selective Logging</td>
            <td style="padding:8px;">Felling only mature, highly valued trees while leaving the canopy and understory intact. Requires ~60 years for the forest to recover.</td>
        </tr>
        <tr style="border-bottom:1px solid #e2e8f0;">
            <td style="padding:8px; font-weight:bold;">FSC Certification</td>
            <td style="padding:8px;">The Forest Stewardship Council certifies timber that is sustainably sourced, relying on consumer pressure to boycott uncertified wood.</td>
        </tr>
        <tr style="border-bottom:1px solid #e2e8f0;">
            <td style="padding:8px; font-weight:bold;">REDD+ & Debt Swaps</td>
            <td style="padding:8px;">Wealthy nations pay developing countries to protect forests as carbon sinks (e.g., Norway paid Brazil $1bn). Debt-for-nature swaps cancel national debt in exchange for conservation.</td>
        </tr>
        <tr style="border-bottom:1px solid #e2e8f0;">
            <td style="padding:8px; font-weight:bold;">Ecotourism</td>
            <td style="padding:8px;">Provides local communities with sustainable income from intact forests, creating jobs without destruction (e.g., Costa Rica).</td>
        </tr>
        <tr>
            <td style="padding:8px; font-weight:bold;">Agroforestry</td>
            <td style="padding:8px;">Growing food crops interspersed with trees, which maintains soil stability, carbon storage, and some biodiversity.</td>
        </tr>
    </table>
</div>
"""

html_34_p2 = """
<h1 style="color:#15803d; border-bottom:3px solid #4ade80; padding-bottom:8px;">3.4 Threats to Rainforest + Management (Bilingual)</h1>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">1. Causes of Deforestation</h2>
<p>Commercial logging (mahogany/teak); Cattle ranching (80% of Amazon loss); Palm oil (SE Asia, affects orangutans); Soy farming (feed for livestock); Subsistence farming (slash and burn); Mining (gold, iron ore); Dams/Infrastructure. Tipping point: 20-25% Amazon loss may trigger savannification.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Nguyên nhân phá rừng (Deforestation): Khai thác gỗ thương mại (commercial logging); Chăn nuôi gia súc quy mô lớn (cattle ranching); Trồng cọ lấy dầu (palm oil); Trồng đậu nành; Nông nghiệp tự cung tự cấp (subsistence farming) bằng cách đốt rẫy (slash and burn); Khai thác mỏ; Xây đập. Điểm bùng phát (tipping point): Mất 20-25% rừng Amazon có thể biến nó thành xavan.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">2. Effects</h2>
<p>Biodiversity loss; soil erosion; water cycle disruption (less evapotranspiration &rarr; drought); climate change (CO&sub2; release + reduced carbon sink); displacement of indigenous tribes; loss of potential medicines.</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Tác động: Suy giảm đa dạng sinh học; xói mòn đất (soil erosion); gián đoạn vòng tuần hoàn nước; biến đổi khí hậu do phát thải carbon (carbon release); xua đuổi người bản địa (indigenous people); mất đi các nguồn thuốc chữa bệnh tiềm năng.
</div>

<h2 style="color:#1e293b; border-bottom:2px solid #4ade80; padding-bottom:4px; margin-top:32px;">3. Management</h2>
<p>National parks (protected areas); Selective logging (cut only specific trees); FSC certification (sustainable sourcing); REDD+ (wealthy nations pay to protect forests); Ecotourism (income from intact forest); Agroforestry (crops + trees).</p>
<div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">
    Quản lý: Vườn quốc gia (national park); Khai thác gỗ có chọn lọc (selective logging); Chứng nhận FSC; Chương trình REDD+ (Giảm phát thải từ phá rừng); Du lịch sinh thái (ecotourism); Nông lâm kết hợp (agroforestry).
</div>
"""

pages = [
    ("47826f24-81dd-457c-a23e-5e5ee172604d", html_31_p1),
    ("06661280-13d0-4e87-92a7-715379c95547", html_31_p2),
    ("1024e019-4073-4186-9a49-aae63a53f80a", html_32_p1),
    ("10c58000-7bbe-44f0-88d5-ae26ecc0a8a6", html_32_p2),
    ("0ab835c5-4ae2-44de-8250-8771acbf5cac", html_33_p1),
    ("31bd1d71-0b97-4de6-ba68-951e45aab17e", html_33_p2),
    ("f2286822-5b3c-4670-859e-34267ab4d9f4", html_34_p1),
    ("bab9af41-a94b-43dd-90b4-0ec077bd7483", html_34_p2)
]

for page_id, raw_html in pages:
    encoded_html = format_html(to_entities(raw_html))
    make_request(page_id, encoded_html)

print("All requests completed.")
