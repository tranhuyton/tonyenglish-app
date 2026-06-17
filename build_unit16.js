const fs = require('fs');

const words = [
  { word: "chamber", pron: "[tʃeimbər]", pos: "n", def: "A chamber is an old word for a bedroom.", ex: "The girl was tired. She went to her chamber for a nap." },
  { word: "deny", pron: "[dinai]", pos: "v", def: "To deny something is to say it is not true.", ex: "The boy denied that he broke the window." },
  { word: "document", pron: "[dɑkjəmənt]", pos: "n", def: "A document is an official piece of writing.", ex: "He was given an official document proving he was a citizen." },
  { word: "emphasize", pron: "[emfəsaiz]", pos: "v", def: "To emphasize is to give importance or attention to something.", ex: "She emphasized the key points by circling them in red ink." },
  { word: "fever", pron: "[fi:vər]", pos: "n", def: "A fever is a high body temperature that people get when they are sick.", ex: "Lydia had a high fever so she didn't go to school." },
  { word: "flu", pron: "[flu:]", pos: "n", def: "The flu is a type of sickness that makes you feel weak or your body hurt.", ex: "Since he had the flu, he felt miserable." },
  { word: "freeze", pron: "[fri:z]", pos: "v", def: "To freeze is to become very cold.", ex: "If you don't wear your coat in winter, you will freeze." },
  { word: "gesture", pron: "[dʒestʃər]", pos: "n", def: "A gesture is a movement of the hands or body.", ex: "My teacher makes a lot of gestures when she speaks." },
  { word: "interrupt", pron: "[intərʌpt]", pos: "v", def: "To interrupt is to briefly stop someone when they are doing something.", ex: "My mother interrupted me when I was trying to listen to music." },
  { word: "last", pron: "[læst]", pos: "v", def: "To last is to continue or go on for an amount of time.", ex: "The football match lasted for nearly two hours." },
  { word: "likeness", pron: "[laiknis]", pos: "n", def: "Likeness means the state of being like, or resemblance.", ex: "Michelle bears a strong likeness to her older sister Kate." },
  { word: "moreover", pron: "[mɔ:rouvər]", pos: "adv", def: "Moreover means besides or in addition to something.", ex: "It's cold outside. Moreover, the wind is very strong." },
  { word: "perspective", pron: "[pərspektiv]", pos: "n", def: "A perspective is the way you think about something.", ex: "The man's speech gave me a new perspective on our country." },
  { word: "rational", pron: "[ræʃənl]", pos: "adj", def: "When something is rational, it is normal or practical.", ex: "It is hard to think in a rational way when you are scared." },
  { word: "recover", pron: "[rikʌvər]", pos: "v", def: "To recover is to go back to normal after something bad happens.", ex: "I hope the city will recover soon after the flood." },
  { word: "rely", pron: "[rilai]", pos: "v", def: "To rely on something or someone is to trust or depend on them.", ex: "The boy relied on his older brother to help him." },
  { word: "shock", pron: "[ʃɑk]", pos: "v", def: "To shock people is to surprise them.", ex: "The man was shocked by the news." },
  { word: "shy", pron: "[ʃai]", pos: "adj", def: "When people are shy, they are nervous around people strange to them.", ex: "The girl was too shy to try out for the play." },
  { word: "stare", pron: "[stɛər]", pos: "v", def: "To stare at something is to look at it for a long time.", ex: "The young couple stared into each other's eyes." },
  { word: "thus", pron: "[ðʌs]", pos: "adv", def: "Thus means as a result or for that reason.", ex: "The sun was shining. Thus, I wore my sunglasses." }
];

let wordsHtml = '';
for (const w of words) {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}.</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
}

const part1Content = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit16_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit16_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">${wordsHtml}</div></div></div>`;

