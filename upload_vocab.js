const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

async function uploadImages() {
  const folders = JSON.parse(fs.readFileSync('vocab_folders.json', 'utf-8'));
  const imagesDir = 'C:\\Users\\Tony\\.gemini\\antigravity\\brain\\a493a760-b548-4817-97c0-13b4ee51e9fa';
  
  const files = fs.readdirSync(imagesDir).filter(f => f.startsWith('vocab_') && f.endsWith('.png'));
  
  for (const folder of folders) {
    const match = folder.title.match(/Section (\d+):/i);
    if (!match) continue;
    
    const sectionNum = match[1];
    
    // Find all files matching the prefix and get the latest one
    const matchingFiles = files.filter(f => f.startsWith(`vocab_${sectionNum}_`));
    let imageFile = null;
    let latestTime = 0;
    for (const f of matchingFiles) {
      const stats = fs.statSync(path.join(imagesDir, f));
      if (stats.mtimeMs > latestTime) {
        latestTime = stats.mtimeMs;
        imageFile = f;
      }
    }
    
    if (imageFile) {
      console.log(`Processing ${folder.title} with ${imageFile}`);
      const filePath = path.join(imagesDir, imageFile);
      const fileData = fs.readFileSync(filePath);
      
      const fileName = `vocab_thumbnail_${Date.now()}_${imageFile}`;
      
      const { data, error } = await supabase.storage.from('test_assets').upload(fileName, fileData, {
        contentType: 'image/png'
      });
      
      if (error) {
        console.error('Error uploading:', error);
        continue;
      }
      
      const { data: urlData } = supabase.storage.from('test_assets').getPublicUrl(fileName);
      if (urlData && urlData.publicUrl) {
        const { error: updateError } = await supabase.from('folders').update({ thumbnail_url: urlData.publicUrl }).eq('id', folder.id);
        if (updateError) {
           console.error('Error updating DB:', updateError);
        } else {
           console.log(`Successfully updated ${folder.title}`);
        }
      }
    } else {
      console.log(`No image found for ${folder.title}`);
    }
  }
}

uploadImages().then(() => console.log('Done'));
