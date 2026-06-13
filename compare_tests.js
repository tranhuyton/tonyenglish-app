const fs = require('fs');
const st = fs.readFileSync('src/StandardTest.tsx', 'utf-8');
const ct = fs.readFileSync('src/ComputerTest.tsx', 'utf-8');
const pt = fs.readFileSync('src/PaperTest.tsx', 'utf-8');
console.log('StandardTest:', st.split('\n').length, 'lines');
console.log('ComputerTest:', ct.split('\n').length, 'lines');
console.log('PaperTest:', pt.split('\n').length, 'lines');

function findTypes(code, name) {
  console.log(`\n--- ${name}: questionType values ---`);
  const regex = /questionType\s*===?\s*['"]([^'"]+)['"]/g;
  const types = new Set();
  let m;
  while ((m = regex.exec(code)) !== null) {
    types.add(m[1]);
  }
  types.forEach(t => console.log('  ', t));
  return types;
}

function findFeatures(code, name) {
  console.log(`\n--- ${name}: features ---`);
  const features = {
    'Drag & Drop': /onDrag|draggable|onDrop|drag-drop/i.test(code),
    'Matching': /matching|matchItems|matchPairs/i.test(code),
    'Fill blank': /fillBlank|fill.?in|gap.?fill|inputAnswer/i.test(code),
    'Audio player': /<audio|audioRef|playAudio|AudioPlayer/i.test(code),
    'Timer': /setInterval|countdown|timeLeft|timer/i.test(code),
    'Score calc': /calculateScore|totalScore|scoreCalc/i.test(code),
    'Review mode': /reviewMode|showAnswer|isReview|showExplanation/i.test(code),
    'Combo test': /parts\.map|section\.map|part\.sections/i.test(code),
    'Highlight': /highlight|bg-yellow/i.test(code),
    'Multiple select': /multiSelect|checkbox|multiple.?answer/i.test(code),
    'Note completion': /note.?completion|summary.?completion/i.test(code),
    'Map labeling': /map.?label|diagram.?label/i.test(code),
    'Sentence completion': /sentence.?completion/i.test(code),
    'Short answer': /short.?answer/i.test(code),
  };
  Object.entries(features).forEach(([k, v]) => console.log(`  ${v ? '✅' : '❌'} ${k}`));
}

const stTypes = findTypes(st, 'StandardTest');
const ctTypes = findTypes(ct, 'ComputerTest');
const ptTypes = findTypes(pt, 'PaperTest');

console.log('\n=== Types in Computer/Paper but NOT in Standard ===');
const allOtherTypes = new Set([...ctTypes, ...ptTypes]);
allOtherTypes.forEach(t => {
  if (!stTypes.has(t)) console.log('  MISSING:', t);
});

findFeatures(st, 'StandardTest');
findFeatures(ct, 'ComputerTest');
findFeatures(pt, 'PaperTest');
