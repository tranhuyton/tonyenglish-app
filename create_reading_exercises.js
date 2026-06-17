const { GoogleGenerativeAI } = require("@google/generative-ai");
const fs = require("fs");
const path = require("path");

const API_KEY = "AIzaSyAwTqP7jueSQ_vvys6wB20lIManuCXebIM";
const genAI = new GoogleGenerativeAI(API_KEY);

const exercises = [
  {
    ex: 1,
    title: "Exercise 1 - A Giant Step for Artificial Enzymes",
    pages: [6, 7],
    answers: `1. D   2. F   3. G   4. C   5. H   6. E
7. Almost 60,000 times as fast as usual.
8. Diels-Alder reaction.
9. The creation of six-membered rings.`
  },
  {
    ex: 2,
    title: "Exercise 2 - Population Growth and Food Supply",
    pages: [8, 9, 10],
    answers: `1. B   2. H   3. G   4. J   5. A   6. F   7. B   8. 1972
9. Any two of the following: quantity, quality, poverty, distribution, ecological side-effects
10. Any two of the following: developing new hybrids, increasing the use of fertilizers, water, pesticides and herbicides, using modern techniques
11. Pakistan / India
12. Burma / Bangladesh / Thailand / Malaysia / Vietnam / the Philippines
13. Mexico`
  },
  {
    ex: 3,
    title: "Exercise 3 - More Than Sympathy",
    pages: [11, 12, 13],
    answers: `1. i   2. v   3. iv   4. vi   5. ix   6. vii`
  },
  {
    ex: 4,
    title: "Exercise 4 - Energy from Biological Sources",
    pages: [14, 15, 16, 17],
    answers: `1. vii   2. i   3. v   4. iv   5. vi   6. ii   7. viii   8. x   9. T   10. T   11. F   12. T   13. F   14. F   15. T`
  },
  {
    ex: 5,
    title: "Exercise 5 - Sleeping Secrets",
    pages: [18, 19, 20],
    answers: `1. iii   2. i   3. vii   4. xiii   5. iv   6. x   7. ii   8. vi   9. ix   10. v   11. xii`
  },
  {
    ex: 6,
    title: "Exercise 6 - It Never Rains",
    pages: [21, 22],
    answers: `1. x   2. vii   3. ii   4. xiv   5. i   6. vi   7. iii   8. xii   9. v   10. ix`
  },
  {
    ex: 7,
    title: "Exercise 7 - Farmers Harvest the Wind",
    pages: [23, 24, 25],
    answers: `1. iii   2. i   3. iv   4. viii   5. vi   6. ii`
  },
  {
    ex: 8,
    title: "Exercise 8 - Germs and Sickness in a Shrinking World",
    pages: [26, 27, 28],
    answers: `1. ix   2. vi   3. viii   4. vii   5. i   6. iv   7. v`
  },
  {
    ex: 9,
    title: "Exercise 9 - On the Wing",
    pages: [29, 30, 31, 32],
    answers: `1. vi   2. xiv   3. ii   4. xii   5. xi   6. ix   7. i   8. xiii   9. viii   10. vii   11. iv   12. YES   13. NOT GIVEN   14. NO`
  }
];

function fileToGenerativePart(filePath, mimeType) {
  return {
    inlineData: {
      data: Buffer.from(fs.readFileSync(filePath)).toString("base64"),
      mimeType
    },
  };
}

async function run() {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

  for (const ex of exercises) {
    console.log("Processing " + ex.title);
    
    const parts = [];
    parts.push({ text: `You are an expert IELTS curriculum designer. 
I will give you images of an IELTS reading exercise (including reading passage and questions) and the text of the answer key.
Your task is to transcribe the exercise and output a strict JSON object that conforms to this IELTS-Reading schema.

JSON Schema Requirement:
{
  "title": "${ex.title}",
  "test_type": "IELTS-Reading",
  "content_json": {
    "parts": [
      {
        "id": "1",
        "title": "Part 1",
        "content": "<HTML string of the FULL reading passage. Use <p>, <b>, <h3> as appropriate. Do NOT include questions here>",
        "sections": [
          {
            "id": "<Section ID>",
            "title": "Questions 1-5 (or whatever range)",
            "content": "<HTML string of instructions for this section>",
            "questionType": "Trắc nghiệm | TFNG | Droplist | Điền từ | Checkbox",
            "questions": [
              {
                "id": "<Question number as string, e.g. '1'>",
                "content": "<Question text>",
                "options": ["<Option 1>", "<Option 2>", "..."],
                "correctAnswer": "<Exact match of correct option string or the fill-in word>",
                "explanation": ""
              }
            ]
          }
        ]
      }
    ]
  }
}

Guidelines for questionType:
- Multiple Choice (A,B,C,D) -> "Trắc nghiệm" (options array must have all choices)
- TRUE/FALSE/NOT GIVEN or YES/NO/NOT GIVEN -> "TFNG" (options must be ["TRUE", "FALSE", "NOT GIVEN"] or ["YES", "NO", "NOT GIVEN"])
- Matching Headings or similar -> "Droplist" (options should be all the Roman numerals or letters provided in the box)
- Fill in the blank (Short Answer) -> "Điền từ" (options: [])

Make sure to map the correct answer from this provided answer key to the 'correctAnswer' field for each question:
--- ANSWER KEY ---
${ex.answers}
------------------

Respond ONLY with the raw JSON object. Do not use Markdown formatting like \`\`\`json. Return valid parseable JSON.`});

    for (const p of ex.pages) {
      parts.push(fileToGenerativePart(`ielts_book_page_${p}.png`, "image/png"));
    }

    try {
      const result = await model.generateContent({
        contents: [{ role: "user", parts }],
        generationConfig: {
          temperature: 0.2,
          responseMimeType: "application/json"
        }
      });
      
      let jsonText = result.response.text();
      
      const outPath = path.join("src/data/Unit 1", `${ex.title}.json`);
      fs.writeFileSync(outPath, jsonText, "utf-8");
      console.log("Saved", outPath);
    } catch (e) {
      console.error("Failed on", ex.title, e.message);
    }
  }
}

run();
