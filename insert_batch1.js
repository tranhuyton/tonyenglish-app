const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const folderId = '64f471c2-e1c0-431b-bd81-f76aa1c0dc61'; // Volume 2 folder
  const unitsToInsert = [2, 3, 4, 5]; // Batch 1
  
  for (let unitNum of unitsToInsert) {
    const filename = `unit${unitNum}.json`;
    if (!fs.existsSync(filename)) {
      console.log(`File ${filename} not found, skipping...`);
      continue;
    }
    
    console.log(`Processing Unit ${unitNum}...`);
    try {
      const contentStr = fs.readFileSync(filename, 'utf-8');
      const contentJson = JSON.parse(contentStr);
      
      const { data: existingData } = await supabase
        .from('tests')
        .select('id')
        .eq('title', `Unit ${unitNum}`)
        .eq('folder_id', folderId)
        .single();
        
      if (existingData) {
        console.log(`Unit ${unitNum} exists. Updating...`);
        const { error } = await supabase
          .from('tests')
          .update({ content_json: contentJson })
          .eq('id', existingData.id);
        if (error) console.error(`Error updating Unit ${unitNum}:`, error);
        else console.log(`Unit ${unitNum} successfully updated!`);
      } else {
        console.log(`Unit ${unitNum} does not exist. Inserting...`);
        const { error } = await supabase
          .from('tests')
          .insert({
            title: `Unit ${unitNum}`,
            folder_id: folderId,
            content_json: contentJson,
            order_index: unitNum
          });
        if (error) console.error(`Error inserting Unit ${unitNum}:`, error);
        else console.log(`Unit ${unitNum} successfully inserted!`);
      }
    } catch (e) {
      console.error(`Error processing Unit ${unitNum}:`, e.message);
    }
  }
}

run();
