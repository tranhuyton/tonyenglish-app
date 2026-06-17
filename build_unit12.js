const fs = require("fs");

const words = [
  { word: "abuse", pos: "v.", pron: "[əbjúːz]", def: "To abuse someone or something means to hurt them on purpose.", ex: "The mean man abused his dog when it barked too loudly." },
  { word: "afford", pos: "v.", pron: "[əfɔ́ːrd]", def: "To afford something means you have enough money to pay for it.", ex: "I've been saving my money, so I can afford to buy a new bike." },
  { word: "bake", pos: "v.", pron: "[beik]", def: "To bake means to cook food with heat.", ex: "My sister is a good cook. She bakes delicious cakes." },
  { word: "bean", pos: "n.", pron: "[biːn]", def: "A bean is a plant seed that is good to eat.", ex: "There are many different kinds of beans to eat." },
  { word: "candle", pos: "n.", pron: "[kǽndl]", def: "A candle is a stick of wax that is lit on fire for light or heat.", ex: "When the lights went out, we lit some candles." },
  { word: "convert", pos: "v.", pron: "[kənvə́ːrt]", def: "To convert something means to change it into something else.", ex: "The man converted his messy field into a garden of flowers." },
  { word: "debt", pos: "n.", pron: "[det]", def: "A debt is an amount of money that a person owes.", ex: "I have not paid my gas bill. I owe a debt to the gas company." },
  { word: "decrease", pos: "v.", pron: "[dikríːs]", def: "To decrease something is to make it less than it was before.", ex: "Hiring more police officers has decreased crime in the city." },
  { word: "fault", pos: "n.", pron: "[fɔːlt]", def: "A fault is a mistake.", ex: "It is my fault that the cat ran away. I left the door open." },
  { word: "fund", pos: "n.", pron: "[fʌnd]", def: "A fund is an amount of money that people have.", ex: "We all put money into our club's fund." },
  { word: "generous", pos: "adj.", pron: "[dʒénərəs]", def: "When someone is generous, they like to give things to people.", ex: "The generous man donated several new computers to our school." },
  { word: "ingredient", pos: "n.", pron: "[ingríːdiənt]", def: "An ingredient is something that is part of a food dish.", ex: "The main ingredients in cake are eggs, sugar and flour." },
  { word: "insist", pos: "v.", pron: "[insíst]", def: "To insist means to be firm in telling people what to do.", ex: "I insist that you try some of these cookies." },
  { word: "mess", pos: "n.", pron: "[mes]", def: "A mess is a condition that is not clean or neat.", ex: "Heather's room was a complete mess." },
  { word: "metal", pos: "n.", pron: "[métl]", def: "Metal is a strong material people use to build things.", ex: "Steel is a common metal that is used to build buildings." },
  { word: "monitor", pos: "v.", pron: "[mɑ́nitər]", def: "To monitor people or things is to watch them closely.", ex: "The teacher monitors the students when they take tests." },
  { word: "oppose", pos: "v.", pron: "[əpóuz]", def: "To oppose something means to dislike it or act against it.", ex: "I want to be a police officer because I oppose crime." },
  { word: "passive", pos: "adj.", pron: "[pǽsiv]", def: "If a person is passive, they do not take action to solve problems.", ex: "Marcie is so passive that she never solves her own problems." },
  { word: "quantity", pos: "n.", pron: "[kwɑ́ntəti]", def: "A quantity is a certain amount of something.", ex: "I have a small quantity of milk in my glass." },
  { word: "sue", pos: "v.", pron: "[suː]", def: "To sue someone is to take them to court for something wrong they did.", ex: "I sued the company after I slipped on a banana peel in their hallway." }
];

let wordsHtml = `<div style="display: flex; flex-direction: column; gap: 32px; margin-bottom: 20px;"><div style="display: flex; flex-direction: column; gap: 16px;"><img src="/unit12_word_list_1.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /><img src="/unit12_word_list_2.png" style="width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);" /></div><div style="display: flex; flex-direction: column; gap: 24px; padding-top: 24px; border-top: 1px dashed #cbd5e1;"><h3 style="font-size: 1.125rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; margin: 0;">Detailed Meanings</h3><div style="display: flex; flex-direction: column; gap: 24px;">`;

words.forEach(w => {
  wordsHtml += `<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="width: 32px; height: 32px; flex-shrink: 0; background-color: #f8fafc; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; font-size: 16px;">😎</div><div style="display: flex; flex-direction: column; gap: 6px;"><div style="display: flex; align-items: baseline; gap: 8px;"><span style="font-size: 1.25rem; font-weight: 800; color: #65a30d;">${w.word}</span><span style="font-size: 0.875rem; color: #94a3b8; font-family: monospace;">${w.pron}</span><span style="font-size: 0.875rem; color: #94a3b8; font-style: italic;">${w.pos}</span></div><div style="color: #475569; font-size: 0.95rem; line-height: 1.5;">${w.def}</div><div style="color: #64748b; font-size: 0.95rem; font-style: italic;">→ ${w.ex}</div></div></div>`;
});
wordsHtml += `</div></div></div>`;

