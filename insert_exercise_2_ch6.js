const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">The Development of Computers</h2>
<p style="text-indent:2em;line-height:1.9;">The electronic computer is so much a part of our everyday lives that the present generation has difficulty imagining the world without it. Computers regulate temperature in buildings and operate traffic signals at intersections. Computers sit on our desktops at work and at home. We carry computers in our briefcases and even in our pockets. Computers help doctors diagnose illness, schedule patients for surgery at hospitals, and help to operate the surgical equipment in the operating room. <b>[1A]</b> Computers process food, fuel, and bank transactions. Almost all developments in science and engineering today are made possible by computers. <b>[1B]</b> Name almost any form of human activity, and there is a high probability that electronic computers have something to do with it. <b>[1C]</b> Computers are involved at the beginning, middle, and end of nearly everything we do. <b>[1D]</b></p>
<p style="text-indent:2em;line-height:1.9;">It may come as a surprise, then, to learn that the electronic computer is only about 60 years old. <b>[2A]</b> The emergence of the electronic computer was the culmination of a long series of events which began around the start of World War II. <b>[2B]</b> The Germans were using a mechanical encryption machine called Enigma to generate codes for military use. <b>[2C]</b> In principle, Enigma was so complex in its operation that its encoding was thought to be unbreakable. <b>[2D]</b> In fact, sophisticated machines were able to crack the German codes. One of the first code-breaking machines was built in Poland before the German invasion. Thereafter, progress was swift. The British quickly built much larger and more sophisticated machines, partly electronic and partly mechanical, to decipher German coded messages. <b>[3A]</b> These machines were so successful that the British were able to read German communications before Hitler himself could see them. <b>[3B]</b></p>
<p style="text-indent:2em;line-height:1.9;">Such "electromechanical" devices were developed both in Britain and the United States during the war. <b>[3C]</b> They were neither completely mechanical, as earlier computing machines had been, nor fully electronic, as later generations of computers would be. <b>[3D]</b> Although there is some debate about who invented the first electronic (as opposed to electromechanical) computer, it is widely believed that the first completely electronic computer in the US was the Electronic Numerical Integrator and Computer, or ENIAC, built at the University of Pennsylvania to help the Army calculate firing tables for artillery. Filled with thousands of vacuum tubes, ENIAC was a huge machine which filled an entire room. ENIAC was completed too late to affect the war effort greatly, but provided the model for many later machines.</p>
`;

const qList = [
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>Indeed, the invention of the computer is perhaps the most important single event of the 20th century.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [1A]",
      "B. [1B]",
      "C. [1C]",
      "D. [1D]"
    ],
    ans: 3,
    exp: "Cả đoạn 1 liệt kê một loạt các ứng dụng thiết yếu của máy tính trong mọi khía cạnh đời sống (điều hòa nhiệt độ, đèn giao thông, y tế, ngân hàng...). Kết lại chuỗi lập luận này bằng một câu đánh giá tổng quát: 'Indeed, the invention of the computer is perhaps the most important single event of the 20th century.' (Thật vậy, việc phát minh ra máy tính có lẽ là sự kiện quan trọng nhất của thế kỷ 20) ở vị trí [1D] là điểm chốt hoàn hảo để khép lại đoạn văn đầu tiên."
  },
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>Many persons now alive were born and raised before it was even invented.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [2A]",
      "B. [2B]",
      "C. [2C]",
      "D. [2D]"
    ],
    ans: 0,
    exp: "Câu đề bài viết: 'Many persons now alive were born and raised before it was even invented.' (Nhiều người hiện đang còn sống đã được sinh ra và lớn lên từ trước khi nó được phát minh). Câu này bổ sung ý nghĩa trực tiếp và làm rõ cho câu ngay trước vị trí [2A]: 'It may come as a surprise, then, to learn that the electronic computer is only about 60 years old.' (Sẽ thật ngạc nhiên khi biết rằng máy tính điện tử mới chỉ khoảng 60 năm tuổi). Sự ngắn ngủi của lịch sử máy tính giải thích lý do tại sao vẫn còn những người sinh ra trước cả khi nó xuất hiện."
  },
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br><br><b>It took about a decade to complete the transition from the mechanical era to the electronic era in computing.</b><br><br>Where would the sentence best fit?",
    opts: [
      "A. [3A]",
      "B. [3B]",
      "C. [3C]",
      "D. [3D]"
    ],
    ans: 3,
    exp: "Câu trước vị trí [3D] viết: 'They were neither completely mechanical, as earlier computing machines had been, nor fully electronic...' (Chúng không hoàn toàn là cơ học... cũng không hoàn toàn là điện tử...). Câu đề bài: 'It took about a decade to complete the transition from the mechanical era to the electronic era in computing.' (Phải mất khoảng một thập kỷ để hoàn thành quá trình chuyển đổi từ kỷ nguyên cơ học sang điện tử). Câu này đóng vai trò như một mắt xích tóm tắt quá trình chuyển giao ở đoạn này, để làm bước đệm cho câu tiếp theo nói về sự ra đời của ENIAC - máy tính điện tử hoàn toàn (completely electronic computer)."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 6: Exercise 2",
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
    title: "Chapter 6: Exercise 2",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 6: Exercise 2").eq('course_id', courseId);
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
