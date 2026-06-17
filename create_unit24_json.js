const fs = require('fs');

const words = [
  { word: "bath", phonetics: "[baee]", type: "n.", def: "A bath is water in a tub. People take a bath to get clean.", ex: "After playing in the dirt, the boy took a bath." },
  { word: "bend", phonetics: "[bend]", type: "v.", def: "To bend is to move something so it is not straight.", ex: "Lee bent over and picked up the paper on the ground." },
  { word: "chew", phonetics: "[t/u:]", type: "v.", def: "To chew is to move your mouth to break up food.", ex: "I always chew my food carefully before swallowing it." },
  { word: "disabled", phonetics: "[diseibald]", type: "adj.", def: "When a person is disabled, they cannot do what a normal person can do.", ex: "The disabled man used a wheelchair to move around." },
  { word: "fantastic", phonetics: "[fasntaestik]", type: "adj.", def: "If something is fantastic, it is really good.", ex: "The student did a fantastic job on his project and got an award." },
  { word: "fiction", phonetics: "[fi'kjan]", type: "n.", def: "Fiction is a story that is not true.", ex: "I enjoy reading works of fiction because they are very entertaining." },
  { word: "flag", phonetics: "[flaeg]", type: "n.", def: "A flag is a piece of colored cloth that represents something.", ex: "Our country has a beautiful flag." },
  { word: "inspect", phonetics: "[inspekt]", type: "v.", def: "To inspect is to look at something carefully.", ex: "The mechanic inspected our car to see if it had any problems." },
  { word: "journal", phonetics: "[d3a:msl]", type: "n.", def: "A journal is a type of magazine that deals with an academic subject.", ex: "Mi-young was busy working on an article for an art journal." },
  { word: "liquid", phonetics: "[h'kwid]", type: "n.", def: "A liquid is a substance that is neither solid nor gas.", ex: "Water is the most important liquid for life." },
  { word: "marvel", phonetics: "[maxvsl]", type: "v.", def: "To marvel at something is to feel surprise and interest in it.", ex: "We marveled at her excellent piano playing." },
  { word: "nutrient", phonetics: "[nyu:triant]", type: "n.", def: "A nutrient is something that a living thing needs to keep it alive.", ex: "Vegetables are full of important nutrients." },
  { word: "overcome", phonetics: "[ouvarkAm]", type: "v.", def: "To overcome a problem is to successfully fix it.", ex: "She overcame her shyness and spoke in front of the class." },
  { word: "recall", phonetics: "[riko:i]", type: "v.", def: "To recall something is to remember it.", ex: "She was trying to recall what she had told her friend." },
  { word: "regret", phonetics: "[ngret]", type: "v.", def: "To regret something is to wish that it didn’t happen.", ex: "I regret that I was mean to my sister." },
  { word: "soul", phonetics: "[soul]", type: "n.", def: "A soul is a person’s spirit.", ex: "Some people believe that the soul lives after the body dies." },
  { word: "sufficient", phonetics: "[safijsnt]", type: "adj.", def: "When something is sufficient, you have enough of it.", ex: "After eating a sufficient amount of food, I left the table." },
  { word: "surgery", phonetics: "[safari]", type: "n.", def: "Surgery is medical treatment when the doctor cuts open your body.", ex: "I needed surgery to repair my leg after the accident." },
  { word: "tough", phonetics: "[tAf]", type: "adj.", def: "If something is tough, it is difficult.", ex: "The man passed his driving test even though it was very tough." },
  { word: "tube", phonetics: "[t/u:b]", type: "n.", def: "A tube is a pipe through which water or air passes.", ex: "The pile of tubes was going to be put in the ground." }
];

let wordHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit24_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit24_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

for (const w of words) {
  wordHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetics}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
}
wordHtml += `</div></div></div>`;

const boldWords = ["bath", "bend", "chew", "disabled", "fantastic", "fiction", "flag", "inspect", "journal", "liquid", "marvel", "nutrient", "overcome", "recall", "regret", "soul", "sufficient", "surgery", "tough", "tube"];
const boldWordsRegex = new RegExp("\\\\b(" + boldWords.join("|") + "s?|nutrients?|surgeries?|overcame|inspected|marveled|recalls?|disabled)\\\\b", "gi");

