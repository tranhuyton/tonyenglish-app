const fs = require('fs');

// ============== HELPER: Generate Detailed Meanings HTML ==============
function generateMeaningsHtml(words) {
  let html = `<div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">`;
  words.forEach(w => {
    html += `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${w.word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${w.pron}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${w.pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${w.eng} <span style="color:#0ea5e9;">${w.vie}</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${w.ex} <span style="color:#0ea5e9;">${w.exVie}</span></div></div></div>`;
  });
  html += `</div></div>`;
  return html;
}

function wordListContent(unitNum, listNum, words) {
  const imgSrc = `/unit${unitNum}_ielts_word_list_${listNum}.png`;
  return `<p style="display: none;">Word List ${listNum}</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="${imgSrc}" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateMeaningsHtml(words)}</div>`;
}

function readingContent(unitNum, title, paragraphs) {
  const imgSrc = `/unit${unitNum}_ielts_story.png`;
  let html = `<p style="display: none;">Comprehensive Reading</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="${imgSrc}" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">${title}</h1>`;
  paragraphs.forEach(p => {
    html += `<p style="margin-bottom: 1rem;">${p}</p>`;
  });
  html += `</div></div>`;
  return html;
}

// ======================================================================
// ======================== UNIT 5 DATA =================================
// ======================================================================
const u5_wordList1 = [
  { word: "ABC", pos: "n.", pron: "[ˌeɪ biː ˈsiː]", eng: "the basic facts or principles of a subject.", vie: "(khái niệm cơ sở, cơ sở)", ex: "The ABCs of living a happy life.", exVie: "(Những cơ sở của việc sống một cuộc sống hạnh phúc.)" },
  { word: "browse", pos: "v.", pron: "[braʊz]", eng: "to look at or read parts of a book, magazine, etc., casually.", vie: "(đọc lướt qua, xem lướt qua)", ex: "I was browsing around a bookshop.", exVie: "(Tôi đang đi dạo xem lướt qua một hiệu sách.)" },
  { word: "entitle", pos: "v.", pron: "[ɪnˈtaɪtl]", eng: "to give a title to (a book, play, etc.).", vie: "(đặt tên (cuốn sách, vở kịch, v.v.))", ex: "A small, interesting book entitled 'The ABCs of loving yourself'.", exVie: "(Một cuốn sách nhỏ, thú vị có tựa đề 'Những nguyên tắc cơ bản để yêu bản thân'.)" },
  { word: "alphabet", pos: "n.", pron: "[ˈælfəbet]", eng: "a set of letters or symbols in a fixed order.", vie: "(bảng chữ cái)", ex: "Each letter of the alphabet stands for something.", exVie: "(Mỗi chữ cái trong bảng chữ cái tượng trưng cho một điều gì đó.)" },
  { word: "stand for", pos: "phrase", pron: "[stænd fɔːr]", eng: "to represent or mean.", vie: "(là chữ viết tắt của, tượng trưng cho)", ex: "What does this abbreviation stand for?", exVie: "(Từ viết tắt này có nghĩa là gì?)" },
  { word: "motivational", pos: "adj.", pron: "[ˌmoʊtɪˈveɪʃənl]", eng: "designed to promote the desire or willingness to do or achieve something.", vie: "(thúc đẩy)", ex: "A motivational word.", exVie: "(Một từ ngữ mang tính khích lệ, thúc đẩy.)" },
  { word: "guide", pos: "v.", pron: "[ɡaɪd]", eng: "to show or indicate the way to (someone).", vie: "(hướng dẫn)", ex: "Useful to guide our life.", exVie: "(Hữu ích để hướng dẫn cuộc sống của chúng ta.)" },
  { word: "leeway", pos: "n.", pron: "[ˈliːweɪ]", eng: "the amount of freedom to move or act that is available.", vie: "(quyền tự do để ai di chuyển, thay đổi)", ex: "Allowing myself some leeway to adapt.", exVie: "(Cho phép bản thân một chút tự do để thích nghi.)" },
  { word: "adapt", pos: "v.", pron: "[əˈdæpt]", eng: "to make (something) suitable for a new use or purpose; modify.", vie: "(thích nghi)", ex: "Adapt the guidelines.", exVie: "(Sửa đổi các hướng dẫn cho phù hợp.)" },
  { word: "guideline", pos: "n.", pron: "[ˈɡaɪdlaɪn]", eng: "a general rule, principle, or piece of advice.", vie: "(hướng dẫn)", ex: "Adapt the guidelines.", exVie: "(Sửa đổi các hướng dẫn cho phù hợp.)" },
  { word: "go through", pos: "phrasal v.", pron: "[ɡoʊ θruː]", eng: "to examine or search something very carefully.", vie: "(đi hết, hoàn tất)", ex: "Let me go through the alphabet of life.", exVie: "(Hãy để tôi đi qua toàn bộ bảng chữ cái của cuộc sống.)" },
  { word: "acknowledge", pos: "v.", pron: "[əkˈnɑːlɪdʒ]", eng: "to accept or admit the existence or truth of.", vie: "(công nhận)", ex: "Acknowledging or appreciating your value.", exVie: "(Công nhận hoặc trân trọng giá trị của bạn.)" },
  { word: "appreciate", pos: "v.", pron: "[əˈpriːʃieɪt]", eng: "to recognize the full worth of.", vie: "(hiểu với sự thông cảm, đánh giá cao)", ex: "Appreciating your value as a person.", exVie: "(Trân trọng giá trị của bạn như một con người.)" },
  { word: "gifted with", pos: "phrase", pron: "[ˈɡɪftɪd wɪθ]", eng: "having exceptional talent or natural ability.", vie: "(được ban cho)", ex: "Gifted with endowments.", exVie: "(Được ban cho những tài năng thiên bẩm.)" },
  { word: "endowments", pos: "n.", pron: "[ɪnˈdaʊmənts]", eng: "a quality or ability possessed or inherited by someone.", vie: "(tài năng thiên bẩm)", ex: "Gifted with endowments of self-awareness.", exVie: "(Được ban tặng những thiên bẩm về sự tự nhận thức.)" }
];

