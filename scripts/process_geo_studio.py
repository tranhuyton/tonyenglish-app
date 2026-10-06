import os
import sys
import time
import shutil
import json
import re
import subprocess

VIDEO_DIR = r"F:\Downloads\Chrome\IGCSE Geography-studio-2026-10-04_20-38\Videos"
BACKUP_DIR = os.path.join(VIDEO_DIR, "_Originals_Backup")
BADGE_PATH = r"C:\Users\Tony\.gemini\antigravity\brain\31c3a595-fccd-414d-b4a6-fa3caa9a13d7\badge_1080p.png"
TEMP_DIR = r"F:\temp_encode_geo_studio"

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

def sort_key(name):
    m = re.match(r'^(\d+)\.(\d+)', name)
    if m:
        return (int(m.group(1)), int(m.group(2)), name)
    return (999, 999, name)

def main():
    print("=" * 65)
    print("STARTING IGCSE GEOGRAPHY STUDIO VIDEO PROCESSING (35 VIDEOS)")
    print("=" * 65)
    
    all_files = [f for f in os.listdir(VIDEO_DIR) if f.endswith('.mp4') and not f.startswith('.')]
    target_files = sorted(all_files, key=sort_key)
    print(f"Found {len(target_files)} videos to process.")

    total_start = time.time()
    processed_count = 0

    for idx, filename in enumerate(target_files, 1):
        main_path = os.path.join(VIDEO_DIR, filename)
        backup_path = os.path.join(BACKUP_DIR, filename)
        
        # Check if already processed
        dur, size, w, h = get_file_info(main_path)
        if w == 1920 and h == 1080 and os.path.exists(backup_path):
            print(f"[{idx}/{len(target_files)}] Skipping already completed 1080p: {filename}")
            continue

        print(f"\n[{idx}/{len(target_files)}] Processing: {filename}")
        
        # 1. Ensure backup exists
        if not os.path.exists(backup_path):
            print(f"  Backing up original to _Originals_Backup...")
            shutil.copy2(main_path, backup_path)
        else:
            print(f"  Backup already exists in _Originals_Backup.")
            
        source_path = backup_path
            
        dur, size, w, h = get_file_info(source_path)
        
        # Outro begins at dur - 3.15s or dur - 3.00s. Voice finishes around dur - 3.65s.
        # Trimming 3.30s preserves 100% voice and removes 100% outro.
        trim_sec = 3.30
        target_dur = dur - trim_sec
        print(f"  Source: {w}x{h}, {dur:.2f}s, {size / (1024*1024):.1f} MB")
        print(f"  Trimming {trim_sec}s -> Target duration: {target_dur:.2f}s")
        
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
            print(f"  FAILED to encode with AMF! Error: {res.stderr[-500:]}")
            print("  Falling back to libx264...")
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
                print(f"  Fallback also failed! Error: {res_fb.stderr[-500:]}")
                sys.exit(1)
                
        # Verify output
        out_dur, out_size, out_w, out_h = get_file_info(temp_out)
        print(f"  Rendered in {t_enc:.1f}s | Output: {out_w}x{out_h}, {out_dur:.2f}s, {out_size / (1024*1024):.1f} MB")
        
        if out_size < 10 * 1024 * 1024:
            print(f"  ERROR: Output file size too small ({out_size} bytes)!")
            sys.exit(1)
            
        if abs(out_dur - target_dur) > 0.5:
            print(f"  WARNING: Output duration {out_dur:.2f}s differs from target {target_dur:.2f}s by >0.5s")
            
        # Overwrite in main folder
        shutil.move(temp_out, main_path)
        print(f"  SUCCESS: Updated '{filename}' in Videos folder.")
        processed_count += 1

    total_time = time.time() - total_start
    print("=" * 65)
    print(f"ALL {processed_count} VIDEOS PROCESSED SUCCESSFULLY IN {total_time/60:.1f} MINUTES!")
    print("=" * 65)
    
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
        print("Cleaned up temp directory.")

if __name__ == "__main__":
    main()
