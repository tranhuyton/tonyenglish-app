const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);

if (!urlMatch || !keyMatch) {
  console.error("Supabase credentials not found in .env");
  process.exit(1);
}

const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb'; // Reading Strategies course
  const folderId = '051f233b-dd5d-46d4-b851-3a15779ea39e'; // Unit 1 folder

  const dirPath = 'src/data/Unit 1';
  const files = fs.readdirSync(dirPath);

  for (const file of files) {
    if (!file.endsWith('.json')) continue;
    
    const filePath = path.join(dirPath, file);
    const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    
    const title = data.title;
    
    const contentJson = {
      basicInfo: {
        title: title,
        courseId: courseId,
        skill: "IELTS-Reading",
        category: "exercise",
        timeLimit: "40"
      },
      parts: data.content_json.parts
    };

    const payload = {
      title: title,
      test_type: "IELTS-Reading",
      course_id: courseId,
      folder_id: folderId,
      content_json: contentJson,
      is_published: true
    };

    const { data: existing, error: err1 } = await supabase.from('tests').select('id').eq('title', title).eq('course_id', courseId).maybeSingle();

    if (existing) {
      const { error } = await supabase.from('tests').update(payload).eq('id', existing.id);
      if (error) console.error('Error updating', title, error);
      else console.log('Updated', title);
    } else {
      const { error } = await supabase.from('tests').insert(payload);
      if (error) console.error('Error inserting', title, error);
      else console.log('Inserted', title);
    }
  }
}

run();
