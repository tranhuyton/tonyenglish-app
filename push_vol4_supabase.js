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

async function run() {
  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170'; // Vocabulary course
  const folderId = '0c5a5fc1-bdfa-4773-baf1-3430a7e31ad2'; // Volume 4 folder

  for (let unitNum = 1; unitNum <= 30; unitNum++) {
    const rawPath = `unit${unitNum}_vol4_raw.json`;
    const publicPath = `public/unit${unitNum}_vol4.json`;

    if (!fs.existsSync(rawPath)) {
      console.log(`Skipping Unit ${unitNum}, raw JSON not found`);
      continue;
    }

    try {
      const contentJson = JSON.parse(fs.readFileSync(rawPath, 'utf-8'));
      
      // Save it to public/
      fs.writeFileSync(publicPath, JSON.stringify(contentJson, null, 2));

      const title = `Unit ${unitNum}: Volume 4`;

      const { data: existing, error: err2 } = await supabase.from('tests').select('id').eq('title', title).maybeSingle();

      if (existing) {
        const { data, error } = await supabase
          .from('tests')
          .update({ content_json: contentJson, folder_id: folderId })
          .eq('id', existing.id);
        if (error) console.error(`Error updating ${title}:`, error);
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
        if (error) console.error(`Error inserting ${title}:`, error);
        else console.log(`${title} inserted into Supabase successfully!`);
      }
    } catch (e) {
      console.error(`Failed to parse or upload ${rawPath}:`, e);
    }
  }
}

run();