const u5_wordList2 = [
  { word: "self-awareness", pos: "n.", pron: "[ˌself əˈwernəs]", eng: "conscious knowledge of one's own character, feelings, motives, and desires.", vie: "(sự tự ý thức)", ex: "Endowments of self-awareness.", exVie: "(Những tài năng thiên bẩm về sự tự nhận thức.)" },
  { word: "creative", pos: "adj.", pron: "[kriˈeɪtɪv]", eng: "relating to or involving the imagination or original ideas.", vie: "(sáng tạo)", ex: "Creative imagination.", exVie: "(Trí tưởng tượng sáng tạo.)" },
  { word: "imagination", pos: "n.", pron: "[ɪˌmædʒɪˈneɪʃn]", eng: "the faculty or action of forming new ideas.", vie: "(sự tưởng tượng)", ex: "Creative imagination.", exVie: "(Trí tưởng tượng sáng tạo.)" },
  { word: "conscience", pos: "n.", pron: "[ˈkɑːnʃəns]", eng: "an inner feeling or voice viewed as acting as a guide to the rightness or wrongness of one's behavior.", vie: "(lương tâm)", ex: "Conscience, independence, will.", exVie: "(Lương tâm, sự độc lập, ý chí.)" },
  { word: "will", pos: "n.", pron: "[wɪl]", eng: "the faculty by which a person decides on and initiates action.", vie: "(ý chí)", ex: "Conscience, independence, will.", exVie: "(Lương tâm, sự độc lập, ý chí.)" },
  { word: "tap into", pos: "phrasal v.", pron: "[tæp ˈɪntuː]", eng: "to manage to use something in a way that brings good results.", vie: "(khai thác)", ex: "The ability to tap into your endowments.", exVie: "(Khả năng khai thác những tài năng thiên bẩm của bạn.)" },
  { word: "meaningful", pos: "adj.", pron: "[ˈmiːnɪŋfl]", eng: "having a serious, important, or useful quality or purpose.", vie: "(có ý nghĩa)", ex: "An effective, meaningful life.", exVie: "(Một cuộc sống hiệu quả, đầy ý nghĩa.)" },
  { word: "legacy", pos: "n.", pron: "[ˈleɡəsi]", eng: "an amount of money or property left to someone in a will.", vie: "(di sản)", ex: "Leave a legacy.", exVie: "(Để lại một di sản.)" },
  { word: "empathize", pos: "v.", pron: "[ˈempəθaɪz]", eng: "to understand and share the feelings of another.", vie: "(thông cảm, đồng cảm)", ex: "Empathizing with people.", exVie: "(Đồng cảm với mọi người.)" },
  { word: "generously", pos: "adv.", pron: "[ˈdʒenərəsli]", eng: "in a way that shows a readiness to give more than is expected.", vie: "(một cách hào phóng)", ex: "Giving generously your time.", exVie: "(Hào phóng dành thời gian của bạn.)" },
  { word: "betterment", pos: "n.", pron: "[ˈbetərmənt]", eng: "the improvement of something.", vie: "(sự làm cho tốt hơn, sự cải thiện)", ex: "For the betterment of life and society.", exVie: "(Vì sự cải thiện của cuộc sống và xã hội.)" },
  { word: "unconditionally", pos: "adv.", pron: "[ˌʌnkənˈdɪʃənəli]", eng: "without conditions or limits.", vie: "((một cách) vô điều kiện)", ex: "Loving unconditionally.", exVie: "(Yêu thương vô điều kiện.)" },
  { word: "motivation", pos: "n.", pron: "[ˌmoʊtɪˈveɪʃn]", eng: "the reason or reasons one has for acting or behaving in a particular way.", vie: "(động cơ thúc đẩy)", ex: "M is for motivation.", exVie: "(M là viết tắt của động lực.)" },
  { word: "self-discipline", pos: "n.", pron: "[ˌself ˈdɪsəplɪn]", eng: "the ability to control one's feelings and overcome one's weaknesses.", vie: "(kỷ luật tự giác)", ex: "Self-discipline and spurring yourself on.", exVie: "(Kỷ luật bản thân và không ngừng thúc đẩy chính mình.)" },
  { word: "substitute", pos: "v.", pron: "[ˈsʌbstɪtuːt]", eng: "to use or add in place of.", vie: "(thay thế)", ex: "Substitute your own words.", exVie: "(Thay thế bằng từ ngữ của riêng bạn.)" }
];

const u5_readingParagraphs = [
  'I was <b>browsing</b> around a bookshop, a habit of mine, when I saw a small, interesting book <b>entitled</b> "The ABCs of loving yourself."',
  'Each letter of the <b>alphabet stands for</b> an encouraging and <b>motivational</b> word, useful to <b>guide</b> our life.',
  'Working from memory and allowing myself some <b>leeway</b> to <b>adapt</b> the <b>guidelines</b>, let me <b>go through</b> the alphabet of life.',
  '"A" is for <b>acknowledging</b> or <b>appreciating</b> your value as a person, <b>gifted with endowments</b> of <b>self-awareness</b>, <b>creative imagination</b>, <b>conscience</b>, independence, <b>will</b> and multiple intelligence.',
  '"B" is for believing in yourself, that you have the ability to <b>tap into</b> your <b>endowments</b> to lead an effective, <b>meaningful</b> life.',
  '"C" is for caring about yourself and people, taking care of your basic needs to live, learn, love and leave a <b>legacy</b> while caring for similar needs of other people around you.',
  '"D" is for dreaming big dreams, to search for the wildest wishes that may seem impossible, but that begin to point you in certain directions.',
  '"E" is for <b>empathizing</b> with people, understanding their feelings and their thinking.',
  '"F" is for fun, allowing yourself to enjoy life, what you do and how you do things.',
  '"G" is for giving <b>generously</b> your time, your positive thoughts, your kindness and whatever you can afford to bring to others.',
  '"H" is for happiness, being happy with who you are and what you do in life.',
  '"I" is for imagination, stretching your mind to search for dreams and solutions to achieve your goals.',
  '"J" is for joy, bringing joy to people you meet, live with or work with.',
  '"K" is for knowledge; always learning and using what you know for the <b>betterment</b> of life and society.',
  '"L" is for love, loving <b>unconditionally</b>, not only emotionally or physically but spiritually.',
  '"M" is for <b>motivation</b>, <b>self-discipline</b> and spurring yourself on as well as motivating people to excel.',
  '"N" is for being nice, amiable and friendly even to strangers.',
  '"O" is for openness, being open to people, new ideas and absurd but intriguing ideas.',
  '"P" is for patience, to control oneself, to pace oneself and to follow certain steps in nature.',
  '"Q" is for quiet, to find moments of quiet within yourself, to find a quiet spot to review, reflect and rejuvenate yourself.',
  '"R" is for respect, to value diversity of races, religions, cultures, beliefs and values.',
  '"S" is for smiling, the ability to smile freely even in moments of despair.',
  '"T" is for trust, trusting yourself, your relatives, your friends and people.',
  '"U" is for unity, in living peacefully with people and in valuing the input of a unified team of family, friends and colleagues.',
  '"V" is for victory, recognizing and celebrating even the smallest victory in whatever you do.',
  '"W" is for wonder, wondering about mankind, men and women, yourself and nature.',
  '"X" is for the "X" factor, seeking the extra dimension in yourself and in people, finding the winning trait in each person.',
  '"Y" is for saying "yes" to positive challenges and adventures.',
  '"Z" is for zest in life, in whatever you set out to do.',
  'May you be guided by these ABCs of life. Perhaps you can <b>substitute</b> your own words to make them more meaningful for you.'
];

