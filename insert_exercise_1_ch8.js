const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Estuaries</h2>
<p style="text-indent:2em;line-height:1.9;">Estuaries are scattered along the shores of all the oceans and vary widely in origin, type, and size. They may be called lagoons, sloughs, or even bays, but all share the mixing of fresh water with the sea in a partially enclosed section of the coast. Many were formed when sea levels rose because of the melting of ice at the end of the last ice age, about 18,000 years ago. The sea invaded lowlands and river mouths in the process. These estuaries are called drowned river valleys or coastal plain estuaries. They are probably the most common type of estuary. Examples are the Chesapeake Bay and the St. Lawrence River on the east coast of North America and the mouth of the River Thames in England. Coastal plain estuaries rely on tidal action to maintain the correct proportions of both fresh and sea water which are essential to their biospheres. The combination of this brackish water and the flow of nutrient-rich sediments from the upper reaches of their tributary rivers makes these estuaries incredibly rich. Coastal plain estuaries are some of the most productive fishing grounds in the world and often represent an important economic resource for nearby communities. While pollution can be a problem, the constant outflow of river water means that the estuary will typically rebound once the pollution source has been eliminated.</p>
<p style="text-indent:2em;line-height:1.9;">A second type of estuary is the bar-built estuary. Here the accumulation of sediments along the coast builds up sand bars and barrier islands that act as a wall between the ocean and the fresh water from rivers. They are found along the Texas coast of the Gulf of Mexico, and along the North Sea coast of the Netherlands and Germany. Bar-built estuaries are important natural barriers against destructive wave action. Their sand bars reduce the force of waves and storm surges and significantly cut the damage sustained to inland areas during severe storms. Bar-built estuaries also support a broad range of aquatic life, from oysters and shrimp to the sea birds that feed on these shellfish. These estuaries are especially susceptible to the impacts of human development. Their sand bars are easily damaged, and their fresh water areas behind their barrier islands are easily polluted. Once damaged, they do not recover easily.</p>
`;

const opts = [
  "A. Tides maintain correct salinity in water",
  "B. Contain barrier islands",
  "C. Formed during glacial periods",
  "D. Only occur in southern areas",
  "E. Habitats especially fragile",
  "F. Important as fisheries"
];

const qList = [
  {
    q: "Coastal Plain Estuary (Ý 1)",
    ans: "A/C/F",
    opts: opts,
    exp: "Gồm 3 đáp án (thứ tự tùy ý): A, C, F.<br><b>A đúng:</b> 'rely on tidal action to maintain the correct proportions of both fresh and sea water'.<br><b>C đúng:</b> 'formed when sea levels rose because of the melting of ice at the end of the last ice age'.<br><b>F đúng:</b> 'some of the most productive fishing grounds in the world'."
  },
  {
    q: "Coastal Plain Estuary (Ý 2)",
    ans: "A/C/F",
    opts: [],
    exp: ""
  },
  {
    q: "Coastal Plain Estuary (Ý 3)",
    ans: "A/C/F",
    opts: [],
    exp: ""
  },
  {
    q: "Bar-built Estuary (Ý 1)",
    ans: "B/E",
    opts: [],
    exp: "Gồm 2 đáp án (thứ tự tùy ý): B, E.<br><b>B đúng:</b> 'builds up sand bars and barrier islands'.<br><b>E đúng:</b> 'especially susceptible to the impacts of human development... easily damaged... easily polluted'."
  },
  {
    q: "Bar-built Estuary (Ý 2)",
    ans: "B/E",
    opts: [],
    exp: ""
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 8: Exercise 1",
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
          content: `<p style="padding:12px;background:#f0f9ff;border-left:4px solid #2bd6eb;border-radius:8px;margin-bottom:12px;line-height:1.8;"><strong>Directions:</strong> Select the appropriate phrases from the answer choices and match them to the type of estuary to which they relate. ONE of the answer choices will NOT be used.</p>`,
          questionType: "Matching",
          questions: qList.map((data, index) => ({
            id: String(index + 1),
            content: `<b>${data.q}</b>`,
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
  
  // Find Chapter 8 folder
  let chapterFolderId;
  const {data: existingFolder} = await supabase.from('folders').select('id').eq('parent_id', crashCourseFolderId).ilike('title', 'Chapter 8');
  
  if (existingFolder && existingFolder.length > 0) {
    chapterFolderId = existingFolder[0].id;
  } else {
    // get max display_order
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 8",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapterFolderId = newFolder[0].id;
    console.log("Created Chapter 8 folder!");
  }
  
  // check max test order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapterFolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 8: Exercise 1",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 8: Exercise 1").eq('course_id', courseId);
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
