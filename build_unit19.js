const fs = require('fs');

const data = {
  "unit": 19,
  "words": [
    {
      "word": "bench",
      "pos": "n.",
      "pron": "[bentʃ]",
      "def": "A bench is a long seat for two or more people.",
      "ex": "Most parks have benches for citizens to relax upon."
    },
    {
      "word": "confront",
      "pos": "v.",
      "pron": "[kənfrʌnt]",
      "def": "To confront a hard situation or person is to deal with it.",
      "ex": "The couple has to confront each other about their problems."
    },
    {
      "word": "daisy",
      "pos": "n.",
      "pron": "[deizi]",
      "def": "A daisy is a small flower with white petals and a yellow center.",
      "ex": "There were a few daisies growing in the field."
    },
    {
      "word": "dispute",
      "pos": "n.",
      "pron": "[dispju:t]",
      "def": "A dispute is an argument or disagreement that people have.",
      "ex": "Karen and Brian often have disputes about silly things."
    },
    {
      "word": "horror",
      "pos": "n.",
      "pron": "[hɔ:rər]",
      "def": "Horror is a feeling of being very afraid or shocked.",
      "ex": "The audience screamed in horror when the ghost appeared in the movie."
    },
    {
      "word": "incident",
      "pos": "n.",
      "pron": "[insədənt]",
      "def": "An incident is an event that is usually not pleasant.",
      "ex": "Mr. Wilson had an incident where he became sick and had to leave."
    },
    {
      "word": "mist",
      "pos": "n.",
      "pron": "[mist]",
      "def": "Mist is water that you can see in the air or on a surface.",
      "ex": "The forest was covered with mist."
    },
    {
      "word": "object",
      "pos": "n.",
      "pron": "[abudʒikt]",
      "def": "An object is an inanimate thing that you can see or touch.",
      "ex": "The shopping cart was filled with objects."
    },
    {
      "word": "orphan",
      "pos": "n.",
      "pron": "[ɔ:rfən]",
      "def": "An orphan is a child who does not have parents.",
      "ex": "The orphan frequently cried during the night."
    },
    {
      "word": "plot",
      "pos": "v.",
      "pron": "[plat]",
      "def": "To plot is to make a secret plan to do something that is wrong or mean.",
      "ex": "The group was plotting to ruin the company's financial reports."
    },
    {
      "word": "pregnant",
      "pos": "adj.",
      "pron": "[pregnənt]",
      "def": "When a female is pregnant, she is going to have a baby.",
      "ex": "The pregnant woman was shopping for baby clothes."
    },
    {
      "word": "rage",
      "pos": "n.",
      "pron": "[reidʒ]",
      "def": "Rage is a very angry feeling.",
      "ex": "The chef was filled with rage when his helpers ruined the meal."
    },
    {
      "word": "revenge",
      "pos": "n.",
      "pron": "[rivendʒ]",
      "def": "Revenge is what you do to hurt or punish someone who hurts you.",
      "ex": "He broke his sister's doll as revenge after she lost his favorite book."
    },
    {
      "word": "shame",
      "pos": "n.",
      "pron": "[ʃeim]",
      "def": "Shame is a bad feeling about things you have done wrong.",
      "ex": "The boy felt shame about misplacing his clothes."
    },
    {
      "word": "sigh",
      "pos": "v.",
      "pron": "[sai]",
      "def": "To sigh is to breathe out loudly and show that you are tired or sad.",
      "ex": "Molly sighed when she looked at all the information she had to research."
    },
    {
      "word": "sneak",
      "pos": "v.",
      "pron": "[sni:k]",
      "def": "To sneak is to move quietly so that no one hears or sees you.",
      "ex": "The thief snuck out of the house without anyone noticing him."
    },
    {
      "word": "spare",
      "pos": "v.",
      "pron": "[speər]",
      "def": "To spare something is to give it because you have more than you need.",
      "ex": "I wanted to help him but I couldn't spare a tire."
    },
    {
      "word": "stem",
      "pos": "n.",
      "pron": "[stem]",
      "def": "The stem of a plant is the stick that grows leaves or flowers.",
      "ex": "The rose had a long thin stem."
    },
    {
      "word": "supper",
      "pos": "n.",
      "pron": "[sʌpər]",
      "def": "Supper is a meal that is eaten in the evening.",
      "ex": "We usually have supper around 6 o'clock at my house."
    },
    {
      "word": "tender",
      "pos": "adj.",
      "pron": "[tendər]",
      "def": "When something is tender, it is soft and easy to chew.",
      "ex": "The meat was so tender they didn't need knives to cut it with."
    }
  ],
  "story": {
    "title": "The Magic Pear Tree",
    "paragraphs": [
      "It was a cool morning, and the grass was covered in mist. The market was full of people. A mean farmer named Jack yelled, \"Pears for sale!\" He sat on a bench, plotting how he could trick people. Then an orphan came to his cart.",
      "\"Can you spare a pear?\" she asked.",
      "Jack felt rage. He replied, \"You don't have any money!\"",
      "\"Please, I haven't had supper in days.\"",
      "\"No!\" shouted the farmer.",
      "The orphan sighed. However, a pregnant lady heard the dispute and confronted Jack. \"Just give her a pear,\" she said. Jack had no shame and said no.",
      "Finally, a man bought a pear for the girl.",
      "The girl quickly ate it, but she saved the seed. She wanted to get revenge.",
      "She told Jack, \"I know a way to get hundreds of pears in one day. I'll show you how.\"",
      "He watched the girl dig a hole. She dropped the seed into the ground. Then she spread the dirt over it.",
      "\"Watch closely,\" she said. \"In a few minutes, a stem will grow. It'll turn into a tree that's full of pears!\"",
      "Jack stared at the dirt, but nothing happened. The only objects there were a few daisies. He looked for the girl, but she had snuck away.",
      "Then he looked at his cart in horror. It was empty!",
      "He suddenly realized that the orphan had tricked him.",
      "While Jack was waiting for the tree to grow, the people had taken the pears from his cart. They all laughed while they were eating the tender fruit. The farmer felt ashamed. The incident taught him to be kinder."
    ]
  },
  "word_list_exercises": [
    {
      "title": "Exercise 1: Part A",
      "questions": [
        {
          "content": "1. to deal with a difficult situation",
          "options": ["revenge", "confront", "supper", "object"],
          "correctAnswer": "confront",
          "explanation": "confront có nghĩa là đối mặt, giải quyết một tình huống khó khăn."
        },
        {
          "content": "2. a part of a flower",
          "options": ["horror", "mist", "bench", "stem"],
          "correctAnswer": "stem",
          "explanation": "stem là thân, cuống hoa, một phần của bông hoa."
        },
        {
          "content": "3. soft and easy to chew",
          "options": ["tender", "retreat", "steep", "summit"],
          "correctAnswer": "tender",
          "explanation": "tender có nghĩa là mềm và dễ nhai."
        },
        {
          "content": "4. feeling of being afraid",
          "options": ["incident", "pregnant", "horror", "spare"],
          "correctAnswer": "horror",
          "explanation": "horror là cảm giác sợ hãi."
        },
        {
          "content": "5. to breathe air",
          "options": ["sigh", "daisy", "shame", "orphan"],
          "correctAnswer": "sigh",
          "explanation": "sigh là thở dài."
        }
      ]
    },
    {
      "title": "Exercise 1: Part B",
      "questions": [
        {
          "content": "1. bench",
          "options": ["quiet", "a seat", "no parents", "meal"],
          "correctAnswer": "a seat",
          "explanation": "bench là một cái ghế dài (a seat)."
        },
        {
          "content": "2. plot",
          "options": ["to plan", "a flower", "to get even", "soft"],
          "correctAnswer": "to plan",
          "explanation": "plot là lên kế hoạch (thường là kế hoạch bí mật)."
        },
        {
          "content": "3. supper",
          "options": ["a hard situation", "breathe", "meal", "flower part"],
          "correctAnswer": "meal",
          "explanation": "supper là bữa ăn tối (meal)."
        },
        {
          "content": "4. dispute",
          "options": ["an argument", "a shock", "flat rock", "a baby"],
          "correctAnswer": "an argument",
          "explanation": "dispute là một cuộc tranh cãi (an argument)."
        },
        {
          "content": "5. incident",
          "options": ["water", "to feel bad", "extra", "a bad event"],
          "correctAnswer": "a bad event",
          "explanation": "incident là một sự việc (thường là sự việc không hay, a bad event)."
        }
      ]
    },
    {
      "title": "Exercise 2: Choose the answer that best fits the question.",
      "questions": [
        {
          "content": "1. If a child loses their parents, what do they become?",
          "options": ["A daisy", "An orphan", "A spare", "An object"],
          "correctAnswer": "An orphan",
          "explanation": "Một đứa trẻ mất cha mẹ thì trở thành trẻ mồ côi (an orphan)."
        },
        {
          "content": "2. What would you call someone who can spare time to help you?",
          "options": ["greedy", "mean", "kind", "arrogant"],
          "correctAnswer": "kind",
          "explanation": "Người có thể dành thời gian giúp bạn là người tốt bụng (kind)."
        },
        {
          "content": "3. What is something that would fill you with shame?",
          "options": ["Buying new shoes", "Stealing from your grandparents", "Eating cake", "Buying some books"],
          "correctAnswer": "Stealing from your grandparents",
          "explanation": "Việc ăn trộm của ông bà sẽ khiến bạn cảm thấy xấu hổ (shame)."
        },
        {
          "content": "4. What would put a person in a rage?",
          "options": ["Getting a new job", "A bright sunny day", "Meeting friends", "Someone stealing their car"],
          "correctAnswer": "Someone stealing their car",
          "explanation": "Việc ai đó ăn trộm xe của họ sẽ khiến họ nổi cơn thịnh nộ (rage)."
        },
        {
          "content": "5. If you sneak, what are you doing?",
          "options": ["Loudly talking", "Trying not to be seen", "Trying not to be heard", "Happily singing"],
          "correctAnswer": "Trying not to be seen",
          "explanation": "Sneak có nghĩa là lẻn đi, cố gắng không để ai nhìn thấy."
        }
      ]
    },
    {
      "title": "Exercise 3: Choose the word that is the better fit for each blank.",
      "questions": [
        {
          "content": "1. She went to the lawn and cut a ____________ from the garden. It smelled good and was covered in ___________ . (mist / daisy)",
          "options": ["daisy / mist", "mist / daisy"],
          "correctAnswer": "daisy / mist",
          "explanation": "Cắt một bông hoa cúc (daisy), và bông hoa được bao phủ bởi sương mù (mist)."
        },
        {
          "content": "2. The employees had a long ____________ with the owner over their low pay. Eventually, one worker ____________ the owner and was finally able to solve the problem. (dispute / confronted)",
          "options": ["dispute / confronted", "confronted / dispute"],
          "correctAnswer": "dispute / confronted",
          "explanation": "Cuộc tranh cãi (dispute) và đối mặt (confronted)."
        },
        {
          "content": "3. She looked across the schoolyard, hoping to find an empty ____________ where she could rest. Since they were all full, she ____________ and sat on the ground instead. (bench / sighed)",
          "options": ["bench / sighed", "sighed / bench"],
          "correctAnswer": "bench / sighed",
          "explanation": "Tìm một chiếc ghế đá (bench) trống, nhưng vì chúng đã đầy, cô ấy thở dài (sighed)."
        },
        {
          "content": "4. The ___________ of the car accident made him too scared to drive. It wasn't until three years after the ___________ that he got into a car again. (incident / horror)",
          "options": ["horror / incident", "incident / horror"],
          "correctAnswer": "horror / incident",
          "explanation": "Sự sợ hãi (horror) về vụ tai nạn (incident)."
        },
        {
          "content": "5. The ___________ woman couldn't go to work anymore, so she had a lot of time to ___________ with her hobbies. (pregnant / spare)",
          "options": ["pregnant / spare", "spare / pregnant"],
          "correctAnswer": "pregnant / spare",
          "explanation": "Người phụ nữ mang thai (pregnant) có nhiều thời gian rảnh rỗi (spare)."
        },
        {
          "content": "6. He wasn't usually a person who tried to get ___________ . However, when he learned that his classmates had ___________ against him, he changed his position. (revenge / plotted)",
          "options": ["revenge / plotted", "plotted / revenge"],
          "correctAnswer": "revenge / plotted",
          "explanation": "Trả thù (revenge) và âm mưu (plotted)."
        },
        {
          "content": "7. A dog got into the garden and ate all the flowers, leaving behind only the ___________ . When the owner found out, he felt ___________ . (stems / rage)",
          "options": ["stems / rage", "rage / stems"],
          "correctAnswer": "stems / rage",
          "explanation": "Để lại những cái cuống hoa (stems) và cảm thấy tức giận (rage)."
        },
        {
          "content": "8. Mr. Holloway cooked hamburgers and vegetables for ____________ yesterday. Everything was cooked very well. The meat was juicy and the vegetables were ____________ . (tender / supper)",
          "options": ["supper / tender", "tender / supper"],
          "correctAnswer": "supper / tender",
          "explanation": "Nấu cho bữa tối (supper) và rau củ mềm (tender)."
        },
        {
          "content": "9. The ___________ didn't have anybody to take care of him. He often had to ___________ into empty houses during the winter just to keep warm. (sneak / orphan)",
          "options": ["orphan / sneak", "sneak / orphan"],
          "correctAnswer": "orphan / sneak",
          "explanation": "Đứa trẻ mồ côi (orphan) phải lẻn (sneak) vào nhà trống."
        },
        {
          "content": "10. A thief had taken several ____________ from the museum. After a few days, however, he felt a sense of ____________ and returned everything. (shame / objects)",
          "options": ["objects / shame", "shame / objects"],
          "correctAnswer": "objects / shame",
          "explanation": "Lấy một vài đồ vật (objects) và cảm thấy xấu hổ (shame)."
        }
      ]
    }
  ],
  "story_exercise": {
    "title": "Part B: Answer the questions.",
    "questions": [
      {
        "content": "1. What object did the girl keep after she ate the pear?",
        "options": ["The seed", "The stem", "A daisy", "The cart"],
        "correctAnswer": "The seed",
        "explanation": "Cô gái đã giữ lại hạt giống (The seed) sau khi ăn lê."
      },
      {
        "content": "2. What was the dispute between the orphan and the farmer about?",
        "options": ["The girl wanted a spare pear.", "The farmer felt rage about the girl.", "The girl sat on his bench.", "The farmer's pears were too expensive."],
        "correctAnswer": "The girl wanted a spare pear.",
        "explanation": "Cô bé mồ côi muốn xin một quả lê (The girl wanted a spare pear)."
      },
      {
        "content": "3. What did the girl do immediately after she put the seed in the ground?",
        "options": ["She asked the farmer to watch closely.", "She ate the pear.", "She spread the dirt over it.", "She dug a hole."],
        "correctAnswer": "She spread the dirt over it.",
        "explanation": "Ngay sau khi bỏ hạt xuống đất, cô ấy đã phủ đất lên (She spread the dirt over it)."
      },
      {
        "content": "4. What happened to the farmer's pears at the end of the story?",
        "options": ["They were stolen by the crowd.", "They were all sold.", "They were given away.", "They were taken by the girl."],
        "correctAnswer": "They were stolen by the crowd.",
        "explanation": "Đám đông đã lấy trộm lê của người nông dân trong lúc anh ta đang mải nhìn (They were taken by the crowd)."
      }
    ]
  }
};

fs.writeFileSync('unit19_raw.json', JSON.stringify(data, null, 2));
console.log('Successfully wrote unit19_raw.json');