const unit5 = {
  title: "Unit 5: The ABCs of Living a Happy Life",
  parts: [
    {
      title: "Word List 1",
      content: wordListContent(5, 1, u5_wordList1),
      sections: [
        {
          title: "Exercise 1: Choose the correct word to fill in the blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 1, content: "I spent hours ________ in the bookshop, looking at different titles.", options: ["browsing", "guiding", "adapting", "acknowledging"], correctAnswer: "A", explanation: "Browse means to look at or read casually. 'Browsing' fits the context of casually looking around a bookshop." },
            { id: 2, content: "Each letter of the ________ stands for a motivational word.", options: ["guideline", "endowment", "alphabet", "leeway"], correctAnswer: "C", explanation: "Alphabet is a set of letters in a fixed order. The passage uses 'alphabet' to represent the ABCs of life." },
            { id: 3, content: "She couldn't ________ to the new environment easily.", options: ["browse", "entitle", "stand for", "adapt"], correctAnswer: "D", explanation: "Adapt means to make suitable for a new use or purpose; modify." },
            { id: 4, content: "The teacher asked us to ________ the entire textbook before the exam.", options: ["stand for", "go through", "gifted with", "entitle"], correctAnswer: "B", explanation: "Go through means to examine or search something very carefully." },
            { id: 5, content: "She is ________ exceptional talent in music and painting.", options: ["gifted with", "entitled", "standing for", "going through"], correctAnswer: "A", explanation: "Gifted with means having exceptional talent or natural ability." }
          ]
        },
        {
          title: "Exercise 2: Choose the word that best matches the definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 6, content: "A general rule, principle, or piece of advice", options: ["Leeway", "Guideline", "Alphabet", "Endowment"], correctAnswer: "B", explanation: "A guideline is a general rule, principle, or piece of advice." },
            { id: 7, content: "To accept or admit the existence or truth of", options: ["Browse", "Guide", "Acknowledge", "Adapt"], correctAnswer: "C", explanation: "Acknowledge means to accept or admit the existence or truth of something." },
            { id: 8, content: "The amount of freedom to move or act that is available", options: ["Alphabet", "Leeway", "Guideline", "Endowment"], correctAnswer: "B", explanation: "Leeway is the amount of freedom to move or act." }
          ]
        },
        {
          title: "Exercise 3: Mark each statement T for true or F for false.",
          content: "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">True / False</p>",
          questionType: "TFNG",
          questions: [
            { id: 9, content: "If something is 'motivational', it discourages people from taking action.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Motivational means designed to promote the desire or willingness to do or achieve something." },
            { id: 10, content: "'Stand for' means to represent or mean something.", options: ["True", "False"], correctAnswer: "True", explanation: "True. Stand for means to represent or mean." },
            { id: 11, content: "An 'endowment' is a quality or ability possessed or inherited by someone.", options: ["True", "False"], correctAnswer: "True", explanation: "True. An endowment is a quality or ability someone possesses naturally." }
          ]
        }
      ]
    },
    {
      title: "Word List 2",
      content: wordListContent(5, 2, u5_wordList2),
      sections: [
        {
          title: "Exercise 1: Choose the correct word to fill in the blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 12, content: "She loves her children ________, without expecting anything in return.", options: ["generously", "unconditionally", "creatively", "meaningfully"], correctAnswer: "B", explanation: "Unconditionally means without conditions or limits." },
            { id: 13, content: "He always tries to ________ with people who are going through difficult times.", options: ["substitute", "tap into", "empathize", "motivate"], correctAnswer: "C", explanation: "Empathize means to understand and share the feelings of another." },
            { id: 14, content: "This policy aims at the ________ of the poorest communities.", options: ["legacy", "conscience", "self-discipline", "betterment"], correctAnswer: "D", explanation: "Betterment means the improvement of something." },
            { id: 15, content: "You can ________ your own words to make these principles more personal.", options: ["substitute", "empathize", "tap into", "browse"], correctAnswer: "A", explanation: "Substitute means to use or add in place of." }
          ]
        },
        {
          title: "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 16, content: "I haven't done anything wrong — I've got a clear <i>conscience</i>.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Conscience means an inner feeling guiding the rightness or wrongness of one's behavior." },
            { id: 17, content: "She received a small <i>legacy</i> from her grandmother, which helped pay for college.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Legacy means an amount of money or property left to someone." },
            { id: 18, content: "He showed great <i>self-discipline</i> by losing his temper every day.", options: ["C", "I"], correctAnswer: "B", explanation: "Incorrect. Self-discipline is the ability to control one's feelings and overcome weaknesses, not losing temper." }
          ]
        },
        {
          title: "Exercise 3: Choose the word that best matches the definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 19, content: "Conscious knowledge of one's own character, feelings, and desires", options: ["Self-discipline", "Self-awareness", "Imagination", "Motivation"], correctAnswer: "B", explanation: "Self-awareness is conscious knowledge of one's own character, feelings, motives, and desires." },
            { id: 20, content: "To manage to use something in a way that brings good results", options: ["Empathize", "Substitute", "Tap into", "Guide"], correctAnswer: "C", explanation: "Tap into means to manage to use something effectively." },
            { id: 21, content: "Having a serious, important, or useful quality or purpose", options: ["Creative", "Meaningful", "Generous", "Unconditional"], correctAnswer: "B", explanation: "Meaningful means having a serious, important, or useful quality or purpose." }
          ]
        }
      ]
    },
    {
      title: "Comprehensive Reading",
      content: readingContent(5, "The ABCs of Living a Happy Life", u5_readingParagraphs),
      explanation: "Transcript and Reading Passage Explanation",
      sections: [
        {
          title: "Exercise 1: Fill in each blank with the appropriate word",
          content: "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">Drag and drop the correct words into the blanks.</p>",
          questionType: "Kéo thả",
          questions: [
            { id: 22, content: "1. I was [ 1 ] around a bookshop when I found an interesting book.\u003cbr/\u003e\u003cbr/\u003e2. The book was [ 2 ] \"The ABCs of loving yourself.\"\u003cbr/\u003e\u003cbr/\u003e3. Each letter [ 3 ] an encouraging word.\u003cbr/\u003e\u003cbr/\u003e4. I allowed myself some [ 4 ] to adapt the guidelines.\u003cbr/\u003e\u003cbr/\u003e5. \"A\" is for [ 5 ] your value as a person.\u003cbr/\u003e\u003cbr/\u003e6. \"E\" is for [ 6 ] with people.\u003cbr/\u003e\u003cbr/\u003e7. \"L\" is for love, loving [ 7 ].\u003cbr/\u003e\u003cbr/\u003e8. You can [ 8 ] your own words to make them more meaningful.", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "browsing" },
            { id: 23, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "entitled" },
            { id: 24, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "stands for" },
            { id: 25, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "leeway" },
            { id: 26, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "acknowledging" },
            { id: 27, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "empathizing" },
            { id: 28, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "unconditionally" },
            { id: 29, content: "", options: ["browsing", "entitled", "stands for", "leeway", "acknowledging", "empathizing", "unconditionally", "substitute"], correctAnswer: "substitute" }
          ]
        },
        {
          title: "Exercise 2: Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 30, content: "Where did the author find the book 'The ABCs of loving yourself'?", options: ["In a library", "In a bookshop", "At a friend's house", "Online"], correctAnswer: "B", explanation: "The passage states: 'I was browsing around a bookshop... when I saw a small, interesting book.'" },
            { id: 31, content: "What does the letter 'E' stand for in the alphabet of life?", options: ["Excellence", "Empathizing", "Endowment", "Enthusiasm"], correctAnswer: "B", explanation: "The passage states: '\"E\" is for empathizing with people, understanding their feelings and their thinking.'" },
            { id: 32, content: "According to the passage, what does the author suggest readers do at the end?", options: ["Memorize all the words", "Buy the book", "Substitute their own words", "Share the ABCs with friends"], correctAnswer: "C", explanation: "The passage concludes: 'Perhaps you can substitute your own words to make them more meaningful for you.'" }
          ]
        }
      ]
    }
  ],
  basicInfo: {
    skill: "MCQ (Standard)",
    title: "Unit 5: The ABCs of Living a Happy Life",
    category: "exercise",
    courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    timeLimit: 40
  }
};

