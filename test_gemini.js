const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const { GoogleGenerativeAI, SchemaType } = require('@google/generative-ai');

const env = fs.readFileSync('.env', 'utf-8');
const urlMatch = env.match(/^VITE_SUPABASE_URL=(.*)$/m);
const keyMatch = env.match(/^VITE_SUPABASE_SERVICE_ROLE_KEY=(.*)$/m);
const geminiMatch = env.match(/^VITE_GEMINI_API_KEY=(.*)$/m);

const supabase = createClient(urlMatch[1].trim(), keyMatch[1].trim());
const genAI = new GoogleGenerativeAI(geminiMatch[1].trim());

async function run() {
    const { data } = await supabase.from('tests').select('id, title, content_json').ilike('title', '%Unit 15: Volume 6%');
    if (!data || data.length === 0) {
        console.log('Unit not found');
        return;
    }
    
    const test = data[0];
    console.log('Testing on:', test.title);
    
    if (!test.content_json || !test.content_json.parts || !test.content_json.parts[1]) {
        console.log('No reading part found');
        return;
    }
    
    const readingPart = test.content_json.parts[1];
    const storyHtml = readingPart.content;
    const storyText = storyHtml.replace(/<[^>]*>/g, '').trim();
    
    const questionsToProcess = [];
    
    // Flatten all questions
    for (const sec of readingPart.sections) {
        if (!sec.questions) continue;
        for (const q of sec.questions) {
            questionsToProcess.push({
                sectionId: sec.id,
                questionId: q.id,
                content: q.content,
                options: q.options || [],
                correctAnswer: q.correctAnswer,
                originalExplanation: q.explanation
            });
        }
    }
    
    console.log(`Found ${questionsToProcess.length} questions to explain.`);
    
    // Prepare prompt
    const prompt = `Bạn là một gia sư tiếng Anh tận tâm và chuyên nghiệp.
Dưới đây là một bài đọc hiểu tiếng Anh:
---
${storyText}
---

Dưới đây là danh sách các câu hỏi trắc nghiệm / True-False, kèm theo các đáp án (nếu có) và ĐÁP ÁN ĐÚNG:
${questionsToProcess.map((q, i) => `
Câu hỏi ${i + 1}: ${q.content}
Các lựa chọn: ${q.options.join(' | ')}
Đáp án đúng: ${q.correctAnswer}
`).join('\n')}

Nhiệm vụ của bạn là viết "giải thích đáp án" bằng TIẾNG VIỆT cho TỪNG câu hỏi một cách chi tiết, dễ hiểu nhất.
Yêu cầu:
- Trích dẫn câu văn hoặc cụm từ cụ thể trong bài đọc làm bằng chứng.
- Giải thích ngắn gọn tại sao dựa vào bằng chứng đó ta lại chọn đáp án này.
- Đối với câu True/False, hãy giải thích rõ thông tin trong bài ủng hộ hay bác bỏ nhận định đó.
- Đối với từ vựng khó, bạn có thể dịch nhanh nghĩa của từ vựng đó trong ngữ cảnh bài đọc.
- Văn phong thân thiện, truyền cảm hứng, giống như một gia sư (xưng là "Gia sư", gọi người học là "bạn").

Trả về kết quả CỰC KỲ NGHIÊM NGẶT dưới định dạng MẢNG JSON.
Mảng này chứa đúng ${questionsToProcess.length} chuỗi (string), mỗi chuỗi là phần giải thích cho một câu hỏi tương ứng theo đúng thứ tự.`;

    const schema = {
        type: SchemaType.ARRAY,
        description: "List of explanations for the questions",
        items: {
            type: SchemaType.STRING,
        },
    };

    const model = genAI.getGenerativeModel({
        model: "gemini-2.5-flash",
        generationConfig: {
            responseMimeType: "application/json",
            responseSchema: schema,
        }
    });

    try {
        console.log('Sending request to Gemini...');
        const result = await model.generateContent(prompt);
        const responseText = result.response.text();
        const explanations = JSON.parse(responseText);
        
        console.log('\n--- RESULTS ---\n');
        for (let i = 0; i < questionsToProcess.length; i++) {
            console.log(`Q: ${questionsToProcess[i].content}`);
            console.log(`A: ${questionsToProcess[i].correctAnswer}`);
            console.log(`NEW EXP: ${explanations[i]}`);
            console.log('-------------------------');
        }
    } catch (e) {
        console.error('Error generating explanations:', e);
    }
}

run();
