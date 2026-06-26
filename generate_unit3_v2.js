const fs = require('fs');

// ============================================================
// UNIT 3: THE INTERESTING LORE OF APRIL FOOLS' DAY
// ============================================================

const wordsList1 = [
    { word: "lore", pos: "n.", pronunciation: "[lɔːr]", eng: "a body of traditions and knowledge.", eng_vie: "(truyền thuyết)", ex: "According to local lore, a ghost haunts this castle.", ex_vie: "(Theo truyền thuyết địa phương, một con ma ám lâu đài này.)" },
    { word: "April Fools' Day", pos: "n.", pronunciation: "[ˌeɪprəl ˈfuːlz deɪ]", eng: "the 1st of April, a day for practical jokes.", eng_vie: "(ngày cá tháng tư)", ex: "He played a great trick on me on April Fools' Day.", ex_vie: "(Anh ấy đã chơi khăm tôi một vố ra trò vào ngày Cá tháng Tư.)" },
    { word: "practical", pos: "adj.", pronunciation: "[ˈpræktɪkl]", eng: "relating to practice or action (a practical joke is a prank).", eng_vie: "((trò đùa) ác ý, (trò chơi) khăm; thực tế)", ex: "Earning a living is a practical matter.", ex_vie: "(Kiếm sống là một vấn đề thực tế.)" },
    { word: "punishment", pos: "n.", pronunciation: "[ˈpʌnɪʃmənt]", eng: "the infliction of a penalty as retribution for an offense.", eng_vie: "(sự trừng phạt)", ex: "He received a harsh punishment for his crime.", ex_vie: "(Anh ta phải chịu một hình phạt khắc nghiệt vì tội ác của mình.)" },
    { word: "origin", pos: "n.", pronunciation: "[ˈɔːrɪdʒɪn]", eng: "the point or place where something begins.", eng_vie: "(nguồn gốc)", ex: "The origin of the custom is uncertain.", ex_vie: "(Nguồn gốc của phong tục này vẫn chưa chắc chắn.)" },
    { word: "custom", pos: "n.", pronunciation: "[ˈkʌstəm]", eng: "a traditional and widely accepted way of behaving.", eng_vie: "(tập quán)", ex: "When visiting a foreign country, we must respect the country's customs.", ex_vie: "(Khi đến thăm một quốc gia khác, chúng ta phải tôn trọng phong tục của họ.)" },
    { word: "come about", pos: "phrasal v.", pronunciation: "[kʌm əˈbaʊt]", eng: "to happen or take place.", eng_vie: "(xảy ra)", ex: "How did this situation come about?", ex_vie: "(Làm thế nào mà tình huống này lại xảy ra?)" },
    { word: "Gregorian calendar", pos: "n.", pronunciation: "[ɡrɪˌɡɔːriən ˈkæləndər]", eng: "the calendar introduced in 1582 by Pope Gregory XIII.", eng_vie: "(lịch Gregory)", ex: "Most of the world uses the Gregorian calendar today.", ex_vie: "(Phần lớn thế giới ngày nay sử dụng lịch Gregory.)" },
    { word: "observe", pos: "v.", pronunciation: "[əbˈzɜːrv]", eng: "to fulfill or comply with.", eng_vie: "(cử hành, tuân theo)", ex: "The student organization is effective in ensuring that students observe school regulations.", ex_vie: "(Tổ chức sinh viên rất hiệu quả trong việc đảm bảo sinh viên tuân thủ nội quy trường học.)" },
    { word: "celebrate", pos: "v.", pronunciation: "[ˈselɪbreɪt]", eng: "to acknowledge with a social gathering or enjoyable activity.", eng_vie: "(làm lễ kỷ niệm)", ex: "We will celebrate her birthday with a big party.", ex_vie: "(Chúng tôi sẽ kỷ niệm sinh nhật cô ấy bằng một bữa tiệc lớn.)" },
    { word: "fall on", pos: "phrasal v.", pronunciation: "[fɔːl ɑːn]", eng: "to occur on a particular day or date.", eng_vie: "(rơi vào)", ex: "This year, Christmas falls on a Tuesday.", ex_vie: "(Năm nay, Giáng sinh rơi vào thứ Ba.)" },
    { word: "trick", pos: "n.", pronunciation: "[trɪk]", eng: "a cunning or skillful act or scheme intended to deceive.", eng_vie: "(trò chơi khăm, trò chơi xỏ)", ex: "He got the money by a trick.", ex_vie: "(Anh ta lấy được tiền bằng một trò lừa đảo.)" },
    { word: "play tricks on", pos: "phrase", pronunciation: "[pleɪ trɪks ɑːn]", eng: "to deceive or play a joke on someone.", eng_vie: "(chơi xỏ, chơi khăm (ai))", ex: "The children love to play tricks on their teacher.", ex_vie: "(Lũ trẻ thích chơi khăm giáo viên của chúng.)" },
    { word: "errand", pos: "n.", pronunciation: "[ˈerənd]", eng: "a short journey to complete a chore.", eng_vie: "(việc vặt)", ex: "She sent him on a fool's errand.", ex_vie: "(Cô ấy đã sai anh ta đi làm một việc vặt vô ích.)" },
    { word: "fool", pos: "v.", pronunciation: "[fuːl]", eng: "to trick or deceive someone.", eng_vie: "(lừa phỉnh, lừa gạt)", ex: "You can't fool me with that old story.", ex_vie: "(Bạn không thể lừa tôi bằng câu chuyện cũ rích đó đâu.)" },
    { word: "tape", pos: "v.", pronunciation: "[teɪp]", eng: "to fasten or attach with tape.", eng_vie: "(buộc, cột, dán băng keo)", ex: "They taped a paper fish to his back.", ex_vie: "(Họ đã dán một con cá bằng giấy vào lưng anh ta.)" },
    { word: "prankster", pos: "n.", pronunciation: "[ˈpræŋkstər]", eng: "a person who plays practical jokes.", eng_vie: "(người hay đùa nghịch, người chơi khăm)", ex: "The prankster laughed when his joke succeeded.", ex_vie: "(Kẻ trêu chọc cười vang khi trò đùa của mình thành công.)" },
    { word: "shoelace", pos: "n.", pronunciation: "[ˈʃuːleɪs]", eng: "a cord or leather strip used to fasten a shoe.", eng_vie: "(dây giày)", ex: "Your shoelace is untied!", ex_vie: "(Dây giày của bạn bị tuột kìa!)" },
    { word: "untie", pos: "v.", pronunciation: "[ʌnˈtaɪ]", eng: "to undo or unfasten.", eng_vie: "(cởi dây, tháo dây)", ex: "He knelt down to untie his shoes.", ex_vie: "(Anh quỳ xuống để tháo dây giày.)" },
    { word: "flock", pos: "n.", pronunciation: "[flɑːk]", eng: "a number of birds of one kind feeding or resting together.", eng_vie: "(đàn, bầy)", ex: "A flock of geese flew overhead.", ex_vie: "(Một đàn ngỗng bay lượn trên đầu.)" },
    { word: "cancel", pos: "v.", pronunciation: "[ˈkænsl]", eng: "to decide that an organized event will not take place.", eng_vie: "(hủy, bãi bỏ)", ex: "She cancelled her trip to New York as she felt ill.", ex_vie: "(Cô ấy đã hủy chuyến đi New York vì cảm thấy ốm.)" },
    { word: "innocent", pos: "adj.", pronunciation: "[ˈɪnəsnt]", eng: "not guilty of a crime or offense.", eng_vie: "(ngây thơ, vô tội)", ex: "They hanged an innocent man.", ex_vie: "(Họ đã treo cổ một người đàn ông vô tội.)" },
    { word: "victim", pos: "n.", pronunciation: "[ˈvɪktɪm]", eng: "a person harmed or injured.", eng_vie: "(nạn nhân)", ex: "The victim of the joke laughed along with everyone.", ex_vie: "(Nạn nhân của trò đùa đã cười cùng với mọi người.)" },
    { word: "fall for", pos: "phrasal v.", pronunciation: "[fɔːl fɔːr]", eng: "to be deceived by something.", eng_vie: "(mắc lừa)", ex: "He fell for the trick completely.", ex_vie: "(Anh ta đã hoàn toàn mắc bẫy trò lừa.)" },
];

