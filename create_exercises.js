const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
const folderId = 'e2ddb86d-139b-4e3c-9878-ba11a0c808fb';

const ex1Passage = `
<h3 class="text-xl font-bold mb-4 text-center">Body Art</h3>
<p>There is no reason why tattooing and face and body painting should be <mark>barred</mark> from the status of "art"; if they are nevertheless commonly excluded, this may be due to the impermanent nature of face and body painting as well as to marketing problems.</p>
<p>The most common technique of tattooing among native North American Indians was by pricking the skin with sharp points. Sometimes <mark>it</mark> was done using on a special comb-like implement. As in the less widely distributed scratching method, designs are usually first sketched with charcoal paste, then rubbed into the breaks in the skin. In northern and northwestern North America, threads covered with soot are drawn through punctures made by needles to apply the <mark>pigment</mark> beneath the skin. In face painting, mostly mineral pigments (but sometimes including charcoal for black, or pollen for yellow) are mixed with water and/or grease before <mark>they</mark> are applied to the skin with fingers, paint brushes, or wooden paint sticks. Painting is generally done by the wearer himself, with occasional help from others, and with the exception of some ceremonial painting, using a bowl of water to serve as a mirror. Tattooing, on the other hand, is done by others, who tend to be specialists.</p>
<p>The functions of body art are extremely varied, even within a single tribe. <mark>They</mark> range from pure beautification of the wearer, through expression of mood, prevention of disease, protection against misfortunes, and the recording of a ceremonial event, to the identification of an individual's status or membership in a social group.</p>
<p>Even though there is <mark>ample</mark> information on the body art of various individual tribes, significant comparative studies are scarce on the continent. Regional stylistic variations are as yet undefined. Tattooed designs are all basically linear, with simple symmetrical, non-representational designs on the face, and forms of greater complexity on the body. Tattooing is black (with rare red/black exceptions); but painting is frequently bichrome or polychrome, with solid color areas as important as lines.</p>
`;

const ex1Questions = [
  { q: "The word <mark>barred</mark> in paragraph 1 is closest in meaning to", opts: ["kept secret", "made better", "left out", "applied"], ans: "C", exp: "\"Barred from\" có nghĩa là bị ngăn cản, loại trừ khỏi cái gì đó, đồng nghĩa với \"left out\"." },
  { q: "The word <mark>it</mark> in paragraph 2 refers to", opts: ["face and body painting", "North American Indians", "skin", "pricking the skin with sharp points"], ans: "D", exp: "\"it\" thay thế cho hành động xăm hình \"pricking the skin with sharp points\" được nhắc đến ở câu ngay phía trước." },
  { q: "The word <mark>pigment</mark> in paragraph 2 is closest in meaning to", opts: ["dye", "color", "metal", "oil"], ans: "A", exp: "\"Pigment\" là chất nhuộm màu hoặc sắc tố, đồng nghĩa với \"dye\" (thuốc nhuộm, màu nhuộm)." },
  { q: "The word <mark>they</mark> in paragraph 2 refers to", opts: ["mineral pigments", "punctures", "needles", "water and grease"], ans: "A", exp: "Đại từ \"they\" ở đây dùng để thay thế cho danh từ số nhiều \"mineral pigments\" đã được nhắc đến ở đầu câu." },
  { q: "The word <mark>They</mark> in paragraph 3 refers to", opts: ["Specialists", "Single tribe", "Functions", "Body art"], ans: "C", exp: "\"They\" thay thế cho cụm từ \"The functions of body art\" ở câu trước đó, ý nói về các chức năng của nghệ thuật trên cơ thể." },
  { q: "The word <mark>ample</mark> in paragraph 4 is closest in meaning to", opts: ["correct", "enough", "important", "surprising"], ans: "B", exp: "\"Ample\" mang nghĩa là nhiều, dư dật, dồi dào, gần nghĩa nhất với \"enough\" (đủ nhiều) trong ngữ cảnh này." }
];

