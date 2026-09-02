import requests
import json

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
PAGE_ID = "4dfe49c5-2756-4ee4-8db3-615131e39e0b"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>1.2 River Landforms / C\u00e1c D\u1ea1ng \u0110\u1ecba H\u00ecnh S\u00f4ng</title>
<style>
  body{font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;padding:20px;}
  h1{color:#1e3a8a;font-size:32px;border-bottom:3px solid #60a5fa;display:inline-block;padding-bottom:10px;}
  h2{color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:10px;font-size:24px;margin-top:40px;}
  h3{color:#1e3a8a;font-size:19px;}
  img{max-width:420px;height:auto;display:block;margin:0 auto;}
  .caption{font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;}
  .info-box{background:#f1f5f9;padding:15px;border-radius:8px;margin:20px 0;}
  .subtitle{color:#64748b;font-size:17px;margin-top:4px;margin-bottom:30px;}
  .vi{color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;}

  /* SVG long profile */
  #long-profile-wrap{position:relative;margin:30px 0;}
  .lp-btn{cursor:pointer;transition:opacity .2s;}
  .lp-btn:hover .lp-dot{filter:brightness(1.3);}
  #def-panel{display:none;background:#1e3a8a;color:#fff;border-radius:10px;padding:18px 22px;margin-top:14px;}
  #def-panel h4{margin:0 0 6px 0;font-size:17px;color:#93c5fd;}
  #def-panel p{margin:0 0 8px 0;font-size:15px;line-height:1.5;}
  #def-panel p.vi-def{color:#bae6fd;font-style:italic;font-size:14px;border-left:2px solid #60a5fa;padding-left:10px;margin:6px 0 0 0;}

  /* Summary table */
  table{width:100%;border-collapse:collapse;margin-top:16px;font-size:15px;}
  th{background:#1e3a8a;color:#fff;padding:10px 14px;text-align:left;}
  td{padding:9px 14px;border-bottom:1px solid #e2e8f0;}
  tr:nth-child(even) td{background:#f8fafc;}
</style>
</head>
<body>

<h1>&#127956;&#65039; 1.2 River Landforms</h1>
<h1 style="font-size:24px;border-bottom:none;color:#7c3aed;padding-bottom:0;">C\u00e1c D\u1ea1ng \u0110\u1ecba H\u00ecnh S\u00f4ng</h1>
<p class="subtitle">How rivers shape the landscape from source to mouth</p>
<p class="vi">S\u00f4ng h\u00ecnh th\u00e0nh \u0111\u1ecba h\u00ecnh t\u1eeb th\u01b0\u1ee3ng l\u01b0u \u0111\u1ebfn h\u1ea1 l\u01b0u nh\u01b0 th\u1ebf n\u00e0o</p>

<!-- ============= INTERACTIVE LONG PROFILE ============= -->
<h2>&#128506;&#65039; Interactive Long Profile / S\u01a1 \u0110\u1ed3 D\u1ecdc S\u00f4ng T\u01b0\u01a1ng T\u00e1c</h2>
<p>Click any landform marker on the diagram to see its definition.</p>
<p class="vi">Nh\u1ea5p v\u00e0o b\u1ea5t k\u1ef3 \u0111i\u1ec3m n\u00e0o tr\u00ean s\u01a1 \u0111\u1ed3 \u0111\u1ec3 xem \u0111\u1ecbnh ngh\u0129a c\u1ee7a d\u1ea1ng \u0111\u1ecba h\u00ecnh \u0111\u00f3.</p>

<div id="long-profile-wrap">
<svg viewBox="0 0 860 320" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:10px;background:#f0f9ff;border:1px solid #bae6fd;">
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
  <rect width="860" height="320" fill="url(#skyGrad)" rx="10"/>
  <polygon points="0,300 0,80 80,60 160,100 240,130 320,155 420,175 520,205 620,230 720,255 860,270 860,300"
           fill="url(#landGrad)" opacity="0.55"/>
  <polyline points="0,82 80,62 160,102 240,132 320,157 420,177 520,207 620,232 720,257 860,272"
            fill="none" stroke="url(#riverGrad)" stroke-width="5" stroke-linecap="round"/>
  <!-- Zone labels -->
  <rect x="10" y="8" width="220" height="26" rx="5" fill="#1e3a8a" opacity="0.15"/>
  <text x="120" y="26" text-anchor="middle" font-size="13" fill="#1e3a8a" font-weight="bold">UPPER COURSE / TH&#431;&#906;NG L&#431;U</text>
  <rect x="310" y="8" width="220" height="26" rx="5" fill="#7c3aed" opacity="0.12"/>
  <text x="420" y="26" text-anchor="middle" font-size="13" fill="#7c3aed" font-weight="bold">MIDDLE COURSE / TRUNG L&#431;U</text>
  <rect x="610" y="8" width="240" height="26" rx="5" fill="#0369a1" opacity="0.12"/>
  <text x="730" y="26" text-anchor="middle" font-size="13" fill="#0369a1" font-weight="bold">LOWER COURSE / H&#7840; L&#431;U</text>
  <line x1="310" y1="8" x2="310" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/>
  <line x1="610" y1="8" x2="610" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/>

  <!-- 1. V-shaped Valley -->
  <g class="lp-btn" onclick="showDef('vshaped')" style="cursor:pointer;">
    <circle class="lp-dot" cx="80" cy="62" r="9" fill="#dc2626"/>
    <line x1="80" y1="71" x2="80" y2="105" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="22" y="105" width="116" height="20" rx="4" fill="#dc2626" opacity="0.85"/>
    <text x="80" y="119" text-anchor="middle" font-size="11" fill="white" font-weight="bold">V-shaped Valley</text>
  </g>
  <!-- 2. Interlocking Spurs -->
  <g class="lp-btn" onclick="showDef('spurs')" style="cursor:pointer;">
    <circle class="lp-dot" cx="165" cy="100" r="9" fill="#ea580c"/>
    <line x1="165" y1="109" x2="165" y2="140" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="107" y="140" width="116" height="20" rx="4" fill="#ea580c" opacity="0.85"/>
    <text x="165" y="154" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Interlocking Spurs</text>
  </g>
  <!-- 3. Pothole -->
  <g class="lp-btn" onclick="showDef('pothole')" style="cursor:pointer;">
    <circle class="lp-dot" cx="237" cy="131" r="9" fill="#b45309"/>
    <line x1="237" y1="140" x2="237" y2="170" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="183" y="170" width="108" height="20" rx="4" fill="#b45309" opacity="0.85"/>
    <text x="237" y="184" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Pothole</text>
  </g>
  <!-- 4. Waterfall & Gorge -->
  <g class="lp-btn" onclick="showDef('waterfall')" style="cursor:pointer;">
    <circle class="lp-dot" cx="285" cy="147" r="9" fill="#7c3aed"/>
    <line x1="285" y1="156" x2="285" y2="200" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="215" y="200" width="140" height="20" rx="4" fill="#7c3aed" opacity="0.85"/>
    <text x="285" y="214" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Waterfall &amp; Gorge</text>
  </g>
  <!-- 5. Meander -->
  <g class="lp-btn" onclick="showDef('meander')" style="cursor:pointer;">
    <circle class="lp-dot" cx="420" cy="177" r="9" fill="#0891b2"/>
    <line x1="420" y1="186" x2="420" y2="220" stroke="#0891b2" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="370" y="220" width="100" height="20" rx="4" fill="#0891b2" opacity="0.85"/>
    <text x="420" y="234" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Meander</text>
  </g>
  <!-- 6. Oxbow Lake -->
  <g class="lp-btn" onclick="showDef('oxbow')" style="cursor:pointer;">
    <circle class="lp-dot" cx="532" cy="207" r="9" fill="#0f766e"/>
    <line x1="532" y1="216" x2="532" y2="250" stroke="#0f766e" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="474" y="250" width="116" height="20" rx="4" fill="#0f766e" opacity="0.85"/>
    <text x="532" y="264" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Oxbow Lake</text>
  </g>
  <!-- 7. Floodplain & Levee -->
  <g class="lp-btn" onclick="showDef('floodplain')" style="cursor:pointer;">
    <circle class="lp-dot" cx="650" cy="232" r="9" fill="#1d4ed8"/>
    <line x1="650" y1="241" x2="650" y2="182" stroke="#1d4ed8" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="580" y="162" width="140" height="20" rx="4" fill="#1d4ed8" opacity="0.85"/>
    <text x="650" y="176" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Floodplain &amp; Lev\u00e9e</text>
  </g>
  <!-- 8. Braided Channel -->
  <g class="lp-btn" onclick="showDef('braided')" style="cursor:pointer;">
    <circle class="lp-dot" cx="742" cy="257" r="9" fill="#b45309"/>
    <line x1="742" y1="266" x2="742" y2="210" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="672" y="190" width="140" height="20" rx="4" fill="#b45309" opacity="0.85"/>
    <text x="742" y="204" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Braided Channel</text>
  </g>
  <!-- 9. Delta -->
  <g class="lp-btn" onclick="showDef('delta')" style="cursor:pointer;">
    <circle class="lp-dot" cx="835" cy="271" r="9" fill="#065f46"/>
    <line x1="835" y1="262" x2="835" y2="140" stroke="#065f46" stroke-width="1.5" stroke-dasharray="3,2"/>
    <rect x="785" y="120" width="70" height="20" rx="4" fill="#065f46" opacity="0.85"/>
    <text x="820" y="134" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Delta</text>
  </g>
  <text x="12" y="300" font-size="12" fill="#475569" font-style="italic">Source &#9650;</text>
  <text x="800" y="300" font-size="12" fill="#475569" font-style="italic">&#9660; Mouth / Sea</text>
</svg>

<div id="def-panel">
  <h4 id="def-title"></h4>
  <p id="def-body"></p>
  <p id="def-vi" class="vi-def"></p>
</div>
</div>

<script>
const DEFS = {
  vshaped: {
    title: "V-shaped Valley / Thung L\u0169ng H\u00ecnh Ch\u1eef V",
    body: "Formed in the upper course where vertical erosion dominates. The river cuts downward through the rock, creating a steep-sided V-shaped valley. Gravity causes the valley walls to collapse and weather, adding debris to the river.",
    vi: "\u0110\u01b0\u1ee3c h\u00ecnh th\u00e0nh \u1edf th\u01b0\u1ee3ng l\u01b0u, n\u01a1i x\u00f3i m\u00f2n th\u1eb3ng \u0111\u1ee9ng chi ph\u1ed1i. S\u00f4ng c\u1eaft s\u00e2u xu\u1ed1ng, t\u1ea1o ra th\u00f9ng l\u0169ng h\u00ecnh ch\u1eef V d\u1ed1c \u0111\u1ee9ng."
  },
  spurs: {
    title: "Interlocking Spurs / M\u1ecfm \u0110\u1ecba H\u00ecnh Xen K\u1ebd",
    body: "Ridges of hard rock that jut out alternately from each side of the valley. The river lacks the energy to cut through them and instead winds around them, creating an interlocking pattern.",
    vi: "C\u00e1c d\u00e3y \u0111\u00e1 c\u1ee9ng nh\u00f4 ra xen k\u1ebd t\u1eeb hai b\u00ean th\u00f9ng l\u0169ng. S\u00f4ng kh\u00f4ng \u0111\u1ee7 n\u0103ng l\u01b0\u1ee3ng \u0111\u1ec3 c\u1eaft qua, n\u00ean u\u1ed1n l\u01b0\u1ee3n quanh ch\u00fang t\u1ea1o ra d\u1ea1ng m\u1ecfm xen k\u1ebd \u0111\u1eb7c tr\u01b0ng."
  },
  pothole: {
    title: "Pothole / H\u1ed1 B\u00e0o M\u00f2n",
    body: "A circular hole drilled into the riverbed. Pebbles are caught in small hollows and swirled around by turbulent water, grinding the rock beneath into a smooth, cylindrical pit.",
    vi: "\u0110\u00e1 cu\u1ed9i b\u1ecb gi\u1eef l\u1ea1i trong c\u00e1c h\u1ed1c t\u1ea1i \u0111\u00e1y s\u00f4ng. D\u00f2ng ch\u1ea3y xo\u00e1y m\u1ea1nh quay ch\u00fang, kho\u00e9t th\u00e0nh c\u00e1c h\u1ed1 tr\u00f2n nh\u1eb5n g\u1ecdi l\u00e0 h\u1ed1 b\u00e0o m\u00f2n do ma s\u00e1t."
  },
  waterfall: {
    title: "Waterfall & Gorge / Th\u00e1c N\u01b0\u1edbc & H\u1ebb M\u00fai",
    body: "Formed where a band of hard rock overlies softer rock. The softer rock erodes faster, undercutting the hard cap to form an overhang and plunge pool. When the overhang collapses the waterfall retreats upstream leaving a gorge. Example: Niagara Falls.",
    vi: "Th\u00e1c n\u01b0\u1edbc h\u00ecnh th\u00e0nh n\u01a1i \u0111\u00e1 c\u1ee9ng n\u1eb1m tr\u00ean \u0111\u00e1 m\u1ec1m. \u0110\u00e1 m\u1ec1m b\u1ecb xo\u00e1i nhanh h\u01a1n \u2192 t\u1ea1o v\u00e1ch th\u00f2ng v\u00e0 h\u1ed1 xo\u00e1i \u2192 m\u00e1i \u0111\u00e1 s\u1ee5p \u2192 th\u00e1c l\u00f9i d\u1ea7n \u2192 h\u1ebb n\u00fai. V\u00ed d\u1ee5: Th\u00e1c Niagara."
  },
  meander: {
    title: "Meander / Kh\u00fac Cong S\u00f4ng",
    body: "The fastest flow swings to the outside bend, eroding a river cliff. On the inside bend, slow flow deposits a slip-off slope (point bar). The bends migrate and grow over time.",
    vi: "D\u00f2ng ch\u1ea3y nhanh nh\u1ea5t t\u1eadp trung \u1edf b\u1edd ngo\u00e0i \u2192 x\u00f3i m\u00f2n \u2192 v\u00e1ch s\u00f4ng. D\u00f2ng ch\u1ea3y ch\u1eadm h\u01a1n \u1edf b\u1edd trong \u2192 b\u1ed3i \u0111\u1eafp \u2192 s\u01b0\u1eddn tr\u01b0\u1ee3t. Kh\u00fac cong ng\u00e0y c\u00e0ng m\u1edf r\u1ed9ng v\u00e0 di chuy\u1ec3n."
  },
  oxbow: {
    title: "Oxbow Lake / H\u1ed3 M\u00f3ng Ng\u1ef1a",
    body: "The neck of a tight meander is cut through during a flood, and the river takes the shorter straight path. Deposition seals off the old loop, leaving a curved oxbow lake which slowly silts up.",
    vi: "Khi c\u1ed5 c\u1ee7a kh\u00fac cong ng\u00e0y c\u00e0ng h\u1eb9p, trong l\u0169 s\u00f4ng c\u1eaft th\u1eb3ng qua \u2192 \u0111o\u1ea1n s\u00f4ng c\u0169 b\u1ecb c\u00f4 l\u1eadp \u2192 h\u00ecnh th\u00e0nh h\u1ed3 m\u00f3ng ng\u1ef1a. H\u1ed3 d\u1ea7n b\u1ecb b\u1ed3i l\u1eafp."
  },
  floodplain: {
    title: "Floodplain & Lev\u00e9e / \u0110\u1ed3ng B\u1eb1ng Ng\u1eadp L\u1ee5t & \u0110\u00ea T\u1ef1 Nhi\u00ean",
    body: "The wide, flat valley floor built up by alluvium deposited during repeated floods. The coarsest sediment settles first, nearest the channel, building raised natural lev\u00e9es on both banks.",
    vi: "Khi s\u00f4ng tr\u00e0n b\u1edd, ph\u00f9 sa b\u1ed3i \u0111\u1eafp tr\u00ean \u0111\u1ed3ng b\u1eb1ng ph\u1eb3ng \u2192 \u0111\u1ed3ng b\u1eb1ng ng\u1eadp l\u1ee5t. V\u1eadt li\u1ec7u th\u00f4 nh\u1ea5t \u0111\u1ecdc l\u1ea1i ven b\u1edd k\u00eanh, x\u00e2y d\u1ef1ng n\u00ean c\u00e1c \u0111\u00ea t\u1ef1 nhi\u00ean."
  },
  braided: {
    title: "Braided Channel / K\u00eanh Ph\u00e2n L\u01b0u \u0110an Xen",
    body: "When a river carries more sediment than it can transport, it deposits mid-channel bars that split the flow into a network of interwoven channels. Common near glaciers and in semi-arid areas.",
    vi: "Khi s\u00f4ng mang t\u1ea3i l\u01b0\u1ee3ng ph\u00f9 sa r\u1ea5t l\u1edbn, n\u00f3 ph\u00e2n th\u00e0nh nhi\u1ec1u k\u00eanh nh\u1ecf ng\u0103n c\u00e1ch b\u1edfi c\u00e1c b\u00e3i b\u1ed3i. Th\u01b0\u1eddng g\u1eb7p \u1edf s\u00f4ng b\u0103ng tan v\u00e0 m\u00f4i tr\u01b0\u1eddng b\u00e1n kh\u00f4."
  },
  delta: {
    title: "Delta / \u0110\u1ed3ng B\u1eb1ng Ch\u00e2u Th\u1ed5",
    body: "Where a river meets a calm sea or lake, velocity drops to zero and all sediment is deposited. The river splits into a fan of distributaries across the growing deposit. Example: Rh\u00f4ne Delta, France.",
    vi: "Khi s\u00f4ng \u0111\u1ed5 v\u00e0o bi\u1ec3n ho\u1eb7c h\u1ed3 y\u00ean t\u0129nh, v\u1eadn t\u1ed1c gi\u1ea3m \u0111\u1ed9t ng\u1ed9t \u2192 to\u00e0n b\u1ed9 ph\u00f9 sa b\u1ecdi \u0111\u1eafp \u2192 h\u00ecnh qu\u1ea1t v\u1edbi nhi\u1ec1u k\u00eanh ph\u00e2n l\u01b0u. V\u00ed d\u1ee5: \u0110\u1ed3ng b\u1eb1ng ch\u00e2u th\u1ed5 Rh\u00f4ne (Ph\u00e1p)."
  }
};

function showDef(key) {
  const panel = document.getElementById('def-panel');
  const t = document.getElementById('def-title');
  const b = document.getElementById('def-body');
  const v = document.getElementById('def-vi');
  if (panel.style.display === 'block' && t.textContent === DEFS[key].title) {
    panel.style.display = 'none';
    return;
  }
  t.textContent = DEFS[key].title;
  b.textContent = DEFS[key].body;
  v.textContent = DEFS[key].vi;
  panel.style.display = 'block';
}
</script>

<!-- ============= SECTION 1 ============= -->
<h2>&#127956;&#65039; Section 1: Upland Landforms (Upper Course)</h2>
<h2 style="color:#7c3aed;font-size:20px;border-bottom:none;padding-bottom:0;margin-top:-10px;">1. \u0110\u1ecba H\u00ecnh Th\u01b0\u1ee3ng L\u01b0u</h2>

<div class="info-box">
  <strong>Dominant process:</strong> <b style="color:#9333ea">Vertical erosion</b> &mdash; the river cuts downward into the bedrock. The gradient is steep, the channel is narrow, and the river transports large, angular boulders by <b style="color:#9333ea">traction</b> and <b style="color:#9333ea">saltation</b>.
</div>
<p class="vi">\u1edc <b style="color:#9333ea">th\u01b0\u1ee3ng l\u01b0u</b>, s\u00f4ng c\u00f3 \u0111\u1ed9 d\u1ed1c cao v\u00e0 n\u0103ng l\u01b0\u1ee3ng l\u1edbn. Qu\u00e1 tr\u00ecnh ch\u1ee7 \u0111\u1ea1o l\u00e0 <b style="color:#9333ea">x\u00f3i m\u00f2n th\u1eb3ng \u0111\u1ee9ng</b> (vertical erosion) &mdash; s\u00f4ng c\u1eaft s\u00e2u xu\u1ed1ng l\u00f2ng \u0111\u1ea5t, v\u1eadn chuy\u1ec3n c\u00e1c t\u1ea3ng \u0111\u00e1 l\u1edbn b\u1eb1ng <b style="color:#9333ea">k\u00e9o l\u1eaft</b> v\u00e0 <b style="color:#9333ea">nh\u1ea3y c\u00f3c</b>.</p>

<h3>V-shaped Valley &amp; Interlocking Spurs</h3>
<p>
  As the river erodes downward, the valley floor deepens. Weathering and mass movement on the exposed valley walls supply material that the river carries away. This creates a characteristic <b style="color:#9333ea">V-shaped cross profile</b>. Because the river lacks the power to erode sideways through hard rock outcrops, it winds around them. The ridges that jut into the valley from alternate sides are called <b style="color:#9333ea">interlocking spurs</b>.
</p>
<p class="vi">
  \u0110\u00e1 cu\u1ed9i t\u1ea1i \u0111\u00e1y s\u00f4ng b\u00e0o m\u00f2n l\u00f2ng s\u00f4ng theo ki\u1ec3u <b style="color:#9333ea">m\u00e0i m\u00f2n</b> (abrasion), c\u1eaft s\u00e2u xu\u1ed1ng t\u1ea1o h\u00ecnh ch\u1eef V d\u1ed1c \u0111\u1ee9ng. \u0110\u1ea5t v\u00e0 \u0111\u00e1 t\u1eeb s\u01b0\u1eddn th\u00f9ng l\u0169ng b\u1ecb r\u1eeda tr\u00f4i xu\u1ed1ng. Khi s\u00f4ng u\u1ed1n quanh ch\u01b0\u1edbng ng\u1ea1i v\u1eadt, c\u00e1c m\u0169i \u0111\u1ea5t cao nh\u00f4 ra xen k\u1ebd t\u1eeb hai b\u00ean g\u1ecdi l\u00e0 <b style="color:#9333ea">m\u1ecfm \u0111\u1ecba h\u00ecnh xen k\u1ebd</b> (interlocking spurs).
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig118.png" alt="V-shaped valley and interlocking spurs photo"/>
<p class="caption">Fig. 118 &mdash; V-shaped valley with interlocking spurs (photograph) / Thung l\u0169ng h\u00ecnh ch\u1eef V v\u00e0 m\u1ecfm \u0111\u1ecba h\u00ecnh xen k\u1ebd</p>

<h3>Potholes / H\u1ed1 B\u00e0o M\u00f2n</h3>
<p>
  In turbulent upper-course water, pebbles become trapped in small depressions on the riverbed. The swirling current drills these pebbles around in circles, grinding the rock by <b style="color:#9333ea">abrasion</b> into smooth, cylindrical <b style="color:#9333ea">potholes</b>.
</p>
<p class="vi">
  \u0110\u00e1 cu\u1ed9i b\u1ecb gi\u1eef l\u1ea1i trong c\u00e1c h\u1ed1c t\u1ea1i \u0111\u00e1y s\u00f4ng. D\u00f2ng ch\u1ea3y xo\u00e1y m\u1ea1nh quay ch\u00fang, kho\u00e9t th\u00e0nh c\u00e1c h\u1ed1 tr\u00f2n nh\u1eb5n g\u1ecdi l\u00e0 <b style="color:#9333ea">h\u1ed1 b\u00e0o m\u00f2n</b> (potholes) do ma s\u00e1t.
</p>

<h3>Waterfalls &amp; Gorges / Th\u00e1c N\u01b0\u1edbc &amp; H\u1ebb N\u00fai</h3>
<p>
  A waterfall develops where the river crosses a band of <b style="color:#9333ea">resistant (hard) rock</b> overlying <b style="color:#9333ea">less resistant (soft) rock</b>:
</p>
<ol>
  <li>The softer rock erodes faster, undercutting the hard rock to form an <b style="color:#9333ea">overhang</b>.</li>
  <li>A <b style="color:#9333ea">plunge pool</b> is scoured at the base by <b style="color:#9333ea">hydraulic action</b> and abrasion.</li>
  <li>The unsupported overhang collapses; the waterfall retreats upstream.</li>
  <li>Repeated retreat leaves a steep-sided <b style="color:#9333ea">gorge of recession</b> downstream.</li>
</ol>
<p class="vi">
  Th\u00e1c n\u01b0\u1edbc h\u00ecnh th\u00e0nh n\u01a1i s\u00f4ng ch\u1ea3y qua c\u00e1c d\u1ea3i <b style="color:#9333ea">\u0111\u00e1 c\u1ee9ng</b> v\u00e0 <b style="color:#9333ea">\u0111\u00e1 m\u1ec1m</b> xen k\u1ebd. \u0110\u00e1 m\u1ec1m b\u1ecb x\u00f3i m\u00f2n nhanh h\u01a1n t\u1ea1o ra b\u1eadc th\u1ec1m. M\u00e1i \u0111\u00e1 c\u1ee9ng ph\u00eda tr\u00ean b\u1ecb kho\u00e9t r\u1ed7ng b\u00ean d\u01b0\u1edbi t\u1ea1o <b style="color:#9333ea">v\u00e1ch th\u00f2ng</b> (overhang) v\u00e0 <b style="color:#9333ea">h\u1ed1 xo\u00e1i</b> (plunge pool). Khi m\u00e1i \u0111\u00e1 s\u1ee5p xu\u1ed1ng, th\u00e1c l\u00f9i d\u1ea7n v\u1ec1 th\u01b0\u1ee3ng l\u01b0u t\u1ea1o ra <b style="color:#9333ea">h\u1ebb n\u00fai</b> (gorge of recession). V\u00ed d\u1ee5: Th\u00e1c Niagara.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig121.png" alt="Waterfall and gorge formation diagram"/>
<p class="caption">Fig. 121 &mdash; Formation of a waterfall and gorge / S\u01a1 \u0111\u1ed3 h\u00ecnh th\u00e0nh th\u00e1c n\u01b0\u1edbc v\u00e0 h\u1ebb n\u00fai. V\u00ed d\u1ee5: Niagara Falls.</p>

<!-- ============= SECTION 2 ============= -->
<h2>&#127807; Section 2: Lowland Landforms (Middle &amp; Lower Course)</h2>
<h2 style="color:#7c3aed;font-size:20px;border-bottom:none;padding-bottom:0;margin-top:-10px;">2. \u0110\u1ecba H\u00ecnh Trung v\u00e0 H\u1ea1 L\u01b0u</h2>

<div class="info-box">
  <strong>Dominant processes:</strong> <b style="color:#9333ea">Lateral erosion</b> widens the valley in the middle course; <b style="color:#9333ea">deposition</b> dominates in the lower course as gradient decreases and the river loses energy. Sediment (<b style="color:#9333ea">alluvium</b>) is dropped across the floodplain.
</div>
<p class="vi">
  \u1edc <b style="color:#9333ea">trung v\u00e0 h\u1ea1 l\u01b0u</b>, \u0111\u1ed9 d\u1ed1c gi\u1ea3m. Qu\u00e1 tr\u00ecnh ch\u1ee7 \u0111\u1ea1o l\u00e0 <b style="color:#9333ea">x\u00f3i m\u00f2n ngang</b> (lateral erosion) v\u00e0 <b style="color:#9333ea">b\u1ed3i t\u1ee5</b> (deposition). Ph\u00f9 sa (<b style="color:#9333ea">alluvium</b>) \u0111\u01b0\u1ee3c b\u1ed3i \u0111\u1eafp tr\u00ean \u0111\u1ed3ng b\u1eb1ng.
</p>

<h3>Meanders / Kh\u00fac Cong S\u00f4ng</h3>
<p>
  On the gentle gradient of the middle course, the river swings into bends called <b style="color:#9333ea">meanders</b>. The fastest flow is pushed to the <b style="color:#9333ea">outside of each bend</b> where it undercuts the bank, forming a steep <b style="color:#9333ea">river cliff</b>. On the <b style="color:#9333ea">inside bend</b>, flow is slowest and material is deposited to form a gently sloping <b style="color:#9333ea">slip-off slope</b> (point bar). The meander migrates and grows over time.
</p>
<p class="vi">
  D\u00f2ng ch\u1ea3y nhanh nh\u1ea5t t\u1eadp trung \u1edf <b style="color:#9333ea">b\u1edd ngo\u00e0i</b> (outer bend) \u2192 x\u00f3i m\u00f2n \u2192 t\u1ea1o <b style="color:#9333ea">v\u00e1ch s\u00f4ng</b> (river cliff). D\u00f2ng ch\u1ea3y ch\u1eadm h\u01a1n \u1edf <b style="color:#9333ea">b\u1edd trong</b> \u2192 b\u1ed3i \u0111\u1eafp \u2192 t\u1ea1o <b style="color:#9333ea">s\u01b0\u1eddn tr\u01b0\u1ee3t</b> (slip-off slope). Kh\u00fac cong ng\u00e0y c\u00e0ng m\u1edf r\u1ed9ng v\u00e0 di chuy\u1ec3n.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig125.png" alt="Meander formation diagram"/>
<p class="caption">Fig. 125 &mdash; Meander cross-section showing river cliff and slip-off slope / M\u1eb7t c\u1eaft ngang kh\u00fac cong s\u00f4ng</p>

<h3>Oxbow Lakes / H\u1ed3 M\u00f3ng Ng\u1ef1a</h3>
<p>
  As a meander becomes very tight, the neck of land between loops narrows. During a <b style="color:#9333ea">flood</b>, the river breaks through the neck and takes the shorter, straighter path. <b style="color:#9333ea">Deposition</b> seals off the ends of the old loop, isolating it as a curved <b style="color:#9333ea">oxbow lake</b>. Cut off from the main river, it slowly silts up and becomes a marshy hollow.
</p>
<p class="vi">
  Khi c\u1ed5 c\u1ee7a kh\u00fac cong ng\u00e0y c\u00e0ng h\u1eb9p, trong m\u1ed9t tr\u1eadn l\u0169 s\u00f4ng c\u1eaft th\u1eb3ng qua c\u1ed5 \u2192 \u0111o\u1ea1n s\u00f4ng c\u0169 b\u1ecb c\u00f4 l\u1eadp \u2192 h\u00ecnh th\u00e0nh <b style="color:#9333ea">h\u1ed3 m\u00f3ng ng\u1ef1a</b> (oxbow lake). H\u1ed3 d\u1ea7n b\u1ecb b\u1ed3i l\u1eafp v\u00e0 tr\u1edf th\u00e0nh v\u0169ng l\u1ea7y.
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig128.png" alt="Oxbow lake formation diagram"/>
<p class="caption">Fig. 128 &mdash; Stages in the formation of an oxbow lake / C\u00e1c giai \u0111o\u1ea1n h\u00ecnh th\u00e0nh h\u1ed3 m\u00f3ng ng\u1ef1a</p>

<h3>Floodplains &amp; Lev\u00e9es / \u0110\u1ed3ng B\u1eb1ng Ng\u1eadp L\u1ee5t &amp; \u0110\u00ea T\u1ef1 Nhi\u00ean</h3>
<p>
  The <b style="color:#9333ea">floodplain</b> is the wide, flat valley floor built up by layers of <b style="color:#9333ea">alluvium</b> deposited during repeated floods. When the river overtops its banks, it immediately loses velocity; the coarsest sediment is dropped first, right beside the channel, gradually building raised ridges called <b style="color:#9333ea">natural lev\u00e9es</b>. Finer silt spreads further across the floodplain.
</p>
<p class="vi">
  Khi s\u00f4ng tr\u00e0n b\u1edd, n\u00f3 b\u1ed3i \u0111\u1eafp <b style="color:#9333ea">ph\u00f9 sa</b> (alluvium &mdash; c\u00e1t, b\u00f9n, s\u00e9t) tr\u00ean \u0111\u1ed3ng b\u1eb1ng ph\u1eb3ng ven s\u00f4ng \u2192 <b style="color:#9333ea">\u0111\u1ed3ng b\u1eb1ng ng\u1eadp l\u1ee5t</b> (floodplain). V\u1eadt li\u1ec7u th\u00f4 nh\u1ea5t \u0111\u1ecdc l\u1ea1i ven b\u1edd k\u00eanh, x\u00e2y d\u1ef1ng n\u00ean c\u00e1c <b style="color:#9333ea">\u0111\u00ea t\u1ef1 nhi\u00ean</b> (lev\u00e9es).
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig129.png" alt="Floodplain and levee diagram"/>
<p class="caption">Fig. 129 &mdash; Cross-section of a floodplain showing natural lev\u00e9es / M\u1eb7t c\u1eaft \u0111\u1ed3ng b\u1eb1ng ng\u1eadp l\u1ee5t v\u00e0 \u0111\u00ea t\u1ef1 nhi\u00ean</p>

<h3>Braided Channels / K\u00eanh Ph\u00e2n L\u01b0u \u0110an Xen</h3>
<p>
  When a river carries an exceptionally high <b style="color:#9333ea">sediment load</b> (e.g., meltwater rivers downstream of glaciers), it cannot transport all the material and begins to deposit <b style="color:#9333ea">mid-channel bars</b>. These bars split the flow into a network of shallow, interweaving channels &mdash; a <b style="color:#9333ea">braided channel</b>. Common in semi-arid environments and near glaciers.
</p>
<p class="vi">
  Khi s\u00f4ng mang t\u1ea3i l\u01b0\u1ee3ng ph\u00f9 sa r\u1ea5t l\u1edbn so v\u1edbi l\u01b0u l\u01b0\u1ee3ng, n\u00f3 ph\u00e2n th\u00e0nh nhi\u1ec1u k\u00eanh nh\u1ecf ng\u0103n c\u00e1ch b\u1edfi c\u00e1c <b style="color:#9333ea">b\u00e3i b\u1ed3i</b> (bars). Th\u01b0\u1eddng g\u1eb7p \u1edf c\u00e1c s\u00f4ng b\u0103ng tan.
</p>

<h3>Deltas / \u0110\u1ed3ng B\u1eb1ng Ch\u00e2u Th\u1ed5</h3>
<p>
  Where a river reaches a <b style="color:#9333ea">sea or lake</b> with little wave or tidal energy, velocity drops to nearly zero and all remaining sediment is deposited. The river splits into a fan of <b style="color:#9333ea">distributaries</b> spreading across the growing deposit. Example: the <b style="color:#9333ea">Rh\u00f4ne Delta (Camargue), France</b>.
</p>
<p class="vi">
  Khi s\u00f4ng \u0111\u1ed5 v\u00e0o bi\u1ec3n ho\u1eb7c h\u1ed3 y\u00ean t\u0129nh, v\u1eadn t\u1ed1c gi\u1ea3m \u0111\u1ed9t ng\u1ed9t \u2192 to\u00e0n b\u1ed9 ph\u00f9 sa \u0111\u01b0\u1ee3c b\u1ed3i \u0111\u1eafp. \u0110\u1ea5t d\u1ea7n h\u00ecnh th\u00e0nh m\u1ed9t h\u00ecnh qu\u1ea1t v\u1edbi nhi\u1ec1u <b style="color:#9333ea">k\u00eanh ph\u00e2n l\u01b0u</b> (distributaries). V\u00ed d\u1ee5: <b style="color:#9333ea">\u0110\u1ed3ng b\u1eb1ng ch\u00e2u th\u1ed5 Rh\u00f4ne</b> (Ph\u00e1p).
</p>
<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/1_2_fig132.png" alt="Delta formation diagram"/>
<p class="caption">Fig. 132 &mdash; Delta formation showing distributaries fanning out into the sea. Example: Rh\u00f4ne Delta, France / S\u01a1 \u0111\u1ed3 h\u00ecnh th\u00e0nh \u0111\u1ed3ng b\u1eb1ng ch\u00e2u th\u1ed5 Rh\u00f4ne, Ph\u00e1p.</p>

<!-- ============= SUMMARY TABLE ============= -->
<h2>&#128203; Summary Table / B\u1ea3ng T\u00f3m T\u1eaft</h2>
<table>
  <thead>
    <tr>
      <th>Landform / D\u1ea1ng \u0110\u1ecba H\u00ecnh</th>
      <th>Location / V\u1ecb Tr\u00ed</th>
      <th>Dominant Process / Qu\u00e1 Tr\u00ecnh Ch\u1ee7 \u0110\u1ea1o</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>V-shaped Valley (\u0111\u1ecba h\u00ecnh h\u00ecnh ch\u1eef V)</td><td>Upper / Th\u01b0\u1ee3ng l\u01b0u</td><td>Vertical erosion / X\u00f3i m\u00f2n th\u1eb3ng \u0111\u1ee9ng</td></tr>
    <tr><td>Interlocking Spurs (m\u1ecfm \u0111\u1ecba h\u00ecnh xen k\u1ebd)</td><td>Upper / Th\u01b0\u1ee3ng l\u01b0u</td><td>Vertical erosion &mdash; river avoids hard rock</td></tr>
    <tr><td>Pothole (h\u1ed1 b\u00e0o m\u00f2n)</td><td>Upper / Th\u01b0\u1ee3ng l\u01b0u</td><td>Abrasion / M\u00e0i m\u00f2n</td></tr>
    <tr><td>Waterfall &amp; Gorge (th\u00e1c n\u01b0\u1edbc &amp; h\u1ebb n\u00fai)</td><td>Upper / Th\u01b0\u1ee3ng l\u01b0u</td><td>Hydraulic action + abrasion + collapse</td></tr>
    <tr><td>Meander (kh\u00fac cong s\u00f4ng)</td><td>Middle / Trung l\u01b0u</td><td>Lateral erosion + deposition</td></tr>
    <tr><td>Oxbow Lake (h\u1ed3 m\u00f3ng ng\u1ef1a)</td><td>Middle / Trung l\u01b0u</td><td>Erosion (neck cut-off) + deposition</td></tr>
    <tr><td>Floodplain (\u0111\u1ed3ng b\u1eb1ng ng\u1eadp l\u1ee5t)</td><td>Middle &amp; Lower / Trung &amp; H\u1ea1 l\u01b0u</td><td>Deposition / B\u1ed3i t\u1ee5</td></tr>
    <tr><td>Natural Lev\u00e9e (\u0111\u00ea t\u1ef1 nhi\u00ean)</td><td>Middle &amp; Lower / Trung &amp; H\u1ea1 l\u01b0u</td><td>Deposition (coarse sediment beside channel)</td></tr>
    <tr><td>Braided Channel (k\u00eanh \u0111an xen)</td><td>Lower / H\u1ea1 l\u01b0u</td><td>Deposition / B\u1ed3i t\u1ee5</td></tr>
    <tr><td>Delta (\u0111\u1ed3ng b\u1eb1ng ch\u00e2u th\u1ed5)</td><td>Lower &mdash; mouth / H\u1ea1 l\u01b0u &mdash; c\u1eeda s\u00f4ng</td><td>Deposition &mdash; velocity \u2192 zero</td></tr>
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
    print("Upload successful - no content returned (expected for Prefer: return=minimal).")
