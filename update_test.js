const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

const questionsData = [
  {
    q: "When Mario was carried to the hospital, he was unconscious, with several **puncture** wounds to his stomach.",
    opts: ["small hole", "tattoo"],
    ans: "A"
  },
  {
    q: "It is reported that people are more impressed by the dancing of those whose bodies are more **symmetrical**.",
    opts: ["balanced", "slender"],
    ans: "A"
  },
  {
    q: "More than two miles of roadway has been blocked with trees, stones and other **debris**, caused by the explosion.",
    opts: ["charcoal", "broken pieces"],
    ans: "B"
  },
  {
    q: "Several countries are still in the **throes** of a flu outbreak.",
    opts: ["sufferings", "grooves"],
    ans: "A"
  },
  {
    q: "Another knee surgery **dims** the future of the talented tennis player.",
    opts: ["lumps", "obscures"],
    ans: "B"
  },
  {
    q: "A South African paleontologist presented his view that human ancestors were hunted by **predatory** birds.",
    opts: ["living on earth", "eating animals"],
    ans: "B"
  },
  {
    q: "According to one theory, variation in genetic **make-up** determines each person's reaction to certain painkillers.",
    opts: ["willingness", "difference"],
    ans: "B"
  },
  {
    q: "You have to choose between having a **sturdy** structure that does not become unstable and attracting people with a fancy exterior.",
    opts: ["strong", "scarce"],
    ans: "A"
  },
  {
    q: "On Aug. 23, 1996, Noel Gallagher sang lead vocals on Oasis' performance for MTV's Unplugged, and his brother Liam's trademark singing voice was **conspicuous** by its absence.",
    opts: ["marked", "representational"],
    ans: "A"
  },
  {
    q: "The criminal was sentenced to death because of the **severity** of his crime.",
    opts: ["complexity", "cruelty"],
    ans: "B"
  }
];

const questions = questionsData.map((data, index) => ({
  id: String(index + 1),
  content: data.q,
  tags: '',
  audioUrl: '',
  explanation: '',
  options: data.opts,
  correctAnswer: data.ans
}));

const parts = [
  {
    id: Date.now().toString(),
    name: 'Part 1',
    audioUrl: '',
    sections: [
      {
        id: (Date.now() + 1).toString(),
        title: 'Choose the right meaning for the words in bold.',
        content: '',
        tags: '',
        questionType: 'Trắc nghiệm',
        audioUrl: '',
        explanation: '',
        questions: questions
      }
    ]
  }
];

async function run() {
  const { data: testData, error: errFetch } = await supabase.from('tests').select('id, content_json, json_config').eq('title', 'Chapter 1: Words');
  if (errFetch || !testData || testData.length === 0) return console.log('Test not found');
  
  const test = testData[0];
  
  const newContentJson = {
    ...test.content_json,
    parts: parts
  };
  
  const newJsonConfig = {
    ...test.json_config,
    parts: parts
  };
  
  const { error: updErr } = await supabase.from('tests').update({
    content_json: newContentJson,
    json_config: newJsonConfig
  }).eq('id', test.id);
  
  if (updErr) console.error('Update error:', updErr);
  else console.log('Updated parts successfully!');
}

run();
