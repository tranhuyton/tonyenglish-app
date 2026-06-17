const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);

const url = urlMatch[1].trim();
const key = keyMatch[1].trim();
const supabase = createClient(url, key);

async function run() {
  const { data, error } = await supabase.from('tests').select('*').eq('title', 'Unit 2').single();
  if (error) {
    console.error(error);
    return;
  }
  let c = data.content_json;
  
  let html = c.parts[0].content;
  html = html.replace(/<img src="\/unit2_wordlist\.png"[^>]*>/, '<img src="/unit2_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit2_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />');
  
  c.parts[0].content = html;
  
  const { error: updateError } = await supabase.from('tests').update({ content_json: c }).eq('id', data.id);
  if (updateError) {
    console.error('Update failed', updateError);
  } else {
    console.log('Unit 2 updated successfully!');
  }
}
run();
