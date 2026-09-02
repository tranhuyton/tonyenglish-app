import requests

PAGE_ID = "fb591348-a75b-4594-851b-d6b9baafbef4"
SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>1.3 Rivers: Opportunities & Hazards</title>
<style>
  body { font-family: 'Inter', sans-serif; max-width: 900px; margin: 0 auto; color: #1e293b; line-height: 1.6; font-size: 16px; padding: 20px; }
  h1 { color: #1e3a8a; font-size: 32px; border-bottom: 3px solid #60a5fa; display: inline-block; padding-bottom: 10px; }
  h2 { color: #0f172a; border-bottom: 2px solid #a78bfa; padding-bottom: 10px; font-size: 24px; margin-top: 40px; }
  h3 { color: #1e3a8a; font-size: 19px; }
  img { max-width: 420px; height: auto; display: block; margin: 0 auto; }
  .caption { font-size: 13px; color: #94a3b8; font-style: italic; text-align: center; margin-top: 8px; }
  .info-box { background: #f1f5f9; padding: 15px; border-radius: 8px; margin: 20px 0; }
  .info-box.green { background: #f0fdf4; border-left: 4px solid #22c55e; }
  .info-box.orange { background: #fff7ed; border-left: 4px solid #f97316; }
  .info-box.blue { background: #eff6ff; border-left: 4px solid #3b82f6; }
  .info-box.purple { background: #faf5ff; border-left: 4px solid #9333ea; }
  .key-term { color: #9333ea; font-weight: bold; }
  ul { margin: 10px 0 10px 20px; }
  li { margin-bottom: 6px; }
  #svg-section { margin: 30px 0; }
  #def-panel {
    display: none;
    background: #1e293b;
    color: #f8fafc;
    padding: 18px 22px;
    border-radius: 10px;
    margin-top: 16px;
    font-size: 15px;
  }
  #def-panel h4 { margin: 0 0 8px 0; font-size: 17px; }
  #def-panel p { margin: 0; }
  .eng-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 20px 0; }
  .eng-card { padding: 14px 16px; border-radius: 8px; }
  .eng-card.hard { background: #fef2f2; border-left: 4px solid #ef4444; }
  .eng-card.soft { background: #f0fdf4; border-left: 4px solid #22c55e; }
  .eng-card h4 { margin: 0 0 8px 0; color: #0f172a; font-size: 16px; }
  .eng-card ul { margin: 0; padding-left: 18px; }
  .impacts-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 16px 0; }
  .impact-card { padding: 12px 14px; border-radius: 8px; font-size: 14px; }
  .impact-card.primary { background: #fee2e2; border-top: 3px solid #ef4444; }
  .impact-card.secondary { background: #fef9c3; border-top: 3px solid #eab308; }
  .impact-card.tertiary { background: #dbeafe; border-top: 3px solid #3b82f6; }
  .impact-card h5 { margin: 0 0 6px 0; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; }
  .terms-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 16px 0; }
  .term-card { background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 8px; padding: 10px 14px; font-size: 14px; }
  .term-card strong { color: #9333ea; display: block; margin-bottom: 3px; }
  @media (max-width: 600px) {
    .eng-grid, .impacts-grid, .terms-grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<h1>🌊 1.3 Rivers: Opportunities &amp; Hazards</h1>
<p style="color:#64748b; font-size:15px; margin-top:4px;"><em>How living near rivers brings both benefits and risks</em></p>

<div id="svg-section">
  <svg viewBox="0 0 860 320" xmlns="http://www.w3.org/2000/svg"
       style="width:100%;border-radius:12px;background:#f8fafc;border:1px solid #e2e8f0;cursor:pointer;"
       role="img" aria-label="Rivers: Opportunities and Hazards diagram">
    <rect x="0" y="0" width="860" height="42" fill="#1e3a8a" rx="12"/>
    <text x="430" y="27" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="700" font-size="16">Living Near Rivers — Click a topic to explore</text>
    <rect x="0" y="42" width="430" height="278" fill="#f0fdf4" rx="0"/>
    <rect x="430" y="42" width="430" height="278" fill="#fff7ed" rx="0"/>
    <rect x="408" y="42" width="44" height="278" fill="#bfdbfe"/>
    <text x="430" y="108" text-anchor="middle" fill="#1e40af" font-family="Inter,sans-serif" font-size="11" font-weight="600" transform="rotate(-90,430,108)">R I V E R</text>
    <text x="210" y="72" text-anchor="middle" fill="#15803d" font-family="Inter,sans-serif" font-weight="800" font-size="17">🌿 OPPORTUNITIES</text>
    <text x="648" y="72" text-anchor="middle" fill="#c2410c" font-family="Inter,sans-serif" font-weight="800" font-size="17">⚠️ HAZARDS</text>
    <g onclick="showDef('water_supply')" style="cursor:pointer">
      <rect x="18" y="88" width="140" height="46" rx="8" fill="#22c55e" opacity="0.85"/>
      <text x="88" y="107" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">💧</text>
      <text x="88" y="124" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="600">Water Supply</text>
    </g>
    <g onclick="showDef('agriculture')" style="cursor:pointer">
      <rect x="168" y="88" width="140" height="46" rx="8" fill="#16a34a" opacity="0.85"/>
      <text x="238" y="107" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">🌾</text>
      <text x="238" y="124" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="600">Agriculture</text>
    </g>
    <g onclick="showDef('fishing')" style="cursor:pointer">
      <rect x="18" y="148" width="140" height="46" rx="8" fill="#22c55e" opacity="0.85"/>
      <text x="88" y="167" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">🎣</text>
      <text x="88" y="184" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="600">Fishing</text>
    </g>
    <g onclick="showDef('transport')" style="cursor:pointer">
      <rect x="168" y="148" width="140" height="46" rx="8" fill="#16a34a" opacity="0.85"/>
      <text x="238" y="167" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">🚢</text>
      <text x="238" y="184" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="600">Transport</text>
    </g>
    <g onclick="showDef('tourism')" style="cursor:pointer">
      <rect x="18" y="208" width="140" height="46" rx="8" fill="#22c55e" opacity="0.85"/>
      <text x="88" y="227" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">🏞️</text>
      <text x="88" y="244" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="600">Tourism</text>
    </g>
    <g onclick="showDef('hep')" style="cursor:pointer">
      <rect x="168" y="208" width="140" height="46" rx="8" fill="#16a34a" opacity="0.85"/>
      <text x="238" y="227" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">⚡</text>
      <text x="238" y="244" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="600">HEP &amp; Industry</text>
    </g>
    <g onclick="showDef('flooding')" style="cursor:pointer">
      <rect x="462" y="108" width="160" height="76" rx="8" fill="#f97316" opacity="0.9"/>
      <text x="542" y="135" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="26">🌊</text>
      <text x="542" y="162" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="14" font-weight="700">Flooding</text>
      <text x="542" y="178" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="10">(click to explore)</text>
    </g>
    <g onclick="showDef('pollution')" style="cursor:pointer">
      <rect x="638" y="108" width="160" height="76" rx="8" fill="#dc2626" opacity="0.85"/>
      <text x="718" y="135" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="26">☠️</text>
      <text x="718" y="162" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="14" font-weight="700">Pollution</text>
      <text x="718" y="178" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="10">(click to explore)</text>
    </g>
    <g onclick="showDef('management')" style="cursor:pointer">
      <rect x="462" y="208" width="336" height="52" rx="8" fill="#7c3aed" opacity="0.85"/>
      <text x="630" y="231" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="18">🛠️</text>
      <text x="630" y="250" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="13" font-weight="700">Flood Management Strategies</text>
    </g>
    <path d="M408 290 Q418 280 430 290 Q442 300 452 290" stroke="#60a5fa" stroke-width="2.5" fill="none"/>
    <path d="M408 305 Q418 295 430 305 Q442 315 452 305" stroke="#93c5fd" stroke-width="2" fill="none"/>
  </svg>
  <div id="def-panel">
    <h4 id="def-title"></h4>
    <p id="def-body"></p>
  </div>
</div>

<script>
const defs = {
  water_supply: { title: "💧 Water Supply", body: "Rivers provide a reliable, year-round source of fresh water for drinking, cooking, sanitation, irrigation of crops, and industrial processes. Cities have historically grown beside rivers for exactly this reason." },
  agriculture: { title: "🌾 Agriculture & Fertile Soils", body: "Rivers deposit alluvium (fine, nutrient-rich sediment) on their floodplains during floods. These alluvial soils are highly fertile and productive for farming. The Nile, Mesopotamia (Tigris & Euphrates), and Indus valleys were all cradles of early civilisation thanks to river agriculture." },
  fishing: { title: "🎣 Fishing", body: "Rivers and their connected wetlands support abundant fish populations, providing a significant protein source for millions of people worldwide. Communities living along major rivers often rely on fishing as a primary livelihood." },
  transport: { title: "🚢 Transport & Trade", body: "Rivers are natural routes for moving people and goods. Before roads and railways, rivers were the motorways of their era. Wide, navigable rivers reduced the cost of trade and enabled the growth of port cities at their mouths and confluences." },
  tourism: { title: "🏞️ Tourism & Recreation", body: "Scenic river valleys, gorges, and waterfalls attract tourists. Activities include boating, kayaking, fishing, and hiking. Riverside real estate commands premium prices. Tourism generates significant income for local communities." },
  hep: { title: "⚡ Hydroelectric Power & Industry", body: "Dams built across rivers harness the kinetic energy of water to generate hydroelectric power (HEP) — a clean, renewable energy source. Multipurpose schemes combine several functions: HEP, flood control, water storage, and improved navigation. The River Danube locks, for example, generate electricity while managing river levels." },
  flooding: { title: "🌊 Flooding", body: "Flooding occurs when a river overtops its banks and inundates the surrounding land. Natural causes include heavy/prolonged rainfall, rapid snowmelt, steep slopes, and impermeable bedrock. Human causes include urbanisation, deforestation, and building on floodplains. Floods cause loss of life, property damage, disease, and long-term economic disruption." },
  pollution: { title: "☠️ River Pollution", body: "Rivers can be polluted by industrial effluent, agricultural run-off (pesticides and fertilisers causing eutrophication), sewage discharge, and oil spills. Pollution destroys aquatic ecosystems, contaminates drinking water, and poses serious health risks to riverside communities." },
  management: { title: "🛠️ Flood Management Strategies", body: "Hard engineering uses physical structures: dams, levées, channelisation, and flood barriers (e.g. Thames Barrier). Soft engineering works with nature: floodplain zoning, afforestation, wetland restoration, and Sustainable Drainage Systems (SuDS). Soft approaches are generally more sustainable and cost-effective long-term." }
};
function showDef(key) {
  const panel = document.getElementById('def-panel');
  const title = document.getElementById('def-title');
  const body = document.getElementById('def-body');
  if (defs[key]) {
    title.textContent = defs[key].title;
    body.textContent = defs[key].body;
    panel.style.display = 'block';
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}
</script>

<h2>🌿 Section 1: Opportunities of Living Near Rivers</h2>

<p>Rivers have attracted human settlement since prehistory. They offer a unique combination of resources that make them ideal locations to live, farm, trade, and build communities.</p>

<div class="info-box green">
  <strong>Key Fact:</strong> The world's earliest civilisations — Egypt (Nile), Mesopotamia (Tigris &amp; Euphrates), and the Indus Valley — all developed beside rivers. Reliable water and fertile soils were the foundations of organised society.
</div>

<h3>Water Supply</h3>
<p>Rivers provide a <b class="key-term">perennial</b> (year-round) source of fresh water for drinking, cooking, sanitation, and industry. This reliability was critical before the age of pipelines and reservoirs — settlements without a nearby river faced severe limitations.</p>

<h3>Agriculture and Alluvial Soils</h3>
<p>When rivers flood, they deposit <b class="key-term">alluvium</b> — fine, nutrient-rich sediment — across the <b class="key-term">floodplain</b>. These <b class="key-term">alluvial soils</b> are exceptionally fertile, supporting high-yield farming with minimal fertiliser input.</p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig134.png" alt="Nile valley aerial view showing fertile green farmland alongside the desert"/>
<p class="caption">Fig 1.34 — The Nile valley: a narrow ribbon of intensely cultivated land in an otherwise arid landscape, made possible by annual flooding and alluvial soils.</p>

<div class="info-box">
  <strong>Examples of river-based civilisations:</strong>
  <ul>
    <li><b>Nile valley, Egypt</b> — annual floods deposited rich silt; the basis of Ancient Egyptian agriculture for millennia</li>
    <li><b>Mesopotamia</b> (modern Iraq) — the "Fertile Crescent" between the Tigris and Euphrates rivers</li>
    <li><b>Indus valley</b> (modern Pakistan/India) — one of the world's first urban civilisations, c. 3300–1300 BCE</li>
  </ul>
</div>

<h3>Fishing</h3>
<p>Rivers and associated wetlands support productive fisheries. Fish provide an important protein source and support livelihoods for millions of people globally, particularly in South and Southeast Asia and sub-Saharan Africa.</p>

<h3>Transport</h3>
<p>Before roads and railways, rivers were the primary highways for moving goods and people. Wide, navigable rivers reduced the cost of trade and enabled the growth of port cities at their mouths and confluences. Many modern cities (London, Cairo, Paris, Shanghai) developed at key river crossing or trading points.</p>

<h3>Hydroelectric Power (HEP)</h3>
<p>Dams built across rivers harness the kinetic energy of water to generate <b class="key-term">hydroelectric power (HEP)</b> — a clean, renewable energy source. <b class="key-term">Multipurpose river schemes</b> combine several functions in a single infrastructure project.</p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig135.png" alt="River Danube locks showing hydroelectric infrastructure"/>
<p class="caption">Fig 1.35 — River Danube locks: a multipurpose scheme providing hydroelectric power generation, flood control, and improved navigation for river traffic.</p>

<h3>Tourism, Recreation, and Real Estate</h3>
<p>Scenic river valleys, gorges, waterfalls, and riverside towns attract significant tourist numbers. Activities include boat trips, kayaking, fishing, cycling, and walking. Riverside and waterfront properties command premium prices in the housing market.</p>

<h2>⚠️ Section 2: Hazard — Floods</h2>

<p><b class="key-term">Flooding</b> occurs when a river's discharge exceeds its channel capacity, causing water to overtop its banks and inundate surrounding land. It is one of the most widespread and damaging natural hazards on Earth.</p>

<h3>Causes of Flooding</h3>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig136.png" alt="Classification diagram showing natural and human causes of river flooding"/>
<p class="caption">Fig 1.36 — Classification of flood causes: natural (physical) factors on the left, human factors on the right.</p>

<div class="eng-grid">
  <div class="eng-card" style="background:#fef3c7;border-left:4px solid #d97706;">
    <h4>🌧️ Natural Causes</h4>
    <ul>
      <li><strong>Heavy or prolonged rainfall</strong> — most common cause; saturates soil and overwhelms channels</li>
      <li><strong>Rapid snowmelt</strong> — spring thaw releases large volumes of water quickly</li>
      <li><strong>Steep relief</strong> — water runs off hillsides rapidly, reaching rivers quickly</li>
      <li><strong>Impermeable rock</strong> — little water soaks into the ground, so more reaches the river as surface runoff</li>
      <li><strong>Natural vegetation changes</strong> — e.g. natural forest fires remove interception</li>
    </ul>
  </div>
  <div class="eng-card" style="background:#fee2e2;border-left:4px solid #dc2626;">
    <h4>🏙️ Human Causes</h4>
    <ul>
      <li><strong>Urbanisation</strong> — impermeable surfaces (roads, rooftops) and underground drains increase runoff speed dramatically</li>
      <li><strong>Deforestation</strong> — trees intercept rainfall and their roots absorb water; removing them sharply increases surface runoff</li>
      <li><strong>Floodplain development</strong> — buildings and roads reduce the natural storage capacity of the floodplain</li>
      <li><strong>Climate change</strong> — increasing intensity and frequency of extreme rainfall events</li>
    </ul>
  </div>
</div>

<h3>Impacts of Flooding</h3>
<p>Flood impacts are classified by how directly they result from the flood event:</p>

<div class="impacts-grid">
  <div class="impact-card primary">
    <h5>🔴 Primary (Immediate)</h5>
    <ul>
      <li>Loss of life (drowning)</li>
      <li>Buildings flooded and structurally damaged</li>
      <li>Roads, bridges, railways destroyed</li>
      <li>Crops and livestock lost</li>
    </ul>
  </div>
  <div class="impact-card secondary">
    <h5>🟡 Secondary (Short-term)</h5>
    <ul>
      <li>Water supply contaminated</li>
      <li>Disease outbreaks (cholera, typhoid)</li>
      <li>Electricity and gas disrupted</li>
      <li>Business closures; economic loss</li>
    </ul>
  </div>
  <div class="impact-card tertiary">
    <h5>🔵 Tertiary (Long-term)</h5>
    <ul>
      <li>Farmland abandoned due to silt and damage</li>
      <li>Insurance costs rise; devalued land</li>
      <li>Habitat destruction and ecosystem loss</li>
      <li>Psychological trauma in communities</li>
    </ul>
  </div>
</div>

<div class="info-box orange">
  <strong>Exam tip — Primary vs Secondary impacts:</strong> Primary impacts are <em>directly</em> caused by the flood water (e.g. buildings flooded). Secondary impacts are <em>indirect</em> consequences triggered by the primary impacts (e.g. disease from contaminated water). Tertiary impacts are the long-term effects that persist after the flood water recedes.
</div>

<h2>🛠️ Section 3: Flood Management</h2>

<p>Flood management strategies aim to reduce the frequency, severity, or impact of flooding. They are broadly divided into <b class="key-term">hard engineering</b> and <b class="key-term">soft engineering</b> approaches.</p>

<h3>Hard Engineering (Traditional / Structural)</h3>
<p>Hard engineering uses large physical structures to control river flow. It is often effective in the short term but expensive, requires ongoing maintenance, and can create problems downstream.</p>

<div class="eng-grid">
  <div class="eng-card hard">
    <h4>🏗️ Hard Engineering Methods</h4>
    <ul>
      <li><strong>Dams &amp; reservoirs</strong> — store excess water upstream; control release of flow</li>
      <li><strong>Levées (embankments)</strong> — raised earth or concrete walls along riverbanks to contain floodwater</li>
      <li><strong>Channelisation</strong> — straightening, deepening, or lining the river channel to speed up water flow and increase capacity</li>
      <li><strong>Flood barriers</strong> — moveable barriers raised during flood risk; e.g. <em>Thames Barrier</em>, London</li>
      <li><strong>Flood walls</strong> — permanent concrete walls in urban areas to protect buildings</li>
    </ul>
  </div>
  <div class="eng-card hard" style="background:#fef2f2;border-left:4px solid #b91c1c;">
    <h4>⚠️ Disadvantages</h4>
    <ul>
      <li>Very expensive to build and maintain</li>
      <li>Channelisation speeds up flow, increasing flood risk downstream</li>
      <li>Dams trap sediment, reducing downstream fertility</li>
      <li>Can give communities a false sense of security</li>
      <li>Disrupts river ecosystems</li>
    </ul>
  </div>
</div>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig138.png" alt="Hard engineering flood defences including Thames Barrier and Zermatt levees"/>
<p class="caption">Fig 1.38 — Hard engineering examples: the Thames Barrier (London) — a moveable tidal barrier — and reinforced levées protecting the town of Zermatt, Switzerland.</p>

<h3>Soft Engineering (Sustainable / Nature-Based)</h3>
<p>Soft engineering works <em>with</em> natural river processes rather than against them. It is generally cheaper, more sustainable, and better for biodiversity, though it may offer less immediate protection than hard structures.</p>

<div class="eng-grid">
  <div class="eng-card soft">
    <h4>🌿 Soft Engineering Methods</h4>
    <ul>
      <li><strong>Flood warning systems</strong> — real-time monitoring of rainfall and river levels; alerts communities to evacuate and prepare</li>
      <li><strong>Floodplain zoning</strong> — land-use planning that restricts new development in high-risk flood zones</li>
      <li><strong>Flood abatement</strong> — upstream measures to reduce runoff: reforestation, contour ploughing, wetland restoration</li>
      <li><strong>Flood diversion</strong> — controlled release of floodwater into designated washlands, protecting urban areas</li>
      <li><strong>River restoration</strong> — re-meandering straightened channels to slow flow and restore habitat</li>
    </ul>
  </div>
  <div class="eng-card soft" style="background:#f0fdf4;border-left:4px solid #16a34a;">
    <h4>✅ Advantages</h4>
    <ul>
      <li>Lower cost over long term</li>
      <li>Sustainable — improves ecosystem health</li>
      <li>Addresses root causes (e.g. reducing runoff)</li>
      <li>Works with natural processes</li>
      <li>Can enhance biodiversity and recreation</li>
    </ul>
  </div>
</div>

<h3>Sustainable Drainage Systems (SuDS)</h3>
<p><b class="key-term">Sustainable Drainage Systems (SuDS)</b> are urban engineering solutions that mimic natural drainage processes to reduce surface runoff. Rather than channelling rainwater quickly into drains, SuDS slow, store, and naturally filter water.</p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig140.png" alt="Diagram illustrating Sustainable Drainage Systems (SuDS) components in an urban area"/>
<p class="caption">Fig 1.40 — Sustainable Drainage Systems (SuDS): a suite of measures that together reduce urban runoff, attenuate peak flows, and improve water quality.</p>

<div class="info-box blue">
  <strong>Key SuDS methods:</strong>
  <ul>
    <li>🌱 <strong>Green roofs</strong> — living vegetation on rooftops absorbs rainwater and reduces runoff</li>
    <li>🌊 <strong>Swales</strong> — shallow, vegetated channels that slow and filter surface runoff</li>
    <li>🏊 <strong>Infiltration basins</strong> — shallow depressions that allow water to percolate into the ground</li>
    <li>🧱 <strong>Permeable surfaces</strong> — paving that allows water to pass through into the soil below</li>
    <li>🏞️ <strong>Retention ponds</strong> — store stormwater temporarily and release it slowly</li>
    <li>🏗️ <strong>Underground storage tanks</strong> — store rainwater for later use (e.g. toilet flushing, irrigation)</li>
  </ul>
</div>

<h2>📚 Key Terms Summary</h2>

<div class="terms-grid">
  <div class="term-card"><strong>Alluvium</strong>Fine, nutrient-rich sediment deposited by a river on its floodplain during flood events.</div>
  <div class="term-card"><strong>Floodplain</strong>The flat land either side of a river channel, formed by alluvial deposits, prone to flooding.</div>
  <div class="term-card"><strong>Hydroelectric Power (HEP)</strong>Electricity generated by harnessing the energy of flowing or falling water via a turbine.</div>
  <div class="term-card"><strong>Multipurpose river scheme</strong>A dam/reservoir project serving multiple purposes: HEP, water supply, flood control, navigation.</div>
  <div class="term-card"><strong>Flooding</strong>When river discharge exceeds channel capacity, water overtops banks and inundates land.</div>
  <div class="term-card"><strong>Hard engineering</strong>Large-scale physical structures (dams, levées, barriers) used to control river flow.</div>
  <div class="term-card"><strong>Soft engineering</strong>Nature-based or planning approaches (zoning, afforestation, SuDS) to manage flood risk sustainably.</div>
  <div class="term-card"><strong>SuDS</strong>Sustainable Drainage Systems — urban measures that mimic natural drainage to reduce runoff.</div>
  <div class="term-card"><strong>Levée</strong>An embankment (natural or artificial) built along a riverbank to prevent flooding.</div>
  <div class="term-card"><strong>Channelisation</strong>Engineering a river to flow faster by straightening, deepening, or lining its channel.</div>
  <div class="term-card"><strong>Floodplain zoning</strong>Land-use planning that restricts building in flood-prone areas to reduce future flood risk.</div>
  <div class="term-card"><strong>Urbanisation</strong>The growth of towns and cities; increases impermeable surfaces, speeding up runoff into rivers.</div>
</div>

<div class="info-box purple">
  <strong>📝 Exam focus for this topic:</strong>
  <ul>
    <li>Be able to explain <em>why</em> rivers attract settlement — give specific named examples</li>
    <li>Distinguish between natural and human causes of flooding — use geographical terminology</li>
    <li>Compare hard and soft engineering — advantages, disadvantages, and specific examples</li>
    <li>Explain how SuDS work and why they are considered more sustainable than traditional drains</li>
    <li>Use the terms <em>primary, secondary</em> and <em>tertiary</em> correctly when describing flood impacts</li>
  </ul>
</div>

</body>
</html>"""

url = f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{PAGE_ID}"
headers = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}

print(f"Uploading to page ID: {PAGE_ID}")
print(f"HTML length: {len(HTML_CONTENT)} characters")

response = requests.patch(url, headers=headers, json={"content_html": HTML_CONTENT})

print(f"Status code: {response.status_code}")
if response.status_code in (200, 204):
    print("SUCCESS: Lecture 1.3 Page 1 uploaded successfully!")
else:
    print(f"ERROR response: {repr(response.text)}")
