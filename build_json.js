const fs = require('fs');

const words = [
  { word: "accuse", phonetic: "[əˈkyuːz]", type: "v.", def: "To accuse someone of something is to blame them for doing it.", example: "She accused her brother of breaking her computer." },
  { word: "adjust", phonetic: "[əˈdʒʌst]", type: "v.", def: "To adjust something means to change it so it is better.", example: "He adjusted the old guitar to make it sound better." },
  { word: "amuse", phonetic: "[əˈmyuːz]", type: "v.", def: "To amuse someone means to do something that is funny or entertaining.", example: "The singer was very good. She amused the crowd." },
  { word: "coral", phonetic: "[ˈkɔːrəl]", type: "n.", def: "Coral is the hard, colorful material formed by the shells of animals.", example: "The diver admired the beautiful coral under the water." },
  { word: "cotton", phonetic: "[ˈkɑːtn]", type: "n.", def: "Cotton is a cloth made from the fibers of the cotton plant.", example: "I like to wear clothes made from cotton in the summer." },
  { word: "crash", phonetic: "[kræʃ]", type: "v.", def: "To crash means to hit and break something.", example: "There was a loud noise when the car crashed into the tree." },
  { word: "deck", phonetic: "[dek]", type: "n.", def: "A deck is a wooden floor built outside of a house or the floor of a ship.", example: "A ship will store many supplies below its deck." },
  { word: "engage", phonetic: "[ɪnˈɡeɪdʒ]", type: "v.", def: "To engage in something means to do it.", example: "Dad was engaged in sawing a piece of wood in half." },
  { word: "firm", phonetic: "[fɜːrm]", type: "adj.", def: "When something is firm, it is solid but not too hard.", example: "He sleeps better on a firm bed." },
  { word: "fuel", phonetic: "[ˈfjuːəl]", type: "n.", def: "Fuel is something that creates heat or energy.", example: "Heat is the fuel that comes from fire." },
  { word: "grand", phonetic: "[ɡrænd]", type: "adj.", def: "When something is grand, it is big and liked by people.", example: "The grand mountain rose high into the sky." },
  { word: "hurricane", phonetic: "[ˈhɜːrəkeɪn]", type: "n.", def: "A hurricane is a bad storm that happens over the ocean.", example: "The wind from the hurricane bent the palm tree." },
  { word: "loss", phonetic: "[lɔːs]", type: "n.", def: "A loss means the act or an instance of losing something.", example: "I suffered a big loss while I was gambling." },
  { word: "plain", phonetic: "[pleɪn]", type: "adj.", def: "If something is simple, it is plain and not decorated.", example: "He bought a pair of plain white shoes over the weekend." },
  { word: "reef", phonetic: "[riːf]", type: "n.", def: "A reef is a group of rocks or coral that rise to or near the ocean.", example: "He walked along the reef and looked at the water below." },
  { word: "shut", phonetic: "[ʃʌt]", type: "v.", def: "To shut something means to close it tightly.", example: "Please shut the door; the air outside is cold." },
  { word: "strict", phonetic: "[strɪkt]", type: "adj.", def: "When someone is strict, they make sure others follow rules.", example: "The teacher is strict. She does not let students talk in class." },
  { word: "surf", phonetic: "[sɜːrf]", type: "v.", def: "To surf means to use a special board to ride on waves in the ocean.", example: "The students went to the beach to surf during their vacation." },
  { word: "task", phonetic: "[tæsk]", type: "n.", def: "A task is a piece of work to be done that is usually difficult.", example: "My task for the weekend was to clean the entire back yard." },
  { word: "zone", phonetic: "[zoʊn]", type: "n.", def: "A zone is an area that has different qualities from the ones around it.", example: "Firefighters often work in danger zones." }
];

let wordsHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit26_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit26_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

