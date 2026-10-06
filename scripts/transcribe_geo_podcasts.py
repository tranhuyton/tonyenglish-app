import whisper
import os
import subprocess
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

print("Loading Whisper model (base)...")
model = whisper.load_model("base")

base_dir = r"F:\Downloads\Chrome\Geo Podcast\Final"
en_dir = os.path.join(base_dir, "English podcast", "Audio")
vi_dir = os.path.join(base_dir, "Vietnamese podcast")

en_files = sorted(os.listdir(en_dir))
vi_files = sorted(os.listdir(vi_dir))

temp_wav = "scripts/temp_geo.wav"

results = {"en": {}, "vi": {}}

print("\n--- Transcribing English files ---")
for f in en_files:
    if not f.endswith(".mp3"): continue
    p = os.path.join(en_dir, f)
    cmd = f'ffmpeg -ss 0 -t 35 -i "{p}" -ar 16000 -ac 1 -c:a pcm_s16le -y "{temp_wav}" -loglevel error'
    subprocess.run(cmd, shell=True, check=True)
    res = model.transcribe(temp_wav, language="en")
    txt = res.get("text", "").strip()
    results["en"][f] = txt
    print(f"[EN] {f}: {txt[:120]}...")

print("\n--- Transcribing Vietnamese files ---")
for f in vi_files:
    if not f.endswith(".mp3"): continue
    p = os.path.join(vi_dir, f)
    cmd = f'ffmpeg -ss 0 -t 35 -i "{p}" -ar 16000 -ac 1 -c:a pcm_s16le -y "{temp_wav}" -loglevel error'
    subprocess.run(cmd, shell=True, check=True)
    res = model.transcribe(temp_wav, language="vi")
    txt = res.get("text", "").strip()
    results["vi"][f] = txt
    print(f"[VI] {f}: {txt[:120]}...")

if os.path.exists(temp_wav):
    os.remove(temp_wav)

with open("scripts/geo_transcriptions.json", "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print("\nSaved transcriptions to scripts/geo_transcriptions.json")
