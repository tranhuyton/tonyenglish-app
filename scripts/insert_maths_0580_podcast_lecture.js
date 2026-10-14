const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');
const { generateMathsPodcastAndRevisionHtml } = require('./generate_maths_0580_player');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const COURSE_ID = '7211abb0-ccba-479f-92ad-2d218121f717'; // IGCSE - Maths-0580
const YEAR_END_REVISION_LECTURE_ID = '975e20ef-ab09-4aca-a1fb-a1e64f07a91e'; // Year End Revision

async function main() {
  const manifest = JSON.parse(fs.readFileSync('scripts/maths_0580_podcast_manifest.json', 'utf-8'));
  console.log(`Loaded Maths 0580 manifest with ${manifest.length} episodes.`);

  // 1. Verify lecture Year End Revision exists
  const { data: lec, error: lecErr } = await supabase
    .from('lectures')
    .select('id, title, module_id, order_index')
    .eq('id', YEAR_END_REVISION_LECTURE_ID)
    .single();

  if (lecErr || !lec) {
    console.error('Error finding Year End Revision lecture:', lecErr);
    process.exit(1);
  }
  console.log(`Found lecture: ${lec.title} (${lec.id})`);

  // 2. Generate Page 1 HTML (Podcast VI at top + Year End Revision Past Papers below, plus built-in VI/EN toggle)
  const page1Html = generateMathsPodcastAndRevisionHtml(manifest, 'vi');
  console.log(`Generated Page 1 (VI) HTML length: ${page1Html.length} chars.`);

  const { data: p1Data } = await supabase
    .from('lecture_pages')
    .select('id')
    .eq('lecture_id', YEAR_END_REVISION_LECTURE_ID)
    .eq('page_number', 1);

  if (p1Data && p1Data.length > 0) {
    console.log(`Updating existing Page 1 (${p1Data[0].id})...`);
    const { error: u1Err } = await supabase
      .from('lecture_pages')
      .update({ content_html: page1Html })
      .eq('id', p1Data[0].id);
    if (u1Err) console.error('Error updating Page 1:', u1Err);
  } else {
    console.log('Inserting Page 1...');
    const { error: i1Err } = await supabase
      .from('lecture_pages')
      .insert([{
        id: crypto.randomUUID(),
        lecture_id: YEAR_END_REVISION_LECTURE_ID,
        page_number: 1,
        content_html: page1Html
      }]);
    if (i1Err) console.error('Error inserting Page 1:', i1Err);
  }

  // 3. Generate Page 2 HTML (Podcast EN at top + Year End Revision Past Papers below, plus built-in VI/EN toggle)
  const page2Html = generateMathsPodcastAndRevisionHtml(manifest, 'en');
  console.log(`Generated Page 2 (EN) HTML length: ${page2Html.length} chars.`);

  const { data: p2Data } = await supabase
    .from('lecture_pages')
    .select('id')
    .eq('lecture_id', YEAR_END_REVISION_LECTURE_ID)
    .eq('page_number', 2);

  if (p2Data && p2Data.length > 0) {
    console.log(`Updating existing Page 2 (${p2Data[0].id})...`);
    const { error: u2Err } = await supabase
      .from('lecture_pages')
      .update({ content_html: page2Html })
      .eq('id', p2Data[0].id);
    if (u2Err) console.error('Error updating Page 2:', u2Err);
  } else {
    console.log('Inserting Page 2...');
    const { error: i2Err } = await supabase
      .from('lecture_pages')
      .insert([{
        id: crypto.randomUUID(),
        lecture_id: YEAR_END_REVISION_LECTURE_ID,
        page_number: 2,
        content_html: page2Html
      }]);
    if (i2Err) console.error('Error inserting Page 2:', i2Err);
  }

  // 4. Verify pages in DB
  const { data: finalPages } = await supabase
    .from('lecture_pages')
    .select('id, page_number')
    .eq('lecture_id', YEAR_END_REVISION_LECTURE_ID)
    .order('page_number');

  console.log('Verified Pages for Year End Revision:', finalPages);
  console.log('\n🎉 MATHS 0580 YEAR END REVISION PODCAST UPDATED SUCCESSFULLY!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
