import os, re, sys, json, subprocess
sys.stdout.reconfigure(encoding='utf-8')
from supabase import create_client

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

url = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
key = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(url, key)

LECTURE_ID = "d38db7a8-e92e-450c-a034-b9d46dc10a7f"
MANIFEST_PATH = "public/audio/lectures/geography/2_1/manifest.json"

# --- 1. UPDATE MANIFEST 2.1 ---
with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# Update selectors for erosion
for s in manifest['segments']:
    if s['id'] == 'erosion_hydraulic':
        s['selector'] = '#btn-erosion-hydraulic'
    elif s['id'] == 'erosion_abrasion':
        s['selector'] = '#btn-erosion-abrasion'
    elif s['id'] == 'erosion_attrition':
        s['selector'] = '#btn-erosion-attrition'
    elif s['id'] == 'erosion_solution':
        s['selector'] = '#btn-erosion-solution'

# Check if lsd_how_it_works already in segments
has_lsd_how = any(s['id'] == 'lsd_how_it_works' for s in manifest['segments'])
if not has_lsd_how:
    # Insert after lsd_diagram
    diag_idx = next(i for i, s in enumerate(manifest['segments']) if s['id'] == 'lsd_diagram')
    new_seg = {
        "id": "lsd_how_it_works",
        "title": "Cơ chế hoạt động của trôi dạt ven bờ",
        "selector": "#card-lsd-how-it-works",
        "en": "How Longshore Drift Works. First, prevailing winds drive waves to approach the beach at an angle. The swash rushes diagonally up the beach slope, carrying sediment along with it. Second, gravity pulls the backwash straight down the beach perpendicular to the shoreline. Repeating this continuous zigzag pattern moves sand and shingle step by step along the coast.",
        "vi": "Cơ chế hoạt động của hiện tượng trôi dạt ven bờ. Đầu tiên, gió thịnh hành đẩy các con sóng vỗ vào bờ theo một góc chéo. Đợt sóng tràn cuốn theo cát sỏi chạy xiên lên bãi biển. Tiếp theo, trọng lực kéo đợt sóng rút thẳng góc trở lại biển. Quá trình dích dắc này lặp đi lặp lại liên tục, đẩy cát sỏi dịch chuyển từng bước một dọc theo bờ biển.",
        "duration": 45.69,
        "audioUrl": "/audio/lectures/geography/2_1/lsd_how_it_works.mp3",
        "startTime": 0,
        "endTime": 0
    }
    manifest['segments'].insert(diag_idx + 1, new_seg)

# Recalculate start and end times for all segments
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
    "sec_factors": {"start": id_to_idx["sec_factors"], "end": id_to_idx["factor_human"]},
    "sec_erosion": {"start": id_to_idx["sec_erosion"], "end": id_to_idx["erosion_solution"]},
    "sec_transport": {"start": id_to_idx["sec_transport"], "end": id_to_idx["transport_suspended"]},
    "sec_deposition": {"start": id_to_idx["sec_deposition"], "end": id_to_idx["deposition_conditions"]},
    "sec_longshore_drift": {"start": id_to_idx["sec_longshore_drift"], "end": id_to_idx["lsd_groynes"]},
    "sec_wave_types": {"start": id_to_idx["sec_wave_types"], "end": id_to_idx["wave_comparison"]}
}

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print(f"Manifest 2.1 updated! Total duration: {manifest['totalDuration']}s, {len(manifest['segments'])} segments")

