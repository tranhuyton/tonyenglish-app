const fs = require('fs');

const words = [
  { word: "advice", phonetics: "[ədváis]", type: "n.", meaning: "Advice is an opinion about what to do.", example: "I don't know how to study for my exams. Can you give me some advice?" },
  { word: "along", phonetics: "[əlɔ́(ː)ŋ]", type: "prep.", meaning: "Along means to move from one part of a road, river, etc. to another.", example: "Walk along this tunnel for ten minutes, and you'll see a door on the left." },
  { word: "attention", phonetics: "[əténʃən]", type: "n.", meaning: "Attention is the notice, thought, or consideration of someone.", example: "His work got the attention of two of his co-workers." },
  { word: "attract", phonetics: "[ətrǽkt]", type: "v.", meaning: "To attract means to make a person or thing come closer or be interested.", example: "The magnet attracted the metal." },
  { word: "climb", phonetics: "[klaim]", type: "v.", meaning: "To climb means to use your hands and feet to go up on something.", example: "The girls climbed to the top of the mountain." },
  { word: "drop", phonetics: "[drɔp]", type: "v.", meaning: "To drop is to fall or allow something to fall.", example: "A small amount of water dropped from the bottle." },
  { word: "final", phonetics: "[fáinl]", type: "adj.", meaning: "If something is final, it is the last part.", example: "In the final part of the film, the man and the woman got married." },
  { word: "further", phonetics: "[fə́ːrðər]", type: "adj.", meaning: "Further is used to say something is from a distance or time.", example: "The escalator is further along than I thought." },
  { word: "imply", phonetics: "[implái]", type: "v.", meaning: "To imply something is to suggest it without saying it.", example: "The man implied that he wanted the job, but he didn't say so." },
  { word: "maintain", phonetics: "[meintéin]", type: "v.", meaning: "To maintain means to make something stay the same.", example: "The balls maintain constant movement." },
  { word: "neither", phonetics: "[níːðər]", type: "adv.", meaning: "You use neither to connect two negative statements.", example: "Neither the pass on the left nor the pass on the right will lead us home." },
  { word: "otherwise", phonetics: "[ʌ́ðərwàiz]", type: "adv.", meaning: "Otherwise means different or in another way.", example: "It's good to stay active; otherwise, you'll gain weight." },
  { word: "physical", phonetics: "[fízikəl]", type: "adj.", meaning: "If something is physical, it is related to your body and not your mind.", example: "Biking is good for your physical health." },
  { word: "prove", phonetics: "[pruːv]", type: "v.", meaning: "To prove something is to show that it is true.", example: "My teacher proved the answer on the board." },
  { word: "react", phonetics: "[riǽkt]", type: "v.", meaning: "To react is to act in a certain way because of something that happened.", example: "James reacted badly to the news." },
  { word: "ride", phonetics: "[raid]", type: "v.", meaning: "To ride something is to travel on it. You can ride an animal, a bike, etc.", example: "I will ride a roller-coaster for the first time today." },
  { word: "situated", phonetics: "[sítʃuèitid]", type: "adj.", meaning: "If something is situated somewhere, it is in that place.", example: "The white board is situated between the two men." },
  { word: "society", phonetics: "[səsáiəti]", type: "n.", meaning: "Society is people and the way that they live.", example: "Society expects people to be good and honest." },
  { word: "standard", phonetics: "[stǽndərd]", type: "n.", meaning: "A standard is what people consider normal or good.", example: "This older model TV is below our store's standards." },
  { word: "suggest", phonetics: "[səgdʒést]", type: "v.", meaning: "To suggest something means to give an idea or plan about it.", example: "He suggested that we go to see his boss." }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit26_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit26_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetics}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.meaning}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.example}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const storyRaw = `Archie and His Donkey
Old Archie needed some money. He decided to sell his donkey. So he and his son Tom went to town. It was situated many miles away.
Soon, they met a woman. "Where are you going?" she asked.
"To town," said Archie.
"Any smart person would ride the donkey," she said.
"What are you implying?" Archie asked. "I'm very smart!" Archie wanted to look smart. So he climbed onto the donkey. Then they continued in the direction of the town.
Further along the road, they met a farmer.
"Hello," said Archie. "We want to sell this donkey. Do you want to buy it?"
"I don't need a donkey," said the farmer. "But if you want my advice, don't ride it. The donkey needs to be in good physical condition."
"Good idea," said Archie. "Tom, I want you to ride it. You're lighter."
"Neither you nor your son should ride it. It looks very tired. You should carry the donkey," suggested the farmer.
"You're right," said Archie. "Come on, Tom! We'll carry it for the final few miles!"
The donkey was very heavy, and they couldn't maintain a good speed. They didn't arrive until late in the evening. At last, they walked into the town. But there they attracted the attention of some teenage boys. They laughed at Tom and Archie. They started to throw stones at them. The donkey reacted by kicking. Tom and Archie dropped the donkey. It fell on the ground and then ran away. Archie lost his donkey. He went home with no money.
What does this story teach us? We cannot please everyone in our society. Don't take everyone's advice, but set your own standards. Prove to everyone you can make decisions by yourself. Otherwise, you may end up with nothing at all.`;

