const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const readingText = `
<h2 style="text-align:center;font-weight:bold;margin-bottom:20px;font-size:1.3em;">The Cultural Variable</h2>
<p style="text-indent:2em;line-height:1.9;">To understand how the schedule of wants and demands of a given society is balanced against the supply of goods and services available, it is necessary to introduce a noneconomic variable - the anthropological variable of culture. ❶ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">In any given economic system, economic processes cannot be interpreted without culturally defining the demands and understanding the conventions that dictate how and when they are satisfied.</span> As a case in point, we may look briefly at yam production among the Trobriand Islanders, who inhabit a group of coral atolls that lie north of New Guinea's eastern end. Trobriand men spend a great deal of their time and energy raising yams, not for themselves or their own families, but to give others, normally their sisters and married daughters. ❷ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">The purpose of this yam production is not to provision the households of those to whom they are given, as most of what people eat they grow for themselves in gardens in which they plant taro, sweet potatoes, tapioca, greens, beans, and squash, as well as breadfruit and banana trees.</span></p>
<p style="text-indent:2em;line-height:1.9;">The reasons for a man to give yams to a woman are twofold: to show his support for her husband and to enhance his own influence. ❸ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">Once received by the woman, they are loaded into her husband's yam house, symbolizing his worth as a man of power and influence in his community.</span> Some of these yams he may use to purchase a variety of things, including armshells, shell necklaces and earrings, betel nuts, pigs, chickens, and such locally produced goods as woolen bowls, combs, floor mats, lime pots, or even magic spells. Some he must use to discharge obligations, as in the presentation of yams to the relatives of his daughter's husband when she marries, or payments that must be made following the death of a member of his lineage. ❹ <span style="background-color:#FFD54F;padding:1px 3px;border-radius:3px;">Finally, any man who aspires to high status and power is expected to show his worth by organizing a yam competition, in the course of which huge quantities of yams are given away to invited guests.</span> As anthropologist Annette Weiner explains: "A yam house, then, is like a bank account; when full, a man is wealthy and powerful. Until yams are cooked or they rot, they may circulate as limited currency. This is why, once harvested, the usage of yams for daily food is avoided as much as possible."</p>
`;

const qList = [
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❶?",
    opts: [
      "A. Any explanation of economic processes is impossible unless it is based on the cultural demands that form social conventions.",
      "B. Economic processes can only be understood by studying demands and conventions from a cultural perspective.",
      "C. Economic processes can be explained by the mechanism of cultural demands, but only if they are satisfied.",
      "D. The conventions that determine how and when demands are satisfied are the most important factor in an economic process."
    ],
    ans: 1,
    exp: "Ý gốc: Không thể giải thích các quá trình kinh tế nếu không xác định các nhu cầu về mặt văn hóa (culturally defining the demands) và hiểu các quy ước (understanding the conventions). -> Đáp án B: Các quá trình kinh tế chỉ có thể được hiểu (can only be understood) bằng cách nghiên cứu các nhu cầu và quy ước từ góc độ văn hóa."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❷?",
    opts: [
      "A. The purpose of yam production is to replace the food from the garden that is typically eaten by families.",
      "B. People produce yams as a provision for their households because they don't have enough crops growing in gardens.",
      "C. A provision of yam production is that the yams are given to family members who have already eaten the food grown in their garden.",
      "D. Yam production does not aim to provide food for the family, since most crops for food are raised in gardens."
    ],
    ans: 3,
    exp: "Ý gốc: Mục đích của việc sản xuất khoai mỡ này không phải là cung cấp lương thực cho gia đình (not to provision the households) ... vì hầu hết những gì mọi người ăn, họ đều tự trồng trong vườn (as most of what people eat they grow for themselves in gardens). -> Đáp án D thể hiện trọn vẹn ý này."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❸?",
    opts: [
      "A. Men force their wives to receive the yams because the storage of yams stands for power in the community.",
      "B. The woman's act of giving the yams to her husband means that she hands the power over to him.",
      "C. Once the woman's yams are stored in her husband's yam house, they influence the community.",
      "D. A man's yam storage, added to by his wife's gains, indicates his power and influence."
    ],
    ans: 3,
    exp: "Ý gốc: Khi người phụ nữ nhận được (khoai mỡ), chúng được chất vào khoai mỡ của người chồng (loaded into her husband's yam house), tượng trưng cho giá trị của anh ta như một người có quyền lực và ảnh hưởng trong cộng đồng (symbolizing his worth as a man of power and influence). -> Đáp án D diễn đạt lại bằng từ ngữ khác mang ý nghĩa tương đương."
  },
  {
    q: "Which of the sentences below best expresses the essential information in sentence ❹?",
    opts: [
      "A. The arranging of a yam competition is a necessary step to follow for an ambitious man to achieve his goal.",
      "B. A man's aspirations are shown through a yam competition that distributes a great deal of yams to the guests.",
      "C. If a man holds a yam competition through which he shares his yams with the whole community, he can obtain a high status.",
      "D. When an aspiring man gains power in the community, he must arrange a yam competition."
    ],
    ans: 1,
    exp: "Ý gốc: Bất cứ người đàn ông nào khao khát địa vị và quyền lực cao (aspires to high status and power) đều phải thể hiện giá trị của mình bằng cách tổ chức một cuộc thi khoai mỡ (organizing a yam competition), trong đó số lượng lớn khoai mỡ được tặng cho các khách mời (huge quantities of yams are given away to invited guests). -> Đáp án B tóm gọn và truyền đạt đúng trọng tâm."
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 2: Exercise 3",
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
          title: "",
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
    title: "Chapter 2: Exercise 3",
    course_id: courseId,
    folder_id: folderId,
    test_type: "Standard-Reading",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  // check if exists
  const {data: existing} = await supabase.from('tests').select('id').eq('title', "Chapter 2: Exercise 3").eq('course_id', courseId);
  if (existing && existing.length > 0) {
    const { data, error } = await supabase.from('tests').update(payload).eq('id', existing[0].id).select();
    if (error) console.error("Error updating:", error);
    else console.log("Successfully updated test:", data[0].title);
  } else {
    const { data, error } = await supabase.from('tests').insert([payload]).select();
    if (error) console.error("Error inserting:", error);
    else console.log("Successfully inserted test:", data[0].title);
  }
}

run();
