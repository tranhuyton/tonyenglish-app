const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

// Define your Supabase URL and anonymous key
const supabaseUrl = 'https://ubkvzgwespfvrlpjuxkp.supabase.co';
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw';

const supabase = createClient(supabaseUrl, supabaseAnonKey);

const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb'; // Crash Course
const folderId = 'e2ddb86d-139b-4e3c-9878-ba11a0c808fb'; // Chapter 1

const title = "Chapter 1: Mini Test";

const readingPassage = `<h2 class="text-2xl font-bold mb-4 text-center">Supernovae</h2>

<p class="mb-4">Supernovae are the greatest of all stellar explosions, events so powerful that for a brief period a single star will emit, in its death throes, as much light as all the stars of the Milky Way put together. <strong>Such events</strong> are rare. <strong>Our Sun is not fated to become a supernova, but it was born out of the debris of supernova explosions of the distant past, when our Milky Way galaxy was young.</strong> Apart from hydrogen, every atom in our bodies, and every atom on Earth except for hydrogen and helium (there is no helium in our bodies) was manufactured inside stars and then expelled into space by supernova explosions. They laced the clouds of hydrogen and helium from which the Sun and its family of planets formed.</p>

<p class="mb-4">Over three decades, beginning in the 1950s, theorists had developed what seemed to be a satisfactory understanding of supernova explosions, based on their knowledge of the laws of physics, on observations of such explosions in remote galaxies and of the debris from old supernova explosions in our own galaxy, and on computer models of how stars worked. But until 1987 they had no means of checking this understanding directly. The explosion of a star known as Sanduleak -69°C 202 to become a supernova first visible from Earth on the night of February 23/24, 1987 was possibly the single most important event in astronomy since the invention of the telescope.</p>

<p class="mb-4">The event, <strong>dubbed</strong> SN1987A, took place in the Large Magellanic Cloud, a galaxy close to our own Milky Way and part of the system of galaxies, held together by gravity, recognized as the Local Group. <strong>[A]</strong> At a distance of 180,000 light years, just next door by cosmological standards, SN1987A was by far the closest supernova to have occurred since 1604, when the last known supernova in our own galaxy exploded, just before the development of the astronomical telescope. <strong>[B]</strong> It was near enough to be studied in detail by a battery of instruments, including conventional telescopes on mountaintops, X-ray detectors on board satellites in space and neutrino detectors buried deep beneath the ground. <strong>[C]</strong> Both in broad outline and in most details, <strong>those observations</strong> showed over the years following the outburst that the astronomers did have a good understanding of how supernovae work. <strong>[D]</strong></p>`;

