const fs = require('fs');
function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}
const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_ANON_KEY = getEnv('VITE_SUPABASE_ANON_KEY');

async function testDupeAnon() {
  const { data: fullTest } = await fetch(`${SUPABASE_URL}/rest/v1/tests?limit=1&select=*`, {
    headers: { 'apikey': SUPABASE_ANON_KEY, 'Authorization': `Bearer ${SUPABASE_ANON_KEY}` }
  }).then(r => r.json()).then(r => ({ data: r[0] }));

  console.log('Anon read test id:', fullTest.id);

  const payload = { 
       title: fullTest.title + ' Anon Copy', 
       course_id: fullTest.course_id, 
       folder_id: fullTest.folder_id, 
       test_type: fullTest.test_type,
       content_json: fullTest.content_json,
       json_config: fullTest.json_config,
       insert_pdf_url: fullTest.insert_pdf_url,
       is_published: false,
       order_index: 100 
  };
  
  const res = await fetch(`${SUPABASE_URL}/rest/v1/tests`, {
    method: 'POST',
    headers: { 'apikey': SUPABASE_ANON_KEY, 'Authorization': `Bearer ${SUPABASE_ANON_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  console.log('Anon Insert status:', res.status, res.statusText);
  if (!res.ok) console.log(await res.json());
}
testDupeAnon();
