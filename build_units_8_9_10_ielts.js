const fs = require('fs');

// ============================================================
// HELPER: Build a single word meaning HTML block (matches Unit 1 exactly)
// ============================================================
function wordBlock(word, pron, pos, def, viDef, example, viExample) {
  return `<div style="display:flex;gap:16px;align-items:flex-start;"><div style="width:32px;height:32px;flex-shrink:0;background-color:#f8fafc;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid #e2e8f0;font-size:16px;">😎</div><div style="display:flex;flex-direction:column;gap:6px;"><div style="display:flex;align-items:baseline;gap:8px;"><span style="font-size:1.25rem;font-weight:800;color:#65a30d;">${word}</span><span style="font-size:0.875rem;color:#94a3b8;font-family:monospace;">${pron}</span><span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">${pos}</span></div><div style="color:#475569;font-size:0.95rem;line-height:1.5;">${def} <span style="color:#0ea5e9;">(${viDef})</span></div><div style="color:#64748b;font-size:0.95rem;font-style:italic;">→ ${example} <span style="color:#0ea5e9;">(${viExample})</span></div></div></div>`;
}

// ============================================================
// HELPER: Build word list content HTML (image + detailed meanings)
// ============================================================
function buildWordListContent(unitNum, listNum, wordsArray) {
  const imgSrc = `/unit${unitNum}_ielts_word_list_${listNum}.png`;
  let meanings = wordsArray.map(w => wordBlock(w.word, w.pron, w.pos, w.def, w.viDef, w.example, w.viExample)).join('');
  return `<p style="display: none;">Word List ${listNum}</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="${imgSrc}" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="display:flex;flex-direction:column;gap:24px;padding-top:24px;border-top:1px dashed #cbd5e1;"><h3 style="font-size:1.125rem;font-weight:700;color:#475569;text-transform:uppercase;letter-spacing:0.05em;margin:0;">Detailed Meanings</h3><div style="display:flex;flex-direction:column;gap:24px;">${meanings}</div></div></div>`;
}

// ============================================================
// HELPER: Build reading passage content HTML
// ============================================================
function buildReadingContent(unitNum, title, paragraphs) {
  const imgSrc = `/unit${unitNum}_ielts_story.png`;
  let pTags = paragraphs.map(p => `<p style="margin-bottom: 1rem;">${p}</p>`).join('');
  return `<p style="display: none;">Comprehensive Reading</p><div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><img src="${imgSrc}" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">${title}</h1>${pTags}</div></div>`;
}

