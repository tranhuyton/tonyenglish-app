const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const baseDir = 'F:\\Downloads\\Chrome\\Economics podcast\\Final';
const viDir = path.join(baseDir, 'Vietnamese');
const enDir = path.join(baseDir, 'English');

const manifestPath = 'scripts/economics_0455_podcast_manifest.json';
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));

async function uploadFileWithRetry(item, maxRetries = 3) {
  const stat = fs.statSync(item.localPath);
  const mb = (stat.size / (1024 * 1024)).toFixed(1);
  const buffer = fs.readFileSync(item.localPath);

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      console.log(`[Upload] (${attempt}/${maxRetries}) ${item.storageFileName} (${mb} MB): [${item.code}] ${item.title}...`);
      const { error } = await supabase.storage.from('test_assets').upload(item.storagePath, buffer, {
        contentType: 'audio/mpeg',
        upsert: true
      });

      if (error) {
        console.warn(`[Retry ${attempt}] Error for ${item.storageFileName}: ${error.message}`);
        if (attempt === maxRetries) return false;
        await new Promise(r => setTimeout(r, 2000 * attempt));
      } else {
        console.log(`[Success] Finished ${item.storageFileName}`);
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

async function uploadCategory(categoryName, localDir, storagePrefix, fileProp, titleProp) {
  console.log(`\n=== Checking existing files for ${categoryName} (${storagePrefix}) ===`);
  const { data: existingData } = await supabase.storage.from('test_assets').list(storagePrefix, { limit: 100 });
  const existingSet = new Set((existingData || []).map(d => d.name));
  console.log(`Already in storage for ${categoryName}: ${existingSet.size} files.`);

  const queue = manifest.map(item => ({
    localPath: path.join(localDir, item[fileProp]),
    storagePath: `${storagePrefix}/${item.storageFileName}`,
    storageFileName: item.storageFileName,
    title: item[titleProp],
    code: item.code
  }));

  const toUpload = queue.filter(item => !existingSet.has(item.storageFileName));
  console.log(`Files to upload for ${categoryName}: ${toUpload.length} of ${queue.length}`);

  let successCount = queue.length - toUpload.length;
  let failCount = 0;

  // Upload with concurrency 2
  const CONCURRENCY = 2;
  for (let i = 0; i < toUpload.length; i += CONCURRENCY) {
    const chunk = toUpload.slice(i, i + CONCURRENCY);
    const results = await Promise.all(chunk.map(item => uploadFileWithRetry(item)));
    results.forEach(res => {
      if (res) successCount++;
      else failCount++;
    });
  }

  console.log(`\n=== Category Summary: ${categoryName} ===`);
  console.log(`Total: ${queue.length}, Success: ${successCount}, Failed: ${failCount}`);
  return failCount === 0;
}

async function verifyUrls() {
  console.log('\n=== Verifying Public Audio URLs (HTTP HEAD) ===');
  const https = require('https');
  const sampleItems = [manifest[0], manifest[18], manifest[38]];
  
  for (const item of sampleItems) {
    for (const [lang, u] of [['VI', item.audioUrlVi], ['EN', item.audioUrlEn]]) {
      await new Promise(resolve => {
        const req = https.request(u, { method: 'HEAD' }, res => {
          console.log(`[${res.statusCode === 200 ? 'OK' : 'FAIL'} - ${res.statusCode}] [${lang}] Ep ${item.code}: ${u}`);
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
}

async function main() {
  console.log('Starting upload for IGCSE Economics 0455 podcasts...');
  console.log(`Total episodes: ${manifest.length}`);

  const viSuccess = await uploadCategory('Vietnamese', viDir, 'audio/podcast/economics-0455', 'fileNameVi', 'titleVi');
  const enSuccess = await uploadCategory('English', enDir, 'audio/podcast/economics-0455-en', 'fileNameEn', 'titleEn');

  if (viSuccess && enSuccess) {
    console.log('\nAll audio files uploaded successfully!');
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
