const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}
const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));
async function run() {
  const { data: courses, error: err1 } = await supabase.from('courses').select('id, title').ilike('title', '%Grammar%');
  if (err1) return console.error('Err1:', err1);
  if (!courses || courses.length === 0) return console.log('Course not found');
  const courseId = courses[0].id;
  console.log('Course:', courses[0].title);
  
  const { data: folders, error: err2 } = await supabase.from('folders').select('id, title, parent_id, thumbnail_url').eq('course_id', courseId).order('display_order');
  if (err2) return console.error('Err2:', err2);
  
  const rootFolder = folders.find(f => f.title.includes('Vocabulary Organiser'));
  if (!rootFolder) return console.log('Root folder not found');
  
  const subfolders = folders.filter(f => f.parent_id === rootFolder.id);
  console.log('Found ' + subfolders.length + ' subfolders');
  fs.writeFileSync('vocab_folders.json', JSON.stringify(subfolders.map(f => ({id: f.id, title: f.title})), null, 2));
}
run();