const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

async function main() {
  const { data: courses, error } = await supabase.from('courses').select('id, title');
  if (error) {
    console.error('Error fetching courses:', error);
    return;
  }
  console.log('--- ALL COURSES ---');
  for (const c of courses) {
    if (c.title.toLowerCase().includes('ielts') || c.title.toLowerCase().includes('premium')) {
      console.log(`Course: [${c.id}] ${c.title}`);
      const { data: mods } = await supabase
        .from('lecture_modules')
        .select('id, title, order_index')
        .eq('course_id', c.id)
        .order('order_index');
      console.log('  Modules:');
      for (const m of mods || []) {
        console.log(`    - [${m.id}] ${m.title} (order: ${m.order_index})`);
        const { data: lecs } = await supabase
          .from('lectures')
          .select('id, title, order_index')
          .eq('module_id', m.id)
          .order('order_index');
        for (const l of lecs || []) {
          console.log(`        * [${l.id}] ${l.title} (order: ${l.order_index})`);
        }
      }
    }
  }
}

main();
