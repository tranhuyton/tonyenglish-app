import json

words = [
    {"word": "affection", "pron": "[afekjan]", "type": "n.", "def": "Affection is a feeling of liking someone or something.", "ex": "Amanda has a lot of affection for her little sister Sarah."},
    {"word": "agency", "pron": "[eid3ansi]", "type": "n.", "def": "An agency is a business or service set up to act for others.", "ex": "I went to a travel agency to help me arrange a flight home."},
    {"word": "ash", "pron": "[aej]", "type": "n.", "def": "Ash is the grey or black powder created when something is burned.", "ex": "The end of his cigar was full of ashes."},
    {"word": "confine", "pron": "[kanfain]", "type": "v.", "def": "To confine something is to keep it in one place.", "ex": "The elephant is confined to a cage in the zoo."},
    {"word": "dismiss", "pron": "[dismis]", "type": "v.", "def": "To dismiss something is to say it is not important.", "ex": "He quickly dismissed my idea about a new project."},
    {"word": "erupt", "pron": "[irApt]", "type": "v.", "def": "To erupt is for a volcano or something to shoot a hot substance.", "ex": "The volcano erupted for the first time in ten years."},
    {"word": "fate", "pron": "[feit]", "type": "n.", "def": "Fate is a power that causes some things to happen.", "ex": "Some people believe that a person's hand can tell their fate."},
    {"word": "lava", "pron": "[I6:va]", "type": "n.", "def": "Lava is the hot substance made of melted rock that shoots from volcanoes.", "ex": "The red hot lava poured from the volcano."},
    {"word": "miserable", "pron": "[mizerabal]", "type": "adj.", "def": "If someone is miserable, they are very unhappy.", "ex": "He was miserable after his dog died."},
    {"word": "navigate", "pron": "[naevageit]", "type": "v.", "def": "To navigate something is to control the way it moves or goes.", "ex": "She navigated the ship across the ocean."},
    {"word": "originate", "pron": "[ar(d3aneit]", "type": "v.", "def": "To originate somewhere is to start there.", "ex": "The idea of democracy originated in Ancient Greece."},
    {"word": "remainder", "pron": "[rimeindax]", "type": "n.", "def": "The remainder of something is what is left.", "ex": "He took a bite of the apple, then gave me the remainder of it."},
    {"word": "retrieve", "pron": "[ntit.v]", "type": "v.", "def": "To retrieve something is to find it and get it back.", "ex": "She retrieved her mail from the mail box."},
    {"word": "shallow", "pron": "[Jaelou]", "type": "adj.", "def": "If something is shallow, it is not deep.", "ex": "The kids were playing in the shallow water."},
    {"word": "slope", "pron": "[sloup]", "type": "n.", "def": "A slope is ground that is not flat.", "ex": "The slope to the top of the mountain was very steep."},
    {"word": "span", "pron": "[spaen]", "type": "v.", "def": "To span a length of time is to last that long.", "ex": "His work began in 1999. It has spanned many years since then."},
    {"word": "superstition", "pron": "[su:perstijan]", "type": "n.", "def": "A superstition is something magical that people believe is real.", "ex": "It is a superstition that Friday the 13th is an unlucky day."},
    {"word": "sympathy", "pron": "[sfmpaei]", "type": "n.", "def": "Sympathy is a feeling of being sad for another person.", "ex": "I felt sympathy for my sister so I got her a balloon to cheer her up."},
    {"word": "vibrate", "pron": "[vaibreit]", "type": "v.", "def": "To vibrate is to shake very hard.", "ex": "The machine made his whole body vibrate as he broke up the ground."},
    {"word": "wander", "pron": "[wandax]", "type": "v.", "def": "To wander is to walk without going to a certain place.", "ex": "The boys like to wander in the woods and look at birds."}
]

items_html = ""
for w in words:
    items_html += f'<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">{w["word"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">{w["pron"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">{w["type"]}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">{w["def"]}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ {w["ex"]}</div></div></div>'

part1_content = f'<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit17_v3_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit17_v3_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">{items_html}</div></div></div>'

