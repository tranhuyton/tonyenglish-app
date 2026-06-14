const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Emily Dickinson</h2>
<p style="text-indent:2em;line-height:1.9;">One of the greatest American poets, Emily Elizabeth Dickinson is well known for her eccentric lifestyle and character. She was born in Amherst, Massachusetts, and during her lifetime she led an extremely confined and reclusive existence. But to think of Emily Dickinson only as an eccentric recluse is a serious mistake. Like Thoreau, she lived simply and deliberately; she faced the essential facts of life. In Henry James's phrase, she was one of those on whom nothing was lost. Only by living austerely and intensely could Dickinson manage both to fulfill what for her were the strenuous physical and emotional obligations of a daughter, a sister, a sister-in-law, citizen and housekeeper, and write on the average a poem a day.</p>
<p style="text-indent:2em;line-height:1.9;">Her relationship to books reflects her emotional ties with the few men in her life. She was no ransacker and devourer of libraries. Like Lincoln, she knew relatively few volumes but she understood them deeply. As a girl she attended Amherst Academy and also Mount Holyoke Female Seminary, but school gave her neither intellectual nor social satisfactions to compensate for the reassuring intimacy of home and family she keenly missed. The standard works she knew best and drew on most commonly for allusions and references in her poetry and vivid letters were the classic myths, the Bible, and Shakespeare. Among the English Romantics, she valued John Keats especially; among her English contemporaries she was particularly attracted by the Brontës, the Brownings, Lord Tennyson, and George Eliot. None of these, however, can be said to have influenced her literary practice significantly. Indeed, not the least notable quality of her poetry is its dazzling originality. Thoreau and Emerson, notably the latter, as we know from her letters, were perhaps her most important contemporary American intellectual resources, though their liberal influence seems to have been tempered by the legacy of a conservative Puritanism best expressed in the writings of Jonathan Edwards. Her chief prosodic and formal models were the commonly used hymnals of the times, with their simple patterns of meter and rhyme.</p>
<p style="text-indent:2em;line-height:1.9;">Despite its ostensible formal simplicity, Dickinson's poetry is remarkable for its variety, subtlety, and richness. From the beginning, she has attracted both popular and specialized audiences: those who find satisfaction in the sometimes quaint, aphoristic generalizing tendency in her work, as well as those who take pleasure in the experimental, intellectually dense and often darker awareness that marks her most sophisticated poems. There is very little dispute regarding her claim to a very high place among America's poets.</p>
`;

const qList = [
  {
    q: "Select THREE answer choices.",
    opts: [
      "A. Although Dickinson was reclusive, she managed to lead a functional home life and find enough time to write.",
      "B. Dickinson did not find school a satisfying experience because it was not as intellectually challenging nor as comforting as home.",
      "C. Dickinson preferred the writing contained in the Bible and other older texts to that of her contemporaries.",
      "D. While she valued the work of many authors and drew upon their work as resources, Dickinson's writing was strikingly original.",
      "E. Thoreau and Emerson's liberal influence on Dickinson was weakened by the tradition of a conservative Puritanism.",
      "F. Dickinson's poetry shows a perfect balance between literary formalism and flexibility."
    ],
    ans: "0,3,5", // A, D, F using indices 0, 3, 5 for Checkbox.
    exp: "A đúng: Tóm tắt đoạn 1, dù sống ẩn dật (reclusive), bà vẫn làm tròn bổn phận gia đình (functional home life) và viết trung bình một bài thơ mỗi ngày (find enough time to write). Điều này bổ sung cho vế 'eccentric lifestyle' của câu chủ đề.\nD đúng: Tóm tắt đoạn 2, bài nói bà đọc/biết nhiều tác giả (Shakespeare, Keats, Bronte, Thoreau...) nhưng tác phẩm của bà có sự độc đáo đáng kinh ngạc ('dazzling originality'), củng cố vế 'excellence of her poetry'.\nF đúng: Tóm tắt đoạn 3, thơ bà mang vẻ bề ngoài đơn giản về hình thức ('formal models were the commonly used hymnals... formal simplicity') nhưng lại rất đa dạng và mang tính thể nghiệm ('variety, subtlety, experimental...'). Sự cân bằng giữa tính hình thức (formalism) và sự linh hoạt (flexibility) tạo nên sức hấp dẫn lớn.\nB sai: Đây là chi tiết nhỏ (minor detail) trong đoạn 2, không khái quát được ý chính toàn bài.\nC sai: Nội dung bài không cho thấy bà 'thích' (preferred) Kinh Thánh hơn tác phẩm của những người cùng thời. Bà đọc cả hai và đều coi trọng.\nE sai: Việc ảnh hưởng của Thoreau và Emerson bị kìm hãm bởi tư tưởng Thanh giáo cũng chỉ là một tiểu tiết rất nhỏ trong đoạn 2."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 7: Exercise 3",
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
          content: `<p style="padding:12px;background:#f0f9ff;border-left:4px solid #2bd6eb;border-radius:8px;margin-bottom:12px;line-height:1.8;"><strong>Directions:</strong> An introductory sentence for a brief summary of the passage is provided below. Complete the summary by selecting <strong>THREE</strong> answer choices that express the most important ideas in the passage. Some sentences do not belong in the summary because they express ideas that are not presented in the passage or are minor ideas in the passage.</p><p style="padding:12px;background:#FFF9C4;border-radius:8px;font-weight:600;margin-bottom:16px;line-height:1.8;">"Emily Dickinson is known both for her eccentric lifestyle and for the excellence of her poetry."</p>`,
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
    title: "Chapter 7: Exercise 3",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 7: Exercise 3").eq('course_id', courseId);
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
