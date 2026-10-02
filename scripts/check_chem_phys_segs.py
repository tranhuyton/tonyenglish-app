import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

all_codes = [f"c{i}" for i in range(1, 13)] + [f"p{i}" for i in range(1, 7)]

for code in all_codes:
    mpath = f"public/audio/lectures/science/{code}/manifest.json"
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    segs = m.get('segments', [])
    non_sec = [s for s in segs if not s.get('id', '').startswith('sec_') and s.get('id') != 'intro']
    if non_sec:
        print(f"⚠️ {code}: non-sec segments: {[s['id'] for s in non_sec]}")

print("Done checking all 18 manifests for non-sec segments. If nothing printed above, all segments are intro or sec_...!")
