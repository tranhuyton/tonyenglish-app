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

const file = process.argv[2];
if (!file) {
  console.error("Please provide a json file");
  process.exit(1);
}

const contentJson = JSON.parse(fs.readFileSync(file, 'utf-8'));
const unitTitle = contentJson.basicInfo.title;

async function run() {
  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';

  const { data: existing, error: err2 } = await supabase.from('tests').select('id').eq('title', unitTitle).single();

  if (existing) {
    const { data, error } = await supabase
      .from('tests')
      .update({ content_json: contentJson })
      .eq('id', existing.id);
    if (error) console.error('Error updating:', error);
    else console.log(`${unitTitle} updated in Supabase successfully!`);
  } else {
    const { data, error } = await supabase
      .from('tests')
      .insert({
        title: unitTitle,
        test_type: contentJson.basicInfo.skill || 'Standard-Reading',
        course_id: courseId,
        content_json: contentJson,
        is_published: true
      });
    if (error) console.error('Error inserting:', error);
    else console.log(`${unitTitle} inserted into Supabase successfully!`);
  }
}

run();
