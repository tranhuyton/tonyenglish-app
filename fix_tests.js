const fs = require('fs');

function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) {
    return null;
  }
}

const SUPABASE_URL = getEnv('VITE_SUPABASE_URL');
const SUPABASE_SERVICE_ROLE_KEY = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');

async function fixTests() {
  const res = await fetch(`${SUPABASE_URL}/rest/v1/tests?test_type=eq.Mixed%20Paper%20(C%C3%B3%20h%C3%ACnh)`, {
    method: 'PATCH',
    headers: {
      'apikey': SUPABASE_SERVICE_ROLE_KEY,
      'Authorization': `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      test_type: 'Mixed-Paper'
    })
  });
  console.log(res.status, res.statusText);
}
fixTests();
