const fs = require('fs');

const words = [
  { word: "abstract", pronunciation: "[æbstrækt]", type: "adj.", def: "If ideas are abstract, they are based on general ways of thinking.", ex: "The idea of beauty is abstract and changes over time." },
  { word: "annual", pronunciation: "[ænjuəl]", type: "adj.", def: "If something is annual, it happens once a year.", ex: "The only time I see my aunts and uncles is at our annual family picnic." },
  { word: "clay", pronunciation: "[klei]", type: "n.", def: "Clay is a type of heavy, wet soil used to make pots.", ex: "She made a bowl out of the clay." },
  { word: "cloth", pronunciation: "[klɔ(:)θ]", type: "n.", def: "Cloth is material used to make clothes.", ex: "His shirt is made of a very soft type of cloth." },
  { word: "curtain", pronunciation: "[kə:rtən]", type: "n.", def: "A curtain is a cloth hung over a window or used to divide a room.", ex: "She opened the curtains to let light into the room." },
  { word: "deserve", pronunciation: "[dizə:rv]", type: "v.", def: "To deserve is to be worthy of something as a result of one’s actions.", ex: "The dog deserved a bone for behaving very well." },
  { word: "feather", pronunciation: "[feðər]", type: "n.", def: "Feathers are the things covering birds’ bodies.", ex: "That bird has orange feathers on its chest." },
  { word: "fertile", pronunciation: "[fə:rtl]", type: "adj.", def: "If land is fertile, it is able to produce good crops and plants.", ex: "The farmer grew many vegetables in the fertile soil." },
  { word: "flood", pronunciation: "[flʌd]", type: "n.", def: "A flood is an event in which water covers an area which is usually dry.", ex: "After three days of rain, there was a flood in the city." },
  { word: "furniture", pronunciation: "[fə:rnitʃər]", type: "n.", def: "Furniture is the things used in a house such as tables and chairs.", ex: "His living room only had a few simple pieces of furniture." },
  { word: "grave", pronunciation: "[greiv]", type: "n.", def: "A grave is the place where a dead person is buried.", ex: "We visit our grandfather’s grave each year." },
  { word: "ideal", pronunciation: "[aidi:əl]", type: "adj.", def: "If something is ideal, it is the best that it can possibly be.", ex: "This house is an ideal place for my family. It has everything we need." },
  { word: "intelligence", pronunciation: "[intelədʒəns]", type: "n.", def: "Intelligence is the ability to learn and understand things.", ex: "Because of his high intelligence, he finished school early." },
  { word: "nowadays", pronunciation: "[nauədeiz]", type: "adv.", def: "If something happens nowadays, it happens at the present time.", ex: "In the past people walked everywhere. Nowadays, they use cars." },
  { word: "obtain", pronunciation: "[əbtein]", type: "v.", def: "To obtain is to get something you want or need.", ex: "After I passed the test, I obtained my driver’s license." },
  { word: "religious", pronunciation: "[rilidʒəs]", type: "adj.", def: "When something is religious, it has to do with religion.", ex: "The holy man spoke about religious topics." },
  { word: "romantic", pronunciation: "[roumæntik]", type: "adj.", def: "When something is romantic, it has to do with love.", ex: "The young couple went to see a romantic movie." },
  { word: "shell", pronunciation: "[ʃel]", type: "n.", def: "A shell is a hard covering that protects the body of some sea creatures.", ex: "There were many pretty shells on the beach." },
  { word: "shore", pronunciation: "[ʃɔ:r]", type: "n.", def: "A shore is the edge of a large body of water.", ex: "All of the boats were floating near the shore." },
  { word: "wheel", pronunciation: "[hwi:l]", type: "n.", def: "A wheel is a round thing on a vehicle that turns when it moves.", ex: "A car has four wheels." }
];

let wordHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit29_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit29_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pronunciation}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordHtml += `</div></div></div>`;

