const fs = require('fs');

const unit26 = {
  unit: 26,
  words: [
    { word: "alter", pos: "v.", pron: "[ɔːltər]", def: "To alter something means to make a small change to it.", ex: "I altered the color of my nails to match my hair." },
    { word: "aside", pos: "adv.", pron: "[əsaid]", def: "If someone stands aside, they are on or to one side.", ex: "The man stood aside and opened the door for me." },
    { word: "autumn", pos: "n.", pron: "[ɔːtəm]", def: "Autumn is the season of the year between summer and winter.", ex: "I love when the leaves fall in autumn because I can play in them." },
    { word: "blend", pos: "v.", pron: "[blend]", def: "To blend is to mix two or more things together so that they become one thing.", ex: "My wife blended together all of the ingredients to make a delicious stew." },
    { word: "collapse", pos: "v.", pron: "[kəlæps]", def: "To collapse is to fall down suddenly.", ex: "The tree collapsed right in front of our house." },
    { word: "crush", pos: "v.", pron: "[krʌʃ]", def: "To crush something is to press it together so its shape is destroyed.", ex: "Selena's new car was crushed when something fell on top of it." },
    { word: "curve", pos: "v.", pron: "[kəːrv]", def: "To curve is to move in a line that bends and does not go straight.", ex: "The road curves to the left and to the right." },
    { word: "disgusting", pos: "adj.", pron: "[disgʌstiŋ]", def: "If something is disgusting, it is very unpleasant.", ex: "After running all day, Greg's feet had a disgusting odor." },
    { word: "drain", pos: "n.", pron: "[drein]", def: "A drain is a pipe that carries away water from a building, such as in a kitchen.", ex: "The water in the sink goes down the drain as you wash your hands." },
    { word: "embrace", pos: "v.", pron: "[imbreis]", def: "To embrace is to hug.", ex: "When they saw each other again, the happy couple embraced." },
    { word: "envy", pos: "v.", pron: "[envi]", def: "To envy someone is to wish that you had something that they have.", ex: "Sally envied the happy couple." },
    { word: "fireworks", pos: "n.", pron: "[faiərwəːrks]", def: "Fireworks are objects that create colored lights when they are lit.", ex: "The display of fireworks was so beautiful." },
    { word: "flour", pos: "n.", pron: "[flauər]", def: "Flour is a powder made from plants that is used to make foods like bread.", ex: "I wanted to bake a pie, but I needed flour." },
    { word: "fuse", pos: "n.", pron: "[fjuːz]", def: "A fuse is a string that you light on fireworks to make them explode.", ex: "The boy lit the fuse on the rocket and waited for it to burst in the sky." },
    { word: "ginger", pos: "n.", pron: "[dʒindʒər]", def: "Ginger is a spice from the root of a plant. It tastes spicy and sweet.", ex: "Ginger is a common ingredient in many dishes from India." },
    { word: "jealous", pos: "adj.", pron: "[dʒeləs]", def: "If you are jealous, you think someone might take something from you.", ex: "Miriam was jealous because Sue was paying too much attention to jim." },
    { word: "paste", pos: "n.", pron: "[peist]", def: "A paste is a thick and smooth substance.", ex: "My son needed some paste for a school project." },
    { word: "receipt", pos: "n.", pron: "[risiːt]", def: "A receipt is a paper that proves that something was received or bought.", ex: "After looking at my receipt, I realized that I had spent too much money." },
    { word: "wipe", pos: "v.", pron: "[waip]", def: "To wipe something is to slide a piece of cloth over it to clean it.", ex: "She wiped the dust from the windows." },
    { word: "wire", pos: "n.", pron: "[waiər]", def: "A wire is a thin string made out of metal.", ex: "The wires were connected to towers that brought electricity to the city." }
  ],
  story: {
    title: "Everyone is Special",
    paragraphs: [
      "When I was young, everything that went wrong in my house seemed to be my fault. Once, my brothers tried to make cookies. They blended flour and ginger and made a disgusting paste. Then they tried to wash it down the drain, but it got all over the floor. Later, my brothers said that I did it and I had to wipe it up.",
      "I worried that my parents liked them more than me. One autumn day, I was sure I would make my parents proud. I bought a model rocket. After I put it together, I invited everybody to watch it. I wanted my brothers to envy my technical knowledge. I lit the fuse, but nothing happened.",
      "\"Looks like your fireworks don't work. I hope you kept the receipt so you can return them,\" my brother said.",
      "\"It's not fireworks!\" I screamed. They were making fun of me again.",
      "I didn't know what went wrong. I hadn't altered anything. I quickly moved the wires on the bottom, hoping that would help. Suddenly, the rocket flew up. We stood aside as it curved through the lawn and ran straight into the mailbox. Then the mailbox collapsed. The rocket was crushed.",
      "Embarrassed, I ran inside and hid. A few minutes later, my mom asked, \"Are you OK?\"",
      "\"I just wanted them to be jealous of me for once. Now I see why you and Dad don't love me as much as them,\" I said.",
      "\"That's not true!\" said my mom. \"See my fingers... each one is different. You kids are like my fingers: all are different, but I love them all the same.\"",
      "I embraced her. Now I know that my parents love me just as much as my brothers."
    ]
  },
  word_list_exercises: [
    {
      title: "Write a word that is similar in meaning to the underlined part.",
      questions: [
        {
          content: "1. The mixture was a funny color and looked very unpleasant.",
          options: ["a. disgusting", "b. paste", "c. ginger", "d. flour"],
          correctAnswer: "a. disgusting",
          explanation: "unpleasant = disgusting"
        },
        {
          content: "2. After the house fell down suddenly, the family built a new home somewhere else.",
          options: ["a. collapsed", "b. altered", "c. crushed", "d. embraced"],
          correctAnswer: "a. collapsed",
          explanation: "fell down suddenly = collapsed"
        },
        {
          content: "3. When the boy spilled his milk, his mother rubbed a cloth over it.",
          options: ["a. curved", "b. wiped", "c. altered", "d. blended"],
          correctAnswer: "b. wiped",
          explanation: "rubbed a cloth over it = wiped"
        },
        {
          content: "4. The bird moved in a line that was not straight through the sky.",
          options: ["a. aside", "b. curved", "c. collapsed", "d. wiped"],
          correctAnswer: "b. curved",
          explanation: "moved in a line that was not straight = curved"
        },
        {
          content: "5. The mother hugged the crying child to make her feel better.",
          options: ["a. embraced", "b. envied", "c. wiped", "d. crushed"],
          correctAnswer: "a. embraced",
          explanation: "hugged = embraced"
        },
        {
          content: "6. The farmer's food was usually ready in the season before winter.",
          options: ["a. autumn", "b. fireworks", "c. receipt", "d. fuse"],
          correctAnswer: "a. autumn",
          explanation: "season before winter = autumn"
        },
        {
          content: "7. The metal string was in between the two poles.",
          options: ["a. drain", "b. paste", "c. wire", "d. ginger"],
          correctAnswer: "c. wire",
          explanation: "metal string = wire"
        },
        {
          content: "8. She made small changes to her drawing before giving it to her friend.",
          options: ["a. altered", "b. blended", "c. crushed", "d. envied"],
          correctAnswer: "a. altered",
          explanation: "made small changes = altered"
        },
        {
          content: "9. The pipe that carries water away was clogged with hair.",
          options: ["a. wire", "b. drain", "c. fuse", "d. receipt"],
          correctAnswer: "b. drain",
          explanation: "pipe that carries water away = drain"
        },
        {
          content: "10. I asked the taxi driver to give me a document that proved how much I paid.",
          options: ["a. receipt", "b. paste", "c. flour", "d. ginger"],
          correctAnswer: "a. receipt",
          explanation: "document that proved how much I paid = receipt"
        }
      ]
    }
  ],
  story_exercise: {
    title: "Answer the questions based on the story.",
    questions: [
      {
        content: "1. All of the following happened when the brothers tried to cook EXCEPT...",
        options: ["a. they wiped up the mess", "b. they tried to put the paste down the drain", "c. they blended ginger and flour", "d. they got the floor dirty"],
        correctAnswer: "a. they wiped up the mess",
        explanation: "The narrator wiped up the mess, not the brothers."
      },
      {
        content: "2. The girl thought that putting together the model rocket proved her...",
        options: ["a. computer skills", "b. technical knowledge", "c. experience working with wires", "d. disgust of fireworks"],
        correctAnswer: "b. technical knowledge",
        explanation: "The story says: 'I wanted my brothers to envy my technical knowledge.'"
      },
      {
        content: "3. Why does her brother say that he hopes she kept the receipt?",
        options: ["a. He envies her rocket.", "b. He wants to buy her a new rocket.", "c. He wants her to save money.", "d. He thinks she should return the rocket."],
        correctAnswer: "d. He thinks she should return the rocket.",
        explanation: "Because he thinks it's broken fireworks."
      },
      {
        content: "4. The mother tells the girl that her children are like her fingers because...",
        options: ["a. some are larger than others", "b. they all are small", "c. some are more important", "d. they all are different but loved"],
        correctAnswer: "d. they all are different but loved",
        explanation: "The mother says: 'all are different, but I love them all the same.'"
      }
    ]
  }
};

fs.writeFileSync('unit26_raw.json', JSON.stringify(unit26, null, 2));
console.log('Created unit26_raw.json');
