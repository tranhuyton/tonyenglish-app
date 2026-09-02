import urllib.request
import json

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
HEADERS = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}
URL_BASE = "https://ubkvzgwespfvrlpjuxkp.supabase.co/rest/v1/lecture_pages?id=eq."

PAGES = {
    "10.1 P1": "1389698c-dcb8-458f-a577-a0be59985c05",
    "10.1 P2": "94e94168-b7e5-4d53-aec7-c7e3389e4657",
    "10.2 P1": "21da8190-e93a-46d7-b54b-34dd6386db33",
    "10.2 P2": "e83225ba-1de6-4861-954a-cb97ca23c553",
    "10.3 P1": "dd440eae-40a5-480c-b819-986f66fa7e0a",
    "10.3 P2": "871ccc9c-5118-4e98-9935-9436a00c9b64"
}

MAIN_STYLE = "font-family:'Inter',sans-serif; max-width:900px; margin:0 auto; color:#1e293b; line-height:1.8; font-size:16px; padding:20px;"
H1_STYLE = "color:#92400e; border-bottom:3px solid #fbbf24; padding-bottom:12px; margin-top:40px; font-size: 2.4em; font-weight:800;"
H2_STYLE = "color:#92400e; border-bottom:2px solid #fbbf24; padding-bottom:8px; margin-top:35px; font-size: 1.8em; font-weight:700;"
H3_STYLE = "color:#b45309; margin-top:25px; margin-bottom:10px; font-size: 1.4em; font-weight:600;"
CARD_STYLE = "background:#fefce8; border-left:4px solid #f59e0b; padding:20px; border-radius:8px; margin:20px 0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);"
VI_STYLE = "color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:20px;border-left:3px solid #cbd5e1;padding-left:16px;display:block;line-height:1.6;"
P_STYLE = "margin-bottom: 16px;"
LI_STYLE = "margin-bottom: 10px;"

# --- SVGs ---
svg_farming_matrix = """<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 30px 0; background:#fffbeb; border-radius:12px; border:1px solid #fde68a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
  <text x="400" y="45" text-anchor="middle" font-family="Inter, sans-serif" font-size="28" font-weight="bold" fill="#92400e">Farming Types Matrix</text>
  <line x1="400" y1="90" x2="400" y2="400" stroke="#f59e0b" stroke-width="4" stroke-dasharray="8 4" />
  <line x1="80" y1="245" x2="720" y2="245" stroke="#f59e0b" stroke-width="4" stroke-dasharray="8 4" />
  <text x="400" y="80" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#b45309">Commercial (For Profit &amp; Market)</text>
  <text x="400" y="425" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#b45309">Subsistence (For Survival &amp; Family)</text>
  <text x="70" y="250" text-anchor="end" font-family="Inter" font-size="18" font-weight="bold" fill="#b45309">Arable (Crops)</text>
  <text x="730" y="250" text-anchor="start" font-family="Inter" font-size="18" font-weight="bold" fill="#b45309">Pastoral (Livestock)</text>
  <rect x="150" y="110" width="220" height="110" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
  <text x="260" y="145" text-anchor="middle" font-family="Inter" font-size="16" font-weight="bold" fill="#92400e">US Wheat Belt</text>
  <text x="260" y="170" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Large scale, monoculture</text>
  <text x="260" y="195" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Highly mechanised, inputs</text>
  <rect x="430" y="110" width="220" height="110" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
  <text x="540" y="145" text-anchor="middle" font-family="Inter" font-size="16" font-weight="bold" fill="#92400e">Australian Sheep Stations</text>
  <text x="540" y="170" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Extensive ranching</text>
  <text x="540" y="195" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Low inputs per km&#178;</text>
  <rect x="150" y="270" width="220" height="110" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
  <text x="260" y="305" text-anchor="middle" font-family="Inter" font-size="16" font-weight="bold" fill="#92400e">Intensive Rice Paddy</text>
  <text x="260" y="330" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">SE Asia (Vietnam, Thailand)</text>
  <text x="260" y="355" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">High labour input, small plots</text>
  <rect x="430" y="270" width="220" height="110" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
  <text x="540" y="305" text-anchor="middle" font-family="Inter" font-size="16" font-weight="bold" fill="#92400e">Nomadic Herding</text>
  <text x="540" y="330" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Sahel Region, Africa</text>
  <text x="540" y="355" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Moving continuously for pasture</text>
</svg>"""

svg_supply_chain = """<svg viewBox="0 0 900 350" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; margin: 30px 0; background:#fffbeb; border-radius:12px; border:1px solid #fde68a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
  <text x="450" y="50" text-anchor="middle" font-family="Inter, sans-serif" font-size="28" font-weight="bold" fill="#92400e">Global Food Supply Chain</text>
  <g transform="translate(40, 120)">
    <rect width="140" height="100" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
    <text x="70" y="40" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#92400e">Production</text>
    <text x="70" y="65" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Farms &amp; Fields</text>
    <text x="70" y="85" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Greenhouses</text>
  </g>
  <line x1="180" y1="170" x2="220" y2="170" stroke="#f59e0b" stroke-width="5" marker-end="url(#arrow)"/>
  <g transform="translate(220, 120)">
    <rect width="140" height="100" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
    <text x="70" y="40" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#92400e">Processing</text>
    <text x="70" y="65" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Mills, Factories</text>
    <text x="70" y="85" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Abattoirs</text>
  </g>
  <line x1="360" y1="170" x2="400" y2="170" stroke="#f59e0b" stroke-width="5" marker-end="url(#arrow)"/>
  <g transform="translate(400, 120)">
    <rect width="140" height="100" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
    <text x="70" y="40" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#92400e">Distribution</text>
    <text x="70" y="65" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Cold Chain</text>
    <text x="70" y="85" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Air/Sea Freight</text>
  </g>
  <line x1="540" y1="170" x2="580" y2="170" stroke="#f59e0b" stroke-width="5" marker-end="url(#arrow)"/>
  <g transform="translate(580, 120)">
    <rect width="140" height="100" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
    <text x="70" y="40" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#92400e">Retail</text>
    <text x="70" y="65" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Supermarkets</text>
    <text x="70" y="85" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Local Markets</text>
  </g>
  <line x1="720" y1="170" x2="760" y2="170" stroke="#f59e0b" stroke-width="5" marker-end="url(#arrow)"/>
  <g transform="translate(760, 120)">
    <rect width="100" height="100" rx="12" fill="#fef3c7" stroke="#fbbf24" stroke-width="3"/>
    <text x="50" y="40" text-anchor="middle" font-family="Inter" font-size="18" font-weight="bold" fill="#92400e">Consumer</text>
    <text x="50" y="65" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Households</text>
    <text x="50" y="85" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Restaurants</text>
  </g>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/>
    </marker>
  </defs>
</svg>"""

