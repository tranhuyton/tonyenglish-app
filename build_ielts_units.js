const fs = require('fs');

const units = [26, 27, 28, 29, 30];

units.forEach(u => {
    let rawFile = '';
    if (fs.existsSync(`public/unit${u}_vol6.json`)) {
        rawFile = `public/unit${u}_vol6.json`;
    } else if (fs.existsSync(`unit${u}.json`)) {
        rawFile = `unit${u}.json`;
    } else {
        console.log("Not found for unit " + u);
        return;
    }
    
    let rawData = JSON.parse(fs.readFileSync(rawFile, 'utf8'));
    
    // Parse word list HTML
    let words = [];
    let wlHtml = rawData.parts[0].content;
    let wRegex = /color: #65a30d;[^>]*>([^<]+)<\/span>.*?monospace;[^>]*>([^<]+)<\/span>.*?italic;[^>]*>([^<]+)<\/span>.*?line-height: 1\.5;[^>]*>(.*?)<\/div>.*?italic;[^>]*>(.*?)<\/div>/g;
    
    let m;
    while((m = wRegex.exec(wlHtml)) !== null) {
        words.push({
            word: m[1].trim(),
            pron: m[2].trim(),
            type: m[3].trim(),
            meaning: m[4].trim(),
            ex: m[5].trim().replace(/^'+'\s*/, '')
        });
    }
    
    // Parse story HTML to clean it and get Kéo thả sentences
    let storyHtml = rawData.parts[1].content;
    
    // Clean Story HTML
    // We just replace the image src.
    storyHtml = storyHtml.replace(/<img[^>]*src="[^"]*"[^>]*>/, `<img src="/unit${u}_ielts_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 24px;" />`);
    // Remove newlines to minify
    storyHtml = storyHtml.replace(/\r?\n|\r/g, '');
    
    // Extract sentences with <b> for Drag & Drop
    let sentences = [];
    let pRegex = /<p[^>]*>(.*?)<\/p>/g;
    let pm;
    while ((pm = pRegex.exec(storyHtml)) !== null) {
        let text = pm[1];
        let splitted = text.split(/(?<=\.)\s+/);
        splitted.forEach(s => {
            if (s.includes('<b>') && sentences.length < 5) {
                sentences.push(s);
            }
        });
    }
    
    let dropWords = [];
    let keoThaContent = `<p class="font-bold text-[16px] text-slate-800 mb-4">Drag and drop the correct words into the blanks.</p>`;
    
    sentences.forEach((s, idx) => {
        let bMatch = s.match(/<b>(.*?)<\/b>/);
        if (bMatch) {
            let word = bMatch[1].trim();
            dropWords.push(word);
            let sReplaced = s.replace(/<b>.*?<\/b>/, `[ ${idx + 1} ]`);
            keoThaContent += `${idx + 1}. ${sReplaced}<br/><br/>`;
        }
    });
    
    // Generate the Kéo thả questions
    let keoThaQuestions = [];
    dropWords.forEach((word, idx) => {
        keoThaQuestions.push({
            content: idx === 0 ? keoThaContent : "",
            options: [...dropWords],
            correctAnswer: word,
            explanation: `Từ cần điền là: ${word}`
        });
    });

    // Generate Word List HTMLs
    const genWlHtml = (title, imgPath, wList) => {
        let html = `<p style="display: none;">${title}</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="${imgPath}" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;
        wList.forEach(w => {
            html += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.meaning}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">+' ${w.ex}</div></div></div>`;
        });
        html += `</div></div></div>`;
        return html;
    };
    
    let wl1Html = genWlHtml("Word List 1", `/unit${u}_ielts_word_list_1.png`, words.slice(0, 10));
    let wl2Html = genWlHtml("Word List 2", `/unit${u}_ielts_word_list_2.png`, words.slice(10, 20));

    // Pool questions
    let allWlQ = [];
    rawData.parts[0].sections.forEach(s => {
        allWlQ = allWlQ.concat(s.questions.map(q => ({...q, _sectionTitle: s.title, _type: s.questionType})));
    });
    
    // Helper to get chunk of questions
    let curQ = 0;
    const getQs = (count) => {
        let chunk = [];
        for (let i = 0; i < count; i++) {
            if (curQ < allWlQ.length) chunk.push(allWlQ[curQ++]);
        }
        return chunk.map(q => {
            delete q._sectionTitle;
            delete q._type;
            delete q.id;
            // rename questionType if it was droplist or something, wait we set it on section
            return q;
        });
    };

    // Construct JSON
    const unitJson = {
        title: `Unit ${u}: Title Here`,
        parts: [
            {
                title: "Word List 1",
                content: wl1Html,
                sections: [
                    {
                        title: "Exercise 1: Choose the correct word to fill in the blank.",
                        content: "",
                        questionType: "Trắc nghiệm",
                        questions: getQs(5)
                    },
                    {
                        title: "Exercise 2: Choose the word that best matches the definition.",
                        content: "",
                        questionType: "Trắc nghiệm",
                        questions: getQs(5)
                    },
                    {
                        title: "Exercise 3: Mark each statement T for true or F for false.",
                        content: "",
                        questionType: "Droplist",
                        questions: getQs(5).map(q => {
                            // If options aren't T/F, just force it or leave it
                            if(q.options && q.options.length === 2 && q.options.includes('C')) {
                                q.options = ['T', 'F', 'NG']; // to match TFNG Droplist
                                q.correctAnswer = q.correctAnswer === 'C' ? 'T' : 'F';
                            }
                            return q;
                        })
                    }
                ]
            },
            {
                title: "Word List 2",
                content: wl2Html,
                sections: [
                    {
                        title: "Exercise 1: Choose the correct word to fill in the blank.",
                        content: "",
                        questionType: "Trắc nghiệm",
                        questions: getQs(5)
                    },
                    {
                        title: "Exercise 2: Choose the word that best matches the definition.",
                        content: "",
                        questionType: "Trắc nghiệm",
                        questions: getQs(5)
                    },
                    {
                        title: "Exercise 3: Mark each statement T for true or F for false.",
                        content: "",
                        questionType: "Droplist",
                        questions: getQs(5).map(q => {
                            if(q.options && q.options.length === 2 && q.options.includes('C')) {
                                q.options = ['T', 'F', 'NG'];
                                q.correctAnswer = q.correctAnswer === 'C' ? 'T' : 'F';
                            }
                            return q;
                        })
                    }
                ]
            },
            {
                title: "Comprehensive Reading",
                content: storyHtml,
                explanation: "",
                sections: [
                    {
                        title: "Exercise 1: Fill in each blank with the appropriate word",
                        content: "",
                        questionType: "Kéo thả",
                        questions: keoThaQuestions
                    },
                    {
                        title: "Exercise 2: Reading Comprehension",
                        content: "",
                        questionType: "Trắc nghiệm",
                        // Usually part 1 section 1 is the Answer the questions (MCQ)
                        questions: rawData.parts[1].sections.length > 1 ? rawData.parts[1].sections[1].questions : rawData.parts[1].sections[0].questions
                    }
                ]
            }
        ],
        basicInfo: {
            skill: "SplitScreen (Standard)",
            title: `Unit ${u}: Title Here`,
            category: "exercise",
            courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
            timeLimit: 40
        }
    };
    
    // Assign sequential IDs
    let finalId = 1;
    unitJson.parts.forEach(p => {
        p.sections.forEach(s => {
            if (s.questions) {
                s.questions.forEach(q => {
                    q.id = finalId++;
                });
            }
        });
    });

    fs.writeFileSync(`public/unit${u}_ielts.json`, JSON.stringify(unitJson, null, 2));
    console.log(`Created public/unit${u}_ielts.json`);
});
