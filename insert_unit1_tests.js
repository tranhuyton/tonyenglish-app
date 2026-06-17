const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const crypto = require('crypto');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_SERVICE_ROLE_KEY'));

const exercises = [
  "Exercise 1: A Giant Step for Artificial Enzymes",
  "Exercise 2: Population Growth and Food Supply",
  "Exercise 3: More Than Sympathy",
  "Exercise 4: Energy from Biological Sources",
  "Exercise 5: Sleeping Secrets",
  "Exercise 6: It Never Rains",
  "Exercise 7: Farmers Harvest the Wind",
  "Exercise 8: Germs and Sickness in a Shrinking World",
  "Exercise 9: On the Wing"
];

async function run() {
  const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
  const parentFolderId = '23c5be28-2449-46a4-a459-f22c6f82895f'; // "Reading Strategies"
  
  // Find Unit 1 folder
  const { data: unit1Folder, error: fErr } = await supabase
    .from('folders')
    .select('id')
    .eq('title', 'Unit 1')
    .eq('parent_id', parentFolderId)
    .single();
    
  if (fErr || !unit1Folder) {
    console.error("Could not find Unit 1 folder", fErr);
    return;
  }
  
  const folderId = unit1Folder.id;
  
  for (let i = 0; i < exercises.length; i++) {
    const title = exercises[i];
    
    // Check if exists
    const { data: existing } = await supabase
      .from('tests')
      .select('id')
      .eq('title', title)
      .eq('folder_id', folderId)
      .single();
      
    if (existing) {
      console.log(`${title} already exists.`);
      continue;
    }
    
    const payload = {
      title: title,
      test_type: 'IELTS-Reading',
      course_id: courseId,
      folder_id: folderId,
      is_published: true,
      order_index: i + 1,
      content_json: {
        basicInfo: {
          title: title,
          skill: 'IELTS-Reading',
          timeLimit: '60',
          courseId: courseId,
          folderId: folderId,
          category: 'test',
          scoreType: '1 điểm/ câu đúng'
        },
        parts: [
          {
            title: "Passage 1",
            content: "<p>Nội dung bài đọc sẽ được cập nhật sau từ PDF.</p>",
            questionGroups: []
          }
        ]
      },
      json_config: {}
    };
    
    const { error } = await supabase.from('tests').insert([payload]);
    if (error) {
      console.error(`Error inserting ${title}:`, error);
    } else {
      console.log(`Created: ${title}`);
    }
  }
  
  console.log("Done inserting all tests.");
}

run();
