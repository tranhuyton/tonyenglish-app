const fs = require('fs');
let brokenUploads = [];
for (let i = 16; i <= 30; i++) {
  try {
    const data = JSON.parse(fs.readFileSync(`unit${i}_raw.json`, 'utf8'));
    if (!data.basicInfo) {
      brokenUploads.push(i);
    }
  } catch(e) {}
}
console.log('Broken uploads:', brokenUploads);
