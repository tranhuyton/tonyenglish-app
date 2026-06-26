require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

const folderId = '33ff218e-f8ba-48b6-8c7e-f68b64f3be1b';
const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';

async function syncUnit(unitNumber, jsonFile) {
  try {
    const data = JSON.parse(fs.readFileSync(jsonFile, 'utf8'));

    const { data: existingTests, error: searchError } = await supabase
        .from('tests')
        .select('id')
        .eq('folder_id', folderId)
        .eq('order_index', unitNumber);
    
    if (searchError) throw searchError;

    if (existingTests && existingTests.length > 0) {
        const testId = existingTests[0].id;
        const { error: updateError } = await supabase
            .from('tests')
            .update({
                title: data.basicInfo.title,
                content_json: data
            })
            .eq('id', testId);
        if (updateError) throw updateError;
        console.log(`✅ Successfully updated Unit ${unitNumber} (${data.basicInfo.title}) in Supabase!`);
    } else {
        const { error: insertError } = await supabase
            .from('tests')
            .insert({
                folder_id: folderId,
                title: data.basicInfo.title,
                test_type: 'MCQ (Standard)',
                content_json: data,
                is_published: true,
                course_id: courseId,
                order_index: unitNumber
            });
        if (insertError) throw insertError;
        console.log(`✅ Successfully inserted Unit ${unitNumber} (${data.basicInfo.title}) into Supabase!`);
    }
  } catch (error) {
    console.error(`❌ Error syncing Unit ${unitNumber} to Supabase:`, error.message || error);
  }
}

async function run() {
    console.log('🚀 Starting sync of Units 8, 9, 10 to Supabase...\n');
    await syncUnit(8, 'public/unit8_ielts.json');
    await syncUnit(9, 'public/unit9_ielts.json');
    await syncUnit(10, 'public/unit10_ielts.json');
    console.log('\n🎉 Sync complete!');
}

run();