# --- 2. UPDATE HTML 2.1 ---
with open('scratch/db_page1_lec21.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Section 2 Erosion HTML
# We find everything from <div id="sec-erosion" to <div style="margin-top:20px;"> (before the Figure 2.2 image)
old_sec2_pattern = re.compile(
    r'(<div id="sec-erosion"[^>]*>.*?<h2[^>]*>.*?2\. Coastal Erosion.*?</h2>.*?'
    r'<p[^>]*>.*?</p>\s*)'
    r'(<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px;">.*?</div>\s*'
    r'<div id="erosion-panel".*?</div>\s*'
    r'<div id="card-erosion-hydraulic".*?</div>\s*</div>\s*'
    r'<div id="card-erosion-abrasion".*?</div>\s*</div>\s*'
    r'<div id="card-erosion-attrition".*?</div>\s*</div>\s*'
    r'<div id="card-erosion-solution".*?</div>\s*</div>\s*'
    r'<script>.*?</script>)',
    re.S
)

new_sec2_body = """<div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px;">
<button id="btn-erosion-hydraulic" data-lecture-section="erosion_hydraulic" onclick="showErosion('hydraulic')" class="erosion-btn" style="background:#0369a1;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;transition:all 0.2s;box-shadow:0 0 10px rgba(14,165,233,0.5);transform:scale(1.05);">🌊 Hydraulic Action</button>
<button id="btn-erosion-abrasion" data-lecture-section="erosion_abrasion" onclick="showErosion('abrasion')" class="erosion-btn" style="background:#0284c7;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;transition:all 0.2s;opacity:0.75;">🪨 Corrasion</button>
<button id="btn-erosion-attrition" data-lecture-section="erosion_attrition" onclick="showErosion('attrition')" class="erosion-btn" style="background:#0ea5e9;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;transition:all 0.2s;opacity:0.75;">💥 Attrition</button>
<button id="btn-erosion-solution" data-lecture-section="erosion_solution" onclick="showErosion('solution')" class="erosion-btn" style="background:#38bdf8;color:white;border:none;padding:10px 18px;border-radius:20px;cursor:pointer;font-size:14px;font-weight:600;transition:all 0.2s;opacity:0.75;">🧪 Corrosion</button>
</div>

<div id="erosion-panel" onclick="event.stopPropagation();" style="background:#f0f9ff;border:2px solid #7dd3fc;border-radius:12px;padding:20px;margin-bottom:18px;position:relative;">
<h3 id="erosion-title" style="color:#0369a1;margin-bottom:8px;">🌊 Hydraulic Action</h3>
<p id="erosion-body" style="color:#475569;line-height:1.6;margin-bottom:10px;">Waves crash against the cliff face, trapping and compressing air in cracks and joints. As the wave retreats, the sudden pressure release causes an <strong>explosive force</strong> that breaks off rock fragments. This is the most powerful erosion type during storms. Over time, the repeated compression and explosion widens joints until large blocks fall.</p>
<p id="erosion-tip" style="color:#0369a1;font-size:14px;background:#e0f2fe;padding:8px 12px;border-radius:6px;margin:0;">💡 <em>Most effective in well-jointed rocks like limestone, sandstone and granite, and in weak rocks like clays during storm conditions.</em></p>
</div>

<script>
const EROSION_DATA = {
  hydraulic: {
    title: "🌊 Hydraulic Action",
    body: "Waves crash against the cliff face, trapping and compressing air in cracks and joints. As the wave retreats, the sudden pressure release causes an <strong>explosive force</strong> that breaks off rock fragments. This is the most powerful erosion type during storms. Over time, the repeated compression and explosion widens joints until large blocks fall.",
    tip: "💡 <em>Most effective in well-jointed rocks like limestone, sandstone and granite, and in weak rocks like clays during storm conditions.</em>"
  },
  abrasion: {
    title: "🪨 Corrasion (Abrasion)",
    body: "Waves use sand, pebbles and shingle as <strong>tools of erosion</strong>, hurling them against the cliff face. This abrasive action is similar to sandpaper, grinding and scratching the rock surface. It is most effective at the base of cliffs during breaking waves and creates smooth, scratched surfaces called <em>slickensides</em>.",
    tip: "💡 <em>The load carried by the wave determines the erosional power — coarser material is more effective.</em>"
  },
  attrition: {
    title: "💥 Attrition",
    body: "Rock fragments and pebbles transported by waves <strong>collide with each other</strong> as they are rolled around by wave action. This causes them to chip, break and gradually become smaller, more rounded and smoother. This is why beach pebbles are smooth and rounded — they have been worn down over many years. Materials gradually reduce from boulders → cobbles → pebbles → sand grains.",
    tip: "💡 <em>Does not erode the coast directly, but progressively reduces sediment size into smooth, rounded pebbles and sand.</em>"
  },
  solution: {
    title: "🧪 Corrosion (Solution)",
    body: "Seawater is <strong>slightly acidic</strong> (due to dissolved CO₂ forming carbonic acid). This acid dissolves certain rock types, particularly <strong>limestone and chalk</strong>, which contain calcium carbonate. The rock is not mechanically broken — it dissolves chemically into the water. Produces smooth, honeycombed surfaces. Example: chalk cliffs of southern England.",
    tip: "💡 <em>Chemical dissolving action potent on carbonate rock formations such as limestone and chalk cliffs.</em>"
  }
};

function showErosion(type) {
  const data = EROSION_DATA[type];
  if (!data) return;
  const panel = document.getElementById('erosion-panel');
  const t = document.getElementById('erosion-title');
  const b = document.getElementById('erosion-body');
  const tip = document.getElementById('erosion-tip');
  if (t) t.innerHTML = data.title;
  if (b) b.innerHTML = data.body;
  if (tip) tip.innerHTML = data.tip;
  if (panel) {
    panel.style.display = 'block';
    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  document.querySelectorAll('.erosion-btn').forEach(function(btn) {
    btn.style.opacity = '0.75';
    btn.style.transform = 'scale(1)';
    btn.style.boxShadow = 'none';
  });
  const activeBtn = document.getElementById('btn-erosion-' + type);
  if (activeBtn) {
    activeBtn.style.opacity = '1';
    activeBtn.style.transform = 'scale(1.05)';
    activeBtn.style.boxShadow = '0 0 10px rgba(14, 165, 233, 0.5)';
  }
}

window.addEventListener('message', function(e) {
  if (e.data && e.data.type === 'HIGHLIGHT_LECTURE_SECTION') {
    var sel = e.data.selector;
    if (sel && sel.indexOf('#btn-erosion-') === 0) {
      var type = sel.replace('#btn-erosion-', '');
      showErosion(type);
    }
  }
});
</script>"""

if old_sec2_pattern.search(html):
    html = old_sec2_pattern.sub(r'\1' + new_sec2_body, html)
    print("Section 2 Erosion HTML updated successfully!")
else:
    print("WARNING: old_sec2_pattern did not match, using fallback replacement")
    # Fallback string replace
    old_str = html[html.find('<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px;">'):html.find('<div style="margin-top:20px;">\n<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/tasks/2_1_fig22.png"')]
    html = html.replace(old_str, new_sec2_body + "\n\n")
    print("Fallback replace completed!")

# Replace Section 5 "How it works"
old_how_it_works = """<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">
<strong style="color:#15803d;">How it works:</strong>
<ol style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;">
<li>Wave approaches beach at an angle (direction of prevailing wind)</li>
<li>Swash carries sediment diagonally up the beach</li>
<li>Backwash drags sediment straight back down the beach (gravity)</li>
<li>Net result: sediment moves step by step along the shore</li>
</ol>
</div>"""

new_how_it_works = """<div id="card-lsd-how-it-works" data-lecture-section="lsd_how_it_works" class="lecture-interactive-card" style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;cursor:pointer;">
<strong style="color:#15803d;">How it works:</strong>
<ol style="color:#475569;margin-top:8px;padding-left:18px;font-size:14px;">
<li>Wave approaches beach at an angle (direction of prevailing wind)</li>
<li>Swash carries sediment diagonally up the beach</li>
<li>Backwash drags sediment straight back down the beach (gravity)</li>
<li>Net result: sediment moves step by step along the shore</li>
</ol>
</div>"""

assert old_how_it_works in html, "old_how_it_works not found in html"
html = html.replace(old_how_it_works, new_how_it_works)
print("Section 5 How it works updated!")

# Save local
with open('scratch/db_page1_lec21.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('scratch/lectures/2_1_p1.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update Supabase
sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
print("Supabase Page 1 for Lecture 2.1 updated successfully!")
