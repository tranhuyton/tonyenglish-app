const fs = require('fs');
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_SERVICE_ROLE_KEY);

async function run() {
    const activities = ['11', '15'];
    const { data } = await supabase.from('tests')
        .select('title, content_json')
        .in('title', activities.map(a => `Unit 4: Listening Activity ${a}`));
    const out = {};
    data.forEach(row => {
        out[row.title] = row.content_json.parts[0].sections.map((s, i) => ({
            type: s.questionType,
            questions: s.questions.map(q => ({id: q.id, content: q.content, options: q.options}))
        }));
    });
    console.log(JSON.stringify(out, null, 2));
}
run();
