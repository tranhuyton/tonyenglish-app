const fs = require('fs');
const path = require('path');

const words = [
  { word: 'aim', ipa: '[eɪm]', type: 'n.', def: 'An aim is a goal someone wants to make happen.', ex: 'My aim is to become a helicopter pilot.' },
  { word: 'attach', ipa: '[əˈtætʃ]', type: 'v.', def: 'To attach is to put two things together.', ex: 'I attached the socks to the clothesline to dry.' },
  { word: 'bet', ipa: '[bet]', type: 'v.', def: 'To bet is to risk money on the result of a game or a business.', ex: 'How much will you bet that your horse will win?' },
  { word: 'carriage', ipa: '[ˈkærɪdʒ]', type: 'n.', def: 'A carriage is a vehicle pulled by a horse.', ex: 'We took a carriage ride in the park.' },
  { word: 'classic', ipa: '[ˈklæsɪk]', type: 'adj.', def: 'If something is classic, it is typical.', ex: 'The athlete made a classic mistake-he started running too soon.' },
  { word: 'commute', ipa: '[kəˈmjuːt]', type: 'v.', def: 'To commute is to travel a long distance to get to work.', ex: 'I usually commute to work on the train.' },
  { word: 'confirm', ipa: '[kənˈfɜːrm]', type: 'v.', def: 'To confirm is to make sure something is correct.', ex: 'Winning the game confirmed that James was a good player.' },
  { word: 'criticize', ipa: '[ˈkrɪtɪsaɪz]', type: 'v.', def: 'To criticize is to say you do not like someone or something.', ex: 'He criticized his wife for spending too much money.' },
  { word: 'differ', ipa: '[ˈdɪfər]', type: 'v.', def: 'To differ is to not be the same as another person or thing.', ex: 'I differ from my brother: he is short, while I am tall.' },
  { word: 'expense', ipa: '[ɪkˈspens]', type: 'n.', def: 'An expense is the money that people spend on something.', ex: 'She wrote down all the expenses for her trip.' },
  { word: 'formal', ipa: '[ˈfɔːrməl]', type: 'adj.', def: 'If something is formal, it is done in an official way.', ex: 'It was a formal dinner, so we wore our best clothes.' },
  { word: 'height', ipa: '[haɪt]', type: 'n.', def: 'Height is how tall someone or something is.', ex: 'My height is 168 centimeters.' },
  { word: 'invent', ipa: '[ɪnˈvent]', type: 'v.', def: 'To invent something is to create something that never existed before.', ex: 'My grandfather has invented some interesting things.' },
  { word: 'junior', ipa: '[ˈdʒuːniər]', type: 'adj.', def: 'If someone is junior in their job, they do not have a lot of power.', ex: 'When she started at the company, she was only a junior manager.' },
  { word: 'labor', ipa: '[ˈleɪbər]', type: 'n.', def: 'Labor is the act of doing or making something.', ex: 'Building the house took a lot of labor.' },
  { word: 'mechanic', ipa: '[məˈkænɪk]', type: 'n.', def: 'A mechanic is someone who fixes vehicles or machines.', ex: 'We took the car to the mechanic to be fixed.' },
  { word: 'prime', ipa: '[praɪm]', type: 'adj.', def: 'If something is prime, it is the most important one.', ex: 'Dirty air is a prime cause of illness.' },
  { word: 'shift', ipa: '[ʃɪft]', type: 'v.', def: 'To shift to something is to move into a new place or direction.', ex: 'He shifted to the other side of the table to eat his breakfast.' },
  { word: 'signal', ipa: '[ˈsɪɡnəl]', type: 'n.', def: 'A signal is a sound or action that tells someone to do something.', ex: 'The coach blew his whistle as a signal to begin the game.' },
  { word: 'sincere', ipa: '[sɪnˈsɪr]', type: 'adj.', def: 'When people are sincere, they tell the truth.', ex: 'He sounded sincere when he apologized to me.' }
];

let wordHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit17_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit17_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.ipa}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordHtml += `</div></div></div>`;

