import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = '47c476d8-285c-41a9-a158-24194cfaf273'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/'
VI = 'style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"'

html = f"""<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#0369a1;font-size:30px;margin-bottom:10px;border-bottom:3px solid #38bdf8;display:inline-block;padding-bottom:10px;">🌊 2.1 Physical Processes that Shape the Coast<br/><span style="font-size:20px;color:#0ea5e9;font-weight:normal;">C&aacute;c Qu&aacute; Tr&igrave;nh V&#7853;t L&yacute; H&igrave;nh Th&agrave;nh B&#7901; Bi&#7875;n</span></h1>
<p style="color:#64748b;font-size:16px;">Erosion, transportation, deposition and longshore drift</p>
<p {VI}>X&oacute;i m&ograve;n, v&#7853;n chuy&#7875;n, b&#7891;i t&#7909; v&agrave; d&ograve;ng ch&#7843;y ven b&#7901;</p>
</div>

<!-- Section 1 -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🌍 1. Factors Affecting Coastal Processes</h2>
<p style="color:#475569;margin-bottom:14px;">Coastal processes and landforms are shaped by four key factors that interact to create unique coastlines worldwide:</p>
<p {VI}>C&aacute;c qu&aacute; tr&igrave;nh v&agrave; &dagger;&#7883;a h&igrave;nh b&#7901; bi&#7875;n &#7903; tr&ecirc;n kh&#7855;p th&#7871; gi&#7899;i &#7903; &dagger;&#432;&#7907;c h&igrave;nh th&agrave;nh b&#7903;i b&#7889;n y&#7871;u t&#7889; ch&iacute;nh t&#432;&#417;ng t&aacute;c v&#7899;i nhau:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:18px;">
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:14px;border-radius:6px;">
<strong style="color:#0369a1;">🌊 Waves &amp; Currents</strong><br/>
<span style="color:#475569;font-size:14px;">The dominant shaping agent. Include longshore drift, tidal currents and wave energy.</span>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">
<strong style="color:#15803d;">🪨 Local Geology</strong><br/>
<span style="color:#475569;font-size:14px;">Rock type, structure and strength. Hard rocks (granite) resist; soft rocks (clay) erode quickly.</span>
</div>
<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:14px;border-radius:6px;">
<strong style="color:#92400e;">📈 Sea Level Changes</strong><br/>
<span style="color:#475569;font-size:14px;">Rising sea levels increase coastal flooding and erosion. ~3 mm/year globally.</span>
</div>
<div style="background:#fdf4ff;border-left:4px solid #a855f7;padding:14px;border-radius:6px;">
<strong style="color:#7e22ce;">🏗️ Human Activity</strong><br/>
<span style="color:#475569;font-size:14px;">Coastal engineering, urban development, deforestation change coastal responses.</span>
</div>
</div>
<p {VI}><strong>S&oacute;ng v&agrave; d&ograve;ng ch&#7843;y</strong> l&agrave; t&aacute;c nh&acirc;n h&igrave;nh th&agrave;nh ch&#7911; y&#7871;u, bao g&#7891;m d&ograve;ng ch&#7843;y ven b&#7901;, d&ograve;ng tri&#7873;u v&agrave; n&#259;ng l&#432;&#7907;ng s&oacute;ng. <strong>&#272;&#7883;a ch&#7845;t &#273;&#7883;a ph&#432;&#417;ng</strong>: &dagger;&#225; c&#7913;ng (granite) kh&aacute;ng c&#7921; m&#7841;nh; &dagger;&#225; m&#7873;m (s&eacute;t, ph&#7845;n tr&#7855;ng) b&#7883; x&oacute;i nhanh. <strong>Thay &dagger;&#7893;i m&#7921;c n&#432;&#7899;c bi&#7875;n</strong>: n&#432;&#7899;c bi&#7875;n d&acirc;ng l&agrave;m t&#259;ng l&#361; l&#7909;t v&agrave; x&oacute;i m&ograve;n (~3mm/n&#259;m to&agrave;n c&#7847;u). <strong>Ho&#7841;t &dagger;&#7897;ng c&#7911;a con ng&#432;&#7901;i</strong>: c&ocirc;ng tr&igrave;nh b&#7901; bi&#7875;n, &#273;&#244; th&#7883; h&oacute;a, ph&aacute; r&#7915;ng thay &dagger;&#7893;i c&aacute;ch b&#7901; bi&#7875;n ph&#7843;n &uacute;ng v&#7899;i c&aacute;c qu&aacute; tr&igrave;nh t&#7921; nhi&ecirc;n.</p>
</div>

<!-- Section 2: Erosion -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚡ 2. Coastal Erosion — 4 Types</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
<div style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;margin-bottom:8px;">🌊 Hydraulic Action</h3>
<p style="color:#475569;font-size:14px;">Waves trap and compress air in cliff cracks. The explosive pressure release breaks rock. Most powerful during storms in well-jointed rocks.</p>
<p {VI}><strong>L&#7921;c th&#7911;y &dagger;&#7897;ng:</strong> S&oacute;ng &dagger;&#7853;p v&agrave;o v&aacute;ch &dagger;&#225; n&eacute;n kh&ocirc;ng kh&iacute; v&agrave;o c&aacute;c khe n&#7913;t. &Aacute;p su&#7845;t gi&#7843;i ph&oacute;ng b&#7885;t n&#7893; l&agrave;m v&#7905; &dagger;&#225;. M&#7841;nh nh&#7845;t trong b&atilde;o, trong &dagger;&#225; c&oacute; nhi&#7873;u khe n&#7913;t.</p>
</div>
<div style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;margin-bottom:8px;">🪨 Corrasion (Abrasion)</h3>
<p style="color:#475569;font-size:14px;">Waves hurl rock fragments against the cliff face — like sandpaper. Creates smooth, scratched surfaces at the base of cliffs.</p>
<p {VI}><strong>M&agrave;i m&ograve;n:</strong> S&oacute;ng n&eacute;m c&aacute;c m&#7843;nh &dagger;&#225; v&agrave;o m&#7863;t v&aacute;ch &dagger;&#225; — nh&#432; gi&#7845;y nh&aacute;m. T&#7841;o b&#7873; m&#7863;t nh&#7859;n v&agrave; c&oacute; v&#7871;t x&#432;&#7899;c &aacute;m &dagger;&#225;y ch&acirc;n v&aacute;ch.</p>
</div>
<div style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;margin-bottom:8px;">💥 Attrition</h3>
<p style="color:#475569;font-size:14px;">Rock fragments collide with each other → smaller, rounder, smoother particles. Boulders → cobbles → pebbles → sand grains over time.</p>
<p {VI}><strong>Va ch&#7841;m:</strong> M&#7843;nh &dagger;&#225; va &dagger;&#7853;p nhau &rarr; nh&#7887; h&#417;n, tr&ograve;n h&#417;n, m&#7883;n h&#417;n. T&#7843;ng &dagger;&#225; &rarr; cu&#7897;i l&#7899;n &rarr; cu&#7897;i nh&#7887; &rarr; c&aacute;t theo th&#7901;i gian.</p>
</div>
<div style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:10px;padding:16px;">
<h3 style="color:#0369a1;margin-bottom:8px;">🧪 Corrosion (Solution)</h3>
<p style="color:#475569;font-size:14px;">Seawater (slightly acidic with dissolved CO₂) dissolves limestone and chalk. Calcium carbonate dissolves slowly — produces smooth, honeycombed surfaces.</p>
<p {VI}><strong>H&ograve;a tan:</strong> N&#432;&#7899;c bi&#7875;n h&#417;i c&oacute; t&iacute;nh axit (CO&#8322; h&ograve;a tan th&agrave;nh axit cacbonic) h&ograve;a tan &dagger;&#225; v&ocirc;i v&agrave; ph&#7845;n tr&#7855;ng. Canxi cacbonat b&#7883; h&ograve;a tan t&#7915; t&#7915; &rarr; b&#7873; m&#7863;t nh&#7859;n, r&#7895;. V&iacute; d&#7909;: v&aacute;ch &dagger;&#225; ph&#7845;n tr&#7855;ng &#7903; mi&#7873;n nam n&#432;&#7899;c Anh.</p>
</div>
</div>
<img src="{IMG}2_1_fig22.png" alt="Hydraulic action" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.2 Hydraulic action on a coral coastline</p>
</div>

<!-- Section 3: Transportation -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🚚 3. Coastal Transportation</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:18px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🏖️ Bedload Transport</h3>
<ul style="color:#475569;font-size:14px;padding-left:20px;margin:0;">
<li style="margin-bottom:6px;"><strong>Traction</strong>: Large particles roll/slide along seabed</li>
<li><strong>Saltation</strong>: Medium particles bounce along seabed in hops</li>
</ul>
<p {VI}><strong>T&#7843;i &dagger;&#225;y:</strong> V&#7853;t li&#7879;u l&#7899;n di chuy&#7875;n d&#7885;c &dagger;&#225;y bi&#7875;n. <em>K&eacute;o l&#7866; (Traction)</em>: H&#7841;t l&#7899;n l&#259;n/tr&#432;&#7907;t. <em>Nh&#7843;y c&oacute;c (Saltation)</em>: H&#7841;t v&#7915;a n&#7843;y d&#7885;c &dagger;&#225;y.</p>
</div>
<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:18px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🌀 Suspended Load</h3>
<ul style="color:#475569;font-size:14px;padding-left:20px;margin:0;">
<li style="margin-bottom:6px;"><strong>Suspension</strong>: Fine particles (clay, silt) held in turbulent water</li>
<li><strong>Solution</strong>: Dissolved minerals transported invisibly in water</li>
</ul>
<p {VI}><strong>T&#7843;i l&#417; l&#7917;ng:</strong> H&#7841;t m&#7883;n (s&eacute;t, b&ugrave;n) &#273;&#432;&#7907;c gi&#7919; trong d&ograve;ng ch&#7843;y r&#7889;i v&agrave; v&#7853;n chuy&#7875;n trong c&#7897;t n&#432;&#7899;c. <em>H&ograve;a tan (Solution)</em>: Kho&aacute;ng ch&#7845;t h&ograve;a tan &#273;&#432;&#7907;c v&#7853;n chuy&#7875;n v&ocirc; h&igrave;nh trong n&#432;&#7899;c.</p>
</div>
</div>
</div>

<!-- Section 4: Deposition -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⬇️ 4. Deposition</h2>
<p style="color:#475569;margin-bottom:14px;">Deposition occurs when wave energy or velocity <strong>decreases</strong> and the water can no longer carry its sediment load. The heavier, larger particles are deposited first; fine clay travels furthest.</p>
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:16px;border-radius:6px;margin-bottom:12px;">
<strong style="color:#0369a1;">Conditions favouring deposition:</strong>
<ul style="color:#475569;margin-top:8px;padding-left:20px;font-size:15px;">
<li>Waves entering sheltered water — bays, estuaries, lagoons</li>
<li>Calm weather, gently sloping shoreline, obstacles (groynes, headlands)</li>
</ul>
</div>
<p {VI}><strong>B&#7891;i t&#7909;</strong> x&#7843;y ra khi n&#259;ng l&#432;&#7907;ng/v&#7853;n t&#7889;c s&oacute;ng <strong>gi&#7843;m</strong> v&agrave; n&#432;&#7899;c kh&ocirc;ng c&ograve;n &dagger;&#7911; s&#7913;c mang t&#7843;i l&#432;&#7907;ng. H&#7841;t l&#7899;n, n&#7863;ng &dagger;&#7885;ng xu&#7889;ng tr&#432;&#7899;c; s&eacute;t m&#7883;n &dagger;i xa nh&#7845;t. &#272;i&#7873;u ki&#7879;n thu&#7853;n l&#7907;i: s&oacute;ng v&agrave;o v&ugrave;ng n&#432;&#7899;c k&iacute;n (v&#7883;nh, c&#7917;a s&ocirc;ng, &dagger;&#7847;m ph&aacute;), th&#7901;i ti&#7871;t l&#7863;ng, b&#7901; bi&#7875;n tho&#7843;i, v&#7853;t c&#7843;n (groyne, m&#361;i &dagger;&#7845;t) l&agrave;m s&oacute;ng v&#7905;.</p>
</div>

<!-- Section 5: Longshore Drift -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">➡️ 5. Longshore Drift (D&ograve;ng Ch&#7843;y Ven B&#7901;)</h2>
<p style="color:#475569;margin-bottom:12px;"><strong>Longshore drift (LSD)</strong> is the net movement of sediment <em>along</em> the coastline, driven by waves approaching at an angle (determined by prevailing wind direction).</p>
<p {VI}><strong>D&ograve;ng ch&#7843;y ven b&#7901; (Longshore drift)</strong> l&agrave; s&#7921; di chuy&#7875;n t&#7883;nh ti&#7871;n c&#7911;a tr&#7847;m t&iacute;ch d&#7885;c b&#7901; bi&#7875;n. X&#7843;y ra v&igrave; s&oacute;ng ti&#7871;p c&#7853;n b&#7901; theo g&oacute;c (theo h&#432;&#7899;ng gi&oacute; th&#7883;nh h&agrave;nh): <em>Swash</em> mang tr&#7847;m t&iacute;ch ch&eacute;o l&ecirc;n b&#7903;i &rarr; <em>backwash</em> k&eacute;o th&#7859;ng xu&#7889;ng (tr&#7885;ng l&#7921;c) &rarr; tr&#7847;m t&iacute;ch di chuy&#7875;n h&igrave;nh ch&#7919; chi d&#7885;c b&#7901;. H&#432;&#7899;ng ph&#7909; thu&#7897;c v&agrave;o <strong>h&#432;&#7899;ng gi&oacute; th&#7883;nh h&agrave;nh</strong>. &amp;#272;&#7853;p groyne x&acirc;y vu&ocirc;ng g&oacute;c b&#7901; &dagger;&#7875; gi&#7919; tr&#7847;m t&iacute;ch v&agrave; ng&#259;n d&ograve;ng ch&#7843;y ven b&#7901;.</p>
<img src="{IMG}2_1_fig23.png" alt="Longshore drift" style="max-width:420px;height:auto;display:block;margin:0 auto;margin-top:12px;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.3 Longshore drift — swash moves sediment diagonally, backwash perpendicular to shore</p>
</div>

<!-- Section 6: Wave Types -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🏄 6. Wave Types: Constructive vs Destructive</h2>
<img src="{IMG}2_1_fig26.png" alt="Wave types" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.6 Constructive (top) and destructive waves (bottom)</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px;">
<div style="background:#f0fdf4;border:2px solid #22c55e;border-radius:10px;padding:18px;">
<h3 style="color:#15803d;margin-bottom:10px;">✅ Constructive Waves<br/><span style="font-size:13px;font-weight:normal;color:#64748b;">(S&oacute;ng Ki&#7871;n T&#7841;o)</span></h3>
<ul style="color:#475569;font-size:14px;padding-left:18px;margin:0;">
<li>Long wavelength, low height</li>
<li>Elliptical orbit, low gradient beach</li>
<li><strong>Swash &gt; Backwash → Deposition</strong></li>
<li>Formed by distant weather (swell)</li>
</ul>
<p {VI}>B&#432;&#7899;c s&oacute;ng d&agrave;i, chi&#7873;u cao th&#7845;p, qu&#7929; &dagger;&#7841;o elip, b&#7303;i bi&#7875;n tho&#7843;i. <strong>Swash m&#7841;nh h&#417;n backwash &rarr; B&#7891;i t&#7909;</strong>. Li&ecirc;n quan &dagger;&#7871;n th&#7901;i ti&#7871;t xa, y&ecirc;n t&#297;nh (s&oacute;ng l&#7915;ng).</p>
</div>
<div style="background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:18px;">
<h3 style="color:#dc2626;margin-bottom:10px;">⚡ Destructive Waves<br/><span style="font-size:13px;font-weight:normal;color:#64748b;">(S&oacute;ng Ph&aacute; H&#7911;y)</span></h3>
<ul style="color:#475569;font-size:14px;padding-left:18px;margin:0;">
<li>Short wavelength, high height</li>
<li>Circular orbit, steep gradient beach</li>
<li><strong>Backwash &gt; Swash → Erosion</strong></li>
<li>Formed by local storms (wind waves)</li>
</ul>
<p {VI}>B&#432;&#7899;c s&oacute;ng ng&#7855;n, chi&#7873;u cao l&#7899;n, qu&#7929; &dagger;&#7841;o tr&ograve;n, b&#7303;i bi&#7875;n d&#7889;c. <strong>Backwash m&#7841;nh h&#417;n swash &rarr; X&oacute;i m&ograve;n</strong>. Li&ecirc;n quan &dagger;&#7871;n b&atilde;o &dagger;&#7883;a ph&#432;&#417;ng (s&oacute;ng do gi&oacute; &dagger;&#7883;a ph&#432;&#417;ng).</p>
</div>
</div>
<div style="overflow-x:auto;margin-top:18px;">
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<tr style="background:#0369a1;color:white;"><th style="padding:10px;text-align:left;">Feature / &#272;&#7863;c &dagger;i&#7875;m</th><th style="padding:10px;">Constructive / Ki&#7871;n t&#7841;o</th><th style="padding:10px;">Destructive / Ph&aacute; h&#7911;y</th></tr>
<tr style="background:#f0fdf4;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;">Wavelength / B&#432;&#7899;c s&oacute;ng</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Long / D&agrave;i</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Short / Ng&#7855;n</td></tr>
<tr><td style="padding:9px;border-bottom:1px solid #e2e8f0;">Wave height / Chi&#7873;u cao</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Low / Th&#7845;p</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">High / Cao</td></tr>
<tr style="background:#f0fdf4;"><td style="padding:9px;border-bottom:1px solid #e2e8f0;">Orbital motion / Qu&#7929; &dagger;&#7841;o</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Elliptical</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;">Circular / Tr&ograve;n</td></tr>
<tr><td style="padding:9px;border-bottom:1px solid #e2e8f0;">Main process / Qu&aacute; tr&igrave;nh ch&iacute;nh</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;color:#15803d;font-weight:bold;">Deposition / B&#7891;i t&#7909;</td><td style="padding:9px;border-bottom:1px solid #e2e8f0;text-align:center;color:#dc2626;font-weight:bold;">Erosion / X&oacute;i m&ograve;n</td></tr>
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
print(f'PATCH 2.1 P2: HTTP {r.status_code}')
