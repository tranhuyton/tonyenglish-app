const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

async function uploadImage(imagePrefix) {
  const imagesDir = 'C:\\\\Users\\\\Tony\\\\.gemini\\\\antigravity\\\\brain\\\\a493a760-b548-4817-97c0-13b4ee51e9fa';
  const files = fs.readdirSync(imagesDir).filter(f => f.startsWith(imagePrefix) && f.endsWith('.png'));
  
  if (files.length === 0) return null;
  const imageFile = files[0];
  const filePath = path.join(imagesDir, imageFile);
  const fileData = fs.readFileSync(filePath);
  
  const fileName = `ielts_thumbnail_${Date.now()}_${imageFile}`;
  const { error } = await supabase.storage.from('test_assets').upload(fileName, fileData, { contentType: 'image/png' });
  if (error) {
     console.error('Error uploading:', error);
     return null;
  }
  
  const { data: urlData } = supabase.storage.from('test_assets').getPublicUrl(fileName);
  return urlData?.publicUrl || null;
}

async function run() {
  const { data: courses } = await supabase.from('courses').select('id, title').ilike('title', '%IELTS Premium%');
  if (!courses || courses.length === 0) return console.log('Course not found');
  const courseId = courses[0].id;

  // 1. Upload parent image
  const parentImageUrl = await uploadImage('ielts_crash_parent_');
  
  // 2. Insert Parent Folder
  const { data: parentFolder, error: errParent } = await supabase.from('folders').insert([{
    course_id: courseId,
    title: 'Crash Course',
    parent_id: null,
    thumbnail_url: parentImageUrl,
    display_order: 2 // Assuming Cambridge Test is 1
  }]).select().single();
  
  if (errParent) return console.error('Error creating parent folder:', errParent);
  console.log('Created parent folder:', parentFolder.title);

  // 3. Create Child Folders
  for (let i = 1; i <= 7; i++) {
    const childTitle = `Chapter ${i}`;
    const childImageUrl = await uploadImage(`ielts_crash_chap_${i}_`);
    
    const { error: errChild } = await supabase.from('folders').insert([{
      course_id: courseId,
      title: childTitle,
      parent_id: parentFolder.id,
      thumbnail_url: childImageUrl,
      display_order: i
    }]);
    
    if (errChild) console.error(`Error creating ${childTitle}:`, errChild);
    else console.log(`Created ${childTitle}`);
  }
  
  console.log('All done!');
}
run();
