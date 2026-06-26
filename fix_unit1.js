const fs = require('fs');
const u1 = JSON.parse(fs.readFileSync('public/unit1_ielts.json'));
u1.basicInfo = {
    skill: 'MCQ (Standard)',
    title: "Unit 1: What's Your Learning Mode?",
    category: 'exercise',
    courseId: '239a64f0-c106-40e5-a6e2-4e685a0d70fb',
    timeLimit: 40
};
fs.writeFileSync('public/unit1_ielts.json', JSON.stringify(u1, null, 2));

const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();
const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_SERVICE_ROLE_KEY);
async function run() {
    await supabase.from('tests').update({ content_json: u1 }).eq('id', '11ba7152-ea5c-415f-934e-33403ada0e46');
    console.log('Fixed Unit 1 content_json');
}
run();
