const fs = require('fs');

function generateGeographyPodcastPlayerHtml(episodes, lang = 'vi') {
  const isEn = lang === 'en';
  const episodesJson = JSON.stringify(episodes).replace(/</g, '\\u003c');

  const themePrimary = '#0f766e'; // Deep teal for Geography
  const themeCardGradient = 'linear-gradient(135deg, #064e3b 0%, #0f766e 50%, #0284c7 100%)';

  const filterOptions = isEn ? `
    <option value="ALL">🌍 All 35 Topics (Full 0460 Syllabus)</option>
    <option value="Physical">⛰️ Physical Geography (Topics 1 - 5)</option>
    <option value="Human">👥 Human Geography (Topics 6 - 10)</option>
    <option value="Topic 1">🌊 Topic 1: River environments (1.1 - 1.3)</option>
    <option value="Topic 2">🏖️ Topic 2: Coastal environments (2.1 - 2.3)</option>
    <option value="Topic 3">🐧 Topic 3: Ecosystems (3.1 - 3.4)</option>
    <option value="Topic 4">🌋 Topic 4: Tectonic hazards (4.1 - 4.4)</option>
    <option value="Topic 5">🌡️ Topic 5: Climate change (5.1 - 5.3)</option>
    <option value="Topic 6">👥 Topic 6: Populations (6.1 - 6.3)</option>
    <option value="Topic 7">🏙️ Topic 7: Towns and cities (7.1 - 7.3)</option>
    <option value="Topic 8">📈 Topic 8: Development (8.1 - 8.3)</option>
    <option value="Topic 9">🌐 Topic 9: Changing economies (9.1 - 9.3)</option>
    <option value="Topic 10">⚡ Topic 10: Resource provision (10.1 - 10.6)</option>
  ` : `
    <option value="ALL">🌍 Tất cả 35 Chủ đề (Trọn bộ 0460)</option>
    <option value="Physical">⛰️ Địa lý Tự nhiên (Chủ đề 1 - 5)</option>
    <option value="Human">👥 Địa lý Kinh tế - Xã hội (Chủ đề 6 - 10)</option>
    <option value="Topic 1">🌊 Chủ đề 1: Môi trường sông ngòi (1.1 - 1.3)</option>
    <option value="Topic 2">🏖️ Chủ đề 2: Môi trường bờ biển (2.1 - 2.3)</option>
    <option value="Topic 3">🐧 Chủ đề 3: Các hệ sinh thái (3.1 - 3.4)</option>
    <option value="Topic 4">🌋 Chủ đề 4: Thảm họa kiến tạo (4.1 - 4.4)</option>
    <option value="Topic 5">🌡️ Chủ đề 5: Biến đổi khí hậu (5.1 - 5.3)</option>
    <option value="Topic 6">👥 Chủ đề 6: Biến động dân số (6.1 - 6.3)</option>
    <option value="Topic 7">🏙️ Chủ đề 7: Đô thị và thành phố (7.1 - 7.3)</option>
    <option value="Topic 8">📈 Chủ đề 8: Phát triển kinh tế (8.1 - 8.3)</option>
    <option value="Topic 9">🌐 Chủ đề 9: Chuyển dịch kinh tế (9.1 - 9.3)</option>
    <option value="Topic 10">⚡ Chủ đề 10: Cung ứng tài nguyên (10.1 - 10.6)</option>
  `;

  return `
<div id="podcast-app" class="podcast-container">
  <style>
    :root {
      --primary: #0f766e;
      --primary-hover: #115e59;
      --primary-light: #f0fdfa;
      --primary-border: #99f6e4;
      --accent: #0284c7;
      --slate-900: #0f172a;
      --slate-800: #1e293b;
      --slate-700: #334155;
      --slate-600: #475569;
      --slate-500: #64748b;
      --slate-400: #94a3b8;
      --slate-200: #e2e8f0;
      --slate-100: #f1f5f9;
      --slate-50: #f8fafc;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      margin: 0;
      padding: 0;
      background: transparent;
      line-height: 1.5;
    }

    .podcast-container {
      max-width: 980px;
      margin: 0 auto;
      padding: 12px 16px 28px;
    }

    /* LANGUAGE SWITCHER BAR */
    .lang-switch-bar {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }

    .lang-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
      transition: all 0.2s ease;
      border: 1.5px solid transparent;
      text-decoration: none;
      line-height: 1;
    }

    .lang-pill.active {
      background: #0f766e;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(15, 118, 110, 0.25);
    }

    .lang-pill.switch-btn {
      background: #ffffff;
      color: var(--slate-700);
      border-color: var(--slate-200);
      cursor: pointer;
      user-select: none;
    }

    .lang-pill.switch-btn:hover {
      background: #f8fafc;
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-1px);
      box-shadow: 0 4px 8px -2px rgba(0, 0, 0, 0.06);
    }

    /* HERO PLAYER CARD */
    .player-card {
      background: ${themeCardGradient};
      border-radius: 20px;
      padding: 24px 28px;
      color: #ffffff;
      box-shadow: 0 10px 25px -5px rgba(15, 118, 110, 0.28), 0 8px 10px -6px rgba(15, 118, 110, 0.2);
      margin-bottom: 24px;
      position: relative;
    }

    .player-top {
      display: flex;
      align-items: center;
      gap: 20px;
      margin-bottom: 20px;
    }

    .cover-art {
      width: 76px;
      height: 76px;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      backdrop-filter: blur(10px);
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.3);
    }

    .cover-art svg {
      width: 32px;
      height: 32px;
      stroke: #ffffff;
      fill: none;
      stroke-width: 2;
    }

    .cover-art .code {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-top: 2px;
    }

    .cover-art .sub {
      font-size: 9px;
      text-transform: uppercase;
      opacity: 0.85;
      font-weight: 700;
      letter-spacing: 0.5px;
    }

    .track-info {
      flex: 1;
      min-width: 0;
    }

    .track-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 3px 10px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 8px;
    }

    .equalizer-dots {
      display: inline-flex;
      align-items: flex-end;
      gap: 2px;
      height: 12px;
    }

    .equalizer-dots span {
      width: 2px;
      background: #5eead4;
      border-radius: 2px;
      animation: eq 0.8s ease-in-out infinite alternate;
    }

    .equalizer-dots span:nth-child(1) { height: 4px; animation-delay: 0.1s; }
    .equalizer-dots span:nth-child(2) { height: 10px; animation-delay: 0.3s; }
    .equalizer-dots span:nth-child(3) { height: 6px; animation-delay: 0.2s; }

    .equalizer-dots.paused span {
      animation: none !important;
      height: 4px !important;
    }

    @keyframes eq {
      0% { height: 3px; }
      100% { height: 12px; }
    }

    .track-title {
      font-size: 20px;
      font-weight: 800;
      line-height: 1.3;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .track-subtitle {
      font-size: 13px;
      opacity: 0.9;
      font-weight: 500;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      color: #ccfbf1;
    }

    /* TIMELINE */
    .timeline-container {
      margin-bottom: 16px;
    }

    .progress-bar-wrapper {
      position: relative;
      width: 100%;
      height: 7px;
      background: rgba(255, 255, 255, 0.25);
      border-radius: 4px;
      cursor: pointer;
      user-select: none;
    }

    .progress-bar-fill {
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      background: #ffffff;
      border-radius: 4px;
      width: 0%;
      transition: width 0.1s linear;
    }

    .progress-handle {
      position: absolute;
      right: -6px;
      top: 50%;
      transform: translateY(-50%);
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
      opacity: 0;
      transition: opacity 0.15s ease;
    }

    .progress-bar-wrapper:hover .progress-handle {
      opacity: 1;
    }

    .time-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 6px;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.5px;
      opacity: 0.85;
      font-variant-numeric: tabular-nums;
    }

    /* CONTROLS */
    .controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .speed-btn {
      padding: 6px 12px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.16);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
      min-width: 58px;
      text-align: center;
    }

    .speed-btn:hover {
      background: rgba(255, 255, 255, 0.28);
    }

    .playback-cluster {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .btn-circle {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.16);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .btn-circle:hover {
      background: rgba(255, 255, 255, 0.28);
      transform: scale(1.06);
    }

    .btn-circle.btn-play-pause {
      width: 52px;
      height: 52px;
      background: #ffffff;
      color: #0f766e;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .btn-circle.btn-play-pause:hover {
      background: #ffffff;
      transform: scale(1.08);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.28);
    }

    .volume-cluster {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .vol-btn {
      background: transparent;
      border: none;
      color: #ffffff;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0.85;
      transition: opacity 0.15s ease;
    }

    .vol-btn:hover {
      opacity: 1;
    }

    .volume-slider {
      -webkit-appearance: none;
      appearance: none;
      width: 80px;
      height: 5px;
      border-radius: 3px;
      background: rgba(255, 255, 255, 0.3);
      outline: none;
      cursor: pointer;
    }

    .volume-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.3);
      cursor: pointer;
    }

    /* TOOLBAR (FILTER & SEARCH) */
    .playlist-toolbar {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }

    .search-box {
      flex: 1;
      min-width: 220px;
      position: relative;
    }

    .search-input {
      width: 100%;
      padding: 10px 14px 10px 38px;
      border-radius: 12px;
      border: 1.5px solid var(--slate-200);
      background: #ffffff;
      font-size: 13.5px;
      color: var(--slate-800);
      outline: none;
      transition: all 0.15s ease;
    }

    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.12);
    }

    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--slate-400);
      pointer-events: none;
    }

    .filter-select {
      padding: 10px 36px 10px 14px;
      border-radius: 12px;
      border: 1.5px solid var(--slate-200);
      background: #ffffff;
      font-size: 13px;
      font-weight: 600;
      color: var(--slate-700);
      outline: none;
      cursor: pointer;
      appearance: none;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 12px center;
      transition: all 0.15s ease;
    }

    .filter-select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.12);
    }

    .count-badge {
      font-size: 12.5px;
      font-weight: 700;
      color: var(--slate-500);
      white-space: nowrap;
    }

    /* PLAYLIST ITEMS */
    .playlist-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .playlist-item {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 16px;
      background: #ffffff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }

    .playlist-item:hover {
      background: var(--slate-50);
      border-color: #99f6e4;
      transform: translateX(2px);
    }

    .playlist-item.active {
      background: #f0fdfa;
      border-color: #5eead4;
      box-shadow: 0 4px 12px -2px rgba(15, 118, 110, 0.15);
    }

    .item-index {
      font-size: 12px;
      font-weight: 800;
      color: var(--slate-400);
      min-width: 28px;
      text-align: center;
    }

    .playlist-item.active .item-index {
      color: var(--primary);
    }

    .item-play-btn {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--slate-100);
      color: var(--slate-700);
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .playlist-item:hover .item-play-btn {
      background: var(--primary);
      color: #ffffff;
    }

    .playlist-item.active .item-play-btn {
      background: var(--primary);
      color: #ffffff;
    }

    .item-content {
      flex: 1;
      min-width: 0;
    }

    .item-title {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--slate-800);
      margin-bottom: 3px;
      line-height: 1.35;
    }

    .playlist-item.active .item-title {
      color: #115e59;
    }

    .item-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12px;
      color: var(--slate-500);
      flex-wrap: wrap;
    }

    .item-subject-badge {
      font-size: 10.5px;
      font-weight: 800;
      padding: 1.5px 7px;
      border-radius: 6px;
      line-height: 1.2;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .badge-physical {
      background: #ccfbf1;
      color: #0f766e;
      border: 1px solid #99f6e4;
    }

    .badge-human {
      background: #ffedd5;
      color: #c2410c;
      border: 1px solid #fed7aa;
    }

    .item-topic {
      font-weight: 600;
      color: var(--slate-600);
    }

    .item-duration {
      margin-left: auto;
      font-variant-numeric: tabular-nums;
      font-weight: 600;
      color: var(--slate-400);
    }

    .subject-header-row {
      margin-top: 14px;
      margin-bottom: 6px;
      font-size: 12px;
      font-weight: 800;
      color: var(--slate-500);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .subject-header-row:first-child {
      margin-top: 4px;
    }

    @media (max-width: 640px) {
      .player-card {
        padding: 18px 18px;
      }
      .track-title {
        font-size: 16px;
      }
      .volume-cluster {
        display: none;
      }
      .item-topic {
        display: none;
      }
    }
  </style>

  <!-- LANGUAGE SWITCHER BUTTONS -->
  <div class="lang-switch-bar">
    ${isEn ? `
    <button type="button" class="lang-pill switch-btn" data-page="1" onclick="switchLecturePage(1)">
      <span>🇻🇳</span>
      <span>Bản Tiếng Việt (Trang 1)</span>
    </button>
    <div class="lang-pill active">
      <span>🇬🇧</span>
      <span>English Edition (Page 2)</span>
    </div>
    ` : `
    <div class="lang-pill active">
      <span>🇻🇳</span>
      <span>Bản Tiếng Việt (Trang 1)</span>
    </div>
    <button type="button" class="lang-pill switch-btn" data-page="2" onclick="switchLecturePage(2)">
      <span>🇬🇧</span>
      <span>Bản Tiếng Anh (Trang 2)</span>
    </button>
    `}
  </div>

  <!-- PLAYER CARD -->
  <div class="player-card">
    <div class="player-top">
      <div class="cover-art">
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg>
        <span class="code" id="cover-code">1.1</span>
        <span class="sub" id="cover-sub">GEO</span>
      </div>
      <div class="track-info">
        <div class="track-badge">
          <span id="badge-code">1.1</span>
          <span>•</span>
          <span id="badge-subject">Physical Geography</span>
          <div class="equalizer-dots" id="eq-dots">
            <span></span><span></span><span></span>
          </div>
        </div>
        <div class="track-title" id="player-title">Loading...</div>
        <div class="track-subtitle" id="player-subtitle">Cambridge IGCSE Geography (0460)</div>
      </div>
    </div>

    <!-- TIMELINE -->
    <div class="timeline-container">
      <div class="progress-bar-wrapper" id="progress-wrapper">
        <div class="progress-bar-fill" id="progress-fill">
          <div class="progress-handle"></div>
        </div>
      </div>
      <div class="time-row">
        <span id="time-current">0:00</span>
        <span id="time-total">0:00</span>
      </div>
    </div>

    <!-- CONTROLS -->
    <div class="controls-row">
      <button class="speed-btn" id="btn-speed" title="${isEn ? 'Change playback speed' : 'Tốc độ phát'}">1.0x</button>
      
      <div class="playback-cluster">
        <button class="btn-circle" id="btn-prev" title="${isEn ? 'Previous episode' : 'Tập trước'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="19 20 9 12 19 4 19 20"></polygon><line x1="5" y1="19" x2="5" y2="5"></line></svg>
        </button>
        <button class="btn-circle" id="btn-rewind" title="${isEn ? 'Rewind 10s' : 'Lùi 10 giây'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path><text x="12" y="15.5" font-size="7.5" font-weight="bold" fill="currentColor" text-anchor="middle" stroke="none">10</text></svg>
        </button>
        <button class="btn-circle btn-play-pause" id="btn-play" title="${isEn ? 'Play / Pause' : 'Phát / Tạm dừng'}">
          <svg id="icon-play" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          <svg id="icon-pause" width="22" height="22" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>
        </button>
        <button class="btn-circle" id="btn-forward" title="${isEn ? 'Forward 10s' : 'Tua 10 giây'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"></path><path d="M21 3v5h-5"></path><text x="12" y="15.5" font-size="7.5" font-weight="bold" fill="currentColor" text-anchor="middle" stroke="none">10</text></svg>
        </button>
        <button class="btn-circle" id="btn-next" title="${isEn ? 'Next episode' : 'Tập tiếp theo'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 4 15 12 5 20 5 4"></polygon><line x1="19" y1="5" x2="19" y2="19"></line></svg>
        </button>
      </div>

      <div class="volume-cluster">
        <button class="vol-btn" id="btn-vol">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
        </button>
        <input type="range" class="volume-slider" id="vol-slider" min="0" max="1" step="0.05" value="1">
      </div>
    </div>
  </div>

  <!-- TOOLBAR: FILTER & SEARCH -->
  <div class="playlist-toolbar">
    <div class="search-box">
      <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <input type="text" class="search-input" id="search-input" placeholder="${isEn ? 'Search 35 topics (e.g., rivers, coasts, climate, 1.1)...' : 'Tìm kiếm 35 chủ đề (ví dụ: sông ngòi, bờ biển, khí hậu, 1.1)...'}">
    </div>

    <select class="filter-select" id="filter-select">
      ${filterOptions}
    </select>

    <div class="count-badge" id="count-badge">35 / 35 ${isEn ? 'topics' : 'chủ đề'}</div>
  </div>

  <!-- PLAYLIST -->
  <div class="playlist-list" id="playlist-list"></div>
</div>

<script>
(function() {
  const EPISODES = ${episodesJson};
  const IS_EN = ${isEn ? 'true' : 'false'};

  // Bridge for switching pages
  window.switchLecturePage = function(targetPage) {
    const p = parseInt(targetPage, 10);
    if (isNaN(p) || p < 1) return;
    try {
      if (window.parent) window.parent.postMessage({ type: 'LECTURE_SWITCH_PAGE', page: p }, '*');
    } catch(e) {}
    try {
      if (window.top && window.top !== window.parent) window.top.postMessage({ type: 'LECTURE_SWITCH_PAGE', page: p }, '*');
    } catch(e) {}

    // Fallback: Click parent button
    try {
      if (window.parent && window.parent.document) {
        const doc = window.parent.document;
        const btns = doc.querySelectorAll('button');
        for (let b of btns) {
          const txt = b.textContent || '';
          if (p === 1 && (txt.includes('Tiếng Việt') || txt.includes('Trang 1'))) {
            b.click();
            break;
          }
          if (p === 2 && (txt.includes('Tiếng Anh') || txt.includes('English') || txt.includes('Trang 2'))) {
            b.click();
            break;
          }
        }
      }
    } catch(e) {}
  };

  // State
  let currentIndex = 0;
  let isPlaying = false;
  let currentSpeed = 1.0;
  const speeds = [0.75, 1.0, 1.25, 1.5, 2.0];
  let filterVal = 'ALL';
  let searchTerm = '';

  const audio = new Audio();
  audio.preload = 'metadata';

  // DOM
  const coverCode = document.getElementById('cover-code');
  const coverSub = document.getElementById('cover-sub');
  const badgeCode = document.getElementById('badge-code');
  const badgeSubject = document.getElementById('badge-subject');
  const eqDots = document.getElementById('eq-dots');
  const playerTitle = document.getElementById('player-title');
  const playerSubtitle = document.getElementById('player-subtitle');
  const progressWrapper = document.getElementById('progress-wrapper');
  const progressFill = document.getElementById('progress-fill');
  const timeCurrent = document.getElementById('time-current');
  const timeTotal = document.getElementById('time-total');
  const btnSpeed = document.getElementById('btn-speed');
  const btnPrev = document.getElementById('btn-prev');
  const btnRewind = document.getElementById('btn-rewind');
  const btnPlay = document.getElementById('btn-play');
  const iconPlay = document.getElementById('icon-play');
  const iconPause = document.getElementById('icon-pause');
  const btnForward = document.getElementById('btn-forward');
  const btnNext = document.getElementById('btn-next');
  const volSlider = document.getElementById('vol-slider');
  const btnVol = document.getElementById('btn-vol');
  const searchInput = document.getElementById('search-input');
  const filterSelect = document.getElementById('filter-select');
  const countBadge = document.getElementById('count-badge');
  const playlistList = document.getElementById('playlist-list');

  function notifyHeight() {
    try {
      const height = document.getElementById('podcast-app').offsetHeight + 40;
      if (window.parent) window.parent.postMessage({ type: 'SET_IFRAME_HEIGHT', height }, '*');
    } catch(e) {}
  }

  function formatTime(sec) {
    if (isNaN(sec) || sec < 0) sec = 0;
    sec = Math.round(sec);
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return m + ':' + (s < 10 ? '0' : '') + s;
  }

  function getBadgeClass(group) {
    if (group === 'Physical geography') return 'badge-physical';
    return 'badge-human';
  }

  function getGroupDisplay(group) {
    if (IS_EN) return group;
    return group === 'Physical geography' ? 'Địa lý Tự nhiên' : 'Địa lý Nhân văn';
  }

  function loadEpisode(index, autoPlay) {
    if (index < 0 || index >= EPISODES.length) return;
    currentIndex = index;
    const ep = EPISODES[index];

    const audioUrl = IS_EN ? ep.audioUrlEn : ep.audioUrlVi;
    const title = IS_EN ? ep.titleEn : ep.titleVi;
    const durStr = IS_EN ? ep.durationEnStr : ep.durationViStr;

    coverCode.textContent = ep.code;
    coverSub.textContent = ep.group === 'Physical geography' ? 'PHYS' : 'HUMAN';
    badgeCode.textContent = ep.code;
    badgeSubject.textContent = getGroupDisplay(ep.group);
    playerTitle.textContent = title;
    playerSubtitle.textContent = ep.syllabusTitle;
    timeCurrent.textContent = '0:00';
    timeTotal.textContent = durStr;
    progressFill.style.width = '0%';

    audio.src = audioUrl;
    audio.playbackRate = currentSpeed;

    if (autoPlay) {
      audio.play().then(() => {
        setPlayingState(true);
      }).catch(err => {
        console.warn('Autoplay prevented:', err);
        setPlayingState(false);
      });
    } else {
      setPlayingState(false);
    }

    updateActiveRow();
  }

  function setPlayingState(playing) {
    isPlaying = playing;
    if (playing) {
      iconPlay.style.display = 'none';
      iconPause.style.display = 'block';
      eqDots.classList.remove('paused');
    } else {
      iconPlay.style.display = 'block';
      iconPause.style.display = 'none';
      eqDots.classList.add('paused');
    }
    updateActiveRow();
  }

  function togglePlayPause() {
    if (!audio.src) {
      loadEpisode(currentIndex, true);
      return;
    }
    if (audio.paused) {
      audio.play().then(() => setPlayingState(true)).catch(() => {});
    } else {
      audio.pause();
      setPlayingState(false);
    }
  }

  // Audio Event Listeners
  audio.addEventListener('timeupdate', () => {
    if (!audio.duration) return;
    const pct = (audio.currentTime / audio.duration) * 100;
    progressFill.style.width = pct + '%';
    timeCurrent.textContent = formatTime(audio.currentTime);
  });

  audio.addEventListener('loadedmetadata', () => {
    timeTotal.textContent = formatTime(audio.duration);
  });

  audio.addEventListener('ended', () => {
    if (currentIndex < EPISODES.length - 1) {
      loadEpisode(currentIndex + 1, true);
    } else {
      setPlayingState(false);
    }
  });

  audio.addEventListener('play', () => setPlayingState(true));
  audio.addEventListener('pause', () => setPlayingState(false));

  // Controls
  btnPlay.addEventListener('click', togglePlayPause);

  btnRewind.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 10);
  });

  btnForward.addEventListener('click', () => {
    audio.currentTime = Math.min(audio.duration || 9999, audio.currentTime + 10);
  });

  btnPrev.addEventListener('click', () => {
    if (currentIndex > 0) loadEpisode(currentIndex - 1, true);
  });

  btnNext.addEventListener('click', () => {
    if (currentIndex < EPISODES.length - 1) loadEpisode(currentIndex + 1, true);
  });

  btnSpeed.addEventListener('click', () => {
    const curIdx = speeds.indexOf(currentSpeed);
    const nextIdx = (curIdx + 1) % speeds.length;
    currentSpeed = speeds[nextIdx];
    audio.playbackRate = currentSpeed;
    btnSpeed.textContent = currentSpeed + 'x';
  });

  progressWrapper.addEventListener('click', (e) => {
    const rect = progressWrapper.getBoundingClientRect();
    const pos = (e.clientX - rect.left) / rect.width;
    if (audio.duration) {
      audio.currentTime = pos * audio.duration;
    }
  });

  volSlider.addEventListener('input', (e) => {
    audio.volume = parseFloat(e.target.value);
  });

  btnVol.addEventListener('click', () => {
    if (audio.volume > 0) {
      audio.volume = 0;
      volSlider.value = 0;
    } else {
      audio.volume = 1;
      volSlider.value = 1;
    }
  });

  // Filter & Search
  filterSelect.addEventListener('change', (e) => {
    filterVal = e.target.value;
    renderPlaylist();
  });

  searchInput.addEventListener('input', (e) => {
    searchTerm = e.target.value.toLowerCase().trim();
    renderPlaylist();
  });

  function renderPlaylist() {
    let filtered = EPISODES.filter(ep => {
      // Filter by category or topic
      if (filterVal === 'Physical' && ep.group !== 'Physical geography') return false;
      if (filterVal === 'Human' && ep.group !== 'Human geography') return false;
      if (filterVal.startsWith('Topic ')) {
        const topicNum = filterVal.replace('Topic ', '');
        if (!ep.code.startsWith(topicNum + '.')) return false;
      }

      // Search term
      if (searchTerm) {
        const matchTitleVi = ep.titleVi.toLowerCase().includes(searchTerm);
        const matchTitleEn = ep.titleEn.toLowerCase().includes(searchTerm);
        const matchTopic = ep.topic.toLowerCase().includes(searchTerm);
        const matchSyllabus = ep.syllabusTitle.toLowerCase().includes(searchTerm);
        const matchCode = ep.code.toLowerCase().includes(searchTerm);
        if (!matchTitleVi && !matchTitleEn && !matchTopic && !matchSyllabus && !matchCode) return false;
      }
      return true;
    });

    countBadge.textContent = filtered.length + ' / ' + EPISODES.length + ' ' + (IS_EN ? 'topics' : 'chủ đề');

    let html = '';
    let lastTopic = null;

    filtered.forEach(ep => {
      if (ep.topic !== lastTopic) {
        lastTopic = ep.topic;
        html += '<div class="subject-header-row">' +
          (ep.group === 'Physical geography' ? '⛰️ ' : '👥 ') +
          ep.topic +
          '</div>';
      }

      const idx = ep.episode - 1;
      const isActive = idx === currentIndex;
      const durationStr = IS_EN ? ep.durationEnStr : ep.durationViStr;
      const title = IS_EN ? ep.titleEn : ep.titleVi;
      const badgeCls = getBadgeClass(ep.group);

      html += '<div class="playlist-item ' + (isActive ? 'active' : '') + '" data-idx="' + idx + '">' +
        '<div class="item-index">#' + (ep.episode < 10 ? '0' + ep.episode : ep.episode) + '</div>' +
        '<button class="item-play-btn" title="' + (isActive && isPlaying ? (IS_EN ? 'Pause' : 'Tạm dừng') : (IS_EN ? 'Play' : 'Phát')) + '">' +
          (isActive && isPlaying
            ? '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>'
            : '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>') +
        '</button>' +
        '<div class="item-content">' +
          '<div class="item-title">' + title + '</div>' +
          '<div class="item-meta">' +
            '<span class="item-subject-badge ' + badgeCls + '">' + ep.code + '</span>' +
            '<span class="item-topic">' + ep.syllabusTitle + '</span>' +
            '<span class="item-duration">' + durationStr + '</span>' +
          '</div>' +
        '</div>' +
      '</div>';
    });

    playlistList.innerHTML = html;

    // Attach clicks
    playlistList.querySelectorAll('.playlist-item').forEach(el => {
      el.addEventListener('click', () => {
        const idx = parseInt(el.getAttribute('data-idx'), 10);
        if (idx === currentIndex) {
          togglePlayPause();
        } else {
          loadEpisode(idx, true);
        }
      });
    });

    notifyHeight();
  }

  function updateActiveRow() {
    playlistList.querySelectorAll('.playlist-item').forEach(el => {
      const idx = parseInt(el.getAttribute('data-idx'), 10);
      const playBtn = el.querySelector('.item-play-btn');
      if (idx === currentIndex) {
        el.classList.add('active');
        if (playBtn) {
          playBtn.innerHTML = isPlaying
            ? '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>'
            : '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>';
        }
      } else {
        el.classList.remove('active');
        if (playBtn) {
          playBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>';
        }
      }
    });
  }

  // Initial setup
  loadEpisode(currentIndex, false);
  renderPlaylist();

  setTimeout(notifyHeight, 150);
  setTimeout(notifyHeight, 500);
  if (window.ResizeObserver) {
    try {
      const ro = new ResizeObserver(() => notifyHeight());
      const appEl = document.getElementById('podcast-app');
      if (appEl) ro.observe(appEl);
    } catch(e) {}
  }
})();
</script>
`;
}

module.exports = { generateGeographyPodcastPlayerHtml };
