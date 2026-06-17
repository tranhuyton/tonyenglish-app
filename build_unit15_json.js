const fs = require('fs');

const words = [
  { word: "absorb", pron: "[absorb]", pos: "v", def: "To absorb a liquid means to take it inside.", ex: "He used a sponge to absorb the water on the floor." },
  { word: "boss", pron: "[bɔ:s]", pos: "n", def: "A boss is a person in charge of other people at work.", ex: "My boss is a nice person." },
  { word: "committee", pron: "[kəˈmiti]", pos: "n", def: "A committee is a group of people who meet together to make decisions.", ex: "The school's committee agreed on a new dress code for students." },
  { word: "contract", pron: "[ˈkɑntrækt]", pos: "n", def: "A contract is a written agreement between two people.", ex: "The woman signed a contract when she bought the house." },
  { word: "crew", pron: "[kru:]", pos: "n", def: "A crew is a group of workers.", ex: "My father has a crew. They help him build houses." },
  { word: "devote", pron: "[diˈvout]", pos: "v", def: "To devote time to something means to spend a lot of time doing it.", ex: "She devotes two hours a day to playing the piano." },
  { word: "dig", pron: "[dig]", pos: "v", def: "To dig is to make a hole in the ground.", ex: "My dog digs in the yard so he can hide his bones." },
  { word: "dine", pron: "[dain]", pos: "v", def: "To dine means to eat dinner.", ex: "The young couple dined at their home." },
  { word: "donate", pron: "[ˈdouneit]", pos: "v", def: "To donate is to give something to a charity or organization.", ex: "We donate money to Christmas charities every year." },
  { word: "double", pron: "[ˈdʌbəl]", pos: "adj", def: "If something is double, it is twice as much, or twice as many.", ex: "I paid almost double the amount for that shirt." },
  { word: "elevate", pron: "[ˈeləveit]", pos: "v", def: "To elevate something is to put it at a higher level.", ex: "The man elevated the picture so he could see it better." },
  { word: "flavor", pron: "[ˈfleivər]", pos: "n", def: "A flavor is the taste of food or drinks.", ex: "The flavor of the ice cream was very good." },
  { word: "foundation", pron: "[faunˈdeiʃən]", pos: "n", def: "A foundation is a group that provides money for research.", ex: "The foundation raised money to give scholarships to students." },
  { word: "generation", pron: "[ˌdʒenəˈreiʃən]", pos: "n", def: "A generation is a group of people who live at the same time.", ex: "My grandparents are from a different generation than me." },
  { word: "handle", pron: "[ˈhændl]", pos: "n", def: "A handle is the part of an object people hold while using it.", ex: "The pot is very hot. So pick it up by the handle." },
  { word: "layer", pron: "[ˈleiər]", pos: "n", def: "A layer covers over something or is between two things.", ex: "There was a layer of snow on the tops of the houses this morning." },
  { word: "mud", pron: "[mʌd]", pos: "n", def: "Mud is soft, wet dirt.", ex: "My brother played rugby in the mud. Now he's dirty." },
  { word: "smooth", pron: "[smu:ð]", pos: "adj", def: "If something is smooth, it has no bumps.", ex: "The baby's skin felt very smooth." },
  { word: "soil", pron: "[sɔil]", pos: "n", def: "Soil is the top layer of land on the Earth.", ex: "The boy planted flowers in the soil and watered them every day." },
  { word: "unique", pron: "[ju:ˈni:k]", pos: "adj", def: "If people or things are unique, they are not like the others.", ex: "Her dog is unique. I've never seen one quite like it." }
];

let wordsHtml = '';
for (const w of words) {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}.</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
}

const part1Content = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit15_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit15_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">${wordsHtml}</div></div></div>`;