part2_content = '<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Magic Cup</h1><p style="margin-bottom: 1rem;">Paul and John were brothers. They fought all the time because they both wanted to be leaders of the <b>agency</b> they both worked at.</p><p style="margin-bottom: 1rem;">There was a <b>superstition</b> in their town about a magic cup. People said the cup was in a volcano located far away. Anyone who <b>retrieved</b> the cup would have their wish come true. John and Paul both wanted to find it. Then they could become the leader.</p><p style="margin-bottom: 1rem;">They both left to find the cup. Before their trip, their mother said they should work together. They <b>dismissed</b> that idea. Even though their trips <b>originated</b> from the same house, each wanted to travel alone.</p><p style="margin-bottom: 1rem;">They were both <b>miserable</b> during the trip. They had to <b>navigate</b> small boats across <b>shallow</b> rivers and climb difficult <b>slopes</b>. Their journey <b>spanned</b> many days. When they finally got close to the volcano, the ground began to <b>vibrate</b> and the volcano <b>erupted</b>. <b>Ash</b> filled the sky and <b>lava</b> covered everything. John climbed to the top of a hill to keep from getting burned. A few moments later, his brother went up the same hill. They were <b>confined</b> to the hill until the lava cooled down.</p><p style="margin-bottom: 1rem;">They talked about the things they had seen while <b>wandering</b> around the country. They felt more <b>sympathy</b> and <b>affection</b> for each other than ever before. They decided that <b>fate</b> had brought them together.</p><p style="margin-bottom: 1rem;">The next day they left to finish the <b>remainder</b> of the trip together. Everything seemed much easier. When they finally found the cup, they learned that it didn’t make wishes come true. It was only an ordinary cup. But the trip to reach the cup taught them to work together and love each other.</p></div>'

