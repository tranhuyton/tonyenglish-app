import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = 'c27766f1-0030-4641-8d82-d3771b354e01'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/'
VI = 'style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"'

html = f"""<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#1e3a8a;font-size:30px;margin-bottom:10px;border-bottom:3px solid #60a5fa;display:inline-block;padding-bottom:10px;">🌊 1.1 Hydrological Characteristics &amp; Processes<br/><span style="font-size:20px;color:#3b82f6;font-weight:normal;">&#272;&#7863;c &#272;i&#7875;m Thu&#7927; V&#259;n &amp; C&aacute;c Qu&aacute; Tr&igrave;nh S&ocirc;ng</span></h1>
<p style="color:#64748b;font-size:16px;">Rivers, drainage basins, the water cycle and fluvial processes</p>
<p {VI}>S&ocirc;ng ng&ograve;i, l&#432;u v&#7921;c s&ocirc;ng, v&ograve;ng tu&#7847;n ho&agrave;n n&#432;&#7899;c v&agrave; c&aacute;c qu&aacute; tr&igrave;nh b&#7891;i t&#7909;</p>
</div>

<!-- Section 1: Drainage Basins -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">📍 1. Rivers &amp; Drainage Basins / S&ocirc;ng Ng&ograve;i &amp; L&#432;u V&#7921;c</h2>
<p style="color:#475569;margin-bottom:14px;">A <strong>drainage basin</strong> is the area of land drained by a river and all its tributaries. It is an <strong>open system</strong> with inputs (precipitation) and outputs (evaporation, river discharge). The boundary is the <strong>watershed</strong> — a ridge of high ground.</p>
<p {VI}><strong>L&#432;u v&#7921;c s&ocirc;ng (drainage basin)</strong> l&agrave; v&ugrave;ng &#273;&#7845;t &#273;&#432;&#7907;c tho&aacute;t n&#432;&#7899;c b&#7903;i m&#7897;t con s&ocirc;ng v&agrave; c&aacute;c ph&#7909; l&#432;u c&#7911;a n&oacute;. Ho&#7841;t &#273;&#7897;ng nh&#432; m&#7897;t <strong>h&#7879; th&#7889;ng m&#7903;</strong> c&oacute; &#273;&#7847;u v&agrave;o (l&#432;&#7907;ng m&#432;a) v&agrave; &#273;&#7847;u ra (b&#7889;c h&#417;i, d&ograve;ng ch&#7843;y). Ranh gi&#7899;i g&#7885;i l&agrave; <strong>&#273;&#432;&#7901;ng ph&acirc;n th&#7911;y (watershed)</strong> — th&#432;&#7901;ng theo g&#7901; &#273;&#7845;t cao.</p>

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:16px;">
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Source / Ngu&#7891;n</strong><br/><span style="color:#475569;font-size:13px;">Where river begins — usually on high ground<br/><em>N&#417;i s&ocirc;ng b&#7855;t &#273;&#7847;u — th&#432;&#7901;ng tr&ecirc;n v&ugrave;ng cao</em></span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Mouth / C&#7917;a S&ocirc;ng</strong><br/><span style="color:#475569;font-size:13px;">Where river meets the sea<br/><em>N&#417;i s&ocirc;ng &#273;&#7893; ra bi&#7875;n</em></span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Tributary / Ph&#7909; L&#432;u</strong><br/><span style="color:#475569;font-size:13px;">Smaller river flowing into main river<br/><em>S&ocirc;ng nh&aacute;nh &#273;&#7893; v&agrave;o s&ocirc;ng ch&iacute;nh</em></span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Confluence / H&#7907;p L&#432;u</strong><br/><span style="color:#475569;font-size:13px;">Where two rivers join<br/><em>&#272;i&#7875;m hai s&ocirc;ng nh&#7853;p v&agrave;o nhau</em></span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Watershed / &#272;&#432;&#7901;ng Ph&acirc;n Th&#7911;y</strong><br/><span style="color:#475569;font-size:13px;">Boundary between two basins<br/><em>Ranh gi&#7899;i gi&#7919;a hai l&#432;u v&#7921;c</em></span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">
<strong style="color:#1d4ed8;">Flood plain / &#272;&#7891;ng B&#7857;ng L&#361;</strong><br/><span style="color:#475569;font-size:13px;">Flat land beside river, floods when discharge is high<br/><em>&#272;&#7845;t b&#7857;ng ven s&ocirc;ng, ng&#7853;p khi l&#432;&#7907;ng n&#432;&#7899;c cao</em></span>
</div>
</div>

<img src="{IMG}hq_real_fig1_1_cropped_v3.jpeg" alt="Drainage basin" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.1 The features of a drainage basin / C&aacute;c b&#7897; ph&#7853;n c&#7911;a m&#7897;t l&#432;u v&#7921;c s&ocirc;ng</p>
<img src="{IMG}hq_fig1_2.jpeg" alt="Cross-section drainage basins" style="max-width:420px;height:auto;display:block;margin:0 auto;margin-top:14px;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.2 Cross-section showing drainage basins and watersheds</p>
</div>

<!-- Section 2: Bradshaw Model -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">📉 2. The Bradshaw Model / M&ocirc; H&igrave;nh Bradshaw</h2>
<p style="color:#475569;margin-bottom:12px;">The <strong>Bradshaw Model</strong> shows how river characteristics change systematically from source to mouth as discharge increases.</p>
<p {VI}><strong>M&ocirc; h&igrave;nh Bradshaw</strong> cho th&#7845;y c&aacute;c &#273;&#7863;c t&iacute;nh c&#7911;a s&ocirc;ng thay &#273;&#7893;i c&oacute; h&#7879; th&#7889;ng t&#7915; ngu&#7891;n &#273;&#7871;n c&#7917;a s&ocirc;ng khi l&#432;u l&#432;&#7907;ng t&#259;ng l&ecirc;n.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">
<strong style="color:#15803d;">T&#259;ng v&#7873; ph&iacute;a h&#7841; l&#432;u ↑</strong>
<ul style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;margin-bottom:0;">
<li>L&#432;u l&#432;&#7907;ng (Discharge) — nhi&#7873;u ph&#7909; l&#432;u nh&#7853;p v&agrave;o</li>
<li>Chi&#7873;u r&#7897;ng &amp; s&acirc;u (Width &amp; Depth)</li>
<li>V&#7853;n t&#7889;c (Velocity) — l&ograve;ng s&ocirc;ng tr&#417;n h&#417;n</li>
<li>T&#7893;ng l&#432;&#7907;ng ph&ugrave; sa</li>
</ul>
</div>
<div style="background:#fff7ed;border-left:4px solid #f97316;padding:14px;border-radius:6px;">
<strong style="color:#ea580c;">Gi&#7843;m v&#7873; ph&iacute;a h&#7841; l&#432;u ↓</strong>
<ul style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;margin-bottom:0;">
<li>&#272;&#7897; d&#7889;c (Gradient)</li>
<li>K&iacute;ch th&#432;&#7899;c h&#7841;t (Particle size) — va ch&#7841;m l&agrave;m nh&#7887;</li>
<li>&#272;&#7897; nh&#7845;p nh&ocirc; l&ograve;ng s&ocirc;ng (Roughness)</li>
<li>S&#432;&#7901;n th&#361;ng n&#7855;ng (Valley sides)</li>
</ul>
</div>
</div>
<img src="{IMG}hq_fig1_10.jpeg" alt="Bradshaw model" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.10 The Bradshaw model</p>
</div>

<!-- Section 3: Water Cycle -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🔄 3. The Water Cycle / V&ograve;ng Tu&#7847;n Ho&agrave;n N&#432;&#7899;c</h2>
<p style="color:#475569;margin-bottom:12px;">The water cycle describes how water moves through the drainage basin system via <strong>inputs, stores, transfers</strong> and <strong>outputs</strong>.</p>
<p {VI}>V&ograve;ng tu&#7847;n ho&agrave;n n&#432;&#7899;c m&ocirc; t&#7843; c&aacute;ch n&#432;&#7899;c di chuy&#7875;n qua h&#7879; th&#7889;ng l&#432;u v&#7921;c s&ocirc;ng th&ocirc;ng qua c&aacute;c <strong>&#273;&#7847;u v&agrave;o, kho tr&#7919;, truy&#7873;n chuy&#7875;n</strong> v&agrave; <strong>&#273;&#7847;u ra</strong>.</p>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;">
<div style="background:#f0f9ff;border:2px solid #bfdbfe;border-radius:10px;padding:14px;">
<h3 style="color:#1d4ed8;margin-bottom:10px;font-size:16px;">🌧️ Precipitation / L&#432;&#7907;ng M&#432;a</h3>
<p style="color:#475569;font-size:14px;">Main <strong>input</strong> into the basin. Rain, snow, sleet, hail. Heavy rain on saturated ground → rapid overland flow.</p>
<p {VI} style="font-size:13px;"><strong>&#272;&#7847;u v&agrave;o</strong> ch&iacute;nh: M&#432;a, tuy&#7871;t, m&#432;a &#273;&#225;. M&#432;a l&#7899;n tr&ecirc;n &#273;&#7845;t b&atilde;o h&ograve;a → d&ograve;ng ch&#7843;y b&#7873; m&#7863;t nhanh.</p>
</div>
<div style="background:#f0fdf4;border:2px solid #86efac;border-radius:10px;padding:14px;">
<h3 style="color:#15803d;margin-bottom:10px;font-size:16px;">🌿 Interception / Ch&#7855;n Gi&#7919;</h3>
<p style="color:#475569;font-size:14px;">Vegetation catches precipitation before it reaches the ground. Forests intercept up to 35% of annual rainfall — slows runoff, reduces flood risk.</p>
<p {VI} style="font-size:13px;">Th&#7921;c v&#7853;t h&#7913;ng m&#432;a tr&#432;&#7899;c khi ch&#7841;m &#273;&#7845;t. R&#7915;ng c&oacute; th&#7875; gi&#7919; t&#7899;i 35% l&#432;&#7907;ng m&#432;a h&agrave;ng n&#259;m — l&agrave;m ch&#7853;m d&ograve;ng ch&#7843;y, gi&#7843;m r&#7911;i ro l&#361;.</p>
</div>
<div style="background:#ecfeff;border:2px solid #67e8f9;border-radius:10px;padding:14px;">
<h3 style="color:#0891b2;margin-bottom:10px;font-size:16px;">💧 Surface Runoff / D&ograve;ng Ch&#7843;y B&#7873; M&#7863;t</h3>
<p style="color:#475569;font-size:14px;">Water flows over the surface when soil is saturated or impermeable. Fastest route to river channel. Urban areas have high surface runoff. Related: <em>throughflow</em> (lateral through soil) and <em>percolation</em> (downward into rock).</p>
<p {VI} style="font-size:13px;">N&#432;&#7899;c ch&#7843;y tr&#234;n b&#7873; m&#7863;t khi &#273;&#7845;t b&atilde;o h&ograve;a ho&#7863;c kh&ocirc;ng th&#7845;m. Con &#273;&#432;&#7901;ng nhanh nh&#7845;t &#273;&#7871;n s&ocirc;ng. &#272;&ocirc; th&#7883; c&oacute; d&ograve;ng ch&#7843;y b&#7873; m&#7863;t cao. Li&ecirc;n quan: <em>ch&#7843;y qua &#273;&#7845;t (throughflow)</em> v&agrave; <em>th&#7845;m s&acirc;u (percolation)</em>.</p>
</div>
<div style="background:#fdf4ff;border:2px solid #d8b4fe;border-radius:10px;padding:14px;">
<h3 style="color:#7c3aed;margin-bottom:10px;font-size:16px;">⬇️ Infiltration &amp; Groundwater / Th&#7845;m L&#7885;c &amp; N&#432;&#7899;c Ng&#7847;m</h3>
<p style="color:#475569;font-size:14px;">Infiltration: water soaks into soil. Percolation: water seeps deeper into rock. Groundwater stored in aquifers below water table → slow baseflow keeps rivers flowing in dry periods.</p>
<p {VI} style="font-size:13px;">Th&#7845;m l&#7885;c: n&#432;&#7899;c ng&#7845;m v&agrave;o &#273;&#7845;t. Th&#7845;m s&acirc;u: n&#432;&#7899;c xu&#7889;ng &#273;&aacute;. N&#432;&#7899;c ng&#7847;m l&#432;u tr&#7919; trong t&#7847;ng &#273;&#7845;t ng&#7853;m (aquifer) d&#432;&#7899;i m&#7921;c n&#432;&#7899;c ng&#7847;m → d&ograve;ng ch&#7843;y &#7901;n &#273;&#7883;nh gi&#7919; s&ocirc;ng ch&#7843;y trong m&ugrave;a kh&ocirc;.</p>
</div>
</div>
<div style="background:#fef9c3;border-left:4px solid #fde047;padding:14px;border-radius:6px;margin-bottom:16px;">
<strong style="color:#92400e;">☀️ Evapotranspiration / B&#7889;c H&#417;i N&#432;&#7899;c</strong>
<p style="color:#475569;font-size:14px;margin-top:8px;margin-bottom:0;"><strong>Evaporation</strong>: liquid water → vapour from surfaces (powered by solar energy). <strong>Transpiration</strong>: water released through plant leaf stomata. Combined output = evapotranspiration. Highest in hot, sunny, windy conditions with abundant vegetation — the main water output from a drainage basin.</p>
<p {VI} style="font-size:13px;"><strong>B&#7889;c h&#417;i (Evaporation)</strong>: n&#432;&#7899;c l&#7887;ng → h&#417;i n&#432;&#7899;c t&#7915; b&#7873; m&#7863;t (do n&#259;ng l&#432;&#7907;ng m&#7863;t tr&#7901;i). <strong>Tho&aacute;t h&#417;i l&aacute; (Transpiration)</strong>: n&#432;&#7899;c qua khuy&#7871;t kh&#7849;u l&aacute; c&acirc;y. T&#7893;ng c&#7897;ng = <em>evapotranspiration</em>. Cao nh&#7845;t khi tr&#7901;i n&oacute;ng, n&#7855;ng, gi&oacute; v&agrave; nhi&#7873;u th&#7921;c v&#7853;t.</p>
</div>
<img src="{IMG}hq_real_fig1_9_map.jpeg" alt="Water cycle drainage basin" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.9 The water cycle within a drainage basin</p>
</div>

<!-- Section 4: River Processes -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚙️ 4. Fluvial Processes / C&aacute;c Qu&aacute; Tr&igrave;nh S&ocirc;ng</h2>

<h3 style="color:#dc2626;margin-bottom:10px;">💥 Erosion / X&oacute;i M&ograve;n — 4 Ki&#7875;u</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;">
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:12px;border-radius:6px;">
<strong style="color:#dc2626;">Hydraulic action / L&#7921;c th&#7911;y &#273;&#7897;ng</strong><br/>
<span style="color:#475569;font-size:14px;">Force of water on bed/banks. Compresses air into cracks → weakens rock.</span><br/>
<span {VI} style="font-size:13px;">S&#7913;c n&#432;&#7899;c ch&#7843;y v&agrave;o l&ograve;ng v&agrave; b&#7901; s&ocirc;ng. N&eacute;n kh&ocirc;ng kh&iacute; v&agrave;o khe n&#7913;t → y&#7871;u &#273;&aacute;.</span>
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:12px;border-radius:6px;">
<strong style="color:#dc2626;">Corrasion / M&agrave;i M&ograve;n</strong><br/>
<span style="color:#475569;font-size:14px;">River uses load as sandpaper to scrape bed/banks. Main process deepening channel.</span><br/>
<span {VI} style="font-size:13px;">S&ocirc;ng d&ugrave;ng ph&ugrave; sa c&aacute;t &#273;&aacute; nh&#432; gi&#7845;y nh&aacute;m c&#7885; s&#225;t l&ograve;ng v&agrave; b&#7901;.</span>
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:12px;border-radius:6px;">
<strong style="color:#dc2626;">Attrition / Va Ch&#7841;m</strong><br/>
<span style="color:#475569;font-size:14px;">Rock fragments collide → smaller, rounder, smoother. Explains downstream particle size decrease.</span><br/>
<span {VI} style="font-size:13px;">C&aacute;c m&#7843;nh &#273;&aacute; va ch&#7841;m nhau → nh&#7887; h&#417;n, tr&ograve;n h&#417;n. Gi&#7843;i th&iacute;ch t&#7841;i sao h&#7841;t ph&ugrave; sa nh&#7887; d&#7847;n v&#7873; h&#7841; l&#432;u.</span>
</div>
<div style="background:#fff1f2;border-left:4px solid #f87171;padding:12px;border-radius:6px;">
<strong style="color:#dc2626;">Corrosion / H&ograve;a Tan</strong><br/>
<span style="color:#475569;font-size:14px;">Acidic water dissolves limestone/chalk. Calcium carbonate reacts with carbonic acid — invisible process.</span><br/>
<span {VI} style="font-size:13px;">N&#432;&#7899;c c&oacute; t&iacute;nh axit h&ograve;a tan &#273;&aacute; v&ocirc;i/ph&#7845;n tr&#7855;ng. Qu&aacute; tr&igrave;nh v&ocirc; h&igrave;nh.</span>
</div>
</div>
<img src="{IMG}hq_erosion.png" alt="Erosion processes" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ River erosion processes / C&aacute;c qu&aacute; tr&igrave;nh x&oacute;i m&ograve;n s&ocirc;ng</p>

<h3 style="color:#0369a1;margin-top:22px;margin-bottom:10px;">🚚 Transportation / V&#7853;n Chuy&#7875;n — 4 Ki&#7875;u</h3>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:16px;">
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Traction / K&eacute;o L&#7866;</strong><br/><span style="color:#475569;font-size:12px;">Boulders roll/slide along bed<br/><em>T&#7843;ng &#273;&aacute; l&#259;n theo &#273;&aacute;y</em></span>
</div>
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Saltation / Nh&#7843;y C&oacute;c</strong><br/><span style="color:#475569;font-size:12px;">Pebbles bounce along bed<br/><em>Cu&#7897;i n&#7843;y theo &#273;&aacute;y</em></span>
</div>
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Suspension / L&#417; L&#7917;ng</strong><br/><span style="color:#475569;font-size:12px;">Fine silt/clay held in water<br/><em>B&ugrave;n/s&eacute;t &#273;&#432;&#7907;c gi&#7919; trong n&#432;&#7899;c</em></span>
</div>
<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">
<strong style="color:#1d4ed8;font-size:13px;">Solution / H&ograve;a Tan</strong><br/><span style="color:#475569;font-size:12px;">Dissolved minerals in water<br/><em>Kho&aacute;ng ch&#7845;t h&ograve;a tan trong n&#432;&#7899;c</em></span>
</div>
</div>
<img src="{IMG}hq_transport.png" alt="Transportation" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ River transportation / V&#7853;n chuy&#7875;n ph&ugrave; sa s&ocirc;ng</p>

<h3 style="color:#15803d;margin-top:22px;margin-bottom:10px;">⬇️ Deposition / B&#7891;i T&#7909;</h3>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;margin-bottom:16px;">
<p style="color:#475569;margin:0;font-size:15px;">Occurs when river <strong>velocity and energy decrease</strong>. Heaviest particles deposited first (boulders), finest particles travel furthest (clay). Causes: reduced gradient, river enters lake/sea, dry conditions reduce discharge.</p>
<p {VI} style="font-size:14px;">X&#7843;y ra khi <strong>v&#7853;n t&#7889;c v&agrave; n&#259;ng l&#432;&#7907;ng s&ocirc;ng gi&#7843;m</strong>. H&#7841;t n&#7863;ng nh&#7845;t &#273;&#7885;ng xu&#7889;ng tr&#432;&#7899;c (&#273;&aacute; t&#7843;ng), h&#7841;t m&#7883;n nh&#7845;t &#273;i xa nh&#7845;t (s&eacute;t). Nguy&ecirc;n nh&acirc;n: &#273;&#7897; d&#7889;c gi&#7843;m, s&ocirc;ng &#273;&#7893; v&agrave;o h&#7891;/bi&#7875;n, &#273;i&#7873;u ki&#7879;n kh&ocirc; gi&#7843;m l&#432;u l&#432;&#7907;ng.</p>
</div>
<img src="{IMG}hq_deposition.png" alt="Deposition" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ River deposition / B&#7891;i t&#7909; s&ocirc;ng</p>
</div>
</div>"""

html = html.replace('{IMG}', IMG)
print(f'HTML length: {len(html)} chars')

r = requests.patch(
    f'{SUPABASE_URL}/rest/v1/lecture_pages?id=eq.{PAGE_ID}',
    json={'content_html': html},
    headers={'apikey': KEY,'Authorization':f'Bearer {KEY}','Content-Type':'application/json','Prefer':'return=minimal'}
)
print(f'PATCH 1.1 P2: HTTP {r.status_code}')
