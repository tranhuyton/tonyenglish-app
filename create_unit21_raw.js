const fs = require('fs');

const words = [
  { word: "accustomed", phonetics: "[əkʌ́stəmd]", type: "adj.", def: "When you become accustomed to something, you are in the habit of it.", example: "Grandfather is accustomed to reading the newspaper every morning." },
  { word: "affirm", phonetics: "[əfə́:rm]", type: "v.", def: "To affirm is to say that something is true.", example: "Using a graph, Malcolm affirmed the success of the company." },
  { word: "astonished", phonetics: "[əstɑ́niʃt]", type: "adj.", def: "If someone is astonished, they are very surprised or shocked.", example: "I was astonished when he pulled the live rabbit out of his hat." },
  { word: "bang", phonetics: "[bæŋ]", type: "v.", def: "To bang is to hit something to make a noise.", example: "The drummer banged on his drum as he marched in the parade." },
  { word: "clan", phonetics: "[klæn]", type: "n.", def: "A clan is a group of relatives or friends.", example: "The Lee clan meets every year to celebrate the New Year." },
  { word: "dim", phonetics: "[dim]", type: "adj.", def: "When something is dim, it does not give out much light.", example: "Working in a dim room is bad for your eyes." },
  { word: "emphasis", phonetics: "[émfəsis]", type: "n.", def: "Emphasis is special attention or importance.", example: "The students put special emphasis on chapter 4 because it will be on the test." },
  { word: "fable", phonetics: "[féibəl]", type: "n.", def: "A fable is a short story that teaches a lesson.", example: "In the fable about the tortoise and the hare, the lesson is consistency." },
  { word: "feast", phonetics: "[fi:st]", type: "n.", def: "A feast is a large meal for many people.", example: "At Thanksgiving, I enjoy a wonderful feast with my family." },
  { word: "glow", phonetics: "[glou]", type: "v.", def: "To glow is to make a soft light.", example: "The small flame glowed softly." },
  { word: "hollow", phonetics: "[hɑ́lou]", type: "adj.", def: "When something is hollow, it has an empty space inside.", example: "Straws are hollow, so liquid can flow through them." },
  { word: "instinct", phonetics: "[ínstiŋkt]", type: "n.", def: "Instinct is the natural way that people behave without thinking about it.", example: "Cats hunt mice because of instinct." },
  { word: "joint", phonetics: "[dʒɔint]", type: "n.", def: "A joint is a place of the body where the bones meet, such as the knee.", example: "Two important bones in your leg meet at a joint in your knee." },
  { word: "leak", phonetics: "[li:k]", type: "v.", def: "To leak is to let a liquid or gas pass through a flaw.", example: "The pipe leaks from many places." },
  { word: "physician", phonetics: "[fizíʃən]", type: "n.", def: "A physician is a doctor.", example: "The physician said I would feel better if I took my medicine." },
  { word: "sacrifice", phonetics: "[sǽkrəfàis]", type: "v.", def: "To sacrifice something valuable is to give it up to get something else.", example: "Her parents sacrificed a lot of money in order for her to go to college." },
  { word: "stiff", phonetics: "[stif]", type: "adj.", def: "When something is stiff, it is hard to move.", example: "The bird was standing on the tree's stiff branch." },
  { word: "stroke", phonetics: "[strouk]", type: "v.", def: "To stroke is to move a hand over something or someone.", example: "She stroked her cheek to see if there was something on it." },
  { word: "tragic", phonetics: "[trǽdʒik]", type: "adj.", def: "When something is tragic, it is connected with death and suffering.", example: "The airplane crashed in a tragic accident." },
  { word: "tune", phonetics: "[tju:n]", type: "n.", def: "A tune is a song.", example: "The students played a familiar tune for the audience." }
];

let wordListHtml = '<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit21_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit21_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">';

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetics}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.example}</div></div></div>`;
});
wordListHtml += '</div></div></div>';

let readingHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Old Man with a Bump</h1><p style="margin-bottom: 1rem;">An old man had a large bump on his face. He went to the best <b>physician</b> in town. He gave the old man <b>tragic</b> news: "I can't do anything. You'll have to get <b>accustomed</b> to it."</p><p style="margin-bottom: 1rem;">One day, the old man went into the forest. Suddenly, the light became <b>dim</b>. It was going to rain. So he found a <b>hollow</b> tree to sit under. It <b>leaked</b> a little, but there was no other place he could wait.</p><p style="margin-bottom: 1rem;">When the rain stopped, his <b>joints</b> felt <b>stiff</b> from sitting. Suddenly, he heard a <b>tune</b> coming from far away. Many <b>fables</b> said monsters lived in the forest. No one could <b>affirm</b> that the stories were true, though. Still, his <b>instincts</b> told him that there was something out there. He walked farther into the forest. Then he saw a fire <b>glowing</b>. He was <b>astonished</b> to see a <b>clan</b> of monsters. They were having a great <b>feast</b> and <b>banging</b> on drums.</p><p style="margin-bottom: 1rem;">He stood behind a tree, spying on them. Then the leader asked, "Who's the best dancer here?"</p><p style="margin-bottom: 1rem;">"Me!" the man yelled, coming from behind the tree. He started to dance. When he was finished, the leader said, "I want you to dance every night. In order to make sure you return, I'm going to keep something you love."</p><p style="margin-bottom: 1rem;">"Please don't take my bump," he begged. "I can't <b>sacrifice</b> it. It's good luck!" He exclaimed, pointing at it for <b>emphasis</b>.</p><p style="margin-bottom: 1rem;">The monsters agreed that they had to take his bump. After they did, the man <b>stroked</b> his face to make sure it was gone. He had tricked them! He never went back, and he never had to worry about his bump again.</p></div>`;

