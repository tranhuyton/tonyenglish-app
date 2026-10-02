import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

for code in ['c1', 'c2', 'c6', 'p1', 'p2', 'p3']:
    mpath = f"public/audio/lectures/science/{code}/manifest.json"
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    print(f"\n==============================")
    print(f"MANIFEST {code.upper()}: {m.get('lectureTitle')}")
    print("majorSections:", json.dumps(m.get('majorSections'), ensure_ascii=False, indent=2))
    print("segments:")
    for s in m.get('segments', []):
        print(f"  {s['id']:25} | {s.get('selector'):25} | {s.get('title')}")
