const fs = require('fs');
const { createClient } = require('@supabase/supabase-js');
const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());

async function run() {
  const { data, error } = await supabase.from('tests').select('id, title, content_json').ilike('title', '%Volume 3%');
  if (error) {
    console.error(error);
    return;
  }
  
  for (let test of data) {
    if (!test.content_json.parts || !test.content_json.basicInfo) {
      console.log(`Fixing ${test.title}`);
      
      const newJson = {
        basicInfo: {
          skill: "Standard-Reading",
          title: test.title.replace(': Volume 3', ''),
          category: "exercise",
          timeLimit: 0
        },
        parts: []
      };

      // Part 1: Word List
      if (test.content_json.wordList) {
        let contentHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;">`;
        // add images
        const unitNum = test.title.replace('Unit ', '').replace(': Volume 3', '');
        contentHtml += `<div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit${unitNum}_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit${unitNum}_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div>`;
        contentHtml += `<div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;
        
        for (let w of test.content_json.wordList) {
          contentHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">??</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetic || ''}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type || ''}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.meaning || ''}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">? ${w.example || ''}</div></div></div>`;
        }
        contentHtml += `</div></div></div>`;

        let part1 = {
          id: "part1",
          title: "Word List",
          content: contentHtml.replace(/[\n\r]/g, ''),
          sections: []
        };
        
        if (test.content_json.exercises && test.content_json.exercises.length > 0) {
           part1.sections = test.content_json.exercises;
        }
        newJson.parts.push(part1);
      }

      // Part 2: Story
      if (test.content_json.story) {
        let contentHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">${test.content_json.story.title}</h1>`;
        for (let p of test.content_json.story.paragraphs) {
          contentHtml += `<p style="margin-bottom: 1rem;">${p}</p>`;
        }
        contentHtml += `</div>`;
        
        const unitNum = test.title.replace('Unit ', '').replace(': Volume 3', '');
        
        let part2 = {
          id: "part2",
          title: "Comprehensive Reading",
          content: contentHtml.replace(/[\n\r]/g, ''),
          imageUrl: `/unit${unitNum}_v3_story.png`,
          sections: []
        };
        
        if (test.content_json.readingComprehension) {
           part2.sections.push(test.content_json.readingComprehension);
        }
        newJson.parts.push(part2);
      }

      const { error: updateError } = await supabase.from('tests').update({ content_json: newJson }).eq('id', test.id);
      if (updateError) {
         console.error(`Error updating ${test.title}`, updateError);
      } else {
         console.log(`Success ${test.title}`);
      }
    }
  }
}
run();
