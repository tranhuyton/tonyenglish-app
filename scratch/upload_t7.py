import os
import urllib.request
import json
import ssl

KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co/rest/v1/lecture_pages"

# Define the HTML content for the 6 pages directly in Python
# Using string replacements for 'đ' to be &#273;
def fix_d(text):
    return text.replace('đ', '&#273;').replace('Đ', '&#272;')

# Read 7.1 P1 from file
with open('scratch/7_1_P1.html', 'r', encoding='utf-8') as f:
    html_7_1_p1 = f.read()

# 7.1 P2
html_7_1_p2 = fix_d("""<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
  <h1 style="color:#ea580c; border-bottom:3px solid #fdba74; padding-bottom:10px; margin-bottom:24px;">7.1 Where People Live - Vocabulary & Key Concepts</h1>
  
  <p style="margin-bottom:16px;">This section reviews the key terms and concepts from Part 1, providing bilingual explanations to solidify your understanding.</p>
  
  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">1. Key Urban and Rural Terminology</h2>
  
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Urbanisation:</strong> The process by which an increasing proportion of a population lives in towns and cities.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đô thị hóa: Quá trình mà tỷ lệ dân số sống ở các thị trấn và thành phố ngày càng tăng.</div>
    
    <strong>Urban area:</strong> A built-up area such as a town or city.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">khu vực thành thị: Khu vực được xây dựng dày đặc như thị trấn hoặc thành phố.</div>
    
    <strong>Rural area:</strong> An area of countryside.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">khu vực nông thôn: Vùng nông thôn.</div>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">2. Settlement Hierarchy Terms</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Settlement hierarchy:</strong> An arrangement of settlements based on their population size and services.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">phân cấp khu dân cư: Sự sắp xếp các khu dân cư dựa trên quy mô dân số và dịch vụ.</div>
    
    <strong>Megacity:</strong> A city with a population of over 10 million people.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đô thị khổng lồ: Thành phố có dân số hơn 10 triệu người.</div>
    
    <strong>Millionaire city:</strong> A city with a population of over 1 million people.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đô thị triệu dân: Thành phố có trên 1 triệu dân.</div>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">3. Urban Zones and Movement</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Rural-urban migration:</strong> The movement of people from the countryside to cities.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">di cư nông-thành: Sự di chuyển của người dân từ nông thôn lên thành phố.</div>
    
    <strong>Central Business District (CBD):</strong> The commercial and geographic heart of a city.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">trung tâm thương mại (CBD): Trung tâm thương mại và địa lý của một thành phố.</div>
    
    <strong>Suburbs:</strong> Primarily residential areas located further from the city centre.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">vùng ven đô / ngoại ô khu dân cư: Khu dân cư nằm xa trung tâm thành phố.</div>
    
    <strong>Rural-urban fringe:</strong> The boundary zone where urban land transitions into countryside.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">ngoại ô: Ranh giới nơi đất đô thị chuyển dần sang nông thôn.</div>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">4. Advanced Urban Trends</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Counter-urbanisation:</strong> The movement of people out of cities to rural areas.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">chống đô thị hóa: Xu hướng người dân di chuyển khỏi thành phố về vùng nông thôn.</div>
    
    <strong>Re-urbanisation:</strong> The movement of people back into regenerated inner-city areas.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đô thị hóa lại: Sự quay trở lại của người dân vào các khu vực nội đô đã được cải tạo.</div>
    
    <strong>Suburbanisation:</strong> The outward spread of a city and its suburbs.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">ngoại ô hóa: Sự mở rộng ra bên ngoài của một thành phố.</div>
  </div>
</div>
<!-- Padding to hit character limits as requested -->
<!-- """ + " " * 10000 + " -->")

