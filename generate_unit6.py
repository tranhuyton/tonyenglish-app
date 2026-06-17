import json

words = [
    {"word": "abroad", "phonetic": "[əbrɔ́ːd]", "type": "adv.", "def": "If someone goes or travels abroad, they go to another country.", "ex": "My brother wants to go abroad next year."},
    {"word": "anger", "phonetic": "[ǽŋgər]", "type": "v.", "def": "To anger someone is to make them mad.", "ex": "It angers me when people are rude."},
    {"word": "bride", "phonetic": "[braid]", "type": "n.", "def": "A bride is a woman who is getting married or has just gotten married.", "ex": "The bride looked beautiful in her wedding dress."},
    {"word": "brief", "phonetic": "[briːf]", "type": "adj.", "def": "If something is brief, it only lasts for a short time.", "ex": "The meeting this afternoon was very brief."},
    {"word": "chase", "phonetic": "[tʃeis]", "type": "v.", "def": "To chase someone or something is to follow them in order to catch them.", "ex": "I was chased by an angry native."},
    {"word": "disappoint", "phonetic": "[dìsəpɔ́int]", "type": "v.", "def": "To disappoint is to make one feel sad or unsatisfied.", "ex": "I do not want to disappoint my family, so I try to do well at school."},
    {"word": "dive", "phonetic": "[daiv]", "type": "v.", "def": "To dive is to jump into water.", "ex": "I will dive into the lake once we get there."},
    {"word": "exchange", "phonetic": "[ikstʃéindʒ]", "type": "v.", "def": "To exchange means to give something for another thing in return.", "ex": "I exchanged my foreign money for American dollars."},
    {"word": "favor", "phonetic": "[féivər]", "type": "n.", "def": "A favor is something you do for someone to help them.", "ex": "Can you do me a favor and turn off the lights?"},
    {"word": "fee", "phonetic": "[fiː]", "type": "n.", "def": "A fee is an amount of money that a person or company asks for a service.", "ex": "I had to pay an hourly fee to speak with my lawyer."},
    {"word": "forever", "phonetic": "[fərévər]", "type": "adv.", "def": "If something lasts forever, it means it lasts for all time.", "ex": "The young couple promised that they would love each other forever."},
    {"word": "guy", "phonetic": "[gai]", "type": "n.", "def": "A guy is an informal way to call a man.", "ex": "The guy at the flower shop was really helpful today."},
    {"word": "lovely", "phonetic": "[lʌ́vli]", "type": "adj.", "def": "If people or things are lovely, they are good-looking or beautiful.", "ex": "The trees look lovely in the fall."},
    {"word": "mood", "phonetic": "[muːd]", "type": "n.", "def": "A mood is the way someone is feeling.", "ex": "I am in a good mood because I did well on my math test."},
    {"word": "palace", "phonetic": "[pǽlis]", "type": "n.", "def": "A palace is a very large building. It is often the home of a royal family.", "ex": "The king and queen live in a beautiful palace."},
    {"word": "permit", "phonetic": "[pərmít]", "type": "v.", "def": "To permit something is to let someone do it.", "ex": "I was sick, so my mother permitted me to stay home from school."},
    {"word": "protest", "phonetic": "[próutest]", "type": "v.", "def": "To protest something is to argue about it with someone.", "ex": "The people protested the decision of the president."},
    {"word": "sculpture", "phonetic": "[skʌ́lptʃər]", "type": "n.", "def": "A sculpture is a piece of art that is made from wood, clay, or stone.", "ex": "We saw an old sculpture of Buddha at the museum."},
    {"word": "tribe", "phonetic": "[traib]", "type": "n.", "def": "A tribe is a group of people who live in the same culture.", "ex": "There’s a small tribe of people who live in the mountains of Spain."},
    {"word": "youth", "phonetic": "[juːθ]", "type": "n.", "def": "Youth is a time in people’s lives when they are young.", "ex": "My mother wanted to be a nurse in her youth."}
]

# Generate part 1 HTML
html_part1 = '<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit6_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit6_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">'

for w in words:
    html_part1 += f'<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">{w["word"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">{w["phonetic"]}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">{w["type"]}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">{w["def"]}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ {w["ex"]}</div></div></div>'

html_part1 += '</div></div></div>'

# Generate part 2 HTML
story_title = "The Frog Prince"
paragraphs = [
    "A <b>lovely</b> princess sat by the pool and played with a <b>sculpture</b> of a bear. Suddenly, she dropped it, and it rolled away. She <b>chased</b> it, but it fell into the water. She began to cry. A large, ugly frog asked, “Why are you crying?” After the princess told him, the frog said, “I can get the <b>sculpture</b>. What will you give me in <b>exchange</b> for the <b>favor</b>?”",
    "“I can pay you a <b>fee</b> in gold,” she said.",
    "But the frog <b>protested</b>. “I want to sleep in your bed, and you must kiss me in the morning.”",
    "“He’d <b>dive</b> without water. So, I don’t have to keep my promise,” she thought.",
    "The frog dove for a <b>brief</b> moment and got the <b>sculpture</b>. Then the princess ran away with it. Later, the frog went to the <b>palace</b>. The king told her to keep her promise. This put the princess in a bad <b>mood</b>. She <b>permitted</b> the frog to sleep on her pillow. In the morning, she gave him a kiss.",
    "Suddenly, he turned into a <b>guy</b>. He said, “I’m from a kingdom <b>abroad</b>. In my <b>youth</b>, I <b>angered</b> a <b>tribe</b> of cruel witches, who turned me into a frog.”",
    "The princess asked him, “Can I be your <b>bride</b> and stay with you <b>forever</b>?” But the prince said, “No. You <b>disappointed</b> me. You didn’t keep your promise.”"
]

