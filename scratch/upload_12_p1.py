import requests
import json

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
PAGE_ID = "ce4f09bd-c09b-4cc4-8700-18162e86b316"
IMG = "https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/"

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>1.2 River Landforms</title>
<style>
  body{font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;padding:20px;}
  h1{color:#1e3a8a;font-size:32px;border-bottom:3px solid #60a5fa;display:inline-block;padding-bottom:10px;}
  h2{color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:10px;font-size:24px;margin-top:40px;}
  h3{color:#1e3a8a;font-size:19px;}
  img{max-width:420px;height:auto;display:block;margin:0 auto;}
  .caption{font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;}
  .info-box{background:#f1f5f9;padding:15px;border-radius:8px;margin:20px 0;}
  .subtitle{color:#64748b;font-size:17px;margin-top:4px;margin-bottom:30px;}

  /* SVG long profile */
  #long-profile-wrap{position:relative;margin:30px 0;}
  .lp-btn{cursor:pointer;transition:opacity .2s;}
  .lp-btn:hover .lp-dot{filter:brightness(1.3);}
  #def-panel{display:none;background:#1e3a8a;color:#fff;border-radius:10px;padding:18px 22px;margin-top:14px;}
  #def-panel h4{margin:0 0 6px 0;font-size:17px;color:#93c5fd;}
  #def-panel p{margin:0;font-size:15px;line-height:1.5;}

  /* Summary table */
  table{width:100%;border-collapse:collapse;margin-top:16px;font-size:15px;}
  th{background:#1e3a8a;color:#fff;padding:10px 14px;text-align:left;}
  td{padding:9px 14px;border-bottom:1px solid #e2e8f0;}
  tr:nth-child(even) td{background:#f8fafc;}
</style>
</head>
<body>

<h1>🏔️ 1.2 River Landforms</h1>
<p class="subtitle">How rivers shape the landscape from source to mouth</p>

<!-- ═══════════════ INTERACTIVE LONG PROFILE ═══════════════ -->
<h2>🗺️ Interactive Long Profile</h2>
<p>Click any landform marker on the diagram to see its definition.</p>

<div id="long-profile-wrap">
<svg viewBox="0 0 860 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:10px;background:#f0f9ff;border:1px solid #bae6fd;">

  <!-- River bed curve -->
  <defs>
    <linearGradient id="riverGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#7dd3fc"/>
      <stop offset="100%" stop-color="#0ea5e9"/>
    </linearGradient>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#e0f2fe"/>
      <stop offset="100%" stop-color="#f0f9ff"/>
    </linearGradient>
    <linearGradient id="landGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#86efac"/>
      <stop offset="100%" stop-color="#4ade80"/>
    </linearGradient>
  </defs>

  <!-- Sky background -->
  <rect width="860" height="320" fill="url(#skyGrad)" rx="10"/>

  <!-- Land silhouette -->
  <polygon points="0,300 0,80 80,60 160,100 240,130 320,155 420,175 520,205 620,230 720,255 860,270 860,300"
           fill="url(#landGrad)" opacity="0.55"/>

  <!-- River channel -->
  <polyline points="0,82 80,62 160,102 240,132 320,157 420,177 520,207 620,232 720,257 860,272"
            fill="none" stroke="url(#riverGrad)" stroke-width="5" stroke-linecap="round"/>

  <!-- Zone labels -->
  <rect x="10" y="8" width="220" height="26" rx="5" fill="#1e3a8a" opacity="0.15"/>
  <text x="120" y="26" text-anchor="middle" font-size="13" fill="#1e3a8a" font-weight="bold">UPPER COURSE</text>
  <rect x="310" y="8" width="220" height="26" rx="5" fill="#7c3aed" opacity="0.12"/>
  <text x="420" y="26" text-anchor="middle" font-size="13" fill="#7c3aed" font-weight="bold">MIDDLE COURSE</text>
  <rect x="610" y="8" width="240" height="26" rx="5" fill="#0369a1" opacity="0.12"/>
  <text x="730" y="26" text-anchor="middle" font-size="13" fill="#0369a1" font-weight="bold">LOWER COURSE</text>

  <!-- Dividers -->
  <line x1="310" y1="8" x2="310" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/>
  <line x1="610" y1="8" x2="610" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/>

  <!-- ── Clickable markers ── -->

  <!-- 1. V-shaped Valley (upper ~x=80) -->
  <g class="lp-btn" onclick="showDef('vshaped')" style="cursor:pointer;">
    <circle class="lp-dot" cx="80" cy="62" r="9" fill="#dc2626"/>
    <line x1="80" y1="71" x2="80" y2="105" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="22" y="105" width="116" height="20" rx="4" fill="#dc2626" opacity="0.85"/>
    <text x="80" y="119" text-anchor="middle" font-size="11" fill="white" font-weight="bold">V-shaped Valley</text>
  </g>

  <!-- 2. Interlocking Spurs (upper ~x=155) -->
  <g class="lp-btn" onclick="showDef('spurs')" style="cursor:pointer;">
    <circle class="lp-dot" cx="165" cy="100" r="9" fill="#ea580c"/>
    <line x1="165" y1="109" x2="165" y2="140" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="107" y="140" width="116" height="20" rx="4" fill="#ea580c" opacity="0.85"/>
    <text x="165" y="154" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Interlocking Spurs</text>
  </g>

  <!-- 3. Pothole (upper ~x=230) -->
  <g class="lp-btn" onclick="showDef('pothole')" style="cursor:pointer;">
    <circle class="lp-dot" cx="237" cy="131" r="9" fill="#b45309"/>
    <line x1="237" y1="140" x2="237" y2="170" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="183" y="170" width="108" height="20" rx="4" fill="#b45309" opacity="0.85"/>
    <text x="237" y="184" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Pothole</text>
  </g>

  <!-- 4. Waterfall & Gorge (upper ~x=280) -->
  <g class="lp-btn" onclick="showDef('waterfall')" style="cursor:pointer;">
    <circle class="lp-dot" cx="285" cy="147" r="9" fill="#7c3aed"/>
    <line x1="285" y1="156" x2="285" y2="200" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="215" y="200" width="140" height="20" rx="4" fill="#7c3aed" opacity="0.85"/>
    <text x="285" y="214" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Waterfall &amp; Gorge</text>
  </g>

  <!-- 5. Meander (middle ~x=420) -->
  <g class="lp-btn" onclick="showDef('meander')" style="cursor:pointer;">
    <circle class="lp-dot" cx="420" cy="177" r="9" fill="#0891b2"/>
    <line x1="420" y1="186" x2="420" y2="220" stroke="#0891b2" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="370" y="220" width="100" height="20" rx="4" fill="#0891b2" opacity="0.85"/>
    <text x="420" y="234" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Meander</text>
  </g>

  <!-- 6. Oxbow Lake (middle ~x=530) -->
  <g class="lp-btn" onclick="showDef('oxbow')" style="cursor:pointer;">
    <circle class="lp-dot" cx="532" cy="207" r="9" fill="#0f766e"/>
    <line x1="532" y1="216" x2="532" y2="250" stroke="#0f766e" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="474" y="250" width="116" height="20" rx="4" fill="#0f766e" opacity="0.85"/>
    <text x="532" y="264" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Oxbow Lake</text>
  </g>

  <!-- 7. Floodplain & Levée (lower ~x=650) -->
  <g class="lp-btn" onclick="showDef('floodplain')" style="cursor:pointer;">
    <circle class="lp-dot" cx="650" cy="232" r="9" fill="#1d4ed8"/>
    <line x1="650" y1="241" x2="650" y2="182" stroke="#1d4ed8" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="580" y="162" width="140" height="20" rx="4" fill="#1d4ed8" opacity="0.85"/>
    <text x="650" y="176" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Floodplain &amp; Levée</text>
  </g>

  <!-- 8. Braided Channel (lower ~x=740) -->
  <g class="lp-btn" onclick="showDef('braided')" style="cursor:pointer;">
    <circle class="lp-dot" cx="742" cy="257" r="9" fill="#b45309"/>
    <line x1="742" y1="266" x2="742" y2="210" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="672" y="190" width="140" height="20" rx="4" fill="#b45309" opacity="0.85"/>
    <text x="742" y="204" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Braided Channel</text>
  </g>

  <!-- 9. Delta (lower ~x=830) -->
  <g class="lp-btn" onclick="showDef('delta')" style="cursor:pointer;">
    <circle class="lp-dot" cx="835" cy="271" r="9" fill="#065f46"/>
    <line x1="835" y1="262" x2="835" y2="140" stroke="#065f46" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="785" y="120" width="70" height="20" rx="4" fill="#065f46" opacity="0.85"/>
    <text x="820" y="134" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Delta</text>
  </g>

  <!-- Source & Mouth labels -->
  <text x="12" y="300" font-size="12" fill="#475569" font-style="italic">Source ▲</text>
  <text x="800" y="300" font-size="12" fill="#475569" font-style="italic">▼ Mouth / Sea</text>
</svg>

<!-- Definition panel -->
<div id="def-panel">
  <h4 id="def-title"></h4>
  <p id="def-body"></p>
</div>
</div>

<script>
const DEFS = {
  vshaped: {
    title: "V-shaped Valley",
    body: "Formed in the upper course where vertical erosion dominates. The river cuts downward through the rock, creating a steep-sided V-shaped valley. Gravity causes the valley walls to collapse and weather, adding debris to the river."
  },
  spurs: {
    title: "Interlocking Spurs",
    body: "Ridges of hard rock that jut out alternately from each side of the valley. The river lacks the energy to cut through them and instead winds around them, creating an interlocking pattern when viewed from above."
  },
  pothole: {
    title: "Pothole",
    body: "A circular hole drilled into the riverbed. Pebbles are caught in small hollows and swirled around by turbulent water, grinding (abrasion) the rock beneath into a smooth, cylindrical pit."
  },
  waterfall: {
    title: "Waterfall & Gorge",
    body: "Formed where a band of hard rock overlies softer rock. The softer rock is eroded faster, undercutting the hard rock overhang. The overhang collapses into the plunge pool below. Over time the waterfall retreats upstream, leaving a steep-sided gorge. Example: Niagara Falls."
  },
  meander: {
    title: "Meander",
    body: "A bend in the river in the middle/lower course. The fastest flow swings to the outside bend, eroding a river cliff. On the inside bend, slow flow deposits a slip-off slope (point bar). The bends migrate and grow over time."
  },
  oxbow: {
    title: "Oxbow Lake",
    body: "The neck of a tight meander is cut through during a flood, and the river takes the shorter straight path. Deposition seals off the old loop, leaving a curved oxbow lake (billabong). It gradually silts up into a marsh."
  },
  floodplain: {
    title: "Floodplain & Levée",
    body: "The wide, flat valley floor built up by repeated floods. Fine alluvium is deposited across the floodplain each time the river overtops its banks. The coarsest sediment settles first, nearest the channel, building raised natural levées on both banks."
  },
  braided: {
    title: "Braided Channel",
    body: "When a river carries more sediment than it can transport (e.g., after glacial melt), it deposits mid-channel bars that split the flow into a network of interwoven channels separated by temporary islands."
  },
  delta: {
    title: "Delta",
    body: "Where a river meets a calm sea or lake, velocity drops to zero and all sediment is deposited. Distributaries fan out across the growing deposit. Example: Rhône Delta (Camargue), France. Deltas only form when deposition > removal by waves/tides."
  }
};

function showDef(key) {
  const panel = document.getElementById('def-panel');
  const t = document.getElementById('def-title');
  const b = document.getElementById('def-body');
  if (panel.style.display === 'block' && t.textContent === DEFS[key].title) {
    panel.style.display = 'none';
    return;
  }
  t.textContent = DEFS[key].title;
  b.textContent = DEFS[key].body;
  panel.style.display = 'block';
}
</script>

<!-- ═══════════════ SECTION 1: UPLAND LANDFORMS ═══════════════ -->
<h2>🏔️ Section 1: Upland Landforms (Upper Course)</h2>
<div class="info-box">
  <strong>Dominant process:</strong> <b style="color:#9333ea">Vertical erosion</b> — the river cuts downward into the bedrock. The gradient is steep, the channel is narrow, and the river transports large, angular boulders by <b style="color:#9333ea">traction</b> and <b style="color:#9333ea">saltation</b>.
</div>

<h3>V-shaped Valley &amp; Interlocking Spurs</h3>
<p>
  As the river erodes downward, the valley floor deepens. Weathering and mass movement on the exposed valley walls supply material that the river carries away. This creates a characteristic <b style="color:#9333ea">V-shaped cross profile</b>. Because the river lacks the power to erode sideways through hard rock outcrops, it winds around them. The ridges that jut into the valley from alternate sides are called <b style="color:#9333ea">interlocking spurs</b>.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig118.png" alt="V-shaped valley and interlocking spurs photo"/>
<p class="caption">Fig. 118 — V-shaped valley with interlocking spurs (photograph)</p>

<h3>Potholes</h3>
<p>
  In turbulent upper-course water, pebbles become trapped in small depressions on the riverbed. The swirling current drills these pebbles around in circles, grinding the rock by <b style="color:#9333ea">abrasion</b> into smooth, cylindrical <b style="color:#9333ea">potholes</b>. Over time potholes can be metres deep and are clear evidence of the river's erosive power.
</p>

<h3>Waterfalls &amp; Gorges</h3>
<p>
  A waterfall develops where the river crosses a band of <b style="color:#9333ea">resistant (hard) rock</b> overlying <b style="color:#9333ea">less resistant (soft) rock</b>:
</p>
<ol>
  <li>The softer rock erodes faster, undercutting the hard rock to form an <b style="color:#9333ea">overhang</b>.</li>
  <li>A <b style="color:#9333ea">plunge pool</b> is scoured at the base by <b style="color:#9333ea">hydraulic action</b> and abrasion.</li>
  <li>The unsupported overhang collapses; the waterfall retreats upstream.</li>
  <li>Repeated retreat leaves a steep-sided <b style="color:#9333ea">gorge of recession</b> downstream.</li>
</ol>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig121.png" alt="Waterfall and gorge formation diagram"/>
<p class="caption">Fig. 121 — Formation of a waterfall and gorge (diagram). Example: Niagara Falls, USA/Canada.</p>

<!-- ═══════════════ SECTION 2: LOWLAND LANDFORMS ═══════════════ -->
<h2>🌾 Section 2: Lowland Landforms (Middle &amp; Lower Course)</h2>
<div class="info-box">
  <strong>Dominant processes:</strong> <b style="color:#9333ea">Lateral erosion</b> widens the valley in the middle course; <b style="color:#9333ea">deposition</b> dominates in the lower course as gradient decreases and the river loses energy. Sediment (<b style="color:#9333ea">alluvium</b>) is dropped across the floodplain.
</div>

<h3>Meanders</h3>
<p>
  On the gentle gradient of the middle course, the river swings into bends called <b style="color:#9333ea">meanders</b>. The fastest flow is pushed to the <b style="color:#9333ea">outside of each bend</b> where it undercuts the bank, forming a steep <b style="color:#9333ea">river cliff</b>. On the <b style="color:#9333ea">inside bend</b>, flow is slowest and material is deposited to form a gently sloping <b style="color:#9333ea">slip-off slope</b> (point bar). The meander migrates and grows over time.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig125.png" alt="Meander formation diagram"/>
<p class="caption">Fig. 125 — Meander cross-section showing river cliff and slip-off slope</p>

<h3>Oxbow Lakes</h3>
<p>
  As a meander becomes very tight, the neck of land between loops narrows. During a <b style="color:#9333ea">flood</b>, the river breaks through the neck and takes the shorter, straighter path. <b style="color:#9333ea">Deposition</b> seals off the ends of the old loop, isolating it as a curved <b style="color:#9333ea">oxbow lake</b>. Cut off from the main river, it slowly silts up and becomes a marshy hollow.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig128.png" alt="Oxbow lake formation diagram"/>
<p class="caption">Fig. 128 — Stages in the formation of an oxbow lake</p>

<h3>Floodplains &amp; Levées</h3>
<p>
  The <b style="color:#9333ea">floodplain</b> is the wide, flat valley floor built up by layers of <b style="color:#9333ea">alluvium</b> deposited during repeated floods. When the river overtops its banks, it immediately loses velocity; the coarsest sediment is dropped first, right beside the channel, gradually building raised ridges called <b style="color:#9333ea">natural levées</b>. Finer silt spreads further across the floodplain.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig129.png" alt="Floodplain and levée diagram"/>
<p class="caption">Fig. 129 — Cross-section of a floodplain showing natural levées</p>

<h3>Braided Channels</h3>
<p>
  When a river carries an exceptionally high <b style="color:#9333ea">sediment load</b> (e.g., meltwater rivers downstream of glaciers), it cannot transport all the material and begins to deposit <b style="color:#9333ea">mid-channel bars</b>. These bars split the flow into a network of shallow, interweaving channels — a <b style="color:#9333ea">braided channel</b>. Common in semi-arid environments and near glaciers.
</p>

<h3>Deltas</h3>
<p>
  Where a river reaches a <b style="color:#9333ea">sea or lake</b> with little wave or tidal energy, velocity drops to nearly zero and all remaining sediment is deposited. The river splits into a fan of <b style="color:#9333ea">distributaries</b> spreading across the growing deposit. The classic shape is triangular (like the Greek letter Δ). Example: the <b style="color:#9333ea">Rhône Delta (Camargue), France</b>.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig132.png" alt="Delta formation diagram"/>
<p class="caption">Fig. 132 — Delta formation showing distributaries fanning out into the sea. Example: Rhône Delta, France.</p>

<!-- ═══════════════ SUMMARY TABLE ═══════════════ -->
<h2>📋 Summary Table</h2>
<table>
  <thead>
    <tr>
      <th>Landform</th>
      <th>Location in River</th>
      <th>Dominant Process</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>V-shaped Valley</td><td>Upper course</td><td>Vertical erosion</td></tr>
    <tr><td>Interlocking Spurs</td><td>Upper course</td><td>Vertical erosion (river avoids hard rock)</td></tr>
    <tr><td>Pothole</td><td>Upper course</td><td>Abrasion (corrasion)</td></tr>
    <tr><td>Waterfall &amp; Gorge</td><td>Upper course</td><td>Hydraulic action + abrasion + rock collapse</td></tr>
    <tr><td>Meander</td><td>Middle course</td><td>Lateral erosion + deposition</td></tr>
    <tr><td>Oxbow Lake</td><td>Middle course</td><td>Erosion (neck cut-off) + deposition</td></tr>
    <tr><td>Floodplain</td><td>Middle / Lower course</td><td>Deposition (alluvium)</td></tr>
    <tr><td>Natural Levée</td><td>Middle / Lower course</td><td>Deposition (coarse sediment beside channel)</td></tr>
    <tr><td>Braided Channel</td><td>Lower course</td><td>Deposition (excess sediment load)</td></tr>
    <tr><td>Delta</td><td>Lower course (mouth)</td><td>Deposition (velocity → zero)</td></tr>
  </tbody>
</table>

</body>
</html>"""

url = f"{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{PAGE_ID}"
headers = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}
payload = json.dumps({"content_html": HTML_CONTENT})
resp = requests.patch(url, headers=headers, data=payload)
print(f"Status: {resp.status_code}")
if resp.text:
    print(f"Response: {resp.text}")
else:
    print("Upload successful — no content returned (expected for Prefer: return=minimal).")
