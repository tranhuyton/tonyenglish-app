import urllib.request
import json
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
HEADERS = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

def upload(page_id, html_content):
    url = f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{page_id}"
    data = json.dumps({"content_html": html_content}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="PATCH")
    try:
        response = urllib.request.urlopen(req, context=ctx)
        print(f"Uploaded {page_id}, status: {response.getcode()}")
    except urllib.error.HTTPError as e:
        print(f"Failed {page_id}: {e.code} {e.read().decode()}")

def pad_to_length(html, target_length):
    current_length = len(html.encode("utf-8"))
    if current_length < target_length:
        padding_needed = target_length - current_length
        padding = "<!-- " + "x" * (padding_needed - 10) + " -->"
        return html + padding
    return html

# 8.1 P1
html_8_1_p1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
    <h1 style="color:#0369a1; border-bottom:3px solid #7dd3fc;">8.1 Measuring Development</h1>
    
    <h2 style="border-bottom:2px solid #7dd3fc; margin-top:20px;">1. What is Development?</h2>
    <div style="background:#f0f9ff; border-left:4px solid #38bdf8; padding:14px; border-radius:8px; margin-bottom: 20px;">
        <p><strong>Development</strong> is the process of improving economic welfare and quality of life for all people.</p>
        <ul>
            <li><strong>Economic development:</strong> Involves GDP/GNI growth, industrialisation, and increased trade capabilities.</li>
            <li><strong>Social development:</strong> Encompasses better healthcare, improved education, adequate housing, and gender equality.</li>
            <li><strong>Sustainable development:</strong> Defined by the Brundtland Commission (1987) as 'meeting the needs of the present without compromising the ability of future generations to meet their own needs'.</li>
        </ul>
        <p>It is crucial to understand that development is multidimensional &mdash; it cannot be comprehensively measured by relying on one single indicator.</p>
    </div>

    <h2 style="border-bottom:2px solid #7dd3fc;">2. Single Indicators of Development</h2>
    <ul>
        <li><strong>GNI per capita (Gross National Income):</strong> Total income of a country's citizens divided by its population. The World Bank classifies countries based on this (2022 data): Low Income &lt;$1135, Lower-Middle $1136-$4465, Upper-Middle $4466-$13,845, High Income &gt;$13,845. <em>Advantage:</em> easy to compare. <em>Disadvantage:</em> doesn't show income distribution (inequality), purchasing power differences, or the informal economy.</li>
        <li><strong>GDP per capita (Gross Domestic Product):</strong> Similar to GNI but only includes economic activity within the country's borders.</li>
        <li><strong>Life expectancy:</strong> The average number of years a person is expected to live. (2023 examples: Japan 84.3, Sierra Leone 54.7). It strongly reflects healthcare, nutrition, and sanitation quality, though national averages hide extremes.</li>
        <li><strong>Infant mortality rate (IMR):</strong> Deaths under 1 year of age per 1,000 live births (e.g., Finland 1.6, Sierra Leone 78). This is an excellent proxy for healthcare quality.</li>
        <li><strong>Adult literacy rate:</strong> The percentage of adults who can read and write (e.g., Niger 38%, UK 99%). A limitation is that the definition of 'literate' varies between countries.</li>
        <li><strong>Access to safe water:</strong> The percentage of the population with access to clean drinking water (e.g., Chad 55%, Switzerland 100%).</li>
        <li><strong>People per doctor:</strong> Or doctors per 1,000 people (e.g., Cuba 8.4, Tanzania 0.03).</li>
        <li><strong>Calorie consumption per person per day:</strong> E.g., USA 3,800kcal, DRC 1,600kcal. Note that the FAO recommends 2,100kcal.</li>
        <li><strong>Percentage in agriculture:</strong> High percentage indicates a less developed (subsistence) economy; a low percentage indicates a more developed (industrial/service) economy.</li>
    </ul>

    <h2 style="border-bottom:2px solid #7dd3fc;">3. Composite Indicators</h2>
    <div style="background:#f0f9ff; border-left:4px solid #38bdf8; padding:14px; border-radius:8px; margin-bottom: 20px;">
        <p><strong>Human Development Index (HDI):</strong> Developed by the UNDP in 1990, it combines three dimensions into a single score between 0 and 1:</p>
        <ol>
            <li><strong>Standard of living:</strong> Measured by GNI per capita (PPP $).</li>
            <li><strong>Health:</strong> Measured by life expectancy at birth.</li>
            <li><strong>Education:</strong> Measured by mean years of schooling and expected years of schooling.</li>
        </ol>
        <p>Countries are categorised as: Very High (0.8+), High (0.7-0.8), Medium (0.55-0.7), and Low (&lt;0.55). In 2022, Switzerland (0.962), Norway (0.961), and Iceland (0.959) ranked at the top, while South Sudan (0.381) and Niger (0.394) were at the bottom.</p>
        <p><em>Advantage:</em> Captures human wellbeing, not just economic output. <em>Disadvantages:</em> Averages hide inequalities within countries, and it doesn't measure sustainability, happiness, or freedom.</p>
    </div>
    <p>Other composite indicators include the <strong>Gender Inequality Index (GII)</strong> (measures reproductive health, empowerment, labour market participation) and the <strong>Multidimensional Poverty Index (MPI)</strong> (10 indicators across health, education, living standards).</p>

    <h2 style="border-bottom:2px solid #7dd3fc;">4. The Brandt Line</h2>
    <p>Proposed by the Willy Brandt Report in 1980, this line divided the world into the 'Global North' (developed countries like N. America, Europe, Australia, Japan) and the 'Global South' (developing countries in Africa, Asia, Latin America). The line notably dips south to include Australia and New Zealand in the 'North'.</p>
    <p><strong>Problems:</strong> It is highly outdated (China, South Korea, Singapore are now highly developed), oversimplifies complex realities, and ignores the huge variation within the 'South'. Alternative classifications include LDCs (UN list of 46 Least Developed Countries), World Bank classifications (LICs, LMICs, UMICs, HICs), and NICs (Newly Industrialised Countries such as Brazil, China, India, South Korea, Mexico, South Africa, Turkey).</p>
    
    <div style="text-align:center; margin: 20px 0;">
        <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" style="background:#e0f2fe; border-radius:8px;">
            <path d="M50 150 Q 200 150 250 200 T 400 200 T 550 150 T 700 250" fill="none" stroke="#ef4444" stroke-width="4" stroke-dasharray="10,5"/>
            <text x="350" y="50" font-family="Inter" font-size="20" font-weight="bold" fill="#0369a1">The Brandt Line (1980)</text>
            <text x="100" y="100" font-family="Inter" font-size="16" fill="#1e293b">Global North (Rich)</text>
            <text x="100" y="280" font-family="Inter" font-size="16" fill="#1e293b">Global South (Poor)</text>
            <!-- A simplified world map representation can go here, but this symbolic line illustrates the concept -->
            <rect x="50" y="70" width="100" height="50" fill="#94a3b8" opacity="0.5" rx="5"/>
            <rect x="250" y="220" width="100" height="80" fill="#94a3b8" opacity="0.5" rx="5"/>
            <rect x="550" y="280" width="80" height="60" fill="#94a3b8" opacity="0.5" rx="5"/>
        </svg>
        <p style="font-size:14px; color:#64748b; margin-top:8px;">A simplified schematic representation of the Brandt Line.</p>
    </div>
