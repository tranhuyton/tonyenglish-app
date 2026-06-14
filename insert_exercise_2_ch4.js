const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Tides</h2>
<p style="text-indent:2em;line-height:1.9;">The tides are caused by the gravitational pull of the moon and sun and by the rotation of the Earth, moon, and sun. Strictly speaking, the moon does not rotate around the Earth. Instead the Earth and moon both rotate around a common point, their combined center of mass. This rotation produces centrifugal force, which is the force that pushes you outward when you ride on a merry-go-round. The centrifugal force just balances the gravitational attraction between the Earth and moon - otherwise the two would either fly away from each other or crash together.</p>
<p style="text-indent:2em;line-height:1.9;">Centrifugal force and the moon's gravity are not in perfect balance everywhere on the Earth's surface, however. On the side of the Earth nearest the moon, the moon's gravity is stronger and pulls the water toward the moon. On the side away from the moon, centrifugal force predominates, pushing the water away from the moon. If the Earth were completely covered with water, the water would form two bulges on opposite sides of the planet. In addition to the rotation of the moon and the Earth as mentioned above, the Earth is spinning like a top on its own axis. As it does so, any given point on the planet's surface will first be under a bulge and then away from the bulge. High tide occurs when the point is under a bulge. Because the Earth takes 24 hours to complete a rotation, the point will have two high tides and two low tides every day. Actually, the moon advances a little in its own orbit in the course of a day. It takes the point on Earth an extra 50 minutes to catch up and come directly in line with the moon again. A full tidal cycle thus takes 24 hours and 50 minutes.</p>
<p style="text-indent:2em;line-height:1.9;">The sun produces tidal bulges in the same way as the moon. Though it is much larger than the moon, it is 400 times further away, and its effect on the tides is much less. When the sun and moon are in line with each other, which happens at the full and new moons, their effects add together. At these times, the tidal range, or difference in water level between successive high and low tides, is large. Such tides are called spring tides. This name is a misnomer because spring tides occur throughout the year.</p>
`;

const qList = [
  {
    q: "Based on the information in paragraph 1, what can be inferred about the Earth?",
    opts: [
      "A. Its orbit is affected by the moon.",
      "B. It experiences the strongest tidal forces in the solar system.",
      "C. Its centrifugal force is provided by the sun.",
      "D. Its rotation around the sun will eventually eliminate the occurrence of tides."
    ],
    ans: 0,
    exp: "Ý gốc đoạn 1: 'Instead the Earth and moon both rotate around a common point, their combined center of mass.' (Trái Đất và mặt trăng đều quay quanh một điểm chung, tâm khối lượng kết hợp của chúng). Điều này chứng tỏ Trái Đất không tự quay quanh một trục độc lập hoàn toàn mà quỹ đạo của nó bị ảnh hưởng (tác động qua lại) bởi mặt trăng."
  },
  {
    q: "Based on the information in paragraph 2, what can be inferred about high tides?",
    opts: [
      "A. Times for high tides vary with location.",
      "B. Their strength is always consistent.",
      "C. They are stronger at night than in the day.",
      "D. They do not occur close to the Earth's equator."
    ],
    ans: 0,
    exp: "Ý gốc đoạn 2 giải thích rằng khi Trái Đất quay trên trục của nó, 'any given point on the planet's surface will first be under a bulge...' (bất kỳ điểm nào trên bề mặt cũng sẽ lần lượt đi vào vùng phình nước). Lúc đó triều cường (high tide) xảy ra. Vì Trái Đất quay liên tục nên các vị trí (location) khác nhau sẽ tiến vào vùng triều cường ở các thời điểm khác nhau."
  },
  {
    q: "It can be inferred from the passage that gravity",
    opts: [
      "A. is a phenomenon unique to the Earth and the moon",
      "B. would not be possible without the presence of tides",
      "C. weakens as distance increases between two objects",
      "D. prevents the sun from creating strong tides on Earth"
    ],
    ans: 2,
    exp: "Ý gốc đoạn 3: 'Though it [the sun] is much larger than the moon, it is 400 times further away, and its effect on the tides is much less.' Mặc dù Mặt trời lớn hơn Mặt trăng rất nhiều, nhưng vì ở xa hơn 400 lần nên tác động lực hấp dẫn tạo ra thủy triều lại yếu hơn. Từ đó suy ra lực hấp dẫn yếu đi khi khoảng cách tăng lên."
  },
  {
    q: "Based on the information in paragraph 3, which of the following is mostly likely to happen when the sun and the moon are the farthest away in angle from each other?",
    opts: [
      "A. Spring tides will cease to happen.",
      "B. The sun's effect on the tides will increase.",
      "C. An eclipse will take place.",
      "D. The tidal range will be the smallest."
    ],
    ans: 3,
    exp: "Đoạn 3 cho biết khi Mặt trời và Mặt trăng thẳng hàng ('in line with each other'), hiệu ứng của chúng cộng gộp lại tạo ra triều cường rất lớn (Spring tides) với biên độ triều (tidal range) lớn. Ngược lại, khi chúng lệch góc xa nhất với nhau (tức vuông góc với Trái Đất), lực hút của chúng sẽ bị triệt tiêu lẫn nhau phần nào, dẫn đến biên độ triều nhỏ nhất (smallest tidal range)."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 4: Exercise 2",
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
    title: "Chapter 4: Exercise 2",
    course_id: courseId,
    folder_id: chapter4FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 4: Exercise 2").eq('course_id', courseId);
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
