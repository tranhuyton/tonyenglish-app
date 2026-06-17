import json

words = [
    {"word": "alternate", "phonetic": "[ɔ:ltərneit]", "type": "v.", "definition": "To alternate means to switch back and forth between two things.", "example": "The best exercise alternates muscle and heart strengthening."},
    {"word": "apologetic", "phonetic": "[əpɑ:lədʒetik]", "type": "adj.", "definition": "If someone is apologetic, they are sorry about something.", "example": "The boy felt apologetic after losing his sister's favorite toy."},
    {"word": "benign", "phonetic": "[binain]", "type": "adj.", "definition": "If something or someone is benign, they do not hurt anyone.", "example": "Many spiders look scary, but most are actually benign."},
    {"word": "char", "phonetic": "[tʃɑ:r]", "type": "v.", "definition": "To char means to burn something so that it turns black.", "example": "While Frank went inside to get the mustard, he accidentally charred the hotdogs."},
    {"word": "clarify", "phonetic": "[klærəfai]", "type": "v.", "definition": "To clarify means to make something easier to understand by explaining it.", "example": "Drew tried to clarify all the functions of Michelle's new computer."},
    {"word": "distress", "phonetic": "[distres]", "type": "n.", "definition": "Distress is the feeling of being upset or worried.", "example": "Failing a class caused the student a lot of distress."},
    {"word": "dogged", "phonetic": "[dɔ:gid]", "type": "adj.", "definition": "When someone's actions are dogged, they try hard to continue something.", "example": "Her dad bought her a new jacket after her dogged requests for one."},
    {"word": "ensue", "phonetic": "[insu:]", "type": "v.", "definition": "To ensue means to happen after something.", "example": "After a few minutes of lightening, thunder ensued."},
    {"word": "gasp", "phonetic": "[gæsp]", "type": "v.", "definition": "To gasp means to make a noise by quickly breathing in when surprised.", "example": "John always gasps when watching a scary movie."},
    {"word": "negotiate", "phonetic": "[nigouʃieit]", "type": "v.", "definition": "To negotiate means to try to make an agreement through discussion.", "example": "Mario and Joe took a long time negotiating the contract between the companies."},
    {"word": "overdose", "phonetic": "[ouvərdous]", "type": "n.", "definition": "An overdose is an instance of taking or having too much of something.", "example": "John's skin was burned from an overdose of sunshine."},
    {"word": "persuasion", "phonetic": "[pərswelʒən]", "type": "n.", "definition": "Persuasion is the act of making someone do or believe something.", "example": "The persuasion of his argument convinced the customer to buy the laptop."},
    {"word": "relay", "phonetic": "[ri:lei]", "type": "n.", "definition": "A relay is a race in which teams of runners or swimmers race against each other.", "example": "Jerry was the fastest on his team, so he ran the last part of the relay."},
    {"word": "reluctance", "phonetic": "[rilʌktəns]", "type": "n.", "definition": "Reluctance is a feeling of not wanting to do something.", "example": "Jesse took out the trash with great reluctance."},
    {"word": "restate", "phonetic": "[ri:steit]", "type": "v.", "definition": "To restate something means to say it again or in a different way.", "example": "Mrs. Jones restated the test question to the class."},
    {"word": "sesame", "phonetic": "[sesəmi]", "type": "n.", "definition": "Sesame is an herb that is grown for its small seeds and its oil.", "example": "I used the buns with the sesame seeds on them."},
    {"word": "sip", "phonetic": "[sip]", "type": "v.", "definition": "To sip something means to drink a small amount at a time.", "example": "Liza relaxed on the beach, sipping fruit juice through a straw."},
    {"word": "verge", "phonetic": "[və:rdʒ]", "type": "n.", "definition": "The verge is the point at which something is about to happen.", "example": "Joan was on the verge of leaving her house when the phone rang."},
    {"word": "wary", "phonetic": "[wɛəri]", "type": "adj.", "definition": "If someone is wary, they are cautious or mistrusting.", "example": "She was wary of going to school because she hadn't done her homework."},
    {"word": "waver", "phonetic": "[weivər]", "type": "v.", "definition": "To waver is to be unable to decide between two choices.", "example": "I wavered between eating the apple or the cake for a snack."}
]

