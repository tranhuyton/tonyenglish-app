const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

async function fixUnit1() {
  const { data: tests, error } = await supabase.from('tests')
    .select('id, title, content_json')
    .ilike('title', 'Unit 1: Listening Activity%');
    
  if (error) {
    console.error(error);
    return;
  }
  
  let updatedCount = 0;
  
  for (const test of tests) {
    let modified = false;
    const content = test.content_json;
    if (!content || !content.parts || content.parts.length === 0) continue;
    
    content.parts.forEach(part => {
      // Fix Transcript Formatting
      if (part.explanation && (part.explanation.includes('<br>') || part.explanation.includes('<br/>') || part.explanation.includes('<br />'))) {
        let transcript = part.explanation;
        
        // Remove enclosing <p> tags if present
        if (transcript.startsWith('<p') && transcript.endsWith('</p>')) {
          transcript = transcript.replace(/^<p[^>]*>/, '').replace(/<\/p>$/, '');
        }
        
        // Split by <br>, <br/>, <br />
        const lines = transcript.split(/<br\s*\/?>/i);
        
        // Rebuild with <p> tags and bold character names (e.g., "1. ")
        const newTranscript = lines.map(line => {
          let trimmed = line.trim();
          if (!trimmed) return '';
          
          // Bold the speaker name or number if it matches pattern like "1. ", "Man:", "Customer 1:"
          // Wait, the rule says "Tên nhân vật ở đầu mỗi câu thoại phải được bôi đậm".
          // If it's already bolded (<b>...</b>), keep it. If it starts with "Number. " or "Name: ", bold it.
          // Since we can't be perfect with regex for names vs regular text unless there's a colon, we look for a colon or a leading number.
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
            // Find where the instruction ends and where the brackets begin.
            // But since we just prepended the instruction, it might be in sec.content.
            // Actually, the rule says "cắt toàn bộ đoạn văn bản chứa các chỗ trống [ 1 ]... và dán tất cả vào content của Câu hỏi 1".
            // If the section content has a table or div wrapping the brackets, we should move the entire block.
            // To be safe, we can move the whole sec.content to questions[0].content except the first <p> which we just added for instruction!
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
  
  console.log(`\nFinished updating ${updatedCount} tests.`);
}

fixUnit1();
