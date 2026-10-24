// Pure TypeScript MD5 implementation for legacy Yii 1.1 password hashing: md5(salt + md5(pass))
export function md5(inputString: string): string {
  const hc = '0123456789abcdef';
  function rh(n: number) {
    let j, s = '';
    for (j = 0; j <= 3; j++) s += hc.charAt((n >> (j * 8 + 4)) & 0x0f) + hc.charAt((n >> (j * 8)) & 0x0f);
    return s;
  }
  function ad(x: number, y: number) {
    const l = (x & 0xffff) + (y & 0xffff);
    const m = (x >> 16) + (y >> 16) + (l >> 16);
    return (m << 16) | (l & 0xffff);
  }
  function rl(n: number, c: number) { return (n << c) | (n >>> (32 - c)); }
  function cm(q: number, a: number, b: number, x: number, s: number, t: number) {
    return ad(rl(ad(ad(a, q), ad(x, t)), s), b);
  }
  function ff(a: number, b: number, c: number, d: number, x: number, s: number, t: number) {
    return cm((b & c) | (~b & d), a, b, x, s, t);
  }
  function gg(a: number, b: number, c: number, d: number, x: number, s: number, t: number) {
    return cm((b & d) | (c & ~d), a, b, x, s, t);
  }
  function hh(a: number, b: number, c: number, d: number, x: number, s: number, t: number) {
    return cm(b ^ c ^ d, a, b, x, s, t);
  }
  function ii(a: number, b: number, c: number, d: number, x: number, s: number, t: number) {
    return cm(c ^ (b | ~d), a, b, x, s, t);
  }
  function sb(x: string) {
    // UTF-8 encode
    const utf8 = unescape(encodeURIComponent(x));
    let i;
    const nblk = ((utf8.length + 8) >> 6) + 1;
    const blks = new Array(nblk * 16).fill(0);
    for (i = 0; i < utf8.length; i++) {
      blks[i >> 2] |= utf8.charCodeAt(i) << ((i % 4) * 8);
    }
    blks[i >> 2] |= 0x80 << ((i % 4) * 8);
    blks[nblk * 16 - 2] = utf8.length * 8;
    return blks;
  }
  const x = sb(inputString);
  let a = 1732584193, b = -271733879, c = -1732584194, d = 271733878;
  for (let i = 0; i < x.length; i += 16) {
    const olda = a, oldb = b, oldc = c, oldd = d;
    a = ff(a, b, c, d, x[i + 0], 7, -680876936);
    d = ff(d, a, b, c, x[i + 1], 12, -389564586);
    c = ff(c, d, a, b, x[i + 2], 17, 606105819);
    b = ff(b, c, d, a, x[i + 3], 22, -1044525330);
    a = ff(a, b, c, d, x[i + 4], 7, -176418897);
    d = ff(d, a, b, c, x[i + 5], 12, 1200080426);
    c = ff(c, d, a, b, x[i + 6], 17, -1473231341);
    b = ff(b, c, d, a, x[i + 7], 22, -45705983);
    a = ff(a, b, c, d, x[i + 8], 7, 1770035416);
    d = ff(d, a, b, c, x[i + 9], 12, -1958414417);
    c = ff(c, d, a, b, x[i + 10], 17, -42063);
    b = ff(b, c, d, a, x[i + 11], 22, -1990404162);
    a = ff(a, b, c, d, x[i + 12], 7, 1804603682);
    d = ff(d, a, b, c, x[i + 13], 12, -40341101);
    c = ff(c, d, a, b, x[i + 14], 17, -1502002290);
    b = ff(b, c, d, a, x[i + 15], 22, 1236535329);
    a = gg(a, b, c, d, x[i + 1], 5, -165796510);
    d = gg(d, a, b, c, x[i + 6], 9, -1069501632);
    c = gg(c, d, a, b, x[i + 11], 14, 643717713);
    b = gg(b, c, d, a, x[i + 0], 20, -373897302);
    a = gg(a, b, c, d, x[i + 5], 5, -701558691);
    d = gg(d, a, b, c, x[i + 10], 9, 38016083);
    c = gg(c, d, a, b, x[i + 15], 14, -660478335);
    b = gg(b, c, d, a, x[i + 4], 20, -405537848);
    a = gg(a, b, c, d, x[i + 9], 5, 568446438);
    d = gg(d, a, b, c, x[i + 14], 9, -1019803690);
    c = gg(c, d, a, b, x[i + 3], 14, -187363961);
    b = gg(b, c, d, a, x[i + 8], 20, 1163531501);
    a = gg(a, b, c, d, x[i + 13], 5, -1444681467);
    d = gg(d, a, b, c, x[i + 2], 9, -51403784);
    c = gg(c, d, a, b, x[i + 7], 14, 1735328473);
    b = gg(b, c, d, a, x[i + 12], 20, -1926607734);
    a = hh(a, b, c, d, x[i + 5], 4, -378558);
    d = hh(d, a, b, c, x[i + 8], 11, -2022574463);
    c = hh(c, d, a, b, x[i + 11], 16, 1839030562);
    b = hh(b, c, d, a, x[i + 14], 23, -35309556);
    a = hh(a, b, c, d, x[i + 1], 4, -1530992060);
    d = hh(d, a, b, c, x[i + 4], 11, 1272893353);
    c = hh(c, d, a, b, x[i + 7], 16, -155497632);
    b = hh(b, c, d, a, x[i + 10], 23, -1094730640);
    a = hh(a, b, c, d, x[i + 13], 4, 681279174);
    d = hh(d, a, b, c, x[i + 0], 11, -358537222);
    c = hh(c, d, a, b, x[i + 3], 16, -722521979);
    b = hh(b, c, d, a, x[i + 6], 23, 76029189);
    a = hh(a, b, c, d, x[i + 9], 4, -640364487);
    d = hh(d, a, b, c, x[i + 12], 11, -421815835);
    c = hh(c, d, a, b, x[i + 15], 16, 530742520);
    b = hh(b, c, d, a, x[i + 2], 23, -995338651);
    a = ii(a, b, c, d, x[i + 0], 6, -198630844);
    d = ii(d, a, b, c, x[i + 7], 10, 1126891415);
    c = ii(c, d, a, b, x[i + 14], 15, -1416354905);
    b = ii(b, c, d, a, x[i + 5], 21, -57434055);
    a = ii(a, b, c, d, x[i + 12], 6, 1700485571);
    d = ii(d, a, b, c, x[i + 3], 10, -1894986606);
    c = ii(c, d, a, b, x[i + 10], 15, -1051523);
    b = ii(b, c, d, a, x[i + 1], 21, -2054922799);
    a = ii(a, b, c, d, x[i + 8], 6, 1873313359);
    d = ii(d, a, b, c, x[i + 15], 10, -30611744);
    c = ii(c, d, a, b, x[i + 6], 15, -1560198380);
    b = ii(b, c, d, a, x[i + 13], 21, 1309151649);
    a = ii(a, b, c, d, x[i + 4], 6, -145523070);
    d = ii(d, a, b, c, x[i + 11], 10, -1120210379);
    c = ii(c, d, a, b, x[i + 2], 15, 718787259);
    b = ii(b, c, d, a, x[i + 9], 21, -343485551);
    a = ad(a, olda); b = ad(b, oldb); c = ad(c, oldc); d = ad(d, oldd);
  }
  return rh(a) + rh(b) + rh(c) + rh(d);
}

