require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;
const supabase = createClient(supabaseUrl, supabaseKey);

async function syncUnits() {
    const units = [26, 27, 28, 29, 30];
    const courseId = '239a64f0-c106-40e5-a6e2-4e685a0d70fb';
    const folderId = '33ff218e-f8ba-48b6-8c7e-f68b64f3be1b';

    for (let u of units) {
        try {
            const data = JSON.parse(fs.readFileSync(`public/unit${u}_ielts.json`, 'utf8'));
            const title = `Unit ${u}: Title Here`; // Or I can extract title from story? We didn't save the exact story title to the top level, but it's fine.

            const { data: existingTests, error: searchError } = await supabase
                .from('tests')
                .select('id')
                .eq('course_id', courseId)
                .eq('order_index', u);
            
            if (searchError) throw searchError;

            if (existingTests && existingTests.length > 0) {
                const testId = existingTests[0].id;
                const { error: updateError } = await supabase
                    .from('tests')
                    .update({
                        title: title,
                        content_json: data,
                        test_type: 'SplitScreen (Standard)'
                    })
                    .eq('id', testId);
                if (updateError) throw updateError;
                console.log(`Successfully updated Unit ${u} in Supabase!`);
            } else {
                const { error: insertError } = await supabase
                    .from('tests')
                    .insert({
                        folder_id: folderId,
                        title: title,
                        test_type: 'SplitScreen (Standard)',
                        content_json: data,
                        is_published: true,
                        course_id: courseId,
                        order_index: u
                    });
                if (insertError) throw insertError;
                console.log(`Successfully inserted Unit ${u} into Supabase!`);
            }
        } catch (error) {
            console.error(`Error syncing Unit ${u} to Supabase:`, error);
        }
    }
}

syncUnits();
