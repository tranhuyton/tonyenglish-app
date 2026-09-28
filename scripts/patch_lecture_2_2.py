import os, re, sys, json, subprocess
sys.stdout.reconfigure(encoding='utf-8')
from supabase import create_client

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

url = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
key = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(url, key)

LECTURE_ID = "b0ca05f2-dab3-4223-9c25-c92d73df56c1"
MANIFEST_PATH = "public/audio/lectures/geography/2_2/manifest.json"

# --- 1. UPDATE MANIFEST 2.2 ---
with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

NEW_SEGMENTS_2_2 = [
    {
        "id": "dep_spit",
        "title": "Mũi tên cát (Spits)",
        "selector": "#card-dep-spit",
        "en": "Spits. A spit is an extended ridge of sand or shingle connected to the mainland at one end, extending across an estuary or bay. Longshore drift carries sediment until the coastline abruptly changes direction. Wave refraction curves the tip into a recurved hook, while the sheltered waters behind enable salt marshes to develop.",
        "vi": "Mũi tên cát. Là một doi cát hoặc sỏi dài nối với đất liền ở một đầu, vươn dài qua cửa vịnh hoặc cửa sông. Hiện tượng trôi dạt ven bờ vận chuyển trầm tích cho tới khi bờ biển đổi hướng đột ngột. Hiện tượng khúc xạ sóng uốn cong đầu mũi cát thành hình lưỡi câu, trong khi vùng nước lặng phía sau tạo điều kiện cho đầm lầy muối phát triển.",
        "duration": 41.54,
        "audioUrl": "/audio/lectures/geography/2_2/dep_spit.mp3"
    },
    {
        "id": "dep_bar",
        "title": "Bờ chắn vịnh (Bars & Baymouth Bars)",
        "selector": "#card-dep-bar",
        "en": "Bars and Baymouth Bars. A bar forms when a spit grows completely across a bay, connecting two headlands. This seals off the bay, trapping a body of calm water known as a lagoon. Over time, deposition infills the lagoon, converting it into fertile coastal wetland.",
        "vi": "Bờ chắn vịnh và Đầm phá. Bờ chắn hình thành khi mũi tên cát phát triển vươn dài bịt kín hoàn toàn cửa vịnh, nối liền hai mũi đất lại với nhau. Quá trình này cô lập một vùng nước lặng gọi là đầm phá. Theo thời gian, trầm tích bồi tụ dần lấp đầy đầm phá, biến nó thành vùng đất ngập nước phì nhiêu.",
        "duration": 38.56,
        "audioUrl": "/audio/lectures/geography/2_2/dep_bar.mp3"
    },
    {
        "id": "dep_tombolo",
        "title": "Doi cát nối đảo (Tombolos)",
        "selector": "#card-dep-tombolo",
        "en": "Tombolos. A tombolo is a sand or shingle ridge linking an offshore island to the mainland. Wave refraction around both sides of the island produces opposing wave crests that cancel out, creating a sheltered zone where sediment drops and builds up a connecting land bridge. Examples include St Ninians Isle and Mont Saint-Michel.",
        "vi": "Doi cát nối đảo. Doi cát nối đảo là một dải cát sỏi bồi tụ nối liền một hòn đảo ngoài khơi với đất liền. Sóng biển khúc xạ bao quanh hai bên hòn đảo tạo ra vùng nước lặng triệt tiêu năng lượng sóng, khiến trầm tích bồi đắp thành một cây cầu đất tự nhiên. Ví dụ tiêu biểu là đảo thánh Ni-ni-an ở nước Anh và đảo Mông Xanh-Mi-xen ở nước Pháp.",
        "duration": 42.06,
        "audioUrl": "/audio/lectures/geography/2_2/dep_tombolo.mp3"
    },
    {
        "id": "dune_embryo",
        "title": "Đụn cát phôi thai (1. Embryo Dune)",
        "selector": "#card-dune-embryo",
        "en": "Stage 1: Embryo Dunes. Embryo dunes develop at the high-water strandline where dry sand blown inland accumulates around driftwood and seaweed. Extremely saline and alkaline, they are colonised by tough pioneer plants like sea rocket, whose sparse roots begin anchoring the loose sand.",
        "vi": "Giai đoạn một: Đụn cát phôi thai. Đụn cát phôi thai hình thành tại đường mép nước triều cao nhất, nơi cát khô bị gió thổi vào bị giữ lại quanh các khúc gỗ mục và rong biển. Môi trường ở đây rất mặn và có tính kiềm cao, chỉ có các loài cây tiên phong như cải dại biển mới có thể bén rễ bước đầu cố định hạt cát.",
        "duration": 37.55,
        "audioUrl": "/audio/lectures/geography/2_2/dune_embryo.mp3"
    },
    {
        "id": "dune_yellow",
        "title": "Đụn cát vàng (2. Yellow Dune / Foredune)",
        "selector": "#card-dune-yellow",
        "en": "Stage 2: Yellow Dunes and Foredunes. Growing up to five to ten metres tall, yellow dunes are dominated by marram grass. Marram thrives as fresh sand buries it, pushing out extensive rhizomes and root networks that bind dunes firmly. Sand remains distinctly yellow due to minimal organic humus.",
        "vi": "Giai đoạn hai: Đụn cát vàng và Đụn cát phía trước. Đạt độ cao từ năm đến mười mét, đụn cát vàng được thống trị bởi cỏ cát ma-ram. Cỏ cát phát triển mạnh mẽ khi bị cát vùi lấp, đâm sâu mạng lưới rễ chằng chịt giúp liên kết các hạt cát thật vững chắc. Cát có màu vàng đặc trưng vì hàm lượng chất mùn còn rất thấp.",
        "duration": 41.01,
        "audioUrl": "/audio/lectures/geography/2_2/dune_yellow.mp3"
    },
    {
        "id": "dune_semifixed",
        "title": "Đụn cát bán cố định (3. Semi-fixed Dune)",
        "selector": "#card-dune-semifixed",
        "en": "Stage 3: Semi-fixed Dunes. Situated further inland away from harsh salt spray. Decaying marram grass enriches the sand with dark humus, retaining moisture and lowering soil alkalinity. A diverse community of mosses, clovers, dandelions, and fescue grasses flourishes.",
        "vi": "Giai đoạn ba: Đụn cát bán cố định. Nằm sâu hơn vào đất liền, tránh được hơi muối biển gay gắt. Xác cỏ cát ma-ram phân hủy làm giàu thêm chất mùn hữu cơ màu sẫm, giúp giữ ẩm và làm giảm độ kiềm của đất. Một thảm thực vật đa dạng gồm rêu, cỏ ba lá và hoa bồ công anh bắt đầu sinh sôi.",
        "duration": 40.46,
        "audioUrl": "/audio/lectures/geography/2_2/dune_semifixed.mp3"
    },
    {
        "id": "dune_fixed",
        "title": "Đụn cát cố định (4. Fixed Grey Dune & Dune Slacks)",
        "selector": "#card-dune-fixed",
        "en": "Stage 4: Fixed Grey Dunes and Dune Slacks. A mature, stable climax ecosystem. Deep grey soil supports heather, gorse shrubs, and woodland birch trees. In low sheltered depressions between ridges known as dune slacks, the water table reaches the surface, creating lush wetland pools.",
        "vi": "Giai đoạn bốn: Đụn cát cố định và Đầm trũng giữa đụn. Là hệ sinh thái đỉnh cực trưởng thành và ổn định. Tầng đất xám sâu giàu dinh dưỡng nuôi sống cây thạch nam, bụi kim tước và cây gỗ thân nhỏ. Tại các vùng trũng sâu giữa các sống đụn nơi mực nước ngầm lộ ra, các đầm nước ngọt trù phú được hình thành.",
        "duration": 40.74,
        "audioUrl": "/audio/lectures/geography/2_2/dune_fixed.mp3"
    }
]

