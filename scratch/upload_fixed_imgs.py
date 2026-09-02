import requests
import os

SUPABASE_URL = "https://ubkvzgwespfvrlpjuxkp.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVia3Z6Z3dlc3BmdnJscGp1eGtwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcxMTYzNTEsImV4cCI6MjA5MjY5MjM1MX0.ZEgXs3LfI9diL9aji56N9HIxPOl0e1sMeRxbMfSM2qw"
BASE = r"c:\Users\Tony\.gemini\antigravity\scratch\tonyenglish-app\scratch\img_check"

# All 21 images go to geography/tasks/
files_to_upload = [
    "1_2_fig118.png",
    "1_2_fig121.png",
    "1_2_fig125.png",
    "1_2_fig128.png",
    "1_2_fig129.png",
    "1_2_fig132.png",
    "1_3_fig134.png",
    "1_3_fig135.png",
    "1_3_fig136.png",
    "1_3_fig138.png",
    "1_3_fig140.png",
    "2_1_fig22.png",
    "2_1_fig23.png",
    "2_1_fig26.png",
    "2_2_fig29.png",
    "2_2_fig210.png",
    "2_2_fig211.png",
    "2_2_fig212.png",
    "2_2_fig221.png",
    "2_2_fig225.png",
    "2_3_fig229.png",
]

success = 0
fail = 0
for fname in files_to_upload:
    src = os.path.join(BASE, "fixed_" + fname)
    if not os.path.exists(src):
        print(f"MISSING: {src}")
        fail += 1
        continue
    with open(src, "rb") as f:
        data = f.read()
    url = f"{SUPABASE_URL}/storage/v1/object/documents/geography/tasks/{fname}"
    r = requests.put(url, data=data, headers={
        "apikey": KEY,
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "image/png",
        "x-upsert": "true"
    })
    status = "OK" if r.status_code in (200, 201) else "FAIL"
    print(f"{status} {fname}: HTTP {r.status_code}")
    if r.status_code in (200, 201):
        success += 1
    else:
        print(f"   Response: {r.text[:200]}")
        fail += 1

print(f"\nDone: {success} uploaded, {fail} failed")
