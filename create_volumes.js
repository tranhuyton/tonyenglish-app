const fs = require('fs');
const { createClient } = require('@supabase/supabase-js');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';
  const parentFolderId = '4896ce76-eabe-4331-9bdd-41d615af2061'; // "4000 English Words"

  for (let i = 2; i <= 6; i++) {
    const folderName = `Volume ${i}`;
    
    // Check if it already exists
    const { data: existing } = await supabase
      .from('folders')
      .select('*')
      .eq('title', folderName)
      .eq('parent_id', parentFolderId)
      .single();
      
    if (existing) {
      console.log(`${folderName} already exists.`);
      continue;
    }
    
    const { data: newFolder, error: folderErr } = await supabase
      .from('folders')
      .insert({
        title: folderName,
        parent_id: parentFolderId,
        course_id: courseId,
        display_order: i
      });

    if (folderErr) {
      console.error(`Error creating ${folderName}:`, folderErr);
    } else {
      console.log(`Successfully created ${folderName}`);
    }
  }
}

run();
