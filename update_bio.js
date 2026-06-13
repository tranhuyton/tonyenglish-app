const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}

const supabaseUrl = getEnv('VITE_SUPABASE_URL');
const supabaseKey = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');

if (!supabaseUrl || !supabaseKey) {
   console.error("Missing supabase credentials");
   process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseKey);
const BUCKET = 'documents';

async function uploadAndGetUrl(filePath, destName) {
  const fileBuffer = fs.readFileSync(filePath);
  const { data, error } = await supabase.storage.from(BUCKET).upload(destName, fileBuffer, {
    contentType: 'image/png',
    upsert: true
  });
  if (error) {
    console.error(`Failed to upload ${destName}:`, error);
    return null;
  }
  const { data: publicUrlData } = supabase.storage.from(BUCKET).getPublicUrl(destName);
  return publicUrlData.publicUrl;
}

async function run() {
  const basePath = 'C:\\Users\\Tony\\.gemini\\antigravity\\brain\\a493a760-b548-4817-97c0-13b4ee51e9fa';
  const bioCoverPath = path.join(basePath, 'igcse_biology_folder_1781281087317.png');

  console.log("Uploading biology folder image...");
  const bioFolderUrl = await uploadAndGetUrl(bioCoverPath, 'covers/bio_folder.png');
  console.log("URL:", bioFolderUrl);

  const { data: folders } = await supabase.from('folders').select('id, title');
  const bioFold = folders.find(f => f.title.toLowerCase().includes('biology'));
  
  if (bioFold && bioFolderUrl) {
    console.log(`Updating Folder ${bioFold.title}...`);
    await supabase.from('folders').update({ cover_image: bioFolderUrl }).eq('id', bioFold.id);
    console.log('Success!');
  }
}

run();
