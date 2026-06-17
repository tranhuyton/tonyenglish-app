const fs = require('fs');

const words = [
  { word: "appear", phonetics: "[əˈpɪər]", type: "v.", def: "To appear is to seem.", example: "She appeared to be sad. She was crying." },
  { word: "base", phonetics: "[beɪs]", type: "n.", def: "The base is the bottom of something.", example: "The base of the table has three legs." },
  { word: "brain", phonetics: "[breɪn]", type: "n.", def: "The brain is the organ in your head that lets you think.", example: "You must use your brain to solve the problem." },
  { word: "career", phonetics: "[kəˈrɪər]", type: "n.", def: "A career is a job that you do for a large part of your life.", example: "He was in the hospitality business for most of his career." },
  { word: "clerk", phonetics: "[klɜːrk]", type: "n.", def: "A clerk is a type of worker. Clerks in a store help customers.", example: "The clerk added up her bill for the groceries." },
  { word: "effort", phonetics: "[ˈefərt]", type: "n.", def: "Effort is hard work or an attempt to do something.", example: "He always puts a lot of effort into his studies." },
  { word: "enter", phonetics: "[ˈentər]", type: "v.", def: "To enter a place is to go into it.", example: "Two guards greeted me as I entered the front door." },
  { word: "excellent", phonetics: "[ˈeksələnt]", type: "adj.", def: "When something is excellent, it is very good.", example: "I got an excellent score on my school test." },
  { word: "hero", phonetics: "[ˈhɪəroʊ]", type: "n.", def: "A hero is a brave person who does things to help others.", example: "To children, the man in the blue and red costume was a real hero." },
  { word: "hurry", phonetics: "[ˈhɜːri]", type: "v.", def: "To hurry is to do something quickly.", example: "I hurried home on my bike." },
  { word: "inform", phonetics: "[ɪnˈfɔːrm]", type: "v.", def: "To inform someone is to tell them about something.", example: "I called and informed her about my idea." },
  { word: "later", phonetics: "[ˈleɪtər]", type: "adv.", def: "Later means after the present, expected, or usual time.", example: "She missed the train, so she'll arrive a little later than expected." },
  { word: "leave", phonetics: "[liːv]", type: "v.", def: "To leave means to go away from someone or something.", example: "He packed his bag and was ready to leave for home." },
  { word: "locate", phonetics: "[ˈloʊkeɪt]", type: "v.", def: "To locate something is to find it.", example: "I could not locate my keys in the house." },
  { word: "nurse", phonetics: "[nɜːrs]", type: "n.", def: "A nurse is a person who helps sick people in the hospital.", example: "A nurse helped me get better." },
  { word: "operation", phonetics: "[ˌɑːpəˈreɪʃn]", type: "n.", def: "An operation is when a doctor replaces or removes something in the body.", example: "The operation on my arm was a success." },
  { word: "pain", phonetics: "[peɪn]", type: "n.", def: "Pain is the feeling that you have when you are hurt.", example: "His head was full of pain." },
  { word: "refuse", phonetics: "[rɪˈfjuːz]", type: "v.", def: "To refuse something is to say \"no\" to it.", example: "The dog refused to play with the cat." },
  { word: "though", phonetics: "[ðoʊ]", type: "conj.", def: "Though is used when the second idea makes the first seem surprising.", example: "Though he was overweight, he liked to be active." },
  { word: "various", phonetics: "[ˈveriəs]", type: "adj.", def: "If something is various, there are many types of it.", example: "She owned shoes of various styles." }
];

