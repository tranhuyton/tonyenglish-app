const fs = require('fs');

const unitData = {
  unit: 11,
  words: [
    { word: "anticipate", pos: "v.", pron: "[æntísəpèit]", def: "To anticipate something is to think that it will happen.", ex: "Carrie anticipated the arrival of her baby." },
    { word: "barrel", pos: "n.", pron: "[bǽrəl]", def: "A barrel is a round thing that you can keep liquids in.", ex: "There was an empty barrel outside the house." },
    { word: "beam", pos: "n.", pron: "[bi:m]", def: "A beam is a heavy bar.", ex: "Modern skyscrapers are made with several beams." },
    { word: "casual", pos: "adj.", pron: "[kǽʒuəl]", def: "If something is casual, it is relaxed or simple.", ex: "You can wear casual clothes to the party like jeans." },
    { word: "caution", pos: "n.", pron: "[kɔ́:ʃən]", def: "Caution is care and attention in order to avoid danger.", ex: "Please use the power saw with caution. It is very dangerous." },
    { word: "contrary", pos: "adj.", pron: "[kɑ́ntreri]", def: "If something is contrary to something else, it is the opposite.", ex: "It isn't warm outside at all. On the contrary, it is quite cold." },
    { word: "deliberate", pos: "adj.", pron: "[dilíbərit]", def: "If you are deliberate, you do something on purpose.", ex: "Bernie made a deliberate attempt to injure Andy." },
    { word: "dissolve", pos: "v.", pron: "[dizɑ́lv]", def: "To dissolve something is to mix it into a liquid and disappear.", ex: "I dissolved the pill in a glass of water." },
    { word: "explode", pos: "v.", pron: "[iksplóud]", def: "When something explodes, it blows up.", ex: "My new radio exploded when I plugged it in." },
    { word: "fasten", pos: "v.", pron: "[fǽsn]", def: "To fasten something is to close it or put it in the correct place.", ex: "Elizabeth fastened her seat belt." },
    { word: "germ", pos: "n.", pron: "[dʒə:rm]", def: "A germ is something that makes you sick.", ex: "Germs are on everything that you touch." },
    { word: "kit", pos: "n.", pron: "[kit]", def: "A kit is a set of all the things needed to do something.", ex: "Is there a first aid kit in your office?" },
    { word: "puff", pos: "n.", pron: "[pʌf]", def: "A puff is a little bit of smoke or steam.", ex: "A puff of smoke came from the burnt match." },
    { word: "rag", pos: "n.", pron: "[ræg]", def: "A rag is a small towel.", ex: "Please use a rag to clean the dust off the table." },
    { word: "scatter", pos: "v.", pron: "[skǽtər]", def: "To scatter something is to make it go in many places.", ex: "I accidentally scattered all of my pills." },
    { word: "scent", pos: "n.", pron: "[sent]", def: "A scent is a smell.", ex: "Julie enjoyed the scent of the flowers." },
    { word: "steel", pos: "n.", pron: "[sti:l]", def: "Steel is a shiny gray metal.", ex: "The new apartment building was made with steel." },
    { word: "swift", pos: "adj.", pron: "[swift]", def: "If something is swift, it is fast.", ex: "The swift horse easily jumped over the hurdle." },
    { word: "toss", pos: "v.", pron: "[tɔ:s]", def: "If you toss something, you throw it softly.", ex: "He tossed a coin into the air." },
    { word: "triumph", pos: "n.", pron: "[tráiəmf]", def: "Triumph is what you feel when you win or finish something.", ex: "He raised the award in triumph at the end of his speech." }
  ],
  story: {
    title: "The Ice Cream Cone Explosion",
    paragraphs: [
      "One day, John walked to his uncle's ice cream shop. When he reached the sidewalk, he caught the scent of ice cream cones and anticipated eating some ice cream.",
      "Sam opened the door. Uncle John had a new, steel machine. \"What is that?\"",
      "\"It's a cone maker. I built it from a kit. You take flour from the barrel and put it in this pan,\" Uncle John said. \"Then add water and sugar here and stir it so the sugar dissolves. Next, you fasten down the beam.\" Uncle John wanted to look casual, but he was excited. He made a few swift motions and turned it on. There was a puff of smoke, and then cones came out the other end.",
      "\"Is it hard to use?\" Sam asked.",
      "\"On the contrary. It's easy to use. Want to try?\"",
      "Sam washed his hands with caution. He made a deliberate attempt to keep germs out of the dough. Soon, Sam had his first cone. He smiled in triumph!",
      "Uncle John tried to turn the machine off, but it just kept making cones. Sam and Uncle John put them on the counter, then on chairs. Before long, cones scattered all over the floor.",
      "They tried everything to stop it, but it wouldn't stop!",
      "\"What are we going to do?\" he said.",
      "\"Kick it!\" yelled Sam. Uncle John lifted his foot and gave the machine a kick. It made a funny noise and exploded. They were both covered with dough.",
      "Uncle John laughed when he knew Sam was OK. He tossed Sam a rag to clean his face and smiled. \"I guess we have enough cones now!\""
    ]
  },
  word_list_exercises: [
    {
      title: "Part A: Choose the right definition for the given word.",
      questions: [
        { content: "1. anticipate", options: ["a. to win", "b. to wait for", "c. to blow up", "d. to go everywhere"], correctAnswer: "b. to wait for", explanation: "anticipate (mong đợi, dự đoán) = to wait for" },
        { content: "2. kit", options: ["a. something that makes you sick", "b. set of things needed to do something", "c. a round container", "d. a smell"], correctAnswer: "b. set of things needed to do something", explanation: "kit (bộ dụng cụ) = set of things needed to do something" },
        { content: "3. steel", options: ["a. a large bar", "b. a small towel", "c. shiny metal", "d. opposite"], correctAnswer: "c. shiny metal", explanation: "steel (thép) = shiny metal" },
        { content: "4. contrary", options: ["a. careful", "b. the opposite", "c. fast", "d. to lockdown"], correctAnswer: "b. the opposite", explanation: "contrary (ngược lại) = the opposite" },
        { content: "5. toss", options: ["a. to throw", "b. small amount", "c. to smell", "d. smoke"], correctAnswer: "a. to throw", explanation: "toss (quăng, ném) = to throw" },
        { content: "6. triumph", options: ["a. to win", "b. the opposite", "c. to lock something in place", "d. a heavy metal bar"], correctAnswer: "a. to win", explanation: "triumph (chiến thắng) = to win" },
        { content: "7. scatter", options: ["a. careful", "b. metal", "c. relaxed or simple", "d. to go in many places"], correctAnswer: "d. to go in many places", explanation: "scatter (phân tán, rải rác) = to go in many places" },
        { content: "8. casual", options: ["a. a large bar", "b. not fancy", "c. relaxed or simple", "d. opposite"], correctAnswer: "c. relaxed or simple", explanation: "casual (thông thường, tự nhiên) = relaxed or simple" },
        { content: "9. rag", options: ["a. careful", "b. a small towel", "c. on purpose", "d. to expect something"], correctAnswer: "b. a small towel", explanation: "rag (giẻ lau) = a small towel" },
        { content: "10. beam", options: ["a. to throw", "b. metal", "c. to be careful", "d. a heavy metal bar"], correctAnswer: "d. a heavy metal bar", explanation: "beam (cột, xà) = a heavy metal bar" }
      ]
    },
    {
      title: "Part B: Choose the right word for the given definition.",
      questions: [
        { content: "1. a round container", options: ["a. scent", "b. kit", "c. beam", "d. barrel"], correctAnswer: "d. barrel", explanation: "barrel: thùng rỗng, hình trụ" },
        { content: "2. on purpose", options: ["a. deliberate", "b. casual", "c. swift", "d. contrary"], correctAnswer: "a. deliberate", explanation: "deliberate: cố ý" },
        { content: "3. something that makes you sick", options: ["a. puff", "b. rag", "c. germs", "d. triumph"], correctAnswer: "c. germs", explanation: "germs: vi trùng" },
        { content: "4. to lock something in place", options: ["a. anticipate", "b. fasten", "c. scatter", "d. explode"], correctAnswer: "b. fasten", explanation: "fasten: thắt chặt, khóa chặt" },
        { content: "5. to mix in a liquid and disappear", options: ["a. caution", "b. toss", "c. dissolve", "d. steel"], correctAnswer: "c. dissolve", explanation: "dissolve: hòa tan" }
      ]
    },
    {
      title: "Part C: Write a word that is similar in meaning to the underlined part.",
      questions: [
        { content: "1. When the house burned, a large heavy bar fell from the ceiling.", options: ["A. beam", "B. kit", "C. rag", "D. puff"], correctAnswer: "A. beam", explanation: "a large heavy bar = beam (cái xà)" },
        { content: "2. Joshua smiled in great emotion and feeling after he got a good grade on his science test.", options: ["A. triumph", "B. caution", "C. scent", "D. contrary"], correctAnswer: "A. triumph", explanation: "great emotion and feeling (after winning) = triumph (sự chiến thắng)" },
        { content: "3. She walked on the ice with care so she wouldn't fall.", options: ["A. triumph", "B. caution", "C. kit", "D. barrel"], correctAnswer: "B. caution", explanation: "with care = caution (sự cẩn thận)" },
        { content: "4. It was scary when the car blew up, but luckily no one was hurt.", options: ["A. scattered", "B. dissolved", "C. fastened", "D. exploded"], correctAnswer: "D. exploded", explanation: "blew up = exploded (nổ tung)" },
        { content: "5. I used a small towel from the sink to clean up the milk I spilled.", options: ["A. rag", "B. scent", "C. beam", "D. puff"], correctAnswer: "A. rag", explanation: "a small towel = rag (giẻ lau)" },
        { content: "6. The basketball player was fast and stole the ball.", options: ["A. casual", "B. swift", "C. contrary", "D. deliberate"], correctAnswer: "B. swift", explanation: "fast = swift (nhanh chóng)" },
        { content: "7. You can wear relaxed and simple clothes to the school.", options: ["A. swift", "B. casual", "C. deliberate", "D. contrary"], correctAnswer: "B. casual", explanation: "relaxed and simple = casual (đơn giản, bình thường)" },
        { content: "8. I really like the smell of this candle.", options: ["A. scent", "B. kit", "C. rag", "D. puff"], correctAnswer: "A. scent", explanation: "smell = scent (mùi hương)" },
        { content: "9. My cat made her food go in many places.", options: ["A. scattered", "B. fastened", "C. anticipated", "D. dissolved"], correctAnswer: "A. scattered", explanation: "go in many places = scattered (phân tán, rải rác)" },
        { content: "10. When we lit the fire, a little smoke came out of the chimney.", options: ["A. puff", "B. rag", "C. barrel", "D. germ"], correctAnswer: "A. puff", explanation: "a little smoke = puff (luồng khói)" }
      ]
    }
  ],
  story_exercise: {
    title: "Answer the questions based on the story.",
    questions: [
      {
        content: "Mark each statement T for true or F for false.",
        options: ["A. 1.T 2.T 3.F 4.F 5.T 6.T", "B. 1.F 2.T 3.T 4.F 5.T 6.F", "C. 1.T 2.F 3.T 4.T 5.F 6.T", "D. 1.F 2.F 3.F 4.T 5.T 6.T"],
        correctAnswer: "A. 1.T 2.T 3.F 4.F 5.T 6.T",
        explanation: "1. T (John caught the scent of ice cream cones)\n2. T (The cone maker was built from a kit)\n3. F (You have to fasten the beam)\n4. F (Sam washed the germs off his hands)\n5. T (Cones scattered all over the floor)\n6. T (Uncle John tossed Sam a rag)"
      },
      {
        content: "1. Why did Uncle John toss a rag to Sam?",
        options: ["a. To clean the floor", "b. To dissolve the sugar", "c. To clean his face", "d. To clean the steel"],
        correctAnswer: "c. To clean his face",
        explanation: "Theo câu chuyện, Uncle John đưa giẻ lau để Sam lau mặt."
      },
      {
        content: "2. What did Sam anticipate?",
        options: ["a. Going to the shop", "b. Getting an ice cream cone", "c. Working with his uncle", "d. The machine exploding"],
        correctAnswer: "b. Getting an ice cream cone",
        explanation: "Cậu bé mong được ăn kem (anticipated eating some ice cream)."
      },
      {
        content: "3. What did the machine do?",
        options: ["a. Break the barrel", "b. Give a bad scent", "c. Scatter dough", "d. Give a puff of smoke"],
        correctAnswer: "d. Give a puff of smoke",
        explanation: "Máy phà ra khói (There was a puff of smoke)."
      },
      {
        content: "4. What did Uncle John say about the machine?",
        options: ["a. It's easy to use.", "b. It was swift.", "c. It was deliberate.", "d. It was contrary."],
        correctAnswer: "a. It's easy to use.",
        explanation: "Ông chú nói máy dễ sử dụng (It's easy to use)."
      }
    ]
  }
};

fs.writeFileSync('unit11_raw.json', JSON.stringify(unitData, null, 2));
