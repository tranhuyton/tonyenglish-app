const https = require('https');

const ALLOWED_FILES = new Set([
  'index.html',
  'html5-unsupported.html',
  'goodbye.html',
]);

const SUPABASE_STORAGE_BASE =
  'https://ubkvzgwespfvrlpjuxkp.supabase.co/storage/v1/object/public/tonyenglish_uploads/FlashQuiz';

function safeDecode(str) {
  try {
    return decodeURIComponent(str);
  } catch (_) {
    return str;
  }
}

module.exports = (req, res) => {
  const rawDir = req.query.dir;
  const rawFile = (req.query.file || 'index.html').toString().trim();

  if (!ALLOWED_FILES.has(rawFile)) {
    res.status(400).send('Invalid FlashQuiz entry file');
    return;
  }

  let dirStr = '';
  if (Array.isArray(rawDir)) {
    dirStr = rawDir.join('/');
  } else if (typeof rawDir === 'string') {
    dirStr = rawDir;
  }

  if (!dirStr) {
    res.status(400).send('Missing FlashQuiz directory');
    return;
  }

  const segments = dirStr.split('/').filter(Boolean);
  for (const seg of segments) {
    const dec = safeDecode(seg);
    if (dec === '.' || dec === '..' || dec.includes('\\')) {
      res.status(400).send('Invalid path segment');
      return;
    }
  }

  const encodedPath = segments
    .map((seg) => encodeURIComponent(safeDecode(seg)))
    .join('/');

  const targetUrl = `${SUPABASE_STORAGE_BASE}/${encodedPath}/${encodeURIComponent(
    rawFile
  )}`;

  https
    .get(targetUrl, (upRes) => {
      if (upRes.statusCode !== 200) {
        res
          .status(upRes.statusCode || 404)
          .setHeader('Content-Type', 'text/plain; charset=utf-8')
          .send(`FlashQuiz resource not found (${upRes.statusCode})`);
        upRes.resume();
        return;
      }

      res.status(200);
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      res.setHeader(
        'Cache-Control',
        'public, s-maxage=86400, max-age=3600, stale-while-revalidate=604800'
      );
      upRes.pipe(res);
    })
    .on('error', () => {
      res.status(502).send('Upstream storage connection error');
    });
};
