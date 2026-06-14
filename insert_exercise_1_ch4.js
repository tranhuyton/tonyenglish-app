const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Labor Unions in the United States</h2>
<p style="text-indent:2em;line-height:1.9;">The establishment of the American labor union was by no means an easy task. The workers were able to succeed only after much repeated failure. The first unions of workers came during the era of Jacksonian Democracy and were local. In the post-Civil War period attempts were made to create organizations of workers on a national basis. The National Labor Union was created in 1866 with the goal of establishing the eight-hour day. In 1868, Congress passed an eight-hour day for mechanics and laborers who worked for the US government, but progress elsewhere was slow. In 1872, after turning to national politics, the National Labor Union collapsed. After the Panic of 1873, there was labor agitation, but labor unions were unsuccessful in organizing support and eliminating unrest.</p>
<p style="text-indent:2em;line-height:1.9;">In 1878, the Knights of Labor was organized as a national union of both skilled and unskilled workers. Their platform called for the eight-hour day, boycotts not strikes, a graduated income tax, and consumer cooperatives. The Knights forced some concessions from several railways but collapsed after a general strike for an eight-hour day failed in Chicago and the Haymarket Massacre of 1886. One of the key weaknesses lay in the effort to bring together all workers, skilled and unskilled, whose wage levels and concerns differed greatly.</p>
<p style="text-indent:2em;line-height:1.9;">The next national union to be founded, the American Federation of Labor (AFL), was formed in 1886. It concentrated on organizing skilled workers. It continues today as the important AFL-CIO. Under its first president, Samuel Gompers, the AFL recognized the autonomy of each specialized trade, such as carpenters or cigar makers. The AFL formed the coordinating group for these separate trades. Its program included laws curbing immigration, introduction of new machines and labor legislation to include the eight-hour day and workmen's compensation.</p>
`;

const qList = [
  {
    q: "What can be inferred about work hours in the US?",
    opts: [
      "A. They are typically longer for unskilled laborers.",
      "B. They were higher than 8 hours a day before the Civil War.",
      "C. They were tied to wage levels in many companies.",
      "D. They were the only concern of the first labor unions."
    ],
    ans: 1,
    exp: "Đoạn 1 đề cập rằng Liên đoàn Lao động Quốc gia (National Labor Union) được thành lập sau Nội chiến (1866) với mục tiêu thiết lập ngày làm việc 8 giờ ('with the goal of establishing the eight-hour day'). Điều này có thể suy ra (infer) rằng trước thời điểm đó, giờ làm việc mỗi ngày phải cao hơn 8 giờ thì họ mới cần đấu tranh để giảm xuống mức này."
  },
  {
    q: "Which of the following can be inferred from paragraph 2 about labor strikes in the US?",
    opts: [
      "A. They ceased with the creation of labor unions.",
      "B. They were an important means for labor unions to achieve their goals.",
      "C. They were more common among unskilled workers.",
      "D. They reached their highest levels in 1878."
    ],
    ans: 1,
    exp: "Trong đoạn 2, nghiệp đoàn Knights of Labor dù chủ trương 'boycotts not strikes' (tẩy chay chứ không đình công) nhưng cuối cùng vẫn phải thực hiện một cuộc tổng đình công ('a general strike') để đòi ngày làm việc 8 giờ. Dù cuộc đình công này thất bại dẫn tới sự sụp đổ của họ, nhưng điều này cho thấy đình công là một phương thức đấu tranh quan trọng không thể thiếu của các nghiệp đoàn để đạt được mục tiêu."
  },
  {
    q: "It can be inferred from paragraph 3 that skilled laborers",
    opts: [
      "A. were mainly engaged in cigar making and carpentry",
      "B. held extremely independent attitudes that made it hard to form unions",
      "C. were generally opposed to greater levels of immigration",
      "D. were far more politically active than unskilled laborers"
    ],
    ans: 2,
    exp: "Đoạn 3 cho biết nghiệp đoàn AFL tập trung vào việc tổ chức các lao động có tay nghề (skilled workers). Và chương trình hành động của AFL bao gồm việc thúc đẩy các đạo luật hạn chế nhập cư ('laws curbing immigration'). Từ đó có thể suy ra rằng những lao động có tay nghề (đại diện bởi AFL) nhìn chung là phản đối tình trạng nhập cư ngày càng tăng."
  },
  {
    q: "It can be inferred from the passage that labor unions are effective when",
    opts: [
      "A. they focus on a particular class of workers and specific goals",
      "B. there are limitations on their engagement in politics",
      "C. they are organized by skilled workers rather than by unskilled workers",
      "D. they sometimes use violence during strikes"
    ],
    ans: 0,
    exp: "Đoạn 1 cho thấy National Labor Union sụp đổ sau khi chuyển hướng sang chính trị quốc gia (không tập trung vào mục tiêu cụ thể cho lao động). Đoạn 2 cho thấy Knights of Labor thất bại do cố gắng gộp chung cả lao động có tay nghề và không có tay nghề - những người có khác biệt lớn về mức lương và mối quan tâm. Ngược lại, đoạn 3 cho thấy AFL thành công và tồn tại đến ngày nay vì họ tập trung tổ chức một nhóm lao động cụ thể ('concentrated on organizing skilled workers') và tôn trọng tính tự chủ của từng ngành nghề riêng biệt. Do đó, nghiệp đoàn hiệu quả nhất khi họ tập trung vào một tầng lớp lao động cụ thể và các mục tiêu rõ ràng."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 4: Exercise 1",
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
    title: "Chapter 4: Exercise 1",
    course_id: courseId,
    folder_id: chapter4FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 4: Exercise 1").eq('course_id', courseId);
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
