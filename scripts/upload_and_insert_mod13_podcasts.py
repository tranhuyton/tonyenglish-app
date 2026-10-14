import os
import sys
import json
import uuid
import urllib.request
from bs4 import BeautifulSoup
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
EN_AUDIO_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'sentences')
STORAGE_PODCAST_PREFIX = "audio/communication/podcasts"
STORAGE_SENTENCE_PREFIX = "audio/communication/sentences"
STORAGE_BASE = f"{SUPABASE_URL}/storage/v1/object/public/test_assets/{STORAGE_PODCAST_PREFIX}"

with open('scratch/mod13_lectures_data.json', 'r', encoding='utf-8') as f:
    mod13_data = json.load(f)


def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"


def upload_file_to_supabase(local_path, storage_path):
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
                    kb = len(data) / 1024
                    print(f"  [Uploaded] {storage_path} ({kb:.0f} KB)")
                    return True
        except Exception as e:
            print(f"  [Retry {attempt}/3] {storage_path}: {e}")
    return False


def generate_mod13_page2_html(lec):
    slug = lec['slug']
    clean_title = lec['clean_title']
    mod_title = lec['module_title']

    sh_json_path = os.path.join(PODCAST_DIR, f"podcast_shadowing_{slug}.json")
    rf_json_path = os.path.join(PODCAST_DIR, f"podcast_reflex_vi_en_{slug}.json")

    with open(sh_json_path, 'r', encoding='utf-8') as f:
        sh_data = json.load(f)
    with open(rf_json_path, 'r', encoding='utf-8') as f:
        rf_data = json.load(f)

    sh_dur = sh_data['total_duration']
    rf_dur = rf_data['total_duration']

    sh_patterns = sh_data['patterns']
    rf_patterns = rf_data['patterns']
    total_dialogues = len(sh_patterns)
    total_sentences = sum(len(p['sentences']) for p in sh_patterns)

    sh_storage_mp3 = f"{STORAGE_BASE}/podcast_shadowing_{slug}.mp3"
    rf_storage_mp3 = f"{STORAGE_BASE}/podcast_reflex_vi_en_{slug}.mp3"
    sh_local_mp3 = f"/audio/communication/podcasts/podcast_shadowing_{slug}.mp3"
    rf_local_mp3 = f"/audio/communication/podcasts/podcast_reflex_vi_en_{slug}.mp3"

    dual_bundle = {
        "slug": slug,
        "module": mod_title,
        "cleanTitle": clean_title,
        "totalDialogues": total_dialogues,
        "totalSentences": total_sentences,
        "shadowing": {
            "title": sh_data["title"],
            "localMp3": sh_local_mp3,
            "storageMp3": sh_storage_mp3,
            "totalDur": sh_dur,
            "patterns": sh_patterns
        },
        "reflex": {
            "title": rf_data["title"],
            "localMp3": rf_local_mp3,
            "storageMp3": rf_storage_mp3,
            "totalDur": rf_dur,
            "patterns": rf_patterns
        }
    }

    bundle_json_str = json.dumps(dual_bundle, ensure_ascii=False)

    html = f"""<meta charset="utf-8"/>
<style>
    .pod-page-wrap {{
        max-width: 900px;
        margin: 0 auto;
        font-family: Arial, sans-serif;
        color: #1e293b;
        padding: 4px 0 36px 0;
    }}
    .pod-top-nav {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 18px;
        background: #f1f5f9;
        padding: 8px;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
    }}
    .pod-nav-btn {{
        flex: 1;
        min-width: 220px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        padding: 12px 16px;
        border-radius: 10px;
        font-size: 13.5px;
        font-weight: 700;
        cursor: pointer;
        border: 1.5px solid transparent;
        background: transparent;
        color: #475569;
        transition: all 0.2s ease;
    }}
    .pod-nav-btn:hover {{
        background: #ffffff;
        color: #0f172a;
    }}
    .pod-nav-btn.active {{
        background: #ffffff;
        color: #0284c7;
        border-color: #bae6fd;
        box-shadow: 0 2px 8px rgba(2, 132, 199, 0.12);
    }}
    .pod-nav-btn.active.reflex-active {{
        color: #4f46e5;
        border-color: #c7d2fe;
        box-shadow: 0 2px 8px rgba(79, 70, 229, 0.15);
    }}
    .pod-card {{
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #cbd5e1;
        background: #ffffff;
        box-shadow: 0 8px 25px -5px rgba(15, 23, 42, 0.08);
    }}
    .pod-header {{
        padding: 22px 24px;
        color: #ffffff;
        transition: background 0.3s ease;
    }}
    .pod-header.mode-shadowing {{
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #0284c7 100%);
    }}
    .pod-header.mode-reflex {{
        background: linear-gradient(135deg, #1e1b4b 0%, #3730a3 55%, #6366f1 100%);
    }}
    .pod-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.15);
        color: #f8fafc;
        font-size: 11.5px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.25);
    }}
    .pod-jump-bar {{
        display: flex;
        align-items: center;
        gap: 6px;
        flex-wrap: wrap;
        padding: 12px 20px;
        background: #f8fafc;
        border-bottom: 1px solid #e2e8f0;
    }}
    .pod-jump-pill {{
        border: 1px solid #cbd5e1;
        background: #ffffff;
        color: #334155;
        font-size: 12px;
        font-weight: 700;
        padding: 5px 11px;
        border-radius: 18px;
        cursor: pointer;
        transition: all 0.15s ease;
        display: inline-flex;
        align-items: center;
        gap: 5px;
    }}
    .pod-jump-pill:hover {{
        border-color: #0284c7;
        color: #0284c7;
        background: #f0f9ff;
    }}
    .pod-jump-pill.active-dialogue {{
        background: #0284c7;
        color: #ffffff;
        border-color: #0284c7;
        box-shadow: 0 2px 6px rgba(2, 132, 199, 0.25);
    }}
    .pod-jump-pill.active-dialogue.reflex-pill {{
        background: #4f46e5;
        border-color: #4f46e5;
        box-shadow: 0 2px 6px rgba(79, 70, 229, 0.25);
    }}
    .pod-btn-play {{
        border: none;
        border-radius: 30px;
        padding: 12px 28px;
        font-size: 15px;
        font-weight: 700;
        color: #ffffff;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        transition: transform 0.15s, box-shadow 0.15s;
    }}
    .pod-btn-play.shadowing {{
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
    }}
    .pod-btn-play.reflex {{
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
    }}
    .pod-btn-sec {{
        border: 1px solid #cbd5e1;
        background: #ffffff;
        color: #334155;
        border-radius: 20px;
        padding: 8px 14px;
        font-size: 13px;
        font-weight: 700;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 4px;
        transition: all 0.15s;
    }}
    .pod-btn-sec:hover {{
        background: #f1f5f9;
        border-color: #94a3b8;
    }}
    .pod-speed-btn {{
        border: 1px solid #cbd5e1;
        background: #ffffff;
        color: #475569;
        border-radius: 8px;
        padding: 5px 10px;
        font-size: 12px;
        font-weight: 700;
        cursor: pointer;
    }}
    .pod-speed-btn.active {{
        background: #0f172a;
        color: #ffffff;
        border-color: #0f172a;
    }}
    .pod-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 11px 14px;
        margin-bottom: 6px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        background: #ffffff;
        cursor: pointer;
        transition: all 0.15s ease;
    }}
    .pod-row:hover {{
        border-color: #93c5fd;
        background: #f8fafc;
    }}
    .pod-row.active-speaking {{
        border-color: #0284c7;
        background: #e0f2fe;
        box-shadow: 0 2px 8px rgba(2, 132, 199, 0.12);
    }}
    .pod-row.active-turn {{
        border-color: #f59e0b;
        background: #fef3c7;
        box-shadow: 0 2px 8px rgba(245, 158, 11, 0.16);
    }}
    .pod-row.active-answer {{
        border-color: #10b981;
        background: #d1fae5;
        box-shadow: 0 2px 8px rgba(16, 185, 129, 0.15);
    }}
    .pod-row-play-btn {{
        border: none;
        background: #f1f5f9;
        color: #0284c7;
        font-size: 12px;
        font-weight: 700;
        padding: 6px 12px;
        border-radius: 16px;
        cursor: pointer;
        white-space: nowrap;
        display: inline-flex;
        align-items: center;
        gap: 4px;
        transition: all 0.15s;
    }}
    .pod-row:hover .pod-row-play-btn {{
        background: #0284c7;
        color: #ffffff;
    }}
    .speaker-chip {{
        display: inline-block;
        font-size: 11px;
        font-weight: 800;
        padding: 2px 8px;
        border-radius: 6px;
        margin-right: 6px;
        text-transform: uppercase;
    }}
    .speaker-chip.role-A {{
        background: #dbeafe;
        color: #1d4ed8;
    }}
    .speaker-chip.role-B {{
        background: #FCE7F3;
        color: #be185d;
    }}
    input[type=range].pod-range {{
        -webkit-appearance: none;
        width: 100%;
        height: 8px;
        border-radius: 6px;
        background: #cbd5e1;
        outline: none;
        cursor: pointer;
    }}
    input[type=range].pod-range::-webkit-slider-thumb {{
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #0284c7;
        cursor: pointer;
        border: 2px solid #ffffff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.3);
    }}
</style>

<div class="pod-page-wrap">
    <!-- Top Mode Switcher -->
    <div class="pod-top-nav">
        <button type="button" id="tab-mode-shadowing" class="pod-nav-btn active">
            <span style="font-size: 16px;">🎧</span>
            <span>Chế độ 1: Đọc Nhại Shadowing</span>
        </button>
        <button type="button" id="tab-mode-reflex" class="pod-nav-btn">
            <span style="font-size: 16px;">🗣️</span>
            <span>Chế độ 2: Phản Xạ Dịch Việt - Anh</span>
        </button>
    </div>

    <!-- Main Podcast Card -->
    <div class="pod-card">
        <!-- Dynamic Header -->
        <div id="pod-header" class="pod-header mode-shadowing">
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 10px; margin-bottom: 12px;">
                <span class="pod-badge">
                    <span id="pod-mode-icon">🎧</span>
                    <span id="pod-mode-tag">Shadowing Podcast</span>
                    <span>•</span>
                    <span>{mod_title}</span>
                </span>
                <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                    <span class="pod-badge" id="pod-badge-count">💬 {total_dialogues} hội thoại • {total_sentences} lượt thoại</span>
                    <span class="pod-badge" id="pod-badge-live" style="background: rgba(56, 189, 248, 0.25);">⏱️ <span id="pod-badge-live-text">Khoảng lặng đọc theo: Đã bật</span></span>
                </div>
            </div>
            <h3 id="pod-title" style="margin: 0 0 8px 0; font-size: 20px; font-weight: 800; color: #ffffff; line-height: 1.35;">
                Podcast Luyện Nghe &amp; Đọc Nhại: {clean_title}
            </h3>
            <p id="pod-desc" style="margin: 0; font-size: 13.5px; color: #e2e8f0; line-height: 1.55;">
                💡 <strong>Phương pháp Shadowing:</strong> Nghe người bản xứ đọc mẫu từng lượt hội thoại ➔ Lặp lại to rõ trong khoảng lặng tiếp theo (được căn chỉnh tự động bằng độ dài câu + 1.5s).
            </p>
        </div>

        <!-- Quick-Jump Dialogue Selector -->
        <div class="pod-jump-bar" id="pod-jump-bar">
            <span style="font-size: 11.5px; font-weight: 800; color: #64748b; text-transform: uppercase; margin-right: 4px;">Chuyển nhanh:</span>
        </div>

        <!-- Player Body -->
        <div style="padding: 20px 24px; background: #f8fafc;">
            <!-- Live Status Box -->
            <div id="now-playing-box" style="background: #ffffff; border: 2px solid #e2e8f0; border-left: 5px solid #0284c7; border-radius: 12px; padding: 16px 18px; margin-bottom: 18px; min-height: 92px; display: flex; flex-direction: column; justify-content: center; transition: all 0.2s;">
                <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 6px; flex-wrap: wrap;">
                    <span id="np-pattern-tag" style="font-size: 12px; font-weight: 700; color: #0284c7; text-transform: uppercase; letter-spacing: 0.4px;">
                        CHỦ ĐỀ: {clean_title.upper()} ({total_dialogues} HỘI THOẠI)
                    </span>
                    <span id="np-turn-badge" style="font-size: 12px; font-weight: 800; padding: 3px 12px; border-radius: 14px; background: #e0f2fe; color: #0369a1;">
                        🎧 Máy đọc mẫu
                    </span>
                </div>
                <div id="np-primary-text" style="font-size: 17px; font-weight: 800; color: #0f172a; line-height: 1.45; margin-bottom: 4px;">
                    Nhấn "Bắt đầu nghe" để luyện nghe và đọc nhại theo {total_dialogues} đoạn hội thoại...
                </div>
                <div id="np-secondary-text" style="font-size: 13.5px; color: #64748b; font-style: italic;">
                    (Bạn có thể nghe liên tục từ đầu đến cuối hoặc bấm vào từng hội thoại / từng câu bên dưới để nghe ngay câu đó)
                </div>
            </div>

            <!-- Audio Element -->
            <audio id="pod-audio" preload="auto" style="display:none;">
                <source id="pod-source-storage" src="{sh_storage_mp3}" type="audio/mpeg" />
                <source id="pod-source-local" src="{sh_local_mp3}" type="audio/mpeg" />
            </audio>

            <!-- Seek Bar -->
            <div style="margin-bottom: 16px;">
                <input type="range" id="pod-progress" class="pod-range" value="0" min="0" max="{sh_dur}" step="0.1" />
                <div style="display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; color: #64748b; margin-top: 6px;">
                    <span id="pod-time-current">00:00</span>
                    <span id="pod-time-total">{format_time(sh_dur)}</span>
                </div>
            </div>

            <!-- Controls Row -->
            <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px;">
                <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                    <button type="button" id="btn-back-10" class="pod-btn-sec" title="Tua lùi 10 giây">⏪ -10s</button>
                    <button type="button" id="btn-play-toggle" class="pod-btn-play shadowing">
                        <span id="play-icon">▶</span>
                        <span id="play-label">Bắt đầu nghe</span>
                    </button>
                    <button type="button" id="btn-forward-10" class="pod-btn-sec" title="Tua tới 10 giây">+10s ⏩</button>
                </div>

                <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
                    <span style="font-size: 12px; font-weight: 700; color: #64748b; margin-right: 2px;">Tốc độ:</span>
                    <button type="button" class="pod-speed-btn" data-speed="0.75">0.75x</button>
                    <button type="button" class="pod-speed-btn" data-speed="0.9">0.9x</button>
                    <button type="button" class="pod-speed-btn active" data-speed="1">1.0x</button>
                    <button type="button" class="pod-speed-btn" data-speed="1.15">1.15x</button>
                </div>
            </div>
        </div>

        <!-- Playlist / Transcript Section -->
        <div style="border-top: 1px solid #e2e8f0; background: #ffffff;">
            <div id="btn-toggle-transcript" style="padding: 13px 24px; background: #f1f5f9; cursor: pointer; display: flex; align-items: center; justify-content: space-between; font-size: 13.5px; font-weight: 700; color: #334155; user-select: none;">
                <span>📋 Danh sách {total_dialogues} hội thoại &amp; lời dịch ({total_sentences} lượt thoại — Nhấn vào câu bất kỳ để phát từ câu đó)</span>
                <span id="transcript-toggle-icon" style="color: #0284c7;">▲ Thu gọn</span>
            </div>

            <div id="pod-transcript-container" style="padding: 16px 20px; max-height: 560px; overflow-y: auto; background: #f8fafc;">
            </div>
        </div>
    </div>

    <!-- Bottom Back to Page 1 Button -->
    <div style="margin-top: 22px; display: flex; justify-content: flex-start;">
        <button type="button" onclick="window.parent.postMessage({{ type: 'LECTURE_SWITCH_PAGE', page: 1 }}, '*')" class="pod-btn-sec" style="padding: 10px 18px; border-radius: 12px; font-size: 13.5px;">
            <span>⬅</span>
            <span>Quay lại Trang 1: Bài Học &amp; Hội Thoại</span>
        </button>
    </div>
</div>

<script id="podcast-dual-bundle" type="application/json">
{bundle_json_str}
</script>

<script>
(function() {{
    var bundleEl = document.getElementById('podcast-dual-bundle');
    if (!bundleEl) return;
    var bundle = JSON.parse(bundleEl.textContent);

    var currentMode = 'shadowing';
    var audio = document.getElementById('pod-audio');
    var playBtn = document.getElementById('btn-play-toggle');
    var playIcon = document.getElementById('play-icon');
    var playLabel = document.getElementById('play-label');
    var progressBar = document.getElementById('pod-progress');
    var timeCurrent = document.getElementById('pod-time-current');
    var timeTotal = document.getElementById('pod-time-total');

    var tabShadowing = document.getElementById('tab-mode-shadowing');
    var tabReflex = document.getElementById('tab-mode-reflex');
    var header = document.getElementById('pod-header');
    var modeIcon = document.getElementById('pod-mode-icon');
    var modeTag = document.getElementById('pod-mode-tag');
    var modeTitle = document.getElementById('pod-title');
    var modeDesc = document.getElementById('pod-desc');
    var badgeLiveText = document.getElementById('pod-badge-live-text');
    var jumpBar = document.getElementById('pod-jump-bar');

    var nowPlayingBox = document.getElementById('now-playing-box');
    var npPatternTag = document.getElementById('np-pattern-tag');
    var npTurnBadge = document.getElementById('np-turn-badge');
    var npPrimaryText = document.getElementById('np-primary-text');
    var npSecondaryText = document.getElementById('np-secondary-text');

    var transcriptContainer = document.getElementById('pod-transcript-container');
    var toggleTranscriptBtn = document.getElementById('btn-toggle-transcript');
    var transcriptToggleIcon = document.getElementById('transcript-toggle-icon');
    var speedBtns = document.querySelectorAll('.pod-speed-btn');

    function fmtTime(sec) {{
        if (!sec || isNaN(sec) || sec < 0) return '00:00';
        var m = Math.floor(sec / 60);
        var s = Math.floor(sec % 60);
        return (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
    }}

    function getCurrentModeData() {{
        return currentMode === 'reflex' ? bundle.reflex : bundle.shadowing;
    }}

    function seekAndPlay(targetTime) {{
        var mData = getCurrentModeData();
        if (!audio.src || (!audio.src.includes(mData.storageMp3) && !audio.src.includes(mData.localMp3))) {{
            audio.src = mData.storageMp3;
        }}

        var doSeek = function() {{
            try {{
                audio.currentTime = Math.max(0, targetTime);
            }} catch (err) {{}}
            var p = audio.play();
            if (p !== undefined) {{
                p.then(function() {{
                    playIcon.textContent = '⏸';
                    playLabel.textContent = 'Tạm dừng';
                }}).catch(function(e) {{
                    console.warn('Seek play error:', e);
                }});
            }}
        }};

        if (audio.readyState >= 1) {{
            doSeek();
        }} else {{
            var onMeta = function() {{
                audio.removeEventListener('loadedmetadata', onMeta);
                doSeek();
            }};
            audio.addEventListener('loadedmetadata', onMeta);
            audio.load();
        }}
    }}

    function renderJumpBar() {{
        var mData = getCurrentModeData();
        var html = '<span style="font-size: 11.5px; font-weight: 800; color: #64748b; text-transform: uppercase; margin-right: 4px;">Chuyển nhanh:</span>';
        mData.patterns.forEach(function(p) {{
            html += '<button type="button" class="pod-jump-pill" id="jump-pill-' + p.pattern_num + '" data-start="' + (p.start_time || 0) + '" title="' + p.pattern_title + '">';
            html += '  <span>💬 Hội thoại ' + p.pattern_num + '</span>';
            html += '  <span style="font-size: 11px; opacity: 0.75;">(' + fmtTime(p.start_time || 0) + ')</span>';
            html += '</button>';
        }});
        jumpBar.innerHTML = html;

        var pills = jumpBar.querySelectorAll('.pod-jump-pill');
        pills.forEach(function(pill) {{
            pill.addEventListener('click', function(e) {{
                e.preventDefault();
                var st = parseFloat(this.getAttribute('data-start'));
                if (!isNaN(st)) {{
                    seekAndPlay(st);
                }}
            }});
        }});
    }}

    function renderPlaylist() {{
        var mData = getCurrentModeData();
        var html = '';
        var idx = 1;

        mData.patterns.forEach(function(p) {{
            html += '<div style="margin-bottom: 14px;" id="pod-group-' + p.pattern_num + '">';
            html += '  <div style="font-size: 13px; font-weight: 800; color: #0f172a; padding: 8px 14px; background: #e2e8f0; border-radius: 8px; margin-bottom: 8px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 6px;">';
            html += '    <span>💬 Hội thoại ' + p.pattern_num + ': ' + p.pattern_title + '</span>';
            if (p.pattern_translation) {{
                html += '    <span style="font-size: 11.5px; color: #475569; font-weight: 600;">' + p.pattern_translation + ' • ' + fmtTime(p.start_time || 0) + '</span>';
            }}
            html += '  </div>';

            p.sentences.forEach(function(s) {{
                var rowId = 'pod-row-' + currentMode + '-' + s.audio_key;
                var roleClass = s.role === 'B' ? 'role-B' : 'role-A';
                var speakerPrefix = s.speaker ? ('<span class="speaker-chip ' + roleClass + '">' + s.speaker + '</span>') : '';
                html += '  <div id="' + rowId + '" class="pod-row" data-start="' + s.start_time + '" style="cursor: pointer;">';
                html += '    <div style="display: flex; align-items: flex-start; gap: 10px; flex: 1; padding-right: 10px;">';
                html += '      <span style="font-size: 11px; font-weight: 700; color: #94a3b8; min-width: 24px; padding-top: 3px;">#' + idx + '</span>';
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
            npPatternTag.textContent = 'CHỦ ĐỀ: ' + bundle.cleanTitle.toUpperCase() + ' (' + bundle.totalDialogues + ' HỘI THOẠI)';
            npTurnBadge.style.background = '#e0e7ff';
            npTurnBadge.style.color = '#4338ca';
            npTurnBadge.textContent = '🇻🇳 Sẵn sàng luyện tập';
            npPrimaryText.textContent = 'Nhấn "Bắt đầu nghe" bên dưới để khởi động phản xạ dịch ' + bundle.totalDialogues + ' đoạn hội thoại...';
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
            npPatternTag.textContent = 'CHỦ ĐỀ: ' + bundle.cleanTitle.toUpperCase() + ' (' + bundle.totalDialogues + ' HỘI THOẠI)';
            npTurnBadge.style.background = '#e0f2fe';
            npTurnBadge.style.color = '#0369a1';
            npTurnBadge.textContent = '🎧 Máy đọc mẫu';
            npPrimaryText.textContent = 'Nhấn "Bắt đầu nghe" để luyện nghe và đọc nhại theo ' + bundle.totalDialogues + ' đoạn hội thoại...';
            npSecondaryText.textContent = '(Nhấn nút phát để bắt đầu nghe toàn bộ ' + bundle.totalSentences + ' lượt hội thoại hoặc chọn nhanh từng hội thoại ở trên)';
            playBtn.className = 'pod-btn-play shadowing';
        }}

        renderJumpBar();
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

        if (!activeSentence || !activePattern) return;

        // Highlight active dialogue pill
        var pills = jumpBar.querySelectorAll('.pod-jump-pill');
        pills.forEach(function(pill) {{
            pill.classList.remove('active-dialogue', 'reflex-pill');
        }});
        var curPill = document.getElementById('jump-pill-' + activePattern.pattern_num);
        if (curPill) {{
            curPill.classList.add('active-dialogue');
            if (currentMode === 'reflex') curPill.classList.add('reflex-pill');
        }}

        var spkTag = activeSentence.speaker ? (' • 👤 ' + activeSentence.speaker.toUpperCase()) : '';
        npPatternTag.textContent = 'HỘI THOẠI ' + activePattern.pattern_num + '/' + bundle.totalDialogues + ': ' + activePattern.pattern_title.toUpperCase() + ' • CÂU #' + (activeSentence.turn_num || 1) + '/' + activePattern.sentences.length + spkTag;

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

    applyModeUI('shadowing');
}})();
</script>
"""
    return html


