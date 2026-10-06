const fs = require('fs');
const { spawn } = require('child_process');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();

const filePath = 'F:\\Downloads\\Chrome\\Combined and Co-ordinated Sciences\\English\\02-How Diffusion and Osmosis Power Life.mp3';
const uploadUrl = `${url}/storage/v1/object/test_assets/audio/podcast/science-0654-en/ep_02.mp3`;

console.log('Starting curl upload for ep_02.mp3 (size:', (fs.statSync(filePath).size / (1024*1024)).toFixed(1), 'MB)...');

const args = [
  '-X', 'POST',
  uploadUrl,
  '-H', `Authorization: Bearer ${anon}`,
  '-H', `apikey: ${anon}`,
  '-H', 'Content-Type: audio/mpeg',
  '-H', 'x-upsert: true',
  '--data-binary', `@${filePath}`,
  '--retry', '5',
  '--retry-delay', '3',
  '--retry-connrefused',
  '--progress-bar',
  '-w', '\nHTTP_STATUS: %{http_code}\nTIME_TOTAL: %{time_total}s\n'
];

const proc = spawn('curl.exe', args, { stdio: 'inherit' });

proc.on('close', code => {
  console.log(`curl process exited with code ${code}`);
  process.exit(code);
});
