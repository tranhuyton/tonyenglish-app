const fs = require('fs');
function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}
const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_SERVICE_ROLE_KEY = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');

async function testDupe() {
  const { data: fullTest } = await fetch(`${SUPABASE_URL}/rest/v1/tests?limit=1&select=*`, {
    headers: { 'apikey': SUPABASE_SERVICE_ROLE_KEY, 'Authorization': `Bearer ${SUPABASE_SERVICE_ROLE_KEY}` }
  }).then(r => r.json()).then(r => ({ data: r[0] }));

  console.log('Original test id:', fullTest.id);

  const payload = { 
       title: fullTest.title + ' Copy', 
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
    headers: { 'apikey': SUPABASE_SERVICE_ROLE_KEY, 'Authorization': `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  console.log('Insert status:', res.status, res.statusText);
  if (!res.ok) console.log(await res.json());
}
testDupe();