const storyHtmlRaw = `<div style="font-family: Arial, sans-serif; ">
<h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Doctor's Cure</h1>
<p style="margin-bottom: 1rem;">James Fry was a fantastic doctor. His surgeries helped many disabled people overcome their injuries. He also wrote for a popular medical journal. James was very busy. His son, Steve, rarely saw him.</p>
<p style="margin-bottom: 1rem;">One day, James was walking and inspecting a patient's file. There was water all over the floor. James slipped on the liquid and fell. He fell on a broken glass tube. He was hurt.</p>
<p style="margin-bottom: 1rem;">Steve came to visit him in the hospital. James said, "It will be tough for me to stay in bed. But I can hardly bend my legs."</p>
<p style="margin-bottom: 1rem;">"Then let's watch a movie." Steve said. It made them laugh together. Steve said, "I have to leave, but here's some fiction to read."</p>
<p style="margin-bottom: 1rem;">James started to recall fun parts of life. He marveled at small things, like food. He was too busy to notice them before. "Steve," he said, "you get more nutrients when you chew slowly. But I think it makes food taste better, too!"</p>
<p style="margin-bottom: 1rem;">Weeks later, James said, "Steve, I haven't spent enough time with you. I regret this. Even my soul feels better when you visit. But I have spent sufficient time here. We should go home."</p>
<p style="margin-bottom: 1rem;">Outside, there was a warm breeze. James watched a flag blow.</p>
<p style="margin-bottom: 1rem;">Finally, James said, "I'm not ready to work. I'm going to take a long bath. And then we'll watch a movie together."</p>
</div>`;

