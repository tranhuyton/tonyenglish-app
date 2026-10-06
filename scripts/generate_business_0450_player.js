/**
 * Generator for Cambridge IGCSE Business Studies (0450) Bilingual Podcast Player HTML
 * Supports Vietnamese (Page 1) and English (Page 2)
 */

function generateBusinessPodcastPlayerHtml(episodes, lang = 'vi') {
  const isEn = lang === 'en';

  const sections = [
    { id: 1, nameEn: "Section 1: Understanding business activity", nameVi: "Phần 1: Hiểu về hoạt động kinh doanh", color: "#0ea5e9" },
    { id: 2, nameEn: "Section 2: People in business", nameVi: "Phần 2: Con người trong doanh nghiệp", color: "#f43f5e" },
    { id: 3, nameEn: "Section 3: Marketing", nameVi: "Phần 3: Marketing", color: "#f97316" },
    { id: 4, nameEn: "Section 4: Operations management", nameVi: "Phần 4: Quản trị vận hành", color: "#8b5cf6" },
    { id: 5, nameEn: "Section 5: Financial information and financial decisions", nameVi: "Phần 5: Thông tin và quyết định tài chính", color: "#10b981" },
    { id: 6, nameEn: "Section 6: External influences on business issues", nameVi: "Phần 6: Ảnh hưởng bên ngoài tới kinh doanh", color: "#06b6d4" }
  ];

  const payloadJson = JSON.stringify(episodes.map(ep => ({
    episode: ep.episode,
    code: ep.code,
    sectionNumber: ep.sectionNumber,
    group: isEn ? ep.group : ep.groupVi,
    topic: isEn ? ep.topic : ep.topicVi,
    syllabusTitle: isEn ? ep.syllabusTitle : ep.syllabusTitleVi,
    title: isEn ? ep.titleEn : ep.titleVi,
    audioUrl: isEn ? ep.audioUrlEn : ep.audioUrlVi,
    durationSec: isEn ? ep.durationEnSec : ep.durationViSec,
    durationStr: isEn ? ep.durationEnStr : ep.durationViStr
  }))).replace(/</g, '\\u003c');

  return `
<div class="podcast-wrapper">
  <style>
    :root {
      --biz-primary: #1e40af;
      --biz-primary-hover: #1d4ed8;
      --biz-secondary: #0284c7;
      --biz-accent: #0ea5e9;
      --biz-dark: #0f172a;
      --biz-dark-surface: #1e293b;
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
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: var(--slate-800);
      background: transparent;
    }

    .podcast-wrapper {
      max-width: 980px;
      margin: 0 auto;
      padding: 12px 16px 28px;
    }

    /* HERO PLAYER CARD */
    .player-card {
      background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0369a1 100%);
      color: #ffffff;
      border-radius: 24px;
      padding: 24px 28px;
      box-shadow: 0 16px 36px -8px rgba(15, 23, 42, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.1) inset;
      margin-bottom: 24px;
      position: sticky;
      top: 12px;
      z-index: 40;
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .player-top {
      display: flex;
      align-items: center;
      gap: 20px;
      margin-bottom: 18px;
    }

    .cover-art {
      width: 80px;
      height: 80px;
      border-radius: 18px;
      background: linear-gradient(135deg, #0284c7 0%, #1e40af 100%);
      box-shadow: 0 8px 24px rgba(2, 132, 199, 0.4);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      border: 2px solid rgba(255, 255, 255, 0.2);
      text-align: center;
      padding: 4px;
      position: relative;
      overflow: hidden;
    }

    .cover-art svg {
      width: 28px;
      height: 28px;
      fill: none;
      stroke: #ffffff;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      margin-bottom: 2px;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    }

    .cover-art .code {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #e0f2fe;
    }

    .cover-art .sub {
      font-size: 7.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: rgba(255, 255, 255, 0.85);
    }

    .track-info {
      flex: 1;
      min-width: 0;
    }

    .track-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.15);
      font-size: 11px;
      font-weight: 700;
      color: #e0f2fe;
      margin-bottom: 6px;
      backdrop-filter: blur(8px);
      letter-spacing: 0.3px;
      max-width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .track-title {
      font-size: 19px;
      font-weight: 800;
      line-height: 1.35;
      color: #ffffff;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      text-shadow: 0 1px 3px rgba(0,0,0,0.25);
    }

    .track-syllabus {
      font-size: 12.5px;
      color: #bae6fd;
      line-height: 1.4;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      opacity: 0.95;
    }

    /* EQUALIZER ANIMATION */
    .equalizer-dots {
      display: inline-flex;
      align-items: flex-end;
      gap: 2px;
      height: 12px;
      margin-left: 6px;
    }

    .equalizer-dots span {
      width: 2.5px;
      height: 100%;
      background: #38bdf8;
      border-radius: 1px;
      transform-origin: bottom;
      animation: eq 1s ease-in-out infinite alternate;
    }
    .equalizer-dots span:nth-child(1) { animation-delay: 0.1s; height: 60%; }
    .equalizer-dots span:nth-child(2) { animation-delay: 0.3s; height: 100%; }
    .equalizer-dots span:nth-child(3) { animation-delay: 0.2s; height: 40%; }
    .equalizer-dots.paused span {
      animation-play-state: paused;
      height: 3px !important;
    }

    @keyframes eq {
      0% { transform: scaleY(0.2); }
      100% { transform: scaleY(1); }
    }

    /* PROGRESS BAR */
    .progress-cluster {
      margin-bottom: 16px;
    }

    .progress-bar-container {
      width: 100%;
      height: 7px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 9999px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: height 0.15s ease;
    }

    .progress-bar-container:hover {
      height: 9px;
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #38bdf8 0%, #60a5fa 100%);
      border-radius: 9999px;
      position: relative;
      transition: width 0.08s linear;
    }

    .time-stamps {
      display: flex;
      justify-content: space-between;
      font-size: 11.5px;
      font-weight: 600;
      color: rgba(255, 255, 255, 0.75);
      margin-top: 6px;
      font-variant-numeric: tabular-nums;
    }

    /* CONTROLS ROW */
    .controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }

    .speed-btn {
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      padding: 6px 12px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      min-width: 48px;
    }

    .speed-btn:hover {
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }

    .main-transport {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .btn-control {
      background: transparent;
      border: none;
      color: #ffffff;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      transition: all 0.2s ease;
      opacity: 0.9;
    }

    .btn-control:hover {
      opacity: 1;
      transform: scale(1.1);
    }

    .btn-skip {
      width: 36px;
      height: 36px;
      background: rgba(255, 255, 255, 0.12);
    }

    .btn-skip svg {
      width: 18px;
      height: 18px;
      fill: currentColor;
    }

    .btn-play {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: #ffffff;
      color: #0f172a;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
      opacity: 1;
    }

    .btn-play:hover {
      transform: scale(1.08);
      background: #f0fdf4;
      color: #0f172a;
    }

    .btn-play svg {
      width: 22px;
      height: 22px;
      fill: currentColor;
      margin-left: 2px;
    }
    .btn-play.playing svg {
      margin-left: 0;
    }

    .volume-cluster {
      display: flex;
      align-items: center;
      gap: 8px;
      min-width: 120px;
      justify-content: flex-end;
    }

    .volume-btn {
      background: transparent;
      border: none;
      color: #ffffff;
      cursor: pointer;
      opacity: 0.85;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .volume-btn:hover {
      opacity: 1;
    }

    .volume-slider {
      -webkit-appearance: none;
      appearance: none;
      width: 76px;
      height: 5px;
      border-radius: 5px;
      background: rgba(255, 255, 255, 0.25);
      outline: none;
      cursor: pointer;
    }

    .volume-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #ffffff;
      cursor: pointer;
      box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }

    /* SEARCH & FILTER BAR */
    .filter-bar {
      display: grid;
      grid-template-columns: 1fr auto auto;
      gap: 12px;
      margin-bottom: 22px;
      align-items: center;
    }

    .search-box {
      position: relative;
      display: flex;
      align-items: center;
    }

    .search-box svg {
      position: absolute;
      left: 14px;
      width: 18px;
      height: 18px;
      stroke: var(--slate-400);
      stroke-width: 2;
      pointer-events: none;
    }

    .search-input {
      width: 100%;
      padding: 11px 16px 11px 42px;
      border-radius: 14px;
      border: 1.5px solid var(--slate-200);
      background: #ffffff;
      font-size: 14px;
      color: var(--slate-800);
      outline: none;
      transition: all 0.2s ease;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }

    .search-input:focus {
      border-color: var(--biz-secondary);
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
    }

    .section-select {
      padding: 10px 14px;
      border-radius: 14px;
      border: 1.5px solid var(--slate-200);
      background: #ffffff;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--slate-700);
      outline: none;
      cursor: pointer;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      max-width: 260px;
    }

    .section-select:focus {
      border-color: var(--biz-secondary);
    }

    .track-counter {
      font-size: 12.5px;
      font-weight: 700;
      color: var(--slate-500);
      white-space: nowrap;
      padding: 0 4px;
    }

    /* PLAYLIST SECTIONS */
    .section-group {
      margin-bottom: 26px;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
      padding-left: 2px;
    }

    .section-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      background: #e0f2fe;
      color: #0369a1;
    }

    .section-title-text {
      font-size: 13px;
      font-weight: 700;
      color: var(--slate-500);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* PLAYLIST ITEMS */
    .playlist-card {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .track-item {
      display: grid;
      grid-template-columns: 46px 1fr auto;
      gap: 14px;
      align-items: center;
      padding: 12px 16px;
      border-radius: 16px;
      background: #ffffff;
      border: 1.5px solid var(--slate-200);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }

    .track-item:hover {
      border-color: var(--biz-secondary);
      background: #f8fafc;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.08);
    }

    .track-item.active {
      border-color: var(--biz-secondary);
      background: #f0f9ff;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.12);
    }

    .item-play-btn {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--slate-100);
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--slate-700);
      cursor: pointer;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }

    .track-item:hover .item-play-btn {
      background: #e0f2fe;
      color: var(--biz-primary);
    }

    .track-item.active .item-play-btn {
      background: var(--biz-primary);
      color: #ffffff;
    }

    .item-play-btn svg {
      width: 18px;
      height: 18px;
      fill: currentColor;
    }

    .item-meta {
      min-width: 0;
    }

    .item-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 2px;
    }

    .item-code {
      font-size: 11px;
      font-weight: 800;
      color: var(--biz-primary);
      background: #e0f2fe;
      padding: 2px 7px;
      border-radius: 6px;
      letter-spacing: 0.3px;
      flex-shrink: 0;
    }

    .item-title {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--slate-800);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .track-item.active .item-title {
      color: var(--biz-primary);
    }

    .item-desc {
      font-size: 12.5px;
      color: var(--slate-500);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      line-height: 1.35;
    }

    .item-trailing {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 4px;
      flex-shrink: 0;
    }

    .item-duration {
      font-size: 12px;
      font-weight: 700;
      color: var(--slate-400);
      font-variant-numeric: tabular-nums;
    }

    .track-item.active .item-duration {
      color: var(--biz-primary);
    }

    .active-wave {
      display: none;
      align-items: flex-end;
      gap: 2px;
      height: 10px;
    }

    .track-item.active .active-wave {
      display: flex;
    }

    .active-wave span {
      width: 2px;
      height: 100%;
      background: var(--biz-primary);
      border-radius: 1px;
      transform-origin: bottom;
      animation: eq 0.8s ease-in-out infinite alternate;
    }
    .active-wave span:nth-child(1) { animation-delay: 0.1s; }
    .active-wave span:nth-child(2) { animation-delay: 0.25s; }
    .active-wave span:nth-child(3) { animation-delay: 0.15s; }

    /* EMPTY STATE */
    .empty-search {
      display: none;
      text-align: center;
      padding: 48px 16px;
      color: var(--slate-400);
      background: #ffffff;
      border-radius: 18px;
      border: 1.5px dashed var(--slate-200);
    }

    .empty-search svg {
      width: 44px;
      height: 44px;
      stroke: var(--slate-300);
      margin-bottom: 10px;
    }

    /* RESPONSIVE */
    @media (max-width: 640px) {
      .player-card {
        padding: 16px 18px;
        border-radius: 18px;
      }
      .cover-art {
        width: 60px;
        height: 60px;
        border-radius: 14px;
      }
      .cover-art svg {
        width: 22px;
        height: 22px;
      }
      .track-title {
        font-size: 16px;
      }
      .filter-bar {
        grid-template-columns: 1fr;
      }
      .section-select {
        max-width: 100%;
      }
      .volume-cluster {
        display: none;
      }
      .item-desc {
        display: none;
      }
    }
  </style>

  <!-- HERO AUDIO PLAYER CARD -->
  <div class="player-card">
    <div class="player-top">
      <div class="cover-art">
        <svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
        <span class="code" id="cover-code">1</span>
        <span class="sub" id="cover-sub">BIZ</span>
      </div>
      <div class="track-info">
        <div class="track-badge">
          <span id="badge-code">1</span>
          <span>•</span>
          <span id="badge-subject">Understanding business activity</span>
          <div class="equalizer-dots" id="eq-dots">
            <span></span><span></span><span></span>
          </div>
        </div>
        <div class="track-title" id="player-title">${isEn ? episodes[0].titleEn : episodes[0].titleVi}</div>
        <div class="track-syllabus" id="player-syllabus">${isEn ? episodes[0].syllabusTitle : episodes[0].syllabusTitleVi}</div>
      </div>
    </div>

    <!-- PROGRESS BAR -->
    <div class="progress-cluster">
      <div class="progress-bar-container" id="progress-container">
        <div class="progress-fill" id="progress-fill"></div>
      </div>
      <div class="time-stamps">
        <span id="current-time">0:00</span>
        <span id="total-duration">${isEn ? episodes[0].durationEnStr : episodes[0].durationViStr}</span>
      </div>
    </div>

    <!-- CONTROLS ROW -->
    <div class="controls-row">
      <button type="button" class="speed-btn" id="btn-speed" title="${isEn ? 'Playback Speed' : 'Tốc độ phát'}">1.0x</button>

      <div class="main-transport">
        <button type="button" class="btn-control btn-skip" id="btn-prev" title="${isEn ? 'Previous Track' : 'Bài trước'}">
          <svg viewBox="0 0 24 24"><polygon points="19 20 9 12 19 4 19 20"></polygon><line x1="5" y1="19" x2="5" y2="5" stroke="currentColor" stroke-width="2"></line></svg>
        </button>

        <button type="button" class="btn-control btn-skip" id="btn-backward-15" title="${isEn ? 'Rewind 15 seconds' : 'Lùi 15 giây'}">
          <svg viewBox="0 0 24 24"><path d="M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z"/><text x="12" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="currentColor">15</text></svg>
        </button>

        <button type="button" class="btn-control btn-play" id="btn-main-play" title="${isEn ? 'Play / Pause' : 'Phát / Tạm dừng'}">
          <svg viewBox="0 0 24 24" id="play-icon"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
        </button>

        <button type="button" class="btn-control btn-skip" id="btn-forward-15" title="${isEn ? 'Forward 15 seconds' : 'Tiến 15 giây'}">
          <svg viewBox="0 0 24 24"><path d="M12 5V1l5 5-5 5V7c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6h2c0 4.42-3.58 8-8 8s-8-3.58-8-8 3.58-8 8-8z"/><text x="12" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="currentColor">15</text></svg>
        </button>

        <button type="button" class="btn-control btn-skip" id="btn-next" title="${isEn ? 'Next Track' : 'Bài tiếp'}">
          <svg viewBox="0 0 24 24"><polygon points="5 4 15 12 5 20 5 4"></polygon><line x1="19" y1="5" x2="19" y2="19" stroke="currentColor" stroke-width="2"></line></svg>
        </button>
      </div>

      <div class="volume-cluster">
        <button type="button" class="volume-btn" id="btn-mute" title="${isEn ? 'Mute' : 'Tắt tiếng'}">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" id="volume-icon"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
        </button>
        <input type="range" class="volume-slider" id="volume-slider" min="0" max="1" step="0.05" value="1">
      </div>
    </div>
  </div>

  <!-- SEARCH & FILTER BAR -->
  <div class="filter-bar">
    <div class="search-box">
      <svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      <input type="text" class="search-input" id="search-input" placeholder="${isEn ? 'Search 29 episodes (e.g. Scarcity, Marketing, Cash flow, Ch 1)...' : 'Tìm kiếm 29 chủ đề (ví dụ: Marketing, Dòng tiền, Chi phí, Bài 1)...'}">
    </div>

    <select class="section-select" id="section-select">
      <option value="all">${isEn ? 'All 29 Topics (Full 0450)' : 'Tất cả 29 Chủ đề (Trọn bộ 0450)'}</option>
      ${sections.map(s => `<option value="${s.id}">${isEn ? s.nameEn : s.nameVi}</option>`).join('')}
    </select>

    <div class="track-counter" id="track-counter">29 / 29 ${isEn ? 'topics' : 'chủ đề'}</div>
  </div>

  <!-- PLAYLIST CONTAINER -->
  <div class="playlist-container" id="playlist-container">
    ${sections.map(sec => {
      const secEpisodes = episodes.filter(e => e.sectionNumber === sec.id);
      if (!secEpisodes.length) return '';
      return `
      <div class="section-group" data-section="${sec.id}">
        <div class="section-header">
          <span class="section-pill" style="background: ${sec.color}15; color: ${sec.color};">
            ${isEn ? 'Part' : 'Phần'} ${sec.id}
          </span>
          <span class="section-title-text">${isEn ? sec.nameEn.split(':')[1].trim() : sec.nameVi.split(':')[1].trim()}</span>
        </div>
        <div class="playlist-card">
          ${secEpisodes.map(ep => {
            const title = isEn ? ep.titleEn : ep.titleVi;
            const subtitle = isEn ? ep.syllabusTitle : ep.syllabusTitleVi;
            const dur = isEn ? ep.durationEnStr : ep.durationViStr;
            return `
            <div class="track-item ${ep.episode === 1 ? 'active' : ''}" 
                 data-episode="${ep.episode}" 
                 data-code="${ep.code}"
                 data-title="${title.replace(/"/g, '&quot;')}"
                 data-section="${ep.sectionNumber}"
                 onclick="selectEpisode(${ep.episode})">
              <button type="button" class="item-play-btn" title="${isEn ? 'Play' : 'Nghe bài này'}">
                <svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              </button>
              <div class="item-meta">
                <div class="item-header">
                  <span class="item-code">#${ep.episode.toString().padStart(2, '0')}</span>
                  <span class="item-title">${title}</span>
                </div>
                <div class="item-desc">${subtitle}</div>
              </div>
              <div class="item-trailing">
                <span class="item-duration">${dur}</span>
                <div class="active-wave">
                  <span></span><span></span><span></span>
                </div>
              </div>
            </div>
            `;
          }).join('')}
        </div>
      </div>
      `;
    }).join('')}
  </div>

  <div class="empty-search" id="empty-search">
    <svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <p style="font-weight: 700; margin-bottom: 4px;">${isEn ? 'No topics found' : 'Không tìm thấy chủ đề phù hợp'}</p>
    <p style="font-size: 13px;">${isEn ? 'Try adjusting your search terms or filter.' : 'Vui lòng thử lại với từ khóa hoặc bộ lọc khác.'}</p>
  </div>
</div>

<script>
(function() {
  const EPISODES = ${payloadJson};
  let currentEpisodeIndex = 0;
  let isPlaying = false;
  let currentSpeedIdx = 1;
  const SPEEDS = [0.75, 1.0, 1.25, 1.5, 1.75, 2.0];

  const audio = new Audio();
  audio.preload = 'metadata';

  // DOM Elements
  const btnMainPlay = document.getElementById('btn-main-play');
  const playIcon = document.getElementById('play-icon');
  const progressContainer = document.getElementById('progress-container');
  const progressFill = document.getElementById('progress-fill');
  const currentTimeEl = document.getElementById('current-time');
  const totalDurationEl = document.getElementById('total-duration');
  const playerTitleEl = document.getElementById('player-title');
  const playerSyllabusEl = document.getElementById('player-syllabus');
  const badgeCodeEl = document.getElementById('badge-code');
  const badgeSubjectEl = document.getElementById('badge-subject');
  const coverCodeEl = document.getElementById('cover-code');
  const eqDotsEl = document.getElementById('eq-dots');
  const btnSpeed = document.getElementById('btn-speed');
  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');
  const btnBack15 = document.getElementById('btn-backward-15');
  const btnFwd15 = document.getElementById('btn-forward-15');
  const btnMute = document.getElementById('btn-mute');
  const volumeSlider = document.getElementById('volume-slider');
  const volumeIcon = document.getElementById('volume-icon');
  const searchInput = document.getElementById('search-input');
  const sectionSelect = document.getElementById('section-select');
  const trackCounter = document.getElementById('track-counter');
  const emptySearch = document.getElementById('empty-search');

  function formatTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return '0:00';
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return m + ':' + (s < 10 ? '0' : '') + s;
  }

  function updatePlayerUI(ep) {
    playerTitleEl.textContent = ep.title;
    playerSyllabusEl.textContent = ep.syllabusTitle;
    badgeCodeEl.textContent = ep.code;
    coverCodeEl.textContent = ep.code;
    badgeSubjectEl.textContent = ep.group;
    totalDurationEl.textContent = ep.durationStr || formatTime(ep.durationSec);

    document.querySelectorAll('.track-item').forEach(item => {
      const epNum = parseInt(item.getAttribute('data-episode'), 10);
      const btn = item.querySelector('.item-play-btn');
      if (epNum === ep.episode) {
        item.classList.add('active');
        if (btn) {
          btn.innerHTML = isPlaying 
            ? '<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>'
            : '<svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>';
        }
      } else {
        item.classList.remove('active');
        if (btn) {
          btn.innerHTML = '<svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>';
        }
      }
    });

    if (isPlaying) {
      btnMainPlay.classList.add('playing');
      playIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>';
      eqDotsEl.classList.remove('paused');
    } else {
      btnMainPlay.classList.remove('playing');
      playIcon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
      eqDotsEl.classList.add('paused');
    }

    if ('mediaSession' in navigator) {
      navigator.mediaSession.metadata = new MediaMetadata({
        title: ep.title,
        artist: 'Cambridge IGCSE Business Studies 0450',
        album: ep.group
      });
    }
  }

  function loadEpisode(index, autoPlay = true) {
    if (index < 0) index = 0;
    if (index >= EPISODES.length) index = EPISODES.length - 1;
    currentEpisodeIndex = index;
    const ep = EPISODES[index];

    audio.src = ep.audioUrl;
    audio.playbackRate = SPEEDS[currentSpeedIdx];
    progressFill.style.width = '0%';
    currentTimeEl.textContent = '0:00';

    if (autoPlay) {
      audio.play().then(() => {
        isPlaying = true;
        updatePlayerUI(ep);
      }).catch(err => {
        console.warn('Autoplay prevented:', err);
        isPlaying = false;
        updatePlayerUI(ep);
      });
    } else {
      isPlaying = false;
      updatePlayerUI(ep);
    }

    try {
      localStorage.setItem('tony_business_0450_last_ep', ep.episode);
    } catch(e) {}
  }

  window.selectEpisode = function(epNumber) {
    const idx = EPISODES.findIndex(e => e.episode === epNumber);
    if (idx !== -1) {
      if (idx === currentEpisodeIndex) {
        togglePlay();
      } else {
        loadEpisode(idx, true);
      }
    }
  };

  function togglePlay() {
    if (!audio.src) {
      loadEpisode(currentEpisodeIndex, true);
      return;
    }
    if (audio.paused) {
      audio.play().then(() => {
        isPlaying = true;
        updatePlayerUI(EPISODES[currentEpisodeIndex]);
      }).catch(e => console.error(e));
    } else {
      audio.pause();
      isPlaying = false;
      updatePlayerUI(EPISODES[currentEpisodeIndex]);
    }
  }

  // Event Listeners
  btnMainPlay.addEventListener('click', togglePlay);

  btnPrev.addEventListener('click', () => {
    if (audio.currentTime > 5) {
      audio.currentTime = 0;
    } else {
      loadEpisode(currentEpisodeIndex - 1, true);
    }
  });

  btnNext.addEventListener('click', () => {
    if (currentEpisodeIndex < EPISODES.length - 1) {
      loadEpisode(currentEpisodeIndex + 1, true);
    }
  });

  btnBack15.addEventListener('click', () => {
    audio.currentTime = Math.max(0, audio.currentTime - 15);
  });

  btnFwd15.addEventListener('click', () => {
    audio.currentTime = Math.min(audio.duration || Infinity, audio.currentTime + 15);
  });

  btnSpeed.addEventListener('click', () => {
    currentSpeedIdx = (currentSpeedIdx + 1) % SPEEDS.length;
    const s = SPEEDS[currentSpeedIdx];
    audio.playbackRate = s;
    btnSpeed.textContent = s.toFixed(2).replace(/\\.00$/, '').replace(/0$/, '') + 'x';
  });

  audio.addEventListener('timeupdate', () => {
    if (!audio.duration) return;
    const pct = (audio.currentTime / audio.duration) * 100;
    progressFill.style.width = pct + '%';
    currentTimeEl.textContent = formatTime(audio.currentTime);
  });

  audio.addEventListener('loadedmetadata', () => {
    totalDurationEl.textContent = formatTime(audio.duration);
  });

  audio.addEventListener('ended', () => {
    if (currentEpisodeIndex < EPISODES.length - 1) {
      loadEpisode(currentEpisodeIndex + 1, true);
    } else {
      isPlaying = false;
      updatePlayerUI(EPISODES[currentEpisodeIndex]);
    }
  });

  progressContainer.addEventListener('click', (e) => {
    const rect = progressContainer.getBoundingClientRect();
    const pos = (e.clientX - rect.left) / rect.width;
    if (audio.duration) {
      audio.currentTime = pos * audio.duration;
    }
  });

  volumeSlider.addEventListener('input', (e) => {
    const v = parseFloat(e.target.value);
    audio.volume = v;
    audio.muted = (v === 0);
    updateVolumeIcon(v);
  });

  btnMute.addEventListener('click', () => {
    audio.muted = !audio.muted;
    updateVolumeIcon(audio.muted ? 0 : audio.volume);
    volumeSlider.value = audio.muted ? 0 : audio.volume;
  });

  function updateVolumeIcon(v) {
    if (v === 0 || audio.muted) {
      volumeIcon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line>';
    } else if (v < 0.5) {
      volumeIcon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
    } else {
      volumeIcon.innerHTML = '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>';
    }
  }

  // Filter & Search Logic
  function applyFilters() {
    const q = (searchInput.value || '').trim().toLowerCase();
    const secVal = sectionSelect.value;
    let visibleCount = 0;

    document.querySelectorAll('.section-group').forEach(grp => {
      const sId = grp.getAttribute('data-section');
      let sectionHasVisible = false;

      grp.querySelectorAll('.track-item').forEach(item => {
        const itemSec = item.getAttribute('data-section');
        const itemTitle = (item.getAttribute('data-title') || '').toLowerCase();
        const itemCode = (item.getAttribute('data-code') || '').toLowerCase();
        const itemEp = item.getAttribute('data-episode');

        const matchSec = (secVal === 'all' || secVal === itemSec);
        const matchQ = !q || itemTitle.includes(q) || itemCode.includes(q) || ('ch ' + itemEp).includes(q) || ('bài ' + itemEp).includes(q) || ('#' + itemEp).includes(q);

        if (matchSec && matchQ) {
          item.style.display = 'grid';
          sectionHasVisible = true;
          visibleCount++;
        } else {
          item.style.display = 'none';
        }
      });

      grp.style.display = sectionHasVisible ? 'block' : 'none';
    });

    trackCounter.textContent = visibleCount + ' / 29 ' + (${isEn ? "'topics'" : "'chủ đề'"});
    emptySearch.style.display = (visibleCount === 0) ? 'block' : 'none';
  }

  searchInput.addEventListener('input', applyFilters);
  sectionSelect.addEventListener('change', applyFilters);

  // Keyboard Navigation
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
    if (e.code === 'Space') {
      e.preventDefault();
      togglePlay();
    } else if (e.code === 'ArrowLeft') {
      e.preventDefault();
      audio.currentTime = Math.max(0, audio.currentTime - 10);
    } else if (e.code === 'ArrowRight') {
      e.preventDefault();
      audio.currentTime = Math.min(audio.duration || Infinity, audio.currentTime + 10);
    }
  });

  // Initial Load
  let initialEpIdx = 0;
  try {
    const saved = parseInt(localStorage.getItem('tony_business_0450_last_ep'), 10);
    if (!isNaN(saved)) {
      const foundIdx = EPISODES.findIndex(e => e.episode === saved);
      if (foundIdx !== -1) initialEpIdx = foundIdx;
    }
  } catch(e) {}

  loadEpisode(initialEpIdx, false);
})();
</script>
  `;
}

module.exports = {
  generateBusinessPodcastPlayerHtml
};
