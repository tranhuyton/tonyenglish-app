const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const { data, error } = await supabase.from('tests').select('title, content_json');
  if (error) {
    console.error("DB Error:", error);
    return;
  }
  if (!data) {
    console.log("Data is null");
    return;
  }
  data.forEach(d => {
    if (d.content_json && d.content_json.parts && d.content_json.parts[1]) {
      const content = d.content_json.parts[1].content;
      if (content.includes('Lion and the Rabbit') || d.title.includes('Unit 1')) {
        console.log(`\n--- ${d.title} ---`);
        console.log(content);
      }
    }
  });
}
run();
