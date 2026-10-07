const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');
const https = require('https');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const baseDir = 'F:\\Downloads\\Chrome\\IELTS Premium-studio';
const manifestPath = 'scripts/ielts_premium_podcast_manifest.json';
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));

async function uploadFileWithRetry(item, maxRetries = 3) {
  const stat = fs.statSync(item.localPath);
  const mb = (stat.size / (1024 * 1024)).toFixed(1);
  const buffer = fs.readFileSync(item.localPath);

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      console.log(`[Upload] (${attempt}/${maxRetries}) ${item.storagePath} (${mb} MB): [${item.code}] ${item.title.substring(0, 45)}...`);
      const { error } = await supabase.storage.from('test_assets').upload(item.storagePath, buffer, {
        contentType: 'audio/mpeg',
        upsert: true
      });

      if (error) {
        console.warn(`[Retry ${attempt}] Error for ${item.storageFileName}: ${error.message}`);
        if (attempt === maxRetries) return false;
        await new Promise(r => setTimeout(r, 2000 * attempt));
      } else {
        console.log(`[Success] Finished ${item.storagePath}`);
        return true;
      }
    } catch (err) {
      console.warn(`[Retry ${attempt}] Exception for ${item.storageFileName}: ${err.message}`);
      if (attempt === maxRetries) return false;
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }
  return false;
}

async function uploadSkillCategory(skillKey, skillData) {
  const localDir = path.join(baseDir, skillData.folder || skillKey);
  const storagePrefix = skillData.storageFolder;

  console.log(`\n=== Checking existing files for ${skillData.moduleName} (${storagePrefix}) ===`);
  const { data: existingData } = await supabase.storage.from('test_assets').list(storagePrefix, { limit: 100 });
  const existingSet = new Set((existingData || []).map(d => d.name));
  console.log(`Already in storage for ${skillData.moduleName}: ${existingSet.size} files.`);

  const queue = skillData.episodes.map(ep => ({
    localPath: path.join(baseDir, getFolderByKey(skillKey), ep.localFile),
    storagePath: `${storagePrefix}/${ep.storageFileName}`,
    storageFileName: ep.storageFileName,
    title: ep.title,
    code: ep.code
  }));

  const toUpload = queue.filter(item => !existingSet.has(item.storageFileName));
  console.log(`Files to upload: ${toUpload.length} of ${queue.length}`);

  let successCount = queue.length - toUpload.length;
  let failCount = 0;

  const CONCURRENCY = 2;
  for (let i = 0; i < toUpload.length; i += CONCURRENCY) {
    const chunk = toUpload.slice(i, i + CONCURRENCY);
    const results = await Promise.all(chunk.map(item => uploadFileWithRetry(item)));
    results.forEach(res => {
      if (res) successCount++;
      else failCount++;
    });
  }

  console.log(`\n=== Summary for ${skillData.moduleName} ===`);
  console.log(`Total: ${queue.length}, Success: ${successCount}, Failed: ${failCount}`);
  return failCount === 0;
}

function getFolderByKey(k) {
  const map = {
    task1: 'Writing Task 1',
    task2: 'Writing Task 2',
    reading: 'Reading',
    listening: 'Listening',
    speaking: 'Speaking Part 2'
  };
  return map[k];
}

async function verifyUrls() {
  console.log('\n=== Verifying Sample Public Audio URLs (HTTP HEAD) ===');
  const sampleUrls = [
    manifest.task1.episodes[0].audioUrl,
    manifest.task2.episodes[0].audioUrl,
    manifest.reading.episodes[0].audioUrl,
    manifest.listening.episodes[0].audioUrl,
    manifest.speaking.episodes[0].audioUrl,
  ];

  for (const u of sampleUrls) {
    await new Promise(resolve => {
      const req = https.request(u, { method: 'HEAD' }, res => {
        console.log(`[${res.statusCode === 200 ? 'OK' : 'FAIL'} - ${res.statusCode}]: ${u}`);
        resolve();
      });
      req.on('error', e => {
        console.error(`[ERR] ${u}: ${e.message}`);
        resolve();
      });
      req.end();
    });
  }
}

async function main() {
  console.log('Starting upload for IELTS Premium podcasts (36 files total)...');
  let allSuccess = true;

  for (const [k, sData] of Object.entries(manifest)) {
    const ok = await uploadSkillCategory(k, sData);
    if (!ok) allSuccess = false;
  }

  if (allSuccess) {
    console.log('\nAll 36 IELTS Premium podcast audio files uploaded successfully!');
    await verifyUrls();
  } else {
    console.error('\nSome files failed to upload. Check logs above.');
    process.exit(1);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
