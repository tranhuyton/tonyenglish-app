import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = '90d85cb0-b984-4083-864a-8ead0c4119f7'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/'

html = """<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">

<!-- Header -->
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#1e3a8a;font-size:30px;margin-bottom:10px;border-bottom:3px solid #60a5fa;display:inline-block;padding-bottom:10px;">🌊 1.1 Hydrological Characteristics &amp; Processes</h1>
<p style="color:#64748b;font-size:16px;">Rivers, drainage basins, the water cycle and fluvial processes</p>
</div>

<!-- Section 1: Drainage Basins -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">📍 1. Rivers &amp; Drainage Basins</h2>
<p style="color:#475569;margin-bottom:14px;">A <strong>drainage basin</strong> is the area of land drained by a river and all its tributaries. It is an <strong>open system</strong> with inputs (precipitation) and outputs (evaporation, river discharge to sea). The boundary of a drainage basin is called the <strong>watershed</strong> — usually following a ridge of high ground.</p>

<!-- Key Terms Grid -->
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px;">
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Source</strong><br/><span style="color:#475569;font-size:13px;">Where the river begins — usually on high ground (bog, spring)</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Mouth</strong><br/><span style="color:#475569;font-size:13px;">Where the river meets the sea, a lake, or another river</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Tributary</strong><br/><span style="color:#475569;font-size:13px;">A smaller river or stream that flows into the main river</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Confluence</strong><br/><span style="color:#475569;font-size:13px;">The point where two rivers join</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Watershed</strong><br/><span style="color:#475569;font-size:13px;">The boundary/ridge separating one drainage basin from another</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Flood plain</strong><br/><span style="color:#475569;font-size:13px;">Flat land beside the river, flooded when discharge is high</span>
</div>
</div>

<img src="{IMG}hq_real_fig1_1_cropped_v3.jpeg" alt="Drainage basin features" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.1 The features of a drainage basin</p>
<img src="{IMG}hq_fig1_2.jpeg" alt="Cross-section of drainage basins" style="max-width:420px;height:auto;display:block;margin:0 auto;margin-top:16px;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.2 Cross-section showing drainage basins and watersheds</p>
</div>

<!-- Section 2: Bradshaw Model -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">📉 2. The Bradshaw Model — How Rivers Change Downstream</h2>
<p style="color:#475569;margin-bottom:16px;">The <strong>Bradshaw Model</strong> shows how river characteristics change systematically from source to mouth as discharge increases. Understanding these changes helps explain why different landforms occur in different parts of a river.</p>

<!-- Bradshaw SVG diagram -->
<div style="background:#f8fafc;border-radius:12px;padding:16px;margin-bottom:16px;overflow-x:auto;">
<svg width="680" height="200" viewBox="0 0 680 200" style="max-width:100%;display:block;margin:0 auto;">
  <!-- Axes -->
  <line x1="60" y1="20" x2="60" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="60" y1="170" x2="640" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <!-- Labels -->
  <text x="30" y="100" fill="#64748b" font-size="11" transform="rotate(-90,30,100)" text-anchor="middle">River characteristic</text>
  <text x="350" y="195" fill="#64748b" font-size="12" text-anchor="middle">← Source (upper) ──────────────── Mouth (lower) →</text>
  <!-- Increasing lines (discharge, width, depth, velocity) -->
  <path d="M 70,155 Q 350,140 620,60" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="625" y="57" fill="#3b82f6" font-size="11">Discharge ↑</text>
  <path d="M 70,160 Q 350,148 620,80" fill="none" stroke="#6366f1" stroke-width="2"/>
  <text x="625" y="78" fill="#6366f1" font-size="11">Width &amp; Depth ↑</text>
  <path d="M 70,165 Q 350,155 620,100" fill="none" stroke="#22c55e" stroke-width="2"/>
  <text x="625" y="98" fill="#22c55e" font-size="11">Velocity ↑</text>
  <!-- Decreasing lines (particle size, channel roughness) -->
  <path d="M 70,50 Q 350,100 620,150" fill="none" stroke="#f97316" stroke-width="2.5" stroke-dasharray="6,3"/>
  <text x="5" y="48" fill="#f97316" font-size="11">Particle</text>
  <text x="5" y="60" fill="#f97316" font-size="11">size ↓</text>
  <path d="M 70,35 Q 350,80 620,140" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6,3"/>
  <text x="5" y="33" fill="#94a3b8" font-size="11">Roughness</text>
  <text x="5" y="45" fill="#94a3b8" font-size="11">↓</text>
</svg>
<p style="text-align:center;font-size:11px;color:#64748b;margin-top:6px;">Solid lines = increasing downstream; Dashed lines = decreasing downstream</p>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">
<strong style="color:#15803d;">Increase downstream ↑</strong>
<ul style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;margin-bottom:0;">
<li>Discharge (more tributaries join)</li>
<li>Channel width &amp; depth</li>
<li>Velocity (smoother bed)</li>
<li>Load volume (more input)</li>
</ul>
</div>
<div style="background:#fff7ed;border-left:4px solid #f97316;padding:14px;border-radius:6px;">
<strong style="color:#ea580c;">Decrease downstream ↓</strong>
<ul style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;margin-bottom:0;">
<li>Gradient/slope</li>
<li>Particle size (attrition rounds them)</li>
<li>Channel roughness</li>
<li>Valley sides become gentler</li>
</ul>
</div>
</div>

<img src="{IMG}hq_fig1_10.jpeg" alt="Bradshaw model and river profiles" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.10 The Bradshaw model — river characteristics from source to mouth</p>
</div>

<!-- Section 3: Water Cycle -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🔄 3. The Drainage Basin Water Cycle</h2>
<p style="color:#475569;margin-bottom:16px;">The water cycle within a drainage basin describes how water moves from the atmosphere, through the land, and back. It has <strong>inputs</strong>, <strong>stores</strong>, <strong>transfers</strong>, and <strong>outputs</strong>. Click each process to learn more:</p>

<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;">
<button onclick="showWater('precip')" style="background:#3b82f6;color:white;border:none;padding:8px 14px;border-radius:16px;cursor:pointer;font-size:13px;">🌧️ Precipitation</button>
<button onclick="showWater('interception')" style="background:#22c55e;color:white;border:none;padding:8px 14px;border-radius:16px;cursor:pointer;font-size:13px;">🌿 Interception</button>
<button onclick="showWater('runoff')" style="background:#06b6d4;color:white;border:none;padding:8px 14px;border-radius:16px;cursor:pointer;font-size:13px;">💧 Surface Runoff</button>
<button onclick="showWater('infiltration')" style="background:#8b5cf6;color:white;border:none;padding:8px 14px;border-radius:16px;cursor:pointer;font-size:13px;">⬇️ Infiltration</button>
<button onclick="showWater('groundwater')" style="background:#64748b;color:white;border:none;padding:8px 14px;border-radius:16px;cursor:pointer;font-size:13px;">🪨 Groundwater</button>
<button onclick="showWater('et')" style="background:#f59e0b;color:white;border:none;padding:8px 14px;border-radius:16px;cursor:pointer;font-size:13px;">☀️ Evapotranspiration</button>
</div>

<div id="water-default" style="background:#f0f9ff;border:2px solid #bfdbfe;border-radius:10px;padding:16px;margin-bottom:16px;">
<p style="color:#64748b;font-style:italic;text-align:center;">👆 Click a process to learn how it works</p>
</div>
<div id="water-precip" style="display:none;background:#f0f9ff;border:2px solid #bfdbfe;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#1d4ed8;">🌧️ Precipitation</h3>
<p style="color:#475569;">The main <strong>input</strong> into the drainage basin system. Includes rain, snow, sleet, and hail. Intensity and type of precipitation affects how quickly water enters the system. Heavy rain on saturated ground leads to rapid surface runoff; steady rain on dry, vegetated slopes infiltrates more slowly.</p>
</div>
<div id="water-interception" style="display:none;background:#f0fdf4;border:2px solid #86efac;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#15803d;">🌿 Interception</h3>
<p style="color:#475569;">Precipitation is <strong>caught by vegetation</strong> (leaves, branches) before reaching the ground. Some evaporates directly from leaf surfaces. Forests can intercept up to 35% of annual rainfall. Reduces overland flow and slows water reaching the river — important for flood prevention.</p>
</div>
<div id="water-runoff" style="display:none;background:#ecfeff;border:2px solid #67e8f9;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#0891b2;">💧 Surface Runoff (Overland Flow)</h3>
<p style="color:#475569;">Water flows over the surface when <strong>precipitation rate exceeds infiltration rate</strong> (soil is saturated or impermeable). This is the fastest route to the river channel — causes rapid rise in river discharge. Urban areas with tarmac and concrete have very high surface runoff. Related process: <em>throughflow</em> (water moving laterally through the soil above an impermeable layer) and <em>percolation</em> (water moving down through soil into rock).</p>
</div>
<div id="water-infiltration" style="display:none;background:#fdf4ff;border:2px solid #d8b4fe;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#7c3aed;">⬇️ Infiltration, Throughflow &amp; Percolation</h3>
<p style="color:#475569;"><strong>Infiltration</strong>: Water soaks into the soil from the surface. Rate depends on soil type, vegetation cover, and whether soil is already saturated. <strong>Throughflow</strong>: Water moves laterally (sideways) through the soil, above an impermeable layer, toward the river. Slower than overland flow. <strong>Percolation</strong>: Water seeps deeper through soil into bedrock, recharging groundwater stores.</p>
</div>
<div id="water-groundwater" style="display:none;background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#334155;">🪨 Groundwater Flow &amp; Storage</h3>
<p style="color:#475569;"><strong>Groundwater</strong> is water stored in rock (aquifer) below the water table. It moves very slowly toward the river as <strong>groundwater flow (baseflow)</strong> — this is what keeps rivers flowing during dry periods. The water table rises after wet periods and falls during droughts. Springs form where the water table intersects the surface.</p>
</div>
<div id="water-et" style="display:none;background:#fef9c3;border:2px solid #fde047;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#92400e;">☀️ Evapotranspiration</h3>
<p style="color:#475569;">The combined <strong>output</strong> of water back into the atmosphere via: <strong>Evaporation</strong> (from water surfaces, soil, and bare ground — liquid water → water vapour, powered by solar energy) and <strong>Transpiration</strong> (water released through leaf stomata of plants during photosynthesis). Evapotranspiration is highest in hot, sunny, windy conditions with abundant vegetation — the main water output from a drainage basin.</p>
</div>

<script>
function showWater(name) {
  ['precip','interception','runoff','infiltration','groundwater','et'].forEach(function(f){
    var el=document.getElementById('water-'+f); if(el) el.style.display='none';
  });
  document.getElementById('water-default').style.display='none';
  var t=document.getElementById('water-'+name); if(t) t.style.display='block';
}
</script>

<img src="{IMG}hq_real_fig1_9_map.jpeg" alt="Water cycle in a drainage basin" style="max-width:420px;height:auto;display:block;margin:0 auto;margin-top:8px;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.9 The water cycle within a drainage basin</p>
</div>

<!-- Section 4: River Processes -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚙️ 4. Fluvial Processes</h2>

<!-- Erosion -->
<h3 style="color:#dc2626;margin-bottom:10px;">💥 Erosion — 4 Types</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;">
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">
<strong style="color:#dc2626;">Hydraulic action</strong><br/>
<span style="color:#475569;font-size:14px;">Force of flowing water on the river bed/banks. Water is forced into cracks, compressing air → weakens rock. Most powerful on outside of meanders and during floods.</span>
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">
<strong style="color:#dc2626;">Corrasion (Abrasion)</strong><br/>
<span style="color:#475569;font-size:14px;">River uses its load (sand, pebbles) as tools to scrape and scratch the bed and banks — like sandpaper. Main process deepening the river channel.</span>
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">
<strong style="color:#dc2626;">Attrition</strong><br/>
<span style="color:#475569;font-size:14px;">Rock fragments carried by the river collide with each other, breaking into smaller, rounder, smoother pieces. Explains why particles get smaller downstream.</span>
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">
<strong style="color:#dc2626;">Corrosion (Solution)</strong><br/>
<span style="color:#475569;font-size:14px;">Slightly acidic river water dissolves soluble rocks (limestone, chalk). Calcium carbonate chemically reacts with carbonic acid. Invisible process.</span>
</div>
</div>
<img src="{IMG}hq_erosion.png" alt="River erosion processes" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ River erosion processes</p>

<!-- Transportation -->
<h3 style="color:#0369a1;margin-top:24px;margin-bottom:10px;">🚚 Transportation — 4 Types</h3>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px;">
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Traction</strong><br/>
<span style="color:#475569;font-size:12px;">Large boulders rolled along bed by strong current</span>
</div>
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Saltation</strong><br/>
<span style="color:#475569;font-size:12px;">Pebbles bounce along bed in series of hops</span>
</div>
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Suspension</strong><br/>
<span style="color:#475569;font-size:12px;">Fine particles (silt, clay) held up in turbulent water — makes rivers look brown</span>
</div>
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Solution</strong><br/>
<span style="color:#475569;font-size:12px;">Dissolved minerals carried invisibly in the water</span>
</div>
</div>
<img src="{IMG}hq_transport.png" alt="River transportation" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ River transportation methods</p>

<!-- Deposition -->
<h3 style="color:#15803d;margin-top:24px;margin-bottom:10px;">⬇️ Deposition</h3>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;margin-bottom:14px;">
<p style="color:#475569;margin:0;">Deposition occurs when the river's <strong>velocity and energy decrease</strong>, and it can no longer transport its load. Heaviest particles (boulders) are deposited first; finest particles (clay) travel furthest. Conditions causing deposition:
<ul style="margin-top:8px;padding-left:20px;font-size:14px;color:#475569;">
<li>Reduced gradient (approaching the sea)</li>
<li>River enters a lake, sea, or wide valley</li>
<li>Large amounts of load reduce water energy</li>
<li>Dry conditions reduce discharge</li>
</ul>
</p>
</div>
<img src="{IMG}hq_deposition.png" alt="River deposition" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ River deposition and the Hjulstrom curve</p>
</div>

</div>"""

html = html.replace('{IMG}', IMG)
print(f'HTML length: {len(html)} chars')

r = requests.patch(
    f'{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{PAGE_ID}',
    json={'content_html': html},
    headers={'apikey': KEY,'Authorization':f'Bearer {KEY}','Content-Type':'application/json','Prefer':'return=minimal'}
)
print(f'PATCH 1.1 P1: HTTP {r.status_code}')