// ============================================================
// UNIT 8: The Anniversary Gift
// ============================================================
function buildUnit8() {
  const wordList1 = [
    { word: "anniversary", pron: "[ˌænɪˈvɜːrsəri]", pos: "n.", def: "a day that celebrates something from the past.", viDef: "Ngày kỉ niệm một sự kiện trong quá khứ.", example: "My parents went out to eat for their wedding anniversary.", viExample: "Bố mẹ tôi đi ăn ngoài nhân dịp kỷ niệm ngày cưới." },
    { word: "arithmetic", pron: "[əˈrɪθmətɪk]", pos: "n.", def: "the branch of math dealing with numbers and basic operations.", viDef: "Môn toán học cơ bản liên quan đến số và các phép tính.", example: "I like to study arithmetic at school.", viExample: "Tôi thích học môn số học ở trường." },
    { word: "ashamed", pron: "[əˈʃeɪmd]", pos: "adj.", def: "feeling upset because you did something wrong or bad.", viDef: "Cảm thấy buồn vì đã làm điều gì đó sai hoặc tệ, xấu hổ.", example: "He was ashamed when he found out that I knew about his past.", viExample: "Anh ấy xấu hổ khi phát hiện tôi biết về quá khứ của anh ấy." },
    { word: "burst", pron: "[bɜːrst]", pos: "v.", def: "to suddenly break open or apart.", viDef: "Đột ngột vỡ ra hoặc bung ra.", example: "The bomb burst over the city.", viExample: "Quả bom nổ tung trên thành phố." },
    { word: "carpenter", pron: "[ˈkɑːrpəntər]", pos: "n.", def: "a person who builds things with wood.", viDef: "Người đóng đồ bằng gỗ, thợ mộc.", example: "We hired a carpenter to make a cupboard.", viExample: "Chúng tôi thuê một thợ mộc để đóng tủ." },
    { word: "coal", pron: "[koʊl]", pos: "n.", def: "a hard black rock that you burn for heat.", viDef: "Một loại đá đen cứng dùng để đốt lấy nhiệt, than đá.", example: "Many power stations burn coal to produce energy.", viExample: "Nhiều nhà máy điện đốt than đá để sản xuất năng lượng." },
    { word: "couch", pron: "[kaʊtʃ]", pos: "n.", def: "a long, soft seat that many people can sit on.", viDef: "Ghế dài, mềm cho nhiều người ngồi, ghế sofa.", example: "Kim and Martin's new couch was very expensive.", viExample: "Chiếc ghế sofa mới của Kim và Martin rất đắt." },
    { word: "drip", pron: "[drɪp]", pos: "v.", def: "when a liquid falls just a little bit at a time.", viDef: "Khi chất lỏng rơi từng giọt một, nhỏ giọt.", example: "I heard water dripping from the faucet.", viExample: "Tôi nghe thấy nước nhỏ giọt từ vòi." },
    { word: "elegant", pron: "[ˈelɪɡənt]", pos: "adj.", def: "very fancy and pleasing in appearance.", viDef: "Rất sang trọng và đẹp mắt, thanh lịch.", example: "In Japan, women wear elegant kimonos on special occasions.", viExample: "Ở Nhật, phụ nữ mặc kimono thanh lịch trong những dịp đặc biệt." },
    { word: "fabric", pron: "[ˈfæbrɪk]", pos: "n.", def: "cloth used to make clothes, furniture, etc.", viDef: "Vải dùng để may quần áo, đồ nội thất, v.v.", example: "The towels were made from a soft fabric.", viExample: "Những chiếc khăn được làm từ loại vải mềm." },
  ];

  const wordList2 = [
    { word: "highlands", pron: "[ˈhaɪləndz]", pos: "n.", def: "high areas of land, usually with mountains.", viDef: "Vùng đất cao, thường có núi, vùng cao nguyên.", example: "The man had a small home in the highlands.", viExample: "Người đàn ông có một ngôi nhà nhỏ ở vùng cao nguyên." },
    { word: "ivory", pron: "[ˈaɪvəri]", pos: "n.", def: "a white, hard substance that comes from elephants.", viDef: "Chất cứng, màu trắng lấy từ voi, ngà voi.", example: "The elephant's long ivory tusks looked very impressive.", viExample: "Cặp ngà voi dài trông rất ấn tượng." },
    { word: "mill", pron: "[mɪl]", pos: "n.", def: "a building where flour is made.", viDef: "Tòa nhà nơi bột mì được sản xuất, nhà máy xay.", example: "The farmer took his wheat to the mill to make it into flour.", viExample: "Người nông dân mang lúa mì đến nhà máy xay để xay thành bột." },
    { word: "needle", pron: "[ˈniːdl]", pos: "n.", def: "a small, sharp piece of metal used to make or fix clothes.", viDef: "Mảnh kim loại nhỏ, nhọn dùng để may hoặc sửa quần áo, cây kim.", example: "I used a needle to fix the hole in my pants.", viExample: "Tôi dùng một cây kim để vá lỗ thủng trên quần." },
    { word: "polish", pron: "[ˈpɑːlɪʃ]", pos: "v.", def: "to rub something in order to make it shiny.", viDef: "Chà xát một vật gì đó để làm cho nó sáng bóng, đánh bóng.", example: "Mark spent all morning polishing his shoes for the wedding.", viExample: "Mark dành cả buổi sáng đánh bóng giày cho đám cưới." },
    { word: "sew", pron: "[soʊ]", pos: "v.", def: "to put pieces of cloth together using string.", viDef: "Ghép các mảnh vải lại với nhau bằng chỉ, may.", example: "I learned to sew when I was a little girl.", viExample: "Tôi học may từ khi còn nhỏ." },
    { word: "shed", pron: "[ʃed]", pos: "n.", def: "a small building where you store things like tools.", viDef: "Tòa nhà nhỏ nơi bạn cất giữ đồ đạc như dụng cụ, nhà kho.", example: "We have a small shed in the backyard for storage.", viExample: "Chúng tôi có một nhà kho nhỏ ở sân sau để cất đồ." },
    { word: "thread", pron: "[θred]", pos: "n.", def: "a thin piece of string.", viDef: "Một sợi dây mỏng, sợi chỉ.", example: "I have many different colors of thread at home.", viExample: "Tôi có nhiều màu chỉ khác nhau ở nhà." },
    { word: "trim", pron: "[trɪm]", pos: "v.", def: "to cut something a little bit.", viDef: "Cắt bớt một chút, cắt tỉa.", example: "I had my hair trimmed this afternoon.", viExample: "Tôi đã cắt tỉa tóc chiều nay." },
    { word: "upwards", pron: "[ˈʌpwərdz]", pos: "adv.", def: "moving vertically higher.", viDef: "Di chuyển theo chiều dọc lên cao hơn, hướng lên trên.", example: "The kite went upwards further and further.", viExample: "Con diều bay lên cao ngày càng xa hơn." },
  ];

  const storyParagraphs = [
    `Joe was a <b>carpenter</b>. He built houses in the <b>highlands</b>. Joe's wife Stella used a <b>needle</b> and <b>thread</b> to <b>sew</b> <b>elegant</b> clothing. She only used beautiful <b>fabric</b> to make clothes.`,
    `Since they didn't have a lot of money, they lived in an old <b>shed</b>. Water <b>dripped</b> in when it rained. They had broken chairs instead of a <b>couch</b>. But they had <b>coal</b> for heat, and flour from the <b>mill</b> for bread. Together, they <b>trimmed</b> the bushes to make their house look nice. Joe and Stella were poor, but not <b>ashamed</b>. They were happy.`,
    `Sometimes in the evening, they walked downtown. They looked in store windows and dreamed. Stella wanted a hairbrush with an <b>ivory</b> handle. She pulled her hair <b>upwards</b> every day because she didn't have a brush to make it nice. Joe wanted to fix his grandfather's watch.`,
    `For their <b>anniversary</b>, Stella wanted to get Joe what he wanted. But then she did the <b>arithmetic</b>. It would take at least six months to save enough money. Then she had an idea. She cut off all of her hair and sold it.`,
    `Meanwhile, Joe knew that he could never fix his watch. So he <b>polished</b> it and sold it. He made enough to buy the brush.`,
    `On their anniversary, the door <b>burst</b> open. Joe was excited to give Stella his gift. But first, Stella gave him the money to fix the watch. When he saw his wife without any hair, he smiled. "I sold my watch to buy you something," Joe said. He gave her the brush, and she laughed. They were both willing to give up something very special to make each other happy.`,
  ];

  let qId = 1;

  const unit = {
    title: "Unit 8: The Anniversary Gift",
    parts: [
      {
        title: "Word List 1",
        content: buildWordListContent(8, 1, wordList1),
        sections: [
          {
            title: "Exercise 1: Choose the correct word to fill in the blank.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "Because it was their ________, my father bought my mother a gift.", options: ["anniversary", "arithmetic", "fabric", "shed"], correctAnswer: "A", explanation: "Anniversary means a day that celebrates something from the past." },
              { id: qId++, content: "I heard water ________ from the faucet all night long.", options: ["bursting", "sewing", "dripping", "trimming"], correctAnswer: "C", explanation: "To drip means liquid falls a little bit at a time." },
              { id: qId++, content: "In Japan, women wear ________ kimonos on special occasions.", options: ["ashamed", "elegant", "arithmetic", "coal"], correctAnswer: "B", explanation: "Elegant means very fancy and pleasing in appearance." },
              { id: qId++, content: "The towels were made from a very soft ________.", options: ["couch", "needle", "fabric", "mill"], correctAnswer: "C", explanation: "Fabric is cloth used to make clothes, furniture, etc." },
              { id: qId++, content: "You should be ________ of yourself for lying to your teacher.", options: ["elegant", "ashamed", "upward", "ivory"], correctAnswer: "B", explanation: "Ashamed means feeling upset because you did something wrong." },
            ]
          },
          {
            title: "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "My brother is a <i>carpenter</i>, so he knows about building things with wood.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. A carpenter is a person who builds things with wood." },
              { id: qId++, content: "We sat on the <i>coal</i> and watched television together.", options: ["C", "I"], correctAnswer: "B", explanation: "Incorrect. It should be 'couch'. Coal is a hard black rock burned for heat." },
              { id: qId++, content: "When the wind blew, the door <i>burst</i> open suddenly.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Burst means to suddenly break open or apart." },
            ]
          },
          {
            title: "Exercise 3: Choose the word that best matches the definition.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The branch of math dealing with numbers and basic operations", options: ["Fabric", "Arithmetic", "Couch", "Anniversary"], correctAnswer: "B", explanation: "Arithmetic is the branch of math dealing with numbers." },
              { id: qId++, content: "To suddenly break open or apart", options: ["Drip", "Sew", "Burst", "Trim"], correctAnswer: "C", explanation: "Burst means to suddenly break open or apart." },
              { id: qId++, content: "A long, soft seat that many people can sit on", options: ["Shed", "Mill", "Couch", "Fabric"], correctAnswer: "C", explanation: "A couch is a long, soft seat." },
            ]
          }
        ]
      },
      {
        title: "Word List 2",
        content: buildWordListContent(8, 2, wordList2),
        sections: [
          {
            title: "Exercise 1: Choose the correct word to fill in the blank.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The farmer took his wheat to the ________ to make it into flour.", options: ["shed", "mill", "highlands", "thread"], correctAnswer: "B", explanation: "A mill is a building where flour is made." },
              { id: qId++, content: "Mark spent all morning ________ his shoes for the wedding.", options: ["sewing", "trimming", "polishing", "dripping"], correctAnswer: "C", explanation: "To polish means to rub something to make it shiny." },
              { id: qId++, content: "The kite went ________ further and further into the sky.", options: ["upwards", "highlands", "ivory", "thread"], correctAnswer: "A", explanation: "Upwards means moving vertically higher." },
              { id: qId++, content: "I used a ________ and thread to fix the hole in my pants.", options: ["mill", "shed", "needle", "coal"], correctAnswer: "C", explanation: "A needle is a small, sharp piece of metal used to fix clothes." },
            ]
          },
          {
            title: "Exercise 2: Choose the word that best matches the definition.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "A white, hard substance that comes from elephants", options: ["Coal", "Thread", "Ivory", "Fabric"], correctAnswer: "C", explanation: "Ivory is a white, hard substance from elephants." },
              { id: qId++, content: "A small building where you store things like tools", options: ["Mill", "Shed", "Highlands", "Couch"], correctAnswer: "B", explanation: "A shed is a small building for storage." },
              { id: qId++, content: "To cut something a little bit", options: ["Sew", "Polish", "Burst", "Trim"], correctAnswer: "D", explanation: "To trim means to cut something a little bit." },
            ]
          },
          {
            title: "Exercise 3: Mark each statement T for true or F for false.",
            content: `<p class="font-bold text-[16px] text-slate-800 mb-4">True / False</p>`,
            questionType: "TFNG",
            questions: [
              { id: qId++, content: "A 'needle' is a large, blunt piece of wood used for cooking.", options: ["True", "False"], correctAnswer: "False", explanation: "False. A needle is a small, sharp piece of metal used to make or fix clothes." },
              { id: qId++, content: "If something goes 'upwards', it moves vertically higher.", options: ["True", "False"], correctAnswer: "True", explanation: "True. Upwards means moving vertically higher." },
              { id: qId++, content: "The 'highlands' are flat, low-lying areas near the coast.", options: ["True", "False"], correctAnswer: "False", explanation: "False. The highlands are high areas of land, usually with mountains." },
            ]
          }
        ]
      },
      {
        title: "Comprehensive Reading",
        content: buildReadingContent(8, "The Anniversary Gift", storyParagraphs),
        explanation: "Transcript and Reading Passage Explanation",
        sections: [
          {
            title: "Exercise 1: Fill in each blank with the appropriate word, making changes where necessary",
            content: `<p class="font-bold text-[16px] text-slate-800 mb-4">Drag and drop the correct words into the blanks.</p>`,
            questionType: "Kéo thả",
            questions: (() => {
              const dragOptions = ["carpenter", "highlands", "needle", "thread", "sew", "elegant", "fabric", "shed", "dripped", "couch", "coal"];
              const answers = ["carpenter", "highlands", "needle", "thread", "sew", "elegant", "fabric", "shed", "dripped", "couch", "coal"];
              const contentText = `1. Joe was a [ 1 ]. He built houses in the highlands.<br/><br/>2. Joe built houses in the [ 2 ].<br/><br/>3. Stella used a [ 3 ] and thread to sew clothing.<br/><br/>4. She used a needle and [ 4 ] to sew clothing.<br/><br/>5. Stella knew how to [ 5 ] elegant clothing.<br/><br/>6. She made [ 6 ] clothing from beautiful fabric.<br/><br/>7. She only used beautiful [ 7 ] to make clothes.<br/><br/>8. They lived in an old [ 8 ].<br/><br/>9. Water [ 9 ] in when it rained.<br/><br/>10. They had broken chairs instead of a [ 10 ].<br/><br/>11. They had [ 11 ] for heat.`;
              const questions = [];
              for (let i = 0; i < answers.length; i++) {
                questions.push({
                  id: qId++,
                  content: i === 0 ? contentText : "",
                  options: [...dragOptions],
                  correctAnswer: answers[i]
                });
              }
              return questions;
            })()
          },
          {
            title: "Exercise 2: Reading Comprehension",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "What did Joe do for a living?", options: ["He was a mill worker.", "He was a carpenter.", "He sold ivory.", "He polished shoes."], correctAnswer: "B", explanation: "The passage states: 'Joe was a carpenter. He built houses in the highlands.'" },
              { id: qId++, content: "Why were Joe and Stella not ashamed of their poverty?", options: ["They had elegant furniture.", "They had plenty of money.", "They were happy together.", "They lived in the highlands."], correctAnswer: "C", explanation: "The passage states: 'Joe and Stella were poor, but not ashamed. They were happy.'" },
              { id: qId++, content: "What did Stella want as a gift?", options: ["A needle and thread", "An elegant coat", "A hairbrush with an ivory handle", "A new couch"], correctAnswer: "C", explanation: "The passage states: 'Stella wanted a hairbrush with an ivory handle.'" },
              { id: qId++, content: "How did Stella get the money for Joe's gift?", options: ["She sold fabric.", "She did arithmetic.", "She sold her hair.", "She polished ivory."], correctAnswer: "C", explanation: "The passage states: 'She cut off all of her hair and sold it.'" },
              { id: qId++, content: "What happened when Joe gave Stella the brush?", options: ["She cried.", "She was ashamed.", "She laughed.", "She burst into tears."], correctAnswer: "C", explanation: "The passage states: 'He gave her the brush, and she laughed.'" },
            ]
          }
        ]
      }
    ],
    basicInfo: {
      skill: "MCQ (Standard)",
      title: "Unit 8: The Anniversary Gift",
      category: "exercise",
      courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
      timeLimit: 40
    }
  };

  return unit;
}

