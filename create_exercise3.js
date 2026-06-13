const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
const folderId = 'e2ddb86d-139b-4e3c-9878-ba11a0c808fb';

const ex3Passage = `
<h3 class="text-[24px] font-bold mb-4 text-center">Language and Reality</h3>
<p>An important ethnolinguistic concern of the 1930s and 1940s was the question of whether language might indeed determine culture. Do we see and react differently to the colors blue and green, with different cultural symbolism for the two different colors, only because our language has different names for these two neighboring parts of the unbroken color spectrum? When anthropologists noticed that some cultures lump together blue and green with one name, they began to wonder about this question. The American linguists Edward Sapir and Benjamin Lee Whorf, drawing on their experience with the language of the Hopi Indians, developed a full-fledged theory, sometimes called the <mark>Whorfian hypothesis</mark>. Whorf proposed that a language is not simply an encoding process for voicing our ideas and needs but is rather a shaping force, which, by providing habitual grooves of expression that <mark>predispose</mark> people to see the world in a certain way, guides their thinking and behavior.</p>
<p>The opposite point of view is that language reflects reality. In this view, language mirrors cultural reality, and as <mark>the latter</mark> changes, so too will language. Some support for this is provided by studies of blue-green color terms. It has been shown that eye pigmentation acts to filter out the shorter wavelengths of solar radiation. Color vision is thus limited through a reduced sensitivity to blue and confusion between the shorter visible wavelengths. The effect shows up in color-naming behavior, where green may be identified with blue, blue with black, or both green and blue with black. The severity of visual limitation, as well as the extent of lumping of color terms, depends on the density of eye pigmentation characteristic of people in a given society.</p>
<p>These findings do not mean that language merely reflects reality, any more than thinking and behavior are determined by language. The truth of the matter is more as anthropologist Peter Woolfson has put it: "Reality should be the same for us all. Our nervous systems, however, are being <mark>bombarded</mark> by a continual flow of sensations of different kinds, intensities, and durations. It is obvious that all of these sensations do not reach our consciousness; some kind of filtering system reduces them to manageable propositions. The Whorfian hypothesis suggests that the filtering system is one's language. Our language, in effect, provides us with a special pair of glasses that heightens certain perceptions and <mark>dims</mark> others. Thus, while all sensations are received by the nervous system, only <mark>some</mark> are brought to the level of consciousness."</p>
`;

const ex3Questions = [
  { q: "Based on the information in paragraph 1, which of the following best explains the term <mark>Whorfian hypothesis</mark>?", opts: ["A theory that language determines culture", "A theory that language reflects reality", "A theory about the relationship between language and color", "A view against established theories about language"], ans: "A", exp: "Giả thuyết Whorfian (Whorfian hypothesis) cho rằng ngôn ngữ quyết định hoặc định hình văn hóa và cách tư duy (language determines culture)." },
  { q: "The word <mark>predispose</mark> in paragraph 1 is closest in meaning to", opts: ["influence", "resolve", "deal with", "categorize"], ans: "A", exp: "\"Predispose\" có nghĩa là dẫn dắt, ảnh hưởng hoặc tạo thiên hướng, đồng nghĩa với \"influence\"." },
  { q: "The phrase <mark>the latter</mark> in paragraph 2 refers to", opts: ["view", "language", "cultural reality", "behavior"], ans: "C", exp: "\"The latter\" (cái nhắc đến sau) dùng để chỉ \"cultural reality\" trong cụm \"language mirrors cultural reality\"." },
  { q: "The word <mark>bombarded</mark> in paragraph 3 is closest in meaning to", opts: ["argued", "attacked", "prevented", "heated"], ans: "B", exp: "\"Bombarded\" mang nghĩa bị tấn công dồn dập (nghĩa bóng là bị tác động liên tục), gần nghĩa nhất với \"attacked\"." },
  { q: "The word <mark>dims</mark> in paragraph 3 is closest in meaning to", opts: ["damages", "enlarges", "removes", "obscures"], ans: "D", exp: "\"Dims\" có nghĩa là làm mờ đi, làm tối đi, đồng nghĩa với \"obscures\" (che khuất, làm mờ nhạt)." },
  { q: "The word <mark>some</mark> in paragraph 3 refers to", opts: ["nervous system", "sensations", "consciousness", "perceptions"], ans: "B", exp: "\"Some\" ở đây thay thế cho danh từ số nhiều \"sensations\" (cảm giác) ở vế câu trước đó." }
];

