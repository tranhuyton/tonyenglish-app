const { createClient } = require('@supabase/supabase-js');

const supabaseUrl = 'https://ubkvzgwespfvrlpjuxkp.supabase.co';
const supabaseKey = 'sb_secret_5huRcnLVzDU92RUpJ6H6mw_zOGBmCNw';
const supabase = createClient(supabaseUrl, supabaseKey);

async function run() {
  // Get all folders
  const { data: folders, error: err1 } = await supabase.from('folders').select('id');
  if (err1) throw err1;
  const folderIds = folders.map(f => f.id);
  
  // Get all tests that have a folder_id
  const { data: tests, error: err2 } = await supabase.from('tests').select('id, folder_id, title').not('folder_id', 'is', null);
  if (err2) throw err2;
  
  // Find orphaned tests
  const orphanedTests = tests.filter(t => !folderIds.includes(t.folder_id));
  console.log(`Found ${orphanedTests.length} orphaned tests.`);
  
  for (const t of orphanedTests) {
    console.log(`Resetting folder_id for test: ${t.title}`);
    await supabase.from('tests').update({ folder_id: null }).eq('id', t.id);
  }
  
  console.log('Cleanup done!');
}

run().catch(console.error);