def clean_and_append_page1_cta(lec_order, orig_p1_html, orig_p2_html, clean_title, total_dialogues):
    html = orig_p1_html

    # 1. If Lecture 1 and Introducing People (orig_p2_html) hasn't been merged into Page 1 yet, merge it cleanly!
    merge_marker = "<!-- MERGED_INTRODUCING_PEOPLE_SLIDES -->"
    if lec_order == 1 and orig_p2_html and "Introducing People" in orig_p2_html and merge_marker not in html:
        soup2 = BeautifulSoup(orig_p2_html, 'html.parser')
        slides2 = soup2.find_all('div', class_='slide')
        if slides2:
            slides_html = "\n".join(str(s) for s in slides2)
            html = html.rstrip() + f"\n{merge_marker}\n{slides_html}\n"

    # 2. Minor cleanups on Page 1 for Lec 5, 8, 10
    if lec_order == 5:
        html = html.replace('data-sentence="B: &quot;That\'s an understatement.&quot; (Nói thế còn nhẹ đấy)"', 'data-sentence="That\'s an understatement."')
        html = html.replace('data-sentence=\'B: "That\\\'s an understatement." (Nói thế còn nhẹ đấy)\'', 'data-sentence="That\'s an understatement."')
        html = html.replace('data-sentence="B: &quot;I\'m glad I\'m not in your shoes.&quot; (Thật may là tôi không ở trong hoàn cảnh của bạn)"', 'data-sentence="I\'m glad I\'m not in your shoes."')
    elif lec_order == 8:
        soup8 = BeautifulSoup(html, 'html.parser')
        dup_row = soup8.find('div', attrs={'data-audio-key': 'c13_l8p1_d3_t7_a'})
        if dup_row:
            dup_row.decompose()
            html = str(soup8)
    elif lec_order == 10:
        html = html.replace('data-sentence="B: &quot;What are we going to order?&quot; (Chuyển chủ đề khi đi ăn sau rạp!)"', 'data-sentence="What are we going to order?"')
        html = html.replace('"B: "What are we going to order?" (Chuyển chủ đề khi đi ăn sau rạp!)"', '"What are we going to order?" (Chuyển chủ đề khi đi ăn sau rạp!)')

    # 3. Append CTA button to Page 2 Podcast
    cta_marker = "<!-- CTA_TO_PAGE_2_PODCAST -->"
    if cta_marker in html:
        return html

    cta_html = f"""
{cta_marker}
<div style="width: 100%; max-width: 900px; margin: 24px auto 8px auto; padding: 18px 22px; border-radius: 14px; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1.5px dashed #38bdf8; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; font-family: Arial, sans-serif; box-sizing: border-box;">
    <div style="display: flex; align-items: center; gap: 12px;">
        <span style="font-size: 28px;">🎧</span>
        <div>
            <div style="font-size: 15px; font-weight: bold; color: #0369a1;">Đã nắm vững {total_dialogues} đoạn hội thoại trong bài "{clean_title}"?</div>
            <div style="font-size: 13px; color: #0284c7; margin-top: 2px;">Chuyển sang <strong>Trang 2</strong> để luyện <strong>Podcast Đọc nhại Shadowing &amp; Phản xạ dịch Việt - Anh</strong> nhé!</div>
        </div>
    </div>
    <button type="button" onclick="window.parent.postMessage({{ type: 'LECTURE_SWITCH_PAGE', page: 2 }}, '*')" style="border: none; border-radius: 25px; padding: 11px 22px; font-size: 14px; font-weight: bold; color: #ffffff; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); cursor: pointer; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);">
        <span>🎧 Sang Trang 2: Luyện Podcast Shadowing &amp; Phản Xạ</span>
        <span>➔</span>
    </button>
</div>
"""
    return html.rstrip() + "\n" + cta_html