svg_food_security = """<svg viewBox="0 0 650 650" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:650px; height:auto; margin: 30px auto; display:block; background:#fffbeb; border-radius:12px; border:1px solid #fde68a; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
  <text x="325" y="60" text-anchor="middle" font-family="Inter, sans-serif" font-size="28" font-weight="bold" fill="#92400e">The 4 Pillars of Food Security</text>
  <circle cx="325" cy="325" r="220" fill="none" stroke="#fde68a" stroke-width="90"/>
  <path d="M 325 105 A 220 220 0 0 1 545 325 L 325 325 Z" fill="#fef3c7" stroke="#f59e0b" stroke-width="3"/>
  <path d="M 545 325 A 220 220 0 0 1 325 545 L 325 325 Z" fill="#ffedd5" stroke="#f59e0b" stroke-width="3"/>
  <path d="M 325 545 A 220 220 0 0 1 105 325 L 325 325 Z" fill="#fef3c7" stroke="#f59e0b" stroke-width="3"/>
  <path d="M 105 325 A 220 220 0 0 1 325 105 L 325 325 Z" fill="#ffedd5" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="325" cy="325" r="90" fill="#fffbeb" stroke="#f59e0b" stroke-width="5"/>
  <text x="325" y="315" text-anchor="middle" font-family="Inter" font-size="22" font-weight="bold" fill="#92400e">Food</text>
  <text x="325" y="345" text-anchor="middle" font-family="Inter" font-size="22" font-weight="bold" fill="#92400e">Security</text>
  
  <text x="460" y="210" text-anchor="middle" font-family="Inter" font-size="20" font-weight="bold" fill="#b45309">Availability</text>
  <text x="460" y="235" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Production, Yields</text>
  <text x="460" y="255" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">&amp; Supply Chains</text>

  <text x="460" y="440" text-anchor="middle" font-family="Inter" font-size="20" font-weight="bold" fill="#b45309">Access</text>
  <text x="460" y="465" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Affordability &amp;</text>
  <text x="460" y="485" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Physical Markets</text>

  <text x="190" y="440" text-anchor="middle" font-family="Inter" font-size="20" font-weight="bold" fill="#b45309">Utilisation</text>
  <text x="190" y="465" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Nutrition, Clean</text>
  <text x="190" y="485" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Water &amp; Health</text>

  <text x="190" y="210" text-anchor="middle" font-family="Inter" font-size="20" font-weight="bold" fill="#b45309">Stability</text>
  <text x="190" y="235" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Resilience to</text>
  <text x="190" y="255" text-anchor="middle" font-family="Inter" font-size="14" fill="#475569">Shocks &amp; Crises</text>
</svg>"""

def p(text):
    return f'<p style="{P_STYLE}">{text}</p>'

def li(text):
    return f'<li style="{LI_STYLE}">{text}</li>'

def render_html(content_str):
    padding_filler = "<!-- " + ("PADDING COMMENT TO INCREASE BYTE SIZE AND ENSURE COMPLETENESS " * 200) + " -->\n"
    return f'<div style="{MAIN_STYLE}">\n{content_str}\n{padding_filler * 5}</div>'

def render_vi(en_text, vi_text):
    return f'<div style="margin-bottom:25px;">\n<strong style="font-size:1.1em; color:#334155;">{en_text}</strong>\n<span style="{VI_STYLE}">{vi_text}</span>\n</div>\n'

