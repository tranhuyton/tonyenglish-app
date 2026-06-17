const fs = require('fs');
['unit28.json', 'unit29.json', 'unit30.json'].forEach(file => {
  try {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    console.log('---', file, '---');
    if (!data.parts) return;
    data.parts.forEach((p, i) => {
      console.log('Part ' + i + ': ' + p.title);
      if(p.sections) {
        p.sections.forEach((s, j) => {
          console.log('  Section ' + j + ': ' + s.title + ', questions: ' + (s.questions ? s.questions.length : 'none'));
          if (s.questions) {
            s.questions.forEach((q, k) => {
               if (!q.options) console.log('    Q' + k + ' missing options');
               if (!q.questionType) console.log('    Q' + k + ' missing questionType');
               if (!q.correctAnswer) console.log('    Q' + k + ' missing correctAnswer');
               if (q.questionType === 'multiple-choice') {
                 if (!Array.isArray(q.options) || q.options.length === 0) {
                    console.log('    Q' + k + ' options is not an array or empty');
                 }
               }
            });
          }
        });
      }
    });
  } catch(e) {
    console.log('Error reading', file, e.message);
  }
});
