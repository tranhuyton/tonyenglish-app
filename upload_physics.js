const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

function getEnv(key) {
  const envContent = fs.readFileSync('.env', 'utf-8');
  const match = envContent.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabaseUrl = getEnv('VITE_SUPABASE_URL');
const supabaseKey = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');
const supabase = createClient(supabaseUrl, supabaseKey);

const physicsImages = [
  { prefix: 'P1', file: 'p1_motion_1781286471262.png' },
  { prefix: 'P2', file: 'p2_waves_1781286483487.png' },
  { prefix: 'P3', file: 'p3_electricity_1781286494567.png' },
  { prefix: 'P4', file: 'p4_nuclear_1781286504678.png' },
  { prefix: 'P5', file: 'p5_thermal_1781286516264.png' },
  { prefix: 'P6', file: 'p6_space_1781286528164.png' }
];

async function run() {
  const { data: folders } = await supabase.from('folders').select('id, title, parent_id');
  const physFolders = folders.filter(f => f.parent_id && f.title.startsWith('P'));

  for (let mapping of physicsImages) {
    const folder = physFolders.find(f => f.title.startsWith(mapping.prefix + ':'));
    if (!folder) continue;

    const filePath = `C:\\Users\\Tony\\.gemini\\antigravity\\brain\\a493a760-b548-4817-97c0-13b4ee51e9fa\\${mapping.file}`;
    if (!fs.existsSync(filePath)) {
      console.log('File not found:', filePath);
      continue;
    }

    const fileExt = path.extname(filePath);
    const fileName = `physics_${mapping.prefix}_${Date.now()}${fileExt}`;
    const fileBuffer = fs.readFileSync(filePath);

    console.log(`Uploading ${fileName}...`);
    const { data: uploadData, error: uploadError } = await supabase.storage
      .from('documents')
      .upload(`folder_images/${fileName}`, fileBuffer, {
        contentType: 'image/png',
        upsert: true
      });

    if (uploadError) {
      console.error('Upload error:', uploadError);
      continue;
    }

    const { data: publicUrlData } = supabase.storage
      .from('documents')
      .getPublicUrl(`folder_images/${fileName}`);

    const publicUrl = publicUrlData.publicUrl;

    console.log(`Updating folder ${folder.title}...`);
    await supabase.from('folders').update({ thumbnail_url: publicUrl }).eq('id', folder.id);
  }
  console.log('Done Physics images!');
}

run();
