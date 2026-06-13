const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY'));

async function updateImages() {
  const { data: courses } = await supabase.from('courses').select('id, title');
  const chemistryCourse = courses.find(c => c.title.includes('Chemistry'));
  
  if (chemistryCourse) {
     console.log('Updating Chemistry Course:', chemistryCourse.title);
     // Let's do the update later, first just print to make sure we found it.
  }
  
  const { data: folders } = await supabase.from('test_folders').select('id, name');
  const chemistryFolder = folders.find(f => f.name.includes('Chemistry'));
  const physicsFolder = folders.find(f => f.name.includes('Physics'));
  const mathsFolder = folders.find(f => f.name.includes('Maths'));
  
  console.log('Folders found:');
  if (chemistryFolder) console.log('Chemistry Folder:', chemistryFolder.name);
  if (physicsFolder) console.log('Physics Folder:', physicsFolder.name);
  if (mathsFolder) console.log('Maths Folder:', mathsFolder.name);
}
updateImages();
