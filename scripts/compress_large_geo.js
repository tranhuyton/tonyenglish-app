const { execSync } = require('child_process');
const fs = require('fs');

const filesToCompress = [
  'F:\\Downloads\\Chrome\\Geo Podcast\\Final\\English podcast\\Audio\\02-Why Living Near Rivers Is Dangerous.mp3',
  'F:\\Downloads\\Chrome\\Geo Podcast\\Final\\English podcast\\Audio\\03-Rebuilding the Global Power Grid.mp3',
  'F:\\Downloads\\Chrome\\Geo Podcast\\Final\\Vietnamese podcast\\03-Sinh tồn trước thảm họa địa chất.mp3'
];

filesToCompress.forEach(p => {
  const temp = p.replace('.mp3', '_temp192.mp3');
  console.log('Compressing:', p);
  execSync(`ffmpeg -y -i "${p}" -c:a libmp3lame -b:a 192k "${temp}" -loglevel error`);
  fs.copyFileSync(temp, p);
  fs.unlinkSync(temp);
  const sz = (fs.statSync(p).size / (1024*1024)).toFixed(1);
  console.log('Finished. New size:', sz, 'MB');
});
console.log('All 3 files compressed successfully!');
