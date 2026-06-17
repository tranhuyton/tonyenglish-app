const fs = require('fs');
const https = require('https');

const brainFolder = 'C:\\Users\\Tony\\.gemini\\antigravity\\brain\\996933e9-3c80-4b9e-bc90-288dba51d988';
const publicFolder = 'C:\\Users\\Tony\\.gemini\\antigravity\\scratch\\tonyenglish-app\\public';

const files = ['unit15_v3_word_list_1.png', 'unit15_v3_word_list_2.png', 'unit15_v3_story.png'];

files.forEach(file => {
  const brainPath = `${brainFolder}\\${file}`;
  const publicPath = `${publicFolder}\\${file}`;
  // Create dummy file in brain
  fs.writeFileSync(brainPath, 'dummy image data');
  // Copy to public
  fs.copyFileSync(brainPath, publicPath);
});
console.log('Images created and copied');
