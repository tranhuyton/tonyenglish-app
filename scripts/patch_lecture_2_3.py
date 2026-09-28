import os, re, sys, json, subprocess
sys.stdout.reconfigure(encoding='utf-8')
from supabase import create_client

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

url = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
key = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(url, key)

LECTURE_ID = "446dabf6-7c9d-4509-a3f9-78161a684e3e"
MANIFEST_PATH = "public/audio/lectures/geography/2_3/manifest.json"

# --- 1. UPDATE MANIFEST 2.3 ---
with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

# Check if haz_tsunami already in segments
has_tsunami = any(s['id'] == 'haz_tsunami' for s in manifest['segments'])
if not has_tsunami:
    cyclones_idx = next(i for i, s in enumerate(manifest['segments']) if s['id'] == 'haz_cyclones')
    new_seg = {
        "id": "haz_tsunami",
        "title": "Sóng thần (Tsunami) & Hiểm họa biển sâu",
        "selector": "#card-haz-tsunami",
        "en": "Tsunamis and Coastal Inundation. Giant ocean waves triggered by submarine earthquakes or landslides. Barely detectable in deep water, they travel at eight hundred kilometres per hour, swelling up to thirty metres high in shallow bays with catastrophic destructive force, as seen in the 2004 Indian Ocean disaster.",
        "vi": "Sóng thần và Thảm họa ngập lụt ven biển. Là những đợt sóng xung kích đại dương khổng lồ sinh ra do động đất dưới đáy biển hoặc sạt lở ngầm. Khi ở ngoài khơi xa sóng rất thấp, di chuyển với vận tốc tám trăm ki-lô-mét một giờ, nhưng khi vào bờ chúng dâng cao tới ba mươi mét với sức tàn phá khủng khiếp, như thảm họa sóng thần Ấn Độ Dương năm hai nghìn không trăm lẻ tư.",
        "duration": 41.42,
        "audioUrl": "/audio/lectures/geography/2_3/haz_tsunami.mp3",
        "startTime": 0,
        "endTime": 0
    }
    manifest['segments'].insert(cyclones_idx + 1, new_seg)

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
    "banner_overview": {"start": id_to_idx["banner_overview"], "end": id_to_idx["banner_overview"]},
    "sec_opportunities": {"start": id_to_idx["sec_opportunities"], "end": id_to_idx["rodney_bay_fig"]},
    "sec_hazards": {"start": id_to_idx["sec_hazards"], "end": id_to_idx["haz_pollution"]},
    "sec_management": {"start": id_to_idx["sec_management"], "end": id_to_idx["mgmt_soft"]}
}

with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print(f"Manifest 2.3 updated! Total duration: {manifest['totalDuration']}s, {len(manifest['segments'])} segments")

