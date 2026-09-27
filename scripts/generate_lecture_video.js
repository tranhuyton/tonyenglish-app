const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const SLIDES_DIR = path.join(__dirname, '..', 'scratch', 'slides');
const CLIPS_DIR = path.join(__dirname, '..', 'scratch', 'clips');
const AUDIO_DIR = path.join(__dirname, '..', 'public', 'audio', 'lectures', 'geography', '1_1');
const OUTPUT_VIDEO = path.join(__dirname, '..', 'public', 'videos', 'geography_1_1_lecture.mp4');

// Base64 Logo
const logoBase64 = fs.readFileSync(path.join(__dirname, '..', 'public', 'logo-shield.png')).toString('base64');
const logoSrc = `data:image/png;base64,${logoBase64}`;

const manifest = JSON.parse(fs.readFileSync(path.join(AUDIO_DIR, 'manifest.json'), 'utf8'));

// Common HTML template generator
function generateSlideHtml({ badge, title, subtitle, contentHtml, enSubtitle, viSubtitle, segmentIndex, totalSegments }) {
  return `<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: radial-gradient(circle at 15% 15%, #1e3a8a 0%, #0f172a 45%, #020617 100%);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    /* Ambient background glowing circles */
    body::before {
      content: "";
      position: absolute;
      top: -150px;
      right: -150px;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(14, 165, 233, 0.15) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }
    body::after {
      content: "";
      position: absolute;
      bottom: -150px;
      left: -150px;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(59, 130, 246, 0.12) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }

    /* TOP HEADER BAR */
    .top-bar {
      height: 90px;
      padding: 0 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(12px);
      z-index: 10;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .brand img {
      height: 52px;
      width: auto;
      filter: drop-shadow(0 4px 10px rgba(14, 165, 233, 0.4));
    }
    .brand-text h2 {
      font-size: 20px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 1.5px;
      line-height: 1.1;
    }
    .brand-text p {
      font-size: 13px;
      font-weight: 700;
      color: #38bdf8;
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .watermark-badge {
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(14, 165, 233, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 8px 20px;
      border-radius: 30px;
      box-shadow: 0 0 20px rgba(14, 165, 233, 0.2);
    }
    .watermark-badge .dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #22c55e;
      box-shadow: 0 0 10px #22c55e;
    }
    .watermark-badge span {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.5px;
    }

    /* MAIN HERO CONTENT */
    .main-content {
      flex: 1;
      padding: 30px 60px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      z-index: 10;
    }
    .section-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: rgba(14, 165, 233, 0.2);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 800;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 12px;
      align-self: flex-start;
    }
    .main-title {
      font-size: 38px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.25;
      margin-bottom: 6px;
      text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    .main-subtitle {
      font-size: 18px;
      color: #94a3b8;
      margin-bottom: 24px;
      font-weight: 600;
    }

    /* SUBTITLE BOTTOM BAR */
    .subtitle-bar {
      height: 175px;
      background: rgba(10, 15, 30, 0.85);
      border-top: 2px solid rgba(56, 189, 248, 0.3);
      backdrop-filter: blur(16px);
      padding: 20px 60px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 10px;
      z-index: 10;
      box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
    }
    .sub-en {
      display: flex;
      align-items: flex-start;
      gap: 14px;
    }
    .sub-flag {
      font-size: 18px;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 13px;
      flex-shrink: 0;
      margin-top: 2px;
    }
    .flag-uk {
      background: rgba(59, 130, 246, 0.3);
      color: #93c5fd;
      border: 1px solid rgba(147, 197, 253, 0.3);
    }
    .flag-vi {
      background: rgba(245, 158, 11, 0.3);
      color: #fde047;
      border: 1px solid rgba(253, 224, 71, 0.3);
    }
    .sub-en-text {
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
    }
    .sub-vi-text {
      font-size: 21px;
      font-weight: 600;
      color: #fde047;
      line-height: 1.35;
    }

    /* CARDS GRID FOR KEY TERMS */
    .terms-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      width: 100%;
    }
    .term-card {
      background: rgba(30, 41, 59, 0.7);
      border: 2px solid rgba(255, 255, 255, 0.1);
      border-radius: 16px;
      padding: 22px 24px;
      transition: all 0.3s;
      position: relative;
    }
    .term-card.active {
      background: linear-gradient(135deg, rgba(14, 165, 233, 0.25) 0%, rgba(30, 58, 138, 0.4) 100%);
      border: 3px solid #38bdf8;
      box-shadow: 0 0 35px rgba(56, 189, 248, 0.45);
      transform: scale(1.03);
    }
    .term-card.active::after {
      content: "🎙️ ĐANG GIẢNG";
      position: absolute;
      top: -14px;
      right: 18px;
      background: #0284c7;
      color: #ffffff;
      font-size: 12px;
      font-weight: 900;
      padding: 4px 12px;
      border-radius: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      letter-spacing: 0.5px;
    }
    .term-title {
      font-size: 24px;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 8px;
    }
    .term-desc {
      font-size: 16px;
      color: #cbd5e1;
      line-height: 1.45;
      font-weight: 500;
    }

    /* INTRO HERO */
    .hero-center {
      text-align: center;
      max-width: 1200px;
      margin: 0 auto;
    }
    .hero-icon {
      font-size: 72px;
      margin-bottom: 20px;
      filter: drop-shadow(0 10px 20px rgba(14, 165, 233, 0.4));
    }
    .hero-badge {
      display: inline-block;
      background: linear-gradient(90deg, #0284c7, #06b6d4);
      color: white;
      padding: 8px 24px;
      border-radius: 30px;
      font-weight: 800;
      font-size: 18px;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 20px;
      box-shadow: 0 10px 25px rgba(2, 132, 199, 0.4);
    }

    /* DEFINITION BOX */
    .def-box {
      background: rgba(30, 41, 59, 0.7);
      border-left: 6px solid #38bdf8;
      border-radius: 16px;
      padding: 28px 34px;
      margin-bottom: 24px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .def-box p {
      font-size: 23px;
      line-height: 1.6;
      color: #e2e8f0;
    }

    /* BRADSHAW TABLE */
    .bradshaw-table {
      width: 100%;
      border-collapse: collapse;
      background: rgba(30, 41, 59, 0.6);
      border-radius: 16px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .bradshaw-table th, .bradshaw-table td {
      padding: 16px 24px;
      text-align: left;
      font-size: 18px;
    }
    .bradshaw-table th {
      background: rgba(15, 23, 42, 0.8);
      font-weight: 800;
      color: #38bdf8;
      border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    }
    .bradshaw-table td {
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: #e2e8f0;
    }
    .tag-up { color: #4ade80; font-weight: 800; }
    .tag-down { color: #f87171; font-weight: 800; }

    /* WATER CYCLE FLOW */
    .flow-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }
    .flow-card {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 20px;
    }
    .flow-badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 800;
      margin-bottom: 10px;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <!-- Top Branding Header -->
  <div class="top-bar">
    <div class="brand">
      <img src="${logoSrc}" alt="TonyEnglish">
      <div class="brand-text">
        <h2>TONYENGLISH TEST CENTRE</h2>
        <p>IGCSE GEOGRAPHY 0460 • VIDEO BÀI GIẢNG SONG NGỮ</p>
      </div>
    </div>
    <div class="watermark-badge">
      <div class="dot"></div>
      <span>tonyenglish.vn</span>
    </div>
  </div>

  <!-- Main Slide Content Area -->
  <div class="main-content">
    <div class="section-badge">${badge} • Phân đoạn ${segmentIndex + 1}/${totalSegments}</div>
    <h1 class="main-title">${title}</h1>
    <div class="main-subtitle">${subtitle}</div>
    ${contentHtml}
  </div>

  <!-- Subtitle Bar (Bilingual) -->
  <div class="subtitle-bar">
    <div class="sub-en">
      <span class="sub-flag flag-uk">🇬🇧 UK</span>
      <div class="sub-en-text">${enSubtitle}</div>
    </div>
    <div class="sub-en">
      <span class="sub-flag flag-vi">🇻🇳 VI</span>
      <div class="sub-vi-text">${viSubtitle}</div>
    </div>
  </div>
</body>
</html>`;
}