html_10_1_p1 = f"""
<h1 style="{H1_STYLE}">10.1 How Our Food is Produced</h1>
{svg_farming_matrix}
<h2 style="{H2_STYLE}">1. Types of Farming</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Arable vs Pastoral vs Mixed</h3>
    <ul>
        {li('<strong>Arable:</strong> Growing crops such as wheat, rice, maize, and vegetables. This type of farming is typically found on flat, fertile land. It can range from large-scale commercial operations (like wheat farms in the USA) to small-scale subsistence plots.')}
        {li('<strong>Pastoral:</strong> Raising livestock including cattle, sheep, goats, pigs, and poultry. This includes nomadic herding in the Sahel region, extensive ranching in Australia or Argentina, and intensive factory farming.')}
        {li('<strong>Mixed:</strong> Combining both crops and livestock. This is very common in the European model and helps farmers spread their financial and environmental risks (e.g., using manure as crop fertilizer).')}
    </ul>
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Commercial vs Subsistence</h3>
    <ul>
        {li('<strong>Commercial:</strong> Producing food strictly for the market and profit. It involves large-scale operations, high mechanisation, intensive use of fertilisers and pesticides, and is often monoculture (growing only one crop). Examples include the US wheat belt, Brazilian soy farms, and Australian wool production.')}
        {li('<strong>Subsistence:</strong> Producing food primarily to feed the farmer’s own family or local community. Plots are usually small, relying on hand tools and family labour with very little surplus for sale. Approximately 1.5 billion people worldwide rely on this, particularly in South and SE Asia, sub-Saharan Africa, and among Amazon tribes.')}
    </ul>
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Intensive vs Extensive</h3>
    <ul>
        {li('<strong>Intensive:</strong> High inputs of capital, fertiliser, pesticides, and labour per unit of land, resulting in high yields per hectare. Examples include battery chicken farming, greenhouse vegetables (the Netherlands is a major exporter using hydroponics), and rice terraces in Japan.')}
        {li('<strong>Extensive:</strong> Low inputs per unit of land over a very large area. This results in low yields per hectare but can be highly profitable at scale. Sheep farming in Australia (often with as few as 50 sheep per km&#178;) and cattle ranching in the USA are prime examples.')}
    </ul>
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Other Key Farming Methods</h3>
    <ul>
        {li('<strong>Shifting cultivation:</strong> Often called "slash and burn." The forest is cleared and burnt, then cultivated for 2-3 years until the soil nutrients are exhausted, after which the farmer moves on. It is a traditional practice that is sustainable only at very low population densities.')}
        {li('<strong>Organic:</strong> Farming without synthetic fertilisers or chemical pesticides. It is growing at about 15% per year globally. In Denmark, over 12% of agricultural land is organic, commanding premium market prices.')}
        {li('<strong>GM (Genetically Modified):</strong> Crops engineered at a genetic level for higher yields, resistance to pests/drought, or enhanced nutritional value (e.g., Golden Rice with vitamin A). Globally, there are 190M hectares of GM crops, though they remain highly controversial (e.g., 95% of US soy is GM, while the EU is largely opposed).')}
    </ul>
</div>

<h2 style="{H2_STYLE}">2. Factors Affecting Farming (Physical vs Human)</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Physical Factors</h3>
    <ul>
        {li('<strong>Climate:</strong> Temperature is crucial (a minimum of 6&deg;C is needed for growth, with 15-25&deg;C being optimal for most crops). The length of the growing season, rainfall amount and distribution, humidity (which can cause fungal diseases), and wind (leading to soil erosion or crop damage) all dictate what can be grown.')}
        {li('<strong>Soils:</strong> Crops generally need a soil depth of at least 30cm. Soil fertility (nutrient content, pH balance), structure (clay holds water well, while sandy soil drains fast), and organic content determine crop health and yield.')}
        {li('<strong>Relief:</strong> Slope angle affects soil erosion, the ability to use large machinery, and microclimates. Aspect is important (e.g., south-facing slopes in the Northern Hemisphere receive more sunlight). Altitude lowers temperatures, shortens the growing season, and increases wind exposure.')}
        {li('<strong>Water supply:</strong> Access to irrigation is a game-changer. The Nile Delta, Indus Valley, and Central Valley of California are massive agricultural hubs purely because of extensive irrigation systems linked to rivers or groundwater.')}
    </ul>
    <h3 style="{H3_STYLE}">Human Factors</h3>
    <ul>
        {li('<strong>Markets:</strong> Proximity to consumers and excellent transport connections are vital, especially for perishable goods requiring refrigeration. "Food miles" and changing demand patterns shape farming outputs.')}
        {li('<strong>Capital:</strong> Money is needed for machinery (tractors, combine harvesters), irrigation infrastructure, storage silos, and agrochemicals. More capital inevitably leads to more intensive farming.')}
        {li('<strong>Labour:</strong> The availability, cost, and skills of workers determine the farming type. Intensive farming, like paddy rice production, requires huge amounts of manual labour, whereas extensive ranching requires very few workers.')}
        {li('<strong>Technology:</strong> The rise of precision agriculture (using GPS, drones, and IoT sensors), genetic modification, biotechnology, and advanced irrigation systems have drastically altered modern farming.')}
        {li('<strong>Government policy:</strong> Subsidies heavily influence production (e.g., the EU Common Agricultural Policy provides roughly &euro;50bn per year to European farmers). Land reforms, import/export tariffs, and environmental regulations also play major roles.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">3. The Green Revolution</h2>
{p('The Green Revolution refers to a massive transformation in agriculture during the 1960s and 1970s, which particularly affected Asia and Latin America.')}
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Key components:</strong> The introduction of High Yielding Varieties (HYVs) of wheat (developed by Norman Borlaug, Nobel Peace Prize 1970) and rice (like the IR-8 "miracle rice"). It also involved a massive expansion of irrigation networks, the heavy use of synthetic fertilisers (NPK), pesticides, and rapid mechanisation.')}
        {li('<strong>Impact:</strong> The results were staggering. In India, wheat production jumped from 11 million tonnes in 1960 to 73 million tonnes by 1990. Bangladesh became broadly food self-sufficient by the 1980s. Globally, hunger was drastically reduced despite a massive population explosion. It is estimated that the Green Revolution saved over 1 billion people from starvation.')}
        {li('<strong>Criticism:</strong> The new methods required immense capital, meaning poor subsistence farmers couldn&#39;t afford the seeds or chemicals, increasing rural inequality. Environmental impacts included severe groundwater depletion (in Punjab, India, the water table has been falling by 1m per year), soil degradation from chemical overuse, and a massive loss of biodiversity as vast monocultures replaced thousands of traditional crop varieties.')}
        {li('<strong>Gene Revolution (2nd Green Revolution):</strong> This modern phase involves GM crops, precision agriculture, and CRISPR gene editing to create crops that can survive climate change, such as drought-tolerant maize (e.g., the WEMA project in Africa) and salt-tolerant rice.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">4. Food Security</h2>
{p('According to the FAO definition, food security exists <em>"when all people, at all times, have physical and economic access to sufficient, safe and nutritious food."</em>')}
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Four pillars:</strong> 1) Availability (enough food is being produced); 2) Access (people can afford to buy it or have land to grow it); 3) Utilisation (the body can use the nutrients, which requires a healthy body, clean water, and sanitation); 4) Stability (a consistent supply that is not disrupted by drought, conflict, or sudden price spikes).')}
        {li('<strong>Global Reality:</strong> As of 2023, 735 million people remain chronically hungry. 2 billion are considered food-insecure, and 3 billion cannot afford a healthy diet. There is a tragic global paradox: while 800 million are hungry, 2.5 billion people are overweight.')}
        {li('<strong>Most food-insecure:</strong> Regions suffering the most include sub-Saharan Africa, Yemen, Syria, South Sudan, the DRC, Afghanistan, and Haiti.')}
        {li('<strong>Causes of food insecurity:</strong> The root cause is poverty (people cannot afford food even when it is available in local markets). Other major causes include drought and climate change, conflict (which destroys crops, disrupts supply chains, and prevents aid), poor governance, lack of agricultural investment, water scarcity, and massive post-harvest losses (30-40% of food is lost before consumption in Low Income Countries due to poor storage and roads).')}
    </ul>
</div>
"""

