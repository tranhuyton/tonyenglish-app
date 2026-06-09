const fs = require('fs');

const topics = [
  "Present Simple", "Present Continuous", "Present Simple vs Present Continuous", "Present Continuous vs Future Simple", "Present Perfect Tense", "Present Perfect Continuous", "Present Perfect vs Past Simple", "Present Perfect vs Present Perfect Continuous", "Present Simple - Present Continuous - Present Perfect", "Past Simple", "Past Continuous", "Past Simple vs Past Continuous", "Past Simple vs Past Perfect", "Past Perfect", "Past Perfect Continuous", "Past Perfect vs Past Perfect Continuous", "Past Simple - Past Continuous - Past Perfect", "Future Simple", "Be going to", "Future Continuous", "Future Perfect", "Future Perfect vs Future Continuous", "Future Simple - Be Going To - Present Continuous", "Future Simple vs Future Continuous", "Verb Tenses"
];

const SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw";
const SUPABASE_SERVICE_ROLE_KEY = "sb_secret_5huRcnLVzDU92RUpJ6H6mw_zOGBmCNw";

async function generateTest(topic, index) {
  const prompt = `Tạo 1 đề thi trắc nghiệm tiếng Anh cho chủ đề ngữ pháp: "${topic}".
Bao gồm 20 câu hỏi trắc nghiệm (10 câu cơ bản, 10 câu nâng cao).
Mỗi câu có 4 đáp án A, B, C, D, chỉ có 1 đáp án đúng. Kèm theo giải thích chi tiết tiếng Việt.
Trả về định dạng JSON theo cấu trúc sau, KHÔNG CÓ BẤT KỲ VĂN BẢN NÀO KHÁC BÊN NGOÀI JSON (không dùng markdown code block, chỉ trả về JSON thuần):
{
  "basicInfo": {
    "title": "${index}. Grammar: ${topic}",
    "courseId": "all",
    "folderId": "",
    "skill": "Mixed-Paper",
    "category": "exercise",
    "mode": "Đề thi",
    "timeLimit": "40",
    "scoreType": "1 điểm/ câu đúng"
  },
  "parts": [
    {
      "id": "part_1",
      "title": "Part 1: Cơ bản",
      "content": "",
      "sections": [
        {
          "id": "sec_1",
          "title": "",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "q1",
              "content": "[Nội dung câu hỏi]",
              "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
              "correctAnswer": "A",
              "explanation": "[Giải thích]"
            }
          ]
        }
      ]
    },
    {
      "id": "part_2",
      "title": "Part 2: Nâng cao",
      "content": "",
      "sections": [
        {
          "id": "sec_2",
          "title": "",
          "content": "",
          "questionType": "Trắc nghiệm",
          "questions": [
            {
              "id": "q11",
              "content": "[Nội dung câu hỏi]",
              "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
              "correctAnswer": "A",
              "explanation": "[Giải thích]"
            }
          ]
        }
      ]
    }
  ]
}`;

  const res = await fetch(`${SUPABASE_URL}/functions/v1/omni-ai-grader`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
    },
    body: JSON.stringify({
      taskType: 'custom',
      prompt: prompt,
      content: "Please strictly output valid JSON only."
    })
  });

  if (!res.ok) throw new Error("Edge Function error: " + res.statusText);
  const data = await res.json();
  let text = data.result;
  if (!text) throw new Error("Empty response from AI");
  text = text.replace(/```json/gi, '').replace(/```/g, '').trim();
  
  return JSON.parse(text);
}

async function uploadToSupabase(title, content_json) {
  const payload = {
    title: title,
    course_id: null,
    folder_id: null,
    test_type: "Mixed-Paper",
    content_json: content_json,
    is_published: true
  };

  const res = await fetch(`${SUPABASE_URL}/rest/v1/tests`, {
    method: "POST",
    headers: {
      "apikey": SUPABASE_SERVICE_ROLE_KEY,
      "Authorization": `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`,
      "Content-Type": "application/json",
      "Prefer": "return=minimal"
    },
    body: JSON.stringify(payload)
  });

  if (!res.ok) throw new Error("Supabase API error: " + res.statusText);
}

const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

async function run() {
  console.log("Starting Tenses test generation via Edge Function...");
  let successCount = 0;
  for (let i = 0; i < topics.length; i++) {
    const topic = topics[i];
    const index = i + 75; // Continue from 74
    console.log(`[${index}/${74+topics.length}] Generating ${topic}...`);
    
    let retries = 3;
    while (retries > 0) {
      try {
        const json = await generateTest(topic, index);
        await uploadToSupabase(`${index}. Grammar: ${topic}`, json);
        console.log(`✅ Successfully created: ${index}. Grammar: ${topic}`);
        successCount++;
        break;
      } catch (err) {
        console.error(`❌ Error generating ${topic}:`, err.message);
        retries--;
        if (retries > 0) {
          console.log("Retrying in 5 seconds...");
          await delay(5000);
        } else {
          console.error("Failed to generate", topic, "after 3 retries.");
        }
      }
    }
    
    await delay(3000);
  }
  console.log(`🎉 All ${successCount} tests generated and uploaded!`);
}

run();
