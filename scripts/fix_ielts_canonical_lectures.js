const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');
const { generateIeltsSkillPlayerHtml } = require('./generate_ielts_skill_player');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const manifest = JSON.parse(fs.readFileSync('scripts/ielts_premium_podcast_manifest.json', 'utf-8'));

const CANONICAL_MAP = {
  task1: 'ede14d51-3169-4f0e-a1a8-a2d8b9a31a4b',
  task2: 'b01279e6-fed1-4647-8b45-65c39f73003e',
  reading: '4474b4db-59d1-4f50-9a44-004a547b6521',
  listening: '11f45a0a-3288-479d-8b90-fcf9ce6ca484',
  speaking: 'bbd2be97-406d-41b5-a337-8e210e2f49c9'
};

const DUPLICATE_IDS = [
  'de1b8a6b-2f61-4bc4-86c2-b14cd50ebea4',
  'ec9fe735-7379-4590-87be-d2447c83e95e',
  'aa4ab4ae-be09-4957-a47c-f97f6be18ba5',
  '64970f0b-4756-4926-a5c1-6f9b548943af',
  '2dfc8d7c-a4b4-47c4-b092-b9699a74dce9'
];

async function fix() {
  console.log('1. Inserting pages for canonical lectures...');
  for (const [skillKey, lectureId] of Object.entries(CANONICAL_MAP)) {
    const skillData = manifest[skillKey];
    const html = generateIeltsSkillPlayerHtml(skillKey, skillData);
    
    // Check if page already exists
    const { data: pages } = await supabase.from('lecture_pages').select('id').eq('lecture_id', lectureId).eq('page_number', 1);
    if (pages && pages.length > 0) {
      await supabase.from('lecture_pages').update({ content_html: html }).eq('id', pages[0].id);
      console.log('Updated page for ' + skillKey + ' (' + lectureId + ')');
    } else {
      await supabase.from('lecture_pages').insert([{
        id: crypto.randomUUID(),
        lecture_id: lectureId,
        page_number: 1,
        content_html: html
      }]);
      console.log('Inserted page for ' + skillKey + ' (' + lectureId + ')');
    }
  }

  console.log('\n2. Deleting duplicate lectures...');
  await supabase.from('lecture_pages').delete().in('lecture_id', DUPLICATE_IDS);
  const { error: delErr } = await supabase.from('lectures').delete().in('id', DUPLICATE_IDS);
  if (delErr) console.error('Error deleting duplicate lectures:', delErr);
  else console.log('Deleted duplicate lectures and their pages.');

  console.log('\n3. Verification:');
  for (const [skillKey, lectureId] of Object.entries(CANONICAL_MAP)) {
    const { data: lec } = await supabase.from('lectures').select('id, title, module_id, order_index').eq('id', lectureId).single();
    const { count } = await supabase.from('lecture_pages').select('id', { count: 'exact', head: true }).eq('lecture_id', lectureId);
    console.log(`[${skillKey}] ${lec.title} (${lec.id}) -> ${count} page(s), order: ${lec.order_index}`);
  }
}

fix().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
