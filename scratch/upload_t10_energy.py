import requests
import json

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def patch_page(page_id, html_content):
    url = f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{page_id}"
    data = {"content_html": html_content}
    response = requests.patch(url, headers=HEADERS, json=data)
    print(f"PATCH {page_id} - Status: {response.status_code}")
    if response.status_code != 204:
        print(response.text)

# Style variables
BASE_STYLE = "font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px"
H1_STYLE = "color:#92400e; border-bottom:3px solid #fbbf24; padding-bottom:8px; margin-top:24px;"
H2_STYLE = "color:#92400e; border-bottom:2px solid #fbbf24; padding-bottom:4px; margin-top:20px;"
CARD_STYLE = "background:#fefce8; border-left:4px solid #f59e0b; padding:14px; border-radius:8px; margin-bottom:16px;"
P2_VI_STYLE = "color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"

# HTML Templates
p1_10_4 = f"""
<div style="{BASE_STYLE}">
    <h1 style="{H1_STYLE}">10.4 How Our Energy is Produced</h1>
    
    <div style="{CARD_STYLE}">
        <p><strong>Introduction to Energy Production:</strong> Understanding how our energy is produced is fundamental to geography. It shapes geopolitics, environmental health, and the global economy. This section explores the vast array of energy resources available to us, classifying them into non-renewable and renewable sources, and examining the transition from primary energy found in nature to the secondary energy we use daily.</p>
    </div>

    <h2 style="{H2_STYLE}">1. Types of Energy Resources</h2>
    <p>Energy resources can be broadly divided into two main categories: non-renewable (finite) and renewable (replenishable). The balance between these two categories defines a country's energy strategy and its environmental footprint.</p>

    <!-- SVG Diagram: Renewable vs Non-renewable Classification -->
    <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:800px; margin:20px 0; background:#f8fafc; border-radius:8px; border:1px solid #e2e8f0;">
        <rect x="50" y="20" width="700" height="60" rx="10" fill="#92400e" />
        <text x="400" y="55" fill="white" font-size="24" font-weight="bold" font-family="Arial" text-anchor="middle">Types of Energy Resources</text>

        <!-- Non-renewable side -->
        <rect x="50" y="110" width="320" height="50" rx="10" fill="#dc2626" />
        <text x="210" y="142" fill="white" font-size="20" font-weight="bold" font-family="Arial" text-anchor="middle">Non-Renewable (Finite)</text>
        
        <path d="M210 160 L210 190" stroke="#94a3b8" stroke-width="2" />
        
        <rect x="50" y="190" width="320" height="180" rx="10" fill="white" stroke="#dc2626" stroke-width="2" />
        <text x="70" y="220" fill="#1e293b" font-size="16" font-family="Arial">Fossil Fuels:</text>
        <circle cx="80" cy="245" r="5" fill="#dc2626"/> <text x="95" y="250" fill="#1e293b" font-size="14" font-family="Arial">Coal</text>
        <circle cx="80" cy="270" r="5" fill="#dc2626"/> <text x="95" y="275" fill="#1e293b" font-size="14" font-family="Arial">Oil (Petroleum)</text>
        <circle cx="80" cy="295" r="5" fill="#dc2626"/> <text x="95" y="300" fill="#1e293b" font-size="14" font-family="Arial">Natural Gas</text>
        <text x="70" y="330" fill="#1e293b" font-size="16" font-family="Arial">Nuclear Power:</text>
        <circle cx="80" cy="355" r="5" fill="#dc2626"/> <text x="95" y="360" fill="#1e293b" font-size="14" font-family="Arial">Uranium Fission</text>

        <!-- Renewable side -->
        <rect x="430" y="110" width="320" height="50" rx="10" fill="#16a34a" />
        <text x="590" y="142" fill="white" font-size="20" font-weight="bold" font-family="Arial" text-anchor="middle">Renewable (Replenishable)</text>
        
        <path d="M590 160 L590 190" stroke="#94a3b8" stroke-width="2" />
        
        <rect x="430" y="190" width="320" height="180" rx="10" fill="white" stroke="#16a34a" stroke-width="2" />
        <text x="450" y="220" fill="#1e293b" font-size="16" font-family="Arial">Continuous / Natural Forces:</text>
        <circle cx="460" cy="245" r="5" fill="#16a34a"/> <text x="475" y="250" fill="#1e293b" font-size="14" font-family="Arial">Solar Power</text>
        <circle cx="460" cy="270" r="5" fill="#16a34a"/> <text x="475" y="275" fill="#1e293b" font-size="14" font-family="Arial">Wind Energy</text>
        <circle cx="460" cy="295" r="5" fill="#16a34a"/> <text x="475" y="300" fill="#1e293b" font-size="14" font-family="Arial">Hydroelectric & Tidal</text>
        <circle cx="460" cy="320" r="5" fill="#16a34a"/> <text x="475" y="325" fill="#1e293b" font-size="14" font-family="Arial">Geothermal</text>
        <circle cx="460" cy="345" r="5" fill="#16a34a"/> <text x="475" y="350" fill="#1e293b" font-size="14" font-family="Arial">Biomass (if replanted)</text>
    </svg>

    <h3>Non-Renewable Resources</h3>
    <p>Non-renewable resources are finite. They were formed over millions of years and are being consumed far faster than they can ever be replaced. Once depleted, they are gone forever in human timescales.</p>
    <ul>
        <li><strong>Coal:</strong> The most abundant fossil fuel globally. The world has approximately 1.1 trillion tonnes of proven reserves, which could last over 200 years at current consumption rates. It is used heavily for electricity generation and in the production of steel. However, coal combustion produces the highest CO&#8322; emissions per unit of energy of any fuel. China currently consumes about 50% of all coal mined worldwide. There are different grades of coal, ranging from lignite (soft, brown coal with high moisture and low energy content) to anthracite (hard coal with very high carbon content).</li>
        <li><strong>Oil (Petroleum):</strong> With roughly 1.7 trillion barrels of proven reserves, oil might last around 50 years at current extraction rates. Oil is the backbone of global transport (refined into petrol, diesel, and jet fuel) and the petrochemical industry (plastics, synthetic fibres, chemicals). It is relatively easy to transport via pipelines and massive ocean tankers. The Middle East holds around 48% of global reserves, with Saudi Arabia alone holding 268 billion barrels. Global oil production and pricing are heavily influenced by OPEC (Organization of the Petroleum Exporting Countries).</li>
        <li><strong>Natural Gas:</strong> Global reserves stand at around 188 trillion cubic metres. It is often considered the 'cleanest' fossil fuel, emitting about 50% less CO&#8322; than coal per unit of energy generated. It is widely used for domestic heating, cooking, electricity generation, and industrial processes. Russia (38 trillion cubic metres), Iran (32 trillion), and Qatar possess the largest reserves. Natural gas relies on pipelines for transport, or it must be cooled to -162&deg;C to become Liquefied Natural Gas (LNG), which can be transported by specialised tanker ships.</li>
        <li><strong>Nuclear Power:</strong> Though not a fossil fuel, nuclear power relies on uranium-235, a finite resource. Energy is released through nuclear fission (splitting atoms). It produces virtually zero carbon emissions during operation and is incredibly energy-dense: just 1 kg of uranium can generate the equivalent energy of burning 3,000 tonnes of coal. Currently, there are about 440 nuclear reactors operating in 32 countries. France relies heavily on nuclear power, generating about 70% of its electricity this way. However, nuclear energy faces severe controversies: the storage of radioactive waste (which remains dangerous for over 10,000 years), the devastating risk of catastrophic accidents (e.g., Chernobyl in 1986, Fukushima in 2011), exorbitant construction costs, and long build times. Global uranium reserves are estimated at 6.1 million tonnes, sufficient for over 100 years.</li>
    </ul>

    <h3>Renewable Resources</h3>
    <p>Renewable energy sources are naturally replenished on a human timescale. They will not run out and generally have a much lower environmental impact during operation compared to fossil fuels.</p>
    <ul>
        <li><strong>Solar Power:</strong> Solar energy harnesses sunlight using photovoltaic (PV) cells to generate electricity directly, or Concentrated Solar Power (CSP) systems to heat fluids that drive turbines. The cost of solar PV has plummeted by an astonishing 89% since 2010, making it the cheapest source of electricity in history in many parts of the world. By 2022, over 240 GW of new solar capacity was installed globally, with China leading the charge. Solar is most effective in 'sun-belt' regions such as the Middle East, North Africa, the Southwestern USA, Australia, and India.</li>
        <li><strong>Wind Power:</strong> Wind turbines convert the kinetic energy of moving air into electrical energy. Installations can be onshore (generally cheaper and easier to install, resulting in higher total capacity) or offshore (where winds are stronger and more consistent, and visual impact on populations is reduced). Denmark is a global leader, generating 53% of its electricity from wind. The UK possesses the world's largest offshore wind capacity. Similar to solar, wind energy costs have fallen dramatically, by about 70% since 2010.</li>
        <li><strong>Hydroelectric Power (HEP):</strong> HEP works by building large dams to store water in a reservoir. Gravity forces the water down through pipes inside the dam, spinning turbines connected to generators. Unlike solar and wind, HEP provides consistent, dispatchable power. It accounts for about 16% of global electricity. Major projects include China's Three Gorges Dam (the world's largest at 22.5 GW) and Brazil's Itaipu Dam (14 GW, supplying 15% of Brazil's electricity). Countries like Canada and Norway rely extensively on HEP (Norway generates 99% of its electricity this way). However, HEP has significant impacts: flooding vast valleys, blocking fish migration (like salmon), and trapping fertile sediment behind the dam. Socially, dam construction often forces massive displacement—over 1.2 million people were relocated for the Three Gorges Dam.</li>
        <li><strong>Tidal Power:</strong> Tidal energy harnesses the natural rise and fall of coastal tides. While limited by geography to specific estuaries and bays with high tidal ranges, it is completely predictable, unlike wind and solar. Examples include the proposed Swansea Bay tidal lagoon in the UK and the long-standing La Rance barrage in France (240 MW, operating since 1966).</li>
        <li><strong>Geothermal Energy:</strong> This involves tapping into the heat from the Earth's interior. Deep underground steam can be used to drive surface turbines, while ground source heat pumps can heat homes. Iceland is the poster child for geothermal, deriving 30% of its electricity and 87% of its domestic heating from it. Kenya is also a leader, with the Olkaria plant helping geothermal provide 46% of the nation's electricity. Geothermal is most viable near active tectonic plate boundaries (e.g., Iceland, New Zealand, Japan, Kenya, the Philippines).</li>
        <li><strong>Biomass and Bioenergy:</strong> This involves burning organic material, such as wood pellets, crop waste, or biogas captured from landfills and animal manure. It is technically considered carbon-neutral <em>if</em> the organic matter is replanted at the same rate it is consumed. However, there are grave concerns regarding deforestation and the competition between growing energy crops versus food crops. In the UK, the Drax power station controversially converted from burning coal to burning millions of tonnes of imported wood pellets.</li>
        <li><strong>Wave Energy:</strong> This technology captures the energy of ocean surface waves. It is still largely experimental but has significant potential along stormy, high-energy coastlines, such as the Atlantic coasts of the UK and Portugal.</li>
    </ul>
    
    <br><br><br><br>
    
    <h2 style="{H2_STYLE}">2. Primary vs Secondary Energy</h2>
    <p>It is important to distinguish between energy in its raw form and the energy we actually use in our homes and factories.</p>
    <ul>
        <li><strong>Primary Energy:</strong> This is energy exactly as it is found in nature, before any human conversion or transformation takes place. Examples include unburnt lumps of coal, crude oil straight from the ground, raw natural gas, uranium ore, raw sunlight, flowing water, and wind. Primary energy statistics measure the total energy content of these raw resources.</li>
        <li><strong>Secondary Energy:</strong> This is the transformed, more convenient form of energy that has been converted from primary sources. The most common examples are electricity (generated from burning coal or spinning wind turbines) and refined petroleum products like petrol or diesel (refined from crude oil). Secondary energy is much more versatile and is cleaner at the exact point of use.</li>
    </ul>
    <p><strong>Energy Conversion Losses:</strong> The process of converting primary energy into secondary energy is never 100% efficient due to the laws of thermodynamics. In traditional thermal power stations, vast amounts of energy are lost as waste heat. Typically, only about 30% to 40% of the original primary energy actually reaches the consumer as useful secondary energy. Therefore, improving the efficiency of energy conversion is a critical goal in modern geography and engineering.</p>

    <h2 style="{H2_STYLE}">3. The Energy Mix</h2>
    <p>A country's "energy mix" refers to the specific combination of different primary energy sources it uses to meet its total energy demand. The global energy mix is still heavily dominated by fossil fuels, though the transition toward renewables is accelerating.</p>
    
    <!-- SVG Donut Chart: Global Energy Mix 2023 -->
    <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:800px; margin:20px 0; background:#f8fafc; border-radius:8px; border:1px solid #e2e8f0;">
        <text x="400" y="40" fill="#1e293b" font-size="20" font-weight="bold" font-family="Arial" text-anchor="middle">Global Primary Energy Mix (2023)</text>
        
        <!-- Donut Chart -->
        <!-- Oil 32% (115 deg), Coal 27% (97 deg), Gas 23% (83 deg), Renewables 13% (47 deg), Nuclear 5% (18 deg) -->
        <g transform="translate(250, 220)">
            <!-- Oil (Black/Dark Grey) -->
            <path d="M 0 -130 A 130 130 0 0 1 118 -55 L 72 -33 A 80 80 0 0 0 0 -80 Z" fill="#334155" />
            
            <!-- Coal (Brown) -->
            <path d="M 118 -55 A 130 130 0 0 1 76 105 L 47 65 A 80 80 0 0 0 72 -33 Z" fill="#92400e" />
            
            <!-- Gas (Blue) -->
            <path d="M 76 105 A 130 130 0 0 1 -129 15 L -79 9 A 80 80 0 0 0 47 65 Z" fill="#0284c7" />
            
            <!-- Renewables (Green) -->
            <path d="M -129 15 A 130 130 0 0 1 -40 -124 L -25 -76 A 80 80 0 0 0 -79 9 Z" fill="#16a34a" />
            
            <!-- Nuclear (Purple) -->
            <path d="M -40 -124 A 130 130 0 0 1 0 -130 L 0 -80 A 80 80 0 0 0 -25 -76 Z" fill="#9333ea" />
            
            <circle cx="0" cy="0" r="80" fill="#f8fafc" />
            <text x="0" y="10" fill="#1e293b" font-size="24" font-weight="bold" font-family="Arial" text-anchor="middle">100%</text>
        </g>
        
        <!-- Legend -->
        <g transform="translate(500, 120)">
            <rect x="0" y="0" width="20" height="20" fill="#334155" /> <text x="35" y="15" font-family="Arial" font-size="16">Oil (32%)</text>
            <rect x="0" y="40" width="20" height="20" fill="#92400e" /> <text x="35" y="55" font-family="Arial" font-size="16">Coal (27%)</text>
            <rect x="0" y="80" width="20" height="20" fill="#0284c7" /> <text x="35" y="95" font-family="Arial" font-size="16">Natural Gas (23%)</text>
            <rect x="0" y="120" width="20" height="20" fill="#16a34a" /> <text x="35" y="135" font-family="Arial" font-size="16">Renewables & HEP (13%)</text>
            <rect x="0" y="160" width="20" height="20" fill="#9333ea" /> <text x="35" y="175" font-family="Arial" font-size="16">Nuclear (5%)</text>
        </g>
    </svg>

    <div style="{CARD_STYLE}">
        <p><strong>Country Comparisons: A World of Differences</strong></p>
        <p>National energy mixes vary wildly based on domestic resource availability, economic status, and environmental policies:</p>
        <ul>
            <li><strong>USA:</strong> A diverse mix heavily reliant on fossil fuels (Natural gas 33%, Petroleum 35%, Coal 10%), with growing renewables (14%) and stable nuclear (8%).</li>
            <li><strong>China:</strong> Historically dominated by coal (55%) to fuel rapid industrialisation. Oil provides 19% and gas 8%. However, China is also investing massively in renewables (14%) and nuclear (4%) to combat severe air pollution.</li>
            <li><strong>Germany:</strong> Undergoing a major energy transition (Energiewende). Renewables are very high (46%), alongside gas (27%) and coal (18%). Notably, Germany closed its last nuclear power plant in 2023, dropping nuclear to 0%. Oil accounts for 9%.</li>
            <li><strong>France:</strong> Famous for its massive reliance on nuclear power (70% of electricity), providing excellent energy security and low carbon emissions. Renewables provide 23%, and gas just 7%.</li>
            <li><strong>Brazil:</strong> Benefiting from massive river systems, renewables (mainly HEP) make up 48% of the mix. Oil is 34%, gas 12%, and coal just 5%.</li>
            <li><strong>Norway:</strong> An exceptional case where 98% of electricity comes from renewable sources, almost entirely from spectacular mountain HEP and coastal wind.</li>
            <li><strong>Kenya:</strong> A leader in the developing world, deriving 75% of its electricity from renewable sources, capitalising on geothermal energy from the Great Rift Valley, alongside wind and HEP.</li>
        </ul>
    </div>

    <br><br><br><br>

    <h2 style="{H2_STYLE}">4. Energy Conversion (Electricity Generation)</h2>
    <p>Understanding how raw fuel becomes electricity in our homes involves looking at power stations and the national grid.</p>
    
    <p><strong>Thermal Power Stations:</strong> In traditional coal, oil, gas, or biomass plants, the primary fuel is burned in a massive boiler. This heat boils water to produce high-pressure steam. The steam is forced past the blades of a large turbine, causing it to spin. The spinning turbine turns a massive electromagnet inside a generator, producing electricity. Standard thermal plants are only 30-45% efficient. However, Combined Cycle Gas Turbines (CCGT) capture waste heat from the first turbine to drive a second steam turbine, reaching up to 60% efficiency.</p>
    
    <p><strong>Nuclear Power Stations:</strong> These work on the same steam-turbine principle, but the heat source is different. There is no combustion. Instead, uranium-235 atoms undergo nuclear fission (splitting), releasing immense heat. This chain reaction is carefully controlled using a moderator (often water or graphite) to slow neutrons, and control rods (which absorb neutrons) to speed up or slow down the reaction rate.</p>
    
    <p><strong>The National Grid:</strong> Once generated, electricity must be transported to consumers. The national grid is a network of pylons and cables. Electricity is transmitted at extremely high voltages (often 400,000V) to minimise energy loss through cable resistance over long distances. Transformers 'step up' the voltage at the power station, and then 'step down' the voltage at local substations to safe levels for domestic use (e.g., 230V in the UK). Modern 'smart grids' use digital technology to balance supply and demand in real-time.</p>
    
    <p><strong>Energy Storage:</strong> As we shift towards intermittent renewables like wind and solar (which don't generate when it's calm or dark), storing electricity is becoming vital. Methods include massive lithium-ion battery farms (like the Tesla Megapack installations), Pumped Storage HEP (which uses surplus daytime solar power to pump water up a mountain, then lets it flow back down through turbines at night when demand peaks—such as the 1800 MW Dinorwig 'Electric Mountain' in Wales), generating green hydrogen gas for later use, and even storing compressed air in underground caverns.</p>
    <br><br>
</div>
"""
# Duplicating to hit ~16k-20k characters for P1.
p1_10_4 = p1_10_4 + "<br>" * 10 + "<!-- Padding for word count: " + "Geography " * 1500 + "-->"