// Generate the specific content for each of the 11 slides
function getSlideData(segment, index, total) {
  const id = segment.id;

  // Helper for key terms grid
  const renderTermsGrid = (activeId) => `
    <div class="terms-grid">
      <div class="term-card ${activeId === 'source' ? 'active' : ''}">
        <div class="term-title">Source</div>
        <div class="term-desc">Where the river begins — usually on high ground (bog, spring).</div>
      </div>
      <div class="term-card ${activeId === 'mouth' ? 'active' : ''}">
        <div class="term-title">Mouth</div>
        <div class="term-desc">Where the river meets the sea, a lake, or another river.</div>
      </div>
      <div class="term-card ${activeId === 'tributary' ? 'active' : ''}">
        <div class="term-title">Tributary</div>
        <div class="term-desc">A smaller river or stream that flows into the main river.</div>
      </div>
      <div class="term-card ${activeId === 'confluence' ? 'active' : ''}">
        <div class="term-title">Confluence</div>
        <div class="term-desc">The point where two rivers join together.</div>
      </div>
      <div class="term-card ${activeId === 'watershed' ? 'active' : ''}">
        <div class="term-title">Watershed</div>
        <div class="term-desc">The boundary/ridge separating one drainage basin from another.</div>
      </div>
      <div class="term-card ${activeId === 'floodplain' ? 'active' : ''}">
        <div class="term-title">Flood plain</div>
        <div class="term-desc">Flat land beside the river, flooded when discharge is high.</div>
      </div>
    </div>
  `;

  if (id === 'intro') {
    return {
      badge: 'Bắt đầu bài giảng',
      title: '🌊 1.1 Hydrological Characteristics & Processes',
      subtitle: 'Rivers, drainage basins, the water cycle and fluvial processes',
      contentHtml: `
        <div class="hero-center">
          <div class="hero-icon">🏞️</div>
          <div class="hero-badge">CAMBRIDGE IGCSE GEOGRAPHY • TOPIC 1: RIVERS</div>
          <p style="font-size: 26px; color: #cbd5e1; max-width: 900px; margin: 0 auto; line-height: 1.6;">
            Chào mừng các em đến với chuỗi bài giảng trực tuyến của <strong>TonyEnglish Test Centre</strong>.
            Hôm nay chúng ta sẽ tìm hiểu về hệ thống lưu vực sông, các đặc tính thủy văn và quá trình vận hành của dòng nước.
          </p>
        </div>
      `
    };
  }

  if (id === 'drainage_basin') {
    return {
      badge: 'Phần 1: Khái niệm cốt lõi',
      title: '📍 1. Rivers & Drainage Basins (Lưu Vực Sông)',
      subtitle: 'Hệ thống mở tuần hoàn & Ranh giới phân thủy',
      contentHtml: `
        <div class="def-box">
          <p>
            A <strong>drainage basin</strong> is the area of land drained by a river and all its tributaries.<br/>
            It is an <strong>open system</strong> with <strong>inputs</strong> (precipitation) and <strong>outputs</strong> (evaporation, river discharge to sea).
          </p>
        </div>
        <div class="def-box" style="border-left-color: #a855f7;">
          <p>
            The boundary of a drainage basin is called the <strong>watershed</strong> — usually following a ridge of high ground that divides one basin from another.
          </p>
        </div>
      `
    };
  }

  if (['source', 'mouth', 'tributary', 'confluence', 'watershed', 'floodplain'].includes(id)) {
    return {
      badge: 'Thuật ngữ trọng tâm (Key Terms)',
      title: '🔍 Drainage Basin Key Features (6 Khái Niệm Quan Trọng)',
      subtitle: 'Xác định các thành phần của hệ thống dòng sông từ thượng lưu ra hạ lưu',
      contentHtml: renderTermsGrid(id)
    };
  }

  if (id === 'bradshaw_model') {
    return {
      badge: 'Phần 2: Quy luật dòng chảy',
      title: '📉 2. The Bradshaw Model (Mô Hình Bradshaw)',
      subtitle: 'Sự biến đổi của các yếu tố lòng sông từ thượng lưu (Source) ra cửa biển (Mouth)',
      contentHtml: `
        <table class="bradshaw-table">
          <thead>
            <tr>
              <th>Đặc tính sông (Characteristic)</th>
              <th>Xu hướng xuôi dòng</th>
              <th>Nguyên nhân cốt lõi (Cambridge Logic)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="font-weight: 700; color: #38bdf8;">Discharge (Lưu lượng)</td>
              <td class="tag-up">TĂNG MẠNH ↗</td>
              <td>Nhiều phụ lưu (tributaries) hòa nhập vào dòng chính</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #38bdf8;">Width & Depth (Bề rộng & Độ sâu)</td>
              <td class="tag-up">TĂNG ↗</td>
              <td>Lưu lượng lớn thúc đẩy xói mòn ngang mở rộng lòng sông</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #38bdf8;">Velocity (Vận tốc trung bình)</td>
              <td class="tag-up">TĂNG ↗ (Học sinh hay nhầm!)</td>
              <td>Lòng sông sâu nhẵn, ít ma sát biên hơn vùng thượng lưu đá tảng</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #38bdf8;">Gradient / Slope (Độ dốc)</td>
              <td class="tag-down">GIẢM ↘</td>
              <td>Từ núi non hiểm trở thoai thoải dần về đồng bằng bằng phẳng</td>
            </tr>
            <tr>
              <td style="font-weight: 700; color: #38bdf8;">Bed Roughness & Particle Size</td>
              <td class="tag-down">GIẢM ↘</td>
              <td>Va đập nghiền nhỏ (attrition) làm đá mài nhẵn thành cát mịn</td>
            </tr>
          </tbody>
        </table>
      `
    };
  }

  if (id === 'water_cycle') {
    return {
      badge: 'Phần 3: Chu trình thủy văn',
      title: '🔄 3. The Drainage Basin Hydrological Cycle',
      subtitle: '4 Nhóm thành phần: Inputs ➜ Stores ➜ Transfers ➜ Outputs',
      contentHtml: `
        <div class="flow-grid">
          <div class="flow-card" style="border-top: 4px solid #38bdf8;">
            <span class="flow-badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">1. Inputs (Đầu vào)</span>
            <h3 style="font-size: 20px; color: #fff; margin-bottom: 8px;">🌧️ Precipitation</h3>
            <p style="font-size: 15px; color: #94a3b8; line-height: 1.45;">Mưa, tuyết, sương mù cung cấp nguồn nước duy nhất vào hệ thống.</p>
          </div>
          <div class="flow-card" style="border-top: 4px solid #22c55e;">
            <span class="flow-badge" style="background: rgba(34, 197, 94, 0.2); color: #4ade80;">2. Stores (Lưu trữ)</span>
            <h3 style="font-size: 20px; color: #fff; margin-bottom: 8px;">🌿 Interception & Soil</h3>
            <p style="font-size: 15px; color: #94a3b8; line-height: 1.45;">Tán cây chắn mưa (Interception) và nước tích tụ trong tầng đất/ngầm.</p>
          </div>
          <div class="flow-card" style="border-top: 4px solid #a855f7;">
            <span class="flow-badge" style="background: rgba(168, 85, 247, 0.2); color: #c084fc;">3. Transfers (Chuyển dịch)</span>
            <h3 style="font-size: 20px; color: #fff; margin-bottom: 8px;">💧 Runoff & Throughflow</h3>
            <p style="font-size: 15px; color: #94a3b8; line-height: 1.45;">Dòng chảy mặt (Runoff), thấm đất (Infiltration) và dòng ngầm.</p>
          </div>
          <div class="flow-card" style="border-top: 4px solid #f59e0b;">
            <span class="flow-badge" style="background: rgba(245, 158, 11, 0.2); color: #fbbf24;">4. Outputs (Đầu ra)</span>
            <h3 style="font-size: 20px; color: #fff; margin-bottom: 8px;">☀️ Evapotranspiration</h3>
            <p style="font-size: 15px; color: #94a3b8; line-height: 1.45;">Tổng lượng bốc hơi bề mặt + thoát hơi nước qua lá cây trở lại khí quyển.</p>
          </div>
        </div>
      `
    };
  }

  if (id === 'fluvial_processes') {
    return {
      badge: 'Phần 4: Quá trình tác động',
      title: '⚙️ 4. Fluvial Processes (Quá Trình Sông Ngòi)',
      subtitle: '4 Hình thức Xói mòn (Erosion) & 4 Hình thức Vận chuyển (Transportation)',
      contentHtml: `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
          <!-- 4 Types of Erosion -->
          <div style="background: rgba(239, 68, 68, 0.1); border: 2px solid rgba(239, 68, 68, 0.3); border-radius: 16px; padding: 22px;">
            <h3 style="font-size: 22px; color: #f87171; margin-bottom: 14px; font-weight: 800;">💥 4 Types of Erosion (Xói mòn)</h3>
            <ul style="list-style: none; space-y: 8px; font-size: 16px; color: #e2e8f0; line-height: 1.6;">
              <li style="margin-bottom: 8px;"><strong>1. Hydraulic Action:</strong> Sức nước nén khí vào kẽ nứt làm vỡ đá.</li>
              <li style="margin-bottom: 8px;"><strong>2. Abrasion (Corrasion):</strong> Đất đá đáy sông đóng vai trò giấy ráp mài mòn.</li>
              <li style="margin-bottom: 8px;"><strong>3. Attrition:</strong> Các hòn đá va đập vào nhau vỡ vụn và mài tròn.</li>
              <li><strong>4. Solution (Corrosion):</strong> Nước sông có axit hòa tan các loại đá vôi.</li>
            </ul>
          </div>
          <!-- 4 Types of Transportation -->
          <div style="background: rgba(56, 189, 248, 0.1); border: 2px solid rgba(56, 189, 248, 0.3); border-radius: 16px; padding: 22px;">
            <h3 style="font-size: 22px; color: #38bdf8; margin-bottom: 14px; font-weight: 800;">🚚 4 Types of Transportation (Vận chuyển)</h3>
            <ul style="list-style: none; space-y: 8px; font-size: 16px; color: #e2e8f0; line-height: 1.6;">
              <li style="margin-bottom: 8px;"><strong>1. Traction:</strong> Cuội tảng lớn lăn trượt dọc theo đáy sông.</li>
              <li style="margin-bottom: 8px;"><strong>2. Saltation:</strong> Các viên sỏi nhảy cóc từng đợt trên đáy sông.</li>
              <li style="margin-bottom: 8px;"><strong>3. Suspension:</strong> Hạt sét và phù sa lơ lửng làm nước có màu nâu đục.</li>
              <li><strong>4. Solution:</strong> Các khoáng chất hòa tan hoàn toàn trong nước.</li>
            </ul>
          </div>
        </div>
      `
    };
  }

  return {
    badge: 'Bài giảng IGCSE Geography',
    title: segment.title,
    subtitle: 'TonyEnglish Test Centre',
    contentHtml: `<div></div>`
  };
}

