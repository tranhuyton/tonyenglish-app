import os
import sys
import json
import uuid
import urllib.request
from supabase import create_client

sys.stdout.reconfigure(encoding='utf-8')

env_vars = {}
with open('.env', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            env_vars[k.strip()] = v.strip().strip("'").strip('"')

SUPABASE_URL = env_vars['VITE_SUPABASE_URL']
SUPABASE_ANON_KEY = env_vars['VITE_SUPABASE_ANON_KEY']
supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

PODCAST_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'podcasts')
STORAGE_PREFIX = "audio/communication/podcasts"
STORAGE_BASE = f"{SUPABASE_URL}/storage/v1/object/public/test_assets/{STORAGE_PREFIX}"

with open('scratch/dialogue_lectures_data.json', 'r', encoding='utf-8') as f:
    dialogues_data = json.load(f)


def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def upload_file_to_supabase(local_path, storage_filename):
    storage_path = f"{STORAGE_PREFIX}/{storage_filename}"
    upload_url = f"{SUPABASE_URL}/storage/v1/object/test_assets/{storage_path}"
    with open(local_path, 'rb') as f:
        data = f.read()

    req = urllib.request.Request(upload_url, data=data, method='POST')
    req.add_header('Authorization', f'Bearer {SUPABASE_ANON_KEY}')
    req.add_header('apikey', SUPABASE_ANON_KEY)
    req.add_header('Content-Type', 'audio/mpeg')
    req.add_header('x-upsert', 'true')

    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                if resp.status in (200, 201):
                    print(f"  [Uploaded] {storage_path} ({len(data)/1024:.0f} KB)")
                    return True
        except Exception as e:
            print(f"  [Retry {attempt}] Upload error for {storage_path}: {e}")
    return False


