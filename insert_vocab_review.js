const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const env = fs.readFileSync('.env', 'utf-8');
const url = env.match(/^VITE_SUPABASE_URL=(.*)$/m)[1].trim();
const key = env.match(/^VITE_SUPABASE_ANON_KEY=(.*)$/m)[1].trim();
const supabase = createClient(url, key);

const qList = [
  {
    q: "Chinese people toss raw fish to ensure business _________ as a tradition during Chinese New Year.",
    opts: ["A. recession", "B. prosperity", "C. simplicity"],
    ans: 1,
    exp: "prosperity (sự phồn thịnh, thịnh vượng). Người Trung Quốc có truyền thống tung cá sống để cầu mong công việc kinh doanh phát đạt trong năm mới.\n- recession (suy thoái)\n- simplicity (sự đơn giản)"
  },
  {
    q: "Some doctors say running, weight lifting, and other strenuous activities can _________ a stroke or heart attack.",
    opts: ["A. pocket", "B. precipitate", "C. fertilize"],
    ans: 1,
    exp: "precipitate (làm đẩy nhanh, gây ra). Một số bác sĩ cho rằng chạy bộ, nâng tạ và các hoạt động căng thẳng khác có thể gây ra đột quỵ hoặc đau tim.\n- pocket (bỏ túi)\n- fertilize (thụ tinh, bón phân)"
  },
  {
    q: "Several hotels have been found to be in _________ of law, as they illegally removed parking facilities to build more guest rooms.",
    opts: ["A. breach", "B. lineage", "C. share"],
    ans: 0,
    exp: "in breach of law (vi phạm pháp luật). Một số khách sạn đã bị phát hiện vi phạm pháp luật khi loại bỏ trái phép bãi đậu xe để xây thêm phòng khách.\n- lineage (nòi giống)\n- share (cổ phần, phần chia)"
  },
  {
    q: "Mike's company is on the verge of _________, with funds expected to run out by next week.",
    opts: ["A. bankruptcy", "B. unevenness", "C. variable"],
    ans: 0,
    exp: "on the verge of bankruptcy (bên bờ vực phá sản). Công ty của Mike đang trên bờ vực phá sản, với nguồn vốn dự kiến sẽ cạn kiệt vào tuần tới.\n- unevenness (sự không bằng phẳng)\n- variable (biến số)"
  },
  {
    q: "Bison use their big heads to clear away snow to _________ for food.",
    opts: ["A. fuse", "B. harvest", "C. forage"],
    ans: 2,
    exp: "forage (tìm kiếm thức ăn). Bò rừng sử dụng cái đầu to của chúng để dọn tuyết nhằm tìm kiếm thức ăn.\n- fuse (cầu chì, hợp nhất)\n- harvest (thu hoạch)"
  },
  {
    q: "A UN official said Sudan should _________ to the elimination of all forms of discrimination against women.",
    opts: ["A. respect", "B. restrict", "C. adhere"],
    ans: 2,
    exp: "adhere to (tuân thủ, gắn bó với). Một quan chức Liên Hợp Quốc cho biết Sudan nên tuân thủ việc xóa bỏ mọi hình thức phân biệt đối xử với phụ nữ.\n- respect (tôn trọng - không đi với 'to')\n- restrict (hạn chế)"
  },
  {
    q: "There is a Spanish proverb that says, \"Knowledge without sense is a _________ folly.\"",
    opts: ["A. fragile", "B. determined", "C. twofold"],
    ans: 2,
    exp: "twofold (gấp đôi). Tục ngữ Tây Ban Nha có câu: \"Kiến thức mà không có ý thức là một sự ngu ngốc gấp đôi\".\n- fragile (mỏng manh)\n- determined (kiên quyết)"
  },
  {
    q: "The city government may lose its _________ status over telephone services due to changes in economic policy.",
    opts: ["A. monopoly", "B. contrivance", "C. multi-national"],
    ans: 0,
    exp: "monopoly (độc quyền). Chính quyền thành phố có thể mất vị thế độc quyền đối với các dịch vụ điện thoại do những thay đổi trong chính sách kinh tế.\n- contrivance (sự mưu đồ)\n- multi-national (đa quốc gia)"
  },
  {
    q: "Environmentalists insist that every government should prohibit the use of genetically _________ seeds because of the environmental risk they pose.",
    opts: ["A. modified", "B. edible", "C. elongated"],
    ans: 0,
    exp: "genetically modified (biến đổi gen). Các nhà bảo vệ môi trường nhấn mạnh rằng mọi chính phủ nên cấm sử dụng hạt giống biến đổi gen do rủi ro môi trường mà chúng gây ra.\n- edible (có thể ăn được)\n- elongated (kéo dài ra)"
  },
  {
    q: "The film festival provides free downloads of films to movie fans in a way that _________ the Hollywood system.",
    opts: ["A. misfires", "B. bypasses", "C. rots"],
    ans: 1,
    exp: "bypasses (vượt qua, bỏ qua). Liên hoan phim cung cấp bản tải xuống phim miễn phí cho người hâm mộ theo cách bỏ qua hệ thống của Hollywood.\n- misfires (thất bại, tịt ngòi)\n- rots (mục nát)"
  }
];

const contentJson = {
  basicInfo: {
    title: "Chapter 2: Vocabulary Review",
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
          sectionTitle: "Vocabulary Review",
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
  const folderId = 'ba08090a-d614-40a8-b7dc-89c7723daf89'; // Chapter 2
  
  const { data, error } = await supabase.from('tests')
    .update({
      content_json: contentJson,
      test_type: 'Standard-Listening'
    })
    .eq('course_id', courseId)
    .eq('folder_id', folderId)
    .eq('title', 'Chapter 2: Vocabulary Review');
    
  if (error) {
    console.error("Error updating:", error);
  } else {
    console.log("Successfully updated test format");
  }
}

run();
