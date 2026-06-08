const fs = require('fs');
const data = JSON.parse(fs.readFileSync('unite1_new.json'));
const parts = data.content_json.parts;
parts.forEach((p, i) => {
  p.sections.forEach((s, j) => {
    const qCount = s.questions ? s.questions.length : 0;
    const ids = s.questions ? s.questions.map(q => q.id).join(',') : '';
    const contentText = String(s.content || '') + ' ' + String(s.questions?.[0]?.content || '');
    const matches = contentText.match(/\[\s*\d+\s*\]/g);
    console.log(`P${i}S${j}: ${s.questionType} | ${qCount} qs | IDs: ${ids} | Matches: ${matches}`);
  });
});