// ======================================================================
// ======================== UNIT 6 DATA =================================
// ======================================================================
const u6_wordList1 = [
  { word: "abroad", pos: "adv.", pron: "[əˈbrɔːd]", eng: "in or to a foreign country.", vie: "(ở nước ngoài, ra nước ngoài)", ex: "My brother wants to go abroad next year.", exVie: "(Anh trai tôi muốn đi nước ngoài vào năm tới.)" },
  { word: "anger", pos: "v.", pron: "[ˈæŋɡər]", eng: "to make someone feel strong displeasure.", vie: "(chọc tức, làm giận)", ex: "It angers me when people are rude.", exVie: "(Điều đó khiến tôi tức giận khi mọi người bất lịch sự.)" },
  { word: "bride", pos: "n.", pron: "[braɪd]", eng: "a woman who is getting married or has just gotten married.", vie: "(cô dâu)", ex: "The bride looked beautiful in her wedding dress.", exVie: "(Cô dâu trông rất đẹp trong chiếc váy cưới.)" },
  { word: "brief", pos: "adj.", pron: "[briːf]", eng: "lasting only a short time.", vie: "(ngắn gọn)", ex: "The meeting this afternoon was very brief.", exVie: "(Cuộc họp chiều nay rất ngắn gọn.)" },
  { word: "chase", pos: "v.", pron: "[tʃeɪs]", eng: "to follow someone or something in order to catch them.", vie: "(đuổi theo, rượt đuổi)", ex: "I was chased by an angry native.", exVie: "(Tôi bị một người bản địa tức giận rượt đuổi.)" },
  { word: "disappoint", pos: "v.", pron: "[ˌdɪsəˈpɔɪnt]", eng: "to make one feel sad or unsatisfied.", vie: "(làm thất vọng)", ex: "I do not want to disappoint my family.", exVie: "(Tôi không muốn làm gia đình thất vọng.)" },
  { word: "dive", pos: "v.", pron: "[daɪv]", eng: "to jump into water.", vie: "(lặn, nhảy xuống nước)", ex: "I will dive into the lake once we get there.", exVie: "(Tôi sẽ nhảy xuống hồ khi chúng ta đến đó.)" },
  { word: "exchange", pos: "v.", pron: "[ɪksˈtʃeɪndʒ]", eng: "to give something for another thing in return.", vie: "(trao đổi)", ex: "I exchanged my foreign money for American dollars.", exVie: "(Tôi đã đổi tiền nước ngoài lấy đô la Mỹ.)" },
  { word: "favor", pos: "n.", pron: "[ˈfeɪvər]", eng: "something you do for someone to help them.", vie: "(ân huệ, sự giúp đỡ)", ex: "Can you do me a favor and turn off the lights?", exVie: "(Bạn có thể giúp tôi tắt đèn được không?)" },
  { word: "fee", pos: "n.", pron: "[fiː]", eng: "an amount of money that a person or company asks for a service.", vie: "(phí, lệ phí)", ex: "I had to pay an hourly fee to speak with my lawyer.", exVie: "(Tôi phải trả phí theo giờ để nói chuyện với luật sư.)" }
];

const u6_wordList2 = [
  { word: "forever", pos: "adv.", pron: "[fɔːrˈevər]", eng: "for all time; for always.", vie: "(mãi mãi)", ex: "The young couple promised they would love each other forever.", exVie: "(Cặp đôi trẻ hứa sẽ yêu nhau mãi mãi.)" },
  { word: "guy", pos: "n.", pron: "[ɡaɪ]", eng: "an informal way to call a man.", vie: "(chàng trai, anh chàng)", ex: "The guy at the flower shop was really helpful today.", exVie: "(Anh chàng ở tiệm hoa hôm nay rất nhiệt tình.)" },
  { word: "lovely", pos: "adj.", pron: "[ˈlʌvli]", eng: "good-looking or beautiful.", vie: "(đáng yêu, đẹp)", ex: "The trees look lovely in the fall.", exVie: "(Cây cối trông rất đẹp vào mùa thu.)" },
  { word: "mood", pos: "n.", pron: "[muːd]", eng: "the way someone is feeling.", vie: "(tâm trạng)", ex: "I am in a good mood because I did well on my math test.", exVie: "(Tôi đang vui vì làm bài kiểm tra toán tốt.)" },
  { word: "palace", pos: "n.", pron: "[ˈpæləs]", eng: "a very large building, often the home of a royal family.", vie: "(cung điện)", ex: "The king and queen live in a beautiful palace.", exVie: "(Nhà vua và hoàng hậu sống trong một cung điện đẹp.)" },
  { word: "permit", pos: "v.", pron: "[pərˈmɪt]", eng: "to let someone do something.", vie: "(cho phép)", ex: "My mother permitted me to stay home from school.", exVie: "(Mẹ tôi cho phép tôi ở nhà không đi học.)" },
  { word: "protest", pos: "v.", pron: "[prəˈtest]", eng: "to argue about something with someone.", vie: "(phản đối)", ex: "The people protested the decision of the president.", exVie: "(Người dân phản đối quyết định của tổng thống.)" },
  { word: "sculpture", pos: "n.", pron: "[ˈskʌlptʃər]", eng: "a piece of art made from wood, clay, or stone.", vie: "(bức tượng, tác phẩm điêu khắc)", ex: "We saw an old sculpture of Buddha at the museum.", exVie: "(Chúng tôi đã thấy một bức tượng Phật cổ ở bảo tàng.)" },
  { word: "tribe", pos: "n.", pron: "[traɪb]", eng: "a group of people who live in the same culture.", vie: "(bộ lạc)", ex: "There's a small tribe of people who live in the mountains.", exVie: "(Có một bộ lạc nhỏ sống trên núi.)" },
  { word: "youth", pos: "n.", pron: "[juːθ]", eng: "a time in people's lives when they are young.", vie: "(tuổi trẻ)", ex: "My mother wanted to be a nurse in her youth.", exVie: "(Mẹ tôi muốn trở thành y tá khi còn trẻ.)" }
];

