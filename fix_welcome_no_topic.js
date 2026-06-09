const fs = require('fs');
const file = 'src/AITutorSidebar.tsx';
let lines = fs.readFileSync(file, 'utf8').split('\n');

let start = -1;
let end = -1;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes("if (taskType === 'speaking') {") && lines[i+1].includes('Chào em! Thầy là trợ lý Speaking')) {
    start = i;
  }
  if (start !== -1 && lines[i].includes('if (topicImage) welcomeText += `\\n\\n*(📷 Thầy đã nhận được hình ảnh/biểu đồ kèm theo)*`;')) {
    end = i;
    break;
  }
}

if (start !== -1 && end !== -1) {
  const replacement = `          if (taskType === 'speaking') {
              welcomeText = \`Chào em! Thầy là trợ lý Speaking.\\n\\n\`;
              welcomeText += \`Em gửi đề bài hoặc paste câu hỏi vào đây, thầy sẽ tư vấn Kịch bản Lego, gợi ý từ vựng Band 8+ hoặc cùng em luyện tập trả lời nhé!\`;
          } else if (taskType === 'task1') {
              welcomeText = \`Chào em! Thầy là trợ lý Writing Task 1.\\n\\n\`;
              welcomeText += \`Em gửi đề bài hoặc paste nội dung vào đây, thầy sẽ phân tích biểu đồ, lập dàn ý, hoặc chấm điểm bài viết cho em nhé!\`;
          } else if (taskType === 'task2') {
              welcomeText = \`Chào em! Thầy là trợ lý Writing Task 2.\\n\\n\`;
              welcomeText += \`Em gửi đề bài hoặc paste nội dung vào đây, thầy sẽ lập dàn ý, gợi ý từ vựng, hoặc chấm điểm bài làm cho em nhé!\`;
          } else {
              welcomeText = \`Chào em! Thầy đã sẵn sàng hỗ trợ.\\n\\n\`;
              if (topicTitle) welcomeText += \`**💡 Chủ đề:** "\${topicTitle}"\\n\\n\`;
              welcomeText += \`Em gửi câu hỏi hoặc dán nội dung vào đây để thầy hỗ trợ nhé!\`;
          }
          if (topicImage) welcomeText += \`\\n\\n*(📷 Thầy đã nhận được hình ảnh/biểu đồ kèm theo)*\`;`;
  
  lines.splice(start, end - start + 1, replacement);
  fs.writeFileSync(file, lines.join('\n'));
  console.log('Replaced welcome messages completely!');
} else {
  console.log('Could not find boundaries.');
}
