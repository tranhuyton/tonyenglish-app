require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

const supabaseUrl = process.env.VITE_SUPABASE_URL;
const supabaseKey = process.env.VITE_SUPABASE_SERVICE_ROLE_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.error("Missing Supabase credentials in .env file");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseKey);

async function syncUnit2() {
  try {
    const unit2Data = JSON.parse(fs.readFileSync('public/unit2_ielts.json', 'utf8'));

    const { error } = await supabase
      .from('course_units')
      .upsert({
        id: unit2Data.id,
        course_id: 'expand_vocabulary',
        title: unit2Data.title,
        data: unit2Data,
        order_index: 2
      });

    if (error) throw error;

    console.log('Successfully synced Unit 2 to Supabase!');

  } catch (error) {
    console.error('Error syncing to Supabase:', error);
  }
}

syncUnit2();