json_data = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 17",
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
          "title": "Part A: Choose the answer that best fits the question.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "1",
              "content": "1. Which of the following mean that something is not important?",
              "options": ["a. Superstition", "b. Dismiss", "c. Vibrate", "d. Miserable"],
              "correctAnswer": "b. Dismiss",
              "explanation": "Dismiss: To say it is not important."
            },
            {
              "id": "2",
              "content": "2. What is the power that causes things to happen?",
              "options": ["a. Affection", "b. To originate", "c. To wander", "d. Fate"],
              "correctAnswer": "d. Fate",
              "explanation": "Fate: A power that causes some things to happen."
            },
            {
              "id": "3",
              "content": "3. What is the hot liquid from a volcano called?",
              "options": ["a. Shallow", "b. Ash", "c. Slope", "d. Lava"],
              "correctAnswer": "d. Lava",
              "explanation": "Lava: The hot substance made of melted rock that shoots from volcanoes."
            },
            {
              "id": "4",
              "content": "4. What is something that a volcano does?",
              "options": ["a. Fate", "b. Erupt", "c. Remainder", "d. Sympathy"],
              "correctAnswer": "b. Erupt",
              "explanation": "Erupt: To shoot a hot substance."
            },
            {
              "id": "5",
              "content": "5. What is it called to have belief in something magical?",
              "options": ["a. Superstition", "b. Vibrate", "c. Agency", "d. Confine"],
              "correctAnswer": "a. Superstition",
              "explanation": "Superstition: Something magical that people believe is real."
            }
          ]
        },
        {
          "id": "sec2_wordlist",
          "title": "Part B: Write a word that is similar in meaning to the underlined part.",
          "content": "",
          "questionType": "Điền khuyết",
          "questions": [
            {
              "id": "6",
              "content": "1. John was very *unhappy* when he lost his favorite book.",
              "options": [],
              "correctAnswer": "miserable",
              "explanation": "unhappy = miserable"
            },
            {
              "id": "7",
              "content": "2. Manny found a job with a local news *company that deals with other businesses*.",
              "options": [],
              "correctAnswer": "agency",
              "explanation": "company that deals with other businesses = agency"
            },
            {
              "id": "8",
              "content": "3. The river in front of her house is *not deep*.",
              "options": [],
              "correctAnswer": "shallow",
              "explanation": "not deep = shallow"
            },
            {
              "id": "9",
              "content": "4. I don’t like to *keep in one place* my dog; I want him to run around.",
              "options": [],
              "correctAnswer": "confine",
              "explanation": "keep in one place = confine"
            },
            {
              "id": "10",
              "content": "5. The house burned down, and there was only *grey powder* left.",
              "options": [],
              "correctAnswer": "ash",
              "explanation": "grey powder = ash"
            },
            {
              "id": "11",
              "content": "6. She has to *control where to go* when she travels with her father.",
              "options": [],
              "correctAnswer": "navigate",
              "explanation": "control where to go = navigate"
            },
            {
              "id": "12",
              "content": "7. My plan to become a farmer *started* when I was a child.",
              "options": [],
              "correctAnswer": "originated",
              "explanation": "started = originated"
            },
            {
              "id": "13",
              "content": "8. He has a *feeling of love* for his grandfather.",
              "options": [],
              "correctAnswer": "affection",
              "explanation": "feeling of love = affection"
            },
            {
              "id": "14",
              "content": "9. The people left the town when the ground started *shaking*.",
              "options": [],
              "correctAnswer": "vibrating",
              "explanation": "shaking = vibrating"
            },
            {
              "id": "15",
              "content": "10. I had a *feeling of sadness* for her when her dog died.",
              "options": [],
              "correctAnswer": "sympathy",
              "explanation": "feeling of sadness = sympathy"
            }
          ]
        },
        {
          "id": "sec3_wordlist",
          "title": "Part C: Choose the word that is a better fit for each blank.",
          "content": "",
          "questionType": "Điền khuyết",
          "questions": [
            {
              "id": "16",
              "content": "1. originated / superstition\nThe ________ from Europe and was brought to North America.",
              "options": [],
              "correctAnswer": "superstition",
              "explanation": "superstition"
            },
            {
              "id": "17",
              "content": "1b. originated / superstition\nThe superstition ________ from Europe and was brought to North America.",
              "options": [],
              "correctAnswer": "originated",
              "explanation": "originated"
            },
            {
              "id": "18",
              "content": "2. agency / dismissed\nThe ________ quickly",
              "options": [],
              "correctAnswer": "agency",
              "explanation": "agency"
            },
            {
              "id": "19",
              "content": "2b. agency / dismissed\nThe agency quickly ________ his idea as being too unrealistic to be of any use.",
              "options": [],
              "correctAnswer": "dismissed",
              "explanation": "dismissed"
            },
            {
              "id": "20",
              "content": "3. slope / lava\nTheir house is built on a ________ .",
              "options": [],
              "correctAnswer": "slope",
              "explanation": "slope"
            },
            {
              "id": "21",
              "content": "3b. slope / lava\nThere is great concern that ________ from a nearby volcano will destroy the house easily.",
              "options": [],
              "correctAnswer": "lava",
              "explanation": "lava"
            },
            {
              "id": "22",
              "content": "4. vibrate / fate\nWhen he learned of his ________ , he was frightened.",
              "options": [],
              "correctAnswer": "fate",
              "explanation": "fate"
            },
            {
              "id": "23",
              "content": "4b. vibrate / fate\nIt made his entire body ________ uncontrollably.",
              "options": [],
              "correctAnswer": "vibrate",
              "explanation": "vibrate"
            },
            {
              "id": "24",
              "content": "5. sympathy / confine\nPlease ________ your",
              "options": [],
              "correctAnswer": "confine",
              "explanation": "confine"
            },
            {
              "id": "25",
              "content": "5b. sympathy / confine\nconfine your ________ for someone who really needs it.",
              "options": [],
              "correctAnswer": "sympathy",
              "explanation": "sympathy"
            },
            {
              "id": "26",
              "content": "6. ash / erupted\nA gray cloud of ________",
              "options": [],
              "correctAnswer": "ash",
              "explanation": "ash"
            },
            {
              "id": "27",
              "content": "6b. ash / erupted\ncloud of ash ________ from the tailpipe of the car that had not been started in three years.",
              "options": [],
              "correctAnswer": "erupted",
              "explanation": "erupted"
            },
            {
              "id": "28",
              "content": "7. retrieve / miserable\nI felt ________ all evening.",
              "options": [],
              "correctAnswer": "miserable",
              "explanation": "miserable"
            },
            {
              "id": "29",
              "content": "7b. retrieve / miserable\nPerhaps I caught a virus when I had to ________ the missing sheep from the heavy rainstorm.",
              "options": [],
              "correctAnswer": "retrieve",
              "explanation": "retrieve"
            },
            {
              "id": "30",
              "content": "8. wander / affection\nI have great ________ for those who do exciting things.",
              "options": [],
              "correctAnswer": "affection",
              "explanation": "affection"
            },
            {
              "id": "31",
              "content": "8b. wander / affection\nWhen I was young, I would often ________ the countryside just for fun.",
              "options": [],
              "correctAnswer": "wander",
              "explanation": "wander"
            },
            {
              "id": "32",
              "content": "9. remainder / shallow\nWe sent the youngsters home while the ________ of the group crossed the",
              "options": [],
              "correctAnswer": "remainder",
              "explanation": "remainder"
            },
            {
              "id": "33",
              "content": "9b. remainder / shallow\ncrossed the ________ but fast moving stream.",
              "options": [],
              "correctAnswer": "shallow",
              "explanation": "shallow"
            },
            {
              "id": "34",
              "content": "10. spanned / navigate\nIt was a difficult trip, but we managed to ________ our way through the wilderness",
              "options": [],
              "correctAnswer": "navigate",
              "explanation": "navigate"
            },
            {
              "id": "35",
              "content": "10b. spanned / navigate\nin a trip that ________ five days.",
              "options": [],
              "correctAnswer": "spanned",
              "explanation": "spanned"
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": part2_content,
      "imageUrl": "/unit17_v3_story.png",
      "sections": [
        {
          "id": "sec4_reading_A",
          "title": "Part A: Mark each statement T for true or F for false.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "36",
              "content": "1. The trip to find the magic cup was very easy.",
              "options": ["T", "F"],
              "correctAnswer": "F",
              "explanation": "The trip to find the magic cup was very difficult."
            },
            {
              "id": "37",
              "content": "2. The boys dismissed their mother’s advice before they left for the trip.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            },
            {
              "id": "38",
              "content": "3. The boys were confined to a hilltop by the lava after the volcano erupted.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            },
            {
              "id": "39",
              "content": "4. A superstition said that anyone who retrieved the cup would become the leader of the agency.",
              "options": ["T", "F"],
              "correctAnswer": "F",
              "explanation": "A superstition said that anyone who retrieved the magic cup would get their greatest wish."
            },
            {
              "id": "40",
              "content": "5. The boys had more affection and sympathy for each other after the trip.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            },
            {
              "id": "41",
              "content": "6. After the volcano erupted, there was ash in the sky and lava on the ground.",
              "options": ["T", "F"],
              "correctAnswer": "T",
              "explanation": "True"
            }
          ]
        },
        {
          "id": "sec5_reading_B",
          "title": "Part B: Answer the questions.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "42",
              "content": "1. Why didn’t the boys travel together?",
              "options": ["a. Their trips originated from different places.", "b. They were both miserable.", "c. They had to navigate boats across shallow rivers.", "d. They wanted to travel alone."],
              "correctAnswer": "d. They wanted to travel alone.",
              "explanation": "Even though their trips originated from the same house, each wanted to travel alone."
            },
            {
              "id": "43",
              "content": "2. Why were the boys always fighting??",
              "options": ["a. The cup had special powers.", "b. They had very little food to eat.", "c. There was a hole beneath the tree.", "d. They both wanted to be leaders of the agency."],
              "correctAnswer": "d. They both wanted to be leaders of the agency.",
              "explanation": "They fought all the time because they both wanted to be leaders of the agency they both worked at."
            },
            {
              "id": "44",
              "content": "3. Why did fate bring the boys together?",
              "options": ["a. To show that stories about the tree weren’t true", "b. So they could complete the remainder of the trip together", "c. So they could return home together", "d. So their trip could span many days"],
              "correctAnswer": "b. So they could complete the remainder of the trip together",
              "explanation": "The next day they left to finish the remainder of the trip together."
            },
            {
              "id": "45",
              "content": "4. What was surprising about the cup?",
              "options": ["a. It was only an ordinary cup.", "b. It did not really exist,", "c. It had their names written on it.", "d. It was made of gold."],
              "correctAnswer": "a. It was only an ordinary cup.",
              "explanation": "When they finally found the cup, they learned that it didn’t make wishes come true. It was only an ordinary cup."
            }
          ]
        }
      ]
    }
  ]
}

with open("c:\\Users\\Tony\\.gemini\\antigravity\\scratch\\tonyenglish-app\\unit17_raw.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Saved to unit17_raw.json")
