/**
 * Extract ONLY diagram illustrations v4
 * 
 * Approach: Use text positions from pdf-parse to find the largest vertical
 * gap between text items within each question. That gap IS the diagram area.
 * Include text labels that border the gap (diagram annotations).
 */

const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const pdfParse = require('pdf-parse');
require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');

const supabase = createClient(process.env.VITE_SUPABASE_URL, process.env.VITE_SUPABASE_ANON_KEY);
const courseId = 'a68bae8c-a21c-4cb2-8cd7-6097de211060';
const BUCKET = 'test_assets';
const imgDir = path.join('public', 'Biology 0610', 'images');
if (!fs.existsSync(imgDir)) fs.mkdirSync(imgDir, { recursive: true });

async function pdfToPages(pdfPath) {
  const { pdf } = await import('pdf-to-img');
  const pages = [];
  let pageNum = 0;
  for await (const buf of await pdf(pdfPath, { scale: 3 })) { pages.push({ pageNum: ++pageNum, buffer: buf }); }
  return pages;
}

async function getPageData(pdfPath) {
  const buffer = fs.readFileSync(pdfPath);
  const pageData = {};
  await pdfParse(buffer, {
    pagerender: (pd) => pd.getTextContent().then(tc => {
      const pn = pd.pageIndex + 1;
      pageData[pn] = tc.items
        .filter(i => i.str.trim().length > 0)
        .map(i => ({ text: i.str.trim(), x: Math.round(i.transform[4]), y: Math.round(i.transform[5]) }));
      return '';
    })
  });
  return pageData;
}

function findQuestionPositions(pageData) {
  const positions = {};
  for (const [pn, items] of Object.entries(pageData)) {
    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      const m = item.text.match(/^(\d{1,2})$/);
      if (m && item.x < 80) {
        const num = parseInt(m[1]);
        if (num >= 1 && num <= 40 && items[i+1] && items[i+1].text.length > 3) {
          positions[num] = { pageNum: parseInt(pn), y: item.y };
        }
      }
    }
  }
  return positions;
}

/**
 * For a given question, find the diagram region by locating the space 
 * between the intro text and follow-up text/options.
 */
function findDiagramByTextGap(qNum, positions, pageData) {
  const qPos = positions[qNum];
  if (!qPos) return null;
  const { pageNum, y: qY } = qPos;
  const items = pageData[pageNum];
  if (!items) return null;

  // Find next question Y on same page
  let nextQY = null;
  for (let nq = qNum + 1; nq <= 40; nq++) {
    if (positions[nq] && positions[nq].pageNum === pageNum) {
      nextQY = positions[nq].y;
      break;
    }
  }
  
  if (nextQY === null) {
    nextQY = 30; // default bottom of page (above footer)
    const copyrightItem = items.find(i => i.text.includes('Permission to reproduce'));
    if (copyrightItem) {
      nextQY = copyrightItem.y;
    }
  }

  // Get items within this question's range
  const qItems = items.filter(i => i.y <= qY + 5 && i.y >= nextQY);
  if (qItems.length < 4) return null;

  // Sort by y descending (visually top to bottom)
  const sorted = [...qItems].sort((a, b) => b.y - a.y);

  // Find where the actual options (A,B,C,D) start so we don't confuse diagram labels below them
  const allOptions = sorted.filter(i => ['A','B','C','D'].includes(i.text.trim()) && (i.x <= 75 || i.x > 150));
  const firstOptionY = allOptions.length > 0 ? allOptions[0].y : 0;

  // Identify "Main Text": x <= 75, not an isolated A, B, C, D option, and must be ABOVE the first option
  const mainTextItems = sorted.filter(i => {
    if (i.x > 75) return false;
    if (i.y <= firstOptionY + 5) return false; // Ignore text that is at or below the options zone
    const text = i.text.trim();
    if (['A','B','C','D'].includes(text)) return false; // Options
    if (text.length <= 2) return false;      // Ignore random numbers/letters
    return true;
  });

  if (mainTextItems.length === 0) return null;

  // The intro block is the contiguous block of main text at the top
  let introLastIdx = 0;
  for (let i = 0; i < mainTextItems.length - 1; i++) {
    const gap = mainTextItems[i].y - mainTextItems[i + 1].y;
    if (gap > 35) { // Paragraph break or diagram space
      break;
    }
    introLastIdx = i + 1;
  }

  const introLastItem = mainTextItems[introLastIdx];
  const diagramTopY = introLastItem.y - 8; // Start crop further below intro text baseline to avoid descenders (g, p, y)

  let diagramBottomY = nextQY + 25; // Default bottom is above next question

  // Check if there is follow-up main text
  if (introLastIdx < mainTextItems.length - 1) {
    const followUpItem = mainTextItems[introLastIdx + 1];
    diagramBottomY = followUpItem.y + 18; // End crop just above follow-up text
  } else {
    // If no follow-up main text, look for options (A, B, C, D)
    // We strictly check for typical left-aligned options (x <= 75).
    // If options are shifted right, they are likely labels inside a diagram or side-by-side graphs.
    const options = sorted.filter(i => ['A','B','C','D'].includes(i.text.trim()) && i.x <= 75);
    if (options.length > 0) {
      // Find the highest Y option
      const firstOption = options[0]; 
      diagramBottomY = firstOption.y + 18;
    }
  }

  const gapBeforeFailsafe = diagramTopY - diagramBottomY;
  if (gapBeforeFailsafe < 30) {
    // Boundary text was too close or embedded in the diagram (e.g. A,B,C,D arrows inside the image).
    // Fallback to cropping all the way down to the next question.
    diagramBottomY = nextQY + 25;
  }

  const gap = diagramTopY - diagramBottomY;
  if (gap < 30) return null; // Not a significant gap, probably no diagram

  return {
    pageNum,
    topY: diagramTopY,
    bottomY: diagramBottomY,
    gap
  };
}