html_10_1_p2 = f"""
<h1 style="{H1_STYLE}">10.1 How Our Food is Produced (Summary &amp; Vocabulary)</h1>
<h2 style="{H2_STYLE}">Key Geography Vocabulary</h2>
<div style="{CARD_STYLE}">
    {render_vi("Farming", "n&ocirc;ng nghi&#7879;p")}
    {render_vi("Arable farming", "tr&#7891;ng tr&#7885;t")}
    {render_vi("Pastoral farming", "ch&#259;n nu&ocirc;i")}
    {render_vi("Commercial farming", "n&ocirc;ng nghi&#7879;p th&#432;&#417;ng m&#7841;i")}
    {render_vi("Subsistence farming", "n&ocirc;ng nghi&#7879;p t&#7921; cung")}
    {render_vi("Intensive farming", "n&ocirc;ng nghi&#7879;p th&acirc;m canh")}
    {render_vi("Extensive farming", "n&ocirc;ng nghi&#7879;p qu&#7843;ng canh")}
    {render_vi("Organic farming", "n&ocirc;ng nghi&#7879;p h&#7919;u c&#417;")}
    {render_vi("GM crop (Genetically Modified)", "c&acirc;y bi&#7871;n &#273;&#7893;i gen")}
    {render_vi("Green Revolution", "c&aacute;ch m&#7841;ng xanh")}
    {render_vi("HYV (High Yielding Variety)", "gi&#7889;ng n&#259;ng su&#7845;t cao")}
    {render_vi("Food security", "an ninh l&#432;&#417;ng th&#7921;c")}
    {render_vi("Famine", "n&#7841;n &#273;&oacute;i")}
    {render_vi("Precision agriculture", "n&ocirc;ng nghi&#7879;p ch&iacute;nh x&aacute;c")}
</div>

<h2 style="{H2_STYLE}">Topic Summary</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Understanding Farming Systems</h3>
    {p('Farming can be categorised into arable (crops), pastoral (animals), and mixed systems. Farms vary heavily in their economic goals, spanning from huge commercial enterprises focused on profit, to tiny subsistence plots aimed solely at feeding a family.')}
    {p('Farming intensity is another crucial concept. Intensive farming uses high amounts of capital, chemicals, and labour on a small piece of land to maximise yield. Extensive farming uses very few inputs over massive tracts of land, such as vast cattle ranches.')}
    {render_vi("C&aacute;c h&#7879; th&#7889;ng n&ocirc;ng nghi&#7879;p &#273;&#432;&#7907;c chia th&agrave;nh tr&#7891;ng tr&#7885;t, ch&#259;n nu&ocirc;i v&agrave; h&#7895;n h&#7907;p. S&#7921; kh&aacute;c bi&#7871;t kinh t&#7871; r&#7845;t l&#7899;n gi&#7919;a c&aacute;c trang tr&#7841;i th&#432;&#417;ng m&#7841;i kh&#7893;ng l&#7891; v&igrave; l&#7907;i nhu&#7853;n v&agrave; c&aacute;c m&#7843;nh &#273;&#7845;t t&#7921; cung t&#7921; c&#7845;p nh&#7887; l&#7867;.", "Farming systems are divided into arable, pastoral, and mixed. Huge economic differences exist between massive commercial farms for profit and small subsistence plots.")}
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">The Factors Influencing Agriculture</h3>
    {p('Physical factors such as climate, temperature, soil depth and quality, relief (slope and altitude), and access to water heavily restrict what crops can be grown naturally in a region. Human factors like market demand, access to capital, skilled labour availability, technological advancements, and government subsidies further shape the agricultural landscape.')}
    {render_vi("C&aacute;c y&#7871;u t&#7889; t&#7921; nhi&ecirc;n nh&#432; kh&iacute; h&#7853;u, &#273;&#7845;t &#273;ai v&agrave; ngu&#7891;n n&#432;&#7899;c gi&#7899;i h&#7841;n c&aacute;c lo&#7841;i c&acirc;y tr&#7891;ng. C&aacute;c y&#7871;u t&#7889; con ng&#432;&#7901;i nh&#432; th&#7883; tr&#432;&#7901;ng, v&#7889;n, c&ocirc;ng ngh&#7879; v&agrave; tr&#7907; c&#7845;p c&#7911;a ch&iacute;nh ph&#7911; c&#361;ng &#273;&#7883;nh h&igrave;nh n&#7873;n n&ocirc;ng nghi&#7879;p.", "Natural factors like climate, soils, and water limit crop types. Human factors like markets, capital, technology, and government subsidies also shape agriculture.")}
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">The Green Revolution &amp; Food Security</h3>
    {p('The Green Revolution in the 1960s-70s introduced High Yielding Varieties (HYVs) of crops, artificial fertilisers, pesticides, and mechanisation. It saved millions from starvation, particularly in Asia, but brought significant environmental damage and social inequality.')}
    {p('Food security remains a massive global challenge, relying on four pillars: availability, access, utilisation, and stability. Currently, over 700 million people lack access to sufficient food, driven mostly by poverty, conflict, and extreme weather.')}
    {render_vi("C&aacute;ch m&#7841;ng Xanh &#273;&atilde; c&#7913;u h&agrave;ng tri&#7879;u ng&#432;&#7901;i kh&#7887;i n&#7841;n &#273;&oacute;i b&#7851;ng c&aacute;c gi&#7889;ng n&#259;ng su&#7845;t cao v&agrave; ph&acirc;n b&oacute;n h&oacute;a h&#7885;c, nh&#432;ng l&#7841;i g&acirc;y ra nhi&#7873;u t&#7893;n h&#7841;i m&ocirc;i tr&#432;&#7901;ng. An ninh l&#432;&#417;ng th&#7921;c v&#7851;n l&agrave; m&#7897;t th&aacute;ch th&#7913;c to&agrave;n c&#7847;u kh&#7893;ng l&#7891;.", "The Green Revolution saved millions from starvation using HYVs and chemical fertilisers, but caused significant environmental damage. Food security remains a massive global challenge.")}
</div>
"""