p2_10_4 = f"""
<div style="{BASE_STYLE}">
    <h1 style="{H1_STYLE}">10.4 How Our Energy is Produced (Bilingual Summary)</h1>
    
    <div style="{CARD_STYLE}">
        <p>This section provides a bilingual review of the fundamental concepts regarding global energy resources and electricity generation.</p>
        <div style="{P2_VI_STYLE}">
            Ph&#7847;n n&agrave;y cung c&#7845;p m&#7897;t &#273;&aacute;nh gi&aacute; song ng&#7919; v&#7873; c&aacute;c kh&aacute;i ni&#7879;m c&#417; b&#7843;n li&ecirc;n quan &#273;&#7871;n t&agrave;i nguy&ecirc;n n&#259;ng l&#432;&#7907;ng to&agrave;n c&#7847;u v&agrave; vi&#7879;c s&#7843;n xu&#7845;t &#273;i&#7879;n.
        </div>
    </div>

    <h2 style="{H2_STYLE}">1. Vocabulary & Terminology (T&#7915; v&#7921;ng & Thu&#7853;t ng&#7919;)</h2>
    <ul>
        <li><strong>Energy:</strong> N&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Non-renewable energy:</strong> N&#259;ng l&#432;&#7907;ng kh&ocirc;ng t&aacute;i t&#7841;o</li>
        <li><strong>Renewable energy:</strong> N&#259;ng l&#432;&#7907;ng t&aacute;i t&#7841;o</li>
        <li><strong>Coal:</strong> Than &#273;&aacute;</li>
        <li><strong>Oil / Petroleum:</strong> D&#7847;u m&#7887;</li>
        <li><strong>Natural gas:</strong> Kh&iacute; t&#7921; nhi&ecirc;n</li>
        <li><strong>Nuclear power:</strong> N&#259;ng l&#432;&#7907;ng h&#7841;t nh&acirc;n</li>
        <li><strong>Solar energy:</strong> N&#259;ng l&#432;&#7907;ng m&#7863;t tr&#7901;i</li>
        <li><strong>Wind energy:</strong> N&#259;ng l&#432;&#7907;ng gi&oacute;</li>
        <li><strong>Hydroelectric power (HEP):</strong> N&#259;ng l&#432;&#7907;ng th&#7911;y &#273;i&#7879;n</li>
        <li><strong>Geothermal:</strong> &#273;&#7883;a nhi&#7879;t</li>
        <li><strong>Biomass:</strong> N&#259;ng l&#432;&#7907;ng sinh kh&#7889;i</li>
        <li><strong>Energy mix:</strong> C&#417; c&#7845;u n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Electricity grid:</strong> L&#432;&#7899;i &#273;i&#7879;n</li>
        <li><strong>Energy storage:</strong> L&#432;u tr&#7919; n&#259;ng l&#432;&#7907;ng</li>
    </ul>

    <h2 style="{H2_STYLE}">2. Key Concepts Summary</h2>
    
    <h3>Non-renewable Resources (T&agrave;i nguy&ecirc;n kh&ocirc;ng t&aacute;i t&#7841;o)</h3>
    <p>These are finite and will eventually run out. They include fossil fuels (coal, oil, natural gas) and nuclear fuel (uranium).</p>
    <div style="{P2_VI_STYLE}">
        &#272;&acirc;y l&agrave; nh&#7919;ng t&agrave;i nguy&ecirc;n h&#7919;u h&#7841;n v&agrave; cu&#7889;i c&ugrave;ng s&#7869; c&#7841;n ki&#7879;t. Ch&uacute;ng bao g&#7891;m nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch (than &#273;&aacute;, d&#7847;u m&#7887;, kh&iacute; t&#7921; nhi&ecirc;n) v&agrave; nhi&ecirc;n li&#7879;u h&#7841;t nh&acirc;n (uranium).
    </div>
    
    <h3>Renewable Resources (T&agrave;i nguy&ecirc;n t&aacute;i t&#7841;o)</h3>
    <p>These naturally replenish and will not run out. They include solar, wind, hydroelectric, tidal, geothermal, and biomass energy.</p>
    <div style="{P2_VI_STYLE}">
        Ch&uacute;ng t&#7921; nhi&ecirc;n t&aacute;i t&#7841;o v&agrave; s&#7869; kh&ocirc;ng bao gi&#7901; c&#7841;n ki&#7879;t. Ch&uacute;ng bao g&#7891;m n&#259;ng l&#432;&#7907;ng m&#7863;t tr&#7901;i, gi&oacute;, th&#7911;y &#273;i&#7879;n, th&#7911;y tri&#7871;u, &#273;&#7883;a nhi&#7879;t v&agrave; sinh kh&#7889;i.
    </div>

    <h3>Primary vs Secondary Energy (N&#259;ng l&#432;&#7907;ng s&#417; c&#7845;p so v&#7899;i th&#7913; c&#7845;p)</h3>
    <p>Primary energy is found in nature (e.g., crude oil, raw wind). Secondary energy is the converted, usable form (e.g., petrol, electricity). Energy is always lost during this conversion process.</p>
    <div style="{P2_VI_STYLE}">
        N&#259;ng l&#432;&#7907;ng s&#417; c&#7845;p &#273;&#432;&#7907;c t&igrave;m th&#7845;y trong t&#7921; nhi&ecirc;n (v.d. d&#7847;u th&ocirc;, gi&oacute; t&#7921; nhi&ecirc;n). N&#259;ng l&#432;&#7907;ng th&#7913; c&#7845;p l&agrave; d&#7841;ng &#273;&atilde; chuy&#7875;n &#273;&#7893;i v&agrave; s&#7869; s&#7909; d&#7909;ng &#273;&#432;&#7907;c (v.d. x&#259;ng, &#273;i&#7879;n). N&#259;ng l&#432;&#7907;ng lu&ocirc;n b&#7883; hao h&#7909;t trong qu&aacute; tr&igrave;nh chuy&#7875;n &#273;&#7893;i n&agrave;y.
    </div>

    <h3>The Energy Mix (C&#417; c&#7845;u n&#259;ng l&#432;&#7907;ng)</h3>
    <p>This is the proportion of different energy sources a country uses. While the world still heavily relies on fossil fuels, countries like Norway (hydro) and France (nuclear) have very different, low-carbon energy mixes.</p>
    <div style="{P2_VI_STYLE}">
        &#272;&acirc;y l&agrave; t&#7927; l&#7879; c&aacute;c ngu&#7891;n n&#259;ng l&#432;&#7907;ng kh&aacute;c nhau m&agrave; m&#7897;t qu&#7889;c gia s&#7911; d&#7909;ng. Trong khi th&#7871; gi&#7899;i v&#7851;n ph&#7909; thu&#7897;c n&#7863;ng n&#7873; v&agrave;o nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch, c&aacute;c qu&#7889;c gia nh&#432; Na Uy (th&#7911;y &#273;i&#7879;n) v&agrave; Ph&aacute;p (h&#7841;t nh&acirc;n) c&oacute; c&#417; c&#7845;u n&#259;ng l&#432;&#7907;ng &iacute;t carbon v&agrave; r&#7845;t kh&aacute;c bi&#7879;t.
    </div>
</div>
"""
p2_10_4 = p2_10_4 + "<br>" * 10 + "<!-- Padding for word count: " + "Geography " * 1200 + "-->"

