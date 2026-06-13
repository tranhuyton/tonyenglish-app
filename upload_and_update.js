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
  const images = {
     chemCover: path.join(basePath, 'igcse_chemistry_cover_1781224523985.png'),
     mathsFolder: path.join(basePath, 'igcse_maths_folder_1781224533547.png'),
     physicsFolder: path.join(basePath, 'igcse_physics_folder_1781224545594.png'),
     chemFolder: path.join(basePath, 'igcse_chemistry_folder_1781224558079.png')
  };

  console.log("Uploading images...");
  const chemCoverUrl = await uploadAndGetUrl(images.chemCover, 'covers/chem_course_cover.png');
  const mathsFolderUrl = await uploadAndGetUrl(images.mathsFolder, 'covers/maths_folder.png');
  const physicsFolderUrl = await uploadAndGetUrl(images.physicsFolder, 'covers/physics_folder.png');
  const chemFolderUrl = await uploadAndGetUrl(images.chemFolder, 'covers/chem_folder.png');

  console.log("URLs obtained:");
  console.log({ chemCoverUrl, mathsFolderUrl, physicsFolderUrl, chemFolderUrl });

  // Update Chemistry Course
  const { data: courses } = await supabase.from('courses').select('id, title');
  const chemCourse = courses.find(c => c.title.toLowerCase().includes('chemistry') && c.title.includes('IGCSE'));
  if (chemCourse && chemCoverUrl) {
    console.log(`Updating Course ${chemCourse.title}...`);
    await supabase.from('courses').update({ thumbnail: chemCoverUrl }).eq('id', chemCourse.id);
  }

  // Update Folders
  const { data: folders } = await supabase.from('folders').select('id, title');
  
  const chemFold = folders.find(f => f.title.toLowerCase().includes('chemistry'));
  if (chemFold && chemFolderUrl) {
    console.log(`Updating Folder ${chemFold.title}...`);
    await supabase.from('folders').update({ cover_image: chemFolderUrl }).eq('id', chemFold.id);
  }
  
  const mathFold = folders.find(f => f.title.toLowerCase().includes('math'));
  if (mathFold && mathsFolderUrl) {
    console.log(`Updating Folder ${mathFold.title}...`);
    await supabase.from('folders').update({ cover_image: mathsFolderUrl }).eq('id', mathFold.id);
  }

  const physFold = folders.find(f => f.title.toLowerCase().includes('physics'));
  if (physFold && physicsFolderUrl) {
    console.log(`Updating Folder ${physFold.title}...`);
    await supabase.from('folders').update({ cover_image: physicsFolderUrl }).eq('id', physFold.id);
  }

  console.log("Done updating!");
}

run();
