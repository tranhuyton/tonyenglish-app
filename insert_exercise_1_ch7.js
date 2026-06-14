const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Protozoa</h2>
<p style="text-indent:2em;line-height:1.9;">Among biologists, there is no real consensus as to what defines a protozoan. These organisms are classified in a kingdom of their own - the Protista - because they differ in some respects from bacteria, fungi, animals and plants. They have a more advanced organization than bacteria in that they possess distinct components such as nuclei and mitochondria. But they are distinguished from plants, animals and fungi in that they are unicellular. Some of them are plant-like, having the ability to photosynthesize, but most are non-photosynthetic, gaining nourishment by absorbing organic detritus or other micro-organisms.</p>
<p style="text-indent:2em;line-height:1.9;">There are nearly 30,000 different species of protozoa, single-celled microorganisms that live mostly in water or watery liquids. Abundant throughout the world, they may drift in their liquid environments, or actively swim or crawl along; a few remain relatively static and some live as parasites in animals. Many are microscopic, although some of the larger ones are visible to the naked eye. In form the protozoa are also amazingly diverse, from simple blob-like amoeba to those that are equipped with elaborate structures for catching prey, feeding and moving.</p>
<p style="text-indent:2em;line-height:1.9;">The actual sizes and shapes of protozoa are extraordinarily diverse, proving that protozoa represent a peak of unicellular evolution. The familiar amoeba, continually changing shape, is one type of protozoan. Others have contractile stalk-like elements, and yet others include foraminiferans, which are encased in coiled shells.</p>
<p style="text-indent:2em;line-height:1.9;">Protozoa are responsible for various human illnesses, including malaria and sleeping sickness, and also for many diseases in other animals, notably in cattle, fish, game and poultry. However, protozoa can be beneficial, and even essential to some animals. Ciliates are part of the microbe life in the rumen or stomach of cud chewing animals such as cows, helping to digest the enormous amount of cellulose present in the animal's diet, which it cannot digest itself. Protozoa are useful to humans in sewage treatment works, where they help to remove bacteria during processing.</p>
`;

const qList = [
  {
    q: "Select THREE answer choices.",
    opts: [
      "A. Although they share some characteristics of other kinds of organisms, protozoa are different from any of them.",
      "B. Protozoa are more like plants because they are photosynthetic organisms.",
      "C. Protozoa have complex internal structures and take on a wide variety of shapes and sizes.",
      "D. Most protozoa live in aquatic environments and actively swim to catch the parasites they feed on.",
      "E. Although protozoa are responsible for many illnesses, some form helpful, symbiotic relationships with their hosts.",
      "F. Protozoa require an enormous amount of cellulose, which they gain from the stomachs of cud chewing animals."
    ],
    ans: "0,2,4", // A, C, E using indices 0, 2, 4 for Checkbox.
    exp: "A đúng: Đoạn 1 nêu 'They are classified in a kingdom of their own... because they differ in some respects from bacteria, fungi, animals and plants.'\nC đúng: Đoạn 1 nêu chúng có 'nuclei and mitochondria', đoạn 2-3 khẳng định hình dạng và kích thước 'amazingly/extraordinarily diverse'.\nE đúng: Đoạn 4 nói chúng 'responsible for various illnesses' nhưng cũng 'can be beneficial... helping to digest cellulose'.\nB sai: Đoạn 1 nêu 'most are non-photosynthetic'.\nD sai: Đoạn 2 nói 'live mostly in water' nhưng 'some live as parasites', chứ không phải bơi đi săn ký sinh trùng.\nF sai: Ciliates giúp động vật phân giải cellulose trong thức ăn, chứ không phải bản thân protozoa cần nạp một lượng khổng lồ cellulose."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 7: Exercise 1",
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
          content: `<p style="padding:12px;background:#f0f9ff;border-left:4px solid #2bd6eb;border-radius:8px;margin-bottom:12px;line-height:1.8;"><strong>Directions:</strong> An introductory sentence for a brief summary of the passage is provided below. Complete the summary by selecting <strong>THREE</strong> answer choices that express the most important ideas in the passage. Some sentences do not belong in the summary because they express ideas that are not presented in the passage or are minor ideas in the passage.</p><p style="padding:12px;background:#FFF9C4;border-radius:8px;font-weight:600;margin-bottom:16px;line-height:1.8;">"Protozoa are unique unicellular life forms which are difficult to classify."</p>`,
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
    title: "Chapter 7: Exercise 1",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 7: Exercise 1").eq('course_id', courseId);
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
