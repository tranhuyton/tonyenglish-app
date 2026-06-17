const fs = require('fs');

const words = [
  { word: "acknowledge", phonetic: "[əknɑ́lɪdʒ]", type: "v.", meaning: "If you acknowledge something, you accept that it is true or that it exists.", example: "The teacher acknowledged that the young student was hungry." },
  { word: "ambassador", phonetic: "[æmbǽsədər]", type: "n.", meaning: "An ambassador is a government worker who works in another country.", example: "The ambassador from Korea was in charge of the conference." },
  { word: "blonde", phonetic: "[blɑnd]", type: "n.", meaning: "If someone is a blonde, they have light-colored hair.", example: "My cousin is different from me. She is a blonde with blue eyes." },
  { word: "conquer", phonetic: "[kɑ́ŋkər]", type: "v.", meaning: "To conquer a country means to attack and take control of it.", example: "The soldiers were trying to conquer the world." },
  { word: "drag", phonetic: "[dræg]", type: "v.", meaning: "To drag something means to pull it across the ground.", example: "The dog was dragging his owner down the street." },
  { word: "exaggerate", phonetic: "[ɪgzǽdʒəreɪt]", type: "v.", meaning: "To exaggerate is to say that something is bigger or better than it really is.", example: "Jimmy wasn’t exaggerating about the seriousness of his injury." },
  { word: "heritage", phonetic: "[hérɪtɪdʒ]", type: "n.", meaning: "Heritage is the collection of features of a society, such as language and religion.", example: "Teepees are part of the heritage of the American Indians of the plains." },
  { word: "insult", phonetic: "[ɪ́nsʌlt]", type: "v.", meaning: "To insult someone is to say things that will hurt their feelings.", example: "The girls insulted each other all afternoon." },
  { word: "meanwhile", phonetic: "[míːnhwaɪl]", type: "adv.", meaning: "Meanwhile means until something happens or while something is happening.", example: "He wants to be a doctor in the future, but meanwhile, he works a regular job." },
  { word: "necklace", phonetic: "[néklɪs]", type: "n.", meaning: "A necklace is a piece of jewelry that people wear around their necks.", example: "Joyce received a lovely pearl necklace for her wedding anniversary." },
  { word: "noble", phonetic: "[nóubl]", type: "n.", meaning: "A noble is a rich and powerful person.", example: "The Queen invited a noble from a nearby country to dinner." },
  { word: "precious", phonetic: "[préʃəs]", type: "adj.", meaning: "When something is precious, it is valuable and important.", example: "In a desert, water can be more precious than money." },
  { word: "prejudice", phonetic: "[prédʒədɪs]", type: "n.", meaning: "A prejudice is an unfair opinion about someone before you get to know them.", example: "The company’s rules against gender prejudice must be enforced." },
  { word: "rumor", phonetic: "[rúːmər]", type: "n.", meaning: "A rumor is a story that may not be true.", example: "Carla was spreading rumors around the office." },
  { word: "sin", phonetic: "[sɪn]", type: "n.", meaning: "A sin is something that is wrong for religious reasons.", example: "Taking something that doesn’t belong to you is a sin." },
  { word: "spectacle", phonetic: "[spéktəkl]", type: "n.", meaning: "A spectacle is an amazing sight.", example: "Niagara Falls is quite a spectacle." },
  { word: "stack", phonetic: "[stæk]", type: "n.", meaning: "A stack is a pile of different things.", example: "There was a stack of paperwork on his desk to complete." },
  { word: "suspicious", phonetic: "[səspɪ́ʃəs]", type: "adj.", meaning: "If someone is suspicious of someone else, they do not trust that person.", example: "Dad was suspicious of the caller on the line." },
  { word: "tin", phonetic: "[tɪn]", type: "n.", meaning: "Tin is a cheap white metal.", example: "Soup is a common food that is often sold in tin cans." },
  { word: "vase", phonetic: "[veɪs]", type: "n.", meaning: "A vase is an attractive container where people keep flowers.", example: "The vase was filled with such lovely flowers." }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit27_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit27_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetic}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.meaning}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.example}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

let readingHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Pizarro and the Inca Gold</h1><p style="margin-bottom: 1rem;">According to <b>rumors</b>, there’s lots of <b>precious</b> gold hidden in the jungles of Peru. It got there when the Spanish <b>conquered</b> parts of South America. The Spanish <b>noble</b>, Francisco Pizarro, arrived in Peru in the 1500s. He found a group of people called the Incas. The Incas believed that their leader, Atahualpa, was both a king and a god. But Pizarro didn’t agree.</p><p style="margin-bottom: 1rem;">“It is a <b>sin</b> for a man to think he is God!” he said to Atahualpa.</p><p style="margin-bottom: 1rem;">Atahualpa thought Pizarro was <b>insulting</b> his <b>heritage</b>. He thought the <b>blonde</b> Spanish men held <b>prejudices</b> against the Incas. But Atahualpa was a kind man and didn’t want to fight the Spaniards. He said, “If I give you a room full of gold, will you leave my country in peace?”</p><p style="margin-bottom: 1rem;">Pizarro was <b>suspicious</b>. He thought Atahualpa was <b>exaggerating</b>. But a few days later, Pizarro returned to the Inca palace with his <b>ambassadors</b>. He saw a room filled with <b>stacks</b> of gold. There were golden <b>necklaces</b>, cups, plates and <b>vases</b>. It was a great <b>spectacle</b>. He <b>acknowledged</b> that Atahualpa had told the truth. But after seeing the gold, he wanted all of Peru’s gold. So he didn’t leave the country.</p><p style="margin-bottom: 1rem;">The Spanish soldiers stayed in Peru and grabbed all the gold they could find. But the Inca people tricked the Spaniards. They mixed the gold with <b>tin</b> so that it was poor quality. They gave this gold to the Spaniards. <b>Meanwhile</b>, they hid the good gold. They stuffed it into sacks and <b>dragged</b> it deep into the jungle. The Spanish conquerors never found the gold. People think it is still there today.</p></div>`;

const data = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 27",
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
          title: "Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "1",
              content: "1. something you keep flowers in",
              options: ["a. vase", "b. stack", "c. tin", "d. spectacle"],
              correctAnswer: "a. vase",
              explanation: "vase là bình hoa (something you keep flowers in)."
            },
            {
              id: "2",
              content: "2. to say something is better than it really is",
              options: ["a. exaggerate", "b. drag", "c. heritage", "d. insult"],
              correctAnswer: "a. exaggerate",
              explanation: "exaggerate nghĩa là phóng đại (to say something is better than it really is)."
            },
            {
              id: "3",
              content: "3. a rich and important person",
              options: ["a. ambassador", "b. noble", "c. rumor", "d. conquer"],
              correctAnswer: "b. noble",
              explanation: "noble là quý tộc (a rich and important person)."
            },
            {
              id: "4",
              content: "4. having light, yellow-colored hair",
              options: ["a. suspicious", "b. blonde", "c. acknowledge", "d. precious"],
              correctAnswer: "b. blonde",
              explanation: "blonde là người có mái tóc vàng."
            },
            {
              id: "5",
              content: "5. not trusting of someone",
              options: ["a. suspicious", "b. meanwhile", "c. necklace", "d. prejudice"],
              correctAnswer: "a. suspicious",
              explanation: "suspicious là đáng ngờ, không tin tưởng ai đó (not trusting of someone)."
            }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Part B: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "6",
              content: "1. heritage",
              options: ["a. features of a society", "b. to put into something else", "c. a government worker", "d. a rich and powerful person"],
              correctAnswer: "a. features of a society",
              explanation: "heritage là di sản (features of a society)."
            },
            {
              id: "7",
              content: "2. spectacle",
              options: ["a. an amazing sight", "b. to take something", "c. something that is wrong", "d. a piece of jewelry"],
              correctAnswer: "a. an amazing sight",
              explanation: "spectacle là cảnh tượng ngoạn mục (an amazing sight)."
            },
            {
              id: "8",
              content: "3. drag",
              options: ["a. to attack", "b. very important", "c. not trusting", "d. to pull something"],
              correctAnswer: "d. to pull something",
              explanation: "drag là kéo (to pull something)."
            },
            {
              id: "9",
              content: "4. sin",
              options: ["a. something wrong for religious reasons", "b. the traditions of a country", "c. a place to keep flowers", "d. an official working in a foreign country"],
              correctAnswer: "a. something wrong for religious reasons",
              explanation: "sin là tội lỗi (something wrong for religious reasons)."
            },
            {
              id: "10",
              content: "5. tin",
              options: ["a. a color of hair", "b. to say mean things", "c. a cheap metal", "d. to control a country"],
              correctAnswer: "c. a cheap metal",
              explanation: "tin là thiếc (a cheap metal)."
            }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: readingHtml,
      imageUrl: "/unit27_v3_story.png",
      sections: [
        {
          id: "sec3",
          title: "Part A: Mark each statement T for true or F for false. Rewrite the false statements to make them true.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "11",
              content: "1. Atahualpa didn't want to fight the Spaniards.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "Atahualpa was a kind man and didn't want to fight the Spaniards."
            },
            {
              id: "12",
              content: "2. The Incas had blonde hair.",
              options: ["T", "F"],
              correctAnswer: "F",
              explanation: "The Spanish had blonde hair."
            },
            {
              id: "13",
              content: "3. Atahualpa offered Pizarro a room filled with stacks of precious gold.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "He said, “If I give you a room full of gold, will you leave my country in peace?”"
            },
            {
              id: "14",
              content: "4. The Spanish conquered parts of South America.",
              options: ["T", "F"],
              correctAnswer: "T",
              explanation: "The Spanish conquered parts of South America."
            },
            {
              id: "15",
              content: "5. Pizarro thought that Atahualpa had insulted his heritage and that his men held prejudices against the Incas.",
              options: ["T", "F"],
              correctAnswer: "F",
              explanation: "Atahualpa thought that Pizarro had insulted his heritage and held prejudices."
            },
            {
              id: "16",
              content: "6. Pizarro agreed that Atahualpa was both a god and a king.",
              options: ["T", "F"],
              correctAnswer: "F",
              explanation: "Pizarro did not agree that Atahualpa was both a god and a king."
            }
          ]
        },
        {
          id: "sec4",
          title: "Part B: Answer the questions.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "17",
              content: "1. Which of the following did NOT appear in the room with gold?",
              options: ["a. Pieces of tin", "b. Necklaces", "c. Vases", "d. Cups"],
              correctAnswer: "a. Pieces of tin",
              explanation: "There were golden necklaces, cups, plates and vases. Tin did not appear in the room."
            },
            {
              id: "18",
              content: "2. Which adjective describes Pizarro?",
              options: ["a. Noble", "b. Gentle", "c. Suspicious", "d. Sensitive"],
              correctAnswer: "a. Noble",
              explanation: "The text says: The Spanish noble, Francisco Pizarro, arrived in Peru in the 1500s."
            },
            {
              id: "19",
              content: "3. What do the rumors say?",
              options: ["a. Pizarro defeated the Incas easily", "b. There is a lot of gold in the Peruvian jungle", "c. The Incas discovered the Spanish", "d. The Spanish arrived in Peru in the 1500s"],
              correctAnswer: "b. There is a lot of gold in the Peruvian jungle",
              explanation: "Theo đoạn văn: According to rumors, there’s lots of precious gold hidden in the jungles of Peru."
            },
            {
              id: "20",
              content: "4. Who went to the room of gold with Pizarro?",
              options: ["a. The King of Spain", "b. Spanish ambassadors", "c. Men from the jungle", "d. Tin makers"],
              correctAnswer: "b. Spanish ambassadors",
              explanation: "Theo đoạn văn: Pizarro returned to the Inca palace with his ambassadors."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit27_raw.json', JSON.stringify(data, null, 2));
console.log("Successfully created unit27_raw.json");
