const { createClient } = require('@supabase/supabase-js');

// 1. Setup Supabase
const supabaseUrl = 'https://ubkvzgwespfvrlpjuxkp.supabase.co';
const supabaseKey = 'sb_secret_5huRcnLVzDU92RUpJ6H6mw_zOGBmCNw'; // Use the secret key from your previous requests to write to DB
const anonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw';
const supabase = createClient(supabaseUrl, supabaseKey);

const topics = [
  "Sentence Patterns", "Subject and Verb Agreement", "Present Subjunctive", "Past Subjunctive", 
  "Past Perfect Subjunctive", "Mixed Subjunctive", "Question Tag", "Measures", "Regular and Irregular Verbs", 
  "Verbal", "Verbs"
];

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function generateTest(topic) {
  const prompt = `You are an expert English teacher. Create a grammar test for the topic: "${topic}".
Output ONLY a valid JSON string without markdown code blocks, backticks, or any conversational text.

The JSON MUST follow this exact structure:
{
  "basicInfo": {
    "title": "Grammar: ${topic}",
    "timeLimit": "00:15:00",
    "category": "exercise"
  },
  "parts": [
    {
      "id": "p1",
      "title": "Part 1: Multiple Choice",
      "content": "Choose the best answer to complete the sentences.",
      "sections": [
        {
          "id": "s1",
          "questionType": "Trắc nghiệm",
          "content": "",
          "questions": [
            {
              "id": "1",
              "content": "This is a question about ${topic}. For example: I have ___ apple.",
              "options": ["A. a", "B. an", "C. the", "D. no article"],
              "correctAnswer": "B",
              "explanation": "Because apple starts with a vowel."
            }
          ]
        }
      ]
    }
  ]
}

Rules:
1. Create exactly 10 high-quality multiple choice questions.
2. Options MUST start with "A. ", "B. ", "C. ", "D. ".
3. correctAnswer MUST be exactly one uppercase letter (A, B, C, or D).
4. Provide a clear explanation in Vietnamese for each question.
5. The questions must accurately test the topic "${topic}".
6. Make sure the JSON is perfectly valid.`;

  const res = await fetch(`${supabaseUrl}/functions/v1/omni-ai-grader`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${anonKey}`
    },
    body: JSON.stringify({
      taskType: 'tutor',
      prompt: prompt,
      content: ''
    })
  });

  if (!res.ok) {
    const errorBody = await res.text();
    throw new Error(`Edge function failed: ${res.statusText} - ${errorBody}`);
  }

  const result = await res.json();
  let text = result.result; // The omni-ai-grader returns { result: "..." }
  text = text.replace(/```json/gi, '').replace(/```/g, '').trim();
  return JSON.parse(text);
}

async function run() {
  console.log(`Starting to generate tests for ${topics.length} topics...`);
  
  for (let i = 0; i < topics.length; i++) {
    const topic = topics[i];
    console.log(`[${i+1}/${topics.length}] Generating test for: ${topic}...`);
    
    try {
      const testJson = await generateTest(topic);
      
      const title = testJson.basicInfo?.title || `Grammar: ${topic}`;
      const testType = testJson.basicInfo?.category || "exercise";
      
      const { data, error } = await supabase
        .from('tests')
        .insert([{
          title: title,
          test_type: testType,
          content_json: testJson,
          is_published: true
        }]);
        
      if (error) {
        console.error(`Failed to insert ${topic} into database:`, error.message);
      } else {
        console.log(`✅ Successfully created test: ${title}`);
      }
      
    } catch (e) {
      console.error(`❌ Error generating/inserting test for ${topic}:`, e.message);
    }
    
    if (i < topics.length - 1) {
      await sleep(4000);
    }
  }
  
  console.log('🎉 All tasks completed!');
}

run();
