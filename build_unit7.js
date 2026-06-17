const fs = require('fs');

const story = {
  title: 'A Beautiful Bird',
  paragraphs: [
    'Dr. Norton’s occupation was a scholar of biology. He learned about all animals on a daily basis. One day he met a sailor from a colony overseas. The man told Dr. Norton about a talking bird! The bird fascinated Dr. Norton, so he told his colleagues about it. They debated with him: no one thought a bird could talk. He tried to persuade them, but they laughed at him. Nevertheless, Dr. Norton believed the bird was real. His new mission was to find it. He wanted factual proof.',
    'The next day he departed for the colony. The sailor he had met told him to look for a man named Jai, who would be able to help him in his search. After a month of sailing, Dr. Norton finally reached the colony where he met Jai.',
    '“I can take you to where it lives. It lives by the volcano,” Jai said.',
    'They left the next day. A week later, they arrived at the volcano. Every day they walked around and looked for the bird, but they couldn’t find it. After one month, Dr. Norton could not find the bird, and this depressed him. He decided to go home. On the route back, he walked past some old ruins. He heard someone say, “Hello.”',
    '“Who are you?” he asked. Dr. Norton looked up and saw a bird!',
    'Dr. Norton put the talking bird into a cage. Then he returned home. He had made a significant discovery.'
  ]
};

const wordsData = [
  { word: 'basis', pos: 'n.', pron: '[beisis]', def: 'To do something on time’s basis is how often you do it.', ex: 'My grandfather gets his hearing checked on a yearly basis.' },
  { word: 'biology', pos: 'n.', pron: '[baiɑlədʒi]', def: 'Biology is the study of living things.', ex: 'We learned about the human heart in biology class.' },
  { word: 'cage', pos: 'n.', pron: '[keidʒ]', def: 'A cage is something that holds an animal so it cannot leave.', ex: 'We put the parrots in their cage at night.' },
  { word: 'colleague', pos: 'n.', pron: '[kɑli:g]', def: 'A colleague is somebody you work with.', ex: 'My colleague helped me finish the job.' },
  { word: 'colony', pos: 'n.', pron: '[kɑləni]', def: 'A colony is a country controlled by another country.', ex: 'The USA was at one time a colony of Great Britain.' },
  { word: 'debate', pos: 'v.', pron: '[dibeit]', def: 'To debate is to seriously discuss something with someone.', ex: 'The husband and wife debated over which TV to buy.' },
  { word: 'depart', pos: 'v.', pron: '[dipɑ:rt]', def: 'To depart is to leave some place so you can go to another place.', ex: 'The plane departed for Italy at 3:00 this afternoon.' },
  { word: 'depress', pos: 'v.', pron: '[dipres]', def: 'To depress someone is to make them sad.', ex: 'The bad news from work depressed the man.' },
  { word: 'factual', pos: 'adj.', pron: '[fæktʃuəl]', def: 'When something is factual, it is true.', ex: 'John learns about history from factual books.' },
  { word: 'fascinate', pos: 'v.', pron: '[fæsəneit]', def: 'To fascinate someone is to make them really like something.', ex: 'The kitten was fascinated by the ball of yarn.' },
  { word: 'mission', pos: 'n.', pron: '[miʃən]', def: 'A mission is an important job that is sometimes far away.', ex: 'The woman’s mission was to help sick people.' },
  { word: 'nevertheless', pos: 'adv.', pron: '[nevərðəles]', def: 'You use nevertheless to show that something goes against a fact.', ex: 'He is usually friendly. Nevertheless, he wasn’t this afternoon.' },
  { word: 'occupation', pos: 'n.', pron: '[ɑkjəpeiʃən]', def: 'An occupation is a person’s job.', ex: 'My father’s occupation is a dentist.' },
  { word: 'overseas', pos: 'adv.', pron: '[ouvərsi:z]', def: 'If you go overseas, you go to a country on the other side of an ocean.', ex: 'John often goes overseas for vacations.' },
  { word: 'persuade', pos: 'v.', pron: '[pər:sweid]', def: 'To persuade someone is to make them agree to do something.', ex: 'The children persuaded their parents to buy them gifts.' },
  { word: 'route', pos: 'n.', pron: '[ru:t]', def: 'A route is the way you go from one place to another.', ex: 'I saw many new houses along the route to the city.' },
  { word: 'ruins', pos: 'n.', pron: '[ru:inz]', def: 'Ruins are old buildings that are not used anymore.', ex: 'I visited some interesting ruins in Greece.' },
  { word: 'scholar', pos: 'n.', pron: '[skɑlər]', def: 'A scholar is a person who studies something and knows much about it.', ex: 'The scholar knew much about art history.' },
  { word: 'significant', pos: 'adj.', pron: '[signifikənt]', def: 'When someone or something is significant, they are important.', ex: 'I read many significant novels as a literature major in university.' },
  { word: 'volcano', pos: 'n.', pron: '[vɑlkeinou]', def: 'A volcano is a mountain with a hole on top where hot liquid comes out.', ex: 'When the volcano erupted, smoke and heat filled the air.' }
];