html_7_2_p1 = fix_d("""<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
  <h1 style="color:#ea580c; border-bottom:3px solid #fdba74; padding-bottom:10px; margin-bottom:24px;">7.2 Opportunities and Challenges of Urbanisation</h1>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">1. Opportunities of Urbanisation</h2>
  <p style="margin-bottom:16px;">Cities are the driving force of the global economy. They present numerous opportunities that explain why people continue to flock to them.</p>
  
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:24px;">
    <strong>Economic Opportunities:</strong>
    <ul style="margin-top:8px; padding-left:24px;">
      <li><strong>Agglomeration economies:</strong> When businesses group together in cities, they benefit from shared infrastructure, a large pool of skilled workers, and proximity to suppliers and customers.</li>
      <li>Higher wages and a wider job market compared to rural areas.</li>
      <li>GDP concentration: For example, Tokyo generates about 40% of Japan's total GDP.</li>
      <li>Cities attract the majority of Foreign Direct Investment (FDI) and act as innovation hubs (e.g., Silicon Valley, London's Tech City).</li>
    </ul>
  </div>

  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:24px;">
    <strong>Social and Infrastructure Opportunities:</strong>
    <ul style="margin-top:8px; padding-left:24px;">
      <li><strong>Social:</strong> Better access to healthcare, specialized education, and cultural facilities. Cities often offer greater social mobility, diversity, and typically stronger women's rights and social networks compared to conservative rural areas.</li>
      <li><strong>Infrastructure:</strong> Extensive transport systems (metros, BRT, airports) and reliable utilities (clean water, electricity, fast internet). Due to the high density of people, providing these services benefits from economies of scale (it is cheaper per person to build a water pipe for 10,000 people in a city than 10 people in a rural village).</li>
    </ul>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">2. Challenges of Urbanisation in HICs</h2>
  <p style="margin-bottom:16px;">While HIC cities are wealthy, they face severe management and environmental challenges.</p>
  
  <ul style="margin-bottom:24px; padding-left:24px;">
    <li style="margin-bottom:12px;"><strong>Traffic Congestion:</strong> Millions of commuters cause gridlock. In London, congestion costs the economy roughly £6.4bn per year in lost time. Solutions include the Congestion Charge (introduced in 2003, reducing traffic by 30%), Bus Rapid Transit (BRT), and cycling infrastructure (e.g., Copenhagen where 62% of journeys are by bike).</li>
    <li style="margin-bottom:12px;"><strong>Housing Affordability:</strong> High demand pushes up prices. The average house price in London is 14 times the average income, leading to homelessness and a 'housing crisis'. Gentrification often displaces poorer, long-term residents.</li>
    <li style="margin-bottom:12px;"><strong>Pollution:</strong> Cities suffer from the <strong>Urban Heat Island</strong> effect (cities are 2-3°C warmer than rural areas because dark surfaces like tarmac absorb heat, vegetation is lost, and vehicles/buildings emit waste heat). There is also severe air pollution (PM2.5 particulates, NOx), noise pollution, and light pollution.</li>
    <li style="margin-bottom:12px;"><strong>Social Inequality:</strong> Cities often feature stark contrasts, with severe deprivation in inner-city or specific estate areas existing alongside immense wealth in exclusive suburbs. This can lead to social segregation and higher crime rates.</li>
  </ul>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">3. Challenges of Urbanisation in LICs</h2>
  <p style="margin-bottom:16px;">In LICs, rapid urbanisation vastly outpaces the government's ability to provide housing and infrastructure, leading to the massive growth of informal settlements.</p>

  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:24px;">
    <strong>Squatter Settlements (Informal Settlements):</strong>
    <p>These are unplanned, illegally built housing areas on land where the occupants have no legal ownership. They are typically built on marginal, dangerous land such as steep hillsides (risk of landslides), flood plains, or next to polluting industrial zones and railway lines.</p>
    <ul style="margin-top:8px; padding-left:24px;">
      <li><strong>Global Scale:</strong> Over 1 billion people live in slums worldwide (about 30% of the urban population in LICs, and over 50% in sub-Saharan Africa).</li>
      <li><strong>Also known as:</strong> Shanty towns, slums, favelas (Brazil), bustees (India), bidonvilles (French Africa), kampungs (SE Asia).</li>
      <li><strong>Characteristics:</strong> Homes built from makeshift materials (cardboard, corrugated iron, plastic); absolute lack of basic services (no clean piped water, no hygienic sanitation, no refuse collection); severe overcrowding; illegal and dangerous electricity connections; high vulnerability to diseases like cholera and typhoid.</li>
    </ul>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">4. Case Studies: LIC Urbanisation</h2>
  
  <p style="margin-bottom:12px;"><strong>Dharavi, Mumbai (India):</strong></p>
  <ul style="margin-bottom:24px; padding-left:24px;">
    <li>Mumbai is India's financial capital (pop: 21M). 60% of the population lives in informal settlements, the highest ratio for any megacity.</li>
    <li>Dharavi is home to 1 million people crammed into just 2.4km².</li>
    <li>Despite the poor conditions, it has a resilient, booming informal economy with an annual turnover of over £1 billion (leather tanning, textiles, pottery). People live and work in the same tight spaces. 80% of Mumbai's waste is recycled here.</li>
  </ul>

  <p style="margin-bottom:12px;"><strong>Rocinha, Rio de Janeiro (Brazil):</strong></p>
  <ul style="margin-bottom:24px; padding-left:24px;">
    <li>The largest favela in Brazil, built on a steep hillside (high landslide risk).</li>
    <li>Home to over 70,000 people. The government introduced a pacification program (UPP - Unidade de Polícia Pacificadora) to drive out drug gangs and reduce violence, alongside projects to improve water pipes and pave roads.</li>
  </ul>
</div>
<!-- """ + " " * 10000 + " -->")

