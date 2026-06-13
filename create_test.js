const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');

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
    ans: 0
  },
  {
    q: "It is reported that people are more impressed by the dancing of those whose bodies are more **symmetrical**.",
    opts: ["balanced", "slender"],
    ans: 0
  },
  {
    q: "More than two miles of roadway has been blocked with trees, stones and other **debris**, caused by the explosion.",
    opts: ["charcoal", "broken pieces"],
    ans: 1
  },
  {
    q: "Several countries are still in the **throes** of a flu outbreak.",
    opts: ["sufferings", "grooves"],
    ans: 0
  },
  {
    q: "Another knee surgery **dims** the future of the talented tennis player.",
    opts: ["lumps", "obscures"],
    ans: 1
  },
  {
    q: "A South African paleontologist presented his view that human ancestors were hunted by **predatory** birds.",
    opts: ["living on earth", "eating animals"],
    ans: 1
  },
  {
    q: "According to one theory, variation in genetic **make-up** determines each person's reaction to certain painkillers.",
    opts: ["willingness", "difference"],
    ans: 1
  },
  {
    q: "You have to choose between having a **sturdy** structure that does not become unstable and attracting people with a fancy exterior.",
    opts: ["strong", "scarce"],
    ans: 0
  },
  {
    q: "On Aug. 23, 1996, Noel Gallagher sang lead vocals on Oasis' performance for MTV's Unplugged, and his brother Liam's trademark singing voice was **conspicuous** by its absence.",
    opts: ["marked", "representational"],
    ans: 0
  },
  {
    q: "The criminal was sentenced to death because of the **severity** of his crime.",
    opts: ["complexity", "cruelty"],
    ans: 1
  }
];

const questions = questionsData.map((data) => ({
  id: crypto.randomUUID(),
  type: 'mcq',
  question: data.q,
  options: data.opts,
  correctAnswer: data.ans,
  explanation: ''
}));

const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
const folderId = 'e2ddb86d-139b-4e3c-9878-ba11a0c808fb';

const payload = {
  title: 'Chapter 1: Words',
  test_type: 'standard',
  course_id: courseId,
  folder_id: folderId,
  is_published: true,
  content_json: {
    basicInfo: {
      title: 'Chapter 1: Words',
      skill: 'standard',
      timeLimit: '15',
      courseId: courseId,
      category: 'test'
    },
    questions: questions
  },
  json_config: {
    timeLimit: 15,
    questions: questions
  }
};

async function run() {
  const { data, error } = await supabase.from('tests').insert([payload]);
  if (error) {
    console.error('Error inserting test:', error);
  } else {
    console.log('Test created successfully!');
  }
}

run();
