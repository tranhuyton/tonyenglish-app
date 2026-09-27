const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)?.[1]?.trim();
const key = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)?.[1]?.trim();
const supabase = createClient(url, key);

async function run() {
  let html = fs.readFileSync('scratch_page_1.html', 'utf8');

  // 1. CSS styling for interactive cards
  const styleBlock = `
<style>
.lecture-interactive-card {
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  position: relative;
}
.lecture-interactive-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(14, 165, 233, 0.28) !important;
  border-color: #0284c7 !important;
}
</style>
`;
  if (!html.includes('lecture-interactive-card')) {
    html = styleBlock + html;
  }

  // 2. Section 2: Bradshaw Increase & Decrease cards
  html = html.replace(
    '<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;">\n<strong style="color:#15803d;">Increase downstream ↑</strong>',
    '<div id="card-bradshaw-increase" data-lecture-section="bradshaw_increase" class="lecture-interactive-card" style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;cursor:pointer;">\n<strong style="color:#15803d;">Increase downstream ↑</strong>'
  );

  html = html.replace(
    '<div style="background:#fff7ed;border-left:4px solid #f97316;padding:14px;border-radius:6px;">\n<strong style="color:#ea580c;">Decrease downstream ↓</strong>',
    '<div id="card-bradshaw-decrease" data-lecture-section="bradshaw_decrease" class="lecture-interactive-card" style="background:#fff7ed;border-left:4px solid #f97316;padding:14px;border-radius:6px;cursor:pointer;">\n<strong style="color:#ea580c;">Decrease downstream ↓</strong>'
  );

  // 3. Section 3: Water Cycle Buttons
  html = html.replace(
    '<button onclick="showWater(\'precip\')"',
    '<button data-lecture-section="water_precip" onclick="showWater(\'precip\')"'
  );
  html = html.replace(
    '<button onclick="showWater(\'interception\')"',
    '<button data-lecture-section="water_interception" onclick="showWater(\'interception\')"'
  );
  html = html.replace(
    '<button onclick="showWater(\'runoff\')"',
    '<button data-lecture-section="water_runoff" onclick="showWater(\'runoff\')"'
  );
  html = html.replace(
    '<button onclick="showWater(\'infiltration\')"',
    '<button data-lecture-section="water_infiltration" onclick="showWater(\'infiltration\')"'
  );
  html = html.replace(
    '<button onclick="showWater(\'groundwater\')"',
    '<button data-lecture-section="water_groundwater" onclick="showWater(\'groundwater\')"'
  );
  html = html.replace(
    '<button onclick="showWater(\'et\')"',
    '<button data-lecture-section="water_et" onclick="showWater(\'et\')"'
  );

  // Section 3: Water Cycle Content Boxes
  html = html.replace(
    '<div id="water-precip"',
    '<div id="water-precip" data-lecture-section="water_precip" class="lecture-interactive-card"'
  );
  html = html.replace(
    '<div id="water-interception"',
    '<div id="water-interception" data-lecture-section="water_interception" class="lecture-interactive-card"'
  );
  html = html.replace(
    '<div id="water-runoff"',
    '<div id="water-runoff" data-lecture-section="water_runoff" class="lecture-interactive-card"'
  );
  html = html.replace(
    '<div id="water-infiltration"',
    '<div id="water-infiltration" data-lecture-section="water_infiltration" class="lecture-interactive-card"'
  );
  html = html.replace(
    '<div id="water-groundwater"',
    '<div id="water-groundwater" data-lecture-section="water_groundwater" class="lecture-interactive-card"'
  );
  html = html.replace(
    '<div id="water-et"',
    '<div id="water-et" data-lecture-section="water_et" class="lecture-interactive-card"'
  );

  // Section 3: Water Basin Map (Figure 1.9)
  const oldMapBlock = `<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_real_fig1_9_map.jpeg" alt="Water cycle in a drainage basin" style="width:75%;max-width:80%;min-width:50%;height:auto;display:block;margin:20px auto 8px auto;border-radius:8px;box-shadow:0 4px 14px rgba(0,0,0,0.08);"/>\n<p style="font-size:13px;color:#94a3b8;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.9 The water cycle within a drainage basin</p>`;
  
  const newMapBlock = `
<div id="card-water-map" data-lecture-section="water_basin_map" class="lecture-interactive-card" style="cursor:pointer;padding:12px;border-radius:12px;margin:20px auto 8px auto;background:#f8fafc;border:1px solid #e2e8f0;transition:all 0.2s;">
  <img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_real_fig1_9_map.jpeg" alt="Water cycle in a drainage basin" style="width:75%;max-width:80%;min-width:50%;height:auto;display:block;margin:0 auto 8px auto;border-radius:8px;box-shadow:0 4px 14px rgba(0,0,0,0.08);"/>
  <p style="font-size:13px;color:#64748b;font-style:italic;text-align:center;margin-top:8px;">▲ Figure 1.9 The water cycle within a drainage basin (Bấm để nghe giảng)</p>
</div>`;

  if (html.includes(oldMapBlock)) {
    html = html.replace(oldMapBlock, newMapBlock);
  }

  // Section 3: Auto-reveal tab when player highlights water process
  const scriptSync = `
<script>
window.addEventListener('message', function(e) {
  if (e.data && e.data.type === 'HIGHLIGHT_LECTURE_SECTION') {
    var sel = e.data.selector;
    if (sel && sel.indexOf('#water-') === 0) {
      var name = sel.replace('#water-', '');
      if (['precip','interception','runoff','infiltration','groundwater','et'].indexOf(name) !== -1) {
        showWater(name);
      }
    }
  }
});
</script>
`;
  if (!html.includes("sel.indexOf('#water-')")) {
    html = html.replace('</script>\n\n<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_real_fig1_9_map.jpeg"', '</script>' + scriptSync + '\n\n<img src="https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/documents/geography/images/hq_real_fig1_9_map.jpeg"');
  }

  // 4. Section 4: 4 Types of Erosion
  html = html.replace(
    '<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">\n<strong style="color:#dc2626;">Hydraulic action</strong>',
    '<div id="card-hydraulic-action" data-lecture-section="hydraulic_action" class="lecture-interactive-card" style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;cursor:pointer;">\n<strong style="color:#dc2626;">Hydraulic action</strong>'
  );

  html = html.replace(
    '<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">\n<strong style="color:#dc2626;">Corrasion (Abrasion)</strong>',
    '<div id="card-abrasion" data-lecture-section="abrasion" class="lecture-interactive-card" style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;cursor:pointer;">\n<strong style="color:#dc2626;">Corrasion (Abrasion)</strong>'
  );

  html = html.replace(
    '<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">\n<strong style="color:#dc2626;">Attrition</strong>',
    '<div id="card-attrition" data-lecture-section="attrition" class="lecture-interactive-card" style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;cursor:pointer;">\n<strong style="color:#dc2626;">Attrition</strong>'
  );

  html = html.replace(
    '<div style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;">\n<strong style="color:#dc2626;">Corrosion (Solution)</strong>',
    '<div id="card-solution-erosion" data-lecture-section="solution_erosion" class="lecture-interactive-card" style="background:#fff1f2;border-left:4px solid #f87171;padding:14px;border-radius:6px;cursor:pointer;">\n<strong style="color:#dc2626;">Corrosion (Solution)</strong>'
  );

  // Section 4: 4 Types of Transportation
  html = html.replace(
    '<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">\n<strong style="color:#1d4ed8;font-size:13px;">Traction</strong>',
    '<div id="card-transport-traction" data-lecture-section="transport_traction" class="lecture-interactive-card" style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;cursor:pointer;">\n<strong style="color:#1d4ed8;font-size:13px;">Traction</strong>'
  );

  html = html.replace(
    '<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">\n<strong style="color:#1d4ed8;font-size:13px;">Saltation</strong>',
    '<div id="card-transport-saltation" data-lecture-section="transport_saltation" class="lecture-interactive-card" style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;cursor:pointer;">\n<strong style="color:#1d4ed8;font-size:13px;">Saltation</strong>'
  );

  html = html.replace(
    '<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">\n<strong style="color:#1d4ed8;font-size:13px;">Suspension</strong>',
    '<div id="card-transport-suspension" data-lecture-section="transport_suspension" class="lecture-interactive-card" style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;cursor:pointer;">\n<strong style="color:#1d4ed8;font-size:13px;">Suspension</strong>'
  );

  html = html.replace(
    '<div style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;">\n<strong style="color:#1d4ed8;font-size:13px;">Solution</strong>',
    '<div id="card-transport-solution" data-lecture-section="transport_solution" class="lecture-interactive-card" style="background:#f0f9ff;border-top:4px solid #3b82f6;padding:12px;border-radius:6px;text-align:center;cursor:pointer;">\n<strong style="color:#1d4ed8;font-size:13px;">Solution</strong>'
  );

  // Section 4: Deposition
  html = html.replace(
    '<div style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;margin-bottom:14px;">\n<p style="color:#475569;margin:0;">Deposition occurs',
    '<div id="card-deposition" data-lecture-section="deposition" class="lecture-interactive-card" style="background:#f0fdf4;border-left:4px solid #22c55e;padding:14px;border-radius:6px;margin-bottom:14px;cursor:pointer;">\n<p style="color:#475569;margin:0;">Deposition occurs'
  );

  fs.writeFileSync('scratch_page_1_updated.html', html, 'utf8');

  // Update Supabase
  const { error } = await supabase
    .from('lecture_pages')
    .update({ content_html: html })
    .eq('lecture_id', '6286cb6f-b4ac-495b-b2ea-5a2bab09f764')
    .eq('page_number', 1);

  if (error) {
    console.error('Lỗi cập nhật Supabase:', error);
    process.exit(1);
  }

  console.log('✅ Đã cập nhật thành công Page 1 lên Supabase với đầy đủ 29 phân đoạn tương tác!');
}

run();
