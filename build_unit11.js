const fs = require('fs');

const words = [
  { word: 'admission', pron: '[ədmíʃən]', pos: 'n.', def: 'Admission is the act of allowing to enter a place.', ex: 'The admission ticket to the movie was $5.' },
  { word: 'astronomy', pron: '[əstrɑ́nəmi]', pos: 'n.', def: 'Astronomy is the study of the stars and planets.', ex: 'Harold loved watching the stars, so he decided to study astronomy.' },
  { word: 'blame', pron: '[bleim]', pos: 'v.', def: 'To blame someone for something bad is to say they did it.', ex: 'My mom blamed me for something I didn’t do.' },
  { word: 'chemistry', pron: '[kémistri]', pos: 'n.', def: 'Chemistry the study of and reaction to substances.', ex: 'In chemistry class, the professor taught us about chemical reactions.' },
  { word: 'despite', pron: '[dispáit]', pos: 'prep.', def: 'If something happens despite what you do, it happens anyway.', ex: 'We still played the game despite the cold weather.' },
  { word: 'dinosaur', pron: '[dáinəsɔ̀:r]', pos: 'n.', def: 'A dinosaur is a very big animal that lived millions of years ago.', ex: 'I like to see the dinosaur bones at the museum.' },
  { word: 'exhibit', pron: '[igzíbit]', pos: 'n.', def: 'An exhibit is a display of interesting things.', ex: 'There was an animal exhibit at the fair.' },
  { word: 'fame', pron: '[feim]', pos: 'n.', def: 'Fame is reputation one has gained among the public.', ex: 'He had fame and fortune, but he was not happy.' },
  { word: 'forecast', pron: '[fɔ́:rkæ̀st]', pos: 'n.', def: 'A forecast is an idea about what the weather will be like in the future.', ex: 'The forecast says that it will rain all week.' },
  { word: 'genius', pron: '[dʒí:njəs]', pos: 'n.', def: 'A genius is a very smart person.', ex: 'Since she was a genius, she easily passed all of her school exams.' },
  { word: 'gentle', pron: '[dʒéntl]', pos: 'adj.', def: 'Someone who is gentle is kind and calm.', ex: 'He is very gentle with the baby.' },
  { word: 'geography', pron: '[dʒiɑ́grəfi]', pos: 'n.', def: 'Geography is the study of where things are.', ex: 'I had to draw a map for geography class.' },
  { word: 'interfere', pron: '[ìntərfíər]', pos: 'v.', def: 'To interfere is to cause problems and keep something from happening.', ex: 'My little sister always interferes when I’m trying to study.' },
  { word: 'lightly', pron: '[láitli]', pos: 'adv.', def: 'To do something lightly is to not push very hard.', ex: 'Draw lightly so you do not tear your paper.' },
  { word: 'principal', pron: '[prínsəpəl]', pos: 'n.', def: 'A principal is a person in charge of a school.', ex: 'My school’s principal can be very strict with the rules.' },
  { word: 'row', pron: '[rou]', pos: 'n.', def: 'A row is a line of things.', ex: 'James put all of his toy soldiers into neat rows.' },
  { word: 'shelf', pron: '[ʃelf]', pos: 'n.', def: 'A shelf is a place on a wall where you put things.', ex: 'I keep my clothes on a shelf in my closet.' },
  { word: 'spite', pron: '[spait]', pos: 'n.', def: 'If you do something out of spite, you want to be mean.', ex: 'He snuck into his sister’s room and stole her bag out of spite.' },
  { word: 'super', pron: '[sú:pər]', pos: 'adj.', def: 'Super means really good.', ex: 'My dad said I did a super job cleaning the house.' },
  { word: 'wet', pron: '[wet]', pos: 'adj.', def: 'If something is wet, it has water on it.', ex: 'Since my dog was wet, he tried to shake all the water off his body.' }
];

const storyTitle = 'Dinosaur Drawings';
const storyParagraphs = [
  'It was the worst morning ever. When Carl woke up, he realized that he didn’t do his <b>astronomy</b> and <b>chemistry</b> homework. Also, the <b>forecast</b> called for rain and that would affect baseball practice. Suddenly, his mother yelled, “Take out the garbage right now!” When Carl returned from taking the garbage outside, he was all <b>wet</b>. “What a terrible day,” he said.',
  'He walked to class. He put his umbrella on the <b>shelf</b> and sat in the third <b>row</b>. But the teacher asked why Carl’s umbrella was on the floor. He told her not to <b>blame</b> him. But she sent him to the <b>principal</b> out of <b>spite</b>.',
  'Next, he took a <b>geography</b> test. <b>Despite</b> studying, Carl didn’t know the answers. He started drawing <b>lightly</b> on his paper.',
  'Carl drew a huge <b>dinosaur</b>. What if it were real? He saw it in his mind. Carl’s class said he was a <b>genius</b> for having a <b>dinosaur</b>. It could <b>interfere</b> with math class, too! Soon, Carl’s <b>fame</b> spread through school.',
  'He taught his <b>dinosaur</b> to be very <b>gentle</b> and put it on <b>exhibit</b>. But <b>admission</b> would only be given to those classmates who paid him a fee. His idea was <b>super</b>.',
  '“It’s time to turn in your tests,” the teacher said. Carl looked at his paper. As he was dreaming in class, he hadn’t finished the test!'
];

// Combine words into HTML format
const wordsHtmlList = words.map(w => `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`).join('');

const part1Content = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit11_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit11_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">${wordsHtmlList}</div></div></div>`;

const paragraphsHtml = storyParagraphs.map(p => `<p style="margin-bottom: 1rem;">${p}</p>`).join('');
const part2Content = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">${storyTitle}</h1>${paragraphsHtml}</div>`;

