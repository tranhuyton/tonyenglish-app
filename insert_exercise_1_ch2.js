const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">The Great Depression</h2>
<p style="text-indent:2em;line-height:1.9;">The economic boom that the United States enjoyed after the end of World War I ended in the 1920s with the Stock Market Crash of 1929. During the years of business prosperity in the 1920s, the value of stock on the New York stock market grew steadily. ❶ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">Many people bought "on margin," investing a small amount of cash and borrowing the rest to be paid back when the stock prices increased, as everyone came to believe it was bound to do.</span> For example, if a share of stock sold for $100, the buyer might put up $10 in cash and borrow $90. When the stock rose to, say, $120, the buyer could sell, pay back the borrowed $90 (with interest) and still pocket a comfortable profit on the $10 investment.</p>
<p style="text-indent:2em;line-height:1.9;">But what if stock prices dropped? If the share he/she bought at $100 dropped to $80, the buyer not only lost the $10 investment but could not pay back the full loan. The buyer lost his/her investment, the person from whom he/she borrowed lost and both would be headed towards bankruptcy. This is what happened in October 1929. Stock prices dropped, and then individuals lost their investments. Then banks began to fail. As banks and businesses went bankrupt, unemployment rose. ❷ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">As the crash of the stock market became a reality, chaos spread quickly across the nation.</span> A recession began and by 1931, it had turned into America's worst recession.</p>
<p style="text-indent:2em;line-height:1.9;">❸ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">The various factors that precipitated the stock market crash range from frenzied speculation and the overpriced nature of stocks to the unevenness of prosperity and the farmers' depressed status.</span> A rise in interest rates in England, designed to attract investment money away from Wall Street and to England, also had an effect as investors moved money from stocks to English bonds to get these higher earnings. ❹ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">Perhaps the most important factor was psychological - a desire to get rich quick, which led to gambling with borrowed money, which is one way of looking at buying "on margin."</span></p>
`;

const qList = [
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❶?",
    opts: [
      "A. Based on the common belief in continued rising stock value, stock purchase using borrowed money was widespread.",
      "B. By investing just a small amount of money on buying stocks, many people could make a large profit.",
      "C. When the stock prices rose, everyone paid back the money they had borrowed to purchase a stock.",
      "D. Many people bought stocks on credit because everyone believed it was a right thing to do."
    ],
    ans: 0,
    exp: "Dựa vào niềm tin chung về việc giá trị cổ phiếu sẽ tiếp tục tăng, việc mua cổ phiếu bằng tiền vay mượn đã trở nên phổ biến. Ý chính của câu là: 'Many people bought on margin (bằng tiền vay)' vì 'everyone came to believe it was bound to do (giá sẽ tăng)'."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❷?",
    opts: [
      "A. There was a huge gap between the stock market and reality across the country.",
      "B. The economic situation got more chaotic as the stock prices became realistic.",
      "C. There was a sudden fall of the stock market as national chaos was spreading.",
      "D. When stock value suddenly dropped, the whole country fell into complete disorder."
    ],
    ans: 3,
    exp: "Ý gốc: 'As the crash of the stock market became a reality (khi sự sụp đổ thị trường chứng khoán thành sự thật = When stock value suddenly dropped), chaos spread quickly across the nation (hỗn loạn lan rộng khắp cả nước = the whole country fell into complete disorder).'"
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❸?",
    opts: [
      "A. Wild speculation, overly high stock prices, and the gap between the rich and the poor all contributed to the recession.",
      "B. Unrealistic speculation precipitated by an overheated economy was part of the factors that brought about the recession.",
      "C. The stock market crash happened when the farmers, whose status was largely ignored, showed strong opposition.",
      "D. The stock market crash was quickened as the overpriced stocks were unfairly distributed."
    ],
    ans: 0,
    exp: "Câu gốc liệt kê các yếu tố gây ra sự sụp đổ của thị trường chứng khoán: đầu cơ điên cuồng (frenzied speculation), cổ phiếu định giá quá cao (overpriced nature of stocks), sự thịnh vượng không đồng đều (unevenness of prosperity) và tình trạng khốn khổ của nông dân (farmers' depressed status). Đáp án A thâu tóm được hầu hết: đầu cơ mù quáng, giá cổ phiếu quá cao, khoảng cách giàu nghèo (gap between the rich and the poor)."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❹?",
    opts: [
      "A. Those who started gambling to make money were the biggest cause of the depression.",
      "B. People's desire to make quick money most strongly affected the depression.",
      "C. One of the things people desired to do was gamble with borrowed money.",
      "D. Psychology can best explain the reason why people get addicted to gambling."
    ],
    ans: 1,
    exp: "Câu gốc nói yếu tố quan trọng nhất là tâm lý mong muốn làm giàu nhanh chóng (desire to get rich quick). Đáp án B diễn đạt lại rằng khát khao kiếm tiền nhanh của mọi người ảnh hưởng mạnh nhất đến cuộc khủng hoảng."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 2: Exercise 1",
    timeLimit: 0,
    category: "exercise",
    skill: "Standard-Reading"
  },
  parts: [
    {
      id: "part1",
      content: readingText,
      sections: [
        {
          id: "sec1",
          title: "Questions 1-4",
          content: "",
          questionType: "Trắc nghiệm",
          questions: qList.map((data, index) => ({
            id: String(index + 1),
            content: data.q,
            options: data.opts,
            correctAnswer: data.ans,
            explanation: data.exp
          }))
        }
      ]
    }
  ]
};

async function run() {
  const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb'; // IELTS Premium
  const folderId = 'ba08090a-d614-40a8-b7dc-89c7723daf89'; // Chapter 2 inside Crash Course
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 2: Exercise 1",
    course_id: courseId,
    folder_id: folderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  const { data, error } = await supabase.from('tests').update(payload).eq('title', "Chapter 2: Exercise 1").eq('course_id', courseId).select();
  if (error) {
    console.error("Error updating:", error);
  } else {
    console.log("Successfully updated test:", data && data.length > 0 ? data[0].title : "Not found");
  }
}

run();