// ============================================================
// UNIT 9: The Tale of Bartelby O'Boyle
// ============================================================
function buildUnit9() {
  const wordList1 = [
    { word: "admire", pron: "[ədˈmaɪər]", pos: "v.", def: "to like someone for what they do.", viDef: "Thích ai đó vì những gì họ làm, ngưỡng mộ.", example: "I admire my brother for his hard work.", viExample: "Tôi ngưỡng mộ anh trai vì sự chăm chỉ của anh ấy." },
    { word: "aid", pron: "[eɪd]", pos: "v.", def: "to help someone when they need something.", viDef: "Giúp đỡ ai đó khi họ cần, viện trợ.", example: "The doctor aided the boy after his accident.", viExample: "Bác sĩ đã hỗ trợ cậu bé sau tai nạn." },
    { word: "attempt", pron: "[əˈtempt]", pos: "v.", def: "to try to do something.", viDef: "Cố gắng làm một việc gì đó, nỗ lực.", example: "I am attempting to learn English.", viExample: "Tôi đang cố gắng học tiếng Anh." },
    { word: "authority", pron: "[əˈθɔːrəti]", pos: "n.", def: "the power that someone has because of their position.", viDef: "Quyền lực mà ai đó có nhờ vị trí của họ, thẩm quyền.", example: "The policeman has authority on the streets.", viExample: "Cảnh sát có thẩm quyền trên đường phố." },
    { word: "capital", pron: "[ˈkæpɪtl]", pos: "n.", def: "an important city where a country's leaders live and work.", viDef: "Thành phố quan trọng nơi các nhà lãnh đạo sống và làm việc, thủ đô.", example: "We will visit the capital to learn about our government.", viExample: "Chúng tôi sẽ thăm thủ đô để tìm hiểu về chính phủ." },
    { word: "cooperate", pron: "[koʊˈɑːpəreɪt]", pos: "v.", def: "to work together to do something.", viDef: "Làm việc cùng nhau để thực hiện điều gì đó, hợp tác.", example: "The students cooperated to clean up the classroom.", viExample: "Các học sinh hợp tác dọn dẹp lớp học." },
    { word: "defend", pron: "[dɪˈfend]", pos: "v.", def: "to protect someone or something from attack.", viDef: "Bảo vệ ai đó hoặc cái gì đó khỏi sự tấn công.", example: "The soldiers defended the town from the invaders.", viExample: "Các chiến sĩ bảo vệ thị trấn khỏi quân xâm lược." },
    { word: "destruction", pron: "[dɪˈstrʌkʃn]", pos: "n.", def: "damage to something so bad that it can't be fixed.", viDef: "Thiệt hại nghiêm trọng đến mức không thể sửa chữa, sự tàn phá.", example: "After the big fire, there was much destruction in the city.", viExample: "Sau trận cháy lớn, thành phố bị tàn phá nặng nề." },
    { word: "disorder", pron: "[dɪsˈɔːrdər]", pos: "n.", def: "a lack of order, or a complete mess.", viDef: "Thiếu trật tự, hoặc tình trạng hỗn loạn.", example: "The teacher's desk had many papers in disorder.", viExample: "Bàn giáo viên có nhiều giấy tờ bừa bộn." },
    { word: "division", pron: "[dɪˈvɪʒn]", pos: "n.", def: "the act of making smaller groups out of a larger one.", viDef: "Hành động chia nhóm lớn thành các nhóm nhỏ hơn, sự phân chia.", example: "The chart had six divisions which all had different colors.", viExample: "Biểu đồ có sáu phần được phân chia với các màu khác nhau." },
  ];

  const wordList2 = [
    { word: "enable", pron: "[ɪˈneɪbl]", pos: "v.", def: "to make it possible for someone to do something.", viDef: "Làm cho ai đó có thể làm được việc gì, cho phép.", example: "Having the key enabled us to open the door.", viExample: "Có chìa khóa cho phép chúng tôi mở cửa." },
    { word: "frustrate", pron: "[ˈfrʌstreɪt]", pos: "v.", def: "to prevent someone from fulfilling their desire.", viDef: "Ngăn cản ai đó thực hiện mong muốn của họ, gây thất vọng.", example: "The machine frustrated me because I could not fix it.", viExample: "Cái máy làm tôi bực bội vì tôi không thể sửa nó." },
    { word: "govern", pron: "[ˈɡʌvərn]", pos: "v.", def: "to control the public business of a country, state, or city.", viDef: "Điều hành công việc công cộng của một quốc gia, bang hoặc thành phố, cai trị.", example: "The United States is governed from the White House.", viExample: "Hoa Kỳ được điều hành từ Nhà Trắng." },
    { word: "plenty", pron: "[ˈplenti]", pos: "n.", def: "more of something than you need.", viDef: "Nhiều hơn những gì bạn cần, dồi dào.", example: "The school had plenty of books for the students to read.", viExample: "Trường có rất nhiều sách cho học sinh đọc." },
    { word: "relieve", pron: "[rɪˈliːv]", pos: "v.", def: "to make someone feel less pain.", viDef: "Làm cho ai đó cảm thấy bớt đau, giảm nhẹ.", example: "The medicine relieved the sick boy.", viExample: "Thuốc đã làm giảm đau cho cậu bé bị bệnh." },
    { word: "reputation", pron: "[ˌrepjuˈteɪʃn]", pos: "n.", def: "the opinion that people have about someone.", viDef: "Ý kiến mà mọi người có về ai đó, danh tiếng.", example: "The doctor had a reputation for helping people.", viExample: "Bác sĩ có danh tiếng về việc giúp đỡ mọi người." },
    { word: "royal", pron: "[ˈrɔɪəl]", pos: "adj.", def: "belonging to a king or queen.", viDef: "Thuộc về vua hoặc hoàng hậu, hoàng gia.", example: "The king sat upon the royal throne.", viExample: "Nhà vua ngồi trên ngai vàng hoàng gia." },
    { word: "slave", pron: "[sleɪv]", pos: "n.", def: "a person who is not free and must work for someone else.", viDef: "Người không tự do và phải làm việc cho người khác, nô lệ.", example: "The slave worked very hard all day long.", viExample: "Người nô lệ làm việc rất vất vả cả ngày." },
    { word: "struggle", pron: "[ˈstrʌɡl]", pos: "v.", def: "to fight against someone or something.", viDef: "Chiến đấu chống lại ai đó hoặc cái gì đó, đấu tranh.", example: "The kids struggled with each other for the toy.", viExample: "Lũ trẻ giành giật nhau món đồ chơi." },
    { word: "stupid", pron: "[ˈstuːpɪd]", pos: "adj.", def: "lacking intelligence.", viDef: "Thiếu trí thông minh, ngu ngốc.", example: "He said something stupid that made everyone angry.", viExample: "Anh ấy nói điều gì đó ngu ngốc khiến mọi người tức giận." },
  ];

  const storyParagraphs = [
    `Long ago, there was a clever man by the name of Bartelby O'Boyle. As a boy, he was kept as a <b>slave</b> by the <b>royal</b> family. He saw other children play, but he always had to work. This <b>frustrated</b> him very much. But he was not <b>stupid</b>, and he wanted to change things.`,
    `Then one day there was a <b>struggle</b> for <b>authority</b> in the kingdom. There was a <b>division</b> of the people, and one group fought against another group to see which would <b>govern</b> the kingdom. There was <b>disorder</b> in the kingdom. Bartelby ran away. He saw much fighting and <b>destruction</b>. Many people had nothing to eat; Bartelby decided to <b>aid</b> them. He would help them get food. But how?`,
    `Bartelby went to the <b>capital</b> to find an answer. There, he met a man named Gilliam. A group of men <b>attempted</b> to hurt Gilliam. Bartelby <b>defended</b> him. Then, he gave Gilliam some food to <b>relieve</b> his hunger. After that, the two became friends. They took food from the rich and gave it to the poor.`,
    `Soon, other people <b>cooperated</b> with them. Working together <b>enabled</b> them to take more food, but they only took food from people who had <b>plenty</b>, and they always gave it to those who had none. Because of this, Bartelby gained a <b>reputation</b> across the kingdom. Even today, many people <b>admire</b> him for helping the poor.`,
  ];

  let qId = 1;

  const unit = {
    title: "Unit 9: The Tale of Bartelby O'Boyle",
    parts: [
      {
        title: "Word List 1",
        content: buildWordListContent(9, 1, wordList1),
        sections: [
          {
            title: "Exercise 1: Choose the correct word to fill in the blank.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The soldiers ________ the town from the invaders.", options: ["admired", "defended", "attempted", "aided"], correctAnswer: "B", explanation: "To defend means to protect someone or something from attack." },
              { id: qId++, content: "The policeman has ________ on the streets.", options: ["destruction", "disorder", "authority", "division"], correctAnswer: "C", explanation: "Authority is the power someone has because of their position." },
              { id: qId++, content: "After the big fire, there was much ________ in the city.", options: ["capital", "division", "cooperation", "destruction"], correctAnswer: "D", explanation: "Destruction is damage so bad that it can't be fixed." },
              { id: qId++, content: "We will visit the ________ to learn about our government.", options: ["capital", "disorder", "division", "authority"], correctAnswer: "A", explanation: "A capital is an important city where a country's leaders live and work." },
              { id: qId++, content: "I am ________ to learn English this year.", options: ["aiding", "admiring", "attempting", "defending"], correctAnswer: "C", explanation: "To attempt means to try to do something." },
            ]
          },
          {
            title: "Exercise 2: Choose the word that best matches the definition.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "To like someone for what they do", options: ["Aid", "Attempt", "Admire", "Defend"], correctAnswer: "C", explanation: "Admire means to like someone for what they do." },
              { id: qId++, content: "A lack of order, or a complete mess", options: ["Division", "Disorder", "Destruction", "Authority"], correctAnswer: "B", explanation: "Disorder is a lack of order, or a complete mess." },
              { id: qId++, content: "To help someone when they need something", options: ["Cooperate", "Govern", "Aid", "Attempt"], correctAnswer: "C", explanation: "To aid means to help someone when they need something." },
            ]
          },
          {
            title: "Exercise 3: Mark each statement T for true or F for false.",
            content: `<p class="font-bold text-[16px] text-slate-800 mb-4">True / False</p>`,
            questionType: "TFNG",
            questions: [
              { id: qId++, content: "If there is a 'division' of people, they are all united together.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Division means making smaller groups out of a larger one." },
              { id: qId++, content: "A 'capital' is an important city where a country's leaders live and work.", options: ["True", "False"], correctAnswer: "True", explanation: "True. A capital is where a country's leaders live and work." },
              { id: qId++, content: "If you 'attempt' something, you give up before trying.", options: ["True", "False"], correctAnswer: "False", explanation: "False. To attempt means to try to do something." },
            ]
          }
        ]
      },
      {
        title: "Word List 2",
        content: buildWordListContent(9, 2, wordList2),
        sections: [
          {
            title: "Exercise 1: Choose the correct word to fill in the blank.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The medicine ________ the sick boy of his pain.", options: ["frustrated", "governed", "relieved", "struggled"], correctAnswer: "C", explanation: "To relieve means to make someone feel less pain." },
              { id: qId++, content: "The king sat upon the ________ throne.", options: ["stupid", "royal", "slave", "plenty"], correctAnswer: "B", explanation: "Royal describes something belonging to a king or queen." },
              { id: qId++, content: "The school had ________ of books for the students to read.", options: ["reputation", "plenty", "struggle", "frustration"], correctAnswer: "B", explanation: "Plenty means having more of something than you need." },
              { id: qId++, content: "Having the key ________ us to open the door.", options: ["frustrated", "enabled", "struggled", "governed"], correctAnswer: "B", explanation: "To enable means to make it possible for someone to do something." },
            ]
          },
          {
            title: "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The doctor had a good <i>reputation</i> for helping people.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Reputation is the opinion people have about someone." },
              { id: qId++, content: "The children <i>frustrated</i> happily in the playground.", options: ["C", "I"], correctAnswer: "B", explanation: "Incorrect. Frustrated means prevented from fulfilling a desire, not playing happily." },
              { id: qId++, content: "The <i>slave</i> worked very hard all day long without any freedom.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. A slave is a person who is not free and must work for someone else." },
            ]
          },
          {
            title: "Exercise 3: Choose the word that best matches the definition.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "To control the public business of a country, state, or city", options: ["Enable", "Frustrate", "Govern", "Relieve"], correctAnswer: "C", explanation: "Govern means to control the public business of a country." },
              { id: qId++, content: "To fight against someone or something", options: ["Struggle", "Cooperate", "Enable", "Admire"], correctAnswer: "A", explanation: "Struggle means to fight against someone or something." },
              { id: qId++, content: "Lacking intelligence", options: ["Royal", "Slave", "Stupid", "Plenty"], correctAnswer: "C", explanation: "Stupid means lacking intelligence." },
            ]
          }
        ]
      },
      {
        title: "Comprehensive Reading",
        content: buildReadingContent(9, "The Tale of Bartelby O'Boyle", storyParagraphs),
        explanation: "Transcript and Reading Passage Explanation",
        sections: [
          {
            title: "Exercise 1: Fill in each blank with the appropriate word, making changes where necessary",
            content: `<p class="font-bold text-[16px] text-slate-800 mb-4">Drag and drop the correct words into the blanks.</p>`,
            questionType: "Kéo thả",
            questions: (() => {
              const dragOptions = ["slave", "royal", "frustrated", "stupid", "struggle", "authority", "division", "govern", "disorder", "destruction", "aid"];
              const answers = ["slave", "royal", "frustrated", "stupid", "struggle", "authority", "division", "govern", "disorder", "destruction", "aid"];
              const contentText = `1. Bartelby was kept as a [ 1 ] by the royal family.<br/><br/>2. The [ 2 ] family kept him as a servant.<br/><br/>3. Not being able to play [ 3 ] Bartelby very much.<br/><br/>4. But he was not [ 4 ], and he wanted to change things.<br/><br/>5. There was a [ 5 ] for authority in the kingdom.<br/><br/>6. Groups fought to see who would have [ 6 ].<br/><br/>7. There was a [ 7 ] of the people into different groups.<br/><br/>8. Each group wanted to [ 8 ] the kingdom.<br/><br/>9. There was [ 9 ] in the kingdom.<br/><br/>10. He saw much fighting and [ 10 ].<br/><br/>11. Bartelby decided to [ 11 ] the hungry people.`;
              const questions = [];
              for (let i = 0; i < answers.length; i++) {
                questions.push({
                  id: qId++,
                  content: i === 0 ? contentText : "",
                  options: [...dragOptions],
                  correctAnswer: answers[i]
                });
              }
              return questions;
            })()
          },
          {
            title: "Exercise 2: Reading Comprehension",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "What is this story mainly about?", options: ["How a slave became a king", "How a stupid mistake made Bartelby a slave", "How a man found plenty of food", "How a man aided poor people"], correctAnswer: "D", explanation: "The story is about how Bartelby aided the poor by taking food from the rich and giving it to those who had none." },
              { id: qId++, content: "What did Bartelby do in the capital?", options: ["He cooperated with his group of friends.", "He enabled Gilliam to have authority over the king.", "He relieved Gilliam of his hunger.", "He found a mask to wear."], correctAnswer: "C", explanation: "The passage states: 'he gave Gilliam some food to relieve his hunger.'" },
              { id: qId++, content: "In paragraph 1, we can infer that ________", options: ["Bartelby did not like the royal family", "The family attempted to cause disorder", "The other children were not clever", "Bartelby had a bad reputation"], correctAnswer: "A", explanation: "Since Bartelby was frustrated being a slave, we can infer he did not like the royal family." },
              { id: qId++, content: "According to the passage, all the following are true EXCEPT", options: ["People today still admire Bartelby", "Gilliam struggled with Bartelby", "Bartelby defended Gilliam", "The fighting caused destruction"], correctAnswer: "B", explanation: "Gilliam did not struggle with Bartelby. They became friends after Bartelby defended him." },
            ]
          }
        ]
      }
    ],
    basicInfo: {
      skill: "MCQ (Standard)",
      title: "Unit 9: The Tale of Bartelby O'Boyle",
      category: "exercise",
      courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
      timeLimit: 40
    }
  };

  return unit;
}

