const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">Freudian and Jungian Psychology</h2>
<p style="text-indent:2em;line-height:1.9;">Two of the most influential psychologists of the early 20th century were Sigmund Freud and Carl Jung. While the two men worked in collaboration for a number of years and held each other in high esteem, they developed psychological theories which were quite different from each other.</p>
<p style="text-indent:2em;line-height:1.9;">The basis of Freud's theory was the separation of the mind into the conscious and the unconscious. According to Freud, the mind consisted of three parts: the id, the ego, and the super-ego. Of these three, the only conscious element was the ego. The super-ego and the id were unconscious elements that basically acted in opposition to each other. The id consisted of a person's desires and urges, and the super-ego consisted of the moral rules which sought to suppress these urges. When the super-ego and the id were balanced, the result was a normal, healthy ego. Mental problems resulted from imbalances in these two elements. Freud placed a high emphasis on sexual drives. He believed that sexual drives were present from birth, and that much of the mental instability he saw in people was due to the imbalance in their sexual drives and the social values which sought to repress those drives.</p>
<p style="text-indent:2em;line-height:1.9;">Jung also believed the unconscious mind played a large role in the make-up of a person's personality. Unlike Freud, however, Jung did not focus on instinctual drives. He felt the most powerful force in the unconscious was the presence of shadows. Jung was a firm believer in the concept of opposites, and felt that they were always present in the human mind. For example, he believed basically kind persons also had cruel aspects in their unconscious mind, but that they would not allow themselves to consciously admit this to themselves. Jung also believed in a deeper level of the unconscious which he called the collective unconscious. This, according to Jung, was the shared unconscious of all of humanity. Jung felt that there were unconscious elements that were common in every person. He called these shared elements archetypes. Mental illness came about when a person's unconscious deviated too greatly from these archetypes.</p>
`;

const opts = [
  "A. Sought to cure mental illness by developing the unconscious mind",
  "B. Heavy focus on sexual impulses",
  "C. Believed in an unconscious section of the mind",
  "D. Believed in a collective unconscious",
  "E. Mental illness as a result of problems in the unconscious",
  "F. Believed everyone has contradictions in their personality"
];

const qList = [
  {
    q: "Freudian Psychology",
    ans: "B",
    opts: opts,
    exp: "<b>B đúng:</b> 'Freud placed a high emphasis on sexual drives... sexual drives were present from birth'."
  },
  {
    q: "Jungian Psychology (Ý 1)",
    ans: "D/F",
    opts: [],
    exp: "Gồm 2 đáp án (thứ tự tùy ý): D, F.<br><b>D đúng:</b> 'Jung also believed in a deeper level of the unconscious which he called the collective unconscious'.<br><b>F đúng:</b> 'Jung was a firm believer in the concept of opposites... he believed basically kind persons also had cruel aspects'."
  },
  {
    q: "Jungian Psychology (Ý 2)",
    ans: "D/F",
    opts: [],
    exp: ""
  },
  {
    q: "Both (Ý 1)",
    ans: "C/E",
    opts: [],
    exp: "Gồm 2 đáp án (thứ tự tùy ý): C, E.<br><b>C đúng:</b> Freud chia tâm trí thành ý thức và vô thức ('separation of the mind into the conscious and the unconscious'). Jung cũng tin vô thức đóng vai trò lớn ('Jung also believed the unconscious mind played a large role').<br><b>E đúng:</b> Cả hai đều cho rằng bệnh tâm lý đến từ vô thức. Freud: 'Mental problems resulted from imbalances in these two elements (id và super-ego thuộc vô thức)'. Jung: 'Mental illness came about when a person's unconscious deviated too greatly from these archetypes'."
  },
  {
    q: "Both (Ý 2)",
    ans: "C/E",
    opts: [],
    exp: ""
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 8: Exercise 2",
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
          content: `<p style="padding:12px;background:#f0f9ff;border-left:4px solid #2bd6eb;border-radius:8px;margin-bottom:12px;line-height:1.8;"><strong>Directions:</strong> Select the appropriate phrases from the answer choices and match them to the psychology to which they relate. ONE of the answer choices will NOT be used.</p>`,
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
    const {data: folders} = await supabase.from('folders').select('display_order').eq('parent_id', crashCourseFolderId);
    const maxFolderOrder = folders && folders.length > 0 ? Math.max(...folders.map(f => f.display_order || 0)) : 0;
    
    const {data: newFolder} = await supabase.from('folders').insert([{
      title: "Chapter 8",
      course_id: courseId,
      parent_id: crashCourseFolderId,
      display_order: maxFolderOrder + 1
    }]).select();
    chapterFolderId = newFolder[0].id;
  }
  
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', chapterFolderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 8: Exercise 2",
    course_id: courseId,
    folder_id: chapterFolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 8: Exercise 2").eq('course_id', courseId);
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
