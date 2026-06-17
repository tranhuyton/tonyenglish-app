const fs = require('fs');
const { createClient } = require('@supabase/supabase-js');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';
  const parentFolderId = '4896ce76-eabe-4331-9bdd-41d615af2061'; // "4000 English Words"

  // 1. Create the new folder "Volume 1"
  let { data: newFolder, error: folderErr } = await supabase
    .from('folders')
    .insert({
      title: 'Volume 1',
      parent_id: parentFolderId,
      course_id: courseId,
      display_order: 1
    })
    .select()
    .single();

  if (folderErr) {
    console.error('Error creating folder:', folderErr);
    // If it already exists, let's just fetch it
    const { data: existing } = await supabase
      .from('folders')
      .select('*')
      .eq('title', 'Volume 1')
      .eq('parent_id', parentFolderId)
      .single();
    if (existing) newFolder = existing;
    else return;
  }

  console.log('Created/Found Volume 1 folder with ID:', newFolder.id);

  // 2. Fetch and update Unit 1 to 30
  for (let i = 1; i <= 30; i++) {
    const oldTitle = `Unit ${i}`;
    const newTitle = `Unit ${i}: Volume 1`;

    const { data: test, error: testErr } = await supabase
      .from('tests')
      .select('*')
      .eq('title', oldTitle)
      .single();

    if (testErr || !test) {
      console.log(`Could not find ${oldTitle}`);
      continue;
    }

    // Update the content_json
    let c = test.content_json;
    if (c && c.basicInfo) {
      c.basicInfo.title = newTitle;
    }

    // Update the DB record
    const { error: updateErr } = await supabase
      .from('tests')
      .update({
        title: newTitle,
        folder_id: newFolder.id,
        content_json: c
      })
      .eq('id', test.id);

    if (updateErr) {
      console.error(`Error updating ${oldTitle}:`, updateErr);
    } else {
      console.log(`Successfully updated ${oldTitle} to ${newTitle} and moved to Volume 1`);
    }
  }
}

run();
