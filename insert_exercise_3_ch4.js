const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Photosynthesis</h2>
<p style="text-indent:2em;line-height:1.9;">Almost all living things ultimately get their energy from the sun. In a process called photosynthesis, plants, algae, and some other organisms capture the sun's energy and use it to make simple sugars such as glucose. Most other organisms use these organic molecules as a source of energy. Organic materials contain a tremendous amount of energy. As food, they fuel our bodies and those of most other creatures. In such forms as oil, gas, and coal, they heat our homes, run our factories and power our cars.</p>
<p style="text-indent:2em;line-height:1.9;">Photosynthesis begins when solar energy is absorbed by chemicals called photosynthetic pigments that are contained within an organism. The most common photosynthetic pigment is chlorophyll. The bright green color characteristic of plants is caused by it. Most algae have additional pigments that may mask the green chlorophyll. Because of these pigments, algae may be not only green but brown, red, blue or even black.</p>
<p style="text-indent:2em;line-height:1.9;">In a series of enzyme-controlled reactions, the solar energy captured by chlorophyll and other pigments is used to make simple sugars, with carbon dioxide and water as the raw materials. Carbon dioxide is one of very few carbon-containing molecules not considered to be organic compounds. Photosynthesis then converts carbon from an inorganic to an organic form. This is called carbon fixation. In this process, the solar energy that was absorbed by chlorophyll is stored as chemical energy in the form of simple sugars like glucose. The glucose is then used to make other organic compounds. In addition, photosynthesis produces oxygen gas. All the oxygen gas on earth, both in the atmosphere we breathe and in the ocean, was produced by photosynthetic organisms. Photosynthesis constantly replenishes the earth's oxygen supply.</p>
<p style="text-indent:2em;line-height:1.9;">Organisms that are capable of photosynthesis can obtain all the energy they need from sunlight and do not need to eat. They are called autotrophs. Plants are the most familiar autotrophs on land. In the ocean, algae and bacteria are the most important autotrophs. Many organisms cannot produce their own food and must obtain energy by eating organic matter. These are called heterotrophs.</p>
`;

const qList = [
  {
    q: "What can be inferred about algae?",
    opts: [
      "A. Green algae are less common than other colors of algae.",
      "B. Algae are photosynthetic organisms.",
      "C. They are ineffective producers of sugars.",
      "D. They are chemically different from other plants."
    ],
    ans: 1,
    exp: "Ý gốc đoạn 1: 'In a process called photosynthesis, plants, algae, and some other organisms capture the sun's energy...'. Tảo (algae) có khả năng quang hợp để thu năng lượng mặt trời. Do đó, có thể suy ra chúng là sinh vật quang hợp (photosynthetic organisms)."
  },
  {
    q: "Based on the information in paragraph 3, it can be inferred that glucose",
    opts: [
      "A. is needed to create enzymes",
      "B. is a byproduct of oxygen production",
      "C. enables photosynthesis",
      "D. contains carbon"
    ],
    ans: 3,
    exp: "Đoạn 3 cho biết quang hợp sử dụng carbon dioxide (CO2) để tạo ra đường đơn. Quá trình này chuyển hóa carbon từ dạng vô cơ sang dạng hữu cơ, và năng lượng được lưu trữ dưới dạng đường đơn như glucose ('...stored as chemical energy in the form of simple sugars like glucose'). Từ đó suy ra đường đơn (như glucose) là hợp chất hữu cơ được tạo thành từ carbon (contains carbon)."
  },
  {
    q: "What can be inferred about heterotrophs?",
    opts: [
      "A. They are not reliant on simple sugars for energy.",
      "B. They require more energy than autotrophs.",
      "C. They cannot exist without the presence of autotrophs.",
      "D. They are mostly land-bound organisms."
    ],
    ans: 2,
    exp: "Đoạn cuối cho biết sinh vật dị dưỡng (heterotrophs) 'cannot produce their own food and must obtain energy by eating organic matter' (không thể tự tạo thức ăn mà phải lấy năng lượng bằng cách ăn chất hữu cơ). Vì các chất hữu cơ này ban đầu được tạo ra bởi sinh vật tự dưỡng (autotrophs) thông qua quang hợp, nên sinh vật dị dưỡng không thể tồn tại nếu thiếu vắng sinh vật tự dưỡng (cannot exist without the presence of autotrophs)."
  },
  {
    q: "It can be inferred from the passage that the author considers solar energy to be",
    opts: [
      "A. essential for every organism on earth",
      "B. a perfect solution to the energy problem",
      "C. a permanent and everlasting source of energy",
      "D. useless to most bacteria and algae"
    ],
    ans: 0,
    exp: "Ngay câu đầu tiên, tác giả khẳng định 'Almost all living things ultimately get their energy from the sun' (Hầu như mọi sinh vật sống rốt cuộc đều lấy năng lượng từ mặt trời). Các đoạn sau giải thích sinh vật tự dưỡng dùng năng lượng này tạo chất hữu cơ, còn sinh vật dị dưỡng lại ăn chất hữu cơ đó. Do đó, năng lượng mặt trời là thiết yếu (essential) đối với mọi sinh vật trên Trái Đất."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 4: Exercise 3",
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
  const crashCourseFolderId = 'ed267b14-83b3-44f2-8b83-c6fe5ea55686'; // Crash Course
  
  // Find Chapter 4 folder
  let chapter4FolderId;
  const {data: existingFolder} = await supabase.from('folders').select('id').eq('parent_id', crashCourseFolderId).ilike('title', 'Chapter 4');
  
  if (existingFolder && existingFolder.length > 0) {
    chapter4FolderId = existingFolder[0].id;
  } else {
    // get max display_order
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 4",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapter4FolderId = newFolder[0].id;
    console.log("Created Chapter 4 folder!");
  }
  
  // check max test order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapter4FolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 4: Exercise 3",
    course_id: courseId,
    folder_id: chapter4FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 4: Exercise 3").eq('course_id', courseId);
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
