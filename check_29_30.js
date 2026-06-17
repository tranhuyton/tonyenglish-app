const fs = require('fs');
['unit28.json', 'unit29.json', 'unit30.json'].forEach(file => {
  try {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    console.log('---', file, '---');
    if (!data.parts) {
      console.log('Missing parts array!');
      return;
    }
    data.parts.forEach((p, i) => {
      console.log('Part ' + i + ': ' + p.title + ', questions: ' + (p.questions ? p.questions.length : 'none'));
      if(p.questions) {
        p.questions.forEach((q, j) => {
          if (!q.options) console.log('  Q' + j + ' missing options');
          if (!q.questionType) console.log('  Q' + j + ' missing questionType');
          if (!q.correctAnswer) console.log('  Q' + j + ' missing correctAnswer');
        });
      }
    });
  } catch(e) {
    console.log('Error reading', file, e.message);
  }
});
