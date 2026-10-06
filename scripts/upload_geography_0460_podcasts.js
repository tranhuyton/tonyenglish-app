const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/VITE_SUPABASE_URL=(.*)/)[1].trim();
const anon = env.match(/VITE_SUPABASE_ANON_KEY=(.*)/)[1].trim();
const supabase = createClient(url, anon);

const baseDir = 'F:\\Downloads\\Chrome\\Geo Podcast\\Final';
const enDir = path.join(baseDir, 'English podcast', 'Audio');
const viDir = path.join(baseDir, 'Vietnamese podcast');

const manifestPath = 'scripts/geography_0460_podcast_manifest.json';
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));

async function uploadFileWithRetry(item, storagePrefix, maxRetries = 3) {
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

  const CONCURRENCY = 3;
  let active = 0;
  let nextIdx = 0;
  let completed = existingSet.size;
  let failed = [];

  await new Promise(resolve => {
    function launch() {
      if (nextIdx >= queue.length && active === 0) {
        resolve();
        return;
      }

      while (active < CONCURRENCY && nextIdx < queue.length) {
        const item = queue[nextIdx++];
        active++;

        (async () => {
          if (existingSet.has(item.storageFileName)) {
            active--;
            launch();
            return;
          }

          const ok = await uploadFileWithRetry(item, storagePrefix, 3);
          if (ok) {
            completed++;
            console.log(`[${categoryName}] [${completed}/${queue.length}] Completed ${item.storageFileName}`);
          } else {
            failed.push(item);
          }

          active--;
          launch();
        })();
      }
    }

    launch();
  });

  console.log(`\n${categoryName} finished: ${completed}/${queue.length} completed. Failed: ${failed.length}`);
  return failed;
}

async function main() {
  console.log(`Starting upload for 0460 Geography (${manifest.length * 2} files total)...`);

  // 1. Upload Vietnamese
  const failedVi = await uploadCategory('VIETNAMESE', viDir, 'audio/podcast/geography-0460', 'newViFile', 'titleVi');

  // 2. Upload English
  const failedEn = await uploadCategory('ENGLISH', enDir, 'audio/podcast/geography-0460-en', 'newEnFile', 'titleEn');

  if (failedVi.length > 0 || failedEn.length > 0) {
    console.log('Failed items exist, re-running once for failed items...');
    await uploadCategory('VIETNAMESE_RETRY', viDir, 'audio/podcast/geography-0460', 'newViFile', 'titleVi');
    await uploadCategory('ENGLISH_RETRY', enDir, 'audio/podcast/geography-0460-en', 'newEnFile', 'titleEn');
  }

  console.log('\n🎉 ALL GEOGRAPHY 0460 PODCAST FILES UPLOAD PROCESS COMPLETED!');
}

main().catch(err => {
  console.error('Fatal upload error:', err);
  process.exit(1);
});
