const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(^=(.*)$, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}
const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY'));

async function run() {
  const { data: courses } = await supabase.from('courses').select('id, title, thumbnail');
  console.log('Courses:', courses.filter(c => c.title.includes('IGCSE')));
  
  const { data: folders } = await supabase.from('test_folders').select('id, name, cover_image');
  console.log('Folders:', folders.filter(f => f.name.includes('IGCSE')));
}
run();
