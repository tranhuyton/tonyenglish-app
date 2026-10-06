const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');
const { generateSciencePodcastPlayerHtml } = require('./generate_science_0654_player');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const COURSE_ID = 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7';
const MODULE_ID = 'ed75a372-2216-4d4f-b135-9aff40d65b19'; // 0654 Past Papers
const LECTURE_TITLE = 'Podcast ôn tập';

async function main() {
  const manifest = JSON.parse(fs.readFileSync('scripts/science_0654_podcast_manifest.json', 'utf-8'));
  console.log(`Loaded Science 0654 manifest with ${manifest.length} episodes.`);

  // 1. Find or create Lecture
  const { data: existingLecs, error: errLecFind } = await supabase
    .from('lectures')
    .select('id, title, order_index')
    .eq('course_id', COURSE_ID)
    .eq('module_id', MODULE_ID)
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
    const { error: insErr } = await supabase.from('lectures').insert([{
      id: lectureId,
      course_id: COURSE_ID,
      module_id: MODULE_ID,
      title: LECTURE_TITLE,
      order_index: 1,
      is_published: true
    }]);
    if (insErr) {
      console.error('Error inserting lecture:', insErr);
      return;
    }
  }

  console.log(`Lecture ready: ${lectureId}`);

  // 2. Generate Page 1 (Vietnamese)
  const page1Html = generateSciencePodcastPlayerHtml(manifest, 'vi');
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

  // 3. Generate Page 2 (English)
  const page2Html = generateSciencePodcastPlayerHtml(manifest, 'en');
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

  // 4. Verification
  const { data: pages } = await supabase
    .from('lecture_pages')
    .select('id, page_number, created_at')
    .eq('lecture_id', lectureId)
    .order('page_number');

  console.log('Lecture Pages verified:', pages);
  console.log(`\n🎉 Podcast lecture successfully created/updated in 0654 Past Papers!`);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