const ex2Passage = `
<h3 class="text-xl font-bold mb-4 text-center">Seaweeds</h3>
<p>Most species of marine algae are represented by the forms popularly known as seaweeds. This, however, is a rather unfortunate term. For one thing, the word weeds does not do justice to these <mark>conspicuous</mark> and often elegant inhabitants of rocky shores and other marine environments. Some biologists opt for the more formal name of macrophytes. On the other hand, the term seaweeds is useful in distinguishing them from the unicellular algae. The structures of seaweeds are far more complex than <mark>those</mark> of unicellular algae, and reproduction is also more <mark>elaborate</mark>. Seaweeds are all eukaryotes, as opposed to prokaryotes, which are the simplest type of cells that lack organelles. Most are multicellular, but some forms consisting of single cells or simple filaments are considered seaweeds. This is because the classification of seaweeds is based not only on structure but also on other features such as the types of pigments and food storage products.</p>
<p>Although more complex than unicellular algae, seaweeds still lack the complex structures and reproductive mechanisms <mark>characteristic of</mark> the higher, mostly terrestrial plants. Most specialists include them in the kingdom Protista. There are some who disagree and assign them instead to the kingdom Plantae, together with the higher plants.</p>
<p>The range of variation observed among the multicellular algae is spectacular. <mark>Those</mark> we see on rocky shores at low tide are usually small and sturdy as an adaptation to withstand waves. Kelps found offshore in cold waters are true giants that form dense underwater forests. The multicellular condition of seaweeds allows many adaptations not available to unicellular forms. For example, they can grow tall and rise off the bottom. <mark>This</mark> provides new opportunities as well as challenges: wave action and turbulence, competition for space and light, and the problem of predatory sea urchins and fish.</p>
`;

const ex2Questions = [
  { q: "The word <mark>conspicuous</mark> in paragraph 1 is closest in meaning to", opts: ["easily seen", "well-known", "huge", "graceful"], ans: "A", exp: "\"Conspicuous\" có nghĩa là dễ thấy, đập vào mắt, đồng nghĩa với \"easily seen\"." },
  { q: "The word <mark>those</mark> in paragraph 1 refers to", opts: ["structures", "seaweeds", "unicellular algae", "macrophytes"], ans: "A", exp: "\"those\" được dùng để thay thế cho danh từ số nhiều \"structures\" ở vế trước (\"The structures of seaweeds are far more complex than those of unicellular algae\")." },
  { q: "The word <mark>elaborate</mark> in paragraph 1 is closest in meaning to", opts: ["complicated", "advanced", "common", "decisive"], ans: "A", exp: "\"Elaborate\" có nghĩa là tỉ mỉ, phức tạp, tinh vi, đồng nghĩa với \"complicated\"." },
  { q: "The phrase <mark>characteristic of</mark> in paragraph 2 is closest in meaning to", opts: ["based on", "lacking", "regarded as", "typical of"], ans: "D", exp: "\"Characteristic of\" mang ý nghĩa là đặc trưng cho, tiêu biểu cho, đồng nghĩa với \"typical of\"." },
  { q: "The word <mark>Those</mark> in paragraph 3 refers to", opts: ["Variation", "Multicellular algae", "Rocky shores", "Waves"], ans: "B", exp: "\"Those\" ở đây thay thế cho danh từ số nhiều \"multicellular algae\" (tảo đa bào) đã được nhắc đến ở câu ngay phía trước." },
  { q: "The word <mark>This</mark> in paragraph 3 refers to", opts: ["Living in underwater forests", "Living in cold water", "Having unicellular forms", "Growing tall and rising off the bottom"], ans: "D", exp: "\"This\" thay thế cho sự việc \"grow tall and rise off the bottom\" được nhắc tới ngay trước đó." }
];

function buildTestPayload(title, passage, qList) {
  const parts = [
    {
      id: crypto.randomUUID(),
      name: 'Part 1',
      content: passage,
      sections: [
        {
          id: crypto.randomUUID(),
          title: 'Section 1',
          questionType: 'Trắc nghiệm',
          questions: qList.map((data, index) => ({
            id: String(index + 1),
            content: data.q,
            options: data.opts,
            correctAnswer: data.ans,
            explanation: data.exp
          }))
        }
      ]
    }
  ];

  return {
    title: title,
    test_type: 'Standard-Reading',
    course_id: courseId,
    folder_id: folderId,
    is_published: true,
    content_json: {
      basicInfo: {
        title: title,
        skill: 'Standard-Reading',
        category: 'exercise',
        timeLimit: '0',
        courseId: courseId
      },
      parts: parts
    },
    json_config: {
      timeLimit: 0,
      parts: parts
    }
  };
}

async function run() {
  const payload1 = buildTestPayload('Chapter 1: Exercise 1', ex1Passage, ex1Questions);
  const payload2 = buildTestPayload('Chapter 1: Exercise 2', ex2Passage, ex2Questions);
  
  const { error } = await supabase.from('tests').insert([payload1, payload2]);
  if (error) {
    console.error('Error inserting tests:', error);
  } else {
    console.log('Inserted Exercise 1 and Exercise 2 successfully!');
  }
}

run();
