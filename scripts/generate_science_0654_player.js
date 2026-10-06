const fs = require('fs');

function generateSciencePodcastPlayerHtml(episodes, lang = 'vi') {
  const isEn = lang === 'en';
  const episodesJson = JSON.stringify(episodes).replace(/</g, '\\u003c');

  const themePrimary = '#0284c7'; // Blue/sky accent for Co-ordinated Science 0654
  const themePrimaryDark = '#0369a1';
  const themePrimaryLight = '#f0f9ff';
  const themeCardGradient = 'linear-gradient(135deg, #0c4a6e 0%, #075985 50%, #0284c7 100%)';

  const filterOptions = isEn ? `
    <option value="ALL">All 35 Topics (Full 0654 Syllabus)</option>
    <option value="Biology">🧬 Biology (B1 - B13)</option>
    <option value="Chemistry">🧪 Chemistry (C1 - C14)</option>
    <option value="Physics">⚡ Physics (P1 - P8)</option>
  ` : `
    <option value="ALL">Tất cả 35 Chủ đề (Trọn bộ 0654)</option>
    <option value="Biology">🧬 Sinh học (B1 - B13)</option>
    <option value="Chemistry">🧪 Hóa học (C1 - C14)</option>
    <option value="Physics">⚡ Vật lý (P1 - P8)</option>
  `;

  return `
<div id="podcast-app" class="podcast-container">
  <style>
    :root {
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-light: #f0f9ff;
      --primary-border: #bae6fd;
      --accent: #059669;
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



    /* HERO PLAYER CARD */
    .player-card {
      background: ${themeCardGradient};
      border-radius: 20px;
      padding: 24px 28px;
      color: #ffffff;
      box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.28), 0 8px 10px -6px rgba(2, 132, 199, 0.2);
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
      background: #38bdf8;
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
      color: #e0f2fe;
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
      bottom: 0;
      background: #38bdf8;
      border-radius: 4px;
      width: 0%;
      transition: width 0.1s linear;
    }

    .progress-thumb {
      position: absolute;
      right: -6px;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      opacity: 0;
      transition: opacity 0.15s ease;
    }

    .progress-bar-wrapper:hover .progress-thumb {
      opacity: 1;
    }

    .time-row {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: #bae6fd;
      font-weight: 600;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      margin-top: 6px;
    }

    /* CONTROLS ROW */
    .controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .playback-buttons {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn-icon {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .btn-icon:hover {
      background: rgba(255, 255, 255, 0.24);
      transform: scale(1.05);
    }

    .btn-icon:active {
      transform: scale(0.96);
    }

    .btn-play-main {
      background: #ffffff;
      color: #0369a1;
      border: none;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
      transition: all 0.2s ease;
    }

    .btn-play-main:hover {
      transform: scale(1.08);
      background: #f0fdf4;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    }

    .btn-play-main:active {
      transform: scale(0.95);
    }

    .extra-controls {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .btn-speed {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      padding: 5px 11px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .btn-speed:hover {
      background: rgba(255, 255, 255, 0.22);
    }

    .volume-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .volume-slider {
      width: 76px;
      height: 5px;
      -webkit-appearance: none;
      background: rgba(255, 255, 255, 0.25);
      border-radius: 3px;
      outline: none;
      cursor: pointer;
    }

    .volume-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #ffffff;
      cursor: pointer;
      box-shadow: 0 1px 4px rgba(0,0,0,0.3);
    }

    .auto-next-toggle {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      user-select: none;
      color: #bae6fd;
    }

    .auto-next-toggle input {
      accent-color: #38bdf8;
      cursor: pointer;
      width: 14px;
      height: 14px;
    }

    /* SECTION / SUBJECT SELECTOR */
    .filter-section {
      margin-bottom: 14px;
    }

    .section-select-wrapper {
      display: flex;
      gap: 10px;
      align-items: center;
    }

    .section-select {
      flex: 1;
      min-width: 240px;
      padding: 9px 14px;
      border-radius: 12px;
      border: 1.5px solid var(--slate-200);
      background: #ffffff;
      color: var(--slate-800);
      font-size: 13px;
      font-weight: 600;
      outline: none;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .section-select:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
    }

    /* SEARCH & FILTER SECTION */
    .playlist-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }

    .playlist-title-area {
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .playlist-heading {
      font-size: 17px;
      font-weight: 800;
      color: var(--slate-900);
    }

    .playlist-count {
      font-size: 12px;
      font-weight: 600;
      color: var(--slate-500);
      background: var(--slate-100);
      padding: 2px 8px;
      border-radius: 10px;
    }

    .search-box-wrapper {
      flex: 1;
      max-width: 380px;
      min-width: 220px;
      position: relative;
    }

    .search-input {
      width: 100%;
      padding: 8px 12px 8px 36px;
      font-size: 13px;
      border-radius: 12px;
      border: 1.5px solid var(--slate-200);
      outline: none;
      transition: all 0.15s ease;
      background: #ffffff;
      color: var(--slate-800);
    }

    .search-input:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
    }

    .search-icon {
      position: absolute;
      left: 11px;
      top: 50%;
      transform: translateY(-50%);
      width: 15px;
      height: 15px;
      stroke: var(--slate-400);
      fill: none;
      stroke-width: 2;
      pointer-events: none;
    }

    /* PLAYLIST ITEMS */
    .playlist-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .subject-header-row {
      margin-top: 14px;
      margin-bottom: 4px;
      padding: 4px 8px;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--primary-hover);
      background: var(--primary-light);
      border-radius: 8px;
      border-left: 3px solid var(--primary);
    }

    .playlist-item {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 14px;
      border-radius: 12px;
      background: #ffffff;
      border: 1px solid var(--slate-100);
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
      overflow: hidden;
    }

    .playlist-item:hover {
      background: var(--slate-50);
      border-color: var(--slate-200);
      transform: translateX(2px);
    }

    .playlist-item.active {
      background: #f0f9ff;
      border-color: #bae6fd;
    }

    .playlist-item.active::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 4px;
      background: var(--primary);
    }

    .item-index {
      font-family: ui-monospace, SFMono-Regular, monospace;
      font-size: 12px;
      font-weight: 700;
      color: var(--slate-400);
      width: 32px;
      flex-shrink: 0;
    }

    .playlist-item.active .item-index {
      color: var(--primary);
      font-weight: 800;
    }

    .item-play-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #f1f5f9;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--slate-600);
      flex-shrink: 0;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .playlist-item:hover .item-play-btn {
      background: var(--primary);
      color: #ffffff;
      transform: scale(1.05);
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
      font-size: 14px;
      font-weight: 600;
      color: var(--slate-800);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 2px;
    }

    .playlist-item.active .item-title {
      color: var(--primary-hover);
      font-weight: 700;
    }

    .item-meta {
      font-size: 12px;
      color: var(--slate-500);
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .item-topic {
      color: #0369a1;
      font-weight: 600;
      background: #e0f2fe;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 11px;
    }

    .item-subject-badge {
      font-size: 10px;
      font-weight: 700;
      padding: 1px 5px;
      border-radius: 4px;
      text-transform: uppercase;
    }

    .badge-bio { background: #dcfce7; color: #15803d; }
    .badge-chem { background: #fee2e2; color: #b91c1c; }
    .badge-phys { background: #f3e8ff; color: #7e22ce; }

    .item-duration {
      font-family: ui-monospace, SFMono-Regular, monospace;
      font-size: 11px;
      font-weight: 600;
      color: var(--slate-400);
      margin-left: auto;
      flex-shrink: 0;
    }

    @media (max-width: 640px) {
      .player-card {
        padding: 16px;
      }
      .track-title {
        font-size: 16px;
      }
      .extra-controls {
        width: 100%;
        justify-content: space-between;
      }
      .volume-slider {
        width: 60px;
      }
    }
  </style>


  <!-- HERO AUDIO PLAYER -->
  <div class="player-card">
    <div class="player-top">
      <div class="cover-art">
        <svg viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z" /></svg>
        <div class="code">0654</div>
        <div class="sub">${isEn ? 'Science' : 'Khoa học'}</div>
      </div>
      <div class="track-info">
        <div class="track-badge">
          <div id="eq-dots" class="equalizer-dots paused">
            <span></span><span></span><span></span>
          </div>
          <span id="badge-status">PODCAST #<span id="current-ep-num">01</span> • <span id="current-code-tag">B1</span></span>
        </div>
        <h1 id="player-title" class="track-title">${isEn ? 'How MRS GREN Defines Life' : 'Bảy đặc điểm của sự sống'}</h1>
        <div id="player-sub" class="track-subtitle">${isEn ? 'Characteristics of living organisms • Cambridge IGCSE 0654 Co-ordinated Sciences' : 'Đặc điểm của các sinh vật sống • Cambridge IGCSE 0654 Co-ordinated Sciences'}</div>
      </div>
    </div>

    <!-- TIMELINE SCRUBBER -->
    <div class="timeline-container">
      <div id="progress-wrapper" class="progress-bar-wrapper">
        <div id="progress-fill" class="progress-bar-fill">
          <div class="progress-thumb"></div>
        </div>
      </div>
      <div class="time-row">
        <span id="time-current">00:00</span>
        <span id="time-total">--:--</span>
      </div>
    </div>

    <!-- CONTROLS -->
    <div class="controls-row">
      <div class="playback-buttons">
        <button id="btn-prev" class="btn-icon" title="${isEn ? 'Previous Episode (Shift + P)' : 'Tập trước (Shift + P)'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="19 20 9 12 19 4 19 20"></polygon><line x1="5" y1="19" x2="5" y2="5"></line></svg>
        </button>
        <button id="btn-back10" class="btn-icon btn-skip" title="${isEn ? 'Rewind 10s' : 'Lùi 10 giây'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M1 4v6h6"></path><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path></svg>
        </button>
        <button id="btn-play-pause" class="btn-play-main" title="${isEn ? 'Play / Pause (Space)' : 'Phát / Tạm dừng (Phím Space)'}">
          <svg id="icon-play" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          <svg id="icon-pause" style="display:none;" width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>
        </button>
        <button id="btn-fwd10" class="btn-icon btn-skip" title="${isEn ? 'Forward 10s' : 'Tua 10 giây'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M23 4v6h-6"></path><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path></svg>
        </button>
        <button id="btn-next" class="btn-icon" title="${isEn ? 'Next Episode (Shift + N)' : 'Tập tiếp theo (Shift + N)'}">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 4 15 12 5 20 5 4"></polygon><line x1="19" y1="5" x2="19" y2="19"></line></svg>
        </button>
      </div>

      <div class="extra-controls">
        <button id="btn-speed" class="btn-speed" title="${isEn ? 'Playback Speed' : 'Tốc độ phát'}">
          <span id="speed-label">1.0x</span>
        </button>
        <div class="volume-group">
          <button id="btn-mute" class="btn-icon" style="width:32px;height:32px;" title="${isEn ? 'Mute' : 'Tắt tiếng'}">
            <svg id="icon-vol" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
            <svg id="icon-mute" style="display:none;" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
          </button>
          <input id="volume-range" type="range" min="0" max="1" step="0.05" value="1" class="volume-slider" title="${isEn ? 'Volume' : 'Âm lượng'}">
        </div>
        <label class="auto-next-toggle" title="${isEn ? 'Auto play next episode' : 'Tự động chuyển bài khi kết thúc'}">
          <input id="auto-next-checkbox" type="checkbox" checked>
          <span>Auto-next</span>
        </label>
      </div>
    </div>
  </div>

  <!-- SECTION SELECTOR -->
  <div class="filter-section">
    <div class="section-select-wrapper">
      <select id="section-select" class="section-select">
        ${filterOptions}
      </select>
    </div>
  </div>

  <!-- SEARCH & PLAYLIST HEADER -->
  <div class="playlist-header">
    <div class="playlist-title-area">
      <h2 class="playlist-heading">${isEn ? 'Science Podcast Episodes' : 'Danh mục Podcast Ôn tập'}</h2>
      <span id="playlist-count" class="playlist-count">35 / 35</span>
    </div>
    <div class="search-box-wrapper">
      <svg class="search-icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <input id="search-input" type="text" class="search-input" placeholder="${isEn ? 'Search by title, topic, or code (B1, C2, P3)...' : 'Tìm kiếm theo tên bài, chủ đề, mã (B1, C2, P3)...'}">
    </div>
  </div>

  <!-- PLAYLIST CONTAINER -->
  <div id="playlist-list" class="playlist-list"></div>
</div>

<script>
window.switchLecturePage = function(targetPage) {
  var p = parseInt(targetPage, 10);
  if (isNaN(p)) return;

  try {
    if (window.parent) window.parent.postMessage({ type: 'LECTURE_SWITCH_PAGE', page: p }, '*');
  } catch(e) {}
  try {
    if (window.top && window.top !== window.parent) window.top.postMessage({ type: 'LECTURE_SWITCH_PAGE', page: p }, '*');
  } catch(e) {}

  try {
    var pDoc = (window.parent && window.parent.document) || (window.top && window.top.document);
    if (pDoc) {
      var btns = Array.from(pDoc.querySelectorAll('button'));
      var targetBtn = btns.find(function(b) {
        var txt = (b.textContent || '').trim();
        return txt === String(p) && (
          b.className.includes('rounded-lg') || 
          b.closest('.custom-scrollbar') || 
          b.closest('div[class*="overflow-x-auto"]')
        );
      });
      if (!targetBtn) {
        targetBtn = btns.find(function(b) {
          return (b.textContent || '').trim() === String(p);
        });
      }
      if (targetBtn) {
        targetBtn.click();
        try { window.parent.scrollTo({ top: 0, behavior: 'smooth' }); } catch(err) {}
      }
    }
  } catch(e) {}
};

(function() {
  try {
    document.querySelectorAll('.lang-pill.switch-btn').forEach(function(btn) {
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        var targetP = parseInt(btn.getAttribute('data-page'), 10);
        if (!isNaN(targetP)) window.switchLecturePage(targetP);
      });
    });
  } catch(e) {}

  const IS_EN = ${isEn ? 'true' : 'false'};
  const EPISODES = ${episodesJson};

  let currentIndex = 0;
  let isPlaying = false;
  let isMuted = false;
  let savedVolume = 1.0;
  const speedList = [1.0, 1.25, 1.5, 1.75, 2.0, 0.75];
  let currentSpeedIdx = 0;

  const storageKey = IS_EN ? 'tony_science_0654_podcast_en_idx' : 'tony_science_0654_podcast_vi_idx';
  try {
    const saved = localStorage.getItem(storageKey);
    if (saved !== null) {
      const parsed = parseInt(saved, 10);
      if (!isNaN(parsed) && parsed >= 0 && parsed < EPISODES.length) {
        currentIndex = parsed;
      }
    }
  } catch(e) {}

  const audio = new Audio();
  audio.preload = 'metadata';

  // DOM Elements
  const playerTitle = document.getElementById('player-title');
  const playerSub = document.getElementById('player-sub');
  const currentEpNum = document.getElementById('current-ep-num');
  const currentCodeTag = document.getElementById('current-code-tag');
  const progressWrapper = document.getElementById('progress-wrapper');
  const progressFill = document.getElementById('progress-fill');
  const timeCurrent = document.getElementById('time-current');
  const timeTotal = document.getElementById('time-total');
  const btnPlayPause = document.getElementById('btn-play-pause');
  const iconPlay = document.getElementById('icon-play');
  const iconPause = document.getElementById('icon-pause');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnBack10 = document.getElementById('btn-back10');
  const btnFwd10 = document.getElementById('btn-fwd10');
  const btnSpeed = document.getElementById('btn-speed');
  const speedLabel = document.getElementById('speed-label');
  const btnMute = document.getElementById('btn-mute');
  const iconVol = document.getElementById('icon-vol');
  const iconMute = document.getElementById('icon-mute');
  const volumeRange = document.getElementById('volume-range');
  const autoNextCheckbox = document.getElementById('auto-next-checkbox');
  const eqDots = document.getElementById('eq-dots');
  const searchInput = document.getElementById('search-input');
  const sectionSelect = document.getElementById('section-select');
  const playlistList = document.getElementById('playlist-list');
  const playlistCount = document.getElementById('playlist-count');

  function notifyHeight() {
    try {
      const appEl = document.getElementById('podcast-app');
      if (appEl && window.parent && window.parent !== window) {
        const height = Math.ceil(appEl.getBoundingClientRect().height);
        window.parent.postMessage({ type: 'LECTURE_RESIZE', height: height + 24 }, '*');
      }
    } catch(e) {}
  }

  function formatTime(secs) {
    if (isNaN(secs) || secs < 0) return '00:00';
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
  }

  function loadEpisode(index, autoPlay) {
    if (index < 0 || index >= EPISODES.length) return;
    currentIndex = index;
    try {
      localStorage.setItem(storageKey, currentIndex.toString());
    } catch(e) {}

    const ep = EPISODES[currentIndex];
    const epNumStr = ep.episode < 10 ? '0' + ep.episode : '' + ep.episode;

    currentEpNum.textContent = epNumStr;
    currentCodeTag.textContent = ep.code;
    playerTitle.textContent = IS_EN ? ep.titleEn : ep.titleVi;
    playerSub.textContent = IS_EN 
      ? (ep.topicEn + ' • Cambridge IGCSE 0654 Co-ordinated Sciences')
      : (ep.topicVi + ' • Cambridge IGCSE 0654 Co-ordinated Sciences');

    timeCurrent.textContent = '00:00';
    timeTotal.textContent = IS_EN ? ep.durationEnStr : ep.durationViStr;
    progressFill.style.width = '0%';

    const audioUrl = IS_EN ? ep.audioUrlEn : ep.audioUrlVi;
    audio.src = audioUrl;
    audio.playbackRate = speedList[currentSpeedIdx];

    updateActiveRow();

    if (autoPlay) {
      playAudio();
    } else {
      pauseAudio();
    }
  }

  function playAudio() {
    audio.play().then(() => {
      isPlaying = true;
      iconPlay.style.display = 'none';
      iconPause.style.display = 'block';
      eqDots.classList.remove('paused');
    }).catch(err => {
      console.warn('Play prevented:', err);
      pauseAudio();
    });
  }

  function pauseAudio() {
    audio.pause();
    isPlaying = false;
    iconPlay.style.display = 'block';
    iconPause.style.display = 'none';
    eqDots.classList.add('paused');
  }

  function togglePlayPause() {
    if (isPlaying) pauseAudio();
    else playAudio();
  }

  // Audio Event Listeners
  audio.addEventListener('timeupdate', () => {
    if (audio.duration) {
      const pct = (audio.currentTime / audio.duration) * 100;
      progressFill.style.width = pct + '%';
      timeCurrent.textContent = formatTime(audio.currentTime);
      timeTotal.textContent = formatTime(audio.duration);
    }
  });

  audio.addEventListener('loadedmetadata', () => {
    if (audio.duration) {
      timeTotal.textContent = formatTime(audio.duration);
    }
  });

  audio.addEventListener('ended', () => {
    if (autoNextCheckbox.checked) {
      if (currentIndex < EPISODES.length - 1) {
        loadEpisode(currentIndex + 1, true);
      } else {
        pauseAudio();
      }
    } else {
      pauseAudio();
    }
  });

  // UI Event Listeners
  btnPlayPause.addEventListener('click', togglePlayPause);

  btnPrev.addEventListener('click', () => {
    if (audio.currentTime > 3) {
      audio.currentTime = 0;
    } else if (currentIndex > 0) {
      loadEpisode(currentIndex - 1, isPlaying);
    }
  });

  btnNext.addEventListener('click', () => {
    if (currentIndex < EPISODES.length - 1) {
      loadEpisode(currentIndex + 1, isPlaying);
    }
  });

  btnBack10.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 10);
  });

  btnFwd10.addEventListener('click', () => {
    if (audio.duration) {
      audio.currentTime = Math.min(audio.duration, audio.currentTime + 10);
    }
  });

  btnSpeed.addEventListener('click', () => {
    currentSpeedIdx = (currentSpeedIdx + 1) % speedList.length;
    const spd = speedList[currentSpeedIdx];
    audio.playbackRate = spd;
    speedLabel.textContent = spd.toFixed(spd % 1 === 0 ? 1 : 2) + 'x';
  });

  btnMute.addEventListener('click', () => {
    isMuted = !isMuted;
    audio.muted = isMuted;
    if (isMuted) {
      iconVol.style.display = 'none';
      iconMute.style.display = 'block';
    } else {
      iconVol.style.display = 'block';
      iconMute.style.display = 'none';
    }
  });

  volumeRange.addEventListener('input', (e) => {
    const v = parseFloat(e.target.value);
    audio.volume = v;
    if (v === 0) {
      audio.muted = true;
      iconVol.style.display = 'none';
      iconMute.style.display = 'block';
    } else {
      audio.muted = false;
      iconVol.style.display = 'block';
      iconMute.style.display = 'none';
    }
  });

  progressWrapper.addEventListener('click', (e) => {
    const rect = progressWrapper.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const ratio = Math.max(0, Math.min(1, clickX / rect.width));
    if (audio.duration) {
      audio.currentTime = ratio * audio.duration;
    }
  });

  // Keyboard Shortcuts
  document.addEventListener('keydown', (e) => {
    if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT')) return;
    if (e.code === 'Space') {
      e.preventDefault();
      togglePlayPause();
    } else if (e.code === 'ArrowLeft') {
      audio.currentTime = Math.max(0, audio.currentTime - 5);
    } else if (e.code === 'ArrowRight') {
      if (audio.duration) audio.currentTime = Math.min(audio.duration, audio.currentTime + 5);
    } else if (e.shiftKey && e.code === 'KeyN') {
      if (currentIndex < EPISODES.length - 1) loadEpisode(currentIndex + 1, isPlaying);
    } else if (e.shiftKey && e.code === 'KeyP') {
      if (currentIndex > 0) loadEpisode(currentIndex - 1, isPlaying);
    }
  });

  // Filter & Search
  sectionSelect.addEventListener('change', renderPlaylist);
  searchInput.addEventListener('input', renderPlaylist);

  function getBadgeClass(subject) {
    if (subject === 'Biology') return 'badge-bio';
    if (subject === 'Chemistry') return 'badge-chem';
    return 'badge-phys';
  }

  function getSubjectName(subject) {
    if (IS_EN) return subject;
    if (subject === 'Biology') return 'Sinh học';
    if (subject === 'Chemistry') return 'Hóa học';
    return 'Vật lý';
  }

  function renderPlaylist() {
    const selectedSub = sectionSelect.value;
    const query = (searchInput.value || '').trim().toLowerCase();

    const filtered = EPISODES.filter((ep, idx) => {
      if (selectedSub !== 'ALL' && ep.subject !== selectedSub) return false;
      if (!query) return true;

      const title = (IS_EN ? ep.titleEn : ep.titleVi).toLowerCase();
      const topic = (IS_EN ? ep.topicEn : ep.topicVi).toLowerCase();
      const code = ep.code.toLowerCase();
      const epNum = '#' + ep.episode;
      const epNum2 = '#' + (ep.episode < 10 ? '0' + ep.episode : ep.episode);

      return title.includes(query) || topic.includes(query) || code.includes(query) || epNum.includes(query) || epNum2.includes(query);
    });

    playlistCount.textContent = filtered.length + ' / ' + EPISODES.length;

    if (filtered.length === 0) {
      playlistList.innerHTML = '<div style="text-align:center;padding:36px;color:#64748b;font-weight:600;">' +
        (IS_EN ? 'No podcast episodes found matching your filter.' : 'Không tìm thấy tập podcast nào phù hợp.') +
        '</div>';
      notifyHeight();
      return;
    }

    let html = '';
    let lastSubject = null;

    filtered.forEach(ep => {
      if (selectedSub === 'ALL' && ep.subject !== lastSubject) {
        lastSubject = ep.subject;
        html += '<div class="subject-header-row">' +
          (ep.subject === 'Biology' ? '🧬 ' : ep.subject === 'Chemistry' ? '🧪 ' : '⚡ ') +
          getSubjectName(ep.subject) + ' (' + (ep.subject === 'Biology' ? 'B1 - B13' : ep.subject === 'Chemistry' ? 'C1 - C14' : 'P1 - P8') + ')' +
          '</div>';
      }

      const idx = ep.episode - 1;
      const isActive = idx === currentIndex;
      const durationStr = IS_EN ? ep.durationEnStr : ep.durationViStr;
      const title = IS_EN ? ep.titleEn : ep.titleVi;
      const topic = IS_EN ? ep.topicEn : ep.topicVi;
      const badgeCls = getBadgeClass(ep.subject);

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
            '<span class="item-topic">' + topic + '</span>' +
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

module.exports = { generateSciencePodcastPlayerHtml };
