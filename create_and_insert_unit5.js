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

const words = [
  { word: "aware", pos: "adj.", pron: "[əwéər]", def: "If you are aware of something, you know about it.", ex: "I was not aware of the ringing phone.", emoji: "👀" },
  { word: "badly", pos: "adv.", pron: "[bædli]", def: "Badly means in a severe or harmful way.", ex: "He hurt his arm badly playing with friends.", emoji: "🤕" },
  { word: "belong", pos: "v.", pron: "[bilɔ́:ŋ]", def: "If something belongs to you, you own it.", ex: "The blue suit belongs to Paul.", emoji: "👔" },
  { word: "continue", pos: "v.", pron: "[kəntínju:]", def: "To continue something is to keep doing it.", ex: "She stood under her umbrella as the rain continued to fall.", emoji: "☔" },
  { word: "error", pos: "n.", pron: "[érər]", def: "An error is something you do wrong.", ex: "I made an error on my report, so my boss was angry.", emoji: "❌" },
  { word: "experience", pos: "n.", pron: "[ikspíəriəns]", def: "An experience is something you have seen or done.", ex: "Rock climbing was a fun experience.", emoji: "🧗" },
  { word: "field", pos: "n.", pron: "[fi:ld]", def: "A field is a big area of land.", ex: "The field of flowers looked so pretty.", emoji: "🌻" },
  { word: "hurt", pos: "v.", pron: "[hə:rt]", def: "To hurt is to do something that makes you feel pain.", ex: "She hurt her leg falling down the stairs.", emoji: "🩹" },
  { word: "judgment", pos: "n.", pron: "[dʒʌ́dʒmənt]", def: "Judgment is the ability to form opinions or decisions.", ex: "It’s good judgment to recycle your aluminum cans.", emoji: "🧠" },
  { word: "likely", pos: "adv.", pron: "[láikli]", def: "If something likely happens, it will probably happen.", ex: "I will likely stay at home and watch TV tonight.", emoji: "📺" },
  { word: "normal", pos: "adj.", pron: "[nɔ́:rməl]", def: "If something is normal, it is not strange nor surprising to you.", ex: "It is normal for me to bathe every night.", emoji: "🛁" },
  { word: "rare", pos: "adj.", pron: "[rɛər]", def: "If something is rare, you do not see it very often.", ex: "It is rare for him to miss his flight.", emoji: "✈️" },
  { word: "relax", pos: "v.", pron: "[rilǽks]", def: "To relax is to rest.", ex: "The frog relaxed in the warm sun.", emoji: "🐸" },
  { word: "request", pos: "v.", pron: "[rikwést]", def: "To request something is to ask for it.", ex: "The little girl requested a special gift from Santa Claus.", emoji: "🎁" },
  { word: "reside", pos: "v.", pron: "[rizáid]", def: "To reside means to live somewhere permanently or for a long time.", ex: "My brother and his family reside in a lovely house on the beach.", emoji: "🏠" },
  { word: "result", pos: "n.", pron: "[rizʌ́lt]", def: "A result is something that happens because of something else.", ex: "As a result of all the rain, the man had to climb on the roof.", emoji: "🌧️" },
  { word: "roll", pos: "v.", pron: "[roul]", def: "To roll is to move by turning over and over.", ex: "You must roll the ball into the pins when you bowl.", emoji: "🎳" },
  { word: "since", pos: "prep.", pron: "[sins]", def: "Since is used to talk about a past event still happening now.", ex: "Since 1992, he has been driving that car.", emoji: "🚗" },
  { word: "visible", pos: "adj.", pron: "[vízəbəl]", def: "If something is visible, it can be seen.", ex: "The moon and stars were visible in the night sky.", emoji: "✨" },
  { word: "wild", pos: "adj.", pron: "[waild]", def: "If something is wild, it is found in nature.", ex: "You should be careful around a fox, because it is a wild animal.", emoji: "🦊" }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit5_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit5_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${w.emoji}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Jackal and the Sun Child</h1><p style="margin-bottom: 1rem;">A jackal is a <b>wild</b> dog with a big black back. It <b>resides</b> in the desert. But how did the jackal get his black back? This was how it happened.</p><p style="margin-bottom: 1rem;">One day, the jackal saw a girl. She was sitting upon a rock. She was not a <b>normal</b> child. She was a <b>rare</b> and beautiful sun child. She was bright and warm like the sun. The child saw the jackal and smiled.</p><p style="margin-bottom: 1rem;">She said, "Jackal, I have been <b>relaxing</b> on this rock for too long. I must get home soon. But, I am slow and you are fast. You will <b>likely</b> get me home more quickly." Then she <b>requested</b>, "Will you carry me home? If you do, I'll give you a gift. This necklace <b>belongs</b> to me, but I will give it to you."</p><p style="margin-bottom: 1rem;">The <b>wild</b> jackal agreed. So the sun child sat on the dog's back. They started to walk. But soon, the jackal felt ill. The sun child was very hot on his back. The heat was <b>hurting</b> his back very <b>badly</b>. "I made a terrible <b>error</b> in <b>judgment</b>." he thought. He shouldn't have agreed to carry her. So he asked her to get off.</p><p style="margin-bottom: 1rem;">But she did not. The jackal's back <b>continued</b> to get hotter and hotter. He had to get away from the sun child. So he made a plan. First, he ran as fast as he could. He hoped the sun child would fall off. But she did not. So when the sun child was looking at the sky, not <b>aware</b> of the jackal's next plan, he jumped into a <b>field</b> of flowers. As a <b>result</b>, the child <b>rolled</b> off his back. The jackal ran away.</p><p style="margin-bottom: 1rem;">But the sun child left a mark on the jackal's back, a <b>visible</b> black mark. Ever <b>since</b> his <b>experience</b> with the sun child, the jackal has had a black back.</p></div>`;
const wordListSections = [
  {
    "id": "u5_wl_ex1",
    "title": "Part A: Choose the right definition for the given word.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u5_q1",
        "content": "1. roll",
        "options": ["to rest", "a rule", "to grow", "to move by turning"],
        "correctAnswer": "to move by turning",
        "explanation": "roll nghĩa là lăn, di chuyển bằng cách lật qua lật lại."
      },
      {
        "id": "u5_q2",
        "content": "2. error",
        "options": ["a nice man", "very old", "something you do wrong", "open land"],
        "correctAnswer": "something you do wrong",
        "explanation": "error nghĩa là lỗi lầm."
      },
      {
        "id": "u5_q3",
        "content": "3. hurt",
        "options": ["to disagree", "how much something costs", "from nature", "to do something that causes pain"],
        "correctAnswer": "to do something that causes pain",
        "explanation": "hurt nghĩa là làm đau."
      },
      {
        "id": "u5_q4",
        "content": "4. reside",
        "options": ["to relax", "to live in a place for long", "something that can be seen", "to know about something"],
        "correctAnswer": "to live in a place for long",
        "explanation": "reside nghĩa là cư trú."
      },
      {
        "id": "u5_q5",
        "content": "5. relax",
        "options": ["to keep going", "a large group of people", "to rest", "to move"],
        "correctAnswer": "to rest",
        "explanation": "relax nghĩa là thư giãn, nghỉ ngơi."
      },
      {
        "id": "u5_q6",
        "content": "6. continue",
        "options": ["to be in the right place", "to stay", "to have", "to keep doing something"],
        "correctAnswer": "to keep doing something",
        "explanation": "continue nghĩa là tiếp tục."
      },
      {
        "id": "u5_q7",
        "content": "7. normal",
        "options": ["the perfect amount", "friendly", "not strange", "different"],
        "correctAnswer": "not strange",
        "explanation": "normal nghĩa là bình thường, không xa lạ."
      },
      {
        "id": "u5_q8",
        "content": "8. rare",
        "options": ["quiet", "not full", "interesting", "not seen often"],
        "correctAnswer": "not seen often",
        "explanation": "rare nghĩa là hiếm, không thường thấy."
      },
      {
        "id": "u5_q9",
        "content": "9. visible",
        "options": ["from nature", "easy to see", "new", "normal"],
        "correctAnswer": "easy to see",
        "explanation": "visible nghĩa là có thể nhìn thấy."
      },
      {
        "id": "u5_q10",
        "content": "10. field",
        "options": ["open land", "to reside", "a thing", "a tool"],
        "correctAnswer": "open land",
        "explanation": "field nghĩa là cánh đồng."
      }
    ]
  },
  {
    "id": "u5_wl_ex2",
    "title": "Part B: Choose the right word for the given definition.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u5_q11",
        "content": "1. in a severe or harmful way",
        "options": ["continue", "wild", "judgment", "badly"],
        "correctAnswer": "badly",
        "explanation": "badly nghĩa là một cách tồi tệ, nghiêm trọng."
      },
      {
        "id": "u5_q12",
        "content": "2. the ability to form opinions or decisions",
        "options": ["experience", "reside", "judgment", "result"],
        "correctAnswer": "judgment",
        "explanation": "judgment nghĩa là khả năng phán đoán, đánh giá."
      },
      {
        "id": "u5_q13",
        "content": "3. to fit or be in the right place",
        "options": ["roll", "relax", "continue", "belong"],
        "correctAnswer": "belong",
        "explanation": "belong nghĩa là thuộc về, phù hợp, đúng chỗ."
      },
      {
        "id": "u5_q14",
        "content": "4. not strange or different",
        "options": ["normal", "visible", "uncommon", "aware"],
        "correctAnswer": "normal",
        "explanation": "normal nghĩa là bình thường."
      },
      {
        "id": "u5_q15",
        "content": "5. to do something that makes you feel pain",
        "options": ["rare", "hurt", "error", "since"],
        "correctAnswer": "hurt",
        "explanation": "hurt nghĩa là làm đau."
      }
    ]
  },
  {
    "id": "u5_wl_ex3",
    "title": "Part C: Write a word that is similar in meaning to the underlined part.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u5_q16",
        "content": "1. My day at school was not strange. (nor______)",
        "options": ["normal", "wild", "hurt", "relax"],
        "correctAnswer": "normal",
        "explanation": "normal có nghĩa tương tự 'not strange'."
      },
      {
        "id": "u5_q17",
        "content": "2. The bird was from nature. (wi___)",
        "options": ["wild", "normal", "rare", "visible"],
        "correctAnswer": "wild",
        "explanation": "wild có nghĩa tương tự 'from nature'."
      },
      {
        "id": "u5_q18",
        "content": "3. Sorry I can’t come; I’m feeling discomfort in my body. (h______)",
        "options": ["hurt", "relax", "badly", "error"],
        "correctAnswer": "hurt",
        "explanation": "hurt có nghĩa tương tự 'discomfort in my body'."
      },
      {
        "id": "u5_q19",
        "content": "4. He’s going to rest instead of going to the movie. (r________)",
        "options": ["relax", "reside", "request", "roll"],
        "correctAnswer": "relax",
        "explanation": "relax có nghĩa tương tự 'rest'."
      },
      {
        "id": "u5_q20",
        "content": "5. The man walked through a large area of land. (f______)",
        "options": ["field", "result", "experience", "judgment"],
        "correctAnswer": "field",
        "explanation": "field có nghĩa tương tự 'large area of land'."
      }
    ]
  }
];

