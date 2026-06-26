require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

const COURSE_ID = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
const FOLDER_ID = '33ff218e-f8ba-48b6-8c7e-f68b64f3be1b';

const units = [
  { file: 'public/unit2_ielts.json', title: 'Unit 2: Siesta Time', order: 2 },
  { file: 'public/unit3_ielts.json', title: "Unit 3: The Interesting Lore of April Fools' Day", order: 3 },
  { file: 'public/unit4_ielts.json', title: 'Unit 4: Oh, Temptation', order: 4 },
];

async function syncUnit(unit) {
  const data = JSON.parse(fs.readFileSync(unit.file, 'utf8'));

  // Check if exists
  const { data: existing, error: searchError } = await supabase
    .from('tests')
    .select('id')
    .eq('course_id', COURSE_ID)
    .eq('order_index', unit.order);

  if (searchError) throw searchError;

  if (existing && existing.length > 0) {
    const testId = existing[0].id;
    const { error: updateError } = await supabase
      .from('tests')
      .update({
        title: unit.title,
        content_json: data,
        test_type: 'MCQ (Standard)',
        folder_id: FOLDER_ID,
        is_published: true
      })
      .eq('id', testId);
    if (updateError) throw updateError;
    console.log(`✅ Updated ${unit.title} (id: ${testId})`);
  } else {
    const { data: inserted, error: insertError } = await supabase
      .from('tests')
      .insert({
        folder_id: FOLDER_ID,
        title: unit.title,
        test_type: 'MCQ (Standard)',
        content_json: data,
        is_published: true,
        course_id: COURSE_ID,
        order_index: unit.order
      })
      .select('id');
    if (insertError) throw insertError;
    console.log(`✅ Inserted ${unit.title} (id: ${inserted[0].id})`);
  }
}

async function main() {
  try {
    for (const unit of units) {
      await syncUnit(unit);
    }
    console.log('\n🎉 All units synced successfully!');
  } catch (error) {
    console.error('Error syncing to Supabase:', error);
  }
}

main();