# Build new segments array:
# Replace 'spits_bars_tombolos' with dep_spit, dep_bar, dep_tombolo
# Replace 'dunes_succession' with dune_embryo, dune_yellow, dune_semifixed, dune_fixed
new_segs = []
for s in manifest['segments']:
    if s['id'] == 'spits_bars_tombolos':
        new_segs.extend(NEW_SEGMENTS_2_2[:3])
    elif s['id'] == 'dunes_succession':
        new_segs.extend(NEW_SEGMENTS_2_2[3:])
    else:
        new_segs.append(s)

manifest['segments'] = new_segs

# Recalculate durations and times
curr_time = 0.0
for s in manifest['segments']:
    audio_file = os.path.join('public', s['audioUrl'].lstrip('/'))
    if os.path.exists(audio_file):
        cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', audio_file]
        dur = round(float(subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True).stdout.strip()), 2)
        s['duration'] = dur
    s['startTime'] = round(curr_time, 2)
    curr_time += s['duration']
    s['endTime'] = round(curr_time, 2)

manifest['totalDuration'] = round(curr_time, 2)

# Update majorSections
id_to_idx = {s['id']: i for i, s in enumerate(manifest['segments'])}
manifest['majorSections'] = {
    "intro": {"start": id_to_idx["intro"], "end": id_to_idx["intro"]},
    "sec_coastline_types": {"start": id_to_idx["sec_coastline_types"], "end": id_to_idx["coast_concordant"]},
    "sec_erosional_landforms": {"start": id_to_idx["sec_erosional_landforms"], "end": id_to_idx["caves_arches_figs"]},
    "sec_depositional_landforms": {"start": id_to_idx["sec_depositional_landforms"], "end": id_to_idx["dune_fixed"]},
    "summary_table": {"start": id_to_idx["summary_table"], "end": id_to_idx["summary_table"]}
}

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print(f"Manifest 2.2 updated! Total duration: {manifest['totalDuration']}s, {len(manifest['segments'])} segments")

