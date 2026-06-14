const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">DNA Fingerprinting</h2>
<p style="text-indent:2em;line-height:1.9;">An individual's DNA is as distinctive as a fingerprint and, in certain types of violent crime, more likely to be obtainable. The method for "DNA fingerprinting" which was devised by Alec Jeffreys of the University of Leicester in England, is basically simple. The eukaryotic genome contains many regions of simple-sequence DNA, identical short nucleotide sequences lined up in tandem and recurring thousands of times. Jeffreys noted that the number of repeated units in such regions differs distinctively from individual to individual. The regions can be excised from the total DNA by the use of appropriate restriction enzymes, placed on an electrophoretic gel, separated by length, denatured, and identified by a radioactive probe. When the process is completed, the end result, visible on x-ray film, looks like the <span class="amber-highlight">bar code</span> on a supermarket package.</p>
<p style="text-indent:2em;line-height:1.9;">Such a DNA bar code helped to convict Randall Jones, now on Death Row in Florida. Jones's car got stuck in the mud. In search of a tow, he found a young couple asleep in a pickup truck parked by a fishing ramp. He shot each of them in the head with a rifle, dragged their bodies into the woods, used the truck to pull out his car, and then went back and raped the woman. In such cases, standard blood or semen analysis can identify a suspect with a certainty of about 90 to 95 percent, leaving some room for argument. However, Jones's DNA pattern, which matched the sperm found in the victim's body, could occur in only one person out of 9.34 billion - which is significantly more than the present population of the world.</p>
<p style="text-indent:2em;line-height:1.9;">Often only very small samples of biological evidence are found at a crime scene. A gene amplification method known as PCR, or polymerase chain reaction, has been developed that can take a minute fragment of DNA and synthesize millions of copies. Gene amplification has made it possible to obtain DNA fingerprints from trace amounts of blood and semen and even from the root of a single hair. It has been used to speed up prenatal diagnosis of genetic disease and to detect latent virus infections. It also made possible the analysis of mitochondrial DNA from a <span class="amber-highlight">wooly mammoth that died some 40,000 years ago</span>.</p>
`;

const qList = [
  {
    q: "Why does the author discuss a **bar code** in the passage?",
    opts: [
      "A. To illustrate the alternative uses of DNA fingerprinting",
      "B. To better illustrate the appearance of DNA x-rays",
      "C. To describe the chemical action of enzymes on DNA",
      "D. To illustrate the precision of DNA fingerprinting"
    ],
    ans: 1,
    exp: "Cuối đoạn 1 viết: 'When the process is completed, the end result, visible on x-ray film, looks like the bar code on a supermarket package.' Việc nhắc đến mã vạch (bar code) là để giúp người đọc dễ hình dung diện mạo/hình ảnh của phim X-quang DNA (appearance of DNA x-rays)."
  },
  {
    q: "The author discusses the case of Randall Jones in paragraph 2 in order to",
    opts: [
      "A. compare his case with other crimes that happened before the invention of DNA fingerprinting",
      "B. argue that DNA fingerprinting should only be used for convicting violent criminals",
      "C. suggest that Randall Jones committed an organized crime",
      "D. explain how DNA fingerprinting improves the chance of convicting criminals"
    ],
    ans: 3,
    exp: "Đoạn 2 đưa ra vụ án của Randall Jones để so sánh giữa phân tích máu/tinh dịch thông thường (chỉ chắc chắn 90-95%, vẫn có thể tranh cãi) với phân tích DNA (xác suất trùng hợp chỉ 1 trên 9.34 tỷ người). Qua đó, vụ án này nhằm giải thích việc lấy dấu vân tay DNA đã cải thiện/tăng cường khả năng kết án tội phạm (improves the chance of convicting criminals) như thế nào."
  },
  {
    q: "In paragraph 2, the author discusses world population in order to",
    opts: [
      "A. suggest the unlikelihood of mistakes in DNA fingerprinting",
      "B. show the rarity with which extremely violent crimes are committed",
      "C. demonstrate the improbability of solving crimes with DNA fingerprinting",
      "D. indicate that DNA fingerprinting is now used in law enforcement worldwide"
    ],
    ans: 0,
    exp: "Cuối đoạn 2 viết mô hình DNA của Jones chỉ có thể trùng lặp với 1 người trong số 9.34 tỷ người - 'which is significantly more than the present population of the world' (lớn hơn đáng kể so với dân số thế giới hiện tại). Sự so sánh này nhằm nhấn mạnh xác suất nhầm lẫn là gần như không thể, gợi ý sự khó có thể xảy ra sai sót (unlikelihood of mistakes) trong phân tích DNA."
  },
  {
    q: "Why does the author mention a **wooly mammoth that died some 40,000 years ago**?",
    opts: [
      "A. To illustrate another way DNA analysis can be used",
      "B. To further explain the use of DNA analysis in medicine",
      "C. To support the idea that the use of DNA fingerprinting should be prohibited",
      "D. To explain why wooly mammoths became extinct"
    ],
    ans: 0,
    exp: "Trong đoạn 3, tác giả liệt kê hàng loạt các ứng dụng của phương pháp khuếch đại gen (PCR/DNA analysis): tìm thủ phạm từ dấu vết nhỏ, chẩn đoán bệnh di truyền trước sinh, phát hiện virus tiềm ẩn, và 'It also made possible the analysis of mitochondrial DNA from a wooly mammoth...'. Do đó, việc nhắc đến voi ma mút lông cừu nhằm cung cấp thêm một ví dụ/một cách khác mà phân tích DNA có thể được sử dụng (illustrate another way DNA analysis can be used)."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 5: Exercise 3",
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
    title: "Chapter 5: Exercise 3",
    course_id: courseId,
    folder_id: chapter5FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 5: Exercise 3").eq('course_id', courseId);
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