const u6_readingParagraphs = [
  'A <b>lovely</b> princess sat by the pool and played with a <b>sculpture</b> of a bear. Suddenly, she dropped it, and it rolled away. She <b>chased</b> it, but it fell into the water. She began to cry. A large, ugly frog asked, "Why are you crying?" After the princess told him, the frog said, "I can get the <b>sculpture</b>. What will you give me in <b>exchange</b> for the <b>favor</b>?"',
  '"I can pay you a <b>fee</b> in gold," she said.',
  'But the frog <b>protested</b>. "I want to sleep in your bed, and you must kiss me in the morning."',
  '"He\'d <b>dive</b> without water. So, I don\'t have to keep my promise," she thought.',
  'The frog dove for a <b>brief</b> moment and got the <b>sculpture</b>. Then the princess ran away with it. Later, the frog went to the <b>palace</b>. The king told her to keep her promise. This put the princess in a bad <b>mood</b>. She <b>permitted</b> the frog to sleep on her pillow. In the morning, she gave him a kiss.',
  'Suddenly, he turned into a <b>guy</b>. He said, "I\'m from a kingdom <b>abroad</b>. In my <b>youth</b>, I <b>angered</b> a <b>tribe</b> of cruel witches, who turned me into a frog."',
  'The princess asked him, "Can I be your <b>bride</b> and stay with you <b>forever</b>?" But the prince said, "No. You <b>disappointed</b> me. You didn\'t keep your promise."'
];