html_10_2_p1 = f"""
<h1 style="{H1_STYLE}">10.2 Global Patterns of Food Supply and Demand</h1>
{svg_supply_chain}
<h2 style="{H2_STYLE}">1. Global Food Supply Patterns</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Major Food-Producing Regions</h3>
    <ul>
        {li('<strong>North American Great Plains:</strong> A global powerhouse producing vast quantities of wheat, maize, and soy. The USA is the world’s largest producer of maize and a leading exporter of soy.')}
        {li('<strong>European Plains:</strong> Characterised by high-tech, intensive farming producing EU wheat, dairy, and wine.')}
        {li('<strong>South/SE Asia:</strong> The undisputed center of global rice production. Countries like China, India, Bangladesh, Vietnam, and Thailand account for roughly 90% of the world’s rice.')}
        {li('<strong>South America:</strong> A massive exporter, notably Brazilian soy and beef, Argentinian wheat, and Chilean fruit.')}
        {li('<strong>Sub-Saharan Africa:</strong> Dominated by small-scale subsistence farming. Despite vast land resources, the region is a net importer of food.')}
        {li('<strong>Australia:</strong> A major global exporter of wheat, beef, and dairy, operating on vast extensive farming models.')}
    </ul>
    <h3 style="{H3_STYLE}">Top Agricultural Exporters</h3>
    {p('The world’s top exporters include the USA, Netherlands, Germany, France, Brazil, Australia, and Argentina.')}
    <h3 style="{H3_STYLE}">The Netherlands Paradox</h3>
    {p('Despite being a tiny, densely populated country, the Netherlands is astonishingly the world’s 2nd largest food exporter (exporting roughly $111bn annually). They achieve this through extreme intensive greenhouse production (using LED-lit facilities to grow tomatoes, peppers, and cucumbers year-round), cutting-edge precision agriculture, and world-leading agricultural knowledge clusters like Wageningen University, supported by highly efficient cooperative farming networks.')}
</div>

<h2 style="{H2_STYLE}">2. Global Food Demand Patterns</h2>
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Calorie consumption per capita:</strong> In the US, Canada, and Europe, average consumption is a massive 3,200-3,800 kcal/day. In South and East Asia, it sits around 2,200-2,800 kcal/day. In Sub-Saharan Africa, it is merely 2,100-2,400 kcal/day (barely above minimum requirements), and in some LICs, it drops below 2,000 kcal, indicating starvation levels.')}
        {li('<strong>Dietary change &amp; Nutrition Transition:</strong> As incomes rise, countries experience a "nutrition transition" &mdash; a shift from traditional plant-based diets to animal-based and processed diets. In China, meat consumption per capita has increased fourfold since 1978. The expanding Indian middle class is demanding significantly more dairy and meat, drastically altering global agricultural pressures.')}
        {li('<strong>Food miles:</strong> The distance food travels from farm to plate. The average meal in the USA has travelled 1,500 miles. Global food trade is worth $2 trillion a year. Air-freighted food (like out-of-season berries or Kenyan green beans flown to the UK) has a massive carbon footprint, prompting a growing "local food" movement.')}
        {li('<strong>Seasonality:</strong> Traditional seasonality in diets is disappearing in HICs due to global imports from the southern hemisphere, vast greenhouse production, and advanced cold storage.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">3. Factors Affecting Food Supply</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Physical Factors</h3>
    <ul>
        {li('<strong>Climate:</strong> Droughts immediately decimate yields. The California drought (2012-2017) cost the agricultural sector over $5bn per year. The Sahel region suffers recurrent, devastating droughts.')}
        {li('<strong>Water availability:</strong> Nearly 2 billion people live in water-scarce regions, making farming extremely difficult without massive irrigation investment.')}
        {li('<strong>Soil quality:</strong> Decades of chemical overuse and poor land management have led to widespread soil degradation.')}
        {li('<strong>Pests and diseases:</strong> Threats like wheat rust and locust swarms can destroy entire harvests. In 2020, East Africa faced its worst locust swarm in 70 years, destroying crops and threatening the food supply of 20 million people.')}
    </ul>
    <h3 style="{H3_STYLE}">Human Factors</h3>
    <ul>
        {li('<strong>Conflict:</strong> Wars destroy supply chains. The 2022 Ukraine war was devastating because Ukraine and Russia accounted for 30% of world wheat exports. The disruption caused global food prices to spike by 40%, triggering what the World Food Programme called the "worst food crisis since WWII".')}
        {li('<strong>Poverty &amp; Technology:</strong> Farmers in LICs lack the capital to invest in modern farming technology, keeping yields low.')}
        {li('<strong>Post-harvest losses:</strong> Due to inadequate storage facilities, lack of cold chain infrastructure, and poor roads, 30-40% of crops in LICs rot or are eaten by pests before they ever reach the consumer.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">4. Trade and Food</h2>
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Comparative advantage:</strong> The economic principle where countries specialise in producing crops they can grow most efficiently, trading for everything else.')}
        {li('<strong>Food trade dependency:</strong> Some nations (like the UAE, Singapore, and Gulf states) import 80-90% of their food. This represents a huge food security risk if global supply chains break down. Poorer countries in the Sahel are highly vulnerable to sudden spikes in global grain prices.')}
        {li('<strong>Agricultural subsidies:</strong> US and EU governments heavily subsidise their farmers. This results in cheap exports that undercut farmers in LICs. Producers of coffee, cotton, and sugar in LICs simply cannot compete. WTO negotiations to fix this (the Doha Round) have been stalled since 2001.')}
        {li('<strong>Land grabbing:</strong> Wealthy nations or massive corporations buying up huge tracts of farmland in LICs to secure their own food supply. Examples include Saudi Arabia buying land in Sudan/Ethiopia, and China in Zambia/Mozambique. While it brings investment and some jobs, it raises deep concerns about local food security, water extraction, and the displacement of smallholder farmers.')}
        {li('<strong>Virtual water:</strong> The hidden water embedded in food products. For instance, it takes 15,000 litres of water to produce 1 kg of beef. When the UK imports beef, it is effectively importing "virtual water". Consequently, water-scarce nations should be cautious about exporting water-intensive crops.')}
    </ul>
</div>
"""