html_words = ""
for w in words:
    html_words += f'<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">{w["word"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">{w["phonetic"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">{w["type"]}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">{w["definition"]}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ {w["example"]}</div></div></div>'

part1_html = f'<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit5_vol6_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit5_vol6_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">{html_words}</div></div></div>'

part2_html = '<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">A Bet</h1><p style="margin-bottom: 1rem;">Russell finished running a <b>relay</b> and joined his friend Becky in the cafeteria. He asked, "What\'s for lunch?"</p><p style="margin-bottom: 1rem;">"<b>Sesame</b> chicken. It\'s OK, except the meat\'s <b>charred</b>. Oh, and watch out for the chili peppers," Becky said.</p><p style="margin-bottom: 1rem;">"Chilies don\'t bother me!" said Russell.</p><p style="margin-bottom: 1rem;">"My stepmother says you should be careful with them," replied Becky.</p><p style="margin-bottom: 1rem;">An argument <b>ensued</b> about eating chilies. "Chilies aren\'t so bad. I bet I can take more bites of this chili than you," Russell said.</p><p style="margin-bottom: 1rem;">Becky was <b>wary</b> of eating the pepper. Despite her <b>reluctance</b>, she didn\'t want to say no to the bet. She <b>wavered</b> about whether to do it or not. She <b>negotiated</b> the details. "What will the winner get?" she asked.</p><p style="margin-bottom: 1rem;">"The loser has to carry the winner\'s books for a year! I\'ll even let you go first."</p><p style="margin-bottom: 1rem;">Becky replied, "Fine, but to <b>clarify</b>, you\'ll carry my books for the entire school year, right?"</p><p style="margin-bottom: 1rem;">Russell <b>restated</b> the agreement, "That\'s right—I\'ll carry your books all year if you win—which you won\'t!"</p><p style="margin-bottom: 1rem;">His <b>dogged</b> <b>persuasion</b> convinced her. The chili looked <b>benign</b>, but Becky knew it could cause a lot of pain. She bit the bottom of the pepper. Surprisingly, she felt nothing.</p><p style="margin-bottom: 1rem;">"My turn," said Russell. He bit the middle of the chili. Immediately, he seemed to be in <b>distress</b>. He <b>gasped</b> and his face <b>alternated</b> between brave and pained expressions. He experienced an <b>overdose</b> of spice. He was on the <b>verge</b> of tears and finally let out a horrible cry.</p><p style="margin-bottom: 1rem;">"Take this," said Becky, handing him her drink.</p><p style="margin-bottom: 1rem;">"That was awful!" he said, continuing to <b>sip</b> from the glass.</p><p style="margin-bottom: 1rem;">That night, Becky researched chilies. The next day she said in an <b>apologetic</b> voice, "I read that the hot part of chilies is in the middle, where the seeds are. I\'m sorry—I feel like I cheated by going first."</p><p style="margin-bottom: 1rem;">Russell was relieved, not only did he learn something new about chilies, but he learned that Becky was a good friend.</p></div>'

