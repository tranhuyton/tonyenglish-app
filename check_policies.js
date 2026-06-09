const fs = require('fs');
function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(^=(.*)$, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}
const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_SERVICE_ROLE_KEY = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');

async function checkPolicies() {
  const res = await fetch(${SUPABASE_URL}/rest/v1/rpc/get_policies, {
    method: 'POST',
    headers: { 'apikey': SUPABASE_SERVICE_ROLE_KEY, 'Authorization': Bearer , 'Content-Type': 'application/json' }
  });
  if (res.ok) console.log(await res.json());
  else console.log('RPC failed');
  
  // Alternative: query pg_policies
  const res2 = await fetch(${SUPABASE_URL}/rest/v1/pg_policies?tablename=eq.tests, {
    headers: { 'apikey': SUPABASE_SERVICE_ROLE_KEY, 'Authorization': Bearer  }
  });
  if (res2.ok) console.log('Policies for tests:', await res2.json());
  else console.log('pg_policies query failed');
}
checkPolicies();
