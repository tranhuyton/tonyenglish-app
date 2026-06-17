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
  let found = false;
  data.forEach(d => {
    if (d.content_json && d.content_json.parts && d.content_json.parts[1]) {
      const content = d.content_json.parts[1].content;
      if (content.includes('Lion and the Rabbit')) {
        console.log(`\n--- ${d.title} (Lion and Rabbit) ---`);
        console.log(content);
        found = true;
      }
    }
  });
  if (!found) {
     console.log("Could not find 'Lion and the Rabbit'");
     // Just print out any unit from Volume 1 to see its style
     const vol1Data = data.filter(d => d.title.includes('Unit 2'));
     if (vol1Data.length > 0) {
        console.log(`\n--- Unit 2 ---`);
        console.log(vol1Data[0].content_json.parts[1].content);
     }
  }
}
run();
