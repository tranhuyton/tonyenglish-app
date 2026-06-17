const fs = require('fs');
let brokenUnits = [];
for (let i = 16; i <= 30; i++) {
  try {
    const data = JSON.parse(fs.readFileSync(`unit${i}.json`, 'utf8'));
    let hasQuestionType = false;
    let missingQuestionType = false;
    data.parts.forEach((p) => {
      if(p.sections) {
        p.sections.forEach((s) => {
          if (s.questions) {
            s.questions.forEach((q) => {
               if (!q.questionType) missingQuestionType = true;
               else hasQuestionType = true;
            });
          }
        });
      }
    });
    if (missingQuestionType) brokenUnits.push(i);
  } catch(e) {
  }
}
console.log('Broken units missing questionType:', brokenUnits);