const wordsList2 = [
    { word: "stuff", pos: "v.", pronunciation: "[stʌf]", eng: "to fill a receptacle or space tightly with something.", eng_vie: "(nhồi, nhét)", ex: "He stuffed the shoe with newspapers.", ex_vie: "(Anh ấy nhét đầy giấy báo vào chiếc giày.)" },
    { word: "keep up", pos: "phrasal v.", pronunciation: "[kiːp ʌp]", eng: "to continue a course of action.", eng_vie: "(duy trì, tiếp tục)", ex: "Some practical jokes are kept up the whole day.", ex_vie: "(Một số trò đùa ác ý được duy trì cả ngày.)" },
    { word: "in (good) fun", pos: "phrase", pronunciation: "[ɪn ɡʊd fʌn]", eng: "not intended to be serious or to cause harm.", eng_vie: "(rất vui, đùa thôi)", ex: "The teasing was all in good fun.", ex_vie: "(Những lời trêu chọc chỉ là đùa vui thôi.)" },
    { word: "mean", pos: "v.", pronunciation: "[miːn]", eng: "to intend to convey or refer to.", eng_vie: "(có ý định)", ex: "I'm sorry, I didn't mean to imply that you were dishonest.", ex_vie: "(Tôi xin lỗi, tôi không có ý ám chỉ rằng bạn không trung thực.)" },
    { word: "composite", pos: "n.", pronunciation: "[kəmˈpɑːzɪt]", eng: "a thing made up of several parts or elements.", eng_vie: "(hỗn hợp, hợp chất, sự kết hợp)", ex: "The letters are composites of prankishness and love.", ex_vie: "(Những bức thư là sự kết hợp giữa tính hay chơi khăm và tình yêu.)" },
    { word: "prankishness", pos: "n.", pronunciation: "[ˈpræŋkɪʃnəs]", eng: "the quality of being mischievous or playing pranks.", eng_vie: "(tính hay chơi khăm)", ex: "His prankishness always gets him into trouble.", ex_vie: "(Tính hay chơi khăm luôn khiến anh ta gặp rắc rối.)" },
    { word: "deception", pos: "n.", pronunciation: "[dɪˈsepʃn]", eng: "the action of deceiving someone.", eng_vie: "(sự lừa dối)", ex: "The deception of the salesman turned out to be disastrous.", ex_vie: "(Sự lừa dối của nhân viên bán hàng hóa ra lại là một thảm họa.)" },
    { word: "absurdity", pos: "n.", pronunciation: "[əbˈsɜːrdəti]", eng: "the quality or state of being ridiculous or wildly unreasonable.", eng_vie: "(sự phi lý, sự ngu xuẩn)", ex: "Sometimes a thing is absurd but intriguing.", ex_vie: "(Đôi khi một điều gì đó thật phi lý nhưng lại hấp dẫn.)" },
    { word: "folk verse", pos: "n.", pronunciation: "[foʊk vɜːrs]", eng: "traditional poetry of a particular community.", eng_vie: "(bài thơ dân gian)", ex: "The letters contained old folk verses.", ex_vie: "(Những lá thư chứa đựng những bài thơ dân gian xưa.)" },
    { word: "deem", pos: "v.", pronunciation: "[diːm]", eng: "to regard or consider in a specified way.", eng_vie: "(cho rằng, nghĩ rằng)", ex: "The event was deemed a great success.", ex_vie: "(Sự kiện được coi là một thành công lớn.)" },
    { word: "flattering", pos: "adj.", pronunciation: "[ˈflætərɪŋ]", eng: "full of praise and compliments.", eng_vie: "(xu nịnh)", ex: "It is deemed a most flattering honor.", ex_vie: "(Đó được coi là một vinh dự đáng tự hào nhất.)" },
    { word: "envious", pos: "adj.", pronunciation: "[ˈenviəs]", eng: "feeling or showing envy.", eng_vie: "(ghen tị, đố kỵ)", ex: "Mary was always envious of her younger sister's beauty.", ex_vie: "(Mary luôn ghen tị với vẻ đẹp của em gái mình.)" },
    { word: "acquaintance", pos: "n.", pronunciation: "[əˈkweɪntəns]", eng: "a person's knowledge or experience of something or someone.", eng_vie: "(người quen)", ex: "They are old acquaintances.", ex_vie: "(Họ là những người quen cũ.)" },
    { word: "confine", pos: "v.", pronunciation: "[kənˈfaɪn]", eng: "to keep or restrict someone or something within certain limits.", eng_vie: "(giới hạn)", ex: "The tour group is confined to the planned activities.", ex_vie: "(Đoàn du lịch bị giới hạn trong các hoạt động đã lên kế hoạch.)" },
    { word: "fake", pos: "v.", pronunciation: "[feɪk]", eng: "to forge or counterfeit.", eng_vie: "(làm giả)", ex: "He faked his father's signature on the document.", ex_vie: "(Anh ta đã làm giả chữ ký của cha mình trên tài liệu.)" },
    { word: "issue", pos: "v.", pronunciation: "[ˈɪʃuː]", eng: "to supply or distribute.", eng_vie: "(lưu hành, in ra, cấp phát)", ex: "The school issued uniforms to the players.", ex_vie: "(Trường học đã cấp đồng phục cho các cầu thủ.)" },
    { word: "nonexistent", pos: "adj.", pronunciation: "[ˌnɑːnɪɡˈzɪstənt]", eng: "not existing, or not real or present.", eng_vie: "(không tồn tại)", ex: "He issued tickets for nonexistent parties.", ex_vie: "(Anh ta phát hành vé cho những bữa tiệc không tồn tại.)" },
    { word: "elaborate", pos: "adj.", pronunciation: "[ɪˈlæbərət]", eng: "involving many carefully arranged parts or details.", eng_vie: "(kỹ lưỡng, công phu)", ex: "She made elaborate preparations for the party.", ex_vie: "(Cô ấy đã chuẩn bị kỹ lưỡng cho bữa tiệc.)" },
    { word: "persuade", pos: "v.", pronunciation: "[pərˈsweɪd]", eng: "to cause someone to do something through reasoning or argument.", eng_vie: "(thuyết phục)", ex: "They persuaded her to tell a lie.", ex_vie: "(Họ đã thuyết phục cô ấy nói dối.)" },
    { word: "keep on", pos: "phrasal v.", pronunciation: "[kiːp ɑːn]", eng: "to continue to do something.", eng_vie: "(tiếp tục)", ex: "He kept on laughing at the joke.", ex_vie: "(Anh ấy tiếp tục cười nhạo trò đùa.)" },
    { word: "go around", pos: "phrasal v.", pronunciation: "[ɡoʊ əˈraʊnd]", eng: "to circulate or spend time with.", eng_vie: "(đi chơi, lui tới với (ai))", ex: "He kept right on going around with her.", ex_vie: "(Anh ấy vẫn tiếp tục đi chơi với cô ấy.)" },
    { word: "make a game of", pos: "phrase", pronunciation: "[meɪk ə ɡeɪm əv]", eng: "to treat an activity as a game.", eng_vie: "(chơi trò)", ex: "They make a game of trying to guess who sent the letters.", ex_vie: "(Họ chơi trò cố gắng đoán xem ai đã gửi những lá thư đó.)" },
    { word: "scare", pos: "n.", pronunciation: "[sker]", eng: "a sudden attack of fright.", eng_vie: "(sự sợ hãi, sự hoang mang)", ex: "They created a bomb scare in the office.", ex_vie: "(Họ đã tạo ra một sự hoang mang về bom trong văn phòng.)" },
    { word: "fool around", pos: "phrasal v.", pronunciation: "[fuːl əˈraʊnd]", eng: "to behave in a silly or irresponsible way.", eng_vie: "(đùa cợt, lăng nhăng)", ex: "He had been fooling around with his secretary.", ex_vie: "(Anh ta đã lăng nhăng với cô thư ký của mình.)" },
];

