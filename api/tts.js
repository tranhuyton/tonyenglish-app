const https = require('https');

module.exports = (req, res) => {
  const tl = (req.query.tl || 'en').toString().trim();
  const q = (req.query.q || '').toString().trim().slice(0, 200);

  if (!q) {
    res.status(400).send('Missing q');
    return;
  }

  const targetUrl = `https://translate.googleapis.com/translate_tts?ie=UTF-8&client=gtx&tl=${encodeURIComponent(
    tl
  )}&q=${encodeURIComponent(q)}`;

  https
    .get(
      targetUrl,
      {
        headers: {
          'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        },
      },
      (upRes) => {
        if (upRes.statusCode !== 200) {
          res.status(upRes.statusCode || 502).send('TTS upstream error');
          return;
        }
        res.setHeader('Content-Type', 'audio/mpeg');
        res.setHeader('Cache-Control', 'public, s-maxage=31536000, max-age=31536000, immutable');
        upRes.pipe(res);
      }
    )
    .on('error', () => {
      res.status(500).send('TTS fetch failed');
    });
};
