const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY || process.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.error("Missing Supabase env vars");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseKey);

// Maps folder id to the local file path
const updates = [
  // to be filled
];

async function main() {
  for (const item of updates) {
    const { folderId, filePath, fileName } = item;
    console.log(`Processing folder ${folderId}...`);
    
    // Read file
    const fileContent = fs.readFileSync(filePath);
    
    // Upload to Supabase
    const storagePath = `folder_images/${fileName}`;
    console.log(`Uploading to documents bucket at ${storagePath}...`);
    const { data: uploadData, error: uploadError } = await supabase.storage
      .from('documents')
      .upload(storagePath, fileContent, { upsert: true, contentType: 'image/png' });
      
    if (uploadError) {
      console.error(`Error uploading ${fileName}:`, uploadError);
      continue;
    }
    
    // Get public URL
    const { data: publicUrlData } = supabase.storage
      .from('documents')
      .getPublicUrl(storagePath);
      
    const publicUrl = publicUrlData.publicUrl;
    console.log(`Public URL: ${publicUrl}`);
    
    // Update folder thumbnail_url
    console.log(`Updating folder ${folderId}...`);
    const { error: updateError } = await supabase
      .from('folders')
      .update({ thumbnail_url: publicUrl })
      .eq('id', folderId);
      
    if (updateError) {
      console.error(`Error updating folder ${folderId}:`, updateError);
    } else {
      console.log(`Successfully updated folder ${folderId}.`);
    }
  }
}

main().catch(console.error);
