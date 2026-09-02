import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = '5d5f042f-1017-4ca5-ba80-5359f111ac0f'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/'

html = """<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">

<!-- Header -->
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#0369a1;font-size:30px;margin-bottom:10px;border-bottom:3px solid #38bdf8;display:inline-block;padding-bottom:10px;">🌊 2.3 Coastal Opportunities &amp; Hazards</h1>
<p style="color:#64748b;font-size:16px;">How people use and are affected by coastal environments</p>
</div>

<!-- Interactive SVG Banner -->
<div style="border-radius:12px;overflow:hidden;margin-bottom:28px;box-shadow:0 2px 8px rgba(0,0,0,0.12);">
<svg width="100%" viewBox="0 0 800 140" xmlns="http://www.w3.org/2000/svg" style="display:block;">
<defs>
<linearGradient id="gGreen23" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#bbf7d0"/><stop offset="100%" style="stop-color:#4ade80"/></linearGradient>
<linearGradient id="gRed23" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#fed7aa"/><stop offset="100%" style="stop-color:#f87171"/></linearGradient>
</defs>
<rect x="0" y="0" width="400" height="140" fill="url(#gGreen23)"/>
<rect x="400" y="0" width="400" height="140" fill="url(#gRed23)"/>
<text x="200" y="38" text-anchor="middle" fill="#14532d" font-size="22" font-weight="bold">🌿 OPPORTUNITIES</text>
<text x="600" y="38" text-anchor="middle" fill="#7f1d1d" font-size="22" font-weight="bold">⚠️ HAZARDS</text>
<rect x="20" y="55" width="85" height="32" rx="16" fill="#16a34a" onclick="showCoast('tourism')" style="cursor:pointer"/>
<text x="62" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('tourism')" style="cursor:pointer">🏖️ Tourism</text>
<rect x="115" y="55" width="85" height="32" rx="16" fill="#15803d" onclick="showCoast('fishing')" style="cursor:pointer"/>
<text x="157" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('fishing')" style="cursor:pointer">🐟 Fishing</text>
<rect x="210" y="55" width="85" height="32" rx="16" fill="#166534" onclick="showCoast('transport')" style="cursor:pointer"/>
<text x="252" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('transport')" style="cursor:pointer">⚓ Transport</text>
<rect x="305" y="55" width="85" height="32" rx="16" fill="#14532d" onclick="showCoast('settlement')" style="cursor:pointer"/>
<text x="347" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('settlement')" style="cursor:pointer">🏙️ Settlement</text>
<rect x="415" y="55" width="90" height="32" rx="16" fill="#dc2626" onclick="showCoast('erosion')" style="cursor:pointer"/>
<text x="460" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('erosion')" style="cursor:pointer">🌊 Erosion</text>
<rect x="515" y="55" width="80" height="32" rx="16" fill="#b91c1c" onclick="showCoast('flooding')" style="cursor:pointer"/>
<text x="555" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('flooding')" style="cursor:pointer">💧 Flooding</text>
<rect x="605" y="55" width="80" height="32" rx="16" fill="#991b1b" onclick="showCoast('cyclones')" style="cursor:pointer"/>
<text x="645" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('cyclones')" style="cursor:pointer">🌀 Cyclones</text>
<rect x="695" y="55" width="85" height="32" rx="16" fill="#7f1d1d" onclick="showCoast('tsunami')" style="cursor:pointer"/>
<text x="737" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600" onclick="showCoast('tsunami')" style="cursor:pointer">🌊 Tsunami</text>
<text x="200" y="118" text-anchor="middle" fill="#14532d" font-size="11" style="cursor:pointer" onclick="showCoast('mgmt')">▼ Coastal Management Strategies</text>
<text x="600" y="118" text-anchor="middle" fill="#7f1d1d" font-size="11">Click any button to learn more</text>
</svg>
</div>

<!-- Info Panel -->
<div id="coast-default" style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:24px;">
<p style="color:#64748b;font-style:italic;text-align:center;">👆 Click any button above to explore coastal opportunities and hazards</p>
</div>
<div id="coast-tourism" style="display:none;background:#f0fdf4;border:2px solid #4ade80;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#15803d;">🏖️ Tourism &amp; Recreation</h3>
<p style="color:#475569;">Coastal areas attract millions of tourists: beaches, warm climates, water sports, coral reefs, marine wildlife. The Caribbean, Mediterranean, Southeast Asian coasts depend heavily on tourism income. <strong>Example:</strong> Rodney Bay, St Lucia — cruise ships, hotels, water sports, diving. Tourism provides jobs and income for local communities but can also cause environmental damage (pollution, habitat destruction).</p>
</div>
<div id="coast-fishing" style="display:none;background:#f0fdf4;border:2px solid #4ade80;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#15803d;">🐟 Fishing &amp; Aquaculture</h3>
<p style="color:#475569;">Coastal waters are rich in marine life — fish, shellfish, seaweed. <strong>Artisanal fishing</strong> (small boats, traditional methods) supports millions of families worldwide. <strong>Aquaculture</strong> (farming fish, shrimp, oysters in lagoons, pens, or ponds) is the world's fastest-growing food sector. Example: shrimp farming in Bangladesh, salmon farming in Norwegian fjords. However, overfishing and fish farm effluents threaten marine ecosystems.</p>
</div>
<div id="coast-transport" style="display:none;background:#f0fdf4;border:2px solid #4ade80;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#15803d;">⚓ Transport &amp; Trade</h3>
<p style="color:#475569;">Ports and harbours enable global trade — over 80% of world trade by volume travels by sea. Coastal cities like Shanghai, Rotterdam, Singapore, and Dubai are major global trading hubs. Natural deep-water harbours (e.g. Hong Kong, Sydney) are especially valuable. Inland waterways and estuaries also allow goods to move between ports and inland cities.</p>
</div>
<div id="coast-settlement" style="display:none;background:#f0fdf4;border:2px solid #4ade80;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#15803d;">🏙️ Settlement &amp; Industry</h3>
<p style="color:#475569;">About 40% of the world's population lives within 100 km of a coast. Flat coastal plains and deltas provide fertile agricultural land (e.g. Nile Delta, Mekong Delta). Industries include: shipbuilding, oil refining (coastal refineries), energy generation (offshore wind, tidal barrages), tourism infrastructure. Coastal land reclamation (e.g. Singapore, Netherlands) creates new land for settlement.</p>
</div>
<div id="coast-erosion" style="display:none;background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#dc2626;">🌊 Coastal Erosion</h3>
<p style="color:#475569;">Rising sea levels and increased storm activity accelerate coastal erosion. <strong>Soft rock cliffs</strong> (e.g. clay, chalk) can retreat at 1–10 metres per year. Farmland, roads, buildings and entire villages can be lost to the sea. <strong>Example: Holderness Coast, Yorkshire, UK</strong> — loses ~2m of cliff per year (fast in UK). Villages such as Skipsea have been lost. Management: hard engineering (sea walls, groynes) can protect specific locations but may accelerate erosion elsewhere.</p>
</div>
<div id="coast-flooding" style="display:none;background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#dc2626;">💧 Coastal Flooding</h3>
<p style="color:#475569;">Low-lying coastal areas face increasing flood risk from three main causes:
<br/>• <strong>Storm surges</strong>: Intense low pressure + strong winds pile seawater inland (e.g. 1953 North Sea flood killed 2,500+ people)
<br/>• <strong>Sea level rise (SLR)</strong>: Global warming → thermal expansion of oceans + melting ice → ~3.7 mm/yr rise. Threatens: Bangladesh (10% could flood), Maldives (avg 1.5m high), Pacific island nations
<br/>• <strong>Tsunamis</strong>: Underwater earthquakes generate massive waves. 2004 Indian Ocean tsunami: 9.1 magnitude, 30m waves, >230,000 deaths across 14 countries</p>
</div>
<div id="coast-cyclones" style="display:none;background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#dc2626;">🌀 Tropical Cyclones (Hurricanes / Typhoons)</h3>
<p style="color:#475569;">Tropical cyclones are the most dangerous coastal hazard. They bring:
<br/>• Sustained winds &gt;119 km/h (Category 1), up to 315 km/h (Category 5)
<br/>• Storm surges up to 8–9 metres above normal sea level
<br/>• Extreme rainfall and inland flooding
<br/>They form over warm tropical seas (&gt;27°C) between 5°–20° latitude. Names vary by region: <strong>Hurricanes</strong> (Atlantic/Caribbean), <strong>Typhoons</strong> (W. Pacific), <strong>Cyclones</strong> (Indian Ocean, SW Pacific).
<br/><strong>Management:</strong> Satellite prediction, aircraft reconnaissance, early warning systems, evacuation plans, wind-resistant buildings (hurricane straps, shutters), land-use zoning, mangrove restoration to absorb wave energy.</p>
</div>
<div id="coast-tsunami" style="display:none;background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#dc2626;">🌊 Tsunamis</h3>
<p style="color:#475569;">Tsunamis are giant ocean waves triggered by underwater earthquakes, volcanic eruptions, or submarine landslides. In the open ocean they travel at 800 km/h but are only 1m high — undetectable. As they approach shallow water they slow down and pile up, reaching 30m+ height. <strong>2004 Indian Ocean Tsunami</strong> (9.1 magnitude, off Sumatra): killed 227,898 people across 14 countries including Indonesia, Sri Lanka, India, Thailand. <strong>Management:</strong> Pacific Tsunami Warning System (PTWS), deep-ocean pressure sensors (DART buoys), coastal mangroves as natural barriers, coastal zoning (no buildings in hazard zones).</p>
</div>
<div id="coast-mgmt" style="display:none;background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;margin-bottom:24px;">
<h3 style="color:#0369a1;">🏗️ Coastal Management Strategies</h3>
<p style="color:#475569;">Coastal managers choose from four options: <strong>do nothing</strong> (let nature take its course), <strong>maintain existing defence</strong>, <strong>improve defence</strong>, or <strong>managed retreat</strong>. Strategies are classified as <em>hard engineering</em> (structures working against nature) or <em>soft engineering</em> (working with nature).</p>
</div>

<script>
function showCoast(name) {
  ['tourism','fishing','transport','settlement','erosion','flooding','cyclones','tsunami','mgmt'].forEach(function(f){
    var el=document.getElementById('coast-'+f);
    if(el) el.style.display='none';
  });
  document.getElementById('coast-default').style.display='none';
  var target=document.getElementById('coast-'+name);
  if(target) target.style.display='block';
}
</script>

<!-- Opportunities Section -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #4ade80;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🌿 Coastal Opportunities</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<strong style="color:#15803d;">🏖️ Tourism</strong>: Caribbean, Mediterranean and SE Asian coasts attract millions of tourists. Provides jobs, income, infrastructure — but risks pollution and habitat damage.
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<strong style="color:#15803d;">🐟 Fishing &amp; Aquaculture</strong>: Coastal waters supply global protein needs. Artisanal fishing, shrimp farming, oyster cultivation provide livelihoods for coastal communities.
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<strong style="color:#15803d;">⚓ Transport</strong>: 80%+ of world trade moves by sea. Major ports (Shanghai, Rotterdam, Singapore) drive global economies.
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<strong style="color:#15803d;">🏙️ Settlement</strong>: 40% of world population lives within 100km of coast. Flat fertile coastal plains + industry + energy generation (offshore wind).
</div>
</div>
<img src="{IMG}2_3_fig229.png" alt="Rodney Bay tourist development" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.29 Tourist development at Rodney Bay, St Lucia — cruise ship port and waterfront</p>
</div>

<!-- Hazards Section -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #f87171;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚠️ Coastal Hazards</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;">
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:8px;">
<strong style="color:#dc2626;">🌊 Coastal Erosion</strong>: Retreating cliffs threaten settlements. Holderness, UK: ~2m/year. Rising sea levels accelerate erosion. Farmland, roads, villages lost permanently.
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:8px;">
<strong style="color:#dc2626;">💧 Coastal Flooding</strong>: Storm surges, sea level rise (~3.7 mm/yr), tsunamis. Most at risk: Bangladesh, Maldives, Pacific islands. 2004 tsunami: 230,000+ deaths.
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:8px;">
<strong style="color:#dc2626;">🌀 Tropical Cyclones</strong>: Winds &gt;119 km/h, storm surges up to 9m, extreme rain. Atlantic: Hurricanes; W. Pacific: Typhoons; Indian Ocean: Cyclones. Form over warm seas &gt;27°C.
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:8px;">
<strong style="color:#dc2626;">💧 Water Pollution</strong>: Runoff, industrial effluents, wastewater discharge. Dead zones from nutrient pollution (eutrophication). Risk to fishing, tourism and human health.
</div>
</div>
</div>

<!-- Management Section -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🏗️ Coastal Management Strategies</h2>

<h3 style="color:#0369a1;margin-bottom:12px;">Hard Engineering (working against nature)</h3>
<div style="overflow-x:auto;margin-bottom:20px;">
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<tr style="background:#0369a1;color:white;"><th style="padding:9px;text-align:left;">Strategy</th><th style="padding:9px;">Method</th><th style="padding:9px;">✅ Strengths</th><th style="padding:9px;">❌ Weaknesses</th></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Sea walls</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Curved concrete walls reflect wave energy</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Effective; 30–40 yr lifespan</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Very expensive; foundations may be undermined</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Revetments</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Sloping structures absorb wave energy</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Cheaper; permeable</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Limited lifespan; ugly</td></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Groynes</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Perpendicular barriers trap longshore drift</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Builds up beach</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Starves beaches downdrift</td></tr>
<tr><td style="padding:8px;font-weight:600;">Rock armour (rip-rap)</td><td style="padding:8px;">Large boulders absorb/reduce wave energy</td><td style="padding:8px;">Relatively cheap</td><td style="padding:8px;">Ugly; can shift; expensive to maintain</td></tr>
</table>
</div>

<h3 style="color:#0369a1;margin-bottom:12px;">Soft Engineering (working with nature)</h3>
<div style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<tr style="background:#166534;color:white;"><th style="padding:9px;text-align:left;">Strategy</th><th style="padding:9px;">Method</th><th style="padding:9px;">✅ Strengths</th><th style="padding:9px;">❌ Weaknesses</th></tr>
<tr style="background:#f0fdf4;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Beach nourishment</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Pump sand from seabed to eroded beach</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Looks natural; good for tourism</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Expensive; temporary (1–5 years)</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Managed retreat</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Allow coast to flood/erode in low-value zones</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Cost-effective; natural; creates wetland habitat</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Unpopular; political issues; loss of land</td></tr>
<tr style="background:#f0fdf4;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;font-weight:600;">Dune regeneration</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Plant marram grass; install sand fencing</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Sustainable; biodiversity benefit</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Slow; needs maintenance</td></tr>
<tr><td style="padding:8px;font-weight:600;">Offshore reefs</td><td style="padding:8px;">Submerge old materials offshore to absorb wave energy</td><td style="padding:8px;">Low tech; relatively cheap</td><td style="padding:8px;">Long-term impacts unknown</td></tr>
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
print(f'PATCH 2.3 P1: HTTP {r.status_code}')