// Story HTML
const storyRaw = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Osiris and the Nile</h1><p style="margin-bottom: 1rem;">Long ago, Osiris was the king of Egypt, and Isis was the queen. They ruled the <b>fertile</b> land by the Nile River. They had great <b>intelligence</b>, and they shared their <b>abstract</b> ideas with everyone. Osiris taught the Egyptians how to make <b>wheels</b> and <b>furniture</b>. Isis taught them how to make things from <b>clay</b> and <b>cloth</b>. The people thought they <b>deserved</b> a gift. So they built Osiris and Isis a pyramid. Everyone loved Osiris except his brother, Set. Set wanted to be king.</p><p style="margin-bottom: 1rem;">Osiris made his <b>annual</b> trip around Egypt and led <b>religious</b> events. The villages gave him beautiful <b>shells</b> and colorful <b>feathers</b> as gifts.</p><p style="margin-bottom: 1rem;">When Osiris returned, Set brought a beautiful wooden box from behind a <b>curtain</b>.</p><p style="margin-bottom: 1rem;">"If someone fits inside this box, I will give it to him or her," Set said.</p><p style="margin-bottom: 1rem;">Osiris got in it. It was an <b>ideal</b> fit!</p><p style="margin-bottom: 1rem;">Suddenly, Set closed the box and threw it into the river. "Now I will be king!" Set said.</p><p style="margin-bottom: 1rem;">The box washed up on a foreign <b>shore</b> after a <b>flood</b>. Isis brought his body home and <b>obtained</b> a <b>grave</b> for him in Egypt. The Egyptian gods thought Isis had done something very <b>romantic</b>.</p><p style="margin-bottom: 1rem;">Because of her love, the gods made him the god of the underworld. Osiris returned every spring to help the farmers. Even <b>nowadays</b>, people say Osiris keeps their crops alive.</p></div>`;

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 29",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordHtml,
      sections: [
        {
          id: "sec1_wordlist",
          title: "Exercise 1: Part A: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "1",
              content: "1. I need your help to move the tables and chairs.",
              options: ["furniture", "cloth", "curtains", "intelligence"],
              correctAnswer: "furniture",
              explanation: "furniture (n): tables and chairs."
            },
            {
              id: "2",
              content: "2. This problem will test your ability to understand.",
              options: ["intelligence", "romantic", "feathers", "abstract"],
              correctAnswer: "intelligence",
              explanation: "intelligence (n): ability to learn and understand things."
            },
            {
              id: "3",
              content: "3. I don’t like to be in dark rooms with covers over the windows.",
              options: ["curtains", "shells", "clay", "cloth"],
              correctAnswer: "curtains",
              explanation: "curtains (n): cloth hung over a window."
            },
            {
              id: "4",
              content: "4. Tom and Rob are the best roommates.",
              options: ["ideal", "religious", "annual", "fertile"],
              correctAnswer: "ideal",
              explanation: "ideal (adj): the best that it can possibly be."
            },
            {
              id: "5",
              content: "5. I need to get a ticket before I can board the train.",
              options: ["obtain", "deserve", "flood", "grave"],
              correctAnswer: "obtain",
              explanation: "obtain (v): get something you want or need."
            }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 1: Part B: Fill in the blanks with the correct words from the word bank.",
          content: "WORD BANK: clay, cloth, fertile, graves, flood. Jimmy went on a trip to Egypt. There, he visited the great pyramids. Inside them were the 1._________ of old kings. He also visited a village near the river and learned about a recent 2._________. People grew many crops on this 3._________ land. They used 4._________ pots to carry water from the river into their homes. One friendly man gave Jimmy a white 5._________ to cover his head from the hot sun. It was a wonderful trip.",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "6",
              content: "1. Inside them were the _______ of old kings.",
              options: ["graves", "clay", "cloth", "fertile"],
              correctAnswer: "graves",
              explanation: "graves: the place where a dead person is buried."
            },
            {
              id: "7",
              content: "2. He also visited a village near the river and learned about a recent _______.",
              options: ["flood", "graves", "clay", "cloth"],
              correctAnswer: "flood",
              explanation: "flood: an event in which water covers an area which is usually dry."
            },
            {
              id: "8",
              content: "3. People grew many crops on this _______ land.",
              options: ["fertile", "flood", "graves", "clay"],
              correctAnswer: "fertile",
              explanation: "fertile: able to produce good crops and plants."
            },
            {
              id: "9",
              content: "4. They used _______ pots to carry water from the river into their homes.",
              options: ["clay", "fertile", "flood", "graves"],
              correctAnswer: "clay",
              explanation: "clay: a type of heavy, wet soil used to make pots."
            },
            {
              id: "10",
              content: "5. One friendly man gave Jimmy a white _______ to cover his head from the hot sun.",
              options: ["cloth", "clay", "fertile", "flood"],
              correctAnswer: "cloth",
              explanation: "cloth: material used to make clothes."
            }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 2: Check (V) the sentence with the bolded word that makes better sense.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "11",
              content: "1. Which sentence makes better sense?",
              options: ["a. Many people wear a shell before going out into the rain.", "b. In the past three years, the city has had two floods."],
              correctAnswer: "b. In the past three years, the city has had two floods.",
              explanation: "A flood is an event in which water covers an area which is usually dry."
            },
            {
              id: "12",
              content: "2. Which sentence makes better sense?",
              options: ["a. Nowadays, many students like using the Internet to do research.", "b. Many groups have annual meetings every month."],
              correctAnswer: "a. Nowadays, many students like using the Internet to do research.",
              explanation: "Nowadays means at the present time."
            },
            {
              id: "13",
              content: "3. Which sentence makes better sense?",
              options: ["a. Some dogs have interesting feathers.", "b. You cannot ride a bicycle if it doesn’t have wheels."],
              correctAnswer: "b. You cannot ride a bicycle if it doesn’t have wheels.",
              explanation: "A wheel is a round thing on a vehicle that turns when it moves."
            },
            {
              id: "14",
              content: "4. Which sentence makes better sense?",
              options: ["a. Churches don’t let people read religious books.", "b. Birds use their feathers to help them fly."],
              correctAnswer: "b. Birds use their feathers to help them fly.",
              explanation: "Feathers are the things covering birds' bodies."
            },
            {
              id: "15",
              content: "5. Which sentence makes better sense?",
              options: ["a. Many people enjoy watching romantic movies.", "b. If you get good grades, you don’t deserve to graduate."],
              correctAnswer: "a. Many people enjoy watching romantic movies.",
              explanation: "Romantic means it has to do with love."
            },
            {
              id: "16",
              content: "6. Which sentence makes better sense?",
              options: ["a. A crab is an example of an animal that has a shell.", "b. People never go fishing near the shore."],
              correctAnswer: "a. A crab is an example of an animal that has a shell.",
              explanation: "A shell is a hard covering that protects the body of some sea creatures."
            },
            {
              id: "17",
              content: "7. Which sentence makes better sense?",
              options: ["a. People who do bad things deserve to be punished.", "b. Mountains and hills are examples of floods."],
              correctAnswer: "a. People who do bad things deserve to be punished.",
              explanation: "Deserve means to be worthy of something as a result of one's actions."
            },
            {
              id: "18",
              content: "8. Which sentence makes better sense?",
              options: ["a. Horses are more common than cars nowadays.", "b. People who are religious go to church."],
              correctAnswer: "b. People who are religious go to church.",
              explanation: "Religious means having to do with religion."
            },
            {
              id: "19",
              content: "9. Which sentence makes better sense?",
              options: ["a. If you are romantic, you probably don’t like movies about love.", "b. There are beaches along the shore of some oceans and lakes."],
              correctAnswer: "b. There are beaches along the shore of some oceans and lakes.",
              explanation: "A shore is the edge of a large body of water."
            },
            {
              id: "20",
              content: "10. Which sentence makes better sense?",
              options: ["a. You should see your doctor once a year for an annual checkup.", "b. The wind makes the wheels of a car turn."],
              correctAnswer: "a. You should see your doctor once a year for an annual checkup.",
              explanation: "Annual means it happens once a year."
            }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyRaw,
      imageUrl: "/unit29_story.png",
      sections: [
        {
          id: "sec4_reading",
          title: "Answer the questions.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "21",
              content: "1. What is this story about?",
              options: ["a. Why Osiris built a pyramid for Isis", "b. How Set created a grave for Osiris", "c. How Osiris died and returned to make Egypt fertile", "d. Why the gods thought Isis’ actions were romantic"],
              correctAnswer: "c. How Osiris died and returned to make Egypt fertile",
              explanation: "The story mainly describes how Osiris was killed by Set, buried by Isis, and returned as the god of the underworld to help make the land fertile."
            },
            {
              id: "22",
              content: "2. What happened each spring?",
              options: ["a. Osiris gave people feathers and shells.", "b. Set obtained furniture from people.", "c. Set hid a box behind a curtain.", "d. Osiris made an annual trip to villages."],
              correctAnswer: "d. Osiris made an annual trip to villages.",
              explanation: "The passage states: 'Osiris made his annual trip around Egypt and led religious events.'"
            },
            {
              id: "23",
              content: "3. In the last paragraph, we can infer that______________ .",
              options: ["a. the shore is the ideal home for Osiris", "b. Set had greater intelligence than the gods", "c. the gods felt that Isis did a good deed", "d. nowadays, the Egyptians don’t use Osiris’ abstract ideas"],
              correctAnswer: "c. the gods felt that Isis did a good deed",
              explanation: "The gods thought Isis had done something very romantic and made him god of the underworld because of her love."
            },
            {
              id: "24",
              content: "4. According to the passage, all the following are true EXCEPT",
              options: ["a. the Egyptians made wheels", "b. the Egyptians used clay pots", "c. the Egyptians made cloth", "d. the Egyptians built religious villages"],
              correctAnswer: "d. the Egyptians built religious villages",
              explanation: "The passage does not mention Egyptians building religious villages. They built a pyramid."
            },
            {
              id: "25",
              content: "5. What did the Egyptians do for their king and queen?",
              options: ["a. They made religious cloth.", "b. They obtained furniture.", "c. They built them a pyramid.", "d. They threw them in a flood."],
              correctAnswer: "c. They built them a pyramid.",
              explanation: "The passage says: 'So they built Osiris and Isis a pyramid.'"
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit29.json', JSON.stringify(json, null, 2));
console.log('Successfully created unit29.json');
