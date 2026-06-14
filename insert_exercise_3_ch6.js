const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Biogenesis</h2>
<p style="text-indent:2em;line-height:1.9;"><b>[1A]</b> No principle of biology is more firmly established or less likely to be qualified than that of "biogenesis," which avows that all living things are descended from living things. <b>[1B]</b> In its negative form the principle would state that there is no such thing as "spontaneous generation" - e.g., the spontaneous generation of bacteria from putrefying organic matter or of protozoa from infusions of hay. <b>[1C]</b> Louis Pasteur, the greatest of all experimental biologists, is rightly credited with having carried out the experiments that falsified the notion of spontaneous generation of bacteria and at the same time made an alternative hypothesis much more attractive, viz. that the bacteria which so readily proliferate in warm organic broths derive from airborne organisms. <b>[1D]</b> This discovery, of which the medical significance was clearly perceived by Joseph Lister, lies at the root of all antiseptic and aseptic techniques in surgery today.</p>
<p style="text-indent:2em;line-height:1.9;">The principle of biogenesis applies not only to whole organisms but also to some of their constituent parts. Among cellular organelles the mitochondria are biogenetic in origin in the sense that they do not arise <i>de novo</i> by some synthetic process in the cell but are derived from pre-existing mitochondria only. Biogenesis does not imply evolution, but an evolutionary relationship does of course imply biogenesis. <b>[2A]</b> Normal biogenesis is often given the extra connotation of "homogenesis," i.e. of like begetting like. <b>[2B]</b> Broadly speaking this particularization is true, although the theory of evolution obliges us to qualify it in detail. <b>[2C]</b> No genuinely extravagant heterogenesis occurs, although in the days before empirical truthfulness was thought to be either a necessary or desirable characteristic of professedly factual statements; all kinds of strange notions were rife - the most famous being the myth that geese might be born of such organisms as the attractive barnacle-like crustacean the goose barnacle, <i>Lepas anatifera</i>. <b>[2D]</b></p>
`;

const qList = [
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>In other words, behind each living organism today there is an unbroken lineage of descent going back to the beginnings of biological time.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [1A]",
      "B. [1B]",
      "C. [1C]",
      "D. [1D]"
    ],
    ans: 1,
    exp: "Câu ngay trước vị trí [1B] giải thích khái niệm cơ bản của nguyên lý 'biogenesis' (thuyết sinh nguyên): '...which avows that all living things are descended from living things' (thừa nhận rằng tất cả các sinh vật sống đều bắt nguồn từ các sinh vật sống). Câu đề bài viết: 'In other words, behind each living organism today there is an unbroken lineage of descent...' (Nói cách khác, đằng sau mỗi sinh vật sống ngày nay là một dòng dõi truyền thừa không gián đoạn...). Cụm từ nối 'In other words' (Nói cách khác) cho thấy câu này đang diễn giải lại nội dung ở câu trước một cách chi tiết hơn. Vì vậy, [1B] là vị trí chuẩn xác nhất."
  },
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>Such notions belong to \"poetism,\" a style of thinking which arouses as much indignation among scientists as the more idiotic extravagances of computerized literary criticism arouse in lovers of literature.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [2A]",
      "B. [2B]",
      "C. [2C]",
      "D. [2D]"
    ],
    ans: 3,
    exp: "Câu ngay trước vị trí [2D] nhắc đến việc trong quá khứ có rất nhiều niềm tin và quan niệm kỳ lạ từng lan truyền: '...all kinds of strange notions were rife - the most famous being the myth that geese might be born of... the goose barnacle...' (...đủ loại quan niệm kỳ lạ nhan nhản - nổi tiếng nhất là huyền thoại rằng ngỗng có thể được sinh ra từ con hà ngỗng). Câu đề bài bắt đầu bằng: 'Such notions belong to \"poetism\"...' (Những quan niệm như vậy thuộc về 'chủ nghĩa thi ca'...). Cụm từ 'Such notions' (Những quan niệm như vậy) có chức năng liên kết, trỏ ngược lại chính xác vào 'strange notions' và ví dụ thần thoại về loài ngỗng vừa được nhắc tới trước đó. Do vậy, phải đặt ở vị trí [2D]."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 6: Exercise 3",
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
    title: "Chapter 6: Exercise 3",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 6: Exercise 3").eq('course_id', courseId);
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