// ============================================================
// UNIT 10: Anna the Babysitter
// ============================================================
function buildUnit10() {
  const wordList1 = [
    { word: "absence", pron: "[ˈæbsəns]", pos: "n.", def: "the state of something being away.", viDef: "Trạng thái vắng mặt hoặc thiếu vắng.", example: "There is an absence of sand in the hourglass.", viExample: "Đồng hồ cát không còn cát bên trong." },
    { word: "aloud", pron: "[əˈlaʊd]", pos: "adv.", def: "saying something so that others can hear you.", viDef: "Nói điều gì đó để người khác có thể nghe được, thành tiếng.", example: "My father often reads stories aloud to me and my sister.", viExample: "Bố tôi thường đọc truyện thành tiếng cho tôi và em gái." },
    { word: "bald", pron: "[bɔːld]", pos: "adj.", def: "having no hair.", viDef: "Không có tóc, hói đầu.", example: "My oldest brother is bald.", viExample: "Anh cả của tôi bị hói." },
    { word: "blanket", pron: "[ˈblæŋkɪt]", pos: "n.", def: "a piece of cloth used to keep warm or to sit upon.", viDef: "Miếng vải dùng để giữ ấm hoặc ngồi lên, chăn.", example: "I laid a blanket on the ground for a picnic.", viExample: "Tôi trải một tấm chăn trên mặt đất để đi dã ngoại." },
    { word: "creep", pron: "[kriːp]", pos: "v.", def: "to move quietly and slowly.", viDef: "Di chuyển nhẹ nhàng và chậm rãi, bò, rón rén.", example: "The cat slowly crept down the tree.", viExample: "Con mèo từ từ bò xuống cây." },
    { word: "divorce", pron: "[dɪˈvɔːrs]", pos: "n.", def: "an event in which a marriage is ended.", viDef: "Sự kiện kết thúc hôn nhân, ly hôn.", example: "Divorce rates have increased in the past twenty years.", viExample: "Tỷ lệ ly hôn đã tăng trong hai mươi năm qua." },
    { word: "imitate", pron: "[ˈɪmɪteɪt]", pos: "v.", def: "to do exactly what someone else does.", viDef: "Làm giống hệt những gì người khác làm, bắt chước.", example: "He imitated his favorite superhero by putting on a costume.", viExample: "Anh ấy bắt chước siêu anh hùng yêu thích bằng cách mặc trang phục." },
    { word: "infant", pron: "[ˈɪnfənt]", pos: "n.", def: "a baby.", viDef: "Em bé, trẻ sơ sinh.", example: "The infant cried all night.", viExample: "Đứa trẻ sơ sinh khóc suốt đêm." },
    { word: "kidnap", pron: "[ˈkɪdnæp]", pos: "v.", def: "to take someone illegally.", viDef: "Bắt ai đó một cách bất hợp pháp, bắt cóc.", example: "She was terrified to find out her son was kidnapped.", viExample: "Cô ấy kinh hoàng khi biết con trai mình bị bắt cóc." },
    { word: "nap", pron: "[næp]", pos: "n.", def: "a short sleep, usually during the day.", viDef: "Giấc ngủ ngắn, thường vào ban ngày, giấc ngủ trưa.", example: "I took a short nap because I stayed up late last night.", viExample: "Tôi ngủ trưa một lát vì thức khuya đêm qua." },
  ];

  const wordList2 = [
    { word: "nowhere", pron: "[ˈnoʊwer]", pos: "adv.", def: "used to say that a place or thing does not exist.", viDef: "Dùng để nói rằng một nơi hoặc vật không tồn tại, không đâu.", example: "Unfortunately, water was nowhere to be found.", viExample: "Thật không may, nước không thể tìm thấy ở đâu." },
    { word: "pat", pron: "[pæt]", pos: "v.", def: "to hit something softly with your hand.", viDef: "Đập nhẹ vào cái gì đó bằng tay, vỗ nhẹ.", example: "I patted some lotion onto my face.", viExample: "Tôi vỗ nhẹ kem dưỡng lên mặt." },
    { word: "relief", pron: "[rɪˈliːf]", pos: "n.", def: "a feeling you get when something bad or challenging ends.", viDef: "Cảm giác khi điều gì đó tệ hoặc khó khăn kết thúc, sự nhẹ nhõm.", example: "I felt a sense of relief when I heard the good news.", viExample: "Tôi cảm thấy nhẹ nhõm khi nghe tin tốt." },
    { word: "reproduce", pron: "[ˌriːprəˈduːs]", pos: "v.", def: "to make something exactly how someone else did it.", viDef: "Làm lại điều gì đó giống hệt cách người khác đã làm, tái tạo.", example: "The children tried to reproduce their house using toy blocks.", viExample: "Lũ trẻ cố tái tạo ngôi nhà của chúng bằng các khối đồ chơi." },
    { word: "rhyme", pron: "[raɪm]", pos: "n.", def: "words having the same sounds at the end.", viDef: "Các từ có âm giống nhau ở cuối, vần điệu.", example: "Humpty Dumpty is an old rhyme that children learn in school.", viExample: "Humpty Dumpty là một bài vần cũ mà trẻ em học ở trường." },
    { word: "suck", pron: "[sʌk]", pos: "v.", def: "to put something in your mouth and try to get flavor from it.", viDef: "Đặt thứ gì đó vào miệng và cố lấy hương vị, mút.", example: "The baby sucked milk from her bottle.", viExample: "Em bé mút sữa từ bình." },
    { word: "urgent", pron: "[ˈɜːrdʒənt]", pos: "adj.", def: "important and needing to be done now.", viDef: "Quan trọng và cần được thực hiện ngay, khẩn cấp.", example: "He had to leave now; it was urgent.", viExample: "Anh ấy phải đi ngay; việc rất khẩn cấp." },
    { word: "vanish", pron: "[ˈvænɪʃ]", pos: "v.", def: "to go away suddenly.", viDef: "Biến mất đột ngột.", example: "All the passengers vanished from the train station.", viExample: "Tất cả hành khách biến mất khỏi nhà ga." },
    { word: "wagon", pron: "[ˈwæɡən]", pos: "n.", def: "a cart used to carry heavy things.", viDef: "Xe đẩy dùng để chở đồ nặng, xe kéo.", example: "He used his wagon to carry some of his gifts.", viExample: "Anh ấy dùng xe kéo để chở một số món quà." },
    { word: "wrinkle", pron: "[ˈrɪŋkl]", pos: "n.", def: "a line on a person's face that happens as they get old.", viDef: "Đường nhăn trên mặt người khi họ già đi, nếp nhăn.", example: "My grandfather has some wrinkles on his face.", viExample: "Ông tôi có vài nếp nhăn trên mặt." },
  ];

  const storyParagraphs = [
    `Since her parents got a <b>divorce</b>, Anna has had to help her mother. In her mother's <b>absence</b>, Anna takes care of Grace, the baby. At first, Anna thought it was an easy job.`,
    `One afternoon, Anna played with Grace. She meowed like a cat and Grace <b>imitated</b> her. In fact, Grace <b>reproduced</b> every sound that Anna made. She took her sister outside. She put Grace in the <b>wagon</b>, but there was <b>nowhere</b> for them to go. So they went back inside.`,
    `Anna put the <b>infant</b> on the floor and went into her room. But when she came back, Grace had <b>vanished</b>! Anna looked everywhere, but she could not find her sister. Maybe the baby had been <b>kidnapped</b>! "Where are you?" Anna called <b>aloud</b>.`,
    `The situation was becoming <b>urgent</b>. She wanted to call her mom, but she didn't want her to think Anna couldn't do the job. Anna sat down. What was she going to do?`,
    `But then, Anna heard something. It was coming from her room. "Grace?" She got down on her knees and looked under the bed. She could see Grace's <b>bald</b> head. Grace had followed Anna into her room and <b>crept</b> under the bed.`,
    `"What a <b>relief</b>!" Anna cried.`,
    `She picked up her sister and <b>patted</b> her on the head. Her head was soft and had no <b>wrinkles</b>. Grace was <b>sucking</b> on her thumb and looked tired. So, Anna wrapped her in a <b>blanket</b> and sang <b>rhymes</b> for her. Then she put Grace in bed for a <b>nap</b>.`,
    `After that afternoon, Anna knew that taking care of Grace was not an easy job. It takes a lot of work to take care of a baby!`,
  ];

  let qId = 1;

  const unit = {
    title: "Unit 10: Anna the Babysitter",
    parts: [
      {
        title: "Word List 1",
        content: buildWordListContent(10, 1, wordList1),
        sections: [
          {
            title: "Exercise 1: Choose the correct word to fill in the blank.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "My oldest brother is ________ — he has no hair at all.", options: ["infant", "bald", "absent", "aloud"], correctAnswer: "B", explanation: "Bald means having no hair." },
              { id: qId++, content: "He ________ his favorite superhero by putting on a costume.", options: ["kidnapped", "imitated", "crept", "divorced"], correctAnswer: "B", explanation: "To imitate means to do exactly what someone else does." },
              { id: qId++, content: "She was terrified to find out her son was ________.", options: ["napping", "creeping", "kidnapped", "absent"], correctAnswer: "C", explanation: "To kidnap means to take someone illegally." },
              { id: qId++, content: "I took a short ________ because I stayed up late last night.", options: ["nap", "blanket", "divorce", "absence"], correctAnswer: "A", explanation: "A nap is a short sleep, usually during the day." },
              { id: qId++, content: "The cat slowly ________ down the tree without making a sound.", options: ["imitated", "sucked", "crept", "divorced"], correctAnswer: "C", explanation: "To creep means to move quietly and slowly." },
            ]
          },
          {
            title: "Exercise 2: Choose the word that best matches the definition.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The state of something being away", options: ["Nap", "Absence", "Divorce", "Blanket"], correctAnswer: "B", explanation: "Absence is the state of something being away." },
              { id: qId++, content: "An event in which a marriage is ended", options: ["Infant", "Kidnap", "Divorce", "Creep"], correctAnswer: "C", explanation: "Divorce is an event in which a marriage is ended." },
              { id: qId++, content: "A baby", options: ["Infant", "Nap", "Bald", "Blanket"], correctAnswer: "A", explanation: "An infant is a baby." },
            ]
          },
          {
            title: "Exercise 3: Mark each statement T for true or F for false.",
            content: `<p class="font-bold text-[16px] text-slate-800 mb-4">True / False</p>`,
            questionType: "TFNG",
            questions: [
              { id: qId++, content: "If you say something 'aloud', you whisper it so nobody can hear.", options: ["True", "False"], correctAnswer: "False", explanation: "False. Aloud means saying something so others can hear you." },
              { id: qId++, content: "A 'blanket' is a piece of cloth used to keep warm.", options: ["True", "False"], correctAnswer: "True", explanation: "True. A blanket is used to keep warm or to sit upon." },
              { id: qId++, content: "To 'creep' means to run fast and make loud noises.", options: ["True", "False"], correctAnswer: "False", explanation: "False. To creep means to move quietly and slowly." },
            ]
          }
        ]
      },
      {
        title: "Word List 2",
        content: buildWordListContent(10, 2, wordList2),
        sections: [
          {
            title: "Exercise 1: Choose the correct word to fill in the blank.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "I felt a sense of ________ when I heard the good news.", options: ["wrinkle", "relief", "wagon", "rhyme"], correctAnswer: "B", explanation: "Relief is a feeling you get when something bad ends." },
              { id: qId++, content: "All the passengers ________ from the train station suddenly.", options: ["patted", "reproduced", "vanished", "sucked"], correctAnswer: "C", explanation: "To vanish means to go away suddenly." },
              { id: qId++, content: "He had to leave now; the situation was ________.", options: ["nowhere", "urgent", "wrinkled", "pat"], correctAnswer: "B", explanation: "Urgent means important and needing to be done now." },
              { id: qId++, content: "My grandfather has some ________ on his face from getting old.", options: ["rhymes", "wrinkles", "wagons", "reliefs"], correctAnswer: "B", explanation: "A wrinkle is a line on a person's face that happens as they get old." },
            ]
          },
          {
            title: "Exercise 2: Write C if the italicized word is used correctly. Write I if the word is used incorrectly.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "The baby <i>sucked</i> milk from her bottle happily.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. To suck means to put something in your mouth and try to get flavor." },
              { id: qId++, content: "He used his <i>rhyme</i> to carry heavy boxes across the yard.", options: ["C", "I"], correctAnswer: "B", explanation: "Incorrect. It should be 'wagon'. A rhyme is words having the same sounds at the end." },
              { id: qId++, content: "Water was <i>nowhere</i> to be found in the desert.", options: ["C", "I"], correctAnswer: "A", explanation: "Correct. Nowhere means a place or thing does not exist." },
            ]
          },
          {
            title: "Exercise 3: Choose the word that best matches the definition.",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "To make something exactly how someone else did it", options: ["Pat", "Reproduce", "Vanish", "Suck"], correctAnswer: "B", explanation: "To reproduce means to make something exactly how someone else did it." },
              { id: qId++, content: "To hit something softly with your hand", options: ["Suck", "Creep", "Pat", "Vanish"], correctAnswer: "C", explanation: "To pat means to hit something softly with your hand." },
              { id: qId++, content: "A cart used to carry heavy things", options: ["Blanket", "Wagon", "Wrinkle", "Rhyme"], correctAnswer: "B", explanation: "A wagon is a cart used to carry heavy things." },
            ]
          }
        ]
      },
      {
        title: "Comprehensive Reading",
        content: buildReadingContent(10, "Anna the Babysitter", storyParagraphs),
        explanation: "Transcript and Reading Passage Explanation",
        sections: [
          {
            title: "Exercise 1: Fill in each blank with the appropriate word, making changes where necessary",
            content: `<p class="font-bold text-[16px] text-slate-800 mb-4">Drag and drop the correct words into the blanks.</p>`,
            questionType: "Kéo thả",
            questions: (() => {
              const dragOptions = ["divorce", "absence", "imitated", "reproduced", "wagon", "nowhere", "infant", "vanished", "kidnapped", "aloud", "urgent"];
              const answers = ["divorce", "absence", "imitated", "reproduced", "wagon", "nowhere", "infant", "vanished", "kidnapped", "aloud", "urgent"];
              const contentText = `1. Anna's parents got a [ 1 ].<br/><br/>2. In her mother's [ 2 ], Anna took care of Grace.<br/><br/>3. Grace [ 3 ] the sounds Anna made, like a cat meowing.<br/><br/>4. Grace [ 4 ] every sound that Anna made.<br/><br/>5. Anna put Grace in the [ 5 ] and took her outside.<br/><br/>6. There was [ 6 ] for them to go.<br/><br/>7. Anna put the [ 7 ] on the floor and went to her room.<br/><br/>8. When she came back, Grace had [ 8 ]!<br/><br/>9. Maybe the baby had been [ 9 ]!<br/><br/>10. "Where are you?" Anna called [ 10 ].<br/><br/>11. The situation was becoming [ 11 ].`;
              const questions = [];
              for (let i = 0; i < answers.length; i++) {
                questions.push({
                  id: qId++,
                  content: i === 0 ? contentText : "",
                  options: [...dragOptions],
                  correctAnswer: answers[i]
                });
              }
              return questions;
            })()
          },
          {
            title: "Exercise 2: Reading Comprehension",
            content: "",
            questionType: "Trắc nghiệm",
            questions: [
              { id: qId++, content: "Why does Anna take care of Grace?", options: ["Because her parents got a divorce and she helps her mother.", "Because Grace is her own baby.", "Because she wants to earn money.", "Because her teacher asked her to."], correctAnswer: "A", explanation: "The passage states: 'Since her parents got a divorce, Anna has had to help her mother.'" },
              { id: qId++, content: "What happened when Anna came back from her room?", options: ["Grace was sleeping.", "Grace had vanished.", "Grace was crying.", "Grace was playing."], correctAnswer: "B", explanation: "The passage states: 'when she came back, Grace had vanished!'" },
              { id: qId++, content: "Where did Anna find Grace?", options: ["In the wagon", "In the kitchen", "Under the bed", "In the closet"], correctAnswer: "C", explanation: "The passage states: 'She got down on her knees and looked under the bed. She could see Grace's bald head.'" },
              { id: qId++, content: "What did Anna do to help Grace fall asleep?", options: ["She read a book aloud.", "She wrapped her in a blanket and sang rhymes.", "She patted her and gave her a wagon.", "She played with Grace outside."], correctAnswer: "B", explanation: "The passage states: 'Anna wrapped her in a blanket and sang rhymes for her. Then she put Grace in bed for a nap.'" },
              { id: qId++, content: "Which is NOT something Anna did with Grace?", options: ["Went outside in the wagon", "Patted her on the head", "Read a book aloud", "Sang rhymes for her"], correctAnswer: "C", explanation: "Anna never read a book aloud to Grace in the story." },
            ]
          }
        ]
      }
    ],
    basicInfo: {
      skill: "MCQ (Standard)",
      title: "Unit 10: Anna the Babysitter",
      category: "exercise",
      courseId: "239a64f0-c106-40e5-a6e2-4e685a0d70fb",
      timeLimit: 40
    }
  };

  return unit;
}

// ============================================================
// MAIN: Generate all 3 JSON files
// ============================================================
const unit8 = buildUnit8();
const unit9 = buildUnit9();
const unit10 = buildUnit10();

fs.writeFileSync('public/unit8_ielts.json', JSON.stringify(unit8, null, 2));
console.log('✅ Created public/unit8_ielts.json');

fs.writeFileSync('public/unit9_ielts.json', JSON.stringify(unit9, null, 2));
console.log('✅ Created public/unit9_ielts.json');

fs.writeFileSync('public/unit10_ielts.json', JSON.stringify(unit10, null, 2));
console.log('✅ Created public/unit10_ielts.json');

console.log('\n🎉 All 3 unit JSON files have been generated!');
