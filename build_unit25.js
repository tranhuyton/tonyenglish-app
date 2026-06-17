const fs = require('fs');

const words = [
  { w: "circulate", p: "[sə́ːrkjəlèit]", pos: "v.", d: "To circulate something is to spread it quickly.", e: "The fan helped to circulate cool air through the room." },
  { w: "consequent", p: "[kɑ́nsikwènt]", pos: "adj.", d: "Consequent means happening because of a different situation.", e: "Her consequent rash came after she touched the poison ivy." },
  { w: "derive", p: "[diráiv]", pos: "v.", d: "To derive something from another source means to get it from that thing.", e: "Red's nickname was derived from the color of her hair." },
  { w: "drown", p: "[droun]", pos: "v.", d: "To drown is to die from not being able to breathe underwater.", e: "He would have drowned if the sailors would not have rescued him." },
  { w: "dynasty", p: "[dáinəsti]", pos: "n.", d: "A dynasty is a series of rulers who are all from the same family.", e: "The ancient Egyptians had a dynasty that lasted for many years." },
  { w: "fraction", p: "[frǽkʃən]", pos: "n.", d: "A fraction is a small part of something.", e: "Only a fraction of the cake was gone." },
  { w: "frost", p: "[frɔːst]", pos: "n.", d: "Frost is a white layer of ice that forms during very cold weather.", e: "In the morning, the trees were all covered with frost." },
  { w: "illusion", p: "[ilúːʒən]", pos: "n.", d: "An illusion is something that looks real, but doesn't actually exist.", e: "Some pictures create an illusion for the eyes." },
  { w: "invade", p: "[invéid]", pos: "v.", d: "To invade is to take over a place by force.", e: "The enemy forces tried to invade our country through the air." },
  { w: "lieutenant", p: "[luːténənt]", pos: "n.", d: "A lieutenant is a rank in the military or police, or a person with that rank.", e: "The lieutenant was a good leader, and his soldiers respected him." },
  { w: "marine", p: "[məríːn]", pos: "adj.", d: "The word marine describes something related to the sea.", e: "A healthy ocean is full of marine animals." },
  { w: "merit", p: "[mérit]", pos: "n.", d: "The merit of something or someone is their good qualities.", e: "The actor received an award for his merits in the movie." },
  { w: "navy", p: "[néivi]", pos: "n.", d: "A navy is the part of a country's military that fights at sea.", e: "My country is known for our strong navy." },
  { w: "polar", p: "[póulər]", pos: "adj.", d: "Polar relates to the cold places on Earth's north and south ends.", e: "Only a few people live in the Earth's northern polar region." },
  { w: "ray", p: "[rei]", pos: "n.", d: "A ray is a line of light that comes from a bright object.", e: "The sun's warm rays covered the beach." },
  { w: "resign", p: "[rizáin]", pos: "v.", d: "To resign means to quit a job.", e: "After I officially resigned from work, I said goodbye to my boss." },
  { w: "suicide", p: "[súːəsàid]", pos: "n.", d: "Suicide is the act of killing oneself.", e: "Some people feel so sad that they think suicide is the only answer." },
  { w: "tremble", p: "[trémbəl]", pos: "v.", d: "To tremble is to shake as a result of cold weather.", e: "Harry was not used to the cold, so he trembled most of the day." },
  { w: "underlying", p: "[ʌ̀ndərláiiŋ]", pos: "adj.", d: "When something is underlying, it is a hidden cause of something else.", e: "Her underlying fear of flying reduced her traveling options." },
  { w: "via", p: "[víːə]", pos: "prep.", d: "To travel via something means to travel through or using something.", e: "We arrived in the city from the airport via the train." }
];

let wordItems = words.map(w => `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.w}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.p}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.d}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.e}</div></div></div>`).join('');

const wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit25_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit25_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">${wordItems}</div></div></div>`;

const readingHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">How Did Greenland Get Its Name?</h1><p style="margin-bottom: 1rem;">The nation of Greenland isn't very green. The sun's <b>rays</b> don't shine there for three whole months. As a result, it's covered with snow, ice and <b>frost</b>. Then how was the name <b>derived</b>? It started with a Viking named Erik the Red. Erik had many <b>merits</b>. However, there was an <b>underlying</b> problem ... he got angry easily. People were scared of him. However, he was married to the niece of a very powerful man. So everybody tried to be nice to him.</p><p style="margin-bottom: 1rem;">One day, Erik fought with his neighbor and killed him. His <b>consequent</b> punishment was to leave Iceland.</p><p style="margin-bottom: 1rem;">Many stories <b>circulated</b> about a land west of Iceland. But only a <b>fraction</b> of the people in Iceland believed them. Still, Erik wanted to find it.</p><p style="margin-bottom: 1rem;">Erik sailed toward the land <b>via</b> the Atlantic Ocean. His <b>marine</b> knowledge was good, but the trip was hard. Some of his men <b>drowned</b>. Erik's <b>lieutenant</b> wanted to <b>resign</b> from his position. Others thought about committing <b>suicide</b>.</p><p style="margin-bottom: 1rem;">Suddenly, Erik thought he saw something.</p><p style="margin-bottom: 1rem;">"I don't believe it," said Erik. "It must be an <b>illusion</b>." But it was no trick—it was the new land!</p><p style="margin-bottom: 1rem;">Erik <b>trembled</b> in the cold <b>polar</b> air. He saw that there was ice everywhere. He realized that the ice could keep enemies out. Not even the best <b>navy</b> could <b>invade</b> the new land. He could start a new <b>dynasty</b> in his name. But how could he convince people to live here?</p><p style="margin-bottom: 1rem;">"I'll call it 'Greenland,'" he said. Erik's plan worked. Within two years, over a thousand people moved to Greenland. In the end, Greenland got its name all because of a trick.</p></div>`;

