const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

async function uploadImage() {
  const imagesDir = 'C:\\\\Users\\\\Tony\\\\.gemini\\\\antigravity\\\\brain\\\\a493a760-b548-4817-97c0-13b4ee51e9fa';
  const files = fs.readdirSync(imagesDir).filter(f => f.startsWith('ielts_cam_parent') && f.endsWith('.png'));
  
  if (files.length === 0) return console.log('No parent image found');
  const imageFile = files[0];
  
  const filePath = path.join(imagesDir, imageFile);
  const fileData = fs.readFileSync(filePath);
  
  const fileName = `ielts_thumbnail_${Date.now()}_${imageFile}`;
  
  const { data, error } = await supabase.storage.from('test_assets').upload(fileName, fileData, {
    contentType: 'image/png'
  });
  
  if (error) return console.error('Error uploading:', error);
  
  const { data: urlData } = supabase.storage.from('test_assets').getPublicUrl(fileName);
  if (urlData && urlData.publicUrl) {
    const { error: updateError } = await supabase.from('folders').update({ thumbnail_url: urlData.publicUrl }).eq('title', 'Cambridge Test');
    if (updateError) {
       console.error('Error updating DB:', updateError);
    } else {
       console.log('Successfully updated Cambridge Test folder image!');
    }
  }
}
uploadImage();
