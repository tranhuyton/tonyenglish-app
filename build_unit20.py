import json

words = [
    ("adhesive", "[*dh ( siv]", "n.", "An adhesive is a substance used for sticking things together.", "The carpenter used an adhesive to hold the two pieces of wood together."),
    ("adverse", "[aedvairs]", "adj.", "If something is adverse, then it is harmful.", "Not eating healthy foods can have an adverse effect on your health."),
    ("dependency", "[dipendansi]", "n.", "A dependency is a strong need for someone or something.", "The child still has a dependency on her mother."),
    ("dump", "[d A m p ]", "v.", "To dump something means to throw it away or get rid of it.", "She dumped the garbage into the trash can."),
    ("eternal", "[itamsi]", "adj.", "If something is eternal, then it lasts forever.", "She said that her love for him was eternal."),
    ("fluctuate", "[flAktfueit]", "v.", "To fluctuate means to rise and fall in number or amount.", "Prices for gasoline have been fluctuating all month."),
    ("fro", "[frou]", "adv.", "If something moves to and fro, it moves backward and forward or side to side.", "Her long hair went to and fro as she swung on the swing."),
    ("inclusion", "[inklu:3an]", "n.", "Inclusion is the act of including someone or something in a group.", "Her inclusion into the photo club was well received."),
    ("intermediate", "[intarmhdiit]", "adj.", "If something is intermediate, then it is in the middle of two levels, places, or times.", "He selected the intermediate ski hill to begin his afternoon of skiing."),
    ("intermittent", "[intarmftent]", "adj.", "If something is intermittent, then it happens in a way that is not constant.", "It was hard to focus because intermittent noises came from the workers outside."),
    ("mentor", "[mentor]", "n.", "A mentor is a person with experience or knowledge who advises someone.", "The students each chose a mentor to help them with the experiment."),
    ("phoenix", "[frniks]", "n.", "A phoenix is an imaginary bird that burned to ashes and was reborn.", "Some believe the phoenix is a symbol for rebirth and a new beginning."),
    ("photosynthesis", "[foutot/sineesis]", "n.", "Photosynthesis is the process in which plants change sunlight and air.", "The chemical in plants that makes them green is used in photosynthesis."),
    ("pollen", "[palen]", "n.", "Pollen is the tiny yellow powder made in the flowers of plants.", "During the spring, the pollen in the air makes some people become sick."),
    ("regain", "[rigein]", "v.", "To regain something means to get it back.", "The battery regained its power after being recharged."),
    ("reverse", "[rivers]", "v.", "To reverse means to change to the opposite direction.", "They reversed their direction after seeing the sign."),
    ("swarm", "[sworm]", "n.", "A swarm is a group of flying insects.", "A beautiful swarm of butterflies filled the summer sky."),
    ("texture", "[tekstjar]", "n.", "Texture is the quality of something that can be known by its touch.", "The texture of her skin was very soft and smooth."),
    ("tickle", "[tlkal]", "v.", "To tickle someone is to touch them in a way that causes laughter.", "The mother tickled the little boy’s foot, and he screamed with laughter."),
    ("vibrant", "[vaibrant]", "adj.", "If something is vibrant, then it is bright and full of color.", "Their new shirts were a vibrant shade of red.")
]

word_html_parts = []
for word, pron, pos, defi, ex in words:
    part = f'<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">{word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">{pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">{pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">{defi}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ {ex}</div></div></div>'
    word_html_parts.append(part)

words_content = "".join(word_html_parts)
part1_content = f'<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit20_vol6_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit20_vol6_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">{words_content}</div></div></div>'

