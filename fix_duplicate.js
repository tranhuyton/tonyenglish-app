const fs = require('fs');
const file = 'src/AITutorSidebar.tsx';
let lines = fs.readFileSync(file, 'utf8').split('\n');

let start = -1;
let end = -1;
let occurrences = 0;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes("case 'speaking':")) {
    occurrences++;
    if (occurrences === 2) {
      start = i;
    }
  }
  if (start !== -1 && lines[i].includes("width: 'md:w-[500px]'") && lines[i+1] && lines[i+1].includes('};')) {
    end = i + 1;
    break;
  }
}

if (start !== -1 && end !== -1) {
  lines.splice(start, end - start + 1);
  fs.writeFileSync(file, lines.join('\n'));
  console.log('Removed duplicate speaking theme');
} else {
  console.log('Duplicate not found');
}
