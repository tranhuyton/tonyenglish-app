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

async function main() {
  console.log(`Loaded IELTS Premium manifest.`);

  for (const [skillKey, lectureId] of Object.entries(CANONICAL_MAP)) {
    const skillData = manifest[skillKey];
    console.log(`\n=== Processing [${skillKey}] -> Lecture: ${lectureId} ===`);

    const playerHtml = generateIeltsSkillPlayerHtml(skillKey, skillData);
    console.log(`Generated HTML length: ${playerHtml.length} characters.`);

    const { data: existingPages } = await supabase
      .from('lecture_pages')
      .select('id, page_number')
      .eq('lecture_id', lectureId)
      .eq('page_number', 1);

    if (existingPages && existingPages.length > 0) {
      console.log(`Updating existing page 1 (${existingPages[0].id})...`);
      await supabase
        .from('lecture_pages')
        .update({ content_html: playerHtml })
        .eq('id', existingPages[0].id);
    } else {
      console.log('Inserting new page 1...');
      await supabase
        .from('lecture_pages')
        .insert([{
          id: crypto.randomUUID(),
          lecture_id: lectureId,
          page_number: 1,
          content_html: playerHtml
        }]);
    }
  }

  console.log('\n🎉 ALL 5 IELTS PREMIUM CANONICAL LECTURE PAGES UPDATED SUCCESSFULLY!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
