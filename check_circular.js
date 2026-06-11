const fs = require('fs');
function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}
const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_ANON_KEY = getEnv('VITE_SUPABASE_ANON_KEY');

async function checkFolders() {
  const { data: testFolders } = await fetch(`${SUPABASE_URL}/rest/v1/test_folders?select=id,parent_id,name`, {
    headers: { 'apikey': SUPABASE_ANON_KEY, 'Authorization': `Bearer ${SUPABASE_ANON_KEY}` }
  }).then(r => r.json()).then(r => ({ data: r }));
  
  if (testFolders) {
    for (let f of testFolders) {
      if (f.id === f.parent_id) console.log('CIRCULAR TEST FOLDER:', f);
      // Check deeper circular
      let curr = f;
      let visited = new Set();
      while(curr) {
         if (visited.has(curr.id)) {
            console.log('DEEP CIRCULAR TEST FOLDER:', f.id, f.name);
            break;
         }
         visited.add(curr.id);
         curr = testFolders.find(x => x.id === curr.parent_id);
      }
    }
  }
  
  const { data: pdfFolders } = await fetch(`${SUPABASE_URL}/rest/v1/pdf_folders?select=id,parentId,name`, {
    headers: { 'apikey': SUPABASE_ANON_KEY, 'Authorization': `Bearer ${SUPABASE_ANON_KEY}` }
  }).then(r => r.json()).then(r => ({ data: r }));
  
  if (pdfFolders) {
    for (let f of pdfFolders) {
      if (f.id === f.parentId) console.log('CIRCULAR PDF FOLDER:', f);
      let curr = f;
      let visited = new Set();
      while(curr) {
         if (visited.has(curr.id)) {
            console.log('DEEP CIRCULAR PDF FOLDER:', f.id, f.name);
            break;
         }
         visited.add(curr.id);
         curr = pdfFolders.find(x => x.id === curr.parentId);
      }
    }
  }
  console.log("Check complete.");
}
checkFolders();
