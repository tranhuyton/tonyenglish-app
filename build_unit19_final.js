const fs = require('fs');

const words = [
  { word: 'adopt', phonetic: '[adapt]', type: 'v.', def: 'To adopt someone is to make them as a part of one’s own family.', ex: 'The girl was adopted by the couple when she was three.' },
  { word: 'beg', phonetic: '[beg]', type: 'v.', def: 'To beg is to ask for something one really wants.', ex: 'The man begged for some money.' },
  { word: 'beyond', phonetic: '[bi/and]', type: 'prep.', def: 'If A is beyond B, A is farther away.', ex: 'John’s house is beyond that lake.' },
  { word: 'costume', phonetic: '[kasyuim]', type: 'n.', def: 'A costume is a set of clothes people wear for a particular occasion.', ex: 'The woman wore a mask with her costume.' },
  { word: 'exclaim', phonetic: '[ikskleim]', type: 'v.', def: 'To exclaim is to say something loudly, usually due to being excited.', ex: '“Look at her dress!” Sara exclaimed.' },
  { word: 'extend', phonetic: '[ikstend]', type: 'v.', def: 'To extend is to stretch out or reach.', ex: 'The boy extended his hand to catch the ball.' },
  { word: 'fool', phonetic: '[fu:I]', type: 'n.', def: 'A fool is someone who makes unwise choices.', ex: 'The girl was a fool for playing too close to the water.' },
  { word: 'forbid', phonetic: '[faxbfd]', type: 'v.', def: 'To forbid is to tell someone they cannot do something.', ex: 'My father forbids watching TV while we’re eating dinner.' },
  { word: 'illustrate', phonetic: '[ilastreit]', type: 'v.', def: 'To illustrate is to show something by drawing a picture.', ex: 'The executive illustrated the decreasing profits of the company.' },
  { word: 'indeed', phonetic: '[indid]', type: 'adv.', def: 'Indeed means truly or really.', ex: 'The birthday party was indeed fun last night.' },
  { word: 'interpret', phonetic: '[intarprit]', type: 'v.', def: 'To interpret is to explain what something means.', ex: 'The woman interpreted what her co-worker was trying to say.' },
  { word: 'kindly', phonetic: '[kaindli]', type: 'adv.', def: 'If people do something kindly, they do it in a nice way.', ex: 'The stranger kindly cared for the hurt man.' },
  { word: 'motive', phonetic: '[moutiv]', type: 'n.', def: 'A motive is the reason someone does something.', ex: 'His motive for studying so hard is to get into a good college.' },
  { word: 'nest', phonetic: '[nest]', type: 'n.', def: 'A nest is a place where a bird lays its eggs.', ex: 'The bird laid her eggs in the nest that she made.' },
  { word: 'origin', phonetic: '[d:rad3in]', type: 'n.', def: 'The origin of someone or something is where they come from.', ex: 'The origin of the honey that we eat is from a beehive.' },
  { word: 'reception', phonetic: '[risepjan]', type: 'n.', def: 'A reception is a party to welcome a person or celebrate an event.', ex: 'We all danced and had a good time at the wedding reception.' },
  { word: 'reject', phonetic: '[rid3ekt]', type: 'v.', def: 'To reject is to refuse something because you do not want it.', ex: 'The girl rejected the broken cup.' },
  { word: 'silence', phonetic: '[sailans]', type: 'n.', def: 'Silence is complete quiet.', ex: 'The man asked for silence while he worked on the problem.' },
  { word: 'stream', phonetic: '[stri:m]', type: 'n.', def: 'A stream is a small river.', ex: 'The boy caught a fish in the stream.' },
  { word: 'tone', phonetic: '[toun]', type: 'n.', def: 'Tone is the sound of someone’s voice. It shows how they feel.', ex: 'My father’s tone told me I had broken the rule.' }
];

const icons = ['😎', '🚀', '🌟', '🎨', '📚', '🧩', '🏆', '💡', '🎸', '🌍', '😎', '🚀', '🌟', '🎨', '📚', '🧩', '🏆', '💡', '🎸', '🌍'];

let wordListHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit19_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit19_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach((w, i) => {
  wordListHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">${icons[i]}</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetic}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});

wordListHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Mrs. May and the Green Girl</h1><p style="margin-bottom: 1rem;">One morning, people from a small town found a little girl by a <b>stream</b>. She seemed to be wearing a green <b>costume</b>. As the people got closer, they saw that the girl’s skin was green!</p><p style="margin-bottom: 1rem;">“Oh my!” The people <b>exclaimed</b>. “What if her <b>motive</b> for coming to our town is bad? What if she has a strange <b>origin</b>?”</p><p style="margin-bottom: 1rem;">An old woman <b>kindly</b> went to her. “Look how scared she is. Please,” she <b>begged</b>. “Do not <b>reject</b> her. I will <b>adopt</b> her.”</p><p style="margin-bottom: 1rem;">There was <b>silence</b> until the judge spoke. “I don’t know,” he said in a worried <b>tone</b>. “But we cannot <b>forbid</b> you. I <b>indeed</b> hope you’re not being a <b>fool</b>.”</p><p style="margin-bottom: 1rem;">Mrs. May <b>extended</b> her hand to the girl. “Come with me. I won’t hurt you.”</p><p style="margin-bottom: 1rem;">The girl spoke a language Mrs. May didn’t know. But she was able to <b>interpret</b> what the girl was trying to say. Sometimes the girl drew pictures to <b>illustrate</b> what she meant.</p><p style="margin-bottom: 1rem;">The green girl was from a place far <b>beyond</b> the sun. There, people lived in <b>nests</b> built in trees. They only ate green leaves, which made their skin green.</p><p style="margin-bottom: 1rem;">“Well, you can’t just eat leaves,” Mrs. May said. She fed the green girl home-cooked meals, and soon the girl wasn’t green anymore. The people had a huge <b>reception</b> to welcome her as a citizen of the town.</p></div>`;

const json = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 19",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordListHtml.replace(/\n/g, ''),
      sections: [
        {
          id: "sec1_wordlist",
          title: "Exercise 1: Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. to tell or explain meaning", options: ["adopt", "exclaim", "interpret", "reject"], correctAnswer: "interpret", explanation: "interpret: to tell or explain meaning" },
            { id: "2", content: "2. a person without sense", options: ["fool", "nest", "stream", "vitamin"], correctAnswer: "fool", explanation: "fool: a person without sense" },
            { id: "3", content: "3. clothes that people wear for a particular occasion", options: ["motive", "neat", "costume", "tone"], correctAnswer: "costume", explanation: "costume: clothes that people wear for a particular occasion" },
            { id: "4", content: "4. to reach or put out", options: ["beg", "extend", "forbid", "silence"], correctAnswer: "extend", explanation: "extend: to reach or put out" },
            { id: "5", content: "5. in a kind way", options: ["beyond", "illustrate", "indeed", "kindly"], correctAnswer: "kindly", explanation: "kindly: in a kind way" }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 1: Part B: Check (V) the one that suits the blank naturally.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "6", content: "1. When I found the lost cat,________________ .", options: ["I asked my mom if we could adopt it", "I extended my hurt foot"], correctAnswer: "I asked my mom if we could adopt it", explanation: "We adopt a lost cat." },
            { id: "7", content: "2. When I visit other countries,________________ .", options: ["I usually tell them how much better my country is than theirs", "someone has to interpret what I say"], correctAnswer: "someone has to interpret what I say", explanation: "People need someone to interpret language." },
            { id: "8", content: "3. Not having enough money.", options: ["can put you beyond the forest", "can indeed be a big problem"], correctAnswer: "can indeed be a big problem", explanation: "Not having money can indeed be a big problem." },
            { id: "9", content: "4. At the start of class,________________", options: ["the teacher kindly asked for us to stop talking", "the teacher exclaimed the lesson"], correctAnswer: "the teacher kindly asked for us to stop talking", explanation: "The teacher kindly asked..." },
            { id: "10", content: "5. The woman wanted to go to Africa.", options: ["The tone of her voice was angry", "Her motive was to help people"], correctAnswer: "Her motive was to help people", explanation: "Her motive to go to Africa was to help people." }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 2: Fill in the blanks with the correct words from the word bank: illustrate, costume, silence, fool, origin, begged, forbids, reception, rejected, stream",
          content: "",
          questionType: "Điền từ",
          questions: [
            { id: "11", content: "1. We had a big [11] to welcome my grandmother home from the hospital.", correctAnswer: "reception", explanation: "reception (tiệc tiếp đón) để chào đón bà." },
            { id: "12", content: "2. The man was a [12] for crossing the street without looking.", correctAnswer: "fool", explanation: "fool (kẻ ngốc) vì băng qua đường không nhìn." },
            { id: "13", content: "3. A friend asked me to [13] the book she wrote because I am an artist.", correctAnswer: "illustrate", explanation: "illustrate (minh họa) sách vì là họa sĩ." },
            { id: "14", content: "4. I sewed feathers on my [14] for the play.", correctAnswer: "costume", explanation: "costume (trang phục) cho vở kịch." },
            { id: "15", content: "5. My teacher [15] my paper because I didn’t follow the directions.", correctAnswer: "rejected", explanation: "rejected (từ chối) bài tập vì không làm theo hướng dẫn." },
            { id: "16", content: "6. I like being alone in the forest because of the [16] that’s around me.", correctAnswer: "silence", explanation: "silence (sự yên lặng) trong rừng." },
            { id: "17", content: "7. The boy who stole the bread [17] me not to tell.", correctAnswer: "begged", explanation: "begged (van xin) đừng kể ra." },
            { id: "18", content: "8. Some fish swim up a [18] to lay their eggs.", correctAnswer: "stream", explanation: "stream (suối)." },
            { id: "19", content: "9. We learned about the [19] of the Statue of Liberty.", correctAnswer: "origin", explanation: "origin (nguồn gốc) của tượng Nữ thần Tự do." },
            { id: "20", content: "10. My sister [20] anyone to come in her room without asking first.", correctAnswer: "forbids", explanation: "forbids (cấm) vào phòng không hỏi trước." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml.replace(/\n/g, ''),
      imageUrl: "/unit19_story.png",
      sections: [
        {
          id: "sec4_reading",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "21", content: "1. What is this story about?", options: ["A reception for an old woman", "A girl who liked to find nests in the trees", "The people in the land beyond the sunset", "How a woman kindly took care of a girl"], correctAnswer: "How a woman kindly took care of a girl", explanation: "Câu chuyện kể về người phụ nữ đã nhận nuôi một cô bé màu xanh." },
            { id: "22", content: "2. What are the people trying to do to the green girl?", options: ["Beg her to jump into the stream", "Make her leave", "Forbid her to stay with Mrs. May", "Interpret what she was trying to say"], correctAnswer: "Make her leave", explanation: "Mọi người nghi ngờ và sợ hãi cô bé." },
            { id: "23", content: "3. What is true of the green girl in the story?", options: ["She was good at drawing illustrating about what she meant.", "She was indeed there to bring bad luck.", "Her costume turned her skin green.", "She asked Mrs. May to adopt her."], correctAnswer: "She was good at drawing illustrating about what she meant.", explanation: "Cô bé vẽ tranh để minh họa ý mình." },
            { id: "24", content: "4. Why did Mrs. May extend her hand to the green girl?", options: ["To tell the girl that she was a fool", "To show that she indeed had good motives", "To exclaim that she didn’t want to adopt her", "To silence the crowd from hurting the girl"], correctAnswer: "To show that she indeed had good motives", explanation: "Bà đưa tay ra để cho thấy bà có thiện chí." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit19.json', JSON.stringify(json, null, 2));
console.log('Successfully generated unit19.json');
