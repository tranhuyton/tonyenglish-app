const fs = require('fs');
const file = 'src/AITutorSidebar.tsx';
let lines = fs.readFileSync(file, 'utf8').split('\n');

let start = -1;
let end = -1;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes('welcomeText = `Ch') && lines[i].includes('u c') && lines[i].includes('ph')) {
    start = i;
  }
  if (start !== -1 && lines[i].includes('else welcomeText +=')) {
    end = i;
    break;
  }
}

if (start !== -1 && end !== -1) {
  const replacement = `          if (taskType === 'speaking') {
              welcomeText = \`Chào em! Thầy là trợ lý Speaking.\\n\\n\`;
              if (topicTitle) welcomeText += \`**💡 Chủ đề hiện tại:** "\${topicTitle}"\\n\\n\`;
              welcomeText += \`Em cần thầy tư vấn Kịch bản Lego, gợi ý từ vựng Band 8+ hay luyện tập trả lời câu hỏi nào?\`;
          } else if (taskType === 'task1') {
              welcomeText = \`Chào em! Thầy là trợ lý Writing Task 1.\\n\\n\`;
              if (topicTitle) welcomeText += \`**💡 Chủ đề hiện tại:** "\${topicTitle}"\\n\\n\`;
              welcomeText += \`Em cần thầy phân tích biểu đồ, lập dàn ý, hay chấm điểm bài viết của em?\`;
          } else if (taskType === 'task2') {
              welcomeText = \`Chào em! Thầy là trợ lý Writing Task 2.\\n\\n\`;
              if (topicTitle) welcomeText += \`**💡 Chủ đề hiện tại:** "\${topicTitle}"\\n\\n\`;
              welcomeText += \`Em cần thầy lập dàn ý, gợi ý từ vựng hay chấm điểm bài làm của em?\`;
          } else {
              welcomeText = \`Chào em! Thầy đã sẵn sàng hỗ trợ.\\n\\n\`;
              if (topicTitle) welcomeText += \`**💡 Đề bài:** "\${topicTitle}"\\n\\n\`;
              welcomeText += \`Em gửi câu hỏi hoặc dán nội dung vào đây để thầy hỗ trợ nhé!\`;
          }
          if (topicImage) welcomeText += \`\\n\\n*(📷 Thầy đã nhận được hình ảnh/biểu đồ kèm theo)*\`;`;
  
  lines.splice(start, end - start + 1, replacement);
  fs.writeFileSync(file, lines.join('\n'));
  console.log('Replaced welcome messages!');
} else {
  console.log('Could not find boundaries.');
}