const unit6 = {
  title: "Unit 6: The Frog Prince",
  parts: [
    {
      title: "Word List 1",
      content: wordListContent(6, 1, u6_wordList1),
      sections: [
        {
          title: "Exercise 1: Choose the correct word to fill in the blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 1, content: "I had to pay an hourly ________ to speak with my lawyer.", options: ["favor", "fee", "exchange", "bride"], correctAnswer: "B", explanation: "A fee is an amount of money asked for a service." },
            { id: 2, content: "She ________ the ball across the field, but it fell into the water.", options: ["dived", "chased", "angered", "exchanged"], correctAnswer: "B", explanation: "Chase means to follow someone or something in order to catch them." },
            { id: 3, content: "The meeting this afternoon was very ________.", options: ["abroad", "brief", "disappointed", "lovely"], correctAnswer: "B", explanation: "Brief means lasting only a short time." },
            { id: 4, content: "I ________ my foreign money for American dollars.", options: ["angered", "chased", "exchanged", "dived"], correctAnswer: "C", explanation: "Exchange means to give something for another thing in return." },
            { id: 5, content: "Can you do me a ________ and turn off the lights?", options: ["fee", "favor", "bride", "anger"], correctAnswer: "B", explanation: "A favor is something you do for someone to help them." }
          ]
        },
        {
          title: "Exercise 2: Choose the word that best matches the definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 6, content: "To make someone feel strong displeasure", options: ["Dive", "Anger", "Chase", "Exchange"], correctAnswer: "B", explanation: "Anger means to make someone feel strong displeasure." },
            { id: 7, content: "A woman who is getting married", options: ["Guy", "Fee", "Bride", "Youth"], correctAnswer: "C", explanation: "A bride is a woman who is getting married." },
            { id: 8, content: "To jump into water", options: ["Chase", "Exchange", "Dive", "Disappoint"], correctAnswer: "C", explanation: "Dive means to jump into water." }
          ]
        },
        {
          title: "Exercise 3: Mark each statement T for true or F for false.",
          content: "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">True / False</p>",
          questionType: "TFNG",
          questions: [
            { id: 9, content: "If something is 'brief', it lasts a very long time.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Brief means lasting only a short time." },
            { id: 10, content: "If you go 'abroad', you go to a foreign country.", options: ["True", "False"], correctAnswer: "True", explanation: "True. Abroad means in or to a foreign country." },
            { id: 11, content: "To 'disappoint' someone means to make them happy.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Disappoint means to make someone feel sad or unsatisfied." }
          ]
        }
      ]
    },
    {
      title: "Word List 2",
      content: wordListContent(6, 2, u6_wordList2),
      sections: [
        {
          title: "Exercise 1: Choose the correct word to fill in the blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 12, content: "The king and queen live in a beautiful ________.", options: ["sculpture", "tribe", "palace", "mood"], correctAnswer: "C", explanation: "A palace is a very large building, often the home of a royal family." },
            { id: 13, content: "The ________ at the flower shop was really helpful today.", options: ["bride", "guy", "tribe", "youth"], correctAnswer: "B", explanation: "Guy is an informal way to call a man." },
            { id: 14, content: "My mother ________ me to stay home from school.", options: ["protested", "permitted", "disappointed", "angered"], correctAnswer: "B", explanation: "Permit means to let someone do something." },
            { id: 15, content: "We saw an old ________ of Buddha at the museum.", options: ["palace", "mood", "sculpture", "tribe"], correctAnswer: "C", explanation: "A sculpture is a piece of art made from wood, clay, or stone." }
          ]
        },
        {
          title: "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 16, content: "The young couple promised they would love each other <i>forever</i>.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Forever means for all time." },
            { id: 17, content: "She was in a good <i>mood</i> because she failed her test.", options: ["C", "I"], correctAnswer: "B", explanation: "Incorrect. Failing a test would put someone in a bad mood, not a good one." },
            { id: 18, content: "My mother wanted to be a nurse in her <i>youth</i>.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Youth is a time in people's lives when they are young." }
          ]
        },
        {
          title: "Exercise 3: Choose the word that best matches the definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 19, content: "Good-looking or beautiful", options: ["Brief", "Lovely", "Abroad", "Forever"], correctAnswer: "B", explanation: "Lovely means good-looking or beautiful." },
            { id: 20, content: "To argue about something with someone", options: ["Permit", "Protest", "Exchange", "Dive"], correctAnswer: "B", explanation: "Protest means to argue about something with someone." },
            { id: 21, content: "A group of people who live in the same culture", options: ["Palace", "Sculpture", "Tribe", "Youth"], correctAnswer: "C", explanation: "A tribe is a group of people who live in the same culture." }
          ]
        }
      ]
    },
    {
      title: "Comprehensive Reading",
      content: readingContent(6, "The Frog Prince", u6_readingParagraphs),
      explanation: "Transcript and Reading Passage Explanation",
      sections: [
        {
          title: "Exercise 1: Fill in each blank with the appropriate word",
          content: "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">Drag and drop the correct words into the blanks.</p>",
          questionType: "Kéo thả",
          questions: [
            { id: 22, content: "1. A [ 1 ] princess sat by the pool and played with a sculpture.\u003cbr/\u003e\u003cbr/\u003e2. She [ 2 ] it, but it fell into the water.\u003cbr/\u003e\u003cbr/\u003e3. \"I can pay you a [ 3 ] in gold,\" she said.\u003cbr/\u003e\u003cbr/\u003e4. He turned into a guy from a kingdom [ 4 ].\u003cbr/\u003e\u003cbr/\u003e5. In his [ 5 ], he angered a tribe of cruel witches.\u003cbr/\u003e\u003cbr/\u003e6. \"You [ 6 ] me. You didn't keep your promise.\"", options: ["lovely", "chased", "fee", "abroad", "youth", "disappointed"], correctAnswer: "lovely" },
            { id: 23, content: "", options: ["lovely", "chased", "fee", "abroad", "youth", "disappointed"], correctAnswer: "chased" },
            { id: 24, content: "", options: ["lovely", "chased", "fee", "abroad", "youth", "disappointed"], correctAnswer: "fee" },
            { id: 25, content: "", options: ["lovely", "chased", "fee", "abroad", "youth", "disappointed"], correctAnswer: "abroad" },
            { id: 26, content: "", options: ["lovely", "chased", "fee", "abroad", "youth", "disappointed"], correctAnswer: "youth" },
            { id: 27, content: "", options: ["lovely", "chased", "fee", "abroad", "youth", "disappointed"], correctAnswer: "disappointed" }
          ]
        },
        {
          title: "Exercise 2: Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 28, content: "What is this story mainly about?", options: ["A guy who angers a cruel witch", "How people are not always what they seem to be", "Why princes should go abroad to find a bride", "How to keep promises made in exchange for favors"], correctAnswer: "B", explanation: "The story is about how appearances can be deceiving — the ugly frog was actually a prince." },
            { id: 29, content: "What did the frog ask the princess to do?", options: ["Be in a better mood", "Kiss him in the morning", "Dive into the pool to get the ball", "Permit him to live in the palace"], correctAnswer: "B", explanation: "The frog said: 'I want to sleep in your bed, and you must kiss me in the morning.'" },
            { id: 30, content: "Why did the prince refuse the princess at the end?", options: ["She didn't pay the fee in gold", "She disappointed him by not keeping her promise", "She was not lovely enough", "She angered his tribe"], correctAnswer: "B", explanation: "The prince said: 'No. You disappointed me. You didn't keep your promise.'" }
          ]
        }
      ]
    }
  ],
  basicInfo: {
    skill: "MCQ (Standard)",
    title: "Unit 6: The Frog Prince",
    category: "exercise",
    courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    timeLimit: 40
  }
};

// ======================================================================
// ======================== UNIT 7 DATA =================================
// ======================================================================
const u7_wordList1 = [
  { word: "basis", pos: "n.", pron: "[ˈbeɪsɪs]", eng: "the underlying support or foundation for an idea, argument, or process.", vie: "(cơ sở, nền tảng)", ex: "My grandfather gets his hearing checked on a yearly basis.", exVie: "(Ông tôi kiểm tra thính lực hàng năm.)" },
  { word: "biology", pos: "n.", pron: "[baɪˈɑːlədʒi]", eng: "the study of living things.", vie: "(sinh học)", ex: "We learned about the human heart in biology class.", exVie: "(Chúng tôi học về tim người trong giờ sinh học.)" },
  { word: "cage", pos: "n.", pron: "[keɪdʒ]", eng: "something that holds an animal so it cannot leave.", vie: "(lồng, chuồng)", ex: "We put the parrots in their cage at night.", exVie: "(Chúng tôi cho vẹt vào lồng vào ban đêm.)" },
  { word: "colleague", pos: "n.", pron: "[ˈkɑːliːɡ]", eng: "somebody you work with.", vie: "(đồng nghiệp)", ex: "My colleague helped me finish the job.", exVie: "(Đồng nghiệp của tôi đã giúp tôi hoàn thành công việc.)" },
  { word: "colony", pos: "n.", pron: "[ˈkɑːləni]", eng: "a country controlled by another country.", vie: "(thuộc địa)", ex: "The USA was at one time a colony of Great Britain.", exVie: "(Hoa Kỳ từng là thuộc địa của Anh.)" },
  { word: "debate", pos: "v.", pron: "[dɪˈbeɪt]", eng: "to seriously discuss something with someone.", vie: "(tranh luận)", ex: "The husband and wife debated over which TV to buy.", exVie: "(Vợ chồng tranh luận về việc mua TV nào.)" },
  { word: "depart", pos: "v.", pron: "[dɪˈpɑːrt]", eng: "to leave some place so you can go to another place.", vie: "(khởi hành, rời đi)", ex: "The plane departed for Italy at 3:00 this afternoon.", exVie: "(Máy bay khởi hành đi Ý lúc 3 giờ chiều nay.)" },
  { word: "depress", pos: "v.", pron: "[dɪˈpres]", eng: "to make someone sad.", vie: "(làm chán nản, buồn bã)", ex: "The bad news from work depressed the man.", exVie: "(Tin xấu từ công việc khiến người đàn ông chán nản.)" },
  { word: "factual", pos: "adj.", pron: "[ˈfæktʃuəl]", eng: "based on or concerned with facts; true.", vie: "(thực tế, có thật)", ex: "John learns about history from factual books.", exVie: "(John học về lịch sử từ những cuốn sách có thật.)" },
  { word: "fascinate", pos: "v.", pron: "[ˈfæsəneɪt]", eng: "to attract and hold the attention of someone strongly.", vie: "(làm say mê, cuốn hút)", ex: "The kitten was fascinated by the ball of yarn.", exVie: "(Chú mèo con bị cuốn hút bởi cuộn len.)" }
];

