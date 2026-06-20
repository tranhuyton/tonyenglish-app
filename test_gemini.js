const { createClient } = require('@supabase/supabase-js');
const { GoogleGenerativeAI } = require('@google/generative-ai');
const dotenv = require('dotenv');

dotenv.config();

const supabase = createClient(
  process.env.VITE_SUPABASE_URL,
  process.env.VITE_SUPABASE_SERVICE_ROLE_KEY
);

const genAI = new GoogleGenerativeAI(process.env.VITE_GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash", generationConfig: { responseMimeType: "application/json" } });

async function run() {
  const i = 2; // Test with Activity 2
  const title = 'Unit 3: Listening Activity ' + i;
  const { data } = await supabase.from('tests').select('id, content_json').eq('title', title).single();
  
  if (data && data.content_json && data.content_json.parts && data.content_json.parts[0].sections[0].questions) {
    let cj = data.content_json;
    let sec = cj.parts[0].sections[0];
    const questions = sec.questions;
    const transcript = sec.explanation; // This is where the transcript is stored now
    
    if (!transcript) {
      console.log('No transcript found in sec.explanation');
      return;
    }

    const qs = questions.map((q, idx) => `Question ${idx + 1}: ${q.answer || q.content}\nCorrect Answer: ${q.correctAnswer}`).join('\n\n');
    
    const prompt = `You are an English teacher creating answer explanations for a listening test.
Here is the audio transcript:
"""
${transcript}
"""

Here are the questions and their correct answers:
"""
${qs}
"""

For each question, extract the exact short sentence or phrase from the transcript that contains the answer, and provide a short Vietnamese translation/explanation. 
Format each explanation EXACTLY like this: "Dựa vào transcript: '[English quote]'. ([Vietnamese translation/explanation])."
Keep it very concise. Only include the most relevant part of the transcript.

Return ONLY a valid JSON array of strings, where each string is the explanation for the corresponding question in order. The array length must exactly match the number of questions (${questions.length}).`;

    console.log('Calling Gemini...');
    const result = await model.generateContent(prompt);
    const responseText = result.response.text();
    console.log(responseText);
    
    try {
      const explanations = JSON.parse(responseText);
      if (explanations.length === questions.length) {
        console.log('Success!');
      } else {
        console.log(`Length mismatch: got ${explanations.length}, expected ${questions.length}`);
      }
    } catch (e) {
      console.log('JSON Parse error:', e);
    }
  }
}

run();