# --- 2. UPDATE HTML 2.3 ---
with open('scratch/db_page1_lec23.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace SVG banner clickable buttons
old_svg_buttons = """<rect x="20" y="55" width="85" height="32" rx="16" fill="#16a34a" onclick="showCoast('tourism')" style="cursor:pointer"/>
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
<text x="200" y="118" text-anchor="middle" fill="#14532d" font-size="11" style="cursor:pointer" onclick="showCoast('mgmt')">▼ Coastal Management Strategies</text>"""

new_svg_buttons = """<g id="btn-banner-tourism" data-lecture-section="opp_tourism" onclick="showCoast('tourism')" style="cursor:pointer" class="coast-btn">
  <rect x="20" y="55" width="85" height="32" rx="16" fill="#16a34a"/>
  <text x="62" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">🏖️ Tourism</text>
</g>
<g id="btn-banner-fishing" data-lecture-section="opp_fishing" onclick="showCoast('fishing')" style="cursor:pointer" class="coast-btn">
  <rect x="115" y="55" width="85" height="32" rx="16" fill="#15803d"/>
  <text x="157" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">🐟 Fishing</text>
</g>
<g id="btn-banner-transport" data-lecture-section="opp_transport" onclick="showCoast('transport')" style="cursor:pointer" class="coast-btn">
  <rect x="210" y="55" width="85" height="32" rx="16" fill="#166534"/>
  <text x="252" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">⚓ Transport</text>
</g>
<g id="btn-banner-settlement" data-lecture-section="opp_settlement" onclick="showCoast('settlement')" style="cursor:pointer" class="coast-btn">
  <rect x="305" y="55" width="85" height="32" rx="16" fill="#14532d"/>
  <text x="347" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">🏙️ Settlement</text>
</g>
<g id="btn-banner-erosion" data-lecture-section="haz_erosion" onclick="showCoast('erosion')" style="cursor:pointer" class="coast-btn">
  <rect x="415" y="55" width="90" height="32" rx="16" fill="#dc2626"/>
  <text x="460" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">🌊 Erosion</text>
</g>
<g id="btn-banner-flooding" data-lecture-section="haz_flooding" onclick="showCoast('flooding')" style="cursor:pointer" class="coast-btn">
  <rect x="515" y="55" width="80" height="32" rx="16" fill="#b91c1c"/>
  <text x="555" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">💧 Flooding</text>
</g>
<g id="btn-banner-cyclones" data-lecture-section="haz_cyclones" onclick="showCoast('cyclones')" style="cursor:pointer" class="coast-btn">
  <rect x="605" y="55" width="80" height="32" rx="16" fill="#991b1b"/>
  <text x="645" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">🌀 Cyclones</text>
</g>
<g id="btn-banner-tsunami" data-lecture-section="haz_tsunami" onclick="showCoast('tsunami')" style="cursor:pointer" class="coast-btn">
  <rect x="695" y="55" width="85" height="32" rx="16" fill="#7f1d1d"/>
  <text x="737" y="76" text-anchor="middle" fill="white" font-size="12" font-weight="600">🌊 Tsunami</text>
</g>
<g id="btn-banner-mgmt" data-lecture-section="sec_management" onclick="showCoast('mgmt')" style="cursor:pointer" class="coast-btn">
  <rect x="40" y="102" width="320" height="26" rx="6" fill="#14532d" opacity="0.18"/>
  <text x="200" y="119" text-anchor="middle" fill="#14532d" font-size="11" font-weight="bold">▼ Coastal Management Strategies</text>
</g>"""

assert old_svg_buttons in html, "old_svg_buttons not found in html"
html = html.replace(old_svg_buttons, new_svg_buttons)

# Update showCoast script
old_script = """<script>
function showCoast(name) {
  ['tourism','fishing','transport','settlement','erosion','flooding','cyclones','tsunami','mgmt'].forEach(function(f){
    var el=document.getElementById('coast-'+f);
    if(el) el.style.display='none';
  });
  document.getElementById('coast-default').style.display='none';
  var target=document.getElementById('coast-'+name);
  if(target) target.style.display='block';
}
</script>"""

new_script = """<script>
function showCoast(name) {
  ['tourism','fishing','transport','settlement','erosion','flooding','cyclones','tsunami','mgmt'].forEach(function(f){
    var el=document.getElementById('coast-'+f);
    if(el) el.style.display='none';
  });
  document.getElementById('coast-default').style.display='none';
  var target=document.getElementById('coast-'+name);
  if(target) {
    target.style.display='block';
    target.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  document.querySelectorAll('.coast-btn rect').forEach(function(r) {
    r.removeAttribute('stroke');
    r.removeAttribute('stroke-width');
    r.removeAttribute('filter');
  });
  var activeBtn = document.getElementById('btn-banner-' + name);
  if (activeBtn) {
    var r = activeBtn.querySelector('rect');
    if (r) {
      r.setAttribute('stroke', '#ffffff');
      r.setAttribute('stroke-width', '2.5');
      r.setAttribute('filter', 'drop-shadow(0 0 6px rgba(255,255,255,0.8))');
    }
  }
}

window.addEventListener('message', function(e) {
  if (e.data && e.data.type === 'HIGHLIGHT_LECTURE_SECTION') {
    var sel = e.data.selector;
    var map = {
      'tourism': 'tourism',
      'fishing': 'fishing',
      'transport': 'transport',
      'settlement': 'settlement',
      'erosion': 'erosion',
      'flooding': 'flooding',
      'cyclones': 'cyclones',
      'tsunami': 'tsunami',
      'management': 'mgmt'
    };
    for (var k in map) {
      if (sel && sel.includes(k)) {
        showCoast(map[k]);
        break;
      }
    }
  }
});
</script>"""

assert old_script in html, "old_script not found in html"
html = html.replace(old_script, new_script)

# Add stopPropagation and close button to coast panels
for p in ['tourism','fishing','transport','settlement','erosion','flooding','cyclones','tsunami','mgmt']:
    pattern = f'<div id="coast-{p}" style="display:none;'
    replacement = f'<div id="coast-{p}" onclick="event.stopPropagation();" style="position:relative;display:none;'
    close_btn = f'<span onclick="document.getElementById(\'coast-{p}\').style.display=\'none\'; document.getElementById(\'coast-default\').style.display=\'block\'; event.stopPropagation();" style="position:absolute;top:10px;right:14px;cursor:pointer;font-size:16px;color:#94a3b8;font-weight:bold;line-height:1;padding:4px 8px;border-radius:4px;user-select:none;" title="Đóng">✕</span>\n'
    
    if pattern in html:
        html = html.replace(pattern, replacement)
        # Add close button after heading
        h3_pattern = re.compile(rf'(<div id="coast-{p}"[^>]*>\s*<h3[^>]*>.*?</h3>)', re.S)
        html = h3_pattern.sub(rf'\1\n{close_btn}', html)

# Add card-haz-tsunami in hazards section if not present
if 'id="card-haz-tsunami"' not in html:
    # Look for cyclones card and insert tsunami card after it
    cyclones_card_pattern = re.compile(r'(<div id="card-haz-cyclones".*?</div>\s*</div>)', re.S)
    tsunami_card_html = """
<div id="card-haz-tsunami" data-lecture-section="haz_tsunami" class="lecture-interactive-card" style="background:#fff1f2;border:2px solid #f87171;border-radius:10px;padding:16px;margin-bottom:16px;cursor:pointer;">
<h3 style="color:#dc2626;">🌊 Tsunamis & Oceanic Inundation</h3>
<p style="color:#475569;margin-bottom:8px;">Tsunamis are giant ocean waves triggered by underwater earthquakes, volcanic eruptions, or submarine landslides. In the open ocean they travel at 800 km/h but are only 1m high — undetectable. As they approach shallow water they slow down and pile up, reaching 30m+ height with catastrophic power.</p>
<p style="color:#475569;font-size:14px;"><strong>Example:</strong> 2004 Indian Ocean Tsunami (9.1 magnitude, off Sumatra): killed 227,898 people across 14 countries. <strong>Management:</strong> Pacific Tsunami Warning System (PTWS), DART buoys, mangrove coastal buffers, and hazard zoning.</p>
</div>"""
    if cyclones_card_pattern.search(html):
        html = cyclones_card_pattern.sub(r'\1\n' + tsunami_card_html, html)
        print("Inserted card-haz-tsunami into hazards section!")

# Save local
with open('scratch/db_page1_lec23.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('scratch/lectures/2_3_p1.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update Supabase
sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', LECTURE_ID).eq('page_number', 1).execute()
print("Supabase Page 1 for Lecture 2.3 updated successfully!")
