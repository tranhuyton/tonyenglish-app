const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);

const url = urlMatch[1].trim();
const key = keyMatch[1].trim();
const supabase = createClient(url, key);

async function run() {
  const { data: courses } = await supabase.from('courses').select('id, title').ilike('title', '%Grammar%');
  console.log("Courses:", courses);
  
  const { data: folders, error } = await supabase.from('folders').select('id, title, course_id, parent_id');
  if (error) console.error("Error:", error);
  console.log("Folders:", folders);
}
run();
