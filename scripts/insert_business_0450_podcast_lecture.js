const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');
const { generateBusinessPodcastPlayerHtml } = require('./generate_business_0450_player');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const COURSE_ID = '564f9e56-b77c-43af-9299-23eb2e7dcb7e'; // IGCSE-Business Studies-0450
const MODULE_TITLE = 'Revision [color:#f0fdf4,#15803d]';
const LECTURE_TITLE = 'Podcast ôn tập';

async function main() {
  const manifest = JSON.parse(fs.readFileSync('scripts/business_0450_podcast_manifest.json', 'utf-8'));
  console.log(`Loaded Business 0450 manifest with ${manifest.length} episodes.`);

  // 1. Find or create Module "Revision"
  const { data: existingMods, error: errModFind } = await supabase
    .from('lecture_modules')
    .select('id, title, order_index')
    .eq('course_id', COURSE_ID)
    .ilike('title', '%Revision%');

  if (errModFind) {
    console.error('Error finding module:', errModFind);
    return;
  }

  // Get max order_index of existing modules to put Revision at the bottom
  const { data: allMods } = await supabase
    .from('lecture_modules')
    .select('order_index')
    .eq('course_id', COURSE_ID)
    .order('order_index', { ascending: false });

  const maxOrder = (allMods && allMods.length > 0 && allMods[0].order_index) ? allMods[0].order_index : 6;
  const targetModuleOrder = Math.max(maxOrder + 1, 7);

  let moduleId;
  if (existingMods && existingMods.length > 0) {
    moduleId = existingMods[0].id;
    console.log(`Found existing Revision module (${moduleId}). Updating title & order...`);
    await supabase.from('lecture_modules').update({
      title: MODULE_TITLE,
      order_index: targetModuleOrder
    }).eq('id', moduleId);
  } else {
    moduleId = crypto.randomUUID();
    console.log(`Creating new Revision module (${moduleId}) at order ${targetModuleOrder}...`);
    const { error: insModErr } = await supabase.from('lecture_modules').insert([{
      id: moduleId,
      course_id: COURSE_ID,
      title: MODULE_TITLE,
      order_index: targetModuleOrder
    }]);
    if (insModErr) {
      console.error('Error inserting module:', insModErr);
      return;
    }
  }

  console.log(`Module ready: ${moduleId}`);

  // 2. Find or create Lecture "Podcast ôn tập"
  const { data: existingLecs, error: errLecFind } = await supabase
    .from('lectures')
    .select('id, title, order_index')
    .eq('course_id', COURSE_ID)
    .eq('module_id', moduleId)
    .eq('title', LECTURE_TITLE);

  if (errLecFind) {
    console.error('Error finding lecture:', errLecFind);
    return;
  }

  let lectureId;
  if (existingLecs && existingLecs.length > 0) {
    lectureId = existingLecs[0].id;
    console.log(`Found existing lecture (${lectureId}). Updating...`);
    await supabase.from('lectures').update({
      title: LECTURE_TITLE,
      order_index: 1,
      is_published: true
    }).eq('id', lectureId);
  } else {
    lectureId = crypto.randomUUID();
    console.log(`Creating new lecture (${lectureId})...`);
    const { error: insLecErr } = await supabase.from('lectures').insert([{
      id: lectureId,
      course_id: COURSE_ID,
      module_id: moduleId,
      title: LECTURE_TITLE,
      order_index: 1,
      is_published: true
    }]);
    if (insLecErr) {
      console.error('Error inserting lecture:', insLecErr);
      return;
    }
  }

  console.log(`Lecture ready: ${lectureId}`);

  // 3. Generate Page 1 (Vietnamese)
  const page1Html = generateBusinessPodcastPlayerHtml(manifest, 'vi');
  console.log(`Page 1 (VI) HTML length: ${page1Html.length} chars.`);

  const { data: p1Data } = await supabase
    .from('lecture_pages')
    .select('id')
    .eq('lecture_id', lectureId)
    .eq('page_number', 1);

  if (p1Data && p1Data.length > 0) {
    console.log(`Updating existing Page 1 (${p1Data[0].id})...`);
    await supabase.from('lecture_pages').update({
      content_html: page1Html
    }).eq('id', p1Data[0].id);
  } else {
    console.log('Creating Page 1...');
    await supabase.from('lecture_pages').insert([{
      id: crypto.randomUUID(),
      lecture_id: lectureId,
      page_number: 1,
      content_html: page1Html
    }]);
  }

  // 4. Generate Page 2 (English)
  const page2Html = generateBusinessPodcastPlayerHtml(manifest, 'en');
  console.log(`Page 2 (EN) HTML length: ${page2Html.length} chars.`);

  const { data: p2Data } = await supabase
    .from('lecture_pages')
    .select('id')
    .eq('lecture_id', lectureId)
    .eq('page_number', 2);

  if (p2Data && p2Data.length > 0) {
    console.log(`Updating existing Page 2 (${p2Data[0].id})...`);
    await supabase.from('lecture_pages').update({
      content_html: page2Html
    }).eq('id', p2Data[0].id);
  } else {
    console.log('Creating Page 2...');
    await supabase.from('lecture_pages').insert([{
      id: crypto.randomUUID(),
      lecture_id: lectureId,
      page_number: 2,
      content_html: page2Html
    }]);
  }

  // 5. Verification
  const { data: finalPages } = await supabase
    .from('lecture_pages')
    .select('id, page_number, created_at')
    .eq('lecture_id', lectureId)
    .order('page_number');

  console.log('Verified Lecture Pages in DB:', finalPages);
  console.log('\n🎉 ALL BUSINESS 0450 LECTURE & PAGES CREATED / UPDATED SUCCESSFULLY!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