const mpPassage = `
<h3 class="text-[24px] font-bold mb-4 text-center">More Practice</h3>
<p><strong>A.</strong> To understand how the schedule of <mark>wants</mark> and demands of a given society is balanced against the supply of goods and services available, it is necessary to introduce a noneconomic variable - the anthropological variable of culture. In any given economic system, economic processes cannot be interpreted without culturally defining the demands and understanding the conventions that dictate how and when <mark>they</mark> are satisfied.</p>
<p><strong>B.</strong> However impressive all these discoveries may be, one important link is still missing: the social organization. There is evidence that chimpanzees lead a highly subtle and complex social life, but this picture is still vague. <mark>This</mark> is due to the fact that it is impossible to follow social processes in every detail in the jungle. Presently, there is one place in the world where such a <mark>comprehensive</mark> study of chimpanzees is possible.</p>
<p><strong>C.</strong> The audience for a work of art may consist of members of a particular group, perhaps a lineage or age set or people of a certain social rank, and the theme, content, and purpose of the oral narrative to <mark>which</mark> they listen may change to fit the social context in which it is recited. The words may also change from recitation to recitation as the mood of the audience changes. And a story told to children will be told differently to adults.</p>
<p><strong>D.</strong> As continents and ocean basins change shape, some strata sink below the surface of an ocean or lake, others are forced upward into mountain ranges, and <mark>some</mark> are worn away by water, wind or ice or are <mark>deformed</mark> by heat or pressure.</p>
<p><strong>E.</strong> Although the Sumerians and the Egyptians took steps needed to turn the simple ideography into the full alphabet, writing still needed to develop. Having a different sign for every single word would require knowing thousands of different signs, and abstract ideas and grammar are still difficult to express. A way of overcoming <mark>this problem</mark> is to turn to sound devices. For example, by using the <mark>character</mark> for a bee and the character for the leaf of a tree, one can combine them, "bee" plus "leaf," to form "belief." This kind of writing is called "word-syllabic."</p>
<p><strong>F.</strong> Before the invention of photography, <mark>the great majority</mark> of painted images were portraits, small enough to be carried in a locket for remembrance. Suddenly, painting was relieved of the necessity of "communicating" in this pedestrian way. The result was an explosion of new styles and methods. Impressionism was the crowning glory of those times. It was followed by cubism, dadaism, surrealism and abstract expressionism, as well as other movements in art of our time, including photorealism, in which the painter paints an image that, from a distance, is <mark>indistinguishable from</mark> a photograph.</p>
<p><strong>G.</strong> Darwin saw that food supply and other factors <mark>hold populations in check</mark>. Darwin calculated that a single breeding pair of elephants would, if all their progeny lived and reproduced the normal number of offspring over a normal life span, produce a standing population of 19 million elephants in 750 years, yet the average number of elephants generally remains the same over the years. Although a single breeding pair could have produced 19 million descendants, it did produce an average of only two. But why these particular two? Darwin gave birth to the theory of natural selection by answering <mark>the question</mark>.</p>
`;

