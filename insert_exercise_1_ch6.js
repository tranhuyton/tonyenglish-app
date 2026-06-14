const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Glaciation</h2>
<p style="text-indent:2em;line-height:1.9;">Much of the North American landscape has been shaped by glaciation, the formation and movement of great sheets of ice, or glaciers, across the continent. <b>[1A]</b> North America is believed to have undergone several major periods of glaciation. <b>[1B]</b> Exactly why these periods occurred is uncertain, but glaciation is believed to be related to irregularities in the Earth's rotation. <b>[1C]</b> During the most recent glacial period, the northern part of the continent, including part of what is now the northern United States, is thought to have been buried under a layer of ice several kilometers thick. <b>[1D]</b> The weight of this ice was so tremendous that it actually depressed, or bent downward, the crust of the Earth in some places, even as it scoured the surface of the continent. The advancing glaciers left more dramatic evidence of their passage in the form of large basins, or depressed areas, which filled with water after the glaciers melted and disappeared. <b>[2A]</b></p>
<p style="text-indent:2em;line-height:1.9;">Several of these enormous water-filled basins are known today as the Great Lakes. <b>[2B]</b> Important avenues of maritime commerce, they have played an important part in the history of the United States and Canada and have made seaports out of cities such as Chicago, Milwaukee, Marquette, and Duluth, which lie hundreds of kilometers from the Atlantic Ocean. <b>[2C]</b> The Great Lakes are connected to the Atlantic Ocean by the St. Lawrence River, which flows into the Gulf of St. Lawrence and from there to the Atlantic. <b>[2D]</b></p>
<p style="text-indent:2em;line-height:1.9;">Before the most recent glaciation, the location of the present-day Great Lakes was an area of low elevation in an inland plain. <b>[3A]</b> At its greatest extent, the ice sheet reached as far south as the modern Ohio River valley. <b>[3B]</b> Then, the global climate became warmer, and the glacial ice began to melt and retreat, leaving behind the deep basins which now contain the Great Lakes. <b>[3C]</b> Other glacial landforms were created from the moraines, or deposits of ground and fragmented rock, left behind by the shrinking glaciers. <b>[3D]</b> Moraines in some places acted as great natural dams which trapped water from the melted ice. The glacial debris also accumulated in long, sinuous ridges which indicate where rivers of water from the melting glaciers once ran.</p>
`;

const qList = [
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>While the causes remain uncertain, the chronological record of past glacial periods is both complete and accurate.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [1A]",
      "B. [1B]",
      "C. [1C]",
      "D. [1D]"
    ],
    ans: 2,
    exp: "Câu đề bài đề cập: 'While the causes remain uncertain, the chronological record of past glacial periods is both complete and accurate.' (Mặc dù nguyên nhân vẫn chưa chắc chắn, nhưng hồ sơ niên đại của các thời kỳ băng hà trong quá khứ vừa hoàn chỉnh vừa chính xác). Câu ngay phía trước vị trí [1C] nói: 'Exactly why these periods occurred is uncertain...' (Chính xác tại sao các thời kỳ này xảy ra thì không chắc chắn...). Sự liên kết về việc 'nguyên nhân không chắc chắn' (uncertain) làm cho [1C] là vị trí phù hợp nhất để nối tiếp đoạn văn."
  },
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>These cities owe the wealth and power they have today to the lakes.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [2A]",
      "B. [2B]",
      "C. [2C]",
      "D. [2D]"
    ],
    ans: 2,
    exp: "Câu đề bài viết: 'These cities owe the wealth and power they have today to the lakes.' (Những thành phố này có được sự giàu có và quyền lực ngày nay là nhờ vào các hồ). Cụm từ 'These cities' (Những thành phố này) ám chỉ trực tiếp đến các thành phố vừa được liệt kê ở câu ngay trước vị trí [2C]: '...cities such as Chicago, Milwaukee, Marquette, and Duluth...'. Vì vậy, [2C] là vị trí chính xác nhất."
  },
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>The southward-moving sheet of ice, flowing into the lowest lying portions of the plain, eroded the lowlands even more deeply.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [3A]",
      "B. [3B]",
      "C. [3C]",
      "D. [3D]"
    ],
    ans: 0,
    exp: "Câu trước vị trí [3A] mô tả: '...the location of the present-day Great Lakes was an area of low elevation in an inland plain.' (vị trí hiện tại của vùng Ngũ Hồ từng là một khu vực có độ cao thấp trong một đồng bằng nội địa). Câu đề bài: 'The southward-moving sheet of ice, flowing into the lowest lying portions of the plain, eroded the lowlands even more deeply.' (Dải băng di chuyển về phía nam, chảy vào những phần thấp nhất của đồng bằng, xói mòn các vùng đất thấp này sâu hơn nữa). Sự kết nối rõ ràng giữa 'an inland plain/low elevation' ở câu trước và 'portions of the plain/the lowlands' ở câu sau chỉ ra rằng [3A] là vị trí ghép nối tự nhiên và chuẩn xác nhất."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 6: Exercise 1",
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
  
  // Find Chapter 6 folder
  let chapterFolderId;
  const {data: existingFolder} = await supabase.from('folders').select('id').eq('parent_id', crashCourseFolderId).ilike('title', 'Chapter 6');
  
  if (existingFolder && existingFolder.length > 0) {
    chapterFolderId = existingFolder[0].id;
  } else {
    // get max display_order
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 6",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapterFolderId = newFolder[0].id;
    console.log("Created Chapter 6 folder!");
  }
  
  // check max test order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapterFolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 6: Exercise 1",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 6: Exercise 1").eq('course_id', courseId);
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
