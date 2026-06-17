const fs = require('fs');

const words = [
  { word: "alarm", pron: "[əlá:rm]", type: "n.", def: "An alarm is something that warns people of danger.", ex: "When the students heard the fire alarm, they left the building.", icon: "🚨" },
  { word: "apart", pron: "[əpά:rt]", type: "adv.", def: "When people or things are apart, they are not close together.", ex: "The couple decided to live apart from each other.", icon: "↔️" },
  { word: "arrest", pron: "[ərést]", type: "v.", def: "To arrest someone means to catch them for doing something bad.", ex: "The man was arrested for breaking the law.", icon: "👮" },
  { word: "award", pron: "[əwɔ́:rd]", type: "n.", def: "An award is a prize someone gets for doing something well.", ex: "He got an award for having the best grades in class.", icon: "🏆" },
  { word: "breed", pron: "[bri:d]", type: "n.", def: "A breed is a group of animals within a species.", ex: "I like small dog breeds, such as terriers.", icon: "🐕" },
  { word: "bucket", pron: "[bΛkit]", type: "n.", def: "A bucket is a round container to put things in.", ex: "I filled the bucket with water.", icon: "🪣" },
  { word: "contest", pron: "[kάntest]", type: "n.", def: "A contest is a game or a race.", ex: "The girls had a contest to see who could jump higher.", icon: "🏁" },
  { word: "convict", pron: "[kənvíkt]", type: "v.", def: "To convict someone means to prove that they did a bad thing.", ex: "He was convicted of the crime and sent to jail.", icon: "⚖️" },
  { word: "garage", pron: "[gərά:ʒ]", type: "n.", def: "A garage is the part of a house where people put their cars.", ex: "My car does not get dirty because I keep it in the garage.", icon: "🚗" },
  { word: "journalist", pron: "[dʒə́:rnəlist]", type: "n.", def: "A journalist is a person who writes news stories.", ex: "The journalist took notes for a story he was writing.", icon: "📝" },
  { word: "pup", pron: "[pʌp]", type: "n.", def: "A pup is a young dog.", ex: "All the girl wanted for her birthday was a pup.", icon: "🐶" },
  { word: "qualify", pron: "[kwάləfài]", type: "v.", def: "To qualify is to get, or to be declared, adequate or good enough.", ex: "He qualified to go to the final match by beating the opponent.", icon: "✅" },
  { word: "repair", pron: "[ripέər]", type: "v.", def: "To repair something is to fix it.", ex: "I repaired the flat tire on my car.", icon: "🔧" },
  { word: "resume", pron: "[rizú:m]", type: "v.", def: "To resume something means to start it again after taking a break.", ex: "I put the newspaper down to eat breakfast. Then I resumed reading.", icon: "▶️" },
  { word: "rob", pron: "[rɑb]", type: "v.", def: "To rob a person or place is to take their property by using force.", ex: "A thief has robbed me of my passport.", icon: "🦹" },
  { word: "slip", pron: "[slip]", type: "v.", def: "To slip means to slide and fall down.", ex: "The man slipped on the wet floor.", icon: "🍌" },
  { word: "somewhat", pron: "[sΛmw(h)Λt]", type: "adv.", def: "Somewhat means to some degree, but not to a large degree.", ex: "James was somewhat upset when he had to move some boxes.", icon: "🤏" },
  { word: "stable", pron: "[stéibl]", type: "adj.", def: "When something is stable, it will not fall over.", ex: "The chair is stable. Its legs are strong.", icon: "🪑" },
  { word: "tissue", pron: "[tíʃu:]", type: "n.", def: "A tissue is a soft piece of paper people use to wipe their noses.", ex: "There was a box of tissue on the table.", icon: "🤧" },
  { word: "yard", pron: "[jɑ:rd]", type: "n.", def: "A yard is the ground just outside of a person's house.", ex: "The girls jumped rope in the yard.", icon: "🏡" }
];

let wordsHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit22_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit22_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${w.icon}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordsHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Farm Festival</h1><p style="margin-bottom: 1rem;">Once there was a farm. Many animals lived there. One day, they had a <b>contest</b> in the <b>yard</b>. They were going to race from the barn to the farmer's <b>garage</b>. The barn and the <b>garage</b> were far <b>apart</b>. It would be a long race. The winner <b>qualified</b> to win a bag full of apples as an <b>award</b>.</p><p style="margin-bottom: 1rem;">But the race did not start well. The cart with all the apples was not <b>stable</b>, and the animals had to <b>repair</b> it. Then the <b>pup</b> knocked over the apples. The pig yelled, "We are going to <b>slip</b>! We must clean up this mess." The <b>pup</b> felt bad, and she began to cry. The dog gave her a <b>tissue</b> to wipe her tears.</p><p style="margin-bottom: 1rem;">Then the race <b>resumed</b>. But the duck tried to <b>rob</b> them and take all the apples. The cat said, "I will have you <b>arrested</b>!" The duck said, "You can't <b>convict</b> me! You can't prove I took it." The race stopped yet again.</p><p style="margin-bottom: 1rem;">The animals tried to race one more time. Then they heard an <b>alarm</b> coming from the barn. There was a fire! They got <b>buckets</b> of water to put out the fire. A <b>journalist</b> came to write a story about the festival and the race. The horse told her, "I am a special <b>breed</b> of horse. I would have won the race easily." The pig said, "It was <b>somewhat</b> hard to have the race. But we had fun. That is what's important."</p></div>`;

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 22",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordsHtml,
      sections: [
        {
          id: "sec1_wordlist",
          title: "Exercise 1 Part A: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. repair", options: ["to fix", "to start after a break", "to slide and fall", "to catch a bad person"], correctAnswer: "to fix", explanation: "repair: sửa chữa (to fix)" },
            { id: "2", content: "2. tissue", options: ["a soft paper", "a machine that blows air", "a news writer", "a container with wheels"], correctAnswer: "a soft paper", explanation: "tissue: khăn giấy (a soft paper)" },
            { id: "3", content: "3. pup", options: ["a place for a car", "a prize", "a baby dog", "a game or race"], correctAnswer: "a baby dog", explanation: "pup: chó con (a baby dog)" },
            { id: "4", content: "4. resume", options: ["to slide and fall", "to start after a break", "to prove", "to fix"], correctAnswer: "to start after a break", explanation: "resume: tiếp tục (to start after a break)" },
            { id: "5", content: "5. stable", options: ["a little bit", "a place for a car", "type of animal", "will not fall"], correctAnswer: "will not fall", explanation: "stable: ổn định (will not fall)" }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 1 Part B: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "6", content: "1. a place to put a car", options: ["stable", "bucket", "alarm", "garage"], correctAnswer: "garage", explanation: "garage: nhà để xe (a place to put a car)" },
            { id: "7", content: "2. to prove someone did a bad thing", options: ["somewhat", "repair", "convict", "resume"], correctAnswer: "convict", explanation: "convict: kết án (to prove someone did a bad thing)" },
            { id: "8", content: "3. not close together", options: ["apart", "arrest", "slip", "qualify"], correctAnswer: "apart", explanation: "apart: cách xa (not close together)" },
            { id: "9", content: "4. a type of animal", options: ["tissue", "breed", "yard", "contest"], correctAnswer: "breed", explanation: "breed: giống loài (a type of animal)" },
            { id: "10", content: "5. a news writer", options: ["pup", "journalist", "award", "qualify"], correctAnswer: "journalist", explanation: "journalist: nhà báo (a news writer)" }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 2: Check (√) the sentence with the bolded word that makes better sense.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "11", content: "1. Which sentence makes better sense?", options: ["Be careful not to slip on the ice.", "I hope my yard is ready to eat."], correctAnswer: "Be careful not to slip on the ice.", explanation: "slip: trượt té." },
            { id: "12", content: "2. Which sentence makes better sense?", options: ["I made a cake with my stable.", "The man robbed the store of over 200 dollars."], correctAnswer: "The man robbed the store of over 200 dollars.", explanation: "rob: cướp." },
            { id: "13", content: "3. Which sentence makes better sense?", options: ["The boy carried sand in his bucket.", "He used the contest to clean the floor."], correctAnswer: "The boy carried sand in his bucket.", explanation: "bucket: cái xô." },
            { id: "14", content: "4. Which sentence makes better sense?", options: ["The award for winning the game is a new toy.", "The boy pulled the car apart by washing it."], correctAnswer: "The award for winning the game is a new toy.", explanation: "award: phần thưởng." },
            { id: "15", content: "5. Which sentence makes better sense?", options: ["The mother arrested dinner for her family.", "An alarm sounds to warn us of a fire."], correctAnswer: "An alarm sounds to warn us of a fire.", explanation: "alarm: báo động." },
            { id: "16", content: "6. Which sentence makes better sense?", options: ["The stable tree did not fall in the wind.", "She slipped the table after dinner."], correctAnswer: "The stable tree did not fall in the wind.", explanation: "stable: ổn định, vững chắc." },
            { id: "17", content: "7. Which sentence makes better sense?", options: ["My dog likes to play in the yard.", "The man was upset after he robbed himself."], correctAnswer: "My dog likes to play in the yard.", explanation: "yard: cái sân." },
            { id: "18", content: "8. Which sentence makes better sense?", options: ["I fell down and got hurt as an award.", "I won the contest because I was the fastest runner."], correctAnswer: "I won the contest because I was the fastest runner.", explanation: "contest: cuộc thi." },
            { id: "19", content: "9. Which sentence makes better sense?", options: ["China and Mexico are far apart.", "The alarm washed away the dirt."], correctAnswer: "China and Mexico are far apart.", explanation: "apart: cách xa." },
            { id: "20", content: "10. Which sentence makes better sense?", options: ["The bucket wrote down every word.", "If you steal, the police will arrest you."], correctAnswer: "If you steal, the police will arrest you.", explanation: "arrest: bắt giữ." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit22_story.png",
      sections: [
        {
          id: "sec4_reading",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "21", content: "1. What is this story about?", options: ["Why contests have awards", "How a special breed of racehorse would've won the race", "Why animals have to repair things on a farm", "How animals had trouble during a race"], correctAnswer: "How animals had trouble during a race", explanation: "Đoạn văn kể về các vấn đề mà các con vật gặp phải trong cuộc đua." },
            { id: "22", content: "2. When the cart with the apples fell over, why did the animals stop running?", options: ["Because they did not want to slip on the apples", "Because they had to find tissue", "Because they did not want to resume the race", "Because the yard was far apart"], correctAnswer: "Because they did not want to slip on the apples", explanation: "Pig nói: 'We are going to slip!'" },
            { id: "23", content: "3. What did the duck do wrong?", options: ["He was arrested and convicted of stealing a bag of money.", "He stole the bucket.", "He tried to steal the award.", "He set the garage on fire."], correctAnswer: "He tried to steal the award.", explanation: "Vịt định trộm túi táo (phần thưởng)." },
            { id: "24", content: "4. According to the passage, all the following are true EXCEPT", options: ["the alarm sounded when there was a fire", "the animals were somewhat angry", "the cart was not stable", "a journalist wrote about the festival"], correctAnswer: "the animals were somewhat angry", explanation: "Không có chỗ nào nói các con vật 'somewhat angry', chúng nói 'somewhat hard' nhưng 'had fun'." },
            { id: "25", content: "5. How far was the race going to be?", options: ["From the barn to the farmer's garage", "From the yard to the house", "From the stable to the barn", "From the house to the field"], correctAnswer: "From the barn to the farmer's garage", explanation: "Cuộc đua từ the barn đến the farmer's garage." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit22.json', JSON.stringify(json, null, 0).replace(/\n/g, '').replace(/\r/g, ''));
console.log("JSON written successfully.");
