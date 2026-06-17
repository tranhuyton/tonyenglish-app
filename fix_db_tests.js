const fs = require('fs');
const { createClient } = require('@supabase/supabase-js');
const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  let count = 0;
  let page = 0;
  const pageSize = 100;
  while (true) {
    const { data: tests, error } = await supabase.from('tests').select('id, title, test_type, content_json').range(page * pageSize, (page + 1) * pageSize - 1);
    if (error) { console.error(error); return; }
    if (!tests || tests.length === 0) break;
    
    for (const t of tests) {
      const cSkill = t.content_json?.basicInfo?.skill;
      if (cSkill && t.test_type !== cSkill) {
        console.log(`Updating ${t.title} (${t.id}) from ${t.test_type} to ${cSkill}`);
        await supabase.from('tests').update({ test_type: cSkill }).eq('id', t.id);
        count++;
      } else if (!cSkill && t.test_type === 'vocabulary') {
        console.log(`Updating ${t.title} (${t.id}) from vocabulary to Standard-Reading (defaulting)`);
        await supabase.from('tests').update({ test_type: 'Standard-Reading' }).eq('id', t.id);
        count++;
      }
    }
    page++;
  }
  console.log('Total fixed:', count);
}
run();
