const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

async function fixTest(title) {
  const { data: testData, error: errFetch } = await supabase.from('tests').select('id, content_json, json_config').eq('title', title);
  if (errFetch || !testData || testData.length === 0) return console.log('Test not found:', title);
  
  const test = testData[0];
  
  // Create deep copies
  const newContentJson = JSON.parse(JSON.stringify(test.content_json));
  const newJsonConfig = JSON.parse(JSON.stringify(test.json_config));
  
  const processParts = (parts) => {
      if (!parts) return;
      parts.forEach(part => {
          if (part.content) {
              // Replace h3 class to text-[24px]
              part.content = part.content.replace(/class="text-xl font-bold mb-4 text-center"/g, 'class="text-[24px] font-bold mb-4 text-center"');
          }
          if (part.sections) {
              part.sections.forEach(section => {
                  if (section.title === 'Section 1') {
                      section.title = '';
                  }
              });
          }
      });
  };
  
  if (newContentJson) processParts(newContentJson.parts);
  if (newJsonConfig) processParts(newJsonConfig.parts);
  
  const { error: updErr } = await supabase.from('tests').update({
    content_json: newContentJson,
    json_config: newJsonConfig
  }).eq('id', test.id);
  
  if (updErr) console.error('Update error for', title, ':', updErr);
  else console.log('Fixed test successfully:', title);
}

async function run() {
  await fixTest('Chapter 1: Exercise 1');
  await fixTest('Chapter 1: Exercise 2');
}

run();
