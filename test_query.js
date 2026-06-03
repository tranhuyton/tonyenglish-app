import { createClient } from '@supabase/supabase-js';
import * as dotenv from 'dotenv';
dotenv.config();
const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);
async function run() {
  const { data, error } = await supabase.from('tests').select('id, content_json->basicInfo->category').limit(1);
  console.log(JSON.stringify(data, null, 2));
  if(error) console.log(error);
}
run();
