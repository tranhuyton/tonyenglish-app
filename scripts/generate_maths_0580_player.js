/**
 * Generator for Cambridge IGCSE Mathematics (0580) Bilingual Podcast Player + Year End Revision HTML
 * Supports both in-player language toggle (VI / EN) and Page 1 (VI) / Page 2 (EN)
 */

function generateMathsPodcastAndRevisionHtml(episodes, defaultLang = 'vi') {
  const payloadJson = JSON.stringify(episodes).replace(/</g, '\\u003c');
  const initialLang = defaultLang === 'en' ? 'en' : 'vi';

  return `
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<div class="maths-podcast-wrapper">
  <style>
    .maths-podcast-wrapper {
      --math-primary: #1d4ed8;
      --math-primary-hover: #1e40af;
      --math-secondary: #2563eb;
      --math-accent: #3b82f6;
      --math-dark: #1e3a8a;
      --slate-50: #f8fafc;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --slate-600: #475569;
      --slate-700: #334155;
      --slate-800: #1e293b;
      --slate-900: #0f172a;
      max-width: 980px;
      margin: 0 auto 36px;
      padding: 8px 16px 24px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: var(--slate-800);
    }

    .maths-podcast-wrapper * {
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
    }

    /* SECTION HEADER & LANGUAGE SWITCHER */
    .mp-header-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 2px solid #dbeafe;
    }

    .mp-header-title-group {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .mp-header-title {
      font-size: 22px;
      font-weight: 800;
      color: #1e3a8a;
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 0;
    }

    .mp-header-sub {
      font-size: 13.5px;
      color: var(--slate-500);
      font-weight: 500;
      margin: 0;
    }

    .mp-lang-switcher {
      display: inline-flex;
      background: #f1f5f9;
      padding: 4px;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
      gap: 4px;
    }

    .mp-lang-btn {
      border: none;
      background: transparent;
      padding: 7px 14px;
      border-radius: 9px;
      font-size: 13px;
      font-weight: 700;
      color: var(--slate-600);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .mp-lang-btn:hover {
      color: var(--slate-900);
    }

    .mp-lang-btn.active {
      background: #1d4ed8;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(29, 78, 216, 0.28);
    }

    /* HERO PLAYER CARD */
    .mp-player-card {
      background: linear-gradient(135deg, #1e3a8a 0%, #1d4ed8 55%, #2563eb 100%);
      color: #ffffff;
      border-radius: 24px;
      padding: 24px 28px;
      box-shadow: 0 16px 36px -8px rgba(30, 58, 138, 0.42), 0 0 0 1px rgba(255, 255, 255, 0.12) inset;
      margin-bottom: 22px;
      position: sticky;
      top: 12px;
      z-index: 40;
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .mp-player-top {
      display: flex;
      align-items: center;
      gap: 20px;
      margin-bottom: 18px;
    }

    .mp-cover-art {
      width: 78px;
      height: 78px;
      border-radius: 18px;
      background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      position: relative;
      overflow: hidden;
      border: 2px solid rgba(255, 255, 255, 0.22);
    }

    .mp-cover-art::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.32), transparent 70%);
    }

    .mp-cover-icon {
      width: 38px;
      height: 38px;
      color: #ffffff;
      position: relative;
      z-index: 2;
    }

    .mp-meta-box {
      flex: 1;
      min-width: 0;
    }

    .mp-meta-badge-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
      flex-wrap: wrap;
    }

    .mp-meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 3px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.28);
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .mp-meta-badge .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #93c5fd;
      box-shadow: 0 0 8px #93c5fd;
    }

    .mp-current-title {
      font-size: 19px;
      font-weight: 800;
      line-height: 1.3;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 4px;
    }

    .mp-current-sub {
      font-size: 13px;
      color: rgba(255, 255, 255, 0.86);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      font-weight: 400;
    }

    /* SCRUBBER */
    .mp-scrubber-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
    }

    .mp-time-stamp {
      font-size: 12px;
      font-variant-numeric: tabular-nums;
      color: rgba(255, 255, 255, 0.88);
      font-weight: 600;
      width: 44px;
    }
    .mp-time-stamp.right {
      text-align: right;
    }

    .mp-scrubber-container {
      flex: 1;
      position: relative;
      height: 20px;
      display: flex;
      align-items: center;
      cursor: pointer;
    }

    .mp-scrubber-track {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.24);
      position: relative;
      overflow: hidden;
    }

    .mp-scrubber-buffer {
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 0%;
      background: rgba(255, 255, 255, 0.36);
      border-radius: 999px;
      transition: width 0.2s ease;
    }

    .mp-scrubber-fill {
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 0%;
      background: #ffffff;
      border-radius: 999px;
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
    }

    .mp-scrubber-thumb {
      position: absolute;
      left: 0%;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
      transform: translateX(-50%);
      pointer-events: none;
      transition: transform 0.1s ease;
    }

    .mp-scrubber-container:hover .mp-scrubber-thumb {
      transform: translateX(-50%) scale(1.25);
    }

    /* CONTROLS */
    .mp-controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .mp-controls-left,
    .mp-controls-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .mp-controls-center {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .mp-ctrl-btn {
      background: transparent;
      border: none;
      color: rgba(255, 255, 255, 0.88);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      width: 36px;
      height: 36px;
      transition: all 0.2s;
    }

    .mp-ctrl-btn:hover {
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      transform: scale(1.06);
    }

    .mp-play-btn {
      width: 48px;
      height: 48px;
      background: #ffffff;
      color: var(--math-primary);
      border-radius: 50%;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .mp-play-btn:hover {
      transform: scale(1.08);
      box-shadow: 0 8px 22px rgba(255, 255, 255, 0.4);
    }

    .mp-speed-btn {
      background: rgba(255, 255, 255, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.28);
      color: #ffffff;
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }

    .mp-speed-btn:hover {
      background: rgba(255, 255, 255, 0.28);
    }

    /* SEARCH & FILTER */
    .mp-filter-bar {
      margin-bottom: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .mp-search-box {
      position: relative;
      width: 100%;
    }

    .mp-search-input {
      width: 100%;
      padding: 11px 14px 11px 40px;
      border-radius: 12px;
      border: 1.5px solid var(--slate-200);
      background: #ffffff;
      font-size: 13.5px;
      color: var(--slate-800);
      outline: none;
      transition: all 0.2s;
    }

    .mp-search-input:focus {
      border-color: var(--math-primary);
      box-shadow: 0 0 0 3px rgba(29, 78, 216, 0.1);
    }

    .mp-search-icon {
      position: absolute;
      left: 13px;
      top: 50%;
      transform: translateY(-50%);
      width: 16px;
      height: 16px;
      color: var(--slate-400);
      pointer-events: none;
    }

    /* EPISODE LIST */
    .mp-episodes-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .mp-episode-card {
      background: #ffffff;
      border: 1.5px solid var(--slate-200);
      border-radius: 14px;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .mp-episode-card:hover {
      border-color: var(--math-accent);
      background: #f8fafc;
      transform: translateY(-1px);
      box-shadow: 0 6px 16px -4px rgba(29, 78, 216, 0.1);
    }

    .mp-episode-card.active {
      background: #eff6ff;
      border-color: var(--math-primary);
      box-shadow: 0 6px 20px -4px rgba(29, 78, 216, 0.16);
    }

    .mp-ep-num {
      width: 40px;
      height: 40px;
      border-radius: 11px;
      background: var(--slate-100);
      color: var(--slate-700);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 14px;
      flex-shrink: 0;
      border: 1px solid var(--slate-200);
      transition: all 0.2s;
    }

    .mp-episode-card.active .mp-ep-num {
      background: var(--math-primary);
      color: #ffffff;
      border-color: var(--math-primary);
    }

    .mp-ep-main {
      flex: 1;
      min-width: 0;
    }

    .mp-ep-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--slate-900);
      margin-bottom: 3px;
      line-height: 1.35;
    }

    .mp-episode-card.active .mp-ep-title {
      color: var(--math-dark);
    }

    .mp-ep-desc {
      font-size: 12.5px;
      color: var(--slate-500);
      line-height: 1.45;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .mp-ep-right {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }

    .mp-ep-duration {
      font-size: 12px;
      font-weight: 600;
      color: var(--slate-500);
      font-variant-numeric: tabular-nums;
    }

    .mp-card-play-icon {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--slate-100);
      color: var(--slate-700);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .mp-episode-card:hover .mp-card-play-icon {
      background: #dbeafe;
      color: var(--math-primary);
    }

    .mp-episode-card.active .mp-card-play-icon {
      background: var(--math-primary);
      color: #ffffff;
    }

    @media (max-width: 640px) {
      .mp-player-card {
        padding: 18px 16px;
        border-radius: 18px;
      }
      .mp-cover-art {
        width: 60px;
        height: 60px;
      }
      .mp-current-title {
        font-size: 16px;
      }
      .mp-episode-card {
        padding: 12px 12px;
      }
    }
  </style>

  <!-- HEADER & IN-PLAYER LANGUAGE SWITCHER -->
  <div class="mp-header-bar">
    <div class="mp-header-title-group">
      <h3 class="mp-header-title">
        <span>🎧</span>
        <span id="mpHeaderTitleText">${initialLang === 'en' ? 'IGCSE Mathematics (0580) Revision Podcast' : 'Podcast Ôn Tập IGCSE Mathematics (0580)'}</span>
      </h3>
      <p class="mp-header-sub" id="mpHeaderSubText">
        ${initialLang === 'en'
          ? 'Comprehensive audio revision across all 9 syllabus topics (Core & Extended)'
          : 'Hệ thống 9 bài giảng âm thanh tổng ôn toàn bộ 9 chủ đề trọng tâm Toán IGCSE 0580'}
      </p>
    </div>

    <div class="mp-lang-switcher">
      <button type="button" class="mp-lang-btn ${initialLang === 'vi' ? 'active' : ''}" id="mpLangBtnVi" data-lang="vi">
        <span>🇻🇳</span>
        <span>Tiếng Việt</span>
      </button>
      <button type="button" class="mp-lang-btn ${initialLang === 'en' ? 'active' : ''}" id="mpLangBtnEn" data-lang="en">
        <span>🇬🇧</span>
        <span>English</span>
      </button>
    </div>
  </div>

  <!-- STICKY HERO PLAYER -->
  <div class="mp-player-card">
    <div class="mp-player-top">
      <div class="mp-cover-art">
        <svg class="mp-cover-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 2L2 7l10 5 10-5-10-5z"/>
          <path d="M2 17l10 5 10-5"/>
          <path d="M2 12l10 5 10-5"/>
        </svg>
      </div>
      <div class="mp-meta-box">
        <div class="mp-meta-badge-row">
          <span class="mp-meta-badge">
            <span class="dot"></span>
            <span id="mpGroupBadge">IGCSE MATHS 0580</span>
          </span>
        </div>
        <div class="mp-current-title" id="mpCurrentTitle">Topic 1: Number</div>
        <div class="mp-current-sub" id="mpCurrentSyllabus">Loading...</div>
      </div>
    </div>

    <div class="mp-scrubber-row">
      <span class="mp-time-stamp" id="mpCurTime">0:00</span>
      <div class="mp-scrubber-container" id="mpScrubberContainer">
        <div class="mp-scrubber-track">
          <div class="mp-scrubber-buffer" id="mpScrubberBuffer"></div>
          <div class="mp-scrubber-fill" id="mpScrubberFill"></div>
        </div>
        <div class="mp-scrubber-thumb" id="mpScrubberThumb"></div>
      </div>
      <span class="mp-time-stamp right" id="mpTotalTime">0:00</span>
    </div>

    <div class="mp-controls-row">
      <div class="mp-controls-left">
        <button type="button" class="mp-speed-btn" id="mpSpeedBtn" title="Playback Speed">1.0x</button>
      </div>

      <div class="mp-controls-center">
        <button type="button" class="mp-ctrl-btn" id="mpPrevBtn" title="Previous Episode">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 6h2v12H6zm3.5 6l8.5 6V6z"/>
          </svg>
        </button>

        <button type="button" class="mp-ctrl-btn" id="mpRewindBtn" title="Rewind 10s">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z"/>
          </svg>
        </button>

        <button type="button" class="mp-play-btn" id="mpPlayBtn" title="Play/Pause">
          <svg id="mpPlayIcon" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M8 5v14l11-7z"/>
          </svg>
          <svg id="mpPauseIcon" style="display:none;" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
          </svg>
        </button>

        <button type="button" class="mp-ctrl-btn" id="mpForwardBtn" title="Forward 10s">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 5V1l5 5-5 5V7c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6h2c0 4.42-3.58 8-8 8s-8-3.58-8-8 3.58-8 8-8z"/>
          </svg>
        </button>

        <button type="button" class="mp-ctrl-btn" id="mpNextBtn" title="Next Episode">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z"/>
          </svg>
        </button>
      </div>

      <div class="mp-controls-right">
        <button type="button" class="mp-ctrl-btn" id="mpMuteBtn" title="Mute/Unmute">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
        </button>
      </div>
    </div>

    <audio id="mpNativeAudio" preload="metadata"></audio>
  </div>

  <!-- SEARCH BAR -->
  <div class="mp-filter-bar">
    <div class="mp-search-box">
      <svg class="mp-search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input type="text" class="mp-search-input" id="mpSearchInput" placeholder="${initialLang === 'en' ? 'Search topic, formula, keywords...' : 'Tìm kiếm chủ đề Toán, công thức, từ khóa...'}">
    </div>
  </div>

  <!-- EPISODES LIST -->
  <div class="mp-episodes-list" id="mpEpisodesList"></div>
</div>

<!-- YEAR END REVISION PAST PAPERS SECTION -->
<style>
  .course-wrapper {
      font-family: 'Nunito', sans-serif; 
      background-color: #ffffff; 
      color: #334155; 
      display: flex; 
      flex-direction: column; 
      align-items: center; 
      padding: 0; 
      width: 100%;
  }
  .course-wrapper .slide { 
      width: 100%; 
      max-width: 980px; 
      background-color: #ffffff; 
      border-radius: 16px; 
      border: 1px solid #e2e8f0;
      position: relative; 
      padding: 40px 32px; 
      margin-top: 8px;
  }
  .course-wrapper .slide-math::before { 
      content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 8px; 
      background: linear-gradient(90deg, #1e40af, #3b82f6, #60a5fa); 
      border-radius: 16px 16px 0 0;
  }
  .course-wrapper h2 { font-size: 22px; font-weight: 700; margin-bottom: 18px; border-bottom: 2px solid #dbeafe; padding-bottom: 10px; color: #1d4ed8; margin-top: 32px;}
  .course-wrapper p.subtitle { font-size: 17px; color: #64748b; font-weight: 600; margin-bottom: 20px; }
  .course-wrapper .grid-papers { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 14px; margin-top: 14px; }
  .course-wrapper .paper-btn { 
      display: flex; align-items: center; padding: 15px 18px;
      background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px;
      color: #1e293b; font-weight: 700; text-decoration: none; transition: all 0.2s;
      font-size: 14px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  }
  .course-wrapper .paper-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 15px -3px rgba(0,0,0,0.1); }
  .course-wrapper .icon { font-size: 20px; margin-right: 12px; }
  .course-wrapper .paper-btn.p2 { background: #fff7ed; border-color: #ffedd5; color: #c2410c; }
  .course-wrapper .paper-btn.p2:hover { background: #ffedd5; border-color: #fdba74; }
  .course-wrapper .paper-btn.p4 { background: #fdf4ff; border-color: #fae8ff; color: #a21caf; }
  .course-wrapper .paper-btn.p4:hover { background: #fae8ff; border-color: #f5d0fe; }
  .course-wrapper .paper-btn.collection { background: #f0fdf4; border-color: #dcfce7; color: #15803d; }
  .course-wrapper .paper-btn.collection:hover { background: #dcfce7; border-color: #bbf7d0; }
  @media (max-width: 768px) {
      .course-wrapper .slide { padding: 28px 18px; }
  }
</style>

<div class="course-wrapper">
    <div class="slide slide-math">
        <p class="subtitle">Tổng hợp đề thi cũ và bài tập thực hành (Past Papers Practice)</p>
        
        <h2 style="margin-top: 10px;">📝 Solved Paper 2 Samples</h2>
        <div class="grid-papers">
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P22-MAY-2018-IGCSE%20MATH-SOLVED/res/index.html" class="paper-btn p2" target="_blank">
                <span class="icon">📄</span> 0580-P22-MAY-2018 (Solved)
            </a>
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P22-MAY-2019-IGCSE%20MATH-SOLVED/res/index.html" class="paper-btn p2" target="_blank">
                <span class="icon">📄</span> 0580-P22-MAY-2019 (Solved)
            </a>
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P22-NOV-2017-IGCSE%20MATH-SOLVED/res/index.html" class="paper-btn p2" target="_blank">
                <span class="icon">📄</span> 0580-P22-NOV-2017 (Solved)
            </a>
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P22-NOV-2018-IGCSE%20MATH-SOLVED/res/index.html" class="paper-btn p2" target="_blank">
                <span class="icon">📄</span> 0580-P22-NOV-2018 (Solved)
            </a>
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P23-MAY-2019-IGCSE-MATH-SOLVED/res/index.html" class="paper-btn p2" target="_blank">
                <span class="icon">📄</span> 0580-P23-MAY-2019 (Solved)
            </a>
        </div>
        
        <h2>📝 Solved Paper 4 Samples</h2>
        <div class="grid-papers">
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P41-MAY-2018-IGCSE%20MATH%20SOLVED/res/index.html" class="paper-btn p4" target="_blank">
                <span class="icon">📄</span> 0580-P41-MAY-2018 (Solved)
            </a>
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P42-NOV-2017-IGCSE%20MATH-SOLVED/res/index.html" class="paper-btn p4" target="_blank">
                <span class="icon">📄</span> 0580-P42-NOV-2017 (Solved)
            </a>
            <a href="https://tonyenglish.vn/uploads/FlashQuiz/2024/1031/0580-P42-NOV-2018-IGCSE%20MATH-SOLVED/res/index.html" class="paper-btn p4" target="_blank">
                <span class="icon">📄</span> 0580-P42-NOV-2018 (Solved)
            </a>
        </div>
        
        <h2>📚 Past Paper Collection (2002 - 2025)</h2>
        <div class="grid-papers">
            <a href="https://drive.google.com/drive/folders/1GZUs34yS5dMmhO8Pm8rWokkS7VBQ5bqF" class="paper-btn collection" target="_blank">
                <span class="icon">📁</span> Mở thư mục Google Drive
            </a>
        </div>
    </div>
</div>

<script>
(function() {
  const RAW_EPISODES = ${payloadJson};
  let currentLang = '${initialLang}';
  let currentIndex = 0;
  let isPlaying = false;
  let searchTerm = '';

  const audio = document.getElementById('mpNativeAudio');
  const playBtn = document.getElementById('mpPlayBtn');
  const playIcon = document.getElementById('mpPlayIcon');
  const pauseIcon = document.getElementById('mpPauseIcon');
  const prevBtn = document.getElementById('mpPrevBtn');
  const nextBtn = document.getElementById('mpNextBtn');
  const rewindBtn = document.getElementById('mpRewindBtn');
  const forwardBtn = document.getElementById('mpForwardBtn');
  const speedBtn = document.getElementById('mpSpeedBtn');
  const muteBtn = document.getElementById('mpMuteBtn');

  const curTitleEl = document.getElementById('mpCurrentTitle');
  const curSyllabusEl = document.getElementById('mpCurrentSyllabus');
  const groupBadgeEl = document.getElementById('mpGroupBadge');
  const curTimeEl = document.getElementById('mpCurTime');
  const totalTimeEl = document.getElementById('mpTotalTime');

  const scrubberContainer = document.getElementById('mpScrubberContainer');
  const scrubberFill = document.getElementById('mpScrubberFill');
  const scrubberThumb = document.getElementById('mpScrubberThumb');
  const scrubberBuffer = document.getElementById('mpScrubberBuffer');

  const searchInput = document.getElementById('mpSearchInput');
  const epListEl = document.getElementById('mpEpisodesList');
  const headerTitleText = document.getElementById('mpHeaderTitleText');
  const headerSubText = document.getElementById('mpHeaderSubText');
  const langBtnVi = document.getElementById('mpLangBtnVi');
  const langBtnEn = document.getElementById('mpLangBtnEn');

  const speeds = [1.0, 1.25, 1.5, 1.75, 2.0];
  let curSpeedIdx = 0;

  function getEpView(ep) {
    const isEn = currentLang === 'en';
    return {
      episode: ep.episode,
      code: ep.code,
      group: isEn ? ep.group : ep.groupVi,
      title: isEn ? ep.titleEn : ep.titleVi,
      syllabus: isEn ? ep.syllabusTitle : ep.syllabusTitleVi,
      audioUrl: isEn ? ep.audioUrlEn : ep.audioUrlVi,
      durationSec: isEn ? ep.durationEnSec : ep.durationViSec,
      durationStr: isEn ? ep.durationEnStr : ep.durationViStr
    };
  }

  function formatTime(sec) {
    if (isNaN(sec) || !isFinite(sec)) return "0:00";
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return m + ":" + (s < 10 ? "0" : "") + s;
  }

  function updateHeaderLangUI() {
    const isEn = currentLang === 'en';
    headerTitleText.textContent = isEn
      ? 'IGCSE Mathematics (0580) Revision Podcast'
      : 'Podcast Ôn Tập IGCSE Mathematics (0580)';
    headerSubText.textContent = isEn
      ? 'Comprehensive audio revision across all 9 syllabus topics (Core & Extended)'
      : 'Hệ thống 9 bài giảng âm thanh tổng ôn toàn bộ 9 chủ đề trọng tâm Toán IGCSE 0580';
    searchInput.placeholder = isEn
      ? 'Search topic, formula, keywords...'
      : 'Tìm kiếm chủ đề Toán, công thức, từ khóa...';

    if (isEn) {
      langBtnEn.classList.add('active');
      langBtnVi.classList.remove('active');
    } else {
      langBtnVi.classList.add('active');
      langBtnEn.classList.remove('active');
    }
  }

  function loadEpisode(index, autoPlay = true) {
    if (index < 0 || index >= RAW_EPISODES.length) return;
    currentIndex = index;
    const ep = getEpView(RAW_EPISODES[currentIndex]);

    curTitleEl.textContent = ep.title;
    curSyllabusEl.textContent = ep.syllabus;
    groupBadgeEl.textContent = (ep.group || 'IGCSE MATHS 0580') + (currentLang === 'en' ? ' • EN' : ' • VI');

    audio.src = ep.audioUrl;
    audio.playbackRate = speeds[curSpeedIdx];
    curTimeEl.textContent = "0:00";
    totalTimeEl.textContent = ep.durationStr || formatTime(ep.durationSec);
    updateScrubber(0);

    renderList();

    if (autoPlay) {
      audio.play().then(() => {
        isPlaying = true;
        updatePlayState();
      }).catch(err => {
        console.warn('Autoplay prevented:', err);
      });
    } else {
      isPlaying = false;
      updatePlayState();
    }

    try {
      localStorage.setItem('tony_maths_0580_last_ep', ep.episode);
    } catch(e) {}
  }

  function updatePlayState() {
    if (isPlaying) {
      playIcon.style.display = 'none';
      pauseIcon.style.display = 'block';
    } else {
      playIcon.style.display = 'block';
      pauseIcon.style.display = 'none';
    }

    document.querySelectorAll('.mp-episode-card').forEach(card => {
      const epIdx = parseInt(card.getAttribute('data-index'), 10);
      if (epIdx === currentIndex) {
        card.classList.add('active');
      } else {
        card.classList.remove('active');
      }
    });
  }

  function togglePlay() {
    if (!audio.src) {
      loadEpisode(currentIndex, true);
      return;
    }
    if (audio.paused) {
      audio.play().then(() => {
        isPlaying = true;
        updatePlayState();
      });
    } else {
      audio.pause();
      isPlaying = false;
      updatePlayState();
    }
  }

  function updateScrubber(percent) {
    const p = Math.max(0, Math.min(100, percent));
    scrubberFill.style.width = p + '%';
    scrubberThumb.style.left = p + '%';
  }

  audio.addEventListener('timeupdate', () => {
    if (!audio.duration) return;
    curTimeEl.textContent = formatTime(audio.currentTime);
    updateScrubber((audio.currentTime / audio.duration) * 100);
  });

  audio.addEventListener('progress', () => {
    if (!audio.duration || audio.buffered.length === 0) return;
    const bufferedEnd = audio.buffered.end(audio.buffered.length - 1);
    scrubberBuffer.style.width = ((bufferedEnd / audio.duration) * 100) + '%';
  });

  audio.addEventListener('ended', () => {
    if (currentIndex < RAW_EPISODES.length - 1) {
      loadEpisode(currentIndex + 1, true);
    } else {
      isPlaying = false;
      updatePlayState();
    }
  });

  audio.addEventListener('play', () => { isPlaying = true; updatePlayState(); });
  audio.addEventListener('pause', () => { isPlaying = false; updatePlayState(); });

  playBtn.addEventListener('click', togglePlay);
  prevBtn.addEventListener('click', () => {
    if (audio.currentTime > 5) audio.currentTime = 0;
    else if (currentIndex > 0) loadEpisode(currentIndex - 1, true);
  });
  nextBtn.addEventListener('click', () => {
    if (currentIndex < RAW_EPISODES.length - 1) loadEpisode(currentIndex + 1, true);
  });
  rewindBtn.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 10);
  });
  forwardBtn.addEventListener('click', () => {
    audio.currentTime = Math.min(audio.duration || Infinity, audio.currentTime + 10);
  });
  speedBtn.addEventListener('click', () => {
    curSpeedIdx = (curSpeedIdx + 1) % speeds.length;
    const sp = speeds[curSpeedIdx];
    audio.playbackRate = sp;
    speedBtn.textContent = sp.toFixed(2).replace(/\\.00$/, '.0').replace(/0$/, '') + 'x';
  });
  muteBtn.addEventListener('click', () => {
    audio.muted = !audio.muted;
    muteBtn.style.opacity = audio.muted ? '0.4' : '1';
  });

  let isDragging = false;
  function seekFromEvent(e) {
    const rect = scrubberContainer.getBoundingClientRect();
    const x = Math.max(0, Math.min(e.clientX - rect.left, rect.width));
    const pct = x / rect.width;
    updateScrubber(pct * 100);
    if (audio.duration) audio.currentTime = pct * audio.duration;
  }
  scrubberContainer.addEventListener('mousedown', (e) => { isDragging = true; seekFromEvent(e); });
  window.addEventListener('mousemove', (e) => { if (isDragging) seekFromEvent(e); });
  window.addEventListener('mouseup', () => { isDragging = false; });

  function renderList() {
    const term = searchTerm.toLowerCase();
    const filtered = RAW_EPISODES.map((raw, idx) => ({ ...getEpView(raw), originalIndex: idx })).filter(ep => {
      if (!term) return true;
      return (ep.title || '').toLowerCase().includes(term) ||
             (ep.syllabus || '').toLowerCase().includes(term) ||
             (ep.code || '').toLowerCase().includes(term);
    });

    if (filtered.length === 0) {
      epListEl.innerHTML = \`
        <div style="text-align: center; padding: 36px 16px; color: var(--slate-500); font-size: 14px;">
          \${currentLang === 'en' ? 'No matching topics found.' : 'Không tìm thấy chủ đề phù hợp.'}
        </div>
      \`;
      return;
    }

    epListEl.innerHTML = filtered.map(ep => {
      const isActive = ep.originalIndex === currentIndex;
      return \`
        <div class="mp-episode-card \${isActive ? 'active' : ''}" data-index="\${ep.originalIndex}">
          <div class="mp-ep-num">\${ep.code}</div>
          <div class="mp-ep-main">
            <div class="mp-ep-title">\${ep.title}</div>
            <div class="mp-ep-desc">\${ep.syllabus}</div>
          </div>
          <div class="mp-ep-right">
            <span class="mp-ep-duration">\${ep.durationStr}</span>
            <div class="mp-card-play-icon">
              \${isActive && isPlaying ? \`
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
                </svg>
              \` : \`
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M8 5v14l11-7z"/>
                </svg>
              \`}
            </div>
          </div>
        </div>
      \`;
    }).join('');

    document.querySelectorAll('.mp-episode-card').forEach(card => {
      card.addEventListener('click', () => {
        const idx = parseInt(card.getAttribute('data-index'), 10);
        if (idx === currentIndex) togglePlay();
        else loadEpisode(idx, true);
      });
    });
  }

  function switchLanguage(newLang) {
    if (newLang === currentLang) return;
    const wasPlaying = !audio.paused;
    currentLang = newLang;
    updateHeaderLangUI();
    loadEpisode(currentIndex, wasPlaying);
  }

  langBtnVi.addEventListener('click', () => switchLanguage('vi'));
  langBtnEn.addEventListener('click', () => switchLanguage('en'));

  searchInput.addEventListener('input', (e) => {
    searchTerm = e.target.value.trim();
    renderList();
  });

  let initialEpIdx = 0;
  try {
    const saved = parseInt(localStorage.getItem('tony_maths_0580_last_ep'), 10);
    if (!isNaN(saved)) {
      const foundIdx = RAW_EPISODES.findIndex(e => e.episode === saved);
      if (foundIdx !== -1) initialEpIdx = foundIdx;
    }
  } catch(e) {}

  updateHeaderLangUI();
  loadEpisode(initialEpIdx, false);
})();
</script>
  `;
}

module.exports = {
  generateMathsPodcastAndRevisionHtml
};
