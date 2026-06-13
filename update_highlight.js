const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');

function getEnv(key) {
  const content = fs.readFileSync('.env', 'utf-8');
  const match = content.match(new RegExp('^' + key + '=(.*)$', 'm'));
  return match ? match[1].trim() : null;
}

const supabase = createClient(getEnv('VITE_SUPABASE_URL'), getEnv('VITE_SUPABASE_ANON_KEY'));

async function run() {
  const { data } = await supabase.from('tests').select('*').eq('title', 'Chapter 1: Mini Test');
  if (data && data.length > 0) {
    const test = data[0];
    const newContentJson = { ...test.content_json };
    
    // Fix the passage
    let passage = newContentJson.parts[0].content;
    
    passage = passage.replace(/<strong>Such events<\/strong>/g, '<span class="bg-yellow-300 px-1">Such events</span>');
    passage = passage.replace(/<strong>Our Sun is not fated to become a supernova, but it was born out of the debris of supernova explosions of the distant past, when our Milky Way galaxy was young.<\/strong>/g, '<span class="bg-yellow-300 px-1">Our Sun is not fated to become a supernova, but it was born out of the debris of supernova explosions of the distant past, when our Milky Way galaxy was young.</span>');
    passage = passage.replace(/<strong>dubbed<\/strong>/g, '<span class="bg-yellow-300 px-1">dubbed</span>');
    passage = passage.replace(/<strong>those observations<\/strong>/g, '<span class="bg-yellow-300 px-1">those observations</span>');
    
    newContentJson.parts[0].content = passage;

    // Fix the questions
    const questions = newContentJson.parts[0].sections[0].questions;
    
    // Q1
    questions[0].content = "The phrase <span class=\"bg-yellow-300 px-1\">Such events</span> in the passage refers to";
    
    // Q2
    questions[1].content = "Which of the sentences below best expresses the essential information in the highlighted sentence in the passage? <em>Incorrect choices change the meaning in important ways or leave out essential information.</em>";
    
    // Q4
    questions[3].content = "The word <span class=\"bg-yellow-300 px-1\">dubbed</span> in the passage is closest in meaning to";
    
    // Q5
    questions[4].content = "The phrase <span class=\"bg-yellow-300 px-1\">those observations</span> in the passage refers to the observations of";
    
    await supabase.from('tests').update({ content_json: newContentJson }).eq('id', test.id);
    console.log('Fixed Mini Test highlighting');
  }
}

run();
