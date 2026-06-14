const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">The Making of a Supernova</h2>
<p style="text-indent:2em;line-height:1.9;">The key theoretical insight as to how supernovae, the greatest of all stellar explosions, work actually dates back to 1934. At that time, less than two years after the discovery of the neutron, Walter Baade and Fritz Zwicky offered the dramatic theory that a "supernova represents the transition of an ordinary star into a neutron star." But although half a century of observations of distant supernovae and theorizing had filled in the details of how that might happen, the hypothesis could only be tested fully by studying a nearby supernova at work.</p>
<p style="text-indent:2em;line-height:1.9;">By the late 1980s, astronomers were satisfied, from their studies of supernovae in other galaxies, that there are two basic, different types of supernova. In each case, an ordinary star is converted into a neutron star, releasing gravitational energy as it shrinks. The first way to make a supernova (type I) involves a cold, dead star which has less than the critical amount of mass. It then gains additional matter from a nearby companion. Such a star starts out as a white dwarf, a dead star with about the mass of the Sun, maybe a little less, contained in a volume comparable to the size of the Earth. It is the fate of the Sun to end its life as a white dwarf, because it does not have enough mass to become a neutron star and it has no companion from which to steal mass. A star like the Sun which has become a white dwarf and orbits around another star can gain mass by pulling forcibly streamers of gas off its companion through tidal forces and swallowing the gaseous ribbons. When its mass reaches the critical value, the atoms of which the star is made will collapse, electrons being forced to merge with protons to become neutrons.</p>
<p style="text-indent:2em;line-height:1.9;">Another way of making a supernova, known as type II, happens when a very massive star near the end of its life runs out of nuclear fuel to keep its heart hot. A star like the Sun keeps hot by "burning" hydrogen to make helium, in a process known as nuclear fusion - the same process that operates in a hydrogen bomb. When it has no more nuclear fuel to burn, the inner part of such a star, already with more than the critical mass needed to make a neutron star, collapses all the way to the neutron star state, without stopping off as a white dwarf.</p>
`;

const qList = [
  {
    q: "According to the passage, what was originally the difficulty with the theory of supernova proposed by Walter Baade and Fritz Zwicky?",
    opts: [
      "A. It did not account for the effects of neutron stars.",
      "B. It lacked observational evidence to support it.",
      "C. It had taken over half a century for them to develop.",
      "D. Their theory of supernova was too dramatic."
    ],
    ans: 1,
    exp: "Ý gốc ở cuối đoạn 1: '...the hypothesis could only be tested fully by studying a nearby supernova at work.' -> Giả thuyết ban đầu chỉ có thể được kiểm chứng đầy đủ bằng cách quan sát một siêu tân tinh ở gần. Do đó, lúc đầu lý thuyết này thiếu bằng chứng quan sát thực tế (observational evidence) để củng cố."
  },
  {
    q: "According to paragraph 2, a white dwarf can only become a neutron star if",
    opts: [
      "A. it has a companion star from which it can gain mass",
      "B. it has retained some of its nuclear fuel",
      "C. it can release enough of its gravitational energy",
      "D. it has a smaller volume than the Earth"
    ],
    ans: 0,
    exp: "Ý gốc trong đoạn 2: Trái Đất kết thúc với tư cách là sao lùn trắng vì 'it does not have enough mass to become a neutron star and it has no companion from which to steal mass.' Ngược lại, một sao lùn trắng nếu có sao đồng hành thì có thể hút khối lượng (gain mass by pulling forcibly streamers of gas off its companion) để đạt tới khối lượng tới hạn và thành sao nơ-tron. -> Vậy điều kiện là phải có sao đồng hành."
  },
  {
    q: "In the passage, all of the following are mentioned as aspects of supernovas EXCEPT",
    opts: [
      "A. the release of gravitational energy",
      "B. a significant decrease in the volume of a star",
      "C. the formation of gaseous ribbons",
      "D. the creation of a neutron star"
    ],
    ans: 2,
    exp: "A ('releasing gravitational energy'), B ('shrinks' - thu nhỏ thể tích) và D ('converted into a neutron star') đều là các đặc điểm được nhắc đến về sự hình thành siêu tân tinh. C ('formation of gaseous ribbons') chỉ là hiện tượng hút khí từ sao đồng hành trước khi trở thành siêu tân tinh loại I, chứ không phải đặc điểm của chính siêu tân tinh."
  },
  {
    q: "According to paragraph 3, stars in type II supernovae are able to bypass the white dwarf stage because",
    opts: [
      "A. they lack a nearby orbiting star",
      "B. their atoms have already collapsed to neutrons",
      "C. they already have the critical mass needed for neutron collapse",
      "D. they burn a different type of nuclear fuel"
    ],
    ans: 2,
    exp: "Ý gốc đoạn 3: 'already with more than the critical mass needed to make a neutron star, collapses all the way to the neutron star state, without stopping off as a white dwarf.' -> Vì chúng đã đạt đủ khối lượng tới hạn cần thiết (critical mass) để sụp đổ thành sao nơ-tron nên không cần trải qua giai đoạn sao lùn trắng."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 3: Exercise 2",
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
    title: "Chapter 3: Exercise 2",
    course_id: courseId,
    folder_id: chapter3FolderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 3: Exercise 2").eq('course_id', courseId);
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