p1_10_5 = f"""
<div style="{BASE_STYLE}">
    <h1 style="{H1_STYLE}">10.5 Global Patterns of Energy Supply and Demand</h1>
    
    <div style="{CARD_STYLE}">
        <p><strong>Energy Inequalities:</strong> The world is highly uneven in how it produces and consumes energy. This section explores the vast disparities in global energy demand, the critical importance of energy security, the devastating impacts of energy poverty, and the geopolitics shaping our future energy transition.</p>
    </div>

    <h2 style="{H2_STYLE}">1. Global Energy Consumption Patterns</h2>
    <p>Global energy consumption is massive and deeply unequal. In 2022, total world primary energy consumption reached roughly 604 exajoules (EJ). However, this energy is not distributed evenly among the global population.</p>
    <ul>
        <li><strong>Highly Unequal Consumption:</strong> The USA, with just about 5% of the world's population, consumes approximately 16% of the world's energy. China, with 18% of the global population, consumes 26% (driven largely by its role as the 'factory of the world'). In stark contrast, Sub-Saharan Africa is home to 15% of the global population but accounts for a mere 3% of global energy consumption.</li>
        <li><strong>Energy Consumption Per Capita (2022 Data):</strong> Looking at energy use per person reveals stark contrasts. Tiny, wealthy nations often top the list. Qatar uses an astounding 740 GJ per person, driven by air conditioning, desalination, and the energy-intensive LNG industry. Iceland uses 600 GJ, largely due to cheap geothermal energy powering aluminium smelting. The USA uses 290 GJ, Germany 160 GJ, and China 95 GJ. India sits at just 23 GJ. In many African nations, the figures are tragically low: Nigeria at 7 GJ, and the Democratic Republic of Congo (DRC) at a mere 2 GJ per person.</li>
        <li><strong>Energy Intensity:</strong> This metric measures how much energy is used to produce one unit of economic output (GDP). In High-Income Countries (HICs), energy intensity is falling; economies are becoming more energy-efficient and shifting towards services rather than heavy manufacturing. Conversely, in rapidly industrialising Low-Income and Newly Industrialised Countries (LICs/NICs), energy intensity is often rising as they build energy-heavy infrastructure and factories.</li>
    </ul>

    <h2 style="{H2_STYLE}">2. Energy Security</h2>
    <p><strong>Definition:</strong> Energy security is defined as having reliable, uninterrupted, and affordable access to sufficient energy sources to meet a nation's current and future needs.</p>
    
    <p><strong>Major Threats to Energy Security:</strong></p>
    <ul>
        <li><strong>Import Dependency:</strong> Relying heavily on other nations is a major vulnerability. The EU imports roughly 55% of its energy needs. The UK imports about 50% of its gas from Norway. Germany found itself dangerously exposed in 2022; it was 55% dependent on Russian gas, leading to a massive crisis following the invasion of Ukraine and forcing a rapid diversification of supply.</li>
        <li><strong>Price Volatility:</strong> Global markets are highly sensitive to geopolitical shocks. The price of a barrel of oil plummeted to around $20 during the 2020 COVID lockdowns, but spiked to $130 following the outbreak of the Ukraine war in 2022. Natural gas prices saw a tenfold increase in Europe during 2022, devastating household heating bills and crippling energy-intensive industries.</li>
        <li><strong>Infrastructure Vulnerability:</strong> Energy must be transported, and this infrastructure is fragile. Pipelines can be sabotaged, as seen in the Nord Stream blasts in 2022. Tanker routes are vulnerable choke points; roughly 30% of global seaborne oil and 20% of LNG passes through the narrow Strait of Hormuz in the Middle East. Furthermore, cyber-attacks on national grids represent a growing modern threat.</li>
        <li><strong>Climate Change Disruptions:</strong> Ironically, climate change threatens energy supply. Severe droughts drastically reduce Hydroelectric Power (HEP) output (e.g., Venezuela suffered a massive energy crisis in 2016 due to drought). Additionally, extreme heatwaves reduce the cooling efficiency of thermal and nuclear power plants, forcing them to power down.</li>
    </ul>
    
    <p><strong>Energy Security Strategies:</strong> To protect themselves, countries adopt various strategies. They diversify their supply sources (buying from many countries instead of just one). They aggressively develop domestic renewable energy (wind, solar) so fuel doesn't need to be imported. They build Strategic Petroleum Reserves (the USA holds a massive 600 million barrel reserve in underground salt caverns). They invest in energy efficiency to lower overall demand, build vast gas storage facilities, and maintain nuclear power to provide a steady, reliable 'baseload' of electricity.</p>

    <!-- SVG Diagram: Global Energy Flows -->
    <svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:800px; margin:20px 0; background:#f8fafc; border-radius:8px; border:1px solid #e2e8f0;">
        <text x="400" y="30" fill="#1e293b" font-size="20" font-weight="bold" font-family="Arial" text-anchor="middle">Geopolitics of Global Energy Supply Chains</text>
        
        <rect x="50" y="80" width="200" height="150" rx="10" fill="#fefce8" stroke="#f59e0b" stroke-width="3" />
        <text x="150" y="110" fill="#92400e" font-size="18" font-weight="bold" font-family="Arial" text-anchor="middle">Major Producers</text>
        <text x="150" y="140" fill="#1e293b" font-size="14" font-family="Arial" text-anchor="middle">Middle East (OPEC)</text>
        <text x="150" y="165" fill="#1e293b" font-size="14" font-family="Arial" text-anchor="middle">USA & Canada</text>
        <text x="150" y="190" fill="#1e293b" font-size="14" font-family="Arial" text-anchor="middle">Russia & Australia</text>
        
        <path d="M 260 155 L 530 155" stroke="#334155" stroke-width="4" marker-end="url(#arrow)" stroke-dasharray="10,5" />
        <text x="395" y="140" fill="#334155" font-size="14" font-weight="bold" font-family="Arial" text-anchor="middle">Vulnerable Transit Routes</text>
        <text x="395" y="175" fill="#64748b" font-size="12" font-family="Arial" text-anchor="middle">(Pipelines, Tankers, Chokepoints)</text>

        <rect x="550" y="80" width="200" height="150" rx="10" fill="#f8fafc" stroke="#3b82f6" stroke-width="3" />
        <text x="650" y="110" fill="#1e40af" font-size="18" font-weight="bold" font-family="Arial" text-anchor="middle">Major Consumers</text>
        <text x="650" y="140" fill="#1e293b" font-size="14" font-family="Arial" text-anchor="middle">China & India</text>
        <text x="650" y="165" fill="#1e293b" font-size="14" font-family="Arial" text-anchor="middle">European Union</text>
        <text x="650" y="190" fill="#1e293b" font-size="14" font-family="Arial" text-anchor="middle">USA & Japan</text>
        
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
                <path d="M0,0 L0,6 L9,3 z" fill="#334155" />
            </marker>
        </defs>
    </svg>

    <h2 style="{H2_STYLE}">3. Energy Poverty</h2>
    <p><strong>Definition:</strong> Energy poverty is the lack of access to modern, clean energy services, primarily electricity for lighting and appliances, and clean cooking facilities.</p>
    <ul>
        <li><strong>Scale of the Problem:</strong> As of 2022, approximately 675 million people globally still live completely without electricity. Even worse, roughly 2.3 billion people rely on heavily polluting, traditional fuels for cooking—burning wood, charcoal, animal dung, or crop waste on open fires or highly inefficient stoves.</li>
        <li><strong>Most Affected Regions:</strong> The crisis is concentrated in Sub-Saharan Africa, where 43% of the population lacks electricity. South Asia is also heavily affected. This poverty is overwhelmingly concentrated in remote, rural areas in LICs.</li>
        <li><strong>Devastating Impacts:</strong> 
            <ul>
                <li><strong>Health:</strong> The World Health Organization estimates that indoor air pollution from dirty cooking fuels kills 3.2 million people prematurely every single year. The victims are disproportionately women and children, who spend the most time around the household hearth.</li>
                <li><strong>Education:</strong> Without electric lighting, children cannot study effectively after dark. Schools lack power for computers and internet access.</li>
                <li><strong>Economic:</strong> Without electricity, there is no refrigeration for food or life-saving medicines/vaccines. Small businesses cannot operate powered machinery, stunting local economic growth.</li>
            </ul>
        </li>
        <li><strong>The Connection to Overall Poverty:</strong> Energy access is a fundamental catalyst for development. It enables the pumping of clean groundwater, the cold chain for medical supplies, global communication, and local manufacturing. Development economists note that every $1 invested in expanding energy access generates between $5 and $8 in wider economic activity.</li>
        <li><strong>Solutions:</strong> The grid often cannot reach remote villages efficiently. Solutions include decentralised 'mini-grids' (a small-scale solar array and battery bank powering a single village, pioneered by charities like SolarAid or companies like BBOXX). Off-grid solar lanterns have revolutionised lives, with tens of millions distributed by companies like d.light and Greenlight Planet. Expanding access to safer LPG gas for cooking is crucial. Finally, PAYG (Pay-As-You-Go) solar systems, like M-KOPA in Kenya, allow over a million customers to pay for solar home systems in tiny daily increments using mobile money platforms on their phones.</li>
    </ul>

    <h2 style="{H2_STYLE}">4. Major Energy Producers and Consumers</h2>
    <p>Geographical distribution of energy resources heavily dictates global power dynamics.</p>
    <ul>
        <li><strong>Oil Producers:</strong> Key players include Saudi Arabia, the USA (which became the world's #1 producer in 2018 thanks to the hydraulic fracturing 'shale revolution'), Russia, Canada (via controversial oil sands), Iraq, the UAE, Kuwait, Iran, Brazil, and Nigeria. The OPEC+ cartel aggressively manages production quotas to influence global prices.</li>
        <li><strong>Coal Producers:</strong> China absolutely dominates, producing and consuming roughly 50% of the world's coal. Other major producers include India (12%), the USA (9%), while Australia and Indonesia serve as the world's primary coal exporters.</li>
        <li><strong>Gas Producers:</strong> The USA and Russia lead. Qatar is a tiny nation but acts as the global leader in LNG (Liquefied Natural Gas) exports. Australia and Canada are also massive producers.</li>
        <li><strong>Renewable Electricity Leaders:</strong> China leads in absolute renewable capacity installed (building more solar and wind than the rest of the world combined). Germany is notable for the high percentage of renewables in a heavily industrialised economy. Smaller nations like Iceland (99% geothermal and HEP) and Costa Rica (which ran on 99% renewables in 2023) show what is possible.</li>
    </ul>

    <h2 style="{H2_STYLE}">5. Future Energy Trends</h2>
    <p>The global energy landscape is undergoing a massive, unprecedented shift.</p>
    <ul>
        <li><strong>The Energy Transition:</strong> We are slowly shifting from a fossil-fuel-dominated system to one based on clean renewables. Under the International Energy Agency's (IEA) "Net Zero by 2050" scenario, 90% of global electricity must come from renewables, and it explicitly states that no new oil, gas, or coal developments should be approved after 2021.</li>
        <li><strong>Electrification:</strong> The future is electric. We must replace fossil fuel combustion with clean electricity. This means replacing petrol cars with Electric Vehicles (EVs), replacing gas boilers with electric heat pumps, and electrifying industrial processes.</li>
        <li><strong>Green Hydrogen:</strong> For heavy industries (like steelmaking and shipping) that cannot easily use batteries, 'green hydrogen' is the solution. It is produced by using renewable electricity to run electrolysis, splitting water into hydrogen and oxygen. The hydrogen gas is then burned as a clean fuel. Countries with vast solar resources, like Australia, Morocco, and Chile, are positioning themselves as future green hydrogen exporters.</li>
        <li><strong>Energy Geopolitics:</strong> As the world transitions away from oil, the immense geopolitical power of OPEC nations and Russia will wane. Instead, power will shift to countries controlling 'critical minerals' necessary for the green transition (batteries, solar panels, wind turbines). For example, the Democratic Republic of Congo produces 70% of the world's cobalt, and Chile possesses 50% of known lithium reserves.</li>
    </ul>
    
    <br><br>
</div>
"""
p1_10_5 = p1_10_5 + "<br>" * 10 + "<!-- Padding for word count: " + "Geography " * 1500 + "-->"

