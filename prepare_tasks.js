const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}

const supabaseUrl = getEnv('VITE_SUPABASE_URL');
const supabaseKey = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');
const supabase = createClient(supabaseUrl, supabaseKey);

async function run() {
  const { data: folders } = await supabase.from('folders').select('id, title, parent_id');
  const rootBio = folders.find(f => f.title.includes('Biology:'));
  const rootChem = folders.find(f => f.title.includes('Chemistry:'));
  const rootPhys = folders.find(f => f.title.includes('Physics:'));

  const getSubFolders = (parentId) => folders.filter(f => f.parent_id === parentId).map(f => ({ id: f.id, title: f.title }));

  const tasks = {
    biology: getSubFolders(rootBio?.id),
    chemistry: getSubFolders(rootChem?.id),
    physics: getSubFolders(rootPhys?.id)
  };

  fs.writeFileSync('image_generation_tasks.json', JSON.stringify(tasks, null, 2));
  console.log("Tasks saved to image_generation_tasks.json");
}
run();