data = {
    "basicInfo": {
        "skill": "Standard-Reading",
        "title": "Unit 5: Volume 6",
        "category": "exercise",
        "timeLimit": 0
    },
    "parts": [
        {
            "id": "part1",
            "title": "Word List",
            "content": part1_html,
            "sections": [
                {
                    "id": "sec1_wordlist",
                    "title": "Exercise 1: Choose the answer that best fits the question.",
                    "content": "",
                    "questionType": "Trắc nghiệm",
                    "questions": [
                        {
                            "id": "1",
                            "content": "1. An overdose of something is __________.",
                            "options": ["expensive", "too much", "not true", "not enough"],
                            "correctAnswer": "too much",
                            "explanation": "overdose (n): too much."
                        },
                        {
                            "id": "2",
                            "content": "2. What might cause someone to gasp?",
                            "options": ["Falling asleep", "Getting a surprise party", "Eating too much", "Laying on a bed"],
                            "correctAnswer": "Getting a surprise party",
                            "explanation": "gasp (v): to make a noise by quickly breathing in when surprised."
                        },
                        {
                            "id": "3",
                            "content": "3. What is something that can be sipped?",
                            "options": ["A plate of rice", "A bowl of fruit", "A glass of soda", "A piece of chicken"],
                            "correctAnswer": "A glass of soda",
                            "explanation": "sip (v): drink a small amount at a time."
                        },
                        {
                            "id": "4",
                            "content": "4. If you knew that a snake was benign, you would probably feel like this:",
                            "options": ["Fine", "Scared", "Angry", "Hungry"],
                            "correctAnswer": "Fine",
                            "explanation": "benign (adj): do not hurt anyone."
                        },
                        {
                            "id": "5",
                            "content": "5. She felt apologetic about __________.",
                            "options": ["calling her friend back", "walking home alone", "forgetting her friend's birthday", "giving to charity"],
                            "correctAnswer": "forgetting her friend's birthday",
                            "explanation": "apologetic (adj): sorry about something."
                        },
                        {
                            "id": "6",
                            "content": "6. If people are negotiating, what are they doing?",
                            "options": ["Deciding on something", "Arguing about a silly topic", "Meeting for the first time", "Going on a date"],
                            "correctAnswer": "Deciding on something",
                            "explanation": "negotiate (v): try to make an agreement through discussion."
                        },
                        {
                            "id": "7",
                            "content": "7. What does charred meat look like?",
                            "options": ["It is raw and not cooked enough.", "It is cooked perfectly.", "It is black on the outside.", "It is red on the outside."],
                            "correctAnswer": "It is black on the outside.",
                            "explanation": "char (v): burn something so that it turns black."
                        },
                        {
                            "id": "8",
                            "content": "8. If someone does something with reluctance, how do they feel?",
                            "options": ["Excited", "Unwilling", "Frightened", "Nervous"],
                            "correctAnswer": "Unwilling",
                            "explanation": "reluctance (n): feeling of not wanting to do something."
                        },
                        {
                            "id": "9",
                            "content": "9. What might ensue after someone has misplaced a lot of money?",
                            "options": ["A worried search", "A visit from the doctor", "The arrival of a friend", "A party"],
                            "correctAnswer": "A worried search",
                            "explanation": "ensue (v): to happen after something."
                        },
                        {
                            "id": "10",
                            "content": "10. What might cause a teacher distress?",
                            "options": ["All the students doing their homework", "Her students always arriving on time", "Her students not coming to class", "Her students all passing an exam"],
                            "correctAnswer": "Her students not coming to class",
                            "explanation": "distress (n): feeling of being upset or worried."
                        }
                    ]
                },
                {
                    "id": "sec2_wordlist",
                    "title": "Exercise 2: Choose the one that is similar in meaning to the given word",
                    "content": "",
                    "questionType": "Trắc nghiệm",
                    "questions": [
                        {
                            "id": "11",
                            "content": "1. reluctance",
                            "options": ["loneliness", "hesitance", "dependence"],
                            "correctAnswer": "hesitance",
                            "explanation": "reluctance is similar to hesitance."
                        },
                        {
                            "id": "12",
                            "content": "2. apologetic",
                            "options": ["unsure", "lucky", "sorry"],
                            "correctAnswer": "sorry",
                            "explanation": "apologetic is similar to sorry."
                        },
                        {
                            "id": "13",
                            "content": "3. char",
                            "options": ["burn", "cook", "on fire"],
                            "correctAnswer": "burn",
                            "explanation": "char means to burn."
                        },
                        {
                            "id": "14",
                            "content": "4. relay",
                            "options": ["plate", "race", "desert"],
                            "correctAnswer": "race",
                            "explanation": "a relay is a race."
                        },
                        {
                            "id": "15",
                            "content": "5. persuasion",
                            "options": ["talent", "influence", "ripeness"],
                            "correctAnswer": "influence",
                            "explanation": "persuasion is related to influence."
                        },
                        {
                            "id": "16",
                            "content": "6. restate",
                            "options": ["decide", "discuss", "lose", "summarize"],
                            "correctAnswer": "summarize",
                            "explanation": "restate can be similar to summarize."
                        },
                        {
                            "id": "17",
                            "content": "7. gasp",
                            "options": ["breathe", "announce", "mean", "drink"],
                            "correctAnswer": "breathe",
                            "explanation": "gasp is related to breathing."
                        },
                        {
                            "id": "18",
                            "content": "8. negotiate",
                            "options": ["decide", "discuss", "fair", "ask"],
                            "correctAnswer": "discuss",
                            "explanation": "negotiate means to discuss for an agreement."
                        },
                        {
                            "id": "19",
                            "content": "9. sesame",
                            "options": ["container", "food", "an animal", "shell"],
                            "correctAnswer": "food",
                            "explanation": "sesame is a food item."
                        },
                        {
                            "id": "20",
                            "content": "10. verge",
                            "options": ["edge", "done", "plan", "last"],
                            "correctAnswer": "edge",
                            "explanation": "verge means edge or border."
                        }
                    ]
                },
                {
                    "id": "sec3_wordlist",
                    "title": "Exercise 3: Choose the one that is opposite in meaning to the given word",
                    "content": "",
                    "questionType": "Trắc nghiệm",
                    "questions": [
                        {
                            "id": "21",
                            "content": "1. benign",
                            "options": ["quick", "painful", "harmful", "warm"],
                            "correctAnswer": "harmful",
                            "explanation": "benign means harmless, so harmful is the opposite."
                        },
                        {
                            "id": "22",
                            "content": "2. dogged",
                            "options": ["working", "arrival", "flexible", "serious"],
                            "correctAnswer": "flexible",
                            "explanation": "dogged means persistent, so flexible is the opposite."
                        },
                        {
                            "id": "23",
                            "content": "3. clarify",
                            "options": ["confuse", "clean", "do again", "order"],
                            "correctAnswer": "confuse",
                            "explanation": "clarify means to make clear, so confuse is the opposite."
                        },
                        {
                            "id": "24",
                            "content": "4. waver",
                            "options": ["river", "determine", "chili", "solid"],
                            "correctAnswer": "determine",
                            "explanation": "waver means to be undecided, so determine is the opposite."
                        },
                        {
                            "id": "25",
                            "content": "5. distress",
                            "options": ["thoughtful", "reasonable", "peace", "surprising"],
                            "correctAnswer": "peace",
                            "explanation": "distress means worry, so peace is the opposite."
                        },
                        {
                            "id": "26",
                            "content": "6. sip",
                            "options": ["gulp", "laugh", "provide", "keep"],
                            "correctAnswer": "gulp",
                            "explanation": "sip means to drink a little, gulp means to drink a lot."
                        },
                        {
                            "id": "27",
                            "content": "7. alternate",
                            "options": ["divide", "move", "travel", "continue"],
                            "correctAnswer": "continue",
                            "explanation": "alternate means to switch back and forth, continue is the opposite."
                        },
                        {
                            "id": "28",
                            "content": "8. overdose",
                            "options": ["lack", "mixture", "teacher", "cottage"],
                            "correctAnswer": "lack",
                            "explanation": "overdose means too much, lack means too little."
                        },
                        {
                            "id": "29",
                            "content": "9. wary",
                            "options": ["tired", "mad", "small", "trusting"],
                            "correctAnswer": "trusting",
                            "explanation": "wary means cautious/distrusting, trusting is the opposite."
                        },
                        {
                            "id": "30",
                            "content": "10. ensue",
                            "options": ["come before", "safe", "punish", "ask about"],
                            "correctAnswer": "come before",
                            "explanation": "ensue means to happen after, come before is the opposite."
                        }
                    ]
                }
            ]
        },
        {
            "id": "part2",
            "title": "Comprehensive Reading",
            "content": part2_html,
            "imageUrl": "/unit5_vol6_story.png",
            "sections": [
                {
                    "id": "sec4",
                    "title": "Part A: Mark each statement T for true or F for false.",
                    "content": "",
                    "questionType": "Trắc nghiệm",
                    "questions": [
                        {
                            "id": "31",
                            "content": "1. Becky was having charred sesame chicken for lunch.",
                            "options": ["F", "T"],
                            "correctAnswer": "T",
                            "explanation": "T"
                        },
                        {
                            "id": "32",
                            "content": "2. The argument ensued because Becky wavered about whether to run the relay.",
                            "options": ["F", "T"],
                            "correctAnswer": "F",
                            "explanation": "F: The argument ensued about eating chilies."
                        },
                        {
                            "id": "33",
                            "content": "3. After Russell and Becky negotiated the bet, they decided that whoever lost would carry the winner's books for a year.",
                            "options": ["F", "T"],
                            "correctAnswer": "T",
                            "explanation": "T"
                        },
                        {
                            "id": "34",
                            "content": "4. Russell was wary about eating the pepper even if it looked benign.",
                            "options": ["F", "T"],
                            "correctAnswer": "F",
                            "explanation": "F: Becky was wary about eating the pepper even if it looked benign."
                        },
                        {
                            "id": "35",
                            "content": "5. Becky was apologetic because of her choice to take the first bite of the pepper.",
                            "options": ["F", "T"],
                            "correctAnswer": "F",
                            "explanation": "F: Becky was apologetic because she felt like she cheated by taking the first bite."
                        }
                    ]
                },
                {
                    "id": "sec5",
                    "title": "Part B: Answer the questions.",
                    "content": "",
                    "questionType": "Trắc nghiệm",
                    "questions": [
                        {
                            "id": "36",
                            "content": "1. Why did Becky take the bet in spite of her reluctance?",
                            "options": ["Becky took the bet because of Russell's dogged persuasion.", "She wanted to win.", "She liked chilies.", "She was hungry."],
                            "correctAnswer": "Becky took the bet because of Russell's dogged persuasion.",
                            "explanation": "Becky took the bet because of Russell's dogged persuasion."
                        },
                        {
                            "id": "37",
                            "content": "2. Why did Russell have to restate the terms of the bet?",
                            "options": ["Russell had to restate the terms to clarify for Becky.", "He forgot what he said.", "He wanted to trick her.", "He changed his mind."],
                            "correctAnswer": "Russell had to restate the terms to clarify for Becky.",
                            "explanation": "Russell had to restate the terms to clarify for Becky."
                        },
                        {
                            "id": "38",
                            "content": "3. How did Becky know that Russell was in distress and had an overdose of spice after he ate the pepper?",
                            "options": ["He gasped, alternated between pained and brave, and was on the verge of tears.", "He said he was fine.", "He ate another pepper.", "He ran away."],
                            "correctAnswer": "He gasped, alternated between pained and brave, and was on the verge of tears.",
                            "explanation": "Becky knew Russell was in distress because he gasped, then his expressions alternated between pained and brave, and he was on the verge of tears."
                        },
                        {
                            "id": "39",
                            "content": "4. Who warned Becky about chilies?",
                            "options": ["Becky's stepmother warned her to be careful with chilies.", "Russell.", "Her friend.", "The lunch lady."],
                            "correctAnswer": "Becky's stepmother warned her to be careful with chilies.",
                            "explanation": "Becky's stepmother warned her to be careful with chilies."
                        },
                        {
                            "id": "40",
                            "content": "5. What did Russell do after he ate the chili?",
                            "options": ["Russell sipped from the beverage.", "He ate another one.", "He cried.", "He threw the chili away."],
                            "correctAnswer": "Russell sipped from the beverage.",
                            "explanation": "Russell sipped from the beverage."
                        }
                    ]
                }
            ]
        }
    ]
}

with open("c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/public/unit5_vol6.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

