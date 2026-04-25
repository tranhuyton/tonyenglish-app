export const testData = {
  testId: "test_23_nov_24",
  title: "Test 23 November 24",
  timeLimit: "55:54 phút",
  audioUrl: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
  partName: "Part 1:",
  instructions: [
    "You will hear short recordings. For each question, choose the correct answer, A, B, C or D.",
    "You will hear each recording twice."
  ],
  totalQuestions: 4, // Đặt là 4 để anh test chấm điểm cho nhanh
  questions: [
    {
      id: 1,
      text: "Where are the friends going to spend their break?",
      options: ["A. At the beach", "B. In the mountains", "C. At home", "D. In the city"],
      correctAnswer: "B. In the mountains",
      explanation: "Trong đoạn băng, người nam nói rõ ràng là: 'I have successfully booked a wooden cabin in the mountains for our weekend.' Do đó B là đáp án chính xác."
    },
    {
      id: 2,
      text: "What did the boy enjoy the most during the trip?",
      options: ["A. The food", "B. The scenery", "C. The people", "D. The activities"],
      correctAnswer: "A. The food",
      explanation: "Mặc dù anh ấy có nhắc đến cảnh đẹp (scenery), nhưng anh ấy nhấn mạnh: 'Nothing could beat the local seafood we had on the second night.' (Không gì đánh bại được món hải sản địa phương...)"
    },
    {
      id: 3,
      text: "Which instrument is the girl going to play at the school concert?",
      options: ["A. Piano", "B. Violin", "C. Guitar", "D. Flute"],
      correctAnswer: "A. Piano",
      explanation: "Cô gái nói lúc đầu định chơi Guitar, nhưng sau đó giáo viên yêu cầu cô đệm đàn Piano cho dàn đồng ca. Chọn A."
    },
    {
      id: 4,
      text: "What will the weather be like tomorrow?",
      options: ["A. Sunny", "B. Rainy", "C. Cloudy", "D. Windy"],
      correctAnswer: "B. Rainy",
      explanation: "Bản tin thời tiết cảnh báo: 'Make sure to bring your umbrella as heavy showers are expected throughout the day.' (Mang theo ô vì dự báo có mưa rào). Chọn B."
    }
  ]
};