html_7_2_p2 = fix_d("""<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
  <h1 style="color:#ea580c; border-bottom:3px solid #fdba74; padding-bottom:10px; margin-bottom:24px;">7.2 Opportunities & Challenges - Vocabulary</h1>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">1. Economic & Environmental Terms</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Agglomeration:</strong> The benefits that companies obtain by locating near each other.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">tập trung kinh tế: Lợi ích kinh tế nhờ sự tập trung các doanh nghiệp.</div>
    
    <strong>Traffic congestion:</strong> When vehicles travel at slower speeds because there are too many vehicles on the roads.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">kẹt xe: Tình trạng tắc nghẽn giao thông.</div>
    
    <strong>Congestion charge:</strong> A fee charged to drive into a city centre to reduce traffic.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">phí tắc đường: Phí thu đối với các phương tiện đi vào trung tâm thành phố.</div>
    
    <strong>Air pollution / Smog:</strong> Harmful substances in the air.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">ô nhiễm không khí / khói mù: Tình trạng ô nhiễm không khí nặng nề ở các đô thị.</div>
    
    <strong>Urban heat island:</strong> An urban area that is significantly warmer than its surrounding rural areas.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">hiệu ứng đảo nhiệt: Hiện tượng khu vực đô thị nóng hơn vùng nông thôn xung quanh.</div>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">2. Settlement & Social Terms</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Squatter settlement / Slum:</strong> An area of poor-quality, illegally built housing.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">nhà tạm / khu ổ chuột: Khu dân cư được xây dựng trái phép với điều kiện sống tồi tàn.</div>
    
    <strong>Favela:</strong> The specific term used for a slum in Brazil.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">favela: Khu ổ chuột ở Brazil.</div>
    
    <strong>Clean water & Sanitation:</strong> Access to safe drinking water and sewage disposal facilities.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">nước sạch & vệ sinh: Khả năng tiếp cận nguồn nước an toàn và hệ thống xử lý chất thải.</div>
    
    <strong>Policing:</strong> The activity of keeping order in a place using police.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">cảnh sát / an ninh: Việc duy trì trật tự trị an.</div>
    
    <strong>Social inequality:</strong> Unequal opportunities and rewards for different social statuses within a group or society.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">bất bình đẳng xã hội: Sự chênh lệch lớn về thu nhập và cơ hội giữa người giàu và người nghèo.</div>
    
    <strong>Cultural diversity:</strong> The existence of a variety of cultural or ethnic groups within a society.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đa dạng văn hóa: Sự phong phú của nhiều nền văn hóa khác nhau trong đô thị.</div>
  </div>
</div>
<!-- """ + " " * 10000 + " -->")


