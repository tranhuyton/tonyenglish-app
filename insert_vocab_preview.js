const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "According to a study, genetically modified food has negative effects on the <b>offspring</b> of rats.",
    opts: ["A. health", "B. children"],
    ans: 1,
    exp: "offspring (con cái) = children. Theo một nghiên cứu, thực phẩm biến đổi gen có tác động tiêu cực đến con cái của loài chuột.\n- health: sức khỏe"
  },
  {
    q: "Air quality and effective <b>ventilation</b> are key factors in making a good residence.",
    opts: ["A. housekeeping", "B. draft"],
    ans: 1,
    exp: "ventilation (sự thông gió) = draft (luồng gió). Chất lượng không khí và sự thông gió hiệu quả là những yếu tố then chốt để tạo nên một nơi ở tốt.\n- housekeeping: công việc quản gia/dọn dẹp"
  },
  {
    q: "The Hampton History Museum in Virginia has a great <b>assemblage</b> of Civil War portraits, some of which have national importance.",
    opts: ["A. collection", "B. similarity"],
    ans: 0,
    exp: "assemblage (bộ sưu tập, sự tập hợp) = collection. Bảo tàng Lịch sử Hampton ở Virginia có một bộ sưu tập lớn các bức chân dung thời Nội chiến, một số trong đó có tầm quan trọng quốc gia.\n- similarity: sự tương đồng"
  },
  {
    q: "The Chinese government canceled the release of the US film Memoirs of a Geisha over fears that the sight of Chinese actresses playing Japanese geishas would <b>antagonize</b> Chinese people.",
    opts: ["A. attack", "B. offend"],
    ans: 1,
    exp: "antagonize (làm phản cảm, chọc giận) = offend (xúc phạm, làm mất lòng). Chính phủ Trung Quốc đã hủy bỏ việc phát hành bộ phim Mỹ Hồi ức của một Geisha vì lo sợ rằng hình ảnh các nữ diễn viên Trung Quốc đóng vai geisha Nhật Bản sẽ làm mất lòng người dân Trung Quốc.\n- attack: tấn công"
  },
  {
    q: "Every participant in the contest <b>battled</b> for the judges' attention through their performance.",
    opts: ["A. debated", "B. struggled"],
    ans: 1,
    exp: "battled (chiến đấu, tranh giành) = struggled (nỗ lực, đấu tranh). Mọi thí sinh trong cuộc thi đều cố gắng tranh giành sự chú ý của ban giám khảo thông qua phần trình diễn của họ.\n- debated: tranh luận"
  },
  {
    q: "The international community is trying hard to <b>foster</b> stability in the war-stricken region.",
    opts: ["A. threaten", "B. nurture"],
    ans: 1,
    exp: "foster (thúc đẩy, bồi dưỡng) = nurture (nuôi dưỡng). Cộng đồng quốc tế đang cố gắng hết sức để thúc đẩy sự ổn định trong khu vực bị chiến tranh tàn phá.\n- threaten: đe dọa"
  },
  {
    q: "The company's net profit has dropped 75 percent and is expected to <b>shrink</b> further.",
    opts: ["A. diminish", "B. outdo"],
    ans: 0,
    exp: "shrink (co lại, giảm) = diminish (giảm bớt). Lợi nhuận ròng của công ty đã giảm 75% và dự kiến sẽ còn giảm thêm.\n- outdo: vượt qua, làm giỏi hơn"
  },
  {
    q: "The report provides <b>in-depth</b> analysis of the possible effects of avian influenza on Asian countries.",
    opts: ["A. synonymous", "B. detailed"],
    ans: 1,
    exp: "in-depth (chuyên sâu, chi tiết) = detailed. Báo cáo cung cấp phân tích chi tiết về những tác động có thể có của dịch cúm gia cầm đối với các nước châu Á.\n- synonymous: đồng nghĩa"
  },
  {
    q: "Children can easily be affected by media's <b>skewed</b> images of attractiveness.",
    opts: ["A. distorted", "B. notorious"],
    ans: 0,
    exp: "skewed (bị bóp méo, lệch lạc) = distorted. Trẻ em có thể dễ dàng bị ảnh hưởng bởi những hình ảnh lệch lạc về sự hấp dẫn trên các phương tiện truyền thông.\n- notorious: khét tiếng"
  },
  {
    q: "In the Kuria community of Kenya, a <b>barren</b> woman may marry another woman to raise children for the family.",
    opts: ["A. infertile", "B. asexual"],
    ans: 0,
    exp: "barren (vô sinh, không có con) = infertile. Trong cộng đồng Kuria ở Kenya, một người phụ nữ vô sinh có thể kết hôn với một người phụ nữ khác để nuôi dạy con cái cho gia đình.\n- asexual: vô tính"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 3: Vocabulary Preview",
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
  const folderId = 'a5a97a84-7f39-47bf-80c9-8eed287636e8'; // Chapter 3
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 3: Vocabulary Preview",
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