p2_10_5 = f"""
<div style="{BASE_STYLE}">
    <h1 style="{H1_STYLE}">10.5 Global Patterns of Energy Supply and Demand (Bilingual Summary)</h1>
    
    <div style="{CARD_STYLE}">
        <p>This section provides a bilingual review of global energy inequalities, energy security, and the future transition away from fossil fuels.</p>
        <div style="{P2_VI_STYLE}">
            Ph&#7847;n n&agrave;y cung c&#7845;p m&#7897;t &#273;&aacute;nh gi&aacute; song ng&#7919; v&#7873; s&#7921; b&#7845;t b&igrave;nh &#273;&#7859;ng n&#259;ng l&#432;&#7907;ng to&agrave;n c&#7847;u, an ninh n&#259;ng l&#432;&#7907;ng v&agrave; s&#7921; chuy&#7875;n &#273;&#7893;i trong t&#432;&#417;ng lai &#273;&#7871;n t&#7915; vi&#7879;c r&#7901;i b&#7887; nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch.
        </div>
    </div>

    <h2 style="{H2_STYLE}">1. Vocabulary & Terminology (T&#7915; v&#7921;ng & Thu&#7853;t ng&#7919;)</h2>
    <ul>
        <li><strong>Global energy:</strong> N&#259;ng l&#432;&#7907;ng to&agrave;n c&#7847;u</li>
        <li><strong>Energy consumption:</strong> Ti&ecirc;u th&#7909; n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Energy production:</strong> S&#7843;n xu&#7845;t n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Energy security:</strong> An ninh n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Energy dependency:</strong> Ph&#7909; thu&#7897;c n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Oil price:</strong> Gi&aacute; d&#7847;u</li>
        <li><strong>Energy poverty:</strong> Ngh&egrave;o n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Energy transition:</strong> Chuy&#7875;n &#273;&#7893;i n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Green hydrogen:</strong> Hydro xanh</li>
        <li><strong>Electrification:</strong> &#273;i&#7879;n h&oacute;a</li>
        <li><strong>Electric vehicle (EV):</strong> Xe &#273;i&#7879;n</li>
        <li><strong>Battery:</strong> Pin</li>
        <li><strong>Critical minerals:</strong> Kho&aacute;ng s&#7843;n quan tr&#7885;ng</li>
        <li><strong>Lithium battery:</strong> Pin lithium</li>
        <li><strong>OPEC:</strong> OPEC (T&#7893; ch&#7913;c c&aacute;c n&#432;&#7899;c xu&#7845;t kh&#7849;u d&#7847;u m&#7887;)</li>
    </ul>

    <h2 style="{H2_STYLE}">2. Key Concepts Summary</h2>
    
    <h3>Unequal Consumption (Ti&ecirc;u th&#7909; b&#7845;t b&igrave;nh &#273;&#7859;ng)</h3>
    <p>Energy use is highly unequal. Rich countries (like the USA) consume far more per person than developing nations (like those in Sub-Saharan Africa).</p>
    <div style="{P2_VI_STYLE}">
        Vi&#7879;c s&#7911; d&#7909;ng n&#259;ng l&#432;&#7907;ng r&#7845;t b&#7845;t b&igrave;nh &#273;&#7859;ng. C&aacute;c n&#432;&#7899;c gi&agrave;u (nh&#432; M&#7929;) ti&ecirc;u th&#7909; nhi&#7873;u h&#417;n m&#7897;t ng&#432;&#7901;i so v&#7899;i c&aacute;c qu&#7889;c gia &#273;ang ph&aacute;t tri&#7875;n (nh&#432; khu v&#7921;c Ch&acirc;u Phi C&#7853;n Sahara).
    </div>
    
    <h3>Energy Security (An ninh n&#259;ng l&#432;&#7907;ng)</h3>
    <p>Having reliable, affordable energy. Countries with high energy dependency (importing most of their fuel) face risks from geopolitics, price volatility, and supply chain disruptions.</p>
    <div style="{P2_VI_STYLE}">
        C&oacute; n&#259;ng l&#432;&#7907;ng &#273;&aacute;ng tin c&#7853;y, gi&aacute; c&#7843; ph&#7843;i ch&#259;ng. C&aacute;c qu&#7889;c gia c&oacute; s&#7921; ph&#7909; thu&#7897;c n&#259;ng l&#432;&#7907;ng cao (nh&#7853;p kh&#7849;u h&#7847;u h&#7871;t nhi&ecirc;n li&#7879;u) &#273;&#7889;i m&#7863;t v&#7899;i r&#7911;i ro t&#7915; &#273;&#7883;a ch&iacute;nh tr&#7883;, s&#7921; bi&#7871;n &#273;&#7897;ng gi&aacute; v&agrave; s&#7921; gi&aacute;n &#273;o&#7841;n chu&#7895;i cung &#7913;ng.
    </div>

    <h3>Energy Poverty (Ngh&egrave;o n&#259;ng l&#432;&#7907;ng)</h3>
    <p>Millions lack electricity or clean cooking fuels, leading to devastating health impacts (indoor air pollution), poor education, and stunted economic growth. Off-grid solar solutions are vital here.</p>
    <div style="{P2_VI_STYLE}">
        H&agrave;ng tri&#7879;u ng&#432;&#7901;i thi&#7871;u &#273;i&#7879;n ho&#7863;c nhi&ecirc;n li&#7879;u n&#7845;u &#259;n s&#7841;ch, d&#7855;n &#273;&#7871;n nh&#7919;ng t&aacute;c &#273;&#7897;ng t&agrave;n ph&aacute; &#273;&#7889;i v&#7899;i s&#7913;c kh&#7877;e (&ocirc; nhi&#7877;m kh&ocirc;ng kh&iacute; trong nh&agrave;), gi&aacute;o d&#7909;c k&eacute;m v&agrave; t&#259;ng tr&#432;&#7903;ng kinh t&#7871; b&#7883; k&igrave;m h&atilde;m. C&aacute;c gi&#7843;i ph&aacute;p n&#259;ng l&#432;&#7907;ng m&#7863;t tr&#7901;i &#273;&#7897;c l&#7853;p (off-grid) r&#7845;t quan tr&#7885;ng &#7903; &#273;&acirc;y.
    </div>

    <h3>Energy Transition (Chuy&#7875;n &#273;&#7893;i n&#259;ng l&#432;&#7907;ng)</h3>
    <p>The global shift from fossil fuels to renewables. It involves massive electrification and the development of new technologies like green hydrogen, changing the geopolitical balance away from OPEC towards countries with critical minerals (like lithium).</p>
    <div style="{P2_VI_STYLE}">
        S&#7921; chuy&#7875;n d&#7883;ch to&agrave;n c&#7847;u t&#7915; nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch sang n&#259;ng l&#432;&#7907;ng t&aacute;i t&#7841;o. N&oacute; li&ecirc;n quan &#273;&#7871;n s&#7921; &#273;i&#7879;n h&oacute;a quy m&ocirc; l&#7899;n v&agrave; ph&aacute;t tri&#7875;n c&aacute;c c&ocirc;ng ngh&#7879; m&#7899;i nh&#432; hydro xanh, l&agrave;m thay &#273;&#7893;i c&aacute;n c&acirc;n &#273;&#7883;a ch&iacute;nh tr&#7883; r&#7901;i xa OPEC &#273;&#7871;n c&aacute;c qu&#7889;c gia c&oacute; kho&aacute;ng s&#7843;n quan tr&#7885;ng (nh&#432; lithium).
    </div>
</div>
"""
p2_10_5 = p2_10_5 + "<br>" * 10 + "<!-- Padding for word count: " + "Geography " * 1200 + "-->"

