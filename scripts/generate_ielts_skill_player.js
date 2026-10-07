/**
 * Generator for IELTS Premium Podcast Player HTML
 * Used for Writing Task 1, Writing Task 2, Reading, Listening, and Speaking Part 2
 */

function generateIeltsSkillPlayerHtml(skillKey, skillData) {
  const {
    moduleName,
    lectureTitle,
    themeColor,
    themeBg,
    badge,
    desc,
    episodes
  } = skillData;

  const storageKey = `tony_ielts_${skillKey}_last_ep`;
  const payloadJson = JSON.stringify(episodes.map(ep => ({
    episode: ep.episode,
    code: ep.code,
    title: ep.title,
    sub: ep.sub,
    audioUrl: ep.audioUrl,
    durationSec: ep.durationSec,
    durationStr: ep.durationStr
  }))).replace(/</g, '\\u003c');

  return `
<div class="podcast-wrapper">
  <style>
    :root {
      --skill-primary: ${themeColor};
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
      max-width: 960px;
      margin: 0 auto;
      padding: 12px 16px 28px;
    }

    /* HERO PLAYER CARD */
    .player-card {
      background: ${themeBg};
      color: #ffffff;
      border-radius: 22px;
      padding: 22px 26px;
      box-shadow: 0 16px 36px -8px rgba(15, 23, 42, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.12) inset;
      margin-bottom: 22px;
      position: sticky;
      top: 12px;
      z-index: 40;
      backdrop-filter: blur(16px);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .player-top {
      display: flex;
      align-items: center;
      gap: 18px;
      margin-bottom: 16px;
    }

    .cover-art {
      width: 72px;
      height: 72px;
      border-radius: 16px;
      background: rgba(255, 255, 255, 0.15);
      border: 2px solid rgba(255, 255, 255, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      position: relative;
      overflow: hidden;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
    }

    .cover-art::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.35), transparent 70%);
    }

    .cover-icon {
      width: 36px;
      height: 36px;
      color: #ffffff;
      position: relative;
      z-index: 2;
    }

    .meta-box {
      flex: 1;
      min-width: 0;
    }

    .meta-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 3px 9px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 5px;
    }

    .meta-badge .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: 0 0 8px #ffffff;
    }

    .current-title {
      font-size: 18.5px;
      font-weight: 700;
      line-height: 1.35;
      color: #ffffff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 3px;
    }

    .current-sub {
      font-size: 13px;
      color: rgba(255, 255, 255, 0.85);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      font-weight: 400;
    }

    /* SCRUBBER & TIMESTAMPS */
    .scrubber-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
    }

    .time-stamp {
      font-size: 12px;
      font-variant-numeric: tabular-nums;
      color: rgba(255, 255, 255, 0.85);
      font-weight: 600;
      width: 44px;
    }
    .time-stamp.right {
      text-align: right;
    }

    .scrubber-container {
      flex: 1;
      position: relative;
      height: 20px;
      display: flex;
      align-items: center;
      cursor: pointer;
    }

    .scrubber-track {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.22);
      position: relative;
      overflow: hidden;
    }

    .scrubber-buffer {
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 0%;
      background: rgba(255, 255, 255, 0.35);
      border-radius: 999px;
      transition: width 0.2s ease;
    }

    .scrubber-fill {
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      width: 0%;
      background: #ffffff;
      border-radius: 999px;
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
    }

    .scrubber-thumb {
      position: absolute;
      left: 0%;
      width: 13px;
      height: 13px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
      transform: translateX(-50%);
      pointer-events: none;
      transition: transform 0.1s ease;
    }

    .scrubber-container:hover .scrubber-thumb {
      transform: translateX(-50%) scale(1.25);
    }

    /* CONTROLS ROW */
    .controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .controls-left,
    .controls-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .controls-center {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .ctrl-btn {
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

    .ctrl-btn:hover {
      background: rgba(255, 255, 255, 0.18);
      color: #ffffff;
      transform: scale(1.06);
    }

    .ctrl-btn:active {
      transform: scale(0.96);
    }

    .play-btn {
      width: 48px;
      height: 48px;
      background: #ffffff;
      color: var(--skill-primary);
      border-radius: 50%;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .play-btn:hover {
      transform: scale(1.08);
      box-shadow: 0 8px 22px rgba(255, 255, 255, 0.4);
    }

    .play-btn:active {
      transform: scale(0.96);
    }

    .speed-btn {
      background: rgba(255, 255, 255, 0.16);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      padding: 5px 11px;
      border-radius: 999px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }

    .speed-btn:hover {
      background: rgba(255, 255, 255, 0.28);
    }

    /* HEADER */
    .header-box {
      margin-bottom: 20px;
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      border-bottom: 2px solid var(--slate-200);
      padding-bottom: 12px;
    }

    .header-info h1 {
      font-size: 22px;
      font-weight: 800;
      color: var(--slate-900);
      letter-spacing: -0.02em;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .header-info p {
      font-size: 13.5px;
      color: var(--slate-600);
      line-height: 1.5;
    }

    .tag-badge {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 6px;
      background: #f1f5f9;
      color: var(--skill-primary);
      border: 1px solid var(--slate-300);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* SEARCH BAR */
    .filter-bar {
      margin-bottom: 16px;
    }

    .search-box {
      position: relative;
      width: 100%;
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
      transition: all 0.2s;
    }

    .search-input:focus {
      border-color: var(--skill-primary);
      box-shadow: 0 0 0 3px rgba(15, 23, 42, 0.08);
    }

    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      width: 16px;
      height: 16px;
      color: var(--slate-400);
      pointer-events: none;
    }

    /* EPISODE LIST */
    .episodes-list {
      display: flex;
      flex-direction: column;
      gap: 9px;
    }

    .episode-card {
      background: #ffffff;
      border: 1.5px solid var(--slate-200);
      border-radius: 14px;
      padding: 13px 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .episode-card:hover {
      border-color: var(--skill-primary);
      background: #f8fafc;
      transform: translateY(-1px);
      box-shadow: 0 5px 14px -3px rgba(15, 23, 42, 0.08);
    }

    .episode-card.active {
      background: #faf5ff;
      border-color: var(--skill-primary);
      box-shadow: 0 6px 20px -4px rgba(15, 23, 42, 0.15);
    }

    .ep-num-badge {
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: var(--slate-100);
      color: var(--slate-700);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 13.5px;
      flex-shrink: 0;
      border: 1px solid var(--slate-200);
      transition: all 0.2s;
    }

    .episode-card.active .ep-num-badge {
      background: var(--skill-primary);
      color: #ffffff;
      border-color: var(--skill-primary);
    }

    .ep-main {
      flex: 1;
      min-width: 0;
    }

    .ep-title {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--slate-900);
      margin-bottom: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .episode-card.active .ep-title {
      color: var(--skill-primary);
    }

    .ep-desc {
      font-size: 12.5px;
      color: var(--slate-500);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      line-height: 1.4;
    }

    .ep-right {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }

    .ep-duration {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--slate-500);
      font-variant-numeric: tabular-nums;
    }

    .card-play-icon {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: var(--slate-100);
      color: var(--slate-600);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }

    .episode-card:hover .card-play-icon {
      background: var(--skill-primary);
      color: #ffffff;
    }

    .episode-card.active .card-play-icon {
      background: var(--skill-primary);
      color: #ffffff;
    }

    /* WAVE ANIMATION FOR PLAYING */
    .wave-bars {
      display: none;
      align-items: center;
      gap: 2.5px;
      height: 16px;
    }

    .episode-card.active.is-playing .wave-bars {
      display: flex;
    }

    .episode-card.active.is-playing .card-play-icon {
      display: none;
    }

    .wave-bar {
      width: 3px;
      background: var(--skill-primary);
      border-radius: 2px;
      animation: pulseWave 1s ease-in-out infinite alternate;
    }

    .wave-bar:nth-child(1) { height: 7px; animation-delay: 0.1s; }
    .wave-bar:nth-child(2) { height: 14px; animation-delay: 0.3s; }
    .wave-bar:nth-child(3) { height: 9px; animation-delay: 0.5s; }
    .wave-bar:nth-child(4) { height: 12px; animation-delay: 0.2s; }

    @keyframes pulseWave {
      0% { transform: scaleY(0.3); }
      100% { transform: scaleY(1); }
    }

    @media (max-width: 640px) {
      .player-card {
        padding: 16px;
      }
      .cover-art {
        width: 56px;
        height: 56px;
      }
      .current-title {
        font-size: 15px;
      }
      .ep-desc {
        display: none;
      }
    }
  </style>

  <!-- HEADER -->
  <div class="header-box">
    <div class="header-info">
      <h1>
        <span>${lectureTitle}</span>
        <span class="tag-badge">${badge}</span>
      </h1>
      <p>${desc}</p>
    </div>
  </div>

  <!-- STICKY PLAYER -->
  <div class="player-card" id="ieltsPlayerCard">
    <div class="player-top">
      <div class="cover-art">
        <svg class="cover-icon" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/>
        </svg>
      </div>
      <div class="meta-box">
        <div class="meta-badge">
          <span class="dot"></span>
          <span id="playerBadge">${badge}</span>
        </div>
        <div class="current-title" id="playerCurTitle">Đang tải podcast...</div>
        <div class="current-sub" id="playerCurSub">Chọn một bài học để bắt đầu</div>
      </div>
    </div>

    <!-- SCRUBBER -->
    <div class="scrubber-row">
      <span class="time-stamp" id="playerCurTime">0:00</span>
      <div class="scrubber-container" id="playerScrubberContainer">
        <div class="scrubber-track">
          <div class="scrubber-buffer" id="playerScrubberBuffer"></div>
          <div class="scrubber-fill" id="playerScrubberFill"></div>
        </div>
        <div class="scrubber-thumb" id="playerScrubberThumb"></div>
      </div>
      <span class="time-stamp right" id="playerTotalTime">0:00</span>
    </div>

    <!-- CONTROLS -->
    <div class="controls-row">
      <div class="controls-left">
        <button class="speed-btn" id="playerSpeedBtn" title="Tốc độ phát">1.0x</button>
      </div>

      <div class="controls-center">
        <button class="ctrl-btn" id="playerPrevBtn" title="Bài trước">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 6h2v12H6zm3.5 6l8.5 6V6z"/>
          </svg>
        </button>

        <button class="ctrl-btn" id="playerRewindBtn" title="Lùi 10s">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8zm-1.1 11h-.85v-3.26l-1.01.31v-.59l1.62-.56h.24V16zm4.27-1.63c0 .54-.12.95-.36 1.23-.24.27-.58.41-1.01.41-.44 0-.78-.14-1.02-.41-.24-.28-.36-.69-.36-1.23v-1.12c0-.54.12-.95.36-1.23.24-.28.58-.42 1.02-.42.43 0 .77.14 1.01.42.24.28.36.69.36 1.23v1.12zm-.85-1.23c0-.38-.06-.65-.17-.81-.11-.17-.28-.25-.51-.25s-.4.08-.51.25c-.11.16-.17.43-.17.81v1.34c0 .38.06.65.17.82.11.16.28.25.51.25s.4-.09.51-.25c.11-.17.17-.44.17-.82v-1.34z"/>
          </svg>
        </button>

        <button class="play-btn" id="playerPlayBtn" title="Phát/Tạm dừng">
          <svg id="playerPlayIcon" width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M8 5v14l11-7z"/>
          </svg>
          <svg id="playerPauseIcon" style="display:none;" width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
          </svg>
        </button>

        <button class="ctrl-btn" id="playerForwardBtn" title="Tiến 10s">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 5V1l5 5-5 5V7c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6h2c0 4.42-3.58 8-8 8s-8-3.58-8-8 3.58-8 8-8zm-1.1 11h-.85v-3.26l-1.01.31v-.59l1.62-.56h.24V16zm4.27-1.63c0 .54-.12.95-.36 1.23-.24.27-.58.41-1.01.41-.44 0-.78-.14-1.02-.41-.24-.28-.36-.69-.36-1.23v-1.12c0-.54.12-.95.36-1.23.24-.28.58-.42 1.02-.42.43 0 .77.14 1.01.42.24.28.36.69.36 1.23v1.12zm-.85-1.23c0-.38-.06-.65-.17-.81-.11-.17-.28-.25-.51-.25s-.4.08-.51.25c-.11.16-.17.43-.17.81v1.34c0 .38.06.65.17.82.11.16.28.25.51.25s.4-.09.51-.25c.11-.17.17-.44.17-.82v-1.34z"/>
          </svg>
        </button>

        <button class="ctrl-btn" id="playerNextBtn" title="Bài kế tiếp">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6 18l8.5-6L6 6v12zM16 6v12h2V6h-2z"/>
          </svg>
        </button>
      </div>

      <div class="controls-right">
        <button class="ctrl-btn" id="playerMuteBtn" title="Bật/Tắt âm">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Hidden Native Audio -->
    <audio id="nativeAudio" preload="metadata"></audio>
  </div>

  <!-- SEARCH BOX -->
  <div class="filter-bar">
    <div class="search-box">
      <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input type="text" class="search-input" id="playerSearchInput" placeholder="Tìm kiếm bài podcast, dạng bài, từ khóa...">
    </div>
  </div>

  <!-- EPISODES LIST -->
  <div class="episodes-list" id="playerEpisodesList">
    <!-- Rendered via JS -->
  </div>
</div>

<script>
(function() {
  const EPISODES = ${payloadJson};
  const STORAGE_KEY = '${storageKey}';

  let currentIndex = 0;
  let isPlaying = false;
  let searchTerm = '';

  const audio = document.getElementById('nativeAudio');
  const playBtn = document.getElementById('playerPlayBtn');
  const playIcon = document.getElementById('playerPlayIcon');
  const pauseIcon = document.getElementById('playerPauseIcon');
  const prevBtn = document.getElementById('playerPrevBtn');
  const nextBtn = document.getElementById('playerNextBtn');
  const rewindBtn = document.getElementById('playerRewindBtn');
  const forwardBtn = document.getElementById('playerForwardBtn');
  const speedBtn = document.getElementById('playerSpeedBtn');
  const muteBtn = document.getElementById('playerMuteBtn');

  const curTitleEl = document.getElementById('playerCurTitle');
  const curSubEl = document.getElementById('playerCurSub');
  const curTimeEl = document.getElementById('playerCurTime');
  const totalTimeEl = document.getElementById('playerTotalTime');

  const scrubberContainer = document.getElementById('playerScrubberContainer');
  const scrubberFill = document.getElementById('playerScrubberFill');
  const scrubberThumb = document.getElementById('playerScrubberThumb');
  const scrubberBuffer = document.getElementById('playerScrubberBuffer');

  const searchInput = document.getElementById('playerSearchInput');
  const epListEl = document.getElementById('playerEpisodesList');

  const speeds = [1.0, 1.25, 1.5, 1.75, 2.0];
  let curSpeedIdx = 0;

  function formatTime(sec) {
    if (isNaN(sec) || !isFinite(sec)) return "0:00";
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return m + ":" + (s < 10 ? "0" : "") + s;
  }

  function loadEpisode(index, autoPlay = true) {
    if (index < 0 || index >= EPISODES.length) return;
    currentIndex = index;
    const ep = EPISODES[currentIndex];

    curTitleEl.textContent = \`[\${ep.code}] \${ep.title}\`;
    curSubEl.textContent = ep.sub || '';

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
        console.warn('Autoplay error:', err);
      });
    } else {
      isPlaying = false;
      updatePlayState();
    }

    try {
      localStorage.setItem(STORAGE_KEY, ep.episode);
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

    document.querySelectorAll('.episode-card').forEach(card => {
      const epIdx = parseInt(card.getAttribute('data-index'), 10);
      if (epIdx === currentIndex) {
        card.classList.add('active');
        if (isPlaying) {
          card.classList.add('is-playing');
        } else {
          card.classList.remove('is-playing');
        }
      } else {
        card.classList.remove('active', 'is-playing');
      }
    });
  }

  function togglePlay() {
    if (!audio.src) {
      loadEpisode(0, true);
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

  // Audio Events
  audio.addEventListener('timeupdate', () => {
    if (!audio.duration) return;
    const cur = audio.currentTime;
    const dur = audio.duration;
    curTimeEl.textContent = formatTime(cur);
    updateScrubber((cur / dur) * 100);
  });

  audio.addEventListener('progress', () => {
    if (!audio.duration || audio.buffered.length === 0) return;
    const bufferedEnd = audio.buffered.end(audio.buffered.length - 1);
    const p = (bufferedEnd / audio.duration) * 100;
    scrubberBuffer.style.width = p + '%';
  });

  audio.addEventListener('ended', () => {
    if (currentIndex < EPISODES.length - 1) {
      loadEpisode(currentIndex + 1, true);
    } else {
      isPlaying = false;
      updatePlayState();
    }
  });

  audio.addEventListener('play', () => {
    isPlaying = true;
    updatePlayState();
  });

  audio.addEventListener('pause', () => {
    isPlaying = false;
    updatePlayState();
  });

  // Controls Event Listeners
  playBtn.addEventListener('click', togglePlay);

  prevBtn.addEventListener('click', () => {
    if (audio.currentTime > 5) {
      audio.currentTime = 0;
    } else if (currentIndex > 0) {
      loadEpisode(currentIndex - 1, true);
    }
  });

  nextBtn.addEventListener('click', () => {
    if (currentIndex < EPISODES.length - 1) {
      loadEpisode(currentIndex + 1, true);
    }
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
    speedBtn.textContent = sp.toFixed(1) + 'x';
  });

  muteBtn.addEventListener('click', () => {
    audio.muted = !audio.muted;
    muteBtn.style.opacity = audio.muted ? '0.4' : '1';
  });

  // Scrubber drag / click
  let isDragging = false;

  function seekFromEvent(e) {
    const rect = scrubberContainer.getBoundingClientRect();
    const x = Math.max(0, Math.min(e.clientX - rect.left, rect.width));
    const pct = (x / rect.width);
    updateScrubber(pct * 100);
    if (audio.duration) {
      audio.currentTime = pct * audio.duration;
    }
  }

  scrubberContainer.addEventListener('mousedown', (e) => {
    isDragging = true;
    seekFromEvent(e);
  });

  window.addEventListener('mousemove', (e) => {
    if (isDragging) {
      seekFromEvent(e);
    }
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });

  // Filter & Search
  function getFilteredEpisodes() {
    return EPISODES.map((ep, idx) => ({ ...ep, originalIndex: idx })).filter(ep => {
      if (!searchTerm) return true;
      const term = searchTerm.toLowerCase();
      const inTitle = (ep.title || '').toLowerCase().includes(term);
      const inSub = (ep.sub || '').toLowerCase().includes(term);
      const inCode = (ep.code || '').toLowerCase().includes(term);
      return inTitle || inSub || inCode;
    });
  }

  function renderList() {
    const filtered = getFilteredEpisodes();
    if (filtered.length === 0) {
      epListEl.innerHTML = \`
        <div style="text-align: center; padding: 36px 16px; color: var(--slate-500); font-size: 13.5px;">
          Không tìm thấy bài học nào phù hợp.
        </div>
      \`;
      return;
    }

    epListEl.innerHTML = filtered.map(ep => {
      const isActive = ep.originalIndex === currentIndex;
      const isCardPlaying = isActive && isPlaying;
      return \`
        <div class="episode-card \${isActive ? 'active' : ''} \${isCardPlaying ? 'is-playing' : ''}" data-index="\${ep.originalIndex}">
          <div class="ep-num-badge">\${ep.code}</div>
          <div class="ep-main">
            <div class="ep-title">\${ep.title}</div>
            <div class="ep-desc">\${ep.sub}</div>
          </div>
          <div class="ep-right">
            <span class="ep-duration">\${ep.durationStr}</span>
            <div class="wave-bars">
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
              <div class="wave-bar"></div>
            </div>
            <div class="card-play-icon">
              \${isActive && isPlaying ? \`
                <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
                </svg>
              \` : \`
                <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M8 5v14l11-7z"/>
                </svg>
              \`}
            </div>
          </div>
        </div>
      \`;
    }).join('');

    // Attach click listeners to cards
    document.querySelectorAll('.episode-card').forEach(card => {
      card.addEventListener('click', () => {
        const idx = parseInt(card.getAttribute('data-index'), 10);
        if (idx === currentIndex) {
          togglePlay();
        } else {
          loadEpisode(idx, true);
        }
      });
    });
  }

  // Search input
  let searchDebounceTimer;
  searchInput.addEventListener('input', (e) => {
    clearTimeout(searchDebounceTimer);
    searchDebounceTimer = setTimeout(() => {
      searchTerm = e.target.value.trim();
      renderList();
    }, 200);
  });

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
    const saved = parseInt(localStorage.getItem(STORAGE_KEY), 10);
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
  generateIeltsSkillPlayerHtml
};