let paragraphs = storyRaw.split('\n').filter(p => p.trim().length > 0);
let title = paragraphs[0];
let bodyLines = paragraphs.slice(1);

let storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">${title}</h1>`;

bodyLines.forEach(line => {
  let p = line;
  const wordMatches = words.map(w => w.word);
  wordMatches.forEach(w => {
    const regex = new RegExp(`\\b(${w})(s|ed|ing|d|es)?\\b`, "gi");
    p = p.replace(regex, "<b>$1$2</b>");
  });
  storyHtml += `<p style="margin-bottom: 1rem;">        ${p}</p>`;
});

storyHtml += `</div>`;
storyHtml = storyHtml.replace(/\n/g, '').replace(/\r/g, '').replace(/\t/g, '');

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 26",
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
          id: "sec1",
          title: "Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "1",
              content: "1. to keep something going",
              options: ["maintain", "react", "standard", "prove"],
              correctAnswer: "maintain",
              explanation: "maintain nghĩa là duy trì, giữ cho việc gì đó tiếp tục."
            },
            {
              id: "2",
              content: "2. not this one or that one",
              options: ["neither", "further", "along", "situated"],
              correctAnswer: "neither",
              explanation: "neither nghĩa là không cái này cũng không cái kia."
            },
            {
              id: "3",
              content: "3. people and how they act",
              options: ["otherwise", "society", "advice", "climb"],
              correctAnswer: "society",
              explanation: "society nghĩa là xã hội, con người và cách họ sống."
            },
            {
              id: "4",
              content: "4. describing the body",
              options: ["final", "drop", "physical", "attention"],
              correctAnswer: "physical",
              explanation: "physical nghĩa là thuộc về thể chất."
            },
            {
              id: "5",
              content: "5. to make someone interested",
              options: ["imply", "suggest", "attract", "ride"],
              correctAnswer: "attract",
              explanation: "attract nghĩa là thu hút, làm ai đó quan tâm."
            }
          ]
        },
        {
          id: "sec2",
          title: "Part B: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Điền từ",
          questions: [
            {
              id: "6",
              content: "1. How did Clare act when you told her about the party? (re[1])",
              options: [],
              correctAnswer: "react",
              explanation: "react: phản ứng"
            },
            {
              id: "7",
              content: "2. In this group of people, wearing hats is common. (soc[2])",
              options: [],
              correctAnswer: "society",
              explanation: "society: xã hội, nhóm người"
            },
            {
              id: "8",
              content: "3. I invited Jane and Lisa to my house, but not Jane or Lisa could come. (nei[3])",
              options: [],
              correctAnswer: "neither",
              explanation: "neither: không phải một trong hai"
            },
            {
              id: "9",
              content: "4. I've nearly finished the book. I'm on the last page. (f[4])",
              options: [],
              correctAnswer: "final",
              explanation: "final: cuối cùng"
            },
            {
              id: "10",
              content: "5. I can jump higher than you. Watch me, and I will show you that I can do it. (p[5])",
              options: [],
              correctAnswer: "prove",
              explanation: "prove: chứng minh"
            }
          ]
        },
        {
          id: "sec3",
          title: "Part C: Choose the word that is a better fit for each sentence.",
          content: "",
          questionType: "Điền từ",
          questions: [
            { id: "11", content: "1a. Can I give you some [1]? (suggest / advice)", options: [], correctAnswer: "advice", explanation: "advice là lời khuyên." },
            { id: "12", content: "1b. I [2] that you do your homework before you go out. (suggest / advice)", options: [], correctAnswer: "suggest", explanation: "suggest là đề nghị, gợi ý." },
            { id: "13", content: "2a. I got everyone's [3] with my new dress. (situated / attention)", options: [], correctAnswer: "attention", explanation: "attention là sự chú ý." },
            { id: "14", content: "2b. Where is your office [4] in the building? (situated / attention)", options: [], correctAnswer: "situated", explanation: "situated là nằm ở vị trí nào đó." },
            { id: "15", content: "3a. The [5] of his work is very high. (dropped / standard)", options: [], correctAnswer: "standard", explanation: "standard là tiêu chuẩn." },
            { id: "16", content: "3b. I accidentally [6] my phone in the snow. (dropped / standard)", options: [], correctAnswer: "dropped", explanation: "dropped là đánh rơi." },
            { id: "17", content: "4a. He [7] my attention by waving to me. (attracted / reacted)", options: [], correctAnswer: "attracted", explanation: "attracted là thu hút." },
            { id: "18", content: "4b. She [8] badly to the news. (attracted / reacted)", options: [], correctAnswer: "reacted", explanation: "reacted là phản ứng." },
            { id: "19", content: "5a. How much [9] is the beach? I'm tired! (further / along)", options: [], correctAnswer: "further", explanation: "further là xa hơn." },
            { id: "20", content: "5b. We walked [10] the path for two hours. (further / along)", options: [], correctAnswer: "along", explanation: "along là dọc theo." }
          ]
        },
        {
          id: "sec4",
          title: "Part D: Check the one that suits the blank naturally.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "21",
              content: "1. She was angry when__________.",
              options: ["he implied that she was not smart", "he proved that she was right"],
              correctAnswer: "he implied that she was not smart",
              explanation: "Cô ấy tức giận khi anh ta ám chỉ rằng cô ấy không thông minh."
            },
            {
              id: "22",
              content: "2. If you want to win the race, you need to __________.",
              options: ["be in good physical condition", "drop off all of your extra work"],
              correctAnswer: "be in good physical condition",
              explanation: "Cần phải có thể lực tốt (physical condition) để thắng cuộc đua."
            },
            {
              id: "23",
              content: "3. He said that I should play sports, so I __________.",
              options: ["suggested playing football", "gave him my advice"],
              correctAnswer: "suggested playing football",
              explanation: "Gợi ý (suggest) chơi bóng đá phù hợp với vế trước."
            },
            {
              id: "24",
              content: "4. The sound of the car's horn__________.",
              options: ["got everyone's attention", "is situated next to the bus stop"],
              correctAnswer: "got everyone's attention",
              explanation: "Tiếng còi ô tô thu hút sự chú ý của mọi người (attention)."
            },
            {
              id: "25",
              content: "5. We are nearly at Jack's house.__________.",
              options: ["It's much further down the road", "He lives along this road"],
              correctAnswer: "He lives along this road",
              explanation: "Anh ấy sống dọc theo (along) con đường này."
            }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit26_story.png",
      sections: [
        {
          id: "sec_reading",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "26",
              content: "1. What is the main idea of this story?",
              options: ["You should always take the advice of older people.", "Teenage boys are the nicest people in society.", "You should set your own standards.", "You should neither ride nor carry a donkey."],
              correctAnswer: "You should set your own standards.",
              explanation: "Đoạn cuối câu chuyện chỉ ra bài học: Hãy thiết lập tiêu chuẩn của riêng bạn (set your own standards)."
            },
            {
              id: "27",
              content: "2. Why did Archie get on the donkey?",
              options: ["The woman implied that he wasn't smart.", "The town was situated further away than he had thought.", "He did not want to climb the final hill.", "His walking speed was too slow."],
              correctAnswer: "The woman implied that he wasn't smart.",
              explanation: "Archie leo lên lừa vì người phụ nữ ngầm ám chỉ (implied) ông không thông minh."
            },
            {
              id: "28",
              content: "3. Why did the farmer suggest carrying the donkey?",
              options: ["To attract people's attention", "To keep the donkey in good physical condition", "To maintain their speed", "To prove that Archie was strong"],
              correctAnswer: "To keep the donkey in good physical condition",
              explanation: "Người nông dân khuyên vậy vì con lừa cần có thể trạng tốt (good physical condition)."
            },
            {
              id: "29",
              content: "4. Why did the donkey start kicking?",
              options: ["It didn't want to be carried along the road.", "It didn't want to go in the direction of the river.", "It reacted badly to a group of teenage boys' teasing.", "It became very angry at Archie and Tom."],
              correctAnswer: "It reacted badly to a group of teenage boys' teasing.",
              explanation: "Con lừa phản ứng (reacted) khi bị bọn trẻ trêu chọc và ném đá."
            },
            {
              id: "30",
              content: "5. What did the teenage boys do when they saw Archie, Tom, and the donkey?",
              options: ["They laughed at Tom and Archie and started to throw stones.", "They tried to buy the donkey.", "They gave Archie some advice.", "They helped carry the donkey."],
              correctAnswer: "They laughed at Tom and Archie and started to throw stones.",
              explanation: "Bọn trẻ cười nhạo và bắt đầu ném đá."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit26.json', JSON.stringify(json, null, 2));
console.log('JSON file created successfully.');
