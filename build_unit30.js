const fs = require('fs');

const words = [
  { word: "above", phonetics: "[əbʌv]", type: "prep.", def: "If something is above, it is at a higher level than something else.", ex: "He straightened the sign that was above the crowd." },
  { word: "ahead", phonetics: "[əhed]", type: "adv.", def: "If something is ahead of something else, it is in front of it.", ex: "The blue car drove on ahead of us." },
  { word: "amount", phonetics: "[əmaunt]", type: "n.", def: "An amount is how much there is of something.", ex: "Can I use my card to pay for the entire amount?" },
  { word: "belief", phonetics: "[bili:f]", type: "n.", def: "A belief is a strong feeling that something is correct or true.", ex: "A preacher or priest should have a strong belief in God." },
  { word: "center", phonetics: "[sentər]", type: "n.", def: "The center of something is the middle of it.", ex: "The center of a dart board is the most important spot." },
  { word: "common", phonetics: "[kɑmən]", type: "adj.", def: "If something is common, it happens often or there is much of it.", ex: "It is common for snow to fall in the winter." },
  { word: "cost", phonetics: "[kɔ:st]", type: "v.", def: "To cost is to require expenditure or payment.", ex: "These designer shoes cost more than the regular ones." },
  { word: "demonstrate", phonetics: "[demənstreit]", type: "v.", def: "To demonstrate something is to show how it is done.", ex: "She demonstrated her plan to her co-workers." },
  { word: "different", phonetics: "[difərənt]", type: "adj.", def: "Different describes someone or something that is not the same as others.", ex: "Each of my sisters has a different hair style from one another." },
  { word: "evidence", phonetics: "[evidəns]", type: "n.", def: "Evidence is a fact or thing that you use to prove something.", ex: "He used the pictures as evidence that UFOs are real." },
  { word: "honesty", phonetics: "[anisti]", type: "n.", def: "Honesty means the quality of being truthful or honest.", ex: "A courtroom should be a place of honesty." },
  { word: "idiom", phonetics: "[idiəm]", type: "n.", def: "An idiom is a phrase with a meaning different from its words.", ex: "The idiom “when pigs fly” means that something will never happen." },
  { word: "independent", phonetics: "[indipendənt]", type: "adj.", def: "If something is independent, it is not controlled by something else.", ex: "She chose to live an independent life in the country." },
  { word: "inside", phonetics: "[insaid]", type: "n.", def: "Inside means the inner part, space or side of something.", ex: "The inside of the box was empty." },
  { word: "master", phonetics: "[mæstər]", type: "n.", def: "A master is a person who is very good at something.", ex: "My brother is a master of taekwondo." },
  { word: "memory", phonetics: "[meməri]", type: "n.", def: "A memory is something you remember.", ex: "The memory of my first time in the city will always be the best." },
  { word: "proper", phonetics: "[prɑpər]", type: "adj.", def: "If something is proper, it is right.", ex: "It is not proper to throw your garbage on the road." },
  { word: "scan", phonetics: "[skæn]", type: "v.", def: "To scan something is to look at it very carefully.", ex: "You must scan each person closely." },
  { word: "section", phonetics: "[sekʃən]", type: "n.", def: "A section is a part of something larger.", ex: "The green section of the graph is the most important part." },
  { word: "surface", phonetics: "[sə:rfis]", type: "n.", def: "The surface of something is the top part or outside of it.", ex: "The surface of the moon is very rough." }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit30_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit30_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetics}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const questions1 = [
  { id: "1", content: "1. section", options: ["higher", "the top layer", "a part", "to look at"], correctAnswer: "a part", explanation: "section nghĩa là phần (a part)." },
  { id: "2", content: "2. inside", options: ["in front", "the inner part", "proof", "someone very good at something"], correctAnswer: "the inner part", explanation: "inside nghĩa là bên trong (the inner part)." },
  { id: "3", content: "3. proper", options: ["a strong feeling", "to treat the same", "correct", "in the middle"], correctAnswer: "correct", explanation: "proper nghĩa là đúng, thích hợp (correct)." },
  { id: "4", content: "4. different", options: ["not influenced", "not the same", "to show how to do", "a phrase with a different meaning"], correctAnswer: "not the same", explanation: "different nghĩa là khác biệt (not the same)." },
  { id: "5", content: "5. memory", options: ["a bag in clothes", "a normal thing", "how much money", "something you remember"], correctAnswer: "something you remember", explanation: "memory nghĩa là trí nhớ (something you remember)." },
  { id: "6", content: "6. idiom", options: ["higher", "a meaning different from its words", "facts that prove something", "to look carefully"], correctAnswer: "a meaning different from its words", explanation: "idiom nghĩa là thành ngữ (a meaning different from its words)." },
  { id: "7", content: "7. amount", options: ["how much there is", "a part of something larger", "to treat the same", "the right thing to do"], correctAnswer: "how much there is", explanation: "amount nghĩa là số lượng (how much there is)." },
  { id: "8", content: "8. honesty", options: ["the top of something", "to learn about something", "in front of something", "the quality of being truthful"], correctAnswer: "the quality of being truthful", explanation: "honesty nghĩa là sự trung thực (the quality of being truthful)." },
  { id: "9", content: "9. master", options: ["a way of acting", "someone who is very good at something", "to show how to do something", "a feeling that something is correct or true"], correctAnswer: "someone who is very good at something", explanation: "master nghĩa là chuyên gia, bậc thầy (someone who is very good at something)." },
  { id: "10", content: "10. scan", options: ["to give something to someone", "to look carefully at something", "something that happens a lot", "something you remember"], correctAnswer: "to look carefully at something", explanation: "scan nghĩa là quét, nhìn kỹ (to look carefully at something)." }
];

