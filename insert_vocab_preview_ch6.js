const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "After considering the risks, the investors were _________ to turn down the company's request for additional funding.",
    opts: ["A. obliged", "B. informed", "C. hindered"],
    ans: 0,
    exp: "obliged (bắt buộc, có nghĩa vụ). Sau khi xem xét các rủi ro, các nhà đầu tư buộc phải từ chối yêu cầu tài trợ thêm của công ty.\n- informed: được thông báo\n- hindered: bị cản trở"
  },
  {
    q: "While there have been any number of unconfirmed UFO sightings, there has been little, if any, _________ evidence.",
    opts: ["A. human", "B. empirical", "C. telltale"],
    ans: 1,
    exp: "empirical (theo kinh nghiệm, thực tiễn, thực nghiệm). Mặc dù đã có vô số vụ nhìn thấy UFO chưa được xác nhận, nhưng có rất ít, nếu không muốn nói là không có, bằng chứng thực nghiệm nào.\n- human: con người\n- telltale: làm lộ tẩy, để lộ"
  },
  {
    q: "After the accident, in which he suffered internal injuries, he was given massive _________ of blood to stabilize his condition.",
    opts: ["A. infusions", "B. containers", "C. arteries"],
    ans: 0,
    exp: "infusions (sự truyền - máu, dịch). Sau vụ tai nạn khiến anh bị nội thương, anh đã được truyền một lượng máu lớn để ổn định tình trạng.\n- containers: thùng chứa\n- arteries: động mạch"
  },
  {
    q: "Despite the preponderance of evidence to the contrary, some scientists still _________ the theory to be false.",
    opts: ["A. wish", "B. accuse", "C. avow"],
    ans: 2,
    exp: "avow (thừa nhận, công nhận, tuyên bố). Bất chấp sự vượt trội của các bằng chứng trái ngược, một số nhà khoa học vẫn tuyên bố lý thuyết này là sai.\n- wish: mong muốn\n- accuse: buộc tội"
  },
  {
    q: "For the performers, opening night of the musical will be the _________ of months of practice.",
    opts: ["A. culmination", "B. reward", "C. goal"],
    ans: 0,
    exp: "culmination (đỉnh cao, kết quả cuối cùng). Đối với các nghệ sĩ biểu diễn, đêm khai mạc của vở nhạc kịch sẽ là đỉnh cao của nhiều tháng luyện tập.\n- reward: phần thưởng\n- goal: mục tiêu"
  },
  {
    q: "He is one of the most _________ liars I have ever known; nearly every word out of his mouth is a falsehood.",
    opts: ["A. despised", "B. prolific", "C. unsubstantiated"],
    ans: 1,
    exp: "prolific (phong phú, sản xuất nhiều - ở đây chỉ việc nói dối rất nhiều). Anh ta là một trong những kẻ nói dối tệ hại (thường xuyên) nhất mà tôi từng biết; gần như mọi lời thốt ra khỏi miệng anh ta đều là dối trá.\n- despised: bị khinh thường\n- unsubstantiated: vô căn cứ"
  },
  {
    q: "It is in the long-term interests of the community to protect the area's _________ from pollution because they are important for tourism as well as shipping.",
    opts: ["A. ecologies", "B. species", "C. estuaries"],
    ans: 2,
    exp: "estuaries (cửa sông). Việc bảo vệ các cửa sông trong khu vực khỏi ô nhiễm là lợi ích lâu dài của cộng đồng vì chúng quan trọng đối với du lịch cũng như vận tải biển.\n- ecologies: hệ sinh thái\n- species: các loài"
  },
  {
    q: "The best method of solving a difficult math problem is to break it down into its _________ parts.",
    opts: ["A. irrelevant", "B. constituent", "C. established"],
    ans: 1,
    exp: "constituent (cấu thành, hợp thành). Phương pháp tốt nhất để giải một bài toán khó là chia nó thành các phần cấu thành.\n- irrelevant: không liên quan\n- established: đã được thiết lập"
  },
  {
    q: "When learning a new language, one must keep in mind that even seemingly innocent words may carry _________ that one is not aware of.",
    opts: ["A. intonations", "B. connotations", "C. vocabularies"],
    ans: 1,
    exp: "connotations (hàm ý, ý nghĩa liên tưởng). Khi học một ngôn ngữ mới, người ta phải nhớ rằng ngay cả những từ dường như vô hại cũng có thể mang những hàm ý mà người ta không nhận thức được.\n- intonations: ngữ điệu\n- vocabularies: từ vựng"
  },
  {
    q: "While renewable energy sources such as wind are abundant, we currently lack the technology to _________ them efficiently.",
    opts: ["A. allocate", "B. initialize", "C. harness"],
    ans: 2,
    exp: "harness (khai thác). Mặc dù các nguồn năng lượng tái tạo như gió rất dồi dào, chúng ta hiện đang thiếu công nghệ để khai thác chúng một cách hiệu quả.\n- allocate: phân bổ\n- initialize: khởi tạo"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 6: Vocabulary Preview",
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
          title: "Choose the right word for each blank in the sentence.",
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
  const folderId = 'a8f791a4-7b63-4ebe-a9a9-a2667a45f3eb'; // Chapter 6
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 6: Vocabulary Preview",
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