const mpQuestions = [
  { q: "A.1. The word <mark>wants</mark> in the paragraph is closest in meaning to", opts: ["needs", "supplies", "prices"], ans: "A", exp: "\"Wants\" (những mong muốn, nhu cầu) đồng nghĩa với \"needs\" (nhu cầu)." },
  { q: "A.2. The word <mark>they</mark> in the paragraph refers to", opts: ["conventions", "economic processes", "demands"], ans: "C", exp: "\"They\" thay thế cho \"demands\" (các nhu cầu) trong câu \"culturally defining the demands and understanding the conventions that dictate how and when they are satisfied\"." },
  { q: "B.1. The word <mark>This</mark> in the paragraph refers to", opts: ["The subtle and complicated nature of chimpanzees' social life", "The uncertainty of ideas about chimpanzees' social life", "The impressive discoveries about chimpanzees' social life"], ans: "B", exp: "\"This\" chỉ sự mơ hồ, không chắc chắn về đời sống xã hội của tinh tinh (\"this picture is still vague\")." },
  { q: "B.2. The word <mark>comprehensive</mark> in the paragraph is closest in meaning to", opts: ["exclusive", "thorough", "progressive"], ans: "B", exp: "\"Comprehensive\" có nghĩa là toàn diện, bao quát, đồng nghĩa với \"thorough\"." },
  { q: "C.1. The word <mark>which</mark> in the paragraph refers to", opts: ["purpose", "oral narrative", "people"], ans: "B", exp: "\"Which\" trong cụm \"to which they listen\" thay thế cho \"oral narrative\" (câu chuyện truyền miệng) đứng ngay trước đó." },
  { q: "D.1. The word <mark>some</mark> in the paragraph refers to", opts: ["surface", "ranges", "strata"], ans: "C", exp: "\"Some\" ở đây thay thế cho danh từ \"strata\" (các tầng địa chất) ở vế câu trước." },
  { q: "D.2. The word <mark>deformed</mark> in the paragraph is closest in meaning to", opts: ["distorted", "united", "destroyed"], ans: "A", exp: "\"Deformed\" có nghĩa là bị biến dạng, đồng nghĩa với \"distorted\" (bị bóp méo, biến dạng)." },
  { q: "E.1. The phrase <mark>this problem</mark> in the paragraph refers to", opts: ["the difficulty of expressing abstract ideas", "the difference between signs and ideas", "the task of turning the simple ideography into the full alphabet"], ans: "A", exp: "\"This problem\" chỉ những khó khăn trong việc thể hiện các ý tưởng trừu tượng và ngữ pháp (\"abstract ideas and grammar are still difficult to express\")." },
  { q: "E.2. The word <mark>character</mark> in the paragraph is closest in meaning to", opts: ["place", "feature", "letter"], ans: "C", exp: "\"Character\" ở đây mang nghĩa là ký tự, chữ cái, đồng nghĩa với \"letter\"." },
  { q: "F.1. The phrase <mark>the great majority</mark> in the paragraph is closest in meaning to", opts: ["some", "most", "all"], ans: "B", exp: "\"The great majority\" có nghĩa là đại đa số, phần lớn, đồng nghĩa với \"most\"." },
  { q: "F.2. The phrase <mark>indistinguishable from</mark> in the paragraph is closest in meaning to", opts: ["inseparable from", "suitable to", "identical with"], ans: "C", exp: "\"Indistinguishable from\" mang nghĩa là không thể phân biệt được, giống hệt nhau, đồng nghĩa với \"identical with\"." },
  { q: "G.1. In stating that food supply and other factors <mark>hold populations in check</mark>, the author means that they", opts: ["control populations", "reduce populations", "increase populations"], ans: "A", exp: "\"Hold in check\" mang nghĩa là kìm hãm, kiểm soát, giữ trong tầm kiểm soát, đồng nghĩa với \"control\"." },
  { q: "G.2. The phrase <mark>the question</mark> in the paragraph refers to the question as to", opts: ["why a single breeding pair of elephants only produced two descendants on average", "how many years it would take for the number of elephants to increase", "how elephants could survive up to modern times producing only two descendants"], ans: "A", exp: "\"The question\" thay thế cho câu hỏi \"But why these particular two?\" ngay đằng trước, ý hỏi tại sao chỉ có 2 hậu duệ sống sót." }
];

function buildTestPayload(title, passage, qList) {
  const parts = [
    {
      id: crypto.randomUUID(),
      name: 'Part 1',
      content: passage,
      sections: [
        {
          id: crypto.randomUUID(),
          title: '', // Set title to empty string to hide Section badge
          questionType: 'Trắc nghiệm',
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
  ];

  return {
    title: title,
    test_type: 'Standard-Reading',
    course_id: courseId,
    folder_id: folderId,
    is_published: true,
    content_json: {
      basicInfo: {
        title: title,
        skill: 'Standard-Reading',
        category: 'exercise',
        timeLimit: '0',
        courseId: courseId
      },
      parts: parts
    },
    json_config: {
      timeLimit: 0,
      parts: parts
    }
  };
}

async function run() {
  const payload1 = buildTestPayload('Chapter 1: Exercise 3', ex3Passage, ex3Questions);
  const payload2 = buildTestPayload('Chapter 1: More Practice', mpPassage, mpQuestions);
  
  const { error } = await supabase.from('tests').insert([payload1, payload2]);
  if (error) {
    console.error('Error inserting tests:', error);
  } else {
    console.log('Inserted Exercise 3 and More Practice successfully!');
  }
}

run();
