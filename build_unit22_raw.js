const fs = require('fs');

const words = [
  { word: "accommodate", pron: "[əkɑ́mədeit]", type: "v.", def: "To accommodate is to have enough room.", ex: "The meeting room can accommodate nine people.", icon: "🏢" },
  { word: "circus", pron: "[sə́:rkəs]", type: "n.", def: "A circus is a traveling show with animals and people.", ex: "I like to go to the circus to see the animals do tricks.", icon: "🎪" },
  { word: "coincide", pron: "[ˌkoʊɪnˈsaɪd]", type: "v.", def: "If two things coincide, they happen at the same time.", ex: "My birthday coincides with Christmas.", icon: "📅" },
  { word: "commission", pron: "[kəmíʃən]", type: "v.", def: "To commission someone to do something is to pay them to do it.", ex: "The artist was commissioned to create a picture.", icon: "💵" },
  { word: "dose", pron: "[dous]", type: "n.", def: "A dose is a certain amount of medicine that you take at one time.", ex: "My mother gave me a dose of medicine before I went to bed.", icon: "💊" },
  { word: "dye", pron: "[dai]", type: "v.", def: "To dye something is to make it a certain color by using a special chemical.", ex: "Valery got her hair dyed at the salon yesterday.", icon: "🎨" },
  { word: "extent", pron: "[ikstént]", type: "n.", def: "The extent of something is how large, important, or serious it is.", ex: "He ate to such an extent that he became overweight.", icon: "📏" },
  { word: "gender", pron: "[dʒéndər]", type: "n.", def: "Gender is a category that describes being either a boy or a girl.", ex: "Do you know the gender of her new baby?", icon: "🚻" },
  { word: "headline", pron: "[hédlain]", type: "n.", def: "A headline is the title of a newspaper story.", ex: "The headline on the front page was about the economy.", icon: "📰" },
  { word: "informal", pron: "[infɔ́:rməl]", type: "adj.", def: "When something is informal, it is not official.", ex: "They had an informal meeting to talk about their experiences.", icon: "🤝" },
  { word: "inquire", pron: "[inkwáiər]", type: "v.", def: "To inquire about something is to ask about it.", ex: "Dad called to inquire about the price of tickets for the show.", icon: "❓" },
  { word: "messenger", pron: "[mésəndʒər]", type: "n.", def: "A messenger is one who carries information from one place to another.", ex: "The messenger delivered an important document to the office.", icon: "📩" },
  { word: "peer", pron: "[piər]", type: "v.", def: "To peer at something is to watch it carefully.", ex: "She peered at people through the window.", icon: "👀" },
  { word: "portrait", pron: "[pɔ́:rtrit]", type: "n.", def: "A portrait is a painting or photograph of someone.", ex: "I saw many religious portraits when I went to the museum.", icon: "🖼️" },
  { word: "pose", pron: "[pouz]", type: "v.", def: "To pose is to stay in one place without moving.", ex: "The kids and their dog posed for a picture.", icon: "🧍" },
  { word: "ranch", pron: "[ræntʃ]", type: "n.", def: "A ranch is a large farm where animals are kept.", ex: "My uncle has many horses on his ranch.", icon: "🐎" },
  { word: "steer", pron: "[stiər]", type: "v.", def: "To steer something is to control where it goes.", ex: "He steered the go-cart around the track.", icon: "🎡" },
  { word: "stripe", pron: "[straip]", type: "n.", def: "A stripe is a thick line.", ex: "The flag of the United States has red and white stripes.", icon: "🦓" },
  { word: "tame", pron: "[teim]", type: "adj.", def: "When an animal is tame, it is not afraid to be near people.", ex: "The tame bird rested on his hand.", icon: "🕊️" },
  { word: "tempt", pron: "[tempt]", type: "v.", def: "To tempt people is to offer them something they want but shouldn't have.", ex: "I wasn't hungry, but she tempted me with a piece of my favorite cake.", icon: "🍰" }
];

let wordsHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit22_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit22_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${w.icon}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordsHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Circus</h1><p style="margin-bottom: 1rem;">Ben was unhappy. He lived on a <b>ranch</b> near a small town, and he didn't have many friends. Then one day a <b>messenger</b> came to the <b>ranch</b>. He showed the <b>headline</b> in the town newspaper. The <b>circus</b> was coming to the town. It even <b>coincided</b> with Ben's birthday!</p><p style="margin-bottom: 1rem;">Ben was very excited as his father <b>steered</b> the car through the town. The <b>circus</b> couldn't <b>accommodate</b> all the people who wanted to see the show, but Ben had a ticket.</p><p style="margin-bottom: 1rem;">Ben <b>peered</b> at the activity around him. He watched people of both <b>genders</b> dance all around. They wore funny costumes, and their hair was <b>dyed</b> many different colors. Also, <b>tame</b> tigers with <b>stripes</b> on their fur did tricks. Outside, people could <b>commission</b> an <b>informal</b> <b>portrait</b>. They <b>posed</b> in front of a funny picture while an artist quickly drew them. Ben couldn't believe it. He was happier than he had ever been before.</p><p style="margin-bottom: 1rem;">That day, Ben knew what he wanted to do. He loved the <b>circus</b> to such an <b>extent</b> that he wanted to have his own <b>circus</b> when he grew older. Seeing the <b>circus</b> was like a <b>dose</b> of medicine for him. He wasn't unhappy anymore. He felt special. He <b>inquired</b> about what he needed to do to have his own <b>circus</b>. He studied hard and learned about business.</p><p style="margin-bottom: 1rem;">Ben worked very hard, and one day, he had his own <b>circus</b>. It was a great <b>circus</b>. People told him that he could be very rich. But he wasn't <b>tempted</b> by money. He just wanted to make children happy. He knew the <b>circus</b> had changed his life, and he wanted to do the same thing for others.</p></div>`;

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
          title: "Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. to have enough room", options: ["accommodate", "circus", "tame", "steer"], correctAnswer: "accommodate", explanation: "accommodate (cung cấp chỗ ở, có đủ chỗ)." },
            { id: "2", content: "2. to change the color of something", options: ["tempt", "dye", "stripe", "dose"], correctAnswer: "dye", explanation: "dye (nhuộm)." },
            { id: "3", content: "3. a category of being either a boy or a girl", options: ["wipe", "extent", "informal", "gender"], correctAnswer: "gender", explanation: "gender (giới tính)." },
            { id: "4", content: "4. the title of a newspaper story", options: ["pose", "headline", "ranch", "inquire"], correctAnswer: "headline", explanation: "headline (tiêu đề)." },
            { id: "5", content: "5. to pay someone to do something", options: ["portrait", "commission", "peer", "messenger"], correctAnswer: "commission", explanation: "commission (ủy thác, trả tiền để làm gì)." }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Part B: Choose the right definition for the given word.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "6", content: "1. inquire", options: ["to pay someone for something", "to ask about something", "to make someone want something", "not wild"], correctAnswer: "to ask about something", explanation: "inquire (hỏi, yêu cầu thông tin)." },
            { id: "7", content: "2. steer", options: ["a picture of someone", "to stay in one position", "a traveling show", "to control the direction of a car"], correctAnswer: "to control the direction of a car", explanation: "steer (điều khiển hướng)." },
            { id: "8", content: "3. stripe", options: ["a line", "a person who carries news", "an amount of medicine", "describes being either a boy or a girl"], correctAnswer: "a line", explanation: "stripe (sọc, đường viền)." },
            { id: "9", content: "4. extent", options: ["to have room for", "how much", "to change color", "a place with many animals"], correctAnswer: "how much", explanation: "extent (mức độ, phạm vi)." },
            { id: "10", content: "5. coincide", options: ["to happen at the same time", "not official", "to watch carefully", "the title of a news story"], correctAnswer: "to happen at the same time", explanation: "coincide (xảy ra cùng lúc)." }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 2: Choose the word that is a better fit for each blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "11", content: "1. The patient ______ if the doctor could help his shoulder pain. The doctor gave him a ______ of medication that would relieve the pain.", options: ["inquired / dose", "peered / pose"], correctAnswer: "inquired / dose", explanation: "inquire (hỏi), dose (liều thuốc)." },
            { id: "12", content: "2. The photographer ______ through the camera, but the picture didn’t seem right. So he asked the people to ______ differently.", options: ["peered / pose", "portrait / commissioned"], correctAnswer: "peered / pose", explanation: "peer (nhìn kỹ), pose (tạo dáng)." },
            { id: "13", content: "3. Her grandfather gave her a ______ that was painted when he was a boy. Her grandfather’s family had ______ a famous artist to do it.", options: ["portrait / commissioned", "accommodate / coincided"], correctAnswer: "portrait / commissioned", explanation: "portrait (chân dung), commission (ủy thác)." },
            { id: "14", content: "4. The day of the wedding ______ with an important baseball game. As a result, the hotels couldn’t ______ the extra guests.", options: ["coincided / accommodate", "circus / dyed"], correctAnswer: "coincided / accommodate", explanation: "coincide (xảy ra cùng lúc), accommodate (cung cấp chỗ ở)." },
            { id: "15", content: "5. The performers at the ______ had clothing that was ______ funny colors.", options: ["circus / dyed", "headline / extent"], correctAnswer: "circus / dyed", explanation: "circus (rạp xiếc), dye (nhuộm)." },
            { id: "16", content: "6. They didn’t understand the ______ of the damage until they saw the ______ that said that thousands of people had lost their homes in the storm.", options: ["extent / headline", "messenger / stripe"], correctAnswer: "extent / headline", explanation: "extent (mức độ), headline (tiêu đề)." },
            { id: "17", content: "7. The ______ carried the notes in a bag that had a long green ______ on the side.", options: ["messenger / stripe", "ranch / informal"], correctAnswer: "messenger / stripe", explanation: "messenger (người đưa thư), stripe (sọc)." },
            { id: "18", content: "8. The owner of the ______ had an ______ meeting with his employees to talk to them about the recent problems.", options: ["ranch / informal", "steering / gender"], correctAnswer: "ranch / informal", explanation: "ranch (nông trại), informal (thân mật)." },
            { id: "19", content: "9. I couldn’t tell the ______ of the person ______ the car because it was dark outside.", options: ["gender / steering", "tame / tempted"], correctAnswer: "gender / steering", explanation: "gender (giới tính), steer (điều khiển xe)." },
            { id: "20", content: "10. The trainer ______ the tiger with a treat, but the animal remained ______ in his place.", options: ["tempted / tame", "inquired / dose"], correctAnswer: "tempted / tame", explanation: "tempt (cám dỗ), tame (thuần hóa)." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit22_v3_story.png",
      sections: [
        {
          id: "sec4_reading",
          title: "Part A: Mark each statement T for true or F for false.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "21", content: "1. Ben was unhappy because he lived on a ranch near a small town and didn't have many friends.", options: ["T", "F"], correctAnswer: "T", explanation: "Đúng theo câu chuyện." },
            { id: "22", content: "2. Ben was tempted by money when he had his own circus.", options: ["T", "F"], correctAnswer: "F", explanation: "Ben wasn't tempted by money when he had his own circus." },
            { id: "23", content: "3. The circus coincided with Ben's birthday.", options: ["T", "F"], correctAnswer: "T", explanation: "Đúng theo câu chuyện." },
            { id: "24", content: "4. Seeing the circus was like a dose of medicine for Ben.", options: ["T", "F"], correctAnswer: "T", explanation: "Đúng theo câu chuyện." },
            { id: "25", content: "5. Ben learned about the circus from a television advertisement.", options: ["T", "F"], correctAnswer: "F", explanation: "Ben learned about the circus from a messenger with newspaper headlines." },
            { id: "26", content: "6. Ben was commissioned to paint informal portraits of people posing in front of a funny picture.", options: ["T", "F"], correctAnswer: "F", explanation: "An artist could be commissioned to paint informal portraits of people." }
          ]
        },
        {
          id: "sec5_reading",
          title: "Part B: Answer the questions.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "27", content: "1. Why did Ben like the circus to such an extent?", options: ["He could be very rich.", "He inquired about getting his own circus.", "It made him feel special.", "He took a dose of special medicine."], correctAnswer: "It made him feel special.", explanation: "Nó khiến anh ấy cảm thấy đặc biệt." },
            { id: "28", content: "2. What good news did the messenger bring?", options: ["The circus was coming.", "Ice cream was free.", "Good weather was coming.", "A new movie was showing."], correctAnswer: "The circus was coming.", explanation: "Tin tốt là rạp xiếc sắp tới." },
            { id: "29", content: "3. What did Ben’s dad do on his birthday?", options: ["He tamed tigers.", "He paid for Ben's portrait.", "He taught Ben how to drive.", "He steered around town looking for the circus."], correctAnswer: "He steered around town looking for the circus.", explanation: "Bố anh ấy lái xe chạy quanh thị trấn." },
            { id: "30", content: "4. Why wasn’t Ben tempted by money?", options: ["His circus wasn't very good.", "He was already very rich.", "He wanted other kids to like him.", "He only wanted to make people happy."], correctAnswer: "He only wanted to make people happy.", explanation: "Anh ấy chỉ muốn làm mọi người vui vẻ." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit22_raw.json', JSON.stringify(json, null, 2));
console.log("JSON written successfully.");
