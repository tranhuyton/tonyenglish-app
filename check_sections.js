const { createClient } = require('@supabase/supabase-js');
const supabaseUrl = 'https://ubkvzgwespfvrlpjuxkp.supabase.co';
const supabaseKey = 'sb_secret_5huRcnLVzDU92RUpJ6H6mw_zOGBmCNw';
const supabase = createClient(supabaseUrl, supabaseKey);

async function fetchSections() {
  const { data, error } = await supabase
    .from('tests')
    .select('*')
    .ilike('title', '%Unit 13: Volume 4%')
    .limit(1);

  if (data && data.length > 0) {
    const content = data[0].content;
    console.log(content.sections.map(s => ({
      type: s.type,
      title: s.title,
      numQuestions: s.questions ? s.questions.length : (s.parts ? s.parts.length : 0)
    })));
  }
}

fetchSections();