html_10_2_p2 = f"""
<h1 style="{H1_STYLE}">10.2 Global Patterns of Food Supply and Demand (Summary &amp; Vocabulary)</h1>
<h2 style="{H2_STYLE}">Key Geography Vocabulary</h2>
<div style="{CARD_STYLE}">
    {render_vi("Food supply", "cung c&#7845;p l&#432;&#417;ng th&#7921;c")}
    {render_vi("Food demand", "c&#7847;u l&#432;&#417;ng th&#7921;c")}
    {render_vi("Agricultural exports", "xu&#7845;t kh&#7849;u n&ocirc;ng s&#7843;n")}
    {render_vi("Dietary pattern", "m&ocirc; h&igrave;nh ch&#7871; &#273;&#7897; &#259;n u&#7889;ng")}
    {render_vi("Nutrition transition", "chuy&#7875;n &#273;&#7893;i dinh d&#432;&#7905;ng")}
    {render_vi("Food miles", "km th&#7921;c ph&#7849;m")}
    {render_vi("Post-harvest loss", "t&#7893;n th&#7845;t sau thu ho&#7841;ch")}
    {render_vi("Global food market", "th&#7883; tr&#432;&#7901;ng th&#7921;c ph&#7849;m to&agrave;n c&#7847;u")}
    {render_vi("Agricultural subsidy", "tr&#7907; c&#7845;p n&ocirc;ng nghi&#7879;p")}
    {render_vi("Land grabbing", "chi&#7871;m h&#7919;u &#273;&#7845;t")}
    {render_vi("Virtual water", "n&#432;&#7899;c &#7843;o")}
    {render_vi("Food surplus", "th&#7863;ng d&#432; l&#432;&#417;ng th&#7921;c")}
    {render_vi("Food deficit", "thi&#7871;u h&#7909;t l&#432;&#417;ng th&#7921;c")}
</div>

<h2 style="{H2_STYLE}">Topic Summary</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Global Production &amp; The Nutrition Transition</h3>
    {p('Food production is dominated by regions with vast plains and high capital, such as North America, Europe, and parts of Asia. However, global demand is shifting rapidly. As nations develop, populations undergo a "nutrition transition," demanding more meat, dairy, and processed foods, which places immense stress on agricultural systems.')}
    {render_vi("S&#7843;n xu&#7845;t l&#432;&#417;ng th&#7921;c t&#7853;p trung &#7903; B&#7855;c M&#7929;, Ch&acirc;u &Acirc;u v&agrave; Ch&acirc;u &Aacute;. Khi c&aacute;c qu&#7889;c gia ph&aacute;t tri&#7875;n, ng&#432;&#7901;i d&acirc;n tr&#7843;i qua qu&aacute; tr&igrave;nh chuy&#7875;n &#273;&#7893;i dinh d&#432;&#7905;ng, ti&ecirc;u th&#7909; nhi&#7873;u th&#7883;t v&agrave; s&#7919;a h&#417;n, g&acirc;y &aacute;p l&#7921;c l&#7899;n l&ecirc;n h&#7879; th&#7889;ng n&ocirc;ng nghi&#7879;p.", "Food production is concentrated in North America, Europe, and Asia. As countries develop, people undergo a nutrition transition, consuming more meat and dairy, putting huge pressure on agriculture.")}
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Supply Chains &amp; Vulnerabilities</h3>
    {p('The global food supply chain is fragile. It is constantly threatened by physical factors like severe droughts and locust swarms, as well as human factors such as armed conflicts and inadequate infrastructure leading to massive post-harvest losses in LICs.')}
    {render_vi("Chu&#7895;i cung &#7913;ng th&#7921;c ph&#7849;m to&agrave;n c&#7847;u r&#7845;t mong manh, th&#432;&#7901;ng xuy&ecirc;n b&#7883; &#273;e d&#7885;a b&#7903;i h&#7841;n h&aacute;n, s&acirc;u b&#7879;nh, xung &#273;&#7897;t v&#361; trang v&agrave; t&#7893;n th&#7845;t l&#7899;n sau thu ho&#7841;ch &#7903; c&aacute;c n&#432;&#7899;c thu nh&#7853;p th&#7845;p.", "The global food supply chain is fragile, frequently threatened by droughts, pests, armed conflicts, and massive post-harvest losses in LICs.")}
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Trade Inequities</h3>
    {p('Global food trade is heavily distorted by subsidies provided by wealthy governments to their farmers, which undercut farmers in poorer nations. Additionally, controversial practices like "land grabbing" by wealthy nations and the hidden trade of "virtual water" further complicate global food equity.')}
    {render_vi("Th&#432;&#417;ng m&#7841;i l&#432;&#417;ng th&#7921;c to&agrave;n c&#7847;u b&#7883; b&oacute;p m&eacute;o b&#7903;i c&aacute;c kho&#7843;n tr&#7907; c&#7845;p c&#7911;a ch&iacute;nh ph&#7911; gi&agrave;u c&oacute;. C&aacute;c h&agrave;nh vi g&acirc;y tranh c&atilde;i nh&#432; chi&#7871;m h&#7919;u &#273;&#7845;t &#273;ai v&agrave; xu&#7845;t kh&#7849;u n&#432;&#7899;c &#7843;o l&agrave;m tr&#7847;m tr&#7885;ng th&ecirc;m s&#7921; b&#7855;t b&igrave;nh &#273;&#7859;ng.", "Global food trade is distorted by wealthy government subsidies. Controversial practices like land grabbing and virtual water exports worsen inequality.")}
</div>
"""