const processedStoryHtml = storyHtmlRaw.replace(boldWordsRegex, "<b>$1</b>").replace(/\\n/g, "");

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
      content: wordHtml,
      sections: [
        {
          id: "sec1_wordlist",
          title: "Exercise 1: Check (V) the better response for each question.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "1",
              content: "1. Why do you look so clean?",
              options: ["I was using a journal.", "I just took a bath."],
              correctAnswer: "I just took a bath.",
              explanation: "Tắm rửa giúp sạch sẽ."
            },
            {
              id: "2",
              content: "2. Can you touch your toes?",
              options: ["I marvel at my abilities.", "No, I can't bend that far."],
              correctAnswer: "No, I can't bend that far.",
              explanation: "Bend (cúi gập) liên quan đến việc chạm ngón chân."
            },
            {
              id: "3",
              content: "3. Do you remember the movie we saw together?",
              options: ["Yes, I recall it was wonderful.", "No, I think it was fiction."],
              correctAnswer: "Yes, I recall it was wonderful.",
              explanation: "Recall có nghĩa là remember (nhớ lại)."
            },
            {
              id: "4",
              content: "4. What do you think we need for our classroom?",
              options: ["We should have a flag in the corner.", "Yes, I think it is fantastic."],
              correctAnswer: "We should have a flag in the corner.",
              explanation: "Flag (lá cờ) phù hợp để đặt trong lớp học."
            },
            {
              id: "5",
              content: "5. How do you feel about your new car?",
              options: ["It uses sufficient gas.", "I regret buying it."],
              correctAnswer: "I regret buying it.",
              explanation: "Regret (hối hận) nói lên cảm xúc về chiếc xe mới."
            }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 2: Fill in the blanks with the correct words from the word bank.",
          content: "Word bank: chew, inspected, nutrients, overcome, surgery",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "6",
              content: "1. Franklin felt pain in his stomach. The doctor _____ him to find the cause.",
              options: ["inspected", "chew", "nutrients", "overcome", "surgery"],
              correctAnswer: "inspected",
              explanation: "inspected (kiểm tra)"
            },
            {
              id: "7",
              content: "2. His doctor said Franklin needed to _____ his food more slowly.",
              options: ["inspected", "chew", "nutrients", "overcome", "surgery"],
              correctAnswer: "chew",
              explanation: "chew (nhai)"
            },
            {
              id: "8",
              content: "3. If he did, he could get all the _____ he needed.",
              options: ["inspected", "chew", "nutrients", "overcome", "surgery"],
              correctAnswer: "nutrients",
              explanation: "nutrients (chất dinh dưỡng)"
            },
            {
              id: "9",
              content: "4. It would also help him _____ his pain.",
              options: ["inspected", "chew", "nutrients", "overcome", "surgery"],
              correctAnswer: "overcome",
              explanation: "overcome (vượt qua)"
            },
            {
              id: "10",
              content: "5. If Franklin didn't listen, the doctor would have to perform _____.",
              options: ["inspected", "chew", "nutrients", "overcome", "surgery"],
              correctAnswer: "surgery",
              explanation: "surgery (phẫu thuật)"
            }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 3: Complete the sentences.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "11",
              content: "1. When you want to learn about history, _____",
              options: ["you should read an academic journal", "you should read fiction"],
              correctAnswer: "you should read an academic journal",
              explanation: "journal (tạp chí học thuật) phù hợp với lịch sử."
            },
            {
              id: "12",
              content: "2. In front of a government building, _____",
              options: ["there is usually a flag", "there are usually baths"],
              correctAnswer: "there is usually a flag",
              explanation: "flag (lá cờ) trước tòa nhà chính phủ."
            },
            {
              id: "13",
              content: "3. When people die, _____",
              options: ["they have to get surgery", "their soul goes to heaven"],
              correctAnswer: "their soul goes to heaven",
              explanation: "soul (linh hồn)."
            },
            {
              id: "14",
              content: "4. A lot of people eat too quickly. _____",
              options: ["They hardly chew their food", "They only drink liquids"],
              correctAnswer: "They hardly chew their food",
              explanation: "chew (nhai) quá ít khi ăn nhanh."
            },
            {
              id: "15",
              content: "5. The movie was better than we imagined. _____",
              options: ["It was sufficient", "It was fantastic"],
              correctAnswer: "It was fantastic",
              explanation: "fantastic (tuyệt vời)."
            },
            {
              id: "16",
              content: "6. This is an important decision. _____",
              options: ["I feel like I need to bend forward", "I don't want to have to regret making a mistake"],
              correctAnswer: "I don't want to have to regret making a mistake",
              explanation: "regret (hối hận) khi quyết định sai."
            },
            {
              id: "17",
              content: "7. Before you buy a car, _____",
              options: ["marvel at it", "inspect it carefully"],
              correctAnswer: "inspect it carefully",
              explanation: "inspect (kiểm tra)."
            },
            {
              id: "18",
              content: "8. After the accident, _____",
              options: ["Ali was disabled", "Ali had a tube"],
              correctAnswer: "Ali was disabled",
              explanation: "disabled (khuyết tật)."
            },
            {
              id: "19",
              content: "9. Memorize this address, _____",
              options: ["then you will feel tough", "so you will be able to recall it in the future"],
              correctAnswer: "so you will be able to recall it in the future",
              explanation: "recall (nhớ lại)."
            },
            {
              id: "20",
              content: "10. He climbed the mountain _____",
              options: ["and overcame his fear of heights", "to get more nutrients"],
              correctAnswer: "and overcame his fear of heights",
              explanation: "overcame (vượt qua)."
            }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: processedStoryHtml,
      imageUrl: "/unit24_story.png",
      sections: [
        {
          id: "sec4_reading",
          title: "Reading Comprehension: Answer the questions based on the story.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "21",
              content: "1. What is this story about?",
              options: [
                "A doctor who needs surgery",
                "A boy with a fantastic comedy video",
                "A doctor who recalls fun things",
                "A disabled boy who overcomes injuries"
              ],
              correctAnswer: "A doctor who recalls fun things",
              explanation: "Câu chuyện về một bác sĩ (James) bị thương và nhớ lại những điều vui vẻ trong cuộc sống."
            },
            {
              id: "22",
              content: "2. What does James notice now that he isn't busy?",
              options: [
                "Food tastes better when you chew it slowly.",
                "Reading fiction is tough.",
                "He regrets not working more.",
                "His soul feels worse than before."
              ],
              correctAnswer: "Food tastes better when you chew it slowly.",
              explanation: "Anh ấy nhận ra thức ăn ngon hơn khi nhai chậm."
            },
            {
              id: "23",
              content: "3. How did James get hurt?",
              options: [
                "He didn't get enough nutrients.",
                "He slipped and fell on a broken tube.",
                "He didn't spend sufficient time at the hospital.",
                "He slipped on liquid after a bath."
              ],
              correctAnswer: "He slipped and fell on a broken tube.",
              explanation: "Anh ấy trượt ngã và rơi vào ống thủy tinh bị vỡ."
            },
            {
              id: "24",
              content: "4. What does James do when he leaves the hospital?",
              options: [
                "He inspects a patient's file.",
                "He shows Steve that he can bend his legs.",
                "He watches a flag blow in the breeze.",
                "He marvels at the taste of food."
              ],
              correctAnswer: "He watches a flag blow in the breeze.",
              explanation: "Bên ngoài có làn gió ấm, James nhìn lá cờ bay (He watches a flag blow)."
            },
            {
              id: "25",
              content: "5. What did the movie do to James and Steve?",
              options: [
                "It made them laugh together.",
                "It made them cry.",
                "It made them angry.",
                "It put them to sleep."
              ],
              correctAnswer: "It made them laugh together.",
              explanation: "Bộ phim làm họ cười cùng nhau."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync("unit24.json", JSON.stringify(json, null, 2));
