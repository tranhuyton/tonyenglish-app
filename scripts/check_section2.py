import whisper
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
model = whisper.load_model('tiny')
base_dir = r"F:\Downloads\Chrome\Economics podcast\Final\Vietnamese"

files_vi = [
    '12-Tín hiệu giá và độ co giãn.mp3',
    '24-Cơ chế giá chi phối thị trường.mp3',
    '26-Nền kinh tế không cần bếp trưởng.mp3'
]

temp_wav = 'scripts/temp_check2.wav'

for f in files_vi:
    p = os.path.join(base_dir, f)
    cmd = f'ffmpeg -ss 90 -t 60 -i "{p}" -ar 16000 -ac 1 -c:a pcm_s16le -y "{temp_wav}" -loglevel error'
    subprocess.run(cmd, shell=True, check=True)
    txt = model.transcribe(temp_wav, language='vi')['text'].strip()
    print(f"[{f}]:\n  {txt}\n", flush=True)

if os.path.exists(temp_wav):
    os.remove(temp_wav)
