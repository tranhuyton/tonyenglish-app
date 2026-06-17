const fs = require('fs');

const words = [
  { word: "actual", pron: "[æktʃuəl]", type: "adj.", def: "Actual means that something is real or true.", ex: "This is the actual sword that the King owned, not a fake one.", icon: "🎯" },
  { word: "amaze", pron: "[əméiz]", type: "v.", def: "To amaze someone is to surprise them very much.", ex: "The news in the paper amazed Jack.", icon: "😲" },
  { word: "charge", pron: "[tʃɑ:rdʒ]", type: "n.", def: "A charge is the price to pay for something.", ex: "The charge for the shirts was $15.00.", icon: "💰" },
  { word: "comfort", pron: "[kʌ́mfərt]", type: "v.", def: "To comfort someone means to make them feel better.", ex: "I wanted to comfort my friend after I heard the bad news.", icon: "🫂" },
  { word: "contact", pron: "[kɑ́ntækt]", type: "v.", def: "To contact someone is to speak or write to them.", ex: "I contacted Sue about my party.", icon: "📞" },
  { word: "customer", pron: "[kʌ́stəmər]", type: "n.", def: "A customer is a person who buys something at a store.", ex: "The customer put a few items in a bag.", icon: "🛒" },
  { word: "deliver", pron: "[dilívər]", type: "v.", def: "To deliver something is to take it from one place to another.", ex: "The man delivered Chinese food to my house.", icon: "🚚" },
  { word: "earn", pron: "[ə:rn]", type: "v.", def: "To earn means to get money for the work you do.", ex: "He earns his living as a chef in a great restaurant.", icon: "💵" },
  { word: "gate", pron: "[geit]", type: "n.", def: "A gate is a type of door. Gates are usually made of metal or wood.", ex: "We want to put up a wooden gate around our house.", icon: "🚪" },
  { word: "include", pron: "[inklu:d]", type: "v.", def: "To include something means to have it as part of a group.", ex: "Does this meal include a soft drink?", icon: "➕" },
  { word: "manage", pron: "[mǽnidʒ]", type: "v.", def: "To manage something means to control or be in charge of it.", ex: "I had to manage the meeting myself.", icon: "👨‍💼" },
  { word: "mystery", pron: "[místəri]", type: "n.", def: "A mystery is something that is difficult to understand or explain.", ex: "The path on the map was a complete mystery to me.", icon: "🕵️" },
  { word: "occur", pron: "[əkə:r]", type: "v.", def: "To occur means to happen.", ex: "When did the thunderstorm occur?", icon: "⚡" },
  { word: "opposite", pron: "[ɑ́pəzit]", type: "n.", def: "If A is the opposite of B, A is completely different from B.", ex: "The opposite of black is white.", icon: "↔️" },
  { word: "plate", pron: "[pleit]", type: "n.", def: "A plate is a flat round thing that you put food on.", ex: "I put my plate down so I could put some food on it.", icon: "🍽️" },
  { word: "receive", pron: "[risí:v]", type: "v.", def: "To receive something is to get it.", ex: "I received a present on my birthday.", icon: "🎁" },
  { word: "reward", pron: "[riwɔ́:rd]", type: "n.", def: "A reward is something given in exchange for good behavior or work.", ex: "He was given a reward for his excellent performance.", icon: "🏆" },
  { word: "set", pron: "[set]", type: "v.", def: "To set something is to put it somewhere.", ex: "Please set the dice down on the table.", icon: "🎲" },
  { word: "steal", pron: "[sti:l]", type: "v.", def: "To steal is to take something that is not yours.", ex: "The men tried to steal money from the bank.", icon: "🦹" },
  { word: "thief", pron: "[θi:f]", type: "n.", def: "A thief is someone who quietly takes things that do not belong to them.", ex: "A thief broke into our home and took my mother's jewelry.", icon: "🥷" }
];

let wordsHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit22_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit22_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${w.icon}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordsHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; ">    <h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">A Better Reward</h1>        <p style="margin-bottom: 1rem;">Jenny <b>delivered</b> food for a restaurant. She read the newspaper and said, "Uh oh." There was a story about a <b>thief</b>. He <b>stole</b> food, and no one had seen him. Even the police couldn't catch him. Jenny was a little scared. She worked close to that area.</p>    <p style="margin-bottom: 1rem;">The newspaper <b>included</b> a message from the police: "If anything strange <b>occurs</b>, call us. If you help us catch the <b>thief</b>, you'll <b>earn</b> a <b>reward</b>."</p>    <p style="margin-bottom: 1rem;">Jenny talked to Jim. He <b>managed</b> the restaurant. "Do you know about the <b>thief</b>?"</p>    <p style="margin-bottom: 1rem;">"Yes," he said. "But he <b>steals</b> more than one person can eat. And why haven't the police stopped him yet? It's a <b>mystery</b>. If you see him, <b>contact</b> the police. Don't run after him."</p>    <p style="margin-bottom: 1rem;">Jenny drove to a <b>customer</b>'s house. She left her car and opened the <b>gate</b> to the house. But then she heard a noise by her car. She yelled, "Thief!" She wasn't scared. She wanted the <b>reward</b>! She did the <b>opposite</b> of what Jim told her to do.</p>    <p style="margin-bottom: 1rem;">"Hey," she yelled. "Get back here!" She <b>set</b> the food on the ground and ran to her car.</p>    <p style="margin-bottom: 1rem;">But the <b>thief</b> had already left with the food. Jenny followed a noise around the corner. She was <b>amazed</b>. She saw a dog and some puppies. They were eating her food! They looked thin and scared. "The <b>actual</b> <b>thief</b> is just a dog. She's feeding her puppies," she said. "That's why she <b>steals</b> so much food."</p>    <p style="margin-bottom: 1rem;">Jenny felt bad. She tried to <b>comfort</b> the dogs with another <b>plate</b> of food. Then she took them back to the store. Everyone there took a puppy home. Jenny called the police. She told them there was no real <b>thief</b>.</p>    <p style="margin-bottom: 1rem;">Jenny didn't do it to <b>receive</b> the <b>reward</b> anymore. She said, "It was just a dog. But there's no <b>charge</b> for catching this '<b>thief</b>,'" she said. "My new dog is a better <b>reward</b>."</p></div>`;

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
          title: "Exercise 1: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. to take something that does not belong to you", options: ["steal", "include", "amaze", "plate"], correctAnswer: "steal", explanation: "steal (ăn cắp)." },
            { id: "2", content: "2. to happen", options: ["manage", "set", "deliver", "occur"], correctAnswer: "occur", explanation: "occur (xảy ra)." },
            { id: "3", content: "3. to make someone feel better", options: ["reward", "earn", "comfort", "contact"], correctAnswer: "comfort", explanation: "comfort (an ủi)." },
            { id: "4", content: "4. to get", options: ["receive", "gate", "charge", "actual"], correctAnswer: "receive", explanation: "receive (nhận)." },
            { id: "5", content: "5. a person who buys something", options: ["opposite", "mystery", "customer", "thief"], correctAnswer: "customer", explanation: "customer (khách hàng)." }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 2: Check (√) the sentence with the bolded word that makes better sense.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "6", content: "1. Which sentence makes better sense?", options: ["If I receive a present, I give someone something.", "If you steal money, you can get in trouble."], correctAnswer: "If you steal money, you can get in trouble.", explanation: "Ăn cắp tiền (steal money) thì sẽ gặp rắc rối." },
            { id: "7", content: "2. Which sentence makes better sense?", options: ["A man who is alone can contact many people.", "If a woman is sad, someone should comfort her."], correctAnswer: "If a woman is sad, someone should comfort her.", explanation: "Khi buồn thì cần được an ủi (comfort)." },
            { id: "8", content: "3. Which sentence makes better sense?", options: ["He was given a reward for his poor work performance.", "You eat dinner off a plate."], correctAnswer: "You eat dinner off a plate.", explanation: "Ăn tối trên đĩa (plate)." },
            { id: "9", content: "4. Which sentence makes better sense?", options: ["Everything that is for sale has a charge.", "A customer sells things to people."], correctAnswer: "Everything that is for sale has a charge.", explanation: "Mọi thứ để bán đều có giá (charge)." },
            { id: "10", content: "5. Which sentence makes better sense?", options: ["If you earn something, you give it to someone.", "Postmen deliver mail from one house to another."], correctAnswer: "Postmen deliver mail from one house to another.", explanation: "Người đưa thư giao thư (deliver)." }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 3: Check (√) the better response to each question.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "11", content: "1. Who should manage the classroom?", options: ["The teacher should be in charge.", "The students should go to the classroom."], correctAnswer: "The teacher should be in charge.", explanation: "manage (quản lý)." },
            { id: "12", content: "2. When did the theft occur?", options: ["It happened this afternoon.", "It stopped early."], correctAnswer: "It happened this afternoon.", explanation: "occur (xảy ra)." },
            { id: "13", content: "3. What is the actual number of people there?", options: ["There are 31,872 people there.", "There are a lot of people there."], correctAnswer: "There are 31,872 people there.", explanation: "actual (thực tế, chính xác)." },
            { id: "14", content: "4. Did that movie amaze you?", options: ["Yes, I had seen it many times before.", "Yes, the ending surprised me very much."], correctAnswer: "Yes, the ending surprised me very much.", explanation: "amaze (làm ngạc nhiên)." },
            { id: "15", content: "5. Where should I set this book?", options: ["Put it on the bookshelf.", "It came from the library."], correctAnswer: "Put it on the bookshelf.", explanation: "set (đặt)." },
            { id: "16", content: "6. Does the wall have a gate?", options: ["Yes, and it is often locked.", "Yes, the wall is very high."], correctAnswer: "Yes, and it is often locked.", explanation: "gate (cổng)." },
            { id: "17", content: "7. Does the book include a CD?", options: ["No, it is inside the book.", "No, we must buy the extra CD."], correctAnswer: "No, we must buy the extra CD.", explanation: "include (bao gồm)." },
            { id: "18", content: "8. Has he received my present?", options: ["He got it yesterday.", "He sent it to you yesterday."], correctAnswer: "He got it yesterday.", explanation: "receive (nhận)." },
            { id: "19", content: "9. What happened to the plate?", options: ["It broke when I dropped it.", "It helped me with my homework."], correctAnswer: "It broke when I dropped it.", explanation: "plate (cái đĩa)." },
            { id: "20", content: "10. Did you hear the news about the thief?", options: ["He stole some expensive diamonds from the jewelry store.", "There was a person buying something."], correctAnswer: "He stole some expensive diamonds from the jewelry store.", explanation: "thief (kẻ trộm)." }
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
            { id: "21", content: "1. What is this story about?", options: ["A dog that steals a plate", "A man who tells a mystery", "A man who writes for a newspaper", "A girl who delivers food"], correctAnswer: "A girl who delivers food", explanation: "Câu chuyện về cô gái đi giao thức ăn." },
            { id: "22", content: "2. Why did Jenny decide to run after the thief?", options: ["She wanted to earn the reward.", "She knew that there was no actual thief.", "She always did the opposite of what Jim said.", "She wanted to charge a customer for that food."], correctAnswer: "She wanted to earn the reward.", explanation: "Cô ấy muốn phần thưởng (She wanted the reward!)." },
            { id: "23", content: "3. What was true of Jim?", options: ["He tried to comfort Jenny with food.", "He told Jenny that she should contact the police.", "He wrote a story that included a message from the police.", "He received a reward because he managed the store."], correctAnswer: "He told Jenny that she should contact the police.", explanation: "Anh ta khuyên cô ấy gọi cảnh sát (contact the police)." },
            { id: "24", content: "4. How did Jenny act when she heard the noise?", options: ["She was amazed by the noise.", "She followed it around the corner.", "She ran through the gate to get away from it.", "She set the food on a table and ran to her car."], correctAnswer: "She followed it around the corner.", explanation: "Cô ấy đi theo tiếng động qua góc đường (Jenny followed a noise around the corner)." },
            { id: "25", content: "5. What did the police say to do if something strange occured?", options: ["\"If anything strange occurs, call us. If you help us catch the thief, you'll earn a reward.\"", "Do not run after the thief.", "Wait for a reward.", "Contact Jim at the restaurant."], correctAnswer: "\"If anything strange occurs, call us. If you help us catch the thief, you'll earn a reward.\"", explanation: "Cảnh sát nói hãy gọi họ và nhận thưởng (call us... earn a reward)." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit22.json', JSON.stringify(json, null, 2));
console.log("JSON written successfully.");
