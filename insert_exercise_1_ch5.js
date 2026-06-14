const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Cetaceans</h2>
<p style="text-indent:2em;line-height:1.9;">The largest group of marine mammals is the cetaceans, the whales, dolphins and porpoises. Of all marine mammals, the cetaceans have made the most complete transition to aquatic life. Whereas <span class="amber-highlight">most other marine mammals</span> return to land at least part of the time, cetaceans spend their entire lives in the water. Their bodies are streamlined and look remarkably fish-like. This is a dramatic example of convergent evolution, where different species develop similar structures because they have similar lifestyles. Although they superficially resemble fishes, cetaceans breathe air and will drown if trapped below the surface. They are "warm-blooded," have hair, though scanty, and produce milk for their young.</p>
<p style="text-indent:2em;line-height:1.9;">Cetaceans have a pair of front flippers, but the rear pair of limbs has disappeared. Actually, the rear limbs are present in the embryo but fail to develop. In adults they remain only as small, useless bones. These bones, however, are important from a scientific point of view because they definitely link cetaceans to land mammals in the evolutionary chain. In most cetaceans, the hind legs have given way to a muscular tail that ends in a pair of fin-like, horizontal flukes. Blubber provides insulation and buoyancy; body hair is practically absent. Rather than being on the front of the head, the nostrils are on top, forming a single or double opening called the blowhole.</p>
<p style="text-indent:2em;line-height:1.9;">There are around 90 species of cetaceans. They are all ocean dwelling except for five species of freshwater dolphins. Cetaceans are divided into two groups: the toothless, filter-feeding whales and the toothed, carnivorous whales, a group that includes the dolphins and porpoises. The toothless whales are better known as the baleen whales. Instead of teeth they have rows of flexible, fibrous plates named baleen that hang from the upper jaw. Baleen is made of the same material as our hair and nails. These plates act as <span class="amber-highlight">sieves</span>, filtering plankton from the water.</p>
`;

const qList = [
  {
    q: "The author mentions **most other marine mammals** in order to",
    opts: [
      "A. suggest cetaceans are more advanced than other marine mammals",
      "B. indicate the evolutionary origins of cetaceans",
      "C. emphasize how completely cetaceans have adapted to aquatic life",
      "D. reinforce the fact that cetaceans are not a species of fish"
    ],
    ans: 2,
    exp: "Đoạn 1 viết: 'Whereas most other marine mammals return to land at least part of the time, cetaceans spend their entire lives in the water.' Tác giả so sánh Cetaceans với hầu hết các động vật có vú ở biển khác để nhấn mạnh rằng Cetaceans đã thích nghi hoàn toàn tuyệt đối với cuộc sống dưới nước (chứ không cần lên bờ như những loài kia)."
  },
  {
    q: "In paragraph 2, why does the author discuss the hind legs of cetaceans?",
    opts: [
      "A. To explain how animals evolve to adapt to their environment",
      "B. To suggest that cetaceans are slowly evolving into fish",
      "C. To discuss the evidence linking cetaceans to land mammals",
      "D. To better explain the shape of the tail and flukes in cetaceans"
    ],
    ans: 2,
    exp: "Đoạn 2 nhắc đến tàn tích của đôi chân sau (hind legs/rear limbs) của Cetaceans và khẳng định: 'These bones, however, are important from a scientific point of view because they definitely link cetaceans to land mammals in the evolutionary chain.' -> Đóng vai trò là bằng chứng liên kết chúng với động vật có vú trên cạn."
  },
  {
    q: "In paragraph 2, the author discusses cetaceans by",
    opts: [
      "A. listing several body parts that are characteristic of cetaceans",
      "B. comparing cetaceans with other sea animals",
      "C. showing similarities between cetaceans and land mammals",
      "D. explaining the evolutionary process through which cetaceans became mammals"
    ],
    ans: 0,
    exp: "Trong suốt đoạn 2, tác giả chủ yếu liệt kê hàng loạt các bộ phận cơ thể đặc trưng của Cetaceans để mô tả chúng, bao gồm: front flippers (vây trước), rear limbs/bones (chân sau), muscular tail (đuôi cơ bắp), flukes (vây đuôi), blubber (mỡ), body hair (lông), blowhole (lỗ thở)."
  },
  {
    q: "The author mentions **sieves** in the passage in order to",
    opts: [
      "A. describe what baleen looks like",
      "B. explain the function of baleen",
      "C. identify what baleen is made of",
      "D. give an example of the objects that can be used instead of baleen"
    ],
    ans: 1,
    exp: "Cuối đoạn 3 viết: 'These plates act as sieves, filtering plankton from the water.' Tác giả ví tấm sừng hàm (baleen) hoạt động như một cái rây/sàng lọc (sieves) nhằm mục đích giải thích rõ chức năng của chúng là để lọc sinh vật phù du ra khỏi nước."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 5: Exercise 1",
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
    title: "Chapter 5: Exercise 1",
    course_id: courseId,
    folder_id: chapter5FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 5: Exercise 1").eq('course_id', courseId);
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