export function encryptLegacyPass(salt: string, passIn: string): string {
  return md5((salt || '') + md5(passIn));
}

// Parse PHP serialized arrays of IDs/strings like a:3:{i:0;s:2:"15";i:1;i:22;...}
export function unserializePhpIds(serialized: string | null | undefined): number[] {
  if (!serialized) return [];
  const ids: number[] = [];
  // Match s:len:"val"; or i:val; after a key
  const regex = /(?:i:\d+;|s:\d+:"[^"]+";)\s*(?:s:\d+:"(\d+)";|i:(\d+);)/g;
  let m;
  while ((m = regex.exec(serialized)) !== null) {
    const num = parseInt(m[1] || m[2], 10);
    if (!isNaN(num)) ids.push(num);
  }
  return ids;
}

// Parse PHP serialized array of objects like a:1:{i:1;a:2:{s:4:"name";s:8:"Quiz 1";s:4:"path";s:12:"FlashQuiz/..";}}
export function unserializePhpQuizList(serialized: string | null | undefined): Array<{ name: string; path: string }> {
  if (!serialized) return [];
  const result: Array<{ name: string; path: string }> = [];
  const itemRegex = /s:4:"name";s:\d+:"([^"]*)";s:4:"path";s:\d+:"([^"]*)";/g;
  let m;
  while ((m = itemRegex.exec(serialized)) !== null) {
    result.push({ name: m[1], path: m[2] });
  }
  return result;
}

export function getYoutubeEmbedUrl(url: string | null | undefined): string {
  if (!url) return '';
  const regExp = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
  const match = url.match(regExp);
  if (match && match[2].length === 11) {
    const listMatch = url.match(/[?&]list=([a-zA-Z0-9_-]+)/);
    if (listMatch && listMatch[1]) {
      return `https://www.youtube.com/embed/${match[2]}?list=${listMatch[1]}`;
    }
    return `https://www.youtube.com/embed/${match[2]}`;
  }
  return url;
}

export function decodeHtmlEntities(text: string): string {
  if (!text) return '';
  return text
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&quot;/gi, '"')
    .replace(/&#0*39;|&apos;|&rsquo;|&lsquo;/gi, "'")
    .replace(/&ldquo;|&rdquo;/gi, '"')
    .replace(/&ndash;/gi, '–')
    .replace(/&mdash;/gi, '—')
    .replace(/&hellip;/gi, '...');
}

export function fixLegacyWordSpacing(html: string | null | undefined): string {
  if (!html) return '';
  return html
    // 1. Fix known mid-word split formatting tags from legacy CKEditor
    .replace(/De<\/strong><strong>bbie/g, 'Debbie')
    .replace(/Richa<\/strong><strong>rd/g, 'Richard')
    .replace(/Da<\/strong><strong>vid/g, 'David')
    .replace(/we<\/strong><strong>llness/g, 'wellness')
    .replace(/ec<\/strong><strong>osystem/g, 'ecosystem')
    .replace(/gre<\/strong><strong>at/g, 'great')
    .replace(/\bh<em>ighly<\/em>/g, '<em>highly</em>')
    .replace(/\bo<\/strong>f\b/g, 'of</strong>')
    .replace(/\bDa<\/strong>y\b/g, 'Day</strong>')
    .replace(/\bdomesticate<\/strong>d\b/g, 'domesticated</strong>')
    .replace(/\bawa<\/strong>y\b/g, 'away</strong>')
    .replace(/\bfootprin<\/em>t\b/g, 'footprint</em>')
    .replace(/\bthoughtfu<\/strong>l\b/g, 'thoughtful</strong>')
    .replace(/\bcalorie<\/em>s\b/g, 'calories</em>')
    // 2. Add space between adjacent closing and opening inline tags
    .replace(/([a-zA-Z0-9.,;!?])(<\/(?:strong|b|em|i)>)(<(?:strong|b|em|i)\b[^>]*>)(?=[a-zA-Z0-9])/g, '$1$2 $3')
    // 3. Add space before opening inline tag when preceded by a word/letter
    .replace(/([a-zA-Z0-9])((?:<(?:strong|b|em|i)\b[^>]*>)+)(?=[a-zA-Z0-9])/g, '$1 $2')
    // 4. Add space after closing inline tag when followed by a word
    .replace(/([a-zA-Z0-9.,;!?])((?:<\/(?:strong|b|em|i)>)+)(?=[a-zA-Z0-9]{2,}|[aAI]\b)/g, '$1$2 ')
    // 5. Add space after period/comma/semicolon/exclamation/question when followed by Capitalized word
    .replace(/([a-z]{2,})([.,;!?])(?=[A-Z][a-z]+|[AI]\b)/g, '$1$2 ');
}

export function stripTags(html: string | null | undefined): string {
  if (!html) return '';
  return decodeHtmlEntities(
    fixLegacyWordSpacing(html)
      // Turn block boundaries & line breaks into spaces so sentences don't stick together (e.g. believe.</p><p>A -> believe. A)
      .replace(/<\/?(?:p|div|br|li|ul|ol|tr|td|th|h[1-6]|dt|dd|blockquote|hr)\b[^>]*>/gi, ' ')
      .replace(/<[^>]*>?/gm, '')
  )
    .replace(/\s+/g, ' ')
    .trim();
}

export interface ArticleVocabItem {
  term: string;
  definition: string;
}

export interface CambridgeParagraph {
  label: string;
  enParagraph: string;
  viParagraph: string;
  pairs: Array<{ en: string; vi: string }>;
}

export interface CambridgeBilingualData {
  titleVi: string;
  paragraphs: CambridgeParagraph[];
}

export function parseCambridgeBilingual(html: string | null | undefined): CambridgeBilingualData | null {
  if (!html || !html.includes('cambridge-bilingual')) return null;

  const titleMatch = html.match(/data-title-vi="([^"]*)"/i);
  const titleVi = titleMatch ? decodeHtmlEntities(titleMatch[1]).trim() : '';

  const paragraphs: CambridgeParagraph[] = [];
  const paraRegex = /<div\s+class="cam-para"\s+data-label="([^"]*)"\s*>([\s\S]*?)<\/div>\s*<!--\s*\/cam-para\s*-->/gi;
  let pm: RegExpExecArray | null;

  while ((pm = paraRegex.exec(html)) !== null) {
    const label = decodeHtmlEntities(pm[1]).trim();
    const block = pm[2];
    const enMatch = block.match(/<p\s+class="cam-para-en">([\s\S]*?)<\/p>/i);
    const viMatch = block.match(/<p\s+class="cam-para-vi">([\s\S]*?)<\/p>/i);
    const stripPreserveLines = (s: string) =>
      s
        .replace(/<br\s*\/?>/gi, '\n')
        .split('\n')
        .map((line) => stripTags(line))
        .filter(Boolean)
        .join('\n');
    const enParagraph = enMatch ? stripPreserveLines(enMatch[1]) : '';
    const viParagraph = viMatch ? stripPreserveLines(viMatch[1]) : '';

    const pairs: Array<{ en: string; vi: string }> = [];
    const pairRegex = /<div\s+class="cam-pair">\s*<span\s+class="cam-s-en">([\s\S]*?)<\/span>\s*<span\s+class="cam-s-vi">([\s\S]*?)<\/span>\s*<\/div>/gi;
    let sm: RegExpExecArray | null;
    while ((sm = pairRegex.exec(block)) !== null) {
      const en = stripTags(sm[1]);
      const vi = stripTags(sm[2]);
      if (en || vi) pairs.push({ en, vi });
    }

    if (enParagraph || viParagraph || pairs.length > 0) {
      paragraphs.push({
        label,
        enParagraph,
        viParagraph,
        pairs,
      });
    }
  }

  if (paragraphs.length === 0) return null;
  return { titleVi, paragraphs };
}