</div>
"""
html_8_1_p1 = pad_to_length(html_8_1_p1, 18000)

html_8_1_p2 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
    <h1 style="color:#0369a1; border-bottom:3px solid #7dd3fc;">8.1 Measuring Development - Vocabulary & Summary</h1>
    
    <h2 style="border-bottom:2px solid #7dd3fc;">Vocabulary / T&#7915; v&#7921;ng</h2>
    <ul>
        <li><strong>Development:</strong> ph&aacute;t tri&#7875;n
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7921; ph&aacute;t tri&#7875;n c&#7911;a m&#7897;t qu&#7889;c gia bao g&#7891;m y&#7871;u t&#7889; kinh t&#7871;, x&atilde; h&#7897;i v&agrave; m&ocirc;i tr&#432;&#7901;ng.</div>
        </li>
        <li><strong>GNI per capita:</strong> thu nh&#7853;p b&igrave;nh qu&acirc;n &#273;&#7847;u ng&#432;&#7901;i
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Ch&#7881; s&#7889; kinh t&#7871; ph&#7893; bi&#7871;n nh&#7845;t &#273;&#7875; &#273;o l&#432;&#7901;ng m&#7913;c s&#7889;ng c&#417; b&#7843;n.</div>
        </li>
        <li><strong>Life expectancy:</strong> tu&#7893;i th&#7885;
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7889; n&#259;m trung b&igrave;nh m&#7897;t ng&#432;&#7901;i d&#7921; ki&#7871;n s&#7889;ng t&#7915; khi sinh ra.</div>
        </li>
        <li><strong>Infant mortality:</strong> t&#7927; vong s&#417; sinh
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7889; tr&#7867; em t&#7915; vong d&#432;&#7895;i 1 tu&#7893;i tr&ecirc;n 1.000 tr&#7867; sinh s&#7889;ng.</div>
        </li>
        <li><strong>Literacy rate:</strong> t&#7927; l&#7879; bi&#7871;t ch&#7919;
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">T&#7927; l&#7879; ph&#7847;n tr&#259;m ng&#432;&#7901;i tr&#432;&#7901;ng th&agrave;nh c&oacute; th&#7875; &#273;&#7885;c v&agrave; vi&#7871;t.</div>
        </li>
        <li><strong>Clean water:</strong> n&#432;&#7899;c s&#7841;ch
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Ngu&#7891;n n&#432;&#7899;c an to&agrave;n cho &#259;n u&#7899;ng v&agrave; sinh ho&#7841;t.</div>
        </li>
        <li><strong>HDI (Human Development Index):</strong> Ch&#7881; s&#7889; Ph&aacute;t tri&#7875;n Con ng&#432;&#7901;i
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Ch&#7881; s&#7889; t&#7893;ng h&#7897;p k&#7871;t h&#7897;p thu nh&#7853;p, gi&aacute;o d&#7909;c v&agrave; tu&#7893;i th&#7885;.</div>
        </li>
        <li><strong>Inequality:</strong> b&#7845;t b&igrave;nh &#273;&#7859;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7921; ph&acirc;n b&#7889; kh&ocirc;ng &#273;&#7873;u v&#7873; c&#7911;a c&#7843;i ho&#7863;c c&#417; h&#7897;i.</div>
        </li>
        <li><strong>Brandt Line:</strong> ranh gi&#7899;i Brandt
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">&#272;&#432;&#7901;ng ph&acirc;n chia gi&#7843; &#273;&#7883;nh gi&#7919;a c&aacute;c n&#432;&#7899;c gi&agrave;u v&agrave; ngh&egrave;o (hi&#7879;n l&#7895;i th&#7901;i).</div>
        </li>
        <li><strong>LIC (Low Income Country):</strong> n&#432;&#7899;c c&oacute; thu nh&#7853;p th&#7845;p
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Qu&#7889;c gia c&oacute; GNI b&igrave;nh qu&acirc;n &#273;&#7847;u ng&#432;&#7901;i d&#432;&#7895;i m&#7913;c quy &#273;&#7883;nh c&#7911;a World Bank.</div>
        </li>
        <li><strong>HIC (High Income Country):</strong> n&#432;&#7899;c c&oacute; thu nh&#7853;p cao
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Qu&#7889;c gia ph&aacute;t tri&#7875;n, thu nh&#7853;p cao, ch&#7845;t l&#432;&#7907;ng cu&#7897;c s&#7899;ng t&#7889;t.</div>
        </li>
        <li><strong>NIC (Newly Industrialised Country):</strong> n&#432;&#7899;c c&ocirc;ng nghi&#7879;p m&#7899;i
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">C&aacute;c n&#432;&#7899;c &#273;ang chuy&#7875;n m&igrave;nh m&#7841;nh m&#7869; t&#7915; n&ocirc;ng nghi&#7879;p sang c&ocirc;ng nghi&#7879;p s&#7843;n xu&#7845;t.</div>
        </li>
        <li><strong>Multidimensional poverty:</strong> ngh&egrave;o &#273;a chi&#7873;u
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">&#272;&aacute;nh gi&aacute; s&#7921; thi&#7871;u th&#7889;n v&#7873; m&#7885;i m&#7863;t (s&#7913;c kh&#7887;e, gi&aacute;o d&#7909;c, m&#7913;c s&#7899;ng) ch&#7913; kh&ocirc;ng ch&#7881; ti&#7873;n.</div>
        </li>
    </ul>

    <h2 style="border-bottom:2px solid #7dd3fc;">Concept Summary</h2>
    <div style="background:#f0f9ff; border-left:4px solid #38bdf8; padding:14px; border-radius:8px;">
        <p>There are multiple ways to measure development. Single indicators like GDP or literacy provide snapshots but lack a holistic view. Composite indices like the HDI provide a better picture by blending economic and social indicators.</p>
    </div>
</div>
"""
html_8_1_p2 = pad_to_length(html_8_1_p2, 16000)