const part2Content = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Prince Sam</h1><p style="margin-bottom: 1rem;">Sam's mother cooked at the royal palace. One day, he went to work with her. She <b>emphasized</b> that he should stay in the kitchen. But Sam was bored. <b>Thus</b>, he decided to look around.</p><p style="margin-bottom: 1rem;">He went around a corner. It <b>shocked</b> him to see a boy who had a strong <b>likeness</b> to him. Sam soon <b>recovered</b>. The other boy <b>stared</b> at him. Then he spoke. "Come with me."</p><p style="margin-bottom: 1rem;">He needed to be <b>rational</b>. But he couldn't <b>deny</b> that he wanted to go. So he followed the boy to a <b>chamber</b>. "I am Prince Bertram," the boy said.</p><p style="margin-bottom: 1rem;">Sam felt <b>shy</b> talking to a prince. "I'm Sam."</p><p style="margin-bottom: 1rem;">"Trade places with me." The prince said.</p><p style="margin-bottom: 1rem;">"We can't. My mother will kill me. <b>Moreover</b>, I don't know anything about being a prince."</p><p style="margin-bottom: 1rem;">"No one will find out," the prince <b>interrupted</b>. "We look the same, and even our <b>gestures</b> are the same. It will only <b>last</b> for a week."</p><p style="margin-bottom: 1rem;">Sam said OK. Soon, Sam's <b>perspective</b> on being a prince changed. He spent most of his day signing royal <b>documents</b>. At night, the prince's <b>chamber</b> was cold. He thought he was going to <b>freeze</b> or get sick with a <b>fever</b> or the <b>flu</b>. He was happy when the week ended. So was the prince.</p><p style="margin-bottom: 1rem;">"I didn't know how to do anything," the prince said. "I've always <b>relied</b> on my servants to do everything for me."</p><p style="margin-bottom: 1rem;">"I think I like being a regular person," Sam said. "Being a prince isn't fun." So, they both returned to their normal positions and enjoyed their lives more than before.</p></div>`;

const data = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 16",
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
          title: "Exercise 1: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u16_1_1", content: "1. Jennifer looked for a long time at the girl who looked just like her sister.", options: ["stared", "recovered", "lasted", "shy"], correctAnswer: "stared" },
            { id: "u16_1_2", content: "2. Even though the noise scared me, I returned to my calm mood.", options: ["stared", "recovered", "lasted", "shy"], correctAnswer: "recovered" },
            { id: "u16_1_3", content: "3. The man's speech went on for another thirty minutes.", options: ["stared", "recovered", "lasted", "shy"], correctAnswer: "lasted" },
            { id: "u16_1_4", content: "4. I am quiet in a big crowd of people.", options: ["fever", "recovered", "lasted", "shy"], correctAnswer: "shy" },
            { id: "u16_1_5", content: "5. My little brother woke up with a really bad hot temperature today.", options: ["stared", "fever", "lasted", "shy"], correctAnswer: "fever" }
          ]
        },
        {
          id: "sec2",
          title: "Exercise 1: Check the one that suits the blank naturally.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u16_2_1", content: "1. My friend said I took her book, ________________ .", options: ["but I didn't, so I denied it", "so I relied on what she told me"], correctAnswer: "but I didn't, so I denied it" },
            { id: "u16_2_2", content: "2. When I opened the door, ________________ .", options: ["I was shocked by what I saw", "it made a funny gesture"], correctAnswer: "I was shocked by what I saw" },
            { id: "u16_2_3", content: "3. My teacher ________________ .", options: ["wanted to take a likeness of the class this year", "emphasized that students must follow the classroom rules"], correctAnswer: "emphasized that students must follow the classroom rules" },
            { id: "u16_2_4", content: "4. The book was easy for me to read , ________________ .", options: ["thus I finished it in two days", "so I recovered a harder book"], correctAnswer: "thus I finished it in two days" },
            { id: "u16_2_5", content: "5. The things my sister said ________________ .", options: ["seemed really shy", "gave me a new perspective"], correctAnswer: "gave me a new perspective" }
          ]
        },
        {
          id: "sec3",
          title: "Exercise 2: Choose the word that is a better fit for each sentence.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u16_3_1", content: "1. He woke up feeling sick and with a high _______________ .", options: ["chamber", "fever"], correctAnswer: "fever" },
            { id: "u16_3_2", content: "2. The door to her private _______________ was unlocked.", options: ["chamber", "fever"], correctAnswer: "chamber" },
            { id: "u16_3_3", content: "3. Many people have a different _______________ than me.", options: ["perspective", "likeness"], correctAnswer: "perspective" },
            { id: "u16_3_4", content: "4. The painting didn't have much of a _______________ to my dad.", options: ["perspective", "likeness"], correctAnswer: "likeness" },
            { id: "u16_3_5", content: "5. The _______________ had to be signed by ten people.", options: ["rational", "document"], correctAnswer: "document" },
            { id: "u16_3_6", content: "6. My brother was too excited to have a _______________ plan.", options: ["rational", "document"], correctAnswer: "rational" },
            { id: "u16_3_7", content: "7. The loud noise _______________ me.", options: ["stared", "shocked"], correctAnswer: "shocked" },
            { id: "u16_3_8", content: "8. The monkey _______________ at me through the bars.", options: ["stared", "shocked"], correctAnswer: "stared" },
            { id: "u16_3_9", content: "9. I'm not old enough to drive; _______________ , it seems kind of scary.", options: ["moreover", "flu"], correctAnswer: "moreover" },
            { id: "u16_3_10", content: "10. I'm scared that I might get the _______________ this winter.", options: ["moreover", "flu"], correctAnswer: "flu" },
            { id: "u16_3_11", content: "11. The boy made a _______________ to his friends to follow him.", options: ["interrupted", "gesture"], correctAnswer: "gesture" },
            { id: "u16_3_12", content: "12. My sister ran in and _______________ what I was saying.", options: ["interrupted", "gesture"], correctAnswer: "interrupted" },
            { id: "u16_3_13", content: "13. I trusted the man, so I _______________ on his advice.", options: ["thus", "relied"], correctAnswer: "relied" },
            { id: "u16_3_14", content: "14. I could not depend on the man; _______________, I had to do it all myself.", options: ["thus", "relied"], correctAnswer: "thus" },
            { id: "u16_3_15", content: "15. The basketball game _______________ longer than three hours.", options: ["recovered", "lasted"], correctAnswer: "lasted" },
            { id: "u16_3_16", content: "16. I was sick, but I _______________ in time to go on the field trip.", options: ["recovered", "lasted"], correctAnswer: "recovered" },
            { id: "u16_3_17", content: "17. The girl at the store was _______________, so she didn't talk.", options: ["deny", "shy"], correctAnswer: "shy" },
            { id: "u16_3_18", content: "18. The man did not _______________ that he liked ice cream.", options: ["deny", "shy"], correctAnswer: "deny" },
            { id: "u16_3_19", content: "19. She _______________ the need for good manners.", options: ["emphasized", "freeze"], correctAnswer: "emphasized" },
            { id: "u16_3_20", content: "20. Did the flowers _______________ last night due to the snow?", options: ["emphasized", "freeze"], correctAnswer: "freeze" }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: part2Content,
      imageUrl: "/unit16_story.png",
      sections: [
        {
          id: "sec4",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "u16_4_1", content: "1. What is the main idea of this story?", options: ["A boy who denies that he's a prince", "A student who's too shy to talk to a prince", "How two boys who bore a likeness to each other traded places", "A prince who has a rational perspective"], correctAnswer: "How two boys who bore a likeness to each other traded places" },
            { id: "u16_4_2", content: "2. What happened after Sam ran into the prince?", options: ["Sam was too shocked to recover.", "The prince stared at Sam.", "Sam couldn't talk; thus, he ran away.", "Sam made a gesture."], correctAnswer: "The prince stared at Sam." },
            { id: "u16_4_3", content: "3. What did Sam think about being a prince?", options: ["He thought it was fun while it lasted.", "He didn't like it; moreover, he missed his mother.", "He liked to rely on the servants at the palace.", "He was afraid he would freeze or get a fever or the flu."], correctAnswer: "He liked to rely on the servants at the palace." }, 
            { id: "u16_4_4", content: "4. What did the Prince miss when he was being Sam?", options: ["Sleeping in his own chamber", "Having servants do things for him", "Signing all of the official documents", "People not emphasizing how important he was"], correctAnswer: "Having servants do things for him" },
            { id: "u16_4_5", content: "5. Why didn't Sam like the prince's chamber?", options: ["Because it was cold at night.", "Because it was too small.", "Because it was dirty.", "Because he didn't like the color."], correctAnswer: "Because it was cold at night." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('unit16.json', JSON.stringify(data, null, 2));
console.log('Successfully created unit16.json');
