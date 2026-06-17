const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);

if (!urlMatch || !keyMatch) {
  console.error("Supabase credentials not found in .env");
  process.exit(1);
}

const url = urlMatch[1].trim();
const key = keyMatch[1].trim();

const supabase = createClient(url, key);

const words = [
  { word: "arise", pos: "v.", pron: "[araiz]", def: "To arise is to happen.", ex: "Difficulties arose with his computer because it was old.", emoji: "⬆️" },
  { word: "benefactor", pos: "n.", pron: "[benafasktar]", def: "A benefactor is a person who gives money to help someone.", ex: "The student's benefactor gave him money to spend on his studies.", emoji: "🤝" },
  { word: "blacksmith", pos: "n.", pron: "[blaeksmle]", def: "A blacksmith is a person who makes things out of metal.", ex: "The blacksmith pounded the piece of metal until it was flat.", emoji: "⚒️" },
  { word: "charitable", pos: "adj.", pron: "[tjaeratabal]", def: "When someone is charitable, they help people who are in need.", ex: "My sister was charitable enough to help me buy my first house.", emoji: "❤️" },
  { word: "chimney", pos: "n.", pron: "[tjfmni]", def: "A chimney is a tall pipe used to carry smoke out of a building.", ex: "The cat was on the roof sitting next to the chimney.", emoji: "🧱" },
  { word: "compensate", pos: "v.", pron: "[kampanseit]", def: "To compensate is to pay someone for the time they spent doing something.", ex: "Her boss compensated her for the extra work she did last week.", emoji: "💰" },
  { word: "encounter", pos: "v.", pron: "[inkauntar]", def: "If you encounter something, you meet or come close to it.", ex: "I encountered a sea turtle while I was swimming.", emoji: "👋" },
  { word: "exceed", pos: "v.", pron: "[iksi:d]", def: "To exceed is to be more than something.", ex: "Since I exceeded my limit, I decided to get rid of my credit cards.", emoji: "📈" },
  { word: "forge", pos: "v.", pron: "[fo:rd3]", def: "To forge is to make or produce, especially with difficulty.", ex: "Stacy and Heather forged their friendship when they were teenagers.", emoji: "🔨" },
  { word: "humble", pos: "adj.", pron: "[hAmbl]", def: "People who are humble do not believe that they are better than other people.", ex: "Even though Bob is the smartest boy in his class, he is humble.", emoji: "🙏" },
  { word: "iron", pos: "n.", pron: "[a ism]", def: "Iron is a strong metal that is used to make many objects.", ex: "The horse had shoes made of iron.", emoji: "⛓️" },
  { word: "ladder", pos: "n.", pron: "[Isedax]", def: "A ladder is an object that is used to climb up and down things.", ex: "He used a ladder to climb to the top of his tree house.", emoji: "🪜" },
  { word: "modest", pos: "adj.", pron: "[madist]", def: "If people are modest, they do not think that they are too important.", ex: "Derek is very modest for someone who is so rich.", emoji: "😌" },
  { word: "occupy", pos: "v.", pron: "[akjapai]", def: "To occupy a place is to live, work, or be there.", ex: "Kevin and Alice occupied the chairs and had a long discussion.", emoji: "🪑" },
  { word: "penny", pos: "n.", pron: "[peni]", def: "A penny is a coin worth one cent.", ex: "U.S. President Abraham Lincoln is on the penny.", emoji: "🪙" },
  { word: "preach", pos: "v.", pron: "[pit.tj]", def: "To preach is to talk about and promote a religious idea.", ex: "Aaron often preached about living an honest life.", emoji: "🗣️" },
  { word: "prosper", pos: "v.", pron: "[prosper]", def: "To prosper is to be successful or make a lot of money.", ex: "Frank's new business finally prospered after many years of hard work.", emoji: "🌟" },
  { word: "province", pos: "n.", pron: "[prdvins]", def: "A province is a small area that is controlled by a country.", ex: "Canada is divided into several different provinces.", emoji: "🗺️" },
  { word: "satisfaction", pos: "n.", pron: "[saetisfaekjan]", def: "Satisfaction is a feeling you get when you do or receive something good.", ex: "Brad was filled with satisfaction when he saw what was for dinner.", emoji: "😊" },
  { word: "sustain", pos: "v.", pron: "[sastein]", def: "To sustain something is to keep it going.", ex: "Wind power is a clean way to sustain a city with energy.", emoji: "🔋" }
];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit1_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit1_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${w.emoji}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Real St. Nick</h1><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">At Christmas, children wait for St. Nicholas to bring gifts down the <b>chimney</b>. But it's not just a story. St. Nicholas was a real person.</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">A long time ago, a man named Marcus <b>occupied</b> a house with his family. He was not <b>modest</b>. He always told everybody he was the strongest man in the <b>province</b>.</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">He worked hard, but he could barely <b>sustain</b> his family. He wanted to save money and <b>prosper</b>. Still, he could never earn a <b>penny</b> more than he needed.</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">One day, Marcus made an agreement with a <b>blacksmith</b>. The <b>blacksmith</b> had a lot of work to do. But he couldn't do it all by himself. Marcus wanted to help him <b>forge</b> <b>iron</b>. The <b>blacksmith</b> agreed to <b>compensate</b> him with a lot of money.</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">In the same town, there was a man named Nicholas. At an early age, Nicholas started <b>preaching</b>. But he also believed that he should be <b>humble</b> and <b>charitable</b>. He learned that helping people gave him even more <b>satisfaction</b> than <b>preaching</b>.</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">One day, Nicholas <b>encountered</b> Marcus. Marcus told Nicholas about his agreement with the <b>blacksmith</b>. "I worked hard for him," Marcus said, "but a problem <b>arose</b>. Even though I worked for him, he didn't pay me."</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">Nicholas wanted to help Marcus. That night, he went back to Marcus's house. He brought a bag of gold. It <b>exceeded</b> the amount that Marcus needed. Nicholas climbed up a <b>ladder</b> and dropped the bag of gold down the <b>chimney</b>. Marcus thanked his <b>benefactor</b>.</p><p style="margin-bottom: 1.25rem; line-height: 1.6; color: #374151; font-size: 1.125rem;">Soon, people found out about Nicholas's gift. He became well known and loved. Even today, people still give secret gifts to children. And we say they are from St. Nicholas.</p></div>`;

const wordListSections = [
  {
    "id": "u1_v3_wl_ex1",
    "title": "Part A: Choose the right word for the given definition.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u1_v3_q1",
        "content": "1. to make or produce with difficulty",
        "options": ["prosper", "arise", "penny", "forge"],
        "correctAnswer": "forge",
        "explanation": "forge nghĩa là tạo ra, rèn."
      },
      {
        "id": "u1_v3_q2",
        "content": "2. a person who works with metal",
        "options": ["iron", "blacksmith", "charitable", "benefactor"],
        "correctAnswer": "blacksmith",
        "explanation": "blacksmith nghĩa là thợ rèn."
      },
      {
        "id": "u1_v3_q3",
        "content": "3. to keep something going",
        "options": ["exceed", "sustain", "preach", "occupy"],
        "correctAnswer": "sustain",
        "explanation": "sustain nghĩa là duy trì."
      },
      {
        "id": "u1_v3_q4",
        "content": "4. a small area that is part of a country",
        "options": ["ladder", "province", "encounter", "compensate"],
        "correctAnswer": "province",
        "explanation": "province nghĩa là tỉnh, khu vực nhỏ trong 1 đất nước."
      },
      {
        "id": "u1_v3_q5",
        "content": "5. thinking oneself not to be too important",
        "options": ["humble", "satisfaction", "chimney", "modest"],
        "correctAnswer": "modest",
        "explanation": "modest nghĩa là khiêm tốn."
      }
    ]
  },
  {
    "id": "u1_v3_wl_ex2",
    "title": "Part B: Choose the right definition for the given word.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u1_v3_q6",
        "content": "1. benefactor",
        "options": ["giver", "an area", "money", "too much"],
        "correctAnswer": "giver",
        "explanation": "benefactor nghĩa là người cho, ân nhân."
      },
      {
        "id": "u1_v3_q7",
        "content": "2. compensate",
        "options": ["where smoke goes", "to shape metal", "a tool used to climb", "to pay someone in return"],
        "correctAnswer": "to pay someone in return",
        "explanation": "compensate nghĩa là đền bù, trả công."
      },
      {
        "id": "u1_v3_q8",
        "content": "3. occupy",
        "options": ["to be rich", "to happen", "to see someone you know", "to be in a place"],
        "correctAnswer": "to be in a place",
        "explanation": "occupy nghĩa là chiếm chỗ, ở một nơi nào đó."
      },
      {
        "id": "u1_v3_q9",
        "content": "4. iron",
        "options": ["a baby", "a type of metal", "a good feeling", "a person who makes things with metal"],
        "correctAnswer": "a type of metal",
        "explanation": "iron nghĩa là kim loại sắt."
      },
      {
        "id": "u1_v3_q10",
        "content": "5. exceed",
        "options": ["to keep something going", "to not talk about yourself too much", "to be kind to others", "to go past a certain limit"],
        "correctAnswer": "to go past a certain limit",
        "explanation": "exceed nghĩa là vượt qua một giới hạn nào đó."
      }
    ]
  },
  {
    "id": "u1_v3_wl_ex3",
    "title": "Part C: Choose the answer that best fits the question.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u1_v3_q11",
        "content": "1. Which of the following is a form of money?",
        "options": ["A province", "A penny", "A blacksmith", "A ladder"],
        "correctAnswer": "A penny",
        "explanation": "penny là một dạng tiền xu."
      },
      {
        "id": "u1_v3_q12",
        "content": "2. If you meet a boy on the street, you ___ him.",
        "options": ["exceed", "occupy", "encounter", "sustain"],
        "correctAnswer": "encounter",
        "explanation": "encounter nghĩa là bắt gặp."
      },
      {
        "id": "u1_v3_q13",
        "content": "3. Which of the following is a good feeling?",
        "options": ["Modest", "Humble", "Satisfaction", "Charitable"],
        "correctAnswer": "Satisfaction",
        "explanation": "Satisfaction nghĩa là sự hài lòng."
      },
      {
        "id": "u1_v3_q14",
        "content": "4. Which one is part of a house?",
        "options": ["Forge", "Compensate", "Arise", "Chimney"],
        "correctAnswer": "Chimney",
        "explanation": "Chimney nghĩa là ống khói."
      },
      {
        "id": "u1_v3_q15",
        "content": "5. Which word relates to the word religion?",
        "options": ["Iron", "Preach", "Benefactor", "Prosper"],
        "correctAnswer": "Preach",
        "explanation": "Preach nghĩa là thuyết giáo."
      },
      {
        "id": "u1_v3_q16",
        "content": "6. Which of the following means to happen?",
        "options": ["Sustain", "Arise", "Province", "Prosper"],
        "correctAnswer": "Arise",
        "explanation": "Arise nghĩa là xảy ra, phát sinh."
      },
      {
        "id": "u1_v3_q17",
        "content": "7. Which of the following do people use to reach high places?",
        "options": ["A chimney", "A blacksmith", "A benefactor", "A ladder"],
        "correctAnswer": "A ladder",
        "explanation": "ladder nghĩa là cái thang."
      },
      {
        "id": "u1_v3_q18",
        "content": "8. If you are smart with your money, then what will happen to you?",
        "options": ["You will occupy a jail cell", "You will forge a strong relationship", "You will prosper", "You will become humble"],
        "correctAnswer": "You will prosper",
        "explanation": "prosper nghĩa là thịnh vượng, phát đạt."
      },
      {
        "id": "u1_v3_q19",
        "content": "9. If someone gives money to others, we could say that they are ___ .",
        "options": ["charitable", "modest", "prosper", "exceed"],
        "correctAnswer": "charitable",
        "explanation": "charitable nghĩa là từ thiện, hay giúp đỡ."
      },
      {
        "id": "u1_v3_q20",
        "content": "10. Which of the following describes someone who thinks they are no better than others?",
        "options": ["Benefactor", "Satisfaction", "Humble", "Compensate"],
        "correctAnswer": "Humble",
        "explanation": "Humble nghĩa là khiêm tốn."
      }
    ]
  }
];

const storySections = [
  {
    "id": "u1_v3_rd_ex1",
    "title": "Answer the questions based on the story.",
    "content": "",
    "questionType": "Trắc nghiệm",
    "questions": [
      {
        "id": "u1_v3_q21",
        "content": "1. Which of the following is true about the job Marcus did?",
        "options": [
          "He made pennies.",
          "He was compensated unfairly.",
          "He preached to people.",
          "He barely sustained his family."
        ],
        "correctAnswer": "He barely sustained his family.",
        "explanation": "Marcus làm việc chăm chỉ nhưng chỉ đủ nuôi sống gia đình (barely sustained his family)."
      },
      {
        "id": "u1_v3_q22",
        "content": "2. Why didn't Nicolas tell people that he gave money away?",
        "options": [
          "He prospered.",
          "He didn't want to be modest.",
          "He wanted to be humble.",
          "He wasn't popular in the province."
        ],
        "correctAnswer": "He wanted to be humble.",
        "explanation": "Nicholas muốn giữ sự khiêm tốn (humble) khi làm việc thiện."
      },
      {
        "id": "u1_v3_q23",
        "content": "3. What was dropped down the chimney?",
        "options": [
          "A penny",
          "A ladder",
          "Gold",
          "A benefactor"
        ],
        "correctAnswer": "Gold",
        "explanation": "Nicholas đã thả túi vàng xuống qua ống khói."
      },
      {
        "id": "u1_v3_q24",
        "content": "4. Why did Marcus want more money?",
        "options": [
          "To buy more iron",
          "To feed his family",
          "To give it away",
          "To become a blacksmith"
        ],
        "correctAnswer": "To feed his family",
        "explanation": "Anh ấy cần thêm tiền để lo cho gia đình."
      }
    ]
  }
];

const contentJson = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 1: Volume 3",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordListHtml,
      sections: wordListSections
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit1_v3_story.png",
      sections: storySections
    }
  ]
};

async function run() {
  const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';
  const folderId = '0f15a9d8-efc3-45ca-8fd3-aaa02ffa914c';

  const { data: existing, error: err2 } = await supabase.from('tests').select('id').eq('title', 'Unit 1: Volume 3').single();

  if (existing) {
    const { data, error } = await supabase
      .from('tests')
      .update({ content_json: contentJson, folder_id: folderId })
      .eq('id', existing.id);
    if (error) console.error('Error updating:', error);
    else console.log('Unit 1: Volume 3 updated in Supabase successfully!');
  } else {
    const { data, error } = await supabase
      .from('tests')
      .insert({
        title: 'Unit 1: Volume 3',
        test_type: 'vocabulary',
        course_id: courseId,
        folder_id: folderId,
        content_json: contentJson,
        is_published: true
      });
    if (error) console.error('Error inserting:', error);
    else console.log('Unit 1: Volume 3 inserted into Supabase successfully!');
  }
}

run();