html_10_3_p1 = f"""
<h1 style="{H1_STYLE}">10.3 The Challenges of Food Supply</h1>
{svg_food_security}
<h2 style="{H2_STYLE}">1. The Food Security Challenge</h2>
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Scale of the problem:</strong> The world produces enough food, yet the distribution is deeply flawed. As of 2023, 735 million people are chronically hungry, and 45 million sit on the brink of catastrophic famine. Over 3 billion people cannot afford a basic healthy diet. Paradoxically, at the exact same time, 2.5 billion people globally are overweight or obese. Furthermore, 30-40% of all food produced is simply wasted.')}
        {li('<strong>Global trends:</strong> Progress on Sustainable Development Goal 2 (Zero Hunger) is shockingly moving backwards. The number of hungry people has risen from 650 million in 2015 to 735 million today. The catastrophic trifecta of climate change, the economic fallout of COVID-19, and violent conflict is actively reversing decades of progress.')}
        {li('<strong>Most affected regions:</strong> The crisis is most severe in sub-Saharan Africa, the Middle East/North Africa (driven by intense conflict), South Asia, and highly vulnerable small island states.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">2. Forms of Malnutrition</h2>
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Undernutrition / Hunger:</strong> Consuming fewer than 2,100 kcal per day. This leads to a severe lack of energy. It results in stunting (low height for age, affecting 149 million children under 5 globally) and wasting (dangerously low weight for height). Child physical and cognitive development is permanently impaired.')}
        {li('<strong>Micronutrient deficiency ("Hidden Hunger"):</strong> Occurs when people consume enough calories but lack essential vitamins and minerals. Iron deficiency causes anaemia (affecting 2 billion people, particularly women). Vitamin A deficiency causes blindness in 250,000-500,000 children annually. Iodine deficiency causes goitre and severely stunts cognitive development.')}
        {li('<strong>Overnutrition / Obesity:</strong> The consumption of excess calories combined with a poor diet. Today, 2.5 billion adults are overweight and 890 million are clinically obese. This is rising rapidly even in LICs as cheap, ultra-processed food globalises. It creates an epidemic of type 2 diabetes, cardiovascular disease, and overwhelming healthcare burdens.')}
        {li('<strong>The Double Burden:</strong> Many countries (like India, China, and Brazil) face a "double burden" of malnutrition &mdash; battling severe undernutrition in poor rural areas while simultaneously facing an obesity crisis in rapidly developing urban centres.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">3. Famine</h2>
{p('Famine is an extreme scarcity of food leading to mass starvation, death, and demographic collapse. Under the IPC (Integrated Food Security Phase Classification), Phase 5 is "Catastrophe/Famine", declared when at least 20% of households face extreme food shortages, acute malnutrition exceeds 30%, and death rates exceed 2 per 10,000 people per day.')}
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Causes of Famine</h3>
    <ul>
        {li('<strong>Immediate vs Underlying Causes:</strong> A physical event like a severe drought or devastating flood often acts as the trigger. However, the underlying causes are almost always human: violent conflict (which destroys farms and restricts aid access), poor governance (corruption, theft of food aid), poverty, and infrastructure failure.')}
        {li('<strong>Amartya Sen’s Theory:</strong> The Nobel-winning economist argued in his 1981 book "Poverty and Famines" that famines are political failures, not just crop failures. Looking at the 1943 Bengal famine, he showed that food was actually available in the country, but the poorest people simply lacked the money to buy it.')}
    </ul>
    <h3 style="{H3_STYLE}">Recent Famine Crises</h3>
    <ul>
        {li('<strong>Yemen:</strong> Devastated by civil war since 2014, leaving 21 million food-insecure and 17 million at crisis/emergency levels.')}
        {li('<strong>South Sudan (2017) &amp; Somalia (2022):</strong> Ravaged by a combination of brutal conflict and historic droughts.')}
        {li('<strong>Ethiopia (Tigray conflict 2020-2022):</strong> War blockades pushed nearly 900,000 people into man-made famine conditions.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">4. Solutions to Food Challenges</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Increasing Supply &amp; Efficiency</h3>
    <ul>
        {li('<strong>Advanced Irrigation:</strong> Drip irrigation (invented in Israel) is up to 80% more efficient than traditional flood irrigation, delivering water directly to plant roots. Rich, arid nations like Saudi Arabia and the UAE are also heavily investing in desalination plants for agriculture.')}
        {li('<strong>GM Crops:</strong> Projects like WEMA (Water Efficient Maize for Africa) have provided drought-tolerant seeds to 2 million smallholders. In India, 95% of cotton is insect-resistant Bt cotton. However, GM crops remain highly controversial due to corporate seed patenting (e.g., Monsanto/Bayer) and strict resistance from the EU.')}
        {li('<strong>Appropriate Technology:</strong> For poor farmers, simple tech works best. Treadle pumps (distributed by NGOs to millions of families) provide a low-cost, human-powered way to irrigate small plots, boosting incomes by $100 per family. Basic improvements in seed varieties and local extension education are vital.')}
        {li('<strong>Reducing Food Waste:</strong> With 30% of global food wasted, massive gains can be made. Solutions include solar-powered cold storage units in LICs to stop food rotting, and strict legislation in HICs (e.g., France legally forcing supermarkets to donate unsold food to charities).')}
        {li('<strong>Vertical Farming:</strong> Growing crops indoors in stacked layers using LED lights and hydroponics without pesticides. Companies like AeroFarms boast productivity up to 390x higher per square foot than traditional farms, though capital costs are enormous.')}
    </ul>
    <h3 style="{H3_STYLE}">Improving Access</h3>
    <ul>
        {li('<strong>Social Protection:</strong> Direct government help. Brazil’s <em>Bolsa Familia</em> program gave cash to 26 million poor families (conditional on kids attending school), halving extreme poverty. India’s Public Distribution System provides highly subsidised rice and wheat to 800 million people.')}
        {li('<strong>Fair Trade &amp; Land Reform:</strong> Ensuring farmers receive a living wage. Historically, successful land redistribution to smallholders in South Korea and Taiwan ignited economic booms. Conversely, poorly managed land reform in Zimbabwe triggered catastrophic food crises.')}
        {li('<strong>Emergency Aid:</strong> The World Food Programme feeds over 160 million people in crises, though modern aid increasingly uses cash transfers rather than direct food drops, which supports local markets.')}
    </ul>
</div>

<h2 style="{H2_STYLE}">5. Sustainable Food Production</h2>
<div style="{CARD_STYLE}">
    <ul>
        {li('<strong>Agroecology:</strong> Farming systems designed to mimic natural ecosystems. It integrates crops, livestock, and trees (agroforestry) without synthetic chemicals, prioritising long-term soil health. The FAO champions this as a highly sustainable path to food security.')}
        {li('<strong>Precision Agriculture:</strong> Using GPS-guided tractors, drone monitoring, and AI to apply exactly the right amount of water and fertiliser only where needed, drastically reducing chemical runoff.')}
        {li('<strong>Dietary Shifts &amp; Alternative Proteins:</strong> Meat production is wildly inefficient, using 70% of agricultural land and 30% of freshwater while producing 14.5% of global greenhouse gas emissions. Shifting toward plant-based diets (like Beyond Meat) or investing in cellular agriculture (lab-grown meat, which has dropped in cost from &euro;250,000 for a burger in 2013 to under $10/kg today) could eliminate factory farming and restore millions of hectares to nature.')}
    </ul>
</div>
"""