def generate_dialogue_page2_html(d):
    slug = d['slug']
    clean_title = d['clean_title']
    lecture_title = d['lecture_title']
    mod_title = d['module_title']

    sh_path = os.path.join(PODCAST_DIR, f"podcast_shadowing_{slug}.json")
    rf_path = os.path.join(PODCAST_DIR, f"podcast_reflex_vi_en_{slug}.json")

    with open(sh_path, 'r', encoding='utf-8') as f:
        sh_data = json.load(f)
    with open(rf_path, 'r', encoding='utf-8') as f:
        rf_data = json.load(f)

    sh_total_dur = sh_data['total_duration']
    rf_total_dur = rf_data['total_duration']
    total_sentences = sum(len(p['sentences']) for p in sh_data['patterns'])

    reflex_audio_url = f"{STORAGE_BASE}/podcast_reflex_vi_en_{slug}.mp3"
    shadowing_audio_url = f"{STORAGE_BASE}/podcast_shadowing_{slug}.mp3"

    js_bundle = {
        'slug': slug,
        'cleanTitle': clean_title,
        'lectureTitle': lecture_title,
        'moduleTitle': mod_title,
        'totalSentences': total_sentences,
        'reflex': {
            'totalDur': round(rf_total_dur, 2),
            'mp3': reflex_audio_url,
            'storageMp3': reflex_audio_url,
            'patterns': rf_data['patterns']
        },
        'shadowing': {
            'totalDur': round(sh_total_dur, 2),
            'mp3': shadowing_audio_url,
            'storageMp3': shadowing_audio_url,
            'patterns': sh_data['patterns']
        }
    }
    js_bundle_str = json.dumps(js_bundle, ensure_ascii=False)

    html = f"""<!-- 🎙️ DIALOGUE DUAL-MODE PODCAST (SHADOWING & REFLEX VI-EN) - PAGE 2 -->
<style>
.dialogue-pod-wrapper {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    margin: 0 auto;
    max-width: 100%;
}}
.part-header-banner {{
    padding: 16px 20px;
    border-radius: 14px;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border: 1px solid #bae6fd;
    border-left: 6px solid #0284c7;
}}
.banner-badge {{
    width: 42px;
    height: 42px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 900;
    flex-shrink: 0;
    background: #0284c7;
    color: #ffffff;
    box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);
}}
.banner-tag {{
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 2px;
    color: #0369a1;
}}
.banner-title {{
    margin: 0;
    font-size: 17.5px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.3;
}}
.banner-desc {{
    margin: 4px 0 0 0;
    font-size: 13px;
    color: #475569;
    line-height: 1.4;
}}
.banner-pill {{
    font-size: 12px;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #e0f2fe;
    color: #075985;
    border: 1px solid #bae6fd;
}}
.pod-card {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin-bottom: 24px; background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.06); overflow: hidden; }}
.pod-nav-tabs {{ display: flex; background: #0f172a; padding: 6px 8px; gap: 6px; border-bottom: 1px solid rgba(255,255,255,0.1); }}
.pod-nav-btn {{ flex: 1; padding: 10px 14px; border: none; border-radius: 10px; background: transparent; color: #94a3b8; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s ease; text-align: left; }}
.pod-nav-btn:hover {{ background: rgba(255,255,255,0.06); color: #f8fafc; }}
.pod-nav-btn.active {{ background: #0284c7; color: #ffffff; box-shadow: 0 4px 12px rgba(2,132,199,0.4); }}
.pod-nav-btn.active.reflex-active {{ background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%); box-shadow: 0 4px 12px rgba(79,70,229,0.4); }}
.pod-header {{ padding: 18px 24px; color: #ffffff; transition: background 0.3s ease; }}
.pod-header.mode-reflex {{ background: linear-gradient(135deg, #3730a3 0%, #4338ca 50%, #4f46e5 100%); }}
.pod-header.mode-shadowing {{ background: linear-gradient(135deg, #0369a1 0%, #0284c7 50%, #0ea5e9 100%); }}
.pod-body {{ padding: 20px 24px; background: #f8fafc; border-bottom: 1px solid #e2e8f0; }}
.pod-now-playing {{ background: #ffffff; border-radius: 12px; padding: 16px 20px; margin-bottom: 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.04); transition: all 0.25s ease; border-left: 5px solid #0284c7; }}
.pod-btn-round {{ background: #ffffff; border: 1px solid #cbd5e1; color: #475569; width: 38px; height: 38px; border-radius: 50%; font-size: 12px; font-weight: bold; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.15s ease; }}
.pod-btn-round:hover {{ background: #f1f5f9; color: #0f172a; border-color: #94a3b8; }}
.pod-btn-play {{ color: #ffffff; height: 42px; padding: 0 24px; border-radius: 25px; border: none; font-size: 14.5px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.2s ease; }}
.pod-btn-play.reflex {{ background: #4f46e5; box-shadow: 0 4px 14px rgba(79,70,229,0.35); }}
.pod-btn-play.reflex:hover {{ background: #4338ca; transform: scale(1.02); }}
.pod-btn-play.shadowing {{ background: #0284c7; box-shadow: 0 4px 14px rgba(2,132,199,0.35); }}
.pod-btn-play.shadowing:hover {{ background: #0369a1; transform: scale(1.02); }}
.pod-speed-btn {{ background: transparent; border: none; color: #64748b; font-size: 12px; font-weight: 700; padding: 4px 8px; border-radius: 6px; cursor: pointer; }}
.pod-speed-btn.active {{ background: #e0e7ff; color: #4338ca; }}
.pod-row {{ display: flex; align-items: center; justify-content: space-between; padding: 10px 14px; border-radius: 10px; background: #ffffff; margin-bottom: 8px; transition: all 0.2s ease; border: 1px solid #e2e8f0; }}
.pod-row:hover {{ background: #f8fafc; border-color: #94a3b8; }}
.pod-row.active-speaking {{ background: #e0e7ff !important; border-color: #818cf8 !important; border-left: 4px solid #4f46e5 !important; }}
.pod-row.active-turn {{ background: #fef3c7 !important; border-color: #fcd34d !important; border-left: 4px solid #f59e0b !important; }}
.pod-row.active-answer {{ background: #dcfce7 !important; border-color: #86efac !important; border-left: 4px solid #16a34a !important; }}
.pod-row-play-btn {{ background: #e0e7ff; color: #4338ca; border-radius: 6px; padding: 4px 9px; font-size: 11px; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; border: 1px solid #c7d2fe; transition: all 0.15s ease; flex-shrink: 0; }}
.pod-row:hover .pod-row-play-btn {{ background: #4f46e5; color: #ffffff; border-color: #4f46e5; }}
.speaker-chip {{ display: inline-block; font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 6px; margin-right: 6px; }}
.speaker-chip.role-A {{ background: #e0f2fe; color: #0369a1; }}
.speaker-chip.role-B {{ background: #f1f5f9; color: #334155; }}
.part-flow-action {{
    margin-top: 20px;
    padding: 16px 20px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 14px;
    background: #f8fafc;
    border: 1.5px dashed #94a3b8;
}}
.part-flow-btn {{
    border: none;
    border-radius: 25px;
    padding: 10px 20px;
    font-size: 13.5px;
    font-weight: 700;
    color: #ffffff;
    background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
    transition: all 0.2s ease;
}}
.part-flow-btn:hover {{
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(2, 132, 199, 0.35);
}}
</style>

<div class="dialogue-pod-wrapper">
    <!-- Section Header Banner -->
    <div class="part-header-banner">
        <div style="display: flex; align-items: center; gap: 14px;">
            <div class="banner-badge">🎧</div>
            <div>
                <div class="banner-tag">TRANG 2 • LUYỆN NGHE NÓI PHẢN XẠ HỘI THOẠI</div>
                <h2 class="banner-title">Luyện nghe nói phản xạ (Shadowing & Dịch Việt - Anh)</h2>
                <p class="banner-desc">Rèn luyện phản xạ hội thoại <strong>"{clean_title}"</strong> với 2 chế độ: <strong>Chế độ 1 - Đọc nhại Shadowing</strong> (nghe và nhại theo từng lượt thoại) & <strong>Chế độ 2 - Phản xạ dịch Việt - Anh</strong> (nghe câu thoại tiếng Việt và tự dịch sang tiếng Anh ngay trong khoảng dừng).</p>
            </div>
        </div>
        <div>
            <span class="banner-pill">
                <span>🎧</span>
                <span>2 Chế Độ Luyện Tập</span>
            </span>
        </div>
    </div>

    <div class="pod-card">
        <!-- MODE SELECTOR TABS -->
        <div class="pod-nav-tabs">
            <button id="tab-btn-shadowing" class="pod-nav-btn active">
                <span style="font-size: 16px;">🎧</span>
                <div>
                    <div style="line-height: 1.2;">Chế độ 1: Đọc Nhại Shadowing</div>
                    <div style="font-size: 10.5px; opacity: 0.8; font-weight: normal;">Nghe người bản xứ ➔ Nhại lại to rõ</div>
                </div>
            </button>
            <button id="tab-btn-reflex" class="pod-nav-btn">
                <span style="font-size: 16px;">🗣️</span>
                <div>
                    <div style="line-height: 1.2;">Chế độ 2: Phản Xạ Dịch Việt - Anh</div>
                    <div style="font-size: 10.5px; opacity: 0.8; font-weight: normal;">Nghe TV ➔ Tự dịch TA ➔ Đối chiếu đáp án</div>
                </div>
            </button>
        </div>

        <!-- HEADER -->
        <div id="pod-main-header" class="pod-header mode-shadowing">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div id="pod-mode-icon" style="width: 44px; height: 44px; background: rgba(255, 255, 255, 0.18); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px;">
                        🎧
                    </div>
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span id="pod-mode-tag" style="background: rgba(255,255,255,0.2); font-size: 11px; font-weight: 800; letter-spacing: 0.5px; padding: 3px 8px; border-radius: 6px; text-transform: uppercase;">Shadowing Podcast</span>
                            <span style="font-size: 12px; opacity: 0.9;">{total_sentences} lượt thoại thực tế</span>
                        </div>
                        <h2 id="pod-mode-title" style="margin: 4px 0 0 0; font-size: 18px; font-weight: 700; color: #ffffff;">Podcast Luyện Nghe & Đọc Nhại: {clean_title}</h2>
                    </div>
                </div>
                <div>
                    <span id="pod-badge-live" style="background: rgba(255,255,255,0.15); color: #ffffff; font-size: 12px; font-weight: 700; padding: 5px 12px; border-radius: 20px; display: inline-flex; align-items: center; gap: 6px; border: 1px solid rgba(255,255,255,0.25);">
                        <span style="width: 8px; height: 8px; background: #38bdf8; border-radius: 50%;"></span>
                        <span id="pod-badge-live-text">Khoảng lặng đọc theo: Đã bật</span>
                    </span>
                </div>
            </div>
            <p id="pod-mode-desc" style="margin: 10px 0 0 0; font-size: 13px; line-height: 1.5; color: #ffffff; opacity: 0.95;">
                💡 <strong>Phương pháp Shadowing:</strong> Nghe người bản xứ đọc mẫu từng lượt hội thoại ➔ Lặp lại to rõ trong khoảng lặng tiếp theo (được căn chỉnh tự động bằng độ dài câu + 1.5s).
            </p>
        </div>

        <!-- AUDIO CONTROLS & DISPLAY -->
        <div class="pod-body">
            <audio id="podcast-audio" preload="auto" playsinline webkit-playsinline src="{shadowing_audio_url}">
                <source id="audio-source-main" src="{shadowing_audio_url}" type="audio/mpeg">
            </audio>

            <!-- NOW PLAYING DISPLAY -->
            <div id="now-playing-box" class="pod-now-playing" style="border-left: 5px solid #0284c7;">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; flex-wrap: wrap; gap: 6px;">
                    <span id="np-pattern-tag" style="color: #0284c7; font-size: 11px; font-weight: 800; text-transform: uppercase;">HỘI THOẠI: {clean_title.upper()}</span>
                    <span id="np-turn-badge" style="background: #e0f2fe; color: #0369a1; font-size: 11.5px; font-weight: 700; padding: 3px 10px; border-radius: 12px;">🎧 Máy đọc mẫu</span>
                </div>
                <div id="np-primary-text" style="font-size: 16.5px; font-weight: 700; color: #0f172a; line-height: 1.45; margin-bottom: 4px;">
                    Nhấn "Bắt đầu nghe" bên dưới để luyện nghe và đọc nhại theo đoạn hội thoại...
                </div>
                <div id="np-secondary-text" style="font-size: 13.5px; color: #64748b; font-style: italic;">
                    (Audio sẽ đọc mẫu từng lượt thoại tiếng Anh, bạn nghe và đọc nhại lại theo trong khoảng lặng)
                </div>
            </div>

            <!-- PROGRESS BAR -->
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                <span id="time-current" style="font-family: monospace; font-size: 12px; font-weight: 600; color: #64748b; min-width: 42px;">00:00</span>
                <input id="podcast-progress" type="range" min="0" max="{sh_total_dur:.2f}" value="0" step="0.5" style="flex: 1; height: 6px; -webkit-appearance: none; appearance: none; background: #cbd5e1; border-radius: 4px; outline: none; cursor: pointer;">
                <span id="time-total" style="font-family: monospace; font-size: 12px; font-weight: 600; color: #64748b; min-width: 42px;">{format_time(sh_total_dur)}</span>
            </div>

            <!-- CONTROLS ROW -->
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <button id="btn-back-10" class="pod-btn-round" title="Lùi lại 10 giây">-10s</button>
                    <button id="btn-play-podcast" class="pod-btn-play shadowing">
                        <span id="play-icon">▶</span>
                        <span id="play-label">Bắt đầu nghe</span>
                    </button>
                    <button id="btn-forward-10" class="pod-btn-round" title="Tua tới 10 giây">+10s</button>
                </div>

                <!-- SPEED -->
                <div style="display: flex; align-items: center; gap: 4px; background: #ffffff; padding: 3px 6px; border-radius: 8px; border: 1px solid #e2e8f0;">
                    <span style="font-size: 11px; font-weight: 700; color: #64748b;">Tốc độ:</span>
                    <button class="pod-speed-btn" data-speed="0.8">0.8x</button>
                    <button class="pod-speed-btn active" data-speed="1.0">1.0x</button>
                    <button class="pod-speed-btn" data-speed="1.2">1.2x</button>
                </div>
            </div>
        </div>

        <!-- ACCORDION PLAYLIST (OPEN BY DEFAULT FOR DIALOGUES) -->
        <div style="background: #ffffff;">
            <button id="toggle-transcript-btn" style="width: 100%; text-align: left; padding: 13px 24px; background: #ffffff; border: none; border-bottom: 1px solid #f1f5f9; display: flex; align-items: center; justify-content: space-between; font-size: 13px; font-weight: 700; color: #334155; cursor: pointer;">
                <span id="playlist-title-label">📋 Danh sách các lượt hội thoại trong bài ({total_sentences} lượt thoại)</span>
                <span id="transcript-toggle-icon" style="color: #64748b; font-size: 11px;">▲ Thu gọn</span>
            </button>

            <div id="transcript-container" style="display: block; max-height: 520px; overflow-y: auto; padding: 16px 20px; background: #f8fafc;">
                <!-- JS renders items here -->
            </div>
        </div>
    </div>

    <!-- Bottom Flow Action back to Page 1 -->
    <div class="part-flow-action">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 24px;">💬</span>
            <div>
                <div style="font-size: 14px; font-weight: 700; color: #0f172a;">Muốn xem lại văn bản hội thoại & làm bài tập điền từ?</div>
                <div style="font-size: 12.5px; color: #475569; margin-top: 1px;">Quay về <strong>Trang 1</strong> để đóng vai nhân vật (Roleplay) và ôn tập từ vựng nhé!</div>
            </div>
        </div>
        <button class="part-flow-btn" onclick="window.parent.postMessage({{ type: 'LECTURE_SWITCH_PAGE', page: 1 }}, '*')">
            <span>⬅ Quay lại Trang 1: Bài Hội Thoại</span>
        </button>
    </div>
</div>

<script>
(function() {{
    var bundle = {js_bundle_str};
    var currentMode = 'shadowing'; // 'shadowing' or 'reflex'

    var audio = document.getElementById('podcast-audio');
    var tabReflex = document.getElementById('tab-btn-reflex');
    var tabShadowing = document.getElementById('tab-btn-shadowing');
    var header = document.getElementById('pod-main-header');
    var modeIcon = document.getElementById('pod-mode-icon');
    var modeTag = document.getElementById('pod-mode-tag');
    var modeTitle = document.getElementById('pod-mode-title');
    var modeDesc = document.getElementById('pod-mode-desc');
    var badgeLiveText = document.getElementById('pod-badge-live-text');
    var nowPlayingBox = document.getElementById('now-playing-box');
    var npPatternTag = document.getElementById('np-pattern-tag');
    var npTurnBadge = document.getElementById('np-turn-badge');
    var npPrimaryText = document.getElementById('np-primary-text');
    var npSecondaryText = document.getElementById('np-secondary-text');
    var playBtn = document.getElementById('btn-play-podcast');
    var playIcon = document.getElementById('play-icon');
    var playLabel = document.getElementById('play-label');
    var progressBar = document.getElementById('podcast-progress');
    var timeCurrent = document.getElementById('time-current');
    var timeTotal = document.getElementById('time-total');
    var toggleTranscriptBtn = document.getElementById('toggle-transcript-btn');
    var transcriptContainer = document.getElementById('transcript-container');
    var transcriptToggleIcon = document.getElementById('transcript-toggle-icon');
    var speedBtns = document.querySelectorAll('.pod-speed-btn');

    function fmtTime(sec) {{
        sec = Math.floor(sec || 0);
        var m = Math.floor(sec / 60);
        var s = sec % 60;
        return (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
    }}

    function getCurrentModeData() {{
        return bundle[currentMode];
    }}

    function seekAndPlay(timeSec) {{
        var mData = getCurrentModeData();
        var targetSrc = mData.storageMp3;

        if (!audio.src || !audio.src.includes('supabase.co')) {{
            audio.src = targetSrc;
            audio.preload = 'auto';
        }}

        var executeSeek = function() {{
            try {{
                audio.currentTime = timeSec;
            }} catch(err) {{
                console.warn('Seek currentTime warning:', err);
            }}
            var p = audio.play();
            if (p !== undefined) {{
                p.then(function() {{
                    playIcon.textContent = '⏸';
                    playLabel.textContent = 'Tạm dừng';
                }}).catch(function(err) {{
                    console.warn('Playback error:', err);
                }});
            }}
        }};

        if (audio.readyState >= 1) {{
            executeSeek();
        }} else {{
            var onLoaded = function() {{
                audio.removeEventListener('loadedmetadata', onLoaded);
                executeSeek();
            }};
            audio.addEventListener('loadedmetadata', onLoaded);
            audio.load();
        }}
    }}

    function renderPlaylist() {{
        var mData = getCurrentModeData();
        var html = '';
        var idx = 1;

        mData.patterns.forEach(function(p) {{
            html += '<div style="margin-bottom: 10px;">';
            html += '  <div style="font-size: 12.5px; font-weight: 700; color: #1e293b; padding: 7px 12px; background: #e2e8f0; border-radius: 8px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">';
            html += '    <span>💬 Hội thoại ' + p.pattern_num + ': ' + p.pattern_title + '</span>';
            if (p.pattern_translation) {{
                html += '    <span style="font-size: 11.5px; color: #475569; font-weight: 600;">' + p.pattern_translation + '</span>';
            }}
            html += '  </div>';

            p.sentences.forEach(function(s) {{
                var rowId = 'pod-row-' + currentMode + '-' + s.audio_key;
                var roleClass = s.role === 'B' ? 'role-B' : 'role-A';
                var speakerPrefix = s.speaker ? ('<span class="speaker-chip ' + roleClass + '">' + s.speaker + '</span>') : '';
                html += '  <div id="' + rowId + '" class="pod-row" data-start="' + s.start_time + '" style="cursor: pointer;">';
                html += '    <div style="display: flex; align-items: flex-start; gap: 10px; flex: 1; padding-right: 10px;">';
                html += '      <span style="font-size: 11px; font-weight: 700; color: #94a3b8; min-width: 22px; padding-top: 3px;">#' + idx + '</span>';
                html += '      <div style="flex: 1;">';
                if (currentMode === 'reflex') {{
                    html += '        <div style="font-size: 13.5px; font-weight: 700; color: #1e293b; line-height: 1.45;">' + speakerPrefix + '🇻🇳 ' + (s.translation_vi || s.translation || '') + '</div>';
                    html += '        <div style="font-size: 12.5px; color: #4338ca; font-weight: 600; margin-top: 3px; line-height: 1.4;">🇬🇧 ' + s.sentence + '</div>';
                }} else {{
                    html += '        <div style="font-size: 13.5px; font-weight: 700; color: #0f172a; line-height: 1.45;">' + speakerPrefix + s.sentence + '</div>';
                    html += '        <div style="font-size: 12px; color: #64748b; margin-top: 3px; line-height: 1.4;">' + (s.translation || s.translation_vi || '') + '</div>';
                }}
                html += '      </div>';
                html += '    </div>';
                html += '    <div style="display: flex; align-items: center; gap: 8px;">';
                html += '      <span class="pod-row-play-btn"><span>▶</span> <span>' + fmtTime(s.start_time) + '</span></span>';
                html += '    </div>';
                html += '  </div>';
                idx++;
            }});
            html += '</div>';
        }});

        transcriptContainer.innerHTML = html;

        var rows = transcriptContainer.querySelectorAll('.pod-row');
        rows.forEach(function(r) {{
            r.addEventListener('click', function(e) {{
                e.preventDefault();
                var st = parseFloat(this.getAttribute('data-start'));
                if (!isNaN(st)) {{
                    seekAndPlay(st);
                }}
            }});
        }});
    }}

    function applyModeUI(mode) {{
        currentMode = mode;
        var wasPlaying = !audio.paused && audio.currentTime > 0;
        var mData = getCurrentModeData();

        audio.pause();
        audio.src = mData.storageMp3;
        audio.preload = 'auto';
        audio.load();

        progressBar.max = mData.totalDur;
        progressBar.value = 0;
        timeCurrent.textContent = '00:00';
        timeTotal.textContent = fmtTime(mData.totalDur);
        playIcon.textContent = '▶';
        playLabel.textContent = 'Bắt đầu nghe';

        if (mode === 'reflex') {{
            tabReflex.className = 'pod-nav-btn active reflex-active';
            tabShadowing.className = 'pod-nav-btn';
            header.className = 'pod-header mode-reflex';
            modeIcon.textContent = '🗣️';
            modeTag.textContent = 'Phản Xạ Dịch Song Ngữ';
            modeTitle.textContent = 'Podcast Phản Xạ Dịch Việt - Anh: ' + bundle.cleanTitle;
            modeDesc.innerHTML = '💡 <strong>Phương pháp Phản Xạ:</strong> Lắng nghe lượt thoại tiếng Việt ➔ Tự nói to câu dịch tiếng Anh trong khoảng dừng ➔ Nghe người bản xứ đọc đáp án chuẩn để đối chiếu.';
            badgeLiveText.textContent = 'Khoảng dừng dịch: Đã bật';
            nowPlayingBox.style.borderLeftColor = '#6366f1';
            npPatternTag.style.color = '#4f46e5';
            npPatternTag.textContent = 'HỘI THOẠI: ' + bundle.cleanTitle.toUpperCase();
            npTurnBadge.style.background = '#e0e7ff';
            npTurnBadge.style.color = '#4338ca';
            npTurnBadge.textContent = '🇻🇳 Sẵn sàng luyện tập';
            npPrimaryText.textContent = 'Nhấn "Bắt đầu nghe" bên dưới để khởi động phản xạ dịch hội thoại...';
            npSecondaryText.textContent = '(Audio sẽ đọc tiếng Việt trước, bạn dịch sang tiếng Anh, sau đó đối chiếu với đáp án chuẩn)';
            playBtn.className = 'pod-btn-play reflex';
        }} else {{
            tabReflex.className = 'pod-nav-btn';
            tabShadowing.className = 'pod-nav-btn active';
            header.className = 'pod-header mode-shadowing';
            modeIcon.textContent = '🎧';
            modeTag.textContent = 'Shadowing Podcast';
            modeTitle.textContent = 'Podcast Luyện Nghe & Đọc Nhại: ' + bundle.cleanTitle;
            modeDesc.innerHTML = '💡 <strong>Phương pháp Shadowing:</strong> Nghe người bản xứ đọc mẫu từng lượt hội thoại ➔ Lặp lại to rõ trong khoảng lặng tiếp theo (được căn chỉnh tự động bằng độ dài câu + 1.5s).';
            badgeLiveText.textContent = 'Khoảng lặng đọc theo: Đã bật';
            nowPlayingBox.style.borderLeftColor = '#0284c7';
            npPatternTag.style.color = '#0284c7';
            npPatternTag.textContent = 'HỘI THOẠI: ' + bundle.cleanTitle.toUpperCase();
            npTurnBadge.style.background = '#e0f2fe';
            npTurnBadge.style.color = '#0369a1';
            npTurnBadge.textContent = '🎧 Máy đọc mẫu';
            npPrimaryText.textContent = 'Nhấn "Bắt đầu nghe" để luyện nghe và đọc nhại theo đoạn hội thoại...';
            npSecondaryText.textContent = '(Nhấn nút phát để bắt đầu nghe toàn bộ ' + bundle.totalSentences + ' lượt hội thoại)';
            playBtn.className = 'pod-btn-play shadowing';
        }}

        renderPlaylist();
        if (wasPlaying) {{
            seekAndPlay(0);
        }}
    }}

    tabReflex.addEventListener('click', function() {{ applyModeUI('reflex'); }});
    tabShadowing.addEventListener('click', function() {{ applyModeUI('shadowing'); }});

    playBtn.addEventListener('click', function(e) {{
        e.preventDefault();
        var mData = getCurrentModeData();
        if (!audio.src || !audio.src.includes('supabase.co')) {{
            audio.src = mData.storageMp3;
        }}

        if (audio.paused) {{
            var playPromise = audio.play();
            if (playPromise !== undefined) {{
                playPromise.then(function() {{
                    playIcon.textContent = '⏸';
                    playLabel.textContent = 'Tạm dừng';
                }}).catch(function(err) {{
                    console.warn('Playback error, reloading from storage:', err);
                    audio.src = mData.storageMp3;
                    audio.load();
                    audio.play();
                }});
            }}
        }} else {{
            audio.pause();
            playIcon.textContent = '▶';
            playLabel.textContent = 'Tiếp tục nghe';
        }}
    }});

    audio.addEventListener('play', function() {{
        playIcon.textContent = '⏸';
        playLabel.textContent = 'Tạm dừng';
    }});

    audio.addEventListener('pause', function() {{
        playIcon.textContent = '▶';
        playLabel.textContent = 'Tiếp tục nghe';
    }});

    audio.addEventListener('loadedmetadata', function() {{
        if (audio.duration && !isNaN(audio.duration) && audio.duration > 0) {{
            progressBar.max = audio.duration;
            timeTotal.textContent = fmtTime(audio.duration);
        }}
    }});

    audio.addEventListener('error', function() {{
        console.warn('Audio load error:', audio.error);
        var mData = getCurrentModeData();
        if (audio.src !== mData.storageMp3) {{
            audio.src = mData.storageMp3;
            audio.load();
        }}
    }});

    document.getElementById('btn-back-10').addEventListener('click', function(e) {{
        e.preventDefault();
        audio.currentTime = Math.max(0, audio.currentTime - 10);
    }});

    document.getElementById('btn-forward-10').addEventListener('click', function(e) {{
        e.preventDefault();
        audio.currentTime = Math.min(audio.duration || 9999, audio.currentTime + 10);
    }});

    speedBtns.forEach(function(btn) {{
        btn.addEventListener('click', function(e) {{
            e.preventDefault();
            var spd = parseFloat(this.getAttribute('data-speed'));
            audio.playbackRate = spd;
            speedBtns.forEach(function(b) {{ b.classList.remove('active'); }});
            this.classList.add('active');
        }});
    }});

    progressBar.addEventListener('input', function() {{
        audio.currentTime = parseFloat(this.value);
    }});

    audio.addEventListener('timeupdate', function() {{
        var t = audio.currentTime;
        progressBar.value = t;
        timeCurrent.textContent = fmtTime(t);

        var mData = getCurrentModeData();
        var activeSentence = null;
        var activePattern = null;

        for (var i = 0; i < mData.patterns.length; i++) {{
            var p = mData.patterns[i];
            for (var j = 0; j < p.sentences.length; j++) {{
                var s = p.sentences[j];
                var endT = s.end_time || (s.start_time + s.duration + (s.pause_duration || 0));
                if (t >= s.start_time && t < endT) {{
                    activeSentence = s;
                    activePattern = p;
                    break;
                }}
            }}
            if (activeSentence) break;
        }}

        if (!activeSentence) return;

        var spkTag = activeSentence.speaker ? (' • 👤 ' + activeSentence.speaker.toUpperCase()) : '';
        npPatternTag.textContent = 'LƯỢT THOẠI #' + (activeSentence.turn_num || 1) + '/' + bundle.totalSentences + spkTag;

        var allRows = transcriptContainer.querySelectorAll('.pod-row');
        allRows.forEach(function(r) {{
            r.classList.remove('active-speaking', 'active-turn', 'active-answer');
        }});

        var curRow = document.getElementById('pod-row-' + currentMode + '-' + activeSentence.audio_key);
        var spkLabel = activeSentence.speaker ? (activeSentence.speaker + ': ') : '';

        if (currentMode === 'reflex') {{
            if (t < activeSentence.pause_reflex_start) {{
                npTurnBadge.style.background = '#e0e7ff';
                npTurnBadge.style.color = '#4338ca';
                npTurnBadge.textContent = '🇻🇳 1. Lắng nghe tiếng Việt (' + (activeSentence.speaker || '') + ')';
                npPrimaryText.textContent = spkLabel + (activeSentence.translation_vi || '');
                npSecondaryText.textContent = '⏳ Chuẩn bị nói câu dịch tiếng Anh...';
                if (curRow) curRow.classList.add('active-speaking');
            }} else if (t < activeSentence.en_start) {{
                npTurnBadge.style.background = '#fef3c7';
                npTurnBadge.style.color = '#b45309';
                npTurnBadge.textContent = '🗣️ 2. Lượt bạn: Dịch sang tiếng Anh ngay!';
                npPrimaryText.textContent = spkLabel + (activeSentence.translation_vi || '');
                npSecondaryText.textContent = '👉 Hãy nói to câu tiếng Anh của ' + (activeSentence.speaker || 'nhân vật') + '!';
                if (curRow) curRow.classList.add('active-turn');
            }} else if (t < activeSentence.pause_absorb_start) {{
                npTurnBadge.style.background = '#dcfce7';
                npTurnBadge.style.color = '#15803d';
                npTurnBadge.textContent = '🇬🇧 3. Đáp án tiếng Anh chuẩn (' + (activeSentence.speaker || '') + ')';
                npPrimaryText.textContent = spkLabel + activeSentence.sentence;
                npSecondaryText.textContent = '🇻🇳 (' + (activeSentence.translation_vi || '') + ')';
                if (curRow) curRow.classList.add('active-answer');
            }} else {{
                npTurnBadge.style.background = '#ccfbf1';
                npTurnBadge.style.color = '#0f766e';
                npTurnBadge.textContent = '✨ 4. Ngẫm & đối chiếu phát âm';
                npPrimaryText.textContent = spkLabel + activeSentence.sentence;
                npSecondaryText.textContent = '🇻🇳 (' + (activeSentence.translation_vi || '') + ')';
                if (curRow) curRow.classList.add('active-answer');
            }}
        }} else {{
            var speakEnd = activeSentence.start_time + activeSentence.duration;
            if (t < speakEnd) {{
                npTurnBadge.style.background = '#e0f2fe';
                npTurnBadge.style.color = '#0369a1';
                npTurnBadge.textContent = '🎧 Máy đọc mẫu (' + (activeSentence.speaker || '') + ')';
                if (curRow) curRow.classList.add('active-speaking');
            }} else {{
                npTurnBadge.style.background = '#fef9c3';
                npTurnBadge.style.color = '#854d0e';
                npTurnBadge.textContent = '🗣️ Lượt bạn: Đọc nhại theo (' + (activeSentence.speaker || '') + ')';
                if (curRow) curRow.classList.add('active-turn');
            }}
            npPrimaryText.textContent = spkLabel + activeSentence.sentence;
            npSecondaryText.textContent = activeSentence.translation ? '(' + activeSentence.translation + ')' : '';
        }}

        if (curRow && transcriptContainer.style.display !== 'none') {{
            var rTop = curRow.offsetTop - transcriptContainer.offsetTop;
            if (rTop < transcriptContainer.scrollTop || rTop > transcriptContainer.scrollTop + transcriptContainer.clientHeight - 80) {{
                transcriptContainer.scrollTop = rTop - 40;
            }}
        }}
    }});

    toggleTranscriptBtn.addEventListener('click', function(e) {{
        e.preventDefault();
        var isHidden = transcriptContainer.style.display === 'none';
        transcriptContainer.style.display = isHidden ? 'block' : 'none';
        transcriptToggleIcon.textContent = isHidden ? '▲ Thu gọn' : '▼ Mở rộng danh sách';
    }});

    // Initialize with Shadowing mode
    applyModeUI('shadowing');
}})();
</script>
"""
    return html


