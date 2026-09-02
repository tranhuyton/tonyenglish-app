import requests

SUPABASE_URL = 'https://ubkvzgwespfvrlpjuxkp.supabase.co'
KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw'
PAGE_ID = 'ae8dd7f6-0215-45c3-bb94-f60f373c170f'
IMG = 'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/'
VI = 'style="color:#64748b;font-style:italic;font-size:15px;margin-top:6px;margin-bottom:16px;border-left:3px solid #cbd5e1;padding-left:12px;"'

html = f"""<div style="font-family:'Inter',sans-serif;max-width:900px;margin:0 auto;color:#1e293b;line-height:1.6;font-size:16px;">
<div style="text-align:center;margin-bottom:40px;">
<h1 style="color:#0369a1;font-size:30px;margin-bottom:10px;border-bottom:3px solid #38bdf8;display:inline-block;padding-bottom:10px;">🏔️ 2.2 Coastal Landforms<br/><span style="font-size:20px;color:#0ea5e9;font-weight:normal;">Đ&#7883;a H&igrave;nh B&#7901; Bi&#7875;n</span></h1>
<p style="color:#64748b;font-size:16px;">Erosional and depositional features created by coastal processes</p>
<p {VI}>C&aacute;c &dagger;&#7883;a h&igrave;nh x&oacute;i m&ograve;n v&agrave; b&#7891;i t&#7909; &dagger;&#432;&#7907;c t&#7841;o ra b&#7903;i c&aacute;c qu&aacute; tr&igrave;nh b&#7901; bi&#7875;n</p>
</div>

<!-- Section 1: Concordant/Discordant -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">🗺️ 1. Coastline Types / Lo&#7841;i &Dagger;&#432;&#7901;ng B&#7901; Bi&#7875;n</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
<div style="background:#fef3c7;border-left:4px solid #f59e0b;padding:16px;border-radius:8px;">
<h3 style="color:#92400e;margin-bottom:8px;">⛰️ Discordant Coastline</h3>
<p style="color:#475569;font-size:14px;">Alternating hard and soft rock bands perpendicular to coast → headlands (hard) and bays (soft). Wave refraction focuses energy on headlands. Example: Jurassic Coast, Dorset, UK.</p>
<p {VI}><strong>B&#7901; bi&#7875;n kh&ocirc;ng thu&#7847;n nh&#7845;t:</strong> C&aacute;c d&#7843;i &dagger;&#225; c&#7913;ng v&agrave; m&#7873;m xen k&#7869; vu&ocirc;ng g&oacute;c v&#7899;i b&#7901; &rarr; m&#361;i &dagger;&#7845;t (&dagger;&#225; c&#7913;ng) v&agrave; v&#7883;nh (&dagger;&#225; m&#7873;m). S&oacute;ng kh&uacute;c x&#7841; t&#7853;p trung n&#259;ng l&#432;&#7907;ng v&agrave;o m&#361;i &dagger;&#7845;t.</p>
</div>
<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:16px;border-radius:8px;">
<h3 style="color:#15803d;margin-bottom:8px;">🏝️ Concordant Coastline</h3>
<p style="color:#475569;font-size:14px;">Rock bands parallel to coast → uniform coastline. Example: Dalmatian coast, Croatia.</p>
<p {VI}><strong>B&#7901; bi&#7875;n thu&#7847;n nh&#7845;t:</strong> C&aacute;c d&#7843;i &dagger;&#225; song song v&#7899;i b&#7901; &rarr; b&#7901; bi&#7875;n &dagger;&#7891;ng &dagger;&#7873;u h&#417;n. V&iacute; d&#7909;: B&#7901; bi&#7875;n Dalmatia, Croatia.</p>
</div>
</div>
<img src="{IMG}2_2_fig29.png" alt="Headlands and bays" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.9 Headlands and bays diagram</p>
<img src="{IMG}2_2_fig210.png" alt="Portugal coast" style="max-width:420px;height:auto;display:block;margin:0 auto;margin-top:16px;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.10 Headlands and bays at Praia de Rocha, Portugal</p>
</div>

<!-- Section 2: Erosional Landforms -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⚡ 2. Erosional Landforms / Đ&#7883;a H&igrave;nh X&oacute;i M&ograve;n</h2>

<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🏔️ Cliffs &amp; Wave-cut Platforms / V&aacute;ch Đ&aacute; v&agrave; B&#7853;c S&oacute;ng</h3>
<p style="color:#475569;font-size:15px;">Waves attack cliff base via hydraulic action and corrasion → <strong>wave-cut notch</strong> → cliff collapses → cliff retreats leaving a <strong>wave-cut platform</strong> (flat rocky shelf, exposed at low tide).</p>
<p {VI}>S&oacute;ng t&#7845;n c&ocirc;ng ch&acirc;n v&aacute;ch &dagger;&#225; b&#7857;ng l&#7921;c th&#7911;y &dagger;&#7897;ng v&agrave; m&agrave;i m&ograve;n &rarr; <strong>kh&iacute;a s&oacute;ng (wave-cut notch)</strong> &rarr; v&aacute;ch &dagger;&#225; s&#7909;p &dagger;&#7893; &rarr; v&aacute;ch l&ugrave;i v&agrave;o trong &dagger;&#7875; l&#7841;i <strong>b&#7853;c s&oacute;ng</strong> (b&#7873; m&#7863;t &dagger;&#225; b&#7857;ng ph&#7859;ng l&#7897; ra khi tri&#7873;u xu&#7889;ng th&#7845;p).</p>
</div>

<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🕳️ Caves, Arches, Stacks, Stumps / Hang, C&#7893;ng, C&#7897;t, G&#7889;c Đ&aacute;</h3>
<p style="color:#475569;font-size:15px;">Hydraulic action exploits weaknesses in headland → <strong>cave</strong> → caves meet from both sides → <strong>arch</strong> → arch roof collapses → <strong>stack</strong> → eroded further → <strong>stump</strong>.</p>
<p {VI}>L&#7921;c th&#7911;y &dagger;&#7897;ng khai th&aacute;c &dagger;i&#7875;m y&#7871;u c&#7911;a m&#361;i &dagger;&#7845;t &rarr; <strong>hang bi&#7875;n</strong> &rarr; hai hang th&ocirc;ng nhau &rarr; <strong>c&#7895;ng &dagger;&#225;</strong> &rarr; m&aacute;i s&#7909;p &rarr; <strong>c&#7897;t &dagger;&#225;</strong> c&ocirc; l&#7853;p &rarr; b&#7883; x&oacute;i m&ograve;n ti&#7871;p &rarr; <strong>g&#7889;c c&#7897;t</strong> (stump).</p>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px;">
<div>
<img src="{IMG}2_2_fig211.png" alt="Cave arch stack" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.11 Cave &rarr; Arch &rarr; Stack formation</p>
</div>
<div>
<img src="{IMG}2_2_fig212.png" alt="Durdle Door" style="max-width:420px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.12 Durdle Door arch, Dorset, UK</p>
</div>
</div>
</div>

<!-- Section 3: Depositional -->
<div style="margin-bottom:44px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:18px;font-size:22px;">⬇️ 3. Depositional Landforms / Đ&#7883;a H&igrave;nh B&#7891;i T&#7909;</h2>

<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:16px;margin-bottom:16px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🌊 Spits &amp; Bars / M&#361;i C&aacute;t v&agrave; Đ&ecirc; C&aacute;t</h3>
<p style="color:#475569;font-size:15px;">A <strong>spit</strong> is a ridge of sand/shingle linked to land at one end, extending across a bay/estuary. Longshore drift builds it up; wave refraction curves the tip (<strong>recurved end</strong>). Salt marsh forms behind. A <strong>bar</strong> forms when a spit seals a bay completely, cutting off a lagoon. A <strong>tombolo</strong> connects mainland to an island.</p>
<p {VI}><strong>M&#361;i c&aacute;t (Spit):</strong> D&#7843;i c&aacute;t/s&#7887;i n&#7889;i v&#7899;i &dagger;&#7845;t li&#7873;n m&#7897;t &dagger;&#7847;u, k&eacute;o d&agrave;i qua v&#7883;nh/c&#7917;a s&ocirc;ng. D&ograve;ng ch&#7843;y ven b&#7901; b&#7891;i t&#7909; n&oacute;; s&oacute;ng kh&uacute;c x&#7841; t&#7841;o &dagger;&#7847;u cong (m&oacute;c c&acirc;u). \u0110&#7847;m l&#7847;y m&#7863;n h&igrave;nh th&agrave;nh ph&iacute;a sau. <strong>Đ&ecirc; c&aacute;t (Bar):</strong> M&#361;i c&aacute;t k&eacute;o d&agrave;i qua to&agrave;n b&#7897; v&#7883;nh &rarr; t&#7841;o h&#7891; lagoon ph&iacute;a sau. <strong>C&#7847;u c&aacute;t n&#7889;i &dagger;&#7843;o (Tombolo):</strong> N&#7889;i &dagger;&#7845;t li&#7873;n v&#7899;i &dagger;&#7843;o.</p>
</div>

<img src="{IMG}2_2_fig221.png" alt="Spit formation" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.21 Spit formation — longshore drift, recurved end, salt marsh</p>

<div style="background:#f8fafc;border:2px solid #e2e8f0;border-radius:10px;padding:16px;margin-top:20px;margin-bottom:16px;">
<h3 style="color:#0369a1;margin-bottom:10px;">🏜️ Sand Dunes / C&#7891;n C&aacute;t</h3>
<p style="color:#475569;font-size:15px;">Sand dunes form where constructive waves deposit sand on beaches → dried by wind → blown inland. <strong>Vegetation succession</strong>: Embryo dune (strand line) → Yellow dune (sea couch) → Semi-fixed (marram grass) → Fixed/grey dune (diverse plants + trees).</p>
<p {VI}><strong>C&#7891;n c&aacute;t:</strong> H&igrave;nh th&agrave;nh khi s&oacute;ng ki&#7871;n t&#7841;o &dagger;&#7849;y c&aacute;t l&ecirc;n b&#7827;i &rarr; kh&ocirc; &dagger;i &rarr; gi&oacute; th&#7893;i v&agrave;o &dagger;&#7845;t li&#7873;n. <strong>Di&#7877;n th&#7871; th&#7921;c v&#7853;t:</strong> C&#7891;n ph&ocirc;i thai (ng&#7855;n v&ugrave;ng n&#432;&#7899;c) &rarr; C&#7891;n v&agrave;ng (c&#7887; sea couch) &rarr; C&#7891;n b&aacute;n c&#7889; &dagger;&#7883;nh (c&#7887; marram) &rarr; C&#7891;n c&#7889; &dagger;&#7883;nh/x&aacute;m (&dagger;a d&#7841;ng th&#7921;c v&#7853;t + c&acirc;y). C&#7887; marram c&oacute; r&#7877; s&acirc;u l&agrave; lo&agrave;i g&#7855;n k&#7871;t ch&iacute;nh c&#7911;a c&#7891;n v&agrave;ng.</p>
</div>

<img src="{IMG}2_2_fig225.png" alt="Sand dune succession" style="max-width:460px;height:auto;display:block;margin:0 auto;"/>
<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 2.25 Sand dune succession: embryo → yellow → semi-fixed → fixed</p>
</div>

<!-- Summary Table -->
<div style="margin-bottom:40px;">
<h2 style="color:#0f172a;border-bottom:2px solid #7dd3fc;padding-bottom:8px;margin-bottom:16px;font-size:22px;">📊 Summary / T&oacute;m T&#7855;t</h2>
<p {VI}>C&aacute;c &dagger;&#7883;a h&igrave;nh b&#7901; bi&#7875;n &dagger;&#432;&#7907;c ph&acirc;n th&agrave;nh hai nh&oacute;m ch&iacute;nh: <strong>x&oacute;i m&ograve;n</strong> (do s&oacute;ng ph&aacute; h&#7911;y t&#7841;o n&ecirc;n) v&agrave; <strong>b&#7891;i t&#7909;</strong> (do s&oacute;ng v&agrave; d&ograve;ng ch&#7843;y t&#7871; b&agrave;o l&#7855;ng &dagger;&#7885;ng v&#7853;t li&#7879;u t&#7841;o n&ecirc;n).</p>
<div style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<tr style="background:#0369a1;color:white;"><th style="padding:10px;text-align:left;">Landform / Địa Hình</th><th style="padding:10px;">Type / Loại</th><th style="padding:10px;">Key Process / Quá Trình Chính</th></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Headland &amp; Bay / Mũi đất &amp; Vịnh</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#dc2626;">Erosional / Xói mòn</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Differential erosion / Xói mòn chênh lệch</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Cave→Arch→Stack / Hang→Cổng→Cột</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#dc2626;">Erosional / Xói mòn</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Hydraulic action / Lực thủy động</td></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Beach / Bãi biển</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#15803d;">Depositional / Bồi tụ</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Constructive waves / Sóng kiến tạo</td></tr>
<tr><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Spit / Mũi cát</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;color:#15803d;">Depositional / Bồi tụ</td><td style="padding:8px;border-bottom:1px solid #e2e8f0;">Longshore drift / Dòng chảy ven bờ</td></tr>
<tr style="background:#f8fafc;"><td style="padding:8px;">Sand Dune / Cồn cát</td><td style="padding:8px;color:#15803d;">Depositional / Bồi tụ</td><td style="padding:8px;">Wind + vegetation / Gió + thực vật</td></tr>
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
print(f'PATCH 2.2 P2: HTTP {r.status_code}')
