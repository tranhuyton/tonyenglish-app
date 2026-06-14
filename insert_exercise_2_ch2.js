const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Flowers</h2>
<p style="text-indent:2em;line-height:1.9;">Most flowers consist of four sets of floral parts - sepals, petals, stamens and carpels. Each floral part is thought to be, evolutionarily speaking, a modified leaf. ❶ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">The floral parts may be arranged spirally on a more or less elongated stalk, or similar parts - such as petals - may be located at one level in a whorl.</span></p>
<p style="text-indent:2em;line-height:1.9;">The outermost parts of the flower are the sepals, which are usually green and leaflike. The sepals, collectively known as calyx, enclose and protect the developing flower bud. Next are the petals, which together are called the corolla. Petals may also be leaf-shaped, but they are often brightly colored. ❷ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">They advertise the presence of the flower among the green leaves, attracting insects or other animals that visit flowers for their nectar or for other edible substances.</span> As these animals forage for food, they are likely to carry pollen from flower to flower. Within the corolla are the stamens. Each stamen consists of a single elongated stalk, called the filament, and at the end of the filament, the anther. The pollen grains, formed within the anther, are the immature male gametophytes. ❸ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">When ripe, the pollen grains are released, often in large numbers, through slits or pores in the anther.</span> The centermost parts of the flower are the carpels, which contain the female gametophytes. A single flower may have one carpel or several carpels, which may be separate or fused together. Typically a single carpel or fused carpels consist of a stigma, which is the sticky surface to which pollen grains adhere; a stalk, the style through which the pollen tube grows; and a swollen base, the ovary. Within the ovary are one or more ovules, each of which encloses a female gametophyte, or embryo sac, containing a single egg cell. After the egg is fertilized, the ovule develops into a seed and the ovary into a fruit.</p>
<p style="text-indent:2em;line-height:1.9;">A flower that contains both stamens and carpels is known as a perfect flower. In some species, the flowers are imperfect - that is, they are either male (staminate) or female (carpellate). Male and female flowers may be present on the same plant, as in corn, squash, oaks and birches; such plants are said to be monoecious ("one house"). ❹ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">Species in which the male and female flowers are on separate plants, such as the American mistletoe, the tree of heaven, and holly, are known as dioecious ("two houses").</span> As gardeners know, in order for a female holly plant to produce berries, a male holly - which never produces berries - must be planted nearby.</p>
`;

const qList = [
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❶?",
    opts: [
      "A. The parts of a flower are arranged in a circular pattern either at one level or at multiple levels.",
      "B. The spiral arrangement of the floral parts is a characteristic similar to petals, which circle around a long stalk.",
      "C. The parts of a flower located in a spiral along a long stalk are called petals.",
      "D. The floral parts around a stalk are elongated, so that similar parts can be placed in a circular shape."
    ],
    ans: 0,
    exp: "Ý gốc: Các bộ phận của hoa có thể được sắp xếp theo hình xoắn ốc (spirally) trên một cuống thon dài, hoặc các bộ phận tương tự - chẳng hạn như cánh hoa - có thể nằm ở cùng một độ cao theo vòng tròn (whorl = circular pattern)."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❷?",
    opts: [
      "A. The presence of the flower shows that insects or other animals visit flowers.",
      "B. Some insects or other animals are dependent on flowers for food.",
      "C. Petals differ from leaves in that they advertise their presence to insects.",
      "D. Petals function as a sign of the flower for insects and other animals."
    ],
    ans: 3,
    exp: "Ý gốc: Chúng (cánh hoa) báo hiệu sự hiện diện của hoa (advertise the presence of the flower) giữa những chiếc lá xanh, thu hút côn trùng hoặc động vật khác. -> Cánh hoa đóng vai trò như một dấu hiệu của hoa đối với côn trùng và động vật (function as a sign...)."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❸?",
    opts: [
      "A. A large number of the pollen grains are released from the ripe anther.",
      "B. When the pollen grains are spread, they go through holes in the anther.",
      "C. Mature pollen grains set themselves apart from the anther.",
      "D. The anther becomes mature by releasing a large number of pollen grains."
    ],
    ans: 2,
    exp: "Ý gốc: Khi chín (ripe = mature), các hạt phấn hoa được giải phóng (released = set themselves apart) khỏi bao phấn."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❹?",
    opts: [
      "A. The American mistletoe, the tree of heaven, and holly are some of the best-known dioecious plants.",
      "B. Dioecious plant species are unisexual.",
      "C. When male and female flowers are located in one plant, it is called dioecious.",
      "D. Plants that only have flowers of one sex are called dioecious."
    ],
    ans: 3,
    exp: "Ý gốc: Những loài mà hoa đực và hoa cái nằm trên các cây riêng biệt (separate plants) ... được gọi là thực vật đơn tính khác gốc (dioecious). -> Nghĩa là các cây đó chỉ có hoa thuộc một giới tính (flowers of one sex)."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 2: Exercise 2",
    timeLimit: 0,
    category: "exercise",
    skill: "Standard-Reading"
  },
  parts: [
    {
      id: "part1",
      content: readingText,
      sections: [
        {
          id: "sec1",
          title: "",
          content: "",
          questionType: "Trắc nghiệm",
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
  ]
};

async function run() {
  const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb'; // IELTS Premium
  const folderId = 'ba08090a-d614-40a8-b7dc-89c7723daf89'; // Chapter 2 inside Crash Course
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 2: Exercise 2",
    course_id: courseId,
    folder_id: folderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 2: Exercise 2").eq('course_id', courseId);
  if (existing && existing.length > 0) {
    const { data, error } = await supabase.from('tests').update(payload).eq('id', existing[0].id).select();
    if (error) console.error("Error updating:", error);
    else console.log("Successfully updated test:", data[0].title);
  } else {
    const { data, error } = await supabase.from('tests').insert([payload]).select();
    if (error) console.error("Error inserting:", error);
    else console.log("Successfully inserted test:", data[0].title);
  }
}

run();