let wordListHtml = '<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit21_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit21_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">';

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetics}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.example}</div></div></div>`;
});
wordListHtml += '</div></div></div>';

let readingHtml = `<div style="font-family: Arial, sans-serif; ">    <h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Katy, the Little Hero</h1>        <p style="margin-bottom: 1rem;">I first met 8-year-old Katy on a rainy afternoon. I was a <b>nurse</b> at a hospital. The <b>clerk</b> at the desk told me about Katy. She was there because she felt a lot of <b>pain</b>. The doctors <b>located</b> a problem at the <b>base</b> of her <b>brain</b>. I knew she was special, even before she got better. I'll always remember Katy as a <b>hero</b>.</p>    <p style="margin-bottom: 1rem;">When I <b>entered</b> Katy's room, she was not in her bed. She was in a chair next to Tommy, a little boy. <b>Though</b> Katy did not feel well, she was playing with Tommy and his toys. It took a lot of <b>effort</b> for her just to sit in the chair. But she played with Tommy because it made him happy.</p>    <p style="margin-bottom: 1rem;">Katy was always smiling and never <b>appeared</b> to be in <b>pain</b>. She <b>refused</b> to just lie in bed. One day I found her painting a picture. <b>Later</b>, she gave it to one of the older patients. Another day she went outside to get flowers for another sick little girl. Katy made everyone smile.</p>    <p style="margin-bottom: 1rem;">The doctors <b>hurried</b> to fix the problem in Katy's <b>brain</b>. The <b>operation</b> was successful! The doctors <b>informed</b> the hospital staff of the good news. Katy was fine. She soon felt <b>excellent</b>. She got better and was able to <b>leave</b> the hospital a month <b>later</b>.</p>    <p style="margin-bottom: 1rem;">I have had a long <b>career</b> as a <b>nurse</b>. I have met many patients. However, I have never met another girl like Katy. Even after she got well, she still came to the hospital. She played <b>various</b> games with the young patients. She read many books to the older patients. Katy's kind heart helped her get better so quickly. She is a <b>hero</b> to me and everyone else at the hospital.</p></div>`;

const json = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 21",
    "category": "exercise",
    "timeLimit": 0
  },
  "parts": [
    {
      "id": "part1",
      "title": "Word List",
      "content": wordListHtml,
      "sections": [
        {
          "id": "sec1",
          "title": "Fill in the blanks with the right words from the word bank. (locate, hero, pain, hurried, clerk)",
          "content": "",
          "questionType": "Điền từ",
          "questions": [
            {
              "id": "1",
              "content": "I went to the video store last night. I wanted to (app[1]) a DVD. I didn't know the name of the movie, so I told the (app[2]) what it was about. I told her there was a (app[3]) who could fly and nothing caused him (app[4]). She went to the shelf and brought it to me. Then I (app[5]) home to watch it.",
              "blanks": [
                { "id": "1", "answer": "locate" },
                { "id": "2", "answer": "clerk" },
                { "id": "3", "answer": "hero" },
                { "id": "4", "answer": "pain" },
                { "id": "5", "answer": "hurried" }
              ]
            }
          ]
        },
        {
          "id": "sec2",
          "title": "Check the one that suits the blank naturally.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "2",
              "content": "1. When I went to the hospital,____________.",
              "options": ["the nurse gave me medicine", "all the doctors and nurses will leave"],
              "correctAnswer": "the nurse gave me medicine",
              "explanation": "the nurse gave me medicine suits the blank."
            },
            {
              "id": "3",
              "content": "2. He arrived on time, but Sarah won't be here ___________",
              "options": ["until much later", "leaves in the morning"],
              "correctAnswer": "until much later",
              "explanation": "until much later suits the blank."
            },
            {
              "id": "4",
              "content": "3. I really like that writer. He wrote an____________.",
              "options": ["effort of a story", "excellent book"],
              "correctAnswer": "excellent book",
              "explanation": "excellent book suits the blank."
            },
            {
              "id": "5",
              "content": "4. After I dropped the book on my foot, ____________.",
              "options": ["I was in pain", "I hurried home"],
              "correctAnswer": "I was in pain",
              "explanation": "I was in pain suits the blank."
            },
            {
              "id": "6",
              "content": "5. He did not want to go to the party. He",
              "options": ["appeared ready to go", "refused to get into the car"],
              "correctAnswer": "refused to get into the car",
              "explanation": "refused to get into the car suits the blank."
            }
          ]
        },
        {
          "id": "sec3",
          "title": "Check the sentence with the bolded word that makes better sense.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "7",
              "content": "1.",
              "options": ["Because the base of the lamp was broken, it could not stand up.", "I decided to leave early so that I could be late."],
              "correctAnswer": "Because the base of the lamp was broken, it could not stand up.",
              "explanation": "a is correct."
            },
            {
              "id": "8",
              "content": "2.",
              "options": ["The roof was at the base of the house.", "I had an operation to fix my broken nose."],
              "correctAnswer": "I had an operation to fix my broken nose.",
              "explanation": "b is correct."
            },
            {
              "id": "9",
              "content": "3.",
              "options": ["The various movies were all the same.", "I like dogs, though I don't like most animals."],
              "correctAnswer": "I like dogs, though I don't like most animals.",
              "explanation": "b is correct."
            },
            {
              "id": "10",
              "content": "4.",
              "options": ["I will leave early in the morning to catch my plane.", "My friends and I decided to throw an operation for my sister."],
              "correctAnswer": "I will leave early in the morning to catch my plane.",
              "explanation": "a is correct."
            },
            {
              "id": "11",
              "content": "5.",
              "options": ["Though I was rich, I bought a lot of cars.", "I made an effort to get the job done."],
              "correctAnswer": "I made an effort to get the job done.",
              "explanation": "b is correct."
            },
            {
              "id": "12",
              "content": "6.",
              "options": ["He never used his brain when he faced problems!", "The job appeared very quickly."],
              "correctAnswer": "He never used his brain when he faced problems!",
              "explanation": "a is correct."
            },
            {
              "id": "13",
              "content": "7.",
              "options": ["I entered the house through the door.", "I threw the effort with all my might."],
              "correctAnswer": "I entered the house through the door.",
              "explanation": "a is correct."
            },
            {
              "id": "14",
              "content": "8.",
              "options": ["She appeared very happy on her birthday.", "People use their brains to exercise."],
              "correctAnswer": "She appeared very happy on her birthday.",
              "explanation": "a is correct."
            },
            {
              "id": "15",
              "content": "9.",
              "options": ["I informed him of the new rules.", "I entered out of the room."],
              "correctAnswer": "I informed him of the new rules.",
              "explanation": "a is correct."
            },
            {
              "id": "16",
              "content": "10.",
              "options": ["The rock informed me that I was too heavy.", "There were various things to do at the event."],
              "correctAnswer": "There were various things to do at the event.",
              "explanation": "b is correct."
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": readingHtml,
      "imageUrl": "/unit21_story.png",
      "sections": [
        {
          "id": "sec4",
          "title": "Reading Comprehension",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "17",
              "content": "1. What is this story about?",
              "options": ["A clerk with a brain problem", "A little girl who is a hero", "A little girl who wants a career as a nurse", "Tommy and his various toys"],
              "correctAnswer": "A little girl who is a hero",
              "explanation": "The correct answer is b."
            },
            {
              "id": "18",
              "content": "2. Why does everyone like Katy?",
              "options": ["She does good things, even though she is in pain.", "She enters the hospital and saves a patient's life.", "She has a problem at the base of her brain.", "She hurries to help the clerk at his desk."],
              "correctAnswer": "She does good things, even though she is in pain.",
              "explanation": "The correct answer is a."
            },
            {
              "id": "19",
              "content": "3. Which of the following is true at the end of the story?",
              "options": ["Katy refuses to go back to the hospital.", "Katy makes an effort to become a nurse.", "Katy feels excellent but goes back to the hospital to see other patients.", "Katy informs other patients of how to get better."],
              "correctAnswer": "Katy feels excellent but goes back to the hospital to see other patients.",
              "explanation": "The correct answer is c."
            },
            {
              "id": "20",
              "content": "4. How did the nurse know Katy did not feel well?",
              "options": ["Katy appeared to be sad.", "Katy had to make an effort just to sit in a chair.", "The nurse located a problem in Katy's brain.", "The nurse asked Katy how she felt."],
              "correctAnswer": "Katy had to make an effort just to sit in a chair.",
              "explanation": "The correct answer is b."
            },
            {
              "id": "21",
              "content": "5. What does Katy do to help people?",
              "options": ["Katy played games, read books, and got flowers for patients.", "Katy performed operations.", "Katy cleaned the rooms.", "Katy bought them food."],
              "correctAnswer": "Katy played games, read books, and got flowers for patients.",
              "explanation": "From the passage."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit21.json', JSON.stringify(json, null, 2));
