require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

const folderId = '33ff218e-f8ba-48b6-8c7e-f68b64f3be1b';

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
                content_json: data,
                test_type: 'MCQ (Standard)',
                is_published: true
            })
            .eq('id', testId);
        if (updateError) throw updateError;
        console.log(`✅ Updated Unit ${unitNumber} (id: ${testId}) in Supabase!`);
    } else {
        const { data: insertedData, error: insertError } = await supabase
            .from('tests')
            .insert({
                folder_id: folderId,
                title: data.basicInfo.title,
                test_type: 'MCQ (Standard)',
                content_json: data,
                is_published: true,
                order_index: unitNumber
            })
            .select('id');
        if (insertError) throw insertError;
        console.log(`✅ Inserted Unit ${unitNumber} (id: ${insertedData?.[0]?.id}) into Supabase!`);
    }
  } catch (error) {
    console.error(`❌ Error syncing Unit ${unitNumber}:`, error.message || error);
  }
}

async function run() {
    console.log('Syncing Units 5, 6, 7 to Supabase...\n');
    await syncUnit(5, 'public/unit5_ielts.json');
    await syncUnit(6, 'public/unit6_ielts.json');
    await syncUnit(7, 'public/unit7_ielts.json');
    console.log('\nDone!');
}

run();