export function extractArticleVocabulary(rawHtml: string | null | undefined): {
  bodyHtml: string;
  vocabItems: ArticleVocabItem[];
} {
  if (!rawHtml) return { bodyHtml: '', vocabItems: [] };

  // Match BBC Learning English definition module or standalone Vocabulary heading at the bottom of the article
  const splitRegex =
    /(?:<div[^>]*class="[^"]*module[^"]*"[^>]*>\s*)?(?:<div[^>]*class="[^"]*li-definition|<div[^>]*id="definition\d*"|<h[1-6][^>]*>(?:<[^>]+>|\s|&nbsp;)*Vocabulary(?:\s|&nbsp;|<br\s*\/?>|<\/strong>|<\/b>)*<\/h[1-6]>)/i;
  const match = rawHtml.match(splitRegex);
  if (!match || match.index === undefined) {
    return { bodyHtml: rawHtml, vocabItems: [] };
  }

  const bodyHtml = rawHtml
    .slice(0, match.index)
    .replace(/(?:<p[^>]*>(?:\s|&nbsp;|<br\s*\/?>)*<\/p>\s*)+$/gi, '')
    .trim();
  const vocabRaw = rawHtml.slice(match.index);
  const vocabItems: ArticleVocabItem[] = [];

  // Format 1: BBC <dl><dt>term</dt><dd>definition</dd></dl>
  const dtDdRegex = /<dt[^>]*>([\s\S]*?)<\/dt>\s*<dd[^>]*>([\s\S]*?)<\/dd>/gi;
  let m: RegExpExecArray | null;
  while ((m = dtDdRegex.exec(vocabRaw)) !== null) {
    const term = stripTags(m[1]);
    const definition = stripTags(m[2]);
    if (term && definition) {
      vocabItems.push({ term, definition });
    }
  }

  // Format 2: <p><strong>term</strong><br/>definition</p> or <div class="storytext"><strong>term</strong><br/>definition...</div>
  if (vocabItems.length === 0) {
    const cleanVocabRaw = vocabRaw
      .replace(/<h[1-6][^>]*>[\s\S]*?<\/h[1-6]>/gi, '')
      .replace(/<p[^>]*class="toggle-controls"[^>]*>[\s\S]*?<\/p>/gi, '');

    const blockRegex = /<(?:p|div)[^>]*>([\s\S]*?)<\/(?:p|div)>/gi;
    let bm: RegExpExecArray | null;
    while ((bm = blockRegex.exec(cleanVocabRaw)) !== null) {
      const inner = bm[1].trim();
      if (!inner) continue;
      // Split by <br><br> in case multiple vocab items live inside a single <div class="storytext">
      const subBlocks = inner.split(/<br\s*\/?>\s*<br\s*\/?>/i);
      for (const sb of subBlocks) {
        const strongMatch = sb.match(
          /^\s*<(?:strong|b)\b[^>]*>([\s\S]*?)<\/(?:strong|b)>\s*(?:<br\s*\/?>|:|-|–)?\s*([\s\S]*)$/i
        );
        if (strongMatch) {
          const term = stripTags(strongMatch[1]);
          const definition = stripTags(strongMatch[2]);
          if (term && definition && !/^vocabulary$/i.test(term)) {
            vocabItems.push({ term, definition });
          }
        }
      }
    }
  }

  if (vocabItems.length === 0) {
    return { bodyHtml: rawHtml, vocabItems: [] };
  }

  return { bodyHtml, vocabItems };
}