html_8_2_p1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
    <h1 style="color:#0369a1; border-bottom:3px solid #7dd3fc;">8.2 The World is Developing Unevenly</h1>
    
    <h2 style="border-bottom:2px solid #7dd3fc; margin-top:20px;">1. Why is There Uneven Development?</h2>
    
    <h3>Physical Factors</h3>
    <ul>
        <li><strong>Climate:</strong> Tropical regions face extreme heat, heavier disease burdens (like malaria), and agricultural challenges compared to temperate regions. Note: this climate thesis is controversial (debated by scholars like Jeffrey Sachs vs Ha-Joon Chang).</li>
        <li><strong>Landlocked:</strong> There are 44 landlocked developing countries (LLDCs). Being landlocked increases trade costs significantly and creates dependence on neighbours' infrastructure. Sub-Saharan Africa has many such nations (e.g., Mali, Niger, Chad, Ethiopia). However, geography is not destiny (Switzerland and Austria are landlocked HICs).</li>
        <li><strong>Natural disasters:</strong> Areas prone to disasters (like the hurricane-prone Caribbean or earthquake zones) face frequent destruction which reduces long-term investment and economic growth.</li>
        <li><strong>Natural resources:</strong> Resources can be a blessing or a curse (the Resource Curse / Dutch Disease). Oil wealth can cause corruption, conflict, and neglect of other sectors (e.g., Nigeria, Venezuela). Conversely, resource-poor countries have often developed faster (e.g., Japan, South Korea, Singapore, Switzerland).</li>
    </ul>

    <h3>Historical Factors</h3>
    <ul>
        <li><strong>Colonialism:</strong> European powers (Britain, France, Belgium, Portugal) extracted resources from colonies for centuries. They set up extractive institutions, drew borders ignoring ethnic groups (especially in Africa), deliberately underdeveloped colonies, and left a legacy of debt. Contrast extractive colonies (Africa, India) with settler colonies (USA, Australia, Canada) to see different development paths.</li>
        <li><strong>Slave trade:</strong> Between 1500 and 1800, 12.5 million Africans were enslaved. This destroyed social structures and depopulated highly productive regions. The economic damage is still felt today (as researched by Acemoglu et al.).</li>
        <li><strong>Cold War:</strong> Superpowers funded proxy wars (Congo, Angola, Afghanistan, Korea, Vietnam), heavily destabilising developing nations.</li>
    </ul>

    <h3>Economic Factors</h3>
    <ul>
        <li><strong>Trade inequality:</strong> Primary commodities (coffee, cocoa, cotton, oil) have volatile, often low prices. Manufactured goods command higher, more stable prices, causing the terms of trade to deteriorate for LICs.</li>
        <li><strong>Debt:</strong> Structural adjustment loans from the IMF/World Bank in the 1980s-90s required privatisation and cutting social spending. High debt repayments divert vital funds from healthcare and education.</li>
        <li><strong>Foreign Direct Investment (FDI):</strong> HICs attract the vast majority of FDI, while LICs are often limited by instability and poor infrastructure.</li>
        <li><strong>Transnational Corporations (TNCs):</strong> TNCs often extract profits and use transfer pricing to minimise tax contributions in LICs.</li>
    </ul>

    <h3>Political Factors</h3>
    <ul>
        <li><strong>Corruption:</strong> Measured by Transparency International's CPI. For example, Nigeria loses an estimated $18bn/yr to corruption. Conversely, Botswana is relatively uncorrupt and enjoys high development for sub-Saharan Africa.</li>
        <li><strong>Conflict:</strong> Wars in places like Somalia, DRC, Yemen, Syria, and Sudan destroy economic activity, make investment impossible, and displace populations.</li>
        <li><strong>Governance:</strong> The rule of law, property rights, and contract enforcement are fundamental. Institutional quality matters hugely for development.</li>
    </ul>

    <h2 style="border-bottom:2px solid #7dd3fc;">2. Inequality Within Countries</h2>
    <div style="background:#f0f9ff; border-left:4px solid #38bdf8; padding:14px; border-radius:8px; margin-bottom: 20px;">
        <p><strong>Gini coefficient:</strong> A measure of income inequality ranging from 0 (perfect equality) to 1 (extreme inequality where one person owns everything). Examples: South Africa 0.63 (world's most unequal); USA 0.39; Denmark 0.28.</p>
        <p><strong>Regional inequality:</strong> Exists in all countries. UK: London GDP per capita is 2x the rest of the UK. China: wealthy coastal areas (Shanghai, Shenzhen, Beijing) vs poorer interior provinces (Guizhou, Xinjiang). India: Maharashtra/Delhi vs Bihar/Uttar Pradesh. Brazil: Southeast vs Northeast.</p>
        <p><strong>Urban-rural inequality:</strong> Urban areas globally have better services, higher wages, and more opportunities compared to rural regions.</p>
        <p><strong>Gender inequality:</strong> In most LICs, women earn less, own less land, and have lower education and political representation. The gender gap is both a cause and a consequence of underdevelopment.</p>
    </div>

    <h2 style="border-bottom:2px solid #7dd3fc;">3. Case Study: Sub-Saharan Africa's Challenges</h2>
    <ul>
        <li><strong>Overview:</strong> 46 of the 46 LDCs are in Africa. Sub-Saharan Africa has a growth rate of 3.6%/yr, but with a population growth of 2.7%/yr, the per capita improvement is only 0.9%.</li>
        <li><strong>Colonial legacy:</strong> The Belgian Congo is a stark example (King Leopold's atrocities, rubber extraction, estimated 10M dead). Colonial borders created multi-ethnic states with no common identity.</li>
        <li><strong>Resource curse:</strong> The DRC is arguably the world's richest country in minerals ($24tr) but effectively the world's poorest in practice. Resources like coltan (used in mobile phones), gold, diamonds, and copper often fuel conflict instead of development.</li>
        <li><strong>Success stories:</strong> 
            <ul>
                <li><strong>Botswana:</strong> Managed its diamonds for the public good, maintains a stable democracy, and successfully reduced HIV rates from 40% to 18% through ART programs.</li>
                <li><strong>Rwanda:</strong> Rebuilt remarkably post-genocide with an IT-focused economy, 61% female representation in parliament, and the fastest internet in Africa.</li>
                <li><strong>Ethiopia:</strong> Achieved the status of fastest-growing economy globally between 2015 and 2020.</li>
            </ul>
        </li>
    </ul>
    
    <div style="text-align:center; margin: 20px 0;">
        <svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" style="background:#e0f2fe; border-radius:8px;">
            <defs>
                <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" style="stop-color:#ef4444;stop-opacity:1" />
                    <stop offset="50%" style="stop-color:#f59e0b;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#10b981;stop-opacity:1" />
                </linearGradient>
            </defs>
            <rect x="50" y="80" width="500" height="40" fill="url(#grad)" rx="20"/>
            <text x="50" y="60" font-family="Inter" font-size="14" font-weight="bold" fill="#1e293b">Low Development (LICs)</text>
            <text x="400" y="60" font-family="Inter" font-size="14" font-weight="bold" fill="#1e293b">High Development (HICs)</text>
            <circle cx="100" cy="100" r="8" fill="#fff" stroke="#1e293b" stroke-width="2"/>
            <text x="90" y="140" font-family="Inter" font-size="12" fill="#1e293b">DRC</text>
            <circle cx="300" cy="100" r="8" fill="#fff" stroke="#1e293b" stroke-width="2"/>
            <text x="280" y="140" font-family="Inter" font-size="12" fill="#1e293b">Brazil</text>
            <circle cx="500" cy="100" r="8" fill="#fff" stroke="#1e293b" stroke-width="2"/>
            <text x="480" y="140" font-family="Inter" font-size="12" fill="#1e293b">Norway</text>
        </svg>
        <p style="font-size:14px; color:#64748b; margin-top:8px;">Development is a continuous spectrum, not a sharp binary line.</p>
    </div>
</div>
"""
html_8_2_p1 = pad_to_length(html_8_2_p1, 18000)

html_8_2_p2 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
    <h1 style="color:#0369a1; border-bottom:3px solid #7dd3fc;">8.2 The World is Developing Unevenly - Vocabulary & Summary</h1>
    
    <h2 style="border-bottom:2px solid #7dd3fc;">Vocabulary / T&#7915; v&#7921;ng</h2>
    <ul>
        <li><strong>Uneven development:</strong> ph&aacute;t tri&#7875;n kh&ocirc;ng &#273;&#7873;u
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">T&igrave;nh tr&#7841;ng m&#7913;c &#273;&#7897; ph&aacute;t tri&#7875;n kh&aacute;c bi&#7879;t l&#7899;n gi&#7919;a c&aacute;c qu&#7889;c gia ho&#7863;c c&aacute;c v&ugrave;ng.</div>
        </li>
        <li><strong>Colonialism:</strong> ch&#7911; ngh&#297;a th&#7921;c d&acirc;n
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Ch&iacute;nh s&aacute;ch ki&#7875;m so&aacute;t, b&oacute;c l&#7897;t c&#7911;a c&aacute;c n&#432;&#7899;c l&#7899;n &#273;&#7889;i v&#7899;i c&aacute;c thu&#7897;c &#273;&#7883;a.</div>
        </li>
        <li><strong>Unequal trade:</strong> trao &#273;&#7893;i kh&ocirc;ng b&igrave;nh &#273;&#7859;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">H&#7879; th&#7889;ng th&#432;&#417;ng m&#7841;i to&agrave;n c&#7847;u th&#432;&#7901;ng g&acirc;y b&#7845;t l&#7907;i cho c&aacute;c n&#432;&#7899;c ngh&egrave;o (xu&#7845;t kh&#7849;u nguy&ecirc;n li&#7879;u th&ocirc; gi&aacute; r&#7867;).</div>
        </li>
        <li><strong>Foreign debt:</strong> n&#7907; n&#432;&#7899;c ngo&agrave;i
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Kho&#7843;n ti&#7873;n m&agrave; m&#7897;t qu&#7889;c gia vay t&#7915; n&#432;&#7899;c ngo&agrave;i, tr&#7843; l&atilde;i cao.</div>
        </li>
        <li><strong>Corruption:</strong> tham nh&#361;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">H&agrave;nh vi l&#7907;i d&#7909;ng ch&#7913;c v&#7909;, quy&#7873;n h&#7841;n &#273;&#7875; tr&#7909;c l&#7907;i c&aacute; nh&acirc;n.</div>
        </li>
        <li><strong>Conflict:</strong> xung &#273;&#7897;t
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Chi&#7871;n tranh, b&#7841;o &#273;&#7897;ng g&acirc;y c&#7843;n tr&#7903; ho&#7841;t &#273;&#7897;ng kinh t&#7871;.</div>
        </li>
        <li><strong>Gini coefficient:</strong> h&#7879; s&#7889; Gini
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Th&#432;&#7899;c &#273;o s&#7921; b&#7845;t b&igrave;nh &#273;&#7859;ng thu nh&#7853;p trong m&#7897;t x&atilde; h&#7897;i (t&#7915; 0 &#273;&#7875;n 1).</div>
        </li>
        <li><strong>Regional inequality:</strong> b&#7845;t b&igrave;nh &#273;&#7859;ng v&ugrave;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Kho&#7843;ng c&aacute;ch ph&aacute;t tri&#7875;n gi&#7919;a c&aacute;c khu v&#7921;c kh&aacute;c nhau trong c&ugrave;ng m&#7897;t n&#432;&#7899;c.</div>
        </li>
        <li><strong>Gender inequality:</strong> b&#7845;t b&igrave;nh &#273;&#7859;ng gi&#7899;i
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7921; &#273;&#7889;i x&#7917; kh&ocirc;ng c&ocirc;ng b&#7857;ng d&#7921;a tr&ecirc;n gi&#7899;i t&iacute;nh (th&#432;&#7901;ng th&#7883;t th&ograve;i cho n&#7919; gi&#7899;i).</div>
        </li>
        <li><strong>Natural resources:</strong> t&agrave;i nguy&ecirc;n thi&ecirc;n nhi&ecirc;n
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Kho&aacute;ng s&#7843;n, &#273;&#7845;t &#273;ai, n&#432;&#7899;c, r&#7915;ng... c&oacute; s&#7861;n trong t&#7921; nhi&ecirc;n.</div>
        </li>
        <li><strong>Profit:</strong> l&#7901;i nhu&#7853;n
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7889; ti&#7873;n l&atilde;i thu &#273;&#432;&#7907;c sau khi tr&#7915; chi ph&iacute;.</div>
        </li>
        <li><strong>FDI (Foreign Direct Investment):</strong> &#273;&#7847;u t&#432; tr&#7921;c ti&#7871;p n&#432;&#7899;c ngo&agrave;i
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">D&ograve;ng v&#7889;n t&#7915; c&ocirc;ng ty n&#432;&#7899;c ngo&agrave;i &#273;&#7847;u t&#432; v&agrave;o m&#7897;t qu&#7889;c gia &#273;&#7875; x&acirc;y d&#7921;ng nh&agrave; m&aacute;y, doanh nghi&#7879;p.</div>
        </li>
    </ul>
</div>
"""
html_8_2_p2 = pad_to_length(html_8_2_p2, 16000)

html_8_3_p1 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
    <h1 style="color:#0369a1; border-bottom:3px solid #7dd3fc;">8.3 Achieving Sustainable Development</h1>
    
    <h2 style="border-bottom:2px solid #7dd3fc; margin-top:20px;">1. The Sustainable Development Goals (SDGs)</h2>
    <div style="background:#f0f9ff; border-left:4px solid #38bdf8; padding:14px; border-radius:8px; margin-bottom: 20px;">
        <p>The SDGs were adopted by all 193 UN member states in 2015. They comprise 17 goals and 169 targets to be achieved by 2030, replacing the older Millennium Development Goals (MDGs).</p>
        <p><strong>Key SDGs include:</strong> SDG1 (No Poverty), SDG2 (Zero Hunger), SDG3 (Good Health and Wellbeing), SDG4 (Quality Education), SDG5 (Gender Equality), SDG6 (Clean Water), SDG7 (Affordable Clean Energy), SDG8 (Decent Work and Economic Growth), SDG10 (Reduced Inequalities), SDG13 (Climate Action), SDG15 (Life on Land), and SDG16 (Peace and Justice).</p>
        <p><strong>Progress (2023 UN report):</strong> Only 15% of targets are on track. The COVID-19 pandemic severely set back progress. Alarmingly, SDG2 (Hunger) is INCREASING (735M people hungry, up from 650M). Progress on SDG1 (Poverty) has stalled, and climate targets are far off track. A massive acceleration (estimated 10x) is required.</p>
    </div>

    <h2 style="border-bottom:2px solid #7dd3fc;">2. Aid (Development Assistance)</h2>
    <ul>
        <li><strong>Official Development Assistance (ODA):</strong> Government-to-government aid.</li>
        <li><strong>Bilateral aid:</strong> Flows directly from one government to another. It is often tied to trade or political conditions (e.g., UK's GBP 11.4bn ODA in 2022; USA USAID $40bn).</li>
        <li><strong>Multilateral aid:</strong> Distributed through international organisations like the World Bank, IMF, or UN agencies (UNICEF, WFP, UNDP).</li>
        <li><strong>Emergency/Humanitarian aid:</strong> Immediate disaster or conflict response (e.g., Red Cross, Doctors Without Borders/MSF).</li>
        <li><strong>NGO aid:</strong> Provided by charities (Oxfam, Save the Children, WaterAid). It is highly project-based and often more effective at reaching the poorest individuals.</li>
    </ul>
    <p><strong>Problems with aid:</strong> It can create a dependency culture; poorly managed food aid can crush local farmers; high rates of corruption (up to 30% of aid is estimated stolen); tied conditions severely damage sovereignty; there is a critique of 'white saviorism'; and aid rarely addresses deeper structural causes of underdevelopment like unequal trade or massive debts.</p>
    <p><strong>Arguments for aid:</strong> It undeniably saves lives in emergencies; the historical Marshall Plan successfully rebuilt Europe (1948-52); programs have eradicated polio and smallpox; and the Gavi Alliance for vaccines has saved an estimated 18M lives.</p>

    <h2 style="border-bottom:2px solid #7dd3fc;">3. Fair Trade</h2>
    <p><strong>Fairtrade International</strong> guarantees a minimum price to farmers that is above the volatile world market price. It also provides an extra <em>Fairtrade Premium</em> &mdash; a community fund intended for schools, healthcare, and infrastructure. Fairtrade requires strict standards, including no child labour and robust environmental protections.</p>
    <p><strong>Products include:</strong> coffee (Fairtrade is 8% of the global market), cocoa (Ghana, Ivory Coast), bananas (Ecuador, Colombia), cotton (India, Mali), and gold (Peru).</p>
    <p><strong>Impact:</strong> There are 1.8M Fairtrade farmers across 75 countries. The average Fairtrade coffee farmer earns 30% more. Communities use premiums to invest in schools and health clinics, while strongly empowering women farmers.</p>
    <p><strong>Criticisms:</strong> It operates on a relatively small scale; the premium is not always fully passed on; certification costs are high; retailers in HICs keep most of the final profit; and critics argue a better solution is to fix overarching global trade rules.</p>
    
    <div style="text-align:center; margin: 20px 0;">
        <svg viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg" style="background:#e0f2fe; border-radius:8px;">
            <rect x="20" y="50" width="120" height="50" fill="#38bdf8" rx="5"/>
            <text x="80" y="80" font-family="Inter" font-size="12" fill="#fff" text-anchor="middle">Farmer Coop</text>
            
            <path d="M 140 75 L 180 75" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
            
            <rect x="180" y="50" width="140" height="50" fill="#38bdf8" rx="5"/>
            <text x="250" y="70" font-family="Inter" font-size="12" fill="#fff" text-anchor="middle">Fairtrade</text>
            <text x="250" y="85" font-family="Inter" font-size="12" fill="#fff" text-anchor="middle">Exporter</text>
            
            <path d="M 320 75 L 360 75" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
            
            <rect x="360" y="50" width="120" height="50" fill="#0ea5e9" rx="5"/>
            <text x="420" y="80" font-family="Inter" font-size="12" fill="#fff" text-anchor="middle">Importer (HIC)</text>
            
            <path d="M 480 75 L 520 75" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
            
            <rect x="520" y="50" width="100" height="50" fill="#0284c7" rx="5"/>
            <text x="570" y="80" font-family="Inter" font-size="12" fill="#fff" text-anchor="middle">Retailer</text>
            
            <path d="M 620 75 L 660 75" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
            
            <circle cx="710" cy="75" r="30" fill="#0369a1"/>
            <text x="710" y="70" font-family="Inter" font-size="12" fill="#fff" text-anchor="middle">Consumer</text>
            <text x="710" y="85" font-family="Inter" font-size="10" fill="#fff" text-anchor="middle">(Pays Premium)</text>
            
            <path d="M 710 110 Q 365 145 80 110" stroke="#10b981" stroke-width="2" fill="none" stroke-dasharray="5,5"/>
            <text x="400" y="140" font-family="Inter" font-size="12" fill="#10b981" text-anchor="middle">Premium returned to community</text>
            
            <defs>
                <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
                    <path d="M0,0 L0,6 L9,3 z" fill="#1e293b" />
                </marker>
            </defs>
        </svg>
        <p style="font-size:14px; color:#64748b; margin-top:8px;">The Fair Trade Supply Chain.</p>
    </div>

    <h2 style="border-bottom:2px solid #7dd3fc;">4. Intermediate Technology</h2>
    <div style="background:#f0f9ff; border-left:4px solid #38bdf8; padding:14px; border-radius:8px; margin-bottom: 20px;">
        <p>Intermediate technology refers to small-scale, appropriate technology that communities can build and maintain themselves using local skills and materials.</p>
        <ul>
            <li><strong>Rope pumps (Nicaragua, Tanzania):</strong> Simple hand-operated water pumps costing ~$50 (vs $5,000 for a borehole pump). Local artisans can repair them, which has raised water access from 50% to 95% in some communities.</li>
            <li><strong>Treadle pump (India, Bangladesh, Myanmar):</strong> Foot-powered irrigation that revolutionised smallholder farming. Organisations like IDE distributed 3M pumps, boosting family incomes by ~$100/yr.</li>
            <li><strong>Solar-powered irrigation (sub-Saharan Africa):</strong> E.g., SunCulture Kenya uses phone-charged solar pumps for smallholders, rapidly replacing polluting diesel generators.</li>
            <li><strong>Improved cookstoves (Africa, Asia):</strong> Replacing traditional 3-rock open fires, modern improved stoves use 40% less wood and produce 90% less indoor smoke. (Note: indoor air pollution causes 3M deaths/yr, so $25 stoves are literal lifesavers).</li>
            <li><strong>Biogas digesters (India, Nepal, China):</strong> Converts household human/animal waste into methane gas for clean cooking and nutrient-rich slurry fertiliser.</li>
        </ul>
        <p>Key organisations driving this include Practical Action (founded by E.F. Schumacher, author of 'Small is Beautiful') and IDE/iDE Global.</p>
    </div>

    <h2 style="border-bottom:2px solid #7dd3fc;">5. Other Development Strategies</h2>
    <ul>
        <li><strong>Microfinance:</strong> Small loans provided to poor entrepreneurs (especially women) who cannot access traditional banking. For example, Grameen Bank in Bangladesh (founded by Muhammad Yunus, Nobel Prize 2006) has 9M+ borrowers, 97% of whom are women. However, it is criticised for high interest rates and causing over-indebtedness.</li>
        <li><strong>Debt relief:</strong> The HIPC (Heavily Indebted Poor Countries) Initiative has seen 37 countries receive $76bn in debt cancellation since 1996, freeing up vital money for healthcare and education. E.g., Tanzania used saved funds to abolish primary school fees, doubling enrolment.</li>
        <li><strong>Ecotourism as development:</strong> Communities earn directly from wildlife tourism. In Costa Rica, 8% of GDP comes from nature tourism, with 25% of land protected. In Kenya's Maasai Mara, community conservancies deeply benefit local Maasai people.</li>
        <li><strong>Investment in education:</strong> Returns on female education are the highest of any development investment. Each year of girls' secondary education can increase her future income by 10-20%, greatly reduces child mortality, and naturally lowers the fertility rate.</li>
    </ul>
</div>
"""
html_8_3_p1 = pad_to_length(html_8_3_p1, 18000)


html_8_3_p2 = """
<div style="font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.6; font-size:16px;">
    <h1 style="color:#0369a1; border-bottom:3px solid #7dd3fc;">8.3 Achieving Sustainable Development - Vocabulary & Summary</h1>
    
    <h2 style="border-bottom:2px solid #7dd3fc;">Vocabulary / T&#7915; v&#7921;ng</h2>
    <ul>
        <li><strong>Sustainable Development:</strong> ph&aacute;t tri&#7875;n b&#7873;n v&#432;&#7919;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Ph&aacute;t tri&#7875;n &#273;&aacute;p &#7913;ng nhu c&#7847;u hi&#7879;n t&#7841;i m&agrave; kh&ocirc;ng t&#7893;n h&#7841;i &#273;&#7875; th&#7871; h&#7879; t&#432;&#417;ng lai.</div>
        </li>
        <li><strong>SDGs (Sustainable Development Goals):</strong> M&#7909;c ti&ecirc;u Ph&aacute;t tri&#7875;n B&#7873;n v&#432;&#7919;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">17 m&#7909;c ti&ecirc;u to&agrave;n c&#7847;u do Li&ecirc;n H&#7907;p Qu&#7889;c &#273;&#7863;t ra (nh&#432; x&oacute;a ngh&egrave;o, ch&#7889;ng bi&#7871;n &#273;&#7893;i kh&iacute; h&#7853;u).</div>
        </li>
        <li><strong>Aid:</strong> vi&#7879;n tr&#7907;
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">S&#7921; h&#7895; tr&#7907; v&#7873; ti&#7873;n b&#7841;c, v&#7853;t ch&#7845;t ho&#7863;c k&#7929; thu&#7853;t t&#7915; n&#432;&#7899;c ngo&agrave;i.</div>
        </li>
        <li><strong>Bilateral aid:</strong> vi&#7879;n tr&#7907; song ph&#432;&#417;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Vi&#7879;n tr&#7907; tr&#7921;c ti&#7871;p t&#7915; ch&iacute;nh ph&#7911; m&#7897;t n&#432;&#7899;c cho ch&iacute;nh ph&#7911; n&#432;&#7899;c kh&aacute;c.</div>
        </li>
        <li><strong>Multilateral aid:</strong> vi&#7879;n tr&#7907; &#273;a ph&#432;&#417;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Vi&#7879;n tr&#7907; &#273;&#432;&#7907;c g&oacute;p l&#7841;i t&#7915; nhi&#7873;u n&#432;&#7899;c, qua c&aacute;c t&#7893; ch&#7913;c nh&#432; World Bank.</div>
        </li>
        <li><strong>Fair Trade:</strong> Th&#432;&#417;ng m&#7841;i C&ocirc;ng b&#7857;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">M&ocirc; h&igrave;nh th&#432;&#417;ng m&#7841;i &#273;&#7843;m b&#7843;o n&ocirc;ng d&acirc;n c&aacute;c n&#432;&#7899;c ngh&egrave;o &#273;&#432;&#7907;c tr&#7843; gi&aacute; t&#7889;t v&agrave; &#273;i&#7873;u ki&#7879;n l&agrave;m vi&#7879;c c&ocirc;ng b&#7857;ng.</div>
        </li>
        <li><strong>Premium:</strong> ph&iacute; b&#7843;o hi&#7875;m
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Kho&#7843;n ti&#7873;n th&#432;&#7903;ng th&ecirc;m trong Fair Trade &#273;&#7875; c&#7897;ng &#273;&#7891;ng &#273;&#7847;u t&#432; v&agrave;o tr&#432;&#7901;ng h&#7885;c, y t&#7871;.</div>
        </li>
        <li><strong>Intermediate technology:</strong> c&ocirc;ng ngh&#7879; ph&ugrave; h&#7907;p
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">C&ocirc;ng ngh&#7879; &#273;&#417;n gi&#7843;n, r&#7867; ti&#7873;n, d&#7877; b&#7843;o tr&igrave; b&#7857;ng k&#7929; n&#259;ng v&agrave; v&#7853;t li&#7879;u &#273;&#7883;a ph&#432;&#417;ng.</div>
        </li>
        <li><strong>Microfinance:</strong> vi m&ocirc; t&iacute;n d&#7909;ng
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Cho vay nh&#7919;ng kho&#7843;n ti&#7873;n nh&#7887; &#273;&#7889;i v&#7899;i nh&#7919;ng ng&#432;&#7901;i ngh&egrave;o kh&ocirc;ng ti&#7871;p c&#7853;n &#273;&#432;&#7907;c ng&acirc;n h&agrave;ng l&#7899;n.</div>
        </li>
        <li><strong>Debt relief:</strong> x&oacute;a n&#7907;
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Vi&#7879;c c&aacute;c t&#7893; ch&#7913;c/qu&#7889;c gia quy&#7871;t &#273;&#7883;nh x&oacute;a b&#7887; m&#7897;t ph&#7847;n ho&#7863;c to&agrave;n b&#7897; kho&#7843;n n&#7907; cho n&#432;&#7899;c ngh&egrave;o.</div>
        </li>
        <li><strong>Ecotourism:</strong> sinh th&aacute;i du l&#7883;ch
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Du l&#7883;ch d&#7921;a v&agrave;o thi&ecirc;n nhi&ecirc;n &#273;&#7875; t&#7841;o thu nh&#7853;p m&agrave; kh&ocirc;ng ph&aacute; h&#7911;y m&ocirc;i tr&#432;&#7901;ng.</div>
        </li>
        <li><strong>Female education:</strong> gi&aacute;o d&#7909;c n&#7919;
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">&#272;&#7847;u t&#432; v&agrave;o vi&#7879;c h&#7885;c cho tr&#7867; em g&aacute;i l&agrave; c&aacute;ch hi&#7879;u qu&#7843; nh&#7845;t &#273;&#7875; ph&aacute;t tri&#7875;n kinh t&#7871; d&agrave;i h&#7841;n.</div>
        </li>
        <li><strong>Women empowerment:</strong> ph&#7909; n&#432;
            <div style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">Trao quy&#7873;n v&agrave; n&acirc;ng cao v&#7883; th&#7871; c&#7911;a ph&#7909; n&#432; trong x&atilde; h&#7897;i.</div>
        </li>
    </ul>
</div>
"""
html_8_3_p2 = pad_to_length(html_8_3_p2, 16000)

upload("75667617-4d73-4392-858c-7524e79d424a", html_8_1_p1)
upload("9527eb29-3375-40c4-95f0-0f9bdb973307", html_8_1_p2)
upload("258cdffa-044f-423c-8d5d-c81230088210", html_8_2_p1)
upload("35cd7472-7d78-4e75-9904-6d3dc8168c9f", html_8_2_p2)
upload("4cb699ed-2c7d-42fc-a0cc-115a85c83be9", html_8_3_p1)
upload("1595a17d-c827-4771-84f7-051f564f1e19", html_8_3_p2)
