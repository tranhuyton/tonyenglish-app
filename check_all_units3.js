const fs = require('fs');
let brokenUnits = [];
for (let i = 2; i <= 30; i++) {
  try {
    const data = JSON.parse(fs.readFileSync(`unit${i}.json`, 'utf8'));
    let hasSectionLevelQuestionType = false;
    let missingQuestionType = false;
    data.parts.forEach((p) => {
      if(p.sections) {
        p.sections.forEach((s) => {
          if (s.questionType) {
            hasSectionLevelQuestionType = true;
          } else {
             if (s.questions) {
                s.questions.forEach((q) => {
                   if (!q.questionType) missingQuestionType = true;
                });
             }
          }
        });
      }
    });
    if (missingQuestionType) brokenUnits.push(i);
  } catch(e) {
  }
}
console.log('Broken units missing questionType:', brokenUnits);
