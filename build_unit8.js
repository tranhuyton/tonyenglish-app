const fs = require('fs');

const words = [
  { word: "broad", pron: "[brɔ:d]", pos: "adj.", def: "If something is broad, it is wide.", ex: "The river is very long and broad." },
  { word: "bush", pron: "[buʃ]", pos: "n.", def: "A bush is a plant with many thin branches. It is smaller than a tree.", ex: "My dad and I planted some small bushes around the house." },
  { word: "capable", pron: "[keipəbəl]", pos: "adj.", def: "If someone or something is capable of something, they can do it.", ex: "The Olympic athlete is capable of lifting a lot of weight." },
  { word: "cheat", pron: "[tʃi:t]", pos: "v.", def: "To cheat is to be dishonest so that you can win or do well.", ex: "They cheated on the test by sharing answers." },
  { word: "concentrate", pron: "[kɑnsəntreit]", pos: "v.", def: "To concentrate on someone or something is to give your full attention.", ex: "I could not concentrate on my homework because the room was so loud." },
  { word: "conclude", pron: "[kənklu:d]", pos: "v.", def: "To conclude is to arrive at a logical end by looking at evidence.", ex: "I saw crumbs on my dog’s face, so I concluded that he ate my cookie." },
  { word: "confident", pron: "[kɑnfidənt]", pos: "adj.", def: "Confident means that one believes they can do something without failing.", ex: "She was confident she could climb the mountain due to her training." },
  { word: "considerable", pron: "[kənsidərəbəl]", pos: "adj.", def: "If something is considerable, it is large in size, amount or extent.", ex: "They paid a considerable amount of money for that car." },
  { word: "convey", pron: "[kənvei]", pos: "v.", def: "To convey is to communicate or make ideas known.", ex: "That picture of a crying child conveys a feeling of sadness." },
  { word: "definite", pron: "[defənit]", pos: "adj.", def: "If something is definite, it is certain or sure to be true.", ex: "There is a definite connection between hard work and success." },
  { word: "delight", pron: "[dilait]", pos: "n.", def: "Delight is a feeling of being very happy with something.", ex: "He felt such delight after getting a promotion at work." },
  { word: "destination", pron: "[destəneiʃən]", pos: "n.", def: "A destination is the place where someone or something is going to.", ex: "The destination of this plane is Munich, Germany." },
  { word: "dictate", pron: "[dikteit]", pos: "v.", def: "To dictate something is to read it aloud so it can be written down.", ex: "He dictated his speech so his secretary could write it down." },
  { word: "edge", pron: "[edʒ]", pos: "n.", def: "The edge of something is the part of it that is farthest from the center.", ex: "He ran to the edge of the cliff." },
  { word: "path", pron: "[pæθ]", pos: "n.", def: "A path is a way from one place to another that people can walk along.", ex: "We followed a path through the woods." },
  { word: "resort", pron: "[rizɔ:rt]", pos: "v.", def: "To resort to something is to depend on it in order to solve a problem.", ex: "I hope they don’t resort to violence to end the argument." },
  { word: "shadow", pron: "[ʃædou]", pos: "n.", def: "A shadow is the dark area that is made when something blocks light.", ex: "The man’s shadow was taller than he was." },
  { word: "succeed", pron: "[səksi:d]", pos: "v.", def: "To succeed is to complete something that you planned or tried to do.", ex: "He will continue to work on the robot until he succeeds." },
  { word: "suspect", pron: "[səspekt]", pos: "v.", def: "To suspect something is to believe that it is true.", ex: "I suspect that those kids stole the money." },
  { word: "valley", pron: "[væli]", pos: "n.", def: "A valley is a low area of land between two mountains or hills.", ex: "We looked at the valley below from the top of the mountain." }
];

let wordDivs = "";
words.forEach(w => {
  wordDivs += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});

const wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit8_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit8_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">${wordDivs}</div></div></div>`;

const readingHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Tricky Turtle</h1><p style="margin-bottom: 1rem;">Ricky the rabbit and Tera the turtle met by the <b>edge</b> of the river. “No one is <b>capable</b> of beating me in a race!” Ricky said. He was <b>confident</b>—his smile <b>conveyed</b> that.</p><p style="margin-bottom: 1rem;">“I can beat you,” Tera said.</p><p style="margin-bottom: 1rem;">Ricky laughed with <b>delight</b>.</p><p style="margin-bottom: 1rem;">Tera said, “We will race tomorrow. The <b>destination</b> is the hill.”</p><p style="margin-bottom: 1rem;">Ricky agreed. Tera <b>concentrated</b> on winning the race. She was not faster than Ricky. She needed a <b>definite</b> way to <b>succeed</b>. She told her family about the race, “I have <b>concluded</b> that I have to <b>resort</b> to something bad. I will <b>cheat</b>.” She <b>dictated</b> her instructions to them.</p><p style="margin-bottom: 1rem;">At the race, they all wore white feathers. They looked exactly the same! Then, her family members hid in <b>shadows</b> on the <b>path</b>.</p><p style="margin-bottom: 1rem;">The race began. Tera was soon far behind. However, Tera’s brother hid behind a <b>bush</b> in the <b>valley</b> below. When Ricky got close, Tera’s brother began to run. He looked just like Tera! Ricky ran as fast as he could along the <b>path</b>. But, to him, it seemed like Tera was always ahead. Ricky had used a <b>considerable</b> amount of energy.</p><p style="margin-bottom: 1rem;">He reached the top, but Tera’s sister was already there. “Well, you win,” Ricky said.</p><p style="margin-bottom: 1rem;">Later, Tera had a <b>broad</b> smile on her face. Ricky never <b>suspected</b>. He had been tricked by a family of slow turtles.</p></div>`;

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 8",
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
          id: "sec1_wordlist_ex1",
          title: "Exercise 1: Fill in the blanks with the correct words from the word bank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. This river will take us through the_________________ .", options: ["valley", "bush", "edge", "resort"], correctAnswer: "valley", explanation: "valley: a low area of land between two mountains or hills." },
            { id: "2", content: "2. The doctor must_________________during surgery to keep the patient alive.", options: ["convey", "concentrate", "broad", "capable"], correctAnswer: "concentrate", explanation: "concentrate: to give your full attention." },
            { id: "3", content: "3. The sign was so_________________ we couldn’t see around it.", options: ["broad", "capable", "resort", "edge"], correctAnswer: "broad", explanation: "broad: wide." },
            { id: "4", content: "4. People can_________________ their happiness by smiling.", options: ["path", "convey", "concentrate", "bush"], correctAnswer: "convey", explanation: "convey: to communicate or make ideas known." },
            { id: "5", content: "5. What is the_________________ of this train?", options: ["destination", "valley", "edge", "resort"], correctAnswer: "destination", explanation: "destination: the place where someone or something is going to." },
            { id: "6", content: "6. We walked to the_________________ of the cliff and looked down.", options: ["path", "bush", "edge", "valley"], correctAnswer: "edge", explanation: "edge: the part of it that is farthest from the center." },
            { id: "7", content: "7. The hikers walked along the_________________ in the forest.", options: ["bush", "path", "destination", "broad"], correctAnswer: "path", explanation: "path: a way from one place to another that people can walk along." },
            { id: "8", content: "8. I planted a _________________ in my yard last weekend.", options: ["bush", "valley", "capable", "concentrate"], correctAnswer: "bush", explanation: "bush: a plant with many thin branches." },
            { id: "9", content: "9. She is_________________ of running faster than any boy in her class.", options: ["capable", "broad", "convey", "resort"], correctAnswer: "capable", explanation: "capable: able to do something." },
            { id: "10", content: "10. If the boys can’t agree, they will__________________ to fighting.", options: ["resort", "convey", "concentrate", "destination"], correctAnswer: "resort", explanation: "resort to: to depend on it in order to solve a problem." }
          ]
        },
        {
          id: "sec1_wordlist_ex2",
          title: "Exercise 2: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "11", content: "1. He wants to win so much that he will not obey the rules to do it.", options: ["cheat", "shadow", "suspect", "succeed"], correctAnswer: "cheat", explanation: "cheat: to be dishonest so that you can win or do well." },
            { id: "12", content: "2. I’m going to stand in the dark area of the tree because the sun is too hot here.", options: ["shadow", "dictate", "confident", "delight"], correctAnswer: "shadow", explanation: "shadow: the dark area that is made when something blocks light." },
            { id: "13", content: "3. The police believe it’s true that the clerk stole the money.", options: ["suspect", "conclude", "definite", "considerable"], correctAnswer: "suspect", explanation: "suspect: to believe that it is true." },
            { id: "14", content: "4. If we do what we are trying to do, we will become very rich!", options: ["succeed", "cheat", "dictate", "shadow"], correctAnswer: "succeed", explanation: "succeed: to complete something that you planned or tried to do." },
            { id: "15", content: "5. Please read aloud the questions so the students can write them down.", options: ["dictate", "convey", "suspect", "confident"], correctAnswer: "dictate", explanation: "dictate: to read it aloud so it can be written down." },
            { id: "16", content: "6. I am sure I can do something because I have practiced for years.", options: ["confident", "definite", "considerable", "delight"], correctAnswer: "confident", explanation: "confident: believes they can do something without failing." },
            { id: "17", content: "7. After seeing the evidence, you must decide if the man is innocent.", options: ["conclude", "suspect", "succeed", "cheat"], correctAnswer: "conclude", explanation: "conclude: to arrive at a logical end by looking at evidence." },
            { id: "18", content: "8. It was a good feeling knowing that I had saved enough money to go on a trip.", options: ["delight", "shadow", "dictate", "confident"], correctAnswer: "delight", explanation: "delight: a feeling of being very happy with something." },
            { id: "19", content: "9. This horse is a certain winner.", options: ["definite", "considerable", "delight", "suspect"], correctAnswer: "definite", explanation: "definite: certain or sure to be true." },
            { id: "20", content: "10. The large size of the box made it difficult to move.", options: ["considerable", "confident", "conclude", "cheat"], correctAnswer: "considerable", explanation: "considerable: large in size, amount or extent." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: readingHtml,
      imageUrl: "/unit8_story.png",
      sections: [
        {
          id: "sec2_reading",
          title: "Answer the questions.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "21",
              content: "1. What is this story about?",
              options: [
                "A confident rabbit",
                "A rabbit that cheats in a race",
                "A turtle that rests in shadows",
                "A turtle with a crazy idea and a broad family"
              ],
              correctAnswer: "A confident rabbit",
              explanation: "Theo đáp án khóa là (a) A confident rabbit."
            },
            {
              id: "22",
              content: "2. Where was the final destination of the race?",
              options: [
                "The edge of the river",
                "Behind the first bush",
                "The middle of the valley",
                "The top of the hill"
              ],
              correctAnswer: "The top of the hill",
              explanation: "The destination is the hill (đỉnh đồi)."
            },
            {
              id: "23",
              content: "3. Why was Tera the Turtle angry?",
              options: [
                "Because Ricky the rabbit said no one was capable of beating him",
                "Because she thought that the path of the race was too difficult",
                "Because she knew Rabbit would resort to cheating",
                "Because her family wouldn’t gather when she asked them to"
              ],
              correctAnswer: "Because Ricky the rabbit said no one was capable of beating him",
              explanation: "Ricky the rabbit said 'No one is capable of beating me in a race!'."
            },
            {
              id: "24",
              content: "4. What did Tera say to her family?",
              options: [
                "She concluded that she must concentrate on the race.",
                "She conveyed that Rabbit would cheat.",
                "She told them about her definite plan to succeed.",
                "She said the race would take a considerable amount of energy."
              ],
              correctAnswer: "She told them about her definite plan to succeed.",
              explanation: "She needed a definite way to succeed. She told her family about the race..."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit8.json', JSON.stringify(json));
console.log('unit8.json created successfully');
