const fs = require('fs');
let txt = fs.readFileSync('unit10_vol4_text.txt', 'utf8');
let paragraphs = txt.split(/\n\s*\n/);
let reading = paragraphs.slice(-3).join('<br><br>');
let j = JSON.parse(fs.readFileSync('unit10_vol4_raw.json', 'utf8'));
j.parts[1].content = `<div style="padding: 24px; background: #f8fafc; border-radius: 12px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #334155; line-height: 1.8; font-size: 1.05rem; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); border: 1px solid #e2e8f0;"><h2 style="color: #0f172a; text-align: center; margin-top: 0; margin-bottom: 24px; font-size: 1.5rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 2px solid #cbd5e1; padding-bottom: 12px;">Reading Passage</h2>${reading.replace(/\n/g, '<br>')}</div>`;
fs.writeFileSync('unit10_vol4_raw.json', JSON.stringify(j, null, 2));
console.log('Fixed Unit 10');