def append_page1_cta(orig_html, clean_title):
    cta_marker = "<!-- CTA_TO_PAGE_2_PODCAST -->"
    if cta_marker in orig_html:
        return orig_html

    cta_html = f"""
{cta_marker}
<div style="margin-top: 28px; padding: 18px 22px; border-radius: 14px; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1.5px dashed #38bdf8; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; font-family: Arial, sans-serif;">
    <div style="display: flex; align-items: center; gap: 12px;">
        <span style="font-size: 28px;">🎧</span>
        <div>
            <div style="font-size: 15px; font-weight: bold; color: #0369a1;">Đã nắm vững nội dung đoạn hội thoại "{clean_title}"?</div>
            <div style="font-size: 13px; color: #0284c7; margin-top: 2px;">Chuyển sang <strong>Trang 2</strong> để luyện <strong>Podcast Đọc nhại Shadowing & Phản xạ dịch Việt - Anh</strong> nhé!</div>
        </div>
    </div>
    <button type="button" onclick="window.parent.postMessage({{ type: 'LECTURE_SWITCH_PAGE', page: 2 }}, '*')" style="border: none; border-radius: 25px; padding: 11px 22px; font-size: 14px; font-weight: bold; color: #ffffff; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); cursor: pointer; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);">
        <span>🎧 Sang Trang 2: Luyện Podcast Shadowing & Phản Xạ</span>
        <span>➔</span>
    </button>
</div>
"""
    return orig_html.rstrip() + "\n" + cta_html


