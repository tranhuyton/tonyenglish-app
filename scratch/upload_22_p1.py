import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = '55d26cc1-d2f2-4c0e-ac01-b5390cb4315d'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/'

html = """<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">

<!-- Header -->
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#0369a1;font-size:30px;margin-bottom:10px;border-bottom:3px solid #38bdf8;display:inline-block;padding-bottom:10px;">🏔️ 2.2 Coastal Landforms</h1>
<p style="color:#64748b;font-size:16px;">How coastal processes create distinctive erosional and depositional features</p>
</div>

<!-- Section 1: Concordant / Discordant -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🗺️ 1. Coastline Types: Concordant &amp; Discordant</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:16px;border-radius:8px;">
<h3 style="color:#92400e;margin-bottom:8px;">⛰️ Discordant Coastline</h3>
<p style="color:#475569;font-size:14px;">Alternating bands of <strong>hard and soft rock run perpendicular</strong> to the coast. Differential erosion creates alternating headlands (hard rock) and bays (soft rock). Wave refraction focuses wave energy on headlands, disperses it in bays → headlands erode further forming cliffs, bays accumulate sand as beaches.</p>
<p style="color:#92400e;font-size:13px;margin-top:8px;font-style:italic;">Example: Jurassic Coast, Dorset, UK</p>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:16px;border-radius:8px;">
<h3 style="color:#15803d;margin-bottom:8px;">🏝️ Concordant Coastline</h3>
<p style="color:#475569;font-size:14px;">Bands of rock run <strong>parallel to the coast</strong>. Because only one rock type is exposed to the sea, the coastline is more uniform and smooth with fewer headlands and bays. Occasional weak points in the outer hard rock allow the sea to break through.</p>
<p style="color:#15803d;font-size:13px;margin-top:8px;font-style:italic;">Example: Dalmatian coast, Croatia</p>
</div>
</div>
<img src="{IMG}2_2_fig29.png" alt="Headlands and bays diagram" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.9 Headlands and bays — hard rock headlands protrude, soft rock bays are eroded back</p>
<img src="{IMG}2_2_fig210.png" alt="Headlands and bays photo" style="max-width:420px;height:auto;display:block;margin:0 auto;margin-top:16px;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.10 Headlands and bays at Praia de Rocha, Algarve, Portugal</p>
</div>

<!-- Section 2: Erosional Landforms - Interactive SVG -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚡ 2. Erosional Landforms — Cliffs, Caves, Arches &amp; Stacks</h2>
<p style="color:#475569;margin-bottom:16px;">Click on each coastal feature to learn how it forms:</p>

<!-- Interactive SVG Coastal Scene -->
<div style="background:linear-gradient(180deg,#bae6fd 0%,#7dd3fc 40%,#fde68a 70%,#d97706 100%);border-radius:12px;padding:12px;margin-bottom:16px;overflow-x:auto;">
<svg width="760" height="260" viewBox="0 0 760 260" style="max-width:100%;display:block;margin:0 auto;">
  <!-- Sky -->
  <rect x="0" y="0" width="760" height="260" fill="#e0f2fe"/>
  <!-- Sea -->
  <rect x="0" y="130" width="760" height="130" fill="#7dd3fc" opacity="0.7"/>
  <!-- Main Cliff -->
  <polygon points="0,260 0,80 120,70 120,260" fill="#94a3b8"/>
  <polygon points="0,80 120,70 120,120 60,130 0,130" fill="#cbd5e1"/>
  <!-- Wave-cut platform (at base) -->
  <rect x="0" y="230" width="150" height="10" fill="#64748b" opacity="0.5"/>
  <!-- Headland with cave+arch+stack -->
  <polygon points="220,260 220,90 340,80 380,85 380,140 350,145 280,145 260,260" fill="#94a3b8"/>
  <!-- Cave mouth -->
  <ellipse cx="250" cy="138" rx="20" ry="15" fill="#475569"/>
  <!-- Arch opening -->
  <path d="M 340,140 Q 360,105 380,140" fill="#7dd3fc" stroke="#64748b" stroke-width="2"/>
  <!-- Stack -->
  <rect x="430" y="105" width="30" height="155" rx="4" fill="#94a3b8"/>
  <!-- Stump (smaller, at sea level) -->
  <rect x="510" y="215" width="25" height="45" rx="4" fill="#94a3b8" opacity="0.7"/>
  <!-- Beach (right side) -->
  <polygon points="560,260 560,195 760,175 760,260" fill="#fde68a"/>
  <!-- Spit extending right -->
  <polygon points="600,195 760,175 760,185 630,200" fill="#f59e0b" opacity="0.8"/>
  <!-- Labels as clickable buttons -->
  <text x="50" y="50" fill="#1e40af" font-size="11" font-weight="bold" text-anchor="middle" style="cursor:pointer" onclick="showFeature('cliff')">CLIFF ▼</text>
  <text x="50" y="220" fill="#475569" font-size="9" text-anchor="middle">Wave-cut</text>
  <text x="50" y="230" fill="#475569" font-size="9" text-anchor="middle">platform</text>
  <text x="255" y="125" fill="white" font-size="9" text-anchor="middle" style="cursor:pointer" onclick="showFeature('cave')">CAVE</text>
  <text x="360" y="125" fill="#1e40af" font-size="9" text-anchor="middle" style="cursor:pointer" onclick="showFeature('arch')">ARCH</text>
  <text x="445" y="95" fill="#1e40af" font-size="10" text-anchor="middle" style="cursor:pointer" onclick="showFeature('stack')">STACK ▼</text>
  <text x="522" y="208" fill="#1e40af" font-size="9" text-anchor="middle" style="cursor:pointer" onclick="showFeature('stump')">STUMP</text>
  <text x="640" y="190" fill="#92400e" font-size="10" text-anchor="middle" style="cursor:pointer" onclick="showFeature('spit')">SPIT →</text>
  <text x="700" y="230" fill="#92400e" font-size="10" text-anchor="middle" style="cursor:pointer" onclick="showFeature('beach')">BEACH</text>
  <!-- Wave lines -->
  <path d="M 0,165 Q 50,155 100,165 Q 150,175 200,165 Q 250,155 300,165 Q 350,175 400,165 Q 450,155 500,165 Q 550,175 600,165" fill="none" stroke="white" stroke-width="2" opacity="0.6"/>
  <path d="M 0,180 Q 60,170 120,180 Q 180,190 240,180 Q 300,170 360,180 Q 420,190 480,180 Q 540,170 600,180" fill="none" stroke="white" stroke-width="1.5" opacity="0.4"/>
</svg>
<p style="text-align:center;font-size:11px;color:#475569;margin-top:6px;">👆 Click any label to see details</p>
</div>

<!-- Feature info panels -->
<div id="feat-default" style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:16px;">
<p style="color:#64748b;font-style:italic;text-align:center;">👆 Click a feature in the diagram above to learn how it forms</p>
</div>
<div id="feat-cliff" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🏔️ Cliffs &amp; Wave-cut Platforms</h3>
<p style="color:#475569;">Waves attack the base of a cliff via hydraulic action and corrasion, cutting a <strong>wave-cut notch</strong> at the high-tide mark. As the notch deepens, the rock above is unsupported and collapses. The cliff retreats inland, leaving behind a <strong>wave-cut platform</strong> — a flat rocky shelf at sea level. Platforms are exposed at low tide and may have rock pools.</p>
</div>
<div id="feat-cave" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🕳️ Sea Caves</h3>
<p style="color:#475569;">Waves exploit weaknesses (joints, bedding planes, faults) in cliff faces, especially on headlands. Hydraulic action forces water and compressed air into these cracks, widening them. Over time a <strong>cave</strong> is formed. Where the cave reaches right through the headland, a blowhole may form at the surface where compressed air escapes.</p>
</div>
<div id="feat-arch" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🌉 Natural Arches</h3>
<p style="color:#475569;">When caves form on both sides of a narrow headland, they can erode back until they meet, forming a <strong>natural arch</strong>. The sea flows through the opening. A famous example is <em>Durdle Door</em> on the Jurassic Coast, Dorset, UK — formed in Jurassic-age Portland limestone. See Fig 2.11 and 2.12.</p>
</div>
<div id="feat-stack" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🗼 Sea Stacks</h3>
<p style="color:#475569;">Continued erosion and weathering weakens the arch roof until it collapses, leaving an isolated pillar of rock called a <strong>sea stack</strong>. Stacks continue to be attacked by waves at their base. Famous examples: The Old Man of Hoy (Orkney, Scotland), The Twelve Apostles (Victoria, Australia).</p>
</div>
<div id="feat-stump" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🪨 Stumps</h3>
<p style="color:#475569;">As a sea stack continues to be eroded at its base, it eventually collapses to form a low, rounded <strong>stump</strong> — only visible at low tide. The stump may eventually be completely eroded and incorporated into the wave-cut platform.</p>
</div>
<div id="feat-beach" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🏖️ Beaches</h3>
<p style="color:#475569;">Beaches form where constructive waves deposit sand, shingle, or pebbles. Best developed on lowland coasts. A beach has three zones: <strong>backshore</strong> (above normal high-tide mark, reached only by storms), <strong>foreshore</strong> (between high and low tide, the main beach area), and <strong>offshore</strong> (below low tide). Sandy beaches indicate fine material; shingle beaches indicate coarser, higher-energy environments.</p>
</div>
<div id="feat-spit" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;">🌊 Spits</h3>
<p style="color:#475569;">A spit is a ridge of sand or shingle <strong>attached to land at one end</strong>, extending across a bay or estuary. Forms where longshore drift continues past a break in the coastline (e.g. river mouth). As the spit grows, wave refraction around its tip causes the end to curve — a <strong>recurved end</strong>. Salt marsh develops in the sheltered water behind the spit. Example: Blakeney Point, Norfolk, UK; Walvis Bay spit, Namibia.</p>
</div>

<script>
function showFeature(name) {
  ['cliff','cave','arch','stack','stump','beach','spit'].forEach(function(f){
    document.getElementById('feat-'+f).style.display='none';
  });
  document.getElementById('feat-default').style.display='none';
  document.getElementById('feat-'+name).style.display='block';
}
</script>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px;">
<div>
<img src="{IMG}2_2_fig211.png" alt="Cave arch stack formation" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.11 Cave → Arch → Stack formation sequence on a headland</p>
</div>
<div>
<img src="{IMG}2_2_fig212.png" alt="Durdle Door arch" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.12 Natural arch at Durdle Door, Dorset, UK</p>
</div>
</div>
</div>

<!-- Section 3: Depositional Landforms -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⬇️ 3. Depositional Landforms — Beaches, Spits &amp; Dunes</h2>

<h3 style="color:#0369a1;margin-bottom:10px;">🌊 Spits, Bars &amp; Tombolos</h3>
<p style="color:#475569;margin-bottom:14px;">These landforms develop where abundant sand/shingle is available (via longshore drift) and coastline is irregular (variable geology, estuaries, river mouths):</p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px;">
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:14px;border-radius:8px;">
<strong style="color:#0369a1;">Spit</strong><br/>
<span style="color:#475569;font-size:14px;">Ridge linked to land at one end, extending across a bay/estuary. Recurved end from wave refraction. Salt marsh forms in sheltered area behind.</span>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<strong style="color:#15803d;">Bar</strong><br/>
<span style="color:#475569;font-size:14px;">Spit that has grown across an entire bay, cutting off a lagoon. Also called a bay bar. Forms where the bay is narrow enough for longshore drift to seal it.</span>
</div>
<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:14px;border-radius:8px;">
<strong style="color:#92400e;">Tombolo</strong><br/>
<span style="color:#475569;font-size:14px;">Sand or shingle bar connecting the mainland to a nearby island. Example: St Ninian's Isle, Shetland; Mont Saint-Michel, France.</span>
</div>
</div>
<img src="{IMG}2_2_fig221.png" alt="Spit formation" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.21 Spit formation — longshore drift, recurved end caused by wave refraction, salt marsh behind</p>

<h3 style="color:#0369a1;margin-top:24px;margin-bottom:10px;">🏜️ Sand Dunes</h3>
<p style="color:#475569;margin-bottom:14px;">Sand dunes form where constructive waves deposit sand on wide beaches. As the tide goes out, sand dries and is blown inland by onshore winds. A <strong>vegetation succession</strong> develops as dunes stabilise:</p>
<div style="background:#fef9c3;border-radius:10px;padding:16px;margin-bottom:16px;">
<div style="display:flex;gap:8px;align-items:flex-start;flex-wrap:wrap;">
<div style="background:#f59e0b;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;">1. Embryo Dune</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Forms at strand line; sand accumulates around debris</div>
<div style="background:#84cc16;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-left:8px;">2. Yellow Dune</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Sea couch grass colonises; grows to 1m; marram grass establishes</div>
<div style="background:#22c55e;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-left:8px;">3. Semi-fixed</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Marram grass main binder; over 10m high; soil begins to form</div>
<div style="background:#166534;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-left:8px;">4. Fixed (Grey) Dune</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Rich in species: lichens, mosses, flowering plants, eventually small trees</div>
</div>
</div>
<img src="{IMG}2_2_fig225.png" alt="Sand dune formation" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.25 Sand dune succession from embryo dune (sea) to fixed dune (inland)</p>
</div>

<!-- Summary Table -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:16px;font-size:22px;">📊 Summary: Coastal Landforms</h2>
<div style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<tr style="background:#0369a1;color:white;"><th style="padding:10px;text-align:left;">Landform</th><th style="padding:10px;">Type</th><th style="padding:10px;">Key Process</th><th style="padding:10px;">Key Feature</th></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Headland</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#dc2626;">Erosional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Differential erosion</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Hard rock protrudes</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Bay</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#dc2626;">Erosional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Differential erosion</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Soft rock eroded; sheltered</td></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Wave-cut platform</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#dc2626;">Erosional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Hydraulic action + abrasion</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Rocky shelf at sea level</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Cave → Arch → Stack</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#dc2626;">Erosional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Hydraulic action on weakness</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Progressive headland erosion</td></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Beach</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#15803d;">Depositional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Constructive waves</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Sand/shingle accumulation</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Spit</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#15803d;">Depositional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Longshore drift + refraction</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Ridge attached to land; recurved tip</td></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Bar</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#15803d;">Depositional</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Longshore drift seals bay</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Ridge across bay; lagoon behind</td></tr>
<tr><td style="padding:8px;font-weight:600;">Sand Dune</td><td style="padding:8px;color:#15803d;">Depositional</td><td style="padding:8px;">Wind deposition + vegetation</td><td style="padding:8px;">Succession embryo→fixed dune</td></tr>
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
print(f'PATCH 2.2 P1: HTTP {r.status_code}')