for (let w of words) {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.phonetic}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.type}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.example}</div></div></div>`;
}
wordsHtml += `</div></div></div>`;

const readingHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Two Captains</h1><p style="margin-bottom: 1rem;">Once there were two ships. Both ships carried <b>cotton</b>. The captains were very different. Thomas was <b>strict</b>. He made his crew <b>engage</b> in difficult <b>tasks</b>. "Make sure the ship's <b>deck</b> is <b>firm</b> and that nothing falls! Put more <b>fuel</b> in the tank!" he said. His ship was very <b>plain</b>, but he never had a problem with it.</p><p style="margin-bottom: 1rem;">The second captain, William, was not serious. He had a <b>grand</b> ship, and he loved having fun. His crew <b>amused</b> him by singing and dancing. But his crew never fixed anything on the ship. They just wanted to <b>surf</b>.</p><p style="margin-bottom: 1rem;">One day, Thomas saw a <b>hurricane</b> ahead. He knew that his ship needed to turn around. But he was sure William did not see the storm. He <b>adjusted</b> the dials on the radio and called his friend. Thomas said, "You'll hit the <b>reef</b>. It's made completely of <b>coral</b>. Turn around to ensure that you do not <b>crash</b>."</p><p style="margin-bottom: 1rem;">William said, "We will go under the <b>deck</b> and <b>shut</b> the door. We will dance and sing until we are past the danger <b>zone</b>."</p><p style="margin-bottom: 1rem;">When William's ship got to the <b>hurricane</b>, the wind blew it into the <b>reef</b>. The ship <b>crashed</b>, and water flowed below the <b>deck</b>. William's crew <b>accused</b> him of being a bad captain. The <b>loss</b> of the ship taught William a lesson. There are times to have fun, but there are also times to be serious.</p></div>`;