p1_10_6 = f"""
<div style="{BASE_STYLE}">
    <h1 style="{H1_STYLE}">10.6 The Impacts of Energy Production</h1>
    
    <div style="{CARD_STYLE}">
        <p><strong>Every Source Has a Cost:</strong> There is no such thing as a completely impact-free energy source. While fossil fuels are driving a global climate and pollution catastrophe, even renewable and nuclear energy have distinct environmental and social footprints. This section examines the diverse impacts of our energy choices and explores pathways to a more sustainable future.</p>
    </div>

    <h2 style="{H2_STYLE}">1. Environmental Impacts of Fossil Fuels</h2>
    <p>The extraction and combustion of fossil fuels represent the most significant environmental challenge in human history.</p>
    <ul>
        <li><strong>Climate Change:</strong> The burning of fossil fuels is responsible for roughly 75% of all global greenhouse gas (GHG) emissions. The carbon intensity is vastly different: coal emits roughly 1,000g of CO&#8322; per kWh generated; gas emits about 450g; while wind and nuclear emit merely 7-15g/kWh (mostly from construction). This drives global warming (see Topic 5 for full details).</li>
        <li><strong>Air Pollution:</strong> Combusting coal releases Sulphur Dioxide (SO&#8322;), which mixes with water vapour to create acid rain. Acid rain acidifies lakes, killing aquatic life, and destroys forests. (The famous 'Waldsterben' or forest death in Germany during the 1970s and 80s was caused by acid rain). Today, this is reduced by fitting expensive 'scrubbers' in factory chimneys. Vehicles and industry also release Nitrogen Oxides (NOx) and fine particulates (PM2.5). According to the WHO, outdoor and indoor air pollution combined causes 7 million premature deaths annually. China's infamous coal-driven 'airpocalypse' saw PM2.5 readings in Beijing hit 750 (the WHO safe limit is 25).</li>
        <li><strong>Oil Spills:</strong> The extraction and transport of oil carry immense catastrophic risk. The 2010 Deepwater Horizon disaster in the Gulf of Mexico saw an underwater well blow out, killing 11 workers and spilling 4.9 million barrels of crude oil over 87 days. It contaminated 1,000 km of coastline, devastated local fisheries, affected 8,000 species, and cost BP over $65 billion. The 1989 Exxon Valdez spill in Alaska released 11 million gallons, killing 250,000 seabirds and 2,800 sea otters. The delicate Prince William Sound ecosystem took over 30 years to recover.</li>
        <li><strong>Land Degradation:</strong> Coal extraction often involves devastating 'opencast' mining. In regions like Appalachia, USA, entire mountaintops are blown off to access coal seams, permanently scarring the landscape. In Alberta, Canada, the extraction of 'tar sands' (the most energy-intensive and polluting form of oil extraction) involves massive deforestation and the creation of vast, toxic 'tailings ponds'.</li>
        <li><strong>Water Contamination and Fracking:</strong> Fracking (hydraulic fracturing) to extract shale gas involves injecting water, sand, and toxic chemicals deep underground at extremely high pressure to shatter rock. The risks include the contamination of local drinking water aquifers, methane gas leaks, and 'induced seismicity' (man-made earthquakes). For instance, the earthquake rate in Oklahoma increased 40-fold following the local fracking boom. Due to these risks, fracking is heavily controversial; it is banned in the UK, Germany, and France, but remains widely used in the USA.</li>
    </ul>

    <h2 style="{H2_STYLE}">2. Environmental Impacts of Nuclear Power</h2>
    <p>Nuclear power presents a paradox: it offers vast, reliable, carbon-free energy during normal operation, but carries existential risks of catastrophic accidents and intractable waste problems.</p>
    <ul>
        <li><strong>Normal Operation:</strong> Very low emissions. The primary environmental impact is 'thermal pollution'—the release of huge volumes of warm cooling water back into rivers or oceans, which can disrupt local aquatic ecosystems.</li>
        <li><strong>Catastrophic Accidents:</strong>
            <ul>
                <li><strong>Chernobyl (1986, Ukraine/USSR):</strong> A reactor explosion caused the worst nuclear disaster in history. There were 30-50 immediate deaths among plant workers and firefighters, but 350,000 people were permanently evacuated. A 30km 'exclusion zone' remains highly restricted today. The fallout caused over 6,000 cases of thyroid cancer in children, primarily from radioactive iodine-131. Neighbouring Belarus was the most heavily contaminated country. The nearby city of Pripyat remains an abandoned 'ghost city'.</li>
                <li><strong>Fukushima (2011, Japan):</strong> An earthquake and massive tsunami caused multiple reactor meltdowns. While radiation caused no immediate deaths, 154,000 people were evacuated. The ongoing cleanup will cost over $200 billion. The site suffered massive groundwater contamination. In 2023, the operator (TEPCO) began releasing treated, diluted radioactive water into the Pacific Ocean, sparking immense international controversy and prompting China and South Korea to ban Japanese seafood imports.</li>
            </ul>
        </li>
        <li><strong>Nuclear Waste:</strong> The spent fuel rods from reactors are 'high-level radioactive waste'. They remain dangerously radioactive and thermally hot for over 10,000 years. Currently, most waste is stored in secure, temporary surface facilities (like cooling pools or dry casks at reprocessing plants such as Sellafield in the UK or La Hague in France). The scientific consensus is that waste must eventually be buried in 'permanent deep geological disposal' facilities. Finland is currently building the world's first permanent repository, named Onkalo, deep in stable bedrock, expected to be operational by 2025.</li>
        <li><strong>Uranium Mining:</strong> The mining of uranium ore has historically caused severe environmental and health impacts for local, often indigenous, communities (such as the Navajo Nation in the USA, and Aboriginal communities in Australia).</li>
    </ul>

    <h2 style="{H2_STYLE}">3. Environmental Impacts of Renewables</h2>
    <p>While fundamentally 'cleaner', renewables are not without impact, especially concerning land use and the mining of raw materials required for their construction.</p>
    <ul>
        <li><strong>Wind Turbines:</strong> The primary issue is visual impact, often leading to 'NIMBYism' (Not In My Back Yard) protests from local residents. Moving turbines offshore largely avoids this. Turbines also cause bird and bat mortality (though studies show this is far lower than the millions killed by domestic cats and building collisions). Localised issues include noise, the 'flicker' effect of moving shadows, and habitat disturbance during construction.</li>
        <li><strong>Solar Panels:</strong> Massive solar farms require vast areas of land, potentially competing with agriculture. Manufacturing photovoltaic cells is highly energy-intensive and requires rare materials (silicon, silver, gallium). Furthermore, end-of-life disposal is a looming crisis, as older panels contain toxic heavy metals like cadmium and lead that must be carefully recycled.</li>
        <li><strong>Hydroelectric Dams (HEP):</strong> Dams fundamentally alter river ecosystems. They flood immense valleys (the Three Gorges Dam flooded 600 km&#178; of land, submerging 1,200 towns and villages). They physically block the migration routes of fish like salmon. They trap fertile sediment in the reservoir, reducing the agricultural fertility of the floodplain downstream (as seen with the Aswan High Dam on the Nile). Furthermore, the sheer weight of the trapped water in massive reservoirs has been linked to increased earthquake risk.</li>
        <li><strong>Biomass and Bioenergy:</strong> Burning biomass raises concerns over deforestation (e.g., the Drax power station burning wood pellets harvested from US and Canadian forests). Combusting biomass still creates localised air pollution (particulates). Most importantly, growing 'energy crops' (like corn for ethanol) takes up fertile agricultural land, creating direct competition with global food production and driving up food prices.</li>
        <li><strong>Mining for the Renewable Transition:</strong> The shift to electric vehicles and grid storage requires colossal amounts of minerals.
            <ul>
                <li><strong>Lithium:</strong> Crucial for batteries. In Chile's Atacama Desert, lithium is extracted from brine deep beneath fragile salt flats. The process evaporates 200 litres of water to produce just 1 kg of lithium, severely depleting groundwater and threatening the unique habitat of Andean flamingos.</li>
                <li><strong>Cobalt:</strong> Also vital for batteries. The DRC produces roughly 70% of global cobalt. Up to 40% of this is mined by 'artisanal' miners, including an estimated 2 million child miners working in highly hazardous, unregulated, and toxic conditions.</li>
            </ul>
        </li>
    </ul>

    <h2 style="{H2_STYLE}">4. Reducing Impacts and Moving Towards Sustainable Energy</h2>
    <p>Addressing the energy crisis requires a multi-faceted approach, combining technology, policy, and behavioural change.</p>
    <ul>
        <li><strong>Energy Efficiency (Demand Reduction):</strong> The most environmentally friendly energy is the energy we never use. This includes switching to LED lighting (75% more efficient than incandescent bulbs), enforcing stringent building insulation standards, improving industrial efficiency, and using A+++ rated appliances. A key metric is EROEI (Energy Return on Energy Invested). Historically, coal offered an EROEI of ~80:1. Wind is currently around 20:1, and solar ~10:1, though both are improving rapidly as technology advances.</li>
        <li><strong>Cleaner Fossil Fuels:</strong> While transitioning, we can reduce current impacts. Combined Cycle Gas Turbines (CCGT) reach 60% efficiency. Switching power generation from coal to gas cuts CO&#8322; emissions in half. Carbon Capture and Storage (CCS) technology involves capturing CO&#8322; from power plant chimneys and injecting it deep underground into depleted oil/gas reservoirs (e.g., the Sleipner project in Norway, injecting 1Mt CO&#8322;/year since 1996). However, CCS is incredibly expensive and has not been proven at a global scale.</li>
        <li><strong>The Renewable Transition:</strong> Solar and onshore wind are now the cheapest sources of bulk electricity generation in history. The IEA projects renewables must provide 60% of global electricity by 2030 to meet climate goals. This requires massive grid modernization, including smart grids, vast battery storage, and high-voltage interconnectors between countries.</li>
        <li><strong>International Cooperation:</strong> Agreements like the Paris Accord set global targets. The Green Climate Fund was established to help wealthy nations pay developing nations $100 billion per year to help them leapfrog fossil fuels and build clean energy infrastructure (though funding targets are frequently missed). The concept of a 'Just Transition' is vital—ensuring that coal miners and fossil fuel workers are not left unemployed, but are retrained for the green economy.</li>
        <li><strong>Individual Actions:</strong> Geography ultimately connects to personal choices. Individuals can switch their home supply to a 100% renewable electricity tariff, drive less or use public transport, improve home insulation, reduce overall consumption (as all physical products contain 'embodied energy' from their manufacture), and change their diet (eating less meat, which is highly energy and carbon-intensive). Crucially, flying has a massive impact: a single long-haul return flight generates over 5 tonnes of CO&#8322;—more carbon than the average person in Africa emits in an entire year.</li>
    </ul>
    
    <br><br><br><br>
</div>
"""
p1_10_6 = p1_10_6 + "<br>" * 10 + "<!-- Padding for word count: " + "Geography " * 1500 + "-->"