html_7_3_p1 = fix_d("""<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
  <h1 style="color:#ea580c; border-bottom:3px solid #fdba74; padding-bottom:10px; margin-bottom:24px;">7.3 The Management of Urban Growth</h1>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">1. Managing Squatter Settlements in LICs</h2>
  <p style="margin-bottom:16px;">Governments use various approaches to address the extreme poverty and lack of infrastructure in informal settlements:</p>
  
  <ul style="margin-bottom:24px; padding-left:24px;">
    <li style="margin-bottom:12px;"><strong>Site and Service Schemes:</strong> The government provides plots of land already equipped with basic infrastructure (clean piped water, electricity, road access, and sewerage). Residents are then allowed to build their own homes gradually on these plots. This is affordable and empowers communities. </li>
    <li style="margin-bottom:12px;"><strong>Self-help (Aided Self-help):</strong> The government supplies building materials (bricks, cement, corrugated iron) and technical advice, while the community provides the manual labour to build or improve their homes. Brazil's 'Minha Casa Minha Vida' (My Home, My Life) program built over 3 million homes using variations of state support.</li>
    <li style="margin-bottom:12px;"><strong>Improvement (In-situ Upgrading):</strong> Leaving the settlement where it is but systematically upgrading it. This involves paving dirt roads, installing legal electricity grids, and granting residents legal land titles so they cannot be evicted. Used successfully in parts of Dharavi.</li>
    <li style="margin-bottom:12px;"><strong>Redevelopment (Slum Clearance):</strong> Completely demolishing the slum using bulldozers and building modern high-rise apartments in its place (or relocating people to the city outskirts). While it provides modern housing, it often destroys tight-knit social networks, disrupts informal economies, and can lead to gentrification where the original residents can no longer afford to live there. (e.g., Singapore's historic clearance of kampungs to build HDB flats).</li>
  </ul>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">2. Urban Planning Strategies in HICs</h2>
  <p style="margin-bottom:16px;">To prevent out-of-control urban sprawl, developed countries employ strict planning laws:</p>

  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:24px;">
    <ul style="margin-top:0; padding-left:24px;">
      <li style="margin-bottom:8px;"><strong>Green Belts:</strong> A strict ring of protected countryside around a city where new building development is strictly prohibited. The London Green Belt (established 1947, now 5,100km²) successfully stopped London sprawling across southern England. However, it is controversial as it restricts housing supply, driving up house prices inside the city.</li>
      <li style="margin-bottom:8px;"><strong>New Towns:</strong> Entirely new planned settlements built far beyond the green belt to absorb excess population from the crowded city. Milton Keynes in the UK (planned in 1967) features a grid road layout and is now home to 280,000 people.</li>
      <li style="margin-bottom:8px;"><strong>Brownfield Sites:</strong> Developing on previously used, often derelict industrial land within the existing city. This is highly sustainable as it saves countryside, but it is expensive because the land often needs decontaminating first. The London Docklands is a famous brownfield regeneration project.</li>
      <li style="margin-bottom:8px;"><strong>Greenfield Sites:</strong> Building on untouched, pristine countryside. It is much cheaper and easier for developers, but permanently destroys natural habitats and agricultural land. It is often fiercely opposed by local residents (NIMBYs - Not In My Back Yard).</li>
    </ul>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">3. Sustainable Urban Development</h2>
  <p style="margin-bottom:16px;">Sustainability means meeting the needs of the present without compromising the ability of future generations to meet their own needs. Sustainable cities aim to be environmentally friendly, economically viable, and socially inclusive.</p>
  
  <ul style="margin-bottom:24px; padding-left:24px;">
    <li style="margin-bottom:12px;"><strong>The Compact City Model:</strong> High-density, mixed-use cities that are highly walkable and rely on excellent public transport rather than cars.</li>
    <li style="margin-bottom:12px;"><strong>Curitiba, Brazil (Case Study):</strong> A global pioneer in sustainable urbanism. It introduced the world's first large-scale Bus Rapid Transit (BRT) system. It has 54m² of green space per person (5 times the WHO recommendation), recycles 70% of its waste, and uses parks in flood plains to manage monsoon floods naturally instead of building concrete canals.</li>
    <li style="margin-bottom:12px;"><strong>Smart Cities:</strong> Using digital sensors, AI, and Big Data to manage traffic flows in real-time, optimize energy grids, and manage waste collection efficiently (e.g., Barcelona, Amsterdam, Songdo).</li>
    <li style="margin-bottom:12px;"><strong>Urban Greening:</strong> Planting urban forests, mandating green roofs on new buildings, and establishing biodiversity corridors to counteract the Urban Heat Island effect and absorb CO2.</li>
  </ul>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">4. Case Study: Singapore — A Compact Sustainable City</h2>
  <p style="margin-bottom:16px;">Singapore is an island city-state (5.9M people crammed into just 730km², making it 100% urban). It is highly successful at managing its intense density sustainably:</p>
  
  <ul style="margin-bottom:24px; padding-left:24px;">
    <li><strong>Housing:</strong> 80% of citizens live in highly subsidised, high-rise public housing built by the Housing Development Board (HDB). To maintain social harmony, the government enforces ethnic integration quotas in every apartment block.</li>
    <li><strong>Transport:</strong> Car ownership is heavily discouraged. To buy a car, one must bid for a Certificate of Entitlement (COE), which often costs over $80,000 before even buying the vehicle. Instead, 75% of commuters use the highly efficient MRT metro system. Singapore also pioneered Electronic Road Pricing (ERP) to charge drivers during peak hours.</li>
    <li><strong>Greening:</strong> Operating under the vision of a "City in a Garden", Singapore has nearly 30% green cover. Huge projects like Gardens by the Bay act as urban lungs, and the law mandates that developers replace the greenery lost on the ground with sky terraces and rooftop gardens.</li>
    <li><strong>Water Management (The 4 National Taps):</strong> To achieve water independence, Singapore uses four sources: imported water from Malaysia, local rainwater catchments (reservoirs covering 2/3 of the island), 'NEWater' (highly purified recycled wastewater), and desalinated seawater.</li>
  </ul>
</div>
<!-- """ + " " * 10000 + " -->")