story_html = '<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Greedy Bee</h1><p style="margin-bottom: 1rem;">A young bee had passed his <b>intermediate</b> level exams. He now knew everything about flowers. He understood how they used <b>photosynthesis</b> to make oxygen and which ones produced the best <b>pollen</b>. Bees had an important <b>dependency</b> on <b>pollen</b>. From the beginning of time, bees\' <b>eternal</b> task was to gather <b>pollen</b> and make honey with it.</p><p style="margin-bottom: 1rem;">Since he passed his exams, the little bee had earned his <b>inclusion</b> in the <b>swarms</b> that gathered <b>pollen</b>. He was excited because he was finally allowed to leave the hive. He left with the next <b>swarm</b> and was determined to find the perfect flower. Soon he saw a large, <b>vibrant</b> flower full of <b>pollen</b>. He landed on a petal and walked toward the <b>pollen</b> at the flower\'s center.</p><p style="margin-bottom: 1rem;">Immediately, he began rolling in the <b>pollen</b>, gathering it on his legs and wings. The fine <b>texture</b> of the <b>pollen</b> <b>tickled</b> when it stuck to his body. It was the best experience the little bee had ever had. He gathered as much as he could.</p><p style="margin-bottom: 1rem;">But when he was flying back home, he realized that all the <b>pollen</b> had an <b>adverse</b> effect. He had no control over his flight. The <b>intermittent</b> wind <b>fluctuated</b> in power. He was blown to and <b>fro</b>. One minute he was flying straight, and the next minute the wind had <b>reversed</b> his course.</p><p style="margin-bottom: 1rem;">He tried to <b>dump</b> some of the <b>pollen</b>, but it acted as an <b>adhesive</b>. He couldn\'t get it off. He became tired and fell to the ground.</p><p style="margin-bottom: 1rem;">"What am I going to do now?" he thought. Just then, his <b>mentor</b> landed next to him and began cleaning the excess <b>pollen</b> off the little bee. "You shouldn\'t have taken so much," his <b>mentor</b> said.</p><p style="margin-bottom: 1rem;">Finally, with the <b>pollen</b> off of him, the bee easily <b>regained</b> his strength, and like a <b>phoenix</b>, the young bee flew back into the air. When he returned to the hive, he turned to his <b>mentor</b> and said, "I learned an important lesson today. I will never be greedy again."</p></div>'

data = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 20: Volume 6",
    "category": "exercise",
    "timeLimit": 0
  },
  "parts": [
    {
      "id": "part1",
      "title": "Word List",
      "content": part1_content,
      "sections": [
        {
          "id": "sec1_wordlist",
          "title": "Exercise 1: Choose the one that is similar in meaning to the given word.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "1",
              "content": "1. reverse",
              "options": ["spell", "train", "switch", "camp"],
              "correctAnswer": "switch",
              "explanation": "reverse (v): switch. To reverse means to change to the opposite direction."
            },
            {
              "id": "2",
              "content": "2. adverse",
              "options": ["written", "harmful", "tense", "blank"],
              "correctAnswer": "harmful",
              "explanation": "adverse (adj): harmful. If something is adverse, then it is harmful."
            },
            {
              "id": "3",
              "content": "3. intermediate",
              "options": ["amazing", "safe", "stupid", "middle"],
              "correctAnswer": "middle",
              "explanation": "intermediate (adj): middle. If something is intermediate, then it is in the middle of two levels, places, or times."
            },
            {
              "id": "4",
              "content": "4. regain",
              "options": ["reclaim", "book", "member", "length"],
              "correctAnswer": "reclaim",
              "explanation": "regain (v): reclaim. To regain something means to get it back."
            },
            {
              "id": "5",
              "content": "5. mentor",
              "options": ["flavor", "terror", "teacher", "painter"],
              "correctAnswer": "teacher",
              "explanation": "mentor (n): teacher. A mentor is a person with experience or knowledge who advises someone."
            },
            {
              "id": "6",
              "content": "6. inclusion",
              "options": ["energy", "moment", "peninsula", "welcome"],
              "correctAnswer": "welcome",
              "explanation": "inclusion (n): welcome. Inclusion is the act of including someone or something in a group."
            },
            {
              "id": "7",
              "content": "7. adhesive",
              "options": ["paste", "floor", "segment", "treasure"],
              "correctAnswer": "paste",
              "explanation": "adhesive (n): paste. An adhesive is a substance used for sticking things together."
            },
            {
              "id": "8",
              "content": "8. vibrant",
              "options": ["dangerous", "messy", "dynamic", "hollow"],
              "correctAnswer": "dynamic",
              "explanation": "vibrant (adj): dynamic. If something is vibrant, then it is bright and full of color."
            },
            {
              "id": "9",
              "content": "9. dependency",
              "options": ["expanse", "need", "freshness", "tone"],
              "correctAnswer": "need",
              "explanation": "dependency (n): need. A dependency is a strong need for someone or something."
            },
            {
              "id": "10",
              "content": "10. swarm",
              "options": ["heat", "group", "truth", "ledge"],
              "correctAnswer": "group",
              "explanation": "swarm (n): group. A swarm is a group of flying insects."
            }
          ]
        },
        {
          "id": "sec2_wordlist",
          "title": "Exercise 2: Fill in the blanks with the correct words from the word bank: phoenix, intermittent, dependency, texture, fro, mentor, pollen, adverse, photosynthesis, vibrant.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "11",
              "content": "1. He enjoyed watching the ______________ movement of the branch in the wind.",
              "options": ["intermittent", "fro", "phoenix", "vibrant"],
              "correctAnswer": "intermittent",
              "explanation": "intermittent (adj): happening in a way that is not constant."
            },
            {
              "id": "12",
              "content": "2. As the branch moved to and ______________, he felt calmed.",
              "options": ["intermittent", "fro", "dependency", "texture"],
              "correctAnswer": "fro",
              "explanation": "fro (adv): backward and forward or side to side."
            },
            {
              "id": "13",
              "content": "3. Her favorite magical creature was the _____________.",
              "options": ["mentor", "pollen", "phoenix", "texture"],
              "correctAnswer": "phoenix",
              "explanation": "phoenix (n): an imaginary bird that burned to ashes and was reborn."
            },
            {
              "id": "14",
              "content": "4. The bird’s feathers were always a(n) ______________ mix of red and orange.",
              "options": ["adverse", "vibrant", "intermittent", "fro"],
              "correctAnswer": "vibrant",
              "explanation": "vibrant (adj): bright and full of color."
            },
            {
              "id": "15",
              "content": "5. Actually, those flowers have a(n) ______________ effect on my mother’s health.",
              "options": ["dependency", "photosynthesis", "adverse", "vibrant"],
              "correctAnswer": "adverse",
              "explanation": "adverse (adj): harmful."
            },
            {
              "id": "16",
              "content": "6. The ______________ in it makes her sneeze.",
              "options": ["pollen", "texture", "phoenix", "mentor"],
              "correctAnswer": "pollen",
              "explanation": "pollen (n): the tiny yellow powder made in the flowers of plants."
            },
            {
              "id": "17",
              "content": "7. Mr. Roth had been a valuable ______________ for so many years.",
              "options": ["mentor", "dependency", "phoenix", "texture"],
              "correctAnswer": "mentor",
              "explanation": "mentor (n): a person with experience or knowledge who advises someone."
            },
            {
              "id": "18",
              "content": "8. You could feel the knowledge from the ______________ of his wrinkled hands.",
              "options": ["pollen", "texture", "adverse", "photosynthesis"],
              "correctAnswer": "texture",
              "explanation": "texture (n): the quality of something that can be known by its touch."
            },
            {
              "id": "19",
              "content": "9. Plants have a(n) ______________ on sunlight.",
              "options": ["dependency", "phoenix", "mentor", "fro"],
              "correctAnswer": "dependency",
              "explanation": "dependency (n): a strong need for someone or something."
            },
            {
              "id": "20",
              "content": "10. It’s a necessary ingredient for the process of ______________ .",
              "options": ["photosynthesis", "pollen", "texture", "vibrant"],
              "correctAnswer": "photosynthesis",
              "explanation": "photosynthesis (n): the process in which plants change sunlight and air."
            }
          ]
        },
        {
          "id": "sec3_wordlist",
          "title": "Exercise 3: Choose the one that is opposite in meaning to the given word.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "21",
              "content": "1. inclusion",
              "options": ["exclusion", "inside", "instant", "unclean"],
              "correctAnswer": "exclusion",
              "explanation": "Opposite of inclusion is exclusion."
            },
            {
              "id": "22",
              "content": "2. regain",
              "options": ["snow", "break", "lose", "smell"],
              "correctAnswer": "lose",
              "explanation": "Opposite of regain is lose."
            },
            {
              "id": "23",
              "content": "3. eternal",
              "options": ["great", "true", "flat", "brief"],
              "correctAnswer": "brief",
              "explanation": "Opposite of eternal is brief."
            },
            {
              "id": "24",
              "content": "4. dump",
              "options": ["gather", "explain", "solve", "glow"],
              "correctAnswer": "gather",
              "explanation": "Opposite of dump is gather."
            },
            {
              "id": "25",
              "content": "5. fluctuate",
              "options": ["heal", "remain", "stutter", "choose"],
              "correctAnswer": "remain",
              "explanation": "Opposite of fluctuate is remain."
            }
          ]
        },
        {
          "id": "sec4_wordlist",
          "title": "Exercise 4: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "26",
              "content": "1. The branches moved to and *fro* in the breeze.",
              "options": ["C", "I"],
              "correctAnswer": "C",
              "explanation": "fro means backward and forward or side to side."
            },
            {
              "id": "27",
              "content": "2. Honeybees collect *pollen* from flowers.",
              "options": ["C", "I"],
              "correctAnswer": "C",
              "explanation": "pollen is the powder made in flowers."
            },
            {
              "id": "28",
              "content": "3. The meeting was *eternal*. It lasted only ten minutes.",
              "options": ["C", "I"],
              "correctAnswer": "I",
              "explanation": "eternal means lasting forever, which contradicts lasting only ten minutes."
            },
            {
              "id": "29",
              "content": "4. The *adhesive* on this tape doesn’t work anymore. It won’t stick.",
              "options": ["C", "I"],
              "correctAnswer": "C",
              "explanation": "adhesive is a substance used for sticking things together."
            },
            {
              "id": "30",
              "content": "5. In order to get into the sports arena, we had to pay a *phoenix*.",
              "options": ["C", "I"],
              "correctAnswer": "I",
              "explanation": "phoenix is a mythical bird, not a fee or money."
            },
            {
              "id": "31",
              "content": "6. This past week the weather has *fluctuated* a lot. It’s been warm and sunny every day.",
              "options": ["C", "I"],
              "correctAnswer": "I",
              "explanation": "fluctuated means rising and falling or changing; 'warm and sunny every day' means it was constant."
            },
            {
              "id": "32",
              "content": "7. Don’t touch my knee. It *tickles* when anything touches me there.",
              "options": ["C", "I"],
              "correctAnswer": "C",
              "explanation": "tickles means causing laughter by touching."
            },
            {
              "id": "33",
              "content": "8. She *dumped* the dirty water out back in the garden.",
              "options": ["C", "I"],
              "correctAnswer": "C",
              "explanation": "dumped means thrown away or gotten rid of."
            },
            {
              "id": "34",
              "content": "9. My level of Spanish is only at the *intermediate* stage.",
              "options": ["C", "I"],
              "correctAnswer": "C",
              "explanation": "intermediate means in the middle of two levels."
            },
            {
              "id": "35",
              "content": "10. The *texture* of his workload was incredible.",
              "options": ["C", "I"],
              "correctAnswer": "I",
              "explanation": "texture refers to the quality of something known by its touch, it doesn't make sense for a workload."
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": story_html,
      "imageUrl": "/unit20_vol6_story.png",
      "sections": [
        {
          "id": "sec5",
          "title": "Part A: Mark each statement T for true or F for false.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "36",
              "content": "1. The bees had an important dependency on pollen.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "T"
            },
            {
              "id": "37",
              "content": "2. The texture of the petals in the vibrant flower tickled.",
              "options": ["T", "F"],
              "correctAnswer": "F",
              "explanation": "F: The texture of the pollen in the vibrant flower tickled."
            },
            {
              "id": "38",
              "content": "3. The little bee was blown to and fro and reversed in his direction.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "T"
            },
            {
              "id": "39",
              "content": "4. Because the pollen acted like an adhesive, the little bee couldn’t dump it.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "T"
            },
            {
              "id": "40",
              "content": "5. After his mentor helped him regain his strength, the little bee lost his ambitions and fell to the ground like a phoenix.",
              "options": ["T", "F"],
              "correctAnswer": "F",
              "explanation": "F: After his mentor helped him regain his strength, the little bee flew back into the air like a phoenix."
            }
          ]
        },
        {
          "id": "sec6",
          "title": "Part B: Answer the questions.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "41",
              "content": "1. After the intermediate exams, what did the bee know about photosynthesis?",
              "options": ["He understood how flowers used photosynthesis to make food.", "He knew how to use photosynthesis to fly.", "He learned how to stop photosynthesis.", "He didn't know anything about it."],
              "correctAnswer": "He understood how flowers used photosynthesis to make food.",
              "explanation": "He understood how flowers used photosynthesis to make oxygen/food."
            },
            {
              "id": "42",
              "content": "2. What did his inclusion in the swarms finally allow the little bee to do?",
              "options": ["Finally, he was allowed to leave the hive.", "He was allowed to eat all the honey.", "He was allowed to sleep all day.", "He was allowed to sting animals."],
              "correctAnswer": "Finally, he was allowed to leave the hive.",
              "explanation": "He was excited because he was finally allowed to leave the hive."
            },
            {
              "id": "43",
              "content": "3. What was the bees’ eternal task?",
              "options": ["From the beginning of time, bees' eternal task was to gather pollen and make honey with it.", "Their task was to protect the queen at all costs.", "Their task was to build a new hive.", "Their task was to fight other insects."],
              "correctAnswer": "From the beginning of time, bees' eternal task was to gather pollen and make honey with it.",
              "explanation": "From the beginning of time, bees' eternal task was to gather pollen and make honey with it."
            },
            {
              "id": "44",
              "content": "4. How did the excess pollen have an adverse effect on the bee’s flight?",
              "options": ["He had no control over his flight.", "He flew much faster than before.", "He flew higher into the sky.", "He became completely invisible."],
              "correctAnswer": "He had no control over his flight.",
              "explanation": "He had no control over his flight."
            },
            {
              "id": "45",
              "content": "5. What was intermittent and fluctuated in the bees’ power?",
              "options": ["The wind was intermittent and fluctuated in power.", "His wings were intermittent and fluctuated in power.", "The sun was intermittent and fluctuated in power.", "The rain was intermittent and fluctuated in power."],
              "correctAnswer": "The wind was intermittent and fluctuated in power.",
              "explanation": "The wind was intermittent and fluctuated in power."
            }
          ]
        }
      ]
    }
  ]
}

with open("public/unit20_vol6.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