// --- Helper functions ---
function wordHtml(w) {
    return `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${w.word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${w.pronunciation}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${w.pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${w.eng} <span style="color:#0ea5e9;">${w.eng_vie}</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${w.ex} <span style="color:#0ea5e9;">${w.ex_vie}</span></div></div></div>`;
}
function generateDetailedMeanings(words) {
    return `<div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">${words.map(w => wordHtml(w)).join('')}</div></div>`;
}

const word1Content = `<p style="display: none;">Word List 1</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit3_ielts_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateDetailedMeanings(wordsList1)}</div>`;
const word2Content = `<p style="display: none;">Word List 2</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit3_ielts_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" />${generateDetailedMeanings(wordsList2)}</div>`;

const readingContent = `<p style="display: none;">Comprehensive Reading</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="/unit3_ielts_story.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Interesting Lore of April Fools' Day</h1><p style="margin-bottom: 1rem;">The first of April is a special day, on which <b>practical</b> jokes may be played without <b>punishment</b>. The <b>origin</b> of the <b>custom</b> is uncertain, but it seems to have <b>come about</b> in France as a result of change to the <b>Gregorian calendar</b> in 1582.</p><p style="margin-bottom: 1rem;">In sixteenth-century France, the start of the new year was <b>observed</b> on April first. It was <b>celebrated</b> in much the same way as it is today with parties and dancing into the late hours of the night. Then in 1582, Pope Gregory introduced a new calendar for the Christian world, and the new year <b>fell on</b> January first. There were some people, however, who hadn't heard or didn't believe the change in the date, so they continued to celebrate New Year's Day on April first. Others <b>played tricks on</b> them and called them "April Fools." They sent them on a "fool's <b>errand</b>" or tried to make them believe that something false was true.</p><p style="margin-bottom: 1rem;">In France today, children <b>fool</b> their friends by <b>taping</b> a paper fish to their friends' backs. When the "young fool" discovers this <b>trick</b>, the <b>prankster</b> yells "April Fish!" Today Americans play small tricks on friends and strangers alike on the same day. One common trick is pointing down to a friend's shoe and saying, "Your <b>shoelace</b> is <b>untied</b>!" Teachers in the nineteenth century used to say to pupils, "Look! A <b>flock</b> of geese!" and point up. School children might tell a classmate that school has been <b>canceled</b>. Whatever the trick, if the <b>innocent victim falls for</b> the joke the prankster yells, "April Fool!"</p><p style="margin-bottom: 1rem;">The "fool's errands" we play on people are practical jokes. Filling the sugar bowl with salt, <b>stuffing</b> a biscuit with cotton and offering an empty egg shell at breakfast, are good old tricks. Some practical jokes are <b>kept up</b> the whole day before the victim realizes what day it is. Most April Fool jokes are <b>in good fun</b> and not <b>meant</b> to harm anyone. The most clever April Fool joke is the one where everyone laughs, especially the person upon whom the joke is played.</p><p style="margin-bottom: 1rem;">There are also April Fool letters. They are <b>composites</b> of <b>prankishness</b>, <b>deception</b>, <b>absurdity</b>, <b>folk verses</b>, and love. The letters are never signed, but girls, apparently, <b>make a game of</b> trying to guess who send them. To receive an April Fool letter during April, for it can be sent anytime during the month, is <b>deemed</b> a most <b>flattering</b> honor and the contents are shared among <b>envious acquaintances</b>.</p><p style="margin-bottom: 1rem;">April Fool tricks are not, it seems, <b>confined</b> to children. People play tricks in the office. <b>Faking</b> phone calls, <b>issuing</b> tickets for <b>nonexistent</b> parties, and creating bomb <b>scares</b> are all <b>elaborate</b> pranks. The story of a salesman in Rhode Island is said to be the worst trick on April Fools' Day. He had been <b>fooling around</b> with a secretary. He was married and everyone in the office knew about it. The girl was a bit crazy, a real screwball, and one of the other salesmen <b>persuaded</b> her to tell her boyfriend she was pregnant as an April Fool joke. She went in his office and left the door open so everyone could hear her. Her words did make him a little crazy. He thought it was a big joke. Maybe he was happy it was an April Fool joke. But he just laughed and <b>kept right on going around</b> with her.</p></div></div>`;

