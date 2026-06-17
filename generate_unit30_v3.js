const fs = require('fs');

const words = [
  { word: "appliance", pron: "[əplaiəns]", pos: "n.", def: "An appliance is a piece of equipment used for jobs in the home.", ex: "Many homes have appliances like ovens, toasters and refrigerators." },
  { word: "basin", pron: "[beisn]", pos: "n.", def: "A basin is large bowl for washing things. A sink is sometimes called a basin.", ex: "She filled the basin with water and washed her face." },
  { word: "broom", pron: "[bru:m]", pos: "n.", def: "A broom is a brush with a long handle used for cleaning floors.", ex: "My father usually uses a broom to sweep away dust in the basement." },
  { word: "caterpillar", pron: "[kætərpilər]", pos: "n.", def: "A caterpillar is a small insect that looks like a worm and eats plants.", ex: "After eating a lot of leaves, caterpillars change into butterflies." },
  { word: "cupboard", pron: "[kʌbərd]", pos: "n.", def: "A cupboard is a piece of furniture that is used to store food or household items.", ex: "We put all of our dishes and food in the cupboards." },
  { word: "delicate", pron: "[delikət]", pos: "adj.", def: "If something or someone is delicate, they are easy to break or harm.", ex: "You should hold the baby carefully because she’s very delicate." },
  { word: "emerge", pron: "[imə:rdʒ]", pos: "v.", def: "To emerge from something means to come out of it.", ex: "The hand suddenly emerged from the grave." },
  { word: "handicap", pron: "[hændikæp]", pos: "n.", def: "A handicap is a condition that limits someone’s mental or physical abilities.", ex: "Joe has a slight handicap, so he uses a walker to get around." },
  { word: "hook", pron: "[huk]", pos: "n.", def: "A hook is a sharp curved piece of metal used for catching or holding things.", ex: "The fish went after the sharp hook." },
  { word: "hop", pron: "[hɑp]", pos: "v.", def: "To hop means to jump a short distance.", ex: "The kangaroo quickly hopped away from danger." },
  { word: "laundry", pron: "[lɔ:ndri]", pos: "n.", def: "Laundry is clothes that have been or need to be washed.", ex: "He folded the clean laundry and put the dirty laundry in a basket." },
  { word: "pursue", pron: "[pərsu:]", pos: "v.", def: "To pursue someone or something is to chase or follow them.", ex: "The mother pursued her young child down the hill." },
  { word: "reluctant", pron: "[rilʌktənt]", pos: "adj.", def: "If someone is reluctant, they do not want to do something.", ex: "She was reluctant to eat the meager breakfast." },
  { word: "sleeve", pron: "[sli:v]", pos: "n.", def: "Sleeves are the part of a shirt where your arms go.", ex: "Ryan bought a new shirt with long sleeves to keep his arms warm." },
  { word: "spine", pron: "[spain]", pos: "n.", def: "The spine is the bone that runs up and down the middle of the back.", ex: "Our spine helps us to stand up nice and straight." },
  { word: "stain", pron: "[stein]", pos: "n.", def: "A stain is a dirty mark that is difficult to clean.", ex: "He had a red stain on the collar of his shirt." },
  { word: "strip", pron: "[strip]", pos: "n.", def: "A strip is a long, narrow piece of material or land.", ex: "He had long strips of film that held images of his trip abroad." },
  { word: "swear", pron: "[swɛər]", pos: "v.", def: "To swear means to promise to do something.", ex: "I will put my hand on the Bible and swear to do my best for the country." },
  { word: "swing", pron: "[swiŋ]", pos: "v.", def: "To swing something means to move it back and forth or from side to side.", ex: "He can swing a golf club very powerfully." },
  { word: "utilize", pron: "[ju:təlaiz]", pos: "v.", def: "To utilize something means to use it for a specific purpose.", ex: "They utilized a pair of scissors to cut the ribbon." }
];

const questions1 = [
  { content: "1. clothes that need to be washed", options: ["spine", "appliance", "laundry", "cupboard"], correctAnswer: "laundry", explanation: "laundry nghĩa là clothes that need to be washed." },
  { content: "2. easy to break", options: ["emerge", "delicate", "basin", "pursue"], correctAnswer: "delicate", explanation: "delicate nghĩa là easy to break." },
  { content: "3. a brush with a long handle used for cleaning floors", options: ["handicap", "broom", "utilize", "hook"], correctAnswer: "broom", explanation: "broom nghĩa là a brush with a long handle used for cleaning floors." },
  { content: "4. to promise something", options: ["swear", "hop", "caterpillar", "swing"], correctAnswer: "swear", explanation: "swear nghĩa là to promise something." },
  { content: "5. not wanting to do something", options: ["sleeve", "stain", "strip", "reluctant"], correctAnswer: "reluctant", explanation: "reluctant nghĩa là not wanting to do something." }
];