async function renderSlides() {
  console.log('🚀 Khởi động Puppeteer để render 11 slide Full HD (1920x1080)...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });

  const total = manifest.segments.length;
  for (let i = 0; i < total; i++) {
    const seg = manifest.segments[i];
    const data = getSlideData(seg, i, total);

    const fullHtml = generateSlideHtml({
      badge: data.badge,
      title: data.title,
      subtitle: data.subtitle,
      contentHtml: data.contentHtml,
      enSubtitle: seg.en,
      viSubtitle: seg.vi,
      segmentIndex: i,
      totalSegments: total
    });

    await page.setContent(fullHtml, { waitUntil: 'domcontentloaded' });
    const slidePath = path.join(SLIDES_DIR, `slide_${String(i + 1).padStart(2, '0')}.png`);
    await page.screenshot({ path: slidePath });
    console.log(`  [${i + 1}/${total}] Đã render: ${path.basename(slidePath)} (${seg.title})`);
  }

  await browser.close();
  console.log('✅ Hoàn tất render tất cả ảnh slide!');
}

async function encodeClips() {
  console.log('\n🎬 Bắt đầu ghép Slide + Audio thành 11 video clips với ffmpeg...');
  const total = manifest.segments.length;
  const clipList = [];

  for (let i = 0; i < total; i++) {
    const seg = manifest.segments[i];
    const slideImg = path.join(SLIDES_DIR, `slide_${String(i + 1).padStart(2, '0')}.png`);
    const audioPath = path.join(AUDIO_DIR, `${seg.id}.mp3`);
    const clipPath = path.join(CLIPS_DIR, `clip_${String(i + 1).padStart(2, '0')}.mp4`);

    console.log(`  [${i + 1}/${total}] Ghép clip: ${seg.id}.mp4 (thời lượng: ${seg.duration}s)...`);

    // Ghép ảnh tĩnh và file âm thanh với chuẩn H.264 / AAC 1080p
    const cmd = `ffmpeg -y -loop 1 -framerate 25 -i "${slideImg}" -i "${audioPath}" -c:v libx264 -tune stillimage -preset veryfast -crf 22 -c:a aac -b:a 192k -pix_fmt yuv420p -shortest "${clipPath}"`;
    execSync(cmd, { stdio: 'ignore' });

    clipList.push(clipPath);
  }

  console.log('✅ Hoàn tất render 11 video clips!');
  return clipList;
}

async function concatenateVideo(clipList) {
  console.log('\n🔗 Đang nối 11 clip thành video bài giảng hoàn chỉnh...');
  const listFile = path.join(CLIPS_DIR, 'concat_list.txt');
  const fileContent = clipList.map(c => `file '${c.replace(/\\/g, '/')}'`).join('\n');
  fs.writeFileSync(listFile, fileContent, 'utf8');

  // Nối các video bằng concat demuxer
  const cmd = `ffmpeg -y -f concat -safe 0 -i "${listFile}" -c copy "${OUTPUT_VIDEO}"`;
  execSync(cmd, { stdio: 'ignore' });

  const stats = fs.statSync(OUTPUT_VIDEO);
  console.log(`\n🎉 XUẤT XƯỞNG THÀNH CÔNG FILE VIDEO BÀI GIẢNG!`);
  console.log(`📁 Đường dẫn: ${OUTPUT_VIDEO}`);
  console.log(`📦 Kích thước: ${(stats.size / (1024 * 1024)).toFixed(2)} MB`);
  console.log(`⏱️ Tổng thời lượng: ${manifest.totalDuration}s (~${(manifest.totalDuration / 60).toFixed(2)} phút)`);
}

async function main() {
  try {
    await renderSlides();
    const clipList = await encodeClips();
    await concatenateVideo(clipList);
  } catch (err) {
    console.error('Lỗi tạo video:', err);
  }
}

main();