const u7_wordList2 = [
  { word: "mission", pos: "n.", pron: "[ˈmɪʃən]", eng: "an important job that is sometimes far away.", vie: "(nhiệm vụ, sứ mệnh)", ex: "The woman's mission was to help sick people.", exVie: "(Sứ mệnh của người phụ nữ là giúp đỡ người bệnh.)" },
  { word: "nevertheless", pos: "adv.", pron: "[ˌnevərðəˈles]", eng: "in spite of that; notwithstanding; all the same.", vie: "(tuy nhiên, mặc dù vậy)", ex: "He is usually friendly. Nevertheless, he wasn't this afternoon.", exVie: "(Anh ấy thường thân thiện. Tuy nhiên, chiều nay anh ấy không vậy.)" },
  { word: "occupation", pos: "n.", pron: "[ˌɑːkjəˈpeɪʃən]", eng: "a person's job.", vie: "(nghề nghiệp)", ex: "My father's occupation is a dentist.", exVie: "(Nghề nghiệp của bố tôi là nha sĩ.)" },
  { word: "overseas", pos: "adv.", pron: "[ˌoʊvərˈsiːz]", eng: "in or to a country on the other side of an ocean.", vie: "(ở nước ngoài, hải ngoại)", ex: "John often goes overseas for vacations.", exVie: "(John thường đi nước ngoài nghỉ mát.)" },
  { word: "persuade", pos: "v.", pron: "[pərˈsweɪd]", eng: "to make someone agree to do something.", vie: "(thuyết phục)", ex: "The children persuaded their parents to buy them gifts.", exVie: "(Bọn trẻ thuyết phục bố mẹ mua quà cho chúng.)" },
  { word: "route", pos: "n.", pron: "[ruːt]", eng: "the way you go from one place to another.", vie: "(tuyến đường, lộ trình)", ex: "I saw many new houses along the route to the city.", exVie: "(Tôi thấy nhiều ngôi nhà mới dọc theo đường đến thành phố.)" },
  { word: "ruins", pos: "n.", pron: "[ˈruːɪnz]", eng: "old buildings that are not used anymore.", vie: "(tàn tích, phế tích)", ex: "I visited some interesting ruins in Greece.", exVie: "(Tôi đã thăm một số tàn tích thú vị ở Hy Lạp.)" },
  { word: "scholar", pos: "n.", pron: "[ˈskɑːlər]", eng: "a person who studies something and knows much about it.", vie: "(học giả)", ex: "The scholar knew much about art history.", exVie: "(Học giả biết rất nhiều về lịch sử nghệ thuật.)" },
  { word: "significant", pos: "adj.", pron: "[sɪɡˈnɪfɪkənt]", eng: "important or large enough to have an effect.", vie: "(quan trọng, đáng kể)", ex: "I read many significant novels as a literature major.", exVie: "(Tôi đọc nhiều tiểu thuyết quan trọng khi là sinh viên chuyên ngành văn học.)" },
  { word: "volcano", pos: "n.", pron: "[vɑːlˈkeɪnoʊ]", eng: "a mountain with a hole on top where hot liquid comes out.", vie: "(núi lửa)", ex: "When the volcano erupted, smoke and heat filled the air.", exVie: "(Khi núi lửa phun trào, khói và nhiệt bao trùm không khí.)" }
];

const u7_readingParagraphs = [
  'Dr. Norton\'s <b>occupation</b> was a <b>scholar</b> of <b>biology</b>. He learned about all animals on a daily <b>basis</b>. One day he met a sailor from a <b>colony</b> <b>overseas</b>. The man told Dr. Norton about a talking bird! The bird <b>fascinated</b> Dr. Norton, so he told his <b>colleagues</b> about it. They <b>debated</b> with him: no one thought a bird could talk. He tried to <b>persuade</b> them, but they laughed at him. <b>Nevertheless</b>, Dr. Norton believed the bird was real. His new <b>mission</b> was to find it. He wanted <b>factual</b> proof.',
  'The next day he <b>departed</b> for the <b>colony</b>. The sailor he had met told him to look for a man named Jai, who would be able to help him in his search. After a month of sailing, Dr. Norton finally reached the colony where he met Jai.',
  '"I can take you to where it lives. It lives by the <b>volcano</b>," Jai said.',
  'They left the next day. A week later, they arrived at the <b>volcano</b>. Every day they walked around and looked for the bird, but they couldn\'t find it. After one month, Dr. Norton could not find the bird, and this <b>depressed</b> him. He decided to go home. On the <b>route</b> back, he walked past some old <b>ruins</b>. He heard someone say, "Hello."',
  '"Who are you?" he asked. Dr. Norton looked up and saw a bird!',
  'Dr. Norton put the talking bird into a <b>cage</b>. Then he returned home. He had made a <b>significant</b> discovery.'
];