const questions2 = [
  { content: "1. pursue", options: ["a bone in the middle of the back", "a bowl for washing things", "to come out of something", "to chase after something"], correctAnswer: "to chase after something", explanation: "pursue nghĩa là theo đuổi, săn đuổi." },
  { content: "2. appliance", options: ["a piece of equipment used in the home", "a section of cloth used to cover a floor", "a wooden box used for storing things", "a dirty mark that is difficult to clean"], correctAnswer: "a piece of equipment used in the home", explanation: "appliance nghĩa là thiết bị trong nhà." },
  { content: "3. utilize", options: ["to jump a short distance", "an insect that looks like a worm", "to move something back and forth", "to use something for a specific purpose"], correctAnswer: "to use something for a specific purpose", explanation: "utilize nghĩa là sử dụng cho mục đích cụ thể." },
  { content: "4. handicap", options: ["a curved metal for holding things", "something that is easy to break", "a promise to do something", "a condition that limits abilities"], correctAnswer: "a condition that limits abilities", explanation: "handicap nghĩa là nhược điểm, khuyết tật." },
  { content: "5. swing", options: ["to move something back and forth", "a curved piece of metal", "a brush with a long handle", "clothes that need to be washed"], correctAnswer: "to move something back and forth", explanation: "swing nghĩa là đu đưa, đung đưa." }
];

const paragraphs = [
  "Katie the kitten liked to play. One day, Cory the caterpillar emerged from a hole in the wall while Katie was playing in the living room.",
  "“Hey!” Katie yelled. “Do you want to play with me?”",
  "Cory was reluctant. He said, “I’d rather not play with you. I have several handicaps. My body is very delicate. Your claws are as sharp as hooks. You might cut me. Plus, I have no bones, not even a spine. You could easily hurt me.”",
  "“I swear that I won’t hurt you,” Katie said.",
  "“No, I don’t want to,” he said again. He hopped from the wall, but Katie pursued him.",
  "Cory ran into the kitchen and into the cupboard, but Katie chased closely behind. Katie knocked appliances to the floor. Plates fell into the sink and broke in the basin.",
  "Then he ran into a bedroom. Some laundry was on the floor. Cory hid under a shirt, but Katie saw him. She jumped on the shirt. Her paws left stains on the cloth, and her claws ripped the sleeves into strips.",
  "However, Cory escaped. He utilized a small crack in the floor to hide. But Katie saw him.",
  "“Now you are trapped!” said Katie.",
  "Cory tried to avoid Katie’s claws. He moved his body as far into the hole as possible. He didn’t know how he’d get out of the hole.",
  "Just then, Katie’s owner came home. She saw that the house was a mess. She took a broom and swung it at Katie. She chased Katie out of the house.",
  "Cory was safe, and Katie was left outside because she didn’t listen to the wishes of others."
];

const storyQuestions = [
  { content: "1. Which is NOT a reason that Cory was reluctant about playing with Katie?", options: ["Katie had dirty paws.", "Katie had sharp claws.", "His body was delicate.", "He had several handicaps."], correctAnswer: "Katie had dirty paws.", explanation: "Cory không nói rằng Katie có chân bẩn (Katie had dirty paws) là lý do không muốn chơi." },
  { content: "2. Where was Katie playing when Cory emerged from the wall?", options: ["On the counter", "In some laundry", "In the living room", "In the kitchen"], correctAnswer: "In the living room", explanation: "Bài đọc có câu: '...while Katie was playing in the living room.'" },
  { content: "3. Katie did all of the following damage EXCEPT ________.", options: ["knock appliances on the floor", "break plates in the basin", "crack the kitchen door", "rip the sleeves of a shirt into strips"], correctAnswer: "crack the kitchen door", explanation: "Katie không làm nứt cửa bếp (crack the kitchen door)." },
  { content: "4. What did Katie’s owner swing at her?", options: ["A broom", "A shirt", "Appliances", "Laundry"], correctAnswer: "A broom", explanation: "Bài đọc có câu: 'She took a broom and swung it at Katie.'" }
];

const json = {
  words: words,
  story: {
    title: "The Kitten and the Caterpillar",
    paragraphs: paragraphs
  },
  word_list_exercises: [
    {
      title: "Part A: Choose the right word for the given definition.",
      questions: questions1
    },
    {
      title: "Part B: Choose the right definition for the given word.",
      questions: questions2
    }
  ],
  story_exercise: {
    title: "Answer the questions based on the story.",
    questions: storyQuestions
  }
};

fs.writeFileSync('./unit30_raw.json', JSON.stringify(json, null, 2));
console.log("Successfully wrote unit30_raw.json");
