const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "Many big cats are very <b>reclusive</b>, so getting an accurate count of their numbers can be quite difficult.",
    opts: ["A. posing a significant threat", "B. avoiding contact with others"],
    ans: 1,
    exp: "reclusive (sống ẩn dật, trốn tránh) = avoiding contact with others (tránh tiếp xúc với người khác). Nhiều loài mèo lớn sống rất ẩn dật, do đó việc có được con số chính xác về số lượng của chúng có thể khá khó khăn.\n- posing a significant threat: gây ra mối đe dọa đáng kể"
  },
  {
    q: "Marine biologists use a special steel <b>enclosure</b> that allows them to study sharks without endangering themselves.",
    opts: ["A. aquarium", "B. cage"],
    ans: 1,
    exp: "enclosure (rào chắn, chuồng) = cage (lồng, chuồng). Các nhà sinh vật học biển sử dụng một lồng thép đặc biệt cho phép họ nghiên cứu cá mập mà không gây nguy hiểm cho bản thân.\n- aquarium: thủy cung"
  },
  {
    q: "Reinforced concrete, in which steel bars are <b>encased</b> in the concrete, greatly improves the strength of a building.",
    opts: ["A. locked inside", "B. added to something"],
    ans: 0,
    exp: "encased (được bọc trong, được bao bọc) = locked inside (bị khóa/bọc bên trong). Bê tông cốt thép, trong đó các thanh thép được bao bọc trong bê tông, giúp cải thiện đáng kể độ chắc chắn của tòa nhà.\n- added to something: được thêm vào thứ gì đó"
  },
  {
    q: "Many of the literary works of Shakespeare and other Renaissance writers are filled with <b>allusions</b> that are unfamiliar to today's readers.",
    opts: ["A. issues", "B. references"],
    ans: 1,
    exp: "allusions (sự ám chỉ, lời nói bóng gió) = references (sự tham chiếu, sự nhắc đến). Nhiều tác phẩm văn học của Shakespeare và các nhà văn thời Phục hưng khác chứa đầy những sự ám chỉ không quen thuộc đối với độc giả ngày nay.\n- issues: vấn đề"
  },
  {
    q: "There may seem to be no <b>ostensible</b> reason for his actions, but I assure you there is a method to his madness.",
    opts: ["A. justifiable", "B. evident"],
    ans: 1,
    exp: "ostensible (có vẻ bề ngoài, rõ ràng) = evident (rõ ràng, hiển nhiên). Có vẻ như không có lý do rõ ràng nào cho hành động của anh ta, nhưng tôi đảm bảo với bạn là sự điên rồ của anh ta có phương pháp riêng.\n- justifiable: có thể biện minh được"
  },
  {
    q: "The employer gave each employee a small bonus as a <b>token</b> of his gratitude for their hard work on the project.",
    opts: ["A. symbol", "B. payment"],
    ans: 0,
    exp: "token (dấu hiệu, biểu tượng) = symbol (biểu tượng). Người chủ đã tặng mỗi nhân viên một khoản tiền thưởng nhỏ như một biểu tượng của lòng biết ơn đối với sự làm việc chăm chỉ của họ trong dự án.\n- payment: khoản thanh toán"
  },
  {
    q: "The quarterback felt the loss more <b>keenly</b> than some of the other players because it was his last game before retirement.",
    opts: ["A. sorrowfully", "B. deeply"],
    ans: 1,
    exp: "keenly (một cách sắc bén, sâu sắc) = deeply (một cách sâu sắc). Vị trí tiền vệ nhận thấy sự mất mát này sâu sắc hơn một số cầu thủ khác vì đây là trận đấu cuối cùng của anh trước khi giải nghệ.\n- sorrowfully: một cách đau buồn"
  },
  {
    q: "The counselor worked with the couple to help them achieve a greater level of <b>intimacy</b> with each other.",
    opts: ["A. closeness", "B. trust"],
    ans: 0,
    exp: "intimacy (sự thân mật, sự gần gũi) = closeness (sự gần gũi). Chuyên gia tư vấn đã làm việc với cặp đôi để giúp họ đạt được mức độ gần gũi với nhau cao hơn.\n- trust: sự tin tưởng"
  },
  {
    q: "John isn't the best speaker because he often goes off on tangents and has difficulty <b>confining</b> himself to one topic.",
    opts: ["A. expressing", "B. restricting"],
    ans: 1,
    exp: "confining (hạn chế, giới hạn) = restricting (hạn chế). John không phải là diễn giả giỏi nhất vì anh ấy thường hay lan man và gặp khó khăn trong việc giới hạn bản thân vào một chủ đề.\n- expressing: thể hiện"
  },
  {
    q: "Everyone recognized the talent of the new artist, but many felt that his work was too brash and lacked <b>subtlety</b>.",
    opts: ["A. nuance", "B. purpose"],
    ans: 0,
    exp: "subtlety (sự tinh tế, sự huyền ảo) = nuance (sắc thái tinh tế). Mọi người đều công nhận tài năng của nghệ sĩ mới, nhưng nhiều người cảm thấy rằng tác phẩm của anh ấy quá xấc xược và thiếu đi sự tinh tế.\n- purpose: mục đích"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 7: Vocabulary Preview",
    timeLimit: 0,
    category: "exercise",
    skill: "Standard-Listening"
  },
  parts: [
    {
      id: "part1",
      readingText: "",
      sections: [
        {
          id: "sec1",
          title: "Choose the right meaning for the words in bold.",
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
  const folderId = 'aabd2666-a010-411c-81f3-f18693145276'; // Chapter 7
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 7: Vocabulary Preview",
    course_id: courseId,
    folder_id: folderId,
    test_type: "Standard-Listening",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  const { data, error } = await supabase.from('tests').insert([payload]).select();
  if (error) {
    console.error("Error inserting:", error);
  } else {
    console.log("Successfully inserted test:", data[0].title);
  }
}

run();