export function truncateWords(html: string | null | undefined, maxChars = 150): string {
  const clean = stripTags(html);
  if (clean.length <= maxChars) return clean;
  return clean.slice(0, maxChars).replace(/\s+\S*$/, '') + ' ...';
}

export function resolveUploadUrl(path: string | null | undefined, fallback = '/uploads/No_Image_Wide.svg_1.png'): string {
  if (!path || path.trim() === '') return fallback;
  const clean = path
    .trim()
    .replace(/^https?:\/\/(?:www\.)?tonyenglish\.vn\/uploads\//i, '/uploads/')
    .replace(/^https?:\/\/(?:www\.)?tonyenglish\.vn\/themes\/tony\/assets\//i, '/themes/tony/assets/');
  if (clean.startsWith('http://') || clean.startsWith('https://')) return clean;
  if (clean.startsWith('/uploads/') || clean.startsWith('/themes/')) return clean;
  if (clean.startsWith('uploads/')) return '/' + clean;
  return `/uploads/${clean.replace(/^\/+/, '')}`;
}

export function fixLegacyHtmlContent(html: string | null | undefined): string {
  if (!html) return '';
  return fixLegacyWordSpacing(html)
    .replace(/https?:\/\/(?:www\.)?tonyenglish\.vn\/uploads\//gi, '/uploads/')
    .replace(/https?:\/\/(?:www\.)?tonyenglish\.vn\/themes\/tony\/assets\//gi, '/themes/tony/assets/')
    // Remove legacy hardcoded font-family and line-height so content uses unified Inter font & readable spacing
    .replace(/font-family\s*:[^;"]+;?/gi, '')
    .replace(/line-height\s*:[^;"]+;?/gi, '')
    // Remove legacy small/medium inline font-size (e.g. 9pt, 10pt, 11pt, 12px, 13px, 14px, small) so .legacy-prose (17px) takes effect
    .replace(/font-size\s*:\s*([^;"]+)\s*;?/gi, (match, val) => {
      const v = String(val).trim().toLowerCase();
      if (['xx-small', 'x-small', 'small', 'medium', 'smaller', 'inherit', 'initial'].includes(v)) {
        return '';
      }
      const pxMatch = v.match(/^(\d+(?:\.\d+)?)px$/);
      if (pxMatch && parseFloat(pxMatch[1]) < 18) {
        return '';
      }
      const ptMatch = v.match(/^(\d+(?:\.\d+)?)pt$/);
      if (ptMatch && parseFloat(ptMatch[1]) <= 14) {
        return '';
      }
      const emMatch = v.match(/^(\d+(?:\.\d+)?)(?:em|rem)$/);
      if (emMatch && parseFloat(emMatch[1]) <= 1.1) {
        return '';
      }
      const pctMatch = v.match(/^(\d+(?:\.\d+)?)%$/);
      if (pctMatch && parseFloat(pctMatch[1]) <= 110) {
        return '';
      }
      return match;
    })
    // Clean legacy <font face="..." size="..."> attributes
    .replace(/<font\b([^>]*)>/gi, (_m, attrs) => {
      const cleaned = String(attrs)
        .replace(/\bface\s*=\s*["'][^"']*["']/gi, '')
        .replace(/\bsize\s*=\s*["']?[1-4]["']?/gi, '');
      return `<font${cleaned}>`;
    });
}

export interface ReadingQuizOption {
  label: string;
  text: string;
}

export interface ReadingQuizQuestion {
  id: number;
  question: string;
  options: ReadingQuizOption[];
  correctAnswer: string;
  explanation?: string;
}

export function parseArticleInteractiveQuiz(article: any): ReadingQuizQuestion[] {
  if (!article) return [];

  // 1. Check structured JSON in news_quiz
  if (typeof article.news_quiz === 'string' && article.news_quiz.trim().startsWith('[')) {
    try {
      const parsed = JSON.parse(article.news_quiz.trim());
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed.map((q: any, idx: number) => ({
          id: Number(q.id) || idx + 1,
          question: String(q.question || '').trim(),
          options: Array.isArray(q.options)
            ? q.options.map((opt: any, oIdx: number) =>
                typeof opt === 'string'
                  ? { label: String.fromCharCode(65 + oIdx), text: opt }
                  : {
                      label: String(opt.label || String.fromCharCode(65 + oIdx)).toUpperCase(),
                      text: String(opt.text || '').trim(),
                    }
              )
            : [],
          correctAnswer: String(q.correctAnswer || 'A').trim().toUpperCase(),
          explanation: q.explanation ? String(q.explanation).trim() : undefined,
        }));
      }
    } catch {
      // fall through to legacy parser
    }
  }

  // 2. Fallback: parse legacy HTML <input type="radio"> questions in news_question + news_answer
  const rawQ = String(article.news_question || '').trim();
  const rawA = String(article.news_answer || '').trim();
  if (!rawQ || !/<input\b[^>]*type=["']?radio["']?/i.test(rawQ)) {
    return [];
  }

  const answerMap: Record<number, string> = {};
  const ansPlain = stripTags(rawA);
  const ansRegex = /(\d+)\s*[.:)]\s*([a-dA-D])\b/g;
  let am: RegExpExecArray | null;
  while ((am = ansRegex.exec(ansPlain)) !== null) {
    answerMap[parseInt(am[1], 10)] = am[2].toUpperCase();
  }

  const questions: ReadingQuizQuestion[] = [];
  const liRegex = /<li\b[^>]*>([\s\S]*?)<\/li>/gi;
  let lm: RegExpExecArray | null;
  let qIdx = 0;
  while ((lm = liRegex.exec(rawQ)) !== null) {
    qIdx++;
    const block = lm[1];
    const firstOptIdx = block.search(/(?:<p[^>]*>\s*(?:<span[^>]*>\s*)?)?[a-dA-D]\s*\.\s*<input\b/i);
    if (firstOptIdx === -1) continue;
    const stem = stripTags(block.slice(0, firstOptIdx));
    const optsPart = block.slice(firstOptIdx);
    const optRegex = /([a-dA-D])\s*\.\s*<input\b[^>]*>\s*([\s\S]*?)(?=(?:<br\s*\/?>|<\/p>|<p[^>]*>|\s*$|[a-dA-D]\s*\.\s*<input\b))/gi;
    const options: ReadingQuizOption[] = [];
    let om: RegExpExecArray | null;
    while ((om = optRegex.exec(optsPart)) !== null) {
      const label = om[1].toUpperCase();
      const text = stripTags(om[2]);
      if (text) options.push({ label, text });
    }
    if (stem && options.length >= 2) {
      questions.push({
        id: qIdx,
        question: stem,
        options,
        correctAnswer: answerMap[qIdx] || 'A',
      });
    }
  }

  return questions;
}

export function updatePageSeo(title: string, description?: string) {
  if (typeof document === 'undefined') return;
  document.title = title ? `${title} | TonyEnglish` : 'TonyEnglish - Học tiếng Anh giao tiếp & TOEIC trực tuyến';
  const descText = description ? truncateWords(description, 160) : 'Trung tâm tiếng Anh TonyEnglish - Đào tạo tiếng Anh giao tiếp, luyện thi TOEIC, IELTS và thư viện bài đọc, video luyện nghe trực tuyến.';
  let metaDesc = document.querySelector('meta[name="description"]');
  if (!metaDesc) {
    metaDesc = document.createElement('meta');
    metaDesc.setAttribute('name', 'description');
    document.head.appendChild(metaDesc);
  }
  metaDesc.setAttribute('content', descText);
}
