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

# Environment & Supabase
with open(os.path.join(os.path.dirname(__file__), '..', '.env'), 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

EN_VOICE = 'en-GB-RyanNeural'       # Authentic British English Male
VI_VOICE = 'vi-VN-HoaiMyNeural'     # Authentic Hanoi Northern Vietnamese Female

async def _gen_tts(text: str, voice: str, out_file: str, max_retries: int = 5):
    for attempt in range(1, max_retries + 1):
        try:
            if os.path.exists(out_file):
                try:
                    os.remove(out_file)
                except Exception:
                    pass
            communicate = edge_tts.Communicate(text, voice)
            await asyncio.wait_for(communicate.save(out_file), timeout=45.0)
            await asyncio.sleep(0.3)
            if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
                return
            raise Exception(f"TTS output file {out_file} missing or too small ({os.path.getsize(out_file) if os.path.exists(out_file) else 0} B)")
        except Exception as e:
            if attempt == max_retries:
                print(f"  [ERROR] Failed TTS after {max_retries} attempts: {e}")
                raise e
            wait = attempt * 2.0
            print(f"  [RETRY] TTS attempt {attempt} failed ({e}), retrying in {wait}s...")
            await asyncio.sleep(wait)


def get_audio_duration(file_path: str) -> float:
    cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return round(float(res.stdout.strip()), 2)

async def generate_segment_audio(seg, output_dir, temp_dir):
    seg_id = seg['id']
    final_mp3 = os.path.join(output_dir, f"{seg_id}.mp3")
    
    if os.path.exists(final_mp3) and os.path.getsize(final_mp3) > 1000:
        print(f"  [CACHE] Segment '{seg_id}' audio exists.")
        dur = get_audio_duration(final_mp3)
        return dur
    
    print(f"  [TTS] Generating segment '{seg_id}'...")
    en_tmp = os.path.join(temp_dir, f"{seg_id}_en.mp3")
    vi_tmp = os.path.join(temp_dir, f"{seg_id}_vi.mp3")
    
    await _gen_tts(seg['en'], EN_VOICE, en_tmp)
    await _gen_tts(seg['vi'], VI_VOICE, vi_tmp)
    
    # Concat: en + 0.4s silence + vi
    filter_cmd = [
        'ffmpeg', '-y',
        '-i', en_tmp,
        '-f', 'lavfi', '-t', '0.4', '-i', 'anullsrc=r=24000:cl=mono',
        '-i', vi_tmp,
        '-filter_complex', '[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]',
        '-map', '[out]',
        '-b:a', '128k',
        final_mp3
    ]
    subprocess.run(filter_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    
    # Clean up temp mp3 safely
    for tmp in [en_tmp, vi_tmp]:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
            
    dur = get_audio_duration(final_mp3)
    return dur

async def process_lecture_audio(lecture_code, lecture_id, course_title, lecture_title, segments, major_sections, subject='geography'):
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', subject, lecture_code)
    temp_dir = os.path.join(os.path.dirname(__file__), '..', 'scratch', f'audio_temp_{subject}_{lecture_code}')
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    
    print(f"\n=======================================================")
    print(f"Processing Lecture {subject}/{lecture_code}: {lecture_title}")
    print(f"Output directory: {output_dir}")
    print(f"Total segments: {len(segments)}")
    print(f"=======================================================")
    
    curr_time = 0.0
    for seg in segments:
        dur = await generate_segment_audio(seg, output_dir, temp_dir)
        seg['duration'] = dur
        seg['startTime'] = round(curr_time, 2)
        curr_time += dur
        seg['endTime'] = round(curr_time, 2)
        seg['audioUrl'] = f"/audio/lectures/{subject}/{lecture_code}/{seg['id']}.mp3"
    
    total_dur = round(curr_time, 2)
    
    # Build manifest
    manifest = {
        "lectureId": lecture_id,
        "courseTitle": course_title,
        "lectureTitle": lecture_title,
        "totalDuration": total_dur,
        "majorSections": major_sections,
        "segments": segments
    }
    
    manifest_path = os.path.join(output_dir, 'manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        
    print(f"Manifest written to {manifest_path} (Total Duration: {total_dur}s)")
    return manifest

def update_supabase_page(lecture_id, html_content):
    print(f"Updating Supabase page 1 for lecture {lecture_id}...")
    res = sb.table('lecture_pages').update({
        'content_html': html_content
    }).eq('lecture_id', lecture_id).eq('page_number', 1).execute()
    print(f"Updated {len(res.data)} page(s) successfully.")
