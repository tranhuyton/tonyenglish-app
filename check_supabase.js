const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}

const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_SERVICE_ROLE_KEY = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

async function check() {
  const { data: folders, error } = await supabase.from('test_folders').select('id, parent_id, name');
  if (error) { console.error(error); return; }
  
  let found = false;
  for (let f of folders) {
    if (f.id === f.parent_id) {
       console.log('SELF REFERENTIAL FOLDER:', f);
       found = true;
    }
    
    let curr = f;
    let visited = new Set();
    while(curr) {
       if (visited.has(curr.id)) {
          console.log('CIRCULAR LOOP DETECTED:', f.name, f.id, '->', curr.name, curr.id);
          found = true;
          break;
       }
       visited.add(curr.id);
       curr = folders.find(x => x.id === curr.parent_id);
    }
  }
  
  if (!found) console.log("No circular loops found in test_folders.");
}
check();
