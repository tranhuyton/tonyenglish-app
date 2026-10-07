import whisper
import os
import subprocess
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

print("Loading Whisper model (tiny)...")
model = whisper.load_model("tiny")

base_dir = r"F:\Downloads\Chrome\IELTS Premium-studio"
folders = ["Writing Task 1", "Writing Task 2", "Reading", "Listening", "Speaking Part 2"]

temp_wav = "scripts/temp_ielts.wav"
results = {}

for folder in folders:
    p_folder = os.path.join(base_dir, folder)
    if not os.path.exists(p_folder): continue
    results[folder] = {}
    print(f"\n--- Transcribing {folder} ---")
    files = sorted([f for f in os.listdir(p_folder) if f.endswith(".mp3")])
    for f in files:
        p = os.path.join(p_folder, f)
        cmd = f'ffmpeg -ss 10 -t 35 -i "{p}" -ar 16000 -ac 1 -c:a pcm_s16le -y "{temp_wav}" -loglevel error'
        subprocess.run(cmd, shell=True, check=True)
        res = model.transcribe(temp_wav, language="vi")
        txt = res.get("text", "").strip()
        results[folder][f] = txt
        print(f"[{folder}] {f} -> {txt[:100]}...", flush=True)

if os.path.exists(temp_wav):
    os.remove(temp_wav)

with open("scripts/ielts_transcriptions.json", "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("\nSaved transcriptions to scripts/ielts_transcriptions.json")
