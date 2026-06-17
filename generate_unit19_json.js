const fs = require('fs');

const words = [
  { word: 'alive', phonetic: '[alaiv]', type: 'adj.', def: 'If someone or something is alive, they are not dead.', ex: 'My grandparents are still alive even though they are over 90.' },
  { word: 'bone', phonetic: '[boun]', type: 'n.', def: 'A bone is a hard part of the body.', ex: 'I brought home a nice bone for my dog.' },
  { word: 'bother', phonetic: '[bɑðər]', type: 'v.', def: 'To bother is to make the effort to do something.', ex: 'No one bothered to wash the dishes today.' },
  { word: 'captain', phonetic: '[kæptin]', type: 'n.', def: 'A captain is the person who leads a ship or airplane.', ex: 'The captain sailed his ship to Australia.' },
  { word: 'conclusion', phonetic: '[kənklu:ʒən]', type: 'n.', def: 'The conclusion of something is the final part of it.', ex: 'At the conclusion of the race, the spectators cheered for the winner.' },
  { word: 'doubt', phonetic: '[daut]', type: 'n.', def: 'Doubt is a feeling of not being sure.', ex: 'I have doubt that the story is true.' },
  { word: 'explore', phonetic: '[iksplɔ:r]', type: 'v.', def: 'To explore is to look for new places.', ex: 'He wants to explore the world and see new things.' },
  { word: 'foreign', phonetic: '[fɔ(:)rin]', type: 'adj.', def: 'If something is foreign, it is from a different country.', ex: 'Mexican food is a popular foreign food.' },
  { word: 'glad', phonetic: '[glæd]', type: 'adj.', def: 'If you are glad, you are happy.', ex: 'I am glad you came to my party.' },
  { word: 'however', phonetic: '[hauevər]', type: 'adv.', def: 'However means despite or not being influenced by something.', ex: 'She is a great cook. However, she never had professional lessons.' },
  { word: 'injustice', phonetic: '[indʒʌstis]', type: 'n.', def: 'Injustice is a lack of fairness or justice.', ex: 'Putting an innocent person in jail is an act of injustice.' },
  { word: 'international', phonetic: '[intərnæʃənəl]', type: 'adj.', def: 'If something is international, it involves more than one country.', ex: 'The United Nations is a powerful international organization.' },
  { word: 'lawyer', phonetic: '[lɔ:jər]', type: 'n.', def: 'A lawyer works with the law and represents people in court.', ex: 'The lawyer left the courthouse after the judge made her decision.' },
  { word: 'mention', phonetic: '[menʃən]', type: 'v.', def: 'To mention something is to talk about it.', ex: 'The doctors mentioned the problems that the patient was having.' },
  { word: 'policy', phonetic: '[paləsi]', type: 'n.', def: 'A policy is a rule.', ex: 'He told us that his policy was to put customers first.' },
  { word: 'social', phonetic: '[souʃəl]', type: 'adj.', def: 'If something is social, it is about many people in a community.', ex: 'People should come together and fix the world\'s social problems.' },
  { word: 'speech', phonetic: '[spi:tʃ]', type: 'n.', def: 'A speech is something said to a group of people.', ex: 'She gave a speech to the class.' },
  { word: 'staff', phonetic: '[stæf]', type: 'n.', def: 'A staff is a group of people working together in a company.', ex: 'My dad has a staff of four people to help him at the office.' },
  { word: 'toward', phonetic: '[təwɔ:rd]', type: 'prep.', def: 'If you go toward something, you go closer to it.', ex: 'Santa walked toward my house with a special tree.' },
  { word: 'wood', phonetic: '[wud]', type: 'n.', def: 'Wood is the thing that trees are made of.', ex: 'I put the pieces of wood in a pile.' }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit19_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit19_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

const icons = ['😎', '🚀', '🌟', '🎨', '📚', '🧩', '🏆', '💡', '🎸', '🌍', '😎', '🚀', '🌟', '🎨', '📚', '🧩', '🏆', '💡', '🎸', '🌍'];

words.forEach((w, i) => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${icons[i]}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetic}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; ">    <h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Shipwrecked</h1>        <p style="margin-bottom: 1rem;">Simon Yates was a <b>lawyer</b>. He helped many people. <b>However</b>, he was not a nice man. His <b>policy</b> was to help only rich people. He didn't <b>bother</b> about <b>social</b> <b>injustice</b>. He made a lot of money, but many people didn't like him. Even people on his <b>staff</b> didn't like him. They wanted bad things to happen to him. In fact, they were <b>glad</b> when he got into trouble.</p>    <p style="margin-bottom: 1rem;">Simon had a very bad day. He did many things wrong and lost his job. Soon, he didn't have any money. His wife, Mrs. Yates, began to have <b>doubts</b> about him. Simon wanted to start a new life. He planned to leave the country.</p>    <p style="margin-bottom: 1rem;">He <b>mentioned</b> his plan to the <b>captain</b> of a ship. The <b>captain</b> was <b>exploring</b> the world. The <b>captain</b> felt bad for Simon and said, "I will take you to <b>foreign</b> countries." They left the next day.</p>    <p style="margin-bottom: 1rem;">Near the <b>conclusion</b> of their <b>international</b> trip, the weather turned bad. A wave pushed Simon off the boat. But he was <b>alive</b>. He swam <b>toward</b> an island. After a long time he got there.</p>    <p style="margin-bottom: 1rem;">At first he was upset. He was lost and alone. "I'll never go home again," he thought. He had a lot of problems, but he survived. He built a house in a tree. He lived on a diet of fish. He made tools from <b>wood</b> and <b>bones</b>. He made a cup to drink rainwater.</p>    <p style="margin-bottom: 1rem;">Slowly he learned to be happy on the island. He swam every day. He had trouble sometimes, but he always found a way to fix the problem. Life was simple. He liked it.</p>    <p style="margin-bottom: 1rem;">Finally, people on a ship saw Simon on the island. They wanted to take him home. But Simon was happy. He gave them a long <b>speech</b> about life. He said he wanted to stay. He liked his new, simple life more than his old life.</p></div>`;

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 19",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordListHtml,
      sections: [
        {
          id: "sec1_wordlist",
          title: "Exercise 1: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. mention", options: ["to say", "to look at", "to not believe", "to be happy"], correctAnswer: "to say", explanation: "mention nghĩa là nói đến (to say/talk about)." },
            { id: "2", content: "2. social", options: ["about many countries", "not dead", "about many people", "about a different country"], correctAnswer: "about many people", explanation: "social nghĩa là thuộc về xã hội, liên quan đến nhiều người." },
            { id: "3", content: "3. lawyer", options: ["to be treated unfairly", "a person who works with the law", "leader", "a part of the body"], correctAnswer: "a person who works with the law", explanation: "lawyer là luật sư." },
            { id: "4", content: "4. however", options: ["the last part", "part of a tree", "a rule", "despite something"], correctAnswer: "despite something", explanation: "however có nghĩa là tuy nhiên (despite something)." },
            { id: "5", content: "5. bother", options: ["to look for new places", "to make the effort to do something", "to talk about something", "to not believe"], correctAnswer: "to make the effort to do something", explanation: "bother nghĩa là cất công, nỗ lực làm gì." }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 2: Fill in the blanks with the correct words from the word bank: wood, policy, staff, toward, speech",
          content: "",
          questionType: "Điền từ",
          questions: [
            { id: "6", content: "1. My new desk is made of (wo____[6]).", correctAnswer: "wood", explanation: "desk made of wood (gỗ)." },
            { id: "7", content: "2. Students must start class at 9:00 each morning. This is the school's (po____[7]).", correctAnswer: "policy", explanation: "rule (quy định) -> policy." },
            { id: "8", content: "3. There are over 500 people on the hospital's (st____[8]).", correctAnswer: "staff", explanation: "people working -> staff (nhân viên)." },
            { id: "9", content: "4. Go (to____[9]) the river, but stop before you get in the water!", correctAnswer: "toward", explanation: "hướng về phía -> toward." },
            { id: "10", content: "5. The president gave a (sp____[10]) last night.", correctAnswer: "speech", explanation: "give a speech (bài phát biểu)." }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 3: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Điền từ",
          questions: [
            { id: "11", content: "1. He gave a talk to a group of people at the meeting. (spe[11])", correctAnswer: "speech", explanation: "talk to a group -> speech." },
            { id: "12", content: "2. Did anyone make the effort to do their homework? (bo[12])", correctAnswer: "bother", explanation: "make the effort -> bother." },
            { id: "13", content: "3. The chair is made of the material trees are made of. (wo[13])", correctAnswer: "wood", explanation: "material trees are made of -> wood." },
            { id: "14", content: "4. The group of workers helped him with his work. (s[14])", correctAnswer: "staff", explanation: "group of workers -> staff." },
            { id: "15", content: "5. He is not dead; I saw him yesterday. (a[15])", correctAnswer: "alive", explanation: "not dead -> alive." }
          ]
        },
        {
          id: "sec4_wordlist",
          title: "Exercise 4: Fill in the blanks with the correct words from the word bank: mentioned, however, policy, staff, speech, bothered, conclusion, injustice, bones, doubt",
          content: "",
          questionType: "Điền từ",
          questions: [
            { id: "16", content: "My teacher's name is Mrs. Smith. Yesterday, she gave a (sp____[16]) to our class.", correctAnswer: "speech", explanation: "gave a speech." },
            { id: "17", content: "She said there was a new (po____[17]) about the school diet.", correctAnswer: "policy", explanation: "new policy (quy định)." },
            { id: "18", content: "The school's (st____[18]) decided that their students didn't eat healthily.", correctAnswer: "staff", explanation: "school staff (nhân viên)." },
            { id: "19", content: "She said milk gives our bodies stronger (bo____[19]).", correctAnswer: "bones", explanation: "stronger bones (xương)." },
            { id: "20", content: "She also (me____[20]) that sugar is bad for us.", correctAnswer: "mentioned", explanation: "mentioned (nhắc đến)." },
            { id: "21", content: "She said she had no (do____[21]) that we would all feel better.", correctAnswer: "doubt", explanation: "no doubt (không nghi ngờ)." },
            { id: "22", content: "We all thought that it was an (in____[22]).", correctAnswer: "injustice", explanation: "an injustice (sự bất công)." },
            { id: "23", content: "But at the (co____[23]) of class, she told us one more thing, 'It was a joke!'", correctAnswer: "conclusion", explanation: "at the conclusion (cuối)." },
            { id: "24", content: "(Ho____[24]), no one thought that it was very funny.", correctAnswer: "however", explanation: "however (tuy nhiên)." },
            { id: "25", content: "And no students (bo____[25]) to laugh.", correctAnswer: "bothered", explanation: "bothered to laugh (bận tâm cười)." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit19_story.png",
      sections: [
        {
          id: "sec5_reading",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "26", content: "1. What is this story about?", options: ["How the captain of a ship explored foreign places", "How a lawyer stayed alive alone on an island", "Why a man and a woman went on an international trip", "Why it is a good policy to worry about social problems"], correctAnswer: "How a lawyer stayed alive alone on an island", explanation: "Câu chuyện kể về một luật sư sống sót một mình trên đảo." },
            { id: "27", content: "2. Why does Simon not stay on the boat?", options: ["The staff do not like him.", "He wants to swim toward an island.", "A wave pushes him off the ship.", "He does not like the diet of only fish."], correctAnswer: "A wave pushes him off the ship.", explanation: "Một cơn sóng đã đẩy ông ta khỏi thuyền (A wave pushed Simon off the boat)." },
            { id: "28", content: "3. How does Simon stay alive on the island?", options: ["He makes tools from bones and wood.", "He makes clothes from a tree.", "He eats food from the trees.", "He uses a cup to drink seawater."], correctAnswer: "He makes tools from bones and wood.", explanation: "Ông ta tạo ra công cụ từ xương và gỗ (He made tools from wood and bones)." },
            { id: "29", content: "4. What did Simon mention in his speech?", options: ["He wanted to see Mrs. Yates.", "He was unhappy to be alone.", "He was glad to be on the island.", "He had doubts about staying on the island."], correctAnswer: "He was glad to be on the island.", explanation: "Ông nói muốn ở lại và thích cuộc sống mới (glad to be on the island)." },
            { id: "30", content: "5. What happens near the conclusion of Simon's trip?", options: ["The weather became very bad.", "He saw a ship", "He went home", "He got lost"], correctAnswer: "The weather became very bad.", explanation: "Gần cuối chuyến đi quốc tế, thời tiết trở nên tồi tệ (the weather turned bad)." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit19.json', JSON.stringify(json, null, 2));
console.log('Successfully generated unit19.json');