const ex2 = {
  id: "sec2_wordlist",
  title: "Exercise 2: Check the sentence with the bolded word that makes better sense.",
  content: "",
  questionType: "Trắc nghiệm",
  questions: [
    {
      id: "1",
      content: "1.",
      options: ["a. We learned about grammar in astronomy class.", "b. Do not interfere when I am working."],
      correctAnswer: "b. Do not interfere when I am working.",
      explanation: "interfere có nghĩa là xen vào, cản trở. astronomy là thiên văn học, không học ngữ pháp."
    },
    {
      id: "2",
      content: "2.",
      options: ["a. It was very kind of him to spite his sister.", "b. Which shelf should I put this on?"],
      correctAnswer: "b. Which shelf should I put this on?",
      explanation: "shelf là cái kệ. spite là ác ý."
    },
    {
      id: "3",
      content: "3.",
      options: ["a. Do you have a shelf in your yard?", "b. In astronomy class, I learned about the Solar System."],
      correctAnswer: "b. In astronomy class, I learned about the Solar System.",
      explanation: "astronomy học về hệ mặt trời."
    },
    {
      id: "4",
      content: "4.",
      options: ["a. He drank all the milk in the fridge to spite me.", "b. Mrs. Joyner is a strict principal, but she is actually very nice."],
      correctAnswer: "b. Mrs. Joyner is a strict principal, but she is actually very nice.",
      explanation: "The answer key states Exercise 2 Q4 is b."
    },
    {
      id: "5",
      content: "5.",
      options: ["a. The loud music interferes with my concentration.", "b. It is against his principals to be dishonest."],
      correctAnswer: "a. The loud music interferes with my concentration.",
      explanation: "interfere nghĩa là làm cản trở. principal ở câu b bị sai chính tả so với principles."
    }
  ]
};

const ex3 = {
  id: "sec3_wordlist",
  title: "Exercise 3: Choose the word that is a better fit for each sentence.",
  content: "",
  questionType: "Trắc nghiệm",
  questions: [
    {
      id: "6",
      content: "1. Oil and water do not have a good ______ together. / We should go ______ the weather.",
      options: ["chemistry / despite", "despite / chemistry"],
      correctAnswer: "chemistry / despite",
      explanation: "chemistry: hóa học/sự hòa hợp. despite: mặc dù."
    },
    {
      id: "7",
      content: "2. I wanted to see the bird ______. / My daughter has gained ______ to an Ivy League university.",
      options: ["admission / exhibit", "exhibit / admission"],
      correctAnswer: "exhibit / admission",
      explanation: "exhibit: cuộc triển lãm. admission: sự nhận vào."
    },
    {
      id: "8",
      content: "3. I wish I could see a real ______ at the zoo. / I learned about a South American country in my ______ book.",
      options: ["geography / dinosaur", "dinosaur / geography"],
      correctAnswer: "dinosaur / geography",
      explanation: "dinosaur: khủng long. geography: địa lý."
    },
    {
      id: "9",
      content: "4. Be very ______ with the old dishes. / ______ push the dirt in around the flowers.",
      options: ["lightly / gentle", "gentle / lightly"],
      correctAnswer: "gentle / lightly",
      explanation: "gentle: nhẹ nhàng. lightly: một cách nhẹ nhàng."
    },
    {
      id: "10",
      content: "5. I don’t know if I would enjoy ______. / My son is a ______.",
      options: ["genius / fame", "fame / genius"],
      correctAnswer: "fame / genius",
      explanation: "fame: sự nổi tiếng. genius: thiên tài."
    }
  ]
};

const readingComp = {
  id: "sec4_reading",
  title: "Answer the questions.",
  content: "",
  questionType: "Trắc nghiệm",
  questions: [
    {
      id: "11",
      content: "1. What is this story about?",
      options: [
        "a. A wet classroom",
        "b. A boy who is a genius",
        "c. A bell that keeps ringing",
        "d. A day that was not super"
      ],
      correctAnswer: "d. A day that was not super",
      explanation: "The story starts with 'It was the worst morning ever' and describes Carl's bad day."
    },
    {
      id: "12",
      content: "2. What does Carl think his dinosaur can do?",
      options: [
        "a. Make money for him on admission fees",
        "b. Interfere with taking out the garbage",
        "c. Take the blame for failing geography",
        "d. Reach things on the top shelf"
      ],
      correctAnswer: "a. Make money for him on admission fees",
      explanation: "Carl thinks 'admission would only be given to those classmates who paid him a fee.'"
    },
    {
      id: "13",
      content: "3. What did Carl do?",
      options: [
        "a. Break a jar at breakfast",
        "b. Draw lightly on his test paper",
        "c. Forget his hat on the bus",
        "d. Stay after school for being late"
      ],
      correctAnswer: "b. Draw lightly on his test paper",
      explanation: "The story says 'He started drawing lightly on his paper.'"
    },
    {
      id: "14",
      content: "4. Despite Carl studying for his test, what happened?",
      options: [
        "a. His teacher was not gentle with him.",
        "b. He had to sit in the last row.",
        "c. The exhibit did not earn him any fame.",
        "d. He did not do well on his geography test."
      ],
      correctAnswer: "d. He did not do well on his geography test.",
      explanation: "The story says 'Despite studying, Carl didn’t know the answers.'"
    }
  ]
};

const output = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 11",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: part1Content,
      sections: [ ex2, ex3 ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: part2Content,
      imageUrl: "/unit11_story.png",
      sections: [ readingComp ]
    }
  ]
};

fs.writeFileSync('unit11.json', JSON.stringify(output, null, 2));
console.log('Successfully wrote unit11.json');