const word_list_exercises = [
  {
    title: 'Circle two words that are related in each group.',
    questions: [
      { content: '1. a. volcano b. scholar c. colleague d. cage', options: ['b, c', 'a, d', 'b, d', 'a, b', 'c, d'], correctAnswer: 'b, c', explanation: 'scholar và colleague là hai từ liên quan đến công việc, người làm việc.' },
      { content: '2. a. persuade b. basis c. mission d. debate', options: ['b, c', 'a, d', 'b, d', 'a, b', 'c, d'], correctAnswer: 'a, d', explanation: 'persuade và debate đều liên quan đến tranh luận và thuyết phục.' },
      { content: '3. a. depress b. colony c. occupation d. overseas', options: ['b, c', 'a, d', 'b, d', 'a, b', 'c, d'], correctAnswer: 'b, d', explanation: 'colony và overseas đều liên quan đến một vùng đất, hải ngoại.' },
      { content: '4. a. route b. depart c. cheer d. fascinate', options: ['b, c', 'a, d', 'b, d', 'a, b', 'c, d'], correctAnswer: 'a, b', explanation: 'route và depart đều liên quan đến di chuyển, chuyến đi.' },
      { content: '5. a. ruins b. factual c. significant d. nevertheless', options: ['b, c', 'a, d', 'b, d', 'a, b', 'c, d'], correctAnswer: 'b, c', explanation: 'factual và significant đều là tính từ mô tả tầm quan trọng, thực tế.' }
    ]
  },
  {
    title: 'Write a word that is similar in meaning to the underlined part.',
    questions: [
      { content: '1. He had a very important job that he loved.', options: ['mission', 'colleague', 'route', 'factual'], correctAnswer: 'mission', explanation: 'important job đồng nghĩa với mission.' },
      { content: '2. Linda was happy that she had good people at work.', options: ['colleagues', 'basis', 'ruins', 'debate'], correctAnswer: 'colleagues', explanation: 'people at work đồng nghĩa với colleagues.' },
      { content: '3. Bernie had never taken that way home before.', options: ['route', 'volcano', 'overseas', 'occupation'], correctAnswer: 'route', explanation: 'way đồng nghĩa với route.' },
      { content: '4. This is a true movie about her life.', options: ['factual', 'significant', 'depart', 'fascinate'], correctAnswer: 'factual', explanation: 'true đồng nghĩa với factual.' },
      { content: '5. Our country used to have one other country under our control.', options: ['colony', 'cage', 'scholar', 'nevertheless'], correctAnswer: 'colony', explanation: 'country under our control đồng nghĩa với colony.' }
    ]
  },
  {
    title: 'Check the sentence with the bolded word that makes better sense.',
    questions: [
      { content: '1. a. Scholars can teach you many things that you didn’t know. b. Some people like to live in cities, while others like to live in ruins.', options: ['a', 'b'], correctAnswer: 'a', explanation: 'Scholars (học giả) có thể dạy nhiều điều. Ruins là đống đổ nát, không ai sống ở đó.' },
      { content: '2. a. Most people fly on a plane when they go overseas. b. You should watch factual movies if you want to laugh.', options: ['a', 'b'], correctAnswer: 'a', explanation: 'Mọi người thường đi máy bay khi ra nước ngoài (overseas).' },
      { content: '3. a. Many people feel happy when they depart on a trip. b. Doctors never persuade people to take medicine.', options: ['a', 'b'], correctAnswer: 'a', explanation: 'Mọi người thấy vui khi khởi hành (depart) đi chơi.' },
      { content: '4. a. If you travel overseas, you are still in the same country. b. Seeing new things fascinates most people.', options: ['a', 'b'], correctAnswer: 'b', explanation: 'Thấy những điều mới mẻ thường lôi cuốn (fascinates) mọi người.' },
      { content: '5. a. Some people like to visit ruins to learn about the past. b. Getting something they want often depresses people.', options: ['a', 'b'], correctAnswer: 'a', explanation: 'Người ta thường đến thăm di tích (ruins) để học về quá khứ.' },
      { content: '6. a. Some students like biology because they learn about rocks. b. When people debate about something, they have different ideas.', options: ['a', 'b'], correctAnswer: 'b', explanation: 'Khi người ta tranh luận (debate), họ có những ý kiến khác nhau.' },
      { content: '7. a. You should see a scholar if you don’t want to do your homework. b. People who talk about sad things can depress you.', options: ['a', 'b'], correctAnswer: 'b', explanation: 'Người nói về chuyện buồn có thể làm bạn chán nản (depress).' },
      { content: '8. a. Some students debate to get their work done faster. b. I tried to persuade my friends to meet me for lunch today.', options: ['a', 'b'], correctAnswer: 'b', explanation: 'Tôi cố gắng thuyết phục (persuade) bạn tôi gặp nhau ăn trưa.' },
      { content: '9. a. If you study biology, you will learn about different animals. b. People fall asleep when a movie fascinates them.', options: ['a', 'b'], correctAnswer: 'a', explanation: 'Nếu bạn học sinh học (biology), bạn sẽ học về các động vật khác nhau.' },
      { content: '10. a. If you depart late, you can get to school early. b. People who like to know the truth like factual stories.', options: ['a', 'b'], correctAnswer: 'b', explanation: 'Người thích sự thật thường thích những câu chuyện có thật (factual).' }
    ]
  }
];