async function processPaper(paperInfo) {
  const { title, qpPath, prefix } = paperInfo;
  console.log(`\n📄 ${title}`);

  const { data: tests } = await supabase.from('tests').select('id, content_json')
    .eq('course_id', courseId).eq('title', title);
  if (!tests?.length) { console.error('  ❌ Not found'); return; }

  const test = tests[0];
  const questions = test.content_json.parts[0].sections[0].questions;
  const qWithImages = questions.filter(q => (q.content||'').includes('biology-0610')).map(q => parseInt(q.id));
  console.log(`  Images: [${qWithImages.join(',')}] (${qWithImages.length})`);
  if (!qWithImages.length) return;

  const fullPath = path.join(process.cwd(), qpPath);
  console.log('  Converting PDF...');
  const pages = await pdfToPages(fullPath);
  console.log('  Analyzing text...');
  const pageData = await getPageData(fullPath);
  const positions = findQuestionPositions(pageData);

  let updated = 0;
  for (const qNum of qWithImages) {
    const diagram = findDiagramByTextGap(qNum, positions, pageData);
    if (!diagram) { console.log(`  ⚠️ Q${qNum}: no text gap found`); continue; }

    const page = pages.find(p => p.pageNum === diagram.pageNum);
    if (!page) continue;

    const meta = await sharp(page.buffer).metadata();

    // Standard A4 PDF height is ~842 points
    const pdfHeight = 842;
    const scaleY = meta.height / pdfHeight;

    // Convert PDF y (bottom-up) to image y (top-down)
    const imgTop = Math.max(0, Math.round((pdfHeight - diagram.topY) * scaleY));
    const imgBottom = Math.min(meta.height, Math.round((pdfHeight - diagram.bottomY) * scaleY));
    const height = imgBottom - imgTop;

    if (height < 40) { console.log(`  ⚠️ Q${qNum}: too small (${height}px, gap=${diagram.gap}pt)`); continue; }

    const imgFilename = `${prefix}_q${qNum}.png`;
    const localPath = path.join(imgDir, imgFilename);

    try {
      await sharp(page.buffer)
        .extract({ left: 0, top: imgTop, width: meta.width, height })
        .trim()
        .png()
        .toFile(localPath);
    } catch (e) {
      console.log(`  ⚠️ Q${qNum}: trim failed, falling back to untrimmed`);
      await sharp(page.buffer)
        .extract({ left: 0, top: imgTop, width: meta.width, height })
        .png()
        .toFile(localPath);
    }

    // Upload
    const uploadBuf = fs.readFileSync(localPath);
    const { error } = await supabase.storage.from(BUCKET)
      .upload(`biology-0610/${imgFilename}`, uploadBuf, { contentType: 'image/png', upsert: true });

    if (error) { console.log(`  ⚠️ Q${qNum}: upload error`); }
    else { updated++; console.log(`  ✅ Q${qNum}: ${height}px (gap=${diagram.gap}pt)`); }
  }

  console.log(`  📤 ${updated}/${qWithImages.length} updated`);
}

async function main() {
  console.log('🔬 Biology 0610 - Diagram Extraction v4 (text gap)\n');
  const papers = [
    { title: '0610 Feb-March 2025 - Paper 22 (Multiple Choice)', qpPath: 'public/Biology 0610/2025 Feb-March/0610_m25_qp_22.pdf', prefix: 'm25_p22' },
    { title: '0610 June 2025 - Paper 21 (Multiple Choice)', qpPath: 'public/Biology 0610/2025 June/0610_s25_qp_21.pdf', prefix: 's25_p21' },
    { title: '0610 June 2025 - Paper 22 (Multiple Choice)', qpPath: 'public/Biology 0610/2025 June/0610_s25_qp_22.pdf', prefix: 's25_p22' },
    { title: '0610 June 2025 - Paper 23 (Multiple Choice)', qpPath: 'public/Biology 0610/2025 June/0610_s25_qp_23.pdf', prefix: 's25_p23' }
  ];
  for (const p of papers) await processPaper(p);
  console.log('\n🎉 Done!');
}

main().catch(e => { console.error('Fatal:', e); process.exit(1); });
