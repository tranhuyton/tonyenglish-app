import os
import sys
import time
import shutil
import json
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

VIDEO_DIR = r"C:\Users\Tony\Desktop\IELTS Premium-studio-2026-10-07_17-33\Videos"
BACKUP_DIR = os.path.join(VIDEO_DIR, "_Originals_Backup")
BADGE_PATH = r"C:\Users\Tony\.gemini\antigravity\brain\31c3a595-fccd-414d-b4a6-fa3caa9a13d7\badge_1080p.png"
TEMP_DIR = r"F:\temp_encode_ielts_studio"

os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

def get_file_info(path):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size:stream=width,height', '-of', 'json', path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    dur = float(data['format']['duration'])
    size = int(data['format']['size'])
    streams = data.get('streams', [{}])[0]
    w = streams.get('width', 0)
    h = streams.get('height', 0)
    return dur, size, w, h

def main():
    print("=" * 70, flush=True)
    print("STARTING IELTS PREMIUM STUDIO VIDEO PROCESSING (5 VIDEOS)", flush=True)
    print("=" * 70, flush=True)
    
    all_files = [f for f in sorted(os.listdir(VIDEO_DIR)) if f.endswith('.mp4') and not f.startswith('.')]
    print(f"Found {len(all_files)} videos to process.", flush=True)

    total_start = time.time()
    processed_count = 0

    for idx, filename in enumerate(all_files, 1):
        main_path = os.path.join(VIDEO_DIR, filename)
        backup_path = os.path.join(BACKUP_DIR, filename)
        
        # Check if already processed
        dur, size, w, h = get_file_info(main_path)
        if w == 1920 and h == 1080 and os.path.exists(backup_path):
            print(f"[{idx}/{len(all_files)}] Skipping already completed 1080p: {filename}", flush=True)
            processed_count += 1
            continue

        print(f"\n[{idx}/{len(all_files)}] Processing: {filename}", flush=True)
        
        # 1. Ensure backup exists
        if not os.path.exists(backup_path):
            print(f"  Backing up original to _Originals_Backup...", flush=True)
            shutil.copy2(main_path, backup_path)
        else:
            print(f"  Backup already exists in _Originals_Backup.", flush=True)
            
        source_path = backup_path
            
        dur, size, w, h = get_file_info(source_path)
        
        # Outro begins at dur - 3.15s ~ dur - 3.00s. Voice finishes around dur - 3.65s ~ 3.75s.
        # Trimming 3.30s preserves 100% voice and removes 100% outro.
        trim_sec = 3.30
        target_dur = dur - trim_sec
        print(f"  Source: {w}x{h}, {dur:.2f}s, {size / (1024*1024):.1f} MB", flush=True)
        print(f"  Trimming {trim_sec}s -> Target duration: {target_dur:.2f}s", flush=True)
        
        temp_out = os.path.join(TEMP_DIR, f"temp_{idx}.mp4")
        if os.path.exists(temp_out):
            os.remove(temp_out)
            
        cmd = [
            'ffmpeg', '-y',
            '-i', source_path,
            '-i', BADGE_PATH,
            '-t', str(round(target_dur, 2)),
            '-filter_complex', '[0:v]scale=1920:1080:flags=lanczos[bg];[bg][1:v]overlay=1618:1022[outv]',
            '-map', '[outv]',
            '-map', '0:a',
            '-c:v', 'h264_amf',
            '-b:v', '6M',
            '-c:a', 'aac',
            '-b:a', '192k',
            temp_out
        ]
        
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True)
        t_enc = time.time() - t0
        
        if res.returncode != 0:
            print(f"  FAILED to encode with AMF! Error: {res.stderr[-500:]}", flush=True)
            print("  Falling back to libx264...", flush=True)
            cmd_fallback = [
                'ffmpeg', '-y',
                '-i', source_path,
                '-i', BADGE_PATH,
                '-t', str(round(target_dur, 2)),
                '-filter_complex', '[0:v]scale=1920:1080:flags=lanczos[bg];[bg][1:v]overlay=1618:1022[outv]',
                '-map', '[outv]',
                '-map', '0:a',
                '-c:v', 'libx264',
                '-preset', 'fast',
                '-crf', '18',
                '-c:a', 'aac',
                '-b:a', '192k',
                temp_out
            ]
            res_fb = subprocess.run(cmd_fallback, capture_output=True, text=True)
            if res_fb.returncode != 0:
                print(f"  Fallback also failed! Error: {res_fb.stderr[-500:]}", flush=True)
                sys.exit(1)
                
        # Verify output
        out_dur, out_size, out_w, out_h = get_file_info(temp_out)
        print(f"  Rendered in {t_enc:.1f}s | Output: {out_w}x{out_h}, {out_dur:.2f}s, {out_size / (1024*1024):.1f} MB", flush=True)
        
        if out_size < 10 * 1024 * 1024:
            print(f"  ERROR: Output file size too small ({out_size} bytes)!", flush=True)
            sys.exit(1)
            
        if abs(out_dur - target_dur) > 0.5:
            print(f"  WARNING: Output duration {out_dur:.2f}s differs from target {target_dur:.2f}s by >0.5s", flush=True)
            
        # Overwrite in main folder
        shutil.move(temp_out, main_path)
        print(f"  SUCCESS: Updated '{filename}' in Videos folder.", flush=True)
        processed_count += 1

    total_time = time.time() - total_start
    print("=" * 70, flush=True)
    print(f"ALL {processed_count} VIDEOS PROCESSED SUCCESSFULLY IN {total_time:.1f} SECONDS ({total_time/60:.1f} MINUTES)!", flush=True)
    print("=" * 70, flush=True)
    
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
        print("Cleaned up temp directory.", flush=True)

if __name__ == "__main__":
    main()
