import json

data = {
  "unit": 5,
  "words": [
    {"word": "acquaint", "pos": "v.", "pron": "[akweint]", "def": "To acquaint is to get to know something or someone.", "ex": "Nancy acquainted herself with the new computer."},
    {"word": "cemetery", "pos": "n.", "pron": "[semateri]", "def": "A cemetery is where people are buried when they die.", "ex": "Some people are scared of cemeteries."},
    {"word": "curse", "pos": "v.", "pron": "[ka:rs]", "def": "To curse someone or something is to hope that bad things happen to them.", "ex": "The witch cursed the village."},
    {"word": "disguise", "pos": "n.", "pron": "[disgaiz]", "def": "A disguise is something you wear so people cannot tell who you are.", "ex": "Everyone knew that it was Dad in the Santa disguise."},
    {"word": "fancy", "pos": "adj.", "pron": "[faensi]", "def": "If something is fancy, it is nicer than normal.", "ex": "Their table was all set for a fancy dinner."},
    {"word": "flashlight", "pos": "n.", "pron": "[flaeflait]", "def": "A flashlight is a small electric light that you carry in your hand.", "ex": "We took a flashlight when we went camping."},
    {"word": "hood", "pos": "n.", "pron": "[hud]", "def": "A hood is part of a coat that goes over your head.", "ex": "She put on her hood to keep her head warm."},
    {"word": "inhabitant", "pos": "n.", "pron": "[inhaebatant]", "def": "An inhabitant is a person who lives in a certain place.", "ex": "The number of inhabitants in the countryside is increasing."},
    {"word": "nourish", "pos": "v.", "pron": "[na:rif]", "def": "To nourish something is to give it food that it needs to live.", "ex": "A good mother will nourish her baby every day."},
    {"word": "pirate", "pos": "n.", "pron": "[paiarat]", "def": "A pirate is a sailor who steals things from other boats.", "ex": "Pirates are very scary characters."},
    {"word": "publication", "pos": "n.", "pron": "[pAblakeijan]", "def": "A publication is something printed, like a newspaper or book.", "ex": "She's been a subscriber to that publication for over ten years."},
    {"word": "riddle", "pos": "n.", "pron": "[ridl]", "def": "A riddle is a question that is difficult to answer but meant to be funny.", "ex": "I could not answer Wendy's riddle, but it made me laugh."},
    {"word": "rot", "pos": "v.", "pron": "[rot]", "def": "When something rots, it slowly gets softer and is destroyed.", "ex": "The old log began to rot in the forest."},
    {"word": "scare", "pos": "v.", "pron": "[skaear]", "def": "To scare means to cause one to feel frightened.", "ex": "I was scared by the sight of the monster."},
    {"word": "shortly", "pos": "adv.", "pron": "[fo:rtli]", "def": "If something will happen shortly, it will happen very soon.", "ex": "My workday will end shortly."},
    {"word": "skeleton", "pos": "n.", "pron": "[skelatn]", "def": "A skeleton is the bones of a body.", "ex": "There is a skeleton in the science classroom."},
    {"word": "spoil", "pos": "v.", "pron": "[spoil]", "def": "If something spoils, it turns bad or rots.", "ex": "We left the fruit out too long, and it spoiled."},
    {"word": "starve", "pos": "v.", "pron": "[sta:rv]", "def": "If a person starves, they do not get enough to eat and sometimes die.", "ex": "During the war, many people starved."},
    {"word": "thrill", "pos": "n.", "pron": "[eril]", "def": "A thrill is an exciting feeling.", "ex": "The boys enjoy the thrill of surfing a big wave."},
    {"word": "wicked", "pos": "adj.", "pron": "[wikid]", "def": "If something is wicked, it is very bad or evil.", "ex": "My boss is a very wicked man."}
  ],
  "story": {
    "title": "Trick-or-treat!",
    "paragraphs": [
      "Many different cultures have had traditions about the dead. People in places like Ireland, China, Egypt and Mexico believed that souls needed food. They thought the food nourished them on their journey from cemeteries to heaven. People had to put out good things for souls to eat. However, if the food rotted or spoiled, the soul got mad. The wicked soul might curse the family and make them starve during the winter.",
      "In other places, people begged for food on a holiday that remembers the souls of dead saints. People wore disguises with hoods that covered their faces. If they did not get food, they played a trick on the home. For this reason, the activity is known as \"trick-or-treating.\" Shortly after people first began trick-or-treating, parents started sending their children to beg on that day. Housewives gave the children food if they performed a song or a dance. When people moved to America from all over the world, they brought this tradition with them.",
      "Inhabitants of villages started trick-or-treating in the early 1900s. In 1939 a children's publication acquainted the whole country with the tradition. It became very popular.",
      "Today, trick-or-treaters are not begging for food, and they are not scared of souls. They just enjoy the thrill of dressing up like creatures and getting candy. Ghosts and skeletons are favorite costumes. But some children wear fancy disguises, like pirates. They carry flashlights instead of fires. In some places, children still perform songs or riddles to get candy. But most of the time, they just say \"Trick-or-Treat!\""
    ]
  },
  "word_list_exercises": [
    {
      "title": "Exercise 1: Choose the word that is the better fit for each blank.",
      "questions": [
        {
          "content": "1. Mary ____________ the creature that came into her yard and ____________ her dog.",
          "options": ["cursed / scared", "scared / cursed", "curses / scares", "cursing / scary"],
          "correctAnswer": "cursed / scared",
          "explanation": "cursed (nguyền rủa), scared (làm hoảng sợ)."
        },
        {
          "content": "2. I don't like to walk in the ____________. I always think about the ____________ that are under the ground there.",
          "options": ["cemetery / skeletons", "skeletons / cemetery", "cemeteries / skeleton", "skeleton / cemeteries"],
          "correctAnswer": "cemetery / skeletons",
          "explanation": "cemetery (nghĩa trang), skeletons (bộ xương)."
        },
        {
          "content": "3. My mother bought me a ____________ new coat. My favorite part is the warm ____________.",
          "options": ["fancy / hood", "hood / fancy", "fancies / hoods", "hoods / fancies"],
          "correctAnswer": "fancy / hood",
          "explanation": "fancy (lộng lẫy/đẹp đẽ), hood (mũ trùm đầu)."
        },
        {
          "content": "4. When my friend stayed at my house, we sat with a ____________. Instead of sleeping, we sat and told ____________ for an hour!",
          "options": ["flashlight / riddles", "riddles / flashlight", "flashlights / riddle", "riddle / flashlights"],
          "correctAnswer": "flashlight / riddles",
          "explanation": "flashlight (đèn pin), riddles (câu đố)."
        },
        {
          "content": "5. Judy wanted to find a ____________ that was scary. Finally, she decided to dress like a ____________ witch.",
          "options": ["disguise / wicked", "wicked / disguise", "disguises / wickedness", "wickedness / disguises"],
          "correctAnswer": "disguise / wicked",
          "explanation": "disguise (đồ hóa trang), wicked (độc ác)."
        },
        {
          "content": "6. We planted a vegetable garden to help ____________ our family. But many of the plants ____________ before we could eat them.",
          "options": ["nourish / rotted", "rotted / nourish", "nourishes / rotting", "rotting / nourishes"],
          "correctAnswer": "nourish / rotted",
          "explanation": "nourish (nuôi dưỡng), rotted (đã thối rữa)."
        },
        {
          "content": "7. The poor family was ____________ after all of their food ____________.",
          "options": ["starving / spoiled", "spoiled / starving", "starves / spoils", "spoils / starves"],
          "correctAnswer": "starving / spoiled",
          "explanation": "starving (chết đói), spoiled (đã hỏng)."
        },
        {
          "content": "8. Tim loves being an ____________ of that town. Shortly after he moved there, he made many friends.",
          "options": ["inhabitant / shortly", "shortly / inhabitant", "inhabitants / short", "short / inhabitants"],
          "correctAnswer": "inhabitant / shortly",
          "explanation": "inhabitant (cư dân), shortly (không lâu sau)."
        },
        {
          "content": "9. I entered a contest that was in my favorite ____________. Imagine the ____________ when I won!",
          "options": ["publication / thrill", "thrill / publication", "publications / thrills", "thrills / publications"],
          "correctAnswer": "publication / thrill",
          "explanation": "publication (ấn phẩm), thrill (sự phấn khích)."
        },
        {
          "content": "10. Christie ____________ me with her city's library. Since then, I have read every book they have about ____________.",
          "options": ["acquainted / pirates", "pirates / acquainted", "acquaints / pirate", "pirate / acquaints"],
          "correctAnswer": "acquainted / pirates",
          "explanation": "acquainted (làm quen), pirates (cướp biển)."
        }
      ]
    },
    {
      "title": "Exercise 2: Choose the answer that best fits the question.",
      "questions": [
        {
          "content": "1. Which of the following best describes an evil person?",
          "options": ["a. Shortly", "b. Curse", "c. Fancy", "d. Wicked"],
          "correctAnswer": "d. Wicked",
          "explanation": "Wicked có nghĩa là độc ác."
        },
        {
          "content": "2. Which one is a feeling?",
          "options": ["a. A thrill", "b. A hood", "c. A flashlight", "d. An inhabitant"],
          "correctAnswer": "a. A thrill",
          "explanation": "Thrill là một cảm giác hồi hộp, phấn khích."
        },
        {
          "content": "3. Which one can you wear?",
          "options": ["a. A cemetery", "b. A disguise", "c. A publication", "d. A riddle"],
          "correctAnswer": "b. A disguise",
          "explanation": "Disguise (đồ cải trang) là thứ có thể mặc được."
        },
        {
          "content": "4. Which of the following is most related to death?",
          "options": ["a. Spoil", "b. Acquaint", "c. Starve", "d. Nourish"],
          "correctAnswer": "c. Starve",
          "explanation": "Starve (chết đói) là từ liên quan nhiều nhất đến cái chết trong các từ đã cho."
        },
        {
          "content": "5. Which of the following is most commonly related to the ocean?",
          "options": ["a. Rot", "b. Scare", "c. Skeleton", "d. Pirate"],
          "correctAnswer": "d. Pirate",
          "explanation": "Pirate (hải tặc) liên quan đến đại dương."
        }
      ]
    },
    {
      "title": "Exercise 3: Write a word that is similar in meaning to the underlined part.",
      "questions": [
        {
          "content": "1. Mom says we need to hurry because the game will start very soon.",
          "options": ["shortly", "riddles", "curse", "fancy"],
          "correctAnswer": "shortly",
          "explanation": "very soon đồng nghĩa với shortly."
        },
        {
          "content": "2. It's a good idea to get to know with co-workers.",
          "options": ["acquaint", "inhabitant", "scared", "hood"],
          "correctAnswer": "acquaint",
          "explanation": "get to know đồng nghĩa với acquaint."
        },
        {
          "content": "3. My little brother bothered me all day by asking me to solve his difficult questions.",
          "options": ["riddles", "publication", "flashlight", "starve"],
          "correctAnswer": "riddles",
          "explanation": "difficult questions đồng nghĩa với riddles."
        },
        {
          "content": "4. A reporter at that newspaper won a prize.",
          "options": ["publication", "cemetery", "disguise", "pirate"],
          "correctAnswer": "publication",
          "explanation": "newspaper là một dạng publication (ấn phẩm)."
        },
        {
          "content": "5. I am an individual who lives in the central part of town.",
          "options": ["inhabitant", "skeleton", "spoil", "rot"],
          "correctAnswer": "inhabitant",
          "explanation": "individual who lives in đồng nghĩa với inhabitant."
        },
        {
          "content": "6. He was crying because he was caused to feel fright.",
          "options": ["scared", "wicked", "thrill", "curse"],
          "correctAnswer": "scared",
          "explanation": "caused to feel fright đồng nghĩa với scared."
        },
        {
          "content": "7. I want to buy that really nice dress I saw in the store.",
          "options": ["fancy", "shortly", "acquaint", "nourish"],
          "correctAnswer": "fancy",
          "explanation": "really nice đồng nghĩa với fancy."
        },
        {
          "content": "8. I need a light I can carry to see in the dark cabin.",
          "options": ["flashlight", "hood", "disguise", "riddle"],
          "correctAnswer": "flashlight",
          "explanation": "light I can carry đồng nghĩa với flashlight."
        },
        {
          "content": "9. The children were afraid that the witch would hope bad things would happen to them.",
          "options": ["curse", "rot", "scare", "starve"],
          "correctAnswer": "curse",
          "explanation": "hope bad things would happen đồng nghĩa với curse."
        },
        {
          "content": "10. The part of your coat that covers your head keeps your head nice and warm.",
          "options": ["hood", "fancy", "skeleton", "cemetery"],
          "correctAnswer": "hood",
          "explanation": "part of your coat that covers your head đồng nghĩa với hood."
        }
      ]
    }
  ],
  "story_exercise": {
    "title": "Reading Comprehension",
    "questions": [
      {
        "content": "Part A - 1. People from places like Iceland, Italy, Kenya and Canada believed souls needed food.",
        "options": ["True", "False", "Not Given", "None of the above"],
        "correctAnswer": "False",
        "explanation": "People from places like Ireland, China, Egypt, and Mexico believed souls needed food."
      },
      {
        "content": "Part A - 2. Many cultures believed that souls needed food to nourish them on their journey back to life.",
        "options": ["True", "False", "Not Given", "None of the above"],
        "correctAnswer": "False",
        "explanation": "Many cultures believed that souls needed food for their journey to heaven."
      },
      {
        "content": "Part A - 3. Housewives gave children food if they did chores around their homes.",
        "options": ["True", "False", "Not Given", "None of the above"],
        "correctAnswer": "False",
        "explanation": "Housewives gave children food if they sang or danced."
      },
      {
        "content": "Part A - 4. Shortly after a children's publication wrote about trick-or-treating, it became popular.",
        "options": ["True", "False", "Not Given", "None of the above"],
        "correctAnswer": "True",
        "explanation": "Đúng với nội dung bài."
      },
      {
        "content": "Part A - 5. Children often wear fancy disguises for trick-or-treating today.",
        "options": ["True", "False", "Not Given", "None of the above"],
        "correctAnswer": "True",
        "explanation": "Đúng với nội dung bài."
      },
      {
        "content": "Part A - 6. Inhabitants from villages started trick-or-treating in the 1940s.",
        "options": ["True", "False", "Not Given", "None of the above"],
        "correctAnswer": "False",
        "explanation": "Inhabitants from villages started trick-or-treating in the early 1900s."
      },
      {
        "content": "Part B - 1. Which of the following is the most popular disguise?",
        "options": ["a. Hood", "b. Skeleton", "c. Creature", "d. Pirate"],
        "correctAnswer": "b. Skeleton",
        "explanation": "Skeletons (cùng với ghosts) là những trang phục được yêu thích nhất."
      },
      {
        "content": "Part B - 2. Why did souls need food?",
        "options": ["a. Theirs rotted", "b. They were starving", "c. For their long journey to heaven", "d. To obtain new bodies"],
        "correctAnswer": "c. For their long journey to heaven",
        "explanation": "Theo bài, thức ăn nuôi dưỡng linh hồn trên chặng đường dài đến thiên đường."
      },
      {
        "content": "Part B - 3. What did the souls do when they left cemeteries?",
        "options": ["a. Got new bodies", "b. Dug up skeletons", "c. Went to heaven", "d. Got acquainted with people"],
        "correctAnswer": "c. Went to heaven",
        "explanation": "Linh hồn rời khỏi nghĩa địa để đến thiên đường."
      },
      {
        "content": "Part B - 4. Why do children perform riddles when they trick-or-treat?",
        "options": ["a. To get candy", "b. To get flashlights", "c. To get costumes", "d. To get a thrill"],
        "correctAnswer": "a. To get candy",
        "explanation": "Trẻ em giải đố (hoặc hát) để nhận được kẹo."
      }
    ]
  }
}

with open("unit5_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