const data = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 25",
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
              content: "1. relates to the cold places on Earth",
              options: ["polar", "marine", "frost", "underlying"],
              correctAnswer: "polar",
              explanation: "polar nghĩa là thuộc về vùng cực (relates to the cold places on Earth)."
            },
            {
              id: "2",
              content: "2. a small part of something",
              options: ["fraction", "merit", "ray", "dynasty"],
              correctAnswer: "fraction",
              explanation: "fraction nghĩa là phần nhỏ, phân số (a small part of something)."
            },
            {
              id: "3",
              content: "3. something that appears real but is not",
              options: ["resign", "circulate", "derive", "illusion"],
              correctAnswer: "illusion",
              explanation: "illusion nghĩa là ảo giác (something that appears real but is not)."
            },
            {
              id: "4",
              content: "4. to get from another source",
              options: ["frost", "illusion", "derive", "invade"],
              correctAnswer: "derive",
              explanation: "derive nghĩa là bắt nguồn từ, lấy từ (to get from another source)."
            },
            {
              id: "5",
              content: "5. to die in the water from lack of air",
              options: ["via", "drown", "suicide", "underlying"],
              correctAnswer: "drown",
              explanation: "drown nghĩa là chết đuối (to die in the water from lack of air)."
            }
          ]
        },
        {
          id: "sec2",
          title: "Part B: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "6",
              content: "1. invade",
              options: ["to come from", "to kill oneself", "to take over another country", "to happen because of something else"],
              correctAnswer: "to take over another country",
              explanation: "invade nghĩa là xâm lược (to take over another country)."
            },
            {
              id: "7",
              content: "2. dynasty",
              options: ["thin layer of ice", "a group of rulers from the same family", "a person that knows about the sea", "very cold"],
              correctAnswer: "a group of rulers from the same family",
              explanation: "dynasty nghĩa là triều đại (a group of rulers from the same family)."
            },
            {
              id: "8",
              content: "3. merit",
              options: ["a low ranking officer", "a good quality", "a part of a whole", "a hidden problem"],
              correctAnswer: "a good quality",
              explanation: "merit nghĩa là phẩm chất tốt, công trạng (a good quality)."
            },
            {
              id: "9",
              content: "4. resign",
              options: ["to quit", "to die underwater", "to shake", "to move from place to place"],
              correctAnswer: "to quit",
              explanation: "resign nghĩa là từ chức (to quit)."
            },
            {
              id: "10",
              content: "5. ray",
              options: ["a way to get through", "something that seems to be something else", "a group of soldiers at sea", "a line of light"],
              correctAnswer: "a line of light",
              explanation: "ray nghĩa là tia sáng (a line of light)."
            }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: readingHtml,
      imageUrl: "/unit25_v3_story.png",
      sections: [
        {
          id: "sec3",
          title: "Part A: Mark each statement T for true or F for false.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "11",
              content: "1. The sun's rays don't ever shine on Greenland.",
              options: ["True", "False", "Not Given", "None of the above"],
              correctAnswer: "False",
              explanation: "Sai (F). Câu sửa lại: The sun's rays don't shine on Greenland for three months."
            },
            {
              id: "12",
              content: "2. Erik the Red wanted to start a dynasty in his name in Iceland.",
              options: ["True", "False", "Not Given", "None of the above"],
              correctAnswer: "False",
              explanation: "Sai (F). Câu sửa lại: He wanted to start a dynasty in his name in Greenland."
            },
            {
              id: "13",
              content: "3. Erik the Red's consequent punishment for killing his neighbor was to leave Iceland for Denmark.",
              options: ["True", "False", "Not Given", "None of the above"],
              correctAnswer: "False",
              explanation: "Sai (F). Câu sửa lại: Erik the Red's consequent punishment for killing his neighbor was to leave Iceland."
            },
            {
              id: "14",
              content: "4. Erik's lieutenant thought about resigning.",
              options: ["True", "False", "Not Given", "None of the above"],
              correctAnswer: "True",
              explanation: "Đúng (T)."
            },
            {
              id: "15",
              content: "5. The ice around Greenland protected it from being invaded by navies.",
              options: ["True", "False", "Not Given", "None of the above"],
              correctAnswer: "True",
              explanation: "Đúng (T)."
            },
            {
              id: "16",
              content: "6. Greenland's name was derived from Erik's favorite color.",
              options: ["True", "False", "Not Given", "None of the above"],
              correctAnswer: "False",
              explanation: "Sai (F). Câu sửa lại: Erik gave it the name Greenland because he wanted many people to settle there."
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
              content: "1. According to the story, what was Erik's underlying problem?",
              options: ["He traveled via ship.", "He had many merits.", "He got angry easily.", "He circulated stories that weren't true."],
              correctAnswer: "He got angry easily.",
              explanation: "Theo câu chuyện, vấn đề tiềm ẩn của Erik là ông ta rất dễ nổi giận."
            },
            {
              id: "18",
              content: "2. All of the following happened to people on Erik's ship EXCEPT:",
              options: ["they wanted to resign", "they found gold", "they drowned", "they thought about suicide"],
              correctAnswer: "they found gold",
              explanation: "Những người trên tàu đã chết đuối, muốn từ chức, hoặc nghĩ đến việc tự tử. Họ không tìm thấy vàng."
            },
            {
              id: "19",
              content: "3. What did Erik think he was looking at when he first saw Greenland?",
              options: ["A fraction", "An illusion", "Frost", "A marine bird"],
              correctAnswer: "An illusion",
              explanation: "Khi lần đầu nhìn thấy vùng đất, Erik nghĩ đó chắc hẳn là một ảo giác (an illusion)."
            },
            {
              id: "20",
              content: "4. Why did Erik want to bring more people to Greenland?",
              options: ["To help them grow food", "So he could set up a dynasty", "To explore more land", "To protect them from the Vikings"],
              correctAnswer: "So he could set up a dynasty",
              explanation: "Erik muốn thuyết phục mọi người đến sống ở đây để ông có thể lập ra một triều đại mang tên mình (set up a dynasty)."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit25_raw.json', JSON.stringify(data, null, 2));
console.log('Done writing unit25_raw.json');
