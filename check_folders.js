const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

const supabase = createClient(
  process.env.VITE_SUPABASE_URL,
  process.env.VITE_SUPABASE_ANON_KEY
);

async function run() {
  const { data: courses } = await supabase.from('courses').select('id, title').ilike('title', '%Geography%');
  const courseId = courses[0].id;
  
  const { data: folders, error } = await supabase.from('folders').select('*').eq('course_id', courseId);
  if (error) console.error(error);
  else console.log(folders);
}

run();