def main():
    print("=== Step 1: Uploading 20 Dialogue Podcast MP3 files to Supabase Storage ===")
    for d in dialogues_data:
        slug = d['slug']
        for fn in [f"podcast_shadowing_{slug}.mp3", f"podcast_reflex_vi_en_{slug}.mp3"]:
            local_p = os.path.join(PODCAST_DIR, fn)
            if not os.path.exists(local_p):
                raise FileNotFoundError(f"Missing MP3: {local_p}")
            ok = upload_file_to_supabase(local_p, fn)
            if not ok:
                print(f"ERROR uploading {fn}")
                sys.exit(1)

    print("\n=== Step 2: Updating Page 1 CTA and Inserting/Updating Page 2 in Supabase DB ===")
    for d in dialogues_data:
        lec_id = d['lecture_id']
        slug = d['slug']
        clean_title = d['clean_title']

        # 1. Update Page 1 with bottom CTA button to Page 2
        p1_rows = supabase.table('lecture_pages').select('id, content_html').eq('lecture_id', lec_id).eq('page_number', 1).execute().data
        if p1_rows:
            p1_id = p1_rows[0]['id']
            new_p1_html = append_page1_cta(p1_rows[0]['content_html'], clean_title)
            if new_p1_html != p1_rows[0]['content_html']:
                supabase.table('lecture_pages').update({'content_html': new_p1_html}).eq('id', p1_id).execute()

        # 2. Generate and upsert Page 2
        page2_html = generate_dialogue_page2_html(d)
        p2_rows = supabase.table('lecture_pages').select('id').eq('lecture_id', lec_id).eq('page_number', 2).execute().data
        if p2_rows:
            p2_id = p2_rows[0]['id']
            supabase.table('lecture_pages').update({'content_html': page2_html}).eq('id', p2_id).execute()
            print(f"  [Updated Page 2] [{slug}] {d['lecture_title']} (page_id={p2_id}, {len(page2_html)} chars)")
        else:
            p2_id = str(uuid.uuid4())
            supabase.table('lecture_pages').insert({
                'id': p2_id,
                'lecture_id': lec_id,
                'page_number': 2,
                'content_html': page2_html
            }).execute()
            print(f"  [Inserted Page 2] [{slug}] {d['lecture_title']} (page_id={p2_id}, {len(page2_html)} chars)")

    print("\n🎉 ALL 10 DIALOGUE LECTURES UPDATED WITH PAGE 2 SHADOWING & REFLEX PODCASTS!")


if __name__ == '__main__':
    main()