const storyText = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Henry Ford’s Famous Car</h1><p style="margin-bottom: 1rem;">My name is Henry Ford, and I <b>invented</b> a car called the Model T. I used to watch <b>carriages</b> on the streets. They fascinated me. Then I got a job as a <b>junior</b> <b>mechanic</b>. My father <b>criticized</b> me. He wanted me to run the farm. But I did not <b>shift</b> my plans.</p><p style="margin-bottom: 1rem;">Then I worked for the Detroit Auto Company. But I wanted to make cars using less <b>labor</b>. That way, there would be fewer <b>expenses</b>. I started the Ford Motor Company in 1903. At first, the company did not do well. But many people were <b>betting</b> on my success. I also had a <b>sincere</b> <b>aim</b> to make a car that anybody could buy.</p><p style="margin-bottom: 1rem;">Then, in 1908, I introduced the Model-T in a <b>formal</b> ceremony. It <b>confirmed</b> that I was right: it was possible to build a car my way!</p><p style="margin-bottom: 1rem;">The Model T <b>differed</b> from other vehicles. Workers could <b>attach</b> different parts for cars or trucks. This saved time. One Model T could be put together in 93 minutes. All of them had the same <b>classic</b> design. They were all the same size and <b>height</b>. The <b>prime</b> reason for doing this was to save money.</p><p style="margin-bottom: 1rem;">Over 19 years, I sold over 15 million Model Ts. This sent a <b>signal</b> to other companies. People would buy cars to <b>commute</b> to work if the price was low enough.</p></div>`;

const contentJson = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 17",
    "category": "exercise",
    "timeLimit": 0
  },
  "parts": [
    {
      "id": "part1",
      "title": "Word List",
      "content": wordHtml,
      "sections": [
        {
          "id": "sec1_wordlist",
          "title": "Part A: Choose the right word for the given definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "1",
              "content": "1. to create something for the first time",
              "options": ["aim", "signal", "mechanic", "invent"],
              "correctAnswer": "invent",
              "explanation": "invent có nghĩa là tạo ra thứ gì đó lần đầu tiên."
            },
            {
              "id": "2",
              "content": "2. most important",
              "options": ["differ", "junior", "prime", "commute"],
              "correctAnswer": "prime",
              "explanation": "prime có nghĩa là quan trọng nhất."
            },
            {
              "id": "3",
              "content": "3. to move",
              "options": ["attach", "shift", "bet", "confirm"],
              "correctAnswer": "shift",
              "explanation": "shift có nghĩa là di chuyển."
            },
            {
              "id": "4",
              "content": "4. cost",
              "options": ["carriage", "expense", "height", "labor"],
              "correctAnswer": "expense",
              "explanation": "expense có nghĩa là chi phí."
            },
            {
              "id": "5",
              "content": "5. typical",
              "options": ["classic", "criticize", "formal", "sincere"],
              "correctAnswer": "classic",
              "explanation": "classic có nghĩa là điển hình."
            }
          ]
        },
        {
          "id": "sec2_wordlist",
          "title": "Part B: Check (V) the sentence with the bolded word that makes the better sense.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "6",
              "content": "1. a. It is a good idea to bet your money on silly things.\nb. You should go to a mechanic if you have a problem with your car.",
              "options": ["a", "b"],
              "correctAnswer": "b",
              "explanation": "mechanic (thợ cơ khí) sửa xe, đây là lựa chọn hợp lý."
            },
            {
              "id": "7",
              "content": "2. a. Drivers use signals to make their cars go faster.\nb. You should attach a stamp to a letter before you mail it.",
              "options": ["a", "b"],
              "correctAnswer": "b",
              "explanation": "attach a stamp (dán tem) là hành động đúng trước khi gửi thư."
            },
            {
              "id": "8",
              "content": "3. a. If you and your date differ too much, you might not like each other.\nb. When you confirm the results of the test, you make them better.",
              "options": ["a", "b"],
              "correctAnswer": "a",
              "explanation": "differ (khác biệt): nếu hai người khác biệt quá nhiều, có thể họ không thích nhau."
            },
            {
              "id": "9",
              "content": "4. a. It is O.K. to wear sandals to a formal party.\nb. Teachers often criticize lazy students.",
              "options": ["a", "b"],
              "correctAnswer": "b",
              "explanation": "criticize (chỉ trích): giáo viên thường phê bình học sinh lười biếng."
            },
            {
              "id": "10",
              "content": "5. a. People must pay attention to signals when they are driving.\nb. When you visit a mechanic they will sell you a new car.",
              "options": ["a", "b"],
              "correctAnswer": "a",
              "explanation": "signals (tín hiệu): người lái xe phải chú ý đến các tín hiệu."
            },
            {
              "id": "11",
              "content": "6. a. You should wear nice clothing if you go to a formal event.\nb. Good friends like to criticize each other.",
              "options": ["a", "b"],
              "correctAnswer": "a",
              "explanation": "formal event (sự kiện trang trọng): nên mặc đồ đẹp."
            },
            {
              "id": "12",
              "content": "7. a. Husbands and wives who differ are often very busy people.\nb. If you commute to work, you have to travel a certain distance.",
              "options": ["a", "b"],
              "correctAnswer": "b",
              "explanation": "commute (đi làm xa): đi lại một khoảng cách nhất định."
            },
            {
              "id": "13",
              "content": "8. a. It is a good idea to confirm your plans before you travel.\nb. If you attach a large sign to your door, no one will see it.",
              "options": ["a", "b"],
              "correctAnswer": "a",
              "explanation": "confirm (xác nhận): nên xác nhận kế hoạch trước khi đi."
            },
            {
              "id": "14",
              "content": "9. a. If your aim is to learn how to swim, you must get in the water.\nb. Everyone commutes in math class.",
              "options": ["a", "b"],
              "correctAnswer": "a",
              "explanation": "aim (mục tiêu): nếu mục tiêu là học bơi, phải xuống nước."
            },
            {
              "id": "15",
              "content": "10. a. People who have an aim to succeed are very lazy.\nb. When you bet money, you might lose it.",
              "options": ["a", "b"],
              "correctAnswer": "b",
              "explanation": "bet (cá cược): khi cá cược bạn có thể bị mất tiền."
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": storyText,
      "imageUrl": "/unit17_story.png",
      "sections": [
        {
          "id": "sec3",
          "title": "Answer the questions based on the story.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "16",
              "content": "1. What is this story about?",
              "options": [
                "a. How Ford attached cars and engines",
                "b. How Ford aimed to build a better car",
                "c. Why Ford shifted away from carriages",
                "d. Why Ford bet on the gasoline engine"
              ],
              "correctAnswer": "b. How Ford aimed to build a better car",
              "explanation": "Câu chuyện kể về cách Ford nhắm đến việc tạo ra một chiếc xe hơi tốt hơn."
            },
            {
              "id": "17",
              "content": "2. How did the Model T change other car companies?",
              "options": [
                "a. It confirmed that their expenses were large.",
                "b. It made workers criticize their bosses about their labor.",
                "c. It created a signal for them to start making cheaper cars.",
                "d. It forced car companies to bet on Ford’s success."
              ],
              "correctAnswer": "c. It created a signal for them to start making cheaper cars.",
              "explanation": "Nó tạo ra một tín hiệu cho họ bắt đầu sản xuất xe giá rẻ hơn."
            },
            {
              "id": "18",
              "content": "3. In paragraph 1, we can infer that_______",
              "options": [
                "a. Ford had a very formal childhood",
                "b. Ford differed in thought from his father",
                "c. Ford was not of great height",
                "d. Ford’s father was sincere"
              ],
              "correctAnswer": "b. Ford differed in thought from his father",
              "explanation": "Ford khác biệt trong suy nghĩ so với cha mình."
            },
            {
              "id": "19",
              "content": "4. According to the passage, all the following are true EXCEPT___",
              "options": [
                "a. the Model-T had a classic design",
                "b. people would use cars to commute if they weren’t expensive",
                "c. Ford worked as a junior mechanic",
                "d. the first vehicle from the Ford Motor Company was a truck"
              ],
              "correctAnswer": "d. the first vehicle from the Ford Motor Company was a truck",
              "explanation": "Mệnh đề d là sai vì xe đầu tiên không phải là xe tải."
            },
            {
              "id": "20",
              "content": "5. What was the prime reason for making the Model T with one design?",
              "options": [
                "a. To save money.",
                "b. To make it go faster.",
                "c. To save time on labor.",
                "d. To make it look classic."
              ],
              "correctAnswer": "a. To save money.",
              "explanation": "Lý do chính yếu là để tiết kiệm tiền."
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync(path.join(__dirname, 'unit17.json'), JSON.stringify(contentJson, null, 2));
console.log('Successfully wrote unit17.json');
