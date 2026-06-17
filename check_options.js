const fs = require('fs');
['unit28.json', 'unit29.json', 'unit30.json'].forEach(file => {
  try {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    console.log('---', file, '---');
    let hasError = false;
    data.parts.forEach((p, i) => {
      p.sections?.forEach((s, j) => {
        s.questions?.forEach((q, k) => {
          if (!Array.isArray(q.options)) {
            console.log('Part ' + i + ' Sec ' + j + ' Q ' + k + ' options is not array! Type:', typeof q.options);
            hasError = true;
          } else {
            q.options.forEach((opt, idx) => {
              if (typeof opt !== 'string') {
                console.log('Part ' + i + ' Sec ' + j + ' Q ' + k + ' option ' + idx + ' is not string! Type:', typeof opt, opt);
                hasError = true;
              }
            });
          }
          if (q.correctAnswer && typeof q.correctAnswer !== 'string') {
            console.log('Q ' + k + ' correctAnswer is not string:', q.correctAnswer);
            hasError = true;
          }
        });
      });
    });
    if (!hasError) console.log('No option type errors.');
  } catch(e) {}
});
