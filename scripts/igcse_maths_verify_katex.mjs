import fs from 'node:fs';
import path from 'node:path';
import katex from 'katex';

const payloadPath = path.resolve(process.cwd(), 'scratch', 'igcse_katex_payload.json');
if (!fs.existsSync(payloadPath)) {
  console.error('Missing payload file:', payloadPath);
  process.exit(1);
}

const items = JSON.parse(fs.readFileSync(payloadPath, 'utf-8'));
let totalExprs = 0;
const errors = [];

const inlineRe = /\\\(([\s\S]*?)\\\)/g;
const displayRe = /\\\[([\s\S]*?)\\\]/g;

for (const item of items) {
  const { label, text } = item;
  if (!text) continue;
  for (const [re, isDisplay] of [[displayRe, true], [inlineRe, false]]) {
    re.lastIndex = 0;
    let m;
    while ((m = re.exec(text)) !== null) {
      totalExprs++;
      const expr = m[1];
      try {
        katex.renderToString(expr, {
          displayMode: isDisplay,
          throwOnError: true,
          strict: false,
          trust: false,
        });
      } catch (err) {
        errors.push({ label, expr, error: String(err.message || err) });
      }
    }
  }
}

console.log(`KaTeX verified ${totalExprs} expressions across ${items.length} text blocks.`);
if (errors.length > 0) {
  console.error(`FOUND ${errors.length} KATEX ERRORS:`);
  for (const e of errors.slice(0, 30)) {
    console.error(`  [${e.label}] ${e.expr}  ==>  ${e.error}`);
  }
  process.exit(1);
}
console.log('ALL KATEX EXPRESSIONS RENDERED WITH 0 ERRORS!');
