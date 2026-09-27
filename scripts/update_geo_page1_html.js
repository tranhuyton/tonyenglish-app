const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const envContent = fs.readFileSync('.env', 'utf-8');
const url = envContent.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const key = envContent.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const sb = createClient(url, key);

async function updatePage1() {
  const lectureId = '6286cb6f-b4ac-495b-b2ea-5a2bab09f764';
  const { data: page, error: fetchErr } = await sb.from('lecture_pages')
    .select('id, content_html')
    .eq('lecture_id', lectureId)
    .eq('page_number', 1)
    .single();

  if (fetchErr || !page) {
    console.error('Fetch error:', fetchErr);
    return;
  }

  let html = page.content_html;

  // 1. Header
  html = html.replace(
    '<div style="text-align:center;margin-bottom:40px;">',
    '<div id="sec-header" data-lecture-section="intro" style="text-align:center;margin-bottom:40px;cursor:pointer;">'
  );

  // 2. Section 1: Drainage Basins
  html = html.replace(
    /<!-- Section 1: Drainage Basins -->\s*<div style="margin-bottom:44px;">/g,
    '<!-- Section 1: Drainage Basins -->\n<div id="sec-drainage-basin" data-lecture-section="drainage_basin" style="margin-bottom:44px;cursor:pointer;">'
  );

  // 3. Terms Grid items
  const termMap = [
    { key: 'Source', id: 'term-source', sec: 'source' },
    { key: 'Mouth', id: 'term-mouth', sec: 'mouth' },
    { key: 'Tributary', id: 'term-tributary', sec: 'tributary' },
    { key: 'Confluence', id: 'term-confluence', sec: 'confluence' },
    { key: 'Watershed', id: 'term-watershed', sec: 'watershed' },
    { key: 'Flood plain', id: 'term-floodplain', sec: 'floodplain' }
  ];

  termMap.forEach(item => {
    const target = `<strong style="color:#1d4ed8;">${item.key}</strong>`;
    const regex = new RegExp(`(<div style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;">\\s*)(${target})`, 'g');
    html = html.replace(regex, `<div id="${item.id}" data-lecture-section="${item.sec}" style="background:#f0f9ff;border-left:4px solid #3b82f6;padding:12px;border-radius:6px;cursor:pointer;transition:all 0.2s ease;">\n$2`);
  });

  // 4. Section 2: Bradshaw Model
  html = html.replace(
    /<!-- Section 2: Bradshaw Model -->\s*<div style="margin-bottom:44px;">/g,
    '<!-- Section 2: Bradshaw Model -->\n<div id="sec-bradshaw" data-lecture-section="bradshaw_model" style="margin-bottom:44px;cursor:pointer;">'
  );

  // 5. Section 3: Water Cycle
  html = html.replace(
    /<!-- Section 3: Water Cycle -->\s*<div style="margin-bottom:44px;">/g,
    '<!-- Section 3: Water Cycle -->\n<div id="sec-water-cycle" data-lecture-section="water_cycle" style="margin-bottom:44px;cursor:pointer;">'
  );

  // 6. Section 4: Fluvial Processes
  html = html.replace(
    /<!-- Section 4: River Processes -->\s*<div style="margin-bottom:44px;">/g,
    '<!-- Section 4: River Processes -->\n<div id="sec-fluvial-processes" data-lecture-section="fluvial_processes" style="margin-bottom:44px;cursor:pointer;">'
  );

  console.log('sec-header found:', html.includes('id="sec-header"'));
  console.log('sec-drainage-basin found:', html.includes('id="sec-drainage-basin"'));
  console.log('term-source found:', html.includes('id="term-source"'));
  console.log('term-mouth found:', html.includes('id="term-mouth"'));
  console.log('term-tributary found:', html.includes('id="term-tributary"'));
  console.log('term-confluence found:', html.includes('id="term-confluence"'));
  console.log('term-watershed found:', html.includes('id="term-watershed"'));
  console.log('term-floodplain found:', html.includes('id="term-floodplain"'));
  console.log('sec-bradshaw found:', html.includes('id="sec-bradshaw"'));
  console.log('sec-water-cycle found:', html.includes('id="sec-water-cycle"'));
  console.log('sec-fluvial-processes found:', html.includes('id="sec-fluvial-processes"'));

  const { error: updateErr } = await sb.from('lecture_pages')
    .update({ content_html: html })
    .eq('id', page.id);

  if (updateErr) {
    console.error('Update error:', updateErr);
  } else {
    console.log('✅ Page 1 updated in Supabase successfully!');
  }
}

updatePage1();
