const { createClient } = require('@supabase/supabase-js');
const supabaseUrl = 'https://ubkvzgwespfvrlpjuxkp.supabase.co';
const supabaseKey = 'sb_secret_5huRcnLVzDU92RUpJ6H6mw_zOGBmCNw'; 
const supabase = createClient(supabaseUrl, supabaseKey);

async function fixTests() {
  const { data, error } = await supabase.from('tests').select('id, content_json').like('title', 'Grammar:%');
  if (error) {
    console.error(error);
    return;
  }
  
  let count = 0;
  for (const test of data) {
    if (typeof test.content_json === 'string') {
      try {
        const parsed = JSON.parse(test.content_json);
        await supabase.from('tests').update({ content_json: parsed }).eq('id', test.id);
        count++;
        console.log(`Fixed test: ${test.id}`);
      } catch (e) {
        console.error(`Failed to parse test: ${test.id}`, e);
      }
    }
  }
  console.log(`Successfully fixed ${count} tests!`);
}

fixTests();
