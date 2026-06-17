const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);

if (!urlMatch || !keyMatch) {
  console.error("Supabase credentials not found in .env");
  process.exit(1);
}

const url = urlMatch[1].trim();
const key = keyMatch[1].trim();
const supabase = createClient(url, key);

function getEmoji(word) {
  // basic random emoji or deterministic emoji mapping based on word length for simplicity
  const emojis = ['🌟', '🔥', '💧', '🌿', '⚙️', '🛡️', '⚡', '✨', '🎯', '🚀', '💡', '🧠', '💪', '🍎', '🌈', '🧩', '🎨', '🏆', '💎', '🧸'];
  return emojis[word.length % emojis.length];
}

async function run() {
  const unitNum = process.argv[2];
  if (!unitNum) {
    console.error("Usage: node build_supabase_json.js <unit_num>");
    process.exit(1);
  }

  const jsonPath = `unit${unitNum}_raw.json`;
  if (!fs.existsSync(jsonPath)) {
    console.log(`Skipping Unit ${unitNum}, raw json not found.`);
    return;
  }

  const contentJson = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));

  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';
  const folderId = '0f15a9d8-efc3-45ca-8fd3-aaa02ffa914c';
  const title = `Unit ${unitNum}: Volume 3`;

  const { data: existing, error: err2 } = await supabase.from('tests').select('id').eq('title', title).single();

  if (existing) {
    const { data, error } = await supabase
      .from('tests')
      .update({ content_json: contentJson, folder_id: folderId })
      .eq('id', existing.id);
    if (error) console.error('Error updating:', error);
    else console.log(`${title} updated in Supabase successfully!`);
  } else {
    const { data, error } = await supabase
      .from('tests')
      .insert({
        title: title,
        test_type: 'vocabulary',
        course_id: courseId,
        folder_id: folderId,
        content_json: contentJson,
        is_published: true
      });
    if (error) console.error('Error inserting:', error);
    else console.log(`${title} inserted into Supabase successfully!`);
  }
}

run();
