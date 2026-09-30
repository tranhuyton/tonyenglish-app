const { createClient } = require('@supabase/supabase-js');
const fs = require('fs');
const path = require('path');
require('dotenv').config({ path: '.env' });

const supabase = createClient(
  process.env.VITE_SUPABASE_URL,
  process.env.VITE_SUPABASE_ANON_KEY
);

async function run() {
  const { data: tests, error } = await supabase
    .from('tests')
    .select('id, title, insert_pdf_url, resource_pdf_url, content_json')
    .ilike('title', '0450%');

  if (error) {
    console.error('Error fetching tests:', error);
    return;
  }

  console.log(`Found ${tests.length} tests to process`);

  for (const test of tests) {
    // Determine folder from title
    // e.g. "0450 June 2024 - Paper 11", "0450 Feb-March 2024 - Paper 12", "0450 Nov 2024 - Paper 21"
    const match = test.title.match(/0450\s+(Feb-March|June|Nov)\s+(\d{4})\s+-\s+Paper\s+(\d+)/i);
    if (!match) {
      console.log(`Skipping non-matching title: ${test.title}`);
      continue;
    }

    const seasonName = match[1];
    const year = match[2];
    const variant = match[3];

    const folderName = `${year} ${seasonName}`;
    const seasonCodeMap = {
      'Feb-March': 'm',
      'June': 's',
      'Nov': 'w'
    };
    const shortYear = year.slice(2);
    const seasonCode = `${seasonCodeMap[seasonName]}${shortYear}`; // e.g. s24, w24, m24, s25, m25

    const qpFileName = `0450_${seasonCode}_qp_${variant}.pdf`;
    const inFileName = `0450_${seasonCode}_in_${variant}.pdf`;

    const qpLocalPath = path.join('public', 'Business Studies', folderName, qpFileName);
    const inLocalPath = path.join('public', 'Business Studies', folderName, inFileName);

    const hasQp = fs.existsSync(qpLocalPath);
    const hasIn = fs.existsSync(inLocalPath);

    console.log(`Processing: ${test.title}`);
    console.log(`  Folder: ${folderName}, Season: ${seasonCode}, Variant: ${variant}`);
    console.log(`  QP: ${qpFileName} (exists: ${hasQp}), IN: ${inFileName} (exists: ${hasIn})`);

    let finalQpUrl = null;
    let finalInUrl = null;

    if (hasQp) {
      finalQpUrl = `/Business%20Studies/${encodeURIComponent(folderName)}/${qpFileName}`;
    }
    if (hasIn) {
      finalInUrl = `/Business%20Studies/${encodeURIComponent(folderName)}/${inFileName}`;
    }

    // If Paper 2 has no QP file locally (fallback), keep IN as insert_pdf_url
    const insert_pdf_url = finalQpUrl || finalInUrl;
    const resource_pdf_url = finalQpUrl && finalInUrl ? finalInUrl : null;

    const currentContentJson = test.content_json || {};
    const updatedContentJson = {
      ...currentContentJson,
      basicInfo: {
        ...(currentContentJson.basicInfo || {}),
        insert_pdf_url: insert_pdf_url,
        resource_pdf_url: resource_pdf_url
      }
    };

    console.log(`  -> insert_pdf_url: ${insert_pdf_url}`);
    console.log(`  -> resource_pdf_url: ${resource_pdf_url}`);

    const { error: updateError } = await supabase
      .from('tests')
      .update({
        insert_pdf_url: insert_pdf_url,
        resource_pdf_url: resource_pdf_url,
        content_json: updatedContentJson
      })
      .eq('id', test.id);

    if (updateError) {
      console.error(`  Error updating test ${test.id}:`, updateError);
    } else {
      console.log(`  Updated successfully.`);
    }
  }

  console.log('Finished updating all tests!');
}

run();
