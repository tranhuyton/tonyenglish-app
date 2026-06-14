const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Herman Melville</h2>
<p style="text-indent:2em;line-height:1.9;">Melville's life, works and reputation are the stuff of legend. With very little formal education, he turned his early South Sea adventuring to literary use, charming readers in Britain and the United States with his first book, <i>Typee</i>, the story of his captivity by a Polynesian tribe. As the earliest personal account of the South Seas to have the readability and suspense of adventure fiction, it made a great sensation, capturing the imagination of both the literary reviewers and the reading public. Once established as a popular young author, he simultaneously began exploring philosophy and experimenting with literary style and form. Some readers were outraged, and for the rest of Melville's brief career he was torn between his own urge toward aesthetic and philosophical adventuring and the public's demand for racy sea stories which did not disturb its opinion on politics, religion and metaphysics. By his mid-thirties, broken in reputation and health, he ceased writing fiction, gradually passing into a stern and neglected middle age as a deputy customs inspector in Manhattan.</p>
<p style="text-indent:2em;line-height:1.9;">During the forty years he lived after publishing <i>Moby Dick</i>, Melville withdrew into the privacy of his family while men like <span class="amber-highlight">G. W. Curtis, R. H. Stoddard, E. C. Stedman, T. B. Aldrich, E. P. Whipple and R. W. Gilder</span> reigned over a magazine-dominated literary domain whose intellectual and artistic values formed a counterpart to the prevailing shoddiness of political values in post-Civil War America. Rediscovered by a few English readers just before his death, Melville was all but forgotten for another thirty years.</p>
<p style="text-indent:2em;line-height:1.9;">Finally the centennial of his birth brought about a revival of interest; by the 1920s, literary and cultural historians began to see Melville as the archetypal artist <span class="amber-highlight">in a money-grubbing century hostile to all grandeur of intellect and spirit</span>. That was a new distortion, but the "Melville Revival" of the 1920s succeeded in establishing him as one of the greatest American writers, although it took another decade or two for him to gain much space in college textbooks. The facts of his life are as poignant - and as archetypal - as the legends.</p>
`;

const qList = [
  {
    q: "In paragraph 1, the author describes Melville's exploration of philosophy and experimentation with style in order to",
    opts: [
      "A. illustrate Melville's career goals to the reader",
      "B. explain why his later writing was unpopular",
      "C. define the characteristics of great novels",
      "D. illustrate the effects his sea travels had on his writing"
    ],
    ans: 1,
    exp: "Đoạn 1 nêu: '...he simultaneously began exploring philosophy and experimenting with literary style and form. Some readers were outraged... broken in reputation and health, he ceased writing fiction...'. Tác giả miêu tả việc Melville khám phá triết học và thử nghiệm phong cách mới đã làm độc giả phẫn nộ (outraged), dẫn đến việc ông bị hủy hoại danh tiếng và phải ngừng viết. Điều này giải thích tại sao các tác phẩm sau này của ông không được ưa chuộng (unpopular)."
  },
  {
    q: "In paragraph 1, the author describes Melville's life and works by",
    opts: [
      "A. contrasting his life with other writers in his time",
      "B. presenting what happened in chronological order",
      "C. focusing on readers' response to his works",
      "D. emphasizing his achievements from an academic point of view"
    ],
    ans: 1,
    exp: "Đoạn 1 tóm tắt cuộc đời Melville theo trình tự thời gian (chronological order): từ những cuộc phiêu lưu tuổi trẻ (early adventuring), viết cuốn sách đầu tay (first book), trở thành tác giả trẻ nổi tiếng (popular young author), rồi bắt đầu thay đổi phong cách, sau đó bị mất danh tiếng ở độ tuổi giữa 30 (mid-thirties), và cuối cùng bước vào tuổi trung niên (middle age) làm nhân viên hải quan."
  },
  {
    q: "The author mentions **G. W. Curtis, R. H. Stoddard, E. C. Stedman, T. B. Aldrich, E. P. Whipple and R. W. Gilder** in the passage as examples of",
    opts: [
      "A. writers whose value had been neglected before the 1920s",
      "B. men who preserved intellectual and literary traditions in the post-Civil War era",
      "C. critics who were extremely harsh toward Melville's work",
      "D. Melville's contemporary writers who gained recognition while he was in withdrawal"
    ],
    ans: 3,
    exp: "Đoạn 2 viết: 'Melville withdrew into the privacy of his family while men like G. W. Curtis, ... reigned over a magazine-dominated literary domain...'. Tác giả nhắc đến những người này như những nhà văn cùng thời đã thống trị (reigned over/gained recognition) văn đàn, trong khi Melville rút lui khỏi giới văn chương (withdrew/withdrawal)."
  },
  {
    q: "The author describes the century in which Melville lived as **a money-grubbing century hostile to all grandeur of intellect and spirit** in order to",
    opts: [
      "A. suggest why Melville's writing was of such poor quality",
      "B. explain why Melville chose to remove himself from society",
      "C. reinforce the idea that Melville's writing was undervalued in his time",
      "D. question the validity of the \"Melville Revival\" of the 1920s"
    ],
    ans: 2,
    exp: "Đoạn 3 cho biết vào những năm 1920, các nhà sử học nhìn nhận Melville là một nghệ sĩ đích thực sống trong một thế kỷ 'hám tiền và thù địch với mọi sự vĩ đại của trí tuệ và tinh thần'. Việc miêu tả bối cảnh xã hội thù địch với nghệ thuật trí tuệ này nhằm củng cố (reinforce) ý tưởng rằng các tác phẩm của Melville đã bị đánh giá quá thấp (undervalued) so với giá trị thực trong chính thời đại của ông."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 5: Exercise 2",
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
  
  // Find Chapter 5 folder
  let chapter5FolderId;
  const {data: existingFolder} = await supabase.from('folders').select('id').eq('parent_id', crashCourseFolderId).ilike('title', 'Chapter 5');
  
  if (existingFolder && existingFolder.length > 0) {
    chapter5FolderId = existingFolder[0].id;
  } else {
    // get max display_order
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 5",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapter5FolderId = newFolder[0].id;
    console.log("Created Chapter 5 folder!");
  }
  
  // check max test order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapter5FolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 5: Exercise 2",
    course_id: courseId,
    folder_id: chapter5FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 5: Exercise 2").eq('course_id', courseId);
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