const part2Content = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Lucky Knife</h1><p style="margin-bottom: 1rem;">I've <b>devoted</b> my life to studying past <b>generations</b>. Last year, I had a <b>unique</b> chance to work with my uncle. Our job was to find old treasures for a school's history <b>foundation</b>. He also hired a <b>crew</b> of students. They signed a <b>contract</b> to work with him. He was the <b>boss</b>. The place was strange, though. I <b>dined</b> on many things that I had never tasted before. They had an unusual <b>flavor</b>.</p><p style="margin-bottom: 1rem;">We had been there about a month and hadn't found anything. One day, I began to <b>dig</b> in the <b>soil</b>. The ground's <b>layers</b> got wetter. Soon I was digging in the <b>mud</b>. My shovel began to get very heavy. It felt like it had <b>doubled</b> in weight because the ground had <b>absorbed</b> a lot of water.</p><p style="margin-bottom: 1rem;">Finally, I saw something in the <b>mud</b>. It was an old knife! The <b>handle</b> felt <b>smooth</b> in my hand. I <b>elevated</b> it so I could see it better. There was writing on it.</p><p style="margin-bottom: 1rem;">"It says it will bring good luck," my uncle said with a smile. "Why don't you keep it?"</p><p style="margin-bottom: 1rem;">I put it in my tent. The next day, we found many more things. There were pots, jewelry and weapons. My uncle <b>donated</b> all of the things to a special <b>committee</b>. Many newspapers wrote stories about it. It seemed the knife really did bring good luck!</p></div>`;

const data = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 15",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: part1Content,
      sections: [
        {
          id: "sec1",
          title: "Exercise 1: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u15_1_1", content: "1. someone who controls workers", options: ["absorb", "boss", "generation", "crew"], correctAnswer: "boss", explanation: "boss: a person in charge of other people at work." },
            { id: "u15_1_2", content: "2. not like anything else", options: ["flavor", "foundation", "mud", "unique"], correctAnswer: "unique", explanation: "unique: not like the others." },
            { id: "u15_1_3", content: "3. to make two of something", options: ["layer", "dig", "double", "devote"], correctAnswer: "double", explanation: "double: twice as much, or twice as many." },
            { id: "u15_1_4", content: "4. to eat something", options: ["dine", "precise", "handle", "contract"], correctAnswer: "dine", explanation: "dine: to eat dinner." },
            { id: "u15_1_5", content: "5. to put something higher", options: ["donate", "elevate", "committee", "soil"], correctAnswer: "elevate", explanation: "elevate: to put it at a higher level." }
          ]
        },
        {
          id: "sec2",
          title: "Exercise 2: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u15_2_1", content: "1. foundation", options: ["special", "a group that provides money for research", "the part held in the hand", "wet dirt"], correctAnswer: "a group that provides money for research", explanation: "foundation: a group that provides money for research." },
            { id: "u15_2_2", content: "2. generation", options: ["the same age group", "without bumps", "to eat", "something used to cut"], correctAnswer: "the same age group", explanation: "generation: a group of people who live at the same time." },
            { id: "u15_2_3", content: "3. committee", options: ["a group of workmen", "taste of food or drink", "to put higher", "a group that makes decisions"], correctAnswer: "a group that makes decisions", explanation: "committee: a group of people who meet together to make decisions." },
            { id: "u15_2_4", content: "4. donate", options: ["to move dirt", "an agreement", "to give something", "a single thickness"], correctAnswer: "to give something", explanation: "donate: to give something to a charity or organization." },
            { id: "u15_2_5", content: "5. boss", options: ["to give something", "someone who controls workers", "to give everything", "dirt"], correctAnswer: "someone who controls workers", explanation: "boss: a person in charge of other people at work." }
          ]
        },
        {
          id: "sec3",
          title: "Exercise 3: Check the one that suits the blank naturally.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u15_3_1", content: "1. The sponge.", options: ["absorbed all the water", "contracted to save money"], correctAnswer: "absorbed all the water", explanation: "A sponge absorbs water." },
            { id: "u15_3_2", content: "2. They will help.", options: ["They are the crew working on this job", "They aren't in the same generation"], correctAnswer: "They are the crew working on this job", explanation: "A crew is a group of workers who help." },
            { id: "u15_3_3", content: "3. The food tastes better now.", options: ["that you added more salt to give it some flavor", "that you added some soil to make it grow"], correctAnswer: "that you added more salt to give it some flavor", explanation: "Salt gives flavor to food." },
            { id: "u15_3_4", content: "4. She was very special.", options: ["She seldom spent time with the foundation", "She had a unique skill that few people have"], correctAnswer: "She had a unique skill that few people have", explanation: "Unique means special, not like the others." },
            { id: "u15_3_5", content: "5. Dr. Dion started a", options: ["boss at work", "foundation to help sick children"], correctAnswer: "foundation to help sick children", explanation: "A foundation is an organization." },
            { id: "u15_3_6", content: "6. We were able to", options: ["devote no attention", "dig very deep into the soft soil"], correctAnswer: "dig very deep into the soft soil", explanation: "You can dig into soft soil." },
            { id: "u15_3_7", content: "7. Where will you", options: ["dine at for dinner", "donate your table from"], correctAnswer: "dine at for dinner", explanation: "Dine means to eat dinner." },
            { id: "u15_3_8", content: "8. The rock was", options: ["missing its handle", "smooth and flat"], correctAnswer: "smooth and flat", explanation: "A rock can be smooth." },
            { id: "u15_3_9", content: "9. You will get dirty.", options: ["if you elevate your feet", "if you play in the mud"], correctAnswer: "if you play in the mud", explanation: "Mud is wet dirt that makes you dirty." },
            { id: "u15_3_10", content: "10. If you are cooking for more than two people,", options: ["layer it with some milk", "double the amount of water in the recipe"], correctAnswer: "double the amount of water in the recipe", explanation: "You should double the ingredients for more people." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: part2Content,
      imageUrl: "/unit15_story.png",
      sections: [
        {
          id: "sec4",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u15_4_1", content: "1. What is this story about?", options: ["How someone found an old knife", "A generation of college students", "A crew of committee workers digging in the mud", "How a smooth knife handle feels"], correctAnswer: "How someone found an old knife", explanation: "The story is about finding an old lucky knife." },
            { id: "u15_4_2", content: "2. All of the following are true EXCEPT.", options: ["the college students signed a contract", "the author's uncle worked for a foundation", "the items found at the site were donated", "the teen worked double the amount of everyone else"], correctAnswer: "the teen worked double the amount of everyone else", explanation: "The text says 'It felt like it had doubled in weight' referring to the shovel, not that he worked double the amount." },
            { id: "u15_4_3", content: "3. What is probably true of the teen in the story?", options: ["He could not read the writing on the knife.", "He held a higher position than the other students.", "He had to elevate the knife to see what it was.", "He didn't want to devote his time to history"], correctAnswer: "He could not read the writing on the knife.", explanation: "The uncle had to read the writing and tell him what it meant." },
            { id: "u15_4_4", content: "4. Where did the teen find the knife?", options: ["On top of the soil", "Under layers of dirt", "In the museum", "In his boss's tent"], correctAnswer: "Under layers of dirt", explanation: "He had to dig in the soil and layers got wetter, indicating it was under layers of dirt." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit15.json', JSON.stringify(data, null, 2));
console.log('Successfully created unit15.json');
