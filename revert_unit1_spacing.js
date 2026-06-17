const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const folderId = '64f471c2-e1c0-431b-bd81-f76aa1c0dc61'; // Volume 2 folder
  const { data: testData } = await supabase.from('tests').select('content_json').eq('title', 'Unit 1').eq('folder_id', folderId).single();
  
  if (testData && testData.content_json) {
    let content = testData.content_json;
    
    // Find the comprehensive reading part
    let readingPart = content.parts.find(p => p.id === 'part2' || p.title === 'Comprehensive Reading');
    if (readingPart) {
      let html = readingPart.content;
      
      // Revert paragraph styles
      html = html.replace(/<p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">/g, '<p style="margin-bottom: 1rem;">');
      
      readingPart.content = html;
      
      const { error } = await supabase.from('tests').update({ content_json: content }).eq('title', 'Unit 1').eq('folder_id', folderId);
      if (error) {
        console.error('Error updating:', error);
      } else {
        console.log('Successfully reverted Unit 1 HTML spacing!');
      }
    }
  }
}
run();
