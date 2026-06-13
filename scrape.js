const https = require('https');
const fs = require('fs');

async function fetchUnsplash(query) {
  return new Promise((resolve) => {
    https.get(`https://unsplash.com/s/photos/${query}`, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        // Look for image urls like https://images.unsplash.com/photo-15...
        const regex = /https:\/\/images\.unsplash\.com\/photo-[a-zA-Z0-9-]+/g;
        const matches = [...new Set(data.match(regex))];
        resolve(matches);
      });
    });
  });
}

async function run() {
  const bio = await fetchUnsplash('biology-science');
  const chem = await fetchUnsplash('chemistry-lab');
  const phys = await fetchUnsplash('physics');
  
  console.log('Bio:', bio.length);
  console.log('Chem:', chem.length);
  console.log('Phys:', phys.length);
  
  fs.writeFileSync('unsplash_urls.json', JSON.stringify({ bio, chem, phys }, null, 2));
}
run();
