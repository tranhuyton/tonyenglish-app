const fs = require('fs');

const words = [
  { w: "admire", p: "[ədmaiər]", pos: "v.", d: "To admire someone is to like them for what they do.", e: "I admire my brother for his hard work.", emoji: "🤩" },
  { w: "aid", p: "[eid]", pos: "v.", d: "To aid someone is to help them when they need something.", e: "The doctor aided the boy after his accident.", emoji: "🤝" },
  { w: "attempt", p: "[ətempt]", pos: "v.", d: "To attempt something is to try to do that thing.", e: "I am attempting to learn English.", emoji: "🎯" },
  { w: "authority", p: "[əθɔ:rəti]", pos: "n.", d: "Authority is the power that someone has because of their position.", e: "The policeman has authority on the streets.", emoji: "👮" },
  { w: "capital", p: "[kæpitl]", pos: "n.", d: "A capital is an important city where a country's leaders live and work.", e: "We will visit the capital to learn about our government.", emoji: "🏛️" },
  { w: "cooperate", p: "[kouɑpəreit]", pos: "v.", d: "To cooperate is to work together to do something.", e: "The students cooperated to clean up the classroom.", emoji: "👥" },
  { w: "defend", p: "[difend]", pos: "v.", d: "To defend someone or something is to protect them from attack.", e: "The soldiers defended the town from the invaders.", emoji: "🛡️" },
  { w: "destruction", p: "[distrʌkʃən]", pos: "n.", d: "Destruction is damage to something so bad that it can't be fixed.", e: "After the big fire, there was much destruction in the city.", emoji: "🏚️" },
  { w: "disorder", p: "[disɔ:rdər]", pos: "n.", d: "Disorder is a lack of order, or a complete mess.", e: "The teacher's desk had many papers in disorder.", emoji: "🌪️" },
  { w: "division", p: "[diviʒən]", pos: "n.", d: "A division is the act of making smaller groups out of a larger one.", e: "The chart had six divisions which all had different colors.", emoji: "➗" },
  { w: "enable", p: "[ineibəl]", pos: "v.", d: "To enable a person is to make it possible for them to do something.", e: "Having the key enabled us to open the door.", emoji: "🔑" },
  { w: "frustrate", p: "[frʌstreit]", pos: "v.", d: "To frustrate is to prevent someone from fulfilling their desire.", e: "The machine frustrated me because I could not fix it.", emoji: "😫" },
  { w: "govern", p: "[gʌvərn]", pos: "v.", d: "To govern is to control the public business of a country, state, or city.", e: "The United States is governed from the White House.", emoji: "🇺🇸" },
  { w: "plenty", p: "[plenti]", pos: "n.", d: "To have plenty of something is to have more than you need.", e: "The school had plenty of books for the students to read.", emoji: "📚" },
  { w: "relieve", p: "[rili:v]", pos: "v.", d: "To relieve someone is to make them feel less pain.", e: "The medicine relieved the sick boy.", emoji: "💊" },
  { w: "reputation", p: "[repjəteiʃən]", pos: "n.", d: "Reputation is the opinion that people have about someone.", e: "The doctor had a reputation for helping people.", emoji: "⭐" },
  { w: "royal", p: "[rɔiəl]", pos: "adj.", d: "Royal describes something that belongs to a king or queen.", e: "The king sat upon the royal throne.", emoji: "👑" },
  { w: "slave", p: "[sleiv]", pos: "n.", d: "A slave is a person who is not free and must work for someone else.", e: "The slave worked very hard all day long.", emoji: "⛓️" },
  { w: "struggle", p: "[strʌgəl]", pos: "v.", d: "To struggle is to fight against someone or something.", e: "The kids struggled with each other for the toy.", emoji: "🤼" },
  { w: "stupid", p: "[stu:pid]", pos: "adj.", d: "When someone is stupid, they lack intelligence.", e: "He said something stupid that made everyone angry at him.", emoji: "🤦" }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit9_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit9_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(word => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${word.emoji}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${word.w}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${word.p}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${word.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${word.d}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${word.e}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Tale of Bartelby O'Boyle</h1><p style="margin-bottom: 1rem;">Long ago, there was a clever man by the name of Bartelby O'Boyle. As a boy, he was kept as a <b>slave</b> by the <b>royal</b> family. He saw other children play, but he always had to work. This <b>frustrated</b> him very much. But he was not <b>stupid</b>, and he wanted to change things.</p><p style="margin-bottom: 1rem;">Then one day there was a <b>struggle</b> for <b>authority</b> in the kingdom. There was a <b>division</b> of the people, and one group fought against another group to see which would <b>govern</b> the kingdom. There was <b>disorder</b> in the kingdom. Bartelby ran away. He saw much fighting and <b>destruction</b>. Many people had nothing to eat; Bartelby decided to <b>aid</b> them. He would help them get food. But how?</p><p style="margin-bottom: 1rem;">Bartelby went to the <b>capital</b> to find an answer. There, he met a man named Gilliam. A group of men <b>attempted</b> to hurt Gilliam. Bartelby <b>defended</b> him. Then, he gave Gilliam some food to <b>relieve</b> his hunger. After that, the two became friends. They took food from the rich and gave it to the poor.</p><p style="margin-bottom: 1rem;">Soon, other people <b>cooperated</b> with them. Working together <b>enabled</b> them to take more food, but they only took food from people who had <b>plenty</b>, and they always gave it to those who had none. Because of this, Bartleby gained a <b>reputation</b> across the kingdom. Even today, many people <b>admire</b> him for helping the poor.</p></div>`;

const data = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 9",
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
          "id": "sec1_wordlist_ex1",
          "title": "Exercise 1: Check the sentence with the bolded word that makes better sense.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u9_e1_1",
              "content": "1.",
              "options": [
                "a. Parents have authority over their children.",
                "b. Poor people aid rich people by giving them money."
              ],
              "correctAnswer": "a. Parents have authority over their children.",
              "explanation": "Parents have authority over their children."
            },
            {
              "id": "u9_e1_2",
              "content": "2.",
              "options": [
                "a. When you have authority, you cannot do anything.",
                "b. When people cooperate, they can get more done."
              ],
              "correctAnswer": "b. When people cooperate, they can get more done.",
              "explanation": "When people cooperate, they can get more done."
            },
            {
              "id": "u9_e1_3",
              "content": "3.",
              "options": [
                "a. You should admire people who tell lies.",
                "b. Learning a new language can frustrate some people."
              ],
              "correctAnswer": "b. Learning a new language can frustrate some people.",
              "explanation": "Learning a new language can frustrate some people."
            },
            {
              "id": "u9_e1_4",
              "content": "4.",
              "options": [
                "a. If you aid someone, he or she will usually thank you.",
                "b. If you cooperate with your friends, you will feel lonely."
              ],
              "correctAnswer": "a. If you aid someone, he or she will usually thank you.",
              "explanation": "If you aid someone, he or she will usually thank you."
            },
            {
              "id": "u9_e1_5",
              "content": "5.",
              "options": [
                "a. You should frustrate your friends when they help you.",
                "b. Most students admire teachers who work hard."
              ],
              "correctAnswer": "b. Most students admire teachers who work hard.",
              "explanation": "Most students admire teachers who work hard."
            }
          ]
        },
        {
          "id": "sec1_wordlist_ex3",
          "title": "Exercise 2: Check the one that suits the blank naturally.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u9_e3_1",
              "content": "1. If you help other people, ________________ .",
              "options": [
                "a. they will admire you",
                "b. they will struggle with you"
              ],
              "correctAnswer": "a. they will admire you",
              "explanation": "they will admire you"
            },
            {
              "id": "u9_e3_2",
              "content": "2. After the fight, ________________ .",
              "options": [
                "a. the room was in disorder",
                "b. the room got a reputation"
              ],
              "correctAnswer": "a. the room was in disorder",
              "explanation": "the room was in disorder"
            },
            {
              "id": "u9_e3_3",
              "content": "3. The people wanted change, ________________ .",
              "options": [
                "a. so they defended themselves",
                "b. so they elected a new person to govern the country"
              ],
              "correctAnswer": "b. so they elected a new person to govern the country",
              "explanation": "so they elected a new person to govern the country"
            },
            {
              "id": "u9_e3_4",
              "content": "4. Because I could not solve the problem, ________________ .",
              "options": [
                "a. I became frustrated",
                "b. there was a division between the animals"
              ],
              "correctAnswer": "a. I became frustrated",
              "explanation": "I became frustrated"
            },
            {
              "id": "u9_e3_5",
              "content": "5. She found a mistake on her homework, so ________________ .",
              "options": [
                "a. she aided it to be fixed",
                "b. she attempted to correct it"
              ],
              "correctAnswer": "b. she attempted to correct it",
              "explanation": "she attempted to correct it"
            },
            {
              "id": "u9_e3_6",
              "content": "6. After returning from the library, ________________ .",
              "options": [
                "a. we could cooperate with our books",
                "b. we had plenty of books to read"
              ],
              "correctAnswer": "b. we had plenty of books to read",
              "explanation": "we had plenty of books to read"
            },
            {
              "id": "u9_e3_7",
              "content": "7. After her friends laughed at her, ________________ .",
              "options": [
                "a. she thought that the royal palace looked beautiful",
                "b. she knew that her last remark was stupid"
              ],
              "correctAnswer": "b. she knew that her last remark was stupid",
              "explanation": "she knew that her last remark was stupid"
            },
            {
              "id": "u9_e3_8",
              "content": "8. You cannot tell me what to do. ________________ .",
              "options": [
                "a. I live in the capital city",
                "b. You don't have any authority"
              ],
              "correctAnswer": "b. You don't have any authority",
              "explanation": "You don't have any authority"
            },
            {
              "id": "u9_e3_9",
              "content": "9. Read the directions carefully. ________________ .",
              "options": [
                "a. They will cause destruction",
                "b. They will enable you to complete the project"
              ],
              "correctAnswer": "b. They will enable you to complete the project",
              "explanation": "They will enable you to complete the project"
            },
            {
              "id": "u9_e3_10",
              "content": "10. Before he can feel better, ________________ .",
              "options": [
                "a. he must find a way to relieve the pain",
                "b. he must become a slave"
              ],
              "correctAnswer": "a. he must find a way to relieve the pain",
              "explanation": "he must find a way to relieve the pain"
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": storyHtml,
      "imageUrl": "/unit9_story.png",
      "sections": [
        {
          "id": "sec2_reading",
          "title": "Reading Comprehension",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u9_r_1",
              "content": "1. What is this story about?",
              "options": [
                "a. How a slave became a king",
                "b. How a stupid mistake made Bartelby a slave",
                "c. How a lad found plenty of food",
                "d. How a man aided poor people"
              ],
              "correctAnswer": "d. How a man aided poor people",
              "explanation": "How a man aided poor people"
            },
            {
              "id": "u9_r_2",
              "content": "2. What did Bartelby do in the capital?",
              "options": [
                "a. He cooperated with his group of friends.",
                "b. He enabled Gilliam to have authority over the king.",
                "c. He relieved Gilliam of his hunger.",
                "d. He found a mask to wear."
              ],
              "correctAnswer": "c. He relieved Gilliam of his hunger.",
              "explanation": "He relieved Gilliam of his hunger."
            },
            {
              "id": "u9_r_3",
              "content": "3. In paragraph 1, we can infer that________",
              "options": [
                "a. Bartelby did not like the royal family",
                "b. the family attempted to cause disorder",
                "c. the other children were not clever",
                "d. Bartelby had a bad reputation"
              ],
              "correctAnswer": "a. Bartelby did not like the royal family",
              "explanation": "Bartelby did not like the royal family"
            },
            {
              "id": "u9_r_4",
              "content": "4. According to the passage, all the following are true EXCEPT",
              "options": [
                "a. people today still admire Bartleby",
                "b. Gilliam struggled with Bartley",
                "c. Bartleby defended Gilliam",
                "d. the fighting caused destruction"
              ],
              "correctAnswer": "b. Gilliam struggled with Bartley",
              "explanation": "Gilliam struggled with Bartley"
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit9.json', JSON.stringify(data, null, 2));
console.log('unit9.json created successfully!');
