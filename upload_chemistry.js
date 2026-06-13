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

const chemImages = [
  { prefix: 'C1', file: 'c1_matter_1781286577224.png' },
  { prefix: 'C2', file: 'c2_atoms_1781286588754.png' },
  { prefix: 'C3', file: 'c3_stoichiometry_1781286598747.png' },
  { prefix: 'C4', file: 'c4_electrochemistry_1781286609974.png' },
  { prefix: 'C5', file: 'c5_energetics_1781286619471.png' },
  { prefix: 'C6', file: 'c6_reactions_1781286630356.png' },
  { prefix: 'C7', file: 'c7_acids_1781286646208.png' },
  { prefix: 'C8', file: 'c8_table_1781286658689.png' },
  { prefix: 'C9', file: 'c9_metals_1781286670181.png' },
  { prefix: 'C10', file: 'c10_chemistry_1781286681278.png' },
  { prefix: 'C11', file: 'c11_organic_1781286690719.png' },
  { prefix: 'C12', file: 'c12_experimental_1781286701742.png' }
];

async function run() {
  const { data: folders } = await supabase.from('folders').select('id, title, parent_id');
  const cFolders = folders.filter(f => f.parent_id && f.title.startsWith('C'));

  for (let mapping of chemImages) {
    const folder = cFolders.find(f => f.title.startsWith(mapping.prefix + ':'));
    if (!folder) continue;

    const filePath = `C:\\Users\\Tony\\.gemini\\antigravity\\brain\\a493a760-b548-4817-97c0-13b4ee51e9fa\\${mapping.file}`;
    if (!fs.existsSync(filePath)) {
      console.log('File not found:', filePath);
      continue;
    }

    const fileExt = path.extname(filePath);
    const fileName = `chemistry_${mapping.prefix}_${Date.now()}${fileExt}`;
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
  console.log('Done Chemistry images!');
}

run();
