const fs = require('fs');
const path = 'public/unit9_vol1.json';
const data = JSON.parse(fs.readFileSync(path, 'utf8'));

// Find Part C
let partCIndex = -1;
let sectionCIndex = -1;
for (let i = 0; i < data.parts.length; i++) {
    const sIdx = data.parts[i].sections.findIndex(s => s.title.includes('Part C'));
    if (sIdx !== -1) {
        partCIndex = i;
        sectionCIndex = sIdx;
        break;
    }
}

if (partCIndex !== -1) {
    const secC = data.parts[partCIndex].sections[sectionCIndex];
    const newQuestions = [];
    
    // Original Q16
    newQuestions.push({
        id: '16',
        content: '<p><b>wave / beach</b><br/>I like to play on the [16].</p>',
        correctAnswer: 'beach'
    });
    newQuestions.push({
        id: '17',
        content: '<p>The big [17] pushed the swimmer back.</p>',
        correctAnswer: 'wave'
    });
    
    // Original Q17
    newQuestions.push({
        id: '18',
        content: '<p><b>ocean / island</b><br/>They walked across the [18] to find food.</p>',
        correctAnswer: 'island'
    });
    newQuestions.push({
        id: '19',
        content: '<p>I am scared of some animals that live in the [19].</p>',
        correctAnswer: 'ocean'
    });
    
    // Original Q18
    newQuestions.push({
        id: '20',
        content: '<p><b>fix / damage</b><br/>My dad knows how to [20] cars.</p>',
        correctAnswer: 'fix'
    });
    newQuestions.push({
        id: '21',
        content: "<p>If you [21] the light, we won't be able to see at night.</p>",
        correctAnswer: 'damage'
    });
    
    // Original Q19
    newQuestions.push({
        id: '22',
        content: '<p><b>still / rock</b><br/>We have to go around that large [22].</p>',
        correctAnswer: 'rock'
    });
    newQuestions.push({
        id: '23',
        content: '<p>We are [23] planning to go to Florida this winter.</p>',
        correctAnswer: 'still'
    });
    
    // Original Q20
    newQuestions.push({
        id: '24',
        content: '<p><b>step / throw</b><br/>Do you know how to [24] a football?</p>',
        correctAnswer: 'throw'
    });
    newQuestions.push({
        id: '25',
        content: '<p>Please [25] into the house.</p>',
        correctAnswer: 'step'
    });
    
    secC.questions = newQuestions;
    
    // Now renumber the subsequent questions (Reading parts)
    let newId = 26;
    for (let i = partCIndex; i < data.parts.length; i++) {
        const p = data.parts[i];
        for (let j = 0; j < p.sections.length; j++) {
            if (i === partCIndex && j <= sectionCIndex) continue; // Skip Part C and before
            const s = p.sections[j];
            for (const q of s.questions) {
                q.id = newId.toString();
                newId++;
            }
        }
    }
    
    fs.writeFileSync(path, JSON.stringify(data, null, 2), 'utf8');
    console.log('Fixed Unit 9 Vol 1');
} else {
    console.log('Part C not found');
}
