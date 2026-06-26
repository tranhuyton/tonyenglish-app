require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

async function syncUnit4() {
  try {
    const data = JSON.parse(fs.readFileSync('public/unit4_ielts.json', 'utf8'));

    const { data: existingTests, error: searchError } = await supabase
        .from('tests')
        .select('id')
        .eq('course_id', '8c3bea0e-458c-4c18-ab60-44b432e71170')
        .eq('order_index', 4);
    
    if (searchError) throw searchError;

    if (existingTests && existingTests.length > 0) {
        const testId = existingTests[0].id;
        const { error: updateError } = await supabase
            .from('tests')
            .update({
                title: "Unit 4: Oh, Temptation",
                content_json: data
            })
            .eq('id', testId);
        if (updateError) throw updateError;
        console.log('Successfully updated Unit 4 in Supabase!');
    } else {
        const { error: insertError } = await supabase
            .from('tests')
            .insert({
                folder_id: '33ff218e-f8ba-48b6-8c7e-f68b64f3be1b',
                title: "Unit 4: Oh, Temptation",
                test_type: 'SplitScreen (Standard)',
                content_json: data,
                is_published: true,
                course_id: '8c3bea0e-458c-4c18-ab60-44b432e71170',
                order_index: 4
            });
        if (insertError) throw insertError;
        console.log('Successfully inserted Unit 4 into Supabase!');
    }
  } catch (error) {
    console.error('Error syncing to Supabase:', error);
  }
}

syncUnit4();