const storySections = [
  {
    "id": "u5_rd_ex1",
    "title": "Answer the questions based on the story.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u5_q21",
        "content": "1. What is this story about?",
        "options": [
          "Why the sun child has a beautiful smile",
          "Why a wild dog hurt a sun child",
          "An error that the sun child once made",
          "How the jackal got his visible black mark"
        ],
        "correctAnswer": "How the jackal got his visible black mark",
        "explanation": "Câu chuyện giải thích lý do vì sao con chó sói có một vệt đen trên lưng."
      },
      {
        "id": "u5_q22",
        "content": "2. What kind of girl was the sun child?",
        "options": [
          "She was rare and beautiful.",
          "She was likely very shy.",
          "She was an ill child.",
          "She was a normal child."
        ],
        "correctAnswer": "She was rare and beautiful.",
        "explanation": "Cô bé mặt trời được miêu tả là 'rare and beautiful'."
      },
      {
        "id": "u5_q23",
        "content": "3. Why did the jackal run into the field?",
        "options": [
          "To continue his journey",
          "It wanted a new place to reside.",
          "To take a nap and relax",
          "To get away from the sun child"
        ],
        "correctAnswer": "To get away from the sun child",
        "explanation": "Chó sói chạy vào cánh đồng để cố gắng thoát khỏi sức nóng từ cô bé mặt trời."
      },
      {
        "id": "u5_q24",
        "content": "4. What happened at the end of the story?",
        "options": [
          "The sun child forgot the experience.",
          "The sun child became aware of the jackal’s black back.",
          "The sun child rolled off the jackal’s back.",
          "The sun child has stayed upon the jackal’s back since then."
        ],
        "correctAnswer": "The sun child rolled off the jackal’s back.",
        "explanation": "Cô bé lăn khỏi lưng chó sói khi nó nhảy vào cánh đồng hoa."
      },
      {
        "id": "u5_q25",
        "content": "5. What did the sun child request?",
        "options": [
          "For the jackal to give her a necklace.",
          "For the jackal to carry her home.",
          "For the jackal to run fast.",
          "For the jackal to jump into a field."
        ],
        "correctAnswer": "For the jackal to carry her home.",
        "explanation": "Cô bé yêu cầu chó sói cõng mình về nhà."
      }
    ]
  }
];

const contentJson = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 5",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordListHtml,
      sections: wordListSections
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit5_story.png",
      sections: storySections
    }
  ]
};

async function run() {
  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';

  const { data: existing, error: err2 } = await supabase.from('tests').select('id').eq('title', 'Unit 5').single();

  if (existing) {
    const { data, error } = await supabase
      .from('tests')
      .update({ content_json: contentJson })
      .eq('id', existing.id);
    if (error) console.error('Error updating:', error);
    else console.log('Unit 5 updated in Supabase successfully!');
  } else {
    const { data, error } = await supabase
      .from('tests')
      .insert({
        title: 'Unit 5',
        test_type: 'vocabulary',
        course_id: courseId,
        content_json: contentJson,
        is_published: true
      });
    if (error) console.error('Error inserting:', error);
    else console.log('Unit 5 inserted into Supabase successfully!');
  }
}

run();