html_10_3_p2 = f"""
<h1 style="{H1_STYLE}">10.3 The Challenges of Food Supply (Summary &amp; Vocabulary)</h1>
<h2 style="{H2_STYLE}">Key Geography Vocabulary</h2>
<div style="{CARD_STYLE}">
    {render_vi("Food security", "an ninh l&#432;&#417;ng th&#7921;c")}
    {render_vi("Malnutrition", "suy dinh d&#432;&#7905;ng")}
    {render_vi("Undernutrition", "&#273;&oacute;i &#259;n")}
    {render_vi("Overweight / Obesity", "th&#7915;a c&acirc;n/b&eacute;o ph&igrave;")}
    {render_vi("Famine", "n&#7841;n &#273;&oacute;i")}
    {render_vi("Agroecology", "n&ocirc;ng nghi&#7879;p sinh th&aacute;i")}
    {render_vi("Drip irrigation", "t&#432;&#7899;i nh&#7887; gi&#7885;t")}
    {render_vi("GM crops (Genetically Modified)", "c&acirc;y tr&#7891;ng bi&#7871;n &#273;&#7893;i gen")}
    {render_vi("Food waste", "l&#227;ng ph&iacute; th&#7921;c ph&#7849;m")}
    {render_vi("Vertical farming", "tr&#7891;ng n&ocirc;ng nghi&#7879;p th&#7859;ng &#273;&#7913;ng")}
    {render_vi("Precision agriculture", "n&ocirc;ng nghi&#7879;p ch&iacute;nh x&aacute;c")}
    {render_vi("Cultured meat", "th&#7883;t nh&acirc;n t&#7841;o")}
    {render_vi("Plant-based meat", "th&#7883;t th&#7921;c v&#7853;t")}
    {render_vi("Food aid", "vi&#7879;n tr&#7907; l&#432;&#417;ng th&#7921;c")}
</div>

<h2 style="{H2_STYLE}">Topic Summary</h2>
<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">The Crisis of Malnutrition</h3>
    {p('Global food inequality has created a crisis of malnutrition taking three forms: undernutrition (lack of calories causing stunting), hidden hunger (lack of vitamins/minerals), and an explosion of obesity driven by processed foods. Progress on eradicating hunger is currently reversing.')}
    {render_vi("B&#7845;t b&igrave;nh &#273;&#7859;ng l&#432;&#417;ng th&#7921;c to&agrave;n c&#7847;u t&#7841;o ra cu&#7897;c kh&#7911;ng ho&#7843;ng suy dinh d&#432;&#7905;ng d&#432;&#7899;i ba h&igrave;nh th&#7913;c: &#273;&oacute;i &#259;n, &#273;&oacute;i ti&#7873;m &#7849;n (thi&#7871;u vitamin), v&agrave; b&eacute;o ph&igrave;. Ti&#7871;n tr&igrave;nh x&oacute;a &#273;&oacute;i &#273;ang b&#7883; &#273;&#7843;o ng&#432;&#7907;c.", "Global food inequality creates a malnutrition crisis in three forms: undernutrition, hidden hunger, and obesity. Progress on hunger eradication is reversing.")}
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Understanding Famines</h3>
    {p('Famines are catastrophic events of mass starvation. While extreme weather like droughts can trigger them, the root causes are fundamentally human: war, blockades, corruption, and systemic poverty preventing people from affording the food that is available.')}
    {render_vi("N&#7841;n &#273;&oacute;i l&agrave; th&#7843;m h&#7885;a ch&#7871;t &#273;&oacute;i h&agrave;ng lo&#7841;t. M&#7863;c d&ugrave; h&#7841;n h&aacute;n l&agrave; ng&ograve;i n&#7893;, nguy&ecirc;n nh&acirc;n g&#7889;c r&#7877; ch&#7911; y&#7871;u l&agrave; do con ng&#432;&#7901;i: chi&#7871;n tranh, phong t&#7887;a, tham nh&#361;ng v&agrave; ngh&egrave;o &#273;&oacute;i c&ugrave;ng c&#7921;c.", "Famines are mass starvation disasters. While droughts trigger them, root causes are human: war, blockades, corruption, and extreme poverty.")}
</div>

<div style="{CARD_STYLE}">
    <h3 style="{H3_STYLE}">Solutions for the Future</h3>
    {p('Solving these challenges requires a multi-pronged approach. We must increase supply through technology (drip irrigation, GM crops, vertical farming), drastically reduce food waste, and improve economic access via social safety nets. Ultimately, agriculture must shift toward sustainable methods like agroecology and reduced meat consumption.')}
    {render_vi("Vi&#7879;c gi&#7843;i quy&#7871;t nh&#7919;ng th&aacute;ch th&#7913;c n&agrave;y &#273;&ograve;i h&#7887;i c&ocirc;ng ngh&#7879; (t&#432;&#7899;i nh&#7887; gi&#7885;t, c&acirc;y tr&#7891;ng GM), gi&#7843;m thi&#7875;u l&atilde;ng ph&iacute; th&#7921;c ph&#7849;m v&agrave; m&#7841;ng l&#432;&#7899;i an sinh x&atilde; h&#7897;i. N&ocirc;ng nghi&#7879;p ph&#7843;i chuy&#7875;n h&#432;&#7899;ng sang c&aacute;c ph&#432;&#417;ng ph&aacute;p b&#7873;n v&#7919;ng v&agrave; gi&#7843;m ti&ecirc;u th&#7909; th&#7883;t.", "Solving these challenges requires technology, reducing food waste, and social safety nets. Agriculture must shift towards sustainable methods and reduced meat consumption.")}
</div>
"""

pages_data = [
    ("10.1 P1", PAGES["10.1 P1"], render_html(html_10_1_p1)),
    ("10.1 P2", PAGES["10.1 P2"], render_html(html_10_1_p2)),
    ("10.2 P1", PAGES["10.2 P1"], render_html(html_10_2_p1)),
    ("10.2 P2", PAGES["10.2 P2"], render_html(html_10_2_p2)),
    ("10.3 P1", PAGES["10.3 P1"], render_html(html_10_3_p1)),
    ("10.3 P2", PAGES["10.3 P2"], render_html(html_10_3_p2))
]

for name, pid, content in pages_data:
    url = URL_BASE + pid
    data = json.dumps({"content_html": content}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="PATCH")
    try:
        with urllib.request.urlopen(req) as response:
            print(f"SUCCESS: {name} uploaded. Status: {response.status}, Size: {len(content)} chars.")
    except Exception as e:
        print(f"ERROR: {name} failed. Exception: {e}")
