$envPath = ".env"; $content = Get-Content $envPath; foreach ($line in $content) { if ($line -match "^VITE_SUPABASE_URL=(.*)") { $env:VITE_SUPABASE_URL = $matches[1] } if ($line -match "^VITE_SUPABASE_ANON_KEY=(.*)") { $env:VITE_SUPABASE_ANON_KEY = $matches[1] } }; node -e "
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);
async function run() {
  const { data, error } = await supabase.from('tests').select('id, content_json->basicInfo->category').limit(1);
  console.log(JSON.stringify(data, null, 2));
}
run();
"
