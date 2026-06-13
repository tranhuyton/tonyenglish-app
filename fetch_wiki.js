const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  try {
    const envContent = fs.readFileSync('.env', 'utf-8');
    const match = envContent.match(new RegExp(`^${key}=(.*)$`, 'm'));
    return match ? match[1].trim() : null;
  } catch (e) { return null; }
}

const supabaseUrl = getEnv('VITE_SUPABASE_URL');
const supabaseKey = getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY');
const supabase = createClient(supabaseUrl, supabaseKey);

async function searchWikiImage(query) {
  try {
    let res = await fetch('https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=' + encodeURIComponent(query) + '&utf8=&format=json&srlimit=1');
    let data = await res.json();
    if (!data.query.search.length) return null;
    let title = data.query.search[0].title;
    
    res = await fetch('https://en.wikipedia.org/w/api.php?action=query&titles=' + encodeURIComponent(title) + '&prop=pageimages&format=json&pithumbsize=800');
    data = await res.json();
    let page = Object.values(data.query.pages)[0];
    return page.thumbnail ? page.thumbnail.source : null;
  } catch (e) {
    console.log("Error searching Wiki:", e.message);
    return null;
  }
}

async function run() {
  const { data: folders, error } = await supabase.from('folders').select('id, title, parent_id, thumbnail_url');
  
  if (error) {
     console.log("Supabase error:", error);
     process.exit(1);
  }
  if (!folders) {
     console.log("Folders is null but no error was thrown.");
     process.exit(1);
  }
  
  const subFolders = folders.filter(f => f.parent_id && f.parent_id !== 'null' && f.parent_id !== '');
  
  console.log(`Found ${subFolders.length} sub-folders to process.`);
  
  for (let folder of subFolders) {
     const prefixMatch = folder.title.match(/^([A-Z0-9]+)\s*:/i);
     let query = folder.title;
     if (prefixMatch && prefixMatch[1].length <= 4) {
         query = folder.title.substring(prefixMatch[0].length).trim();
     }
     
     if (folder.title.toLowerCase().includes('section') || folder.title.includes('IV.')) continue;
     
     console.log(`Searching for: ${query}`);
     const wikiUrl = await searchWikiImage(query);
     
     if (wikiUrl) {
         console.log(`Found image: ${wikiUrl}`);
         await supabase.from('folders').update({ thumbnail_url: wikiUrl }).eq('id', folder.id);
     } else {
         console.log(`No image found for ${query}`);
     }
  }
  
  console.log("Done updating folder images!");
  process.exit(0);
}

run();
