const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Defining Species</h2>
<p style="text-indent:2em;line-height:1.9;">The word "species" in Latin simply means "kind," and so species are different kinds of organisms. A more vigorous definition of species was set forth in 1940 by Ernst Mayr, who said that species are "groups of actually or potentially interbreeding natural populations which are reproductively isolated from other such groups." The phrase "actually or potentially" allows for the fact that although members of the human population of Greenland are not likely to interbreed with those of Patagonia, they are still members of the human species; similarly, transporting a group of insects to some remote island does not automatically make them members of another species. The words "groups" and "populations" are important also. The possibility that single individuals of different species may have occasional offspring is unimportant in terms of the group. For example, horses and donkeys may occasionally mate, but their offspring, mules, do not represent a distinct species because they are always barren and may not reproduce themselves, and thus do not represent a natural population. Such offspring are referred to as infertile hybrids rather than as a new species. Mayr's definition conforms to common sense: if members of one species freely exchanged genes with members of another species, they could no longer retain those unique characteristics that identify them as different kinds of organisms.</p>
<p style="text-indent:2em;line-height:1.9;">This definition works well for animal species and is generally accepted by zoologists. Many plants, however, can reproduce asexually and also can form fertile hybrids with other species. Bacteria, with their variety of forms of genetic exchange, do not fit into this definition easily, nor do the many unicellular eukaryotes that reproduce by cell division, forming clones of identical cells. Thus, although botanists and microbiologists use the term "species," they are more likely to consider it a category of convenience.</p>
<p style="text-indent:2em;line-height:1.9;">From an evolutionary perspective, however, a species is a group or population of organisms, reproductively united but very probably changing as it moves through space and time. Splinter groups, reproductively isolated from the population as a whole, can undergo sufficient change that they become new species. This process is known as speciation. Occurring repeatedly in the course of more than 3.5 billion years, it has given rise to the diversity of organisms that have lived in the past and that live today.</p>
`;

const qList = [
  {
    q: "According to the passage, all of the following are definitive aspects of a species EXCEPT",
    opts: [
      "A. a common geographic location",
      "B. the ability to reproduce",
      "C. a common set of characteristics",
      "D. naturally occurring populations"
    ],
    ans: 0,
    exp: "Ý gốc đoạn 1: '...although members of the human population of Greenland are not likely to interbreed with those of Patagonia, they are still members of the human species; similarly, transporting a group of insects to some remote island does not automatically make them members of another species.' -> Vị trí địa lý không phải là yếu tố quyết định một loài. Khả năng sinh sản, đặc điểm chung, và quần thể tự nhiên đều được nhắc đến như khía cạnh của loài."
  },
  {
    q: "According to paragraph 1, mules do not represent a distinct species because",
    opts: [
      "A. they are only occasionally produced through mating between horses and donkeys",
      "B. they are sterile and cannot carry on their bloodlines",
      "C. they lack a definitive set of genetic characteristics",
      "D. their populations are limited and widely dispersed"
    ],
    ans: 1,
    exp: "Ý gốc đoạn 1: 'their offspring, mules, do not represent a distinct species because they are always barren and may not reproduce themselves...' -> Con la không phải là một loài riêng biệt vì chúng vô sinh (barren = sterile) và không thể tự sinh sản."
  },
  {
    q: "According to paragraph 2, a definition of species for plants and bacterial organism is more difficult because",
    opts: [
      "A. they possess a wider array of reproductive mechanisms",
      "B. they frequently change their definitive characteristics",
      "C. it is less convenient to categorize these organisms",
      "D. they do not participate in genetic exchange"
    ],
    ans: 0,
    exp: "Ý gốc đoạn 2: 'Many plants, however, can reproduce asexually and also can form fertile hybrids... Bacteria, with their variety of forms of genetic exchange, do not fit into this definition easily...' -> Thực vật và vi khuẩn có nhiều cơ chế sinh sản đa dạng hơn (vô tính, lai hữu thụ, nhiều hình thức trao đổi gen) nên khó áp dụng định nghĩa gốc."
  },
  {
    q: "What role does speciation play in the ecology of the Earth?",
    opts: [
      "A. It provides an evolutionary perspective for species.",
      "B. It allows for the diversification of species.",
      "C. It prevents the formation of splinter groups in species.",
      "D. It keeps a species reproductively united."
    ],
    ans: 1,
    exp: "Ý gốc đoạn cuối: 'Occurring repeatedly in the course of more than 3.5 billion years, it has given rise to the diversity of organisms...' -> Quá trình hình thành loài (speciation) đã tạo ra sự đa dạng (diversification) của các sinh vật."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 3: Exercise 3",
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
  
  // Find Chapter 3 folder
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
    title: "Chapter 3: Exercise 3",
    course_id: courseId,
    folder_id: chapter3FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 3: Exercise 3").eq('course_id', courseId);
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
