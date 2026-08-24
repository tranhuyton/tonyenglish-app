const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

async function fixUnit2() {
  const { data: tests, error } = await supabase.from('tests')
    .select('id, title, content_json')
    .ilike('title', 'Unit 2: Listening Activity%');
    
  if (error) {
    console.error(error);
    return;
  }
  
  let updatedCount = 0;
  let totalRestored = 0;
  
  for (const test of tests) {
    let modified = false;
    const content = test.content_json;
    if (!content || !content.parts || content.parts.length === 0) continue;
    
    content.parts.forEach(part => {
      // Fix Transcript Formatting
      if (part.explanation && (part.explanation.includes('<br>') || part.explanation.includes('<br/>') || part.explanation.includes('<br />'))) {
        let transcript = part.explanation;
        
        if (transcript.startsWith('<p') && transcript.endsWith('</p>')) {
          transcript = transcript.replace(/^<p[^>]*>/, '').replace(/<\/p>$/, '');
        }
        
        const lines = transcript.split(/<br\s*\/?>/i);
        
        const newTranscript = lines.map(line => {
          let trimmed = line.trim();
          if (!trimmed) return '';
          
          if (!trimmed.startsWith('<b>')) {
             trimmed = trimmed.replace(/^(\d+\.|[A-Z][a-zA-Z\s]+:)\s*/, '<b>$1</b> ');
          }
          
          return `<p class="mb-2">${trimmed}</p>`;
        }).filter(l => l).join('');
        
        if (newTranscript !== part.explanation) {
          part.explanation = newTranscript;
          modified = true;
        }
      }
      
      if (!part.sections) return;
      
      part.sections.forEach(sec => {
        // Move section.title to section.content
        if (sec.title && sec.title.trim() !== '') {
          const oldTitle = sec.title;
          const instructionHTML = `<p class="font-bold text-[16px] text-slate-800 mb-4">${oldTitle}</p>`;
          sec.content = instructionHTML + (sec.content ? `<br>${sec.content}` : '');
          sec.title = '';
          modified = true;
        }
        
        // Fix Gap-fill structure
        if (["Điền từ", "Kéo thả", "Matching"].includes(sec.questionType)) {
          if (sec.content && sec.content.match(/\[\s*\d+\s*\]/)) {
            let textToMove = sec.content;
            let instructionText = '';
            
            const pMatch = sec.content.match(/^(<p class="font-bold[^>]*>.*?<\/p>)(?:<br>)?/);
            if (pMatch) {
              instructionText = pMatch[1];
              textToMove = sec.content.substring(pMatch[0].length);
            }
            
            if (textToMove.trim() !== '' && sec.questions && sec.questions.length > 0) {
              sec.questions[0].content = textToMove + (sec.questions[0].content ? `<br>${sec.questions[0].content}` : '');
              sec.content = instructionText;
              modified = true;
            }
          }
        }
        
        // Restore Missing Answers
        if (sec.questions) {
            sec.questions.forEach(q => {
              if (!q.correctAnswer && !q.options && q.explanation) {
                const match = q.explanation.match(/(?:đáp án đúng là|đáp án chính xác là|đáp án là|người được yêu cầu gặp là|người được gọi là|số điện thoại được nhắc đến là|người được tìm là|người cần gọi là|đáp án cho chỗ trống này là|từ cần điền là|thời gian đến nơi là|ngày đến là|đáp án:?)\s*:?\s*(.*?)(?:\.\s*$|$)/i);
                if (match && match[1]) {
                  let ans = match[1].trim();
                  if (ans.startsWith(':')) ans = ans.substring(1).trim();
                  ans = ans.replace(/[\.\"]+$/, '').trim();
                  if (ans) {
                    q.correctAnswer = ans;
                    modified = true;
                    totalRestored++;
                  }
                }
              }
            });
        }
      });
    });
    
    if (modified) {
      const { error: updateError } = await supabase.from('tests').update({ content_json: content }).eq('id', test.id);
      if (updateError) {
        console.error(`Failed to update ${test.title}:`, updateError);
      } else {
        console.log(`Updated ${test.title}`);
        updatedCount++;
      }
    }
  }
  
  console.log(`\nFinished updating ${updatedCount} tests. Restored ${totalRestored} answers.`);
}

fixUnit2();