const storyHtml = `<div style="font-family: Arial, sans-serif; "><h1 style="color: #d6334f; font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem; line-height: 1.2;">The Mean Chef</h1><p style="margin-bottom: 1rem;">Once there was a chef, who was mean to his cooks. He was mean to the people who came in to eat. He charged too much for meals. Many people were not able to <b>afford</b> the cheapest <b>bean</b> dish. When his <b>metal</b> oven broke, he did not have it fixed. So everything <b>baked</b> in it burned. The only light was from <b>candles</b>, and the whole place was a <b>mess</b>. Sometimes, he didn't pay his waiters. Since they had no <b>funds</b>, they had many <b>debts</b>.</p><p style="margin-bottom: 1rem;">The chef behaved this way all the time. He <b>monitored</b> the cooks and yelled if they did not do things his way.</p><p style="margin-bottom: 1rem;">One day, the cooks decided that they were tired of the <b>abuse</b> and that they would not be <b>passive</b> anymore. Everyone <b>opposed</b> the chef. At first, they thought about <b>suing</b> him. Instead, they tied up the chef with rope. Now, they controlled the restaurant! They <b>decreased</b> the price of food. They used the best <b>ingredients</b> and made large <b>quantities</b> of food. They turned on the lights. The restaurant was <b>converted</b> into a happy place. For the first time, many people came to eat.</p><p style="margin-bottom: 1rem;">The chef realized that the restaurant's problems were his <b>fault</b>. The chef learned an important lesson. The new, <b>generous</b> chef <b>insisted</b> on giving the customers a free meal.</p></div>`;