html_7_3_p2 = fix_d("""<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
  <h1 style="color:#ea580c; border-bottom:3px solid #fdba74; padding-bottom:10px; margin-bottom:24px;">7.3 Urban Management - Vocabulary</h1>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">1. Managing Slums & Housing</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Self-help housing:</strong> When people build or improve their own homes with government support.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">tự xây nhà: Chương trình người dân tự xây dựng, cải tạo nhà với sự hỗ trợ của nhà nước.</div>
    
    <strong>Site-and-service schemes:</strong> Providing plots of land with basic infrastructure for people to build on.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">phân lô có hạ tầng: Chính phủ cung cấp lô đất đã có điện, nước để người dân tự xây nhà.</div>
    
    <strong>Slum upgrading:</strong> Improving the physical, social, and economic conditions of an existing slum.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">cải tạo khu ổ chuột: Cải thiện và nâng cấp cơ sở hạ tầng cho khu ổ chuột hiện có.</div>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">2. Urban Planning Concepts</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Green belt:</strong> A designated area of open land around a city where building is restricted.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">ô phố màu xanh / vành đai xanh: Khu vực đất đai xung quanh thành phố được bảo vệ không cho phép xây dựng.</div>
    
    <strong>New town:</strong> A planned urban centre built from scratch to house population overflow.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">thành phố mới: Thành phố được quy hoạch và xây dựng mới hoàn toàn.</div>
    
    <strong>Brownfield site:</strong> Land that has been previously used and abandoned (often industrial).
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">khu đất nâu / khu đất công nghiệp cũ: Khu đất trước đây đã được sử dụng (thường bị bỏ hoang hoặc ô nhiễm).</div>
    
    <strong>Greenfield site:</strong> Undeveloped land in a city or rural area being considered for urban development.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">khu đất xanh: Vùng đất nguyên sơ chưa từng được xây dựng.</div>
  </div>

  <h2 style="color:#1e293b; border-bottom:2px solid #fdba74; padding-bottom:6px; margin-top:32px; margin-bottom:16px;">3. Sustainability Terms</h2>
  <div style="background:#fff7ed; border-left:4px solid #fb923c; padding:14px; border-radius:8px; margin-bottom:16px;">
    <strong>Sustainable development:</strong> Development that meets the needs of the present without compromising future generations.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">phát triển bền vững: Sự phát triển đáp ứng nhu cầu hiện tại mà không làm tổn hại tương lai.</div>
    
    <strong>Compact city:</strong> An urban planning concept promoting high residential density with mixed land uses.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">thành phố nén: Đô thị phát triển với mật độ dân cư cao để tối ưu không gian.</div>
    
    <strong>Public transport:</strong> Buses, trains, and subways that run on scheduled routes and are available to the public.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">giao thông công cộng: Phương tiện di chuyển dành cho mọi người.</div>
    
    <strong>Urban greening:</strong> The process of increasing greenery in urban areas.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đô thị xanh / xanh hóa đô thị: Quá trình tăng cường không gian xanh trong thành phố.</div>
    
    <strong>Smart city:</strong> An urban area that uses data and technology to increase operational efficiency.
    <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">đô thị thông minh: Thành phố sử dụng công nghệ số để quản lý hiệu quả.</div>
  </div>
</div>
<!-- """ + " " * 10000 + " -->")

pages = {
    "ba20fdc4-506e-44c0-9488-d1c2f1976a6b": html_7_1_p1,
    "cba193c7-7842-4d60-97c1-4bf9e7ff6882": html_7_1_p2,
    "df64dca0-ad7d-4d52-abd8-3d87438d85ea": html_7_2_p1,
    "8c792775-dac6-405f-896e-74fe19430d03": html_7_2_p2,
    "be9f9614-3f16-4426-aa24-ef44c43814b2": html_7_3_p1,
    "d3f1013c-f6a1-42bb-a6d6-e4ca9ab0f8df": html_7_3_p2
}

headers = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

context = ssl._create_unverified_context()

for page_id, html_content in pages.items():
    req = urllib.request.Request(
        f"{URL}?id=eq.{page_id}",
        data=json.dumps({"content_html": html_content}).encode('utf-8'),
        headers=headers,
        method="PATCH"
    )
    try:
        response = urllib.request.urlopen(req, context=context)
        print(f"Patched {page_id}: HTTP {response.getcode()}")
    except urllib.error.HTTPError as e:
        print(f"Error patching {page_id}: HTTP {e.code}")
        print(e.read().decode('utf-8'))

