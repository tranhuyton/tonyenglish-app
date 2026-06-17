import json

words = [
    {"word": "congested", "phonetic": "[kand3estid]", "type": "adj.", "def": "If something is congested, it is full or blocked.", "ex": "Tom didn’t get home until after dark because the road was so congested."},
    {"word": "courier", "phonetic": "[kuriar]", "type": "n.", "def": "A courier is someone who takes and delivers mail or packages.", "ex": "Before trains, most couriers used horses to travel."},
    {"word": "deform", "phonetic": "[difo:rm]", "type": "v.", "def": "To deform something means to change it from its correct or original shape.", "ex": "The computer program deformed the building’s picture into an unreal sight."},
    {"word": "etiquette", "phonetic": "[etiket]", "type": "n.", "def": "Etiquette is the group of rules about how to be polite.", "ex": "When in Asian countries, bowing is a form of etiquette."},
    {"word": "exclusive", "phonetic": "[iksklu:siv]", "type": "adj.", "def": "If something is exclusive, it is expensive and only for rich people.", "ex": "The golf course was so exclusive that most people hadn’t even heard of it."},
    {"word": "freight", "phonetic": "[freit]", "type": "n.", "def": "Freight is a set of items carried on a train, boat, or airplane.", "ex": "Trade ships only carried valuable freight like silk and spices."},
    {"word": "garment", "phonetic": "[ga:rmant]", "type": "n.", "def": "A garment is a piece of clothing.", "ex": "The business man had all of his garments cleaned before the important meeting."},
    {"word": "insomnia", "phonetic": "[insamnia]", "type": "n.", "def": "Insomnia is a condition in which a person has difficulty sleeping.", "ex": "Nate’s insomnia prevented him from getting enough rest."},
    {"word": "intuitive", "phonetic": "[intu:itiv]", "type": "adj.", "def": "Intuitive is knowing about something without naturally having support or proof.", "ex": "Rhonda had an intuitive feeling that Shane wasn’t coming to school today."},
    {"word": "liable", "phonetic": "[laiabal]", "type": "adj.", "def": "If something is liable to happen, it is very likely that it will happen.", "ex": "During the summer months, hikers in the forest are liable to see deer and elk."},
    {"word": "obsess", "phonetic": "[abses]", "type": "v.", "def": "To obsess about something means to think about it all of the time.", "ex": "After watching the Star Wars movies, Ike obsessed about becoming a Jedi."},
    {"word": "overboard", "phonetic": "[ouvarbo:rd]", "type": "adv.", "def": "When something is overboard, it is over the side of a boat and in the water.", "ex": "Tom and Gary slipped on the wet floor and fell overboard."},
    {"word": "premium", "phonetic": "[pri:miam]", "type": "n.", "def": "A premium is a payment that is higher than average.", "ex": "Tony paid for premium gas because it made his car run the best."},
    {"word": "privilege", "phonetic": "[privalid3]", "type": "n.", "def": "A privilege is a special right given to only a certain person or group of people.", "ex": "Only the best employee had the privilege of parking in that spot."},
    {"word": "propel", "phonetic": "[prapel]", "type": "v.", "def": "To propel something means to push or move it somewhere.", "ex": "The strong wind propelled the leaf through the air and across the street."},
    {"word": "socialize", "phonetic": "[soujalaiz]", "type": "v.", "def": "To socialize is to have a good time with people.", "ex": "I like to socialize with my classmates after school."},
    {"word": "suppress", "phonetic": "[sapres]", "type": "v.", "def": "To suppress something means to prevent it from happening.", "ex": "She suppressed her urge to scream because she didn’t want to be noticed."},
    {"word": "tram", "phonetic": "[traem]", "type": "n.", "def": "A tram is a vehicle like a streetcar that runs on electricity above ground.", "ex": "I took the tram to Eighth Avenue."},
    {"word": "unsettle", "phonetic": "[Ansetl]", "type": "v.", "def": "To unsettle someone means to make them anxious or worried.", "ex": "The dark clouds in the sky unsettled Beth."},
    {"word": "warp", "phonetic": "[wo:rp]", "type": "v.", "def": "To warp means to become bent into the wrong shape.", "ex": "The woman put the clock above the fireplace, and the heat warped it."}
]

html_words = ""
for w in words:
    html_words += f'<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">{w["word"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">{w["phonetic"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">{w["type"]}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">{w["def"]}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ {w["ex"]}</div></div></div>'

part1_content = f'<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit8_vol6_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit8_vol6_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">{html_words}</div></div></div>'