const json = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 21",
    "category": "exercise",
    "timeLimit": 0
  },
  "parts": [
    {
      "id": "part1",
      "title": "Word List",
      "content": wordListHtml,
      "sections": [
        {
          "id": "sec1",
          "title": "Exercise 1: Choose the right definition for the given word.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "1",
              "content": "1. stroke",
              "options": ["to surprise", "to move a hand", "a light", "to speak"],
              "correctAnswer": "to move a hand",
              "explanation": "b"
            },
            {
              "id": "2",
              "content": "2. sacrifice",
              "options": ["to give up", "to allow", "to cry", "to say"],
              "correctAnswer": "to give up",
              "explanation": "a"
            },
            {
              "id": "3",
              "content": "3. joint",
              "options": ["very sad", "a large meal", "a short story", "where two bones meet"],
              "correctAnswer": "where two bones meet",
              "explanation": "d"
            },
            {
              "id": "4",
              "content": "4. emphasis",
              "options": ["family", "a song", "a doctor", "special attention"],
              "correctAnswer": "special attention",
              "explanation": "d"
            },
            {
              "id": "5",
              "content": "5. hollow",
              "options": ["natural", "cannot move", "to connect", "empty"],
              "correctAnswer": "empty",
              "explanation": "d"
            }
          ]
        },
        {
          "id": "sec2",
          "title": "Exercise 2: Write a word that is similar in meaning to the underlined part.",
          "content": "",
          "questionType": "Điền từ",
          "questions": [
            {
              "id": "6",
              "content": "1. She avoided walking in [low-light] areas.",
              "blanks": [{ "id": "1", "answer": "dim" }]
            },
            {
              "id": "7",
              "content": "2. Since she's lived in hot places all her life, she's [used to] warm weather.",
              "blanks": [{ "id": "1", "answer": "accustomed" }]
            },
            {
              "id": "8",
              "content": "3. The holes in the old pipes let water [pass through] onto the bathroom floor.",
              "blanks": [{ "id": "1", "answer": "leak" }]
            },
            {
              "id": "9",
              "content": "4. Her back felt [hard to move] after she slept on the floor.",
              "blanks": [{ "id": "1", "answer": "stiff" }]
            },
            {
              "id": "10",
              "content": "5. He was happy to go home and see the [group of family and friends].",
              "blanks": [{ "id": "1", "answer": "clan" }]
            },
            {
              "id": "11",
              "content": "6. The very [shocked] crowd watched as the magician performed his tricks.",
              "blanks": [{ "id": "1", "answer": "astonished" }]
            },
            {
              "id": "12",
              "content": "7. The school served a [large meal] in honor of the new principal.",
              "blanks": [{ "id": "1", "answer": "feast" }]
            },
            {
              "id": "13",
              "content": "8. The only thing that I could see in the dark night was my flashlight [making light].",
              "blanks": [{ "id": "1", "answer": "glowing" }]
            },
            {
              "id": "14",
              "content": "9. It was a very [sad event] when his parents passed away in the accident.",
              "blanks": [{ "id": "1", "answer": "tragic" }]
            },
            {
              "id": "15",
              "content": "10. Her [natural behavior] told her to leave the room as soon as possible.",
              "blanks": [{ "id": "1", "answer": "instincts" }]
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": readingHtml,
      "imageUrl": "/unit21_v3_story.png",
      "sections": [
        {
          "id": "sec3",
          "title": "Reading Comprehension - Part A: Mark each statement T for true or F for false.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "16",
              "content": "1. The physician told the old man there was nothing he could do.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            },
            {
              "id": "17",
              "content": "2. The old man waited in the hollow tree even though it leaked a little.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            },
            {
              "id": "18",
              "content": "3. The old man's joints were stiff from walking in the forest.",
              "options": ["T", "F"],
              "correctAnswer": "F",
              "explanation": "False / The old man's joints were stiff from sitting under a tree for a long time."
            },
            {
              "id": "19",
              "content": "4. The old man's instincts told him to return home immediately.",
              "options": ["T", "F"],
              "correctAnswer": "F",
              "explanation": "False / The old man's instincts told him there was something in the forest."
            },
            {
              "id": "20",
              "content": "5. The man danced for the clan of monsters.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            },
            {
              "id": "21",
              "content": "6. The monsters took away the man's tragic bump.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            }
          ]
        },
        {
          "id": "sec4",
          "title": "Reading Comprehension - Part B: Answer the questions.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "22",
              "content": "1. What advice did the doctor give the old man?",
              "options": ["To bang", "To make", "To sacrifice", "To get accustomed to it"],
              "correctAnswer": "To get accustomed to it",
              "explanation": "d"
            },
            {
              "id": "23",
              "content": "2. Why did the man have to wait inside a hollow tree?",
              "options": ["The light became dim.", "It began to rain.", "He was hiding from monsters.", "His joints hurt."],
              "correctAnswer": "It began to rain.",
              "explanation": "b"
            },
            {
              "id": "24",
              "content": "3. Why did the old man come out from behind the tree?",
              "options": ["To run away", "To eat", "To dance", "To play music"],
              "correctAnswer": "To dance",
              "explanation": "c"
            },
            {
              "id": "25",
              "content": "4. Why does the old man stroke his face at the end of the story?",
              "options": ["To astonish the monsters", "To make sure the bump is gone", "For emphasis", "To affirm that the bump is there"],
              "correctAnswer": "To make sure the bump is gone",
              "explanation": "b"
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit21_raw.json', JSON.stringify(json, null, 2));
