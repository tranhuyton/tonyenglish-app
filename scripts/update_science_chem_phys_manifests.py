import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

all_codes = [f"c{i}" for i in range(1, 13)] + [f"p{i}" for i in range(1, 7)]

print("=== UPDATING MAJORSECTIONS IN MANIFESTS C1-C12 & P1-P6 ===")

for code in all_codes:
    mpath = f"public/audio/lectures/science/{code}/manifest.json"
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
        
    segs = m.get('segments', [])
    new_ms = {}
    
    # 1. intro
    new_ms["intro"] = {"start": 0, "end": 0}
    new_ms["sec-header"] = {"start": 0, "end": 0}
    
    # 2. Each section
    for idx, s in enumerate(segs):
        sid = s['id']
        if sid == 'intro':
            continue
        new_ms[sid] = {"start": idx, "end": idx}
        dom_id = sid.replace('_', '-')
        new_ms[dom_id] = {"start": idx, "end": idx}
        
    m['majorSections'] = new_ms
    
    with open(mpath, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
        
    print(f"Updated {code.upper():4}: {len(new_ms)} keys in majorSections dictionary")

print("\n🎉 ALL 18 MANIFESTS (CHEM & PHYS) SUCCESSFULLY UPDATED TO DICTIONARIES!")
