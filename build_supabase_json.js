const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);

if (!urlMatch || !keyMatch) {
  console.error("Supabase credentials not found in .env");
  process.exit(1);
}

const url = urlMatch[1].trim();
const key = keyMatch[1].trim();
const supabase = createClient(url, key);

function getEmoji(word) {
  // basic random emoji or deterministic emoji mapping based on word length for simplicity
  const emojis = ['🌟', '🔥', '💧', '🌿', '⚙️', '🛡️', '⚡', '✨', '🎯', '🚀', '💡', '🧠', '💪', '🍎', '🌈', '🧩', '🎨', '🏆', '💎', '🧸'];
  return emojis[word.length % emojis.length];
}

async function run() {
  const unitNum = process.argv[2];
  if (!unitNum) {
    console.error("Usage: node build_supabase_json.js <unit_num>");
    process.exit(1);
  }

  const jsonPath = `unit${unitNum}_raw.json`;
  if (!fs.existsSync(jsonPath)) {
    console.log(`Skipping Unit ${unitNum}, raw json not found.`);
    return;
  }

  const raw = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
  
  let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit${unitNum}_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit${unitNum}_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

  raw.words.forEach(w => {
    const emoji = getEmoji(w.word);
    wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${emoji}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron || ''}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos || ''}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
  });
  wordListHtml += `</div></div></div>`;

  let storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">${raw.story.title}</h1>`;
  
  raw.story.paragraphs.forEach(p => {
    let pReplaced = p;
    raw.words.forEach(w => {
      const regex = new RegExp(`\\b${w.word}\\b`, 'gi');
      pReplaced = pReplaced.replace(regex, `<b>$&</b>`);
    });
    storyHtml += `<p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">${pReplaced}</p>`;
  });
  storyHtml += `</div>`;

  // Filter out T/F questions or questions without 4 options
  let formattedWordListSections = [];
  raw.word_list_exercises.forEach((ex, idx) => {
    const validQs = ex.questions.filter(q => q.options && q.options.length >= 2);
    if (validQs.length > 0) {
      formattedWordListSections.push({
        id: `u${unitNum}_v3_wl_ex${idx+1}`,
        title: ex.title,
        content: "",
        questionType: "Trắc nghiệm",
        questions: validQs.map((q, i) => ({
          id: `u${unitNum}_v3_wl_q${idx}_${i}`,
          content: q.content,
          options: q.options,
          correctAnswer: q.correctAnswer,
          explanation: q.explanation || ''
        }))
      });
    }
  });

  let formattedStorySections = [];
  const validStoryQs = raw.story_exercise.questions.filter(q => q.options && q.options.length >= 2);
  if (validStoryQs.length > 0) {
    formattedStorySections.push({
      id: `u${unitNum}_v3_rd_ex1`,
      title: raw.story_exercise.title || "Answer the questions based on the story.",
      content: "",
      questionType: "Trắc nghiệm",
      questions: validStoryQs.map((q, i) => ({
        id: `u${unitNum}_v3_rd_q${i}`,
        content: q.content,
        options: q.options,
        correctAnswer: q.correctAnswer,
        explanation: q.explanation || ''
      }))
    });
  }

  const contentJson = {
    basicInfo: {
      skill: "Standard-Reading",
      title: `Unit ${unitNum}: Volume 3`,
      category: "exercise",
      timeLimit: 0
    },
    parts: [
      {
        id: "part1",
        title: "Word List",
        content: wordListHtml,
        sections: formattedWordListSections
      },
      {
        id: "part2",
        title: "Comprehensive Reading",
        content: storyHtml,
        imageUrl: `/unit${unitNum}_v3_story.png`,
        sections: formattedStorySections
      }
    ]
  };

  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';
  const folderId = '0f15a9d8-efc3-45ca-8fd3-aaa02ffa914c';
  const title = `Unit ${unitNum}: Volume 3`;

  const { data: existing, error: err2 } = await supabase.from('tests').select('id').eq('title', title).single();

  if (existing) {
    const { data, error } = await supabase
      .from('tests')
      .update({ content_json: contentJson, folder_id: folderId })
      .eq('id', existing.id);
    if (error) console.error('Error updating:', error);
    else console.log(`${title} updated in Supabase successfully!`);
  } else {
    const { data, error } = await supabase
      .from('tests')
      .insert({
        title: title,
        test_type: 'vocabulary',
        course_id: courseId,
        folder_id: folderId,
        content_json: contentJson,
        is_published: true
      });
    if (error) console.error('Error inserting:', error);
    else console.log(`${title} inserted into Supabase successfully!`);
  }
}

run();
