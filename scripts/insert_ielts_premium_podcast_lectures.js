const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');
const { generateIeltsSkillPlayerHtml } = require('./generate_ielts_skill_player');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const COURSE_ID = '239a64f0-c106-40e5-a6e2-4e685a0d70fb'; // IELTS Premium

async function main() {
  const manifest = JSON.parse(fs.readFileSync('scripts/ielts_premium_podcast_manifest.json', 'utf-8'));
  console.log(`Loaded IELTS Premium manifest with 5 skills.`);

  const results = [];

  for (const [skillKey, skillData] of Object.entries(manifest)) {
    const { moduleId, moduleName, lectureTitle, episodes } = skillData;
    console.log(`\n=== Processing [${skillKey}] ${lectureTitle} (${episodes.length} episodes) -> Module: ${moduleName} (${moduleId}) ===`);

    // 1. Check existing lecture
    const { data: existingLecs, error: errFind } = await supabase
      .from('lectures')
      .select('id, title, order_index')
      .eq('course_id', COURSE_ID)
      .eq('module_id', moduleId)
      .eq('title', lectureTitle);

    if (errFind) {
      console.error(`Error finding lecture for ${skillKey}:`, errFind);
      continue;
    }

    let lectureId;
    if (existingLecs && existingLecs.length > 0) {
      lectureId = existingLecs[0].id;
      console.log(`Found existing lecture (${lectureId}). Updating...`);
      const { error: updErr } = await supabase
        .from('lectures')
        .update({
          title: lectureTitle,
          order_index: 0,
          is_published: true
        })
        .eq('id', lectureId);
      if (updErr) console.error('Error updating lecture:', updErr);
    } else {
      lectureId = crypto.randomUUID();
      console.log(`Creating new lecture (${lectureId}) at order_index 0...`);
      const { error: insErr } = await supabase
        .from('lectures')
        .insert([{
          id: lectureId,
          course_id: COURSE_ID,
          module_id: moduleId,
          title: lectureTitle,
          order_index: 0,
          is_published: true
        }]);
      if (insErr) {
        console.error(`Error creating lecture for ${skillKey}:`, insErr);
        continue;
      }
    }

    console.log(`Lecture ready: ${lectureId}`);

    // 2. Generate Player HTML
    const playerHtml = generateIeltsSkillPlayerHtml(skillKey, skillData);
    console.log(`Generated HTML length: ${playerHtml.length} characters.`);

    // 3. Upsert Lecture Page 1
    const { data: existingPages, error: errPageFind } = await supabase
      .from('lecture_pages')
      .select('id, page_number')
      .eq('lecture_id', lectureId)
      .eq('page_number', 1);

    if (errPageFind) {
      console.error('Error finding page:', errPageFind);
      continue;
    }

    if (existingPages && existingPages.length > 0) {
      console.log(`Updating existing page 1 (${existingPages[0].id})...`);
      const { error: updPageErr } = await supabase
        .from('lecture_pages')
        .update({
          content_html: playerHtml
        })
        .eq('id', existingPages[0].id);
      if (updPageErr) console.error('Error updating page:', updPageErr);
    } else {
      console.log('Inserting new page 1...');
      const { error: insPageErr } = await supabase
        .from('lecture_pages')
        .insert([{
          id: crypto.randomUUID(),
          lecture_id: lectureId,
          page_number: 1,
          content_html: playerHtml
        }]);
      if (insPageErr) console.error('Error inserting page:', insPageErr);
    }

    results.push({
      skillKey,
      moduleName,
      lectureTitle,
      lectureId,
      episodesCount: episodes.length
    });
  }

  console.log('\n================================================================');
  console.log('🎉 ALL 5 IELTS PREMIUM PODCAST LECTURES PROCESSED SUCCESSFULLY:');
  console.table(results);
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