const unit7 = {
  title: "Unit 7: A Beautiful Bird",
  parts: [
    {
      title: "Word List 1",
      content: wordListContent(7, 1, u7_wordList1),
      sections: [
        {
          title: "Exercise 1: Choose the correct word to fill in the blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 1, content: "My grandfather gets his hearing checked on a yearly ________.", options: ["biology", "cage", "basis", "colony"], correctAnswer: "C", explanation: "Basis refers to the underlying support or foundation; 'on a yearly basis' means every year." },
            { id: 2, content: "The kitten was ________ by the ball of yarn.", options: ["debated", "fascinated", "depressed", "departed"], correctAnswer: "B", explanation: "Fascinate means to attract and hold the attention strongly." },
            { id: 3, content: "We put the parrots in their ________ at night.", options: ["colony", "cage", "debate", "basis"], correctAnswer: "B", explanation: "A cage is something that holds an animal so it cannot leave." },
            { id: 4, content: "My ________ helped me finish the project on time.", options: ["colony", "basis", "cage", "colleague"], correctAnswer: "D", explanation: "A colleague is somebody you work with." },
            { id: 5, content: "John learns about history from ________ books.", options: ["depressed", "factual", "fascinated", "biological"], correctAnswer: "B", explanation: "Factual means based on or concerned with facts; true." }
          ]
        },
        {
          title: "Exercise 2: Choose the word that best matches the definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 6, content: "The study of living things", options: ["Colony", "Biology", "Debate", "Basis"], correctAnswer: "B", explanation: "Biology is the study of living things." },
            { id: 7, content: "A country controlled by another country", options: ["Cage", "Route", "Colony", "Ruins"], correctAnswer: "C", explanation: "A colony is a country controlled by another country." },
            { id: 8, content: "To make someone sad", options: ["Fascinate", "Depart", "Debate", "Depress"], correctAnswer: "D", explanation: "Depress means to make someone sad." }
          ]
        },
        {
          title: "Exercise 3: Mark each statement T for true or F for false.",
          content: "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">True / False</p>",
          questionType: "TFNG",
          questions: [
            { id: 9, content: "To 'debate' means to seriously discuss something with someone.", options: ["True", "False"], correctAnswer: "True", explanation: "True. Debate means to seriously discuss something." },
            { id: 10, content: "To 'depart' means to arrive at a new place.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Depart means to leave some place, not to arrive." },
            { id: 11, content: "If something 'fascinates' you, it bores you completely.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Fascinate means to attract and hold attention strongly, the opposite of boring." }
          ]
        }
      ]
    },
    {
      title: "Word List 2",
      content: wordListContent(7, 2, u7_wordList2),
      sections: [
        {
          title: "Exercise 1: Choose the correct word to fill in the blank.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 12, content: "The woman's ________ was to help sick people in remote areas.", options: ["route", "ruins", "mission", "occupation"], correctAnswer: "C", explanation: "A mission is an important job that is sometimes far away." },
            { id: 13, content: "I visited some interesting ________ in Greece last summer.", options: ["volcanoes", "scholars", "routes", "ruins"], correctAnswer: "D", explanation: "Ruins are old buildings that are not used anymore." },
            { id: 14, content: "The children ________ their parents to buy them gifts.", options: ["depressed", "fascinated", "persuaded", "departed"], correctAnswer: "C", explanation: "Persuade means to make someone agree to do something." },
            { id: 15, content: "He is usually friendly. ________, he wasn't very pleasant this afternoon.", options: ["Overseas", "Nevertheless", "Significantly", "Factually"], correctAnswer: "B", explanation: "Nevertheless means in spite of that; notwithstanding." }
          ]
        },
        {
          title: "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 16, content: "My father's <i>occupation</i> is a dentist.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Occupation means a person's job." },
            { id: 17, content: "The <i>scholar</i> knew nothing about his subject.", options: ["C", "I"], correctAnswer: "B", explanation: "Incorrect. A scholar is a person who studies something and knows much about it, not nothing." },
            { id: 18, content: "I read many <i>significant</i> novels as a literature major.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Significant means important or large enough to have an effect." }
          ]
        },
        {
          title: "Exercise 3: Choose the word that best matches the definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 19, content: "The way you go from one place to another", options: ["Mission", "Route", "Colony", "Ruins"], correctAnswer: "B", explanation: "A route is the way you go from one place to another." },
            { id: 20, content: "In or to a country on the other side of an ocean", options: ["Abroad", "Nevertheless", "Overseas", "Significant"], correctAnswer: "C", explanation: "Overseas means in or to a country on the other side of an ocean." },
            { id: 21, content: "A mountain with a hole on top where hot liquid comes out", options: ["Ruins", "Colony", "Scholar", "Volcano"], correctAnswer: "D", explanation: "A volcano is a mountain with a hole on top where hot liquid comes out." }
          ]
        }
      ]
    },
    {
      title: "Comprehensive Reading",
      content: readingContent(7, "A Beautiful Bird", u7_readingParagraphs),
      explanation: "Transcript and Reading Passage Explanation",
      sections: [
        {
          title: "Exercise 1: Fill in each blank with the appropriate word",
          content: "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">Drag and drop the correct words into the blanks.</p>",
          questionType: "Kéo thả",
          questions: [
            { id: 22, content: "1. Dr. Norton's [ 1 ] was a scholar of biology.\u003cbr/\u003e\u003cbr/\u003e2. One day he met a sailor from a [ 2 ] overseas.\u003cbr/\u003e\u003cbr/\u003e3. His new [ 3 ] was to find the talking bird.\u003cbr/\u003e\u003cbr/\u003e4. After a month, he could not find the bird, and this [ 4 ] him.\u003cbr/\u003e\u003cbr/\u003e5. On the [ 5 ] back, he walked past some old ruins.\u003cbr/\u003e\u003cbr/\u003e6. Dr. Norton put the talking bird into a [ 6 ].\u003cbr/\u003e\u003cbr/\u003e7. He had made a [ 7 ] discovery.", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "occupation" },
            { id: 23, content: "", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "colony" },
            { id: 24, content: "", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "mission" },
            { id: 25, content: "", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "depressed" },
            { id: 26, content: "", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "route" },
            { id: 27, content: "", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "cage" },
            { id: 28, content: "", options: ["occupation", "colony", "mission", "depressed", "route", "cage", "significant"], correctAnswer: "significant" }
          ]
        },
        {
          title: "Exercise 2: Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: 29, content: "What is this story mainly about?", options: ["A route to a new place", "A scholar who finds a talking bird", "How to learn about biology", "Why people debate each other"], correctAnswer: "B", explanation: "The story is about Dr. Norton, a scholar, who goes on a mission to find and bring back a talking bird." },
            { id: 30, content: "Why did Dr. Norton go overseas?", options: ["He wanted to leave his colleagues.", "He was on a mission to find the talking bird.", "He wanted to see the volcano.", "He wanted to discover some old ruins."], correctAnswer: "B", explanation: "Dr. Norton departed for the colony because his new mission was to find the talking bird." },
            { id: 31, content: "What can we infer from the end of the story?", options: ["Jai didn't like Dr. Norton", "Finding the volcano was also a significant discovery", "The bird would be the factual proof to persuade his colleagues", "The bird had fascinated people in the colony for a long time"], correctAnswer: "C", explanation: "Dr. Norton wanted factual proof. The bird in the cage would serve as evidence to persuade his colleagues." }
          ]
        }
      ]
    }
  ],
  basicInfo: {
    skill: "MCQ (Standard)",
    title: "Unit 7: A Beautiful Bird",
    category: "exercise",
    courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    timeLimit: 40
  }
};

// ============== WRITE FILES ==============
fs.writeFileSync('public/unit5_ielts.json', JSON.stringify(unit5, null, 2));
console.log('✅ Unit 5 written to public/unit5_ielts.json');

fs.writeFileSync('public/unit6_ielts.json', JSON.stringify(unit6, null, 2));
console.log('✅ Unit 6 written to public/unit6_ielts.json');

fs.writeFileSync('public/unit7_ielts.json', JSON.stringify(unit7, null, 2));
console.log('✅ Unit 7 written to public/unit7_ielts.json');

console.log('\nAll 3 units generated successfully!');
