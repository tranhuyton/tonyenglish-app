const fs = require('fs');
const file = 'src/AITutorSidebar.tsx';
let content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');

const t = `        } else {
          welcomeText = \`Chào em! Thầy đã nhận được yêu cầu phân tích.\\n\\n\`;
          if (topicTitle) welcomeText += \`**💡 Đề bài:** "\${topicTitle}"\\n\\n\`;
          if (topicImage) welcomeText += \`*(📷 Đã nhận kèm hình ảnh/biểu đồ)*\\n\\n\`;
          if (taskType === 'speaking') welcomeText += \`Em cần thầy tư vấn Kịch bản Lego, gợi ý từ vựng hay viết câu mở bài (Hook) nào?\`;
          else if (taskType === 'task1' || taskType === 'task2') welcomeText += \`Em cần thầy lập dàn ý, gợi ý từ vựng hay chấm điểm bài làm của em?\`;
          else welcomeText += \`Em gửi câu hỏi hoặc dán nội dung vào đây để thầy hỗ trợ nhé!\`;
        }`;

const r = `        } else {
          if (taskType === 'speaking') {
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
          if (topicImage) welcomeText += \`\\n\\n*(📷 Thầy đã nhận được hình ảnh/biểu đồ kèm theo)*\`;
        }`;

if (content.includes(t)) {
  content = content.replace(t, r);
  console.log('Fixed welcome message');
  fs.writeFileSync(file, content);
} else {
  console.log('Welcome message target not found');
}
