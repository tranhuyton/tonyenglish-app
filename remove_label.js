const fs = require('fs');
const file = 'src/AdminPanel.tsx';
let lines = fs.readFileSync(file, 'utf8').split('\n');
let start = -1;
let end = -1;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('let c = t.content_json;')) {
    // The span starts a few lines above this
    if (start === -1) {
        start = i - 3; 
    }
  }
  if (start !== -1 && lines[i].includes('</span>')) {
    end = i;
    break; // Break after the first span ends
  }
}
if (start !== -1 && end !== -1) {
  lines.splice(start, end - start + 1);
  fs.writeFileSync(file, lines.join('\n'));
  console.log('Removed the label span successfully.');
} else {
  console.log('Could not find the label span block.');
}