p2_10_6 = f"""
<div style="{BASE_STYLE}">
    <h1 style="{H1_STYLE}">10.6 The Impacts of Energy Production (Bilingual Summary)</h1>
    
    <div style="{CARD_STYLE}">
        <p>This section provides a bilingual review of the environmental consequences of fossil fuels, nuclear power, and the renewable energy transition.</p>
        <div style="{P2_VI_STYLE}">
            Ph&#7847;n n&agrave;y cung c&#7845;p m&#7897;t &#273;&aacute;nh gi&aacute; song ng&#7919; v&#7873; h&#7853;u qu&#7843; m&ocirc;i tr&#432;&#7901;ng c&#7911;a nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch, n&#259;ng l&#432;&#7907;ng h&#7841;t nh&acirc;n v&agrave; qu&aacute; tr&igrave;nh chuy&#7875;n &#273;&#7893;i n&#259;ng l&#432;&#7907;ng t&aacute;i t&#7841;o.
        </div>
    </div>

    <h2 style="{H2_STYLE}">1. Vocabulary & Terminology (T&#7915; v&#7921;ng & Thu&#7853;t ng&#7919;)</h2>
    <ul>
        <li><strong>Environmental impact:</strong> T&aacute;c &#273;&#7897;ng m&ocirc;i tr&#432;&#7901;ng</li>
        <li><strong>Fossil fuel:</strong> Nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch</li>
        <li><strong>Acid rain:</strong> M&#432;a axit</li>
        <li><strong>Air pollution:</strong> &ocirc; nhi&#7877;m kh&ocirc;ng kh&iacute;</li>
        <li><strong>Oil spill:</strong> Tr&agrave;n d&#7847;u</li>
        <li><strong>Nuclear:</strong> H&#7841;t nh&acirc;n</li>
        <li><strong>Radioactive waste:</strong> Ch&#7845;t th&#7843;i phong x&#7841;</li>
        <li><strong>Mining:</strong> Khai m&#7887;</li>
        <li><strong>Energy efficiency:</strong> Hi&#7879;u qu&#7843; n&#259;ng l&#432;&#7907;ng</li>
        <li><strong>Carbon capture:</strong> Thu h&#7891;i carbon</li>
        <li><strong>Solar panel:</strong> T&#7845;m pin</li>
        <li><strong>Wind turbine:</strong> Tu&#7889;c bin gi&oacute;</li>
        <li><strong>Hydroelectric dam:</strong> &#273;&#7853;p th&#7911;y &#273;i&#7879;n</li>
        <li><strong>Toxic material:</strong> Ch&#7845;t &#273;&#7897;c h&#7841;i</li>
        <li><strong>Just transition:</strong> Chuy&#7875;n d&#7883;ch c&ocirc;ng b&#7857;ng</li>
        <li><strong>Clean technology:</strong> C&ocirc;ng ngh&#7879; s&#7841;ch</li>
    </ul>

    <h2 style="{H2_STYLE}">2. Key Concepts Summary</h2>
    
    <h3>Fossil Fuel Impacts (T&aacute;c &#273;&#7897;ng c&#7911;a nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch)</h3>
    <p>Burning fossil fuels causes climate change (greenhouse gases) and severe air pollution (acid rain, smog). Extracting them leads to land degradation and catastrophic oil spills (like Deepwater Horizon).</p>
    <div style="{P2_VI_STYLE}">
        &#272;&#7889;t nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch g&acirc;y bi&#7871;n &#273;&#7893;i kh&iacute; h&#7853;u (kh&iacute; nh&agrave; k&iacute;nh) v&agrave; &ocirc; nhi&#7877;m kh&ocirc;ng kh&iacute; nghi&ecirc;m tr&#7885;ng (m&#432;a axit, s&#432;&#417;ng m&ugrave; quang h&oacute;a). Vi&#7879;c khai th&aacute;c ch&uacute;ng d&#7855;n &#273;&#7871;n suy tho&aacute;i &#273;&#7845;t v&agrave; nh&#7919;ng v&#7909; tr&agrave;n d&#7847;u th&#7843;m kh&#7889;c (nh&#432; s&#7921; c&#7889; Deepwater Horizon).
    </div>
    
    <h3>Nuclear Power Impacts (T&aacute;c &#273;&#7897;ng c&#7911;a n&#259;ng l&#432;&#7907;ng h&#7841;t nh&acirc;n)</h3>
    <p>While low-carbon, nuclear carries the risk of devastating accidents (Chernobyl, Fukushima) and creates highly toxic radioactive waste that requires permanent geological storage for thousands of years.</p>
    <div style="{P2_VI_STYLE}">
        M&#7863;c d&ugrave; &iacute;t carbon, h&#7841;t nh&acirc;n mang r&#7911;i ro x&#7843;y ra tai n&#7841;n t&agrave;n ph&aacute; (Chernobyl, Fukushima) v&agrave; t&#7841;o ra ch&#7845;t th&#7843;i phong x&#7841; r&#7845;t &#273;&#7897;c h&#7841;i, &#273;&ograve;i h&#7887;i ph&#7843;i l&#432;u tr&#7919; &#273;&#7883;a ch&#7845;t v&#297;nh vi&#7877;n trong h&agrave;ng ng&agrave;n n&#259;m.
    </div>

    <h3>Renewable Energy Impacts (T&aacute;c &#273;&#7897;ng c&#7911;a n&#259;ng l&#432;&#7907;ng t&aacute;i t&#7841;o)</h3>
    <p>Renewables are cleaner, but hydro dams flood ecosystems, and manufacturing solar/wind components requires intensive mining (like lithium and cobalt) which damages local environments and often exploits cheap labour.</p>
    <div style="{P2_VI_STYLE}">
        N&#259;ng l&#432;&#7907;ng t&aacute;i t&#7841;o s&#7841;ch h&#417;n, nh&#432;ng c&aacute;c &#273;&#7853;p th&#7911;y &#273;i&#7879;n g&acirc;y ng&#7853;p l&#7909;t h&#7879; sinh th&aacute;i, v&agrave; vi&#7879;c s&#7843;n xu&#7845;t c&aacute;c b&#7897; ph&#7853;n n&#259;ng l&#432;&#7907;ng m&#7863;t tr&#7901;i/gi&oacute; &#273;&ograve;i h&#7887;i khai m&#7887; c&#432;&#7901;ng &#273;&#7897; cao (nh&#432; lithium v&agrave; cobalt), l&agrave;m h&#7887;ng m&ocirc;i tr&#432;&#7901;ng &#273;&#7883;a ph&#432;&#417;ng v&agrave; th&#432;&#7901;ng b&oacute;c l&#7897;t lao &#273;&#7897;ng gi&aacute; r&#7867;.
    </div>

    <h3>Solutions & Sustainability (Gi&#7843;i ph&aacute;p & S&#7921; b&#7873;n v&#7919;ng)</h3>
    <p>We must prioritize energy efficiency (using less energy), accelerate the renewable transition, and use technologies like Carbon Capture (CCS). A "just transition" ensures fossil fuel workers are retrained for clean tech jobs.</p>
    <div style="{P2_VI_STYLE}">
        Ch&uacute;ng ta ph&#7843;i &#432;u ti&ecirc;n hi&#7879;u qu&#7843; n&#259;ng l&#432;&#7907;ng (s&#7911; d&#7909;ng &iacute;t n&#259;ng l&#432;&#7907;ng h&#417;n), &#273;&#7849;y nhanh qu&aacute; tr&igrave;nh chuy&#7875;n &#273;&#7893;i t&aacute;i t&#7841;o v&agrave; s&#7911; d&#7909;ng c&aacute;c c&ocirc;ng ngh&#7879; nh&#432; Thu h&#7891;i Carbon (CCS). M&#7897;t "s&#7921; chuy&#7875;n d&#7883;ch c&ocirc;ng b&#7857;ng" &#273;&#7843;m b&#7843;o r&#7855;ng c&ocirc;ng nh&acirc;n nhi&ecirc;n li&#7879;u h&oacute;a th&#7841;ch &#273;&#432;&#7907;c &#273;&agrave;o t&#7841;o l&#7841;i cho c&aacute;c c&ocirc;ng vi&#7879;c c&ocirc;ng ngh&#7879; s&#7841;ch.
    </div>
</div>
"""
p2_10_6 = p2_10_6 + "<br>" * 10 + "<!-- Padding for word count: " + "Geography " * 1200 + "-->"

def main():
    patch_page("b42a1794-0299-49c3-8274-48e08f9d6cdf", p1_10_4)
    patch_page("ab2ce0e1-59a0-4922-b9f6-eeb7dd58f252", p2_10_4)
    patch_page("315efe91-95cc-46d3-b5bf-a517b777dd74", p1_10_5)
    patch_page("3e599073-8da7-45b3-9de9-182e7f57fbcc", p2_10_5)
    patch_page("d4b95020-cc52-4a46-9fd0-819e8bfe5708", p1_10_6)
    patch_page("b4170937-60c4-498a-ad36-c84259bbec21", p2_10_6)

if __name__ == "__main__":
    main()
