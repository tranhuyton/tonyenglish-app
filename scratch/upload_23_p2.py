import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = '225ae3ec-3ab8-485e-b935-551a8df25bed'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/'
VI = 'style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"'

html = f"""<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#0369a1;font-size:30px;margin-bottom:10px;border-bottom:3px solid #38bdf8;display:inline-block;padding-bottom:10px;">🌊 2.3 Coastal Opportunities &amp; Hazards<br/><span style="font-size:20px;color:#0ea5e9;font-weight:normal;">C&#417; H&#7897;i &amp; Th&aacute;ch Th&#7913;c c&#7911;a V&ugrave;ng B&#7901; Bi&#7875;n</span></h1>
<p style="color:#64748b;font-size:16px;">How people use and are affected by coastal environments</p>
<p {VI}>Con ng&#432;&#7901;i s&#7917; d&#7909;ng v&agrave; b&#7883; &#7843;nh h&#432;&#7903;ng nh&#432; th&#7871; n&agrave;o b&#7903;i m&ocirc;i tr&#432;&#7901;ng b&#7901; bi&#7875;n</p>
</div>

<!-- Opportunities -->
<div style="margin-bottom:44px;">
<h2 style="color:#15803d;border-bottom:2px solid #4ade80;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🌿 1. C&#417; H&#7897;i (Opportunities)</h2>

<div style="background:#f0fdf4;border:2px solid #4ade80;border-radius:10px;padding:16px;margin-bottom:14px;">
<h3 style="color:#15803d;margin-bottom:8px;">🏖️ Tourism &amp; Recreation / Du L&#7883;ch v&agrave; Gi&#7843;i Tr&iacute;</h3>
<p style="color:#475569;">Coastal areas attract millions of tourists due to beaches, warm weather, water sports, coral reefs and marine biodiversity. Tourism is a major employer in the Caribbean, Mediterranean and SE Asia.</p>
<p {VI}>V&ugrave;ng b&#7901; bi&#7875;n thu h&uacute;t h&agrave;ng tri&#7879;u du kh&aacute;ch nh&#7901; b&#7427;i bi&#7875;n, kh&iacute; h&#7853;u &#7845;m &aacute;p, th&#7875; thao n&#432;&#7899;c, r&#7841;n san h&ocirc; v&agrave; &#273;a d&#7841;ng sinh h&#7885;c bi&#7875;n. Du l&#7883;ch l&agrave; ngu&#7891;n vi&#7879;c l&agrave;m quan tr&#7885;ng &#7903; Caribbean, &#272;&#7883;a Trung H&#7843;i v&agrave; &Dagger;&#244;ng Nam &Aacute;. V&iacute; d&#7909;: V&#7883;nh Rodney, St Lucia — t&agrave;u du l&#7883;ch, kh&aacute;ch s&#7841;n, th&#7875; thao n&#432;&#7899;c, l&#7863;n bi&#7875;n.</p>
</div>

<div style="background:#f0fdf4;border:2px solid #4ade80;border-radius:10px;padding:16px;margin-bottom:14px;">
<h3 style="color:#15803d;margin-bottom:8px;">🐟 Fishing &amp; Aquaculture / &Dagger;&aacute;nh B&#7855;t v&agrave; Nu&ocirc;i Tr&#7891;ng Th&#7911;y S&#7843;n</h3>
<p style="color:#475569;">Coastal waters supply most of the world's seafood. Artisanal fishing (small-scale, traditional) provides livelihoods for coastal communities. Aquaculture (fish, shrimp, oyster farming in ponds, lagoons) is growing rapidly.</p>
<p {VI}>V&ugrave;ng bi&#7875;n ven b&#7901; cung c&#7845;p h&#7847;u h&#7871;t h&#7843;i s&#7843;n to&agrave;n c&#7847;u. &Dagger;&aacute;nh b&#7855;t th&#7911; c&ocirc;ng (qui m&ocirc; nh&#7887;, truy&#7873;n th&#7889;ng) cung c&#7845;p sinh k&#7871; cho c&#7897;ng &#273;&#7891;ng ven bi&#7875;n. Nu&ocirc;i tr&#7891;ng th&#7911;y s&#7843;n (c&aacute;, t&ocirc;m, h&agrave;u trong &#273;&#7847;m, ao h&#7891;) &#273;ang ph&aacute;t tri&#7875;n nhanh. V&iacute; d&#7909;: Nu&ocirc;i t&ocirc;m &#7903; Bangladesh, nu&ocirc;i c&aacute; h&#7891;i &#7903; Na Uy.</p>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<h3 style="color:#15803d;margin-bottom:8px;">⚓ Transport &amp; Trade / V&#7853;n T&#7843;i v&agrave; Th&#432;&#417;ng M&#7841;i</h3>
<p style="color:#475569;font-size:14px;">&gt;80% of world trade by volume travels by sea. Major ports (Shanghai, Rotterdam, Singapore) drive global trade.</p>
<p {VI} style="font-size:14px;">&gt;80% h&agrave;ng h&oacute;a xu&#7845;t nh&#7853;p kh&#7849;u &#273;i b&#7857;ng &#273;&#432;&#7901;ng bi&#7875;n. C&#7843;ng l&#7899;n (Th&#432;&#7907;ng H&#7843;i, Rotterdam, Singapore) l&agrave; &#273;&#7897;ng l&#7921;c th&#432;&#417;ng m&#7841;i to&agrave;n c&#7847;u.</p>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:8px;">
<h3 style="color:#15803d;margin-bottom:8px;">🏙️ Settlement &amp; Industry / &Dagger;&#7883;nh C&#432; v&agrave; C&ocirc;ng Nghi&#7879;p</h3>
<p style="color:#475569;font-size:14px;">40% of world population lives within 100 km of coast. Flat coastal plains + agriculture + industry + energy (offshore wind, tidal).</p>
<p {VI} style="font-size:14px;">40% d&acirc;n s&#7889; th&#7871; gi&#7899;i s&#7889;ng trong v&ograve;ng 100km t&#7915; b&#7901; bi&#7875;n. &Dagger;&#7891;ng b&#7857;ng ven bi&#7875;n + n&ocirc;ng nghi&#7879;p + c&ocirc;ng nghi&#7879;p + n&#259;ng l&#432;&#7907;ng (gi&oacute; ngo&#7841;i kh&#417;i, th&#7911;y tri&#7873;u).</p>
</div>
</div>

<img src="{IMG}2_3_fig229.png" alt="Rodney Bay" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.29 Tourist development at Rodney Bay, St Lucia</p>
</div>

<!-- Hazards -->
<div style="margin-bottom:44px;">
<h2 style="color:#dc2626;border-bottom:2px solid #f87171;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚠️ 2. Hi&#7875;m H&#7885;a (Hazards)</h2>

<div style="background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:14px;">
<h3 style="color:#dc2626;margin-bottom:8px;">🌊 Coastal Erosion / X&oacute;i M&ograve;n B&#7901; Bi&#7875;n</h3>
<p style="color:#475569;">Rising sea levels and storms accelerate cliff retreat. Holderness, UK: ~2m/year. Farmland, villages and roads permanently lost.</p>
<p {VI}>M&#7921;c n&#432;&#7899;c bi&#7875;n d&acirc;ng v&agrave; b&atilde;o th&#432;&#7901;ng xuy&ecirc;n h&#417;n &#273;&#7849;y nhanh s&#7921; l&ugrave;i c&#7911;a v&aacute;ch &#273;&aacute;. B&#7901; bi&#7875;n Holderness, Anh: ~2m/n&#259;m. &Dagger;&#7845;t n&ocirc;ng nghi&#7879;p, l&agrave;ng x&#7843; v&agrave; &#273;&#432;&#7901;ng b&#7897; b&#7883; m&#7845;t v&#297;nh vi&#7877;n.</p>
</div>

<div style="background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:14px;">
<h3 style="color:#dc2626;margin-bottom:8px;">💧 Coastal Flooding / L&#361; L&#7909;t Ven Bi&#7875;n</h3>
<p style="color:#475569;">Three main causes: <strong>Storm surges</strong> (intense low pressure + winds push seawater inland), <strong>Sea level rise</strong> (~3.7 mm/yr from thermal expansion + melting ice — threatens Bangladesh, Maldives, Pacific islands), <strong>Tsunamis</strong> (2004 Indian Ocean: 9.1 magnitude, &gt;230,000 deaths across 14 countries).</p>
<p {VI}>Ba nguy&ecirc;n nh&acirc;n ch&iacute;nh: <strong>N&#432;&#7899;c d&acirc;ng do b&atilde;o</strong> (gi&aacute; kh&iacute; th&#7845;p + gi&oacute; &#273;&#7849;y n&#432;&#7899;c v&agrave;o &#273;&#7845;t li&#7873;n), <strong>N&#432;&#7899;c bi&#7875;n d&acirc;ng</strong> (~3,7mm/n&#259;m do gi&atilde;n n&#7903; nhi&#7879;t + tan b&#259;ng — &#273;e d&#7885;a Bangladesh, Maldives, &#273;&#7843;o Th&aacute;i B&igrave;nh D&#432;&#417;ng), <strong>S&oacute;ng th&#7847;n</strong> (2004 &#7844;n &Dagger;&#7897; D&#432;&#417;ng: 9,1 &#273;&#7897; richter, &gt;230.000 ng&#432;&#7901;i ch&#7871;t &#7903; 14 qu&#7889;c gia).</p>
</div>

<div style="background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:14px;">
<h3 style="color:#dc2626;margin-bottom:8px;">🌀 Tropical Cyclones / B&atilde;o Nhi&#7879;t &Dagger;&#7899;i</h3>
<p style="color:#475569;">Form over warm tropical seas (&gt;27°C). Bring winds &gt;119 km/h, storm surges up to 9m, extreme rainfall. Named: <strong>Hurricanes</strong> (Atlantic/Caribbean), <strong>Typhoons</strong> (W. Pacific), <strong>Cyclones</strong> (Indian Ocean). Management: satellite prediction, evacuation, wind-resistant buildings (hurricane straps, shutters), land-use zoning, mangrove restoration.</p>
<p {VI}>H&igrave;nh th&agrave;nh tr&ecirc;n bi&#7875;n nhi&#7879;t &#273;&#7899;i &#7845;m (&gt;27°C). Mang theo gi&oacute; &gt;119 km/h, n&#432;&#7899;c d&acirc;ng do b&atilde;o &#273;&#7871;n 9m, m&#432;a c&#7921;c &#273;&#7841;i. T&ecirc;n g&#7885;i theo khu v&#7921;c: <strong>Hurricane</strong> (&Dagger;&#7841;i T&acirc;y D&#432;&#417;ng/Caribbean), <strong>Typhoon</strong> (T&acirc;y Th&aacute;i B&igrave;nh D&#432;&#417;ng), <strong>Cyclone</strong> (&#7844;n &Dagger;&#7897; D&#432;&#417;ng). Qu&#7843;n l&yacute;: d&#7921; b&aacute;o v&#7879; tinh, s&#417; t&aacute;n, nh&agrave; ch&#7883;u gi&oacute; (&#273;ai l&#7845;p m&aacute;i, c&#7917;a ch&#7889;p th&eacute;p), ph&aacute;t tri&#7875;n c&oacute; ki&#7875;m so&aacute;t, tr&#7891;ng r&#7915;ng ng&#7853;p m&#7863;n.</p>
</div>
</div>

<!-- Management -->
<div style="margin-bottom:40px;">
<h2 style="color:#0369a1;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🏗️ 3. Qu&#7843;n L&yacute; B&#7901; Bi&#7875;n (Coastal Management)</h2>
<p {VI}>C&oacute; 4 chi&#7871;n l&#432;&#7907;c ch&iacute;nh: <strong>Kh&ocirc;ng l&agrave;m g&igrave;</strong> (&#273;&#7875; t&#7921; nhi&ecirc;n di&#7877;n ra), <strong>Duy tr&igrave; b&#7843;o v&#7879; hi&#7879;n t&#7841;i</strong>, <strong>C&#7843;i thi&#7879;n b&#7843;o v&#7879;</strong>, ho&#7863;c <strong>R&uacute;t lui c&oacute; qu&#7843;n l&yacute;</strong>. &Dagger;&#432;&#7907;c ph&acirc;n th&agrave;nh k&#7929; thu&#7853;t c&#7913;ng (ch&#7889;ng l&#7841;i t&#7921; nhi&ecirc;n) v&agrave; k&#7929; thu&#7853;t m&#7873;m (h&ograve;a h&#7907;p v&#7899;i t&#7921; nhi&ecirc;n).</p>

<h3 style="color:#0369a1;margin-bottom:10px;">K&#7929; thu&#7853;t c&#7913;ng (Hard Engineering)</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px;">
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px;border-radius:8px;font-size:14px;">
<strong>T&#432;&#7901;ng bi&#7875;n (Sea walls)</strong><br/><span style="color:#475569;">Ph&#7843;n x&#7841; n&#259;ng l&#432;&#7907;ng s&oacute;ng. ✅ Hi&#7879;u qu&#7843;, b&#7873;n 30–40 n&#259;m. ❌ R&#7845;t &#273;&#7855;t ti&#7873;n.</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px;border-radius:8px;font-size:14px;">
<strong>K&egrave; bi&#7875;n (Revetments)</strong><br/><span style="color:#475569;">H&#7845;p th&#7909; s&oacute;ng &#7903; ch&acirc;n v&aacute;ch &#273;&aacute;. ✅ R&#7867; h&#417;n t&#432;&#7901;ng. ❌ Tu&#7893;i th&#7885; ng&#7855;n.</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px;border-radius:8px;font-size:14px;">
<strong>&Dagger;&#7853;p Groyne</strong><br/><span style="color:#475569;">Ng&#259;n d&ograve;ng ch&#7843;y ven b&#7901;, gi&#7919; c&aacute;t. ✅ X&acirc;y d&#7921;ng b&#7875;n b&atilde;i. ❌ L&agrave;m ngh&egrave;o b&#7843;i ph&iacute;a d&#432;&#7899;i.</span>
</div>
<div style="background:#f0f9ff;border-left:4px solid #0ea5e9;padding:12px;border-radius:8px;font-size:14px;">
<strong>&Dagger;&aacute; h&#7897;c (Rock armour/Rip-rap)</strong><br/><span style="color:#475569;">T&#7843;ng &aacute; l&#7899;n h&#7845;p th&#7909;/gi&#7843;m s&oacute;ng. ✅ T&#432;&#417;ng &#273;&#7889;i r&#7867;. ❌ M&#7845;t m&#7929; quan, c&oacute; th&#7875; d&#7883;ch chuy&#7875;n.</span>
</div>
</div>

<h3 style="color:#15803d;margin-bottom:10px;">K&#7929; thu&#7853;t m&#7873;m (Soft Engineering)</h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:12px;border-radius:8px;font-size:14px;">
<strong>B&#7893; sung c&aacute;t (Beach nourishment)</strong><br/><span style="color:#475569;">B&#417;m c&aacute;t t&#7915; &#273;&aacute;y bi&#7875;n l&ecirc;n b&#7857;i. ✅ T&#7921; nhi&ecirc;n, t&#7889;t cho du l&#7883;ch. ❌ &Dagger;&#7855;t ti&#7873;n, ng&#7855;n h&#7841;n.</span>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:12px;border-radius:8px;font-size:14px;">
<strong>R&uacute;t lui c&oacute; qu&#7843;n l&yacute; (Managed retreat)</strong><br/><span style="color:#475569;">Cho ph&eacute;p ng&#7853;p/x&oacute;i t&#7921; nhi&ecirc;n. ✅ Ti&#7871;t ki&#7879;m, t&#7921; nhi&ecirc;n, t&#7841;o &#273;&#7845;t ng&#7853;p n&#432;&#7899;c. ❌ Kh&ocirc;ng &#273;&#432;&#7907;c &#432;a chu&#7897;ng, m&#7845;t &#273;&#7845;t.</span>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:12px;border-radius:8px;font-size:14px;">
<strong>Ph&#7909;c h&#7891;i c&#7891;n c&aacute;t (Dune regeneration)</strong><br/><span style="color:#475569;">Tr&#7891;ng c&#7887; marram, r&agrave;o ch&#7855;n c&aacute;t. ✅ B&#7873;n v&#7919;ng, &#273;a d&#7841;ng sinh h&#7885;c. ❌; Qu&aacute; tr&igrave;nh ch&#7853;m.</span>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:12px;border-radius:8px;font-size:14px;">
<strong>R&#7841;n nh&acirc;n t&#7841;o (Offshore reefs)</strong><br/><span style="color:#475569;">Ch&igrave;m v&#7853;t li&#7879;u ngo&agrave;i kh&#417;i h&#7845;p th&#7909; s&oacute;ng. ✅ C&ocirc;ng ngh&#7879; th&#7845;p, t&#432;&#417;ng &#273;&#7889;i r&#7867;. ❌ T&aacute;c &#273;&#7897;ng d&agrave;i h&#7841;n ch&#432;a bi&#7871;t.</span>
</div>
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
print(f'PATCH 2.3 P2: HTTP {r.status_code}')
