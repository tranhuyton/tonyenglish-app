const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const dotenv = require('dotenv');
dotenv.config();

const supabase = createClient(
  process.env.VITE_SUPABASE_URL,
  process.env.VITE_SUPABASE_SERVICE_ROLE_KEY
);

async function run() {
  const { data } = await supabase.from('tests').select('title, content_json');
  for (let d of data) {
    if (!d.content_json) continue;
    const str = JSON.stringify(d.content_json);
    const matches = str.match(/src="([^"]+)"/g);
    if (matches && !d.title.includes('Unit 3')) {
      console.log(d.title, matches.slice(0, 2).join(', '));
    }
  }
}
run();