story = """<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">Watch Out!</h1><p style="margin-bottom: 1rem;">Kevin stepped off the <b>tram</b> and walked toward the ship, holding a package tightly in his hands. He had been hired as a <b>courier</b> for an important broker. All he needed to do was deliver a package to an office in New York City; the ship would take him there.</p><p style="margin-bottom: 1rem;">When he boarded, the ship was <b>congested</b> with people. As Kevin walked to his cabin, he saw the <b>exclusive</b> first-class section. Everybody inside was wearing fancy <b>garments</b>. He would have liked to <b>socialize</b> with the people inside, but it was against proper <b>etiquette</b>. People paid a <b>premium</b> for the <b>privilege</b> to ride in first-class.</p><p style="margin-bottom: 1rem;">Instead, he went to his cabin next to the <b>freight</b> section of the boat. His room smelled bad, and the floorboards were <b>warped</b> and <b>deformed</b> in some areas. He could also hear the motor humming as it waited to <b>propel</b> the ship forward. Suddenly, Kevin was <b>unsettled</b> by something, but he wasn’t sure why.</p><p style="margin-bottom: 1rem;">He took a short walk on the ship’s deck, but he still felt strange. That night, he suffered from <b>insomnia</b>—he couldn’t <b>suppress</b> his <b>obsessing</b> over how strange he felt.</p><p style="margin-bottom: 1rem;">Kevin went back on deck. It was cold and dark outside. He looked <b>overboard</b>, but it seemed that everything was all right. “Just go back inside,” he thought. Then Kevin saw it. A giant iceberg was sticking out of the ocean in the distance!</p><p style="margin-bottom: 1rem;">“Help!” he yelled.</p><p style="margin-bottom: 1rem;">People looked at him as if he was crazy, but he continued to shout until he saw the captain.</p><p style="margin-bottom: 1rem;">“There’s an iceberg out there,” Kevin said to him. “If the ship doesn’t move, we’re <b>liable</b> to crash,” he said, pointing toward the iceberg.</p><p style="margin-bottom: 1rem;">The captain saw it and immediately instructed the crew to change the ship’s direction. “Without your help, we would have definitely hit the iceberg. That would have been a terrible disaster!” he said to Kevin.</p><p style="margin-bottom: 1rem;">Kevin felt relieved. Now he knew to always trust his <b>intuitive</b> sense.</p></div>"""

# Remove newlines for minified HTML
story = story.replace('\n', '').replace('\r', '')

data = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 8: Volume 6",
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
              "content": "1. congested",
              "options": ["normal", "crowded", "distinct", "hostile"],
              "correctAnswer": "crowded",
              "explanation": "congested (adj): crowded, full or blocked."
            },
            {
              "id": "2",
              "content": "2. exclusive",
              "options": ["limited", "ancient", "inexpensive", "unruly"],
              "correctAnswer": "limited",
              "explanation": "exclusive (adj): limited, only for rich people."
            },
            {
              "id": "3",
              "content": "3. unsettle",
              "options": ["bring", "intend", "increase", "worry"],
              "correctAnswer": "worry",
              "explanation": "unsettle (v): make anxious or worry."
            },
            {
              "id": "4",
              "content": "4. garment",
              "options": ["clothing", "equipment", "criticism", "unplanned action"],
              "correctAnswer": "clothing",
              "explanation": "garment (n): a piece of clothing."
            },
            {
              "id": "5",
              "content": "5. propel",
              "options": ["avoid", "push", "capable", "toughen"],
              "correctAnswer": "push",
              "explanation": "propel (v): push or move somewhere."
            }
          ]
        },
        {
          "id": "sec2_wordlist",
          "title": "Exercise 2: Write a word that is similar in meaning to the underlined part.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "6",
              "content": "1. The meeting of the citizens’ group was prevented from happening by the police.",
              "options": ["suppressed", "warped", "propel", "socialize"],
              "correctAnswer": "suppressed",
              "explanation": "suppress (v): to prevent from happening."
            },
            {
              "id": "7",
              "content": "2. The warm weather had changed the ice sculptures into strange shapes.",
              "options": ["deformed", "propel", "socialize", "suppressed"],
              "correctAnswer": "deformed",
              "explanation": "deform (v): to change from its correct or original shape."
            },
            {
              "id": "8",
              "content": "3. Dad says drinking milk before going to bed helps with a disorder that makes it hard to sleep.",
              "options": ["insomnia", "etiquette", "garments", "freight"],
              "correctAnswer": "insomnia",
              "explanation": "insomnia (n): a condition with difficulty sleeping."
            },
            {
              "id": "9",
              "content": "4. After I saw the scary movie, walking home in the darkness upset me.",
              "options": ["unsettled", "obsessed", "propel", "deformed"],
              "correctAnswer": "unsettled",
              "explanation": "unsettle (v): to make anxious or upset."
            },
            {
              "id": "10",
              "content": "5. After school, I’m likely to go visit my friend at her house.",
              "options": ["liable", "intuitive", "exclusive", "congested"],
              "correctAnswer": "liable",
              "explanation": "liable (adj): very likely to happen."
            },
            {
              "id": "11",
              "content": "6. Dylan believed it to be his special right to be treated as superior to all the others.",
              "options": ["privilege", "etiquette", "premium", "garment"],
              "correctAnswer": "privilege",
              "explanation": "privilege (n): a special right given to a person or group."
            },
            {
              "id": "12",
              "content": "7. A gust of wind blew her scarf over the edge of the boat while she was sailing.",
              "options": ["overboard", "tram", "courier", "freight"],
              "correctAnswer": "overboard",
              "explanation": "overboard (adv): over the side of a boat."
            },
            {
              "id": "13",
              "content": "8. He didn’t know what the proper set of rules about being polite was for returning a gift.",
              "options": ["etiquette", "privilege", "premium", "garment"],
              "correctAnswer": "etiquette",
              "explanation": "etiquette (n): the rules about how to be polite."
            },
            {
              "id": "14",
              "content": "9. The train was full of clothes that were to be sold overseas.",
              "options": ["garments", "privilege", "premium", "etiquette"],
              "correctAnswer": "garments",
              "explanation": "garments (n): pieces of clothing."
            },
            {
              "id": "15",
              "content": "10. The wax candle twisted and formed a different shape because it was left in the sun.",
              "options": ["warped", "suppressed", "socialized", "obsessed"],
              "correctAnswer": "warped",
              "explanation": "warp (v): to become bent into the wrong shape."
            }
          ]
        },
        {
          "id": "sec3_wordlist",
          "title": "Exercise 3: Fill in the blanks with the correct words from the word bank.",
          "content": "Word Bank: congested, exclusive, suppress, premium, etiquette, courier, socialize, obsessed, warp, tram",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "16",
              "content": "1. The club was very _____ and didn’t have many members.",
              "options": ["exclusive", "congested", "obsessed", "tram"],
              "correctAnswer": "exclusive",
              "explanation": "exclusive (adj): only for rich people, selective."
            },
            {
              "id": "17",
              "content": "2. The members had to pay a _____ just to join.",
              "options": ["premium", "etiquette", "courier", "tram"],
              "correctAnswer": "premium",
              "explanation": "premium (n): a payment higher than average."
            },
            {
              "id": "18",
              "content": "3. My mother is _____ with making sure we impress our guests.",
              "options": ["obsessed", "exclusive", "congested", "socialize"],
              "correctAnswer": "obsessed",
              "explanation": "obsess (v): to think about all the time."
            },
            {
              "id": "19",
              "content": "4. For example, she makes sure our _____ is perfect.",
              "options": ["etiquette", "premium", "courier", "tram"],
              "correctAnswer": "etiquette",
              "explanation": "etiquette (n): the group of rules about how to be polite."
            },
            {
              "id": "20",
              "content": "5. I stepped onto the _____ and couldn’t find a seat right away.",
              "options": ["tram", "courier", "premium", "etiquette"],
              "correctAnswer": "tram",
              "explanation": "tram (n): a vehicle like a streetcar."
            },
            {
              "id": "21",
              "content": "6. Finally, I made my way through the _____ aisle and sat down.",
              "options": ["congested", "exclusive", "obsessed", "socialize"],
              "correctAnswer": "congested",
              "explanation": "congested (adj): full or blocked."
            },
            {
              "id": "22",
              "content": "7. Hannah worked as a _____ for an advertising company.",
              "options": ["courier", "tram", "premium", "etiquette"],
              "correctAnswer": "courier",
              "explanation": "courier (n): someone who delivers mail or packages."
            },
            {
              "id": "23",
              "content": "8. Between making deliveries, she liked to _____ with the employees.",
              "options": ["socialize", "warp", "suppress", "obsessed"],
              "correctAnswer": "socialize",
              "explanation": "socialize (v): to have a good time with people."
            },
            {
              "id": "24",
              "content": "9. The glue couldn’t _____ the water from leaking from the pipes.",
              "options": ["suppress", "warp", "socialize", "obsessed"],
              "correctAnswer": "suppress",
              "explanation": "suppress (v): to prevent from happening."
            },
            {
              "id": "25",
              "content": "10. Since I didn’t clean it up right away, it caused the wooden floor to _____.",
              "options": ["warp", "suppress", "socialize", "obsessed"],
              "correctAnswer": "warp",
              "explanation": "warp (v): to become bent into the wrong shape."
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
              "content": "1. Allie could always count on her *intuitive* powers to know where her cat was.",
              "options": ["I", "C"],
              "correctAnswer": "C",
              "explanation": "Intuitive means knowing something without proof."
            },
            {
              "id": "27",
              "content": "2. The weatherman said it was *liable* to rain over the entire weekend, so we decided to go for a picnic on Saturday.",
              "options": ["I", "C"],
              "correctAnswer": "I",
              "explanation": "If it is liable to rain, going for a picnic is a bad idea."
            },
            {
              "id": "28",
              "content": "3. Jared couldn’t stop *obsessing* about his grade. When his teacher returned his test, he forgot about it immediately.",
              "options": ["I", "C"],
              "correctAnswer": "I",
              "explanation": "Obsessing means to think about it all the time, which contradicts forgetting it immediately."
            },
            {
              "id": "29",
              "content": "4. Maxine suffers from *insomnia*. She has seen several doctors, but none have helped her get any more sleep.",
              "options": ["I", "C"],
              "correctAnswer": "C",
              "explanation": "Insomnia is difficulty sleeping."
            },
            {
              "id": "30",
              "content": "5. Walter didn’t know what to wear to the concert. All of his best *garments* needed to be washed.",
              "options": ["I", "C"],
              "correctAnswer": "C",
              "explanation": "Garments are clothes."
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": story,
      "imageUrl": "/unit8_vol6_story.png",
      "sections": [
        {
          "id": "sec5_reading",
          "title": "Part A: Mark each statement T for true or F for false.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "31",
              "content": "1. Kevin took a taxi to the ship.",
              "options": ["F", "T"],
              "correctAnswer": "F",
              "explanation": "F: Kevin took a tram to the ship."
            },
            {
              "id": "32",
              "content": "2. In order to get the privilege to be in the exclusive section, one had to wear fancy garments.",
              "options": ["F", "T"],
              "correctAnswer": "F",
              "explanation": "F: In order to get the privilege to be in the exclusive section, one had to pay a premium."
            },
            {
              "id": "33",
              "content": "3. Kevin didn’t socialize with the people in the exclusive section because it was too congested.",
              "options": ["F", "T"],
              "correctAnswer": "F",
              "explanation": "F: Kevin didn’t socialize with the people in the exclusive section because it was against etiquette."
            },
            {
              "id": "34",
              "content": "4. Kevin could not sleep because he had insomnia.",
              "options": ["F", "T"],
              "correctAnswer": "T",
              "explanation": "T: That night, he suffered from insomnia."
            },
            {
              "id": "35",
              "content": "5. If Kevin hadn’t seen the iceberg, the ship was liable to have crashed into it.",
              "options": ["F", "T"],
              "correctAnswer": "T",
              "explanation": "T: Without his help, they would have crashed."
            }
          ]
        },
        {
          "id": "sec6_reading",
          "title": "Part B: Answer the questions.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "36",
              "content": "1. Describe Kevin’s room next to the freight section.",
              "options": ["His room smelled bad, and the floorboards were warped and deformed in some areas.", "It was exclusive with fancy garments.", "It was full of mail and packages.", "It was a tram."],
              "correctAnswer": "His room smelled bad, and the floorboards were warped and deformed in some areas.",
              "explanation": "His room smelled bad, and the floorboards were warped and deformed in some areas."
            },
            {
              "id": "37",
              "content": "2. While he was on the ship, what could Kevin hear humming?",
              "options": ["Kevin could hear the humming of the motors as he was on the ship.", "He heard people socializing.", "He heard an iceberg.", "He heard the tram."],
              "correctAnswer": "Kevin could hear the humming of the motors as he was on the ship.",
              "explanation": "He could also hear the motor humming as it waited to propel the ship forward."
            },
            {
              "id": "38",
              "content": "3. What did Kevin see when he looked overboard the first time?",
              "options": ["Kevin didn’t see anything when he looked overboard the first time.", "He saw an iceberg.", "He saw another ship.", "He saw a fish."],
              "correctAnswer": "Kevin didn’t see anything when he looked overboard the first time.",
              "explanation": "He looked overboard, but it seemed that everything was all right."
            },
            {
              "id": "39",
              "content": "4. What did the captain do when he heard the news about the iceberg?",
              "options": ["The captain instructed the crew to change the ship’s direction.", "He ignored Kevin.", "He fell overboard.", "He paid a premium."],
              "correctAnswer": "The captain instructed the crew to change the ship’s direction.",
              "explanation": "The captain saw it and immediately instructed the crew to change the ship’s direction."
            },
            {
              "id": "40",
              "content": "5. What did Kevin learn at the end of the story?",
              "options": ["Kevin learned to always trust his intuitive sense.", "He learned proper etiquette.", "He learned how to sleep with insomnia.", "He learned how to propel a ship."],
              "correctAnswer": "Kevin learned to always trust his intuitive sense.",
              "explanation": "Now he knew to always trust his intuitive sense."
            }
          ]
        }
      ]
    }
  ]
}

with open("public/unit8_vol6.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
print("build_unit8.py executed successfully!")