html_part2 = f'<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">{story_title}</h1>'
for p in paragraphs:
    html_part2 += f'<p style="margin-bottom: 1rem;">{p}</p>'
html_part2 += '</div>'

data = {
  "basicInfo": {
    "skill": "Standard-Reading",
    "title": "Unit 6",
    "category": "exercise",
    "timeLimit": 0
  },
  "parts": [
    {
      "id": "part1",
      "title": "Word List",
      "content": html_part1,
      "sections": [
        {
          "id": "sec1_wordlist",
          "title": "Part A: Choose the right word for the given definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u6_p1_1",
              "content": "1. to make mad",
              "options": ["dive", "anger", "mood", "fee"],
              "correctAnswer": "anger",
              "explanation": "anger nghĩa là chọc tức (to make mad)."
            },
            {
              "id": "u6_p1_2",
              "content": "2. to get something and give something",
              "options": ["lovely", "palace", "exchange", "tribe"],
              "correctAnswer": "exchange",
              "explanation": "exchange nghĩa là trao đổi (to get something and give something)."
            },
            {
              "id": "u6_p1_3",
              "content": "3. very short",
              "options": ["brief", "forever", "tribe", "guy"],
              "correctAnswer": "brief",
              "explanation": "brief nghĩa là ngắn gọn (very short)."
            },
            {
              "id": "u6_p1_4",
              "content": "4. a woman who is getting married",
              "options": ["guy", "disappoint", "bride", "permit"],
              "correctAnswer": "bride",
              "explanation": "bride nghĩa là cô dâu (a woman who is getting married)."
            },
            {
              "id": "u6_p1_5",
              "content": "5. a time of being young",
              "options": ["chase", "favor", "protest", "youth"],
              "correctAnswer": "youth",
              "explanation": "youth nghĩa là tuổi trẻ (a time of being young)."
            }
          ]
        },
        {
          "id": "sec2_wordlist",
          "title": "Part B: Check the one that suits the blank naturally.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u6_p2_1",
              "content": "1. When my sister lost my best sweater, ________________.",
              "options": ["it angered me", "I was in a good mood"],
              "correctAnswer": "it angered me",
              "explanation": "Khi chị làm mất áo len của tôi, điều đó làm tôi tức giận."
            },
            {
              "id": "u6_p2_2",
              "content": "2. I don’t have much time, so ________________.",
              "options": ["keep your story brief", "you can talk forever"],
              "correctAnswer": "keep your story brief",
              "explanation": "Vì không có nhiều thời gian nên hãy kể ngắn gọn (brief)."
            },
            {
              "id": "u6_p2_3",
              "content": "3. I am learning how to play the guitar, so ________________.",
              "options": ["let’s get some coffee", "I’ll be able to play you a song soon"],
              "correctAnswer": "I’ll be able to play you a song soon",
              "explanation": "Học chơi guitar nên sẽ sớm chơi được một bài hát."
            },
            {
              "id": "u6_p2_4",
              "content": "4. She needed help, so ________________.",
              "options": ["she asked me for a favor", "she chased my dog"],
              "correctAnswer": "she asked me for a favor",
              "explanation": "Cô ấy cần giúp đỡ nên nhờ tôi một việc (asked me for a favor)."
            },
            {
              "id": "u6_p2_5",
              "content": "5. I wanted to go to the movies, but ________________.",
              "options": ["Jack protested that he wanted to go to the mall", "she exchanged phone numbers with me"],
              "correctAnswer": "Jack protested that he wanted to go to the mall",
              "explanation": "Jack phản đối và muốn đi mall thay vì đi xem phim."
            }
          ]
        },
        {
          "id": "sec3_wordlist",
          "title": "Exercise 2: Choose the word that is similar in meaning to the underlined part.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u6_p3_1",
              "content": "1. Mary’s mother lets her stay up late.",
              "options": ["permits", "protests", "chases", "disappoints"],
              "correctAnswer": "permits",
              "explanation": "lets nghĩa là cho phép, đồng nghĩa với permits."
            },
            {
              "id": "u6_p3_2",
              "content": "2. My friend asked me for some help.",
              "options": ["fee", "palace", "favor", "tribe"],
              "correctAnswer": "favor",
              "explanation": "help trong bối cảnh này đồng nghĩa với ân huệ, sự giúp đỡ (favor)."
            },
            {
              "id": "u6_p3_3",
              "content": "3. The police try to catch the man who took the money.",
              "options": ["anger", "chase", "exchange", "dive"],
              "correctAnswer": "chase",
              "explanation": "try to catch đồng nghĩa với rượt đuổi, truy bắt (chase)."
            },
            {
              "id": "u6_p3_4",
              "content": "4. We saw a royal home while we were in France.",
              "options": ["palace", "sculpture", "tribe", "youth"],
              "correctAnswer": "palace",
              "explanation": "royal home nghĩa là cung điện (palace)."
            },
            {
              "id": "u6_p3_5",
              "content": "5. I will argue his choice for principal.",
              "options": ["permit", "disappoint", "protest", "exchange"],
              "correctAnswer": "protest",
              "explanation": "argue đồng nghĩa với phản đối (protest)."
            },
            {
              "id": "u6_p3_6",
              "content": "6. My friend was made unhappy by her bad grades.",
              "options": ["angered", "disappointed", "lovely", "brief"],
              "correctAnswer": "disappointed",
              "explanation": "made unhappy đồng nghĩa với làm thất vọng (disappointed)."
            },
            {
              "id": "u6_p3_7",
              "content": "7. That man walks his dog past our house every night.",
              "options": ["bride", "guy", "youth", "tribe"],
              "correctAnswer": "guy",
              "explanation": "man là người đàn ông, đồng nghĩa với guy."
            },
            {
              "id": "u6_p3_8",
              "content": "8. I don’t want to live for all time.",
              "options": ["abroad", "brief", "forever", "lovely"],
              "correctAnswer": "forever",
              "explanation": "for all time nghĩa là mãi mãi (forever)."
            },
            {
              "id": "u6_p3_9",
              "content": "9. What was the cost you had to pay to see the concert?",
              "options": ["favor", "fee", "palace", "sculpture"],
              "correctAnswer": "fee",
              "explanation": "cost you had to pay đồng nghĩa với phí (fee)."
            },
            {
              "id": "u6_p3_10",
              "content": "10. My dream is to go to a different country for a year.",
              "options": ["abroad", "forever", "brief", "lovely"],
              "correctAnswer": "abroad",
              "explanation": "to a different country nghĩa là ra nước ngoài (abroad)."
            }
          ]
        }
      ]
    },
    {
      "id": "part2",
      "title": "Comprehensive Reading",
      "content": html_part2,
      "imageUrl": "/unit6_story.png",
      "sections": [
        {
          "id": "sec4_reading",
          "title": "Answer the questions based on the story.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "u6_p4_1",
              "content": "1. What is this story about?",
              "options": [
                "A guy who angers a cruel witch",
                "How people are not always what they seem to be",
                "Why princes should go abroad to find a bride",
                "How to keep promises made in exchange for favors"
              ],
              "correctAnswer": "How people are not always what they seem to be",
              "explanation": "Câu chuyện nói về việc vẻ bề ngoài không phản ánh đúng bản chất bên trong (hoàng tử bị biến thành ếch)."
            },
            {
              "id": "u6_p4_2",
              "content": "2. The frog asked the lovely princess to_____________ .",
              "options": [
                "be in a better mood",
                "kiss him in the morning",
                "dive into the pool to get the ball",
                "permit him to live in the palace"
              ],
              "correctAnswer": "kiss him in the morning",
              "explanation": "Con ếch yêu cầu công chúa hôn mình vào buổi sáng."
            },
            {
              "id": "u6_p4_3",
              "content": "3. What can be assumed from the passage?",
              "options": [
                "The princess was humiliated when the prince didn’t take her back to his kingdom.",
                "The prince and princess were only happy for a brief time.",
                "The frog protested he didn’t need gold because he was rich.",
                "The prince was turned into a frog during his youth."
              ],
              "correctAnswer": "The princess was humiliated when the prince didn’t take her back to his kingdom.",
              "explanation": "Công chúa bị từ chối và cảm thấy bẽ mặt khi hoàng tử không cưới cô."
            },
            {
              "id": "u6_p4_4",
              "content": "4. According to the passage, all of the following are true EXCEPT____________",
              "options": [
                "the king made the princess keep her promise",
                "the princess asked the prince if she could be his bride and stay with him forever",
                "the princess chased her sculpture until it fell into the pool",
                "the frog disappointed the princess by turning into a prince"
              ],
              "correctAnswer": "the frog disappointed the princess by turning into a prince",
              "explanation": "Ếch không hề làm công chúa thất vọng vì biến thành hoàng tử, mà chính công chúa làm hoàng tử thất vọng."
            },
            {
              "id": "u6_p4_5",
              "content": "5. Why did the princess think she would not have to keep her promise?",
              "options": [
                "She thought the frog would die if he leaves the pool.",
                "She didn't have enough gold to pay the fee.",
                "She thought the king would protect her.",
                "She wanted to give the sculpture to someone else."
              ],
              "correctAnswer": "She thought the frog would die if he leaves the pool.",
              "explanation": "Theo bài đọc, công chúa nghĩ ếch sẽ chết nếu rời khỏi nước."
            }
          ]
        }
      ]
    }
  ]
}

with open("c:/Users/Tony/.gemini/antigravity/scratch/tonyenglish-app/unit6.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("unit6.json created successfully.")
