const fs = require('fs');
const data = JSON.parse(fs.readFileSync('unite1.json'));
let globalId = 1;

data.content_json.parts.forEach(p => {
  p.sections.forEach(s => {
    const idMap = {};
    if (s.questions) {
      s.questions.forEach(q => {
        const oldId = String(q.id).trim();
        const newId = String(globalId++);
        idMap[oldId] = newId;
        q.id = newId;
      });
    }
    const replaceBrackets = (text) => {
      if (!text) return text;
      return text.replace(/\[\s*(\d+)\s*\]/g, (match, p1) => {
        const newId = idMap[p1];
        return newId ? `[${newId}]` : match;
      });
    };
    s.content = replaceBrackets(s.content);
    if (s.questions && s.questions[0]) {
      s.questions[0].content = replaceBrackets(s.questions[0].content);
    }
  });
});

fs.writeFileSync('unite1_fixed.json', JSON.stringify(data, null, 2));
console.log('Done mapping IDs up to', globalId - 1);
