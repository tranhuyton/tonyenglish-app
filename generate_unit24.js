const fs = require('fs');

const words = [
  { word: "baggage", pron: "[bægidʒ]", type: "n.", def: "Baggage is the set of bags that people take with them when they travel.", ex: "I’m taking several pieces of baggage with me on vacation.", emoji: "🧳" },
  { word: "bulb", pron: "[bʌlb]", type: "n.", def: "A bulb is the glass part of an electric light.", ex: "I had to change the light bulb in my bedroom.", emoji: "💡" },
  { word: "bundle", pron: "[bʌndl]", type: "n.", def: "A bundle is a number of things that are tied together.", ex: "I was shocked when he showed me a bundle of money.", emoji: "📦" },
  { word: "cattle", pron: "[kætl]", type: "n.", def: "Cattle are cows and bulls, especially on a farm.", ex: "The rancher's cattle were eating the grass in the field.", emoji: "🐄" },
  { word: "flee", pron: "[fliː]", type: "v.", def: "To flee means to run away from trouble or danger.", ex: "The crowd of men tried to flee from the danger.", emoji: "🏃" },
  { word: "graze", pron: "[greiz]", type: "v.", def: "To graze means to eat grass.", ex: "The cows grazed in the field.", emoji: "🌿" },
  { word: "greed", pron: "[griːd]", type: "n.", def: "Greed is a desire to have more than the things that you need.", ex: "She ate all the cookies out of her greed.", emoji: "🤑" },
  { word: "herd", pron: "[həːrd]", type: "n.", def: "A herd is a large group of the same type of animals that live together.", ex: "The herd of cows moved slowly across the ranch.", emoji: "🐃" },
  { word: "initiate", pron: "[iniʃieit]", type: "v.", def: "To initiate something means to start it.", ex: "You have to turn the switch on to initiate the computer system.", emoji: "▶️" },
  { word: "lane", pron: "[lein]", type: "n.", def: "A lane is a small road.", ex: "The lane passes directly in front of our house.", emoji: "🛣️" },
  { word: "nerve", pron: "[nəːrv]", type: "n.", def: "Nerve is bravery or the belief that you can do something.", ex: "He has the nerve to think that he can actually wrestle with a lion.", emoji: "🦁" },
  { word: "optimist", pron: "[ɑptəmist]", type: "n.", def: "An optimist is somebody who sees the good parts of a situation.", ex: "Even though he has physical problems, my brother is an optimist.", emoji: "😃" },
  { word: "parade", pron: "[pəreid]", type: "n.", def: "A parade is a celebration when groups of people walk in the same direction.", ex: "There were many marching bands in the spring parade.", emoji: "🎉" },
  { word: "pave", pron: "[peiv]", type: "v.", def: "To pave the ground is to lay material on it to make it easier to walk or drive on.", ex: "The path was paved with yellow bricks.", emoji: "🧱" },
  { word: "phantom", pron: "[fæntəm]", type: "n.", def: "A phantom is a ghost or spirit.", ex: "A scary phantom appeared from out of the darkness.", emoji: "👻" },
  { word: "portable", pron: "[pɔːrtəbl]", type: "adj.", def: "Something that is portable is able to be moved or carried easily.", ex: "Since computers are portable, people can use them anywhere.", emoji: "💻" },
  { word: "poster", pron: "[poustər]", type: "n.", def: "A poster is a written announcement that is used to advertise something.", ex: "I saw a poster about a free concert in the park.", emoji: "🖼️" },
  { word: "scratch", pron: "[skrætʃ]", type: "v.", def: "To scratch is to make small cuts with a claw or fingernail.", ex: "I used a stick to scratch my back.", emoji: "🐈" },
  { word: "symphony", pron: "[simfəni]", type: "n.", def: "A symphony is a long piece of music performed by many musicians.", ex: "Alex, a violin player, has always dreamt of playing a symphony.", emoji: "🎼" },
  { word: "widow", pron: "[widou]", type: "n.", def: "A widow is a woman whose husband has died.", ex: "The widow had no children and was very lonely.", emoji: "👵" }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit24_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit24_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${w.emoji}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordListHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Bremen Town Musicians</h1><p style="margin-bottom: 1rem;">Larry the cow, Harry the rooster and Lester the duck lived on a <b>widow</b>'s farm. They dreamed of playing music in a <b>parade</b>.</p><p style="margin-bottom: 1rem;">One day, the <b>widow</b> went to the lawn where her <b>herd</b> of <b>cattle</b> was <b>grazing</b>. "I'll eat him tomorrow," she said, pointing to Larry.</p><p style="margin-bottom: 1rem;">Larry wanted to <b>flee</b>, but he didn't have the <b>nerve</b> to go by himself. Then his friends Lester and Harry showed him a <b>poster</b>.</p><p style="margin-bottom: 1rem;">"It's for a <b>parade</b> in Bremen. We'll go with you, and we can perform our <b>symphony</b> there," Lester said.</p><p style="margin-bottom: 1rem;">The animals put together a small <b>bundle</b> that held a drum, a flute and a <b>portable</b> microphone. Then they took their <b>baggage</b> and <b>initiated</b> their long journey.</p><p style="margin-bottom: 1rem;">They walked down a <b>paved</b> <b>lane</b> all day. That night, they looked in the window of a house. They saw a group of thieves. They were eating a large dinner and telling stories about their <b>greed</b> and the people they stole from.</p><p style="margin-bottom: 1rem;">Lester was an <b>optimist</b>. He said, "I think we can scare them away!"</p><p style="margin-bottom: 1rem;">Soon, the animals came up with a plan. Harry flew inside and knocked over the lamp. "What was that?" screamed a thief as the <b>bulb</b> broke. They could barely see now.</p><p style="margin-bottom: 1rem;">Then Larry stood on two feet, and Lester flew to the top of his head. They looked very big. All three of the animals made scary noises. The thieves tried to hit the animals. But Harry flew over them and <b>scratched</b> them.</p><p style="margin-bottom: 1rem;">"It's a <b>phantom</b>!" yelled one thief.</p><p style="margin-bottom: 1rem;">The thieves ran away. The animals ate and rested. The next morning, Larry said, "Why go to Bremen? We can stay here and make music!" And so they remained there.</p></div>`;

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 24",
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
          id: "sec1_wordlist_partA",
          title: "Exercise 1 Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "ex1a_1",
              content: "1. a group of animals, such as cows",
              options: ["graze", "a herd", "a bundle", "a poster"],
              correctAnswer: "a herd",
              explanation: "A herd is a large group of the same type of animals that live together."
            },
            {
              id: "ex1a_2",
              content: "2. to escape from trouble or danger",
              options: ["flee", "graze", "pave", "initiate"],
              correctAnswer: "flee",
              explanation: "To flee means to run away from trouble or danger."
            },
            {
              id: "ex1a_3",
              content: "3. somebody who thinks that good things will happen",
              options: ["a widow", "a phantom", "a parade", "an optimist"],
              correctAnswer: "an optimist",
              explanation: "An optimist is somebody who sees the good parts of a situation."
            },
            {
              id: "ex1a_4",
              content: "4. able to be moved or carried easily",
              options: ["greed", "parade", "portable", "nerve"],
              correctAnswer: "portable",
              explanation: "Something that is portable is able to be moved or carried easily."
            },
            {
              id: "ex1a_5",
              content: "5. a small road",
              options: ["a bulb", "a symphony", "a scratch", "a lane"],
              correctAnswer: "a lane",
              explanation: "A lane is a small road."
            }
          ]
        },
        {
          id: "sec1_wordlist_partB",
          title: "Exercise 1 Part B: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "ex1b_1",
              content: "1. baggage",
              options: ["a group of animals", "an object used during a trip", "a glass object", "a celebration"],
              correctAnswer: "an object used during a trip",
              explanation: "Baggage is the set of bags that people take with them when they travel."
            },
            {
              id: "ex1b_2",
              content: "2. nerve",
              options: ["happiness", "sadness", "anger", "bravery"],
              correctAnswer: "bravery",
              explanation: "Nerve is bravery or the belief that you can do something."
            },
            {
              id: "ex1b_3",
              content: "3. initiate",
              options: ["to run away", "to start", "to hit", "to cut"],
              correctAnswer: "to start",
              explanation: "To initiate something means to start it."
            },
            {
              id: "ex1b_4",
              content: "4. graze",
              options: ["to eat", "to want more than you need", "to carry", "to make nice sounds"],
              correctAnswer: "to eat",
              explanation: "To graze means to eat grass."
            },
            {
              id: "ex1b_5",
              content: "5. phantom",
              options: ["an animal", "a person who sees the good side of a situation", "a ghost", "a person whose husband has died"],
              correctAnswer: "a ghost",
              explanation: "A phantom is a ghost or spirit."
            }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 2: Choose the word that is a better fit for each blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "ex2_1", content: "1. The band was almost ready to perform the ___________ .", options: ["initiated", "symphony"], correctAnswer: "symphony", explanation: "A symphony is a long piece of music performed by many musicians." },
            { id: "ex2_2", content: "2. After a few moments, they ___________ the thirty-minute piece.", options: ["initiated", "symphony"], correctAnswer: "initiated", explanation: "To initiate something means to start it." },
            { id: "ex2_3", content: "3. The large field was full of grass where the animals could ___________ .", options: ["graze", "cattle"], correctAnswer: "graze", explanation: "To graze means to eat grass." },
            { id: "ex2_4", content: "4. He knew his ___________ would be glad to live there.", options: ["graze", "cattle"], correctAnswer: "cattle", explanation: "Cattle are cows and bulls, especially on a farm." },
            { id: "ex2_5", content: "5. Andy didn't have the ___________ to tell his teacher that he had made a mistake.", options: ["optimist", "nerve"], correctAnswer: "nerve", explanation: "Nerve is bravery or the belief that you can do something." },
            { id: "ex2_6", content: "6. However, Kristin, an ___________, thought the teacher wouldn't get angry.", options: ["optimist", "nerve"], correctAnswer: "optimist", explanation: "An optimist is somebody who sees the good parts of a situation." },
            { id: "ex2_7", content: "7. The man wondered if the ___________ near his house would ever be paved.", options: ["lane", "paved"], correctAnswer: "lane", explanation: "A lane is a small road." },
            { id: "ex2_8", content: "8. The man wondered if the lane near his house would ever be ___________ .", options: ["lane", "paved"], correctAnswer: "paved", explanation: "To pave the ground is to lay material on it to make it easier to walk or drive on." },
            { id: "ex2_9", content: "9. A ___________ of goats followed the rancher into the barn.", options: ["bundle", "herd"], correctAnswer: "herd", explanation: "A herd is a large group of the same type of animals that live together." },
            { id: "ex2_10", content: "10. He opened a ___________ of food and fed them.", options: ["bundle", "herd"], correctAnswer: "bundle", explanation: "A bundle is a number of things that are tied together." },
            { id: "ex2_11", content: "11. The ___________ told the hungry children to leave her house.", options: ["greed", "widow"], correctAnswer: "widow", explanation: "A widow is a woman whose husband has died." },
            { id: "ex2_12", content: "12. She had more than enough food, but her ___________ kept her from sharing.", options: ["greed", "widow"], correctAnswer: "greed", explanation: "Greed is a desire to have more than the things that you need." },
            { id: "ex2_13", content: "13. My whole class was invited to walk in the ___________ .", options: ["parade", "posters"], correctAnswer: "parade", explanation: "A parade is a celebration when groups of people walk in the same direction." },
            { id: "ex2_14", content: "14. We carried large ___________ that had our school's name on them.", options: ["parade", "posters"], correctAnswer: "posters", explanation: "A poster is a written announcement that is used to advertise something." },
            { id: "ex2_15", content: "15. The woman bought a ___________ lamp that she could take with her on trips.", options: ["bulb", "portable"], correctAnswer: "portable", explanation: "Something that is portable is able to be moved or carried easily." },
            { id: "ex2_16", content: "16. After a year, however, she had to buy a new ___________ for the lamp.", options: ["bulb", "portable"], correctAnswer: "bulb", explanation: "A bulb is the glass part of an electric light." },
            { id: "ex2_17", content: "17. There was a loud noise, then a large ___________ came into the room.", options: ["fled", "phantom"], correctAnswer: "phantom", explanation: "A phantom is a ghost or spirit." },
            { id: "ex2_18", content: "18. The children screamed and ___________ immediately.", options: ["fled", "phantom"], correctAnswer: "fled", explanation: "To flee means to run away from trouble or danger." },
            { id: "ex2_19", content: "19. He bought new ___________ before the trip...", options: ["baggage", "scratched"], correctAnswer: "baggage", explanation: "Baggage is the set of bags that people take with them when they travel." },
            { id: "ex2_20", content: "20. ...but after the first time he used them, they were ___________ and looked old.", options: ["baggage", "scratched"], correctAnswer: "scratched", explanation: "To scratch is to make small cuts with a claw or fingernail." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit24_v3_story.png",
      sections: [
        {
          id: "sec3_reading_partA",
          title: "Part A: Mark each statement T for true or F for false.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "rd_a_1", content: "1. Larry, Harry and Lester were cattle on the widow Riley’s farm.", options: ["True", "False"], correctAnswer: "False", explanation: "Larry was a cow, Harry was a rooster and Lester was a duck on the widow's farm." },
            { id: "rd_a_2", content: "2. The animals fled because the widow wanted to kill the herd.", options: ["True", "False"], correctAnswer: "False", explanation: "The widow only pointed to Larry and said she would eat him tomorrow, not the whole herd." },
            { id: "rd_a_3", content: "3. Larry, Harry and Lester wanted to go to Bremen to perform in a parade.", options: ["True", "False"], correctAnswer: "True", explanation: "They dreamed of playing music in a parade in Bremen." },
            { id: "rd_a_4", content: "4. The animals initiated the journey with only a portable microphone and a drum in a bundle.", options: ["True", "False"], correctAnswer: "False", explanation: "The bundle held a drum, a flute and a portable microphone." },
            { id: "rd_a_5", content: "5. Larry was an optimist.", options: ["True", "False"], correctAnswer: "False", explanation: "Lester was the optimist." },
            { id: "rd_a_6", content: "6. Harry scratched the bulb to break it.", options: ["True", "False"], correctAnswer: "False", explanation: "Harry knocked over the lamp to break the bulb." }
          ]
        },
        {
          id: "sec3_reading_partB",
          title: "Part B: Answer the questions.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "rd_b_1", content: "1. Where did the cattle graze at the beginning of the story?", options: ["In an old house", "On a lawn", "On the paved lane", "At a parade"], correctAnswer: "On a lawn", explanation: "One day, the widow went to the lawn where her herd of cattle was grazing." },
            { id: "rd_b_2", content: "2. How did Larry, Harry and Lester find out about the parade?", options: ["From an invitation letter", "From the widow Riley", "From a poster", "From the other animals"], correctAnswer: "From a poster", explanation: "Lester and Harry showed him a poster about a parade in Bremen." },
            { id: "rd_b_3", content: "3. What were the greedy thieves doing when the animals arrived at the house?", options: ["Stealing things from the house", "Eating a large dinner", "Planning to steal from the widow", "Packing their baggage"], correctAnswer: "Eating a large dinner", explanation: "They saw a group of thieves eating a large dinner." },
            { id: "rd_b_4", content: "4. What did the animals pretend to be in order to scare the thieves away?", options: ["Phantoms", "The police", "The owners of the house", "Thieves"], correctAnswer: "Phantoms", explanation: "They looked very big and made scary noises, causing the thieves to think they were a phantom." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit24_raw.json', JSON.stringify(json, null, 2));
