const fs = require('fs');
const data = JSON.parse(fs.readFileSync('unite1_new.json'));
const parts = data.content_json.parts;
parts.forEach((p, i) => {
  p.sections.forEach((s, j) => {
    let combined = String(s.content||'');
    if (s.questions) s.questions.forEach(q => combined += ' ' + String(q.content||''));
    console.log(`P${i}S${j} Matches:`, combined.match(/\[\s*\d+\s*\]/g));
  });
});