# --- 2. UPDATE HTML 2.2 ---
with open('scratch/db_page1_lec22.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Spits, Bars & Tombolos
old_spits_block = """<div id="card-spits-bars-tombolos" data-lecture-section="spits_bars_tombolos" class="lecture-interactive-card" style="cursor:pointer;margin-bottom:16px;">
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
</div>"""

new_spits_block = """<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:16px;">
<div id="card-dep-spit" data-lecture-section="dep_spit" class="lecture-interactive-card" style="background:#f0f9ff;border:2px solid #bae6fd;border-left:5px solid #0ea5e9;padding:16px;border-radius:10px;cursor:pointer;">
<strong style="color:#0369a1;font-size:17px;">🏖️ Spit (Mũi tên cát)</strong><br/>
<p style="color:#475569;font-size:14px;margin:8px 0 0 0;line-height:1.5;">Ridge linked to land at one end, extending across a bay/estuary. Recurved end from wave refraction. Salt marsh forms in sheltered area behind.</p>
</div>
<div id="card-dep-bar" data-lecture-section="dep_bar" class="lecture-interactive-card" style="background:#f0fdf4;border:2px solid #bbf7d0;border-left:5px solid #22c55e;padding:16px;border-radius:10px;cursor:pointer;">
<strong style="color:#15803d;font-size:17px;">🏝️ Bar (Bờ chắn vịnh)</strong><br/>
<p style="color:#475569;font-size:14px;margin:8px 0 0 0;line-height:1.5;">Spit that has grown across an entire bay, cutting off a lagoon. Also called a bay bar. Forms where the bay is narrow enough for longshore drift to seal it.</p>
</div>
<div id="card-dep-tombolo" data-lecture-section="dep_tombolo" class="lecture-interactive-card" style="background:#fef3c7;border:2px solid #fde68a;border-left:5px solid #f59e0b;padding:16px;border-radius:10px;cursor:pointer;">
<strong style="color:#92400e;font-size:17px;">🌉 Tombolo (Doi cát nối đảo)</strong><br/>
<p style="color:#475569;font-size:14px;margin:8px 0 0 0;line-height:1.5;">Sand or shingle bar connecting the mainland to a nearby island. Opposing wave refraction cancels out energy, creating shelter. Example: St Ninian's Isle; Mont Saint-Michel.</p>
</div>
</div>"""

assert old_spits_block in html, "old_spits_block not found in html"
html = html.replace(old_spits_block, new_spits_block)

# Replace Sand Dunes block
old_dunes_block = """<div id="card-dunes-succession" data-lecture-section="dunes_succession" class="lecture-interactive-card" style="background:#fef9c3;border-radius:10px;padding:16px;margin-bottom:16px;cursor:pointer;">
<div style="background:#fef9c3;border-radius:10px;padding:16px;margin-bottom:16px;">
<div style="display:flex;gap:8px;align-items:flex-start;flex-wrap:wrap;">
<div style="background:#f59e0b;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;">1. Embryo Dune</div>
</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Forms at strand line; sand accumulates around debris</div>
<div style="background:#84cc16;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-left:8px;">2. Yellow Dune</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Sea couch grass colonises; grows to 1m; marram grass establishes</div>
<div style="background:#22c55e;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-left:8px;">3. Semi-fixed</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Marram grass main binder; over 10m high; soil begins to form</div>
<div style="background:#166534;color:white;padding:8px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-left:8px;">4. Fixed (Grey) Dune</div>
<div style="color:#64748b;font-size:14px;padding-top:8px;">→ Rich in species: lichens, mosses, flowering plants, eventually small trees</div>
</div>
</div>"""

new_dunes_block = """<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-bottom:16px;">
  <div id="card-dune-embryo" data-lecture-section="dune_embryo" class="lecture-interactive-card" style="background:#fffbeb;border:2px solid #fde68a;border-left:5px solid #f59e0b;border-radius:10px;padding:14px;cursor:pointer;">
    <div style="display:inline-block;background:#f59e0b;color:white;padding:4px 10px;border-radius:14px;font-size:12px;font-weight:700;margin-bottom:6px;">Stage 1</div>
    <h4 style="color:#92400e;margin:0 0 6px 0;font-size:16px;">🌱 1. Embryo Dune</h4>
    <p style="color:#475569;font-size:13.5px;margin:0;line-height:1.5;">Forms at the high-tide strandline where dry sand accumulates around driftwood. Highly saline and alkaline; tough pioneer plants like sea rocket begin to anchor loose sand.</p>
  </div>
  <div id="card-dune-yellow" data-lecture-section="dune_yellow" class="lecture-interactive-card" style="background:#f7fee7;border:2px solid #d9f99d;border-left:5px solid #84cc16;border-radius:10px;padding:14px;cursor:pointer;">
    <div style="display:inline-block;background:#84cc16;color:white;padding:4px 10px;border-radius:14px;font-size:12px;font-weight:700;margin-bottom:6px;">Stage 2</div>
    <h4 style="color:#3f6212;margin:0 0 6px 0;font-size:16px;">🌾 2. Yellow Dune (Foredune)</h4>
    <p style="color:#475569;font-size:13.5px;margin:0;line-height:1.5;">Grows up to 5–10m high. Marram grass dominates and spreads deep fibrous root networks that bind sand tightly. Sand remains yellow due to minimal organic humus.</p>
  </div>
  <div id="card-dune-semifixed" data-lecture-section="dune_semifixed" class="lecture-interactive-card" style="background:#f0fdf4;border:2px solid #bbf7d0;border-left:5px solid #22c55e;border-radius:10px;padding:14px;cursor:pointer;">
    <div style="display:inline-block;background:#22c55e;color:white;padding:4px 10px;border-radius:14px;font-size:12px;font-weight:700;margin-bottom:6px;">Stage 3</div>
    <h4 style="color:#166534;margin:0 0 6px 0;font-size:16px;">🌿 3. Semi-fixed Dune</h4>
    <p style="color:#475569;font-size:13.5px;margin:0;line-height:1.5;">Sheltered further inland. Decomposing marram grass adds dark organic humus, retaining moisture and lowering alkalinity. Mosses, clovers, and wildflowers flourish.</p>
  </div>
  <div id="card-dune-fixed" data-lecture-section="dune_fixed" class="lecture-interactive-card" style="background:#ecfdf5;border:2px solid #a7f3d0;border-left:5px solid #065f46;border-radius:10px;padding:14px;cursor:pointer;">
    <div style="display:inline-block;background:#065f46;color:white;padding:4px 10px;border-radius:14px;font-size:12px;font-weight:700;margin-bottom:6px;">Stage 4</div>
    <h4 style="color:#064e3b;margin:0 0 6px 0;font-size:16px;">🌳 4. Fixed (Grey) Dune &amp; Dune Slacks</h4>
    <p style="color:#475569;font-size:13.5px;margin:0;line-height:1.5;">Mature stable climax ecosystem. True acidic sandy soil supports heather, gorse, and small trees. Deep hollows reach the water table, creating lush wetland pools.</p>
  </div>
</div>"""

assert old_dunes_block in html, "old_dunes_block not found in html"
html = html.replace(old_dunes_block, new_dunes_block)

# Save local
with open('scratch/db_page1_lec22.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('scratch/lectures/2_2_p1.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update Supabase
sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
print("Supabase Page 1 for Lecture 2.2 updated successfully!")
