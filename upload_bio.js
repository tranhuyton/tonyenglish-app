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

const bioImages = [
  { prefix: 'B1', file: 'b1_living_1781286748312.png' },
  { prefix: 'B2', file: 'b2_cells_1781286758068.png' },
  { prefix: 'B3', file: 'b3_movement_1781286768337.png' },
  { prefix: 'B4', file: 'b4_molecules_1781286778133.png' },
  { prefix: 'B5', file: 'b5_enzymes_1781286790167.png' },
  { prefix: 'B6', file: 'b6_plant_1781286799615.png' },
  { prefix: 'B7', file: 'b7_human_1781286811184.png' },
  { prefix: 'B8', file: 'b8_transport_plants_1781286820777.png' },
  { prefix: 'B9', file: 'b9_transport_animals_1781286832508.png' },
  { prefix: 'B10', file: 'b10_diseases_1781286850176.png' },
  { prefix: 'B11', file: 'b11_gas_1781286859938.png' },
  { prefix: 'B12', file: 'b12_respiration_1781286869966.png' },
  { prefix: 'B13', file: 'b13_coordination_1781286882801.png' },
  { prefix: 'B14', file: 'b14_drugs_1781286893702.png' },
  { prefix: 'B15', file: 'b15_reproduction_1781286905318.png' },
  { prefix: 'B16', file: 'b16_inheritance_1781286916369.png' },
  { prefix: 'B17', file: 'b17_variation_1781286927535.png' },
  { prefix: 'B18', file: 'b18_organisms_1781286938802.png' },
  { prefix: 'B19', file: 'b19_ecosystems_1781286949352.png' }
];

async function run() {
  const { data: folders } = await supabase.from('folders').select('id, title, parent_id');
  const bFolders = folders.filter(f => f.parent_id && f.title.startsWith('B'));

  for (let mapping of bioImages) {
    const folder = bFolders.find(f => f.title.startsWith(mapping.prefix + ':'));
    if (!folder) continue;

    const filePath = `C:\\Users\\Tony\\.gemini\\antigravity\\brain\\a493a760-b548-4817-97c0-13b4ee51e9fa\\${mapping.file}`;
    if (!fs.existsSync(filePath)) {
      console.log('File not found:', filePath);
      continue;
    }

    const fileExt = path.extname(filePath);
    const fileName = `biology_${mapping.prefix}_${Date.now()}${fileExt}`;
    const fileBuffer = fs.readFileSync(filePath);

    console.log(`Uploading ${fileName}...`);
    const { error: uploadError } = await supabase.storage
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
  console.log('Done Biology images!');
}

run();
