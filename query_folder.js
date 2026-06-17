const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const { data, error } = await supabase.from('folders').select('*').eq('title', 'Unit 1').eq('course_id', '239a64f0-c106-40e5-a6e2-4e685a0d70fb');
  console.log(data, error);
}
run();
