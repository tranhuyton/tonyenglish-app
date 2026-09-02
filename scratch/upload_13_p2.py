import requests

PAGE_ID = "cf88e936-fa2c-48f2-a9ed-6f81362ba421"
SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>1.3 Rivers: Opportunities &amp; Hazards (Bilingual)</title>
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
  /* Vietnamese translation style */
  .vi { color: #64748b; font-style: italic; font-size: 15px; margin-top: 6px; margin-bottom: 16px; border-left: 3px solid #cbd5e1; padding-left: 12px; }
  .vi ul { margin: 4px 0 4px 16px; }
  .vi li { margin-bottom: 4px; }
  /* Interactive SVG */
  #svg-section { margin: 30px 0; }
  #def-panel { display: none; background: #1e293b; color: #f8fafc; padding: 18px 22px; border-radius: 10px; margin-top: 16px; font-size: 15px; }
  #def-panel h4 { margin: 0 0 6px 0; font-size: 17px; }
  #def-panel p { margin: 0 0 8px 0; }
  #def-panel .vi-def { color: #94a3b8; font-style: italic; font-size: 14px; border-left: 2px solid #475569; padding-left: 10px; margin-top: 4px; }
  /* Grids */
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
  .term-card .vi-term { color: #64748b; font-style: italic; font-size: 13px; }
  @media (max-width: 600px) { .eng-grid, .impacts-grid, .terms-grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>

<h1>&#127754; 1.3 Rivers: Opportunities &amp; Hazards</h1>
<p style="color:#64748b; font-size:15px; margin-top:4px;"><em>How living near rivers brings both benefits and risks</em></p>
<p class="vi">&#127754; 1.3 S&#244;ng: C&#417; H&#7897;i v&#224; Nguy C&#417; &mdash; S&#7889;ng g&#7847;n s&#244;ng mang l&#7841;i l&#7907;i &#237;ch l&#7851;n r&#7911;i ro</p>

<!-- ══════════════ INTERACTIVE SVG ══════════════ -->
<div id="svg-section">
  <svg viewBox="0 0 860 320" xmlns="http://www.w3.org/2000/svg"
       style="width:100%;border-radius:12px;background:#f8fafc;border:1px solid #e2e8f0;cursor:pointer;"
       role="img" aria-label="Rivers: Opportunities and Hazards diagram">
    <rect x="0" y="0" width="860" height="42" fill="#1e3a8a" rx="12"/>
    <text x="430" y="27" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-weight="700" font-size="15">Living Near Rivers / S&#7889;ng g&#7847;n s&#244;ng &mdash; Click a topic to explore</text>
    <rect x="0" y="42" width="430" height="278" fill="#f0fdf4"/>
    <rect x="430" y="42" width="430" height="278" fill="#fff7ed"/>
    <rect x="408" y="42" width="44" height="278" fill="#bfdbfe"/>
    <text x="430" y="108" text-anchor="middle" fill="#1e40af" font-family="Inter,sans-serif" font-size="11" font-weight="600" transform="rotate(-90,430,108)">R I V E R</text>
    <text x="210" y="68" text-anchor="middle" fill="#15803d" font-family="Inter,sans-serif" font-weight="800" font-size="15">&#127807; OPPORTUNITIES / C&#417; H&#7897;i</text>
    <text x="648" y="68" text-anchor="middle" fill="#c2410c" font-family="Inter,sans-serif" font-weight="800" font-size="15">&#9888;&#65039; HAZARDS / Nguy C&#417;</text>
    <!-- Opportunity buttons -->
    <g onclick="showDef('water_supply')" style="cursor:pointer">
      <rect x="18" y="84" width="140" height="46" rx="8" fill="#22c55e" opacity="0.85"/>
      <text x="88" y="103" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#128167;</text>
      <text x="88" y="120" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="11" font-weight="600">Water / C&#7845;p N&#432;&#7899;c</text>
    </g>
    <g onclick="showDef('agriculture')" style="cursor:pointer">
      <rect x="168" y="84" width="140" height="46" rx="8" fill="#16a34a" opacity="0.85"/>
      <text x="238" y="103" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#127806;</text>
      <text x="238" y="120" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="11" font-weight="600">Agriculture / N&#244;ng Nghi&#7879;p</text>
    </g>
    <g onclick="showDef('fishing')" style="cursor:pointer">
      <rect x="18" y="144" width="140" height="46" rx="8" fill="#22c55e" opacity="0.85"/>
      <text x="88" y="163" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#127907;</text>
      <text x="88" y="180" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="11" font-weight="600">Fishing / &#272;&#225;nh C&#225;</text>
    </g>
    <g onclick="showDef('transport')" style="cursor:pointer">
      <rect x="168" y="144" width="140" height="46" rx="8" fill="#16a34a" opacity="0.85"/>
      <text x="238" y="163" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#128674;</text>
      <text x="238" y="180" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="11" font-weight="600">Transport / Giao Th&#244;ng</text>
    </g>
    <g onclick="showDef('tourism')" style="cursor:pointer">
      <rect x="18" y="204" width="140" height="46" rx="8" fill="#22c55e" opacity="0.85"/>
      <text x="88" y="223" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#127964;&#65039;</text>
      <text x="88" y="240" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="11" font-weight="600">Tourism / Du L&#7883;ch</text>
    </g>
    <g onclick="showDef('hep')" style="cursor:pointer">
      <rect x="168" y="204" width="140" height="46" rx="8" fill="#16a34a" opacity="0.85"/>
      <text x="238" y="223" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#9889;</text>
      <text x="238" y="240" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="11" font-weight="600">HEP / Thu&#7927; &#272;i&#7879;n</text>
    </g>
    <!-- Hazard buttons -->
    <g onclick="showDef('flooding')" style="cursor:pointer">
      <rect x="462" y="104" width="160" height="76" rx="8" fill="#f97316" opacity="0.9"/>
      <text x="542" y="132" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="24">&#127754;</text>
      <text x="542" y="156" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="13" font-weight="700">Flooding / L&#361; L&#7909;t</text>
      <text x="542" y="173" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="10">(click to explore)</text>
    </g>
    <g onclick="showDef('pollution')" style="cursor:pointer">
      <rect x="638" y="104" width="160" height="76" rx="8" fill="#dc2626" opacity="0.85"/>
      <text x="718" y="132" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="24">&#9760;&#65039;</text>
      <text x="718" y="156" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="13" font-weight="700">Pollution / &#212; Nhi&#7877;m</text>
      <text x="718" y="173" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="10">(click to explore)</text>
    </g>
    <g onclick="showDef('management')" style="cursor:pointer">
      <rect x="462" y="204" width="336" height="52" rx="8" fill="#7c3aed" opacity="0.85"/>
      <text x="630" y="227" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="17">&#128295;&#65039;</text>
      <text x="630" y="246" text-anchor="middle" fill="white" font-family="Inter,sans-serif" font-size="12" font-weight="700">Flood Management / Qu&#7843;n L&#253; L&#361; L&#7909;t</text>
    </g>
    <path d="M408 286 Q418 276 430 286 Q442 296 452 286" stroke="#60a5fa" stroke-width="2.5" fill="none"/>
    <path d="M408 301 Q418 291 430 301 Q442 311 452 301" stroke="#93c5fd" stroke-width="2" fill="none"/>
  </svg>

  <div id="def-panel">
    <h4 id="def-title"></h4>
    <p id="def-body"></p>
    <div class="vi-def" id="def-vi"></div>
  </div>
</div>

<script>
const defs = {
  water_supply: {
    title: "&#128167; Water Supply",
    body: "Rivers provide a reliable, year-round source of fresh water for drinking, cooking, sanitation, irrigation of crops, and industrial processes. Cities have historically grown beside rivers for exactly this reason.",
    vi: "S&#244;ng cung c&#7845;p ngu&#7891;n n&#432;&#7899;c ng&#7885;t &#7893;n &#273;&#7883;nh quanh n&#259;m cho sinh ho&#7841;t, t&#432;&#7899;i ti&#234;u n&#244;ng nghi&#7879;p v&#224; s&#7843;n xu&#7845;t c&#244;ng nghi&#7879;p. &#272;&#226;y l&#224; l&#253; do ch&#237;nh khi&#7871;n c&#225;c th&#224;nh ph&#7889; l&#7883;ch s&#7917; h&#236;nh th&#224;nh b&#234;n c&#7841;nh s&#244;ng ng&#242;i."
  },
  agriculture: {
    title: "&#127806; Agriculture &amp; Fertile Soils",
    body: "Rivers deposit alluvium (fine, nutrient-rich sediment) on their floodplains during floods. These alluvial soils are highly fertile and productive for farming. The Nile, Mesopotamia, and Indus valleys were all cradles of early civilisation.",
    vi: "S&#244;ng b&#7891;i &#273;&#7855;p ph&#249; sa (&#273;&#7845;t m&#225;u m&#7905;, gi&#224;u ch&#7845;t dinh d&#432;&#7905;ng) l&#234;n &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#361;t trong m&#249;a l&#361;. &#272;&#226;y l&#224; n&#7873;n t&#7843;ng c&#7911;a n&#7873;n v&#259;n minh Ai C&#7853;p (s&#244;ng Nile), L&#432;&#7905;ng H&#224; (Tigris &amp; Euphrates) v&#224; &#7845;n &#272;&#7897; (s&#244;ng Indus)."
  },
  fishing: {
    title: "&#127907; Fishing / &#272;&#225;nh C&#225;",
    body: "Rivers and their connected wetlands support abundant fish populations, providing a significant protein source for millions of people worldwide.",
    vi: "S&#244;ng ng&#242;i v&#224; c&#225;c v&#249;ng &#273;&#7845;t ng&#7853;p n&#432;&#7899;c c&#7843;nh s&#244;ng cung c&#7845;p ngu&#7891;n h&#7843;i s&#7843;n phong ph&#250;, l&#224; ngu&#7891;n &#273;&#7841;m quan tr&#7885;ng cho h&#224;ng tri&#7879;u ng&#432;&#7901;i tr&#234;n th&#7871; gi&#7899;i."
  },
  transport: {
    title: "&#128674; Transport &amp; Trade / Giao Th&#244;ng",
    body: "Before roads and railways, rivers were the primary highways for moving people and goods. Wide, navigable rivers enabled the growth of port cities at their mouths and confluences.",
    vi: "Tr&#432;&#7899;c khi c&#243; &#273;&#432;&#7901;ng b&#7897; v&#224; &#273;&#432;&#7901;ng s&#7855;t, s&#244;ng l&#224; tuy&#7871;n giao th&#244;ng ch&#237;nh &#273;&#7875; v&#7853;n chuy&#7875;n ng&#432;&#7901;i v&#224; h&#224;ng h&#243;a. C&#225;c con s&#244;ng r&#7897;ng, d&#7877; th&#244;ng thuy&#7873;n &#273;&#227; th&#250;c &#273;&#7849;y s&#7921; ph&#225;t tri&#7875;n c&#7911;a c&#225;c th&#224;nh ph&#7889; c&#7843;ng."
  },
  tourism: {
    title: "&#127964;&#65039; Tourism &amp; Recreation / Du L&#7883;ch",
    body: "Scenic river valleys, gorges, and waterfalls attract tourists. Activities include boating, kayaking, fishing, and hiking. Riverside real estate commands premium prices.",
    vi: "C&#225;c th&#249;ng l&#361;ng s&#244;ng, khe su&#7889;i v&#224; th&#225;c n&#432;&#7899;c &#273;&#7865;p thu h&#250;t du kh&#225;ch. Ho&#7841;t &#273;&#7897;ng bao g&#7891;m ch&#232;o thuy&#7873;n, c&#226;u c&#225;, &#273;i b&#7897;. B&#7845;t &#273;&#7897;ng s&#7843;n ven s&#244;ng c&#243; gi&#225; tr&#7883; cao h&#417;n."
  },
  hep: {
    title: "&#9889; Hydroelectric Power / Thu&#7927; &#272;i&#7879;n",
    body: "Dams harness the energy of flowing water to generate HEP — a clean, renewable energy source. Multipurpose schemes also provide flood control, water storage, and improved navigation. Example: River Danube locks.",
    vi: "&#272;&#7853;p th&#7911;y &#273;i&#7879;n khai th&#225;c n&#259;ng l&#432;&#7907;ng d&#242;ng ch&#7843;y &#273;&#7875; t&#7841;o ra &#273;i&#7879;n s&#7841;ch, t&#225;i t&#7841;o. C&#225;c d&#7921; &#225;n &#273;a m&#7909;c &#273;&#237;ch c&#242;n gi&#250;p ki&#7875;m so&#225;t l&#361; l&#7909;t, tr&#7919; n&#432;&#7899;c v&#224; c&#7843;i thi&#7879;n giao th&#244;ng th&#7911;y. V&#237; d&#7909;: h&#7879; th&#7889;ng &#226;u thuy&#7873;n s&#244;ng Danube (ch&#226;u &#194;u)."
  },
  flooding: {
    title: "&#127754; Flooding / L&#361; L&#7909;t",
    body: "Flooding occurs when a river overtops its banks and inundates surrounding land. Natural causes include heavy rainfall, snowmelt, steep slopes, and impermeable rock. Human causes include urbanisation, deforestation, and floodplain development.",
    vi: "L&#361; l&#7909;t x&#7843;y ra khi m&#7921;c n&#432;&#7899;c s&#244;ng v&#432;&#7907;t qu&#225; d&#8217;ng kh&#432;. Nguy&#234;n nh&#226;n t&#7921; nhi&#234;n: m&#432;a l&#7899;n, tan tuy&#7871;t, &#273;&#7883;a h&#236;nh d&#7889;c, &#273;&#7845;t &#273;&#225; kh&#244;ng th&#7845;m n&#432;&#7899;c. Nguy&#234;n nh&#226;n con ng&#432;&#7901;i: &#273;&#244; th&#7883; h&#243;a, ph&#225; r&#7915;ng, x&#226;y d&#7921;ng tr&#234;n &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#361;t."
  },
  pollution: {
    title: "&#9760;&#65039; River Pollution / &#212; Nhi&#7877;m S&#244;ng",
    body: "Rivers can be polluted by industrial effluent, agricultural run-off (pesticides and fertilisers), sewage discharge, and oil spills. Pollution destroys aquatic ecosystems and contaminates drinking water.",
    vi: "S&#244;ng c&#243; th&#7875; b&#7883; &#244; nhi&#7877;m do ch&#7845;t th&#7843;i c&#244;ng nghi&#7879;p, d&#242;ng ch&#7843;y n&#244;ng nghi&#7879;p (thu&#7889;c tr&#7915; s&#226;u, ph&#226;n b&#243;n), x&#7843; n&#432;&#7899;c th&#7843;i v&#224; tr&#224;n d&#7847;u. &#212; nhi&#7877;m h&#7911;y ho&#7841;i h&#7879; sinh th&#225;i d&#432;&#7899;i n&#432;&#7899;c v&#224; g&#226;y nguy hi&#7875;m cho ngu&#7891;n n&#432;&#7899;c u&#7889;ng."
  },
  management: {
    title: "&#128295;&#65039; Flood Management / Qu&#7843;n L&#253; L&#361; L&#7909;t",
    body: "Hard engineering uses physical structures: dams, lev&#233;es, channelisation, flood barriers (e.g. Thames Barrier). Soft engineering works with nature: floodplain zoning, afforestation, wetland restoration, and SuDS.",
    vi: "C&#244;ng tr&#236;nh c&#7913;ng (Hard Engineering) s&#7917; d&#7909;ng c&#244;ng tr&#236;nh v&#7853;t l&#253;: &#273;&#7853;p, &#273;&#234;, n&#7855;n th&#7859;ng l&#242;ng s&#244;ng, r&#224;o ch&#7855;n l&#361;. C&#244;ng tr&#236;nh m&#7873;m (Soft Engineering) l&#224;m vi&#7879;c c&#249;ng t&#7921; nhi&#234;n: quy ho&#7841;ch v&#249;ng, tr&#7891;ng r&#7915;ng, ph&#7909;c h&#7891;i &#273;&#7845;t ng&#7853;p n&#432;&#7899;c v&#224; SuDS."
  }
};
function showDef(key) {
  const panel = document.getElementById('def-panel');
  if (defs[key]) {
    document.getElementById('def-title').innerHTML = defs[key].title;
    document.getElementById('def-body').innerHTML = defs[key].body;
    document.getElementById('def-vi').innerHTML = defs[key].vi;
    panel.style.display = 'block';
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}
</script>

<!-- ══════════════ SECTION 1: OPPORTUNITIES ══════════════ -->
<h2>&#127807; Section 1: Opportunities of Living Near Rivers</h2>
<p class="vi"><strong>&#127807; M&#7909;c 1: C&#417; H&#7897;i Khi S&#7889;ng G&#7847;n S&#244;ng</strong></p>

<p>Rivers have attracted human settlement since prehistory. They offer a unique combination of resources that make them ideal locations to live, farm, trade, and build communities.</p>
<p class="vi">V&#249;ng &#273;&#7845;t ven s&#244;ng, &#273;&#7863;c bi&#7879;t &#7903; h&#7841; l&#432;u, th&#432;&#7901;ng r&#7845;t &#273;&#244;ng d&#226;n v&#236; nh&#7919;ng l&#253; do sau. S&#244;ng ng&#242;i &#273;&#227; thu h&#250;t c&#7843; v&#259;n minh nh&#226;n lo&#7841;i t&#7915; th&#7901;i ti&#7873;n s&#7917;.</p>

<div class="info-box green">
  <strong>Key Fact:</strong> The world's earliest civilisations — Egypt (Nile), Mesopotamia (Tigris &amp; Euphrates), and the Indus Valley — all developed beside rivers. Reliable water and fertile soils were the foundations of organised society.
  <p class="vi" style="margin-bottom:0;">S&#7921; xu&#7845;t hi&#7879;n c&#7911;a c&#225;c th&#224;nh ph&#7889; &#273;&#7847;u ti&#234;n tr&#234;n th&#7871; gi&#7899;i c&#225;ch &#273;&#226;y 5.500 n&#259;m g&#7855;n li&#7873;n v&#7899;i c&#225;c th&#249;ng l&#361;ng s&#244;ng m&#224;u m&#7905;: L&#432;&#7905;ng H&#224; (s&#244;ng Tigris v&#224; Euphrates), th&#249;ng l&#361;ng s&#244;ng Nile (Ai C&#7853;p) v&#224; &#273;&#7891;ng b&#7857;ng s&#244;ng Indus (Pakistan).</p>
</div>

<h3>Water Supply</h3>
<p>Rivers provide a <b class="key-term">perennial</b> (year-round) source of fresh water for drinking, cooking, sanitation, and industry. This reliability was critical before the age of pipelines and reservoirs.</p>
<p class="vi"><strong>C&#7845;p n&#432;&#7899;c:</strong> Ngu&#7891;n n&#432;&#7899;c &#273;&#225;ng tin c&#7853;y cho sinh ho&#7841;t h&#224;ng ng&#224;y, t&#432;&#7899;i ti&#234;u n&#244;ng nghi&#7879;p v&#224; s&#7843;n xu&#7845;t c&#244;ng nghi&#7879;p. &#272;&#226;y l&#224; &#273;i&#7873;u ki&#7879;n then ch&#7889;t tr&#432;&#7899;c khi c&#243; h&#7879; th&#7889;ng &#7889;ng d&#7851;n v&#224; h&#7891; ch&#7913;a n&#432;&#7899;c hi&#7879;n &#273;&#7841;i.</p>

<h3>Agriculture and Alluvial Soils</h3>
<p>When rivers flood, they deposit <b class="key-term">alluvium</b> — fine, nutrient-rich sediment — across the <b class="key-term">floodplain</b>. These <b class="key-term">alluvial soils</b> are exceptionally fertile, supporting high-yield farming with minimal fertiliser input.</p>
<p class="vi"><strong>N&#244;ng nghi&#7879;p:</strong> Khi s&#244;ng ng&#226;p l&#361;t, ph&#249; sa (&#273;&#7845;t m&#225;u m&#7905;, gi&#224;u dinh d&#432;&#7905;ng) &#273;&#432;&#7907;c b&#7891;i &#273;&#7855;p tr&#234;n &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#361;t. &#272;&#7845;t ph&#249; sa r&#7845;t m&#224;u m&#7905;, h&#7895; tr&#7907; n&#244;ng nghi&#7879;p n&#259;ng su&#7845;t cao v&#7899;i &#237;t ph&#226;n b&#243;n.</p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig134.png" alt="Nile valley aerial view showing fertile green farmland alongside the desert"/>
<p class="caption">Fig 1.34 &#8212; The Nile valley: a narrow ribbon of intensely cultivated land in an otherwise arid landscape. / Th&#249;ng l&#361;ng s&#244;ng Nile: d&#7843;i &#273;&#7845;t canh t&#225;c tr&#224;n &#273;&#7847;y m&#224;u xanh gi&#7919;a s&#7913; a m&#7841;c.</p>

<div class="info-box">
  <strong>Examples of river-based civilisations:</strong>
  <ul>
    <li><b>Nile valley, Egypt</b> — annual floods deposited rich silt; the basis of Ancient Egyptian agriculture</li>
    <li><b>Mesopotamia</b> (modern Iraq) — the "Fertile Crescent" between the Tigris and Euphrates rivers</li>
    <li><b>Indus valley</b> (modern Pakistan/India) — one of the world's first urban civilisations, c. 3300&#8211;1300 BCE</li>
  </ul>
  <p class="vi" style="margin-bottom:0;"><strong>V&#237; d&#7909; c&#225;c n&#7873;n v&#259;n minh ven s&#244;ng:</strong>
  <ul class="vi" style="margin-top:4px;">
    <li><b>Th&#249;ng l&#361;ng s&#244;ng Nile, Ai C&#7853;p</b> &#8212; l&#361; h&#224;ng n&#259;m b&#7891;i &#273;&#7855;p ph&#249; sa; n&#7873;n t&#7843;ng n&#244;ng nghi&#7879;p Ai C&#7853;p c&#7893; &#273;&#7841;i</li>
    <li><b>L&#432;&#7905;ng H&#224;</b> (Iraq hi&#7879;n &#273;&#7841;i) &#8212; "Vành &#273;ai M&#224;u m&#7905;" gi&#7919;a s&#244;ng Tigris v&#224; Euphrates</li>
    <li><b>&#272;&#7891;ng b&#7857;ng s&#244;ng Indus</b> (Pakistan/&#7844;n &#272;&#7897;) &#8212; m&#7897;t trong nh&#7919;ng v&#259;n minh &#273;&#244; th&#7883; &#273;&#7847;u ti&#234;n, kho&#7843;ng 3300&#8211;1300 TCN</li>
  </ul></p>
</div>

<h3>Fishing</h3>
<p>Rivers and associated wetlands support productive fisheries. Fish provide an important protein source and support livelihoods for millions of people globally.</p>
<p class="vi"><strong>&#272;&#225;nh b&#7855;t c&#225;:</strong> S&#244;ng ng&#242;i v&#224; c&#225;c v&#249;ng &#273;&#7845;t ng&#7853;p n&#432;&#7899;c l&#224; ngu&#7891;n th&#7921;c ph&#7849;m b&#7893; sung quan tr&#7885;ng, c&#7843;i thi&#7879;n sinh k&#7871; cho h&#224;ng tri&#7879;u ng&#432;&#7901;i, &#273;&#7863;c bi&#7879;t &#7903; Ch&#226;u &#193; v&#224; ch&#226;u Phi.</p>

<h3>Transport</h3>
<p>Before roads and railways, rivers were the primary highways for moving goods and people. Many modern cities (London, Cairo, Paris, Shanghai) developed at key river crossing or trading points.</p>
<p class="vi"><strong>Giao th&#244;ng:</strong> Tr&#432;&#7899;c khi c&#243; &#273;&#432;&#7901;ng b&#7897; v&#224; &#273;&#432;&#7901;ng s&#7855;t, s&#244;ng l&#224; tuy&#7871;n &#273;&#432;&#7901;ng ch&#237;nh v&#7853;n chuy&#7875;n h&#224;ng h&#243;a v&#224; con ng&#432;&#7901;i. Nhi&#7873;u th&#224;nh ph&#7889; l&#7899;n ng&#224;y nay (London, Cairo, Paris, Th&#432;&#7907;ng H&#7843;i) h&#236;nh th&#224;nh t&#7841;i c&#225;c &#273;i&#7875;m giao th&#244;ng quan tr&#7885;ng tr&#234;n s&#244;ng.</p>

<h3>Hydroelectric Power (HEP)</h3>
<p>Dams built across rivers harness the kinetic energy of water to generate <b class="key-term">hydroelectric power (HEP)</b> &#8212; a clean, renewable energy source. <b class="key-term">Multipurpose river schemes</b> combine several functions in a single infrastructure project.</p>
<p class="vi"><strong>Thu&#7927; &#273;i&#7879;n (HEP):</strong> &#272;&#7853;p th&#7911;y &#273;i&#7879;n khai th&#225;c n&#259;ng l&#432;&#7907;ng d&#242;ng ch&#7843;y &#273;&#7875; t&#7841;o ra &#273;i&#7879;n s&#7841;ch, t&#225;i t&#7841;o. C&#225;c d&#7921; &#225;n &#273;&#7853;p &#273;a m&#7909;c &#273;&#237;ch c&#243; th&#7875; k&#7871;t h&#7907;p nhi&#7873;u c&#244;ng n&#259;ng: ph&#225;t &#273;i&#7879;n, ki&#7875;m so&#225;t l&#361; v&#224; c&#7843;i thi&#7879;n giao th&#244;ng th&#7911;y.</p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig135.png" alt="River Danube locks showing hydroelectric infrastructure"/>
<p class="caption">Fig 1.35 &#8212; River Danube locks: a multipurpose scheme providing HEP, flood control, and improved navigation. / H&#7879; th&#7889;ng &#226;u thuy&#7873;n s&#244;ng Danube: d&#7921; &#225;n &#273;a m&#7909;c &#273;&#237;ch t&#7841;o &#273;i&#7879;n, ki&#7875;m so&#225;t l&#361; v&#224; giao th&#244;ng th&#7911;y.</p>

<h3>Tourism, Recreation, and Real Estate</h3>
<p>Scenic river valleys, gorges, waterfalls, and riverside towns attract significant tourist numbers. Riverside and waterfront properties command premium prices in the housing market.</p>
<p class="vi"><strong>Du l&#7883;ch v&#224; b&#7845;t &#273;&#7897;ng s&#7843;n:</strong> M&#244;i tr&#432;&#7901;ng ven s&#244;ng thu h&#250;t du l&#7883;ch, gi&#7843;i tr&#237; v&#224; n&#226;ng cao gi&#225; tr&#7883; nh&#224; &#273;&#7845;t. B&#7845;t &#273;&#7897;ng s&#7843;n ven s&#244;ng c&#243; gi&#225; th&#7883; tr&#432;&#7901;ng cao h&#417;n &#273;&#225;ng k&#7875;.</p>

<!-- ══════════════ SECTION 2: FLOODS ══════════════ -->
<h2>&#9888;&#65039; Section 2: Hazard &#8212; Floods</h2>
<p class="vi"><strong>&#9888;&#65039; M&#7909;c 2: Nguy C&#417; &#8212; L&#361; L&#7909;t</strong></p>

<p><b class="key-term">Flooding</b> occurs when a river's discharge exceeds its channel capacity, causing water to overtop its banks and inundate surrounding land. It is one of the most widespread and damaging natural hazards on Earth.</p>
<p class="vi">L&#361; l&#7909;t l&#224; &#273;&#7863;c t&#237;nh t&#7921; nhi&#234;n c&#7911;a t&#7845;t c&#7843; c&#225;c con s&#244;ng. T&#7847;n su&#7845;t v&#224; c&#432;&#7901;ng &#273;&#7897; l&#361; &#273;ang gia t&#259;ng &#273;&#225;ng k&#7875; t&#7841;i nhi&#7873;u n&#417;i tr&#234;n th&#7871; gi&#7899;i do bi&#7871;n &#273;&#7893;i kh&#237; h&#7853;u.</p>

<h3>Causes of Flooding</h3>
<p class="vi"><strong>Nguy&#234;n nh&#226;n g&#226;y l&#361; l&#7909;t:</strong></p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig136.png" alt="Classification diagram showing natural and human causes of river flooding"/>
<p class="caption">Fig 1.36 &#8212; Classification of flood causes: natural (physical) factors on the left, human factors on the right. / Ph&#226;n lo&#7841;i nguy&#234;n nh&#226;n l&#361;: t&#7921; nhi&#234;n (tr&#225;i) v&#224; con ng&#432;&#7901;i (ph&#7843;i).</p>

<div class="eng-grid">
  <div class="eng-card" style="background:#fef3c7;border-left:4px solid #d97706;">
    <h4>&#127751; Natural Causes</h4>
    <ul>
      <li><strong>Heavy or prolonged rainfall</strong> &#8212; most common cause; saturates soil and overwhelms channels</li>
      <li><strong>Rapid snowmelt</strong> &#8212; spring thaw releases large volumes of water quickly</li>
      <li><strong>Steep relief</strong> &#8212; water runs off hillsides rapidly</li>
      <li><strong>Impermeable rock</strong> &#8212; little water soaks into the ground</li>
      <li><strong>Natural vegetation removal</strong> &#8212; e.g. forest fires reduce interception</li>
    </ul>
    <p class="vi"><strong>Nguy&#234;n nh&#226;n t&#7921; nhi&#234;n:</strong>
    <ul class="vi">
      <li>M&#432;a l&#7899;n ho&#7863;c k&#233;o d&#224;i (ph&#7893; bi&#7871;n nh&#7845;t)</li>
      <li>Tan tuy&#7871;t nhanh</li>
      <li>&#272;&#7883;a h&#236;nh d&#7889;c &#8594; d&#242;ng ch&#7843;y b&#7873; m&#7863;t nhanh</li>
      <li>&#272;&#225; kh&#244;ng th&#7845;m n&#432;&#7899;c &#8594; &#237;t th&#7845;m l&#7885;c</li>
      <li>Ph&#225; r&#7915;ng t&#7921; nhi&#234;n &#8594; gi&#7843;m l&#432;&#7907;ng n&#432;&#7899;c b&#7883; gi&#7919; l&#7841;i</li>
    </ul></p>
  </div>
  <div class="eng-card" style="background:#fee2e2;border-left:4px solid #dc2626;">
    <h4>&#127961;&#65039; Human Causes</h4>
    <ul>
      <li><strong>Urbanisation</strong> &#8212; impermeable surfaces and drains increase runoff speed dramatically</li>
      <li><strong>Deforestation</strong> &#8212; removing trees sharply increases surface runoff</li>
      <li><strong>Floodplain development</strong> &#8212; buildings reduce natural storage capacity</li>
      <li><strong>Climate change</strong> &#8212; increasing intensity of extreme rainfall events</li>
    </ul>
    <p class="vi"><strong>Nguy&#234;n nh&#226;n do con ng&#432;&#7901;i:</strong>
    <ul class="vi">
      <li>&#272;&#244; th&#7883; h&#243;a: b&#7873; m&#7863;t kh&#244;ng th&#7845;m n&#432;&#7899;c + h&#7879; th&#7889;ng c&#7889;ng r&#227;nh &#8594; d&#242;ng ch&#7843;y nhanh h&#417;n</li>
      <li>Ph&#225; r&#7915;ng: gi&#7843;m l&#432;&#7907;ng n&#432;&#7899;c c&#226;y gi&#7919; l&#7841;i</li>
      <li>X&#226;y d&#7921;ng tr&#234;n &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#361;t &#8594; t&#259;ng nguy c&#417; thi&#7879;t h&#7841;i</li>
      <li>Bi&#7871;n &#273;&#7893;i kh&#237; h&#7853;u do con ng&#432;&#7901;i g&#226;y ra &#8594; m&#432;a c&#7921;c &#273;oan h&#417;n</li>
    </ul></p>
  </div>
</div>

<h3>Impacts of Flooding</h3>
<p>Flood impacts are classified by how directly they result from the flood event:</p>
<p class="vi"><strong>&#7842;nh h&#432;&#7903;ng c&#7911;a l&#361; l&#7909;t</strong> &#8212; &#273;&#432;&#7907;c ph&#226;n lo&#7841;i theo m&#7913;c &#273;&#7897; tr&#7921;c ti&#7871;p so v&#7899;i s&#7921; ki&#7879;n l&#361;:</p>

<div class="impacts-grid">
  <div class="impact-card primary">
    <h5>&#128308; Primary (Immediate)</h5>
    <ul>
      <li>Loss of life (drowning)</li>
      <li>Buildings flooded and structurally damaged</li>
      <li>Roads, bridges, railways destroyed</li>
      <li>Crops and livestock lost</li>
    </ul>
    <p class="vi" style="margin-top:8px;font-size:13px;"><strong>S&#417; c&#7845;p:</strong> Thi&#7879;t h&#7841;i v&#7873; ng&#432;&#7901;i, nh&#224; c&#7917;a b&#7883; ng&#7853;p, c&#417; s&#7903; h&#7841; t&#7847;ng (c&#7847;u, &#273;&#432;&#7901;ng, &#273;&#234;) b&#7883; h&#432; h&#7887;ng.</p>
  </div>
  <div class="impact-card secondary">
    <h5>&#128993; Secondary (Short-term)</h5>
    <ul>
      <li>Water supply contaminated</li>
      <li>Disease outbreaks (cholera, typhoid)</li>
      <li>Electricity and gas disrupted</li>
      <li>Business closures; economic loss</li>
    </ul>
    <p class="vi" style="margin-top:8px;font-size:13px;"><strong>Th&#7913; c&#7845;p:</strong> &#212; nhi&#7877;m ngu&#7891;n n&#432;&#7899;c sinh ho&#7841;t, d&#7883;ch b&#7879;nh l&#226;y lan, m&#7845;t &#273;i&#7879;n v&#224; c&#225;c d&#7883;ch v&#7909; n&#259;ng l&#432;&#7907;ng.</p>
  </div>
  <div class="impact-card tertiary">
    <h5>&#128309; Tertiary (Long-term)</h5>
    <ul>
      <li>Farmland abandoned due to silt and damage</li>
      <li>Insurance costs rise; devalued land</li>
      <li>Habitat destruction and ecosystem loss</li>
      <li>Psychological trauma in communities</li>
    </ul>
    <p class="vi" style="margin-top:8px;font-size:13px;"><strong>L&#226;u d&#224;i:</strong> H&#7911;y ho&#7841;i sinh c&#7843;nh t&#7921; nhi&#234;n, &#273;&#7845;t n&#244;ng nghi&#7879;p b&#7883; b&#7887; hoang, chi ph&#237; b&#7843;o hi&#7875;m t&#259;ng cao.</p>
  </div>
</div>

<div class="info-box orange">
  <strong>Exam tip &#8212; Primary vs Secondary impacts:</strong> Primary impacts are <em>directly</em> caused by the flood water. Secondary impacts are <em>indirect</em> consequences triggered by the primary impacts. Tertiary impacts are long-term effects that persist after the water recedes.
  <p class="vi" style="margin-bottom:0;"><strong>M&#7865;o thi:</strong> T&#225;c &#273;&#7897;ng s&#417; c&#7845;p l&#224; h&#7853;u qu&#7843; <em>tr&#7921;c ti&#7871;p</em> c&#7911;a l&#361; l&#7909;t. T&#225;c &#273;&#7897;ng th&#7913; c&#7845;p l&#224; h&#7879; qu&#7843; <em>gi&#225;n ti&#7871;p</em>. T&#225;c &#273;&#7897;ng l&#226;u d&#224;i l&#224; nh&#7919;ng &#7843;nh h&#432;&#7903;ng t&#7891;n t&#7841;i sau khi n&#432;&#7899;c r&#250;t.</p>
</div>

<!-- ══════════════ SECTION 3: MANAGEMENT ══════════════ -->
<h2>&#128295;&#65039; Section 3: Flood Management</h2>
<p class="vi"><strong>&#128295;&#65039; M&#7909;c 3: Qu&#7843;n L&#253; L&#361; L&#7909;t</strong></p>

<p>Flood management strategies aim to reduce the frequency, severity, or impact of flooding. They are broadly divided into <b class="key-term">hard engineering</b> and <b class="key-term">soft engineering</b> approaches.</p>
<p class="vi">Chi&#7871;n l&#432;&#7907;c qu&#7843;n l&#253; l&#361; l&#7909;t nh&#7857;m gi&#7843;m t&#7847;n su&#7845;t, m&#7913;c &#273;&#7897; nghi&#234;m tr&#7885;ng ho&#7863;c t&#225;c &#273;&#7897;ng c&#7911;a l&#361;. &#272;&#432;&#7907;c chia th&#224;nh hai nh&#243;m ch&#237;nh: <strong>c&#244;ng tr&#236;nh c&#7913;ng</strong> v&#224; <strong>c&#244;ng tr&#236;nh m&#7873;m</strong>.</p>

<h3>Hard Engineering (Traditional / Structural)</h3>
<p>Hard engineering uses large physical structures to control river flow. It is often effective in the short term but expensive and can create problems downstream.</p>
<p class="vi"><strong>C&#244;ng tr&#236;nh c&#7913;ng (Hard Engineering):</strong> S&#7917; d&#7909;ng c&#225;c c&#244;ng tr&#236;nh v&#7853;t l&#253; l&#7899;n &#273;&#7875; ki&#7875;m so&#225;t d&#242;ng ch&#7843;y. Hi&#7879;u qu&#7843; trong ng&#7855;n h&#7841;n nh&#432;ng chi ph&#237; cao v&#224; c&#243; th&#7875; g&#226;y ra v&#7845;n &#273;&#7873; &#7903; h&#7841; l&#432;u.</p>

<div class="eng-grid">
  <div class="eng-card hard">
    <h4>&#127959;&#65039; Hard Engineering Methods</h4>
    <ul>
      <li><strong>Dams &amp; reservoirs</strong> &#8212; store excess water upstream; control release of flow</li>
      <li><strong>Lev&#233;es (embankments)</strong> &#8212; raised earth or concrete walls along riverbanks</li>
      <li><strong>Channelisation</strong> &#8212; straightening, deepening, or lining the river channel</li>
      <li><strong>Flood barriers</strong> &#8212; e.g. Thames Barrier, London</li>
      <li><strong>Flood walls</strong> &#8212; permanent concrete walls in urban areas</li>
    </ul>
    <p class="vi"><strong>Ph&#432;&#417;ng ph&#225;p c&#244;ng tr&#236;nh c&#7913;ng:</strong>
    <ul class="vi">
      <li>&#272;&#7853;p v&#224; h&#7891; ch&#7913;a: tr&#7919; n&#432;&#7899;c, &#273;i&#7873;u ti&#7871;t l&#432;u l&#432;&#7907;ng</li>
      <li>&#272;&#234; ch&#7855;n l&#361;: n&#226;ng cao b&#7901; s&#244;ng &#273;&#7875; t&#259;ng dung t&#237;ch k&#234;nh</li>
      <li>N&#7855;n th&#7859;ng l&#242;ng s&#244;ng: t&#259;ng t&#7889;c &#273;&#7897; tho&#225;t n&#432;&#7899;c</li>
      <li>R&#224;o ch&#7855;n l&#361;: v&#237; d&#7909; Thames Barrier (London)</li>
      <li>T&#432;&#7901;ng b&#234; t&#244;ng ch&#7889;ng l&#361; &#7903; &#273;&#244; th&#7883;</li>
    </ul></p>
  </div>
  <div class="eng-card hard" style="background:#fef2f2;border-left:4px solid #b91c1c;">
    <h4>&#9888;&#65039; Disadvantages</h4>
    <ul>
      <li>Very expensive to build and maintain</li>
      <li>Channelisation increases flood risk downstream</li>
      <li>Dams trap sediment, reducing downstream fertility</li>
      <li>Can give communities a false sense of security</li>
      <li>Disrupts river ecosystems</li>
    </ul>
    <p class="vi"><strong>Nh&#432;&#7907;c &#273;i&#7875;m:</strong>
    <ul class="vi">
      <li>Chi ph&#237; x&#226;y d&#7921;ng v&#224; b&#7843;o tr&#236; r&#7845;t cao</li>
      <li>N&#7855;n th&#7859;ng l&#242;ng s&#244;ng t&#259;ng nguy c&#417; l&#361; &#7903; h&#7841; l&#432;u</li>
      <li>&#272;&#7853;p gi&#7919; l&#7841;i ph&#249; sa, gi&#7843;m &#273;&#7897; ph&#236; nhi&#234;u h&#7841; l&#432;u</li>
      <li>C&#243; th&#7875; g&#226;y t&#226;m l&#253; ch&#7911; quan cho c&#7897;ng &#273;&#7891;ng</li>
    </ul></p>
  </div>
</div>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig138.png" alt="Hard engineering flood defences including Thames Barrier and Zermatt levees"/>
<p class="caption">Fig 1.38 &#8212; Hard engineering: the Thames Barrier (London) and reinforced lev&#233;es at Zermatt, Switzerland. / C&#244;ng tr&#236;nh c&#7913;ng: Thames Barrier (London) v&#224; &#273;&#234; gia c&#7889; t&#7841;i Zermatt, Th&#7909;y S&#297;.</p>

<h3>Soft Engineering (Sustainable / Nature-Based)</h3>
<p>Soft engineering works <em>with</em> natural river processes rather than against them. It is generally cheaper, more sustainable, and better for biodiversity.</p>
<p class="vi"><strong>C&#244;ng tr&#236;nh m&#7873;m (Soft Engineering):</strong> L&#224;m vi&#7879;c <em>c&#249;ng</em> v&#7899;i c&#225;c qu&#225; tr&#236;nh t&#7921; nhi&#234;n c&#7911;a s&#244;ng. Th&#432;&#7901;ng r&#7867; h&#417;n, b&#7873;n v&#7919;ng h&#417;n v&#224; t&#7889;t h&#417;n cho &#273;a d&#7841;ng sinh h&#7885;c.</p>

<div class="eng-grid">
  <div class="eng-card soft">
    <h4>&#127807; Soft Engineering Methods</h4>
    <ul>
      <li><strong>Flood warning systems</strong> &#8212; real-time monitoring and alerts to evacuate</li>
      <li><strong>Floodplain zoning</strong> &#8212; restrict new development in high-risk zones</li>
      <li><strong>Flood abatement</strong> &#8212; reforestation, contour ploughing, wetland restoration</li>
      <li><strong>Flood diversion</strong> &#8212; controlled release of floodwater into washlands</li>
      <li><strong>River restoration</strong> &#8212; re-meandering channels to slow flow</li>
    </ul>
    <p class="vi"><strong>Ph&#432;&#417;ng ph&#225;p c&#244;ng tr&#236;nh m&#7873;m:</strong>
    <ul class="vi">
      <li>H&#7879; th&#7889;ng c&#7843;nh b&#225;o l&#361; s&#7899;m</li>
      <li>Quy ho&#7841;ch v&#249;ng &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#361;t: h&#7841;n ch&#7871; x&#226;y d&#7921;ng</li>
      <li>Gi&#7843;m thi&#7875;u l&#361;: t&#225;i tr&#7891;ng r&#7915;ng, canh t&#225;c theo &#273;&#432;&#7901;ng &#273;&#7891;ng m&#7913;c, ph&#7909;c h&#7891;i &#273;&#7845;t ng&#7853;p n&#432;&#7899;c</li>
      <li>Chuy&#7875;n h&#432;&#7899;ng l&#361;: cho ph&#233;p ng&#7853;p c&#243; ki&#7875;m so&#225;t &#7903; m&#7897;t s&#7889; v&#249;ng</li>
    </ul></p>
  </div>
  <div class="eng-card soft" style="background:#f0fdf4;border-left:4px solid #16a34a;">
    <h4>&#10003; Advantages</h4>
    <ul>
      <li>Lower cost over long term</li>
      <li>Sustainable &#8212; improves ecosystem health</li>
      <li>Addresses root causes (e.g. reducing runoff)</li>
      <li>Works with natural processes</li>
      <li>Can enhance biodiversity and recreation</li>
    </ul>
    <p class="vi"><strong>&#431;u &#273;i&#7875;m:</strong>
    <ul class="vi">
      <li>Chi ph&#237; th&#7845;p h&#417;n v&#233; d&#224;i h&#7841;n</li>
      <li>B&#7873;n v&#7919;ng &#8212; c&#7843;i thi&#7879;n s&#7913;c kh&#7887;e h&#7879; sinh th&#225;i</li>
      <li>Gi&#7843;i quy&#7871;t nguy&#234;n nh&#226;n g&#7889;c r&#7877;</li>
      <li>H&#7895; tr&#7907; &#273;a d&#7841;ng sinh h&#7885;c v&#224; du l&#7883;ch sinh th&#225;i</li>
    </ul></p>
  </div>
</div>

<h3>Sustainable Drainage Systems (SuDS)</h3>
<p><b class="key-term">Sustainable Drainage Systems (SuDS)</b> are urban engineering solutions that mimic natural drainage processes to reduce surface runoff. Rather than channelling rainwater quickly into drains, SuDS slow, store, and naturally filter water.</p>
<p class="vi"><strong>H&#7879; th&#7889;ng tho&#225;t n&#432;&#7899;c b&#7873;n v&#7919;ng (SuDS):</strong> Ph&#432;&#417;ng ph&#225;p tho&#225;t n&#432;&#7899;c t&#7921; nhi&#234;n thay th&#7871; cho h&#7879; th&#7889;ng c&#7889;ng r&#227;nh truy&#7873;n th&#7889;ng. M&#7909;c ti&#234;u: gi&#7843;m t&#7889;c &#273;&#7897; d&#242;ng ch&#7843;y, t&#259;ng tr&#7919; n&#432;&#7899;c b&#7873; m&#7863;t v&#224; c&#7843;i thi&#7879;n ch&#7845;t l&#432;&#7907;ng n&#432;&#7899;c.</p>

<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_3_fig140.png" alt="Diagram illustrating Sustainable Drainage Systems (SuDS) components in an urban area"/>
<p class="caption">Fig 1.40 &#8212; Sustainable Drainage Systems (SuDS): a suite of measures that reduce urban runoff and improve water quality. / H&#7879; th&#7889;ng SuDS: t&#7893;ng th&#7875; c&#225;c bi&#7879;n ph&#225;p gi&#7843;m d&#242;ng ch&#7843;y &#273;&#244; th&#7883; v&#224; c&#7843;i thi&#7879;n ch&#7845;t l&#432;&#7907;ng n&#432;&#7899;c.</p>

<div class="info-box blue">
  <strong>Key SuDS methods:</strong>
  <ul>
    <li>&#127793; <strong>Green roofs</strong> &#8212; living vegetation on rooftops absorbs rainwater and reduces runoff</li>
    <li>&#127754; <strong>Swales</strong> &#8212; shallow, vegetated channels that slow and filter surface runoff</li>
    <li>&#128298; <strong>Infiltration basins</strong> &#8212; shallow depressions that allow water to percolate into the ground</li>
    <li>&#129521; <strong>Permeable surfaces</strong> &#8212; paving that allows water to pass through into the soil</li>
    <li>&#127964;&#65039; <strong>Retention ponds</strong> &#8212; store stormwater temporarily and release it slowly</li>
    <li>&#127959;&#65039; <strong>Underground storage tanks</strong> &#8212; store rainwater for later use</li>
  </ul>
  <p class="vi" style="margin-bottom:0;"><strong>C&#225;c ph&#432;&#417;ng ph&#225;p SuDS ch&#237;nh:</strong>
  <ul class="vi">
    <li>M&#225;i nh&#224; xanh (green roofs): th&#7921;c v&#7853;t tr&#234;n m&#225;i h&#7845;p th&#7909; n&#432;&#7899;c m&#432;a</li>
    <li>R&#227;nh th&#7921;c v&#7853;t (swales): l&#224;m ch&#7853;m v&#224; l&#7885;c d&#242;ng ch&#7843;y b&#7873; m&#7863;t</li>
    <li>B&#7875; th&#7845;m (infiltration basins): cho ph&#233;p n&#432;&#7899;c th&#7845;m xu&#7889;ng &#273;&#7845;t</li>
    <li>B&#7873; m&#7863;t th&#7845;m n&#432;&#7899;c (permeable paving): l&#7899;p nh&#7921;a &#273;&#432;&#7901;ng cho ph&#233;p n&#432;&#7899;c th&#7845;m qua</li>
    <li>Ao gi&#7919; n&#432;&#7899;c (retention ponds): tr&#7919; n&#432;&#7899;c t&#7841;m th&#7901;i, th&#7843;i ra t&#7915; t&#7915;</li>
    <li>R&#227;nh l&#7885;c v&#224; b&#7875; ng&#7847;m: tr&#7919; n&#432;&#7899;c m&#432;a &#273;&#7875; t&#225;i s&#7917; d&#7909;ng</li>
  </ul></p>
</div>

<!-- ══════════════ KEY TERMS ══════════════ -->
<h2>&#128218; Key Terms Summary</h2>
<p class="vi"><strong>T&#7893;ng h&#7907;p thu&#7853;t ng&#7919; ch&#237;nh</strong></p>

<div class="terms-grid">
  <div class="term-card"><strong>Alluvium <span class="vi-term">(Ph&#249; sa)</span></strong>Fine, nutrient-rich sediment deposited by a river on its floodplain during flood events.</div>
  <div class="term-card"><strong>Floodplain <span class="vi-term">(&#272;&#7891;ng b&#7857;ng ng&#7853;p l&#361;t)</span></strong>The flat land either side of a river channel, formed by alluvial deposits, prone to flooding.</div>
  <div class="term-card"><strong>Hydroelectric Power &#8212; HEP <span class="vi-term">(Thu&#7927; &#273;i&#7879;n)</span></strong>Electricity generated by harnessing the energy of flowing or falling water via a turbine.</div>
  <div class="term-card"><strong>Multipurpose river scheme <span class="vi-term">(D&#7921; &#225;n s&#244;ng &#273;a m&#7909;c &#273;&#237;ch)</span></strong>A dam/reservoir project serving multiple purposes: HEP, water supply, flood control, navigation.</div>
  <div class="term-card"><strong>Flooding <span class="vi-term">(L&#361; l&#7909;t)</span></strong>When river discharge exceeds channel capacity, water overtops banks and inundates land.</div>
  <div class="term-card"><strong>Hard engineering <span class="vi-term">(C&#244;ng tr&#236;nh c&#7913;ng)</span></strong>Large-scale physical structures (dams, lev&#233;es, barriers) used to control river flow.</div>
  <div class="term-card"><strong>Soft engineering <span class="vi-term">(C&#244;ng tr&#236;nh m&#7873;m)</span></strong>Nature-based or planning approaches (zoning, afforestation, SuDS) to manage flood risk sustainably.</div>
  <div class="term-card"><strong>SuDS <span class="vi-term">(H&#7879; th&#7889;ng tho&#225;t n&#432;&#7899;c b&#7873;n v&#7919;ng)</span></strong>Sustainable Drainage Systems &#8212; urban measures that mimic natural drainage to reduce runoff.</div>
  <div class="term-card"><strong>Lev&#233;e <span class="vi-term">(&#272;&#234; ch&#7855;n l&#361;)</span></strong>An embankment (natural or artificial) built along a riverbank to prevent flooding.</div>
  <div class="term-card"><strong>Channelisation <span class="vi-term">(N&#7855;n th&#7859;ng l&#242;ng s&#244;ng)</span></strong>Engineering a river to flow faster by straightening, deepening, or lining its channel.</div>
  <div class="term-card"><strong>Floodplain zoning <span class="vi-term">(Quy ho&#7841;ch v&#249;ng ng&#7853;p l&#361;t)</span></strong>Land-use planning that restricts building in flood-prone areas to reduce future flood risk.</div>
  <div class="term-card"><strong>Urbanisation <span class="vi-term">(&#272;&#244; th&#7883; h&#243;a)</span></strong>The growth of towns and cities; increases impermeable surfaces, speeding up runoff into rivers.</div>
</div>

<div class="info-box purple">
  <strong>&#128221; Exam focus for this topic:</strong>
  <ul>
    <li>Be able to explain <em>why</em> rivers attract settlement &#8212; give specific named examples</li>
    <li>Distinguish between natural and human causes of flooding</li>
    <li>Compare hard and soft engineering &#8212; advantages, disadvantages, and specific examples</li>
    <li>Explain how SuDS work and why they are considered more sustainable</li>
    <li>Use the terms <em>primary, secondary</em> and <em>tertiary</em> correctly when describing flood impacts</li>
  </ul>
  <p class="vi" style="margin-bottom:0;"><strong>&#10084; T&#7853;p trung &#244;n thi:</strong>
  <ul class="vi">
    <li>Gi&#7843;i th&#237;ch <em>t&#7841;i sao</em> s&#244;ng thu h&#250;t d&#226;n c&#432; &#8212; d&#7851;n ch&#7913;ng c&#7909; th&#7875;</li>
    <li>Ph&#226;n bi&#7879;t nguy&#234;n nh&#226;n t&#7921; nhi&#234;n v&#224; con ng&#432;&#7901;i g&#226;y l&#361; l&#7909;t</li>
    <li>So s&#225;nh c&#244;ng tr&#236;nh c&#7913;ng v&#224; m&#7873;m &#8212; &#432;u nh&#432;&#7907;c &#273;i&#7875;m, v&#237; d&#7909; c&#7909; th&#7875;</li>
    <li>Gi&#7843;i th&#237;ch c&#225;ch SuDS ho&#7841;t &#273;&#7897;ng v&#224; t&#7841;i sao b&#7873;n v&#7919;ng h&#417;n</li>
    <li>D&#249;ng &#273;&#250;ng thu&#7853;t ng&#7919; <em>s&#417; c&#7845;p, th&#7913; c&#7845;p, l&#226;u d&#224;i</em> khi m&#244; t&#7843; t&#225;c &#273;&#7897;ng l&#361;</li>
  </ul></p>
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
    print("SUCCESS: Lecture 1.3 Page 2 (bilingual) uploaded successfully!")
else:
    print(f"ERROR response: {repr(response.text)}")
