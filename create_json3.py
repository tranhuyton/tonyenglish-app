import json

data = {
  "unit": 3,
  "words": [
    { "word": "bloom", "pos": "v.", "pron": "[blu:m]", "def": "When a plant blooms, it makes flowers.", "ex": "Roses look so pretty when they bloom." },
    { "word": "compact", "pos": "adj.", "pron": "[kampaekt]", "def": "If something is compact, it is smaller than normal.", "ex": "A laptop computer is much more compact than a desktop model." },
    { "word": "decay", "pos": "v.", "pron": "[dikei]", "def": "To decay is to be destroyed naturally.", "ex": "The old wooden house was slowly decaying." },
    { "word": "dessert", "pos": "n.", "pron": "[dize:rt]", "def": "Dessert is a sweet food that you eat after a meal.", "ex": "Kayla wants ice cream for dessert." },
    { "word": "dip", "pos": "v.", "pron": "[dip]", "def": "To dip something is to put part of it into a liquid for a short time.", "ex": "Laurel dipped her strawberry into the chocolate." },
    { "word": "distant", "pos": "adj.", "pron": "[distent]", "def": "If something is distant, it is far away.", "ex": "Michael could barely see the distant island." },
    { "word": "eclipse", "pos": "n.", "pron": "[iklips]", "def": "An eclipse is an occasion when the moon moves in front of the sun.", "ex": "A complete eclipse of the sun is a very rare occurrence." },
    { "word": "fairy", "pos": "n.", "pron": "[feari]", "def": "A fairy is a small, magic creature with wings.", "ex": "There are usually fairies in fantasy stories." },
    { "word": "curl", "pos": "n.", "pron": "[kerl]", "def": "A curl is a small piece of something with a round shape.", "ex": "The colorful ribbons were bent into curls." },
    { "word": "grace", "pos": "n.", "pron": "[greis]", "def": "Grace is a quality of moving in a smooth, relaxed and attractive way.", "ex": "The ballerina danced with grace." },
    { "word": "leisure", "pos": "n.", "pron": "[li:39:r]", "def": "Leisure is time when you do not have to do work.", "ex": "Eve likes to listen to music in her leisure time." },
    { "word": "mankind", "pos": "n.", "pron": "[maenkaind]", "def": "Mankind is all of the world’s people.", "ex": "All of mankind has to work to make this a better world." },
    { "word": "passion", "pos": "n.", "pron": "[paejan]", "def": "Passion is a very strong feeling of wanting to do something.", "ex": "She had a passion for dancing." },
    { "word": "pillow", "pos": "n.", "pron": "[pilou]", "def": "A pillow is something that you put your head on when you sleep.", "ex": "When I travel, I usually take along my favorite pillow." },
    { "word": "pulse", "pos": "n.", "pron": "[pAls]", "def": "A pulse is the beat of the heart.", "ex": "The doctor checked the patient’s pulse by feeling his wrist." },
    { "word": "refresh", "pos": "v.", "pron": "[rifrej]", "def": "To refresh someone is to make them feel less hot or tired.", "ex": "The baby was refreshed after taking a cool bath." },
    { "word": "sneeze", "pos": "v.", "pron": "[sni:z]", "def": "To sneeze is to suddenly blow air out of your nose and mouth.", "ex": "He sneezed after smelling the flower." },
    { "word": "spice", "pos": "n.", "pron": "[spais]", "def": "A spice is a flavor for food and drinks.", "ex": "Two common spices found in many homes are salt and pepper." },
    { "word": "whistle", "pos": "v.", "pron": "[hwisl]", "def": "To whistle is to make a sound by putting your lips together and blowing.", "ex": "As he was listening to music, Daryl whistled." },
    { "word": "wool", "pos": "n.", "pron": "[wul]", "def": "Wool is the hair that a sheep has.", "ex": "Grandma wants to use the blue wool to knit me a sweater." }
  ],
  "story": {
    "title": "Tiny Tina",
    "paragraphs": [
      "In a distant land, there was a kingdom where fairies lived. Tina was a fairy. She had yellow curls and wore a dress made of wool. She always moved with grace. However, because of her compact size, she was scared of mankind.",
      "One day, there was an eclipse of the sun. The fairies didn’t know what was happening. They were scared, so they ran away.",
      "Tina looked for a place to hide. She found a garden with flowers blooming. Tina had a passion for flowers. She decided to hide there. She became sleepy and made a pillow with some leaves. She whistled happily as she worked, and she fell asleep.",
      "Suddenly, somebody sneezed. The sound woke Tina up. She saw a very big face looking at her! Tina was so scared that she couldn’t move. She could feel her pulse going very fast.",
      "The big woman went into her house. When she came back, she gave Tina a cup.",
      "The woman sat on the ground among some decaying leaves. Tina dipped a finger in the cup and tasted it. It was tea with all kinds of delicious spices in it. Tina felt refreshed after drinking the tea.",
      "“I’m Wilma,” the lady said. “I spend all my leisure time in my garden cutting flowers. Would you like some dessert?”",
      "Tina said yes. She was hungry, and she wasn’t frightened anymore. She took a bite of cake and relaxed. “How did you get to my garden?”",
      "Tina told Wilma how she got lost.",
      "“That’s terrible! Let us take you home.”",
      "“Actually, I think that I want to stay with you,” Tina said. She wasn’t scared of big people anymore. Wilma and Tina lived happily ever after."
    ]
  },
  "word_list_exercises": [
    {
      "title": "Part A: Choose the right word for the given definition.",
      "questions": [
        {
          "content": "1. far away",
          "options": ["compact", "leisure", "distant", "passion"],
          "correctAnswer": "distant",
          "explanation": "“far away” có nghĩa là xa xôi, xa cách. Từ đồng nghĩa là “distant”."
        },
        {
          "content": "2. a sweet thing to eat",
          "options": ["dessert", "wool", "mankind", "bloom"],
          "correctAnswer": "dessert",
          "explanation": "“a sweet thing to eat” là đồ ngọt để ăn. Đáp án là “dessert” (món tráng miệng)."
        },
        {
          "content": "3. a small magical creature",
          "options": ["pulse", "pillow", "grace", "fairy"],
          "correctAnswer": "fairy",
          "explanation": "“a small magical creature” là sinh vật ma thuật nhỏ bé. Đáp án là “fairy” (tiên nữ)."
        },
        {
          "content": "4. an event that covers the sun",
          "options": ["whistle", "decay", "eclipse", "curl"],
          "correctAnswer": "eclipse",
          "explanation": "“an event that covers the sun” là sự kiện che khuất mặt trời. Đáp án là “eclipse” (nhật thực)."
        },
        {
          "content": "5. to make someone feel less tired",
          "options": ["spice", "refresh", "dip", "sneeze"],
          "correctAnswer": "refresh",
          "explanation": "“to make someone feel less tired” là làm cho ai đó bớt mệt mỏi. Đáp án là “refresh” (làm sảng khoái)."
        }
      ]
    },
    {
      "title": "Part B: Choose the right definition for the given word.",
      "questions": [
        {
          "content": "1. whistle",
          "options": ["a flavor", "to make noise with one’s lips", "people", "a flower"],
          "correctAnswer": "to make noise with one’s lips",
          "explanation": "“whistle” là huýt sáo, tức là tạo ra âm thanh bằng môi."
        },
        {
          "content": "2. compact",
          "options": ["far", "not at work", "small", "to help tired people"],
          "correctAnswer": "small",
          "explanation": "“compact” có nghĩa là nhỏ gọn (small)."
        },
        {
          "content": "3. wool",
          "options": ["sheep’s hair", "magic creature", "something to eat", "strong feeling"],
          "correctAnswer": "sheep’s hair",
          "explanation": "“wool” là len, lông cừu."
        },
        {
          "content": "4. grace",
          "options": ["to chase after", "to get old and rot", "a nice way to move", "in the shape of a circle"],
          "correctAnswer": "a nice way to move",
          "explanation": "“grace” là vẻ duyên dáng, di chuyển uyển chuyển (a nice way to move)."
        },
        {
          "content": "5. dip",
          "options": ["to blow out air", "something soft for your head", "to put in and out", "one of the things on your feet"],
          "correctAnswer": "to put in and out",
          "explanation": "“dip” là nhúng vào rồi rút ra."
        },
        {
          "content": "6. spice",
          "options": ["a flavor added to food or drink", "something with a round shape", "to make one feel less tired", "a sweet thing to eat"],
          "correctAnswer": "a flavor added to food or drink",
          "explanation": "“spice” là gia vị, hương vị thêm vào thức ăn."
        },
        {
          "content": "7. leisure",
          "options": ["time when you do not have to work", "to become naturally destroyed", "the hair of sheep", "a feeling of wanting"],
          "correctAnswer": "time when you do not have to work",
          "explanation": "“leisure” là thời gian rảnh rỗi, không phải làm việc."
        },
        {
          "content": "8. curl",
          "options": ["to get old and fall apart", "something with a curve", "something small", "to go after"],
          "correctAnswer": "something with a curve",
          "explanation": "“curl” là lọn tóc xoăn hoặc vật có hình uốn cong."
        },
        {
          "content": "9. pillow",
          "options": ["something you sleep on", "the quality of moving well", "an event that covers the sun", "far away"],
          "correctAnswer": "something you sleep on",
          "explanation": "“pillow” là cái gối để ngủ."
        },
        {
          "content": "10. pulse",
          "options": ["not at work", "a magic creature", "the beat of one’s heart", "to go away"],
          "correctAnswer": "the beat of one’s heart",
          "explanation": "“pulse” là nhịp tim."
        }
      ]
    }
  ],
  "story_exercise": {
    "title": "Answer the questions based on the story.",
    "questions": [
      {
        "content": "1. Why did Tina suddenly wake up?",
        "options": ["She felt refreshed", "She heard someone sneeze", "The leaves were decayed", "She had a fast pulse"],
        "correctAnswer": "She had a fast pulse",
        "explanation": "Đáp án D theo sách, mặc dù cốt truyện nói Tina thức dậy do tiếng hắt hơi (B)."
      },
      {
        "content": "2. All of the following describe Tina EXCEPT ___.",
        "options": ["she had curls in her hair", "she moved with grace", "she did not like tea with spice", "she was compact"],
        "correctAnswer": "she did not like tea with spice",
        "explanation": "Cô ấy thích trà có gia vị, do đó đáp án C là ngoại lệ."
      },
      {
        "content": "3. What does Wilma do with the flowers?",
        "options": ["She makes dessert with them", "She cuts them", "She dips them in gold", "She lets them decay"],
        "correctAnswer": "She makes dessert with them",
        "explanation": "Đáp án A theo sách, dù trong truyện Wilma nói bà ấy cắt hoa (B)."
      },
      {
        "content": "4. Where did Tina live before she met Wilma?",
        "options": ["In Wilma’s garden", "In a tiny house", "On a street with big cars", "In a distant country"],
        "correctAnswer": "In a distant country",
        "explanation": "Tina từng sống ở một vùng đất xa xôi (distant land)."
      }
    ]
  }
}

with open('unit3_raw.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
