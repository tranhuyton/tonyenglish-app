const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "In submarines, <b>buoyancy</b> is decreased by venting air from ballast tanks and allowing them to flood, thereby allowing the submarine to slip beneath the surface.",
    opts: ["A. flotation ability", "B. speed of travel"],
    ans: 0,
    exp: "buoyancy (sức nổi, sự nổi) = flotation ability (khả năng nổi). Ở tàu ngầm, sức nổi bị giảm bằng cách xả không khí khỏi các thùng dằn và để nước tràn vào, từ đó cho phép tàu ngầm trượt xuống dưới mặt nước.\n- speed of travel: tốc độ di chuyển"
  },
  {
    q: "The judge passed down an especially harsh sentence because the man had <b>evinced</b> essentially no remorse for his crimes.",
    opts: ["A. displayed", "B. offered"],
    ans: 0,
    exp: "evinced (chứng tỏ, biểu lộ) = displayed (thể hiện). Thẩm phán đã tuyên một bản án đặc biệt nghiêm khắc vì người đàn ông này về cơ bản không thể hiện sự hối hận nào về tội ác của mình.\n- offered: đề nghị, đưa ra"
  },
  {
    q: "The aboriginal people of Australia are experts at survival in an environment with <b>scanty</b> resources.",
    opts: ["A. obscure", "B. limited"],
    ans: 1,
    exp: "scanty (ít ỏi, thiếu thốn) = limited (hạn chế). Thổ dân Úc là những chuyên gia sinh tồn trong một môi trường có nguồn tài nguyên hạn chế.\n- obscure: mờ mịt, vô danh"
  },
  {
    q: "Jim's music teacher derided his latest composition as a meaningless jumble of discordant sounds with no <b>aesthetic</b> value.",
    opts: ["A. artistic", "B. monetary"],
    ans: 0,
    exp: "aesthetic (thuộc về thẩm mỹ) = artistic (thuộc về nghệ thuật). Giáo viên âm nhạc của Jim chế nhạo sáng tác mới nhất của cậu ấy là một mớ âm thanh chói tai vô nghĩa không có giá trị nghệ thuật.\n- monetary: thuộc về tiền tệ"
  },
  {
    q: "Many members of the flower generation of the 1960s saw their elders as little more than <b>prudish</b> old gatekeepers of a bankrupt culture.",
    opts: ["A. irrelevant", "B. puritanical"],
    ans: 1,
    exp: "prudish (cổ hủ, hay làm điệu bộ ngoan đạo) = puritanical (khắt khe, bảo thủ). Nhiều thành viên của thế hệ hoa niên những năm 1960 coi những người lớn tuổi của họ chỉ là những người gác cổng già cỗi cổ hủ của một nền văn hóa đã phá sản.\n- irrelevant: không liên quan"
  },
  {
    q: "The primary challenge for cancer surgeons is to completely <b>excise</b> the tumor without harming healthy tissue.",
    opts: ["A. treat", "B. cut away"],
    ans: 1,
    exp: "excise (cắt bỏ) = cut away (cắt đi). Thử thách chính đối với các bác sĩ phẫu thuật ung thư là cắt bỏ hoàn toàn khối u mà không làm tổn hại đến mô khỏe mạnh.\n- treat: điều trị"
  },
  {
    q: "Most hallucinogenic drugs were originally developed to aid psychiatric counseling due to their ability to lower <b>inhibitions</b>.",
    opts: ["A. repressive feelings", "B. unpleasant memories"],
    ans: 0,
    exp: "inhibitions (sự ức chế, sự kiềm chế) = repressive feelings (cảm giác bị dồn nén). Hầu hết các loại thuốc gây ảo giác ban đầu được phát triển để hỗ trợ tư vấn tâm thần do khả năng làm giảm sự ức chế.\n- unpleasant memories: những kỷ niệm không vui"
  },
  {
    q: "The fate of Romeo and Juliet in Shakespeare's famous play serves as a <b>poignant</b> reminder of the dangers of rash actions brought on by foolish love.",
    opts: ["A. keen", "B. theatrical"],
    ans: 0,
    exp: "poignant (chua xót, sâu sắc, thấm thía) = keen (nhạy bén, sâu sắc, mãnh liệt). Số phận của Romeo và Juliet trong vở kịch nổi tiếng của Shakespeare đóng vai trò như một lời nhắc nhở sâu sắc về những nguy hiểm của những hành động bồng bột do tình yêu mù quáng mang lại.\n- theatrical: thuộc về sân khấu, có tính kịch"
  },
  {
    q: "The actress was dogged by vicious and unsubstantiated rumors of her supposed <b>promiscuity</b> during the early stages of her career.",
    opts: ["A. unchecked ambition", "B. immoral sexuality"],
    ans: 1,
    exp: "promiscuity (sự lăng nhăng, bừa bãi trong quan hệ) = immoral sexuality (tình dục vô đạo đức). Nữ diễn viên bị đeo bám bởi những tin đồn ác ý và vô căn cứ về sự lăng nhăng được cho là của cô trong những giai đoạn đầu của sự nghiệp.\n- unchecked ambition: tham vọng không kiểm soát"
  },
  {
    q: "Many argue that the world will never make the switch to cleaner forms of energy as long as easily <b>obtainable</b> oil sources remain.",
    opts: ["A. locatable", "B. accessible"],
    ans: 1,
    exp: "obtainable (có thể đạt được, kiếm được) = accessible (có thể tiếp cận, dễ dàng có được). Nhiều người lập luận rằng thế giới sẽ không bao giờ chuyển sang các dạng năng lượng sạch hơn chừng nào các nguồn dầu dễ dàng tiếp cận vẫn còn.\n- locatable: có thể định vị"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 5: Vocabulary Preview",
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
  const folderId = '9b84c175-d0c2-4d22-98d5-341d2f6ad857'; // Chapter 5
  
  // check max order
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 5: Vocabulary Preview",
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