def main():
    print("=== Step 1: Uploading 3 Fixed EN Sentence MP3s to Supabase Storage ===")
    for ak in ['c13_l5p1_d2_t4_b', 'c13_l5p1_d3_t6_b', 'c13_l10p1_d4_t14_b']:
        local_en = os.path.join(EN_AUDIO_DIR, f"{ak}.mp3")
        if os.path.exists(local_en):
            upload_file_to_supabase(local_en, f"{STORAGE_SENTENCE_PREFIX}/{ak}.mp3")

    print("\n=== Step 2: Uploading 24 Module 13 Podcast MP3 files to Supabase Storage ===")
    for lec in mod13_data:
        slug = lec['slug']
        for fn in [f"podcast_shadowing_{slug}.mp3", f"podcast_reflex_vi_en_{slug}.mp3"]:
            local_p = os.path.join(PODCAST_DIR, fn)
            if not os.path.exists(local_p):
                raise FileNotFoundError(f"Missing MP3: {local_p}")
            ok = upload_file_to_supabase(local_p, f"{STORAGE_PODCAST_PREFIX}/{fn}")
            if not ok:
                print(f"ERROR uploading {fn}")
                sys.exit(1)

    print("\n=== Step 3: Updating Page 1 & Inserting/Updating Page 2 in Supabase DB ===")
    for lec in mod13_data:
        lec_id = lec['lecture_id']
        lec_order = lec['lecture_order']
        slug = lec['slug']
        clean_title = lec['clean_title']
        total_dialogues = lec['dialogues_count']

        p_rows = supabase.table('lecture_pages').select('id, page_number, content_html').eq('lecture_id', lec_id).order('page_number').execute().data
        p1_row = next((r for r in p_rows if r['page_number'] == 1), None)
        p2_row = next((r for r in p_rows if r['page_number'] == 2), None)

        if p1_row:
            orig_p2_html = p2_row['content_html'] if p2_row else ""
            new_p1_html = clean_and_append_page1_cta(lec_order, p1_row['content_html'], orig_p2_html, clean_title, total_dialogues)
            if new_p1_html != p1_row['content_html']:
                supabase.table('lecture_pages').update({'content_html': new_p1_html}).eq('id', p1_row['id']).execute()
                print(f"  [Updated Page 1] [{slug}] {lec['lecture_title']} ({len(new_p1_html)} chars)")

        page2_html = generate_mod13_page2_html(lec)
        if p2_row:
            p2_id = p2_row['id']
            supabase.table('lecture_pages').update({'content_html': page2_html}).eq('id', p2_id).execute()
            print(f"  [Updated Page 2] [{slug}] {lec['lecture_title']} (page_id={p2_id}, {len(page2_html)} chars)")
        else:
            p2_id = str(uuid.uuid4())
            supabase.table('lecture_pages').insert({
                'id': p2_id,
                'lecture_id': lec_id,
                'page_number': 2,
                'content_html': page2_html
            }).execute()
            print(f"  [Inserted Page 2] [{slug}] {lec['lecture_title']} (page_id={p2_id}, {len(page2_html)} chars)")

    print("\n🎉 ALL 12 MODULE 13 LECTURES UPDATED WITH PAGE 2 SHADOWING & REFLEX PODCASTS!")


if __name__ == '__main__':
    main()