const unit3 = {
  "title": "Unit 3: The Interesting Lore of April Fools' Day",
  "parts": [
    {
      "title": "Word List 1",
      "content": word1Content,
      "sections": [
        {
          "title": "Exercise 1: Choose the correct word to fill in the blank.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 1, "content": "The ________ of the custom is uncertain.", "options": ["origin", "lore", "punishment", "trick"], "correctAnswer": "A", "explanation": "Origin means the point or place where something begins." },
            { "id": 2, "content": "When visiting a foreign country, we must respect the country's ________.", "options": ["errands", "customs", "tricks", "punishments"], "correctAnswer": "B", "explanation": "Custom means a traditional and widely accepted way of behaving." },
            { "id": 3, "content": "This year, Christmas ________ a Tuesday.", "options": ["comes about", "falls on", "plays tricks on", "fools"], "correctAnswer": "B", "explanation": "Fall on means to occur on a particular day or date." },
            { "id": 4, "content": "She ________ her trip to New York as she felt ill.", "options": ["cancelled", "observed", "celebrated", "taped"], "correctAnswer": "A", "explanation": "Cancel means to decide that an organized event will not take place." },
            { "id": 5, "content": "He got the money by a ________.", "options": ["flock", "shoelace", "trick", "victim"], "correctAnswer": "C", "explanation": "Trick means a cunning act or scheme intended to deceive." }
          ]
        },
        {
          "title": "Exercise 2: Choose the word that best matches the definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 6, "content": "A body of traditions and knowledge", "options": ["Custom", "Lore", "Punishment", "Origin"], "correctAnswer": "B", "explanation": "Lore is a body of traditions and knowledge." },
            { "id": 7, "content": "A person who plays practical jokes", "options": ["Victim", "Prankster", "Fool", "Innocent"], "correctAnswer": "B", "explanation": "A prankster is a person who plays practical jokes." },
            { "id": 8, "content": "To be deceived by something", "options": ["Come about", "Fall for", "Play tricks on", "Cancel"], "correctAnswer": "B", "explanation": "Fall for means to be deceived by something." }
          ]
        },
        {
          "title": "Exercise 3: Mark each statement T for true or F for false.",
          "content": "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">True / False</p>",
          "questionType": "TFNG",
          "questions": [
            { "id": 9, "content": "April Fools' Day falls on the 1st of March.", "options": ["True", "False"], "correctAnswer": "False", "explanation": "False. April Fools' Day is the 1st of April." },
            { "id": 10, "content": "To 'observe' can mean to fulfill or comply with.", "options": ["True", "False"], "correctAnswer": "True", "explanation": "True. Observe means to fulfill or comply with." },
            { "id": 11, "content": "An 'errand' is a short journey to complete a chore.", "options": ["True", "False"], "correctAnswer": "True", "explanation": "True. An errand is a short journey to complete a chore." }
          ]
        }
      ]
    },
    {
      "title": "Word List 2",
      "content": word2Content,
      "sections": [
        {
          "title": "Exercise 1: Choose the correct word to fill in the blank.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 12, "content": "He ________ the shoe with newspapers.", "options": ["stuffed", "issued", "faked", "deemed"], "correctAnswer": "A", "explanation": "Stuff means to fill a receptacle or space tightly with something." },
            { "id": 13, "content": "The ________ of the salesman turned out to be disastrous.", "options": ["absurdity", "deception", "composite", "scare"], "correctAnswer": "B", "explanation": "Deception means the action of deceiving someone." },
            { "id": 14, "content": "They ________ her to tell a lie.", "options": ["confined", "kept on", "persuaded", "deemed"], "correctAnswer": "C", "explanation": "Persuade means to cause someone to do something through reasoning." },
            { "id": 15, "content": "The event was ________ a great success.", "options": ["deemed", "faked", "stuffed", "confined"], "correctAnswer": "A", "explanation": "Deem means to regard or consider in a specified way." }
          ]
        },
        {
          "title": "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 16, "content": "The teasing was all <i>in good fun</i> and nobody got hurt.", "options": ["C", "I"], "correctAnswer": "A", "explanation": "Correct. In good fun means not intended to be serious or to cause harm." },
            { "id": 17, "content": "She made <i>elaborate</i> preparations, which means she didn't prepare at all.", "options": ["C", "I"], "correctAnswer": "B", "explanation": "Incorrect. Elaborate means involving many carefully arranged parts, so she prepared thoroughly." },
            { "id": 18, "content": "He <i>faked</i> his father's signature, meaning he copied it without permission.", "options": ["C", "I"], "correctAnswer": "A", "explanation": "Correct. Fake means to forge or counterfeit." }
          ]
        },
        {
          "title": "Exercise 3: Choose the word that best matches the definition.",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 19, "content": "The quality of being mischievous or playing pranks", "options": ["Deception", "Prankishness", "Absurdity", "Composite"], "correctAnswer": "B", "explanation": "Prankishness is the quality of being mischievous or playing pranks." },
            { "id": 20, "content": "Not existing, or not real or present", "options": ["Elaborate", "Flattering", "Nonexistent", "Envious"], "correctAnswer": "C", "explanation": "Nonexistent means not existing, or not real or present." },
            { "id": 21, "content": "To keep or restrict within certain limits", "options": ["Confine", "Issue", "Keep up", "Go around"], "correctAnswer": "A", "explanation": "Confine means to keep or restrict within certain limits." }
          ]
        }
      ]
    },
    {
      "title": "Comprehensive Reading",
      "content": readingContent,
      "explanation": "Transcript and Reading Passage Explanation",
      "sections": [
        {
          "title": "Exercise 1: Fill in each blank with the appropriate word",
          "content": "<p class=\"font-bold text-[16px] text-slate-800 mb-4\">Drag and drop the correct words into the blanks.</p>",
          "questionType": "Kéo thả",
          "questions": (() => {
            const blanks = [
              { answer: "practical" },
              { answer: "origin" },
              { answer: "Gregorian calendar" },
              { answer: "observed" },
              { answer: "played tricks on" },
              { answer: "errand" },
              { answer: "prankster" },
              { answer: "innocent" },
              { answer: "kept up" },
              { answer: "composites" },
              { answer: "confined" }
            ];
            const allOptions = blanks.map(b => b.answer);
            const contentText = `1. The first of April is a special day, on which [ 1 ] jokes may be played without punishment.<br/><br/>2. The [ 2 ] of the custom is uncertain.<br/><br/>3. It seems to have come about in France as a result of change to the [ 3 ] in 1582.<br/><br/>4. The start of the new year was [ 4 ] on April first.<br/><br/>5. Others [ 5 ] them and called them "April Fools."<br/><br/>6. They sent them on a "fool's [ 6 ]."<br/><br/>7. When the "young fool" discovers this trick, the [ 7 ] yells "April Fish!"<br/><br/>8. If the [ 8 ] victim falls for the joke...<br/><br/>9. Some practical jokes are [ 9 ] the whole day.<br/><br/>10. The letters are [ 10 ] of prankishness, deception, absurdity, folk verses, and love.<br/><br/>11. April Fool tricks are not [ 11 ] to children.`;
            return blanks.map((b, i) => ({
              "id": 22 + i,
              "content": i === 0 ? contentText : "",
              "options": allOptions,
              "correctAnswer": b.answer
            }));
          })()
        },
        {
          "title": "Exercise 2: Reading Comprehension",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            { "id": 33, "content": "According to the passage, how did April Fools' Day originate?", "options": ["It was created by American school children.", "It came about in France due to a change in the calendar.", "It was started by Pope Gregory as a religious holiday.", "It originated from ancient Roman festivals."], "correctAnswer": "B", "explanation": "The text states: 'it seems to have come about in France as a result of change to the Gregorian calendar in 1582.'" },
            { "id": 34, "content": "What is the common April Fools' Day trick in France today?", "options": ["Pointing at someone's shoe.", "Saying 'Look! A flock of geese!'", "Taping a paper fish to someone's back.", "Telling a classmate that school has been canceled."], "correctAnswer": "C", "explanation": "The text states: 'In France today, children fool their friends by taping a paper fish to their friends' backs.'" },
            { "id": 35, "content": "According to the passage, receiving an April Fool letter is considered:", "options": ["An insult.", "A flattering honor.", "A sign of bad luck.", "A common occurrence."], "correctAnswer": "B", "explanation": "The text states: 'To receive an April Fool letter... is deemed a most flattering honor.'" },
            { "id": 36, "content": "What happened in the story about the salesman in Rhode Island?", "options": ["He quit his job after the prank.", "He got angry and filed a complaint.", "He laughed and kept going around with the secretary.", "He divorced his wife."], "correctAnswer": "C", "explanation": "The text says: 'But he just laughed and kept right on going around with her.'" }
          ]
        }
      ]
    }
  ],
  "basicInfo": {
    "skill": "MCQ (Standard)",
    "title": "Unit 3: The Interesting Lore of April Fools' Day",
    "category": "exercise",
    "courseId": "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
    "timeLimit": 40
  }
};

fs.writeFileSync('public/unit3_ielts.json', JSON.stringify(unit3, null, 2));
console.log('Unit 3 JSON generated successfully! (Unit 1 format)');
