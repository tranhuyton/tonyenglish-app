const fs = require('fs');
const path = require('path');

const srcDir = 'c:\\Users\\Tony\\.gemini\\antigravity\\brain\\e4c48bd7-96c8-4c47-9ee8-f301c8f39327';
const destDir = 'c:\\Users\\Tony\\.gemini\\antigravity\\scratch\\tonyenglish-app\\public';

const files = fs.readdirSync(srcDir);

files.forEach(file => {
  if (file.match(/^unit(1[6-9]|2[0-2])_.*\.png$/)) {
    // Extract base name without timestamp, e.g., unit16_word_list_1 from unit16_word_list_1_123456.png
    const baseMatch = file.match(/^(unit\d+_(?:word_list_[12]|story))_\d+\.png$/);
    if (baseMatch) {
      const newName = `${baseMatch[1]}.png`;
      fs.copyFileSync(path.join(srcDir, file), path.join(destDir, newName));
      console.log(`Copied ${file} to ${newName}`);
    }
  }
});
console.log('Copy complete!');
