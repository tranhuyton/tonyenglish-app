const { createClient } = require('@supabase/supabase-js');
const { translate } = require('@vitalets/google-translate-api');
require('dotenv').config();
const mainDb = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_SERVICE_ROLE_KEY);

const H3_MARKER = '<h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3>';

async function getWordData(word, vietMeaning) {
    let result = {
        word: word,
        phonetic: '',
        pos: '',
        enDef: '',
        viDef: vietMeaning,
        enEx: '',
        viEx: ''
    };
    
    try {
        const resp = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`);
        if (resp.ok) {
            const data = await resp.json();
            const entry = data[0];
            
            if (entry.phonetic) result.phonetic = entry.phonetic;
            else if (entry.phonetics && entry.phonetics.length > 0) {
                const ph = entry.phonetics.find(p => p.text);
                if (ph) result.phonetic = ph.text;
            }
            
            if (entry.meanings && entry.meanings.length > 0) {
                let bestMeaning = entry.meanings[0];
                let bestDef = bestMeaning.definitions[0];
                
                for (let m of entry.meanings) {
                    let d = m.definitions.find(def => def.example);
                    if (d) {
                        bestMeaning = m;
                        bestDef = d;
                        break;
                    }
                }
                
                result.pos = bestMeaning.partOfSpeech;
                result.enDef = bestDef.definition;
                if (bestDef.example) {
                    result.enEx = bestDef.example;
                    try {
                        const tr = await translate(result.enEx, {to: 'vi'});
                        result.viEx = tr.text;
                    } catch (e) {
                        console.error('Translation error', e.message);
                    }
                }
            }
        } else {
            const tr = await translate(vietMeaning, {to: 'en'});
            result.enDef = tr.text;
        }
    } catch (err) {
        console.error('Dict error:', err.message);
    }
    
    if (result.phonetic && result.phonetic.startsWith('/')) {
        result.phonetic = '[' + result.phonetic.substring(1, result.phonetic.length - 1) + ']';
    } else if (result.phonetic && !result.phonetic.startsWith('[')) {
        result.phonetic = '[' + result.phonetic + ']';
    }
    
    let html = `<div style="display: flex; gap: 16px; align-items: flex-start;">\n`;
    html += `<div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div>\n`;
    html += `<div style="display: flex; flex-direction: column; gap: 6px;">\n`;
    html += `<div style="display: flex; align-items: baseline; gap: 8px;">\n`;
    html += `<span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${result.word}</span>\n`;
    if (result.phonetic) html += `<span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${result.phonetic}</span>\n`;
    if (result.pos) html += `<span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${result.pos}.</span>\n`;
    html += `</div>\n`;
    html += `<div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${result.enDef} <span style="color: #0ea5e9;">(${result.viDef})</span></div>\n`;
    
    if (result.enEx) {
        let viExHtml = result.viEx ? ` <span style="color: #0ea5e9;">(${result.viEx})</span>` : '';
        html += `<div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${result.enEx}${viExHtml}</div>\n`;
    }
    
    html += `</div></div>`;
    return html;
}

async function fixUnit10() {
    console.log('Fetching tests...');
    const { data: tests } = await mainDb.from('tests').select('id, title, content_json').eq('title', 'Unit 10: Ruth Handler');
    
    if (!tests || tests.length === 0) return;
    const test = tests[0];
    
    let modified = false;
    for (let p of test.content_json.parts) {
        if (p.title.startsWith('Word List')) {
            if (p.content.includes('✨') || p.content.includes('<span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;"></span>')) {
                const startIndex = p.content.indexOf(H3_MARKER);
                if (startIndex > -1) {
                    const blockToParse = p.content.substring(startIndex);
                    const regex = /<span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">(.*?)<\/span>[\s\S]*?<span style="color: #0ea5e9;">(.*?)<\/span>/g;
                    let match;
                    let wordsToFetch = [];
                    while ((match = regex.exec(blockToParse)) !== null) {
                        wordsToFetch.push({
                            word: match[1].replace(/\.\.\./g, '').trim(),
                            viDef: match[2].trim()
                        });
                    }
                    
                    console.log(`Processing ${wordsToFetch.length} words in ${p.title}`);
                    let newSectionHtml = H3_MARKER + '\n<div style="display: flex; flex-direction: column; gap: 24px;">\n';
                    
                    for (let w of wordsToFetch) {
                        console.log(`Fetching data for: ${w.word}`);
                        const itemHtml = await getWordData(w.word, w.viDef);
                        newSectionHtml += itemHtml + '\n';
                    }
                    
                    newSectionHtml += `</div></div></div>`; // Close wrappers
                    
                    p.content = p.content.substring(0, startIndex) + newSectionHtml;
                    modified = true;
                }
            }
        }
    }
    
    if (modified) {
        console.log('Updating DB...');
        const { error } = await mainDb.from('tests').update({ content_json: test.content_json }).eq('id', test.id);
        if (error) console.error(error);
        else console.log('Successfully updated Unit 10!');
    }
}
fixUnit10();
