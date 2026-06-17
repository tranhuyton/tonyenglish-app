const fs = require('fs');
const { createClient } = require('@supabase/supabase-js');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
  const parentFolderId = '23c5be28-2449-46a4-a459-f22c6f82895f'; // "Reading Strategies"

  for (let i = 1; i <= 8; i++) {
    const folderName = `Unit ${i}`;
    
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
