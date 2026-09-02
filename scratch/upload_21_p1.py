import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = '4d3d8e74-308a-45b3-a271-300ca98aa673'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/'

html = """<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">

<!-- Header -->
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#0369a1;font-size:30px;margin-bottom:10px;border-bottom:3px solid #38bdf8;display:inline-block;padding-bottom:10px;">🌊 2.1 Physical Processes that Shape the Coast</h1>
<p style="color:#64748b;font-size:16px;">Erosion, transportation, deposition and longshore drift</p>
</div>

<!-- Section 1: Factors -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🌍 1. Factors Affecting Coastal Processes</h2>
<p style="color:#475569;margin-bottom:14px;">Coastal processes and landforms are shaped by four key factors that interact to create unique coastlines worldwide:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:18px;">
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:14px;border-radius:6px;">
<strong style="color:#0369a1;">🌊 Waves &amp; Currents</strong><br/>
<span style="color:#475569;font-size:14px;">The dominant shaping agent. Include longshore drift, tidal currents and wave energy. Wave type determines whether erosion or deposition is the dominant process.</span>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">
<strong style="color:#15803d;">🪨 Local Geology</strong><br/>
<span style="color:#475569;font-size:14px;">Rock type, structure and strength determine how quickly a coast erodes. Hard rocks (granite) resist erosion; soft rocks (clay, chalk) erode quickly.</span>
</div>
<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:14px;border-radius:6px;">
<strong style="color:#92400e;">📈 Sea Level Changes</strong><br/>
<span style="color:#475569;font-size:14px;">Both local (isostatic) and global (eustatic) changes. Rising sea levels increase coastal flooding and erosion. Global warming accelerates sea level rise (~3 mm/year globally).</span>
</div>
<div style="background:#fdf4ff;border-left:4px solid #a855f7;padding:14px;border-radius:6px;">
<strong style="color:#7e22ce;">🏗️ Human Activity</strong><br/>
<span style="color:#475569;font-size:14px;">Coastal engineering (sea walls, groynes), urban development and deforestation change how coasts respond to natural processes.</span>
</div>
</div>
</div>

<!-- Section 2: Erosion - Interactive SVG tabs -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚡ 2. Coastal Erosion — 4 Types</h2>
<p style="color:#475569;margin-bottom:16px;">Waves erode coastlines through four distinct processes. Click each type to learn more:</p>

<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px;">
<button onclick="showErosion('hydraulic')" style="background:#0369a1;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;">🌊 Hydraulic Action</button>
<button onclick="showErosion('abrasion')" style="background:#0284c7;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;">🪨 Corrasion</button>
<button onclick="showErosion('attrition')" style="background:#0ea5e9;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;">💥 Attrition</button>
<button onclick="showErosion('solution')" style="background:#38bdf8;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;">🧪 Corrosion</button>
</div>

<div id="erosion-panel" style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:20px;min-height:120px;">
<p style="color:#64748b;font-style:italic;">👆 Click a process above to see details</p>
</div>

<div id="erosion-hydraulic" style="display:none;">
<h3 style="color:#0369a1;margin-bottom:8px;">🌊 Hydraulic Action</h3>
<p style="color:#475569;">Waves crash against the cliff face, trapping and compressing air in cracks and joints. As the wave retreats, the sudden pressure release causes an <strong>explosive force</strong> that breaks off rock fragments. This is the most powerful erosion type during storms. Over time, the repeated compression and explosion widens joints until large blocks fall.</p>
<p style="color:#475569;margin-top:8px;font-size:14px;">💡 <em>Most effective in well-jointed rocks like limestone, sandstone and granite, and in weak rocks like clays during storm conditions.</em></p>
</div>
<div id="erosion-abrasion" style="display:none;">
<h3 style="color:#0369a1;margin-bottom:8px;">🪨 Corrasion (Abrasion)</h3>
<p style="color:#475569;">Waves use sand, pebbles and shingle as <strong>tools of erosion</strong>, hurling them against the cliff face. This abrasive action is similar to sandpaper, grinding and scratching the rock surface. It is most effective at the base of cliffs during breaking waves and creates smooth, scratched surfaces called <em>slickensides</em>.</p>
<p style="color:#475569;margin-top:8px;font-size:14px;">💡 <em>The load carried by the wave determines the erosional power — coarser material is more effective.</em></p>
</div>
<div id="erosion-attrition" style="display:none;">
<h3 style="color:#0369a1;margin-bottom:8px;">💥 Attrition</h3>
<p style="color:#475569;">Rock fragments and pebbles transported by waves <strong>collide with each other</strong> as they are rolled around by wave action. This causes them to chip, break and gradually become smaller, more rounded and smoother. This is why beach pebbles are smooth and rounded — they have been worn down over many years. Materials gradually reduce from boulders → cobbles → pebbles → sand grains.</p>
</div>
<div id="erosion-solution" style="display:none;">
<h3 style="color:#0369a1;margin-bottom:8px;">🧪 Corrosion (Solution)</h3>
<p style="color:#475569;">Seawater is <strong>slightly acidic</strong> (due to dissolved CO₂ forming carbonic acid). This acid dissolves certain rock types, particularly <strong>limestone and chalk</strong>, which contain calcium carbonate. The rock is not mechanically broken — it dissolves chemically into the water. Produces smooth, honeycombed surfaces. Example: chalk cliffs of southern England.</p>
</div>

<script>
function showErosion(type) {
  ['hydraulic','abrasion','attrition','solution'].forEach(function(t){
    document.getElementById('erosion-'+t).style.display='none';
  });
  document.getElementById('erosion-panel').style.display='none';
  document.getElementById('erosion-'+type).style.display='block';
}
</script>

<div style="margin-top:20px;">
<img src="{IMG}2_1_fig22.png" alt="Hydraulic action on a coral coastline" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.2 Hydraulic action on a coral coastline — waves compress air in rock crevices with explosive force</p>
</div>
</div>

<!-- Section 3: Transportation -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🚚 3. Coastal Transportation</h2>
<p style="color:#475569;margin-bottom:16px;">Coastal transportation moves sediment in two main ways depending on particle size and current strength:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:18px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🏖️ Bedload Transport</h3>
<p style="color:#475569;font-size:15px;margin-bottom:10px;">Larger particles that move <em>along the seabed</em> in continuous or discontinuous contact:</p>
<ul style="color:#475569;font-size:14px;padding-left:20px;margin:0;">
<li style="margin-bottom:6px;"><strong>Traction</strong>: Large particles (boulders, cobbles) roll or slide along the seabed under the force of strong currents</li>
<li><strong>Saltation</strong>: Medium particles (sand, pebbles) bounce along the seabed in a series of hops when moderate currents lift them briefly off the bottom</li>
</ul>
</div>
<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:18px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🌀 Suspended Load</h3>
<p style="color:#475569;font-size:15px;margin-bottom:10px;">Fine particles that are <em>carried within the water body</em> by turbulent flow:</p>
<ul style="color:#475569;font-size:14px;padding-left:20px;margin:0;">
<li style="margin-bottom:6px;"><strong>Suspension</strong>: Very fine particles (clay, silt) are held up by turbulent water and can travel long distances before settling</li>
<li><strong>Solution</strong>: Dissolved minerals (e.g. calcium carbonate from limestone) transported invisibly in the water</li>
</ul>
</div>
</div>
</div>

<!-- Section 4: Deposition -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⬇️ 4. Deposition</h2>
<p style="color:#475569;margin-bottom:14px;">Deposition occurs when wave energy or velocity <strong>decreases</strong> and the water can no longer carry its sediment load. The heavier, larger particles are deposited first; fine clay travels furthest before settling.</p>
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:16px;border-radius:6px;margin-bottom:16px;">
<strong style="color:#0369a1;">Conditions favouring deposition:</strong>
<ul style="color:#475569;margin-top:8px;padding-left:20px;font-size:15px;">
<li>Waves entering sheltered water — bays, estuaries, lagoons</li>
<li>Calm weather reducing wave energy</li>
<li>Gently sloping shoreline increasing friction</li>
<li>Obstacles (groynes, headlands) causing waves to break</li>
<li>Rivers meeting the sea — velocity drops suddenly</li>
</ul>
</div>
<p style="color:#475569;font-size:14px;font-style:italic;">📌 <strong>Deposition sequence</strong>: Boulders → Cobbles → Pebbles → Sand → Silt → Clay (finest travels furthest)</p>
</div>

<!-- Section 5: Longshore Drift - Interactive SVG -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">➡️ 5. Longshore Drift</h2>
<p style="color:#475569;margin-bottom:16px;"><strong>Longshore drift (LSD)</strong> is the net movement of sediment <em>along</em> the coastline. It occurs because waves rarely approach the shore at a perfect right angle — instead they approach at an angle determined by the prevailing wind direction.</p>

<!-- SVG Longshore Drift Diagram -->
<div style="background:#e0f2fe;border-radius:12px;padding:16px;margin-bottom:16px;overflow-x:auto;">
<svg width="700" height="280" viewBox="0 0 700 280" style="max-width:100%;display:block;margin:0 auto;">
  <!-- Sea -->
  <rect x="0" y="0" width="700" height="200" fill="#bae6fd"/>
  <!-- Beach -->
  <polygon points="0,160 700,140 700,280 0,280" fill="#fde68a"/>
  <!-- Shoreline -->
  <line x1="0" y1="160" x2="700" y2="140" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Wave lines (approaching at angle) -->
  <line x1="0" y1="60" x2="600" y2="10" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
  <line x1="0" y1="100" x2="650" y2="55" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
  <line x1="0" y1="130" x2="680" y2="90" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
  <!-- Swash arrows (diagonal up beach) -->
  <line x1="80" y1="175" x2="200" y2="160" stroke="#f97316" stroke-width="3" marker-end="url(#arrowO)"/>
  <line x1="230" y1="173" x2="350" y2="158" stroke="#f97316" stroke-width="3" marker-end="url(#arrowO)"/>
  <line x1="380" y1="170" x2="500" y2="156" stroke="#f97316" stroke-width="3" marker-end="url(#arrowO)"/>
  <!-- Backwash arrows (straight down) -->
  <line x1="200" y1="160" x2="200" y2="176" stroke="#60a5fa" stroke-width="3" marker-end="url(#arrowB)"/>
  <line x1="350" y1="158" x2="350" y2="174" stroke="#60a5fa" stroke-width="3" marker-end="url(#arrowB)"/>
  <line x1="500" y1="156" x2="500" y2="172" stroke="#60a5fa" stroke-width="3" marker-end="url(#arrowB)"/>
  <!-- Net drift arrow -->
  <line x1="60" y1="220" x2="620" y2="205" stroke="#16a34a" stroke-width="5" marker-end="url(#arrowG)"/>
  <!-- Pebble path zigzag -->
  <polyline points="70,176 190,162 190,177 330,160 330,175 470,158 470,173 600,156" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,3"/>
  <!-- Labels -->
  <text x="120" y="148" fill="#ea580c" font-size="11" font-weight="bold">SWASH</text>
  <text x="195" y="195" fill="#2563eb" font-size="11" font-weight="bold">BACKWASH</text>
  <text x="260" y="240" fill="#15803d" font-size="13" font-weight="bold">⟶ Net Longshore Drift</text>
  <text x="20" y="25" fill="#0369a1" font-size="12">Waves</text>
  <text x="20" y="42" fill="#0369a1" font-size="11">(prevailing wind)</text>
  <text x="590" y="130" fill="#92400e" font-size="11">BEACH</text>
  <text x="20" y="100" fill="#1e40af" font-size="11">SEA</text>
  <!-- Groyne -->
  <rect x="430" y="160" width="8" height="80" fill="#475569"/>
  <text x="415" y="255" fill="#475569" font-size="10">Groyne</text>
  <!-- Defs -->
  <defs>
    <marker id="arrowO" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#f97316"/></marker>
    <marker id="arrowB" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#60a5fa"/></marker>
    <marker id="arrowG" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L10,3 z" fill="#16a34a"/></marker>
  </defs>
</svg>
<p style="text-align:center;font-size:12px;color:#64748b;margin-top:8px;">Interactive diagram — orange = swash, blue = backwash, green = net sediment drift, red dashed = pebble path</p>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">
<strong style="color:#15803d;">How it works:</strong>
<ol style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;">
<li>Wave approaches beach at an angle (direction of prevailing wind)</li>
<li>Swash carries sediment diagonally up the beach</li>
<li>Backwash drags sediment straight back down the beach (gravity)</li>
<li>Net result: sediment moves step by step along the shore</li>
</ol>
</div>
<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:14px;border-radius:6px;">
<strong style="color:#92400e;">Management — Groynes:</strong>
<p style="color:#475569;margin-top:8px;font-size:14px;">Groynes are wooden/rock barriers built <em>perpendicular</em> to the shore. They trap sediment on the updrift side, building up the beach. However, they starve beaches downdrift of sediment.</p>
</div>
</div>

<img src="{IMG}2_1_fig23.png" alt="Longshore drift diagram" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.3 Longshore drift — swash moves sediment diagonally, backwash returns it perpendicular to shore</p>
</div>

<!-- Section 6: Wave Types -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🏄 6. Wave Types: Constructive vs Destructive</h2>
<p style="color:#475569;margin-bottom:16px;">Not all waves are the same. The type of wave determines whether a beach is built up (deposition) or broken down (erosion):</p>

<img src="{IMG}2_1_fig26.png" alt="Constructive and destructive waves" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.6 Constructive waves (top) and destructive waves (bottom) compared</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px;">
<div style="background:#f0fdf4;border:2px solid #22c55e;border-radius:10px;padding:18px;">
<h3 style="color:#15803d;margin-bottom:10px;">✅ Constructive Waves</h3>
<ul style="color:#475569;font-size:14px;padding-left:18px;margin:0;">
<li style="margin-bottom:6px;">Long wavelength, <strong>low height</strong></li>
<li style="margin-bottom:6px;">Low beach gradient</li>
<li style="margin-bottom:6px;"><strong>Elliptical</strong> orbital motion</li>
<li style="margin-bottom:6px;"><strong>Strong swash &gt; weak backwash</strong></li>
<li style="margin-bottom:6px;">Dominant process: <strong>Deposition</strong> 🏖️</li>
<li>Associated with distant weather (swell waves)</li>
</ul>
</div>
<div style="background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:18px;">
<h3 style="color:#dc2626;margin-bottom:10px;">⚡ Destructive Waves</h3>
<ul style="color:#475569;font-size:14px;padding-left:18px;margin:0;">
<li style="margin-bottom:6px;">Short wavelength, <strong>high height</strong></li>
<li style="margin-bottom:6px;">Steep beach gradient</li>
<li style="margin-bottom:6px;"><strong>Circular</strong> orbital motion</li>
<li style="margin-bottom:6px;"><strong>Weak swash &lt; strong backwash</strong></li>
<li style="margin-bottom:6px;">Dominant process: <strong>Erosion</strong> ⚡</li>
<li>Associated with local storms (wind waves)</li>
</ul>
</div>
</div>

<!-- Summary Table -->
<div style="overflow-x:auto;margin-top:20px;">
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<tr style="background:#0369a1;color:white;"><th style="padding:10px;text-align:left;">Feature</th><th style="padding:10px;">Constructive</th><th style="padding:10px;">Destructive</th></tr>
<tr style="background:#f0fdf4;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;font-weight:600;">Wavelength</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Long</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Short</td></tr>
<tr style="background:#ffffff;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;font-weight:600;">Wave height</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Low</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">High</td></tr>
<tr style="background:#f0fdf4;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;font-weight:600;">Beach gradient</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Low / Gentle</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Steep</td></tr>
<tr style="background:#ffffff;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;font-weight:600;">Orbital motion</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Elliptical</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Circular</td></tr>
<tr style="background:#f0fdf4;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;font-weight:600;">Swash vs Backwash</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;color:#15803d;">Swash &gt; Backwash ✅</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;color:#dc2626;">Backwash &gt; Swash ⚡</td></tr>
<tr style="background:#ffffff;"><td style="padding:9px;font-weight:600;">Main process</td><td style="padding:9px;text-align:center;color:#15803d;font-weight:bold;">Deposition</td><td style="padding:9px;text-align:center;color:#dc2626;font-weight:bold;">Erosion</td></tr>
</table>
</div>
</div>

</div>"""

html = html.replace('{IMG}', IMG)
print(f'HTML length: {len(html)} chars')

r = requests.patch(
    f'{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{PAGE_ID}',
    json={'content_html': html},
    headers={'apikey': KEY,'Authorization':f'Bearer {KEY}','Content-Type':'application/json','Prefer':'return=minimal'}
)
print(f'PATCH 2.1 P1: HTTP {r.status_code}')
