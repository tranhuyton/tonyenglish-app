const fs = require('fs');

const unitData = {
  unit: 15,
  words: [
    { word: "affair", pos: "n.", pron: "[əˈfɛər]", def: "An affair is an event or a thing that happened.", ex: "My wife and I attended a formal affair over the weekend." },
    { word: "assembly", pos: "n.", pron: "[əˈsembli]", def: "An assembly is a group that is together for the same reason.", ex: "The students had an assembly to talk about their interests." },
    { word: "bless", pos: "v.", pron: "[bles]", def: "To bless is to ask God for protection or help.", ex: "The angel blessed the newborn baby to keep it safe." },
    { word: "cereal", pos: "n.", pron: "[ˈsiəriəl]", def: "Cereal is a food that you mix with milk and eat for breakfast.", ex: "Cereal is a fast and common breakfast food enjoyed in the U.S." },
    { word: "cheerful", pos: "adj.", pron: "[ˈtʃɪərfəl]", def: "If someone is cheerful, they are happy or feel good.", ex: "The children were cheerful because they didn't have to go to school." },
    { word: "diameter", pos: "n.", pron: "[daɪˈæmɪtər]", def: "The diameter of a round thing is the length across its center.", ex: "The diameter of the tree was about 22 centimeters." },
    { word: "exploit", pos: "v.", pron: "[ɪkˈsplɔɪt]", def: "To exploit something is to use it for greedy reasons rather than good reasons.", ex: "The company exploits their workers and makes them stay 12 hours a day." },
    { word: "famine", pos: "n.", pron: "[ˈfæmɪn]", def: "A famine is a long time with little or no food.", ex: "The farmers couldn't grow any food on the dry soil, so there was a famine." },
    { word: "harvest", pos: "n.", pron: "[ˈhɑːrvɪst]", def: "A harvest is the act of collecting food from farming.", ex: "They had a lot of wheat from the last harvest." },
    { word: "merry", pos: "adj.", pron: "[ˈmeri]", def: "If someone is merry, they are very happy.", ex: "They felt merry because the weather was great." },
    { word: "nut", pos: "n.", pron: "[nʌt]", def: "A nut is a hard seed or fruit that comes from some trees and bushes.", ex: "To eat a nut, first you have to crack its shell." },
    { word: "pardon", pos: "v.", pron: "[ˈpɑːrdn]", def: "To pardon is a way to ask someone to repeat what was said before.", ex: "Pardon me teacher, but could you repeat what you just said?" },
    { word: "pharaoh", pos: "n.", pron: "[ˈfeəroʊ]", def: "A pharaoh was a king in ancient Egypt.", ex: "The pharaohs ruled Egypt for thousands of years." },
    { word: "ripe", pos: "adj.", pron: "[raɪp]", def: "When a fruit is ripe, it is ready to be eaten.", ex: "The cherries were nice and ripe." },
    { word: "roast", pos: "v.", pron: "[roʊst]", def: "To roast something is to cook it in an oven or over a fire.", ex: "Mom roasted a turkey for the holiday dinner." },
    { word: "routine", pos: "n.", pron: "[ruːˈtiːn]", def: "A routine is a way of doing things that is the same every time.", ex: "My father's daily routine includes shaving right before breakfast." },
    { word: "scheme", pos: "n.", pron: "[skiːm]", def: "A scheme is a plan or design.", ex: "Mickey and Minnie came up with a scheme to solve the problem." },
    { word: "slim", pos: "adj.", pron: "[slɪm]", def: "If something or someone is slim, they are thin.", ex: "Look at my new cell phone. It's very slim." },
    { word: "stove", pos: "n.", pron: "[stoʊv]", def: "A stove is a device used to cook food.", ex: "Our new stove helps us to cook food much faster than before." },
    { word: "theft", pos: "n.", pron: "[θeft]", def: "A theft is a criminal act that involves someone stealing something.", ex: "The theft of his TV took place when he was at work." }
  ],
  story: {
    title: "Why Monkey Has No Home",
    paragraphs: [
      "For five years, there was a famine. The farmers asked people to bless them and finally, they had a good harvest. Since there was now plenty of food, the pharaoh decided to have a party. The party was a happy affair. For five days they had a huge feast.",
      "Monkey was very happy. Because of the famine, he was very slim. He wanted to eat a lot of food.",
      "When he arrived at the feast, hundreds of long tables were filled with food. There were nuts, bowls of cereal, and ripe fruit. He could also smell hot roasted meat cooking on the stove.",
      "The assembly of animals was merry. However, during the feast, Monkey thought of a scheme to exploit the pharaoh's kindness. He decided to steal some of the food and then eat it at home.",
      "All the animals were cheerful. They didn't notice that monkey was hiding food. After the feast, Monkey took the food to his house and ate it. He repeated this routine every day for four days.",
      "But on the fifth day, the pharaoh had a surprise. He was going to give all the animals a home. Monkey was very excited. But when he arrived at the pharaoh's home, he could not get through the door. The diameter of his waist was wider than the doorway. He was too fat!",
      "Monkey asked the pharaoh to forgive him for his theft. But the pharaoh said no.",
      "\"Pardon?\" asked the monkey. He didn't understand why the pharaoh was being unkind.",
      "\"Everybody else will have a home now, but not you. Now you know that greed gets you nothing,\" explained the pharaoh."
    ]
  },
  word_list_exercises: [
    {
      title: "Part A: Circle two words that are related in each group.",
      questions: [
        {
          content: "1. a. theft b. nut c. cereal d. routine",
          options: ["theft, nut", "nut, cereal", "cereal, routine", "theft, routine"],
          correctAnswer: "nut, cereal",
          explanation: "nut (hạt) và cereal (ngũ cốc) đều là các loại thức ăn."
        },
        {
          content: "2. a. roast b. pharaoh c. stove d. pardon",
          options: ["roast, stove", "pharaoh, pardon", "roast, pharaoh", "stove, pardon"],
          correctAnswer: "roast, stove",
          explanation: "roast (nướng) và stove (bếp) đều liên quan đến nấu ăn."
        },
        {
          content: "3. a. assembly b. affair c. bless d. exploit",
          options: ["assembly, bless", "affair, exploit", "assembly, affair", "bless, exploit"],
          correctAnswer: "assembly, affair",
          explanation: "assembly (cuộc họp) và affair (sự kiện) đều chỉ các sự kiện tập trung đông người."
        },
        {
          content: "4. a. exploit b. famine c. merry d. cheerful",
          options: ["exploit, famine", "merry, cheerful", "famine, merry", "exploit, cheerful"],
          correctAnswer: "merry, cheerful",
          explanation: "merry và cheerful đều có nghĩa là vui vẻ."
        },
        {
          content: "5. a. scheme b. slim c. ripe d. harvest",
          options: ["scheme, slim", "ripe, harvest", "slim, ripe", "scheme, harvest"],
          correctAnswer: "ripe, harvest",
          explanation: "ripe (chín) và harvest (thu hoạch) đều liên quan đến mùa màng, nông nghiệp."
        }
      ]
    },
    {
      title: "Part B: Write a word that is similar in meaning to the underlined part.",
      questions: [
        {
          content: "1. The sun has a larger length across its center than the Earth.",
          options: ["diameter", "routine", "theft", "scheme"],
          correctAnswer: "diameter",
          explanation: "length across its center nghĩa là đường kính (diameter)."
        },
        {
          content: "2. The criminal act of taking something stunned the classroom of friends.",
          options: ["bless", "famine", "theft", "assembly"],
          correctAnswer: "theft",
          explanation: "criminal act of taking something nghĩa là hành vi trộm cắp (theft)."
        },
        {
          content: "3. Her new plan may just solve our year-long problem.",
          options: ["affair", "scheme", "routine", "nut"],
          correctAnswer: "scheme",
          explanation: "plan nghĩa là kế hoạch (scheme)."
        },
        {
          content: "4. The woman wanted the religious man to ask God for help for her.",
          options: ["bless", "pardon", "exploit", "roast"],
          correctAnswer: "bless",
          explanation: "ask God for help nghĩa là cầu nguyện, ban phước (bless)."
        },
        {
          content: "5. During the long time with no food, her family had to move to the city.",
          options: ["harvest", "cereal", "famine", "assembly"],
          correctAnswer: "famine",
          explanation: "long time with no food nghĩa là nạn đói (famine)."
        },
        {
          content: "6. The oil company used for greedy reasons the resources of the poor country.",
          options: ["exploited", "blessed", "roasted", "pardoned"],
          correctAnswer: "exploited",
          explanation: "used for greedy reasons nghĩa là bóc lột, lợi dụng (exploited)."
        },
        {
          content: "7. Since he is very skinny, most of his clothes don't fit him too well.",
          options: ["cheerful", "slim", "ripe", "merry"],
          correctAnswer: "slim",
          explanation: "skinny nghĩa là mảnh khảnh, gầy (slim)."
        },
        {
          content: "8. My thing that I do everyday consists of going to work, the health club, and finally home.",
          options: ["routine", "affair", "diameter", "scheme"],
          correctAnswer: "routine",
          explanation: "thing that I do everyday nghĩa là thói quen hàng ngày (routine)."
        },
        {
          content: "9. Would you repeat what you just said to me? I didn't quite understand.",
          options: ["pardon", "bless", "exploit", "roast"],
          correctAnswer: "pardon",
          explanation: "repeat what you just said nghĩa là yêu cầu nhắc lại, xin lỗi vì không nghe rõ (pardon)."
        },
        {
          content: "10. In history class, the students learned about the kings of ancient Egypt.",
          options: ["pharaohs", "thefts", "assemblies", "famines"],
          correctAnswer: "pharaohs",
          explanation: "kings of ancient Egypt nghĩa là các pharaoh (pharaohs)."
        }
      ]
    },
    {
      title: "Part C: Choose the word that is a better fit for each blank.",
      questions: [
        {
          content: "1. After picking the ________ fruit, the cook ________ it in the oven.",
          options: ["ripe, roasted", "roasted, ripe", "ripe, ripe", "roasted, roasted"],
          correctAnswer: "ripe, roasted",
          explanation: "Trái cây chín (ripe) được hái, sau đó được nướng (roasted) trong lò."
        },
        {
          content: "2. The boy didn't hear what the police said, so he asked, \"________ me. Did they say that there had been a ________ in his home?\"",
          options: ["theft, pardon", "pardon, theft", "pardon, pardon", "theft, theft"],
          correctAnswer: "pardon, theft",
          explanation: "Pardon me dùng để xin lỗi và yêu cầu nhắc lại. Theft là vụ trộm."
        },
        {
          content: "3. During the ________, only the ________ had enough food to eat.",
          options: ["famine, pharaoh", "pharaoh, famine", "famine, famine", "pharaoh, pharaoh"],
          correctAnswer: "famine, pharaoh",
          explanation: "Trong nạn đói (famine), chỉ có nhà vua (pharaoh) mới có đủ thức ăn."
        },
        {
          content: "4. He wasn't allowed to use the ________, so he made himself a bowl of ________ instead.",
          options: ["cereal, stove", "stove, cereal", "cereal, cereal", "stove, stove"],
          correctAnswer: "stove, cereal",
          explanation: "Không được dùng bếp (stove) nên cậu ấy làm một bát ngũ cốc (cereal)."
        },
        {
          content: "5. After eating much of the food from the ________, she was no longer very ________.",
          options: ["slim, harvest", "harvest, slim", "harvest, harvest", "slim, slim"],
          correctAnswer: "harvest, slim",
          explanation: "Sau khi ăn nhiều thức ăn từ vụ thu hoạch (harvest), cô ấy không còn gầy (slim) nữa."
        },
        {
          content: "6. You can tell the size of the food inside a ________ if you measure the ________ of its shell.",
          options: ["nut, diameter", "diameter, nut", "nut, nut", "diameter, diameter"],
          correctAnswer: "nut, diameter",
          explanation: "Đo đường kính (diameter) của vỏ hạt (nut) để biết kích thước phần nhân bên trong."
        },
        {
          content: "7. The party was such a happy ________; everyone seemed so ________.",
          options: ["affair, merry", "merry, affair", "affair, affair", "merry, merry"],
          correctAnswer: "affair, merry",
          explanation: "Bữa tiệc là một sự kiện (affair) vui vẻ, mọi người đều rất vui (merry)."
        },
        {
          content: "8. Her daily ________ included visiting her grandmother and asking God to ________ her so she would stay healthy.",
          options: ["routine, bless", "bless, routine", "routine, routine", "bless, bless"],
          correctAnswer: "routine, bless",
          explanation: "Thói quen hàng ngày (routine) của cô ấy là đến thăm bà và xin Chúa ban phước (bless)."
        },
        {
          content: "9. The king had a plan to ________ the people, but the people had an ________ to stop him.",
          options: ["exploit, assembly", "assembly, exploit", "exploit, exploit", "assembly, assembly"],
          correctAnswer: "exploit, assembly",
          explanation: "Nhà vua muốn bóc lột (exploit) người dân, nhưng họ đã tổ chức một cuộc họp (assembly) để ngăn lại."
        },
        {
          content: "10. She was ________ because everything about her ________ had worked.",
          options: ["cheerful, scheme", "scheme, cheerful", "cheerful, cheerful", "scheme, scheme"],
          correctAnswer: "cheerful, scheme",
          explanation: "Cô ấy vui vẻ (cheerful) vì kế hoạch (scheme) của cô ấy đã thành công."
        }
      ]
    }
  ],
  story_exercise: {
    title: "Reading Comprehension",
    questions: [
      {
        content: "1. The pharaoh's party was a sad affair.",
        options: ["True", "False", "Not Given", "None of the above"],
        correctAnswer: "False",
        explanation: "Bữa tiệc của pharaoh là một sự kiện vui vẻ (happy affair), không phải buồn tẻ (sad)."
      },
      {
        content: "2. There was plenty of ripe fruit at the party from the harvest.",
        options: ["True", "False", "Not Given", "None of the above"],
        correctAnswer: "True",
        explanation: "Có rất nhiều trái cây chín (ripe fruit) tại bữa tiệc từ vụ thu hoạch."
      },
      {
        content: "3. The assembly of animals was merry.",
        options: ["True", "False", "Not Given", "None of the above"],
        correctAnswer: "True",
        explanation: "Cuộc tụ tập của các loài động vật rất vui vẻ (merry)."
      },
      {
        content: "4. Monkey repeated his routine for five days.",
        options: ["True", "False", "Not Given", "None of the above"],
        correctAnswer: "False",
        explanation: "Khỉ chỉ lặp lại thói quen đó trong bốn ngày (four days), không phải năm ngày."
      },
      {
        content: "5. The diameter of Monkey's waist was wider than the doorway.",
        options: ["True", "False", "Not Given", "None of the above"],
        correctAnswer: "True",
        explanation: "Đường kính eo của khỉ thực sự rộng hơn cả khung cửa."
      },
      {
        content: "6. The pharaoh asked Monkey, \"Pardon?\"",
        options: ["True", "False", "Not Given", "None of the above"],
        correctAnswer: "False",
        explanation: "Khỉ là người đã hỏi 'Pardon?' chứ không phải pharaoh."
      },
      {
        content: "7. The pharaoh gave a party for all the animals because _____.",
        options: [
          "a. they blessed the farmers",
          "b. the famine ended",
          "c. he wanted to exploit the animals",
          "d. they were too slim"
        ],
        correctAnswer: "b. the famine ended",
        explanation: "Pharaoh tổ chức bữa tiệc vì nạn đói đã kết thúc (the famine ended)."
      },
      {
        content: "8. What did Monkey do with the food?",
        options: [
          "a. He hid it under the table.",
          "b. He took it to his house.",
          "c. He gave it to the pharaoh.",
          "d. He cooked it in the stove."
        ],
        correctAnswer: "b. He took it to his house.",
        explanation: "Khỉ đã mang thức ăn về nhà của mình (took it to his house)."
      },
      {
        content: "9. The tables were full of all of the following EXCEPT _____.",
        options: [
          "a. vegetables",
          "b. ripe fruit",
          "c. cereal",
          "d. roasted meat"
        ],
        correctAnswer: "a. vegetables",
        explanation: "Trên bàn có trái cây chín, ngũ cốc và thịt nướng, không có rau (vegetables)."
      },
      {
        content: "10. What stopped Monkey from entering the party on the fifth day?",
        options: [
          "a. A locked door",
          "b. The pharaoh",
          "c. His fat waist",
          "d. The other animals"
        ],
        correctAnswer: "c. His fat waist",
        explanation: "Eo quá béo (fat waist) khiến khỉ không thể lọt qua cửa."
      }
    ]
  }
};

fs.writeFileSync('c:\\Users\\Tony\\.gemini\\antigravity\\scratch\\tonyenglish-app\\unit15_raw.json', JSON.stringify(unitData, null, 2));
console.log('Done writing JSON');
