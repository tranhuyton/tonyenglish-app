const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">The Origins of Writing</h2>
<p style="text-indent:2em;line-height:1.9;">Like the origins of graphic representation, the origins of true writing are also problematic. One specialist in the prehistoric uses of clay, Denise Schmandt-Besserat, suggests that true writing evolved directly from the shapes produced when such tokens were pressed into wet clay. According to her, clay tablets found at Uruk, Iraq, represent an evolutionary stage in a system of recording that had been in use in the Middle East since the first stages of the transition from a hunter-gatherer way of life to a more settled, agricultural life.</p>
<p style="text-indent:2em;line-height:1.9;">Four principal stages marked the evolution of writing. The first occurred about 10,500 years ago, when tokens of specific shapes were used to represent items, such as bread, sheep, and clothes. They seem to have served as invoices or bills. Thus, a herder selling ten sheep to someone in another village might give a middleman transporting the shipment a sealed pouch containing 10 tokens representing sheep - or perhaps one "sheep" token and one token representing the quantity 10.</p>
<p style="text-indent:2em;line-height:1.9;">The second stage began about 5,500 years ago, with the enclosure of tokens in hollow clay spheres. The personal seal of the seller was pressed into the fresh, wet clay on the outside of each sphere. The third stage began when people found that the need to break open the clay sphere to check the record, perhaps during shipment, could be avoided if a duplicate record was made by pressing each token on the outside of the sphere while the clay was still wet. Intact spheres have been found and the tokens inside have corresponded exactly to the impressions on the outside. Schmandt-Besserat suggests that these marks may be considered to be the crucial link between the old system of recording and writing.</p>
<p style="text-indent:2em;line-height:1.9;">The final stage occurred when the tokens themselves then became unnecessary, and full-fledged writing appeared. A pointed stick was used to inscribe the same symbols into clay. Besserat argues that new words were subsequently added.</p>
`;

const qList = [
  {
    q: "Select THREE answer choices.",
    opts: [
      "A. Although Schmandt-Besserat's theory of writing is interesting, the connection it makes between graphic representation and writing remains problematic.",
      "B. Early merchants used small clay tokens to represent their goods during shipping and trade transactions.",
      "C. The tokens used as invoices in the trade represented basic commodities including bread, sheep, and clothes.",
      "D. The system of tokens in trade grew increasingly representational and abstract over thousands of years.",
      "E. Intact spheres with the corresponding tokens inside show that people started to use duplicate records in wet clay.",
      "F. Eventually, the use of tokens was abandoned altogether in favor of symbols inscribed into clay tablets."
    ],
    ans: "1,3,5", // B, D, F using indices 1, 3, 5 for Checkbox.
    exp: "B đúng: Tóm lược giai đoạn 1 & 2 khi token đất sét được dùng đại diện hàng hóa trong buôn bán/vận chuyển.\nD đúng: Khái quát toàn bộ quá trình tiến hóa dài hàng ngàn năm, từ những vật thể thực (tokens) dần chuyển sang các hình thức trừu tượng và đại diện hơn (chữ viết/kí hiệu).\nF đúng: Nêu kết quả cuối cùng ở giai đoạn 4 (the final stage) khi token không còn cần thiết và được thay thế hoàn toàn bằng việc khắc kí hiệu lên đất sét.\nA sai: Đoạn văn mô tả lý thuyết của bà Besserat coi đây là 'crucial link' (mắt xích quan trọng) chứ không hề cho rằng sự kết nối này là 'problematic' (có vấn đề).\nC sai: Việc nhắc đến 'bread, sheep, and clothes' chỉ là một ví dụ quá nhỏ bé/tiểu tiết trong đoạn 2, không đủ tầm làm ý chính tóm tắt toàn bài.\nE sai: Mô tả việc tìm thấy các quả cầu đất sét nguyên vẹn chỉ là chi tiết minh họa cho giai đoạn 3, là một ý phụ (minor idea)."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 7: Exercise 2",
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
          content: `<p style="padding:12px;background:#f0f9ff;border-left:4px solid #2bd6eb;border-radius:8px;margin-bottom:12px;line-height:1.8;"><strong>Directions:</strong> An introductory sentence for a brief summary of the passage is provided below. Complete the summary by selecting <strong>THREE</strong> answer choices that express the most important ideas in the passage. Some sentences do not belong in the summary because they express ideas that are not presented in the passage or are minor ideas in the passage.</p><p style="padding:12px;background:#FFF9C4;border-radius:8px;font-weight:600;margin-bottom:16px;line-height:1.8;">"According to Denise Schmandt-Besserat, the origins of writing lay in early trade practices."</p>`,
          questionType: "Checkbox",
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
  
  // Find Chapter 7 folder
  let chapterFolderId;
  const {data: existingFolder} = await supabase.from('folders').select('id').eq('parent_id', crashCourseFolderId).ilike('title', 'Chapter 7');
  
  if (existingFolder && existingFolder.length > 0) {
    chapterFolderId = existingFolder[0].id;
  } else {
    // get max display_order
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 7",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapterFolderId = newFolder[0].id;
    console.log("Created Chapter 7 folder!");
  }
  
  // check max test order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapterFolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 7: Exercise 2",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 7: Exercise 2").eq('course_id', courseId);
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
