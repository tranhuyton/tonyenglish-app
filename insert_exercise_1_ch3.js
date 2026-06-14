const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Newspapers in Post-Civil War America</h2>
<p style="text-indent:2em;line-height:1.9;">Before the arrival of television and radio, newspapers were the only source of information for the general public. In a country as vast as the United States, newspapers played a crucial role in the daily lives of the people. They were the fastest, most efficient way to inform people living in such an immense territory. Newspapers were popular in the post-Civil War period. Circulation of newspapers in the United States increased remarkably after the Civil War. Analytical, in-depth reporting made good reading, but it could antagonize readers. Such reporting was often replaced by features in order to avoid offending advertisers upon whom the papers depended for their profits. What the reader pays for a newspaper has never covered the cost of publishing. Advertising has been the great source of income in the publishing business.</p>
<p style="text-indent:2em;line-height:1.9;">Joseph Pulitzer, who began with a St. Louis newspaper and moved to New York, introduced the idea of the "yellow press," which was named for the "yellow kid" in his colored comic page in the <i>New York World</i>. Yellow journalism is synonymous with sensationalism, which served as a sales strategy. Papers battling for more readers and more advertising struggled to outdo each other in reporting scandals. William Hearst in the <i>San Francisco Examiner</i> was another noted practitioner of yellow journalism. Both he and Pulitzer built large publishing empires. Editors' competition for readers led to emotional and ultimately distorted reporting, such as the international situation in Cuba in the 1890s. The press had a major role in bringing the US into the Spanish-American War. Hearst became notorious for fostering the war through skewed reporting.</p>
<p style="text-indent:2em;line-height:1.9;">Though the press might have played a questionable role in some cases, it helped to bring about much-needed urban reform. Magazines such as <i>Harpers</i>, <i>Scribner's Monthly</i> and <i>The Nation</i> published well-researched stories of corruption in cities and business. Influential leaders of business and government read these accounts and worked hard to amend the situation.</p>
`;

const qList = [
  {
    q: "According to paragraph 1, advertisers had influence over newspapers because",
    opts: [
      "A. newspapers relied on them to increase circulation",
      "B. newspapers needed their revenue to cover their overhead",
      "C. advertisers helped increase the sales price of newspapers",
      "D. advertisers helped newspapers recover in the post-Civil War period"
    ],
    ans: 1,
    exp: "Ý gốc trong bài: 'What the reader pays for a newspaper has never covered the cost of publishing. Advertising has been the great source of income in the publishing business.' -> Tiền độc giả trả không bao giờ đủ trang trải chi phí xuất bản, và quảng cáo là nguồn thu nhập lớn. Do đó báo chí cần doanh thu từ họ để trang trải chi phí."
  },
  {
    q: "According to paragraph 1, why were newspapers so crucial to daily life in America?",
    opts: [
      "A. They helped reunite the nation in the post-Civil War period.",
      "B. They helped advertisers reach consumers.",
      "C. They transmitted information reliably over long distances.",
      "D. They were careful never to antagonize their readers."
    ],
    ans: 2,
    exp: "Ý gốc: 'In a country as vast as the United States... They were the fastest, most efficient way to inform people living in such an immense territory.' -> Mỹ là một quốc gia rộng lớn, báo chí là cách nhanh nhất và hiệu quả nhất để thông tin cho người dân sống trên một vùng lãnh thổ bao la. -> Truyền thông tin đi xa."
  },
  {
    q: "In paragraph 2, all of the following are mentioned as aspects of the yellow press EXCEPT",
    opts: [
      "A. biased, unreliable reporting",
      "B. focus on scandals and sensationalism",
      "C. focus on sales rather than honest reporting",
      "D. emphasis on comics rather than news stories"
    ],
    ans: 3,
    exp: "Trong đoạn 2, 'distorted reporting' tương ứng với phương án A; 'reporting scandals' và 'sensationalism' tương ứng với B; 'sales strategy' tương ứng với C. Chỉ có phương án D (nhấn mạnh vào truyện tranh thay vì tin bài) là KHÔNG được đề cập như một đặc điểm của 'báo chí lá cải' (truyện tranh 'yellow kid' chỉ là nguồn gốc tên gọi, không phải là đặc điểm đưa tin)."
  },
  {
    q: "According to the passage, what positive effect did the yellow press have?",
    opts: [
      "A. It helped to prevent unnecessary wars.",
      "B. Reporting on scandals helped fight corruption.",
      "C. It brought Cuba to international attention.",
      "D. It prevented the emergence of large media empires."
    ],
    ans: 1,
    exp: "Ý gốc ở đoạn 3: 'it helped to bring about much-needed urban reform... published well-researched stories of corruption in cities and business.' -> Đưa tin về các vụ bê bối đã giúp đấu tranh chống tham nhũng và mang lại các cải cách đô thị cần thiết."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 3: Exercise 1",
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
  
  // Find or create Chapter 3 folder
  let chapter3FolderId;
  const {data: existingFolder} = await supabase.from('folders').select('id').eq('parent_id', crashCourseFolderId).ilike('title', 'Chapter 3');
  
  if (existingFolder && existingFolder.length > 0) {
    chapter3FolderId = existingFolder[0].id;
  } else {
    // get max display_order
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 3",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapter3FolderId = newFolder[0].id;
    console.log("Created Chapter 3 folder!");
  }
  
  // check max test order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapter3FolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 3: Exercise 1",
    course_id: courseId,
    folder_id: chapter3FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 3: Exercise 1").eq('course_id', courseId);
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