const data = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 26",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordsHtml,
      sections: [
        {
          id: "sec1_wordlist",
          title: "Exercise 1: Choose the word that is a better fit for each sentence.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1a", content: "The _________ for the car is gas.", options: ["fuel", "cotton", "loss", "insure"], correctAnswer: "fuel", explanation: "" },
            { id: "1b", content: "My favorite shirt is made out of _________.", options: ["fuel", "cotton", "loss", "insure"], correctAnswer: "cotton", explanation: "" },
            { id: "2a", content: "The _________ of his job made Steve worry about money.", options: ["loss", "insure", "coral", "reef"], correctAnswer: "loss", explanation: "" },
            { id: "2b", content: "She wanted to _________ that her car was safe, so she locked the door.", options: ["loss", "insure", "coral", "reef"], correctAnswer: "insure", explanation: "" },
            { id: "3a", content: "The boy found a piece of colorful _________ in the ocean.", options: ["coral", "reef", "amuse", "surfed"], correctAnswer: "coral", explanation: "" },
            { id: "3b", content: "That group of rocks coming out of the ocean is a _________.", options: ["coral", "reef", "amuse", "surfed"], correctAnswer: "reef", explanation: "" },
            { id: "4a", content: "Funny stories always _________ me.", options: ["amuse", "surfed", "task", "shut"], correctAnswer: "amuse", explanation: "" },
            { id: "4b", content: "I _________ quite a bit when I was in Hawaii last summer.", options: ["amuse", "surfed", "task", "shut"], correctAnswer: "surfed", explanation: "" },
            { id: "5a", content: "I was given the _________ of editing his entire manuscript.", options: ["task", "shut", "fuel", "cotton"], correctAnswer: "task", explanation: "" },
            { id: "5b", content: "Don't forget to _________ the door on your way out.", options: ["task", "shut", "fuel", "cotton"], correctAnswer: "shut", explanation: "" }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Exercise 2: Fill in the blanks with the correct words from the word bank.",
          content: "Word Bank: accuse, grand, strict, ensure, shut",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "ex2_1", content: "There are _________ rules about what people may wear at fancy parties.", options: ["strict", "ensure", "grand", "accuse", "shut"], correctAnswer: "strict", explanation: "" },
            { id: "ex2_2", content: "Instead of normal things, people must _________ that they wear...", options: ["strict", "ensure", "grand", "accuse", "shut"], correctAnswer: "ensure", explanation: "" },
            { id: "ex2_3", content: "...that they wear _________ clothing.", options: ["strict", "ensure", "grand", "accuse", "shut"], correctAnswer: "grand", explanation: "" },
            { id: "ex2_4", content: "If a man wears the wrong clothes, people will _________ him of ruining the evening.", options: ["strict", "ensure", "grand", "accuse", "shut"], correctAnswer: "accuse", explanation: "" },
            { id: "ex2_5", content: "They will make him leave and _________ the door behind him.", options: ["strict", "ensure", "grand", "accuse", "shut"], correctAnswer: "shut", explanation: "" }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 3: Write a word that is similar in meaning to the underlined part.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "ex3_1", content: "He blamed me of taking the last piece of pie. (ac__________)", options: ["accused", "plain", "amuse", "adjust"], correctAnswer: "accused", explanation: "" },
            { id: "ex3_2", content: "The man's bedroom was very simple. (pla____)", options: ["plain", "accused", "amuse", "adjust"], correctAnswer: "plain", explanation: "" },
            { id: "ex3_3", content: "The clown likes to entertain children. (amu____)", options: ["amuse", "adjust", "engaged", "cotton"], correctAnswer: "amuse", explanation: "" },
            { id: "ex3_4", content: "I need to change the way I run so I can be faster. (adj______)", options: ["adjust", "engaged", "cotton", "hurricane"], correctAnswer: "adjust", explanation: "" },
            { id: "ex3_5", content: "During their free time, the children did many different activities. (en___________ in)", options: ["engaged", "cotton", "hurricane", "shut"], correctAnswer: "engaged", explanation: "" },
            { id: "ex3_6", content: "This cloth dress is one of my favorites. (co_________)", options: ["cotton", "hurricane", "shut", "crash"], correctAnswer: "cotton", explanation: "" },
            { id: "ex3_7", content: "The bad storm over the ocean almost reached the land. (hu_______________)", options: ["hurricane", "shut", "crash", "zone"], correctAnswer: "hurricane", explanation: "" },
            { id: "ex3_8", content: "Tightly close the window before the rain starts! (s______)", options: ["shut", "crash", "zone", "accused"], correctAnswer: "shut", explanation: "" },
            { id: "ex3_9", content: "He will hit something and break his bike if he closes his eyes while riding. (c_____)", options: ["crash", "zone", "accused", "plain"], correctAnswer: "crash", explanation: "" },
            { id: "ex3_10", content: "The army fights in the war area. (z____)", options: ["zone", "crash", "accused", "plain"], correctAnswer: "zone", explanation: "" }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: readingHtml,
      imageUrl: "/unit26_story.png",
      sections: [
        {
          id: "sec_reading",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            {
              id: "rc_1",
              content: "1. What is this story about?",
              options: [
                "a. Why surfing amuses William",
                "b. How Thomas is too strict to be a captain",
                "c. Why people should be serious sometimes",
                "d. Why hurricanes form over the ocean"
              ],
              correctAnswer: "c. Why people should be serious sometimes",
              explanation: ""
            },
            {
              id: "rc_2",
              content: "2. Why did Thomas turn his ship around?",
              options: [
                "a. He saw the hurricane and did not want to crash.",
                "b. He wanted to go to the reef.",
                "c. He could not shut the door.",
                "d. He wanted to engage in other activities."
              ],
              correctAnswer: "a. He saw the hurricane and did not want to crash.",
              explanation: ""
            },
            {
              id: "rc_3",
              content: "3. Why did William's crew accuse him of being a bad captain?",
              options: [
                "a. William did not go into the storm's danger zone.",
                "b. William caused the loss of the ship.",
                "c. He did not succeed in getting the cotton to its destination.",
                "d. He ensured his crew that they would not crash."
              ],
              correctAnswer: "b. William caused the loss of the ship.",
              explanation: ""
            },
            {
              id: "rc_4",
              content: "4. According to the passage, all of the following are true about Thomas EXCEPT",
              options: [
                "a. he told his crew to put fuel in the tank",
                "b. he had his crew make sure the deck was firm",
                "c. he adjusted the radio dial to call William",
                "d. he sang and danced to songs from an opera"
              ],
              correctAnswer: "d. he sang and danced to songs from an opera",
              explanation: ""
            },
            {
              id: "rc_5",
              content: "5. What happened when William's ship reached the hurricane?",
              options: [
                "When his ship reached the hurricane the wind blew it into the reef, and it crashed.",
                "The ship safely sailed through the storm.",
                "Thomas's ship rescued William's crew.",
                "The crew started singing and dancing."
              ],
              correctAnswer: "When his ship reached the hurricane the wind blew it into the reef, and it crashed.",
              explanation: ""
            }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync('C:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit26.json', JSON.stringify(data, null, 2));