const questions2 = [
  { id: "11", content: "1. Is his picture above mine?", options: ["Yes, it is much lower than yours.", "Yes, it is much higher than yours."], correctAnswer: "Yes, it is much higher than yours.", explanation: "above nghĩa là ở trên, cao hơn." },
  { id: "12", content: "2. Should we go straight ahead to get to your house?", options: ["No, we must turn left.", "No, it is in front of us."], correctAnswer: "No, we must turn left.", explanation: "ahead nghĩa là đi thẳng về phía trước. Nếu không đi thẳng thì rẽ trái." },
  { id: "13", content: "3. Is this the correct amount?", options: ["No, you must pay more money.", "No, that is the wrong answer."], correctAnswer: "No, you must pay more money.", explanation: "amount liên quan đến số lượng tiền cần trả." },
  { id: "14", content: "4. What is your belief about ghosts?", options: ["I think they are real.", "There are many movies about ghosts."], correctAnswer: "I think they are real.", explanation: "belief là niềm tin." },
  { id: "15", content: "5. Did he put the table in the center of the room?", options: ["Yes, it is against the wall.", "Yes, it is right in the middle."], correctAnswer: "Yes, it is right in the middle.", explanation: "center nghĩa là ở giữa (in the middle)." },
  { id: "16", content: "6. Is lightning common here?", options: ["No, it happens all the time.", "No, it never happens here."], correctAnswer: "No, it never happens here.", explanation: "common nghĩa là phổ biến. Nếu không phổ biến thì nghĩa là không bao giờ xảy ra (never happens)." },
  { id: "17", content: "7. Can you demonstrate how to solve the problem?", options: ["Yes, I can show you.", "No, I know how to do it."], correctAnswer: "Yes, I can show you.", explanation: "demonstrate nghĩa là thể hiện, trình bày." },
  { id: "18", content: "8. Do you have evidence to prove it?", options: ["Yes, I have a news article.", "Yes, I think that I'm a nice person."], correctAnswer: "Yes, I have a news article.", explanation: "evidence là bằng chứng." },
  { id: "19", content: "9. How much did your shirt cost?", options: ["It was on sale for $15.", "I bought it at the mall last week."], correctAnswer: "It was on sale for $15.", explanation: "cost hỏi về giá cả." },
  { id: "20", content: "10. Will he be an independent leader?", options: ["Yes, he always does what other people do.", "Yes, he makes his own decisions."], correctAnswer: "Yes, he makes his own decisions.", explanation: "independent nghĩa là độc lập, tự đưa ra quyết định." }
];

let storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Cats and Secrets</h1><p style="margin-bottom: 1rem;">        In English, there is a <b>common</b> <b>idiom</b> "let the cat out of the bag." It means to tell a secret. But where did this <b>idiom</b> start?</p><p style="margin-bottom: 1rem;">        It came from a <b>section</b> of England. Long ago, people there went from town to town to sell things like vegetables, clothes, and pigs. They had strong <b>beliefs</b> about <b>honesty</b>. They didn't like lying. One day, a man went to the <b>section</b>'s <b>center</b> to sell things.</p><p style="margin-bottom: 1rem;">        "I have a baby pig for sale! It won't <b>cost</b> much," he said. He held the animal <b>above</b> his head. His style was <b>different</b> from honest people's style. He was a <b>master</b> of tricking people and lying.</p><p style="margin-bottom: 1rem;">        A woman named Beth <b>scanned</b> his pig. He offered her the pig for one gold coin. That was a very small <b>amount</b>. Beth gave him the coin. He put it in his pocket. He walked <b>ahead</b> of Beth to get the pig.</p><p style="margin-bottom: 1rem;">        He gave her a closed bag and said, "Here's your pig." He then left very quickly.</p><p style="margin-bottom: 1rem;">        Beth looked at the bag's <b>surface</b>. It was moving. She opened it to let the pig out. A cat was <b>inside</b>! "He tricked me! That isn't <b>proper</b>," she said.</p><p style="margin-bottom: 1rem;">        Later, the man returned to trick more people. Beth saw him and the <b>memory</b> of the cat came back. She told her friends. They stopped him. But no one knew what to do next.</p><p style="margin-bottom: 1rem;">        Someone said, "We need an <b>independent</b> and fair person to decide that." They went to the judge. Beth told him about the cat in the bag.</p><p style="margin-bottom: 1rem;">        The judge asked, "Is there <b>evidence</b>? Can you <b>demonstrate</b> how he did it?"</p><p style="margin-bottom: 1rem;">        "Look in his bag," said Beth. She opened it and let a cat out of the bag. They learned the man's secret, and he went to jail.</p><p style="margin-bottom: 1rem;">        That's how the <b>idiom</b> "let the cat out of the bag" came to mean to tell a secret.</p></div>`;

// minify HTML
wordListHtml = wordListHtml.replace(/\\n/g, '').replace(/\\r/g, '').replace(/>\\s+</g, '><').trim();
storyHtml = storyHtml.replace(/\\n/g, '').replace(/\\r/g, '').replace(/>\\s+</g, '><').trim();

const storyQuestions = [
  { id: "21", content: "1. What is the main idea of this story?", options: ["It is about a common belief about cats.", "People should scan evidence carefully.", "Masters of lying will go to jail.", "It is about the origin of an idiom."], correctAnswer: "It is about the origin of an idiom.", explanation: "Bài đọc kể về nguồn gốc của một thành ngữ (It is about the origin of an idiom)." },
  { id: "22", content: "2. What did Beth say after she was tricked?", options: ["That's not proper.", "That's a very small amount.", "Can you demonstrate how he did it?", "We need an independent and fair person to help."], correctAnswer: "That's not proper.", explanation: "Trong bài có câu 'That isn't proper, she said.' (Đó không phải là điều đúng đắn)." },
  { id: "23", content: "3. Where did the man hold the pig?", options: ["In a pocket", "On the surface of the bag", "Above his head", "In the section's center"], correctAnswer: "Above his head", explanation: "Trong bài ghi 'He held the animal above his head.' (Anh ta giữ con vật trên đầu mình)." },
  { id: "24", content: "4. Why did Beth look at the bag?", options: ["The surface was moving.", "The man had a different style.", "The man was ahead of her.", "He offered the pig for so little money."], correctAnswer: "The surface was moving.", explanation: "Trong bài ghi 'Beth looked at the bag's surface. It was moving.' (Bề mặt chiếc túi đang chuyển động)." },
  { id: "25", content: "5. When did the memory of the cat come back to Beth?", options: ["When she went to the section's center", "When she looked at the bag's surface", "When the judge asked for evidence", "Later, when the man returned to trick more people"], correctAnswer: "Later, when the man returned to trick more people", explanation: "Trong bài ghi 'Later, the man returned to trick more people. Beth saw him and the memory of the cat came back.'." }
];

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 30",
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
          id: "sec1_wordlist",
          title: "Exercise 1: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: questions1
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 2: Check the better response to each question.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: questions2
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit30_story.png",
      sections: [
        {
          id: "sec3",
          title: "Answer the questions based on the story.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: storyQuestions
        }
      ]
    }
  ]
};

fs.writeFileSync('./unit30.json', JSON.stringify(json, null, 2));
console.log('Successfully wrote unit30.json');
