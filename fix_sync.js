require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

const folderId = '33ff218e-f8ba-48b6-8c7e-f68b64f3be1b';
const courseId = '8c3bea0e-458c-4c18-ab60-44b432e71170';

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
                title: data.title,
                content_json: data
            })
            .eq('id', testId);
        if (updateError) throw updateError;
        console.log(`Successfully updated Unit ${unitNumber} in Supabase!`);
    } else {
        const { error: insertError } = await supabase
            .from('tests')
            .insert({
                folder_id: folderId,
                title: data.title,
                test_type: 'SplitScreen (Standard)',
                content_json: data,
                is_published: true,
                course_id: courseId,
                order_index: unitNumber
            });
        if (insertError) throw insertError;
        console.log(`Successfully inserted Unit ${unitNumber} into Supabase!`);
    }
  } catch (error) {
    console.error(`Error syncing Unit ${unitNumber} to Supabase:`, error);
  }
}

async function run() {
    await syncUnit(2, 'public/unit2_ielts.json');
    await syncUnit(3, 'public/unit3_ielts.json');
    await syncUnit(4, 'public/unit4_ielts.json');
}

run();