const unit12 = {
  basicInfo: {
    skill: "Standard-Reading",
    title: "Unit 12",
    category: "exercise",
    timeLimit: 0
  },
  parts: [
    {
      id: "part1",
      title: "Word List",
      content: wordsHtml,
      sections: [
        {
          id: "sec1_wordlist",
          title: "Part A: Choose the right word for the given definition.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "1", content: "1. a certain amount", options: ["a. ingredient", "b. quantity", "c. metal", "d. fault"], correctAnswer: "b. quantity", explanation: "quantity (n): một số lượng nhất định (a certain amount)." },
            { id: "2", content: "2. to make less", options: ["a. decrease", "b. oppose", "c. insist", "d. abuse"], correctAnswer: "a. decrease", explanation: "decrease (v): làm giảm đi (to make less)." },
            { id: "3", content: "3. to watch closely", options: ["a. bake", "b. monitor", "c. mess", "d. afford"], correctAnswer: "b. monitor", explanation: "monitor (v): giám sát, theo dõi chặt chẽ (to watch closely)." },
            { id: "4", content: "4. a plant seed", options: ["a. sue", "b. passive", "c. bean", "d. fund"], correctAnswer: "c. bean", explanation: "bean (n): hạt đỗ, đậu (a plant seed)." },
            { id: "5", content: "5. money you owe", options: ["a. convert", "b. debt", "c. candle", "d. generous"], correctAnswer: "b. debt", explanation: "debt (n): món nợ, tiền nợ (money you owe)." }
          ]
        },
        {
          id: "sec2_wordlist",
          title: "Part B: Circle two words that are related in each group.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "6", content: "1.", options: ["a. debt / b. fund", "a. debt / c. bean", "b. fund / d. abuse", "c. bean / d. abuse"], correctAnswer: "a. debt / b. fund", explanation: "debt (nợ) và fund (quỹ) đều liên quan đến tiền bạc." },
            { id: "7", content: "2.", options: ["a. fault / b. abuse", "b. abuse / c. monitor", "c. monitor / d. sue", "a. fault / d. sue"], correctAnswer: "a. fault / d. sue", explanation: "fault (lỗi) và sue (kiện) có liên quan đến nhau: ai đó có lỗi nên bị kiện." },
            { id: "8", content: "3.", options: ["a. afford / b. bake", "b. bake / d. ingredient", "c. insist / d. ingredient", "a. afford / c. insist"], correctAnswer: "b. bake / d. ingredient", explanation: "bake (nướng) và ingredient (nguyên liệu) đều liên quan đến nấu ăn." },
            { id: "9", content: "4.", options: ["a. fault / b. decrease", "b. decrease / c. quantity", "c. quantity / d. convert", "a. fault / d. convert"], correctAnswer: "b. decrease / c. quantity", explanation: "decrease (giảm) và quantity (số lượng) có liên quan đến nhau." },
            { id: "10", content: "5.", options: ["a. debt / b. monitor", "b. monitor / c. afford", "a. debt / c. afford", "c. afford / d. generous"], correctAnswer: "a. debt / c. afford", explanation: "debt (nợ) và afford (đủ khả năng chi trả) đều liên quan đến tài chính." }
          ]
        },
        {
          id: "sec3_wordlist",
          title: "Exercise 2: Check (V) the one that suits the blank naturally.",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "11", content: "1. To make sure the door was built strong, ____________.", options: ["a. it was made out of metal", "b. it was monitored to the floor"], correctAnswer: "a. it was made out of metal", explanation: "made out of metal (được làm bằng kim loại) mang ý nghĩa cửa vững chắc." },
            { id: "12", content: "2. I was treated unfairly by my company, so ____________.", options: ["a. we decreased the table", "b. I decided to sue them in court"], correctAnswer: "b. I decided to sue them in court", explanation: "sue them in court (kiện họ ra tòa) vì bị đối xử bất công." },
            { id: "13", content: "3. I went to the grocery store. ____________.", options: ["a. I converted the milk", "b. I got a small quantity of eggs"], correctAnswer: "b. I got a small quantity of eggs", explanation: "got a small quantity of eggs (mua một lượng nhỏ trứng) phù hợp với việc đi siêu thị." },
            { id: "14", content: "4. When your friend borrows money from you, ____________.", options: ["a. he owes you a debt", "b. he opposes you"], correctAnswer: "a. he owes you a debt", explanation: "owes you a debt (nợ bạn một khoản) phù hợp với việc mượn tiền." },
            { id: "15", content: "5. The man wants to cook noodles. ____________.", options: ["a. He will get the ingredients", "b. He will insist the water"], correctAnswer: "a. He will get the ingredients", explanation: "get the ingredients (lấy các nguyên liệu) hợp lý khi muốn nấu ăn." },
            { id: "16", content: "6. I have enough money. ____________.", options: ["a. My fund is too small", "b. I can afford to buy the shirt"], correctAnswer: "b. I can afford to buy the shirt", explanation: "afford to buy the shirt (có đủ tiền để mua chiếc áo) phù hợp với câu trước đó." },
            { id: "17", content: "7. When the oven was hot enough, ____________.", options: ["a. it baked the potato", "b. it made a mess in the kitchen"], correctAnswer: "a. it baked the potato", explanation: "Lò nướng đủ nóng để nướng khoai tây (baked the potato)." },
            { id: "18", content: "8. In case the power goes out, ____________.", options: ["a. you should keep candles at home", "b. you will be generous"], correctAnswer: "a. you should keep candles at home", explanation: "Cần giữ nến (keep candles) ở nhà phòng khi mất điện." },
            { id: "19", content: "9. When the girl became hungry, ____________.", options: ["a. she became passive and decided to do something about it", "b. she cooked some beans"], correctAnswer: "b. she cooked some beans", explanation: "Cô gái nấu đậu (cooked some beans) khi đói." },
            { id: "20", content: "10. My homework was not turned in.", options: ["a. I abused it at home", "b. It was all my fault"], correctAnswer: "b. It was all my fault", explanation: "Đó là lỗi của tôi (my fault) khi không nộp bài tập." }
          ]
        }
      ]
    },
    {
      id: "part2",
      title: "Comprehensive Reading",
      content: storyHtml,
      imageUrl: "/unit12_story.png",
      sections: [
        {
          id: "sec4_reading",
          title: "Reading Comprehension",
          content: "",
          questionType: "Trắc nghiệm",
          questions: [
            { id: "21", content: "1. What is this story about?", options: ["a. How a mean chef was converted into a generous man", "b. Why metal ovens bake food until it burns", "c. Why waiters' funds are not enough to pay their debts", "d. How simple beans brought a large quantity of customers"], correctAnswer: "a. How a mean chef was converted into a generous man", explanation: "Câu chuyện kể về một bếp trưởng khó tính đã thay đổi (converted) thành một người hào phóng." },
            { id: "22", content: "2. Why could people not afford to eat at the restaurant?", options: ["a. The chef insisted they take free food.", "b. The chef made prices too high.", "c. The chef monitored the cooks.", "d. The chef got tied up."], correctAnswer: "b. The chef made prices too high.", explanation: "Bếp trưởng thu phí quá cao (charged too much) khiến khách không đủ tiền trả." },
            { id: "23", content: "3. What did the chef learn at the end of the story?", options: ["a. Electricity was better than using candles.", "b. It was his fault that the restaurant did so well.", "c. The waiters and cooks took over his restaurant.", "d. Behaving in a nice way is better than being mean."], correctAnswer: "d. Behaving in a nice way is better than being mean.", explanation: "Bếp trưởng đã học được bài học rằng cư xử tử tế thì tốt hơn là xấu tính (Behaving in a nice way is better than being mean)." },
            { id: "24", content: "4. According to the passage, all the following are true of the waiters and cooks EXCEPT ____________.", options: ["a. they decreased prices", "b. they used good ingredients", "c. they were replaced by robots", "d. they opposed the abuse of the chef"], correctAnswer: "c. they were replaced by robots", explanation: "Trong bài không hề đề cập đến robots." },
            { id: "25", content: "5. Why did the chef insist on giving his customers a free meal at the end of the story?", options: ["a. He wanted to trick them.", "b. He gave customers free meals to celebrate his big change.", "c. He had too much food.", "d. The food was going to spoil."], correctAnswer: "b. He gave customers free meals to celebrate his big change.", explanation: "Answer key là 'He gave customers free meals to celebrate his big change'." }
          ]
        }
      ]
    }
  ]
};

fs.writeFileSync("unit12.json", JSON.stringify(unit12, null, 2), "utf8");
console.log("unit12.json created successfully.");
