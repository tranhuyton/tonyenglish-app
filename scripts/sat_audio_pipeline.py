import os
import sys
import re
import json
import asyncio
import subprocess
import edge_tts
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
with open(os.path.join(ROOT_DIR, '.env'), 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

# Authentic American English academic male + Hanoi Northern Vietnamese female
EN_VOICE = 'en-US-AndrewNeural'
EN_FALLBACK = 'en-US-BrianNeural'
VI_VOICE = 'vi-VN-HoaiMyNeural'
VI_FALLBACK = 'vi-VN-NamMinhNeural'

IDS_PATH = os.path.join(os.path.dirname(__file__), 'sat_course_ids.json')

def load_ids():
    with open(IDS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_ids(data):
    with open(IDS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

async def _gen_tts(text: str, voice: str, out_file: str, max_retries: int = 20):
    for attempt in range(1, max_retries + 1):
        try:
            if os.path.exists(out_file):
                try:
                    os.remove(out_file)
                except Exception:
                    pass
            current_voice = voice
            if attempt >= 4:
                if voice == VI_VOICE:
                    current_voice = VI_FALLBACK if (attempt % 2 == 1) else VI_VOICE
                elif voice == EN_VOICE:
                    current_voice = EN_FALLBACK if (attempt % 2 == 1) else EN_VOICE

            communicate = edge_tts.Communicate(text, current_voice)
            await asyncio.wait_for(communicate.save(out_file), timeout=45.0)
            await asyncio.sleep(0.5)
            if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
                return
            raise Exception(f"TTS file {out_file} missing/small")
        except Exception as e:
            if attempt == max_retries:
                print(f"  [ERROR] TTS failed after {max_retries} attempts: {e}")
                raise e
            wait = attempt * 2.0 if attempt <= 4 else (12.0 if attempt <= 8 else 25.0)
            print(f"  [RETRY {attempt}] {current_voice} ({e}) -> wait {wait}s")
            await asyncio.sleep(wait)

def get_audio_duration(file_path: str) -> float:
    cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path,
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return round(float(res.stdout.strip()), 2)

async def generate_segment_audio(seg, output_dir, temp_dir):
    seg_id = seg['id']
    final_mp3 = os.path.join(output_dir, f"{seg_id}.mp3")
    if os.path.exists(final_mp3) and os.path.getsize(final_mp3) > 1000:
        return get_audio_duration(final_mp3)

    print(f"  [TTS] {seg_id}...")
    en_tmp = os.path.join(temp_dir, f"{seg_id}_en.mp3")
    vi_tmp = os.path.join(temp_dir, f"{seg_id}_vi.mp3")

    await _gen_tts(seg['en'], EN_VOICE, en_tmp)
    await asyncio.sleep(0.3)
    await _gen_tts(seg['vi'], VI_VOICE, vi_tmp)

    filter_cmd = [
        'ffmpeg', '-y',
        '-i', en_tmp,
        '-f', 'lavfi', '-t', '0.4', '-i', 'anullsrc=r=24000:cl=mono',
        '-i', vi_tmp,
        '-filter_complex', '[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]',
        '-map', '[out]',
        '-b:a', '128k',
        final_mp3,
    ]
    subprocess.run(filter_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    for tmp in (en_tmp, vi_tmp):
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
    return get_audio_duration(final_mp3)

async def generate_lecture_audio(lecture_code, lecture_id, course_title, lecture_title, segments, major_sections, subject='sat_rw'):
    output_dir = os.path.join(ROOT_DIR, 'public', 'audio', 'lectures', subject, lecture_code)
    temp_dir = os.path.join(ROOT_DIR, 'scratch', f'audio_temp_{subject}_{lecture_code}')
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    print(f"\n[AUDIO] {subject}/{lecture_code}: {lecture_title} ({len(segments)} segments)", flush=True)
    curr_time = 0.0
    for seg in segments:
        dur = await generate_segment_audio(seg, output_dir, temp_dir)
        seg['duration'] = dur
        seg['startTime'] = round(curr_time, 2)
        curr_time += dur
        seg['endTime'] = round(curr_time, 2)
        seg['audioUrl'] = f"/audio/lectures/{subject}/{lecture_code}/{seg['id']}.mp3"

    total_dur = round(curr_time, 2)
    manifest = {
        'lectureId': lecture_id,
        'courseTitle': course_title,
        'lectureTitle': lecture_title,
        'totalDuration': total_dur,
        'majorSections': major_sections,
        'segments': segments,
    }
    manifest_path = os.path.join(output_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"  [OK] manifest.json written ({total_dur}s)", flush=True)
    return f"/audio/lectures/{subject}/{lecture_code}/manifest.json"

def upsert_sat_drill(drill_key, title, order_index, content_json, folder_key='rw_drills'):
    ids = load_ids()
    course_id = ids['course_id']
    folder_id = ids['folders'][folder_key]

    content_json['basicInfo']['courseId'] = course_id
    bucket_map = {
        'rw_drills': 'drills',
        'rw_mocks': 'mocks',
        'math_drills': 'math_drills',
        'math_mocks': 'math_mocks',
        'boss_drills': 'boss_drills',
    }
    bucket = bucket_map.get(folder_key, 'drills')
    existing_id = ids.get(bucket, {}).get(drill_key)

    payload = {
        'course_id': course_id,
        'folder_id': folder_id,
        'title': title,
        'test_type': 'SAT-Bluebook',
        'content_json': content_json,
        'is_published': True,
        'order_index': order_index,
    }

    if existing_id:
        res = sb.table('tests').update(payload).eq('id', existing_id).execute().data
        if res:
            print(f"  [UPDATED TEST] {title} ({existing_id})", flush=True)
            return existing_id

    # Check by course_id + title to stay idempotent
    found = sb.table('tests').select('id').eq('course_id', course_id).eq('title', title).execute().data
    if found:
        tid = found[0]['id']
        sb.table('tests').update(payload).eq('id', tid).execute()
        print(f"  [UPDATED TEST] {title} ({tid})", flush=True)
    else:
        tid = sb.table('tests').insert(payload).execute().data[0]['id']
        print(f"  [CREATED TEST] {title} ({tid})", flush=True)

    ids.setdefault(bucket, {})[drill_key] = tid
    save_ids(ids)
    return tid

def upsert_sat_lecture(lecture_code, module_key, title, order_index, html_content, drill_id=None, drill_title=None, extra_manual_task=None, id_bucket='lectures'):
    ids = load_ids()
    course_id = ids['course_id']
    module_id = ids['modules'][module_key]

    task_list = []
    if extra_manual_task:
        task_list.append({
            'id': f'sat_task_{lecture_code}_read',
            'text': extra_manual_task,
            'type': 'manual',
        })
    else:
        task_list.append({
            'id': f'sat_task_{lecture_code}_read',
            'text': 'Nghe trọn bài giảng song ngữ & ghi chú Quy tắc vàng 1500+',
            'type': 'manual',
        })
    if drill_id and drill_title:
        task_list.append({
            'id': f'sat_task_{lecture_code}_drill',
            'text': f'Làm Bluebook Drill: {drill_title}',
            'type': 'exercise',
            'test_id': drill_id,
        })

    existing_id = ids.get(id_bucket, {}).get(lecture_code)
    payload = {
        'course_id': course_id,
        'module_id': module_id,
        'title': title,
        'order_index': order_index,
        'is_published': True,
        'task_list': task_list,
    }

    lec_id = None
    if existing_id:
        res = sb.table('lectures').update(payload).eq('id', existing_id).execute().data
        if res:
            lec_id = existing_id
            print(f"  [UPDATED LECTURE] {title} ({lec_id})", flush=True)

    if not lec_id:
        found = sb.table('lectures').select('id').eq('module_id', module_id).eq('title', title).execute().data
        if found:
            lec_id = found[0]['id']
            sb.table('lectures').update(payload).eq('id', lec_id).execute()
            print(f"  [UPDATED LECTURE] {title} ({lec_id})", flush=True)
        else:
            lec_id = sb.table('lectures').insert(payload).execute().data[0]['id']
            print(f"  [CREATED LECTURE] {title} ({lec_id})", flush=True)

    # Upsert page 1 in lecture_pages
    pages = sb.table('lecture_pages').select('id').eq('lecture_id', lec_id).eq('page_number', 1).execute().data
    if pages:
        sb.table('lecture_pages').update({'content_html': html_content}).eq('id', pages[0]['id']).execute()
    else:
        sb.table('lecture_pages').insert({
            'lecture_id': lec_id,
            'page_number': 1,
            'content_html': html_content,
        }).execute()

    ids.setdefault(id_bucket, {})[lecture_code] = lec_id
    save_ids(ids)
    return lec_id

def build_sat_lecture_html(badge_text, title, subtitle, intro_points, cards_html, quick_check_html=''):
    """Builds a flagship TonyEnglish interactive lecture HTML with clickable audio cards & self-check widget."""
    intro_bullets = ''.join(f'<li style="margin-bottom:6px;">{p}</li>' for p in intro_points)
    return f'''<div style="font-family: 'Segoe UI', Inter, Arial, sans-serif; max-width: 1000px; margin: 18px auto; padding: 0 14px; color: #1e293b; line-height: 1.7; box-sizing: border-box;">
  <style>
    .sat-badge {{ display:inline-flex; align-items:center; gap:6px; padding:4px 11px; border-radius:999px; font-size:12px; font-weight:700; }}
    .sat-listen-pill {{ position:absolute; top:16px; right:16px; display:inline-flex; align-items:center; gap:6px; padding:4px 11px; background:rgba(15,23,42,0.06); border:1px solid rgba(15,23,42,0.14); border-radius:999px; font-size:12px; font-weight:700; color:#1e3a8a; pointer-events:none; }}
    .sat-card {{ position:relative; background:#ffffff; border:1.5px solid #e2e8f0; border-radius:16px; padding:24px 26px; margin-bottom:22px; box-shadow:0 4px 18px -6px rgba(15,23,42,0.08); transition:all 0.2s ease; }}
    .sat-card:hover {{ border-color:#93c5fd; box-shadow:0 10px 26px -8px rgba(30,58,138,0.14); }}
    .sat-card h2 {{ margin:0 0 12px 0; font-size:20px; font-weight:800; color:#0f172a; padding-right:135px; line-height:1.35; }}
    .sat-table {{ width:100%; border-collapse:collapse; margin:14px 0; font-size:14px; }}
    .sat-table th {{ background:#0f172a; color:#ffffff; text-align:left; padding:10px 12px; font-weight:800; }}
    .sat-table td {{ border:1px solid #cbd5e1; padding:10px 12px; vertical-align:top; }}
    .sat-table tr:nth-child(even) td {{ background:#f8fafc; }}
    .sat-rule-box {{ background:#eff6ff; border-left:4px solid #1d4ed8; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; }}
    .sat-trap-box {{ background:#fff1f2; border-left:4px solid #e11d48; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; color:#881337; }}
    .sat-gold-box {{ background:#fefce8; border:1.5px dashed #eab308; padding:16px 18px; border-radius:12px; margin:14px 0; font-size:14.5px; color:#713f12; }}
    .sat-ex-box {{ background:#f8fafc; border:1px solid #cbd5e1; border-radius:12px; padding:15px 18px; margin:12px 0; font-family:Georgia, 'Times New Roman', serif; font-size:15px; color:#0f172a; }}
    .sat-code {{ display:inline-block; background:#e0e7ff; color:#1e3a8a; font-weight:800; padding:1px 7px; border-radius:6px; font-size:13px; font-family:'Segoe UI', sans-serif; }}
    .sat-qc-btn {{ display:block; width:100%; text-align:left; padding:10px 14px; margin:7px 0; border-radius:10px; border:1.5px solid #cbd5e1; background:#ffffff; font-size:14px; font-weight:600; color:#0f172a; cursor:pointer; transition:all 0.15s; }}
    .sat-qc-btn:hover {{ border-color:#2563eb; background:#eff6ff; }}
  </style>

  <!-- HERO HEADER CARD -->
  <div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro" style="background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #0050b3 100%); padding: 28px 32px; border-radius: 18px; color: #ffffff; margin-bottom: 24px; box-shadow: 0 12px 28px -6px rgba(30,58,138,0.32); position: relative;">
    <div style="position: absolute; top: 18px; right: 18px; display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; background: rgba(255,255,255,0.16); border: 1px solid rgba(255,255,255,0.32); border-radius: 999px; font-size: 12px; font-weight: 700; color: #ffffff; pointer-events: none;">🎧 Nghe phần này</div>
    <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.3px; color: #93c5fd; margin-bottom: 8px;">{badge_text}</div>
    <h1 style="margin: 0; font-size: 27px; font-weight: 900; color: #ffffff; letter-spacing: -0.4px; padding-right: 145px; line-height: 1.25;">{title}</h1>
    <p style="margin: 10px 0 14px 0; font-size: 15px; color: #e0f2fe; line-height: 1.55;">{subtitle}</p>
    <div style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 12px; padding: 12px 16px;">
      <div style="font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px; color: #fde047; margin-bottom: 6px;">🎯 Mục tiêu đầu ra 1500+ sau bài học này</div>
      <ul style="margin: 0; padding-left: 18px; font-size: 14px; color: #f8fafc;">
        {intro_bullets}
      </ul>
    </div>
  </div>

  {cards_html}

  {quick_check_html}
</div>'''

def make_quick_check_html(qc_id, question_prompt, passage_html, options, correct_idx, explanation_vi):
    """Creates an interactive self-check micro-quiz at the end of a lecture (won't trigger audio click)."""
    btns = []
    labels = ['A', 'B', 'C', 'D']
    for i, opt in enumerate(options):
        is_c = 'true' if i == correct_idx else 'false'
        btns.append(
            f'<button type="button" class="sat-qc-btn" onclick="(function(b){{'
            f'var box=document.getElementById(\'{qc_id}_fb\');'
            f'var all=b.parentElement.querySelectorAll(\'button\');'
            f'all.forEach(function(x){{x.style.borderColor=\'#cbd5e1\';x.style.background=\'#fff\';}});'
            f'if({is_c}){{b.style.borderColor=\'#16a34a\';b.style.background=\'#dcfce7\';box.style.background=\'#ecfdf5\';box.style.borderColor=\'#16a34a\';box.innerHTML=\'<b>✅ Chính xác ({labels[correct_idx]})!</b> {explanation_vi}\';}}'
            f'else{{b.style.borderColor=\'#e11d48\';b.style.background=\'#ffe4e6\';box.style.background=\'#fff1f2\';box.style.borderColor=\'#e11d48\';box.innerHTML=\'<b>❌ Chưa đúng — Đáp án đúng là {labels[correct_idx]}:</b> {explanation_vi}\';}}'
            f'box.style.display=\'block\';'
            f'}})(this)"><b>{labels[i]}.</b> {opt}</button>'
        )
    return f'''
  <div id="sec-quickcheck" onclick="event.stopPropagation()" style="background:linear-gradient(145deg,#0f172a 0%,#172554 100%); border-radius:18px; padding:24px 26px; margin-top:24px; color:#f8fafc; box-shadow:0 10px 25px rgba(15,23,42,0.22);">
    <div style="font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:1.1px; color:#38bdf8; margin-bottom:6px;">⚡ 1500+ Instant Trap Check (Kiểm tra phản xạ tại chỗ)</div>
    <div style="background:rgba(255,255,255,0.97); color:#0f172a; border-radius:12px; padding:16px 18px; margin:12px 0; font-family:Georgia, serif; font-size:15px; line-height:1.75;">
      {passage_html}
    </div>
    <div style="font-size:15px; font-weight:700; color:#e2e8f0; margin-bottom:10px;">{question_prompt}</div>
    <div>{''.join(btns)}</div>
    <div id="{qc_id}_fb" style="display:none; margin-top:12px; padding:12px 15px; border-radius:10px; border-left:4px solid #16a34a; color:#0f172a; font-size:14px; line-height:1.6;"></div>
  </div>
'''
