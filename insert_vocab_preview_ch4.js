const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "A series of economic reform measures will give the regional governments greater _________ to run their economies.",
    opts: ["A. federation", "B. autonomy", "C. agitation"],
    ans: 1,
    exp: "autonomy (quyền tự trị, sự tự chủ). Một loạt các biện pháp cải cách kinh tế sẽ trao cho chính quyền các khu vực quyền tự trị lớn hơn để điều hành nền kinh tế của họ.\n- federation: liên bang\n- agitation: sự kích động"
  },
  {
    q: "The North and South Poles are located on opposite ends of the _________ on which the Earth rotates.",
    opts: ["A. merry-go-round", "B. rotation", "C. axis"],
    ans: 2,
    exp: "axis (trục). Cực Bắc và Cực Nam nằm ở hai đầu đối diện của trục mà Trái đất quay quanh.\n- merry-go-round: vòng đu quay ngựa gỗ\n- rotation: sự luân phiên, sự xoay"
  },
  {
    q: "Although China is emerging as an influential force in the world politics, it is also experiencing instability and social _________ as a price of its rapid development.",
    opts: ["A. unrest", "B. platform", "C. boycott"],
    ans: 0,
    exp: "unrest (sự bất ổn, tình trạng náo động). Mặc dù Trung Quốc đang nổi lên như một thế lực có ảnh hưởng trong chính trị thế giới, họ cũng đang trải qua sự mất ổn định và bất ổn xã hội như một cái giá phải trả cho sự phát triển nhanh chóng của mình.\n- platform: nền tảng\n- boycott: tẩy chay"
  },
  {
    q: "I think the course title is a _________. This class isn't only about postcolonialism.",
    opts: ["A. misnomer", "B. associate", "C. fragment"],
    ans: 0,
    exp: "misnomer (sự gọi nhầm tên, tên gọi sai). Tôi nghĩ tên khóa học là một cách gọi sai. Lớp học này không chỉ nói về chủ nghĩa hậu thuộc địa.\n- associate: người cộng tác\n- fragment: mảnh vỡ"
  },
  {
    q: "Although many people believe eating less fat _________ disease, a new study suggests that this may not be true.",
    opts: ["A. facilitates", "B. curbs", "C. destroys"],
    ans: 1,
    exp: "curbs (kiềm chế, hạn chế). Mặc dù nhiều người tin rằng ăn ít chất béo giúp kiềm chế bệnh tật, một nghiên cứu mới cho thấy điều này có thể không đúng.\n- facilitates: tạo điều kiện thuận lợi\n- destroys: tiêu diệt"
  },
  {
    q: "Long-awaited rain throughout last week has _________ the reservoirs to their highest point in 9 months.",
    opts: ["A. predominated", "B. replenished", "C. withheld"],
    ans: 1,
    exp: "replenished (làm đầy lại, bổ sung). Cơn mưa được mong đợi từ lâu suốt tuần trước đã làm đầy lại các hồ chứa đạt đến điểm cao nhất trong 9 tháng.\n- predominated: chiếm ưu thế\n- withheld: từ chối, kìm lại"
  },
  {
    q: "While a pilot can in theory avoid _________ objects through the use of a good map, radar is still needed to track the locations of other planes.",
    opts: ["A. ready-made", "B. iridescent", "C. stationary"],
    ans: 2,
    exp: "stationary (đứng yên, cố định). Mặc dù phi công theo lý thuyết có thể tránh được các vật thể đứng yên thông qua việc sử dụng một bản đồ tốt, nhưng radar vẫn cần thiết để theo dõi vị trí của các máy bay khác.\n- ready-made: làm sẵn\n- iridescent: óng ánh nhiều màu"
  },
  {
    q: "Animal behaviorists in the UK suggest that ants are very _________ teachers. They found evidence of two-way teacher-pupil communication between ants.",
    opts: ["A. organic", "B. graduated", "C. adept"],
    ans: 2,
    exp: "adept (tinh thông, lão luyện, giỏi). Các nhà nghiên cứu hành vi động vật ở Anh cho rằng kiến là những giáo viên rất giỏi. Họ đã tìm thấy bằng chứng về sự giao tiếp hai chiều giữa giáo viên và học sinh ở loài kiến.\n- organic: hữu cơ\n- graduated: được chia độ, tốt nghiệp"
  },
  {
    q: "Vietnam was removed from the list of countries with local transmission of SARS in 2003, as it acted _________ to control the disease.",
    opts: ["A. swiftly", "B. casually", "C. unexpectedly"],
    ans: 0,
    exp: "swiftly (một cách nhanh chóng). Việt Nam đã được đưa ra khỏi danh sách các quốc gia có sự lây truyền SARS tại địa phương vào năm 2003, vì họ đã hành động nhanh chóng để kiểm soát căn bệnh này.\n- casually: một cách tình cờ, thờ ơ\n- unexpectedly: một cách bất ngờ"
  },
  {
    q: "In some regions of the world, progress in reducing malnutrition among infants and young children is _________ slow.",
    opts: ["A. actively", "B. exclusively", "C. exceedingly"],
    ans: 2,
    exp: "exceedingly (cực kỳ, quá chừng). Ở một số khu vực trên thế giới, tiến độ trong việc giảm suy dinh dưỡng ở trẻ sơ sinh và trẻ nhỏ là cực kỳ chậm.\n- actively: một cách tích cực\n- exclusively: một cách độc quyền, duy nhất"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 4: Vocabulary Preview",
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
  const folderId = 'de641722-4dd4-43bd-90ff-d13186201b27'; // Chapter 4
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 4: Vocabulary Preview",
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
