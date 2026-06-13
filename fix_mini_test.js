const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

async function run() {
  const { data } = await supabase.from('tests').select('*').eq('title', 'Chapter 1: Mini Test');
  if (data && data.length > 0) {
    const test = data[0];
    const newContentJson = { ...test.content_json };
    newContentJson.parts[0].sections[0].title = '';
    newContentJson.parts[0].sections[0].questionType = 'Trắc nghiệm';
    delete newContentJson.parts[0].sections[0].sectionTitle;
    
    // Fix correct answers to be 'A', 'B', 'C', 'D' instead of numbers
    newContentJson.parts[0].sections[0].questions.forEach(q => {
      if (typeof q.correctAnswer === 'number') {
        q.correctAnswer = String.fromCharCode(65 + q.correctAnswer); // 0 -> A, 1 -> B
      }
    });
    
    await supabase.from('tests').update({ content_json: newContentJson }).eq('id', test.id);
    console.log('Fixed Mini Test record section title, questionType, and correctAnswer');
  }
}

run();
