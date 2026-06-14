const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "Never one to _________ his thoughts or feelings, Greg has a bluntness about him that some people find rude.",
    opts: ["A. relate", "B. mitigate", "C. repress"],
    ans: 2,
    exp: "repress (kìm nén). Không bao giờ là người kìm nén những suy nghĩ hay cảm xúc của mình, Greg có sự thẳng thắn mà một số người cho là thô lỗ.\n- relate: liên hệ, kể lại\n- mitigate: làm giảm nhẹ"
  },
  {
    q: "The group of young artists held little _________ for the established traditions of the art community and enjoyed thumbing their noses at the establishment.",
    opts: ["A. esteem", "B. etiquette", "C. knowledge"],
    ans: 0,
    exp: "esteem (sự tôn trọng, quý trọng). Nhóm nghệ sĩ trẻ ít tôn trọng các truyền thống lâu đời của cộng đồng nghệ thuật và thích chế nhạo giới cầm quyền.\n- etiquette: phép xã giao\n- knowledge: kiến thức"
  },
  {
    q: "The company's website was overloaded with an unexpected _________ of emails requesting information on its new product line.",
    opts: ["A. demand", "B. surge", "C. inquiry"],
    ans: 1,
    exp: "surge (sự dâng lên, sự tăng đột ngột). Trang web của công ty bị quá tải với sự gia tăng đột ngột không ngờ của các email yêu cầu thông tin về dòng sản phẩm mới.\n- demand: nhu cầu\n- inquiry: cuộc điều tra, câu hỏi"
  },
  {
    q: "The CEO, who was an inherently disorganized man, found the services of his secretary to be _________.",
    opts: ["A. reassuring", "B. complimentary", "C. indispensable"],
    ans: 2,
    exp: "indispensable (không thể thiếu được, rất cần thiết). Vị Giám đốc điều hành, vốn là một người bẩm sinh thiếu tổ chức, nhận thấy các dịch vụ của thư ký của mình là không thể thiếu.\n- reassuring: làm yên tâm\n- complimentary: ca ngợi, miễn phí"
  },
  {
    q: "A person can unknowingly live with HIV for years before the symptoms of full blown AIDS begin to _________, and this is why the disease spreads so easily.",
    opts: ["A. afflict", "B. manifest", "C. debilitate"],
    ans: 1,
    exp: "manifest (biểu hiện, lộ rõ). Một người có thể sống với HIV một cách vô tình trong nhiều năm trước khi các triệu chứng của bệnh AIDS toàn phát bắt đầu biểu hiện, và đây là lý do tại sao căn bệnh này lây lan dễ dàng như vậy.\n- afflict: làm đau khổ\n- debilitate: làm suy nhược"
  },
  {
    q: "While the stockbroker rarely did much research into companies before he bought their stock, his _________ proved to be impeccable and he made millions.",
    opts: ["A. hunches", "B. resources", "C. ambitions"],
    ans: 0,
    exp: "hunches (linh cảm). Mặc dù người môi giới chứng khoán hiếm khi nghiên cứu nhiều về các công ty trước khi mua cổ phiếu của họ, linh cảm của anh ta tỏ ra hoàn hảo và anh ta đã kiếm được hàng triệu đô la.\n- resources: tài nguyên\n- ambitions: tham vọng"
  },
  {
    q: "Procreation is a fundamental _________ in all organisms, and is second only to self-preservation as a motivation of behavior.",
    opts: ["A. fact", "B. drive", "C. process"],
    ans: 1,
    exp: "drive (động lực, sự thúc đẩy). Sinh sản là một động lực cơ bản ở mọi sinh vật, và chỉ đứng sau bản năng tự bảo tồn như một động lực của hành vi.\n- fact: sự thật\n- process: quá trình"
  },
  {
    q: "Lacking faith in the judgment of the inexperienced soldiers under his command, the captain ordered his troops not to _________ from his instructions under any circumstances.",
    opts: ["A. deviate", "B. revise", "C. rebel"],
    ans: 0,
    exp: "deviate (đi chệch, lệch hướng). Thiếu niềm tin vào phán đoán của những người lính thiếu kinh nghiệm dưới quyền chỉ huy của mình, vị thuyền trưởng đã ra lệnh cho quân của mình không được đi chệch khỏi chỉ thị của ông trong mọi tình huống.\n- revise: xem xét lại\n- rebel: nổi loạn"
  },
  {
    q: "After an initial period of _________ following the surprise bankruptcy announcement from a major cooperation, the market finally returned to normal in the afternoon.",
    opts: ["A. gossip", "B. instability", "C. inanity"],
    ans: 1,
    exp: "instability (sự bất ổn định). Sau giai đoạn bất ổn định ban đầu do thông báo phá sản bất ngờ từ một tập đoàn lớn, thị trường cuối cùng đã trở lại bình thường vào buổi chiều.\n- gossip: chuyện tầm phào\n- inanity: sự vô nghĩa, ngớ ngẩn"
  },
  {
    q: "The Native Americans, who had never been exposed to European diseases and were thus highly _________ to them, saw their populations drop dramatically with the arrival of the Spanish and Portuguese.",
    opts: ["A. immune", "B. susceptible", "C. ignorant"],
    ans: 1,
    exp: "susceptible (dễ bị ảnh hưởng, nhạy cảm, dễ mắc bệnh). Người Mỹ bản địa, những người chưa bao giờ tiếp xúc với các căn bệnh của châu Âu và do đó rất dễ bị nhiễm chúng, đã chứng kiến dân số của họ giảm đáng kể khi người Tây Ban Nha và Bồ Đào Nha đến.\n- immune: miễn dịch\n- ignorant: không biết"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 8: Vocabulary Preview",
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
  let folderId = null;

  // check if Chapter 8 folder exists
  const {data: existingFolders} = await supabase.from('folders').select('id').eq('course_id', courseId).ilike('title', 'Chapter 8%');
  if (existingFolders && existingFolders.length > 0) {
    folderId = existingFolders[0].id;
    console.log("Found existing Chapter 8 folder:", folderId);
  } else {
    // insert folder
    const {data: newFolder, error: folderErr} = await supabase.from('folders').insert([{
      title: "Chapter 8",
      course_id: courseId,
      display_order: 8
    }]).select();
    
    if (folderErr) {
      console.error("Error creating folder:", folderErr);
      return;
    }
    folderId = newFolder[0].id;
    console.log("Created new Chapter 8 folder:", folderId);
  }

  // check max order for tests in folder
  const {data: tests} = await supabase.from('tests').select('order_index').eq('course_id', courseId).eq('folder_id', folderId);
  const maxOrder = tests && tests.length > 0 ? Math.max(...tests.map(t => t.order_index || 0)) : 0;
  
  const payload = {
    title: "Chapter 8: Vocabulary Preview",
    course_id: courseId,
    folder_id: folderId,
    test_type: "Standard-Listening",
    content_json: contentJson,
    is_published: true,
    order_index: maxOrder + 1
  };
  
  const { data, error } = await supabase.from('tests').insert([payload]).select();
  if (error) {
    console.error("Error inserting test:", error);
  } else {
    console.log("Successfully inserted test:", data[0].title);
  }
}

run();
