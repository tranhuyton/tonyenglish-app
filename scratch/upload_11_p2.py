import requests
import json

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
PAGE_ID = "c27766f1-0030-4641-8d82-d3771b354e01"

VI = '<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">{}</p>'

HTML_CONTENT = """\
<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">

<!-- ═══ HEADER ═══ -->
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#1e3a8a;font-size:32px;margin-bottom:6px;border-bottom:3px solid #60a5fa;display:inline-block;padding-bottom:10px;">&#127754; 1.1 Hydrological Characteristics &amp; Processes</h1>
<h2 style="color:#7c3aed;font-size:20px;border:none;padding:0;margin:4px 0 8px 0;">&#272;&#7863;c &#272;i&#7875;m Th&#7911;y V&#259;n &amp; C&aacute;c Qu&aacute; Tr&igrave;nh S&ocirc;ng</h2>
<p style="color:#64748b;font-size:16px;">Understanding rivers, drainage basins, and the water cycle</p>
<p style="color:#64748b;font-size:15px;font-style:italic;">Hi&#7875;u v&#7873; s&ocirc;ng ng&ograve;i, l&#432;u v&#7921;c v&agrave; v&ograve;ng tu&#7847;n ho&agrave;n n&#432;&#7899;c</p>
</div>

<!-- ═══ SECTION 1 ═══ -->
<div style="margin-bottom:50px;">
<h2 style="color:#0f172a;border-bottom:2px solid #a78bfa;padding-bottom:10px;margin-bottom:25px;font-size:24px;">&#128205; 1. Characteristics of Rivers &amp; Drainage Basins</h2>
<h3 style="color:#1e3a8a;font-size:19px;margin-top:0;">&#272;&#7863;c &#272;i&#7875;m S&ocirc;ng Ng&ograve;i &amp; L&#432;u V&#7921;c</h3>

<p style="color:#475569;margin-bottom:20px;">A <b>drainage basin</b> is the area of land drained by a river and its tributaries. It acts as an open system with inputs and outputs. Rivers are an important part of the water cycle; they are channels of water that flow over the Earth&#x27;s surface. Through gravity, rivers transport precipitation that falls onto the land down towards the sea.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>L&#432;u v&#7921;c s&ocirc;ng</b> (drainage basin) l&agrave; v&ugrave;ng &#273;&#7845;t &#273;&#432;&#7907;c tho&aacute;t n&#432;&#7899;c b&#7903;i m&#7897;t con s&ocirc;ng v&agrave; c&aacute;c ph&#7909; l&#432;u c&#7911;a n&oacute;. N&oacute; ho&#7841;t &#273;&#7897;ng nh&#432; m&#7897;t h&#7879; th&#7889;ng m&#7903; v&#7899;i &#273;&#7847;u v&agrave;o v&agrave; &#273;&#7847;u ra. S&ocirc;ng ng&ograve;i l&agrave; m&#7897;t ph&#7847;n quan tr&#7885;ng c&#7911;a v&ograve;ng tu&#7847;n ho&agrave;n n&#432;&#7899;c; ch&uacute;ng l&agrave; c&aacute;c d&ograve;ng ch&#7843;y tr&ecirc;n b&#7873; m&#7863;t Tr&aacute;i &#272;&#7845;t. Nh&#7901; tr&#7885;ng l&#7921;c, s&ocirc;ng v&#7853;n chuy&#7875;n l&#432;&#7907;ng m&#432;a r&#417;i tr&ecirc;n &#273;&#7845;t li&#7873;n &#273;&#7893; ra bi&#7875;n.</p>

<div style="background:#f1f5f9;padding:15px;border-radius:8px;margin:20px 0;">
<strong>The Watershed:</strong> The edge of a drainage basin is marked by the watershed, which is usually found on higher ground. This acts as a dividing line, where precipitation falling one side of the watershed flows into one drainage basin and water falling the other side flows into another.
</div>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#432;&#7901;ng ph&acirc;n th&#7911;y</b> th&#432;&#7901;ng n&#7857;m &#7903; &#273;&#7883;a h&igrave;nh cao, l&agrave; &#273;&#432;&#7901;ng ranh gi&#7899;i ng&#259;n c&aacute;ch c&aacute;c l&#432;u v&#7921;c s&ocirc;ng v&#7899;i nhau.</p>

<div style="text-align:center;margin-bottom:25px;">
<img alt="Drainage Basin Example" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_real_fig1_1_cropped_v3.jpeg" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;margin-top:8px;">Figure 1.1: The features of a drainage basin</p>
</div>
<div style="text-align:center;margin-bottom:25px;">
<img alt="Cross-section of drainage basins" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_fig1_2.jpeg?v=2" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:10px;margin-bottom:25px;">Figure 1.2: A cross-section showing drainage basins and watersheds</p>
</div>

<!-- ── Interactive Basin SVG ── -->
<div style="background:#f8fafc;border:1px solid #e2e8f0;padding:20px;text-align:center;box-shadow:0 4px 6px rgba(0,0,0,0.02);margin-bottom:20px;">
<h3 style="color:#4f46e5;margin-top:0;font-size:18px;">The Drainage Basin System / H&#7879; Th&#7889;ng L&#432;u V&#7921;c S&ocirc;ng</h3>
<p style="color:#64748b;margin-bottom:15px;">Click on any feature on the map to view its details. / Nh&#7845;p v&agrave;o b&#7845;t k&#7923; &#273;i&#7875;m n&agrave;o &#273;&#7875; xem th&#244;ng tin.</p>
<svg height="auto" style="max-width:550px;" viewBox="0 0 600 300" width="100%">
<rect fill="#f0f9ff" height="300" onclick="showMapInfo('default')" rx="10" style="cursor:pointer;" width="600" x="0" y="0"></rect>
<path class="svg-clickable" d="M 50,150 C 100,50 300,20 500,100 C 550,150 500,250 300,280 C 100,280 20,200 50,150 Z" fill="none" onclick="showMapInfo('watershed')" stroke="#94a3b8" stroke-dasharray="8,8" stroke-width="3"></path>
<text class="svg-clickable-text" fill="#64748b" font-size="14" font-weight="bold" onclick="showMapInfo('watershed')" style="cursor:pointer;" x="350" y="50">Watershed</text>
<path class="svg-clickable" d="M 120,120 C 200,180 300,130 450,220" fill="none" id="mainRiverPath" onclick="showMapInfo('long-profile')" stroke="#3b82f6" stroke-width="6"></path>
<text class="svg-clickable-text" fill="#1d4ed8" font-size="14" font-weight="bold" onclick="showMapInfo('long-profile')" style="cursor:pointer;text-shadow:1px 1px 0 #f0f9ff,-1px -1px 0 #f0f9ff,1px -1px 0 #f0f9ff,-1px 1px 0 #f0f9ff;" transform="rotate(15 320,165)" x="320" y="165">Long Profile</text>
<path class="svg-clickable" d="M 180,70 C 200,100 220,130 230,155" fill="none" onclick="showMapInfo('tributary')" stroke="#60a5fa" stroke-width="3"></path>
<path class="svg-clickable" d="M 380,80 C 370,120 370,150 350,175" fill="none" onclick="showMapInfo('tributary')" stroke="#60a5fa" stroke-width="3"></path>
<path class="svg-clickable" d="M 200,240 C 250,220 280,200 290,175" fill="none" onclick="showMapInfo('tributary')" stroke="#60a5fa" stroke-width="3"></path>
<text class="svg-clickable-text" fill="#2563eb" font-size="12" font-weight="bold" onclick="showMapInfo('tributary')" style="cursor:pointer;" x="180" y="60">Tributary</text>
<circle class="svg-clickable-circle" cx="120" cy="120" fill="#ef4444" onclick="showMapInfo('source')" r="6" style="cursor:pointer;"></circle>
<text class="svg-clickable-text" fill="#ef4444" font-size="14" font-weight="bold" onclick="showMapInfo('source')" style="cursor:pointer;" text-anchor="end" x="110" y="110">Source</text>
<circle class="svg-clickable-circle" cx="230" cy="155" fill="#f59e0b" onclick="showMapInfo('confluence')" r="5" style="cursor:pointer;"></circle>
<text class="svg-clickable-text" fill="#d97706" font-size="12" font-weight="bold" onclick="showMapInfo('confluence')" style="cursor:pointer;" x="210" y="145">Confluence</text>
<circle class="svg-clickable-circle" cx="450" cy="220" fill="#10b981" onclick="showMapInfo('mouth')" r="6" style="cursor:pointer;"></circle>
<text class="svg-clickable-text" fill="#10b981" font-size="14" font-weight="bold" onclick="showMapInfo('mouth')" style="cursor:pointer;" x="465" y="225">Mouth</text>
</svg>
</div>
<style>
  .map-info-panel{display:none;margin-top:20px;animation:fadeIn 0.3s ease;}
  .map-info-panel.active{display:block;}
  .svg-clickable{cursor:pointer;transition:all 0.2s;}
  .svg-clickable:hover{stroke-width:8;opacity:0.8;filter:drop-shadow(0 0 5px rgba(59,130,246,0.5));}
  .svg-clickable-circle:hover{r:9;filter:drop-shadow(0 0 5px rgba(239,68,68,0.5));}
  .svg-clickable-text:hover{font-size:15px;}
  @keyframes fadeIn{from{opacity:0;transform:translateY(-5px);}to{opacity:1;transform:translateY(0);}}
</style>

<!-- Panel: Default -->
<div class="map-info-panel" id="info-default">
<div style="background:#ffffff;border-left:4px solid #94a3b8;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);text-align:center;">
<p style="color:#64748b;margin:0;"><i>Click on any feature on the map to view its definition. / Nh&#7845;p v&agrave;o b&#7845;t k&#7923; &#273;i&#7875;m tr&ecirc;n b&#7843;n &#273;&#7891; &#273;&#7875; xem &#273;&#7883;nh ngh&#297;a.</i></p>
</div>
</div>

<!-- Panel: Mouth -->
<div class="map-info-panel" id="info-mouth">
<div style="background:#ffffff;border-left:4px solid #10b981;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#047857;margin-top:0;font-size:18px;">Mouth / C&#7917;a S&ocirc;ng</h3>
<p style="margin:0;color:#475569;line-height:1.6;">Where the river flows into a lake or ocean.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>C&#7917;a s&ocirc;ng</b> l&agrave; n&#417;i s&ocirc;ng &#273;&#7893; ra bi&#7875;n ho&#7863;c h&#7891;.</p>
</div>
</div>

<!-- Panel: Tributary -->
<div class="map-info-panel" id="info-tributary">
<div style="background:#ffffff;border-left:4px solid #3b82f6;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#1d4ed8;margin-top:0;font-size:18px;">Tributary / Ph&#7909; L&#432;u</h3>
<p style="margin:0;color:#475569;line-height:1.6;">A smaller river or stream flowing into a larger river.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Ph&#7909; l&#432;u</b> l&agrave; d&ograve;ng s&ocirc;ng nh&#7887; h&#417;n ch&#7843;y v&agrave;o s&ocirc;ng ch&iacute;nh.</p>
</div>
</div>

<!-- Panel: Confluence -->
<div class="map-info-panel" id="info-confluence">
<div style="background:#ffffff;border-left:4px solid #f59e0b;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#b45309;margin-top:0;font-size:18px;">Confluence / H&#7907;p L&#432;u</h3>
<p style="margin:0;color:#475569;line-height:1.6;">The point where two rivers meet.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>H&#7907;p l&#432;u</b> l&agrave; &#273;i&#7875;m g&#7863;p nhau c&#7911;a hai d&ograve;ng s&ocirc;ng.</p>
</div>
</div>

<!-- Panel: Watershed -->
<div class="map-info-panel" id="info-watershed">
<div style="background:#ffffff;border-left:4px solid #64748b;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#475569;margin-top:0;font-size:18px;">Watershed / &#272;&#432;&#7901;ng Ph&acirc;n Th&#7911;y</h3>
<p style="margin:0;color:#475569;line-height:1.6;">The boundary dividing one drainage basin from another.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#432;&#7901;ng ph&acirc;n th&#7911;y</b> th&#432;&#7901;ng n&#7857;m &#7903; &#273;&#7883;a h&igrave;nh cao, l&agrave; &#273;&#432;&#7901;ng ranh gi&#7899;i ng&#259;n c&aacute;ch c&aacute;c l&#432;u v&#7921;c s&ocirc;ng v&#7899;i nhau.</p>
</div>
</div>

<!-- Panel: Source (active by default) -->
<div class="map-info-panel active" id="info-source">
<div style="background:#f8fafc;border:1px solid #e2e8f0;border-left:4px solid #ef4444;padding:25px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#0f172a;border-bottom:2px solid #fca5a5;padding-bottom:8px;margin-top:0;">The source of a river / Ngu&#7891;n c&#7911;a m&#7897;t con s&ocirc;ng</h3>
<p style="color:#475569;line-height:1.6;">A river is a large, natural stream of flowing water. The place where a river begins may be:</p>
<ul style="color:#475569;line-height:1.6;padding-left:20px;">
<li>an <b>upland lake</b>. <br/><span style="color:#64748b;"><i>Example: the Mississippi River begins as a stream from Lake Itasca.</i></span></li>
<li>a <b>melting glacier</b>. <br/><span style="color:#64748b;"><i>Example: the Gangotri Glacier is the source of the River Ganges.</i></span></li>
<li>a <b>spring</b> in a boggy upland area.</li>
<li>a <b>spring</b> at the foot of an escarpment at the boundary between permeable and impermeable rock.</li>
</ul>
<p style="color:#475569;line-height:1.6;margin-bottom:8px;">When small streams begin to flow, they act under gravity, following the fastest route downslope. Water is added from <b style="color:#9333ea;">groundwater flow</b>, <b style="color:#9333ea;">throughflow</b> and <b style="color:#9333ea;">overland flow</b>.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;">Ngu&#7891;n c&#7911;a m&#7897;t con s&ocirc;ng c&oacute; th&#7875; l&agrave;: h&#7891; cao nguy&ecirc;n, s&ocirc;ng b&#259;ng tan, ho&#7863;c su&#7889;i &#7903; v&ugrave;ng &#273;&#7845;t ng&#7853;p n&#432;&#7899;c. C&aacute;c d&ograve;ng ch&#7843;y nh&#7887; h&igrave;nh th&agrave;nh d&#432;&#7899;i t&aacute;c d&#7909;ng c&#7911;a tr&#7885;ng l&#7921;c, &#273;&#432;&#7907;c b&#7893; sung b&#7903;i <b style="color:#9333ea;">d&ograve;ng ch&#7843;y ng&#7847;m</b>, <b style="color:#9333ea;">d&ograve;ng ch&#7843;y trong &#273;&#7845;t</b> v&agrave; <b style="color:#9333ea;">d&ograve;ng ch&#7843;y b&#7873; m&#7863;t</b>.</p>
</div>
</div>

<!-- Panel: Long Profile -->
<div class="map-info-panel" id="info-long-profile">
<div style="background:#f8fafc;border:1px solid #e2e8f0;border-left:4px solid #3b82f6;padding:25px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#0f172a;border-bottom:2px solid #93c5fd;padding-bottom:8px;margin-top:0;">The long profile / M&#7863;t c&#7855;t d&#7885;c</h3>
<p style="color:#475569;line-height:1.6;">The <b>long profile</b> of a river is a longitudinal section drawn along the river from source to mouth, expressed as a concave-upwards curve.</p>
<h4 style="margin:20px 0 10px 0;color:#1e40af;font-size:16px;">Channel Characteristics</h4>
<ul style="color:#475569;line-height:1.6;padding-left:20px;margin-bottom:16px;">
<li><b style="color:#2563eb;">Width &amp; Depth:</b> The width and depth of the river channel.</li>
<li><b style="color:#2563eb;">Wetted Perimeter:</b> The total length of bed and bank sides in contact with water.</li>
<li><b style="color:#2563eb;">Velocity:</b> Speed of water flow.</li>
<li><b style="color:#2563eb;">Discharge:</b> Volume of water passing a point (Velocity &times; Cross-sectional area).</li>
</ul>
<p style="color:#475569;line-height:1.6;">As rivers change from upstream to downstream: Discharge, width, depth, velocity and load quantity all <b>increase</b>. Load particle size, channel bed roughness and gradient all <b>decrease</b>.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>M&#7863;t c&#7855;t d&#7885;c</b> (long profile) th&#7875; hi&#7879;n s&#7921; thay &#273;&#7893;i &#273;&#7897; d&#7889;c c&#7911;a s&ocirc;ng t&#7915; ngu&#7891;n &#273;&#7871;n c&#7917;a. Khi s&ocirc;ng ch&#7843;y v&#7873; ph&iacute;a c&#7917;a: l&#432;u l&#432;&#7907;ng, chi&#7873;u r&#7897;ng, chi&#7873;u s&acirc;u v&agrave; v&#7853;n t&#7889;c <b>t&#259;ng</b>; k&iacute;ch th&#432;&#7899;c h&#7841;t t&#7843;i l&#432;&#7907;ng, &#273;&#7897; nh&#225;m &#273;&aacute;y s&ocirc;ng v&agrave; &#273;&#7897; d&#7889;c <b>gi&#7843;m</b>.</p>
</div>
</div>

<script>
  function showMapInfo(panelId){
    document.querySelectorAll('.map-info-panel').forEach(el=>el.classList.remove('active'));
    document.getElementById('info-'+panelId).classList.add('active');
  }
</script>
</div>

<!-- ═══ SECTION 2 ═══ -->
<div style="margin-bottom:50px;">
<h2 style="color:#0f172a;border-bottom:2px solid #34d399;padding-bottom:10px;margin-bottom:25px;font-size:24px;">&#128201; 2. The Bradshaw Model / M&ocirc; H&igrave;nh Bradshaw</h2>

<p style="color:#475569;line-height:1.6;">The <b>Bradshaw model</b> is a geographical model that suggests how a river&#x27;s characteristics change from the source to the mouth of the river. The long profile is sub-divided into three sections: Upper course, Middle course, and Lower course.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>M&ocirc; h&igrave;nh Bradshaw</b> &#273;&#7873; xu&#7845;t c&aacute;ch c&aacute;c &#273;&#7863;c &#273;i&#7875;m c&#7911;a s&ocirc;ng thay &#273;&#7893;i t&#7915; ngu&#7891;n &#273;&#7871;n c&#7917;a. M&#7863;t c&#7855;t d&#7885;c &#273;&#432;&#7907;c chia th&agrave;nh ba &#273;o&#7841;n: th&#432;&#7907;ng l&#432;u, trung l&#432;u v&agrave; h&#7841; l&#432;u.</p>

<div style="background:#f1f5f9;padding:15px;border-radius:8px;margin:20px 0;">
<p style="color:#475569;margin-bottom:10px;"><b>In upland areas</b>, closer to the source, rivers tend to be narrow and shallow. They have a smaller wetted perimeter and a lower discharge. Upland rivers have a lower velocity because the large bedload creates friction, which slows the water down.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:4px;margin-bottom:12px;border-left:3px solid #cbd5e1;padding-left:12px;">&#7902; <b>th&#432;&#7907;ng l&#432;u</b>, g&#7847;n ngu&#7891;n, s&ocirc;ng h&#7865;p v&agrave; n&ocirc;ng h&#417;n, c&oacute; l&#432;u l&#432;&#7907;ng nh&#7887; h&#417;n. S&ocirc;ng th&#432;&#7907;ng l&#432;u c&oacute; v&#7853;n t&#7889;c th&#7845;p h&#417;n do ma s&aacute;t l&#7899;n t&#7915; &#273;&aacute;y s&ocirc;ng th&ocirc; nh&aacute;m.</p>
<p style="color:#475569;margin-bottom:10px;"><b>In lowland areas</b>, closer to the mouth, rivers are wide and deep. They have a much larger wetted perimeter and a higher discharge. Lowland rivers have a higher velocity as there is less friction from the riverbed and banks.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:4px;margin-bottom:4px;border-left:3px solid #cbd5e1;padding-left:12px;">&#7902; <b>h&#7841; l&#432;u</b>, g&#7847;n c&#7917;a s&ocirc;ng, s&ocirc;ng r&#7897;ng v&agrave; s&acirc;u h&#417;n, c&oacute; l&#432;u l&#432;&#7907;ng l&#7899;n h&#417;n. S&ocirc;ng h&#7841; l&#432;u c&oacute; v&#7853;n t&#7889;c cao h&#417;n do &iacute;t ma s&aacute;t t&#7915; &#273;&aacute;y s&ocirc;ng nh&#7861;n.</p>
<p style="font-size:14px;color:#1e3a8a;font-style:italic;">&#128161; <strong>TIP:</strong> Think of river velocity like a ball rolling down a hill; the ball will speed up as it rolls and will be travelling much faster at the bottom of the hill.</p>
</div>

<!-- Interactive Bradshaw SVG -->
<div style="background:#ffffff;border:1px solid #e2e8f0;padding:20px;box-shadow:0 4px 6px rgba(0,0,0,0.05);margin-bottom:30px;margin-top:20px;">
<h4 style="text-align:center;color:#0f172a;margin-top:0;">Interactive Long &amp; Cross Profiles / S&#417; &#272;&#7891; D&#7885;c &amp; C&#7855;t Ngang T&#432;&#417;ng T&aacute;c</h4>
<p style="text-align:center;font-size:13px;color:#64748b;margin-bottom:20px;">Click on each section to view characteristics and real-world examples. / Nh&#7845;p v&agrave;o m&#7895;i &#273;o&#7841;n &#273;&#7875; xem &#273;&#7863;c &#273;i&#7875;m v&agrave; v&iacute; d&#7909; th&#7921;c t&#7871;.</p>
<div style="position:relative;width:100%;max-width:700px;margin:0 auto;">
<svg style="width:100%;height:auto;font-family:sans-serif;" viewBox="0 0 700 320">
<defs>
<linearGradient id="waterGrad2" x1="0%" x2="100%" y1="0%" y2="0%">
<stop offset="0%" stop-color="#93c5fd"></stop>
<stop offset="100%" stop-color="#dbeafe"></stop>
</linearGradient>
</defs>
<text fill="#0f172a" font-size="17" font-weight="bold" text-anchor="middle" x="350" y="25">Long profile / M&#7863;t c&#7855;t d&#7885;c</text>
<text fill="#0f172a" font-size="15" font-weight="bold" text-anchor="middle" x="466" y="247">Cross profiles / M&#7863;t c&#7855;t ngang</text>
<!-- Upper -->
<g class="course-group" onclick="showCourse('upper')" style="cursor:pointer;">
<rect fill="transparent" height="320" width="233" x="0" y="0"></rect>
<path d="M 20 80 Q 150 160 233 175 L 233 220 L 20 220 Z" fill="url(#waterGrad2)"></path>
<text fill="#1e293b" font-size="16" font-weight="bold" text-anchor="middle" x="126" y="30">Upper course</text>
<text fill="#475569" font-size="12" font-style="italic" text-anchor="middle" x="126" y="50">Steep gradient</text>
<text fill="#475569" font-size="12" text-anchor="middle" x="126" y="65">EROSION</text>
<line marker-end="url(#arrow2)" stroke="#94a3b8" stroke-width="2" x1="126" x2="126" y1="230" y2="250"></line>
<path d="M 80 260 L 126 310 L 170 260 L 170 320 L 80 320 Z" fill="#fcd34d"></path>
<path d="M 80 260 L 126 310 L 170 260" fill="none" stroke="#d97706" stroke-width="2"></path>
<polygon fill="#3b82f6" points="116,300 126,310 136,300"></polygon>
<text fill="#475569" font-size="11" text-anchor="middle" x="126" y="315">River</text>
</g>
<!-- Middle -->
<g class="course-group" onclick="showCourse('middle')" style="cursor:pointer;">
<rect fill="transparent" height="320" width="233" x="233" y="0"></rect>
<path d="M 233 175 Q 350 190 466 195 L 466 220 L 233 220 Z" fill="url(#waterGrad2)"></path>
<line stroke="#94a3b8" stroke-dasharray="4" x1="233" x2="233" y1="20" y2="220"></line>
<text fill="#1e293b" font-size="16" font-weight="bold" text-anchor="middle" x="350" y="45">Middle course</text>
<line marker-end="url(#arrow2)" stroke="#94a3b8" stroke-width="2" x1="350" x2="350" y1="230" y2="250"></line>
<path d="M 300 260 L 320 305 Q 350 315 380 305 L 400 260 L 400 320 L 300 320 Z" fill="#fcd34d"></path>
<path d="M 300 260 L 320 305 Q 350 315 380 305 L 400 260" fill="none" stroke="#d97706" stroke-width="2"></path>
<polygon fill="#3b82f6" points="330,308 350,313 370,308 370,305 330,305"></polygon>
<text fill="#475569" font-size="11" text-anchor="middle" x="350" y="315">River</text>
</g>
<!-- Lower -->
<g class="course-group" onclick="showCourse('lower')" style="cursor:pointer;">
<rect fill="transparent" height="320" width="234" x="466" y="0"></rect>
<path d="M 466 195 Q 580 200 680 200 L 680 220 L 466 220 Z" fill="url(#waterGrad2)"></path>
<line stroke="#94a3b8" stroke-dasharray="4" x1="466" x2="466" y1="20" y2="220"></line>
<text fill="#1e293b" font-size="16" font-weight="bold" text-anchor="middle" x="583" y="30">Lower course</text>
<text fill="#475569" font-size="12" font-style="italic" text-anchor="middle" x="583" y="50">Gentle gradient</text>
<text fill="#475569" font-size="12" text-anchor="middle" x="583" y="65">DEPOSITION</text>
<line marker-end="url(#arrow2)" stroke="#94a3b8" stroke-width="2" x1="583" x2="583" y1="230" y2="250"></line>
<path d="M 520 270 L 550 300 L 570 305 L 596 305 L 616 300 L 646 270 L 646 320 L 520 320 Z" fill="#fcd34d"></path>
<path d="M 520 270 L 550 300 L 570 305 L 596 305 L 616 300 L 646 270" fill="none" stroke="#d97706" stroke-width="2"></path>
<polygon fill="#3b82f6" points="570,305 583,310 596,305"></polygon>
<text fill="#475569" font-size="11" text-anchor="middle" x="583" y="315">River Floodplain</text>
</g>
<defs>
<marker id="arrow2" markerHeight="6" markerWidth="6" orient="auto-start-reverse" refX="5" refY="5" viewBox="0 0 10 10">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#94a3b8"></path>
</marker>
</defs>
</svg>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:15px;margin-bottom:20px;"><span style="color:#ef4444;font-style:normal;">&#9650;</span> Figure 1.8 The long and cross profiles of a river</p>
</div>
<style>
  .course-group rect{transition:fill 0.2s;}
  .course-group:hover rect{fill:rgba(59,130,246,0.08);}
  .course-info{display:none;margin-top:20px;padding:20px;border-radius:8px;border-left:4px solid #3b82f6;background:#f8fafc;}
  .course-info.active{display:block;animation:fadeIn 0.3s ease;}
</style>

<!-- Course info panels -->
<div class="course-info active" id="info-upper">
<h5 style="color:#0f172a;margin:0 0 10px 0;font-size:16px;">The upper course / Th&#432;&#7907;ng l&#432;u</h5>
<ul style="color:#475569;line-height:1.6;margin:0;padding-left:20px;">
<li><b>Characteristics:</b> Steep gradient, narrow and shallow channel, uneven riverbed with large boulders.</li>
<li><b>Main Process:</b> Vertical erosion dominates, creating V-shaped valleys and interlocking spurs. High friction causes turbulent flow.</li>
<li><b>Typical Features:</b> Waterfalls, gorges, and rapids.</li>
</ul>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:10px;margin-bottom:6px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7863;c &#273;i&#7875;m:</b> &#272;&#7897; d&#7889;c l&#7899;n, k&ecirc;nh h&#7865;p v&agrave; n&ocirc;ng, &#273;&aacute;y s&ocirc;ng kh&ocirc;ng b&#7857;ng ph&#7859;ng v&#7899;i nhi&#7873;u &#273;&aacute; t&#7843;ng. <b>Qu&aacute; tr&igrave;nh ch&#7911; &#273;&#7841;o:</b> X&oacute;i m&ograve;n th&#7859;ng &#273;&#7913;ng (vertical erosion), t&#7841;o th&#361;ng l&#361;ng h&igrave;nh ch&#7919; V v&agrave; m&#7887;m &#273;&#7883;a h&igrave;nh xen k&#7869;. <b>&#272;&#7883;a h&igrave;nh ti&ecirc;u bi&#7875;u:</b> Th&aacute;c n&#432;&#7899;c, h&#7867; n&uacute;i, th&aacute;c gh&#7873;nh. <b>V&iacute; d&#7909; th&#7921;c t&#7871;:</b> Th&#432;&#7907;ng l&#432;u s&ocirc;ng Tees &mdash; th&aacute;c High Force cao 21m.</p>
<div style="background:#f8fafc;border-left:3px solid #cbd5e1;padding:10px 15px;margin-top:15px;border-radius:4px;">
<p style="color:#64748b;margin:0;"><i><b>Real-world Example:</b> The upper course of the River Tees features steep valley sides, impermeable rock, and the UK&#x27;s largest waterfall, High Force (21 m high).</i></p>
</div>
<div style="text-align:center;margin-top:15px;">
<img alt="High Force Waterfall" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_fig1_10.jpeg" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:12px;color:#94a3b8;font-style:italic;margin-top:8px;">Figure 1.10: High Force waterfall (River Tees)</p>
</div>
</div>

<div class="course-info" id="info-middle">
<h5 style="color:#0f172a;margin:0 0 10px 0;font-size:16px;">The middle course / Trung l&#432;u</h5>
<ul style="color:#475569;line-height:1.6;margin:0;padding-left:20px;">
<li><b>Characteristics:</b> Gentler gradient, wider and deeper channel. The river flows faster with more discharge as tributaries join.</li>
<li><b>Main Process:</b> Lateral (sideways) erosion takes over from vertical erosion. Transportation of smaller load particles (sand, gravel) increases.</li>
<li><b>Typical Features:</b> Meanders (curves) begin to form, and a narrow floodplain develops.</li>
</ul>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:10px;margin-bottom:6px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7863;c &#273;i&#7875;m:</b> &#272;&#7897; d&#7889;c nh&#7865; h&#417;n, k&ecirc;nh r&#7897;ng v&agrave; s&acirc;u h&#417;n. <b>Qu&aacute; tr&igrave;nh ch&#7911; &#273;&#7841;o:</b> X&oacute;i m&ograve;n ngang (lateral erosion) thay th&#7871; x&oacute;i m&ograve;n th&#7859;ng &#273;&#7913;ng. <b>&#272;&#7883;a h&igrave;nh ti&ecirc;u bi&#7875;u:</b> C&aacute;c kh&uacute;c cong (meanders) b&#7855;t &#273;&#7847;u h&igrave;nh th&agrave;nh, &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#7909;t h&#7865;p xu&#7845;t hi&#7879;n. <b>V&iacute; d&#7909;:</b> S&ocirc;ng Tees g&#7847;n Barnard Castle.</p>
<div style="background:#f8fafc;border-left:3px solid #cbd5e1;padding:10px 15px;margin-top:15px;border-radius:4px;">
<p style="color:#64748b;margin:0;"><i><b>Real-world Example:</b> Below Middleton-in-Teesdale, the River Tees valley widens, forming distinctive meanders (e.g., near Barnard Castle) and productive agricultural floodplains.</i></p>
</div>
</div>

<div class="course-info" id="info-lower">
<h5 style="color:#0f172a;margin:0 0 10px 0;font-size:16px;">The lower course / H&#7841; l&#432;u</h5>
<ul style="color:#475569;line-height:1.6;margin:0;padding-left:20px;">
<li><b>Characteristics:</b> Very gentle (almost flat) gradient, widest and deepest channel. High discharge and smooth riverbed.</li>
<li><b>Main Process:</b> Deposition is the dominant process as the river loses energy near the sea. The river carries a lot of fine sediment (silt, clay).</li>
<li><b>Typical Features:</b> Large meanders, oxbow lakes, levees, wide floodplains, and estuaries/deltas at the river mouth.</li>
</ul>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:10px;margin-bottom:6px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7863;c &#273;i&#7875;m:</b> &#272;&#7897; d&#7889;c r&#7845;t nh&#7865; (g&#7847;n nh&#432; b&#7857;ng ph&#7859;ng), k&ecirc;nh r&#7897;ng v&agrave; s&acirc;u nh&#7845;t, l&#432;u l&#432;&#7907;ng l&#7899;n. <b>Qu&aacute; tr&igrave;nh ch&#7911; &#273;&#7841;o:</b> B&#7891;i t&#7909; (deposition) l&agrave; qu&aacute; tr&igrave;nh ch&iacute;nh khi s&ocirc;ng m&#7845;t n&#259;ng l&#432;&#7907;ng g&#7847;n bi&#7875;n. <b>&#272;&#7883;a h&igrave;nh ti&ecirc;u bi&#7875;u:</b> Kh&uacute;c cong l&#7899;n, h&#7891; m&oacute;ng ng&#7921;a, &#273;&ecirc; t&#7921; nhi&ecirc;n, &#273;&#7891;ng b&#7857;ng ng&#7853;p l&#7909;t r&#7897;ng l&#7899;n.</p>
<div style="background:#f8fafc;border-left:3px solid #cbd5e1;padding:10px 15px;margin-top:15px;border-radius:4px;">
<p style="color:#64748b;margin:0;"><i><b>Real-world Example:</b> The lower course of the River Tees meanders across a fertile clay plain to its estuary between Hartlepool and Redcar. It features mudflats, sandbanks, and oxbow lakes.</i></p>
</div>
</div>

<script>
  function showCourse(course){
    document.querySelectorAll('.course-info').forEach(el=>el.classList.remove('active'));
    document.getElementById('info-'+course).classList.add('active');
  }
</script>
</div>

<!-- Bradshaw arrows table -->
<div style="background:#ecfdf5;border:1px solid #a7f3d0;padding:25px;display:flex;flex-direction:column;gap:15px;margin-bottom:30px;">
<div style="display:flex;justify-content:space-between;font-weight:bold;color:#047857;font-size:16px;border-bottom:2px solid #6ee7b7;padding-bottom:10px;">
<span>UPSTREAM (Th&#432;&#7907;ng ngu&#7891;n)</span>
<span>DOWNSTREAM (H&#7841; l&#432;u / C&#7917;a s&ocirc;ng)</span>
</div>
<div style="background:#ffffff;padding:15px;border-radius:8px;">
<h4 style="color:#059669;margin:0 0 10px 0;">&#128200; T&#259;ng d&#7847;n v&#7873; ph&iacute;a h&#7841; l&#432;u (Increases Downstream):</h4>
<div style="display:flex;gap:10px;flex-wrap:wrap;">
<span style="background:#d1fae5;color:#065f46;padding:5px 12px;border-radius:20px;">Discharge (L&#432;u l&#432;&#7907;ng)</span>
<span style="background:#d1fae5;color:#065f46;padding:5px 12px;border-radius:20px;">Occupied Channel Width (Chi&#7873;u r&#7897;ng)</span>
<span style="background:#d1fae5;color:#065f46;padding:5px 12px;border-radius:20px;">Channel Depth (Chi&#7873;u s&acirc;u)</span>
<span style="background:#d1fae5;color:#065f46;padding:5px 12px;border-radius:20px;">Average Velocity (V&#7853;n t&#7889;c trung b&igrave;nh)</span>
<span style="background:#d1fae5;color:#065f46;padding:5px 12px;border-radius:20px;">Load Quantity (L&#432;&#7907;ng v&#7853;t li&#7879;u t&#7843;i)</span>
</div>
</div>
<div style="background:#ffffff;padding:15px;border-radius:8px;">
<h4 style="color:#dc2626;margin:0 0 10px 0;">&#128201; Gi&#7843;m d&#7847;n v&#7873; ph&iacute;a h&#7841; l&#432;u (Decreases Downstream):</h4>
<div style="display:flex;gap:10px;flex-wrap:wrap;">
<span style="background:#fee2e2;color:#991b1b;padding:5px 12px;border-radius:20px;">Load Particle Size (K&iacute;ch th&#432;&#7899;c h&#7841;t v&#7853;t li&#7879;u)</span>
<span style="background:#fee2e2;color:#991b1b;padding:5px 12px;border-radius:20px;">Channel Bed Roughness (&#272;&#7897; nh&aacute;m &#273;&aacute;y s&ocirc;ng)</span>
<span style="background:#fee2e2;color:#991b1b;padding:5px 12px;border-radius:20px;">Gradient / Slope (&#272;&#7897; d&#7889;c)</span>
</div>
</div>
</div>

<p style="color:#475569;line-height:1.6;">The River Tees is a reasonable exemplification of the Bradshaw model. The Tees is one of the major rivers in northeast England; it drains an area of about 1800 km&sup2;. The source of the Tees is at Cross Fell, on the eastern side of the Pennine Mountains.</p>
<div style="text-align:center;margin:20px 0;">
<img alt="Map of River Tees" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_real_fig1_9_map.jpeg" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:10px;margin-bottom:25px;">Figure 1.9: Map of the River Tees from source to mouth</p>
</div>

<div style="background:#f1f5f9;padding:15px;border-radius:8px;margin:20px 0;">
<h3 style="color:#0f172a;margin-top:0;font-size:18px;">River valleys and the long and cross profiles</h3>
<p style="color:#475569;margin-bottom:10px;">River valleys are formed by the continuous processes of flowing water over time. The long profile shows how gradient changes, while the cross profile refers to the cross-sectional view of the valley.</p>
<p style="color:#475569;margin-bottom:10px;">In the upper course, high elevation leads to vertical erosion, creating steep V-shaped valleys and interlocking spurs. In the middle course, lateral erosion becomes more significant. In the lower course, the valley is wide and flat, with sediments deposited to create fertile floodplains.</p>
</div>
</div>

<!-- ═══ SECTION 3 ═══ -->
<div style="margin-bottom:50px;">
<h2 style="color:#0f172a;border-bottom:2px solid #fbbf24;padding-bottom:10px;margin-bottom:25px;font-size:24px;">&#128260; 3. Drainage Basin &amp; The Water Cycle / V&ograve;ng Tu&#7847;n Ho&agrave;n N&#432;&#7899;c</h2>

<div style="background:#f1f5f9;padding:15px;border-radius:8px;margin:20px 0;">
<p style="color:#475569;margin:0;">The water cycle, or hydrological cycle, refers to the movement of water between the atmosphere, land and sea. It is a cycle because there is no start or end. Water falling as precipitation either flows over the land, flows through the land as groundwater, travels back into the atmosphere through evapotranspiration, or is stored on or within the land.</p>
</div>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;">V&ograve;ng tu&#7847;n ho&agrave;n n&#432;&#7899;c (hydrological cycle) l&agrave; s&#7921; v&#7853;n &#273;&#7897;ng li&ecirc;n t&#7909;c c&#7911;a n&#432;&#7899;c gi&#7919;a kh&iacute; quy&#7875;n, &#273;&#7845;t li&#7873;n v&agrave; bi&#7875;n. N&#432;&#7899;c sau khi r&#417;i xu&#7889;ng d&#432;&#7899;i d&#7841;ng m&#432;a c&oacute; th&#7875;: ch&#7843;y tr&ecirc;n b&#7873; m&#7863;t &#273;&#7845;t, th&#7845;m qua &#273;&#7845;t th&agrave;nh n&#432;&#7899;c ng&#7847;m, b&#7889;c h&#417;i tr&#7903; l&#7841;i kh&iacute; quy&#7875;n, ho&#7863;c &#273;&#432;&#7907;c tr&#7919; trong &#273;&#7845;t/th&#7921;c v&#7853;t/h&#7891;/s&ocirc;ng b&#259;ng.</p>

<!-- Water Cycle SVG (identical to Page 1) -->
<div style="background:#ffffff;border:1px solid #e2e8f0;padding:25px;box-shadow:0 4px 6px rgba(0,0,0,0.05);margin-top:40px;">
<h3 style="text-align:center;color:#0f172a;margin-top:0;font-size:18px;">The Water Cycle in a Drainage Basin / V&ograve;ng Tu&#7847;n Ho&agrave;n N&#432;&#7899;c</h3>
<p style="text-align:center;font-size:13px;color:#64748b;margin-bottom:25px;">Click on the processes to view their definitions. / Nh&#7845;p v&agrave;o c&aacute;c qu&aacute; tr&igrave;nh &#273;&#7875; xem &#273;&#7883;nh ngh&#297;a.</p>
<div style="position:relative;width:100%;max-width:420px;margin:0 auto;border-radius:8px;overflow:hidden;border:1px solid #cbd5e1;">
<svg height="auto" style="display:block;font-family:sans-serif;" viewBox="0 0 800 500" width="100%">
<defs>
<linearGradient id="skyGrad2" x1="0%" x2="0%" y1="0%" y2="100%">
<stop offset="0%" stop-color="#bae6fd"></stop>
<stop offset="100%" stop-color="#e0f2fe"></stop>
</linearGradient>
<linearGradient id="seaGrad2" x1="0%" x2="0%" y1="0%" y2="100%">
<stop offset="0%" stop-color="#3b82f6"></stop>
<stop offset="100%" stop-color="#1d4ed8"></stop>
</linearGradient>
<marker id="arrow-blue2" markerHeight="6" markerWidth="6" orient="auto-start-reverse" refX="8" refY="5" viewBox="0 0 10 10">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb"></path>
</marker>
<marker id="arrow-light2" markerHeight="6" markerWidth="6" orient="auto-start-reverse" refX="8" refY="5" viewBox="0 0 10 10">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#0ea5e9"></path>
</marker>
<marker id="arrow-orange2" markerHeight="6" markerWidth="6" orient="auto-start-reverse" refX="8" refY="5" viewBox="0 0 10 10">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"></path>
</marker>
<g id="cloud2">
<path d="M 50 40 Q 60 10 90 20 Q 120 -10 150 20 Q 180 10 190 40 Q 220 50 190 70 L 50 70 Q 20 50 50 40 Z" fill="#f1f5f9" filter="drop-shadow(0 5px 5px rgba(0,0,0,0.1))"></path>
</g>
<g id="tree2">
<rect fill="#78350f" height="20" width="6" x="12" y="30"></rect>
<path d="M 15 0 C 35 0 35 20 15 35 C -5 20 -5 0 15 0 Z" fill="#22c55e"></path>
</g>
</defs>
<rect fill="url(#skyGrad2)" height="350" onclick="showWaterCycleInfo('default')" style="cursor:pointer;" width="800" x="0" y="0"></rect>
<circle cx="700" cy="80" fill="#fde047" filter="drop-shadow(0 0 15px rgba(253,224,71,0.8))" r="40"></circle>
<use href="#cloud2" transform="scale(1.2)" x="100" y="40"></use>
<use href="#cloud2" opacity="0.8" transform="scale(0.8)" x="300" y="20"></use>
<path d="M 0 300 L 550 420 L 800 420 L 800 500 L 0 500 Z" fill="#94a3b8"></path>
<path d="M 0 200 L 500 350 L 550 420 L 0 300 Z" fill="#d4a373"></path>
<path d="M 0 190 L 500 340 L 500 350 L 0 200 Z" fill="#4ade80"></path>
<path d="M 500 350 Q 650 350 800 350 L 800 420 L 550 420 Z" fill="url(#seaGrad2)" opacity="0.9"></path>
<use href="#tree2" transform="scale(1.5)" x="150" y="210"></use>
<use href="#tree2" transform="scale(1.3)" x="250" y="250"></use>
<use href="#tree2" transform="scale(1.6)" x="350" y="285"></use>
<!-- Precipitation -->
<g class="process-group" onclick="showWaterCycleInfo('precipitation')">
<line class="anim-dash" stroke="#2563eb" stroke-dasharray="6,4" stroke-width="3" x1="160" x2="160" y1="120" y2="180"></line>
<line class="anim-dash" stroke="#2563eb" stroke-dasharray="6,4" stroke-width="3" x1="200" x2="200" y1="120" y2="200"></line>
<line class="anim-dash" stroke="#2563eb" stroke-dasharray="6,4" stroke-width="3" x1="240" x2="240" y1="120" y2="220"></line>
<rect fill="#2563eb" height="30" opacity="0.9" rx="5" width="110" x="145" y="60"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="200" y="80">Precipitation</text>
</g>
<!-- Evaporation -->
<g class="process-group" onclick="showWaterCycleInfo('evaporation')">
<path class="anim-up" d="M 600 340 Q 610 320 600 300 Q 590 280 600 260" fill="none" marker-end="url(#arrow-orange2)" stroke="#f59e0b" stroke-width="3"></path>
<path class="anim-up" d="M 650 340 Q 660 320 650 300 Q 640 280 650 260" fill="none" marker-end="url(#arrow-orange2)" stroke="#f59e0b" stroke-width="3"></path>
<rect fill="#f59e0b" height="30" opacity="0.9" rx="5" width="100" x="580" y="210"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="630" y="230">Evaporation</text>
</g>
<!-- Transpiration -->
<g class="process-group" onclick="showWaterCycleInfo('transpiration')">
<path class="anim-up" d="M 390 280 Q 400 260 390 240" fill="none" marker-end="url(#arrow-orange2)" stroke="#f59e0b" stroke-width="3"></path>
<path class="anim-up" d="M 290 240 Q 300 220 290 200" fill="none" marker-end="url(#arrow-orange2)" stroke="#f59e0b" stroke-width="3"></path>
<rect fill="#f59e0b" height="30" opacity="0.9" rx="5" width="110" x="290" y="160"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="345" y="180">Transpiration</text>
</g>
<!-- Evapotranspiration -->
<g class="process-group" onclick="showWaterCycleInfo('evapotranspiration')">
<path d="M 410 175 L 420 175 L 420 145 L 670 145 L 670 225 L 680 225" fill="none" stroke="#d97706" stroke-dasharray="4,4" stroke-width="2"></path>
<rect fill="#b45309" height="30" opacity="0.9" rx="5" width="145" x="475" y="130"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="547" y="150">Evapotranspiration</text>
</g>
<!-- Interception -->
<g class="process-group" onclick="showWaterCycleInfo('interception')">
<circle cx="255" cy="255" fill="none" r="25" stroke="#ef4444" stroke-dasharray="4,4" stroke-width="2"></circle>
<line stroke="#ef4444" stroke-width="2" x1="255" x2="255" y1="230" y2="190"></line>
<rect fill="#ef4444" height="30" opacity="0.9" rx="5" width="100" x="180" y="160"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="230" y="180">Interception</text>
</g>
<!-- Overland Flow -->
<g class="process-group" onclick="showWaterCycleInfo('overland')">
<path class="anim-flow" d="M 330 310 L 450 345" fill="none" marker-end="url(#arrow-light2)" stroke="#0ea5e9" stroke-width="4"></path>
<rect fill="#0ea5e9" height="30" opacity="0.9" rx="5" width="115" x="340" y="315"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="397" y="335">Overland Flow</text>
</g>
<!-- Infiltration -->
<g class="process-group" onclick="showWaterCycleInfo('infiltration')">
<line class="anim-down" marker-end="url(#arrow-blue2)" stroke="#2563eb" stroke-width="3" x1="120" x2="120" y1="230" y2="280"></line>
<line class="anim-down" marker-end="url(#arrow-blue2)" stroke="#2563eb" stroke-width="3" x1="220" x2="220" y1="260" y2="310"></line>
<rect fill="#2563eb" height="30" opacity="0.9" rx="5" width="90" x="130" y="270"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="175" y="290">Infiltration</text>
</g>
<!-- Throughflow -->
<g class="process-group" onclick="showWaterCycleInfo('throughflow')">
<path class="anim-flow" d="M 240 330 L 420 380" fill="none" marker-end="url(#arrow-blue2)" stroke="#2563eb" stroke-dasharray="8,4" stroke-width="4"></path>
<rect fill="#1d4ed8" height="30" opacity="0.9" rx="5" width="105" x="250" y="340"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="302" y="360">Throughflow</text>
</g>
<!-- Percolation -->
<g class="process-group" onclick="showWaterCycleInfo('percolation')">
<line class="anim-down" marker-end="url(#arrow-blue2)" stroke="#1e3a8a" stroke-width="3" x1="150" x2="150" y1="330" y2="390"></line>
<line class="anim-down" marker-end="url(#arrow-blue2)" stroke="#1e3a8a" stroke-width="3" x1="300" x2="300" y1="370" y2="430"></line>
<rect fill="#1e3a8a" height="30" opacity="0.9" rx="5" width="95" x="140" y="390"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="187" y="410">Percolation</text>
</g>
<!-- Groundwater Flow -->
<g class="process-group" onclick="showWaterCycleInfo('groundwater')">
<path class="anim-flow" d="M 260 430 L 500 460" fill="none" marker-end="url(#arrow-blue2)" stroke="#1e3a8a" stroke-dasharray="10,5" stroke-width="5"></path>
<rect fill="#0f172a" height="30" opacity="0.9" rx="5" width="145" x="300" y="455"></rect>
<text fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle" x="372" y="475">Groundwater Flow</text>
</g>
</svg>
<style>
  .process-group{cursor:pointer;transition:all 0.3s ease;}
  .process-group:hover rect{filter:brightness(1.2);}
  @keyframes dash{to{stroke-dashoffset:-20;}}
  @keyframes flow{to{stroke-dashoffset:-24;}}
  @keyframes wup{0%{transform:translateY(0);}50%{transform:translateY(-3px);}100%{transform:translateY(0);}}
  @keyframes wdown{0%{transform:translateY(0);}50%{transform:translateY(3px);}100%{transform:translateY(0);}}
  .process-group:hover .anim-dash{animation:dash 0.8s linear infinite;}
  .process-group:hover .anim-flow{animation:flow 0.8s linear infinite;}
  .process-group:hover .anim-up{animation:wup 0.8s ease infinite;}
  .process-group:hover .anim-down{animation:wdown 0.8s ease infinite;}
</style>
</div>
<style>
  .water-info-panel{display:none;margin-top:20px;animation:fadeIn 0.3s ease;}
  .water-info-panel.active{display:block;}
</style>
<script>
  function showWaterCycleInfo(panelId){
    document.querySelectorAll('.water-info-panel').forEach(el=>el.classList.remove('active'));
    document.getElementById('water-info-'+panelId).classList.add('active');
  }
</script>

<!-- Water cycle panels -->
<div class="water-info-panel active" id="water-info-default">
<div style="background:#ffffff;border-left:4px solid #94a3b8;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);text-align:center;">
<p style="color:#64748b;margin:0;"><i>Click on any process on the map to view its detailed definition. / Nh&#7845;p v&agrave;o b&#7845;t k&#7923; qu&aacute; tr&igrave;nh n&agrave;o tr&ecirc;n s&#417; &#273;&#7891; &#273;&#7875; xem &#273;&#7883;nh ngh&#297;a chi ti&#7871;t.</i></p>
</div>
</div>

<div class="water-info-panel" id="water-info-precipitation">
<div style="background:#ffffff;border-left:4px solid #2563eb;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#1d4ed8;margin-top:0;font-size:18px;">Precipitation / Gi&aacute;ng Th&#7911;y</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Input:</b> All forms of condensed water vapor falling from the atmosphere to the Earth&#x27;s surface, including rain, snow, hail, etc.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7847;u v&agrave;o (Input):</b> T&#7845;t c&#7843; c&aacute;c d&#7841;ng n&#432;&#7899;c ng&#432;ng t&#7909; r&#417;i t&#7915; kh&iacute; quy&#7875;n xu&#7889;ng b&#7873; m&#7863;t Tr&aacute;i &#272;&#7845;t, bao g&#7891;m m&#432;a, tuy&#7871;t, m&#432;a &#273;&aacute;, v.v.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-evaporation">
<div style="background:#ffffff;border-left:4px solid #f59e0b;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#d97706;margin-top:0;font-size:18px;">Evaporation / B&#7889;c H&#417;i</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Output:</b> The process by which liquid water from surfaces (rivers, lakes, oceans) turns into water vapor and enters the atmosphere due to heat from the Sun.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7847;u ra (Output):</b> Qu&aacute; tr&igrave;nh n&#432;&#7899;c l&#7887;ng t&#7915; b&#7873; m&#7863;t (s&ocirc;ng, h&#7891;, &#273;&#7841;i d&#432;&#417;ng) bi&#7871;n th&agrave;nh h&#417;i n&#432;&#7899;c v&agrave; v&agrave;o kh&iacute; quy&#7875;n nh&#7901; nhi&#7879;t t&#7915; M&#7863;t Tr&#7901;i.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-transpiration">
<div style="background:#ffffff;border-left:4px solid #f59e0b;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#d97706;margin-top:0;font-size:18px;">Transpiration / Tho&aacute;t H&#417;i N&#432;&#7899;c</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Output:</b> The process by which water is released into the atmosphere as vapor through the stomata of plant leaves.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7847;u ra (Output):</b> Qu&aacute; tr&igrave;nh n&#432;&#7899;c &#273;&#432;&#7907;c th&#7921;c v&#7853;t th&#7843;i ra kh&iacute; quy&#7875;n d&#432;&#7899;i d&#7841;ng h&#417;i qua c&aacute;c l&#7895; kh&iacute; kh&#7893;ng c&#7911;a l&aacute;.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-evapotranspiration">
<div style="background:#ffffff;border-left:4px solid #b45309;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#92400e;margin-top:0;font-size:18px;">Evapotranspiration / T&#7893;ng B&#7889;c Tho&aacute;t H&#417;i</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Output:</b> The combined loss of water to the atmosphere through evaporation from surfaces and transpiration from plants.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>&#272;&#7847;u ra (Output):</b> T&#7893;ng l&#432;&#7907;ng n&#432;&#7899;c m&#7845;t &#273;i v&agrave;o kh&iacute; quy&#7875;n qua b&#7889;c h&#417;i b&#7873; m&#7863;t v&agrave; tho&aacute;t h&#417;i n&#432;&#7899;c t&#7915; th&#7921;c v&#7853;t.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-interception">
<div style="background:#ffffff;border-left:4px solid #ef4444;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#b91c1c;margin-top:0;font-size:18px;">Interception / Gi&#7919; L&#7841;i</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Store / Transfer:</b> Precipitation that is caught by plant leaves and branches before reaching the ground. This water often evaporates back into the atmosphere.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Tr&#7919;/Chuy&#7875;n:</b> L&#432;&#7907;ng m&#432;a b&#7883; l&aacute; v&agrave; c&agrave;nh c&acirc;y gi&#7919; l&#7841;i tr&#432;&#7899;c khi ch&#7841;m &#273;&#7845;t. L&#432;&#7907;ng n&#432;&#7899;c n&agrave;y th&#432;&#7901;ng b&#7889;c h&#417;i tr&#7903; l&#7841;i kh&iacute; quy&#7875;n.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-overland">
<div style="background:#ffffff;border-left:4px solid #0ea5e9;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#0369a1;margin-top:0;font-size:18px;">Overland Flow / D&ograve;ng Ch&#7843;y B&#7873; M&#7863;t</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Transfer:</b> Water flowing rapidly over the ground surface when the soil is saturated (cannot absorb more) or when rainfall is intense.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Chuy&#7875;n (Transfer):</b> N&#432;&#7899;c ch&#7843;y nhanh tr&ecirc;n b&#7873; m&#7863;t &#273;&#7845;t khi &#273;&#7845;t &#273;&atilde; b&atilde;o h&ograve;a (kh&ocirc;ng th&#7845;m th&ecirc;m &#273;&#432;&#7907;c) ho&#7863;c khi m&#432;a qu&aacute; l&#7899;n.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-infiltration">
<div style="background:#ffffff;border-left:4px solid #2563eb;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#1d4ed8;margin-top:0;font-size:18px;">Infiltration / Th&#7845;m</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Transfer:</b> The process by which water on the ground surface enters and soaks into the shallow soil layer.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Chuy&#7875;n (Transfer):</b> Qu&aacute; tr&igrave;nh n&#432;&#7899;c tr&ecirc;n b&#7873; m&#7863;t th&#7845;m v&agrave;o l&#7899;p &#273;&#7845;t n&ocirc;ng b&ecirc;n d&#432;&#7899;i.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-throughflow">
<div style="background:#ffffff;border-left:4px solid #1d4ed8;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#1e3a8a;margin-top:0;font-size:18px;">Throughflow / D&ograve;ng Ch&#7843;y Trong &#272;&#7845;t</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Transfer:</b> The lateral (sideways) movement of water within the soil layer (above the bedrock) flowing towards a river, lake, or sea.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Chuy&#7875;n (Transfer):</b> S&#7921; di chuy&#7875;n ngang c&#7911;a n&#432;&#7899;c trong l&#7899;p &#273;&#7845;t (tr&ecirc;n n&#7873;n &#273;&aacute; g&#7889;c) v&#7873; ph&iacute;a s&ocirc;ng, h&#7891; ho&#7863;c bi&#7875;n.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-percolation">
<div style="background:#ffffff;border-left:4px solid #1e3a8a;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#172554;margin-top:0;font-size:18px;">Percolation / Th&#7845;m S&acirc;u</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Transfer:</b> The downward movement of water from the soil layer deep into the cracks and joints of the underlying permeable rock.</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Chuy&#7875;n (Transfer):</b> S&#7921; di chuy&#7875;n c&#7911;a n&#432;&#7899;c t&#7915; l&#7899;p &#273;&#7845;t xu&#7889;ng s&acirc;u v&agrave;o c&aacute;c khe n&#7913;t c&#7911;a &#273;&aacute; th&#7845;m n&#432;&#7899;c b&ecirc;n d&#432;&#7899;i.</p>
</div>
</div>

<div class="water-info-panel" id="water-info-groundwater">
<div style="background:#ffffff;border-left:4px solid #0f172a;padding:20px;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.05);">
<h3 style="color:#000000;margin-top:0;font-size:18px;">Groundwater Flow / D&ograve;ng Ch&#7843;y Ng&#7847;m</h3>
<p style="margin:0;color:#475569;line-height:1.6;"><b>Transfer:</b> The very slow movement of water deep underground within the bedrock (aquifer).</p>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:8px;margin-bottom:0;border-left:3px solid #cbd5e1;padding-left:12px;"><b>Chuy&#7875;n (Transfer):</b> S&#7921; di chuy&#7875;n r&#7845;t ch&#7853;m c&#7911;a n&#432;&#7899;c trong l&ograve;ng &#273;&#7845;t, trong t&#7847;ng ch&#7913;a n&#432;&#7899;c (aquifer).</p>
</div>
</div>
</div>
</div>

<!-- ═══ SECTION 4 ═══ -->
<div style="margin-bottom:50px;">
<h2 style="color:#0f172a;border-bottom:2px solid #ef4444;padding-bottom:10px;margin-bottom:25px;font-size:24px;">&#128296; 4. Processes Operating Within a River / Qu&aacute; Tr&igrave;nh Ho&#7841;t &#272;&#7897;ng Trong S&ocirc;ng</h2>

<!-- River Processes SVG flowchart -->
<div style="background:#ffffff;border:1px solid #e2e8f0;padding:20px;box-shadow:0 4px 6px rgba(0,0,0,0.05);margin-bottom:20px;">
<h4 style="text-align:center;color:#0f172a;margin-top:0;font-size:20px;">River processes working together / C&aacute;c qu&aacute; tr&igrave;nh s&ocirc;ng ph&#7889;i h&#7907;p</h4>
<p style="text-align:center;font-size:14px;color:#475569;margin-bottom:20px;">Erosion wears away the landscape and provides material; transportation carries it downstream; deposition settles it in new areas.<br/><br/><b>Click on each process below to view its details. / Nh&#7845;p v&agrave;o t&#7915;ng qu&aacute; tr&igrave;nh &#273;&#7875; xem chi ti&#7871;t.</b></p>
<div style="position:relative;width:100%;max-width:650px;margin:0 auto;">
<svg style="width:100%;height:auto;font-family:sans-serif;" viewBox="0 0 650 300">
<defs>
<marker id="arrowProcess2" markerHeight="6" markerWidth="6" orient="auto" refX="9" refY="5" viewBox="0 0 10 10">
<path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"></path>
</marker>
</defs>
<!-- Erosion box -->
<g class="process-group" onclick="showProcess('erosion')" style="cursor:pointer;">
<rect fill="#d1f2eb" height="90" rx="12" stroke="#10b981" stroke-width="2" width="180" x="50" y="30"></rect>
<text fill="#065f46" font-size="18" font-weight="bold" text-anchor="middle" x="140" y="80">Erosion</text>
<circle cx="260" cy="40" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="275" y="45">Abrasion</text>
<circle cx="260" cy="65" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="275" y="70">Hydraulic Action</text>
<circle cx="260" cy="90" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="275" y="95">Attrition</text>
<circle cx="260" cy="115" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="275" y="120">Solution</text>
</g>
<path d="M 140 120 L 140 175 L 260 175" fill="none" marker-end="url(#arrowProcess2)" stroke="#64748b" stroke-width="2"></path>
<!-- Transportation box -->
<g class="process-group" onclick="showProcess('transportation')" style="cursor:pointer;">
<rect fill="#d1f2eb" height="90" rx="12" stroke="#10b981" stroke-width="2" width="180" x="270" y="130"></rect>
<text fill="#065f46" font-size="18" font-weight="bold" text-anchor="middle" x="360" y="185">Transportation</text>
<circle cx="480" cy="145" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="495" y="150">Traction</text>
<circle cx="480" cy="170" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="495" y="175">Saltation</text>
<circle cx="480" cy="190" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="495" y="195">Suspension</text>
<circle cx="480" cy="215" fill="#475569" r="4"></circle>
<text fill="#334155" font-size="15" x="495" y="220">Solution</text>
</g>
<path d="M 360 220 L 360 275 L 470 275" fill="none" marker-end="url(#arrowProcess2)" stroke="#64748b" stroke-width="2"></path>
<!-- Deposition box -->
<g class="process-group" onclick="showProcess('deposition')" style="cursor:pointer;">
<rect fill="#d1f2eb" height="70" rx="12" stroke="#10b981" stroke-width="2" width="160" x="480" y="230"></rect>
<text fill="#065f46" font-size="18" font-weight="bold" text-anchor="middle" x="560" y="270">Deposition</text>
</g>
</svg>
</div>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:15px;margin-bottom:0;"><span style="color:#ef4444;font-style:normal;">&#9650;</span> Figure 1.4 River processes work together</p>
<style>
  .process-group rect{transition:all 0.2s;}
  .process-group:hover rect{filter:brightness(0.95);stroke-width:3px;}
  .proc-info{display:none;margin-top:20px;padding:20px;border-radius:8px;border-left:4px solid #10b981;background:#f8fafc;animation:fadeIn 0.3s ease;}
  .proc-info.active{display:block;}
</style>
<script>
  function showProcess(proc){
    document.querySelectorAll('.proc-info').forEach(el=>el.classList.remove('active'));
    document.getElementById('proc-'+proc).classList.add('active');
  }
</script>

<!-- Erosion panel -->
<div class="proc-info active" id="proc-erosion">
<h5 style="color:#0f172a;margin:0 0 10px 0;font-size:18px;">1. Erosion / X&oacute;i M&ograve;n</h5>
<p style="margin:0 0 10px 0;color:#475569;line-height:1.6;">The rate of river erosion is influenced by the river&#x27;s gradient, the size and type of transported sediments, and the geology (softer rocks erode more quickly than harder rocks).</p>
<ul style="margin:0;padding-left:20px;color:#475569;line-height:1.6;">
<li><b style="color:#b91c1c;">Hydraulic Action:</b> The force of the river water colliding with rocks breaks rock particles away from the river channel.</li>
<li><b style="color:#b91c1c;">Abrasion:</b> Rocks picked up by the river scrape and rub against the channel, wearing it away.</li>
<li><b style="color:#b91c1c;">Attrition:</b> Rocks picked up by the river smash into each other and break into smaller, smoother, rounder particles.</li>
<li><b style="color:#b91c1c;">Solution / Corrosion:</b> River water dissolves some types of rock, e.g. chalk and limestone.</li>
</ul>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:10px;margin-bottom:6px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>S&#7913;c n&#432;&#7899;c (Hydraulic action):</b> S&#7913;c &eacute;p c&#7911;a n&#432;&#7899;c v&agrave; kh&ocirc;ng kh&iacute; b&#7883; cu&#7889;n v&agrave;o c&aacute;c v&#7871;t n&#7913;t c&#7911;a &#273;&aacute; b&#7901; s&ocirc;ng l&agrave;m &#273;&aacute; n&#7913;t v&#7905; ra. &#272;&acirc;y l&agrave; d&#7841;ng x&oacute;i m&ograve;n m&#7841;nh nh&#7845;t. | <b>M&agrave;i m&ograve;n (Abrasion):</b> &#272;&aacute; cu&#7897;i v&agrave; c&aacute;t do s&ocirc;ng mang theo c&#7885; x&aacute;t v&agrave;o &#273;&aacute;y v&agrave; b&#7901; s&ocirc;ng nh&#432; gi&#7845;y nh&aacute;m. | <b>Va ch&#7841;m (Attrition):</b> &#272;&aacute; cu&#7897;i va &#273;&#7853;p v&agrave;o nhau, v&#7905; th&agrave;nh c&aacute;c m&#7843;nh ng&agrave;y c&agrave;ng nh&#7887; v&agrave; tr&ograve;n h&#417;n. | <b>H&ograve;a tan (Solution):</b> N&#432;&#7899;c s&ocirc;ng h&ograve;a tan c&aacute;c kho&aacute;ng ch&#7845;t trong &#273;&aacute; (&#273;&#7863;c bi&#7879;t l&agrave; &#273;&aacute; v&ocirc;i).</p>
<div style="text-align:center;margin-top:20px;">
<img alt="Types of river erosion" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_erosion.png" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:10px;"><span style="color:#ef4444;font-style:normal;">&#9650;</span> Figure 1.1 Types of river erosion</p>
</div>
</div>

<!-- Transportation panel -->
<div class="proc-info" id="proc-transportation">
<h5 style="color:#0f172a;margin:0 0 10px 0;font-size:18px;">2. Transportation / V&#7853;n Chuy&#7875;n</h5>
<p style="margin:0 0 10px 0;color:#475569;line-height:1.6;">Transportation is the process by which rivers move eroded sediments and materials downstream.</p>
<ul style="margin:0;padding-left:20px;color:#475569;line-height:1.6;">
<li><b style="color:#1d4ed8;">Traction:</b> Large boulders rolling along the river bed. Requires a lot of energy.</li>
<li><b style="color:#1d4ed8;">Saltation:</b> Smaller pebbles bouncing along the bed.</li>
<li><b style="color:#1d4ed8;">Suspension:</b> Fine silt and clay carried along in the water flow. Requires little energy.</li>
<li><b style="color:#1d4ed8;">Solution:</b> Minerals dissolved in water. Can be carried over great distances.</li>
</ul>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:10px;margin-bottom:6px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>K&eacute;o l&ecirc; (Traction):</b> C&aacute;c &#273;&aacute; t&#7843;ng l&#7899;n nh&#7845;t b&#7883; k&eacute;o l&ecirc; d&#7885;c theo &#273;&aacute;y s&ocirc;ng b&#7903;i l&#7921;c d&ograve;ng ch&#7843;y. | <b>Nh&#7843;y c&oacute;c (Saltation):</b> C&aacute;c h&#7841;t cu&#7897;i v&agrave; c&aacute;t nh&#7843;y t&#7915;ng b&#432;&#7899;c theo &#273;&aacute;y s&ocirc;ng. | <b>L&#417; l&#7917;ng (Suspension):</b> H&#7841;t m&#7883;n (b&ugrave;n, s&eacute;t) l&#417; l&#7917;ng trong d&ograve;ng n&#432;&#7899;c v&agrave; &#273;&#432;&#7907;c v&#7853;n chuy&#7875;n &#273;i xa. | <b>H&ograve;a tan (Solution):</b> Kho&aacute;ng ch&#7845;t h&ograve;a tan &#273;&#432;&#7907;c v&#7853;n chuy&#7875;n v&ocirc; h&igrave;nh trong n&#432;&#7899;c.</p>
<div style="text-align:center;margin-top:20px;">
<img alt="Processes of river transportation" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_transport.png" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:10px;"><span style="color:#ef4444;font-style:normal;">&#9650;</span> Figure 1.2 The processes of river transportation</p>
</div>
</div>

<!-- Deposition panel -->
<div class="proc-info" id="proc-deposition">
<h5 style="color:#0f172a;margin:0 0 10px 0;font-size:18px;">3. Deposition / B&#7891;i T&#7909;</h5>
<p style="margin:0 0 10px 0;color:#475569;line-height:1.6;">Occurs when a river loses energy and drops its load. A river deposits larger and heavier material first. The finest sediment is called alluvium.</p>
<p style="margin:0 0 10px 0;color:#475569;line-height:1.6;">Usually happens:</p>
<ul style="margin:0;padding-left:20px;color:#475569;line-height:1.6;">
<li>Where the river enters a lake or sea.</li>
<li>On the inside of a meander.</li>
<li>When river flow decreases (e.g., during a drought) or floods over large areas.</li>
<li>Where the gradient becomes flatter.</li>
</ul>
<p style="color:#64748b;font-style:italic;font-size:15px;margin-top:10px;margin-bottom:6px;border-left:3px solid #cbd5e1;padding-left:12px;"><b>B&#7891;i t&#7909;</b> x&#7843;y ra khi s&ocirc;ng m&#7845;t n&#259;ng l&#432;&#7907;ng v&agrave; kh&ocirc;ng c&ograve;n &#273;&#7911; s&#7913;c mang t&#7843;i l&#432;&#7907;ng. Nguy&ecirc;n nh&acirc;n: s&ocirc;ng ch&#7843;y v&agrave;o v&ugrave;ng n&#432;&#7899;c &#273;&#7913;ng y&ecirc;n (h&#7891;, bi&#7875;n), l&#432;u l&#432;&#7907;ng gi&#7843;m (m&ugrave;a kh&ocirc;), &#273;&#7897; d&#7889;c gi&#7843;m m&#7841;nh. V&#7853;t li&#7879;u n&#7863;ng nh&#7845;t &#273;&#7885;ng xu&#7889;ng tr&#432;&#7899;c, v&#7853;t li&#7879;u m&#7883;n (b&ugrave;n, s&eacute;t) &#273;i xa nh&#7845;t.</p>
<div style="text-align:center;margin-top:20px;">
<img alt="River deposition" src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_deposition.png" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="text-align:center;font-size:13px;color:#94a3b8;font-style:italic;margin-top:10px;"><span style="color:#ef4444;font-style:normal;">&#9650;</span> Figure 1.3 The river deposits larger pebbles and stones first</p>
</div>
</div>
</div>
</div>

</div>"""

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
