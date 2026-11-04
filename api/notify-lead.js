const https = require('https');

const TARGET_ADMIN_EMAIL = 'tranhuyton@gmail.com';
const RELAY_ENDPOINT = 'https://tuvithayton.vn/api/internal/tonyenglish-lead-email';

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    if (req.body && typeof req.body === 'object') {
      resolve(req.body);
      return;
    }
    if (typeof req.body === 'string') {
      try {
        resolve(req.body ? JSON.parse(req.body) : {});
      } catch (err) {
        reject(err);
      }
      return;
    }
    let raw = '';
    req.on('data', (chunk) => {
      raw += chunk;
      if (raw.length > 32 * 1024) {
        reject(new Error('Payload too large'));
      }
    });
    req.on('end', () => {
      try {
        resolve(raw ? JSON.parse(raw) : {});
      } catch (err) {
        reject(err);
      }
    });
    req.on('error', reject);
  });
}

function httpsJsonRequest(urlStr, method, headers, payloadObj) {
  return new Promise((resolve, reject) => {
    const parsed = new URL(urlStr);
    const bodyStr = payloadObj ? JSON.stringify(payloadObj) : '';
    const req = https.request(
      {
        hostname: parsed.hostname,
        port: parsed.port || 443,
        path: parsed.pathname + parsed.search,
        method,
        headers: {
          'Content-Type': 'application/json',
          ...(bodyStr ? { 'Content-Length': Buffer.byteLength(bodyStr, 'utf8') } : {}),
          ...headers,
        },
      },
      (res) => {
        let data = '';
        res.on('data', (chunk) => {
          data += chunk;
        });
        res.on('end', () => {
          let json = null;
          try {
            json = data ? JSON.parse(data) : null;
          } catch (_) {}
          resolve({ status: res.statusCode || 500, json, raw: data });
        });
      }
    );
    req.on('error', reject);
    req.setTimeout(8000, () => {
      req.destroy(new Error('Upstream timeout'));
    });
    if (bodyStr) req.write(bodyStr);
    req.end();
  });
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ ok: false, error: 'Method not allowed' });
    return;
  }

  try {
    const body = await readJsonBody(req);
    const contactId = Number(body.contactId || 0);
    const phone = String(body.phone || '').trim();
    const name = String(body.name || 'Phụ huynh / Học viên').trim();
    const email = String(body.email || '').trim();
    const course = String(body.course || 'Tư vấn khóa học TonyEnglish').trim();
    const note = String(body.note || '').trim();
    const pageUrl = String(body.pageUrl || 'https://tonyenglish.vn/courses').trim();
    const sourceType = String(body.sourceType || 'CallbackForm').trim();

    if (!contactId || !phone) {
      res.status(400).json({ ok: false, error: 'Missing contactId or phone' });
      return;
    }

    // Verify row exists in te_contact and was just created (prevents spoofed spam)
    const sbUrl = (process.env.VITE_SUPABASE_URL || '').replace(/\/$/, '');
    const sbKey = process.env.VITE_SUPABASE_ANON_KEY || '';
    if (sbUrl && sbKey) {
      const verifyUrl = `${sbUrl}/rest/v1/te_contact?contact_id=eq.${encodeURIComponent(
        String(contactId)
      )}&select=contact_id,contact_phone,contact_created_at&limit=1`;
      const verifyRes = await httpsJsonRequest(verifyUrl, 'GET', {
        apikey: sbKey,
        Authorization: `Bearer ${sbKey}`,
      });
      const rows = Array.isArray(verifyRes.json) ? verifyRes.json : [];
      if (rows.length === 0) {
        res.status(403).json({ ok: false, error: 'Unverified contact record' });
        return;
      }
      const createdAtSec = Number(rows[0].contact_created_at || 0);
      const nowSec = Math.floor(Date.now() / 1000);
      if (createdAtSec > 0 && Math.abs(nowSec - createdAtSec) > 600) {
        res.status(403).json({ ok: false, error: 'Expired contact record' });
        return;
      }
    }

    // Option 1: Direct Resend API if RESEND_API_KEY is configured on tonyenglish-app
    if (process.env.RESEND_API_KEY) {
      const subject =
        sourceType === 'ContactPage'
          ? `📩 [Liên hệ TonyEnglish] ${phone} - ${name}`
          : `🔔 [Học Thử TonyEnglish] ${phone} - ${name} (${course})`;
      const directRes = await httpsJsonRequest(
        'https://api.resend.com/emails',
        'POST',
        { Authorization: `Bearer ${process.env.RESEND_API_KEY}` },
        {
          from: process.env.SMTP_FROM || 'TonyEnglish Tuyển Sinh <onboarding@resend.dev>',
          to: [TARGET_ADMIN_EMAIL],
          subject,
          html: `<p><strong>Họ tên:</strong> ${name}</p><p><strong>SĐT / Zalo:</strong> ${phone}</p><p><strong>Khóa học:</strong> ${course}</p><p><strong>Ghi chú:</strong> ${note}</p><p><strong>Link:</strong> ${pageUrl}</p>`,
        }
      );
      if (directRes.status >= 200 && directRes.status < 300) {
        res.status(200).json({ ok: true, provider: 'direct-resend' });
        return;
      }
    }

    // Option 2: Relay via Tony's verified email service on tuvithayton.vn
    const relayRes = await httpsJsonRequest(
      RELAY_ENDPOINT,
      'POST',
      { 'x-tony-lead-relay': 'tonyenglish-v1' },
      {
        contactId,
        name,
        phone,
        email,
        course,
        note,
        pageUrl,
        sourceType,
      }
    );

    if (relayRes.status >= 200 && relayRes.status < 300 && relayRes.json && relayRes.json.ok) {
      res.status(200).json({ ok: true, provider: 'relay', detail: relayRes.json });
      return;
    }

    res.status(502).json({ ok: false, error: 'Email relay failed', detail: relayRes.json });
  } catch (err) {
    res.status(500).json({ ok: false, error: err && err.message ? err.message : 'Server error' });
  }
};