const qList = [
  {
    q: "The phrase <strong>Such events</strong> in the passage refers to",
    opts: [
      "Death throes of a star",
      "Supernovae",
      "The emission of light",
      "Explosions of small stars"
    ],
    ans: 1,
    exp: '"Such events" thay thế cho "stellar explosions" (các vụ nổ vì sao) hay chính là "Supernovae" được nhắc đến ở ngay câu trước đó.'
  },
  {
    q: "Which of the sentences below best expresses the essential information in the highlighted sentence in the passage? <em>Incorrect choices change the meaning in important ways or leave out essential information.</em><br/><br/>Highlighted sentence: <strong>Our Sun is not fated to become a supernova, but it was born out of the debris of supernova explosions of the distant past, when our Milky Way galaxy was young.</strong>",
    opts: [
      "Although the Sun is not going to be a supernova, its birth is related with supernova explosions that occurred in the beginning stage of our galaxy.",
      "The Sun is not a supernova, but it was part of a supernova when our Milky Way started to exist.",
      "It is believed the Sun will explode in the future, but it was born out of a supernova when our Milky Way started in the distant past.",
      "When our galaxy was young, the Sun was separated from the galaxy because of a supernova explosion."
    ],
    ans: 0,
    exp: 'Câu gốc mang ý nghĩa: "Mặt trời của chúng ta không được định sẵn để trở thành một siêu tân tinh (supernova), nhưng nó được sinh ra từ những mảnh vỡ của các vụ nổ siêu tân tinh trong quá khứ xa xôi, khi dải Ngân hà của chúng ta còn trẻ."<br/><br/>Đáp án A truyền tải chính xác nhất ý nghĩa này: "Mặc dù Mặt trời sẽ không trở thành một siêu tân tinh, nhưng sự ra đời của nó có liên quan đến các vụ nổ siêu tân tinh xảy ra ở giai đoạn đầu của thiên hà chúng ta."'
  },
  {
    q: "Before 1987, scientists based their knowledge of supernovae on all of the following EXCEPT",
    opts: [
      "computer models",
      "direct observation of a supernova explosion",
      "debris of old supernova explosions",
      "laws of physics"
    ],
    ans: 1,
    exp: 'Đoạn 2 liệt kê các cơ sở cho kiến thức của các nhà khoa học trước năm 1987: "knowledge of the laws of physics" (đáp án D), "debris from old supernova explosions" (đáp án C), "computer models" (đáp án A). Đồng thời, tác giả khẳng định "until 1987 they had no means of checking this understanding directly" (cho đến năm 1987 họ không có cách nào để kiểm tra trực tiếp). Do đó, họ không dựa trên quan sát trực tiếp (đáp án B).'
  },
  {
    q: "The word <strong>dubbed</strong> in the passage is closest in meaning to",
    opts: [
      "identified as",
      "named",
      "combined",
      "praised"
    ],
    ans: 1,
    exp: '"Dubbed" có nghĩa là được đặt tên, gọi tên (named). Sự kiện này được đặt tên là SN1987A.'
  },
  {
    q: "The phrase <strong>those observations</strong> in the passage refers to the observations of",
    opts: [
      "the Large Magellanic Cloud",
      "the Milky Way",
      "SN1987A",
      "satellites"
    ],
    ans: 2,
    exp: 'Đoạn văn đang nói về việc nghiên cứu chi tiết sự kiện SN1987A bằng nhiều công cụ khác nhau (kính viễn vọng, vệ tinh...). Do đó "those observations" (những quan sát đó) chính là đề cập đến các quan sát về hiện tượng SN1987A này.'
  },
  {
    q: "Look at the four squares [■] that indicate where the following sentence could be added to the passage.<br/><br/><strong>Although some details did not match up to expectations, there were no major surprises.</strong><br/><br/>Where would the sentence best fit? Click on a square to add it to the passage.",
    opts: [
      "[A]",
      "[B]",
      "[C]",
      "[D]"
    ],
    ans: 3,
    exp: 'Câu cần điền có nghĩa là: "Mặc dù một số chi tiết không khớp với kỳ vọng, nhưng không có những bất ngờ lớn nào." Câu trước vị trí [D] nói rằng các quan sát cho thấy các nhà thiên văn học đã hiểu đúng về cách hoạt động của siêu tân tinh (did have a good understanding). Việc bổ sung ý "không có bất ngờ lớn nào" hoàn toàn hợp lý và củng cố cho sự hiểu biết tốt đó của họ. Do đó vị trí [D] là phù hợp nhất.'
  }
];

const parts = [
  {
    id: 'part-1',
    readingText: readingPassage,
    sections: [
      {
        id: 'sec-1',
        sectionTitle: '',
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
];

async function run() {
  const payload = {
    title: title,
    test_type: 'Standard-Reading',
    folder_id: folderId,
    course_id: courseId,
    is_published: true,
    order_index: 3,
    content_json: {
      basicInfo: {
        title: title,
        skill: 'Standard-Reading',
        category: 'exercise',
        timeLimit: 0,
        courseId: courseId
      },
      parts: parts
    },
    json_config: {
      timeLimit: 0,
      questions: []
    }
  };

  const { data, error } = await supabase.from('tests').insert([payload]);
  
  if (error) {
    console.error('Lỗi insert:', error);
  } else {
    console.log('Thành công!');
  }
}

run();
