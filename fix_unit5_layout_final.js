const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m)[1].trim();

const supabase = createClient(url, key);

async function run() {
  const { data: testData } = await supabase.from('tests').select('content_json').eq('title', 'Unit 5').single();
  
  if (testData && testData.content_json) {
    let content = testData.content_json;
    
    // Find the comprehensive reading part
    let readingPart = content.parts.find(p => p.id === 'part2' || p.title === 'Comprehensive Reading');
    if (readingPart) {
      let html = readingPart.content;
      
      // Remove any img tags
      html = html.replace(/<img[^>]*>/, '');
      
      // Revert paragraph styles exactly to Unit 1
      html = html.replace(/<p style="margin-bottom: 1\.25rem; line-height: 1\.6; color: #374151; font-size: 1\.125rem;">/g, '<p style="margin-bottom: 1rem;">');
      
      // Revert div wrapper exactly to Unit 1
      html = html.replace(/<div style="font-family: Arial, sans-serif;">/, '<div style="font-family: Arial, sans-serif; ">');
      
      readingPart.content = html;
      readingPart.imageUrl = '/unit5_story.png';
      
      const { error } = await supabase.from('tests').update({ content_json: content }).eq('title', 'Unit 5');
      if (error) {
        console.error('Error updating:', error);
      } else {
        console.log('Successfully updated Unit 5 HTML and Image structure!');
      }
    }
  }
  process.exit(0);
}
run();