const story_exercise = {
  title: 'Answer the questions.',
  questions: [
    { content: '1. What is this story about?', options: ['A route to a new place', 'A scholar who finds a talking bird', 'How to learn about biology', 'Why people debate each other'], correctAnswer: 'A scholar who finds a talking bird', explanation: 'Câu chuyện kể về một học giả tìm thấy một con chim biết nói.' },
    { content: '2. Why did Dr. Norton go overseas?', options: ['He wanted to depart from his colleagues and start a new life.', 'He was on a mission to find the talking bird.', 'He wanted to see the volcano.', 'He wanted to discover some old ruins.'], correctAnswer: 'He was on a mission to find the talking bird.', explanation: 'Ông ấy ra nước ngoài để thực hiện nhiệm vụ (mission) tìm con chim biết nói.' },
    { content: '3. At the end of the story, we can infer that ____________.', options: ['Jai didn’t like Dr. Norton but nevertheless cheered his discovery', 'finding the volcano was also a significant discovery', 'the bird would be the factual proof that would persuade his colleagues', 'the bird had fascinated people in the colony for a longtime'], correctAnswer: 'the bird would be the factual proof that would persuade his colleagues', explanation: 'Con chim sẽ là bằng chứng thực tế (factual proof) để thuyết phục đồng nghiệp.' },
    { content: '4. According to the passage, all the following are true EXCEPT', options: ['Jai fed bread to the talking bird', 'Dr. Norton put the bird into a cage', 'Dr. Norton took a ship to the colony', 'the talking bird was in the ruins'], correctAnswer: 'Jai fed bread to the talking bird', explanation: 'Chi tiết Jai cho chim ăn bánh mì không được nhắc đến trong truyện.' }
  ]
};

// Generate final unit7.json

// 1. Highlight target words in HTML
let htmlString = "";
story.paragraphs.forEach(paragraph => {
  let p = paragraph;
  wordsData.forEach(w => {
    // case-insensitive match for the whole word or plural forms if possible, wait, just regular expression exact matches for simplicity but taking care of capitalized letters
    // Actually simple case insensitive word boundary regex
    const regex = new RegExp("\\b(" + w.word + "(?:s|es|d|ed|ing|ly)?)\\b", "gi");
    p = p.replace(regex, "<strong>$1</strong>");
  });
  htmlString += `<p style="margin-bottom: 1rem;">${p}</p>`;
});

// Single line HTML
htmlString = htmlString.replace(/\n/g, '').replace(/\s+/g, ' ');

// 2. format for final JSON
const finalJson = {
  unit: 7,
  title: "Unit 7",
  vocabulary: wordsData.map(w => ({
    word: w.word,
    type: w.pos,
    pronunciation: w.pron,
    meaning: "",
    definition: w.def,
    example: w.ex,
    image_url: "",
    audio_url: `https://rbfsyvxtvyqvnwzcdwnd.supabase.co/storage/v1/object/public/vocabulary/vol_2/unit7/${w.word.toLowerCase()}.mp3`
  })),
  reading: {
    title: story.title,
    content_html: htmlString
  },
  exercises: [
    ...word_list_exercises.map(ex => ({
      title: ex.title,
      type: "multiple_choice",
      questions: ex.questions.map(q => ({
        question: q.content,
        options: q.options,
        answer: q.correctAnswer,
        explanation: q.explanation
      }))
    })),
    {
      title: story_exercise.title,
      type: "reading_comprehension",
      questions: story_exercise.questions.map(q => ({
        question: q.content,
        options: q.options,
        answer: q.correctAnswer,
        explanation: q.explanation
      }))
    }
  ]
};

fs.writeFileSync('unit7.json', JSON.stringify(finalJson, null, 2));
console.log('unit7.json created successfully');
