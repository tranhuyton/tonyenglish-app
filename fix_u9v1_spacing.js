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
    
    // We expect 10 questions here (16 to 25) because of the previous fix.
    if (secC.questions.length === 10) {
        // Q16 & Q17
        secC.questions[0].content = '<p style="margin-bottom: 0px;"><b>wave / beach</b><br/>I like to play on the [16].</p>';
        secC.questions[1].content = '<p>The big [17] pushed the swimmer back.</p>';
        
        // Q18 & Q19
        secC.questions[2].content = '<p style="margin-bottom: 0px;"><b>ocean / island</b><br/>They walked across the [18] to find food.</p>';
        secC.questions[3].content = '<p>I am scared of some animals that live in the [19].</p>';
        
        // Q20 & Q21
        secC.questions[4].content = '<p style="margin-bottom: 0px;"><b>fix / damage</b><br/>My dad knows how to [20] cars.</p>';
        secC.questions[5].content = "<p>If you [21] the light, we won't be able to see at night.</p>";
        
        // Q22 & Q23
        secC.questions[6].content = '<p style="margin-bottom: 0px;"><b>still / rock</b><br/>We have to go around that large [22].</p>';
        secC.questions[7].content = '<p>We are [23] planning to go to Florida this winter.</p>';
        
        // Q24 & Q25
        secC.questions[8].content = '<p style="margin-bottom: 0px;"><b>step / throw</b><br/>Do you know how to [24] a football?</p>';
        secC.questions[9].content = '<p>Please [25] into the house.</p>';
        
        fs.writeFileSync(path, JSON.stringify(data, null, 2), 'utf8');
        console.log('Fixed Unit 9 Vol 1 Part C spacing');
    } else {
        console.log('Part C does not have 10 questions. Found ' + secC.questions.length);
    }
} else {
    console.log('Part C not found');
}
